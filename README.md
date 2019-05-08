# PAD Monster Data Scraper

I couldn't find any existing data sets or tools to get PAD data, so I figured I would put something together myself.  
Disclaimer: This is my first time using Scrapy, so I might not be implementing this very well.

## Usage

The monster spider takes in two arguments: start and end. If you don't manually set them, you'll scrape monsters 1 - 5.  
I personally like using the jsonlines output, so I'll provide an example of that here.  
To run the spider, use the following command from the /pad_scraper/pad_scraper directory:  
```scrapy crawl monster -a start=1 -a end=500 -s FEED_FORMAT=jsonlines -s FEED_URI=monster.json```

## To Do List

- Add an Awakenings spider
- Add a script to dedupe data