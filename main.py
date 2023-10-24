from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/blog")
def index(published: bool = True, limit=10, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} blog list"}
    else:
        return {"data": "blogs are not published"}
    
@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


# define int in function so that we get it that way 
@app.get("/blog/{id}")
def get_post(id: int):
    return {"message": id}


@app.get("/blog/{id}/comments")
def comments():
    return {"data": {1,2,3}}
