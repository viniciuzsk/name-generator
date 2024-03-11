import xlsxwriter
import random

# import geradornomes




# escolha = input(print("GERAR NOMES \n -------------------- \n 1 - Prefixo Aleatório\n 2 - Prefixo Não Aleatório"))





workbook = xlsxwriter.Workbook('hello.xlsx')
worksheet = workbook.add_worksheet()

# Listas de exemplos de prefixos e elementos fonéticos
prefixos = ['Cyber', 'Cloud', 'Quantum', 'Virtual', 'Crypto', 'AI', 'Logic', 'Code', 'Digital', 'Stream', 'Sys', 'Dev', 'Net', 'Web', 'Techie', 'Bit', 'Data', 'InfoTech', 'Smart', 'Auto','Nano', 'Mega', 'Ultra', 'Inter', 'Hyper', 'Geo', 'Omni','Meta', 'Alpha' ,'Beta', 'Gamma', 'Delta']
elementos_foneticos = ['sync', 'max', 'tech', 'netic', 'gen', 'nex', 'cube', 'flow', 'grid', 'sphere', 'logic', 'matic', 'node', 'base', 'space', 'frame', 'band', 'cell', 'globe', 'drive','port','cast','graph','wave','form','craft','link','mesh','flex','pulse','vault','breeze']

# Função para gerar nomes
def gerar_nomes(qtd_nomes, prefixos, elementos_foneticos):
    nomes_gerados = set()  # Usamos um set para evitar repetições

    while len(nomes_gerados) < qtd_nomes:
        prefixo = random.choice(prefixos)
        elemento_fonetico = random.choice(elementos_foneticos)
        nome = prefixo + elemento_fonetico
        nomes_gerados.add(nome)

    return list(nomes_gerados)

# Perguntando ao usuário quantos nomes ele deseja gerar
qtd_nomes = int(input("Quantos nomes você deseja gerar? "))
qtd_nomes += 1

# Gerando e exibindo os nomes
nomes = gerar_nomes(qtd_nomes, prefixos, elementos_foneticos)

arquivo = open("arquivo.txt", "w");
for i in range(1, qtd_nomes):
   arquivo.write(nomes[i] + "\n");
   worksheet.write(f"A{i}",nomes[i])
workbook.close()





