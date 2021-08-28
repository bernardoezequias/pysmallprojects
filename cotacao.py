#PRIMEIRO TESTE COM UMA API

import requests 
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()

cotacao_dolar = cotacoes['USDBRL']
cotacao_euro = cotacoes['EURBRL']
cotacao_btc = cotacoes['BTCBRL']


while True:
    opcao = input('Qual moeda você deseja ver a cotação ? (USD/EU/BTC) ou Encerrar ').upper()

    if opcao == 'ENCERRAR': break
    
    if opcao == 'USD':
        for k, v in cotacao_dolar.items():
            if k == 'varBid': 
                variacao = v
                break
        print(f"A cotação atual do Dólar é: R$ {float(cotacao_dolar['bid']):.2f}")
        print(f"Alta: {float(cotacao_dolar['high'])} \nBaixa: {float(cotacao_dolar['low'])} \nVariação: {float(variacao)}")

    elif opcao == 'EU':
        for k, v in cotacao_euro.items():
            if k == 'varBid': 
                variacao = v
                break
        print(f"A cotação atual do Euro é: R$ {float(cotacao_euro['bid']):.2f}")
        print(f"Alta: {float(cotacao_euro['high'])} \nBaixa: {float(cotacao_euro['low'])} \nVariação: {float(variacao)}")

    elif opcao == 'BTC':
        for k, v in cotacao_btc.items():
            if k == 'varBid': 
                variacao = v
                break
        print(f"A cotação atual do Bitcoin é: R$ {float(cotacao_btc['bid'])}")
        print(f"Alta: {float(cotacao_btc['high'])} \nBaixa: {float(cotacao_btc['low'])} \nVariação: {float(variacao)}")

    else:
        print('Moeda não encontrada, tente novamente.')

    
    
