from scrapy import Spider
from scrapy import Selector
import re


class MonsterSpider(Spider):
    name = 'monster'
    start_urls = [
        'http://www.puzzledragonx.com/en/monster.asp?n='
        + str(i) for i in range(1,5000)
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
        skills = sel.xpath("//table[@id='tablestat']//td[@class='value-end']/text()").getall()

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
            'AWAKE': [re.sub("=", "", x) for x in awakenings],
            'S_AWAKE': [re.sub("=", "", x) for x in s_awakenings],
            'SKILL_TEXT': skills[0],
            'LEAD_TEXT': re.sub("\r\n\t\t\t\t\t\t", "None", skills[4])
        }