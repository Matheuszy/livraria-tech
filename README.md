# 📚 Livraria Tech — API REST

API backend de uma livraria digital construída com **FastAPI**, **SQLAlchemy** e **PostgreSQL**. O sistema suporta dois tipos de usuários: **administradores** (gerenciam o catálogo) e **clientes** (navegam e fazem pedidos).

---

## 🛠️ Tecnologias

| Tecnologia | Versão |
|---|---|
| Python | 3.x |
| FastAPI | 0.139.2 |
| SQLAlchemy | 2.0.51 |
| PostgreSQL | — |
| Alembic | 1.19.1 |
| Pydantic | 2.13.4 |
| python-jose | 3.5.0 |
| passlib + bcrypt | 1.7.4 / 4.0.1 |
| Uvicorn | 0.51.0 |

---

## 📁 Estrutura do Projeto

```
livraria-tech/
├── main.py                        # Entry point da aplicação
├── alembic.ini                    # Configuração do Alembic
├── requirements.txt
├── .env                           # Variáveis de ambiente (não versionar)
├── .env.example                   # Exemplo de variáveis de ambiente
│
├── alembic/
│   ├── env.py
│   └── versions/                  # Migrações do banco de dados
│
└── backend/
    ├── config/
    │   ├── database_config.py     # Conexão e engine do SQLAlchemy
    │   ├── dependencies.py        # Injeção de dependência da sessão DB
    │   ├── crypt_config.py        # Configuração do bcrypt
    │   └── token_jwt.py           # Geração e verificação de tokens JWT
    │
    ├── models/
    │   ├── admin.py               # Modelo Admin
    │   ├── book.py                # Modelo Book (Livro)
    │   ├── cliente.py             # Modelo Cliente
    │   ├── order.py               # Modelo Order (Pedido)
    │   └── valueObjects/
    │       └── endereco.py        # Value Object de endereço
    │
    ├── schemas/
    │   ├── admin_schema.py        # Schemas Pydantic para Admin
    │   ├── book_schema.py         # Schemas Pydantic para Livro
    │   ├── cliente_schema.py      # Schemas Pydantic para Cliente
    │   └── pedido_schema.py       # Schemas Pydantic para Pedido
    │
    └── routers/
        ├── admin.py               # Rotas de autenticação do Admin
        ├── admin_book.py          # Rotas de gerenciamento de livros e pedidos (Admin)
        ├── login_cliente.py       # Rotas de cadastro e login do Cliente
        └── orders.py              # Rotas de pedidos do Cliente
```

---

## ⚙️ Configuração

### 1. Clonar e criar ambiente virtual

```bash
git clone <url-do-repositório>
cd livraria-tech
python -m venv venv
venv\Scripts\activate       # Windows
# ou
source venv/bin/activate    # Linux/Mac
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Variáveis de ambiente

Crie um arquivo `.env` na raiz com base no `.env.example`:

```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_NAME=livraria

SECRET_KEY=sua_chave_secreta
ALGORITH=HS256
ACESS_TOKEN_MIN=30
```

### 4. Executar migrações

```bash
alembic upgrade head
```

### 5. Iniciar o servidor

```bash
uvicorn main:app --reload
```

A documentação interativa estará disponível em `http://localhost:8000/docs`.

---

## 🔐 Autenticação

A API usa **JWT Bearer Token**. Todos os endpoints protegidos exigem o header:

```
Authorization: Bearer <token>
```

Tokens de acesso expiram conforme `ACESS_TOKEN_MIN`. Existe também um **refresh token** com duração estendida para renovação sem novo login.

---

## 📌 Endpoints

### Auth — Admin (`/auth`)

| Método | Rota | Descrição | Autenticação |
|---|---|---|---|
| `POST` | `/auth/criar-conta` | Cadastro de novo administrador | Não |
| `POST` | `/auth/admin/logar` | Login do administrador | Não |
| `GET` | `/auth/refresh_token_admin` | Renovar token do admin | ✅ Admin |

### Login — Cliente (`/login`)

| Método | Rota | Descrição | Autenticação |
|---|---|---|---|
| `POST` | `/login/cliente-cadastro` | Cadastro de novo cliente | Não |
| `POST` | `/login/logar` | Login do cliente | Não |
| `GET` | `/login/refresh_token_cliente` | Renovar token do cliente | ✅ Cliente |

### Livros & Pedidos — Admin (`/admin_books`)

| Método | Rota | Descrição | Autenticação |
|---|---|---|---|
| `GET` | `/admin_books/all/orders` | Listar todos os pedidos (paginado) | ✅ Admin |
| `POST` | `/admin_books/create/book` | Criar um novo livro | ✅ Admin |
| `PUT` | `/admin_books/update-book/{id_book}` | Atualizar dados de um livro | ✅ Admin |

### Pedidos — Cliente (`/orders`)

| Método | Rota | Descrição | Autenticação |
|---|---|---|---|
| `GET` | `/orders/my_orders` | Listar pedidos do cliente autenticado | ✅ Cliente |
| `POST` | `/orders/order` | Criar um novo pedido | ✅ Cliente |
| `POST` | `/orders/order/cancel` | Cancelar um pedido | ✅ Cliente |

---

## 🗃️ Modelos de Dados

### Admin
| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer (PK) | Identificador único |
| `username` | String(50) | Nome de usuário (único) |
| `email` | String(255) | E-mail (único) |
| `password` | String(255) | Senha (hash bcrypt) |

### Cliente
| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer (PK) | Identificador único |
| `nome_completo` | String(200) | Nome completo |
| `age` | Integer | Idade |
| `email` | String(200) | E-mail (único) |
| `password` | String(200) | Senha (hash bcrypt) |
| `telephone` | String(200) | Telefone (único) |
| `ativo` | Boolean | Status ativo/inativo |
| `endereco` | Composite | Value Object de endereço |

### Endereço (Value Object)
| Campo | Tipo |
|---|---|
| `rua` | String |
| `numero` | String |
| `bairro` | String |
| `cidade` | String |
| `estado` | String |
| `cep` | String |

### Book (Livro)
| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer (PK) | Identificador único |
| `nome` | String(100) | Título do livro |
| `descricao` | String(200) | Descrição |
| `valor` | Float | Preço |
| `url_imagem` | String | URL da imagem de capa |
| `admin_id` | FK → admins | Admin responsável |
| `pedido_id` | FK → orders | Pedido ao qual pertence |

### Order (Pedido)
| Campo | Tipo | Descrição |
|---|---|---|
| `id` | Integer (PK) | Identificador único |
| `cliente_id` | FK → clientes | Cliente do pedido |
| `status` | String | `EM_ANDAMENTO` ou `CANCELADO` |
| `valor_total` | Float | Soma dos valores dos livros |

---

## 🔄 Migrações com Alembic

Para criar uma nova migração após alterações nos modelos:

```bash
alembic revision --autogenerate -m "descrição da mudança"
alembic upgrade head
```

Para reverter a última migração:

```bash
alembic downgrade -1
```
