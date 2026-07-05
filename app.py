"""
JOAT Instagram Widget
Author: Roger Patton / JOAT Resources LLC

Main FastAPI application.
This app serves the Instagram feed API and static widget assets.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Routers (we'll create these next)
from api.routes.instagram import router as instagram_router

app = FastAPI(
    title="JOAT Instagram Widget",
    version="1.0.0",
    description="Self-hosted Instagram widget for Wix websites."
)

# Allow Wix to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Can be restricted later to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(
    instagram_router,
    prefix="/api"
)

# Static assets
app.mount(
    "/static",
    StaticFiles(directory="public"),
    name="static"
)

@app.get("/")
async def root():
    return {
        "application": "JOAT Instagram Widget",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health():
    """
    Used by Vercel to verify deployment.
    """
    return {
        "status": "healthy"
    }
