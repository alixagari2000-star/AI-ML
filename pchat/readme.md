✅ Frontend: Plain HTML/CSS/JavaScript (no framework)

✅ Backend: FastAPI (Python), JWT, WebSocket

✅ Database: MySQL

✅ Hosting: Apache HTTP Server (httpd) with reverse proxy

✅ No Docker, no Kubernetes

💬 AI Chat App

An AI-powered real-time chat application where users are randomly matched for 1-on-1 private conversations, with support for persistent memory and JWT-based authentication.

🚀 Features

✅ JWT-based user authentication (Login / Signup)

✅ Random user matching for 1-on-1 chats

✅ Private messaging via WebSocket

✅ Persistent chat history using MySQL

✅ Stateless token-based backend

✅ Fast and simple frontend using plain JavaScript

✅ Secure architecture with Apache reverse proxy


User's Browser
   ├── Loads frontend (index.html, chat.html, JS, CSS) ← Apache (HTTPD)
   ├── Sends API requests to /api/...                 → Apache → FastAPI
   └── Connects WebSocket to /ws                      → Apache → FastAPI (WebSocket)

Server
   ├── Apache HTTP Server (port 80)
   │   ├── Serves static frontend from /var/www/html
   │   └── Proxies /api and /ws to FastAPI
   ├── FastAPI backend (localhost:8000 via Gunicorn + Uvicorn)
   └── MySQL database for users, chats, and messages


project-root/
├── backend/
│   ├── main.py               # FastAPI app entrypoint
│   ├── auth.py               # JWT auth logic
│   ├── websocket.py          # WebSocket connection handler
│   ├── chat.py               # Matching and message routing
│   ├── models.py             # SQLAlchemy models
│   ├── database.py           # DB connection setup
│   └── requirements.txt
├── frontend/                 # Static files served by Apache
│   ├── index.html            # Login/signup UI
│   ├── chat.html             # Chat UI
│   ├── js/
│   │   ├── auth.js           # Auth API & token handling
│   │   └── chat.js           # WebSocket messaging
│   └── css/
│       └── styles.css
├── apache/
│   └── chat-app.conf         # Apache VirtualHost config
└── README.md
