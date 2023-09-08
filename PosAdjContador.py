import pandas as pd

# Este Script Recebe um arquivo com um texto tabulado
# Proveniente dos Taggers TreeTagger, CitiusTagger ou FreeLing

# Criação de listas para os 21 termos
livroCont = ["livro", 0, 0, 0]
adaptacaoCont = ["adaptação", 0, 0, 0]
autorCont = ["autor", 0, 0, 0]
criticaCont = ["critica", 0, 0, 0]
edicaoCont = ["edição", 0, 0, 0]
estiloCont = ["estilo", 0, 0, 0]
historiaCont = ["história", 0, 0, 0]
leitorCont = ["leitor", 0, 0, 0]
leituraCont = ["leitura", 0, 0, 0]
linguagemCont = ["linguagem", 0, 0, 0]
passagensCont = ["passagens", 0, 0, 0]
sinopseCont = ["sinopse", 0, 0, 0]
temaCont = ["tema", 0, 0, 0]
traducaoCont = ["tradução", 0, 0, 0]
cenarioCont = ["cenário", 0, 0, 0]
detalhesCont = ["detalhes", 0, 0, 0]
escritaCont = ["escrita", 0, 0, 0]
finalCont = ["final", 0, 0, 0]
inicioCont = ["início", 0, 0, 0]
narradorCont = ["narrador", 0, 0, 0]
personagemCont = ["personagem", 0, 0, 0]

# Para Resultados da Comparação de Taggers!
# Descomente para utilizar o TreeTagger
df = pd.read_csv(r"ArquivoTreeTagger.txt", encoding="utf-8", names=["word", "classe", "lema", "polarity"], usecols=[0,1,2,3], delimiter="\t")
# Descomente para utilizar o FreeLing
# df = pd.read_csv(r"ArquivoFreeLing.txt", encoding="utf-8", names=["word", "lema", "classe", "polarity"], usecols=[0,1,2,3], delimiter="\t")
# Descomente para utilizar o CitiusTagger
# df = pd.read_csv(r"ArquivoCitius.txt", encoding="utf-8", names=["word", "lema", "classe", "polarity"], usecols=[0,1,2,4], delimiter="\t")

# Para Resultados da Comparação de Léxicos!
# Descomente para utilizar o OpLexicon
# df = pd.read_csv(r"ArquivoTreeTagger.txt", encoding="utf-8", names=["word", "classe", "lema", "polarity"], usecols=[0,1,2,4], delimiter="\t")
# Descomente para utilizar o LIWC-PT
# df = pd.read_csv(r"ArquivoTreeTagger.txt", encoding="utf-8", names=["word", "classe", "lema", "polarity"], usecols=[0,1,2,5], delimiter="\t")
# Descomente para utilizar o Onto.PT
# df = pd.read_csv(r"ArquivoTreeTagger.txt", encoding="utf-8", names=["word", "classe", "lema", "polarity"], usecols=[0,1,2,6], delimiter="\t")
# Descomente para utilizar o Onto.PT
# df = pd.read_csv(r"ArquivoTreeTagger.txt", encoding="utf-8", names=["word", "classe", "lema", "polarity"], usecols=[0,1,2,7], delimiter="\t")

df = df.fillna(0)
# Criação de um dicionário para mapear cada termo à sua respectiva lista
termos_dict = {"livro": livroCont,
               "adaptação": adaptacaoCont,
               "autor": autorCont,
               "critica": criticaCont,
               "edição": edicaoCont,
               "estilo": estiloCont,
               "história": historiaCont,
               "leitor": leitorCont,
               "leitura": leituraCont,
               "linguagem": linguagemCont,
               "passagens": passagensCont,
               "sinopse": sinopseCont,
               "tema": temaCont,
               "tradução": traducaoCont,
               "cenário": cenarioCont,
               "detalhes": detalhesCont,
               "escrita": escritaCont,
               "final": finalCont,
               "início": inicioCont,
               "narrador": narradorCont,
               "personagem": personagemCont}

# Percorrer a coluna word
for index, row in df.iterrows():
    word = row["word"]
    if isinstance(word, str):
        word = word.lower()
        if word in termos_dict.keys():
            print('iniciando analise')
            termos_dict[word][1] +=1
            termoCont = termos_dict[word]

            temp_polarity = None
            for i in range(index-1, min(index+4, len(df))):
                if i != index-1 and df.loc[i, "word"] == ".":
                    print('Ponto encontrado')
                    break
                try:
                    if "AQ" in df.loc[i, "classe"]:
                        temp_polarity = df.loc[i,"polarity"]
                        df.loc[index, "polarity"] = temp_polarity
                        break
                except TypeError:
                # handle the exception here
                    print(f'Error at index {i}: {df.loc[i, "classe"]}')

            if temp_polarity is not None:
                for i in range(max(9,index-3), index):
                    if df.loc[i,"word"].lower() == "R":
                        temp_polarity *= -1
                        break

df['polarity'] = df['polarity'].astype(int)
df.to_csv('Arquivo_saida.csv', sep='\t', encoding='utf-8', header=False, index=False)