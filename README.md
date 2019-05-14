# PAD Monster Data Scraper

I couldn't find any existing data sets or tools to get PAD data, so I figured I would put something together myself.  
Ultimately, I'd like to create some kind of useful app using the data.  
Disclaimer: This is my first time using Scrapy, so I might not be implementing this very well.  

## Usage

The monster spider takes in two arguments: start and end. If you don't manually set them, you'll scrape monsters 1 - 5.  
I personally like using the jsonlines output, so I'll provide an example of that here.  
To run the spider, use the following command from the /pad-scraper/pad_scraper(/pad_scraper) directory:  
```scrapy crawl monster -a start=1 -a end=500 -s FEED_FORMAT=jsonlines -s FEED_URI=monster.jsonl```

## To Do List

- Spider for dungeons
- Text parser for skills
- Add a script to find bad data and replace it with good data  
- Add a script to find missing data and simply log it or (if possible) run the spider on those monsters  