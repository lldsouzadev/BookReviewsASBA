from bs4 import BeautifulSoup

# Este Script Recebe um arquivo com um arquivo HTML
# Remove as tags HTML e transforma em um arquivo .txt
# Removendo também as linhas em branco, e linhas iniciadas em "Resenha:", "Livro:" e "Nota:"
# Arquivos para passar aqui estão em \ReLi_Experiments-master\ReLi_Experiments-master\ReLiVisualization\ReLiWeb
# ReLi-Saramago.html, ReLi-Sheldon.html

def transform_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    for br in soup.find_all('br'):
        br.replace_with('\n')
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in soup.text.split('\n'):
            if not any(line.startswith(x) for x in ['Resenha:', 'Livro:', 'Nota:']):
                line = line.strip()
                if line:
                    f.write(line.lower() + '\n')

transform_file('Arquivo_Entrada.html', 'Arquivo_Saida.txt')

# Após este arquivo, passar os arquivos nos taggers.