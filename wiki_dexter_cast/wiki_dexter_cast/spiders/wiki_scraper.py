import scrapy

class WikiDexterCast(scrapy.Spider):
	name = "dexter"
	start_urls = ['https://en.wikipedia.org/wiki/Dexter_(season_1)']

	def parse(self, response):
		for url in self.start_urls:
			yield scrapy.Request(url, callback=self.parse_cast)

	def parse_cast(self, response):
		parent_dirs = []
		parent_dirs.append("//div[@class='mw-parser-output']/ul[1]")
		parent_dirs.append("//table[@class='multicol']//td[1]//ul")
		parent_dirs.append("//table[@class='multicol']//td[2]//ul")

		for parent_dir in parent_dirs:
			casts = response.xpath(parent_dir + "//li")
			count = 1
			for cast in casts:
				sel = parent_dir + ("//li[%d]" % count)
				count += 1
				castLinks = response.xpath(sel + "//a")
				if len(castLinks) != 2:
					continue
				else:
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