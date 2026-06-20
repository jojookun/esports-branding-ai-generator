"""
API Integration Mockup Demonstration

This script demonstrates the complete end-to-end flow of the eSports Branding Generator:
1. Loading environment configuration
2. Constructing prompts using the prompt engineering module
3. Sending requests to IBM Granite via LangChain
4. Parsing and validating JSON responses
5. Displaying results in a user-friendly format

This serves as both a demonstration and a template for integrating the
branding generator into larger applications.
"""

import sys
import os
import json
from pathlib import Path

# Add parent directory to path to import src modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services.llm_service import LLMService
from src.services.prompt_engineer import PromptEngineer
from src.utils.validators import validate_branding_concept
from src.config import get_settings


def print_header(title: str):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")


def print_color_palette(colors: list):
    """Print color palette with visual representation."""
    print("Color Palette:")
    for i, color in enumerate(colors, 1):
        # Create a simple visual representation
        print(f"  {i}. {color} {'█' * 10}")


def print_typography(typography: dict):
    """Print typography recommendations."""
    print("Typography:")
    print(f"  Primary Display: {typography['primary_display']}")
    print(f"  Secondary Body:  {typography['secondary_body']}")
    print(f"\n  Rationale:")
    print(f"  {typography['pairing_rationale']}")


def print_layout_guidelines(layout: dict):
    """Print layout guidelines."""
    print("Layout Guidelines:")
    print(f"\n  Streaming Overlay:")
    print(f"  {layout['streaming_overlay']}")
    print(f"\n  Social Media Banner:")
    print(f"  {layout['social_media_banner']}")
    print(f"\n  Text Masking Concepts:")
    print(f"  {layout['text_masking_concepts']}")


def display_branding_concept(concept: dict):
    """Display a branding concept in a formatted way."""
    print_header(f"BRANDING CONCEPT: {concept['theme_name']}")
    
    print_color_palette(concept['color_palette'])
    print("\n")
    
    print_typography(concept['typography'])
    print("\n")
    
    print_layout_guidelines(concept['layout_guidelines'])


def run_demo_with_mock_data():
    """
    Run the demo with mock data (when API credentials are not available).
    This shows what the output would look like.
    """
    print_header("DEMO MODE: Using Mock Data")
    print("⚠️  watsonx credentials not configured. Showing example output.\n")
    
    # Mock branding concept
    mock_concept = {
        "theme_name": "Cyber Samurai",
        "color_palette": ["#FF0080", "#00D9FF", "#9D00FF", "#FFD700", "#1A1A2E"],
        "typography": {
            "primary_display": "Rajdhani Bold (Sharp, angular, tech-inspired)",
            "secondary_body": "Quicksand Regular (Smooth, modern, highly readable)",
            "pairing_rationale": "Rajdhani's geometric precision evokes cyberpunk aesthetics and competitive gaming intensity, while Quicksand ensures all supporting text remains accessible and professional. The contrast between sharp display and rounded body creates dynamic visual hierarchy perfect for streaming overlays and social media."
        },
        "layout_guidelines": {
            "streaming_overlay": "Create a split-screen layout with the webcam positioned in the bottom-left corner within a hexagonal frame featuring the primary gradient (#FF0080 to #00D9FF). Position subscriber alerts and notifications in the top-right with animated neon glow effects. Use semi-transparent panels (15% opacity) with subtle scan-line animations for chat and recent events overlay.",
            "social_media_banner": "Design a diagonal composition splitting the banner from top-left to bottom-right. Place the team logo in the left third with a glowing outline effect. Use text masking on the player/team name with a gradient fill transitioning through the color palette. Add subtle particle effects and a faint grid pattern in the background for depth.",
            "text_masking_concepts": "Implement gradient-filled text with knockout effects over gameplay footage or abstract backgrounds. Apply chromatic aberration to main headers for a glitch aesthetic. Use animated gradient shifts on interactive elements. Create depth by layering text with different opacity levels and subtle drop shadows with neon glow."
        }
    }
    
    display_branding_concept(mock_concept)
    
    # Validate the mock concept
    print("\n")
    print_header("VALIDATION")
    is_valid, error = validate_branding_concept(mock_concept)
    if is_valid:
        print("✓ Concept structure is valid")
        print("✓ All required fields present")
        print("✓ Color palette format correct")
        print("✓ Typography structure valid")
        print("✓ Layout guidelines complete")
    else:
        print(f"✗ Validation failed: {error}")


def run_demo_with_api():
    """
    Run the demo with actual API calls to IBM Granite.
    This requires valid watsonx credentials.
    """
    print_header("LIVE API MODE: Generating with IBM Granite")
    
    # Initialize the LLM service
    service = LLMService()
    
    # Example vibes to test
    test_cases = [
        {
            "vibe": "Futuristic cyberpunk with neon accents for a competitive FPS team",
            "game_context": "Valorant"
        },
        {
            "vibe": "Clean minimalist design with bold typography for rhythm game streamer",
            "game_context": "osu!mania"
        },
        {
            "vibe": "Dark fantasy aesthetic with gold highlights and royal purple",
            "game_context": "Honor of Kings"
        }
    ]
    
    # Let user choose or use first example
    print("Available test cases:")
    for i, case in enumerate(test_cases, 1):
        print(f"  {i}. {case['vibe'][:60]}... ({case['game_context']})")
    
    print("\nUsing test case 1 for demonstration...\n")
    selected_case = test_cases[0]
    
    # Generate branding concept
    print(f"Generating concept for: '{selected_case['vibe']}'")
    print(f"Game context: {selected_case['game_context']}")
    print("\nSending request to IBM Granite via watsonx.ai...")
    print("(This may take 10-30 seconds)\n")
    
    result = service.generate_branding_concept(
        vibe=selected_case['vibe'],
        game_context=selected_case['game_context']
    )
    
    # Display results
    if result['success']:
        print("✓ Successfully generated branding concept!\n")
        display_branding_concept(result['concept'])
        
        # Show metadata
        print("\n")
        print_header("GENERATION METADATA")
        print(f"Model: {result['metadata'].get('model_id', 'N/A')}")
        print(f"Vibe: {result['metadata'].get('vibe', 'N/A')}")
        print(f"Context: {result['metadata'].get('game_context', 'N/A')}")
        
        # Validate
        print("\n")
        print_header("VALIDATION")
        is_valid, error = validate_branding_concept(result['concept'])
        if is_valid:
            print("✓ Generated concept is valid")
        else:
            print(f"⚠️  Validation warning: {error}")
    else:
        print(f"✗ Generation failed: {result['error']}")
        if 'metadata' in result and 'raw_response' in result['metadata']:
            print(f"\nRaw response preview:")
            print(result['metadata']['raw_response'])


def main():
    """Main entry point for the demo script."""
    print_header("eSports Branding Generator - API Integration Demo")
    
    # Load settings
    settings = get_settings()
    
    print("Configuration:")
    print(f"  Model: {settings.model_id}")
    print(f"  Temperature: {settings.model_temperature}")
    print(f"  Max Tokens: {settings.model_max_tokens}")
    print(f"  watsonx URL: {settings.watsonx_url}")
    
    # Check if API credentials are configured
    if settings.validate_watsonx_config():
        print(f"  API Status: ✓ Configured")
        print("\n")
        
        # Ask user if they want to run with API or mock data
        print("Options:")
        print("  1. Run with live API (requires IBM watsonx credentials)")
        print("  2. Run with mock data (demonstration mode)")
        
        choice = input("\nSelect option (1 or 2, default=2): ").strip()
        
        if choice == "1":
            try:
                run_demo_with_api()
            except Exception as e:
                print(f"\n✗ Error during API demo: {str(e)}")
                print("\nFalling back to mock data demo...\n")
                run_demo_with_mock_data()
        else:
            run_demo_with_mock_data()
    else:
        print(f"  API Status: ✗ Not configured")
        print("\n⚠️  To use live API mode, configure your .env file:")
        print("     WATSONX_API_KEY=your_api_key")
        print("     WATSONX_PROJECT_ID=your_project_id")
        print("\n")
        run_demo_with_mock_data()
    
    # Show prompt engineering example
    print("\n")
    print_header("PROMPT ENGINEERING EXAMPLE")
    engineer = PromptEngineer()
    
    print("System Prompt (first 500 characters):")
    print("-" * 80)
    system_prompt = engineer.get_system_prompt()
    print(system_prompt[:500] + "...")
    print("-" * 80)
    
    print("\nUser Prompt Example:")
    print("-" * 80)
    user_prompt = engineer.construct_user_prompt(
        "Futuristic cyberpunk with neon accents",
        "Valorant"
    )
    print(user_prompt)
    print("-" * 80)
    
    print("\n")
    print_header("Demo Complete")
    print("This demonstration showed:")
    print("  ✓ Environment configuration loading")
    print("  ✓ Prompt construction with PromptEngineer")
    print("  ✓ LLM service integration (mock or live)")
    print("  ✓ JSON response parsing and validation")
    print("  ✓ Formatted output display")
    print("\nFor integration into your application, use the LLMService class")
    print("from src.services.llm_service import LLMService")
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\n\n✗ Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()

# Made with Bob
