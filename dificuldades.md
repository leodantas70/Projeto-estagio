## Desafio-Estágio

---

### Proposta:

- Desenvolver uma função que receba uma data e retorne um MD5 do pdf baixado no site do tribunal

---

#### Métodos utilizados para tentativa de captura de dados

Primeiramente tentei com simples requests e nao obtive a informação necessária.
Pude identificar que dentro do url passado carregavam outro url, após identificar
qual era esse outro url onde só havia os diários e busca do mesmo comecei trabalhar
em cima dele, ele usa javascript para carregar os diários e estou com problema em
capturar as informações desse diário, com o tempo eu consegui filtrar ainda mais
a informação dos diários mas para acessar ela eu primeiro preciso acessar o site anterior,
meio que uma forma de autorização, penso que pelo python se eu conseguisse fazer
com que ele acessasse primeiramente a página de autorização para depois acessar
essa página do diário eu conseguiria as informações necessária, mas não consegui fazer.

    url = "http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/diarioInSession.do?action=buscarDiarios&voDiarioSearch.listState.index=1"
    r = requests.get(url)
    print (r.status_code)
    >>>404
    url = "http://inter03.tse.jus.br/sadJudDiarioDeJusticaConsulta/"
    r = requests.get(url)
    print (r.status_code)
    >>>200

Outro método seria fazer um crawler funcional mas não estou conseguindo fazer também. 
Estou lendo sobre crawler e pretendo usar o módulo selenium para tentar fazer
mas estou com problema no PATCH do CHROME 
`selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH.`
Consegui arrumar isso mas estava abrindo a página do chrome para puxar as informações
necessárias então comecei a ler sobre Headless. Consegui resolver usando Headless.
Após dias pesquisando eu consegui a autenticação e ir para página que terias as informações do diário,
conseguir obter todos os diários mas após isso pude observar que teria que enviar muitas requisições
e depois salvar as datas dos 2700 diários e acabaria ficando pesado,
como estava muito focado nisso esqueci da aba pesquisa que poderia usar para pesquisar apenas o necessário,
após trabalhar em cima da opção pesquisa pude terminar o código em menos de 30 minutos,
mas só consegui terminar rápido assim pois já havia lido bastante sobre as ferramentas necessárias para o crawler. 

---

### Dificuldade encontradas:

- Não saber o que era Hash MD5
- Dúvida sobre onde pesquisar, se era arquivo local ou se pesquisaria do site
- Os posts encontrados eram 99% em inglês - possuo baixo nível em inglês
- Entendendo como efetuar pesquisa em um site usando python
- Instalar biblioteca requests usando python no windows
- Migração para SO Xubunto 18.04
- Instalação do pip com requests
- Salvei o request da página em txt a fim de identificar as datas mas não consegui até então identificadas
- Consegui comparar palavras digitadas pelo input a fim de identificar se existe no site,
as palavras existem, mas as datas não conseguir fazer o download usando request (aparentemente o site é diferente) eu já havia identificado mas quis ter a certeza.
- Entendendo sobre Scrapy
- instalação Scrapy (instalação diferente do tutorial seguido)
- Usar Github
- Identificação do verdadeiro site
- Utilização do Scrapy para obter informações em javascript
- Instalação PhantonJS
- Instalação Drive Chrome para usar selenium
- Nao abrir o navegador para puxar as informações

---

### Justificativa para o método utilizado

- Hash MD5 retorna valores únicos
- Instalação PIP para buscar em site
- Instalei a biblioteca PIP do windows mas não funcionou, depois alterei o SO afim de ganhar tempo
- Usando o módulo request para buscar conteúdo do site
- Usei o módulo request para salvar a página em txt a fim de identificar se estavam sendo salvo as datas de publicação de cada caderno
- Usei o módulo re para identificar se meu input havia dentro dos dados baixados com módulo request
- Como o módulo request não havia baixado as datas comecei a ler sobre o crawler (scrapy)
- Olhando que tem uma forma do crawler baixar informações em java comecei a tentar mas ainda não consegui
- Visando a dificuldade e olhando atento aos pesos para o estágio decidi arrumar
aos 3 primeiros requisitos até voltar a pesquisar sobre crawler
- Após voltar pesquisa sobre crawler descobrir o método selenium para colher as informações
necessárias e me deparei que precisaria abrir o navegador para isso
então pesquisei um método para nao abrir o navegador para isso
- Baixei as informações de todos os diários para comparar com o input mas ao final do código
vi que não era viável pois haveria muitas requisições a ser enviado então usei o campo pesquisa para obter a data que eu quero.

---

### Considerações finais

Após dias estudando, encontrei um jeito simples e rápido de finalizar o projeto

Embora a falta de experiência com a linguagem python, git, relatórios, documentação, testes necessários, versionamento, etc.
Procurei dar o máximo possível para entregar o código com o programa funcionando perfeitamente.
Agradeço a equipe pelo desafio proposto e mesmo não sendo selecionado fico feliz em participar do processo seletivo.

---

### Fonte de pesquisa

- https://pt.wikipedia.org/wiki/MD5
- https://docs.python.org/2/library/md5.html
- https://pythonhelp.wordpress.com/tag/hash/
- https://docs.python.org/3/library/hashlib.html
- https://stackoverflow.com/questions/30536946/how-to-install-requests-module-in-python-3-4-version-on-windows
- https://docs.python.org/3/library/urllib.request.html
- http://docs.python-requests.org/en/v2.7.0/user/install/
- https://stackoverflow.com/questions/24264892/unicodeencodeerror-ascii-codec-cant-encode-character-u-u201c-in-position-3
- https://www.digitalocean.com/community/tutorials/como-fazer-crawling-em-uma-pagina-web-com-scrapy-e-python-3-pt
- https://pythonhelp.wordpress.com/2016/10/22/extraindo-dados-de-paginas-baseadas-em-javascript-com-scrapy/
- https://gist.github.com/julionc/7476620 
- https://imasters.com.br/back-end/como-fazer-web-scraping-com-python
- https://sites.google.com/a/chromium.org/chromedriver/downloads
- https://stackoverflow.com/questions/40437226/selenium-wont-work-with-firefox-or-chrome/40437690
- https://sites.google.com/a/chromium.org/chromedriver/getting-started
- https://stackoverflow.com/questions/54035436/headless-is-not-an-option-in-chrome-webdriver-for-selenium-python
- https://selenium-python.readthedocs.io/locating-elements.html
- http://www.seleniumqref.com/api/python/element_get/Python_find_element_by_class_name.html
