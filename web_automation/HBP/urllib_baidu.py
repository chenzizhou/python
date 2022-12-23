from urllib import request
response = request.urlopen("http://192.168.10.196:7799/")
request.Request()
html = response.read( )
print(html)
