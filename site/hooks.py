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
        from pygments.styles import get_style_by_name
        
        # Test all lexer aliases
        lexer_aliases = ['jython', 'jumperless-python', 'jumperless']
        for alias in lexer_aliases:
            try:
                get_lexer_by_name(alias)
                print(f"✓ Jumperless lexer '{alias}' is available")
            except Exception as e:
                print(f"⚠ Jumperless lexer '{alias}' not available: {e}")
        
        # Test custom styles
        try:
            get_style_by_name('jumperless')
            print("✓ Jumperless style is available")
        except Exception as e:
            print(f"⚠ Jumperless style not available: {e}")
            
    except Exception as e:
        print(f"⚠ Error checking Jumperless lexer/style: {e}")
    
    return config 