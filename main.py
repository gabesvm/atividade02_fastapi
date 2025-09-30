from fastapi import FastAPI  # Passo 1: importar FastAPI

# Passo 2: criar a instância da aplicação
app = FastAPI(title="Atividade 02 - Gabriel Steven")

# Passo 3: criar rota
# Passo 4: definir função de operação
@app.get("/")
def read_root():
    # Passo 5: retornar conteúdo em JSON
    return {"mensagem": "API FastAPI rodando - Atividade 02 (Gabriel Steven)"}
