"""
Validation utilities for branding concept data.

This module provides functions to validate JSON responses against
the expected schema and ensure data quality.
"""

import re
from typing import Dict, Any, List, Tuple


def validate_hex_color(color: str) -> bool:
    """
    Validate that a string is a valid hex color code.
    
    Args:
        color: String to validate
        
    Returns:
        bool: True if valid hex color, False otherwise
    """
    if not isinstance(color, str):
        return False
    
    # Check format: #RRGGBB
    pattern = r'^#[0-9A-Fa-f]{6}$'
    return bool(re.match(pattern, color))


def validate_color_palette(palette: List[str]) -> Tuple[bool, str]:
    """
    Validate a color palette.
    
    Args:
        palette: List of color hex codes
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(palette, list):
        return False, "Color palette must be a list"
    
    if not (4 <= len(palette) <= 5):
        return False, "Color palette must contain 4-5 colors"
    
    for i, color in enumerate(palette):
        if not validate_hex_color(color):
            return False, f"Invalid hex color at index {i}: {color}"
    
    return True, ""


def validate_typography(typography: Dict[str, str]) -> Tuple[bool, str]:
    """
    Validate typography object.
    
    Args:
        typography: Typography dictionary
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(typography, dict):
        return False, "Typography must be a dictionary"
    
    required_fields = ["primary_display", "secondary_body", "pairing_rationale"]
    for field in required_fields:
        if field not in typography:
            return False, f"Missing required field: {field}"
        
        if not isinstance(typography[field], str):
            return False, f"Field {field} must be a string"
        
        if len(typography[field].strip()) < 3:
            return False, f"Field {field} is too short"
    
    return True, ""


def validate_layout_guidelines(layout: Dict[str, str]) -> Tuple[bool, str]:
    """
    Validate layout guidelines object.
    
    Args:
        layout: Layout guidelines dictionary
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(layout, dict):
        return False, "Layout guidelines must be a dictionary"
    
    required_fields = ["streaming_overlay", "social_media_banner", "text_masking_concepts"]
    for field in required_fields:
        if field not in layout:
            return False, f"Missing required field: {field}"
        
        if not isinstance(layout[field], str):
            return False, f"Field {field} must be a string"
        
        if len(layout[field].strip()) < 20:
            return False, f"Field {field} is too short (minimum 20 characters)"
    
    return True, ""


def validate_branding_concept(concept: Dict[str, Any]) -> Tuple[bool, str]:
    """
    Validate a complete branding concept.
    
    Args:
        concept: Branding concept dictionary
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not isinstance(concept, dict):
        return False, "Concept must be a dictionary"
    
    # Check required top-level fields
    required_fields = ["theme_name", "color_palette", "typography", "layout_guidelines"]
    for field in required_fields:
        if field not in concept:
            return False, f"Missing required field: {field}"
    
    # Validate theme_name
    if not isinstance(concept["theme_name"], str):
        return False, "theme_name must be a string"
    
    if not (5 <= len(concept["theme_name"]) <= 100):
        return False, "theme_name must be between 5 and 100 characters"
    
    # Validate color_palette
    is_valid, error = validate_color_palette(concept["color_palette"])
    if not is_valid:
        return False, f"Color palette validation failed: {error}"
    
    # Validate typography
    is_valid, error = validate_typography(concept["typography"])
    if not is_valid:
        return False, f"Typography validation failed: {error}"
    
    # Validate layout_guidelines
    is_valid, error = validate_layout_guidelines(concept["layout_guidelines"])
    if not is_valid:
        return False, f"Layout guidelines validation failed: {error}"
    
    return True, ""


def format_validation_error(error_message: str) -> Dict[str, Any]:
    """
    Format a validation error into a standard response structure.
    
    Args:
        error_message: The validation error message
        
    Returns:
        dict: Formatted error response
    """
    return {
        "success": False,
        "concept": None,
        "error": f"Validation error: {error_message}",
        "metadata": {
            "validation_failed": True
        }
    }


# Example usage and testing
if __name__ == "__main__":
    print("=" * 80)
    print("VALIDATION UTILITIES DEMONSTRATION")
    print("=" * 80)
    
    # Test hex color validation
    print("\n1. Hex Color Validation:")
    test_colors = ["#FF0000", "#ff0000", "#FFF", "FF0000", "#GGGGGG", "#123456"]
    for color in test_colors:
        is_valid = validate_hex_color(color)
        print(f"  {color:12} -> {'✓ Valid' if is_valid else '✗ Invalid'}")
    
    # Test color palette validation
    print("\n2. Color Palette Validation:")
    test_palettes = [
        ["#FF0000", "#00FF00", "#0000FF", "#FFFF00"],
        ["#FF0000", "#00FF00", "#0000FF"],  # Too few
        ["#FF0000", "invalid", "#0000FF", "#FFFF00"],  # Invalid color
    ]
    for i, palette in enumerate(test_palettes):
        is_valid, error = validate_color_palette(palette)
        status = "✓ Valid" if is_valid else f"✗ Invalid: {error}"
        print(f"  Palette {i+1}: {status}")
    
    # Test complete concept validation
    print("\n3. Complete Concept Validation:")
    valid_concept = {
        "theme_name": "Neon Velocity",
        "color_palette": ["#FF006E", "#8338EC", "#3A86FF", "#06FFA5"],
        "typography": {
            "primary_display": "Orbitron Bold",
            "secondary_body": "Quicksand Medium",
            "pairing_rationale": "These fonts create a perfect balance between futuristic and readable."
        },
        "layout_guidelines": {
            "streaming_overlay": "Position webcam in bottom-right with hexagonal frame.",
            "social_media_banner": "Create diagonal split composition with gradient background.",
            "text_masking_concepts": "Use gradient-filled text with knockout effect."
        }
    }
    
    is_valid, error = validate_branding_concept(valid_concept)
    if is_valid:
        print("  ✓ Valid concept structure")
    else:
        print(f"  ✗ Invalid: {error}")
    
    # Test invalid concept
    invalid_concept = {
        "theme_name": "Test",
        "color_palette": ["#FF0000"],  # Too few colors
    }
    
    is_valid, error = validate_branding_concept(invalid_concept)
    if not is_valid:
        print(f"  ✓ Correctly identified invalid concept: {error}")

# Made with Bob
