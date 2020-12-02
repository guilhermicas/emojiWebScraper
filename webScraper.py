# Go to https://unicode.org/emoji/charts/full-emoji-list.html
# In the emoji table extract line by line the UTF-8 Code, the emoji itself and the name of the emoji
# In this order (Emoji, Emoji Name, ASCII code)
import requests
from bs4 import BeautifulSoup

URL = 'https://unicode.org/emoji/charts/full-emoji-list.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

# Do a while true loop, and find the parent of the node which the class is rchars, and the content of that node is a number from 1 till none is found
# Once i find the parent element, get the Emoji, Emoji Name, and ASCII Code, put them in a string with a linebreak on the end
# Once i've gone through every node, pipe the output into a file

res = soup.find_all("td", class_="rchars")

for em in res:
    parent = em.find_parent()
    print(parent.find('td', class_="code").find('a').contents)
    print(parent.find('td', class_="chars").contents)
    print(parent.find('td', class_="name").contents)
    break
