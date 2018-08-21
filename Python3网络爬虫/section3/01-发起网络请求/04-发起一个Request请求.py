import urllib.request
import ssl

context = ssl._create_unverified_context()

request = urllib.request.Request('https://python.org')

resposne = urllib.request.urlopen(request, context=context)

print(resposne.read().decode('utf-8'))







