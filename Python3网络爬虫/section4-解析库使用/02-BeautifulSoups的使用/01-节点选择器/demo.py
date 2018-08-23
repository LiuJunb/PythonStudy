
from bs4 import BeautifulSoup

# Beautiful Soup is not an HTTP client. You should probably use an HTTP client
# soup = BeautifulSoup('http://www.baidu.com', 'lxml')
# print(soup.title)


# serWarning: "b'./test.html'" looks like a filename, not markup
soup = BeautifulSoup('./test.html', 'lxml')
print(soup.title)




