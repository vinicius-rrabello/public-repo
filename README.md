# public-repo

CRUD básico usando FastAPI com db.txt como banco de dados.

## Como rodar

```
pip install -r requirements.txt
uvicorn main:app --reload
```

Acesse a documentação em: http://localhost:8000/docs

## Endpoints

- POST /items → Cria um item
- GET /items → Lista todos os itens
- GET /items/{id} → Busca um item
- PUT /items/{id} → Atualiza um item
- DELETE /items/{id} → Deleta um item
