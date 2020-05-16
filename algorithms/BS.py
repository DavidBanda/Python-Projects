import ssl
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup


class ReadHTML:

    def __init__(self, url):
        self.url = url

    def getNames(self):
        tags = self.__getHTML()
        names = []
        for tag in tags:
            names.append(tag.contents[0])
        return names

    def getLinks(self):
        tags = self.__getHTML()
        contents = []
        for tag in tags:
            contents.append(tag.get('href', None))
        return contents

    def __getHTML(self):
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        html = urllib.request.urlopen(self.url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')

        return tags

    def searchName(self, name):
        return name if name in self.getNames() else 'No se encuentra el nombre'


RH = ReadHTML('http://py4e-data.dr-chuck.net/known_by_Meri.html')
print(RH.getNames())
print(RH.getLinks())
print(RH.searchName('Aaron'))


