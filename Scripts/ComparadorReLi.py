import pandas as pd
from io import StringIO

# Este Script Recebe os arquivos de "\ReLi_Experiments-master\ReLi_Experiments-master\ReLi\corpus"

with open('Arquivo_Entrada.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    content = ''.join(line for line in lines if not line.startswith('#') and line.strip())

df = pd.read_csv(StringIO(content), sep='\t', header=None, usecols=[0, 1, 2, 3])
df.columns = ['palavra', 'lema', 'classe', 'polaridade']

# Deleta todas as linhas onde 'palavra' não for um dos valores especificados
words = ['livro', 'adaptação', 'autor', 'critica', 'edição', 'estilo', 'história', 'leitor', 'leitura', 'linguagem', 'passagens', 'sinopse', 'tema', 'tradução', 'cenário', 'detalhes', 'escrita', 'final', 'início', 'narrador', 'personagem']
df = df[df['palavra'].isin(words)]

# Salva o resultado em um novo arquivo .txt com codificação utf-8 e tabulado com tab
#TreeTaggerSentiPosAdjD, TreeTaggerOntoPosAdjD, TreeTaggerLIWCPosAdjD, TreeTaggerOPPosAdjD
df.to_csv('Arquivo_Saida.txt', sep='\t', index=False, header=False, encoding='utf-8')