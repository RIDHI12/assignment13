Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
response=request.get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
data=response.json()
print(data["quoteText"])
