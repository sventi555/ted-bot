from os import getenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Scraper:
	"""
	A Scraper scrapes data from TED Talks webpages.
	The `close` method must be called before the program is terminated.

	Attributes
	----------
	driver : WebDriver
		The driver used to scrape web content.
	"""

	def __init__(self, chrome_location):
		"""
		Configures options for the driver.

		Parameters
		----------
		chrome_location : string
			The system location of the chromedriver binary.
		"""
		chrome_options = Options()
		chrome_options.add_argument("--headless")	
		chrome_options.add_argument("--no-sandbox")
		self.driver = webdriver.Chrome(executable_path=chrome_location, chrome_options=chrome_options)

	def scrapeUrls(self, topics):
		"""
		Scrapes TED's website for TED Talk urls.

		Parameters
		----------
		topics : list of strings
			The video topics that will be included in the query (must be TED Talk topics).

		Returns
		-------
		list of strings
			The links to all the scraped TED Talks.
		"""
		video_links = []
		for topic in topics:
			self.driver.get('https://www.ted.com/talks?language=en&page=1&sort=newest&topics%5B%5D=' + topic)
			video_elements = self.driver.find_elements_by_xpath("//div[@class='col']//a[@class=' ga-link']")

			for element in video_elements:
				video_links.append(element.get_attribute('href'))

		return video_links


	def scrapeDescription(self, url):
		"""
		Scrapes TED's website for a specific Talk's description.

		Parameters
		----------
		url : string
			The url of the TED Talk to retrieve a description from.

		Returns
		-------
		string
			The description of the specified TED Talk.
		"""
		self.driver.get(url)
		description = self.driver.find_element_by_xpath("//meta[@itemprop='description']")
		return description.get_attribute('content')

	def close(self):
		"""
		Closes `self.driver`.
		"""
		self.driver.quit()
