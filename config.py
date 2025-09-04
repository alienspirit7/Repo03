#!/usr/bin/env python3
"""
Calculator Configuration Module
Handles configuration settings and constants
"""

import os
import json
from pathlib import Path

class CalculatorConfig:
    def __init__(self):
        self.config_dir = Path.home() / ".advanced_calculator"
        self.config_file = self.config_dir / "config.json"
        self.default_config = {
            "theme": "dark",
            "window_geometry": "400x600",
            "precision": 10,
            "angle_mode": "degrees",  # degrees or radians
            "sound_enabled": True,
            "auto_save": True,
            "font_size": 14,
            "show_history": True,
            "memory_persistent": False
        }
        self.config = self.load_config()
        
    def load_config(self):
        """Load configuration from file or create default"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                # Merge with defaults to ensure all keys exist
                config = self.default_config.copy()
                config.update(loaded_config)
                return config
            else:
                return self.default_config.copy()
        except (json.JSONDecodeError, IOError):
            return self.default_config.copy()
            
    def save_config(self):
        """Save current configuration to file"""
        try:
            # Create config directory if it doesn't exist
            self.config_dir.mkdir(exist_ok=True)
            
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
        except IOError as e:
            print(f"Warning: Could not save configuration: {e}")
            
    def get(self, key, default=None):
        """Get configuration value"""
        return self.config.get(key, default)
        
    def set(self, key, value):
        """Set configuration value"""
        self.config[key] = value
        if self.config.get("auto_save", True):
            self.save_config()
            
    def reset_to_defaults(self):
        """Reset configuration to defaults"""
        self.config = self.default_config.copy()
        self.save_config()

# Application constants
class Constants:
    APP_NAME = "Advanced Calculator Pro"
    VERSION = "1.0.0"
    AUTHOR = "Calculator Team"
    
    # Mathematical constants
    PI = 3.141592653589793
    E = 2.718281828459045
    
    # Display limits
    MAX_DIGITS = 15
    MAX_HISTORY_ENTRIES = 100
    
    # Button dimensions
    BUTTON_WIDTH = 8
    BUTTON_HEIGHT = 2
    
    # Font settings
    DISPLAY_FONT = ("Segoe UI", 24, "bold")
    BUTTON_FONT = ("Segoe UI", 12, "bold")
    HISTORY_FONT = ("Segoe UI", 10)
    
    # Colors (fallback if theme fails)
    DEFAULT_BG = "#2d2d30"
    DEFAULT_FG = "#ffffff"
    
    # Keyboard mappings
    KEY_MAPPINGS = {
        "0": "0", "1": "1", "2": "2", "3": "3", "4": "4",
        "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
        "+": "+", "-": "-", "*": "*", "/": "/",
        "=": "=", "Return": "=", "Enter": "=",
        ".": ".", ",": ".",
        "BackSpace": "backspace",
        "Delete": "clear",
        "Escape": "clear_entry",
        "c": "clear",
        "C": "clear"
    }
    
    # Scientific function mappings
    SCIENTIFIC_FUNCTIONS = {
        "sqrt": "√",
        "square": "x²", 
        "reciprocal": "1/x",
        "sin": "sin",
        "cos": "cos", 
        "tan": "tan",
        "log": "log",
        "ln": "ln",
        "exp": "exp",
        "factorial": "n!",
        "abs": "|x|",
        "percent": "%"
    }

# Error messages
class ErrorMessages:
    DIVISION_BY_ZERO = "Cannot divide by zero"
    INVALID_INPUT = "Invalid input"
    OVERFLOW = "Number too large"
    UNDERFLOW = "Number too small"
    INVALID_OPERATION = "Invalid operation"
    SQRT_NEGATIVE = "Cannot calculate square root of negative number"
    LOG_INVALID = "Logarithm undefined for non-positive numbers"
    FACTORIAL_INVALID = "Factorial only defined for non-negative integers"
    GENERAL_ERROR = "An error occurred"

# Help text
class HelpText:
    ABOUT = """
Advanced Calculator Pro v1.0

A feature-rich scientific calculator with:
• Basic arithmetic operations (+, -, ×, ÷)
• Scientific functions (√, x², 1/x, etc.)
• Memory operations (MC, MR, M+, M-)
• Multiple themes (Dark, Light, Blue)
• Keyboard shortcuts support
• Calculation history
• Configurable settings

Created with Python and tkinter
    """.strip()
    
    KEYBOARD_SHORTCUTS = """
Keyboard Shortcuts:

Numbers: 0-9
Operations: + - * /
Decimal point: . or ,
Calculate: Enter or =
Backspace: Backspace
Clear entry: Escape
Clear all: Delete or C

Memory Operations:
Use mouse clicks on memory buttons

Scientific Functions:
Use mouse clicks on function buttons
    """.strip()
    
    MEMORY_HELP = """
Memory Operations:

MC (Memory Clear): Clears the memory
MR (Memory Recall): Recalls the stored value
M+ (Memory Add): Adds current value to memory
M- (Memory Subtract): Subtracts current value from memory

The 'M' indicator shows when memory contains a value.
    """.strip()

# Configuration instance (singleton)
config = CalculatorConfig()