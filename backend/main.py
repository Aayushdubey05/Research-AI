from fastapi import FastAPI, HTTPException, Header 


app = FastAPI()

app.get('/', status_code=200)
def root():
    try:
        return {'details': 'Home'}
    except Exception as err:
        raise HTTPException(err) from err
