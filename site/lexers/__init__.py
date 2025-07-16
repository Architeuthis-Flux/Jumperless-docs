"""
Jumperless Python Lexer and Style for Pygments
"""

from .jumperless_lexer import JumperlessPythonLexer, JumperlessTokens
from .jumperless_style import JumperlessStyle, JumperlessLightStyle

# Register the lexer and styles with Pygments
def register():
    """Register the custom lexer and styles with Pygments."""
    try:
        from pygments.lexers import get_lexer_by_name
        from pygments.styles import get_style_by_name
        from pygments.util import ClassNotFound
        
        # Try to register if not already registered
        try:
            get_lexer_by_name('jumperless')
        except ClassNotFound:
            # Register lexer
            from pygments.lexers import _lexer_cache
            for alias in JumperlessPythonLexer.aliases:
                _lexer_cache[alias] = ('docs.lexers.jumperless_lexer', 'JumperlessPythonLexer')
        
        # Try to register styles
        try:
            get_style_by_name('jumperless')
        except ClassNotFound:
            from pygments.styles import _style_cache
            _style_cache['jumperless'] = ('docs.lexers.jumperless_style', 'JumperlessStyle')
            _style_cache['jumperless-light'] = ('docs.lexers.jumperless_style', 'JumperlessLightStyle')
            
    except ImportError:
        pass  # Pygments not available

# Auto-register when imported
register()

__all__ = ['JumperlessPythonLexer', 'JumperlessTokens', 'JumperlessStyle', 'JumperlessLightStyle', 'register'] 