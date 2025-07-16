# Test Clean Jython Lexer

This page tests the Jython lexer without interference from custom CSS/JS.

## Jython Code Block Test

```jython
# Test Jumperless functions and constants
connect(GPIO_1, D13)
connect(DAC0, A0) 
dac_set(DAC0, 128)
value = adc_get(ADC1)

# Test JFS functions  
file = open("test.txt", "w")
fs_write("config.json", "data")
content = fs_read("config.json")

# Regular Python should still work
print(f"Value: {value}")
for i in range(10):
    print(i)
```

## Expected Results

If working correctly, you should see:
- **Pink** highlighting for: `connect`, `dac_set`, `adc_get` (Jumperless functions)
- **Purple** highlighting for: `GPIO_1`, `D13`, `DAC0`, `A0`, `ADC1` (Jumperless constants) 
- **Cyan** highlighting for: `open`, `fs_write`, `fs_read` (JFS functions)
- Standard Python highlighting for: `print`, `for`, `range`, strings, numbers

## Inline Code Test

Inline code should be normal size: `connect()`, `GPIO_1`, `True`, `False`

## Python Comparison

```python
# Regular Python for comparison
import time
import json

def test_function():
    data = {"key": "value"}
    return json.dumps(data)

result = test_function()
print(result)
``` 