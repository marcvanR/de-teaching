from fastapi import FastAPI, HTTPException

from repository import repository
from base.duck import Duck

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/duck")
async def post_duck(duck: Duck) -> int:
    return await repository.Repository.insert_duck(duck)


@app.get("/duck/{duck_id}")
async def get_duck(duck_id: int) -> Duck:
    duck = await repository.Repository.select_duck(duck_id)
    if duck is None:
        raise HTTPException(status_code=404, detail="That duck was not found, maybe look at another pond?")
    return duck


@app.get("/alive")
async def are_we_alive():
    return 1