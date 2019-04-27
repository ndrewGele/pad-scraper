from scrapy import Spider
from scrapy import Selector


class MonsterSpider(Spider):
    name = 'monster'
    start_urls = [
        'http://www.puzzledragonx.com/en/monster.asp?n='
        + str(i) for i in range(1,501)
    ]

    def parse(self, response):
        sel = Selector(response)
        
        stats = sel.xpath("//div[@id='comparechart']//tr")
        awoken = sel.xpath("//td[@class='awoken1']")
        
        awakenings = []
        s_awakenings = []
        if len(awoken) > 0:
            awakenings = [a[-2:] for a in awoken[0].css('a::attr(href)').getall()]
        if len(awoken) > 1:
                s_awakenings = [a[-2:] for a in awoken[1].css('a::attr(href)').getall()]

        yield {
            'NUMBER': response.url[46:],
            'NAME': sel.css('h1::text').get(),
            'ELEM1': 'placeholder',
            'ELEM2': 'placeholder',
            'RARE': 'placeholder',
            'HP': stats[2].css('td::text').getall()[2],
            'ATK': stats[3].css('td::text').getall()[2],
            'RCV': stats[4].css('td::text').getall()[2],
            'WGHT': stats[5].css('td::text').getall()[1],
            'AWAKE': awakenings,
            'S_AWAKE': s_awakenings
        }