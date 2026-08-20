# Task API

API REST desenvolvida com **Python e FastAPI** para gerenciamento de tarefas.

Este projeto foi desenvolvido como parte do meu processo de aprendizado em desenvolvimento backend, com foco em criação de APIs, validação de dados, operações CRUD e tratamento de erros HTTP.

## 🎯 Objetivo

Criar uma API simples capaz de realizar as principais operações de gerenciamento de tarefas:

* Criar tarefas
* Listar tarefas
* Atualizar tarefas
* Excluir tarefas
* Validar dados recebidos pela API
* Retornar respostas HTTP apropriadas

## 🛠️ Tecnologias

* Python
* FastAPI
* Pydantic
* JSON
* Uvicorn
* Git/GitHub

## 📌 Endpoints

| Método | Endpoint        | Descrição                |
| ------ | --------------- | ------------------------ |
| GET    | `/`             | Verifica o status da API |
| POST   | `/tarefas`      | Cria uma nova tarefa     |
| GET    | `/tarefas`      | Lista as tarefas         |
| PUT    | `/tarefas/{id}` | Atualiza uma tarefa      |
| DELETE | `/tarefas/{id}` | Remove uma tarefa        |

## 🔎 Validação

A API utiliza **Pydantic** para validar os dados recebidos.

Os títulos das tarefas precisam possuir pelo menos 3 caracteres.

Exemplo:

```json
{
  "titulo": "Estudar FastAPI"
}
```

## ⚠️ Estado atual

O projeto está em uma versão inicial de desenvolvimento.

Atualmente, parte das operações utiliza armazenamento em memória e existe uma implementação inicial de persistência utilizando um arquivo JSON.

- ✅ Criar tarefas
- ✅ Listar tarefas
- ✅ Atualizar tarefas
- ✅ Excluir tarefas
- ✅ Validação de dados com Pydantic
- ✅ Tratamento de erros HTTP

## 🚀 Próximos passos

* [x] Corrigir a persistência dos dados
* [ ] Utilizar um banco de dados
* [ ] Separar responsabilidades em diferentes módulos
* [ ] Adicionar testes automatizados
* [ ] Melhorar o tratamento de erros
* [ ] Adicionar autenticação
* [ ] Criar documentação mais detalhada da API

## 📚 Objetivo de aprendizado

Este projeto representa uma das etapas do meu aprendizado em desenvolvimento backend e serviu como base para compreender conceitos de APIs REST utilizando Python e FastAPI.

Projetos posteriores buscam aplicar esses conhecimentos em sistemas mais completos e próximos de problemas reais.

## 👨‍💻 Autor

**Gabriel Carvalho**

Desenvolvedor em formação, interessado em Engenharia de Software, APIs, sistemas e tecnologia aplicada à resolução de problemas reais.
