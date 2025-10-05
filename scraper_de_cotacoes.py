from time import sleep
import requests
from bs4 import BeautifulSoup

def raspar_dados_acao():
    
    urls = ["https://conteudos.xpi.com.br/acoes/irbr3/",
            "https://coinmarketcap.com/pt-br/currencies/bitcoin/",
            "https://coinmarketcap.com/pt-br/currencies/ethereum/",
            "https://coinmarketcap.com/pt-br/currencies/solana/",
            "https://coinmarketcap.com/pt-br/currencies/chiliz/"]
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en;q=0.6',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
    }
    
    try:
        response = requests.get(urls[0], headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"Erro: Status code {response.status_code}")
            return
        
        soup_irb = BeautifulSoup(response.content, 'html.parser')
        lista_irb = soup_irb.find('ul', id='lista-dados-prod')
        
        # Extrair os dados
        print("Dados da ação IRBR3:")
        print("-" * 50)
        
        for row in lista_irb.find_all('li'):
            texto = row.get_text(strip=True)
            if texto:  # Só mostrar se tiver texto
                print(f"• {texto}")
        
        sleep(1)
        #scraper para bitcoin
        response = requests.get(urls[1], headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Erro: Status code {response.status_code}")
            return

        soup_btc = BeautifulSoup(response.content, 'html.parser')
        span = soup_btc.find('span', class_='sc-65e7f566-0 esyGGG base-text')

        if span:
            preco_btc = span.get_text(strip=True) 
            print("-" * 50)
            print(f"Preço do Bitcoin: {preco_btc}")
        else: "Preço não encontrado"

        sleep(1)
        #scraper para ethereum
        response = requests.get(urls[2], headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Erro: Status code {response.status_code}")
            return

        soup_eth = BeautifulSoup(response.content, 'html.parser')
        span = soup_eth.find('span', class_='sc-65e7f566-0 esyGGG base-text')

        if span:
            preco_eth = span.get_text(strip=True) 
            print("-" * 50)
            print(f"Preço do Ethereum: {preco_eth}")
        else: "Preço não encontrado"     

        sleep(1)
        #scraper para solana
        response = requests.get(urls[3], headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Erro: Status code {response.status_code}")
            return

        soup_sol = BeautifulSoup(response.content, 'html.parser')
        span = soup_sol.find('span', class_='sc-65e7f566-0 WXGwg base-text')

        if span:
            preco_sol = span.get_text(strip=True) 
            print("-" * 50)
            print(f"Preço do Solana: {preco_sol}")
        else: "Preço não encontrado"

        sleep(1)
        #scraper para chiliz
        response = requests.get(urls[4], headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"Erro: Status code {response.status_code}")
            return

        soup_chz = BeautifulSoup(response.content, 'html.parser')
        span = soup_chz.find('span', class_='sc-65e7f566-0 WXGwg base-text')

        if span:
            preco_chz = span.get_text(strip=True) 
            print("-" * 50)
            print(f"Preço do Chiliz: {preco_chz}")
        else: "Preço não encontrado"
                
    except requests.Timeout:
        print("Timeout: O site demorou muito para responder")
    except requests.RequestException as e:
        print(f"Erro de conexão: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    raspar_dados_acao()
    