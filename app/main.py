from fastapi import FastAPI

from .routers import clubs, slots

app = FastAPI()

app.include_router(slots.router, prefix="/slots", tags=["slots"])
app.include_router(clubs.router, prefix="/clubs", tags=["clubs"])