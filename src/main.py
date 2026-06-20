"""
FastAPI Application for eSports Branding Generator

This is the main entry point for the API server. It provides endpoints
for generating branding concepts and checking service health.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .models.schemas import (
    BrandingRequest,
    BrandingResponse,
    HealthCheckResponse
)
from .services.llm_service import LLMService
from .config import get_settings
from .utils.validators import validate_branding_concept

# Initialize FastAPI app
app = FastAPI(
    title="eSports Branding Generator API",
    description="AI-powered visual identity concept generator for eSports teams and content creators",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
settings = get_settings()
llm_service = LLMService()


@app.get("/", response_model=HealthCheckResponse)
async def root():
    """
    Root endpoint - returns basic service information.
    """
    return HealthCheckResponse(
        status="healthy",
        version=settings.app_version,
        service=settings.app_name
    )


@app.get("/health", response_model=HealthCheckResponse)
async def health_check():
    """
    Health check endpoint for monitoring and load balancers.
    """
    return HealthCheckResponse(
        status="healthy",
        version=settings.app_version,
        service=settings.app_name
    )


@app.post("/generate", response_model=BrandingResponse)
async def generate_branding_concept(request: BrandingRequest):
    """
    Generate a complete branding concept based on user input.
    
    Args:
        request: BrandingRequest containing vibe and optional game_context
        
    Returns:
        BrandingResponse with generated concept or error
        
    Raises:
        HTTPException: If generation fails
    """
    try:
        # Validate watsonx configuration
        if not settings.validate_watsonx_config():
            raise HTTPException(
                status_code=503,
                detail="Service not configured. Please set watsonx credentials."
            )
        
        # Generate branding concept
        result = llm_service.generate_branding_concept(
            vibe=request.vibe,
            game_context=request.game_context
        )
        
        # Validate the generated concept if successful
        if result["success"] and result["concept"]:
            is_valid, error = validate_branding_concept(result["concept"])
            if not is_valid:
                result["metadata"]["validation_warning"] = error
        
        return BrandingResponse(**result)
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@app.get("/schema")
async def get_output_schema():
    """
    Get the JSON schema for the expected output format.
    
    Returns:
        dict: JSON schema definition
    """
    return JSONResponse(content=llm_service.get_schema())


@app.get("/config")
async def get_config():
    """
    Get current service configuration (non-sensitive information only).
    
    Returns:
        dict: Configuration information
    """
    return {
        "model_id": settings.model_id,
        "temperature": settings.model_temperature,
        "max_tokens": settings.model_max_tokens,
        "app_version": settings.app_version,
        "configured": settings.validate_watsonx_config()
    }


# Run the application
if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=settings.debug_mode
    )

# Made with Bob
