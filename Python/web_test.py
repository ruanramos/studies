import urllib.request
import urllib.parse

try:
	x = urllib.request.urlopen('https://www.google.com/search?q=test')
	print(x.read())

except Exception as e:
	print(str(e))