import urllib.request
import urllib.parse as pa
import re
import ssl

context = ssl._create_unverified_context()

url = 'http://pythonprogramming.net/search'
values = {'q':'basics'}

data = pa.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req, context=context)

#print(resp.read())

paragraphs = re.findall(r'<p>(.*?)</p>', str(resp.read()))

for eachP in paragraphs:
    print(eachP)


