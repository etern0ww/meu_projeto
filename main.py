from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel, Field
import json

app = FastAPI()
@app.get("/")
def root():
    return{"status": "ok"}
class Tarefa(BaseModel):
    id: int
    titulo: str = Field(min_length=3)
class TarefaUpdate(BaseModel):
    titulo: str = Field(min_length=3)
tarefas = []
contador_id= 1

@app.post("/tarefas", status_code=201)
def criar_tarefa(tarefa: Tarefa):
    global contador_id
    tarefa.id = contador_id
    contador_id += 1
    tarefas.append(tarefa)
    return tarefa

@app.get("/tarefas")
def listar_tarefas():
    with open("tarefas.json", "r") as arquivo:
        tarefas = json.load(arquivo)
    return tarefas

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa.id ==id:
            tarefas.remove(tarefa)
            return{"mensagem": "Tarefa removida com sucesso"}
    raise HTTPException(
        status_code=404,
        detail="Tarefa não existe ou ja foi concluida"
    )
@app.put("/tarefas/{id}")
def atualizar_tarefa(id : int, dados: TarefaUpdate):
    for tarefa in tarefas:
        if tarefa.id == id:
            tarefa.titulo = dados.titulo
            return tarefa
    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada"
    )
