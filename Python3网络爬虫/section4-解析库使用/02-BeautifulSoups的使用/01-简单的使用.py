from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(soup)  # <html><body><p>Hello</p></body></html>
print(soup.p)  # <p>Hello</p>
print(soup.p.string)  #  Hello
