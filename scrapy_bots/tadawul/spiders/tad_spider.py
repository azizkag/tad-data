from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tadawul.items import TadawulItem as tad

class TadSpider(BaseSpider):
    name = "tad"
    allowed_domains = ["tadawul.com.sa"]
    start_urls = []
    stocks = [4220,1060,1050,1040,1030,1080,8140,8260,2310,8060,8110,1320,8200,2360,4050,2300,6050,7050,2130,2190,4140,2010,2070,2120,4270,4010,5110,4040,4110,2270,6060,8100,2200,4020,2230,4260,4003,8190,2330,4030,2002,8300,4160,2220,6010,4005,4210,2250,8150,1140,1020,1010,8210,6001,8080,1330,3004,3001,3002,4001,8040,8310,8240,7020,8120,7040,1301,8250,3091,3040,3003,3050,3080,3020,3090,3060,2020,3030,8130,8312,8170,7010,7030,2140,3010,2320,4130,4230,8160,2060,8010,1211,2090,8012,6070,1214,2040,6004,4290,8070,4200,8230,4150,2240,2370,2260,8180,2150,1210,8280,2340,2080,6020,2110,2170,8030,2280,4170,2030,4280,2100,4002,2160,8270,6080,6040,2180,1201,4070,6090,4250,4190,4300,4004,2380,8050,8090,8290,4090,4080,8311,4240,2350,2001,8011,4061,1213,1310,4310,4100,8020,2210,6002,8220,2290,1123,1212,1810,1090,2050,4180,1150,1120]
    #In Tadawul sometimes when you check a company in the history data the results page of another company comes up!
    #It can be a good idea to verify that we have all the data points for the company of interest. 
    #This also can just be verified later as we are about to use the data
    for symb in stocks:
        for page in range(1,120):
            start_urls.append("http://www.tadawul.com.sa/wps/portal/!ut/p/c1/lYuxDoIwGAYf6f_4oRJGZcAiadBCQ7uYDmiIAsYYfX3r5qLG3Hh35Cgw-ftw9LdhnvyZOnKLvUJudjJhFFEWQW70Nmt5ySjT4O27r42ATCrNui5jSP7rhhZ43abJqyIG8OPW_kpqPY89WXLpx3IlqCErQ2S_Rpex7R7qcHoCRSE_JQ!!/dl2/d1/L3dJMjIyMnchL0lGaEFDRW9BREFIS0FBd09LZ0FNQXFvQURBaHFBQXdBNmdBTUFCb0FEQVNhQUF3QVdnQU1BQSEhL1lJNXcvN19OMENWUkk0MjBHMTkxMElLU1E5VTJBMjBCNQ!!/?symbol="+str(symb)+"&tabOrder=2&isNonAdjusted=0&resultPageOrder="+str(page)+"&totalPagingCount=1922&firstinput=2001%2F12%2F31&firstinput=2014%2F06%2F22&firstinput_Month=5&secondinput=2014%2F06%2F19&secondinput=2014%2F06%2F22&secondinput_Month=5")
    
    def parse(self, response):
        comp_ind = response.url.index('?symbol=')
        comp = response.url[comp_ind+8:comp_ind+12]
        print '\n\n\n ###### comp name '+ comp
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
                item['company'] = comp
                item['date'] = data[0]
                item['close'] = data[1]
                item['opening'] = data[2]
                item['high'] = data[3]
                item['low'] = data[4]
                item['change'] = data[5]
                item['change_per'] = data[6]
                item['volume'] = data[7]
                item['value'] = data[8]
                item['num_deals'] = data[9]
                items.append(item)

            counter += 1
        return items
