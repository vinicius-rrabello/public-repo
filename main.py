from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

DB_FILE = "db.txt"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)


def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


class Item(BaseModel):
    nome: str
    descricao: str


@app.post("/items")
def create_item(item: Item):
    db = read_db()
    new_item = {
        "id": len(db) + 1,
        "nome": item.nome,
        "descricao": item.descricao
    }
    db.append(new_item)
    write_db(db)
    return {"message": "Item criado!", "item": new_item}


@app.get("/items")
def get_items():
    return read_db()


@app.get("/items/{item_id}")
def get_item(item_id: int):
    db = read_db()
    item = next((i for i in db if i["id"] == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated: Item):
    db = read_db()
    for item in db:
        if item["id"] == item_id:
            item["nome"] = updated.nome
            item["descricao"] = updated.descricao
            write_db(db)
            return {"message": "Item atualizado!", "item": item}
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = read_db()
    new_db = [i for i in db if i["id"] != item_id]
    if len(new_db) == len(db):
        raise HTTPException(status_code=404, detail="Item não encontrado")
    write_db(new_db)
    return {"message": "Item deletado!"}
