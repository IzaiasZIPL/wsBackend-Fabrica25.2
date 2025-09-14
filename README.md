
---

# Biblioteca – Sistema de Gerenciamento de Livros e Estudantes

Este projeto é um **sistema de biblioteca** desenvolvido em **Django**, que permite gerenciar livros e estudantes de forma simples e eficiente.
Ele integra a **API Open Library**, possibilitando preencher automaticamente as informações de livros a partir do ISBN, e utiliza um banco de dados **PostgreSQL hospedado no Railway**.

---

## 📑 Índice

1. [✨ Funcionalidades](#-funcionalidades)
2. [📂 Estrutura do Projeto](#-estrutura-do-projeto)
3. [🚀 Como Rodar o Projeto](#-como-rodar-o-projeto)
   3.1 [Pré-requisitos](#1️⃣-pré-requisitos)
   3.2 [Passo a Passo](#2️⃣-passo-a-passo)
4. [🛠 Tecnologias Utilizadas](#-tecnologias-utilizadas)
5. [⚙️ Configuração do Banco de Dados (Railway)](#️-configuração-do-banco-de-dados-railway)
6. [📌 Boas Práticas e Observações](#-boas-práticas-e-observações)
7. [🧪 Testes](#-testes)
8. [📜 Licença](#-licença)

---

## ✨ Funcionalidades

### 📚 Livros

* Cadastro, listagem, edição e exclusão
* Campos: **título, ISBN, autor, editora, descrição/assunto, número de páginas**
* Preenchimento automático de informações via [Open Library](https://openlibrary.org/dev/docs/api/books) (ISBN)

### 👩‍🎓 Estudantes

* Cadastro, listagem, edição e exclusão
* Campos: **nome, data de nascimento, telefone, e-mail**
* Associação de livro emprestado ao estudante (**OneToOne**)

### 🌐 Interface Web Responsiva

* Templates organizados e estilizados (compatíveis com **Bootstrap**)

### 🔗 Integração Externa

* Consumo da **API Open Library** para buscar informações de livros dinamicamente

---

## 📂 Estrutura do Projeto

```
biblioteca/
├── app_biblioteca/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── tests.py
│   ├── migrations/
│   └── templates/
│       └── app_biblioteca/
│           ├── livros/
│           │   ├── cadastrar_livros.html
│           │   └── listar_livros.html
│           └── estudantes/
│               ├── cadastrar_estudantes.html
│               └── listar_estudantes.html
├── biblioteca/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── requirements.txt
└── README.md
```

> 💡 O banco de dados está configurado para **PostgreSQL** via Railway (em produção), mas pode ser ajustado para SQLite em desenvolvimento.

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Pré-requisitos

* [Python 3.10+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [Git](https://git-scm.com/)
* Conta no [Railway](https://railway.app/) (opcional, caso queira usar o banco online)

---

### 2️⃣ Passo a Passo

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/biblioteca.git
   cd biblioteca
   ```

2. **Crie e ative um ambiente virtual**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**

   Crie um arquivo `.env` na raiz do projeto com:

   ```env
   DEBUG=True
   SECRET_KEY=sua_chave_secreta
   DATABASE_URL=postgresql://usuario:senha@host:porta/nome_do_banco
   ```

5. **Execute as migrações**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superusuário (opcional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor**

   ```bash
   python manage.py runserver
   ```

8. **Acesse no navegador**

   ```
   http://127.0.0.1:8000/app_biblioteca/home
   ```

---

## 🛠 Tecnologias Utilizadas

* [Django](https://www.djangoproject.com/) – Framework web em Python
* [Open Library API](https://openlibrary.org/dev/docs/api/books) – Consulta de livros via ISBN
* [PostgreSQL (Railway)](https://railway.app/) – Banco de dados em nuvem
* [Bootstrap](https://getbootstrap.com/) – Layout responsivo e estilização
* [Requests](https://pypi.org/project/requests/) – Consumo de API

---

## ⚙️ Configuração do Banco de Dados (Railway)

1. Crie um projeto no [Railway](https://railway.app/).
2. Adicione um banco **PostgreSQL**.
3. Copie a **connection string** gerada.
4. Configure a variável `DATABASE_URL` no seu arquivo `.env`.
5. Ajuste o `settings.py` para ler essa URL com `dj-database-url` ou `os.environ`.

---

## 📌 Boas Práticas e Observações

* Mantenha `DEBUG=False` em produção.

* Nunca suba suas **chaves secretas** ou `.env` para o repositório.

* Adicione ao `.gitignore`:

  ```
  venv/
  __pycache__/
  *.pyc
  .env
  ```

* O projeto pode ser adaptado para rodar com SQLite em ambiente local, facilitando testes rápidos.

---

## 🧪 Testes

Execute os testes automatizados:

```bash
python manage.py test
```

---

## 📜 Licença

Este projeto foi desenvolvido para fins **educacionais e de demonstração**.
Sinta-se livre para utilizar, melhorar e compartilhar.

---


