
# File Manager

The Jumperless has a built in File Manager which you can access in the menu with `/`, or enter `U` in the menu and Jumperless will mount as a USB Mass Storage drive called `JUMPERLESS` where you can edit files on the filesystem.

## Directory Structure


<img width="901" alt="FileManager" src="https://github.com/user-attachments/assets/de4a251a-9727-422d-ade0-53984cf67fba" />
<!-- 
<img width="898" alt="Screenshot 2025-07-06 at 11 25 26 AM" src="https://github.com/user-attachments/assets/aa5db6a7-f9e1-4ea8-902c-050626712c07" /> -->

<img width="657" height="486" alt="Screenshot 2025-07-15 at 1 50 47 PM" src="https://github.com/user-attachments/assets/b4cc86db-7330-4bac-b160-c25eef27a8fa" />


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
| **⟐** | JSON files | .json | Cyan |
| **☊** | Node files | nodeFileSlot*.txt | Magenta |
| **⎃** | Color files | netColorsSlot*.txt | Orange |




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




