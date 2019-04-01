from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Scraper:

	def __init__(self):
		chrome_options = Options()
		# chrome_options.add_argument("--headless")	
		self.driver = webdriver.Chrome(chrome_options=chrome_options)

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
		description = self.driver.find_element_by_xpath("//p[contains(@class, 'l-h') and contains(@class, 'm-b')]")
		return description.text

	def close(self):
		self.driver.close()

	