
# File Manager

The Jumperless has a built in File Manager which you can access in the menu with `/`, or enter `U` in the menu and Jumperless will mount as a USB Mass Storage drive called `JUMPERLESS` where you can edit files on the filesystem.

## File System Structure

```
├── config.txt
│
├── slots/
│   ├── slot0.yaml
│   ├── slot1.yaml
│   ├── slot2.yaml
│   └── ... (up to slot7.yaml)
│
└── python_scripts/
    ├── history.txt
    ├── cool_micropython_script.py
    ├── ... (your python scripts go here)
    │
    └── examples/
        ├── adc_basics.py
        ├── dac_basics.py
        ├── gpio_basics.py
        ├── led_brightness_control.py
        ├── node_connections.py
        ├── stylophone.py
        ├── uart_basics.py
        ├── uart_loopback.py
        └── voltage_monitor.py
```

Each slot's configuration is stored as a YAML file in the `/slots/` directory, and the global hardware configuration is in `/config.txt`.



## Navigation

### Basic Movement

| Control | Action |
|---------|--------|
| **↑/↓ Arrow Keys** or **Rotary Encoder** | Move selection up/down |
| **Enter** or **Click Encoder** | Open directory or edit file |
| **/** | Go to root directory |
| **.** | Go up one directory|
| **CTRL + q** | Quit File Manager or Text Editor


### File Manager Commands
| Key | Action | Description |
|-----|--------|-------------|
| [enter] | Open | Open file or enter directory |
| **h** | Help | Show help |
| **v** | Quick view | View file contents |
| **.** | Up dir | Go up one directory  |
| **n** | New file | Create new file (prompts for filename) |
| **d** | New directory | Create new directory |
| **x** | Delete | Delete file or directory (confirm with `y`/`N`) |



### File Type Icons and Colors
| Icon | File Type | Extensions | Color |
|------|-----------|------------|-------|
| **⌘** | Directories | - | Blue |
| **𓆚** | Python files | .py, .pyw, .pyi | Green |
| **⍺** | Text files | .txt, .md | White |
| **⚙** | Config files | .cfg, .conf, config.txt | Yellow |
| **⟐** | JSON/YAML files | .json, .yaml | Cyan |
| **☊** | Slot files | /slots/slot*.yaml | Magenta |
| **⎃** | Legacy slot files | nodeFileSlot*.txt | Orange |




## Jumperless Kilo Text Editor

The File Manager also has text editor based off [**eKilo**](https://github.com/antonio-foti/ekilo)

<img width="928" alt="Screenshot 2025-07-06 at 11 25 50 AM" src="https://github.com/user-attachments/assets/1b4c74bc-19fa-4e74-8799-b778e8a56825" />


### Editor Controls
- **Ctrl+S**: Save file
- **Ctrl+Q**: Quit editor
- **Ctrl+P**: Save and launch MicroPython REPL
- **Arrow keys**: Navigate cursor
- **Rotary encoder**: Move cursor horizontally
- **Click encoder**: Enter character selection mode (you can scroll through the letters on the OLED and click again to insert it)

### Character Selection With the Click Wheel and OLED
When using the rotary encoder in the editor:

- **Click encoder**: Enter character selection mode
- **Rotate encoder**: Cycle through available characters
- **Click encoder**: Confirm character selection
- **Wait 3 seconds**: Exit character selection mode

Yes, you could write code with just the click wheel and the OLED if you really wanted to.


### MicroPython Examples
The File Manager automatically creates example Python scripts in `/python_scripts/examples/`:

- **01_dac_basics.py**: DAC (Digital-to-Analog Converter) examples
- **02_adc_basics.py**: ADC (Analog-to-Digital Converter) examples  
- **03_gpio_basics.py**: GPIO (General Purpose Input/Output) examples
- **04_node_connections.py**: Node connection and routing examples
- **led_brightness_control.py**: LED brightness control
<!-- - **voltage_monitor.py**: Voltage monitoring utilities
- **stylophone.py**: Musical instrument example -->

You can trigger them to regenerate if you messed them up by deleting it with `x`, and then entering `m` to create new copies of any examples it doesn't see.


## Editing Slot Files

Slot files (located in `/slots/`) use **YAML format** and can be edited directly! They're human-readable files containing:

- **bridges** - Your circuit connections
- **power** - Rail and DAC voltages
- **colors** - Wire colors from Wokwi or custom colors
- **config** - Routing preferences and GPIO settings

**Example slot file:**
```yaml
version: 2
sourceOfTruth: bridges

bridges:
  - {n1: 1, n2: 10, dup: 2, color: red}
  - {n1: NANO_D5, n2: GPIO_1, dup: 2}
  - {n1: TOP_RAIL, n2: 5, dup: 2}

power:
  topRail: 3.30
  bottomRail: 2.50
  dac0: 3.33
  dac1: 0.00
```

**Named nodes** you can use: `NANO_D0-D13`, `NANO_A0-A7`, `GPIO_1-8`, `TOP_RAIL`, `BOTTOM_RAIL`, `GND`, `DAC0_5V`, `DAC1_5V`, and more (see [glossary](99-glossary.md))

When you edit and save a slot file, the Jumperless will automatically reload it if it's the active slot. This works whether you're using the onboard eKilo editor or have the Jumperless mouned as a USB Mass Storage drive and are editing the files on your computer in you favorite editor.

## USB Mass Storage

Enter `U` in the menu and Jumperless will mount as a USB Mass Storage drive called `JUMPERLESS` where you can edit files on the filesystem.

Keep in mind that file operations are pretty slow, so make sure to give it time to fully save files when you drop them onto the filesystem.

When you're finished `u` (or just eject the drive) will unmount the Mass Storage device.

You can also enter `Z` for a little debug menu

<img width="757" height="380" alt="Screenshot 2025-07-15 at 8 55 44 AM" src="https://github.com/user-attachments/assets/124d2f5a-a320-453f-8598-7604f37a57d7" />

<img width="179" height="189" alt="Screenshot 2025-07-15 at 8 55 54 AM" src="https://github.com/user-attachments/assets/4531cae9-56d9-42da-9279-952f7b23d405" />

<img width="1014" height="463" alt="Screenshot 2025-07-15 at 8 56 13 AM" src="https://github.com/user-attachments/assets/a9e79a69-a7da-4365-a457-44b2c5d2fc24" />



## OLED Display Support

If you have an OLED connected, the File Manager shows:
- **Current path** and **selected file**
- **File navigation** with scrolling support
- **Real-time updates** as you navigate





## Navigation Reference
| Key | Action |
|-----|--------|
| ↑/↓ | Move selection |
| Enter | Open/Edit |
| / | Go to root |
| . | Go up directory |
| h | Show help |

### File Operations
| Key | Action |
|-----|--------|
| v | View file |
| e | Edit file |
| i | File info |
| n | New file |
| d | New directory |
| x | Delete |
| r | Refresh |

### System
| Key | Action |
|-----|--------|
| u | Memory status |
| m | Initialize examples |
| Ctrl+Q | Quit |




