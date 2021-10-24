
# https://www.yattag.org
# https://www.programcreek.com/python/example/98644/yattag.Doc
# pip install yattag
from yattag import Doc
from yattag import indent

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
    with doc.tag('body'):
        with doc.tag('div', style='text-align: center;'):
            doc.line('h1', 'Listagem de Preços do AliExpress')
            with doc.tag('h3'):
                with doc.tag('a', href='https://forms.gle/J8KVkJsqYe8GvYW46'):
                    doc.text('Meu Raspberry de Exemplo')
            doc.line('h4', '500.00')
            doc.stag('img', src='/salmon-plays-piano.jpg',
                     alt='Meu Raspberry de Exemplo', style='width: 350px; display: inline-block;')

print(indent(doc.getvalue()))

with open('temp.html', 'w') as f:
    f.write(indent(doc.getvalue()))

# <body >
#    <div style = "text-align: center;" >
#         <h1 > Listagem de Preços do AliExpress < /h1 >
#         <h3 > <a href = "https://google.com" > Meu Raspberry de Exemplo < /a > </h3 >
#         <h4 > 500, 00 < /h4 >
#         <img style = "width: 350px; display: inline-block;"
#             src = "https://m.media-amazon.com/images/I/71IOISwSYZL._AC_SL1400_.jpg" alt = "Meu Raspberry de Exemplo" >
#     </div >
# </body >

# </html >
