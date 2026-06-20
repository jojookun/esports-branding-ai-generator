"""
LLM Service Integration Module.

This module handles communication with IBM Granite via watsonx.ai using LangChain.
It manages prompt construction, API calls, response parsing, and error handling.
"""

import json
import logging
from typing import Dict, Any, Optional

from langchain_ibm import WatsonxLLM
from langchain.schema import HumanMessage, SystemMessage

from ..config import get_settings
from .prompt_engineer import PromptEngineer

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LLMService:
    """
    Service for interacting with IBM Granite via watsonx.ai.
    
    This class encapsulates all LLM interactions, including:
    - Connection management to watsonx.ai
    - Prompt construction and formatting
    - API request handling
    - Response parsing and validation
    - Error handling and retry logic
    """
    
    def __init__(self):
        """Initialize the LLM service with configuration and prompt engineer."""
        self.settings = get_settings()
        self.prompt_engineer = PromptEngineer()
        self.llm = None
        
        # Validate configuration
        if not self.settings.validate_watsonx_config():
            logger.warning(
                "watsonx configuration is incomplete. "
                "Set WATSONX_API_KEY and WATSONX_PROJECT_ID in .env file."
            )
    
    def _initialize_llm(self) -> WatsonxLLM:
        """
        Initialize the WatsonxLLM instance with configuration.
        
        Returns:
            WatsonxLLM: Configured LangChain LLM instance
            
        Raises:
            ValueError: If configuration is invalid
        """
        if not self.settings.validate_watsonx_config():
            raise ValueError(
                "Invalid watsonx configuration. Please check your .env file."
            )
        
        try:
            llm = WatsonxLLM(
                model_id=self.settings.model_id,
                url=self.settings.watsonx_url,
                apikey=self.settings.watsonx_api_key,
                project_id=self.settings.watsonx_project_id,
                params=self.settings.get_model_params()
            )
            logger.info(f"Initialized WatsonxLLM with model: {self.settings.model_id}")
            return llm
        except Exception as e:
            logger.error(f"Failed to initialize WatsonxLLM: {str(e)}")
            raise
    
    def generate_branding_concept(
        self,
        vibe: str,
        game_context: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate a complete branding concept based on user input.
        
        Args:
            vibe: User's creative direction or desired aesthetic
            game_context: Optional specific game or eSports context
            
        Returns:
            dict: Generated branding concept with structure:
                {
                    "success": bool,
                    "concept": dict or None,
                    "error": str or None,
                    "metadata": dict
                }
        """
        try:
            # Initialize LLM if not already done
            if self.llm is None:
                self.llm = self._initialize_llm()
            
            # Construct prompts
            system_prompt = self.prompt_engineer.get_system_prompt()
            user_prompt = self.prompt_engineer.construct_user_prompt(vibe, game_context)
            
            logger.info(f"Generating branding concept for vibe: '{vibe[:50]}...'")
            
            # Prepare messages for the LLM
            # Note: Some LLM implementations may require different message formatting
            full_prompt = f"{system_prompt}\n\n{user_prompt}"
            
            # Invoke the LLM
            response = self.llm.invoke(full_prompt)
            
            logger.info("Received response from LLM")
            
            # Parse the JSON response
            concept = self._parse_response(response)
            
            if concept:
                logger.info(f"Successfully generated concept: {concept.get('theme_name', 'Unknown')}")
                return {
                    "success": True,
                    "concept": concept,
                    "error": None,
                    "metadata": {
                        "model_id": self.settings.model_id,
                        "vibe": vibe,
                        "game_context": game_context
                    }
                }
            else:
                logger.error("Failed to parse valid JSON from LLM response")
                return {
                    "success": False,
                    "concept": None,
                    "error": "Failed to parse valid JSON from LLM response",
                    "metadata": {
                        "raw_response": response[:500] if response else None
                    }
                }
                
        except Exception as e:
            logger.error(f"Error generating branding concept: {str(e)}")
            return {
                "success": False,
                "concept": None,
                "error": str(e),
                "metadata": {}
            }
    
    def _parse_response(self, response: str) -> Optional[Dict[str, Any]]:
        """
        Parse and validate the LLM response as JSON.
        
        Args:
            response: Raw response string from the LLM
            
        Returns:
            dict or None: Parsed JSON object if valid, None otherwise
        """
        try:
            # Try to find JSON in the response
            # Sometimes LLMs add extra text before/after JSON
            response = response.strip()
            
            # Find JSON object boundaries
            start_idx = response.find('{')
            end_idx = response.rfind('}')
            
            if start_idx == -1 or end_idx == -1:
                logger.error("No JSON object found in response")
                return None
            
            json_str = response[start_idx:end_idx + 1]
            concept = json.loads(json_str)
            
            # Validate required fields
            required_fields = ["theme_name", "color_palette", "typography", "layout_guidelines"]
            for field in required_fields:
                if field not in concept:
                    logger.error(f"Missing required field: {field}")
                    return None
            
            # Validate color palette format
            if not isinstance(concept["color_palette"], list):
                logger.error("color_palette must be a list")
                return None
            
            if not (4 <= len(concept["color_palette"]) <= 5):
                logger.error("color_palette must contain 4-5 colors")
                return None
            
            # Validate hex color format
            for color in concept["color_palette"]:
                if not isinstance(color, str) or not color.startswith('#') or len(color) != 7:
                    logger.error(f"Invalid hex color format: {color}")
                    return None
            
            logger.info("Response validation successful")
            return concept
            
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {str(e)}")
            return None
        except Exception as e:
            logger.error(f"Error parsing response: {str(e)}")
            return None
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get the JSON schema for the expected output format.
        
        Returns:
            dict: JSON schema definition
        """
        return self.prompt_engineer.get_json_schema()


# Example usage and testing
if __name__ == "__main__":
    # Demonstrate the LLM service
    service = LLMService()
    
    print("=" * 80)
    print("LLM SERVICE DEMONSTRATION")
    print("=" * 80)
    print(f"Model ID: {service.settings.model_id}")
    print(f"Temperature: {service.settings.model_temperature}")
    print(f"Max Tokens: {service.settings.model_max_tokens}")
    print("\n")
    
    # Note: This will only work if watsonx credentials are configured
    if service.settings.validate_watsonx_config():
        print("watsonx configuration is valid. Ready to generate concepts.")
        
        # Example generation (commented out to avoid API calls during testing)
        # result = service.generate_branding_concept(
        #     vibe="Dark fantasy aesthetic with gold highlights",
        #     game_context="Honor of Kings"
        # )
        # print(json.dumps(result, indent=2))
    else:
        print("⚠️  watsonx configuration is incomplete.")
        print("Please set WATSONX_API_KEY and WATSONX_PROJECT_ID in your .env file.")
        print("\nExample .env configuration:")
        print("WATSONX_API_KEY=your_api_key_here")
        print("WATSONX_PROJECT_ID=your_project_id_here")
    
    print("\n")
    print("=" * 80)
    print("JSON SCHEMA")
    print("=" * 80)
    print(json.dumps(service.get_schema(), indent=2))

# Made with Bob
