import scrapy
import unidecode

class AmericanasSpider(scrapy.Spider):
    name = 'americanas'
    start_urls = ['https://www.americanas.com.br/busca/fralda-descartavel?limit=24&offset=0']

    def parse(self, response):
        for fraldas in response.css('.fsViFX'):
            nome = unidecode.unidecode(fraldas.css('.gUjFDF ::text').get())
            preco = ''.join(fraldas.css('.liXDNM ::text').get().split()[-1:])

            yield {
                'nome': nome,
                'preco': preco,
            }
        pag = 0
        while pag < 481:
            pag = pag +24
            proximapagina = f'https://www.americanas.com.br/busca/fralda-descartavel?limit=24&offset={pag}'
            yield response.follow(proximapagina, callback=self.parse)