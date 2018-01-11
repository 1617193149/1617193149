# -*- co# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

url = 'http://www.job5156.com/ids_it/zhaopin_wl/'
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = { 'User-Agent' : user_agent }
 
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
p = 0
j = 0
content_pattern = re.compile('<a class="text-overflow".*?>.*?<a.*?>(.*?)</div>.*?', re.S) 
content_list = re.findall(content_pattern, html)
content_pattern1 = re.compile('div class="col-10".*?>(.*?)</div>.*?', re.S)    
content_list1 = re.findall(content_pattern1, html)

for item in content_list:                                         
    print '\n'
    print content_list[j]                                         
    j = j + 1                                                     
                                                     

    for i in range(0,1):                                          
        print content_list1[i]

    input = raw_input()                                          
    if input == "e":       
        break
    print "******************************next******************************\n"
