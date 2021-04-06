import urllib.request 
import urllib.parse   #values to post request
import re

# cite url to visit and search f
url = 'http://pythonprogramming.net'
values = {'s':'basic', 
          'submit':'search'}  # dictionary used

# encode values to specific code, request data, and read
data = urllib.parse.urlencode(values) 
data = data.encode('utf-8')   
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()                      

#() is content we're looking for to identify
paragraphs = re.findall(r'<br>(.*?)</br>',str(respData)) 

# print data
for eachP in paragraphs:
    print (eachP)
