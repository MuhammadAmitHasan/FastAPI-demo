from fastapi import FastAPI
import random
from procedure import add_numbers, multiply_numbers
from models import User

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "This is an test", 'random': random.randint(1, 100)}

@app.get("/random/{limit}")
async def read_item(limit: int):
    return {'random with limit': random.randint(1, limit), "limit": limit}

@app.get("/add")
def add(a: int, b: int):
    result = add_numbers(a, b)
    return {"result": result}

@app.get("/multiply")
def multiply(a: int, b: int):
    result = multiply_numbers(a, b)
    return {"result": result}

@app.get("/ds")
async def read_ds():
    my_list = [1, 2, 3, "hello", True]
    my_tuple = (1, 2, 3, "hello", True)
    my_dict = {"key1": "value1", "key2": "value2"}
    my_set = {1, 2, 3, "hello", True}
    my_string = "Hello, World!"
    my_boolean = True

    return {
        "List": {
            "Description": "A list is an ordered collection of items. It is mutable, meaning you can change its content.",
            "Example": my_list
        },
        "Tuple": {
            "Description": "A tuple is similar to a list, but it is immutable, meaning you cannot change its elements after creation.",
            "Example": my_tuple
        },
        "Dictionary": {
            "Description": "A dictionary is a collection of key-value pairs. Keys are unique and are used to access values.",
            "Example": my_dict
        },
        "Set": {
            "Description": "A set is an unordered collection of unique items. It doesn’t allow duplicate values.",
            "Example": list(my_set)  # Converting set to list for better display in JSON
        },
        "String": {
            "Description": "Strings are sequences of characters.",
            "Example": my_string
        },
        "Boolean": {
            "Description": "Booleans represent True or False values.",
            "Example": my_boolean
        }
    }


@app.post("/create-user")
async def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }