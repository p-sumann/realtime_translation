import crud
import models
from crud import create_transalation_task
from database import engine, get_db
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import TaskResponse, TranslationRequest, TranslationStatus
from sqlalchemy.orm import Session
from utils import translations

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"]
)


@app.post("/translate", response_model=TaskResponse)
def translate(request: TranslationRequest, db: Session = Depends(get_db)):
    try:
        task = create_transalation_task(
            db=db, text=request.text, languages=request.languages
        )
        translations(task.id, task.text, task.languages, db)
        return {"task_id": task.id}

    except Exception as e:
        print(e)


@app.get("/translation/{task_id}", response_model=TranslationStatus)
def translation(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_translation_task(task_id=task_id, db=db)
    if not task:
        raise HTTPException(detail="task_id not found !!", status_code=404)
    return {"task_id": task.id, "status": task.status, "translations": task.translation}
