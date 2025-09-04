# Advanced Calculator Pro

A feature-rich, modern calculator application built with Python and tkinter, featuring a sleek UI, scientific functions, and multiple themes.

## Features

### 🧮 Core Functionality
- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (×), Division (÷)
- **Scientific Functions**: Square root (√), Square (x²), Reciprocal (1/x), Sign toggle (±)
- **Memory Operations**: Memory Clear (MC), Recall (MR), Add (M+), Subtract (M-)
- **Precise Calculations**: Uses Python's Decimal module for accurate arithmetic

### 🎨 User Interface
- **Modern Design**: Clean, professional interface with rounded buttons
- **Multiple Themes**: Dark (default), Light, and Blue themes
- **Responsive Layout**: Resizable window that adapts to different sizes
- **Visual Feedback**: Button hover effects and active states
- **History Display**: Shows current operation being performed
- **Memory Indicator**: Visual indicator when memory contains a value

### ⌨️ Input Methods
- **Mouse Input**: Click buttons to perform operations
- **Keyboard Support**: Full keyboard shortcuts for all operations
- **Error Handling**: Comprehensive error detection and user-friendly messages

### 📱 Advanced Features
- **Calculation History**: Keeps track of previous calculations
- **Configuration**: Persistent settings storage
- **Help System**: Built-in help dialogs and keyboard shortcuts reference
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

### Prerequisites
- Python 3.7 or higher
- tkinter (usually included with Python)

### Quick Start
1. Download all the Python files to a folder
2. Run the calculator:
   ```bash
   python calculator.py
   ```

## File Structure

```
calculator/
│
├── calculator.py           # Main application file
├── calculator_engine.py    # Mathematical operations engine
├── calculator_theme.py     # Theme and styling system
├── config.py              # Configuration management
├── requirements.txt       # Dependencies (Python standard library only)
└── README.md             # This documentation
```

## Usage

### Basic Operations
1. **Numbers**: Click number buttons (0-9) or use keyboard
2. **Operations**: Click +, -, ×, ÷ or use keyboard (+, -, *, /)
3. **Calculate**: Click = or press Enter
4. **Decimal**: Click . or use keyboard decimal point
5. **Clear**: 
   - C or Delete: Clear everything
   - CE or Escape: Clear current entry
   - ⌫ or Backspace: Remove last digit

### Scientific Functions
- **√**: Square root of current number
- **x²**: Square of current number  
- **1/x**: Reciprocal of current number
- **±**: Toggle sign of current number

### Memory Operations
- **MC**: Clear memory
- **MR**: Recall value from memory
- **M+**: Add current display to memory
- **M-**: Subtract current display from memory
- **M indicator**: Shows when memory contains a non-zero value

### Keyboard Shortcuts
| Key | Function |
|-----|----------|
| 0-9 | Number input |
| +, -, *, / | Basic operations |
| = or Enter | Calculate result |
| . or , | Decimal point |
| Backspace | Delete last digit |
| Delete or C | Clear all |
| Escape | Clear entry |

### Themes
Switch between themes using the **View** menu:
- **Dark Theme**: Modern dark interface (default)
- **Light Theme**: Clean light interface  
- **Blue Theme**: Professional blue color scheme

## Technical Details

### Architecture
The calculator uses a modular design with separate concerns:

- **calculator.py**: Main GUI application and event handling
- **calculator_engine.py**: Mathematical computation logic
- **calculator_theme.py**: Visual styling and theming
- **config.py**: Settings management and constants

### Mathematical Precision
- Uses Python's `Decimal` module for precise arithmetic
- Handles floating-point precision issues automatically
- Supports up to 15 significant digits
- Proper error handling for edge cases (division by zero, square root of negatives)

### Error Handling
- **Division by Zero**: Displays error message and resets
- **Invalid Operations**: Prevents invalid calculations
- **Overflow Protection**: Handles very large numbers gracefully
- **Input Validation**: Ensures only valid input is processed

## Customization

### Adding New Themes
You can add custom themes by modifying `calculator_theme.py`:

```python
# Add to themes dictionary in CalculatorTheme class
"custom": {
    "bg": "#your_background_color",
    "fg": "#your_foreground_color",
    # ... other color definitions
}
```

### Configuration Options
The calculator stores settings in `~/.advanced_calculator/config.json`:

- Theme preference
- Window size and position
- Precision settings
- Feature toggles

## Troubleshooting

### Common Issues

**Calculator won't start**:
- Ensure Python 3.7+ is installed
- Check that tkinter is available: `python -c "import tkinter"`

**Display issues**:
- Try switching themes from the View menu
- Resize the window if buttons appear cramped

**Keyboard not working**:
- Click on the calculator window to ensure it has focus
- Check that Num Lock is enabled for number pad input

### Error Messages
- **"Cannot divide by zero"**: Attempted division by zero
- **"Invalid input"**: Non-numeric input in calculation
- **"Number too large"**: Result exceeds display limits

## Contributing

This calculator is designed to be educational and extensible. To add features:

1. **New Functions**: Add to `calculator_engine.py`
2. **UI Changes**: Modify `calculator.py`
3. **Themes**: Extend `calculator_theme.py`
4. **Settings**: Update `config.py`

## License

This project is open source and available under the MIT License.

## Version History

- **v1.0.0**: Initial release with full calculator functionality
  - Basic and scientific operations
  - Multiple themes
  - Memory functions
  - Keyboard support
  - Configuration system

---

**Enjoy calculating! 🧮✨**