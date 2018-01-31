### Initiate scrapy project
In cmd/terminal, run the following command under the project directory.
scrapy startproject wiki_dexter_cast

### Crawl cast information and save it in CSV file.
Redirect to /wiki_dexter_cast, run the following command.
scrapy crawl dexter -o cast.csv

### Debug using scrapy shell
1. In cmd/terminal, run
scrapy shell https://en.wikipedia.org/wiki/Dexter_(season_1)

2. Check the validity of html path, e.g.
response.xpath("//table[@class='multicol']//ul//li")

3. Exit scrapy shell by running
exit()