import uvicorn
from fastapi import FastAPI
from DataBaseApi.API import BasicUrls
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="DataBaseApi")
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5000",
    "http://127.1.1.1:5000"]

app.include_router(BasicUrls.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# нет импортов
@app.on_event("startup")
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
if __name__ == "__main__":
    uvicorn.run(app, host='127.1.1.1', port=5000)
