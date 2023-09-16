<p>Este repositório contém os arquivos e passo a passo necessário para reprodução dos resultados obtidos na monografia apresentada por Leandro Luiz de Souza como Trabalho de Conclusão do Curso da Universidade Federal de Pelotas, para o curso de Engenharia da computação.
</p>

<h2>Recursos externos utilizados:</h2>
<ul>
<li>Corpus ReLi: https://www.linguateca.pt/Repositorio/ReLi/</li>
<li>TreeTagger: https://cis.uni-muenchen.de/~schmid/tools/TreeTagger/</li>
<li>CitiusTagger: https://gramatica.usc.es/pln/tools/CitiusTools.html</li>
<li>FreeLing: https://nlp.lsi.upc.edu/freeling/node/1</li>
</ul>
<h2>Metodologia:</h2>
<p>
A Seguir será explicado o passo a passo para execução dos códigos. Todos os códigos estão com nomes de arquivos de entrada e saida genéricos, o usuário deverá alterar os nomes manualmente de acordo com os arquivos gerados em cada etapa. 
</p>
<h3>1. Pré-processamento dos Arquivos</h3>
<ul>
- Inicialmente, utilizar o script <code>TratamentoInicial.py</code> sobre os arquivos HTML do corpus localizados em <code>\ReLi_Experiments-master\ReLi_Experiments-master\ReLiVisualization\ReLiWeb</code>. Este Script é responsável por realizar a limpeza de tags HTML do arquivo, assim como remover as linhas em branco e linhas iniciadas em <code>Livro:</code>, <code>Resenha:</code> e <code>Nota:</code>. 
<ul>
<p>
O procedimento a seguir pode ser feito com 7 arquivos HMTL ou com apenas 1 arquivo resultante da união dos 7 arquivos iniciais. No caso deste trabalho unificou-se os 7 arquivos de forma manual colando um arquivo abaixo do outro.
</p>
<ul>
- Em seguida, passar os arquivos resultantes pelos POS Taggers. O TreeTagger foi utilizado no Windows 10 Atualização 22H2. O Citius e FreeLing foram utilizados no Ubuntu 22.04.3 LTS.
</ul>
<h3>2. Identificação de Aspecto</h3>
<ul>
<li>Os arquivos provenientes dos Taggers deverão ser passados pelo script <code>PassarLexicos.py</code>, que irá adicionar novas colunas com polaridades auxiliares aos arquivos dos taggers.
</li>
</ul>
<h3>3. Identificação de Polaridade</h3>
<ul>
<li>
Estes arquivos deverão então ser passados pelos scripts <code>BaseLineContador.py</code> ou <code>PosAdjContador.py</code>, alterando internamente no arquivo o arquivo referente ao tagger utilizado e descomentar a linha do que se está usando.
</li>
<li>
O script acima irá gerar arquivos .csv, que deverão ser passados pelo script <code>deletalinhasfinal.py</code>, que é responsável por reduzir o tamanho do arquivo se limitando apenas às linhas que contém os aspectos com sua polaridade classificada no passo anterior.
</li>
<li>
Deverá também utilizar o script <code>ComparadorReLi.py</code>, para executar a mesma tarefa sobre os arquivos contidos em: <code>\ReLi_Experiments-master\ReLi_Experiments-master\ReLi\corpus</code>.
</li>
</ul>

<h3>4. Sumarização</h3>
<ul>
<li>
Por fim, os arquivos provenientes dos scripts <code>deletalinhasfinal.py</code>code> e <code>ComparadorReLi.py</code> deverão ser inseridos como arquivos de entrada no script <code>resultadofinal.py</code>
</li>
</ul>
