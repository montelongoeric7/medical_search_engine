
import requests
import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import app.modelos.models as models
import app.schemasstuff.schemas as schemas
from app.dbs.database import get_db
import app.oauth.oauth2 as oauth2
from app.configurations.config import settings
import openai
from langchain_community.llms import OpenAI




router = APIRouter(
    prefix="/search_router",
    tags=["Search Router"],
)

def perplexity_search(query:str):
    API_KEY = settings.perplexity_api_key
    API_ENDPOINT = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload={
        "model": "llama-3-sonar-small-32k-online",
        "messages": [
            {"role": "system", "content": "You are a helpful search assistant."},
            {"role": "user", "content": query}
        ],
        "max_tokens": 1024,
        "temperature": 0.7,
        "stream": False
    }
    response = requests.post(API_ENDPOINT, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@router.post("/search", response_model=schemas.SearchRequest)
def search(search_request: schemas.SearchRequest):
    try:
        response = perplexity_search(search_request.query)
        return {"query": response}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    



def search2(search_request: schemas.SearchRequest):
    try:
        response = perplexity_search(search_request.query)
        return {"query": response}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@router.post("/searchdummy", response_model=schemas.SearchRequest)
def search_dummy(search_request: schemas.SearchRequest):
    return {"query": "This is a dummy response for the search query. Stretching this out for fronted testing purposes."}