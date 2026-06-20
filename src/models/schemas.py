"""
Pydantic models for request/response validation and data structures.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class TypographyRecommendation(BaseModel):
    """Typography pairing recommendations for eSports branding."""
    
    primary_display: str = Field(
        ...,
        description="Primary display font (aggressive/bold for headers)"
    )
    secondary_body: str = Field(
        ...,
        description="Secondary body font (clean/modern like Quicksand)"
    )
    pairing_rationale: str = Field(
        ...,
        description="Explanation of why these fonts work together"
    )


class LayoutGuidelines(BaseModel):
    """Layout and design guidelines for various eSports media."""
    
    streaming_overlay: str = Field(
        ...,
        description="Specific recommendations for OBS/stream overlays"
    )
    social_media_banner: str = Field(
        ...,
        description="Design concepts for Twitter/Instagram headers"
    )
    text_masking_concepts: str = Field(
        ...,
        description="Creative text-masking techniques for visual impact"
    )


class BrandingConcept(BaseModel):
    """Complete visual identity concept for eSports branding."""
    
    theme_name: str = Field(
        ...,
        description="Catchy name for the branding concept"
    )
    color_palette: List[str] = Field(
        ...,
        min_length=4,
        max_length=5,
        description="4-5 hex color codes tailored for gradient use"
    )
    typography: TypographyRecommendation = Field(
        ...,
        description="Font recommendations and pairing rationale"
    )
    layout_guidelines: LayoutGuidelines = Field(
        ...,
        description="Specific concepts for streaming overlays and social media"
    )


class BrandingRequest(BaseModel):
    """Request model for generating branding concepts."""
    
    vibe: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="User's creative direction or 'vibe' for the branding",
        examples=[
            "Futuristic cyberpunk with neon accents for a competitive FPS team",
            "Clean minimalist design with bold typography for osu!mania streamer",
            "Dark fantasy aesthetic with gold highlights for Honor of Kings team"
        ]
    )
    game_context: Optional[str] = Field(
        None,
        description="Specific game or eSports context (e.g., 'Honor of Kings', 'osu!mania')"
    )


class BrandingResponse(BaseModel):
    """Response model containing the generated branding concept."""
    
    success: bool = Field(
        ...,
        description="Whether the generation was successful"
    )
    concept: Optional[BrandingConcept] = Field(
        None,
        description="The generated branding concept"
    )
    error: Optional[str] = Field(
        None,
        description="Error message if generation failed"
    )
    metadata: Optional[dict] = Field(
        None,
        description="Additional metadata about the generation process"
    )


class HealthCheckResponse(BaseModel):
    """Health check response for API status."""
    
    status: str = Field(default="healthy")
    version: str = Field(default="1.0.0")
    service: str = Field(default="eSports Branding Generator")

# Made with Bob
