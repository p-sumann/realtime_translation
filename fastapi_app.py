from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return 'Hello World!'

@app.get("/inputs/{number}")
async def read_input(number):
    return {'hello': number}
    

@app.get("/models/{model}")
async def read_model(model: str):
    return model