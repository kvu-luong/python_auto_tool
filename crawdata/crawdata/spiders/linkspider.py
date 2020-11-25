# -*- coding: utf-8 -*-
import scrapy


class LinkspiderSpider(scrapy.Spider):
	name = 'linkspider'
	allowed_domains = ['www.geeksforgeeks.org']
	start_urls = [
		'https://www.geeksforgeeks.org/top-algorithms-and-data-structures-for-competitive-programming/',
	]

	custom_settings = { 'FEED_URI': "linkspider.csv",
                       'FEED_FORMAT': 'csv'} #default file

	def parse(self, response):
		print('procesing: '+response.url)
		links = response.css("ol li a::attr(href)").getall()
		#Making extracted data row wise
		filename = f'tests.csv'
		with open(filename, 'w') as f:
			for link in links:
				f.write(link+'\n')

