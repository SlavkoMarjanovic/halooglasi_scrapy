# -*- coding: utf-8 -*-
import scrapy


class HaloSpiderSpider(scrapy.Spider):
    name = "halo_spider"
    allowed_domains = ["halooglasi.com"]
    start_urls = ["https://www.halooglasi.com/nekretnine/prodaja-stanova/beograd"]

    def parse(self, response):
        item = {}
        for submission_sel in response.css("h3.ad-title"):
            item['url'] = submission_sel.css("::attr(href)").extract_first().encode('utf-8')
            item['title'] = submission_sel.css("::text").extract_first().encode('utf-8')
            yield item
        next_page = response.css(".next").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
