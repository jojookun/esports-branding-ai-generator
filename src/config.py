"""
Configuration management for the eSports Branding Generator.
Loads settings from environment variables.
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # IBM watsonx.ai Configuration
    watsonx_api_key: str = os.getenv("WATSONX_API_KEY", "")
    watsonx_project_id: str = os.getenv("WATSONX_PROJECT_ID", "")
    watsonx_url: str = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
    
    # IBM Granite Model Configuration
    model_id: str = os.getenv("MODEL_ID", "ibm/granite-13b-chat-v2")
    model_temperature: float = float(os.getenv("MODEL_TEMPERATURE", "0.7"))
    model_max_tokens: int = int(os.getenv("MODEL_MAX_TOKENS", "2000"))
    
    # Application Configuration
    app_name: str = os.getenv("APP_NAME", "eSports Branding Generator")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    debug_mode: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
    
    # API Configuration
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        case_sensitive = False
    
    def validate_watsonx_config(self) -> bool:
        """
        Validate that required watsonx configuration is present.
        
        Returns:
            bool: True if configuration is valid, False otherwise
        """
        if not self.watsonx_api_key:
            return False
        if not self.watsonx_project_id:
            return False
        return True
    
    def get_model_params(self) -> dict:
        """
        Get model parameters for LLM invocation.
        
        Returns:
            dict: Model parameters including temperature and max_tokens
        """
        return {
            "temperature": self.model_temperature,
            "max_tokens": self.model_max_tokens,
        }


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Get the global settings instance.
    
    Returns:
        Settings: Application settings
    """
    return settings

# Made with Bob
