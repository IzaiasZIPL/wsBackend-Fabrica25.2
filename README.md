
---

# Biblioteca – Sistema de Gerenciamento de Livros e Estudantes

Este projeto é um sistema de biblioteca desenvolvido em **Django**, que permite o gerenciamento completo de livros e estudantes, além de integração com a API **Open Library** para preenchimento automático de informações de livros por ISBN.

---

## 📑 Índice

1. [Funcionalidades](#-funcionalidades)
2. [Estrutura do Projeto](#-estrutura-do-projeto)
3. [Como Rodar o Projeto](#-como-rodar-o-projeto)

   * [Pré-requisitos](#1️⃣-pré-requisitos)
   * [Passo a Passo](#2️⃣-passo-a-passo)
4. [Tecnologias Utilizadas](#-tecnologias-utilizadas)
5. [Observações](#-observações)
6. [Testes](#-testes)
7. [Licença](#-licença)

---

## ✨ Funcionalidades

* **Livros**

  * Cadastro, listagem, edição e exclusão
  * Campos: título, ISBN, autor, editora, descrição/assunto, número de páginas
  * Preenchimento automático de dados via Open Library (ISBN)

* **Estudantes**

  * Cadastro, listagem, edição e exclusão
  * Campos: nome, data de nascimento, telefone, e-mail
  * Associação de livro emprestado ao estudante (OneToOne)

* **Interface Web Responsiva**

  * Templates organizados e estilizados (compatíveis com Bootstrap)

* **Integração com API Externa**

  * Consumo da [Open Library](https://openlibrary.org/dev/docs/api/books) para buscar informações de livros dinamicamente

---

## 📂 Estrutura do Projeto

```
biblioteca/
├── app_biblioteca/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
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
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🚀 Como Rodar o Projeto

### 1️⃣ Pré-requisitos

* [Python 3.10+](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/) instalado
* [Git](https://git-scm.com/) (opcional, para clonar o repositório)

---

### 2️⃣ Passo a Passo

1. **Clone o repositório**

   ```bash
   git clone https://github.com/seu-usuario/biblioteca.git
   cd biblioteca
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional, para acessar o admin do Django)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor**

   ```bash
   python manage.py runserver
   ```

7. **Acesse no navegador**

   ```
   http://127.0.0.1:8000/app_biblioteca/
   ```

---

## 🛠 Tecnologias Utilizadas

* [Django](https://www.djangoproject.com/) – Framework web em Python
* [Open Library API](https://openlibrary.org/dev/docs/api/books) – Consumo de dados de livros via ISBN
* [SQLite](https://www.sqlite.org/) – Banco de dados padrão
* [Bootstrap](https://getbootstrap.com/) – Estilização e layout responsivo

---

## 📌 Observações

* O projeto está configurado para ambiente de desenvolvimento (`DEBUG=True`).
* O banco de dados padrão é o **SQLite** (`db.sqlite3`).
* O arquivo `.gitignore` deve conter:

  * `venv/`
  * `__pycache__/`
  * `*.pyc`
  * `db.sqlite3`
  * `.env` (se houver variáveis de ambiente)

---

## 🧪 Testes

Para executar os testes automatizados:

```bash
python manage.py test
```

---

## 📜 Licença

Este projeto foi desenvolvido para fins **educacionais e de demonstração**.
Sinta-se livre para utilizar, melhorar e compartilhar.

---

