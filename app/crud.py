import models
from sqlalchemy.orm import Session


def create_transalation_task(db: Session, text: str, languages: list):
    task = models.TranslationTask(text=text, languages=languages)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_translation_task(db: Session, task_id: int):
    return (
        db.query(models.TranslationTask)
        .filter(models.TranslationTask.id == task_id)
        .first()
    )


def update_translaion_task(db: Session, task_id: int, transalations: dict):
    task = (
        db.query(models.TranslationTask)
        .filter(models.TranslationTask.id == task_id)
        .first()
    )
    task.translation = transalations
    task.status = "completed"
    db.commit()
    db.refresh(task)
    return task
