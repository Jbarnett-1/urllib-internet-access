# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:10:03 2021

@author: Jerrika
"""
import urllib.request
import urllib.parse #values to post request
import re

url = 'https://genius.com/Demi-lovato-met-him-last-night-lyrics'  # url to visit
values = {'s':'basic', 
          'submit':'search'}  # dictionary used

data = urllib.parse.urlencode(values)  #encode values
data = data.encode('utf-8')   # type of coding
req = urllib.request.Request(url,data)   #encode data
resp = urllib.request.urlopen(req)   #request
respData = resp.read()                      

#print(respData)

paragraphs = re.findall(r'<br>(.*?)</br>',str(respData)) #() is content we're looking for to identify
 
for eachP in paragraphs:
    print (eachP)
