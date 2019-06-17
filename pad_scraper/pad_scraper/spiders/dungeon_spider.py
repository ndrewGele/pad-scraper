from scrapy import Spider
from scrapy import Selector
from re import sub
from datetime import datetime


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
        sections[0].xpath("table//tr[2]//td[2]/text()").get()  #table/tbody/tr[1]/td/text()


        # Create Nested List of Floors
        floors = []
        for floor in sel.xpath("//tr[td[@class='enemy']]"):
            
            
            skills = []
            for skill in floor.xpath("FILLTHISIN"):
                skills.append({
                    'SKILL_NAME': skill.xpath(""),
                    'SKILL_TEXT': skill.xpath("") 
                })

            floors.append({
                'FLOOR': floor.xpath("td[1]/text()"),
                'MONSTER': 'mon',
                'TYPES': 'types',
                'TURN': 'trn',
                'DEFENSE': 'def',
                'HP': 'hp',
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