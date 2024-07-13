from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import openai
import os

app = FastAPI()

# Set your OpenAI API key here
openai.api_key = 'your-openai-api-key'

# Serve the static files (index.html and other assets)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("static/index.html", "r") as file:
        return HTMLResponse(content=file.read(), status_code=200)

@app.post("/api")
async def chat_api(request: Request):
    data = await request.json()
    message = data.get('message')

    if not message:
        return JSONResponse(content={"response": "Message cannot be empty."}, status_code=400)

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            max_tokens=150
        )
        response_text = response.choices[0].text.strip()
        return JSONResponse(content={"response": response_text}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"response": f"Error: {str(e)}"}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

