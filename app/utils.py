import os

from crud import update_translaion_task
from dotenv import load_dotenv
from openai import AzureOpenAI
from sqlalchemy.orm import Session

load_dotenv(override=True)

openai = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def translations(task: int, text: str, languages: list, db: Session):
    translations = {}
    languages = [x.strip() for x in languages]
    for lang in languages:
        
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": f'You are a senior assistant who help to translate text into {lang} language. Only translate the given text and dont response anything else.'},
                    {"role": "user", "content": text}
                ]
            )
            translated_text = response.choices[0].message
            translations[lang] = str(translated_text.content.strip())
        
        except Exception as e:
            print(f'Error occured: {e}')
    
    update_translaion_task(db, task, translations)
            
