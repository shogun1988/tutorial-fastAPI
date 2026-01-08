from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'data': 'blog list' }

@app.get('/blog/unpublished')
def unpublished():
    return { 'data': 'all unpublished blogs' }

@app.get('/blog/{id}')
def show(id: int):
    # fetch blow with id = id
    return { 'data': id }

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch the comments
    return { 'data': {"1", "2"}}