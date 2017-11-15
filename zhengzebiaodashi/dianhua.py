Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> y = 'tel:010-12345678 address:changanRoad'
>>> re.findall('\d', y)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    re.findall('\d', y)
NameError: name 're' is not defined
>>> re.findall('\d', y)

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    re.findall('\d', y)
NameError: name 're' is not defined
>>> 
>>> y = 'tel:010-12345678 address:changanRoad'
>>> re.findall('\d', y)

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    re.findall('\d', y)
NameError: name 're' is not defined
>>> import re
>>> re.findall('\d', y)
['0', '1', '0', '1', '2', '3', '4', '5', '6', '7', '8']
>>> re.findall('\d+', y)
['010', '12345678']
>>> re.findall('\d+-', y)
['010-']
>>> re.findall('\d+-\d+', y)
['010-12345678']
>>> 
