from .routers.authorization import auth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, information, chatbot, suggestor, medical
from .routers.search import search_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(information.router)
app.include_router(auth.router)
app.include_router(chatbot.router)
app.include_router(suggestor.router)
app.include_router(medical.router)
app.include_router(search_router.router)

@app.get("/")
async def read_root():
    return {"message": "If you're reading this it's too late."}
