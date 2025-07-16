#!/usr/bin/env python3
"""
Setup script to register the Jython lexer with Pygments.
Run this script to make the custom lexer available to MkDocs.
"""

import sys
import os
from pathlib import Path

# Add current directory to Python path so we can import our lexer
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

try:
    from pygments.lexers import get_all_lexers, get_lexer_by_name
    from pygments import highlight
    from pygments.formatters import TerminalFormatter
    from jython_lexer import JythonLexer, get_jython_lexer
    from jython_style import JythonStyle
    print("✓ Successfully imported Pygments and custom lexer/style")
except ImportError as e:
    print(f"✗ Failed to import required modules: {e}")
    print("Make sure you have Pygments installed: pip install Pygments")
    sys.exit(1)

def register_lexer():
    """Register the Jython lexer with Pygments."""
    try:
        # Try to get the lexer by name to see if it's already registered
        lexer = get_lexer_by_name('jython')
        print("✓ Jython lexer is already registered")
        return True
    except:
        print("! Jython lexer not found in registry")
    
    # Manual registration using entry points simulation
    from pygments.lexers._mapping import LEXERS
    
    # Add our lexer to the mapping
    LEXERS['JythonLexer'] = (
        'jython_lexer', 
        'Jython', 
        ('jython', 'jumperless-python', 'jpython'), 
        ('*.jy', '*.jython', '*.jumperless.py'), 
        ('text/x-jython', 'application/x-jython')
    )
    
    print("✓ Manually registered Jython lexer")
    return True

def test_lexer():
    """Test the lexer with a sample code snippet."""
    test_code = """
# Jumperless Python Example
import jumperless

# Connect GPIO pins
connect(GPIO_1, D13)
connect(DAC0, A0)

# Set LED brightness
dac_set(DAC0, 128)

# Read sensor value
value = adc_get(ADC0)
print(f"Sensor reading: {value}")

# OLED display
oled_print("Hello Jumperless!")
"""
    
    try:
        lexer = JythonLexer()
        formatter = TerminalFormatter()
        result = highlight(test_code, lexer, formatter)
        print("✓ Lexer test successful")
        print("\nSample highlighted output (terminal colors):")
        print(result)
        return True
    except Exception as e:
        print(f"✗ Lexer test failed: {e}")
        return False

def create_mkdocs_hook():
    """Create a MkDocs hook to ensure lexer is registered during build."""
    hook_content = '''
"""
MkDocs hook to register custom Jython lexer.
This ensures the lexer is available during documentation generation.
"""

import sys
from pathlib import Path

def on_startup(command, dirty):
    """Called when MkDocs starts up."""
    # Add docs directory to Python path
    docs_dir = Path(__file__).parent
    if str(docs_dir) not in sys.path:
        sys.path.insert(0, str(docs_dir))
    
    try:
        # Import and register our custom lexer
        from jython_lexer import JythonLexer
        from jython_style import JythonStyle
        from pygments.lexers._mapping import LEXERS
        
        # Register the lexer
        LEXERS['JythonLexer'] = (
            'jython_lexer', 
            'Jython', 
            ('jython', 'jumperless-python', 'jpython'), 
            ('*.jy', '*.jython', '*.jumperless.py'), 
            ('text/x-jython', 'application/x-jython')
        )
        
        print("✓ Custom Jython lexer registered for MkDocs")
        
    except Exception as e:
        print(f"! Warning: Could not register Jython lexer: {e}")

def on_config(config):
    """Called after the config is loaded."""
    return config
'''
    
    hook_file = current_dir / "mkdocs_hooks.py"
    with open(hook_file, 'w') as f:
        f.write(hook_content.strip())
    
    print(f"✓ Created MkDocs hook at {hook_file}")
    return hook_file

def main():
    """Main setup function."""
    print("Setting up Jython lexer for MkDocs...\n")
    
    # Check if we can import everything
    success = True
    
    # Register the lexer
    if not register_lexer():
        success = False
    
    # Test the lexer
    if not test_lexer():
        success = False
    
    # Create MkDocs hook
    create_mkdocs_hook()
    
    if success:
        print("\n✓ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Update mkdocs.yml to include the hooks plugin")
        print("2. Use ```jython in your markdown files for Jumperless Python code")
        print("3. Run 'mkdocs build' or 'mkdocs serve' to test")
    else:
        print("\n✗ Setup completed with warnings")
        print("Check the error messages above and resolve any issues")

if __name__ == "__main__":
    main() 