from src.scrape import Scraper
from src.message import message
from random import sample

scraper = Scraper()
links = scraper.scrapeUrls(['Technology', 'Design', 'Business'])
link = sample(links, 1)[0]

with open('history') as f:
	past_links = f.readlines()
	while link in list(map(lambda x: x.strip(), past_links)):
		link = sample(links, 1)[0]

description = scraper.scrapeDescription(link)

scraper.close()

message(link, description)

with open('history', 'a', ) as f:
	f.write(link + '\n')