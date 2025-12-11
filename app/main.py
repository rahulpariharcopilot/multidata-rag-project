"""
Multi-Source RAG + Text-to-SQL API
FastAPI application with document RAG and natural language to SQL capabilities.
"""

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from datetime import datetime
import sys

# Import will work once .env is created
# from app.config import settings

app = FastAPI(
    title="Multi-Source RAG + Text-to-SQL API",
    description="A system that combines document RAG with natural language to SQL conversion",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health"])
async def health_check():
    """
    Health check endpoint to verify the API is running.

    Returns:
        dict: Status information including timestamp and service state
    """
    return {
        "status": "healthy",
        "service": "Multi-Source RAG + Text-to-SQL API",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "0.1.0",
    }


@app.get("/info", status_code=status.HTTP_200_OK, tags=["Information"])
async def get_info():
    """
    Get system information and configuration details.

    Returns:
        dict: System information including Python version, environment, and features
    """
    return {
        "application": {
            "name": "Multi-Source RAG + Text-to-SQL",
            "version": "0.1.0",
            "environment": "development",  # Will be loaded from settings once .env exists
        },
        "features": {
            "document_rag": "Pending implementation - Phase 1",
            "text_to_sql": "Pending implementation - Phase 2",
            "query_routing": "Pending implementation - Phase 3",
            "evaluation": "Pending implementation - Phase 4",
        },
        "system": {
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        },
        "endpoints": {
            "docs": "/docs",
            "redoc": "/redoc",
            "health": "/health",
            "info": "/info",
        },
    }


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint with welcome message and quick links.

    Returns:
        dict: Welcome message and navigation links
    """
    return {
        "message": "Welcome to Multi-Source RAG + Text-to-SQL API",
        "version": "0.1.0",
        "status": "Phase 0 Complete - Development Ready",
        "documentation": "/docs",
        "health_check": "/health",
        "system_info": "/info",
    }


# Event handlers for startup/shutdown (will be used in later phases)
@app.on_event("startup")
async def startup_event():
    """Execute tasks on application startup."""
    print("Starting Multi-Source RAG + Text-to-SQL API...")
    print("Phase 0: Foundation Setup - COMPLETE")
    print("Next: Phase 1 - Document RAG MVP")


@app.on_event("shutdown")
async def shutdown_event():
    """Execute cleanup tasks on application shutdown."""
    print("Shutting down Multi-Source RAG + Text-to-SQL API...")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
