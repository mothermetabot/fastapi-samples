from typing import Union

from fastapi import FastAPI


map = {
    1 : "item 1",
    2 : "item 2",
    3 : "item 3",
    4 : "item 4",
}

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get('/items')
def method_name():
    return map
    