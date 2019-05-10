from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

config = None
with open('config.json') as f:
	config = json.load(f)

class Scraper:

	def __init__(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")	
		self.driver = webdriver.Chrome(executable_path=config.get('CHROME_LOCATION'), chrome_options=chrome_options)

	def scrapeUrls(self, topics):
		video_links = []
		for topic in topics:
			self.driver.get('https://www.ted.com/talks?language=en&page=1&sort=newest&topics%5B%5D=' + topic)
			video_elements = self.driver.find_elements_by_xpath("//div[@class='col']//a[@class=' ga-link']")

			for element in video_elements:
				video_links.append(element.get_attribute('href'))

		return video_links


	def scrapeDescription(self, url):
		self.driver.get(url)
		description = self.driver.find_element_by_xpath("//meta[@itemprop='description']")
		return description.get_attribute('content')

	def close(self):
		self.driver.quit()
