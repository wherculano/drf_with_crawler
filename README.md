## Teste de Crawling e integração com API feita em DRF

Scraping feito no site [webcraper.io](https://webscraper.io/) para treinamento de scrping/crawling.

Pós raspagem de dados, os mesmos são salvos em uma API feita em Django Rest Framework.    

- Para rodar o projeto é necessário ter o **pipenv** instalado:    
    ``` 
    $ pip install pipenv
    ```

- Para instalar as dependências do projeto, basta rodar:    
    ``` 
    $ pipenv install
    ```

- Faça as migrações:
    ```    
    $ pipenv run python manage.py migrate 
    ```

- Criar o super usuário, digitando as informações solicitadas:
    ``` 
    $ pipenv run python manage.py createsuperuser 
    ```
- Criar o arquivo **.env** na raíz do projeto com o seguinte conteudo:
    ```
    SECRE_KEY=<Sua Chave Secreta>
    ```


- Subir o server:
    ``` 
    $ pipenv run python manage.py runserver
    ```    
  
O endpoint que irá ativar o crawler é:
``` 
localhost:8000/buscar/<modelo a ser procurado>/
```

Assim que o crawler concluir a busca, a página será redirecionada para    
    ``` 
    localhost:8000/notebooks/
    ```    
Mostrando de forma ordenada por valor (do maior para o menor) os notebooks que foram coletados.   
    
<br>

**Obs.:** O crawler está utilizando o driver **geckodriver** para instanciar o navegador Firefox.
Caso você não o tenha, será necesário baixa-lo [neste link](https://github.com/mozilla/geckodriver/releases).