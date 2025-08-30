



from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
import os

from db import get_connection
from models import save_message, get_chat_history

app = FastAPI()

# Mount the frontend folder to serve static files
#app.mount("/", StaticFiles(directory=os.path.abspath("frontend"), html=True), name="static")


connections = {}

@app.get("/")
async def root():
    return HTMLResponse("<h1>Backend Running</h1>")

@app.post("/login")
async def login(username: str = Form(...)):
    # In real apps, validate username/password here
    response = RedirectResponse(url="/chat.html", status_code=303)
    return response

@app.websocket("/ws/chat/{user_id}")
async def chat(websocket: WebSocket, user_id: int):
    await websocket.accept()
    connections[user_id] = websocket

    try:
        while True:
            data = await websocket.receive_text()
            save_message(user_id, data)

            # Echo to sender only for now
            await websocket.send_text(f"You said: {data}")
    except WebSocketDisconnect:
        del connections[user_id]
