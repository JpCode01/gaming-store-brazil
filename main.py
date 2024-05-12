from fastapi import FastAPI, Query
import json
import uvicorn
import os

app = FastAPI()

@app.get('/api/pcs')
def get_pcs(pc: str = Query(None)):
  with open("dados.json") as dados_pc:
    dados_json = json.load(dados_pc)
  if pc is None:
    return {'Dados':dados_json}
  dados_do_pc = []
  for item in dados_json:
    if item['modelName'] == pc:
      dados_do_pc.append({
          "model": item['modelName'],
          "configurations": item['configurations']
      })
  return {'Pc':pc, 'Informações:':dados_do_pc}

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))