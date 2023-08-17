import uvicorn
from fastapi import FastAPI
from DataBaseApi.Routers import BasicUrls

app = FastAPI(title="DataBaseApi")


app.include_router(BasicUrls.router)



if __name__ == "__main__":
    uvicorn.run(app)