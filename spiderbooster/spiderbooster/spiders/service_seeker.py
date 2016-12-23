# -*- coding: utf-8 -*-
import scrapy


class ServiceSeekerSpider(scrapy.Spider):
    name = "service_seeker"
    allowed_domains = ["https://developer.foursquare.com/docs/venues/events"]
    start_urls = ['https://developer.foursquare.com/docs/venues/events']

    def parse(self, response):
    #        blabla = hxs.xpath('b/text()').extract()
    #    for hxs in response.xpath('//body/div'):
            print response.xpath('//body/div').extract()
