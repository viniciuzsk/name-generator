# Ajustando o gerador para criar nomes de empresas mais realistas
import random
# Sílabas mais complexas e naturais
silabas_iniciais = ['In', 'Ex', 'Pro', 'Bio', 'Tech', 'Log', 'Net', 'Sys', 'Fin', 'Re', 'Uni', 'Omni', 'Max', 'Trans', 'Ultra']
silabas_meio = ['con', 'men', 'ter', 'ven', 'fin', 'net', 'log', 'dat', 'mat', 'vid', 'rad', 'tec', 'mod', 'nov', 'sol']
silabas_finais = ['ix', 'ia', 'io', 'ic', 'or', 'er', 'ar', 'us', 'um', 'as', 'es', 'os', 'ito', 'ate', 'edo']

def gerar_nome_empresa():
    # Escolhe uma sílaba de cada tipo para formar um nome
    inicio = random.choice(silabas_iniciais)
    meio = random.choice(silabas_meio)
    fim = random.choice(silabas_finais)

    # Combina as sílabas para formar o nome
    nome_empresa = inicio + meio + fim
    return nome_empresa

# Exemplo de uso: gerar um nome de empresa
nome_empresa_aleatorio = gerar_nome_empresa()
nome_empresa_aleatorio



print(nome_empresa_aleatorio)
