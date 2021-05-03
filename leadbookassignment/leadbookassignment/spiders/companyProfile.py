import scrapy


class CompanyProfileSpider(scrapy.Spider):
  name = 'companyDetails'
  start_urls = ["https://www.adapt.io/directory/industry/telecommunications/A-1"]
  
  def parse(self, response):
    for company in response.xpath("//div[contains(@class, 'DirectoryList_linkItemWrapper__3F2UE ')]"):
      name = company.css('a::text').get()
      company_portal = company.css('a::attr(href)').get()
      
      if company_portal is not None:
        next_page = response.urljoin(company_portal)
        yield scrapy.Request(next_page, callback=self.company_parse)

  def company_parse(self, response):
    block = response.xpath("//span[contains(@class, 'CompanyTopInfo_infoValue__27_Yo')]")
    data = block.xpath("//div[contains(@class, 'CompanyTopInfo_contentWrapper__2Jkic')]")
    output = {}
   # for i in data:
    #  output[i.css('span::text').get()] = i.xpath("//span[contains(@class, 'CompanyTopInfo_infoValue__27_Yo')]").css('span::text').get()
    #yield{
     # 'company_data': output,
    #}

    company_employee = response.xpath("//div[contains(@class, 'TopContacts_roundedBorder__1a3yB undefined')]")
    employee_url = company_employee.xpath("//div[contains(@class, 'TopContacts_contactName__3N-_e')]").css('a::attr(href)').getall()
    for url in employee_url:
      if url is not None:
          next_page = response.urljoin(url)
          yield scrapy.Request(next_page, callback=self.employee)

  def employee(self, response):
    
    
    company_name=response.xpath("//a[contains(@class, 'ContactTopInfo_linkStyle__2lnTY')]")[0].css('a::text').get(),
    company_location =   response.xpath("//span[contains(@itemprop,'addressLocality')]").css('span::text').get(),
    company_website =   response.xpath("//span[contains(@class,'ContactTopInfo_infoValue__DNIWM')]")[3].css('span::text').get(),
    company_industry= response.xpath("//span[contains(@class,'ContactTopInfo_infoValue__DNIWM')]")[7].css('span::text').get(),
    company_employee_size =  response.xpath("//span[contains(@class,'ContactTopInfo_infoValue__DNIWM')]")[4].css('span::text').get(),
    company_revenue = response.xpath("//span[contains(@class,'ContactTopInfo_infoValue__DNIWM')]")[4].css('span::text').get(),
    contact_name = response.xpath("//h1[contains(@class, 'ContactTopInfo_title__2oYe3')]").css('h1::text').get(),
    contact_jobtitle =  response.xpath("//div[contains(@class, 'ContactTopInfo_jobTitle__1Psvw')]")[0].css('div::attr(content)').get(),
    email = response.xpath("//span[contains(@class,'ContactTopInfo_infoValue__DNIWM')]").css('span::text').get(),
    contact_department = response.xpath("//span[contains(@class,'ContactTopInfo_infoValue__DNIWM')]")[2].css('span::text').get()
    
    yield{
      'company_name':company_name,
      'company_location':  company_location,
      'company_website':  company_website,
      'company_industry': company_industry,
      'company_employee_size': company_employee_size,
      'company_revenue': company_revenue,
      
      'contact_details':[
        {
        'contact_name':contact_name,
        'contact_jobtitle': contact_jobtitle,
        'email':email,
        'contact_department':contact_department}
      ]
    }