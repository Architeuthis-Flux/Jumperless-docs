# OLED Support

First, get yourself one of these bad boys (literally any of these are fine.)

[![oled Medium](https://github.com/user-attachments/assets/9b7c6957-3b5f-4296-a0ca-1a5517a1b83b)](https://www.amazon.com/dp/B0CDWQ2RWY/)
https://www.amazon.com/MakerFocus-Display-SSD1306-3-3V-5V-Arduino/dp/B079BN2J8V

![batchone-11](https://github.com/user-attachments/assets/26cc687d-6ebb-40b7-9b72-7eada7a5258c)
Ignore the really cool LEDs.

## Installation

They should friction fit into the SBC/SMD/OLED board included with your Jumperless V5.
![SBCBP-4 copy](https://github.com/user-attachments/assets/43232b06-380d-4e18-9aab-924e45790740)

## Functionality

This should copy basically any text printed on the breadboard, some people have trouble reading text on the breadboard LEDs, which is why I added all this. (if I missed something, let me know, it's a fairly new thing so I've probably forgot to add code for it to print in a bunch of places.)

## Connection

To connect the data lines to the Jumperless' GPIO 7 and 8, just use the menu option `.` (that's a period). It will try to find the OLED on the I2C bus, after a few failed attempts, it'll automatically disconnect to free up GPIO 7 and 8. 

## Auto-Connect on Boot

If you want to use this all the time, there's a config option to connect the OLED on startup. You can just paste this into the main menu:
```
`[top_oled] connect_on_boot = true;
``` 

## Lock Connection

Locking the connection to the OLED ensures that it stays connected even when you enter a complete `node` list. So if you're using Wokwi or manually adding connections in a file, you don't need to add `GPIO_7 - D2` and `GPIO_8 - D3` to keep the I2C connected to the OLED.

```
`[top_oled] lock_connection = true;
```
 
  
## Custom Startup Message

You can customize what appears on the OLED when your Jumperless boots up. There are two options: text messages or custom bitmap images.

### Text Message

Set a custom text message to display on the OLED at startup (max 32 characters):

```jython
`[top_oled] startup_message = Your Message Here;
```

This message will appear after the Jumperless logo on boot.

### Bitmap Image

Display a custom bitmap image at startup by just giving it a path on the filesystem.

```jython
`[top_oled] startup_message = /images/mylogo.bin;
```

**Requirements:**
- Image must be a bitmap file (`.bin` format) with 4-byte header
- Recommended size: 128×32 pixels (standard OLED size)
- Use the built-in [Bitmap Editor](#bitmap-editor) to create or edit images
- Store images in the `/images/` directory on the Jumperless filesystem



## Display Dimensions

If you have a different sized OLED (like 128x64), you can set the dimensions:

```jython
`[top_oled] width = 128;
`[top_oled] height = 64;
```

## Advanced GPIO Configuration

You can change both the GPIO used for the display or the rows it connects to with the config options:

```jython
`[top_oled] sda_pin = 26;
`[top_oled] scl_pin = 27;
`[top_oled] gpio_sda = GP_7;
`[top_oled] gpio_scl = GP_8;
`[top_oled] sda_row = D2;
`[top_oled] scl_row = D3;
```

# Bitmap Editor

The built-in bitmap editor lets you create and edit OLED images directly on your Jumperless using your terminal and the clickwheel encoder. Perfect for creating custom startup images, icons, or pixel art!

## Accessing the Bitmap Editor

### From File Manager

1. Open the file manager from the main menu
2. Navigate to a `.bin` bitmap file 
3. Select the file to open it in the editor

### Creating a New Image

You can create a new bitmap file from the file manager:
1. Navigate to where you want to create the file (e.g., `/images/`)
2. Pess `n` for "new file"
3. Name it with a `.bin` extension (e.g., `mylogo.bin`)
4. The editor will automatically create a blank 128×32 bitmap (or whatever your OLED dimensions are set to in config)

## Editor Interface

The bitmap editor displays your image in the terminal and on the OLED (if connected). You'll see:

- **Main canvas**: Your bitmap rendered using block characters
- **Status bar**: Filename, dimensions, cursor position, and save status
- **Menu bar**: Quick access to View, Encoder, Draw modes, Save, and Quit
- **Help panel**: Keyboard shortcuts and hardware control reference

### View Modes

Press `m` to cycle through three display modes:

1. **Full Block Mode** (1:1 pixel mapping)
   - Each character = 1 pixel

2. **Half Block Mode** (2:1 vertical compression)
   - Each character = 2 pixels vertically
   - Fits 128×32 images on smaller terminals

3. **Quarter Block Mode** (2×2 compression)
   - Each character = 2×2 pixels (4 pixels total)
   - Fits larger images on screen
   

## Navigation

### Moving the Cursor

**Keyboard:**
- Arrow keys or `W/A/S/D` keys
- Vim keys: `j` (down), `k` (up), `l` (right)

**Hardware:**
- **Clickwheel encoder**: Rotate to move cursor
- **Probe switch**: 
  - `Select` position → Horizontal movement
  - `Measure` position → Vertical movement
- Press `/` to toggle encoder direction (H/V) independently

## Editing Pixels


### Editing Methods

The editor has three draw modes (cycle with `.` key) to pick what happens when you press `enter`/`space`/`encoder click`:

1. **Toggle Mode** (default): Flips pixel state (ON↔OFF)
2. **Set Mode**: Always turns pixels ON (draw)
3. **Clear Mode**: Always turns pixels OFF (erase)

Or just use these keys to do it directly and not worry about the mode:

  - `z` = Set pixel (turn ON)
  - `x` = Clear pixel (turn OFF)
  - `c` = Toggle pixel


## Menu Bar Navigation

When the cursor reaches the bottom edge and you press down, you enter the menu bar:

**Navigation:**
- Left/Right arrows: Move between menu items
- Enter/Space: Activate selected item
- Up: Exit menu bar

**Menu Items:**
- **View**: Cycle display modes (Full/Half/Quarter)
- **Enc**: Toggle encoder direction (H/V)
- **Draw**: Cycle draw modes (Toggle/Set/Clear)
- **«Save»**: Save file and return to editing
- **«Quit»**: Exit editor (prompts if modified)

## Saving and Quitting

- **Ctrl+S**: Quick save
- **Ctrl+Q**: Quit (prompts to save if modified)
- **h or ?**: Show help screen

The editor automatically adds the 4-byte header (width and height) when saving, making the file compatible as a startup image.

## Example Workflow: Creating a Startup Logo

1. Open file manager, navigate to `/images/`
2. Create new file: `mylogo.bin`
3. Editor opens with blank 128×32 canvas
4. Switch to Half Block mode (`m`) for better overview
5. Use clickwheel to navigate, Connect button to draw
6. Save with Ctrl+S
7. Set as startup image: 
    - By editing the config file: ``` `[top_oled] startup_image = /images/mylogo.bin``` 
    - Or use the click menus `OLED` > `Startup message` > `image` > (scroll through all the images and `click` to select)
8. Reboot or enter/exit the click menu to see your custom logo

## Editor Screenshots

Full size view (1:1 pixel mapping):
```jython
                                                                                                                       ███████  
                                                                                              ██████      ███████    ██      ██ 
                                                                     ██████    █████        ███    ██   ██      ██  █         █ 
                                            ██████       ██████  ████     ██  ██   ██      ██       █  █         ███          ██
       █████         ███          ████  ████     ██  ████     █ █          ██ █     █     █          ██           ██           █
      ██   █ ████   █  ██  ███   ██  ███          ███          █            ██      ██   █           ██           █     ██     █
    ██      ██  ██ █    ███  ██  █    █           ███          █            ██      ██  ██          ██     ██     █    ████    █
   ██       █    ██     ██    █  █    █            █           █   █████     █      ██  █         ████    ████    █    ████   ██
   ██       █    ██      █    █  █    █    ████    █          ██    █████    █      ██  █     █████ ██    ████   ██    ████████ 
   ██       █    ██      █    █ ██    █   █████    █     ███████    █████    █      ██  █    ████    █    █████████     █████   
    ██      █    ██      █     ██     █   ██████   █    █████  █    █   ██   █     ███  █    ██      █     ████ ████      ███   
    ██      █    ███     █     ██     █   ██  ██   █    ███    ██   █    █   █     ██   █    ███████ ██     ███    █        ██  
     ██     █    ███     █      █     █   █    █   █    ██     ██    █   █   █     ██   ██   ██    ████       ███  ██        █  
     ██     █    ███     █            █   █    █   █    ██████ ██    █   █   █     ██   ██          █ ██        ██  ███      ██ 
     ██     █    ████    █            █   █    █   █    ██   ████    █  ██   █     ██   ██          █  ███       █   ████     ██
      █     █    ████    █            █    █  ██   █          █ █    ████   ███    █    ██         ██    ████    ██   ████     █
      █     ██    ███    █            █    ████    █          █ ██   ███    ███    █     █     █████      ████    █ ███████    █
      ██     █    ███    █        █   █    ███     █         ██ ██         ████    █     █    ████         ███    ███  ████    █
       █     █    ███    ██   █   █   ██          ██      ████  ██        ███ █    █     █    ███████  ███████    ██    ██     █
       █     █    ███    ██   █  ██   ██          ██     ███     █        ██  █    █  ████    ████  ████   ██     █            █
 ████  █     █     █     ██   ██ ██    █         ████    ██      █   ██    ██ █    ████  ██    ██    ██           █           ██
██  ██ █     ██          ██   █████    █    ██████ ██    ███████ █   ███    ███    ██     █          ██           █           █ 
█    ███     ██         ███    ████    █    █████  ██     ██   ███    ██     ██           █          ██          ███         ██ 
█     █      ██         ███    █ ██    █     ██    ██           ██    ███     █           █         ████         ████       ██  
█           ████        █ █    █  █    █     █     ██           ██    ███     ██         ███      ███████       ██ ██████████   
█           █ ██       ██ █    █  █    █     █      ██         ████   ████   ████      ██████████████ ███████████   █████████   
█          ██  ██      ██ █    █  ██  ███   ██      ███     ███████████ ██████████████████ ████████    █████████     ███████    
██         ██  ███    ██  ██  ██  ████████████       ███████████  █████  █████  █████████   ██████       ██████                 
 ██       ██    ████████  ██████  █████ █████        █████████     ███    ███    ██████                                         
 ███     ███     ██████    ████    ███   ███          █████                                                                     
  █████████       ████      ██                                                                                                  
   ███████                                                                                                                      
 /images/bubbleJump.bin   |   128x32   |   (64,16)   |   Saved                                                         
 View:Full   |   Enc:V   |   Draw:CLR   |   «Save»   |   «Quit»                                                        

⟨Clickwheel > ↺ / ↻: move H/V | Click: toggle pixel ⟩ ⟨ Probe Buttons >  Connect:set | Remove:clear  | Switch > Select:H | Measure:V ⟩
⟨Terminal >     [z]:set [x]:clear [c]:toggle pixel   | [m]:Cycle View | [/]: Enc H/V |  ctrl+S:Save  |    ctrl+Q:Quit    | [?]:Help  ⟩


```

Half Block view (2:1 vertical compression - each character is 2 pixels tall):
```jython
                                                                                              ▄▄▄▄▄▄      ▄▄▄▄▄▄▄    ▄▄▀▀▀▀▀▀█▄ 
                                            ▄▄▄▄▄▄       ▄▄▄▄▄▄  ▄▄▄▄▀▀▀▀▀█▄  ▄█▀▀▀█▄      ▄█▀▀    ▀█  ▄▀▀      ▀█▄▄▀         █▄
      ▄█▀▀▀█ ▄▄▄▄   ▄▀▀█▄  ▄▄▄   ▄█▀▀█▄▄▀▀▀▀     ▀█▄▄▀▀▀▀     ▀▄▀          ▀█▄▀     █▄   ▄▀          ██           █▀    ▄▄     █
   ▄█▀      █▀  ▀█▄▀    ██▀  ▀█  █    █           ▀█▀          █   ▄▄▄▄▄    ▀█      ██  █▀        ▄▄██    ▄██▄    █    ████   ▄█
   ██       █    ██      █    █ ▄█    █   ▄████    █     ▄▄▄▄▄██    █████    █      ██  █    ▄███▀▀ ▀█    ████▄▄▄██    ▀█████▀▀ 
    ██      █    ██▄     █     ██     █   ██▀▀██   █    ███▀▀  █▄   █   ▀█   █     ██▀  █    ██▄▄▄▄▄ █▄    ▀███ ▀▀▀█      ▀▀█▄  
     ██     █    ███     █      ▀     █   █    █   █    ██▄▄▄▄ ██    █   █   █     ██   ██   ▀▀    ▀█▀█▄      ▀▀█▄ ▀█▄▄      █▄ 
     ▀█     █    ████    █            █   ▀▄  ▄█   █    ▀▀   ▀█▀█    █▄▄█▀  ▄█▄    █▀   ██         ▄█  ▀▀█▄▄▄    █▄  ▀███▄    ▀█
      █▄    ▀█    ███    █        ▄   █    ███▀    █         ▄█ ▄█   ▀▀▀   ▄███    █     █    ▄███▀▀      ▀███    █▄█▀▀████    █
       █     █    ███    ██   █  ▄█   ██          ██     ▄██▀▀  ▀█        ██▀ █    █  ▄▄▄█    ████▀▀█▄▄█▀▀▀██▀    █▀    ▀▀     █
▄█▀▀█▄ █     █▄    ▀     ██   ██▄██    █    ▄▄▄▄▄█▀██    ██▄▄▄▄▄ █   ██▄   ▀█▄█    ██▀▀  ▀█    ▀▀    ██           █           █▀
█    ▀█▀     ██         ███    █▀██    █    ▀██▀▀  ██     ▀▀   ▀██    ██▄    ▀█           █         ▄██▄         ███▄       ▄█▀ 
█           █▀██       ▄█ █    █  █    █     █     ▀█▄         ▄██▄   ███▄   ▄██▄      ▄▄███▄▄▄▄▄▄███▀███▄▄▄▄▄▄▄█▀ ▀█████████   
█▄         ██  ██▄    ▄█▀ █▄  ▄█  ██▄▄███▄▄▄██      ▀██▄▄▄▄▄████▀▀█████ ▀█████▀▀█████████▀ ▀██████▀    ▀▀██████▀     ▀▀▀▀▀▀▀    
 ██▄     ▄██    ▀██████▀  ▀████▀  ▀███▀ ▀███▀        ▀█████▀▀▀     ▀▀▀    ▀▀▀    ▀▀▀▀▀▀                                         
  ▀███████▀       ▀▀▀▀      ▀▀                                                                                                  
 /images/bubbleJump.bin   |   128x32   |   (64,16)   |   Saved                                                         
 View:Half   |   Enc:V   |   Draw:CLR   |   «Save»   |   «Quit»                                                        

⟨Clickwheel > ↺ / ↻: move H/V | Click: toggle pixel ⟩ ⟨ Probe Buttons >  Connect:set | Remove:clear  | Switch > Select:H | Measure:V ⟩
⟨Terminal >     [z]:set [x]:clear [c]:toggle pixel   | [m]:Cycle View | [/]: Enc H/V |  ctrl+S:Save  |    ctrl+Q:Quit    | [?]:Help  ⟩


```

Quarter Block view (2×2 compression - each character is 4 pixels):
```jython
                                               ▄▄▄   ▄▄▄▖ ▗▞▀▀▜▖
                      ▄▄▄   ▗▄▄▖▗▄▞▀▀▙ ▟▀▜▖  ▗▛▘ ▝▌▗▀   ▜▄▘    ▙
   ▟▀▜▗▄▖ ▞▜▖▗▄ ▗▛▜▄▀▀  ▝▙▞▀▘  ▚▘    ▝▙▘  ▙ ▗▘    ▐▌     ▛  ▄  ▐
 ▗▛   ▛ ▜▞  █▘▝▌▐  ▌     ▜▘    ▐ ▗▄▄  ▜   █ ▛    ▄█  ▟▙  ▌ ▐█▌ ▟
 ▐▌   ▌ ▐▌  ▐  ▌▟  ▌ ▟█▌ ▐  ▗▄▄█  ██▌ ▐   █ ▌ ▗█▛▘▜  ██▄▟▌ ▝██▛▘
  █   ▌ ▐▙  ▐  ▐▌  ▌ █▀█ ▐  █▛▘▐▖ ▌ ▜ ▐  ▐▛ ▌ ▐▙▄▄▐▖ ▝█▌▀▜   ▀▙ 
  ▐▌  ▌ ▐█  ▐   ▘  ▌ ▌ ▐ ▐  █▄▄▐▌ ▐ ▐ ▐  ▐▌ █ ▝▘ ▝▛▙   ▀▙▝▙▖  ▐▖
  ▝▌  ▌ ▐█▌ ▐      ▌ ▚ ▟ ▐  ▀ ▝▛▌ ▐▄▛ ▟▖ ▐▘ █    ▗▌▝▜▄▖ ▐▖▝█▙  ▜
   ▙  ▜  █▌ ▐    ▖ ▌ ▐█▘ ▐    ▗▌▟ ▝▀ ▗█▌ ▐  ▐  ▟█▀   ▜█  ▙▛▜█▌ ▐
   ▐  ▐  █▌ ▐▌ ▌▗▌ █     █  ▗█▀ ▜    █▘▌ ▐ ▄▟  ██▀▙▟▀▜▛  ▛  ▀  ▐
▟▀▙▐  ▐▖ ▝  ▐▌ █▟▌ ▐  ▄▄▟▜▌ ▐▙▄▄▐ ▐▙ ▝▙▌ ▐▛▘▝▌ ▝▘ ▐▌     ▌     ▛
▌ ▝▛  ▐▌    █▌ ▐▜▌ ▐  ▜▛▘▐▌  ▀ ▝█  █▖ ▝▌     ▌    ▟▙    ▐█▖   ▟▘
▌     ▛█   ▗▌▌ ▐ ▌ ▐  ▐  ▝▙    ▗█▖ █▙ ▗█▖  ▗▟█▄▄▄█▛█▙▄▄▄▛▝████▌ 
▙    ▐▌▐▙  ▟▘▙ ▟ █▄█▙▄█   ▜▙▄▄██▀██▌▜██▀████▛▝███▘ ▝▜██▛  ▝▀▀▀  
▐▙  ▗█  ▜██▛ ▜█▛ ▜█▘▜█▘   ▝██▛▀  ▝▀  ▀▘ ▝▀▀▘                    
 ▜███▘   ▀▀   ▀                                                 
 /images/bubbleJump.bin   |   128x32   |   (64,16)   |   Saved                                                         
 View:Qtr   |   Enc:V   |   Draw:CLR   |   «Save»   |   «Quit»                                                         

⟨Clickwheel > ↺ / ↻: move H/V | Click: toggle pixel ⟩ ⟨ Probe Buttons >  Connect:set | Remove:clear  | Switch > Select:H | Measure:V ⟩
⟨Terminal >     [z]:set [x]:clear [c]:toggle pixel   | [m]:Cycle View | [/]: Enc H/V |  ctrl+S:Save  |    ctrl+Q:Quit    | [?]:Help  ⟩

```

The output of `?`
```jython
=== Bitmap Editor Help ===

Navigation:
  Encoder wheel       - Move cursor (H or V mode)
  Arrow keys / WASD   - Move cursor
  j/k/l (vim)         - Move cursor
  Down at bottom edge - Enter menu bar

Editing:
  Encoder click       - Apply current draw mode at cursor
  Enter / Space       - Apply current draw mode at cursor
  Connect button HOLD - Set pixels while held (draw lines)
  Remove button HOLD  - Clear pixels while held (erase lines)

Direct Pixel Actions (keyboard):
  z                   - Set pixel at cursor (draw)
  x                   - Clear pixel at cursor (erase)
  c                   - Toggle pixel at cursor

Draw Mode Control:
  .                   - Cycle draw modes (Toggle/Set/Clear)

Hardware Controls:
  Probe switch SELECT - Encoder horizontal movement
  Probe switch MEASURE- Encoder vertical movement

Display:
  m                   - Cycle view mode (Full/Half/Quarter)
  /                   - Toggle encoder H/V movement

Menu Bar (Down at bottom edge):
  Left/Right arrows   - Navigate menu items
  Enter / Space       - Activate menu item (cycle/Save/Quit)
  Up / Escape         - Exit menu bar

Menu Bar Items:
  View      - Cycle display mode (Full/Half/Quarter)
  Enc       - Toggle encoder direction (H/V)
  Draw      - Cycle draw mode (Toggle/Set/Clear)
  «Save»    - [Button] Save file and exit menu
  «Quit»    - [Button] Quit editor (prompts if modified)

File:
  Ctrl+S              - Save file
  Ctrl+Q / ESC        - Quit (prompts if modified)
  h / ?               - Show this help

Cursor Colors:
  Green background - Pixel is OFF
  Red background   - Pixel is ON
  ```



## Bitmap File Format

The editor works with `.bin` files in two formats:

**With Header (Recommended):**
- 4 bytes: Width (16-bit little-endian)
- 2 bytes: Height (16-bit little-endian)  
- Remaining: Bitmap data (MSB-first, row-major)
- Example: 128×32 = 4 header + 512 data = 516 bytes total

**Raw Format:**
- Just bitmap data, dimensions inferred from file size
- 512 bytes → 128×32, 1024 bytes → 128×64, etc.

The editor automatically adds headers when saving, making files ready to use as startup images.

## Converting External Images

Want to use your own images? The Jumperless repository includes Python scripts to convert PNG/JPG images to OLED bitmaps:

**Location:** `JumperlOS/scripts/image_to_oled_bitmap.py`

**Usage:**
```bash
python image_to_oled_bitmap.py input.png output.bin --width 128 --height 32
```

The script will:
1. Resize your image to fit the OLED dimensions
2. Convert to 1-bit (black/white) format
3. Save with proper header format
4. Output is ready to use as a startup image or edit in the bitmap editor

Then you can mount your Jumperless's filesystem as a mass storage device with `U` and drop it into the `/images/` folder. 
