import scrapy
import unidecode
from datetime import time

class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com.br/s?k=fralda+descart%C3%A1vel&rh=n%3A18467493011&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss']

    def parse(self, response):
        for fraldas in response.css('.puis-padding-right-small'):
            nome = unidecode.unidecode(fraldas.css('.puis-padding-right-small .a-size-base-plus ::text').get())
            preco_reais = ''.join(fraldas.css('.a-price-whole ::text').get().split())
            preco_centavos = fraldas.css('.a-price-fraction::text').get()
            preco = preco_reais + ',' + preco_centavos

            yield {
                'nome': nome,
                'preco': preco
            }

        for pag in range(2, 18, 1):
            proxima_pagina = f'https://www.amazon.com.br/s?k=fralda+descart%C3%A1vel&rh=n%3A18467493011&page={pag}'
            yield response.follow(proxima_pagina, callback=self.parse)