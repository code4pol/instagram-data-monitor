# Contribuições

## Ferramentas utilizadas

* [python 3.6](https://www.python.org/)
* [pip](https://pypi.python.org/pypi/pip)

## Preparar o ambiente

### Clonar repositório

```
$ git clone git@github.com:unb-cic-esw/instagram-data-monitor.git
```

### Criar virtualenv

```
$ python3 -m venv venv
$ source venv/bin/activate
```

### Instalar dependências

Todas as bibliotecas de que o projeto depende estão listadas no arquivo
[requirements.txt](requirements.txt). Para instalá-las, execute:

```
$ cd instagram-data-monitor
$ source venv/bin/activate
$ pip install -r requirements.txt
```


## Adicionar funcionalidades

Para cada estória a ser resolvida, seguir o seguinte procedimento:

- Clone o repositório
- Prepare o ambiente como foi explicado acima
- Crie uma issue em formato de estória da funcionalidade/bug/etc
- Crie uma branch (local e remoto) sobre o problema a ser resolvido, e.g.:

```
$ git checkout -b dev-subscribers
$ git push origin dev-subscribers
```

- Após resolver a issue, rode os devidos testes (rode mesmo porque seu PR não
  será aceito se seus testes não estiverem passando!)
- Abra um ticket de pull request no github com o sentido (base <- head):

 ```
 unb-cic-esw/instagram-data-monitor/master <- unb-cic-esw/instagram-data-monitor/dev-subscribers
 ```

- Espere o Travis CI executar os testes de integração
- Se todos os testes passarem então peça algum colega do time/organização para aceitar seu PR :rocket:



## Executar os testes

Todos os testes foram desenvolvidos utilizando a biblioteca
[unittest](https://docs.python.org/3/library/unittest.html) nativa do Python.
Para executá-los, a partir da pasta raiz do projeto, execute:

```
$ python -m unittest discover tests
```


## Checar cobertura de código

Para checar a cobertura de código foi utilizado a biblioteca
[coverage](https://coverage.readthedocs.io/en/coverage-4.5.1/).
Para verificar o relatório da cobertura a partir de um determinado arquivo,
execute:

```
$ coverage run -m [modulo do arquivo].[arquivo sem .py] && coverage report -m
```


## Checar estilo de código

Para seguir os padrões PEP8 de código python estamos usando a biblioteca
[pycodestyle](http://pycodestyle.pycqa.org/en/latest/).
Para cada novo módulo adicionado ao projeto é necessário criar um teste para
checar seu estilo de código (ver exemplos em [test_pep8](tests/test_pep8.py)).
Para executar a ferramenta e checar algum código, basta executar:

```
$ pip install pycodestyle
$ pycodestyle [arquivo].py
```
