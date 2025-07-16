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