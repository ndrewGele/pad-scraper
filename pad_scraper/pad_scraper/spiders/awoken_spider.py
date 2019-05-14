from scrapy import Spider
from scrapy import Selector
from re import sub
from datetime import datetime


# Following Scrapy Tutorial Mostly
class AwokenSpider(Spider):

    name = 'awoken'

    def __init__(self):

        self.start_urls = [
            'http://www.puzzledragonx.com/en/awokenskill-list.asp'
        ]

    def parse(self, response):
        sel = Selector(response)
        
        

        # Get Awakenings and S.Awakenings if they exist
        nums = sel.xpath("//td[@class='awokenindex']//a/@href").getall()
        descs = sel.xpath("//td[@class='awokenindex']//img/@title").getall()



        # Return this nice json

        for i in range(len(nums)):
            yield {
                'AWOKEN': sub(r'\D', '', nums[i]),
                'AWOKEN_DESC': descs[i],
                'READ_DATE': datetime.now()
            }