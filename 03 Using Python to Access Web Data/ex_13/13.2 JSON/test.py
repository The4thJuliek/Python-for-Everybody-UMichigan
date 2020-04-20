import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode('utf-8')
print('Retrieved', len(data), 'characters')

json_info = json.loads(data)
counter = 0
sumlist = list()
for item in json_info:
    item = json_info['comments']
    for dollar in item:
        dollar = dollar.get('count')
        sumlist.append(dollar)
        counter += 1

print ('Count: ', (counter/2.0))
print ('Sum: ', (sum(sumlist)/2.0))
