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
- Starting a UART message (that would normally just be passed through to the second serial port) with `0x02` ([non-printable ASCII code for Start of Text / STX](https://www.ascii-code.com/)) and ending with `0x03` ([End of Text / ETX](https://www.ascii-code.com/)) will cause the Jumperless to interpret that as something that was sent though the menu on the main serial port. So you can send commands to make connections and such while also using serial passthrough.