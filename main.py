from fastapi import FastAPI
from routers.activities_router import router

app = FastAPI(title="Atividades")
app.include_router(router)