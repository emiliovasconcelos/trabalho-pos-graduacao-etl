# trabalho-pos-graduacao-etl

Este repositório é um trabalho para a disciplina de "Extração Análise e Gestão de Dados"<br><br>

O projeto contém 4 arquivos:<br>
  amazon.py e americanas.py, que fazem a raspagem de dados nos respectivos ecommerce para o item fralda descartável<br>
  amazon.json e americanas.json, que são o resultado da raspagem

Tratamentos realizados. Para este projeto pegamos os valores de nome e preço dos produtos:<br>
  Para o nome removemos os caracteres especiais e acentuação<br>
  Para o preço na Americanas removemos os caracteres R$, na Amazon tivemos que unir os campos de reais e centavos, pois eles são guardados em elementos diferentes do html<br><br>
  
Dependências: scrapy e unidecode<br><br>

Comandos para executar o projeto<br><br>

pip install scrapy<br>
pip install unidecode<br>
scrapy runspider amazon.py -O amazon.json<br>
scrapy runspider americanas.py -O amazon.json<br><br>

Após a execução os arquivos .json com os valores raspados estarão na pasta do projeto
