# LLM Tool Specification for Jumperless V5

A guide for LLMs with some tips to control the Jumperless V5.

---

## Quick Reference

| Category | Key Tools |
|----------|-----------|
| **Connections** | `connect()`, `disconnect()`, `nodes_clear()`, `save_slot()`, `load_slot()` |
| **Voltage** | `dac_set()`, `adc_get()` |
| **Current** | `ina_get_current()`, `ina_get_power()` |
| **GPIO** | `gpio_set()`, `gpio_get()`, `gpio_set_dir()`, `pwm()` |
| **User Interaction** | `oled_print()`, `probe_read_blocking()`, `probe_button()` |
| **Graphic Overlays** | `overlay_set()`, `overlay_clear()`, `overlay_set_pixel()` |
| **State** | `get_state()`, `set_state()` |

(Refer to the full [Micropython API Reference](09.5-micropythonAPIreference.md))

---

## Communication Methods

### Method 1: Direct Python Commands (Main Serial Port)
Prefix single-line Python with `>` on the main serial port (Port 1).
*Best for: Single commands, status checks.*
```
> connect(1, 5)
> voltage = adc_get(0)
> oled_print(f"V = {voltage:.2f}")
> print(f"V = {voltage:.2f}")
```

### Method 2: ViperIDE / Raw REPL (3rd USB Port)
The **third USB port** provides a MicroPython Raw REPL.
*Best for: Complex logic, loops, automated testing scripts.*
```python
# Full scripts run on port 3
import time
for i in range(10):
    voltage = adc_get(0)
    print(f"Reading {i}: {voltage:.2f}V")
    time.sleep(0.5)
```

### Method 3: Arduino Tags (via UART)
From an Arduino connected to the Jumperless.
*Best for: Hybrid Arduino/Python projects.*
```cpp
Serial.print("<p>connect(1, 5)</p>");     // Python command
Serial.print("<j>n</j>");                 // Menu command
```

### Method 4: Single-Character Commands (Main Serial Port)
Raw characters sent to Port 1 trigger immediate menu actions.
*Best for: Fast state dumps, clearing the board, or manual resets.*
```
J  <-- Immediate JSON state dump
L  <-- Immediate JSON state load (paste JSON after L)
x  <-- Immediate board clear
```

### USB Port Structure
macOS / Linux: 
| Port | Name | Function |
|------|------|----------|
| 1 (main) | JLV5port1 | Main terminal, menu, `>` Python commands |
| 2 | JLV5port3 | Arduino UART passthrough |
| 3 | JLV5port5 | MicroPython Raw REPL (ViperIDE) |

Windows: 
| Port | Name | Function |
|------|------|----------|
| 1 (main) | COM1 | Main terminal, menu, `>` Python commands |
| 2 | COM2 | Arduino UART passthrough |
| 3 | COM3 | MicroPython Raw REPL (ViperIDE) |

---

## Hardware Overview

### Physical Layout
- **60 breadboard rows** (1-60) with 5 RGB LEDs underneath each
- **Arduino Nano header** with routable pins
- **OLED display** (128x32, optional but recommended)
- **Probe** with touch-sensing tip, 2 buttons, mode switch
- **Clickwheel** rotary encoder with button
- **12 CH446Q crossbar chips** (A-L) for routing (~80Ω per path)

### Power
- **TOP_RAIL / BOTTOM_RAIL**: Main power rails (±8V, 300mA)
- **DAC0 / DAC1**: Auxiliary voltage outputs (±8V, 300mA each)
  - DAC0 connects to Probe Tip & INA0
  - DAC0 and DAC1 are 0-3.3V native but amplified to ±8V
- **Current Limits**: ~300mA per rail/DAC

### Measurement
- **ADC0-3**: 4 user analog inputs (±8V range)
- **INA0**: High-side current monitor on DAC0 (Probe Tip)
- **INA1**: High-side current monitor on TOP_RAIL (configurable)

### GPIO
- **10 GPIO pins** (RP2350B, 3.3V logic) Defined as GPIO_1 - GPIO_8 (physical gpio 20-27 on RP2350B), and UART_TX (gpio 0 on RP2350B) and UART_RX (gpio 1 on RP2350B)
- **5V Tolerant Inputs**: Yes
- **PWM**: Hardware PWM 0.1Hz-62.5MHz on all pins

---

## Node Addressing

### Breadboard Rows
`1` through `60`

### Power Rails
| Node | Description |
|------|-------------|
| `TOP_RAIL` | Top power rail (default 5V) |
| `BOTTOM_RAIL` | Bottom rail (default GND) |
| `GND` | Ground reference |
| `DAC0` | DAC0 (connected to probe tip and INA0) |
| `DAC1` | DAC1 (8V tolerant) |

### Arduino Pins
`D0`-`D13`, `A0`-`A7`, `AREF`, `RESET`

### GPIO
`GPIO_1`-`GPIO_8`, `UART_TX`, `UART_RX`

### ADC/Current Sense
`ADC0`-`ADC3`, `ISENSE_PLUS`, `ISENSE_MINUS`

---

## Core Tool Definitions

### Connections & Slots

```jython
connect(node1, node2, duplicates=-1)    # Create connection
disconnect(node1, node2)                 # Remove connection
nodes_clear()                            # Remove ALL connections
is_connected(node1, node2)               # Check if connected

# Slot Management
save_slot(slot_id)                       # Save current state to slot 0-7
load_slot(slot_id)                       # Load state from slot 0-7
get_current_slot()                       # Returns active slot number

# JSON State API (Recommended for LLMs)
get_state()                              # Get complete state as JSON string
set_state(json, clear_first=True)        # Apply state from JSON string
```

### Voltage Control

```jython
dac_set(channel, voltage, save=True)   # Set voltage (-8V to +8V)
dac_get(channel)                       # Get current setting
# Channels: 0/DAC0, 1/DAC1, 2/TOP_RAIL, 3/BOTTOM_RAIL
```

### Measurement

```jython
adc_get(channel)           # Read ADC voltage (channels 0-3)
ina_get_current(sensor)    # Read current in Amps (0=DAC0/Probe, 1=TOP_RAIL)
ina_get_voltage(sensor)    # Read INA bus voltage
ina_get_power(sensor)      # Read power in Watts
```

### GPIO & PWM

```jython
gpio_set(pin, value)           # Set output (True=3.3V, False=0V)
gpio_get(pin)                  # Returns HIGH, LOW, or FLOATING
gpio_set_dir(pin, direction)   # True=OUTPUT, False=INPUT
gpio_set_pull(pin, pull)       # 1=PULLUP, -1=PULLDOWN, 0=NONE
pwm(pin, frequency, duty)      # Start PWM (duty: 0.0-1.0)
pwm_stop(pin)                  # Stop PWM
```

### Waveform Generator (WaveGen)

```jython
# Setup
wavegen_set_output(channel)   # 0=DAC0, 1=DAC1 (Default)
wavegen_set_wave(type)        # 0=Sine, 1=Square, 2=Tri, 3=Saw
wavegen_set_freq(hz)          # Frequency in Hz
wavegen_set_amplitude(vpp)    # Peak-to-Peak Voltage (e.g. 3.3)
wavegen_set_offset(volts)     # DC Offset (e.g. 1.65)

# Control
wavegen_start(1)              # Start output
wavegen_stop()                # Stop output
```

### User Interaction

```jython
oled_print(text, size=2)       # Display on OLED
oled_clear()                   # Clear display
probe_read_blocking()          # Wait for probe touch, return row
probe_read_nonblocking()       # Check without waiting (-1 if none)
probe_button()                 # Returns CONNECT, REMOVE, or NONE
clickwheel_get_direction()     # Returns UP, DOWN, or NONE
clickwheel_get_button()        # Returns PRESSED, HELD, RELEASED
```

### Graphic Overlays (Breadboard LEDs)

The breadboard LEDs are addressed as a 10x30 grid (Row 1-10, Col 1-30). Rows 1-5 are top half (E-A), Rows 6-10 are bottom half (F-J).

```jython
# overlay_set(name, x, y, height, width, colors)
# Colors can be flat list or 2D list of 0xRRGGBB integers
overlay_set("box", 1, 1, 5, 5, [0x550000]*25)

overlay_clear("box")           # Remove overlay
overlay_clear_all()            # Remove all
overlay_set_pixel(x, y, color) # Set single pixel (1-30, 1-10)
```

### System & Filesystem

```jython
# Standard Python I/O is supported!
with open('/config.txt', 'r') as f:
    print(f.read())

# List files
import os
os.listdir('/')
```
```jython
get_net_info(netNum)   # Get dict with name, color, nodes
get_num_nets()         # Count of active nets
get_num_bridges()      # Count of bridges
print_bridges()        # Print bridge table
```

### Single-Character Command Reference (Port 1 Only)

These commands are processed immediately when sent as raw characters (no `>` prefix) to the main serial port.

| Char | Description | Action |
|------|-------------|--------|
| `J` | **Show JSON** | Dumps the complete board state as a JSON string. |
| `L` | **Load JSON** | Prepares the board to receive a JSON state. Paste JSON and end with an empty line. |
| `x` | **Clear All** | Removes all connections and resets paths. |
| `n` | **List Nets** | Prints a human-readable list of all active nets. |
| `b` | **Show Bridges**| Prints the internal bridge array. |
| `~` | **Show Config** | Dumps the current `config.txt` settings. |

| `+` | **Add** | Add connections (e.g., `+1-5,10-12`). |
| `-` | **Remove** | Remove connections (e.g., `-1-5`). |
| `v` | **Read ADC** | Follow with a channel (0-4) to get a quick voltage reading. |

| `@` | **I2C Scan** | Scans for I2C devices on a row (e.g., `@10`). |

| `r` | **Reset Arduino** | Follow with `t` or `b` to reset the Top or Bottom Arduino. |
| `A` | **Connect Arduino UART** | Connects Jumperless's UART to the Arduino D0 and D1 pins (`a` to disconnect). |

| `m` | **Menu** | Displays the help menu (`e` to show more options). |

| `[command]?` | **Help** | Displays the help menu for the specified command. |
| `help` | **Help Menu** | Displays the help menu. |

---

## LLM Mental Model File Format

LLMs should maintain a persistent JSON model of what they believe is physically on the breadboard. This model has **confidence values** that increase through user confirmation or automated testing.

### Mental Model Schema

```json
{
  "version": "1.0",
  "last_updated": "2026-02-06T22:00:00Z",
  "nano_header": {
    "device": "arduino_nano",  // "arduino_nano", "rp2040", "rpi_40pin_adapter", "oled_only", "empty"
    "confidence": 0.9,
    "notes": "User confirmed Arduino Nano Every"
  },
  "power_rails": {
    "TOP_RAIL": {"voltage": 5.0, "confidence": 1.0, "source": "measured"},
    "BOTTOM_RAIL": {"voltage": 0.0, "confidence": 1.0, "source": "measured"}
  },
  "components": [
    {
      "id": "comp_001",
      "type": "resistor",
      "value": 1000,
      "unit": "ohms",
      "tolerance": 0.05,
      "pins": [5, 10],
      "confidence": 0.95,
      "detection_method": "measured",
      "notes": "Measured 987Ω between rows 5-10"
    },
    {
      "id": "comp_002",
      "type": "led",
      "color": "red",
      "forward_voltage": 1.8,
      "pins": {"anode": 15, "cathode": 16},
      "confidence": 0.7,
      "detection_method": "user_stated",
      "notes": "User said 'red LED on rows 15-16'"
    },
    {
      "id": "comp_003",
      "type": "module",
      "name": "SSD1306 OLED",
      "pins": {
        "GND": 20, "VCC": 21, "SCL": 22, "SDA": 23
      },
      "confidence": 0.6,
      "detection_method": "inferred",
      "notes": "Searched pinout, user confirmed row 20"
    }
  ],
  "wires": [
    {"from": 1, "to": 30, "confidence": 0.8, "detection_method": "continuity_test"}
  ],
  "unknowns": [
    {"rows": [40, 41, 42], "notes": "Something detected but not identified"}
  ]
}
```

### Nano Header Device Types

| Device | Description |
|--------|-------------|
| `arduino_nano` | Arduino Nano/Every/RP2040 etc. |
| `rp2040` | Bare RP2040 board |
| `rpi_40pin_adapter` | RPi GPIO adapter board |
| `oled_only` | SBC/SMD/OLED adapter for just the OLED |
| `empty` | Nothing plugged in |

### Confidence Levels

| Level | Source | Meaning |
|-------|--------|---------|
| 1.0 | `measured` | Electrically verified |
| 0.9 | `user_confirmed` | User explicitly confirmed |
| 0.7 | `user_stated` | User mentioned it casually |
| 0.5 | `inferred` | LLM guessed from context |
| 0.3 | `assumed` | Default assumption |

---
<!-- 
## Automated Component Detection

The Jumperless can perform automated testing to identify unknown components, similar to transistor testers.

### Detection Algorithm Flowchart

```
START: Unknown component between rows A and B
                    │
                    ▼
┌───────────────────────────────────────┐
│ 1. CONTINUITY TEST                    │
│    Connect DAC1→A, ADC0→B, GND→B      │
│    Set DAC1=0.5V, measure ADC0        │
│    If V_B ≈ V_A → WIRE (R < 1Ω)       │
└───────────────────────────────────────┘
                    │ No
                    ▼
┌───────────────────────────────────────┐
│ 2. RESISTANCE TEST                    │
│    Measure voltage drop, calc R       │
│    If 1Ω < R < 10MΩ → RESISTOR        │
└───────────────────────────────────────┘
                    │ No/Very High R
                    ▼
┌───────────────────────────────────────┐
│ 3. DIODE TEST (Forward)               │
│    DAC1→A (0→3V ramp), ADC0→B         │
│    If Vf ≈ 0.3V → Schottky            │
│    If Vf ≈ 0.6V → Silicon diode       │
│    If Vf ≈ 1.8-3.2V → LED             │
└───────────────────────────────────────┘
                    │ No forward drop
                    ▼
┌───────────────────────────────────────┐
│ 4. DIODE TEST (Reverse - swap)        │
│    DAC1→B, ADC0→A                     │
│    If conducts reversed → WIRE        │
│    If blocks → DIODE (note polarity)  │
└───────────────────────────────────────┘
                    │ Blocks both ways
                    ▼
┌───────────────────────────────────────┐
│ 5. CAPACITANCE TEST                   │
│    Use crossbar R ≈ 80Ω, measure τ    │
│    C = τ / 80Ω                        │
│    If 1pF < C < 10,000µF → CAPACITOR  │
└───────────────────────────────────────┘
                    │ No capacitance (RC method)
                    ▼
┌───────────────────────────────────────┐
│ 5b. CAPACITANCE/INDUCTANCE (AC test)  │
│    Apply AC via WaveGen, measure ΔΦ   │
│    Leading phase → CAPACITOR          │
│    Lagging phase → INDUCTOR           │
│    XC = 1/(2πfC), XL = 2πfL           │
└───────────────────────────────────────┘
                    │ Nothing detected
                    ▼
              OPEN CIRCUIT or
              UNKNOWN 3+ PIN DEVICE

**Note on Confidence**: These automated tests provide estimates, not 
absolute identification. Crossbar R varies 80-88Ω. Always set confidence
≤ 0.85 for automated measurements. Confirm with user if unsure.
```

### Python Implementation

```jython
def detect_component(row_a, row_b):
    """Automated component detection between two rows."""
    
    # 1. Continuity / Resistance Test
    disconnect(row_a, -1)  # Clear existing
    disconnect(row_b, -1)
    connect(DAC1, row_a)
    connect(ADC0, row_b)
    connect(row_b, GND)  # Complete circuit through INA
    
    dac_set(1, 1.0)  # Apply 1V
    time.sleep(0.01)
    v_drop = 1.0 - adc_get(0)
    current = ina_get_current(1)  # If INA1 in path
    
    if current > 0.001:  # > 1mA flows
        resistance = v_drop / current
        if resistance < 1:
            return {"type": "wire", "confidence": 0.95}
        elif resistance < 10_000_000:
            return {"type": "resistor", "value": resistance, "confidence": 0.9}
    
    # 2. Diode Test (Forward)
    dac_set(1, 0)
    time.sleep(0.01)
    for v in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
        dac_set(1, v)
        time.sleep(0.005)
        measured = adc_get(0)
        if measured > 0.1:  # Conducting
            vf = v - measured
            if vf < 0.4:
                return {"type": "diode", "subtype": "schottky", "vf": vf, "confidence": 0.85}
            elif vf < 0.8:
                return {"type": "diode", "subtype": "silicon", "vf": vf, "confidence": 0.85}
            else:
                return {"type": "led", "vf": vf, "confidence": 0.8}
    
    # 3. Diode Test (Reverse - swap polarity)
    disconnect(DAC1, row_a)
    disconnect(ADC0, row_b)
    connect(DAC1, row_b)
    connect(ADC0, row_a)
    dac_set(1, 2.0)
    time.sleep(0.01)
    if adc_get(0) > 0.1:
        return {"type": "wire", "confidence": 0.9}  # Conducts both ways
    
    # 4. Capacitance Test (RC time constant)
    # Use internal resistance + measure charge time
    # ... (implementation depends on available timing)
    
    return {"type": "unknown", "confidence": 0.0}
```

### Test Sequence for Unknown Board

When a user says "I have some stuff on the board but I'm not sure what":

```jython
def scan_all_rows():
    """Scan all 60 rows for connections and components."""
    connections = []
    
    for row_a in range(1, 60):
        for row_b in range(row_a + 1, 61):
            result = detect_component(row_a, row_b)
            if result["type"] != "unknown":
                connections.append({
                    "rows": [row_a, row_b],
                    **result
                })
                oled_print(f"{row_a}-{row_b}: {result['type']}")
    
    return connections
``` -->

### Increasing Confidence

| Method | Confidence Boost |
|--------|------------------|
| User confirms "yes that's right" | +0.2 |
| Electrical measurement matches | +0.3 |
| Multiple consistent tests | +0.1 per test |
| User provides datasheet | Set to 0.95 |

---

## Workflows for LLMs

### 1. Circuit Safe-Check (Mental Model)

**CRITICAL**: The Jumperless prevents internal shorts, but **cannot see external wires or components** on the breadboard.
If a user has a physical wire connecting Row 5 to Row 10, connecting `TOP_RAIL->5` and `GND->10` will cause a dead short through the user's wire.

**Workflow:**
1.  **Ask**: "What is currently on the breadboard? (Wires, components, etc)"
2.  **Model**: Build the mental model JSON with low confidence
3.  **Test**: Run `detect_component()` on key rows to verify
4.  **Update**: Increase confidence as tests confirm the model

```jython
# Safe Power-Up Sequence
oled_print("Checking for shorts...")
# Find an unused ADC
unused_adc = None
for i in range(4):
    name = f"ADC{i}"
    is_used = False
    for net in get_all_nets():
        if name in net['nodes']:
            is_used = True
            break
    if not is_used:
        unused_adc = i
        break

if unused_adc is not None:
    connect(5, f"ADC{unused_adc}")
    connect(10, DAC1)
    # ...
```
     model["wires"].append({"from": 5, "to": 10, "confidence": 0.95})
else:
     connect(5, TOP_RAIL)
     connect(10, GND)
```

### 2. Identifying User Circuits
Use the Probe to "see" the board.
```jython
oled_print("Touch the input of your circuit")
input_row = probe_read_blocking()
oled_print(f"Input is at row {input_row}")
```

### 3. Automated Characterization
Use WaveGen and ADC to treat the circuit as a black box.
```jython
connect(DAC1, 1)
wavegen_set_output(1)
wavegen_set_freq(100)
wavegen_set_wave(0)  # Sine
wavegen_start(1)

connect(ADC0, 10)
for i in range(5):
    val = adc_get(0)
    print(f"Sample {i}: {val}V")
    time.sleep(0.01)
```

---

## Component Library (Dynamic Lookup)

When a user mentions a hardware module, **search the web for its pinout** and build a JSON definition on the fly.

**Workflow:**
1. User mentions: "I have an SSD1306 OLED on the breadboard"
2. LLM searches: "SSD1306 OLED pinout"
3. LLM builds JSON from search results and adds it to `mental_model["components"]`

**Example: NeoPixel Stick**
```json
{
  "name": "NeoPixel Stick 8",
  "pins": {
    "GND": {"default": "GND", "offset": 0},
    "5V": {"default": "TOP_RAIL", "offset": 1},
    "DIN": {"default": "GPIO_1", "offset": 2},
    "DOUT": {"default": "NC", "offset": 7}
  },
  "width": 8,
  "voltage": "5V",
  "notes": "3.3V GPIO works for most NeoPixels. Data on offset 2."
}
```

**Key**: The `offset` field defines pin position relative to pin 1. When user says "pin 1 is on row X", calculate absolute rows as `row = X + offset`.

---

## Safety Guidelines for LLMs

1.  **Voltage Check**: ADCs are buffered for ±8V. The board is ±9V tolerant overall.
2.  **Short Circuit Prevention**: The firmware will ignore requests to connect `TOP_RAIL` directly to `BOTTOM_RAIL` or `GND`.
3.  **Confirm Power**: Ask: "Is the board powered via USB?" (No barrel jack exists).
4.  **Crossbar Resistance**: Remember ~80Ω per connection. High current paths will have voltage drop. Measure voltage *at the destination* with an ADC to compensate.

---

## LLM Preferences (Claude's Additions)

### 1. Structured State Snapshot

**What I want**: A single command that returns the complete board state as structured data (JSON/dict), not just printed text. This lets me reason about the state programmatically.

```python
# REQUESTED: get_state() -> dict
# Returns something like:
{
  "slot": 0,
  "bridges": [[1, 5], [5, "TOP_RAIL"], [10, "GND"]],
  "rails": {"TOP_RAIL": 5.0, "BOTTOM_RAIL": 0.0, "DAC0": 3.3, "DAC1": 0.0},
  "gpio": [
    {"pin": 1, "dir": "OUTPUT", "value": True, "pull": "NONE"},
    {"pin": 2, "dir": "INPUT", "value": False, "pull": "PULLUP"}
  ],
  "adc_snapshot": [3.28, 0.01, 5.02, -0.03]  # Quick reading of all 4
}
```

**Why**: Currently I have to call `get_num_bridges()`, `get_net_info()` for each net, etc. A single snapshot is faster and less error-prone for building my mental model.

### 2. Return Values, Not Just Prints

For debugging, I prefer **return values** over **print statements**:

| Instead of... | I prefer... |
|---------------|-------------|
| `print_nets()` → prints to serial | `get_nets()` → returns list of net dicts |
| `print_bridges()` → prints to serial | `get_bridges()` → returns list of bridge tuples |
| `print_paths_compact()` → prints | `get_paths()` → returns routing info |

**Why**: When I call a tool, I want to capture the result and reason about it. Print output goes to the user's terminal but isn't easily parsed by my next step.

### 3. Error Return Conventions

Consistent error handling helps me recover:

```python
# Good: Returns None or raises exception with message
result = connect(999, 5)  # Invalid node
# Returns: None (or {"error": "Invalid node: 999"})

# Good: Returns success/failure boolean with reason
success, msg = disconnect(1, 5)  
# Returns: (True, "Disconnected") or (False, "No such connection")
```

### 4. Undo via Slot Backup

For destructive operations like `nodes_clear()`, the existing slot system provides an undo mechanism:

```python
# Before destructive operation, save current state to a backup slot
save_slot(7)           # Save to slot 7 as backup
nodes_clear()          # Now safe to clear

# If user wants to undo:
load_slot(7)           # Restore from backup
```

**Pattern**: Always save the current slot to an unused slot (7 is a good "scratch" slot) before any destructive action. This provides a built-in undo without needing special confirm flags.

### 5. Measurement with Context

When measuring, I often want multiple samples or statistics:

```jython
# REQUESTED: adc_get_stats(channel, samples=10)
# Returns: {"mean": 3.28, "min": 3.25, "max": 3.31, "stddev": 0.02}
```

**Why**: A single ADC reading might be noisy. Having built-in averaging/stats means I don't have to write loops for every measurement.

### 6. Interactive Conversation Patterns

When helping users debug, I find these patterns effective:

**Explore First, Act Later**:
```
User: "My LED isn't lighting up"
Me: 
  1. "Where is your LED connected? (Touch the anode with the probe)"
  2. [probe_read_blocking() → row 15]
  3. "I see row 15. Let me check the voltage there..."
  4. [connect(ADC0, 15), adc_get(0) → 0.02V]
  5. "Row 15 is at 0V. Is it supposed to be connected to power?"
```

**Show, Don't Just Do**:
```jython
# Before making a connection, describe it:
oled_print("Connecting row 5 to 5V...")
connect(5, TOP_RAIL)
oled_print("Done! LED should light now")
```

**Verify After Acting**:
```jython
# After connecting power, verify it worked:
connect(5, TOP_RAIL)
connect(ADC0, 5)
v = adc_get(0)
if abs(v - 5.0) < 0.5:
    oled_print(f"✓ Row 5 at {v:.1f}V")
else:
    oled_print(f"⚠ Expected 5V, got {v:.1f}V")
disconnect(ADC0, 5)

```

---

## LLM Best Practices & Future Tools

This section consolidates recommendations for reliable, high-context hardware interaction.

### 1. Explicit State Verification
Trust but verify. Confirm hardware state after critical operations.

```python
# Goal: Set DAC0 to 3.3V
current = dac_get(0)
if abs(current - 3.3) > 0.1:
    dac_set(0, 3.3)
    time.sleep(0.01) # Allow settling
    new_val = dac_get(0)
    if abs(new_val - 3.3) > 0.1:
        print(f"Error: DAC0 failed to set. Got {new_val}V")
```

### 2. Structured State Snapshot
A single command to return the complete board state as a formatted JSON string, enabling detailed programmatic reasoning and full state management.

```jython
# Get the complete current state as a formatted JSON string
snapshot = get_state()

# The snapshot includes:
# - power: Settings for TOP_RAIL, BOTTOM_RAIL, DAC0, DAC1
# - nets: All active connections, names, colors, and voltage assignments
# - gpio: Current configuration and state of all GPIO pins

# Apply a state back to the hardware
# set_state(json_string, clear_first=True)
# If clear_first=True (default), it resets the board before applying
set_state(snapshot)
```

### 3. Search-First Component Handling
Ground knowledge by searching for pinouts *before* asking the user.

**Workflow:**
1. User: "I have a BME280."
2. Agent: `search_web("BME280 pinout SPI I2C")`
3. Agent: "I see the BME280 supports both SPI and I2C. Which one are you using?"

### 4. Batch Operations
Process information efficiently in large chunks to reduce round-trips and ensure atomic updates. The recommended way to perform complex batch reconfigurations is to fetch the current state, modify it in Python, and re-apply it.

```jython
# Recommended Batch Workflow:
state_json = get_state()
state = json.loads(state_json)

# 1. Modify connections
state['nets'].append({"index": 10, "name": "SIGNAL", "nodes": [5, 12, "D7"]})

# 2. Update power settings
state['power']['top_rail'] = 3.3

# 3. Configure GPIO
state['gpio'][0]['dir'] = "OUTPUT"
state['gpio'][0]['value'] = True

# 4. Apply all changes at once
set_state(json.dumps(state))
```

### 5. Return Values Over Prints
Tools should return data structures (lists, dicts) for programmatic use, not just print to stdout.

### 6. undo via Slot Backup
Always save the current state to a scratch slot (e.g. slot 7) before destructive operations like `nodes_clear()`.

### 7. Context-Aware Error Recovery
Error messages should include `suggested_fix` fields to allow self-correction without user intervention.

### 8. Interactive Conversation Patterns

**Explore First, Act Later**:
Probe and measure *before* applying power to unknown circuits.

**Show, Don't Just Do**:
Explain actions via `oled_print()` and `print()` before executing them to keep the user informed.

---

## Implementation Status

| Feature | Status |
|---------|--------|
| `connect()`, `disconnect()`, `is_connected()` | ✅ Implemented |
| `dac_set()`, `adc_get()`, `ina_*()` | ✅ Implemented |
| `gpio_*()`, `pwm()` | ✅ Implemented |
| `oled_print()`, `probe_*()` | ✅ Implemented |
| WaveGen tools | ✅ Implemented |
| Slot management | ✅ Implemented |
| `get_state()` / `set_state()` snapshot | ✅ Implemented |
| Slot backup for undo | ✅ Implemented (use `save_slot(7)` before destructive ops) |

