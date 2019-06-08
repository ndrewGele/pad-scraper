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
        sections = sel.xpath("//div[@id='content']/table//td[@class='section']").getall()
        section_names = sel.xpath("//div[@id='content']/table//h2/text()").getall()
        print(section_names)



        # Get Awakenings and S.Awakenings if they exist
        nums = sel.xpath("//td[@class='awokenindex']//a/@href").getall()
        descs = sel.xpath("//td[@class='awokenindex']//img/@title").getall()



        # Return this nice json
        yield {
            'DUNGEON_NUM': response.url[46:],
            'DUNGEON_NAME': 'monster come get u',
            'DUNGEON_TYPE': 'tech/special/normal',
            'SUB_DUNGEON': 'big monster - mythical',
            'FLOORS': ['nested', 'list', 'of', 'encounters'],
            'READ_DATE': datetime.now()
        }