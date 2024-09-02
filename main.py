from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello from Koyeb"}

@app.get("/tarea-1")
def tarea_1():
    return {"respuesta": "Primer tarea realizada"}