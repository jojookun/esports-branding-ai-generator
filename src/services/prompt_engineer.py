"""
AI Prompt Engineering Module for eSports Branding Generation.

This module constructs sophisticated prompts that instruct IBM Granite
to act as an expert eSports art director and generate structured JSON
containing comprehensive visual identity concepts.
"""

import json
from typing import Dict, Any


class PromptEngineer:
    """
    Constructs and manages prompts for the AI branding generator.
    
    This class implements the prompt engineering strategy that transforms
    user input into structured requests for IBM Granite, ensuring consistent
    and high-quality branding concept generation.
    """
    
    def __init__(self):
        """Initialize the prompt engineer with system configuration."""
        self.system_role = "Expert eSports Art Director & Brand Strategist"
        self.output_format = "JSON"
        
    def get_system_prompt(self) -> str:
        """
        Construct the system prompt that defines the AI's role and behavior.
        
        This prompt instructs IBM Granite to:
        1. Act as an expert eSports art director
        2. Understand gaming aesthetics and trends
        3. Generate structured JSON output
        4. Apply design principles for gradients, typography, and layouts
        
        Returns:
            str: The complete system prompt
        """
        system_prompt = f"""You are an {self.system_role} with deep expertise in:
- eSports visual identity design and branding
- Gaming culture and competitive gaming aesthetics
- Modern design trends in streaming, content creation, and social media
- Color theory for digital displays and gradient design
- Typography pairing for aggressive gaming brands with clean readability
- Layout design for streaming overlays (OBS), social media banners, and promotional materials

**Your Mission:**
Generate comprehensive, production-ready visual identity concepts for eSports teams, content creators, and competitive gamers. Your designs should be bold, modern, and optimized for digital platforms.

**Design Principles:**
1. **Color Palettes**: Create 4-5 hex colors specifically designed for gradient use. Consider:
   - High contrast for visibility during streams
   - Complementary colors that work well in motion
   - Colors that evoke the desired emotional response (aggressive, futuristic, elegant, etc.)
   - Accessibility for colorblind viewers when possible

2. **Typography**: Pair fonts strategically:
   - Primary Display Font: Bold, aggressive, attention-grabbing (for headers, logos, overlays)
   - Secondary Body Font: Clean, modern, highly readable (like Quicksand, Montserrat, or similar)
   - Explain WHY these fonts work together and how they serve the brand

3. **Layout Guidelines**: Provide specific, actionable recommendations for:
   - Streaming Overlays: Placement of webcam, chat, alerts, game info
   - Social Media Banners: Composition, text placement, visual hierarchy
   - Text Masking Concepts: Creative techniques for integrating text with imagery

**Output Format:**
You MUST respond with valid JSON in this exact structure:
{{
  "theme_name": "A catchy, memorable name for this branding concept",
  "color_palette": ["#HEX1", "#HEX2", "#HEX3", "#HEX4", "#HEX5"],
  "typography": {{
    "primary_display": "Font Name (with style descriptor)",
    "secondary_body": "Font Name (with style descriptor)",
    "pairing_rationale": "Detailed explanation of why these fonts work together"
  }},
  "layout_guidelines": {{
    "streaming_overlay": "Specific recommendations for OBS/stream overlay design",
    "social_media_banner": "Specific recommendations for Twitter/Instagram header design",
    "text_masking_concepts": "Creative text-masking and typography integration techniques"
  }}
}}

**Important:**
- Respond ONLY with valid JSON, no additional text
- Be specific and actionable in all recommendations
- Consider the target audience (gamers, viewers, sponsors)
- Ensure designs are modern and aligned with current eSports trends
- Make recommendations that can be implemented by designers immediately"""

        return system_prompt
    
    def construct_user_prompt(self, vibe: str, game_context: str = None) -> str:
        """
        Format user input into a structured prompt for the AI.
        
        Args:
            vibe: User's creative direction or desired aesthetic
            game_context: Optional specific game or eSports context
            
        Returns:
            str: Formatted user prompt
        """
        context_addition = ""
        if game_context:
            context_addition = f"\n\n**Game/Context:** {game_context}"
        
        user_prompt = f"""Generate a complete visual identity concept based on this creative direction:

**Vibe/Direction:** {vibe}{context_addition}

Create a cohesive branding concept that captures this vision. Consider:
- What emotions should this brand evoke?
- What visual elements align with this direction?
- How can color, typography, and layout work together to achieve this aesthetic?

Provide your response as structured JSON following the exact format specified in the system prompt."""

        return user_prompt
    
    def get_json_schema(self) -> Dict[str, Any]:
        """
        Get the expected JSON output schema for validation.
        
        Returns:
            dict: JSON schema definition
        """
        schema = {
            "type": "object",
            "required": ["theme_name", "color_palette", "typography", "layout_guidelines"],
            "properties": {
                "theme_name": {
                    "type": "string",
                    "minLength": 5,
                    "maxLength": 100,
                    "description": "Catchy name for the branding concept"
                },
                "color_palette": {
                    "type": "array",
                    "minItems": 4,
                    "maxItems": 5,
                    "items": {
                        "type": "string",
                        "pattern": "^#[0-9A-Fa-f]{6}$",
                        "description": "Hex color code"
                    },
                    "description": "4-5 hex color codes for gradient use"
                },
                "typography": {
                    "type": "object",
                    "required": ["primary_display", "secondary_body", "pairing_rationale"],
                    "properties": {
                        "primary_display": {
                            "type": "string",
                            "minLength": 3,
                            "description": "Primary display font name"
                        },
                        "secondary_body": {
                            "type": "string",
                            "minLength": 3,
                            "description": "Secondary body font name"
                        },
                        "pairing_rationale": {
                            "type": "string",
                            "minLength": 20,
                            "description": "Explanation of font pairing"
                        }
                    }
                },
                "layout_guidelines": {
                    "type": "object",
                    "required": ["streaming_overlay", "social_media_banner", "text_masking_concepts"],
                    "properties": {
                        "streaming_overlay": {
                            "type": "string",
                            "minLength": 20,
                            "description": "Streaming overlay recommendations"
                        },
                        "social_media_banner": {
                            "type": "string",
                            "minLength": 20,
                            "description": "Social media banner recommendations"
                        },
                        "text_masking_concepts": {
                            "type": "string",
                            "minLength": 20,
                            "description": "Text masking techniques"
                        }
                    }
                }
            }
        }
        return schema
    
    def format_example_output(self) -> str:
        """
        Provide an example of expected output format.
        
        Returns:
            str: JSON string showing example output
        """
        example = {
            "theme_name": "Neon Velocity",
            "color_palette": ["#FF006E", "#8338EC", "#3A86FF", "#06FFA5", "#FFBE0B"],
            "typography": {
                "primary_display": "Orbitron Bold (Futuristic, geometric, high-tech)",
                "secondary_body": "Quicksand Medium (Clean, modern, highly readable)",
                "pairing_rationale": "Orbitron's geometric futurism creates immediate gaming credibility while Quicksand ensures all body text remains accessible and professional. The contrast between angular display and rounded body creates visual interest without sacrificing readability."
            },
            "layout_guidelines": {
                "streaming_overlay": "Position webcam in bottom-right with hexagonal frame using primary gradient (#FF006E to #8338EC). Place subscriber alerts in top-left with animated neon glow effect. Use semi-transparent panels with 20% opacity for chat and recent events.",
                "social_media_banner": "Create diagonal split composition with gradient background (top-left to bottom-right). Place team logo in left third, use text masking on player name with gradient fill. Add subtle animated scanline effect for tech aesthetic.",
                "text_masking_concepts": "Use gradient-filled text with knockout effect over gameplay footage. Apply chromatic aberration to headers for cyberpunk feel. Implement animated gradient shifts on hover states for interactive elements."
            }
        }
        return json.dumps(example, indent=2)


# Example usage and testing
if __name__ == "__main__":
    # Demonstrate the prompt engineering module
    engineer = PromptEngineer()
    
    print("=" * 80)
    print("SYSTEM PROMPT")
    print("=" * 80)
    print(engineer.get_system_prompt())
    print("\n")
    
    print("=" * 80)
    print("USER PROMPT EXAMPLE")
    print("=" * 80)
    test_vibe = "Futuristic cyberpunk with neon accents for a competitive FPS team"
    test_context = "Valorant"
    print(engineer.construct_user_prompt(test_vibe, test_context))
    print("\n")
    
    print("=" * 80)
    print("EXPECTED OUTPUT SCHEMA")
    print("=" * 80)
    print(json.dumps(engineer.get_json_schema(), indent=2))
    print("\n")
    
    print("=" * 80)
    print("EXAMPLE OUTPUT")
    print("=" * 80)
    print(engineer.format_example_output())

# Made with Bob
