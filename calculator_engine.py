#!/usr/bin/env python3
"""
Calculator Engine Module
Handles all mathematical operations and calculations
"""

import math
from decimal import Decimal, InvalidOperation, getcontext

# Set decimal precision for accurate calculations
getcontext().prec = 15

class CalculatorEngine:
    def __init__(self):
        self.reset()
        
    def reset(self):
        """Reset the calculator engine to initial state"""
        self.stored_value = 0
        self.pending_operation = None
        self.last_operation = None
        self.last_operand = 0
        self.should_reset_display = False  # This is crucial!
        
    def clear(self):
        """Clear all stored values and operations"""
        self.reset()
        
    def operator(self, operation, current_value):
        """
        Handle operator input
        Args:
            operation: The operation symbol (+, -, *, /)
            current_value: Current display value
        Returns:
            Value to display
        """
        if self.pending_operation is not None:
            # If there's already a pending operation, calculate it first
            result = self._perform_calculation(self.stored_value, current_value, self.pending_operation)
            self.stored_value = result
        else:
            self.stored_value = current_value
            
        self.pending_operation = operation
        self.should_reset_display = True  # This MUST be set to True
        
        # Return the current value for display (don't change what user sees)
        return current_value
        
    def calculate(self, current_value):
        """
        Perform the pending calculation
        Args:
            current_value: Current display value
        Returns:
            Calculation result
        """
        if self.pending_operation is None:
            return current_value
            
        result = self._perform_calculation(self.stored_value, current_value, self.pending_operation)
        
        # Store for repeat calculations
        self.last_operation = self.pending_operation
        self.last_operand = self.stored_value
        
        # Reset pending operation
        self.pending_operation = None
        self.stored_value = result
        self.should_reset_display = True
        
        return result
        
    def _perform_calculation(self, operand1, operand2, operation):
        """
        Perform the actual calculation
        Args:
            operand1: First operand
            operand2: Second operand  
            operation: Operation to perform
        Returns:
            Calculation result
        Raises:
            ValueError: For invalid operations
            ZeroDivisionError: For division by zero
        """
        try:
            # Use Decimal for precise calculations
            a = Decimal(str(operand1))
            b = Decimal(str(operand2))
            
            if operation == "+":
                result = a + b
            elif operation == "-":
                result = a - b
            elif operation == "*":
                result = a * b
            elif operation == "/":
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = a / b
            else:
                raise ValueError(f"Unknown operation: {operation}")
                
            # Convert back to float and format
            result_float = float(result)
            
            # Format the result to remove unnecessary decimal places
            if result_float == int(result_float):
                return int(result_float)
            else:
                # Round to avoid floating point precision issues
                return round(result_float, 10)
                
        except (InvalidOperation, ValueError) as e:
            raise ValueError(f"Invalid calculation: {e}")
            
    def scientific_function(self, function, value):
        """
        Perform scientific functions
        Args:
            function: Function name (sqrt, square, reciprocal, etc.)
            value: Input value
        Returns:
            Function result
        Raises:
            ValueError: For invalid input or function
        """
        try:
            if function == "sqrt":
                if value < 0:
                    raise ValueError("Cannot calculate square root of negative number")
                result = math.sqrt(value)
                
            elif function == "square":
                result = value ** 2
                
            elif function == "reciprocal":
                if value == 0:
                    raise ZeroDivisionError("Cannot calculate reciprocal of zero")
                result = 1 / value
                
            elif function == "sin":
                result = math.sin(math.radians(value))
                
            elif function == "cos":
                result = math.cos(math.radians(value))
                
            elif function == "tan":
                result = math.tan(math.radians(value))
                
            elif function == "log":
                if value <= 0:
                    raise ValueError("Logarithm undefined for non-positive numbers")
                result = math.log10(value)
                
            elif function == "ln":
                if value <= 0:
                    raise ValueError("Natural logarithm undefined for non-positive numbers")
                result = math.log(value)
                
            elif function == "exp":
                result = math.exp(value)
                
            elif function == "factorial":
                if value < 0 or value != int(value):
                    raise ValueError("Factorial only defined for non-negative integers")
                result = math.factorial(int(value))
                
            elif function == "abs":
                result = abs(value)
                
            elif function == "percent":
                result = value / 100
                
            else:
                raise ValueError(f"Unknown function: {function}")
                
            # Format the result
            if result == int(result):
                return int(result)
            else:
                return round(result, 10)
                
        except (ValueError, OverflowError) as e:
            raise ValueError(f"Function error: {e}")
            
    def power(self, base, exponent):
        """
        Calculate base raised to exponent
        Args:
            base: Base value
            exponent: Exponent value
        Returns:
            Power result
        """
        try:
            result = base ** exponent
            if result == int(result):
                return int(result)
            else:
                return round(result, 10)
        except OverflowError:
            raise ValueError("Result too large to display")
            
    def percentage_calculation(self, base_value, percentage):
        """
        Calculate percentage of a value
        Args:
            base_value: Base value
            percentage: Percentage value
        Returns:
            Percentage result
        """
        result = (base_value * percentage) / 100
        if result == int(result):
            return int(result)
        else:
            return round(result, 10)
            
    def format_number(self, number):
        """
        Format number for display
        Args:
            number: Number to format
        Returns:
            Formatted number string
        """
        if isinstance(number, (int, float)):
            if number == int(number):
                return str(int(number))
            else:
                # Remove trailing zeros
                return f"{number:g}"
        return str(number)