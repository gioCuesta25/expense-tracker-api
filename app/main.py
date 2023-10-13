from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import create_db_and_tables
from routers import user, auth, categories, amount
import uvicorn


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(user.router)
app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(amount.router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=10000, reload=True)
