import scrapy
from ..items import LeadbookassignmentItem

class CompanySpider(scrapy.Spider):
    name = 'company'
    start_urls = ['https://www.adapt.io/directory/industry/telecommunications/A-1']
    
    
    def parse(self,response):

        items = LeadbookassignmentItem()
        
        for company in response.xpath("//div[contains(@class,'DirectoryList_link')]"):
            company_name = company.xpath("./a/text()").get()
            url = company.xpath("./a/@href").get()
            source_url = url.split('https://www.adapt.io')[1]
            
            items['company_name'] = company_name 
            items['source_url'] = source_url 

            yield items