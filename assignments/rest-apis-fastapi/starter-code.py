from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Define your Item model using Pydantic
class Item(BaseModel):
    id: int
    name: str

# In-memory list of items
items = []

# TODO: Define a GET / route that returns a welcome message
@app.get("/")
def read_root():
    pass

# TODO: Define a GET /items route that returns all items
# Add an optional 'search' query parameter to filter by name
@app.get("/items")
def get_items(search: str = None):
    pass

# TODO: Define a GET /items/{item_id} route that returns a single item
# Return a 404 error if not found
@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass

# TODO: Define a POST /items route that accepts an Item body
# Append the new item to the list and return it with status 201
@app.post("/items", status_code=201)
def create_item(item: Item):
    pass
