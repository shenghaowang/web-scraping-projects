import scrapy

class WikiDexterCast(scrapy.Spider):
	name = "dexter"
	start_urls = ["https://en.wikipedia.org/wiki/Dexter_(season_1)"]

	def parse(self, response):
		for url in self.start_urls:
			yield scrapy.Request(url, callback=self.parse_cast)

	# def parse_list(self, response):
	# 	list_wrapper = 

	def parse_cast(self, response):
		cast_lists = []
		parent_dir = response.xpath("//div[@class='mw-parser-output']//ul")

		for cast_list in cast_lists:
			yield {
				'Name':
				'Type':
				'Link':
			}

		# Getting Actor/Character Name
		

		yield item