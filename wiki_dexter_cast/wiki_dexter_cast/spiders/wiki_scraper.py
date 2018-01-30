import scrapy

class WikiDexterCast(scrapy.Spider):
	name = "dexter"
	start_urls = ['https://en.wikipedia.org/wiki/Dexter_(season_1)']

	def parse(self, response):
		for url in self.start_urls:
			yield scrapy.Request(url, callback=self.parse_cast)

	def parse_cast(self, response):
		mainCasts = response.xpath("//div[@class='mw-parser-output']/ul[1]//li")
		count = 1

		for cast in mainCasts:
			sel = "//div[@class='mw-parser-output']/ul[1]//li[%d]" % count
			count += 1
			actorName = cast.xpath(sel + "//a[1]/text()").extract()
			actorLink = "https://en.wikipedia.org" + cast.xpath(sel + "//a[1]/@href").extract()[0]
			yield {
				'Name': actorName,
				'Type': "actor",
				'Link':	actorLink
			}

			characterName = cast.xpath(sel + "//a[2]/text()").extract()
			characterLink = "https://en.wikipedia.org" + cast.xpath(sel + "//a[2]/@href").extract()[0]
			yield {
				'Name': characterName,
				'Type': "character",
				'Link': characterLink
			}

		casts = response.xpath("//table[@class='multicol']//ul//li")
		count = 1

		for cast in casts:
			sel = "//table[@class='multicol']//ul//li[%d]" % count
			count += 1
			actorName = cast.xpath(sel + "//a[1]/text()").extract()
			actorLink = "https://en.wikipedia.org" + cast.xpath(sel + "//a[1]/@href").extract()[0]
			yield {
				'Name': actorName,
				'Type': "actor",
				'Link':	actorLink
			}

			characterName = cast.xpath(sel + "//a[2]/text()").extract()
			characterLink = "https://en.wikipedia.org" + cast.xpath(sel + "//a[2]/@href").extract()[0]
			yield {
				'Name': characterName,
				'Type': "character",
				'Link': characterLink
			}