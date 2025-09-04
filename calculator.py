#!/usr/bin/env python3
"""
Advanced Calculator Application
Main application file with rich UI and comprehensive functionality
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
from decimal import Decimal, InvalidOperation
from calculator_engine import CalculatorEngine
from calculator_theme import CalculatorTheme

class AdvancedCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.engine = CalculatorEngine()
        self.theme = CalculatorTheme()
        
        # Initialize variables
        self.display_var = tk.StringVar(value="0")
        self.history_var = tk.StringVar(value="")
        self.memory_value = 0
        self.history = []
        
        self.setup_window()
        self.create_widgets()
        self.apply_theme()
        self.bind_keyboard()
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("Advanced Calculator Pro")
        self.root.geometry("400x600")
        self.root.resizable(True, True)
        self.root.minsize(350, 500)
        
        # Center window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (400 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"400x600+{x}+{y}")
        
        # Configure grid weights for responsiveness
        self.root.grid_rowconfigure(0, weight=0)  # Menu
        self.root.grid_rowconfigure(1, weight=1)  # Display area
        self.root.grid_rowconfigure(2, weight=4)  # Button area
        self.root.grid_columnconfigure(0, weight=1)
        
    def create_widgets(self):
        """Create and layout all widgets"""
        self.create_menu()
        self.create_display_area()
        self.create_button_area()
        
    def create_menu(self):
        """Create the menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Clear History", command=self.clear_history)
        view_menu.add_separator()
        view_menu.add_command(label="Dark Theme", command=lambda: self.switch_theme("dark"))
        view_menu.add_command(label="Light Theme", command=lambda: self.switch_theme("light"))
        view_menu.add_command(label="Blue Theme", command=lambda: self.switch_theme("blue"))
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Keyboard Shortcuts", command=self.show_shortcuts)
        
    def create_display_area(self):
        """Create the display area with history and main display"""
        display_frame = ttk.Frame(self.root, padding="10")
        display_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(10, 5))
        display_frame.grid_columnconfigure(0, weight=1)
        
        # History display
        self.history_label = ttk.Label(
            display_frame, 
            textvariable=self.history_var, 
            font=("Segoe UI", 10),
            foreground="gray"
        )
        self.history_label.grid(row=0, column=0, sticky="e", pady=(0, 5))
        
        # Main display
        self.display_entry = ttk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Segoe UI", 24, "bold"),
            justify="right",
            state="readonly"
        )
        self.display_entry.grid(row=1, column=0, sticky="ew", ipady=15)
        
        # Memory indicator
        self.memory_label = ttk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 10),
            foreground="orange"
        )
        self.memory_label.grid(row=2, column=0, sticky="w", pady=(5, 0))
        
    def create_button_area(self):
        """Create the button grid"""
        button_frame = ttk.Frame(self.root, padding="10")
        button_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=(5, 10))
        
        # Configure grid weights for button area
        for i in range(7):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        
        # Button definitions: (text, row, col, command, style, columnspan)
        buttons = [
            # Memory and function row
            ("MC", 0, 0, lambda: self.memory_clear(), "function.TButton", 1),
            ("MR", 0, 1, lambda: self.memory_recall(), "function.TButton", 1),
            ("M+", 0, 2, lambda: self.memory_add(), "function.TButton", 1),
            ("M-", 0, 3, lambda: self.memory_subtract(), "function.TButton", 1),
            
            # Scientific functions row
            ("√", 1, 0, lambda: self.scientific_function("sqrt"), "scientific.TButton", 1),
            ("x²", 1, 1, lambda: self.scientific_function("square"), "scientific.TButton", 1),
            ("1/x", 1, 2, lambda: self.scientific_function("reciprocal"), "scientific.TButton", 1),
            ("±", 1, 3, lambda: self.toggle_sign(), "scientific.TButton", 1),
            
            # Clear and backspace row
            ("C", 2, 0, lambda: self.clear(), "clear.TButton", 1),
            ("CE", 2, 1, lambda: self.clear_entry(), "clear.TButton", 1),
            ("⌫", 2, 2, lambda: self.backspace(), "clear.TButton", 1),
            ("÷", 2, 3, lambda: self.operator("/"), "operator.TButton", 1),
            
            # Number and operation rows
            ("7", 3, 0, lambda: self.number_input("7"), "number.TButton", 1),
            ("8", 3, 1, lambda: self.number_input("8"), "number.TButton", 1),
            ("9", 3, 2, lambda: self.number_input("9"), "number.TButton", 1),
            ("×", 3, 3, lambda: self.operator("*"), "operator.TButton", 1),
            
            ("4", 4, 0, lambda: self.number_input("4"), "number.TButton", 1),
            ("5", 4, 1, lambda: self.number_input("5"), "number.TButton", 1),
            ("6", 4, 2, lambda: self.number_input("6"), "number.TButton", 1),
            ("-", 4, 3, lambda: self.operator("-"), "operator.TButton", 1),
            
            ("1", 5, 0, lambda: self.number_input("1"), "number.TButton", 1),
            ("2", 5, 1, lambda: self.number_input("2"), "number.TButton", 1),
            ("3", 5, 2, lambda: self.number_input("3"), "number.TButton", 1),
            ("+", 5, 3, lambda: self.operator("+"), "operator.TButton", 1),
            
            ("0", 6, 0, lambda: self.number_input("0"), "number.TButton", 2),
            (".", 6, 2, lambda: self.decimal_point(), "number.TButton", 1),
            ("=", 6, 3, lambda: self.calculate(), "equals.TButton", 1),
        ]
        
        self.buttons = {}
        for text, row, col, command, style, colspan in buttons:
            btn = ttk.Button(
                button_frame,
                text=text,
                command=command,
                style=style
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
            self.buttons[text] = btn
            
    def apply_theme(self):
        """Apply the current theme"""
        self.theme.apply_theme(self.root, "dark")  # Default to dark theme
        
    def bind_keyboard(self):
        """Bind keyboard shortcuts"""
        self.root.bind("<Key>", self.key_press)
        self.root.focus_set()
        
    def key_press(self, event):
        """Handle keyboard input"""
        key = event.char.lower()
        
        # Numbers
        if key in "0123456789":
            self.number_input(key)
        # Operators
        elif key == "+":
            self.operator("+")
        elif key == "-":
            self.operator("-")
        elif key == "*":
            self.operator("*")
        elif key == "/":
            self.operator("/")
        elif key == ".":
            self.decimal_point()
        elif key in ["=", "\r"]:  # Enter key
            self.calculate()
        elif event.keysym == "BackSpace":
            self.backspace()
        elif event.keysym == "Delete":
            self.clear()
        elif event.keysym == "Escape":
            self.clear_entry()
            
    def number_input(self, num):
        """Handle number button press"""
        current = self.display_var.get()
        if current == "0" or current == "Error":
            self.display_var.set(num)
        else:
            self.display_var.set(current + num)
            
    def decimal_point(self):
        """Handle decimal point input"""
        current = self.display_var.get()
        
        # Check if we need to reset display after an operation
        if self.engine.should_reset_display or current == "Error":
            self.display_var.set("0.")
            self.engine.should_reset_display = False
        elif "." not in current:
            self.display_var.set(current + ".")
                
    def operator(self, op):
        """Handle operator button press"""
        try:
            current_value = float(self.display_var.get())
            result = self.engine.operator(op, current_value)
            
            # Update history display
            if self.engine.pending_operation:
                op_symbol = {"*": "×", "/": "÷"}.get(op, op)
                self.history_var.set(f"{self.engine.stored_value} {op_symbol}")
            
            self.display_var.set(str(result))
            
        except (ValueError, ZeroDivisionError) as e:
            self.display_var.set("Error")
            messagebox.showerror("Error", str(e))
            
    def calculate(self):
        """Handle equals button press"""
        try:
            current_value = float(self.display_var.get())
            result = self.engine.calculate(current_value)
            
            # Add to history
            if self.engine.last_operation:
                op_symbol = {"*": "×", "/": "÷"}.get(self.engine.last_operation, self.engine.last_operation)
                history_entry = f"{self.engine.last_operand} {op_symbol} {current_value} = {result}"
                self.history.append(history_entry)
                
            self.display_var.set(str(result))
            self.history_var.set("")
            
        except (ValueError, ZeroDivisionError) as e:
            self.display_var.set("Error")
            self.history_var.set("")
            messagebox.showerror("Error", str(e))
            
    def scientific_function(self, func):
        """Handle scientific function buttons"""
        try:
            current_value = float(self.display_var.get())
            result = self.engine.scientific_function(func, current_value)
            self.display_var.set(str(result))
            
            # Add to history
            func_names = {
                "sqrt": "√",
                "square": "²",
                "reciprocal": "1/x"
            }
            history_entry = f"{func_names.get(func, func)}({current_value}) = {result}"
            self.history.append(history_entry)
            
        except (ValueError, ZeroDivisionError) as e:
            self.display_var.set("Error")
            messagebox.showerror("Error", str(e))
            
    def toggle_sign(self):
        """Toggle the sign of the current number"""
        try:
            current = float(self.display_var.get())
            self.display_var.set(str(-current))
        except ValueError:
            pass
            
    def clear(self):
        """Clear everything"""
        self.display_var.set("0")
        self.history_var.set("")
        self.engine.clear()
        
    def clear_entry(self):
        """Clear current entry"""
        self.display_var.set("0")
        
    def backspace(self):
        """Remove last character"""
        current = self.display_var.get()
        if len(current) > 1 and current != "Error":
            self.display_var.set(current[:-1])
        else:
            self.display_var.set("0")
            
    def memory_clear(self):
        """Clear memory"""
        self.memory_value = 0
        self.memory_label.config(text="")
        
    def memory_recall(self):
        """Recall memory value"""
        self.display_var.set(str(self.memory_value))
        
    def memory_add(self):
        """Add current value to memory"""
        try:
            current = float(self.display_var.get())
            self.memory_value += current
            self.memory_label.config(text="M" if self.memory_value != 0 else "")
        except ValueError:
            pass
            
    def memory_subtract(self):
        """Subtract current value from memory"""
        try:
            current = float(self.display_var.get())
            self.memory_value -= current
            self.memory_label.config(text="M" if self.memory_value != 0 else "")
        except ValueError:
            pass
            
    def switch_theme(self, theme_name):
        """Switch application theme"""
        self.theme.apply_theme(self.root, theme_name)
        
    def clear_history(self):
        """Clear calculation history"""
        self.history.clear()
        messagebox.showinfo("History", "Calculation history cleared.")
        
    def show_about(self):
        """Show about dialog"""
        messagebox.showinfo(
            "About Advanced Calculator",
            "Advanced Calculator Pro v1.0\n\n"
            "A feature-rich calculator with:\n"
            "• Basic arithmetic operations\n"
            "• Scientific functions\n"
            "• Memory operations\n"
            "• Multiple themes\n"
            "• Keyboard shortcuts\n\n"
            "Created with Python and tkinter"
        )
        
    def show_shortcuts(self):
        """Show keyboard shortcuts dialog"""
        shortcuts = """
Keyboard Shortcuts:

Numbers: 0-9
Operations: +, -, *, /
Decimal: .
Calculate: Enter or =
Backspace: Backspace
Clear Entry: Escape
Clear All: Delete

Memory Operations:
Use mouse clicks on memory buttons
        """
        messagebox.showinfo("Keyboard Shortcuts", shortcuts)
        
    def run(self):
        """Start the calculator application"""
        self.root.mainloop()

if __name__ == "__main__":
    calculator = AdvancedCalculator()
    calculator.run()