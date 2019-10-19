import urllib.request as re
import urllib.parse as pa
import ssl

context = ssl._create_unverified_context()

#x = re.urlopen('https://www.google.com', context=context)
#print(x.read())

'''
url = 'https://www.udemy.com/courses/search/'
values = {'q': 'algorithms',
          'src': 'sac',
          'kw': 'algori'}

data = pa.urlencode(values)
data = data.encode('utf-8')
req = re.Request(url, data)
resp = re.urlopen(req, context=context)

print(resp.read())
'''

try:
    x = re.urlopen('https://www.udemy.com/courses/search/?src=ukw&q=algorithms',
                   context=context)
    print('Res1:', x.read())

except Exception as e:
    print(str(e))

try:
    url = 'https://www.udemy.com/courses/search/?src=ukw&q=algorithms'
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0'
    req = re.Request(url, headers=headers)
    resp = re.urlopen(req, context=context)

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(resp.read()))
    saveFile.close()

    print('Res2:', resp.read())
except Exception as e:
    print(str(e))
