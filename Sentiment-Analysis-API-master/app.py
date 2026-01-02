from fastapi import FastAPI,Query
import uvicorn
from textblob import TextBlob


app = FastAPI()

@app.get('/')
async def inedx():
    return {'text':'Hello'}

@app.get('/sentiment/{text}')
async def get_sentiment(text):
        blob = TextBlob(text).sentiment
        result = {'orginal_text':text,'polarity':blob.polarity,'subjectivity':blob.subjectivity}
        return result

if __name__ == "__main__":
    uvicorn.run(app,host='127.0.0.1',port=8000)
