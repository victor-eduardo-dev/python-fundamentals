"""
Receber do usuário o valor de sua altura.
Receber do usuário o valor do seu peso.
Fazer o cáculo do imc.
Exibir o índice do imc na tela, sem a classificação.
"""
# --- FUNÇÕES ---
def get_user_entry(msg):
    value = float(input(msg).replace(',', '.'))
    return value

# --- CONSTANTES ---
SEP_COUNT = 34

# --- PROGRAMA PRINCIPAL ---
# 1. Criar um pequeno título.
title = 'Calculadora de IMC 1.0'
print('-' * SEP_COUNT)
print(f'{title:-^{SEP_COUNT}}')
print('-' * SEP_COUNT)

# 2. Receber os dados do usuário.
height = get_user_entry("Digite sua altura(m): ")
weight = get_user_entry("Digite seu peso(Kg): ")

# 3. Calcular o imc.
bmi = weight / (height ** 2)

# 4. Exibir o índice.
print('-' * SEP_COUNT)
print(f'Seu IMC é: {bmi:.1f}')
print('-' * SEP_COUNT)
