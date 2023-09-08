import pandas as pd

# Este Script Recebe um arquivo de deletalinhasfinal.py
# e também um arquivo contendo o Dataframe Original do ReLi

# Lendo o primeiro arquivo .txt e criando o primeiro dataframe
df1 = pd.read_csv('Arquivo_Entrada.txt', sep='\t', header=None, encoding='utf-8')
df1.columns = ['word', 'lema', 'classe', 'polarity']

# Lendo o segundo arquivo .txt e criando o segundo dataframe
df2 = pd.read_csv('Arquivo_.txt', sep='\t', header=None, encoding='utf-8')
df2.columns = ['palavra', 'classe', 'tipo', 'tipo 2', 'polaridade', 'auxiliar']

# Criando as variáveis
livro = ['livro', 0, 0, 0, 0, 0, 0]
adaptacao = ['adaptação', 0, 0, 0, 0, 0, 0]
autor = ['autor', 0, 0, 0, 0, 0, 0]
critica = ['critica', 0, 0, 0, 0, 0, 0]
edicao = ['edição', 0, 0, 0, 0, 0, 0]
estilo = ['estilo', 0, 0, 0, 0, 0, 0]
historia = ['história', 0, 0, 0, 0, 0, 0]
leitor = ['leitor', 0, 0, 0, 0, 0, 0]
leitura = ['leitura', 0, 0, 0, 0, 0, 0]
linguagem = ['linguagem', 0, 0, 0, 0, 0, 0]
passagens = ['passagens', 0, 0, 0, 0, 0, 0]
sinopse = ['sinopse', 0, 0, 0, 0, 0, 0]
tema = ['tema', 0, 0, 0, 0, 0, 0]
traducao = ['tradução', 0, 0, 0, 0, 0, 0]
cenario = ['cenário', 0, 0, 0, 0, 0, 0]
detalhes = ['detalhes', 0, 0, 0, 0, 0, 0]
escrita = ['escrita', 0, 0, 0, 0, 0, 0]
final = ['final', 0, 0, 0, 0, 0, 0]
inicio = ['início', 0, 0, 0, 0, 0, 0]
narrador = ['narrador', 0, 0, 0, 0, 0, 0]
personagem = ['personagem', 0, 0, 0, 0, 0, 0]

# Criando o dicionário
dicionario = {'livro': livro,
            'adaptação': adaptacao,
            'autor': autor,
            'critica': critica,
            'edição': edicao,
            'estilo': estilo,
            'história': historia,
            'leitor': leitor,
            'leitura': leitura,
            'linguagem': linguagem,
            'passagens': passagens,
            'sinopse': sinopse,
            'tema': tema,
            'tradução': traducao,
            'cenário': cenario,
            'detalhes': detalhes,
            'escrita': escrita,
            'final': final,
            'início': inicio,
            'narrador': narrador,
            'personagem': personagem}



#Tentativa3
df1 = df1.assign(polaridade=df2.iloc[:, 4])

polarity_map = {(1, '+'): 1, (1, '-'): 2, (1, 'O'): 2, (-1, '-'): 4, (-1, '+'): 5, (-1, 'O'): 5, (0, '-'): 6, (0, '+'): 3}

for index, row in df1.iterrows():
    if row['word'] in dicionario:
        key = (row['polarity'], row['polaridade'])
        print(f"key = {key}")
        if key in polarity_map:
            print(f"polarity_map[{key}] = {polarity_map[key]}")
            print(f"len(dicionario[{row['word']}]) = {len(dicionario[row['word']])}")
            dicionario[row['word']][polarity_map[key]] += 1


# Escrevendo no arquivo de saída
#TreeTaggerSentiPosAdjFinalD, TreeTaggerOntoPosAdjFinalD, TreeTaggerLIWCPosAdjFinalD, TreeTaggerOPPosAdjFinalD
with open('TreeTaggerSentiPosAdjFinalD.csv', 'w', encoding='utf-8') as f:
    for key in dicionario:
        f.write(f'{key},{dicionario[key][1]},{dicionario[key][2]},{dicionario[key][3]},{dicionario[key][4]},{dicionario[key][5]},{dicionario[key][6]}\n')

