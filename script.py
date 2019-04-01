from src.scrape import Scraper
from src.message import message
from random import randint

scraper = Scraper()
links = scraper.scrapeUrls(['Technology', 'Design', 'Business'])
link = links[randint(0, len(links) - 1)]

history = None
with open('history') as f:
	past_links = f.readlines()
	while link in past_links:
		link = links[randin(0, len(links) - 1)]

description = scraper.scrapeDescription(link)

scraper.close()

message(link, description)

with open('history', 'a', ) as f:
	f.write(link + '\n')