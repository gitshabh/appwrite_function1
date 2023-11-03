from fastapi import FastAPI
import model

app = FastAPI(
    docs_url='/'
)

@app.get('/api/{message}')
async def getMessage(message):

    response = model.getResponse(message)

    return {'response' : response}