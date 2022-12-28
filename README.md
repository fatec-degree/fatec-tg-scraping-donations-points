# Donations Points Scraping

Sistema que faz o processo de **Web Scraping** de pontos de coleta de agasalhos para doação. Os dados coletados são tratados e enviados para a [API Donations Points](https://github.com/PedroHPAlmeida/fatec-tg-api-donations-points) para serem consumidos por quaiquer aplicações front-end.

O objetivo destas duas aplicações em conjunto é fazer um "compilado" de pontos de coleta de agasalhos, independente de instituições. Deixando as informações centralizadas em um único lugar e permitindo a fácil consulta.

Atualmente o processo de Web Scraping coleta dados do site do [Exército da Salvação](https://www.exercitodoacoes.org.br/doacoes/pontos-de-coleta/). Futuramente serão introduzidos dados de outros sites.

______
## Tecnologias utilizadas

* Python 3.8 para desenvolvimento da aplicação;
* API do Google Maps para solicitar e salvar os endereços de forma consistente;
* Banco de dados MySQL para salvar os dados extraídos pelo processo de Web Scraping;
* Biblioteca Selenium para fazer o processo de Web Scraping no navegador;
* Biblioteca Beautiful Soup para tratar o HTML;
* Biblioteca Nox para automação de Lint;
* GitHub Actions para CI:
    - Automação de Lint da aplicação;
    - Atualização automática da imagem docker da aplicação no repositório do [DockerHub Repository - Pedro](https://hub.docker.com/repository/docker/pedro6571/points-of-donations).

______
