import requests
from bs4 import BeautifulSoup

urls = ['https://www.uol.com.br/', 'https://www.cnnbrasil.com.br/']

response = requests.get(urls[0])
html_content = response.content
soup_uol = BeautifulSoup(html_content, 'html.parser')

response = requests.get(urls[1])
html_content = response.content
soup_cnn = BeautifulSoup(html_content, 'html.parser')

h3_uol = soup_uol.find_all(
    name='h3', 
    attrs={'class': 'title__element headlineMain__title'})[0]

h2_cnn = soup_cnn.find_all(
    name='h2', 
    attrs={'class': 'font-bold flex group-has-[.featured-media]:md:text-3xl md:text-4xl text-2xl w-11/12 md:w-full'})[0]

print('CAPAS DOS PRINCIPAIS SITES DE NOTÍCIAS DO BRASIL\n')
print(f'#Capa do Uol --> ({h3_uol.text.strip()})\n')
print(f'#Capa da CNN --> ({h2_cnn.text.strip()})\n')