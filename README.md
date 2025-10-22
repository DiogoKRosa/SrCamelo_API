# 🐍 SrCamelo API

## 🧾 Sobre esse projeto

A **SrCamelo API** é o backend do sistema **SrCamelo**, responsável por gerenciar usuários, produtos e compras.  
Ela foi desenvolvida em **Python** com o **FastAPI**, e utiliza o **MongoDB** como banco de dados não relacional.

A API oferece rotas para:

- 👤 **Cadastro e autenticação de usuários** (clientes e vendedores)
- 🛍️ **CRUD completo de produtos** (para vendedores ambulantes)
- 💰 **Registro e listagem de compras**
- 🗨 **Chat para comunicação** (entre vendedores e clientes)
- 🗺 **Cadastro de localização**

A aplicação é containerizada utilizando **Docker**, facilitando o deploy e a execução em diferentes ambientes.

---

## ⚙️ Tecnologias utilizadas

- **Linguagem:** [Python 3.10+](https://www.python.org/)
- **Framework web:** [FastAPI](https://fastapi.tiangolo.com/)
- **Banco de dados:** [MongoDB](https://www.mongodb.com/)
- **Driver MongoDB:** [Motor](https://motor.readthedocs.io/)
- **Containerização:** [Docker](https://www.docker.com/)
- **Filtro de Palavras:** [NLTK](https://www.nltk.org)

---

## ▶️ Como rodar o projeto localmente

### 🔹 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/srcamelo-api.git
cd srcamelo-api
```

### 🔹 2. Rodar com Docker 
O projeto já vem com um docker-compose.yml configurado para subir a API e o MongoDB juntos.
```bash
docker-compose up --build
```
Após o build, a API estará disponível em:

👉 http://localhost:8000

E o MongoDB estará rodando no container mongo na porta 27017.

---

## 🚀 Rotas principais

#### 👤 Usuários
| Método | Rota              | Descrição                     |
|--------|-------------------|-------------------------------|
| POST |`/users` | Cadastra um novo usuário |
| GET |`/users`  | obter informações de todos os usuários cadastrados |
| GET |`/users/{id}`  | Obter informações de um usuário específico |
| GET  |`/vendors` | Traz todo os usuários do tipo vendedor|
| PUT |`/newVendor/{vendor_id}`| Atualiza a imagem e a forma de pagamento de um vendedor recém-cadastrado |

#### 🛍 Produtos
| Método | Rota              | Descrição                     |
|--------|-------------------|-------------------------------|
| POST |`/products`| Cadastra um novo produto|
| GET |`/products/{vendor_id}`| Traz todos os produtos cadastrados de um usuário específico|
| PUT |`/products/{id}`| Atualiza as informações de um produto específico |
| DELETE |`/products/{id}`| Deleta um produto |

#### 💰 Compras
| Método | Rota              | Descrição                     |
|--------|-------------------|-------------------------------|
|POST|`/invoice`| Cadastra uma nova compra |
|GET|`/invoice`| Traz todas as compras de um usuário |

#### 🗺 Localização
| Método | Rota              | Descrição                     |
|--------|-------------------|-------------------------------|
|POST|`/location`| Insere ou atualiza a localização de um usuário |
|GET|`/location`| Recebe todas as localizações do banco|

#### 💬 Chat
| Método | Rota              | Descrição                     |
|--------|-------------------|-------------------------------|
|POST|`/chat`| Cadastra um nova mensagem |
|GET|`/chat`| Traz as mensagens mais recentes das conversas do usuário logado |
|GET|`/chat/{user_id}`| Traz todas as mensagens entre o usuário logado e o usuário específicado |
---

## 🧠 Problemas enfrentados

Durante o desenvolvimento da API, alguns desafios se destacaram:

### 1. Integração com o frontend

 - Criação de endpoints compatíveis com o app mobile (Kotlin/Compose), pois é necessário padronizar a saída da aplicação e a resposta que será enviada para a aplicação.

### 2. Deploy com Docker

 - Configuração de containers interligados (FastAPI + MongoDB).

 - Persistência de dados usando volumes e redes no docker-compose.yml.

### 3. Envio de imagens
 - Na aplicação aceita imagens e fazer com que a API receba a imagem e guarde com um nome aleatório e salvar o nome no banco foi um desafio.

### 4. Filtro de palavras ofensivas
 - Criação da função para filtrar palavras ofensivas
 - Configuração do projeto para aceitar a biblioteca nltk
