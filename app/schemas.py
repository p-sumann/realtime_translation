from typing import Dict, List

from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text cannot be empty")
    languages: List[str] = Field(
        ..., min_length=1, description="Languages cannot be empty"
    )


class TaskResponse(BaseModel):
    task_id: int


class TranslationStatus(BaseModel):
    task_id: int
    status: str
    translations: Dict[str, str]


class Response(BaseModel):
    response: dict
