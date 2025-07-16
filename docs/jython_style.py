"""
Custom Pygments Style for Jython (Jumperless Python)
Defines a dark theme with specific colors for Jumperless-specific tokens.
"""

from pygments.style import Style
from pygments.token import (Keyword, Name, Comment, String, Error, Text, Number, 
                          Operator, Generic, Whitespace, Punctuation, Other, Literal)
from jython_lexer import JythonTokens

class JythonStyle(Style):
    """
    A dark color scheme for Jython (Jumperless Python) with vibrant colors
    for Jumperless-specific keywords and functions.
    """
    
    name = 'jython'
    
    background_color = "#282a36"  # Dark background
    highlight_color = "#44475a"   # Selection background
    line_number_color = "#6272a4" # Muted blue-gray for line numbers
    line_number_background_color = "#44475a"
    line_number_special_color = "#8be9fd"
    line_number_special_background_color = "#44475a"

    styles = {
        # Standard Python syntax
        Whitespace:                '#f8f8f2',
        Comment:                   'italic #6272a4',  # Muted blue-gray
        Comment.Preproc:           'noitalic #ff79c6', # Pink for preprocessor
        Comment.Special:           'italic bold #50fa7b', # Green for special comments

        Keyword:                   'bold #ff79c6',    # Pink for keywords
        Keyword.Pseudo:            'nobold #ff79c6',  # Pink for pseudo keywords
        Keyword.Type:              '#8be9fd',         # Cyan for types

        Operator:                  '#ff79c6',         # Pink for operators
        Operator.Word:             'bold #ff79c6',    # Bold pink for word operators

        Name:                      '#f8f8f2',         # Light gray for general names
        Name.Attribute:            '#50fa7b',         # Green for attributes
        Name.Builtin:              'italic #8be9fd',  # Cyan for builtins
        Name.Builtin.Pseudo:       '#8be9fd',         # Cyan for pseudo builtins
        Name.Class:                'underline #8be9fd', # Underlined cyan for classes
        Name.Constant:             '#bd93f9',         # Purple for constants
        Name.Decorator:            '#50fa7b',         # Green for decorators
        Name.Entity:               '#50fa7b',         # Green for entities
        Name.Exception:            'bold #ffb86c',    # Orange for exceptions
        Name.Function:             '#50fa7b',         # Green for functions
        Name.Property:             '#f8f8f2',         # Light gray for properties
        Name.Label:                '#8be9fd',         # Cyan for labels
        Name.Namespace:            '#f8f8f2',         # Light gray for namespaces
        Name.Other:                '#f8f8f2',         # Light gray for other names
        Name.Tag:                  '#ff79c6',         # Pink for tags
        Name.Variable:             '#f8f8f2',         # Light gray for variables
        Name.Variable.Class:       'italic #8be9fd',  # Italic cyan for class variables
        Name.Variable.Global:      'bold #ffb86c',    # Bold orange for global variables
        Name.Variable.Instance:    '#f8f8f2',         # Light gray for instance variables

        Number:                    '#bd93f9',         # Purple for numbers
        Number.Float:              '#bd93f9',         # Purple for floats
        Number.Hex:                '#bd93f9',         # Purple for hex
        Number.Integer:            '#bd93f9',         # Purple for integers
        Number.Long:               '#bd93f9',         # Purple for long integers
        Number.Oct:                '#bd93f9',         # Purple for octal

        Literal:                   '#f1fa8c',         # Yellow for literals
        Literal.Date:              '#f1fa8c',         # Yellow for dates

        String:                    '#f1fa8c',         # Yellow for strings
        String.Backtick:           '#f1fa8c',         # Yellow for backtick strings
        String.Char:               '#f1fa8c',         # Yellow for character strings
        String.Doc:                'italic #f1fa8c',  # Italic yellow for docstrings
        String.Double:             '#f1fa8c',         # Yellow for double-quoted strings
        String.Escape:             'bold #ff79c6',    # Bold pink for escape sequences
        String.Heredoc:            '#f1fa8c',         # Yellow for heredoc
        String.Interpol:           'bold #f1fa8c',    # Bold yellow for interpolation
        String.Other:              '#f1fa8c',         # Yellow for other strings
        String.Regex:              '#f1fa8c',         # Yellow for regex
        String.Single:             '#f1fa8c',         # Yellow for single-quoted strings
        String.Symbol:             '#f1fa8c',         # Yellow for symbols

        Generic:                   '#f8f8f2',         # Light gray for generic
        Generic.Deleted:           '#ff5555',         # Red for deleted
        Generic.Emph:              'italic #f8f8f2',  # Italic light gray for emphasis
        Generic.Error:             '#ff5555',         # Red for errors
        Generic.Heading:           'bold #6272a4',    # Bold muted blue for headings
        Generic.Inserted:          '#50fa7b',         # Green for inserted
        Generic.Output:            '#6272a4',         # Muted blue for output
        Generic.Prompt:            'bold #6272a4',    # Bold muted blue for prompts
        Generic.Strong:            'bold #f8f8f2',    # Bold light gray for strong
        Generic.Subheading:        'bold #6272a4',    # Bold muted blue for subheadings
        Generic.Traceback:         '#ff5555',         # Red for tracebacks

        Error:                     'bg:#ff5555 #f8f8f2', # Red background for errors

        # Custom Jython/Jumperless-specific token styles
        JythonTokens.JumperlessFunction:    'bold #ff00a2',     # Pink for Jumperless functions
        JythonTokens.JumperlessConstant:    'bold #4200ff',     # Purple for Jumperless constants
        JythonTokens.JumperlessType:        'bold #3aff00',     # Yellow/green for Jumperless types
        JythonTokens.JFSFunction:           'bold #00d4ff',     # Cyan for JFS functions
        JythonTokens.HardwareConstant:      'bold #7000ff',     # Different purple for hardware constants
    }

class JythonLightStyle(Style):
    """
    A light color scheme for Jython (Jumperless Python) for those who prefer light themes.
    """
    
    name = 'jython-light'
    
    background_color = "#f8f8f2"  # Light background
    highlight_color = "#e1e1e1"   # Selection background
    line_number_color = "#6272a4" # Muted blue-gray for line numbers
    line_number_background_color = "#f0f0f0"

    styles = {
        # Standard Python syntax for light theme
        Whitespace:                '#000000',
        Comment:                   'italic #6272a4',  # Muted blue-gray
        Comment.Preproc:           'noitalic #d63384', # Dark pink for preprocessor
        Comment.Special:           'italic bold #198754', # Dark green for special comments

        Keyword:                   'bold #d63384',    # Dark pink for keywords
        Keyword.Pseudo:            'nobold #d63384',  # Dark pink for pseudo keywords
        Keyword.Type:              '#0dcaf0',         # Dark cyan for types

        Operator:                  '#d63384',         # Dark pink for operators
        Operator.Word:             'bold #d63384',    # Bold dark pink for word operators

        Name:                      '#212529',         # Dark gray for general names
        Name.Attribute:            '#198754',         # Dark green for attributes
        Name.Builtin:              'italic #0dcaf0',  # Dark cyan for builtins
        Name.Builtin.Pseudo:       '#0dcaf0',         # Dark cyan for pseudo builtins
        Name.Class:                'underline #0dcaf0', # Underlined dark cyan for classes
        Name.Constant:             '#6f42c1',         # Dark purple for constants
        Name.Decorator:            '#198754',         # Dark green for decorators
        Name.Entity:               '#198754',         # Dark green for entities
        Name.Exception:            'bold #fd7e14',    # Dark orange for exceptions
        Name.Function:             '#198754',         # Dark green for functions
        Name.Property:             '#212529',         # Dark gray for properties
        Name.Label:                '#0dcaf0',         # Dark cyan for labels
        Name.Namespace:            '#212529',         # Dark gray for namespaces
        Name.Other:                '#212529',         # Dark gray for other names
        Name.Tag:                  '#d63384',         # Dark pink for tags
        Name.Variable:             '#212529',         # Dark gray for variables
        Name.Variable.Class:       'italic #0dcaf0',  # Italic dark cyan for class variables
        Name.Variable.Global:      'bold #fd7e14',    # Bold dark orange for global variables
        Name.Variable.Instance:    '#212529',         # Dark gray for instance variables

        Number:                    '#6f42c1',         # Dark purple for numbers
        String:                    '#ffc107',         # Dark yellow for strings
        String.Doc:                'italic #ffc107',  # Italic dark yellow for docstrings
        String.Escape:             'bold #d63384',    # Bold dark pink for escape sequences

        Error:                     'bg:#dc3545 #ffffff', # Red background for errors

        # Custom Jython/Jumperless-specific token styles for light theme
        JythonTokens.JumperlessFunction:    'bold #198754',     # Dark green for Jumperless functions
        JythonTokens.JumperlessConstant:    'bold #dc3545',     # Dark red for Jumperless constants
        JythonTokens.JumperlessType:        'bold #0dcaf0',     # Dark cyan for Jumperless types
        JythonTokens.JFSFunction:           'bold #fd7e14',     # Dark orange for JFS functions
        JythonTokens.HardwareConstant:      'bold #d63384',     # Dark pink for hardware constants
    }

# Export styles
__all__ = ['JythonStyle', 'JythonLightStyle'] 