from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ThomsonLocalSpider(CrawlSpider):
    name = 'thomsonlocal'
    allowed_domains = ['thomsonlocal.com']
    start_urls = ['https://www.thomsonlocal.com/search/plumber/london']

    rules = [
        Rule(LinkExtractor(restrict_css='.resultsBlock .name'),
             callback='parse_seller_page'),
    ]

    def parse_seller_page(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        print(response.css)
        return {
            'link': response.request.url,
            'name': response.css('.branchDetails .listingName::text').get(),
            'email': response.css('.writeReview .customerEmail::attr(value)').get(),
            'phone': response.css('.phoneNumber .fontSize2::text').get(),
            'postalCode': response.css('.address span::text').get(),
            'website': response.css('.branchDetailsButtons .webpageButton::attr(href)').get(),
            'facebook': response.css('.socialMedia .facebook a::attr(href)').get(),
            'twitter': response.css('.socialMedia .twitter a::attr(href)').get(),
        }
