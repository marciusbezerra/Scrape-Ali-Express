import urllib.request as request
import urllib.parse as parse
import json


class product:
    def __init__(self, id, name, price) -> None:
        self.id = id
        self.name = name
        self.price = price


products = []

product_search = "raspberry pi 2gb"

for page in range(1, 50):

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
                    p['productId'], p['title']['displayTitle'], p['prices']['salePrice']['minPrice']))
    else:
        print('no content!')

products.sort(key=lambda p: p.price)

with open(f'{product_search} - aliexpress price.txt', 'a') as file_prices:
    for p in products:
        file_prices.write(f'{p.id}\n')
        file_prices.write(f'{p.name}\n')
        file_prices.write(f'https://pt.aliexpress.com/item/{p.id}.html\n')
        file_prices.write("{0:.2f}\n\n".format(p.price))

print('finish ok!')
