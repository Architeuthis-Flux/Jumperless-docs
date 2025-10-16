# The App

## Installation guide

### The Jumperless App is now on PyPi!

The easiest way to get started is with pip:

```bash
pip install jumperless
```

Then run it with:

```bash
jumperless
```

**Note:** If the app version shows less than the latest release, `pip` defaults to a local version if it's available. In that case, run:

```bash
pip install --no-cache-dir --upgrade jumperless
```

to make sure it grabs the latest version.

The app repo is at [https://github.com/Architeuthis-Flux/Jumperless-App](https://github.com/Architeuthis-Flux/Jumperless-App)

### Alternative: Download Pre-built Binaries

#### Find the latest release
[https://github.com/Architeuthis-Flux/JumperlessV5/releases/latest](https://github.com/Architeuthis-Flux/JumperlessV5/releases/latest)

The link above will magically lead you to the latest version, and will look something like `https://github.com/Architeuthis-Flux/JumperlessV5/releases/tag/5.2.0.0`

**At the bottom under Assets, download the Jumperless App for your OS**

### Windows

  - `Jumperless.exe`
  - `Jumperless-Windows-x64.zip`
  
### macOS

  - `Jumperless_Installer.dmg`
  - `Jumperless_macOS.zip`
  
### Linux

  - x86 `Jumperless-linux-x86_64.tar.gz` (if you're not sure which flavor of Linux, use this one)
  - arm64 `Jumperless-linux-arm64.tar.gz`
  
### Python

  1. download `JumperlessWokwiBridge.py` and `requirements.txt`
  2. open your favorite terminal, navigate to the folder where you downloaded the two files above.
  3. `pip install -r requirements.txt` # run this command to install the needed Python libraries
  4. `python3 JumperlessWokwiBridge.py` # open the app, will update firmware if there's a newer version

---

Now that I've lifted my self-imposed ban on VT100 commands (for compatibility and me-spending-too-much-time-on-them reasons, but, YOLO), we've got colors now! 

<img width="749" alt="Screenshot 2025-05-29 at 10 01 15 PM" src="https://github.com/user-attachments/assets/a0fbbca6-ec16-4a0e-ac36-b4ed1f46663a" />


But that's like the *least* cool thing the new app can do, here's a list of what's new:

## What It Does


- **Firmware updating** should be pretty reliable when there's a new version (falls back to instructions for how to do it manually)
- **Command history and tab completion**, up arrows will go through past commands and are persistent after closing
- **Properly detects** which port is the main Jumperless Serial and which is routable UART
- **Arduino flashing from [Wokwi](https://wokwi.com/)** works once again and is a lot more solid
  - It installs [arduino-cli](https://github.com/arduino/arduino-cli) on first startup and uses it pull in libraries, compile, and flash an arduino Nano in the header
  - If the routable UART lines aren't connected when the app detects a change in the sketch file, it will connect them to flash the new code and then return them to how they were
  - [avrdude](https://github.com/avrdudes/avrdude) output is shown in real time (you'd be amazed how difficult this was)
- **Direct Wokwi circuit import** - Copy diagram.json from Wokwi and import it with the `W` command (see below)
- **No longer a janky pile of garbage**
## Local Arduino Sketch Support

**You can set a `slot` to point to a local Arduino sketch.ino file and it will flash if it detects a change** 

- If you don't like using Arduino IDE or Wokwi and prefer using `vim` or `emacs` or whatever, now you can let the app handle the flashing stuff and just edit an .ino file.
- In the app, type `menu` then `slots` and instead of entering a link to a Wokwi project, just give it a path to a file (this will be saved so you can unassign it and pick it later by name)
- (This one is so fucking sick) 

<img width="1330" alt="Screenshot 2025-05-29 at 9 16 14 AM" src="https://github.com/user-attachments/assets/766dbb09-254e-45c5-8f75-358684729907" />

## Launch Scripts

- Launch scripts included to easily run it from your favorite terminal emulator and not just the system default (terminal.app on macOS, Powershell on Windows, idk on Linux), just go to the directory in a terminal and run the script in [tabby](https://tabby.sh/) or whatever
- The launcher *should* kill other instances (and close their windows) that happen to be open because it's such a common issue for me at least
- Linux people are no longer red-headed stepchildren, there are proper tar.gz packages now for you nerds

## Importing Circuits from Wokwi

You can design circuits in the [Wokwi online simulator](https://wokwi.com) and import them directly to your Jumperless with the `W` command, or use the Jumperless App and it'll pull it from your project automatically and live update.

### Direct Link Import

You can now just dump a Wokwi link into the app at any time and it'll work:

```
		Menu
~~~~~
	x = clear all connections
	+ = add connections
	- = remove connections

https://wokwi.com/projects/424432011346848769


Enter a name for this new project: cool project zone
✓ Saved 'cool project zone' to project library

✓ 'cool project zone' assigned to active slot 0
  URL: https://wokwi.com/projects/424432011346848769
  The project will start updating automatically
```

### How to manually Import from Wokwi

1. **Design your circuit** on [wokwi.com](https://wokwi.com)
2. **Click on the `diagram.json` tab** in the Wokwi editor
3. **Copy all the JSON content** (Ctrl+A, Ctrl+C or Cmd+A, Cmd+C)
4. **In Jumperless, type `W`** and press Enter
5. **Paste the JSON** (Ctrl+V or right-click → Paste)
6. The parser automatically detects when the JSON is complete and imports it!

### Supported Wokwi Components

- **Half breadboard** - Wokwi's breadboard maps directly to Jumperless rows
- **Arduino Nano** - All pins (D0-D13, A0-A7) (GND, 5V, 3.3V, and RST pins are hardwired and don't do anything)
- **Logic Analyzer** - Channels map to GPIO: D0-7 → GPIO 1-8
- **Wire colors** - Wokwi wire colors preserved
- **Rail voltages** - Detected from text labels in Wokwi
- **VCC and GND Nodes** - VCC maps to the `TOP_RAIL`

![LogicAnalyzerMappingV5](https://github.com/user-attachments/assets/3b7bd360-9703-4b0b-925a-aea8ed7e0526)

**Note:** The app still works with the OG Jumperless and those original mappings remain the same.

### Wire Color Mapping

**Wire colors will match the ones you set in Wokwi!** The new Wokwi parser sends the entire `diagram.json` from Wokwi and parses it on the Jumperless, which means color information gets preserved.

![wokwiColor-2](https://github.com/user-attachments/assets/e5607cf9-3a95-42f7-b67c-875ba23e2ee9)

![wokwiColor-1](https://github.com/user-attachments/assets/8a148940-60f8-4741-8905-6b9911ac1f21)

All Wokwi wire colors are preserved and displayed on the breadboard LEDs:

`red`, `orange`, `yellow`, `green`, `blue`, `violet`, `purple`, `magenta`, `cyan`, `white`, `gray`, `black`, `brown`, `limegreen`, `gold`

**Note:** Black wires let the Jumperless auto-assign a color.

If you leave all the wires green (the default in Wokwi) or make a wire black, it'll just auto assign colors.

**About color assignment:** There is some weirdness because colors in Wokwi are applied to `bridges` (a pair of `nodes`) while color in the Jumperless gets assigned to `nets` (a collection of connected `nodes`). So if you have a bunch of things electrically connected together with different wire colors, it'll just pick one. It tries to pick unique colors first (no other nets with that same color), but if it can't, it'll shift the hue a bit so it's still that color but you can hopefully tell them apart.

### Rail Voltage Detection

Add a text label in your Wokwi diagram to specify rail voltages:

```
top rail 5.5V
bottom rail 3.5V
```

The Jumperless parser will automatically detect these values and set the rails accordingly

### Command Variants

```
W              # Paste JSON, save to active slot
W 5            # Paste JSON, save to slot 5
W /file.json   # Load from file, save to active slot
```

### After Import

Use `<` to cycle through slots to activate your imported circuit, or it will be active immediately if imported to the current slot.

## Terminal Compatibility

Or you can use any terminal emulator you like, [iTerm2](https://iterm2.com/), [xTerm](https://invisible-island.net/xterm/), [Tabby](https://github.com/Eugeny/tabby), [Arduino IDE](https://www.arduino.cc/en/software/)'s Serial Monitor, whatever. The TUI is all handled from the Jumperless itself so it just needs something to print text. 