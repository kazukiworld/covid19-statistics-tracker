from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import statistics, email

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://backend:8000",
]

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers as dependencies
app.include_router(statistics.router, tags=["Statistics"])
app.include_router(email.router, tags=["Email"])