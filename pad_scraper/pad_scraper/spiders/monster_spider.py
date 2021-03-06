from scrapy import Spider
from scrapy import Selector
from re import sub
from datetime import datetime


# Following Scrapy Tutorial Mostly
class MonsterSpider(Spider):

    name = 'monster'

    def __init__(self, start = '1', end = '5', **kwargs):

        super().__init__(**kwargs)

        self.start_urls = [
            'http://www.puzzledragonx.com/en/monster.asp?n='
            + str(i) for i in range(int(start), int(end)+1)
        ]

    def parse(self, response):
        sel = Selector(response)
        
        
        # Get Profile Table
        profile = sel.xpath("//table[@class='tableprofile']//td[@class='data']")
        limit = 1
        if len(profile) >= 6:
            limit = profile[5].xpath('normalize-space(./text())').get()
            if limit == '--': limit = '1.0' 
        

        # Get Stats Table
        stats = sel.xpath("//div[@id='comparechart']//tr")
                

        # Get Awakenings and S.Awakenings if they exist
        awoken = sel.xpath("//td[@class='awoken1']")
        awakenings = []
        s_awakenings = []
        if len(awoken) > 0:
            awakenings = [a[-2:] for a in awoken[0].css('a::attr(href)').getall()]
        if len(awoken) > 1:
            s_awakenings = [a[-2:] for a in awoken[1].css('a::attr(href)').getall()]

        
        # Get Skill Text
        active = sel.xpath("//tr[td='Active Skill:']/following-sibling::tr[1][td='Effects:']/td[@class='value-end']//text()").getall()        
        if len(active) == 0: active = 'None' 
        else: active = ''.join(active)

        lead = sel.xpath("//tr[td='Leader Skill:']/following-sibling::tr[1][td='Effects:']/td[@class='value-end']//text()").getall()
        if len(lead) == 0: lead = 'None' 
        else: lead = ''.join(lead)
        


        # Return this nice json
        yield {
            'NUMBER': response.url[46:],
            'NAME': sel.css('h1::text').get(),
            'ELEM': profile[1].css('a::text').getall(),
            'RARE': profile[2].css('a::text').getall()[0],
            'TYPE': profile[0].css('a::text').getall(),
            'COST': profile[3].css('a::text').getall()[0],
            'LB': limit,
            'HP': stats[2].css('td::text').getall()[2],
            'ATK': stats[3].css('td::text').getall()[2],
            'RCV': stats[4].css('td::text').getall()[2],
            'WGHT': stats[5].css('td::text').getall()[1],
            'AWAKE': [sub("=", "", x) for x in awakenings],
            'S_AWAKE': [sub("=", "", x) for x in s_awakenings],
            'SKILL_TEXT': active,
            'LEAD_TEXT': lead,
            'READ_DATE': datetime.now()
        }