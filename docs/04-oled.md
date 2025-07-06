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