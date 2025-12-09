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

If you just want an overview of all the available calls, check out the [MicroPython API Reference](09.5-micropythonAPIreference.md)


## Now you can live code with [Viper IDE](https://viper-ide.org/)!
Holy shit I should have done this years ago

Seriously, this is *such* a better experience than using the onboard text editor and REPL, you should play with it right now

Go to [https://viper-ide.org/](https://viper-ide.org/) and press the connect button.

<img width="1303" height="1246" alt="Screenshot 2025-12-08 at 6 13 21 PM" src="https://github.com/user-attachments/assets/47edf213-8e91-4904-beb4-3a93d71538db" />


Choose the 3rd Jumperless port in that list (Windows may not put them in order, so if nothing happens, try the other ones) and click Connect

<img width="1304" height="1250" alt="Screenshot 2025-12-08 at 6 13 46 PM" src="https://github.com/user-attachments/assets/a9ea53fa-86fd-46b0-839d-eeaa32606454" />

Then open some examples (this update should overwrite the examples with the new ones) and hit the Run / Stop button

<img width="1304" height="1250" alt="Screenshot 2025-12-08 at 6 14 23 PM" src="https://github.com/user-attachments/assets/0190af73-cd5f-49e9-b378-bb6d1c8a7bb4" />

Press it again to Stop. If you make changes, hit the green Save button next to it (it takes a second and the script should be stopped.)

<img width="1306" height="1249" alt="Screenshot 2025-12-08 at 6 15 54 PM" src="https://github.com/user-attachments/assets/29413b36-1de1-478e-8d67-70cb4146fd60" />

### If you write something cool, send it to me and I'll add it to the default examples (I'll put a page on this site soon where you can share them.)


This is using [MicroPython's built-in Raw REPL](https://docs.micropython.org/en/latest/reference/repl.html#raw-mode-and-raw-paste-mode), so anything that can interact with that will work here. I've only tested with Viper IDE but I'm pretty sure just about anything else would work.


There's also `jumperless.py` and `jumperless.pyi` module with stubs for all the built-in functions so syntax highlighting and autocomplete  will work in your favorite code editor (sorry, autocomplete for jumperless functions doesn't work in ViperIDE.) You can grab them here:

### [jumperless.py](https://github.com/Architeuthis-Flux/JumperlOS/blob/main/scripts/jumperless.py)
### [jumperless.pyi](https://github.com/Architeuthis-Flux/JumperlOS/blob/main/scripts/jumperless.pyi)






## Quick Start (to do it from the built-in REPL)

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

# Read GPIO state - returns GPIOState object (prints as "HIGH", "LOW", or "FLOATING")
state = gpio_get(2)
print(state)            # Prints "HIGH", "LOW", or "FLOATING"
if state:               # GPIOState is truthy when HIGH, falsy when LOW/FLOATING
    print("It's HIGH!")

# Configure pull resistors
gpio_set_pull(3, 1)     # Enable pull-up
gpio_set_pull(3, -1)    # Enable pull-down
gpio_set_pull(3, 0)     # No pull resistor

# Read GPIO configuration - returns custom types that print nicely
direction = gpio_get_dir(1)    # Prints "INPUT" or "OUTPUT"
pull = gpio_get_pull(2)        # Prints "PULLUP", "PULLDOWN", or "NONE"

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

## WaveGen (Waveform Generator)
```jython
# Basic sine wave generation
wavegen_set_output(DAC1)      # Output on DAC1
wavegen_set_wave(SINE)        # Sine wave
wavegen_set_freq(100)         # 100 Hz
wavegen_set_amplitude(3.3)    # 3.3V peak-to-peak
wavegen_set_offset(1.65)      # Center at 1.65V (0 to 3.3V range)
wavegen_start()               # Start generating

# Available waveforms: SINE, TRIANGLE, SAWTOOTH (or RAMP), SQUARE

# Change parameters while running
wavegen_set_wave(TRIANGLE)
wavegen_set_freq(50)

# Check status
if wavegen_is_running():
    freq = wavegen_get_freq()
    print("Running at " + str(freq) + " Hz")

# Stop generation
wavegen_stop()

# Sweep configuration (for scripts that use it)
wavegen_set_sweep(20, 2000, 5)  # Sweep from 20Hz to 2000Hz over 5 seconds
```

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

# Connection context - controls whether changes persist after exiting Python
context_toggle()           # Toggle between 'global' and 'python' modes
print(context_get())       # Shows current mode: "global" or "python"

# Show help
help()                # Display all available functions
nodes_help()          # Show all available node names and aliases
```

The [help()](09.5-micropythonAPIreference.md#the-entire-output-of-help) and [nodes_help()](09.5-micropythonAPIreference.md#the-entire-output-of-nodes_help) functions will list all the available commands (except for the new ones I forget to update)

## Slot Management
```jython
# Save current connections to current slot
nodes_save()

# Save to a specific slot (0-7)
nodes_save(3)

# Switch to a different slot
old = switch_slot(2)
print("Switched from slot " + str(old) + " to slot 2")

# Check for unsaved changes
if nodes_has_changes():
    print("You have unsaved changes!")
    nodes_save()  # Save them

# Discard changes and restore last saved state
nodes_discard()
```

## Net Information
```jython
# Get info about nets (groups of connected nodes)
num_nets = get_num_nets()
print("Active nets: " + str(num_nets))

# Get and set net names
name = get_net_name(6)
set_net_name(7, "VCC")
set_net_name(6, "Signal_In")

# Get and set net colors
color_name = get_net_color_name(6)
print("Net 6 is " + color_name)

# Set colors by name
set_net_color(6, "red")
set_net_color(7, "cyan")
set_net_color(8, "pink")

# Set colors by hex
set_net_color(6, "#FF00FF")  # Magenta
set_net_color(7, "0x00FF00")  # Green

# Get full net info as a dictionary
info = get_net_info(6)
print("Name: " + info['name'])
print("Color: " + info['color_name'])
print("Nodes: " + info['nodes'])

# List all bridges
num_bridges = get_num_bridges()
for i in range(num_bridges):
    bridge = get_bridge(i)
    print("Bridge " + str(i) + ": " + str(bridge))
```



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
    
    # Read input (gpio_get returns truthy for HIGH, falsy for LOW)
    if gpio_get(2):
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


## Connection Context Switching

The MicroPython REPL now supports **connection contexts** that determine how connections persist:

- **`global` context**: Changes persist to global state - connections remain after exiting Python
- **`python` context**: Connections are restored to how they were when exiting REPL (saved to `slots/slotPython.yaml`)

**To toggle contexts:** Type `context` in the REPL

**How it works:**
- In `global` mode: Any connections you make become permanent, just like using the normal command interface
- In `python` mode: The connection state when you entered the REPL is saved, and restored when you exit
- The current context is displayed in the REPL prompt


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
The Jumperless module returns custom types that print nicely but also work in conditionals:

```jython
# GPIO functions return custom types that print as readable strings
state = gpio_get(1)           # Prints "HIGH", "LOW", or "FLOATING"
direction = gpio_get_dir(1)   # Prints "INPUT" or "OUTPUT"
pull = gpio_get_pull(1)       # Prints "PULLUP", "PULLDOWN", or "NONE"

# These types are also truthy/falsy for use in conditionals:
if gpio_get(1):               # True if HIGH, False if LOW or FLOATING
    print("Pin is HIGH")
if gpio_get_dir(1):           # True if OUTPUT, False if INPUT
    print("Pin is output")

# Connection status works the same way
connected = is_connected(1, 5) # Prints "CONNECTED" or "DISCONNECTED"
if connected:                  # True if connected, False if not
    print("Nodes are connected")

# Voltage and current readings are floats
voltage = adc_get(0)          # Returns float (e.g., 3.300)
current = ina_get_current(0)  # Returns float in A (e.g., 0.0123)
power = ina_get_power(0)      # Returns float in W (e.g., 0.4567)

# All functions work with both numbers and string aliases
gpio_set_dir("GPIO_1", True)  # Same as gpio_set_dir(1, True)
connect("TOP_RAIL", "GPIO_1") # Same as connect(101, 131)
```
![Screenshot 2025-07-04 at 8 16 04 PM](https://github.com/user-attachments/assets/4ae5e7e2-845a-4e6e-bbd9-5c328624cfe9)



