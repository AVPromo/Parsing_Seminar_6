import scrapy
from scrapy.http import HtmlResponse


class Book24Spider(scrapy.Spider):
    name = "book24"
    allowed_domains = ["book24.ru"]

    def __init__(self, query):
        super().__init__()
        self.query = query
        self.start_urls = [f"https://book24.ru/search/?q={query}"]

    def parse(self, response:HtmlResponse):
        links = response.xpath("//div[@class='product-list__item']//a[@class='product-card__name']")
        for link in links:
            yield response.follow(link, callback=self.parse_book)

    def parse_book(self, response:HtmlResponse):
        print()


