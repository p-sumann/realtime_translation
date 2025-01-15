from sqlalchemy import JSON, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TranslationTask(Base):
    __tablename__ = "translation_tasks"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    languages = Column(JSON, nullable=False)
    status = Column(String, default="in_progress")
    translation = Column(JSON, default={})

