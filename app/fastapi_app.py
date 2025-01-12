from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from schemas import TranslationRequest, TaskResponse, TranslationStatus
app = FastAPI()

@app.get("/")
async def hello():
    return 'Hello World!'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*']
)

@app.post("/translate", response_model=TaskResponse)
def translate(request: TranslationRequest):
    TaskResponse.task_id = 1
    return TaskResponse

