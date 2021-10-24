from yattag import indent
from yattag import Doc
import urllib.request as request
import urllib.parse as parse
import json

# https://www.yattag.org
# https://www.programcreek.com/python/example/98644/yattag.Doc
# pip install yattag
from yattag import Doc
from yattag import indent
from yattag.indentation import Style


class product:
    def __init__(self, id, name, img, price) -> None:
        self.id = id
        self.name = name
        self.img = img
        self.price = price


products = []

product_search = "raspberry pi 2gb"

for page in range(1, 2):

    print(f'reading page {page}...')

    response = request.urlopen(
        f'https://pt.aliexpress.com/wholesale?trafficChannel=main&d=y&CatId=0&SearchText={parse.quote(product_search)}&ltype=wholesale&SortType=price_asc&page={page}&groupsort=1')
    contents = response.read().decode('utf-8')

    start = contents.find("{\"mods\":{")
    if start >= 0:
        end = contents.find("};\n", start)
        json_str = contents[start:end+1]
        json_obj = json.loads(json_str)

        for p in json_obj['mods']['itemList']['content']:
            if 'store' in p:
                products.append(product(
                    p['productId'], p['title']['displayTitle'], p['image']['imgUrl'], p['prices']['salePrice']['minPrice']))
    else:
        print('no content!')

products.sort(key=lambda p: p.price)

doc = Doc()

doc.asis('<!doctype html>')
with doc.tag('html', lang='en'):
    with doc.tag('head'):
        doc.stag('meta', ('charset', 'UTF-8'))
        doc.stag('meta', ('http-equiv', 'X-UA-Compatible'),
                 ('content', 'IE=edge'))
        doc.stag('meta', ('viewport', 'width=device-width, initial-scale=1.0'))
        with doc.tag('title'):
            doc.text('Listagem de Preços do AliExpress')
    with doc.tag('body', style='text-align: center;'):
        doc.line('h1', 'Listagem de Preços do AliExpress')
        for p in products:
            with doc.tag('div', Style='margin: 10px; border: 2px solid lightgray; border-radius: 5px'):
                with doc.tag('h3'):
                    with doc.tag('a', href=f'https://pt.aliexpress.com/item/{p.id}.html'):
                        doc.text(f'{p.name} ({p.id})')
                doc.line('h4', "{0:.2f}\n\n".format(p.price))
                doc.stag('img', src=f'https://{p.img}',
                         alt=f'{p.name} ({p.id})', style='max-width: 350px; display: inline-block;')

filename = product_search.replace(' ', '_')

with open(f'{filename}_aliexpress_price.html', 'w') as file_prices:
    file_prices.write(indent(doc.getvalue()))

print('finish ok!')
