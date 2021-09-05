#TESTE COM O VALOR DO DÓLAR

import requests
from bs4 import BeautifulSoup
import time

while True:
    acao = input("Qual Ação ou FII você deseja buscar ? QUIT para encerrar ").upper()

    if acao == "QUIT":
        print("Encerrando...")
        time.sleep(2)
        break

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
    page = requests.get(f"https://www.google.com/search?client=firefox-b-d&q={acao}", headers=header)
    soup = BeautifulSoup(page.content,'html.parser')

    atributos = {'class':'g'}
    cotacao_dolar = soup.find_all("span", class_="IsqQVc NprOob XcVN5d wT3VGc")[0]
    print(f"Cotação da {acao} hoje: {cotacao_dolar.text}")


