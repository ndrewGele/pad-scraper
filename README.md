# PAD Data Scraper

## About  

I couldn't find any existing data sets or tools to get PAD data, so I figured I would put something together myself.  
Ultimately, I'd like to create some kind of useful app using the data.  
Disclaimer: This is my first time using Scrapy, so I might not be implementing this very well.  

## Current State

I think I'm going to shelve this to work on some other projects, but this is in a pretty good spot.  
The spiders are all pretty reliable, but there are most likely some edge cases that'll fail to scrape.  
Feel free to fork and PR or make something cool using the data. I'd be hype to see it get used.

## Usage

This repo contains some data files already, but you can rerun the spiders to get fresh data.  

### Monster Spider

The monster spider takes in two arguments: start and end. If you don't manually set them, you'll scrape monsters 1 - 5.  
I personally like using the jsonlines output, so I'll provide an example of that here.  
To run the spider, use the following command from the /pad-scraper/pad_scraper(/pad_scraper) directory:  
```scrapy crawl monster -a start=1 -a end=500 -s FEED_FORMAT=jsonlines -s FEED_URI=monster.jsonl```

### Awoken Skill Spider

This spider simply pulls all of the skills from the Awoken Skill List page.  
No arguments are needed, so it can siumply be run with:  
```scrapy crawl awoken -s FEED_FORMAT=jsonlines -s FEED_URI=awoken.jsonl```

### Dungeon Spider

This spider simply pulls all of the skills from the Awoken Skill List page.  
No arguments are needed, so it can siumply be run with:  
```scrapy crawl dungeon -a start=1 -a end=500 -s FEED_FORMAT=jsonlines -s FEED_URI=dungeon.jsonl```

## Things that would be cool to add

- Script that finds missing rows and/or bad data points
  - Use to locate those aforementioned edge cases
  - What if it automatically crawled and updated the bad records too Kreygasm  
- Data cleaning  
  - JSONL is easy to append to and the current format makes sense, but a flatter data structure would likely be easier to use
  - Raw skill text for monsters and dungeons could be turned into dummy variables, but it's **very raw** lol  
- Make something new that actually uses the data!  
