from re import S
import requests
from bs4 import BeautifulSoup

URL="https://en.wikipedia.org/wiki/MacBook"
page=requests.get(URL)
soup=BeautifulSoup(page.content, 'html.parser')

headings=soup.find_all(class_="mw-headline")
print("num headings: "+str(len(headings)))

map={}
content=soup.find_all(text=True)

s = ""
for i in content:
  text = i.get_text().strip()
  s+=text

punctuation = '''[].,?1234'567890!()/\:;""'''
s = s.lower()
for i in s:
  if i in punctuation:
    s = s.replace(i, '')
strlist = s.split(" ")

for i in strlist:
  map[i] = 1 if map.get(i)==None else map.get(i)+1

word="macbook"
print("frequency of "+word+": "+str(map.get(word)))


cleaned=[]
for c in content:
    text=c.get_text().strip()
    cleaned.append(text)
print(cleaned)

x=vectorize(cleaned,vect)
pred_array=model.predict(x)