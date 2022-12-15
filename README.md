# Executando o projeto

1. Instalar as dependências: na pasta raiz execute `pip install requirements.txt`
2. Crie um banco de dados chamado `db_donations` em um servidor MySQL
3. Crie as tabelas necessárias para o projeto: os aquivos `.sql` encontram-se na pasta `src/resources/db`
4. Entre na pasta src: `cd src/`
5. Abra o arquivo `run.sh` e preencha as informações do banco de dados e a chave da API do GoogleMaps 
6. Execute o script: `sh run.py`
7. O resultado da execução do programa estará na tabela `tb_addresses`
8. Caso o script apresente algum erro referente a versão do WebDriver, acesse o site [chromedriver](https://chromedriver.chromium.org/home) e faça o download da versão ```Stable``` para o seu sistema operacional
