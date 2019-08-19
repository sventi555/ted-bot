from os import getenv, path
from random import sample

from dotenv import load_dotenv
load_dotenv()

from scrape import Scraper
from message import message

# set up scraper and grab links, then pick a random one
scraper = Scraper(getenv('CHROME_LOCATION'))
links = scraper.scrapeUrls(['Technology', 'Design', 'Business'])

base_dir = path.dirname(path.dirname(path.abspath(__file__)))
history_path = path.join(base_dir, 'artifacts/history')

# if history artifact does not exist, create one
if not path.exists(history_path):
    open(history_path, 'a').close()

# check history to see if link was posted before, and cycle for a new one
with open(history_path) as f:
	past_links = f.readlines()
	link = sample(links, 1)[0].strip()
	while link in list(map(lambda x: x.strip(), past_links)):
		link = sample(links, 1)[0].strip()
	past_links.append(link + '\n')

# get the description for the chosen link
description = scraper.scrapeDescription(link)

scraper.close()

# send a formatted message to slack workspace determined by HOOK_URL
message(getenv('HOOK_URL'), link, description)

with open(history_path, 'w') as f:
	# save at most 50 most recent links
	f.writelines(past_links[-50:])
