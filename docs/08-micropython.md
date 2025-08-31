# MicroPython

This guide covers how to write, load, and run Python scripts that control Jumperless hardware using the embedded MicroPython interpreter.

<!-- ## Table of Contents

1. [Quick Start](#quick-start)
2. [Hardware Control Functions](#hardware-control-functions)
3. [Writing Python Scripts](#writing-python-scripts)
4. [Loading and Running Scripts](#loading-and-running-scripts)
5. [REPL (Interactive Mode)](#repl-interactive-mode)
6. [File Management](#file-management)
7. [Examples and Demos](#examples-and-demos)
8. [Troubleshooting](#troubleshooting) -->

####If you just want an overview of all the available calls, check out the [MicroPython API Reference](09.5-micropythonAPIreference.md)


## Quick Start

<!-- ### Starting MicroPython REPL -->
From the main Jumperless menu, press `p` to enter the MicroPython REPL:

![Screenshot 2025-07-04 at 7 03 24 PM](https://github.com/user-attachments/assets/e7ce0688-5ddf-48da-8560-4a8f6b747c4f)


## REPL Navigation

Up / Down arrow keys on a blank prompt will scroll through history, any other key will break out of history mode and enter multiline editing. So you can use arrow keys to navigate and edit the script. 


## Hardware Control Functions

All Jumperless hardware functions are automatically imported into the global namespace - no prefix needed


## Basic Hardware Control
```jython
# Connect nodes 1 and 5
connect(1, 5)

# Set GPIO pin 1 to HIGH
gpio_set(1, True)

# Read ADC channel 0
voltage = adc_get(0)
print("Voltage: " + str(voltage) + "V")

# Set DAC channel 0 to 3.3V
dac_set(0, 3.3)
```


## Node Connections
```jython
# Connect two nodes
connect(1, 5)                    # Connect using numbers
connect("d13", "tOp_rAiL")       # Connect using node names (case insensitive when in quotes)
connect(TOP_RAIL, BOTTOM_RAIL)   # Connect using DEFINEs (all caps) Note: This will actually just be ignored by the Jumperless due to Do Not Intersect rules

# Disconnect bridges
disconnect(1, 5)

# Disconnect everything connected to a node
disconnect(5, -1)

# Check if nodes are connected
if is_connected(1, 5):
    print("Nodes 1 and 5 are connected")

# Clear all connections
nodes_clear()
```
![Screenshot 2025-07-04 at 7 22 35 PM](https://github.com/user-attachments/assets/e08d9b83-aa4d-4e1a-873c-7f6c46ddb5bc)


## DAC (Output Voltage)
```jython
# Set DAC voltage (-8.0V to 8.0V)
dac_set(0, 2.5)    # Set DAC channel 0 to 2.5V
dac_set(1, 1.65)   # Set DAC channel 1 to 1.65V

# Read current DAC voltage
voltage = dac_get(0)
print("DAC 0: " + str(voltage) + "V")

# Available channels:
# 0 = DAC0, 1 = DAC1, 2 = TOP_RAIL, 3 = BOTTOM_RAIL
# Can also use node names: DAC0, DAC1, TOP_RAIL, BOTTOM_RAIL
```
![Screenshot 2025-07-04 at 7 17 36 PM](https://github.com/user-attachments/assets/f68b3bf2-3420-4d51-800a-1e8e9e804261)

## ADC (Measure Voltage)
```jython
# Read analog voltage (0-8V range for channels 0-3, 0-5V for channel 4)
voltage = adc_get(0)    # Read ADC channel 0
voltage = adc_get(1)    # Read ADC channel 1

# Available channels: 0, 1, 2, 3, 4
```
![Screenshot 2025-07-04 at 7 22 01 PM](https://github.com/user-attachments/assets/79cf16e8-8a79-4f11-9cf4-52456735b0dc)

## GPIO (General Purpose I/O)
```jython
# Set GPIO direction
gpio_set_dir(1, True)   # Set GPIO 1 as OUTPUT
gpio_set_dir(2, False)  # Set GPIO 2 as INPUT

# Set GPIO state
gpio_set(1, True)       # Set GPIO 1 HIGH
gpio_set(1, False)      # Set GPIO 1 LOW

# Read GPIO state (returns "HIGH" or "LOW")
state = gpio_get(2)     # Returns formatted string

# Configure pull resistors
gpio_set_pull(3, 1)     # Enable pull-up
gpio_set_pull(3, -1)    # Enable pull-down
gpio_set_pull(3, 0)     # No pull resistor

# Read GPIO configuration (returns formatted strings)
direction = gpio_get_dir(1)    # Returns "INPUT" or "OUTPUT"
pull = gpio_get_pull(2)        # Returns "PULLUP", "PULLDOWN", or "NONE"

# Available GPIO pins: 1-8 (GPIO 1-8), 9 (UART Tx), 10 (UART Rx)
```

## PWM (Pulse Width Modulation)
```jython
# Hardware PWM: High frequency (10Hz to 62.5MHz)
pwm(1, 1000, 0.5)       # 1kHz, 50% duty cycle on GPIO_1
pwm(2, 50000, 0.25)     # 50kHz, 25% duty cycle on GPIO_2

# Slow PWM: Low frequency (0.001Hz to 10Hz)
pwm(3, 0.1, 0.75)       # 0.1Hz (10 second period), 75% duty cycle
pwm(4, 0.001, 0.5)      # 0.001Hz (1000 second period), 50% duty cycle

# Change PWM parameters
pwm_set_frequency(1, 2000)     # Change to 2kHz
pwm_set_duty_cycle(1, 0.25)    # Change to 25% duty cycle

# Stop PWM
pwm_stop(1)             # Stop PWM on GPIO_1

# Available GPIO pins: 1-8 (GPIO 1-8 only)
# Automatic mode selection: Hardware PWM for 10Hz+, Slow PWM for <10Hz
```
![Screenshot 2025-07-04 at 7 22 35 PM](https://github.com/user-attachments/assets/5b5f884f-f459-4a31-9f21-89d084594f97)
![Screenshot 2025-07-04 at 7 31 19 PM](https://github.com/user-attachments/assets/c7bdb245-59a4-46db-9c52-fcc43c1f359e)

## Current Sensing (INA219)
```jython
# Read current sensor data
current = ina_get_current(0)          # Current in A
current = ina_get_current(0) * 1000   # Current in mA
voltage = ina_get_voltage(0)          # Shunt voltage in V
bus_voltage = ina_get_bus_voltage(0)  # Bus voltage in V
power = ina_get_power(0)              # Power in W

# Available sensors: 0, 1    # INA 1 is hardwired to the output of DAC 0 because it's meant for measuring resistance
```

## OLED Display
```jython
# Initialize OLED
oled_connect()                 # Connect to OLED
oled_print("Hello World!")     # Display text

# Clear display
oled_clear()

# Disconnect
oled_disconnect()
```

## Probe Functions
```jumperless
# Read probe pad (blocking)
pad = probe_read_blocking()       # Returns ProbePad object only when a pad is touched

# Read probe pad (non-blocking)
pad = probe_read_nonblocking()    # Returns ProbePad object (which can be NO_PAD)

# Button functions (probe button)
button = probe_button()           # Read probe button state (blocking)
button = get_button()             # Alias
button = button_read()            # Another alias
button = read_button()            # Another alias
button = check_button()           # Non-blocking check
button = button_check()           # Alias

# Button with parameters
button = probe_button(True)       # Blocking
button = probe_button(False)      # Non-blocking
```
![Screenshot 2025-07-04 at 7 37 54 PM](https://github.com/user-attachments/assets/4d0b2e29-e33d-4e1c-b339-336d1d686319)


## System Functions
```jython
# Reset Arduino
arduino_reset()

# Run built-in apps
run_app("I2C Scan")        # Run I2C scanner
run_app("Bounce Startup")  # Loop the startup animation

# Advanced system control
pause_core2(True)          # Pause core2 processing
pause_core2(False)         # Resume core2 processing
send_raw("A", 1, 2, 1)     # Send raw data to core2 (chip A, pos 1,2, set)

# Show help
help()                # Display all available functions
nodes_help()          # Show all available node names and aliases
```

The [help()](#the-entire-output-of-help) and [nodes_help()](#the-entire-output-of-nodes_help) functions will list all the available commands (except for the new ones I forget to update)



## Basic Script Structure
```jython
"""
My Jumperless Script
Description of what this script does
"""

print("Starting my script...")

# Connect some nodes
connect(1, 5)
connect(2, 6)

# Set up GPIO
gpio_set_dir(1, True)  # Output
gpio_set_dir(2, False) # Input

# Main loop
for i in range(10):
    gpio_set(1, True)
    time.sleep(0.5)
    gpio_set(1, False)
    time.sleep(0.5)
    
    # Read input
    if gpio_get(2) == "HIGH":
        print("Button pressed!")

# Cleanup
nodes_clear()
print("Script complete!")

```
   
 


## Loading and Running Scripts


### Method 1: File Manager
From the REPL, type `files` to open the file manager:

```
>>> files
```

Navigate to your script and press Enter to load it for editing, then press `Ctrl+P` to load it into the REPL for execution.

**Note:** The standard Python `exec(open(...).read())` method is not supported in the Jumperless MicroPython environment. Always use the file manager and `Ctrl+P` to run scripts.

### Method 2: REPL Commands
From the MicroPython REPL, you can use the following commands to manage scripts:

```
# Load script into editor for modification
load my_script.py

# Save current session as script
save my_new_script.py
```

### Method 4: Direct Execution
From the main Jumperless menu, you can execute single commands:

```
> gpio_set(1, True)
> adc_get(0)
> connect(1, 5)
```

## REPL (Interactive Mode)

### Starting REPL
From main menu: Press `p`

### REPL Commands
```
CTRL + q           - Exit REPL
history            - Show command history and saved scripts
save [name]        - Save last executed script
load <name>        - Load script by name or number
files              - Open file manager
new                - Create new script with eKilo editor
helpl              - Show REPL help
help()             - Show hardware commands
```

### Navigation
```
↑/↓ arrows         - Browse command history
←/→ arrows         - Move cursor, edit text
TAB                - Add 4-space indentation
Enter              - Execute (empty line in multiline to finish)
Ctrl+Q             - Force quit REPL or interrupt running script
```

### Multiline Auto-Indent Mode
The REPL automatically detects when you need multiple lines after a `:`

```jython
>>> def blink_led():
...     for i in range(5):
...         gpio_set(1, True)
...         time.sleep(0.5)
...         gpio_set(1, False)
...         time.sleep(0.5)
... 
>>> blink_led()
```

If you want to use *real* multiline mode, use the Kilo file editor. 

### Command History
- Use ↑/↓ arrows to browse previous commands
- Commands are automatically saved
- Type `history` to see all saved scripts





## Built-in Examples
The system includes several example scripts. To run an example:

1. Type `files` in the REPL.
2. Navigate to the `examples/` directory.
3. Select the desired script and press Enter to edit/view it.
4. Press `Ctrl+P` to load it into the REPL for execution.

Example scripts include:
- 01_dac_basics.py (DAC basics - voltage control)
- 02_adc_basics.py (ADC basics - voltage reading)
- 03_gpio_basics.py (GPIO basics - digital I/O)
- 04_node_connections.py (Node connections)



**REPL not responding:**
- Press Ctrl+Q to force quit
- Unplug / replug your Jumperless (don't worry, almost everything is persistent)



## Formatted Output and Custom Types
The Jumperless module provides formatted output for better readability:

```jython
# GPIO state returns formatted strings
state = gpio_get(1)           # Returns "HIGH" or "LOW"
direction = gpio_get_dir(1)   # Returns "INPUT" or "OUTPUT"
pull = gpio_get_pull(1)       # Returns "PULLUP", "PULLDOWN", or "NONE"

# Connection status returns formatted strings
connected = is_connected(1, 5) # Returns "CONNECTED" (truthy) or "DISCONNECTED" (falsey)

# Voltage and current readings are automatically formatted
voltage = adc_get(0)          # Returns float (e.g., 3.300)
current = ina_get_current(0)  # Returns float in A (e.g., 0.0123)
power = ina_get_power(0)      # Returns float in W (e.g., 0.4567)

# All functions work with both numbers and string aliases
gpio_set_dir("GPIO_1", True)  # Same as gpio_set_dir(1, True)
connect("TOP_RAIL", "GPIO_1") # Same as connect(101, 131)
```
![Screenshot 2025-07-04 at 8 16 04 PM](https://github.com/user-attachments/assets/4ae5e7e2-845a-4e6e-bbd9-5c328624cfe9)



## Node Names and Constants
The Jumperless module provides extensive node name support with multiple aliases for each node:

```jython
# Power rails (multiple aliases supported)
TOP_RAIL = 101        # Also: TOPRAIL, T_R, TOP_R
BOTTOM_RAIL = 102     # Also: BOT_RAIL, BOTTOMRAIL, BOTRAIL, B_R, BOT_R
SUPPLY_3V3 = 103      # Also: 3V3, 3.3V
SUPPLY_5V = 105       # Also: 5V, +5V
SUPPLY_8V_P = 120     # Also: 8V_P, 8V_POS
SUPPLY_8V_N = 121     # Also: 8V_N, 8V_NEG

# Ground connections
GND = 100             # Also: GROUND
TOP_RAIL_GND = 104    # Also: TOP_GND (not actually routable but included for PADs)
BOTTOM_RAIL_GND = 126 # Also: BOT_GND, BOTTOM_GND (not actually routable but included for PADs)

# DAC outputs
DAC0 = 106            # Also: DAC_0, DAC0_5V
DAC1 = 107            # Also: DAC_1, DAC1_8V

# ADC inputs
ADC0 = 110            # Also: ADC_0, ADC0_8V
ADC1 = 111            # Also: ADC_1, ADC1_8V
ADC2 = 112            # Also: ADC_2, ADC2_8V
ADC3 = 113            # Also: ADC_3, ADC3_8V
ADC4 = 114            # Also: ADC_4, ADC4_5V
ADC7 = 115            # Also: ADC_7, ADC7_PROBE, PROBE

# Current sensing
ISENSE_PLUS = 108     # Also: ISENSE_POS, ISENSE_P, INA_P, I_P, CURRENT_SENSE_PLUS, ISENSE_POSITIVE, I_POS
ISENSE_MINUS = 109    # Also: ISENSE_NEG, ISENSE_N, INA_N, I_N, CURRENT_SENSE_MINUS, ISENSE_NEGATIVE, I_NEG

# GPIO pins (multiple naming conventions)
GPIO_1 = 131          # Also: RP_GPIO_1, GPIO1, GP_1, GP1
GPIO_2 = 132          # Also: RP_GPIO_2, GPIO2, GP_2, GP2
GPIO_3 = 133          # Also: RP_GPIO_3, GPIO3, GP_3, GP3
GPIO_4 = 134          # Also: RP_GPIO_4, GPIO4, GP_4, GP4
GPIO_5 = 135          # Also: RP_GPIO_5, GPIO5, GP_5, GP5
GPIO_6 = 136          # Also: RP_GPIO_6, GPIO6, GP_6, GP6
GPIO_7 = 137          # Also: RP_GPIO_7, GPIO7, GP_7, GP7
GPIO_8 = 138          # Also: RP_GPIO_8, GPIO8, GP_8, GP8

# UART pins
UART_TX = 116         # Also: RP_UART_TX, TX, RP_GPIO_16
UART_RX = 117         # Also: RP_UART_RX, RX, RP_GPIO_17

# Additional RP GPIOs
RP_GPIO_18 = 118      # Also: GP_18
RP_GPIO_19 = 119      # Also: GP_19

# Buffer connections
BUFFER_IN = 139       # Also: ROUTABLE_BUFFER_IN, BUF_IN, BUFF_IN, BUFFIN
BUFFER_OUT = 140      # Also: ROUTABLE_BUFFER_OUT, BUF_OUT, BUFF_OUT, BUFFOUT

# Arduino Nano pins (extensive support)
D13 = 83              # Also: NANO_D13
D12 = 82              # Also: NANO_D12
D11 = 81              # Also: NANO_D11
D10 = 80              # Also: NANO_D10
D9 = 79               # Also: NANO_D9
D8 = 78               # Also: NANO_D8
D7 = 77               # Also: NANO_D7
D6 = 76               # Also: NANO_D6
D5 = 75               # Also: NANO_D5
D4 = 74               # Also: NANO_D4
D3 = 73               # Also: NANO_D3
D2 = 72               # Also: NANO_D2
D1 = 71               # Also: NANO_D1
D0 = 70               # Also: NANO_D0

# Arduino Nano analog pins
A0 = 86               # Also: NANO_A0
A1 = 87               # Also: NANO_A1
A2 = 88               # Also: NANO_A2
A3 = 89               # Also: NANO_A3
A4 = 90               # Also: NANO_A4
A5 = 91               # Also: NANO_A5
A6 = 92               # Also: NANO_A6
A7 = 93               # Also: NANO_A7

# Arduino Nano non-routable hardwired connections
VIN = 69              # Unconnected to anything
RST0 = 94             # Hardwired to GPIO 18 on the RP2350
RST1 = 95             # Hardwired to GPIO 19 on the RP2350
N_GND0 = 97           # GND
N_GND1 = 96           # GND
NANO_5V = 99          # Hardwired to USB 5V bus (can also be used to power the Jumperless)
NANO_3V3 = 98         # Unconnected (without bridging the solder jumper on the back)

```




## The entire output of help()

```jython
>>> help()
Jumperless Native MicroPython Module
Hardware Control Functions with Formatted Output:
(GPIO functions return formatted strings like HIGH/LOW, INPUT/OUTPUT, PULLUP/NONE, CONNECTED/DISCONNECTED)

DAC (Digital-to-Analog Converter):
  jumperless.dac_set(channel, voltage)         - Set DAC output voltage
  jumperless.dac_get(channel)                  - Get DAC output voltage
  jumperless.set_dac(channel, voltage)         - Alias for dac_set
  jumperless.get_dac(channel)                  - Alias for dac_get

          channel: 0-3, DAC0, DAC1, TOP_RAIL, BOTTOM_RAIL
          channel 0/DAC0: DAC 0
          channel 1/DAC1: DAC 1
          channel 2/TOP_RAIL: top rail
          channel 3/BOTTOM_RAIL: bottom rail
            voltage: -8.0 to 8.0V

ADC (Analog-to-Digital Converter):
  jumperless.adc_get(channel)                  - Read ADC input voltage
  jumperless.get_adc(channel)                  - Alias for adc_get

                                              channel: 0-4

INA (Current/Power Monitor):
  jumperless.ina_get_current(sensor)          - Read current in amps
  jumperless.ina_get_voltage(sensor)          - Read shunt voltage
  jumperless.ina_get_bus_voltage(sensor)      - Read bus voltage
  jumperless.ina_get_power(sensor)            - Read power in watts
  Aliases: get_current, get_voltage, get_bus_voltage, get_power

             sensor: 0 or 1

GPIO:
  jumperless.gpio_set(pin, value)             - Set GPIO pin state
  jumperless.gpio_get(pin)                    - Read GPIO pin state
  jumperless.gpio_set_dir(pin, direction)     - Set GPIO pin direction
  jumperless.gpio_get_dir(pin)                - Get GPIO pin direction
  jumperless.gpio_set_pull(pin, pull)         - Set GPIO pull-up/down
  jumperless.gpio_get_pull(pin)               - Get GPIO pull-up/down
  Aliases: set_gpio, get_gpio, set_gpio_dir, get_gpio_dir, etc.

            pin 1-8: GPIO 1-8
            pin   9: UART Tx
            pin  10: UART Rx
              value: True/False   for HIGH/LOW
          direction: True/False   for OUTPUT/INPUT
               pull: -1/0/1       for PULL_DOWN/NONE/PULL_UP

PWM (Pulse Width Modulation):
  jumperless.pwm(pin, [frequency], [duty])    - Setup PWM on GPIO pin
  jumperless.pwm_set_duty_cycle(pin, duty)    - Set PWM duty cycle
  jumperless.pwm_set_frequency(pin, freq)     - Set PWM frequency
  jumperless.pwm_stop(pin)                    - Stop PWM on pin
  Aliases: set_pwm, set_pwm_duty_cycle, set_pwm_frequency, stop_pwm

             pin: 1-8       GPIO pins only
       frequency: 0.001-62500000 default 1000Hz
      duty_cycle: 0.0-1.0   default 0.5 (50%)
  **Frequency Ranges:**
  - Hardware PWM: 10Hz to 62.5MHz (high precision)
  - Slow PWM: 0.001Hz to 10Hz (hardware timer based)
  - Automatic mode selection based on frequency

Node Connections:
  jumperless.connect(node1, node2)            - Connect two nodes
  jumperless.disconnect(node1, node2)         - Disconnect nodes
  jumperless.is_connected(node1, node2)       - Check if nodes are connected

  jumperless.nodes_clear()                    - Clear all connections
         set node2 to -1 to disconnect everything connected to node1

OLED Display:
  jumperless.oled_print("text")               - Display text
  jumperless.oled_clear()                     - Clear display
  jumperless.oled_connect()                   - Connect OLED
  jumperless.oled_disconnect()                - Disconnect OLED

Clickwheel:
  jumperless.clickwheel_up([clicks])          - Scroll up
  jumperless.clickwheel_down([clicks])        - Scroll down
  jumperless.clickwheel_press()               - Press button
           clicks: number of steps

Status:
  jumperless.print_bridges()                  - Print all bridges
  jumperless.print_paths()                    - Print path between nodes
  jumperless.print_crossbars()                - Print crossbar array
  jumperless.print_nets()                     - Print nets
  jumperless.print_chip_status()              - Print chip status

Probe Functions:
  jumperless.probe_read([blocking=True])      - Read probe (default: blocking)
  jumperless.read_probe([blocking=True])      - Read probe (default: blocking)
  jumperless.probe_read_blocking()            - Wait for probe touch (explicit)
  jumperless.probe_read_nonblocking()         - Check probe immediately (explicit)
  jumperless.get_button([blocking=True])      - Get button state (default: blocking)
  jumperless.probe_button([blocking=True])    - Get button state (default: blocking)
  jumperless.probe_button_blocking()          - Wait for button press (explicit)
  jumperless.probe_button_nonblocking()       - Check buttons immediately (explicit)
  Touch aliases: probe_wait, wait_probe, probe_touch, wait_touch (always blocking)
  Button aliases: button_read, read_button (parameterized)
  Non-blocking only: check_button, button_check
  Touch returns: ProbePad object (1-60, D13_PAD, TOP_RAIL_PAD, LOGO_PAD_TOP, etc.)
  Button returns: CONNECT, REMOVE, or NONE (front=connect, rear=remove)

Misc:
  jumperless.arduino_reset()                  - Reset Arduino
  jumperless.probe_tap(node)                  - Tap probe on node (unimplemented)
  jumperless.run_app(appName)                 - Run app
  jumperless.pause_core2(pause)               - Pause/resume core2 processing
  jumperless.send_raw(chip, x, y, setOrClear) - Send raw data to core2
  jumperless.format_output(True/False)        - Enable/disable formatted output

Help:
  jumperless.help()                           - Display this help

Node Names:
  jumperless.node("TOP_RAIL")                  - Create node from string name
  jumperless.TOP_RAIL                        - Pre-defined node constant
  jumperless.D2, jumperless.A0, etc.         - Arduino pin constants
  For global access: from jumperless_nodes import *
  Node names: All standard names like "D13", "A0", "GPIO_1", etc.

Examples (all functions available globally):
  dac_set(TOP_RAIL, 3.3)                     # Set Top Rail to 3.3V using node
  set_dac(3, 3.3)                            # Same as above using alias
  dac_set(DAC0, 5.0)                         # Set DAC0 using node constant
  voltage = get_adc(1)                       # Read ADC1 using alias
  connect(TOP_RAIL, D13)                     # Connect using constants
  connect("TOP_RAIL", 5)                      # Connect using strings
  connect(4, 20)                             # Connect using numbers
  top_rail = node("TOP_RAIL")                 # Create node object
  connect(top_rail, D13)                     # Mix objects and constants
  oled_print("Fuck you!")                    # Display text
  current = get_current(0)                   # Read current using alias
  set_gpio(1, True)                          # Set GPIO pin high using alias
  pwm(1, 1000, 0.5)                         # Hardware PWM: 1kHz, 50% duty
  pwm(2, 0.1, 0.25)                         # Slow PWM: 0.1Hz, 25% duty
  pwm(3, 0.001, 0.5)                        # Ultra-slow PWM: 0.001Hz, 50% duty
  pad = probe_read()                         # Wait for probe touch
  if pad == 25: print('Touched pad 25!')    # Check specific pad
  if pad == D13_PAD: connect(D13, TOP_RAIL)  # Auto-connect Arduino pin
  if pad == TOP_RAIL_PAD: show_voltage()     # Show rail voltage
  if pad == LOGO_PAD_TOP: print('Logo!')    # Check logo pad
  button = get_button()                      # Wait for button press (blocking)
  if button == CONNECT_BUTTON: ...          # Front button pressed
  if button == REMOVE_BUTTON: ...           # Rear button pressed
  button = check_button()                   # Check buttons immediately
  if button == BUTTON_NONE: print('None')   # No button pressed
  pad = wait_touch()                        # Wait for touch
  btn = check_button()                      # Check button immediately
  if pad == D13_PAD and btn == CONNECT_BUTTON: connect(D13, TOP_RAIL)
  pause_core2(True)                         # Pause core2 processing
  send_raw("A", 1, 2, 1)                    # Send raw data to core2

Note: All functions and constants are available globally!
No need for 'jumperless.' prefix in REPL or single commands.

>>> 
```



## The entire output of nodes_help()

```jython
>>> nodes_help()
Jumperless Node Reference
========================

NODE TYPES:
  Numbered:     1-60 (breadboard)
  Arduino:      D0-D13, A0-A7 (nano header)
  GPIO:         GPIO_1-GPIO_8 (routable GPIO)
  Power:        TOP_RAIL, BOTTOM_RAIL, GND
  DAC:          DAC0, DAC1 (analog outputs)
  ADC:          ADC0-ADC4, PROBE (analog inputs)
  Current:      ISENSE_PLUS, ISENSE_MINUS
  UART:         UART_TX, UART_RX
  Buffer:       BUFFER_IN, BUFFER_OUT

THREE WAYS TO USE NODES:

1. NUMBERS (direct breadboard holes):
   connect(1, 30)                     # Connect holes 1 and 30
   connect(15, 42)                    # Any number 1-60

2. STRINGS (case-insensitive names):
   connect("D13", "TOP_RAIL")         # Arduino pin to power rail
   connect("gpio_1", "adc0")          # GPIO to ADC (case-insensitive)
   connect("15", "dac1")              # Mix numbers and names

3. CONSTANTS (pre-defined objects):
   connect(TOP_RAIL, D13)            # Using imported constants
   connect(GPIO_1, A0)               # No quotes needed
   connect(DAC0, 25)                 # Mix constants and numbers

MIXED USAGE:
   my_pin = "D13"                    # Create node object from string
   connect(my_pin, TOP_RAIL)         # Use node object with constant
   oled_print(my_pin)                # Display shows 'D13'

COMMON ALIASES (many names work for same node):
   "TOP_RAIL" = "T_R"
   "GPIO_1" = "GPIO1" = "GP1"
   "DAC0" = "DAC_0"
   "UART_TX" = "TX"

NOTES:
  - String names are case-insensitive: "d13" = "D13" = "nAnO_d13"
  - Constants are case-sensitive: use D13, not d13
  - All three methods work in any function
```

![Screenshot 2025-07-04 at 8 27 39 PM](https://github.com/user-attachments/assets/8d8dfc16-0dca-4ab8-9bcf-c511415bffc7)

