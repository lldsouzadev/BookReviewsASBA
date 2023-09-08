import pandas as pd

# Este Script Recebe um arquivo com um texto tabulado
# Proveniente dos Script PosAdjContador.py ou BaseLineContador.py
# mas também pode receber os arquivos: 
# e remove todas as linhas que não sejam Aspectos

# Lê o arquivo .txt e o passa para um dataframe
df = pd.read_csv('Arquivo_Entrada.csv', sep='\t', header=None, encoding='utf-8', usecols=[0, 1, 2, 3])
df.columns = ['palavra', 'lema', 'classe', 'polaridade']

# Deleta todas as linhas onde 'word' não for um dos valores especificados
words = ['livro', 'adaptação', 'autor', 'critica', 'edição', 'estilo', 'história', 'leitor', 'leitura', 'linguagem', 'passagens', 'sinopse', 'tema', 'tradução', 'cenário', 'detalhes', 'escrita', 'final', 'início', 'narrador', 'personagem']
df = df[df['palavra'].isin(words)]

# Salva o resultado em um novo arquivo .txt com codificação utf-8 e tabulado com tab
#TreeTaggerSentiPosAdjD, TreeTaggerOntoPosAdjD, TreeTaggerLIWCPosAdjD, TreeTaggerOPPosAdjD
df.to_csv('Arquivo_Saida.txt', sep='\t', index=False, header=False, encoding='utf-8')