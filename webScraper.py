import requests
from bs4 import BeautifulSoup
import re

# HTML get request da página dos emojis
EMOJI_URL = 'https://unicode.org/emoji/charts/full-emoji-list.html'
page = requests.get(EMOJI_URL)

# Conversão para BeautifulSoup para poder efetuar pesquisas nos elementos da página
soup = BeautifulSoup(page.content, 'html.parser')

# Implementação da estrutura de pesquisa para obter Emoji, nome do emoji (em inglês devido ao site), e o seu código unicode
response = soup.find_all("td", class_="rchars")

with open("./emojis", "w") as listaEmojis:
    for em in response:
        parent = em.find_parent()

        # Emoji
        listaEmojis.write(parent.find(
            'td', class_="chars").contents[0] + " ")

        # Emoji Name
        listaEmojis.write(parent.find(
            'td', class_="name").contents[0].title() + " ")

        # Emoji ASCII
        listaEmojis.write(parent.find('td', class_="code").find(
            'a').contents[0] + "\n")

# Programa completo
input("[Scraping completado]")
