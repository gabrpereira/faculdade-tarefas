# Projeto de Gerenciamento de Tarefas

Este é um projeto simples de gerenciamento de tarefas desenvolvido com **Django** e **SQLite**. 

O objetivo do projeto é permitir que os usuários organizem suas atividades acadêmicas e pessoais de forma prática.

## Participantes:
Arthur Gabriel Silva Pereira
Samuel da Rocha Santana 

## Funcionalidades

- **Listagem de Tarefas**: Visualização de todas as tarefas cadastradas.
- **Criação de Tarefas**: Adição de novas tarefas com título.
- **Conclusão de Tarefas**: Marcar tarefas como finalizadas.
- **Exclusão de Tarefas**: Remover tarefas permanentemente do banco de dados.

## Tecnologias Utilizadas

- **Framework**: Django
- **Banco de Dados**: SQLite
- **Estilização**: HTML/CSS (com templates Django)

## Como Executar o Projeto

1. Certifique-se de ter o Python instalado.
2. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```
3. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
4. Acesse o projeto no navegador em: `http://127.0.0.1:8000`

## Estrutura do Projeto

- `setup/`: Configurações principais do projeto Django.
- `app_tarefas/`: Aplicativo contendo a lógica de modelos, visualizações e templates de tarefas.
- `db.sqlite3`: Banco de dados do projeto.
