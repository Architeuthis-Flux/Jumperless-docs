# Parts

Your Jumperless can know what's plugged into it. Tell it a chip, module, or passive is on the board and it becomes a `part`: its pins get labeled, its power gets wired for you, tapping a pin tells you what it is, and if something's wired dangerously wrong the board warns you. If the part is a little OLED, the Jumperless will even drive it.

The whole idea is that the board *informs* you - it never takes over. You still wire your own circuit with the probe like always; parts just make the board smarter about what's on it.

## Placing a Part

Click into the menu and pick `Parts`. You'll get a class picker on the breadboard LEDs:

- `Logic` - 7400 / 4000 series ICs
- `Analog` - 555s, op-amps, regulators
- `Discrete` - resistors, caps, LEDs, diodes
- `Transistors` - BJTs and MOSFETs
- `Displays` - OLED panels and friends
- `Modules` - BME280, MPU6050, and other breakout boards
- `Clear parts` - shows up whenever you have parts placed

Scroll with the clickwheel, click to pick a class, then pick your part the same way.

### DIP chips: tap pin 1

A DIP package straddles the center line, so it only fits one way. Tap the row where **pin 1** is (or type the row number in a terminal and hit enter). Done - the rest of the pins are wherever physics says they are.

### Everything else: tap each signal

Modules and SIP-header parts have **no standard pin order** - one vendor's OLED is `GND VCC SCL SDA`, the next one's is `VCC GND SCL SDA`. So instead of guessing, the Jumperless asks you to tap each signal by name: the breadboard shows `TAP VCC`, then `TAP GND`, then `TAP SCL`, and so on. Your taps are the truth - the part can be plugged in any orientation, or even spread across fly wires (any rows in the same half of the board work).

Every tap you land flashes that row green, and the rows you've already tapped stay lit so you can see your progress. Tapped the wrong row? It won't let you tap the same row twice for one part, and clicking the wheel backs you out to try again.

Two-legged passives (resistors, LEDs, diodes) get both ends tapped - one hole on the top half, the matching hole on the bottom half. For polarized parts, whichever signal you tap is where that signal *is*, so the anode/cathode labels always match reality.

## Power is wired for you

When a part is placed, its power pins get routed automatically: `VCC`-class pins connect to the rail on their half of the board, `GND`-class pins connect to ground. You wire the interesting stuff; the boring stuff is done.

The rails still obey **you** - nothing is hot until you turn a rail on, and the voltage is whatever you set. (Also worth knowing: most I2C modules are happiest with rails at `3.3V`.)

If you tap a power pin onto a row that's already connected to the *opposite* thing (say, VCC onto a grounded row), the Jumperless refuses to make that bridge and warns you instead - it will never short a rail to ground on your behalf.

## Living with placed parts

**Labels bloom, then hide.** Right after you place a part, its pins light up along the board edge in their class colors for a few seconds, then go dark. An idle board stays clean - labels come back when they're relevant (you tap the part, its net gets highlighted, or a warning is active).

**Tap a pin to ask about it.** With the probe switch on `Select`, tap any row a part lives on and the OLED shows the part name, the pin's label, and its class - `NE555 pin 3 OUT`, that kind of thing.

**Readouts speak your labels.** Highlight a net that lands on a part pin and the OLED says `SSD1306 SDA` instead of `Net 12`. Highlight a GPIO that's genuinely configured as I2C (checked against the actual RP2350 pin function register, not guessed) and it says `GPIO 7 SDA`.

**Warnings show, never block.** If a part's power pin ends up on a grounded net, or its ground pin on a hot rail, the part's pins light up in warning colors and the OLED tells you why (`VCC_TO_GND!`). That's it - the board never refuses your wiring, it just makes sure you know.

**Clearing.** `Parts` > `Clear parts` removes every part (it asks first - confirm with the probe's `Connect` button). Clearing the whole board clears its parts too. Parts are saved with your slot, so they come back after a reboot.

## Breadboard Displays

*(Jumperless V5 only)*

Place a small I2C OLED (the 0.91" 128x32 SSD1306 is the well-tested one) through `Parts` > `Displays`, tapping each of its pins as prompted. Then:

1. The Jumperless routes the display's `SDA`/`SCL` to two of its own GPIOs through the crossbar - you never wire data lines.
2. Power rides the rails you already wired during placement - turn a rail on (3.3V is the happy voltage).
3. The moment the panel powers up, the board finds it and the boot animation starts playing on it, ambient - it keeps running while you use menus, probe around, and measure things.

The serial monitor narrates the lifecycle: `DISPLAY routed`, then `DISPLAY alive` when the panel answers. If you steal its GPIOs from a MicroPython script the display politely pauses (`DISPLAY paused`) and resumes when you release them.

## Terminal twins

Everything above works over serial too: the part pickers echo what they're showing, any "tap a row" prompt accepts a typed row number + enter, and placements print machine-readable lines (`PARTDB place ok=NE555 row=42`, `PARTPICK sig=SDA row=8`, `PARTPIN`/`PARTWARN` for inspects and warnings) so scripts and tools can follow along.
