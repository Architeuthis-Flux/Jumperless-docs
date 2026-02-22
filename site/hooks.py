"""
MkDocs hooks for registering custom Pygments lexers and styles
"""

def on_config(config):
    # Regenerate JUMPERLESS_FUNCTIONS in lexer from API reference before build
    try:
        import runpy
        import os
        script = os.path.join(os.path.dirname(__file__), "generate_lexer_from_api_ref.py")
        if os.path.isfile(script):
            runpy.run_path(script, run_name="__main__")
    except Exception as e:
        print(f"⚠ generate_lexer_from_api_ref: {e}")
    # Verify lexer/style availability
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