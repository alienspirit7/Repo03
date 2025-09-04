#!/usr/bin/env python3
"""
Calculator Theme Module
Handles styling and theming for the calculator application
"""

import tkinter as tk
from tkinter import ttk

class CalculatorTheme:
    def __init__(self):
        self.themes = {
            "dark": {
                "bg": "#2d2d30",
                "fg": "#ffffff",
                "select_bg": "#404040",
                "button_bg": "#404040",
                "button_fg": "#ffffff",
                "button_active": "#505050",
                "number_bg": "#505050",
                "number_fg": "#ffffff",
                "operator_bg": "#ff9500",
                "operator_fg": "#ffffff",
                "equals_bg": "#ff9500",
                "equals_fg": "#ffffff",
                "function_bg": "#606060",
                "function_fg": "#ffffff",
                "clear_bg": "#a0a0a0",
                "clear_fg": "#000000",
                "scientific_bg": "#707070",
                "scientific_fg": "#ffffff",
                "entry_bg": "#1e1e1e",
                "entry_fg": "#ffffff",
                "entry_select_bg": "#404040"
            },
            "light": {
                "bg": "#f0f0f0",
                "fg": "#000000",
                "select_bg": "#e0e0e0",
                "button_bg": "#e1e1e1",
                "button_fg": "#000000",
                "button_active": "#d0d0d0",
                "number_bg": "#ffffff",
                "number_fg": "#000000",
                "operator_bg": "#0078d4",
                "operator_fg": "#ffffff",
                "equals_bg": "#0078d4",
                "equals_fg": "#ffffff",
                "function_bg": "#e1e1e1",
                "function_fg": "#000000",
                "clear_bg": "#ff6b6b",
                "clear_fg": "#ffffff",
                "scientific_bg": "#4ecdc4",
                "scientific_fg": "#ffffff",
                "entry_bg": "#ffffff",
                "entry_fg": "#000000",
                "entry_select_bg": "#0078d4"
            },
            "blue": {
                "bg": "#1e3a5f",
                "fg": "#ffffff",
                "select_bg": "#2a4a6b",
                "button_bg": "#2a4a6b",
                "button_fg": "#ffffff",
                "button_active": "#365577",
                "number_bg": "#3d5a7a",
                "number_fg": "#ffffff",
                "operator_bg": "#4a9eff",
                "operator_fg": "#ffffff",
                "equals_bg": "#4a9eff",
                "equals_fg": "#ffffff",
                "function_bg": "#2a4a6b",
                "function_fg": "#ffffff",
                "clear_bg": "#ff6b6b",
                "clear_fg": "#ffffff",
                "scientific_bg": "#5fb3d4",
                "scientific_fg": "#ffffff",
                "entry_bg": "#0f1e2e",
                "entry_fg": "#ffffff",
                "entry_select_bg": "#4a9eff"
            }
        }
        
    def apply_theme(self, root, theme_name):
        """
        Apply a theme to the calculator
        Args:
            root: Root tkinter window
            theme_name: Name of theme to apply
        """
        if theme_name not in self.themes:
            theme_name = "dark"  # Default to dark theme
            
        theme = self.themes[theme_name]
        style = ttk.Style()
        
        # Configure root window
        root.configure(bg=theme["bg"])
        
        # Configure ttk styles
        style.theme_use("clam")  # Use clam as base theme
        
        # Configure Frame styles
        style.configure(
            "TFrame",
            background=theme["bg"],
            borderwidth=0
        )
        
        # Configure Label styles
        style.configure(
            "TLabel",
            background=theme["bg"],
            foreground=theme["fg"],
            font=("Segoe UI", 10)
        )
        
        # Configure Entry styles
        style.configure(
            "TEntry",
            fieldbackground=theme["entry_bg"],
            foreground=theme["entry_fg"],
            borderwidth=2,
            insertcolor=theme["entry_fg"],
            selectbackground=theme["entry_select_bg"]
        )
        
        style.map(
            "TEntry",
            focuscolor=[("!focus", theme["entry_bg"])]
        )
        
        # Configure button styles
        self._configure_button_styles(style, theme)
        
    def _configure_button_styles(self, style, theme):
        """Configure all button styles"""
        
        # Number buttons
        style.configure(
            "number.TButton",
            background=theme["number_bg"],
            foreground=theme["number_fg"],
            borderwidth=1,
            font=("Segoe UI", 14, "bold"),
            focuscolor="none"
        )
        
        style.map(
            "number.TButton",
            background=[
                ("active", theme["button_active"]),
                ("pressed", theme["select_bg"])
            ]
        )
        
        # Operator buttons
        style.configure(
            "operator.TButton",
            background=theme["operator_bg"],
            foreground=theme["operator_fg"],
            borderwidth=1,
            font=("Segoe UI", 14, "bold"),
            focuscolor="none"
        )
        
        style.map(
            "operator.TButton",
            background=[
                ("active", self._lighten_color(theme["operator_bg"])),
                ("pressed", self._darken_color(theme["operator_bg"]))
            ]
        )
        
        # Equals button
        style.configure(
            "equals.TButton",
            background=theme["equals_bg"],
            foreground=theme["equals_fg"],
            borderwidth=1,
            font=("Segoe UI", 16, "bold"),
            focuscolor="none"
        )
        
        style.map(
            "equals.TButton",
            background=[
                ("active", self._lighten_color(theme["equals_bg"])),
                ("pressed", self._darken_color(theme["equals_bg"]))
            ]
        )
        
        # Function buttons (MC, MR, M+, M-)
        style.configure(
            "function.TButton",
            background=theme["function_bg"],
            foreground=theme["function_fg"],
            borderwidth=1,
            font=("Segoe UI", 11, "bold"),
            focuscolor="none"
        )
        
        style.map(
            "function.TButton",
            background=[
                ("active", self._lighten_color(theme["function_bg"])),
                ("pressed", self._darken_color(theme["function_bg"]))
            ]
        )
        
        # Clear buttons (C, CE, Backspace)
        style.configure(
            "clear.TButton",
            background=theme["clear_bg"],
            foreground=theme["clear_fg"],
            borderwidth=1,
            font=("Segoe UI", 12, "bold"),
            focuscolor="none"
        )
        
        style.map(
            "clear.TButton",
            background=[
                ("active", self._lighten_color(theme["clear_bg"])),
                ("pressed", self._darken_color(theme["clear_bg"]))
            ]
        )
        
        # Scientific function buttons
        style.configure(
            "scientific.TButton",
            background=theme["scientific_bg"],
            foreground=theme["scientific_fg"],
            borderwidth=1,
            font=("Segoe UI", 11, "bold"),
            focuscolor="none"
        )
        
        style.map(
            "scientific.TButton",
            background=[
                ("active", self._lighten_color(theme["scientific_bg"])),
                ("pressed", self._darken_color(theme["scientific_bg"]))
            ]
        )
        
    def _lighten_color(self, color):
        """Lighten a hex color by 20%"""
        try:
            # Remove # if present
            color = color.lstrip('#')
            # Convert to RGB
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            # Lighten by 20%
            rgb = tuple(min(255, int(c * 1.2)) for c in rgb)
            # Convert back to hex
            return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        except:
            return color
            
    def _darken_color(self, color):
        """Darken a hex color by 20%"""
        try:
            # Remove # if present
            color = color.lstrip('#')
            # Convert to RGB
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            # Darken by 20%
            rgb = tuple(max(0, int(c * 0.8)) for c in rgb)
            # Convert back to hex
            return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        except:
            return color
            
    def get_available_themes(self):
        """Get list of available theme names"""
        return list(self.themes.keys())
        
    def add_custom_theme(self, name, theme_dict):
        """
        Add a custom theme
        Args:
            name: Theme name
            theme_dict: Dictionary with theme colors
        """
        self.themes[name] = theme_dict