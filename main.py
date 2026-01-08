from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'data': { 'name': 'Nokah' }}

@app.get('/about')
def about():
    return { 'data': 'about Page' }