HP-RPG

Sistema web para criação e gerenciamento de personagens de RPG.

O HP-RPG é um projeto desenvolvido com Python, Flask, HTML e CSS, com o objetivo de criar uma aplicação web para cadastro e gerenciamento de personagens e campanhas de RPG.

O projeto utiliza como referência o universo de Ordem Paranormal, explorando conceitos de fichas de personagem, classes, origens, atributos e regras personalizadas.

Tecnologias utilizadas:

Python: linguagem utilizada no desenvolvimento da aplicação.

Flask: framework responsável pelas rotas e funcionalidades do sistema.

HTML5: estrutura das páginas.

CSS3: estilização e apresentação visual.

SQLite: banco de dados para armazenamento das informações.

Jinja2: integração entre as páginas HTML e o Flask.

Funcionalidades:

Em desenvolvimento

Estrutura inicial da aplicação Flask.

Organização das páginas HTML.

Estrutura inicial de classes e origens.

Sistema de cadastro e autenticação de usuários.

Criação e gerenciamento de personagens.

Sistema de atributos e perícias.

Aplicação automática das regras das origens.

Armazenamento das fichas no banco de dados SQLite.

Gerenciamento de campanhas.

Sistema de personagens:

O projeto utiliza como referência o sistema de RPG Ordem Paranormal.

Entre os elementos previstos para as fichas estão:

Classes e origens: organização das características iniciais dos personagens.

Atributos:

Força

Agilidade

Intelecto

Presença

Vigor

Origens iniciais:

Acadêmico

Agente de Saúde

Artista

Atleta

Operário

Estrutura do projeto

HP-RPG/
│
├── app.py
├── regras_ordem.py
├── hp_rpg.db
│
└── templates/
    ├── index.html
    ├── cadastro.html
    ├── criar_ordem.html
    └── criar_2d6.html

Como executar o projeto

1 - Clone o repositório

git clone URL_DO_REPOSITORIO

2 - Entre na pasta do projeto

cd HP-RPG

3 - Instale o Flask

pip install flask

4 - Execute a aplicação

python app.py

5 - Acesse no navegador

http://127.0.0.1:5000

Objetivo do projeto:

Este projeto tem como objetivo desenvolver conhecimentos em desenvolvimento web, lógica de programação, organização de código, integração com banco de dados e construção de aplicações utilizando Python e Flask.

O HP-RPG também faz parte da construção do meu portfólio de desenvolvimento de software.

Status: em desenvolvimento
