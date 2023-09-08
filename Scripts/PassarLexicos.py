import pandas as pd
import re

# Este arquivo recebe os arquivos provenientes dos taggers
# Para alterar o arquivo utilizado, trocar a variavel ao final do script
# Este script também recebe os arquivos de lexico_v3.0, LIWC_UTF8, OntoPT e SentiLex-lem-PT02

# Lendo o arquivo de estrutura tabulada
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Descomente abaixo para usar arquivos do TreeTagger
    data = [line.strip().split('\t') for line in lines]
    resenha = pd.DataFrame(data, columns=['Palavra', 'Classe', 'Lema'])
    # Descomente abaixo para usar arquivos do Freeling
    # data = [line.strip().split(' ')[:4] for line in lines]
    # resenha = pd.DataFrame(data, columns=['Palavra', 'Lema', 'Classe', 'Confianca'])
    # Descomente abaixo para usar arquivos do Citius
    # data = [line.strip().split(' ') for line in lines]
    # resenha = pd.DataFrame(data, columns=['Palavra', 'Lema', 'Classe'])

    # Lendo o arquivo TXT com lexico_v3.0
    with open(r'lexico_v3.0.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = [line.strip().split(',') for line in lines]
    OPLex = pd.DataFrame(data, columns=['Palavra', 'Classe', 'Polaridade', 'Tipo'])

    # Lendo o arquivo TXT com LIWC_UTF8
    with open(r'LIWC_UTF8.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = [line.strip().split(',') for line in lines]
    LIWCLex = pd.DataFrame(data, columns=['Palavra', 'Classe', 'Polaridade'])

    # Lendo o arquivo TXT com OntoPT
    with open(r'OntoPT.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = [line.strip().split(',') for line in lines]
    OntoLex = pd.DataFrame(data, columns=['Palavra', 'Classe', 'Polaridade'])

    # Lendo o arquivo TXT com SentiLex
    with open(r'SentiLex-lem-PT02.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = [re.split('[.;]', line.strip()) for line in lines]
    SentiLex = pd.DataFrame(data, columns=['Palavra', 'Classe', 'Tag', 'Polaridade', 'Tipo'])

    # Comparando e adicionando a polaridade ao dataframe 'resenha'

    resenha['Polaridade'] = None  # Criando a coluna inicialmente com valores nulos
    resenha['PolOP'] = None
    resenha['PolLIWC'] = None
    resenha['PolOnto'] = None
    resenha['PolSenti'] = None
    
    # Substiui os valores 'None' em "Polaridade" com o valor 2 (para representar o none)
    resenha['Polaridade'].fillna(0, inplace=True)
    resenha['PolOP'].fillna(0, inplace=True)
    resenha['PolLIWC'].fillna(0, inplace=True)
    resenha['PolOnto'].fillna(0, inplace=True)
    resenha['PolSenti'].fillna(0, inplace=True)
    

    for index, row in resenha.iterrows():
        palavra = row['Palavra']
        matching_entry = OPLex[OPLex['Palavra'] == palavra]

        if not matching_entry.empty:
            polaridade = matching_entry.iloc[0]['Polaridade']
            resenha.at[index, 'PolOP'] = polaridade

    # Converte a colunas de "polaridade para inteiros"
    resenha['Polaridade'] = resenha['Polaridade'].astype(int)
    resenha['PolOP'] = resenha['PolOP'].astype(int)
    resenha['PolLIWC'] = resenha['PolLIWC'].astype(int)
    resenha['PolOnto'] = resenha['PolOnto'].astype(int)
    resenha['PolSenti'] = resenha['PolSenti'].astype(int)

    # Comparando e adicionando polaridade do LIWCLex no dataframe "resenha"
    for index, row in resenha.iterrows():
        palavra = row['Palavra']
        matching_entry = LIWCLex[LIWCLex['Palavra'] == palavra]
        
        if not matching_entry.empty:
            polaridade_liwc = int(matching_entry.iloc[0]['Polaridade'])
            resenha.at[index, 'PolLIWC'] = polaridade_liwc

    # Comparando e adicionando polaridade do OntoLex no dataframe "resenha"
    for index, row in resenha.iterrows():
        palavra = row['Palavra']
        matching_entry = OntoLex[OntoLex['Palavra'] == palavra]
        
        if not matching_entry.empty:
            polaridade_onto = int(matching_entry.iloc[0]['Polaridade'])
            resenha.at[index, 'PolOnto'] += polaridade_onto

    # Comparando e adicionando polaridade do SentiLex no dataframe "resenha"
    for index, row in resenha.iterrows():
        palavra = row['Palavra']
        matching_entry = SentiLex[SentiLex['Palavra'] == palavra]
        
        if not matching_entry.empty:
            polaridade_sentilex = matching_entry.iloc[0]['Polaridade']
            if polaridade_sentilex == "POL:N0=1":
                resenha.at[index, 'PolSenti'] = 1
            elif polaridade_sentilex == "POL:N0=-1":
                resenha.at[index, 'PolSenti'] = -1      

    # Itera sobre a coluna "Polaridade" e ajusta os valores
    for index, row in resenha.iterrows():
        polaridade = row['PolSenti'] + row['PolOP'] + row['PolLIWC'] + row['PolOnto']
        resenha.at[index, 'Polaridade'] = polaridade 
        if polaridade > 0:
           resenha.at[index, 'Polaridade'] = 1
        elif polaridade < 0:
           resenha.at[index, 'Polaridade'] = -1
        else:
           resenha.at[index, 'Polaridade'] = 0

    
    resenha.to_csv(output_file, sep='\t', index=False, header=False, encoding='utf-8')

#Referencie o nome do arquivo de entrada e saida de acordo com o arquivo do tagger sendo utilizado
input_file = 'Arquivo_Entrada.txt' 
output_file = 'Arquivo_Saida.txt'  
process_file(input_file, output_file)