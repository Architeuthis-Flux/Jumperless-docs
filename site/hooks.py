"""
MkDocs hooks for registering custom Pygments lexers and styles
"""

def on_config(config):
    """
    This hook runs when MkDocs loads the configuration.
    Since the lexer is now registered via entry points, we just verify it's available.
    """
    try:
        from pygments.lexers import get_lexer_by_name
        get_lexer_by_name('jython')
        print("✓ Jumperless Python lexer is available")
    except Exception as e:
        print(f"⚠ Jumperless Python lexer not available: {e}")
    
    return config 