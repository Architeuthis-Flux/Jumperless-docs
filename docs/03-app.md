# The App

## Installation guide

### Find the latest release
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

## Terminal Compatibility

Or you can use any terminal emulator you like, [iTerm2](https://iterm2.com/), [xTerm](https://invisible-island.net/xterm/), [Tabby](https://github.com/Eugeny/tabby), [Arduino IDE](https://www.arduino.cc/en/software/)'s Serial Monitor, whatever. The TUI is all handled from the Jumperless itself so it just needs something to print text. 