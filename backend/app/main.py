from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router as applications_router

app = FastAPI(
    title="GCP Fullstack App",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "https://project-31bdab70-9af8-4ea1-a5f.web.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(applications_router)


@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
