# Jython Syntax Highlighting Guide

This documentation site now supports custom syntax highlighting for **Jython** (Jumperless Python) code blocks! [[memory:3398639]]

## How to Use

Simply use `jython`, `jumperless-python`, or `jpython` as the language identifier in your markdown code blocks:

````markdown
```jython
# Your Jumperless Python code here
connect(GPIO_1, D13)
dac_set(DAC0, 128)
```
````

## What Gets Highlighted

The custom lexer recognizes and highlights:

### Jumperless Functions
Functions specific to Jumperless get **special highlighting**:
- Connection: `connect`, `disconnect`, `is_connected`, `nodes_clear`
- DAC/ADC: `dac_set`, `dac_get`, `adc_get`
- GPIO: `gpio_set`, `gpio_get`, `gpio_set_dir`, `gpio_get_dir`
- OLED: `oled_print`, `oled_clear`, `oled_connect`, `oled_disconnect`
- Probe: `probe_read`, `probe_button`, `probe_wait`, `arduino_reset`
- Debug: `print_bridges`, `print_nets`, `print_chip_status`

### Jumperless Constants
Hardware constants get **distinct highlighting**:
- Power: `TOP_RAIL`, `BOTTOM_RAIL`, `GND`
- DAC/ADC: `DAC0`, `DAC1`, `ADC0`-`ADC7`
- GPIO: `GPIO_1`-`GPIO_8`
- Arduino pins: `D0`-`D13`, `A0`-`A7`
- Special: `PROBE`, `ISENSE_PLUS`, `UART_TX`, etc.

### JFS (Jumperless File System) Functions
File system operations get their own highlighting:
- `open`, `read`, `write`, `close`, `exists`
- `fs_read`, `fs_write`, `fs_exists`, `listdir`

## Examples

### Basic Connection Example
```jython
# Connect components using Jumperless
connect(GPIO_1, D13)
connect(DAC0, A0)
connect(TOP_RAIL, BOTTOM_RAIL)

# Set DAC output
dac_set(DAC0, 128)

# Read ADC input
sensor_value = adc_get(ADC0)
print(f"Sensor: {sensor_value}")
```

### File Operations Example
```jython
# Write to file
if not fs_exists("config.json"):
    fs_write("config.json", '{"led_brightness": 50}')

# Read file content
config = fs_read("config.json")
print(f"Config: {config}")
```

## Technical Details

The custom lexer is built on top of Pygments and extends the standard Python lexer with Jumperless-specific keywords. It's properly registered as a Python package, so it integrates seamlessly with MkDocs.

### Files Involved
- `docs/jython_lexer.py` - The custom lexer implementation
- `docs/jython_style.py` - Custom color theme (not currently used)
- `setup.py` - Package registration for Pygments
- `build_docs.py` - Build script that ensures proper setup

### Building Documentation
Use the provided build script to ensure the lexer is properly registered:

```bash
# Serve locally with live reload
python build_docs.py serve

# Build static site
python build_docs.py build

# Deploy to GitHub Pages
python build_docs.py gh-deploy
```

The lexer is automatically installed as an editable package when you first run the build script. 