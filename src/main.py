import uvicorn
from fastapi import FastAPI

from src.core import get_settings


app = FastAPI(title=get_settings().PROJECT_TITLE)


if __name__ == '__main__':
    uvicorn.run('src.main:app', host='0.0.0.0', port=8000, reload=True)