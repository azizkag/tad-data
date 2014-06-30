from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tadawul.items import TadawulItem as tad

class MainIndexSpider(BaseSpider):
    name = "main_index"
    allowed_domains = ["tadawul.com.sa"]
    start_urls = []
    #In Tadawul sometimes when you check a company in the history data the results page of another company comes up!
    #It can be a good idea to verify that we have all the data points for the company of interest. 
    #This also can just be verified later as we are about to use the data
    for page in range(1,59):
        start_urls.append("http://www.tadawul.com.sa/wps/portal/!ut/p/c1/pY3BCoJAFEW_xS94lxk1WpqFvZJJHBVnNjKLCik1Iur3s10FBRF3ec7hkqVxvbu2e3dph94dqSYbNgpxlbMvkKhsCl6HC-Z5DhThyM0zz6oA7Kda6GwlweKnGjrAo66KOE0kgH_qzWv9Rhmk3ZnUcui2ZMhOPv5Inwoy0Wy0zFfr1JVlfVO7Q-R5d81slZY!/dl2/d1/L3dJMjIyMkEhL0lKaEFDRW9BREFMS0FBd0dLZ0FNQXFvQURBSnFBQXdNNmdBTUFCb0FEQUNhQUF3QS9ZSTV3LzdfTjBDVlJJNDIwR05QOTBJSzZFSUlEUjAwMzQ!/?current_page=%2Ftasi%2Fjsp%2Fhtml%2Findeces_performance.&chart_tasi_current_sector=TASI&TASIactionString=chart_tasi.form.config_change&performance_tasi_fromdate=2001%2F12%2F31&performance_tasi_fromdate=2013%2F12%2F28&performance_tasi_fromdate_Month=11&performance_tasi_todate=2013%2F12%2F19&performance_tasi_todate=2013%2F12%2F28&performance_tasi_todate_Month=11&page_index_number="+str(page))

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//table[@class="Table3"]/tbody/tr')
        counter = 0
        items= []
        for site in sites:
            if counter > 1:
                item = tad()
                data = site.xpath('td/text()').extract()
                for i in range(len(data)):
                    data[i] = data[i].replace('\r','')
                    data[i] = data[i].replace('\t','')
                    data[i] = data[i].replace('\n','')
                #print data
                item['company'] = 'main_index'
                item['date'] = data[0]
                item['close'] = data[1]
                item['opening'] = data[2]
                item['high'] = data[3]
                item['low'] = data[4]
                item['volume'] = data[5]
                item['value'] = data[6]
                item['num_deals'] = data[7]

                
                items.append(item)

            counter += 1
        return items
