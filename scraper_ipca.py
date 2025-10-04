import requests
from bs4 import BeautifulSoup
import sqlite3

url = "https://www.idealsoftwares.com.br/indices/ipca_ibge.html"
response = requests.get(url)
response.raise_for_status()
        
soup = BeautifulSoup(response.content, 'html.parser')


table = soup.find_all(
    name='table', 
    attrs={'class': 'table table-bordered table-striped text-center'})[0]

ipca_data = []

for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if cols:
        month_year = cols[0].text.strip()[3:]
        value = cols[1].text.strip().replace(',', '').replace(' ', '').replace('\n', '')
        if value:
            month, year =  month_year.split('/')
            ipca_data.append((float(value), month, int(year)))

print(ipca_data)
con = sqlite3.connect('ipca_data.db')
cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ipca (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        value REAL,
        month TEXT,
        year INTEGER,
        UNIQUE(month, year) 
    )
''')

for data in ipca_data:
    value, month, year = data
    cursor.execute('''
        INSERT OR IGNORE INTO ipca (value, month, year)
        VALUES (?, ?, ?)
    ''', (value, month, year))  

con.commit()
con.close()

print("Dados históricos do IPCA inseridos com sucesso no banco de dados.") 