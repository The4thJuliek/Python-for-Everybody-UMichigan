Extracting Data from JSON

In this assignment you will write a Python program somewhat similar to
http://www.py4e.com/code3/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib
and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below:

We provide two files for this assignment. One is a sample file where we give you
the sum for your testing and the other is the actual data you need to process for
the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_370345.json (Sum ends with 63)

You do not need to save these files to your folder since your program will read the
data directly from the URL. Note: Each student will have a distinct data url for
the assignment - so only use your own data url for analysis.

Data Format

The data consists of a number of names and comment counts in JSON as follows:

{
 comments: [
   {
     name: "Matthias"
     count: 97
   },
   {
     name: "Geomer"
     count: 97
   }
   ...
 ]
}

The closest sample code that shows how to parse JSON and extract a list is json2.py.
You might also want to look at geoxml.py to see how to prompt for a URL and retrieve
data from a URL.

Sample Execution

$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...

Turning in the Assignment
Enter the sum from the actual data and your Python code below:
Sum: (ends with 63)


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
