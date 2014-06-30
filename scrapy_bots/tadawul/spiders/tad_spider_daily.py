from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from tadawul.items import TadawulItem as tad
import datetime

class TadSpider(BaseSpider):
    name = "tad_daily"
    allowed_domains = ["tadawul.com.sa"]
    start_urls = []
    #This list can be replaced with a function that reads a file containing this information
    #for easy update
    stocks = [4220,1060,1050,1040,1030,1080,8140,8260,2310,8060,8110,1320,8200,2360,4050,2300,6050,7050,2130,2190,4140,2010,2070,2120,4270,4010,5110,4040,4110,2270,6060,8100,2200,4020,2230,4260,4003,8190,2330,4030,2002,8300,4160,2220,6010,4005,4210,2250,8150,1140,1020,1010,8210,6001,8080,1330,3004,3001,3002,4001,8040,8310,8240,7020,8120,7040,1301,8250,3091,3040,3003,3050,3080,3020,3090,3060,2020,3030,8130,8312,8170,7010,7030,2140,3010,2320,4130,4230,8160,2060,8010,1211,2090,8012,6070,1214,2040,6004,4290,8070,4200,8230,4150,2240,2370,2260,8180,2150,1210,8280,2340,2080,6020,2110,2170,8030,2280,4170,2030,4280,2100,4002,2160,8270,6080,6040,2180,1201,4070,6090,4250,4190,4300,4004,2380,8050,8090,8290,4090,4080,8311,4240,2350,2001,8011,4061,1213,1310,4310,4100,8020,2210,6002,8220,2290,1123,1212,1810,1090,2050,4180,1150,1120]
    #In Tadawul sometimes when you check a company in the history data the results page of another company comes up!
    #It can be a good idea to verify that we have all the data points for the company of interest. 
    #This also can just be verified later as we are about to use the data
    for symb in stocks:
        start_urls.append("http://www.tadawul.com.sa/wps/portal/!ut/p/c1/lYuxDoIwGAYf6f_4oRJGxQSLpEELDe1iOqghChhj9PWtm4sac-PdkaPA6O_90d_6afRn6sjNdgq52cqEUURZBLnWm6zlOaNMg7fvvjYCMqk067qMIfmvG1rgdZsmr4oYwI9b-yup1TTsyZJLP5YLQQ3ZZYjs1-gytN1DHU5PZ4joZA!!/dl2/d1/L0lJWm1aaWdwUkEhIS9JRGhBQ0VvQURBVEtBQXdBS2dBTUJLb0FEQWhxQUF3QTRlR1NBQXdPL1lJNTBzbHl0d0EhIS83X04wQ1ZSSTQyMEcxOTEwSUtTUTlVMkEyMEI1L2FjdGlvblN0cmluZy9jb21wYW55/?symbol="+str(symb)+"&tabOrder=2")
    
    def parse(self, response):
        #TODO:: read this date from a file
        lastDate = datetime.datetime.strptime("2014/6/19","%Y/%m/%d")
        comp_ind = response.url.index('?symbol=')
        comp = response.url[comp_ind+8:comp_ind+12]
        print '\n\n\n ###### comp name '+ comp
        sel = Selector(response)
        sites = sel.xpath('//table[@class="Table3"]/tbody/tr')
        counter = 0
        items= []
        for site in sites[2:]:
            #creating the data item
            item = tad()
            data = site.xpath('td/text()').extract()
            
            for i in range(len(data)):
                data[i] = data[i].replace('\r','')
                data[i] = data[i].replace('\t','')
                data[i] = data[i].replace('\n','')
            #print data
            date = datetime.datetime.strptime(data[0],"%Y/%m/%d")
            if date > lastDate:
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
            else:
                #we have seen every thing else so exit the for loop
                break

        return items
