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

You can set a custom message to display on the OLED at startup (max 32 characters):

```jython
`[top_oled] startup_message = Your Message Here;
```

This message will appear after the Jumperless logo on boot.

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