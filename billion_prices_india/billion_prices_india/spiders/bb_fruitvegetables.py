__author__ = 'mandeepak'

from BaseBigBasket import PriceSpiderBase
class PriceSpider(PriceSpiderBase):

    name = "bb_fruits_vegetables"
    start_urls = ['http://bigbasket.com/cl/fruits-vegetables/?sid=AooQO4SiY2OjMzUxom1kA6FjA6Jhb8I%3D']

