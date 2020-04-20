import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
results = tree.findall('.//comment')
# counts = tree.findall('.//count')
counter = 0
sumlist = list()
for item in results:
    counter += 1
    counts = item.find('count').text
    counts = float(counts)
    sumlist.append(counts)

print ('Count: ', counter)
print ('Sum: ', sum(sumlist))


for dollar in item:
    dollar = item.get('count')
    print (dollar)
