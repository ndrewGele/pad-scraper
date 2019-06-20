from scrapy import Spider
from scrapy import Selector
from re import sub
from datetime import datetime

# Gonna use this to clean up skill text later.
def clean_sentence (x):
    x = sub('(?<=\w) (?=[A-Z])', '. ', x)
    x = sub(' \.\.', '.', x)

# Following Scrapy Tutorial Mostly
class DungeonSpider(Spider):

    name = 'dungeon'

    def __init__(self, start = '1', end = '5', **kwargs):

        super().__init__(**kwargs)

        self.start_urls = [
            'http://www.puzzledragonx.com/en/mission.asp?m='
            + str(i) for i in range(int(start), int(end)+1)
        ]

    def parse(self, response):
        sel = Selector(response)



        # Basic Dungeon Info
        sections = sel.xpath("//div[@id='content']/table//td[@class='section']")



        # Create Nested List of Floors
        floors = []
        for floor in sel.xpath("//tr[td[@class='enemy']]"):
            
            # Get Monster Skills
            skills = []
            for skill in floor.xpath(".//span[@class='skillexpand']"):

                skills.append({
                    'SKILL_NAME': skill.xpath("./a/text()").get(),
                    'SKILL_TEXT': ' '.join(skill.xpath("./div[contains(@id, 'info')]//text()").getall()),
                    'SKILL_TYPES': [sub(r'\D', '', num) for num in skill.xpath("./a[1]//img[contains(@class, 'abilitytype')]/@data-original").getall()]
                })

            floors.append({
                'FLOOR': floor.xpath("./td[1]/text()").get(),
                'MONSTER': sub(r'[^0-9]', '', floor.xpath("./td[2]/a/@href").get()),
                'TYPES': [sub(r'img/type/|.png' , '', type) for type in floor.xpath("./td[3]/div//img/@data-original").getall()],
                'TURN': floor.xpath("./td[4]/text()").get(),
                'DEFENSE': floor.xpath("./td[6]/span/text()").get(),
                'HP': sub(r',', '', floor.xpath("./td[7]/span/text()").get()),
                'SKILLS': skills
            })



        # Return this nice json
        yield {
            'DUNGEON_NUM': response.url[46:],
            'DUNGEON_NAME': sub(r'\W+', ' ', sections[1].xpath("table//tr[2]/td/text()").get()).strip(),
            'DUNGEON_TYPE': sub(r'\W+', ' ', sections[1].xpath("table//tr[4]/td/text()").get()).strip(),
            'SUB_DUNGEON': sections[0].xpath("table//tr[2]//td[2]/text()").get(),
            'STAMINA': sections[0].xpath("table//tr[4]//td[2]/span/text()").get(),
            'FLOORS': floors,
            'READ_DATE': datetime.now()
        }