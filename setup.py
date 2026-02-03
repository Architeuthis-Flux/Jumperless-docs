"""
Setup script for Jumperless documentation with custom Pygments lexer
"""

from setuptools import setup, find_packages

setup(
    name="jumperless-docs",
    version="1.0.0",
    description="Jumperless documentation with custom Python lexer",
    packages=find_packages(),
    install_requires=[
        "pygments>=2.12.0",
    ],
    extras_require={
        "docs": [
            "mkdocs>=1.4.0",
            "pymdown-extensions>=9.0",
            "pygments>=2.12.0",
        ],
    },
    entry_points={
        'pygments.lexers': [
            'jumperless = jumperless_lexers.jumperless_lexer:JumperlessPythonLexer',
            'jumperless-python = jumperless_lexers.jumperless_lexer:JumperlessPythonLexer',
            'jython = jumperless_lexers.jumperless_lexer:JumperlessPythonLexer',
        ],
        'pygments.styles': [
            'jumperless = jumperless_lexers.jumperless_style:JumperlessStyle',
            'jumperless-light = jumperless_lexers.jumperless_style:JumperlessLightStyle',
        ],
    },
) 