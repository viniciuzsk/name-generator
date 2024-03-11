import random

# Listas de consoantes e vogais comuns no português brasileiro
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']

def gerar_palavra_aleatoria(tamanho):
    palavra = ''
    for i in range(tamanho):
        if i % 2 == 0:
            # Adiciona uma consoante em posições pares
            palavra += random.choice(consoantes)
        else:
            # Adiciona uma vogal em posições ímpares
            palavra += random.choice(vogais)
    return palavra

# Exemplo de uso: gerar uma palavra aleatória com 6 caracteres
palavra_aleatoria = gerar_palavra_aleatoria(6)
palavra_aleatoria

print(palavra_aleatoria)
