# Jython Lexer and Glossary Setup Guide

This guide explains how to use the custom **Jython** (Jumperless Python) lexer for enhanced syntax highlighting and the automatic glossary term highlighting system.

## 🎨 Custom Jython Lexer

### What is Jython?

**Jython** is our custom Pygments lexer that extends standard Python syntax highlighting with Jumperless-specific keywords, functions, and constants. It provides:

- **Enhanced syntax highlighting** for Jumperless functions like `connect()`, `gpio_set()`, `dac_set()`
- **Special coloring** for hardware constants like `TOP_RAIL`, `GPIO_1`, `DAC0`
- **JFS (Jumperless File System)** function highlighting
- **Hardware pin recognition** for `D0`, `A1`, `GPIO2`, etc.

### Using the Jython Lexer

#### Method 1: Specify `jython` language in code blocks

````markdown
```jython
import jumperless

# Connect GPIO_1 to TOP_RAIL
connect(GPIO_1, TOP_RAIL)

# Set DAC output
dac_set(DAC0, 2.5)

# Read analog value
value = adc_get(ADC0)
```
````

#### Method 2: Use alternative aliases

````markdown
```jumperless-python
# Also works with these aliases:
# - jython
# - jumperless-python  
# - jpython
```
````

#### Method 3: File extension recognition

The lexer automatically recognizes these file extensions:
- `*.jy`
- `*.jython`
- `*.jumperless.py`

### Setting up Pygments Integration

If you want to use this in your local environment:

1. **Install the lexer** (copy the files to your Python path):
   ```bash
   # Copy jython_lexer.py and jython_style.py to your project
   cp jython_lexer.py /your/python/path/
   cp jython_style.py /your/python/path/
   ```

2. **Register with Pygments** (add to your `setup.py` or `pyproject.toml`):
   ```python
   entry_points = {
       'pygments.lexers': [
           'jython = jython_lexer:JythonLexer',
       ],
       'pygments.styles': [
           'jython = jython_style:JythonStyle',
           'jython-light = jython_style:JythonLightStyle',
       ],
   }
   ```

3. **Use with MkDocs** (add to `mkdocs.yml`):
   ```yaml
   markdown_extensions:
     - codehilite:
         guess_lang: false
         use_pygments: true
         css_class: highlight
         pygments_style: jython  # or jython-light
   ```

## ✨ Automatic Glossary Highlighting

### How it Works

The JavaScript system automatically:

1. **Loads your glossary** from `99-glossary.md`
2. **Scans all body text** (excluding code blocks)
3. **Highlights matching terms** with dotted underlines
4. **Shows tooltips** with definitions on hover

### Glossary Format

Your glossary should follow this format in `99-glossary.md`:

```markdown
# Glossary of Terms

`net` = a group of all the `node`s that are connected together

`node` = anything the crossbar array can connect to, which includes everything on the breadboard and Nano header

`bridge` = a pair of exactly two `node`s (this is what you're making when you connect stuff with the probe)
```

### Key Features

- **Automatic parsing** - Add new terms to glossary file and they're immediately highlighted
- **Smart detection** - Only highlights whole words, avoids code blocks
- **Rich tooltips** - Supports `*bold*` and `backtick emphasis` in definitions
- **Performance optimized** - Uses efficient tree walking and caching
- **Dark/light themes** - Automatically adapts to your site's theme

### Visual Styling

Glossary terms appear with:
- **Cyan color** (#8be9fd) with dotted underline
- **Green on hover** (#50fa7b) 
- **Subtle background** for better visibility
- **Smooth transitions** for polished UX

## 🎯 Color Scheme Reference

### Jython Lexer Colors

| Element | Color | Usage |
|---------|-------|-------|
| **Jumperless Functions** | `#8aff80` (Bright Green) | `connect()`, `gpio_set()` |
| **Jumperless Constants** | `#ff9580` (Coral) | `TOP_RAIL`, `GPIO_1` |
| **JFS Functions** | `#ffb86c` (Orange) | `open()`, `read()`, `write()` |
| **Hardware Pins** | `#ff79c6` (Pink) | `D0`, `A1`, `GPIO2` |
| **Python Keywords** | `#ff79c6` (Pink) | `def`, `class`, `if` |
| **Strings** | `#f1fa8c` (Yellow) | `"hello world"` |
| **Comments** | `#6272a4` (Muted Blue) | `# comments` |
| **Numbers** | `#bd93f9` (Purple) | `123`, `3.14` |

### Glossary Terms

| State | Color | Description |
|-------|-------|-------------|
| **Default** | `#8be9fd` (Cyan) | Normal glossary term |
| **Hover** | `#50fa7b` (Green) | When mouse hovers |
| **Background** | `rgba(139, 233, 253, 0.1)` | Subtle highlight |

## 🚀 Usage Examples

### Code with Jython Highlighting

````markdown
```jython
import jumperless
import utime

# Initialize the Jumperless
jumperless.init()

# Connect probe to GPIO pin
connect(PROBE, GPIO_1)

# Set up some basic connections
connect(D2, TOP_RAIL)    # Connect Arduino D2 to power rail
connect(A0, ADC0)        # Connect Arduino A0 to ADC input

# Control GPIO
gpio_set(GPIO_1, True)   # Set GPIO high
voltage = adc_get(ADC0)  # Read voltage

# File system operations (JFS)
with open("config.txt", "w") as f:
    write(f, "voltage=" + str(voltage))

print(f"Measured voltage: {voltage}V")
```
````

### Body Text with Glossary Terms

When you write documentation, terms like **net**, **node**, **bridge**, **path**, and **chip** will automatically be highlighted and show definitions when you hover over them.

For example: "Each **bridge** connects two **nodes** in the crossbar matrix, and multiple bridges can form a **net**."

## 🔧 Customization

### Adding New Keywords

Edit `jython_lexer.py` and add to the appropriate set:

```python
JUMPERLESS_FUNCTIONS = {
    'your_new_function',  # Add here
    # ... existing functions
}
```

### Adding New Glossary Terms

Simply add to your `99-glossary.md` file:

```markdown
`your_new_term` = definition of your new term with optional `emphasis` and *bold* text
```

The system automatically picks up new terms on page reload.

### Styling Customization

Modify the CSS in `extra.css`:

```css
.glossary-term {
    color: #your-color !important;
    /* Add your custom styles */
}
```

## 📁 File Structure

```
docs/
├── jython_lexer.py              # Custom Pygments lexer
├── jython_style.py              # Custom Pygments styles  
├── custom-syntax-highlighter.js # JavaScript for highlighting
├── extra.css                    # CSS styles
├── 99-glossary.md              # Glossary definitions
└── jython-setup.md             # This guide
```

---

**Happy coding with enhanced Jython syntax highlighting! 🎉** 