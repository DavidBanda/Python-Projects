import ssl
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

cont = 0
nombres = list()
res = list()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def enlace(url):
    nombres.clear()
    res.clear()
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags:
        nombres.append(tag.get('href', None))
        res.append(tag.contents[0])

    return nombres[17]


aux = enlace('http://py4e-data.dr-chuck.net/known_by_Meri.html')
print(res)

