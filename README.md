# Translation Service API

This is not a core AI/ML project rather learning FastAPI to deploy and run ml models on production.

This application leverages OpenAI/Gemini to provide real-time translation of documents. It uses FastAPI for the backend to handle API requests and Streamlit for the frontend to create an interactive user interface. The combination of these technologies ensures a seamless and efficient translation experience.

## 🌟 Features

- Real-time text translation
- Support for multiple languages
- User-friendly Streamlit interface
- RESTful API endpoints
- Auto language detection

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- openai
- fastapi
- streamlit

### Installation

1. Clone the repository:
```bash
git clone https://github.com/p-sumann/realtime_translation.git

cd fastapi-translation-service
```

2. Install dependencies:
```bash
pythom -m venv .venv
source .venv/bin/activate  

pip install -r requirements.txt
```

3. Configure environment variables:
   - Create a `.env` file
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

4. Run the application:
   - Start the FastAPI backend:
     ```bash
     cd app
     uvicorn fastapi_app:app --reload
     ```
   - Start the Streamlit frontend:
     ```bash
     streamlit run streamlit_app.py
     ```

#### POST /translate
Translates text between languages.
```json
{
  "text": "string",
  "languages": [
    "string"
  ]
}
```

#### GET /translation/{task_id}
Returns translated version of give text.

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Translation**: OpenAI API
