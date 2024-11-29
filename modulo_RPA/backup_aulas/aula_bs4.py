from bs4 import BeautifulSoup

html = '<html><body><h1>Hello, World!</h1></body></html>'
soup = BeautifulSoup(html, features='html.parser')
print(soup.h1.text)