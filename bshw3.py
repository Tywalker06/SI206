import requests
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

x = soup.prettify()

x = x.replace('logo2.png', 'media/logo.png')
x = x.replace('student', 'AMAZING student')
x = x.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg','media/fampic.jpg')


f = open('new.html', 'w')
f.write(x)
f.close()