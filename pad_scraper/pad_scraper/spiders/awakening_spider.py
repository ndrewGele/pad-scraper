from scrapy import Spider
from scrapy import Selector
from re import sub
from datetime import datetime


# Following Scrapy Tutorial Mostly
class AwakeningSpider(Spider):

    name = 'awake'

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
        print(nums)
        print(descs)

        for i in range(len(nums)):
            yield {
                'AWAKE': sub(r'\D', '', nums[i]),
                'AWAKE_DESC': descs[i],
                'READ_DATE': datetime.now()
            }