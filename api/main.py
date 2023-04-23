from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{items_id}/")
def get_data(items_id:int,q: Union[str,None]=None):
    return {"items_id":items_id,"q":q}

