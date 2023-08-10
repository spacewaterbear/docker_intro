from fastapi import FastAPI
from fastapi.responses import RedirectResponse
app = FastAPI()




@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/bonjour")
def read_root():
    return {"message": "Bonjour, le !"}


