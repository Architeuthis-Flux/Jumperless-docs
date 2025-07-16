#!/usr/bin/env python3
"""
Register the Jython lexer with Pygments.
This script should be run before building the documentation.
"""

import sys
from pathlib import Path

# Add current directory to path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def register_jython_lexer():
    """Register the Jython lexer and style with Pygments."""
    try:
        from pygments.lexers import get_lexer_by_name
        from pygments.lexers._mapping import LEXERS
        from pygments.styles import get_style_by_name
        from pygments.util import ClassNotFound
        from jython_lexer import JythonLexer
        from jython_style import JythonStyle
        
        # Check if lexer already registered
        try:
            get_lexer_by_name('jython')
            print("Jython lexer already registered")
        except:
            # Register the lexer
            LEXERS['JythonLexer'] = (
                'jython_lexer', 
                'Jython', 
                ('jython', 'jumperless-python', 'jpython'), 
                ('*.jy', '*.jython', '*.jumperless.py'), 
                ('text/x-jython', 'application/x-jython')
            )
            print("✓ Jython lexer registered")
        
        # Register the style
        from pygments.styles import STYLE_MAP
        STYLE_MAP['jython'] = 'jython_style::JythonStyle'
        print("✓ Jython style registered")
        
        return True
        
    except Exception as e:
        print(f"! Failed to register Jython lexer/style: {e}")
        return False

if __name__ == "__main__":
    register_jython_lexer()

# Auto-register when this module is imported
register_jython_lexer() 