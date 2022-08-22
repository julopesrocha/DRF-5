# Django Rest Framework 05 | Aprofundando em testes e documentação
O objetivo desta formação é a cada curso consolidar novos conhecimentos adquiridos na construção 
de uma API com Django 3

## Índice
* [Objetivo](#objetivo)
* [Roteiro](#roteiro)
* [Informações sobre o hardware](#informações-sobre-o-hardware)
* [Como rodar o programa](#como-rodar-o-programa)

## Objetivo
:target: conhecer e aplicar teses e documentar a API em Django 3

## Roteiro
1. Aprender a escrever testes automatizados nos modelos, serializers e outras partes de sua aplicação
2. Entender a importância dos testes no desenvolvimento de software
3. Saiber como integrar o Swagger para gerar a documentação de sua API
4. Conheçer uma forma de carregar dados JSON no banco de dados, integrando os modelos
5. Descubrir como realizar diferentes testes no Postman

## Informações sobre o hardware
- Distro: Ubuntu 20.04.4 LTS
- Nome do Modelo: Intel(R) Core(TM) i3-8145U CPU @ 2.10GHz
- Arquitetura: x86_64

## Como rodar o programa
:thinking: Compila e executa o programa através dos comandos:

- O Django pode ser instalado através do comando:

```
pip install Django==3.1.5
```

- Para sistemas MacOS ou Linux:
```
$ source venv/bin/activate
```

- Para sistema Windows:
```
$ venv\Scripts\activate.bat
```

- Após ativação, faça a instalação dos módulos necessários com o seguinte comando:
```
pip install -r requirements.txt
```

- Execute as migrações dos modelos:
```
$ python manage.py migrate
```

- Suba o servidor
```
$ python manage.py runserver
```