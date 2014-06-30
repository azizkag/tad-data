# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class TadawulItem(Item):
    # define the fields for your item here like:
    company = Field()
    date = Field()
    close = Field()
    opening = Field()
    high = Field()
    low = Field()
    change = Field()
    change_per = Field()
    volume = Field()
    value  = Field()
    num_deals = Field()
