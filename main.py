import scrapy

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']

    def start_requests(self):
        search_query = 'laptop'  # Replace with your desired search query
        url = f'https://www.amazon.com/s?k={search_query}'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        product_elements = response.css('div.s-result-item')

        for product_element in product_elements:
            product_name = product_element.css('span.a-size-medium::text').get(default='N/A').strip()
            product_price = product_element.css('span.a-offscreen::text').get(default='N/A').strip()
            product_url = product_element.css('a.a-link-normal::attr(href)').get(default='N/A')

            yield {
                'name': product_name,
                'price': product_price,
                'url': response.urljoin(product_url)
            }