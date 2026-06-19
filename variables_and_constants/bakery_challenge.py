'''
Sistema simples de padaria.
constante: preço do pão francês(0.50).
Variáveis: quantidade de pães e nome no cliente.
Objetivo: calcular o valor total da compra e exibir uma mensagem amigável.

'''
SEP_VALUE = 48
BREAD_PRICE = 0.50
phrase = 'DESAFIO: CONSTANTES E VARIÁVEIS'
title_challenge = 'Compra de pães na padaria'
quantity_bread = 10
name_client = 'Victor'

total_value = BREAD_PRICE * quantity_bread

print('-' * SEP_VALUE)
print(f'{phrase:-^{SEP_VALUE}}')
print('-' * SEP_VALUE)
print(f'{title_challenge:^{SEP_VALUE}}')
print('-' * SEP_VALUE)
print(f'Boa tarde {name_client},\no total dos seus {quantity_bread} pães é R$ {total_value:.2f}')
print('-' * SEP_VALUE)
