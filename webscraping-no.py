from lxml import html
import requests

#url = raw_input("> ")
url = "http://www.filmaffinity.com/en/film770252.html"
page = requests.get(url)
tree = html.fromstring(page.text)

paises = tree.xpath('//dd/text()')
a = tree.xpath('//a/text()')

print "Title: " + paises[0] + '\n'

print  "Year: " + paises[1] + '\n'

if paises[2][-4:] == "min.":
     print  "Country: " + paises[3] + '\n'
     count = 4
else:
     print  "Country: " + paises[2] + '\n'
     count = 3

countB = 0
while a[countB] != "Tweet":
     countB += 1

print  "Director: " + a[countB+1] + '\n'
##if a[48]== 'Tweet':
##     print  "Director: " + a[49] + '\n'
##elif a[49]== 'Tweet':
##     print  "Director: " + a[50] + '\n'
##elif a[56]== 'Tweet':
##     print  "Director: " + a[57] + '\n'


while paises[count][0] == ',':
     count += 1

print "Screenwriter: " + paises[count]  + '\n'

print "Music: " + paises[count+1]  + '\n'

print "Cinematography: " + paises[count+2]  + '\n'

count = -1
while paises[count][0] == '\n' or paises[count][0] == '\r' :
     count += -1
     
print "Synopsis / Plot:  " + paises[count]  + '\n'



b= tree.xpath('//img/@src')

count = -1
while b[count][-8:] != 'main.jpg':
     count += -1

print "Img:  " + b[count]  + '\n'
