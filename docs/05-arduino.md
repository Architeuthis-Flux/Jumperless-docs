# Arduino Stuff

## UART Passthrough

With an Arduino Nano in the header and the UART lines connected, anything on those lines should be passed through to the second serial port that shows up when you plug in your Jumperless. 

(You can also set the config option ``[serial_1] print_passthrough = true;` and have it print on both. Don't worry about the baud rate, the Jumperless senses what the host computer is set to and changes the speed accordingly.

<img width="360" alt="Screenshot 2025-05-19 at 11 07 55 AM" src="https://github.com/user-attachments/assets/2b255e34-0d0a-4e86-b577-d59c9561fa42" />

## Quick Connection Shortcuts

The shortcuts to connect `D0` and `D1` to the Jumperless's UART `Tx` and `Rx` is `A` to connect, and `a` to disconnect.

## Automatic Flashing

It will even sense when Arduino IDE is trying to upload code and twiddle the reset lines to allow you to flash code with just a single USB cable going to your Jumperless.
<img width="1277" alt="Screenshot 2025-05-19 at 11 09 38 AM" src="https://github.com/user-attachments/assets/625ebf79-7308-4abb-a321-f1bf1f713d4f" /> 


## Commands from Routable UART

You can send commands to the Jumperless from your Arduino (or anything connected to the routable UART) by wrapping them in XML-style tags. The tags are stripped out and the command is executed as if you typed it in the main menu.

### Supported Tags

Any of these tags will work (use the same tag for opening and closing):

- `<j>command</j>` - Short and sweet
- `<jumperless>command</jumperless>` - Verbose but clear  
- `<jumperlessCommand>command</jumperlessCommand>` - Maximum clarity

### Examples

**Make connections from Arduino:**
```cpp
Serial1.println("<j>+ 1-2</j>");           // Connect nodes 1 and 2
Serial1.println("<j>+ A0-D13</j>");        // Connect A0 to D13
```

**Clear all connections:**
```cpp
Serial1.println("<jumperless>x</jumperless>");
```

**Enter MicroPython REPL:**
```cpp
Serial1.println("<jumperlessCommand>p</jumperlessCommand>");
```

**Load a netlist file:**
```cpp
Serial1.println("<j>f</j>");
Serial1.println("<j>myfile.net</j>");      // Then send the filename
```

The command executes silently - the tags and command content don't appear in the UART passthrough, so your Arduino sketch won't see them. Perfect for controlling the Jumperless while maintaining normal serial communication.