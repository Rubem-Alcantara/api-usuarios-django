📚 3ª EA - API de Usuários com Django Rest Framework

Projeto desenvolvido para a 3ª EA (Atividade de "Colaborar"), com foco na compreensão de **APIs**, sintaxe **JSON** e segurança com **JWT**.

O objetivo prático foi criar uma API REST utilizando **Django** e **Django Rest Framework** para trafegar dados em formato JSON.
O trabalho foi dividido em 4 passos cobrindo as UAs 9 a 12:

🔹 Passo 1: SQL vs NoSQL (UA9)
Análise comparativa entre estruturas de banco de dados.
* **SQL (Relacional):** Estrutura rígida (tabelas), consistência forte (ACID), ideal para dados previsíveis e relacionamentos complexos.
* **NoSQL (Não Relacional):** Estrutura flexível (documentos, chave-valor), alta escalabilidade horizontal, ideal para Big Data e formatos dinâmicos.

🔹 Passo 2: Sintaxe JSON (UA10)

Estruturação dos dados de usuários solicitados no formato JSON:

```json
[
  {
    "nome": "Carlos",
    "email": "carlos@email.com"
  },
  {
    "nome": "João",
    "email": "joão@email.com"
  }
]
```
🔹 Passo 3: Implementação da API
Desenvolvimento de uma rota (endpoint) utilizando APIView do Django Rest Framework para retornar os dados acima.

*Endpoint: /api/usuarios/

*Método: GET

*Status Esperado: 200 OK

🔹 Passo 4: Segurança com JWT (UA12)
Estudo sobre o fluxo de autenticação JSON Web Token:

1. Cliente envia credenciais.
2. Servidor valida e devolve um Token assinado.
3. Cliente armazena o token e o envia no cabeçalho (Authorization) das próximas requisições.
4. Servidor valida a assinatura do token para liberar o acesso (Stateless).

🛠️ Tecnologias Utilizadas
*Python 3.12
*Django 5.2
*Django Rest Framework (DRF)

🚀 Como rodar o projeto
Clone o repositório:

```

git clone [https://github.com/SEU_USUARIO/api-usuarios-django.git](https://github.com/SEU_USUARIO/api-usuarios-django.git)
cd api-usuarios-django
```
Crie e ative o ambiente virtual:

# Windows
```
python -m venv venv
.\venv\Scripts\activate
```
# Linux/Mac
```
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```
pip install django djangorestframework
```
Prepare o banco de dados (migrações iniciais):
```
python manage.py migrate
```
Inicie o servidor:
```
python manage.py runserver
```
Acesse a API: 
Abra o navegador em: http://127.0.0.1:8000/api/usuarios/
