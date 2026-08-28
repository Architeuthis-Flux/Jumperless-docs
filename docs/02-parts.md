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
- `Remove parts` - take parts off the board (leg by leg, or whole)

(There's also [`Auto Scan`](#auto-scan), where the board figures out what's plugged in by itself.)

Scroll with the clickwheel, click to pick a class, then pick your part the same way.

### DIP chips: tap pin 1

A DIP package straddles the center line, so it only fits one way. Tap the row where **pin 1** is (or type the row number in a terminal and hit enter). Done - the rest of the pins are wherever physics says they are.

### Everything else: tap each signal

Modules and SIP-header parts have **no standard pin order** - one vendor's OLED is `GND VCC SCL SDA`, the next one's is `VCC GND SCL SDA`. So instead of guessing, the Jumperless asks you to tap each signal by name: the breadboard shows `TAP VCC`, then `TAP GND`, then `TAP SCL`, and so on. Your taps are the truth - the part can be plugged in any orientation, or even spread across fly wires (any rows in the same half of the board work).

Every tap you land flashes that row green, and the rows you've already tapped stay lit so you can see your progress. Tapped the wrong row? It won't let you tap the same row twice for one part, and clicking the wheel backs you out to try again.

Two-legged passives (resistors, LEDs, diodes) get both ends tapped - one hole on the top half, the matching hole on the bottom half. For polarized parts, whichever signal you tap is where that signal *is*, so the anode/cathode labels always match reality.

## Auto Scan

Or skip all that: `Parts` > `Auto Scan` sweeps the board, measures whatever conducts, names what it can prove, and asks - one find at a time - whether to add it as a placed part. It starts by **lifting your wiring** so every row is measurable; finished, aborted, or refused, every wire goes back exactly as it was. Any press stops it - probe button, wheel, or any key.

The board itself shows the work: the census cursor drags a rainbow down the rows, anything that conducts stays lit green, empties go dark. A second pass sweeps *pairs* of rows to catch parts a single-row poke can't see (a lone transistor conducts between its legs, not to ground). The OLED narrates the phase; the terminal gets the full play-by-play.

![The board mid-scan: everything that conducts is lit green](assets/autoscan-hits.png)

![OLED: scanning the board](assets/autoscan-oled-scanning.png)

Then each cluster of hits gets interrogated with the same measurement machinery `Test Part` uses - real characterization, not just continuity, so this part takes a minute or two:

```jython
PARTSCAN spans=6
  interrogating rows 3-6...
  rows 3-6: 4 legs (a chip?)
  row 10: noise (nothing conducts)
  rows 44-46: BJT_PNP 0.59V
  walking everything that shares row 58...
  rows 57,55,54,52,28,27,23,22 all light from row 58 - a 7-seg display? (common anode)
PARTSCAN auto done in 123s - 2 placeable (CONNECT adds them to the board)
```

- **Two-lead parts** come back typed and measured - `RESISTOR 10.0kΩ`, `LED 1.85V` - anode painted **red**, cathode **blue**.
- **Transistors** get their pinout (emitter **red**, base **amber**, collector **blue**) and the measured junction drop. Something that *acts* like a transistor with an impossible junction voltage gets called a chip's pins instead - a TTL input fakes transistor action, but it can't fake physics.
- **Chips** are reported as presence - `4 legs (a chip?)` - never a guessed part number. But the scan reads their clamp diodes to find the power pins, quietly powers them, and knocks on the I2C bus: a module that answers is named by address (an SSD1306 shows up as `I2C 0x3C module`) and *is* placeable.
- **LED displays** are caught through their common pin: rows that all light from one shared row become `a 7-seg display?` - and it offers to wire it (below).
- **Noise is dismissed** after a real interrogation, and parts you've already placed are recognized (`7SEG52 (placed)`) and left alone.

![The verdict: a chip's span, a PNP in E/B/C colors, and a 7-seg with its common](assets/autoscan-verdict.png)

**Saying yes.** Findings are offered one at a time: `Connect` (or `y`) adds, click (or `n`) skips, hold the wheel to finish early. An added part is a real placed part - labels, tap-to-ask, saved with your slot - and its labels bloom right after the scan:

![OLED: add BJT_PNP rows 44-46?](assets/autoscan-oled-confirm.png)

![New parts' labels blooming after the scan](assets/autoscan-bloom.gif)

**A display wires itself.** If the scan found an LED display, the last question is `wire? 8-seg display (common 58) to GPIOs`. Say yes and every segment gets its own GPIO through the crossbar, the common goes to the rail matching its polarity, and the nets are named `7SEG52_S1`-`S8` - drive it from MicroPython without ever touching a wire.

![OLED: wire the display to GPIOs?](assets/autoscan-oled-wire.png)

**When it refuses:** a board that reads powered (`board reads powered - scan can't see parts`), a span that reads powered (`not a part`), or no free ADC lane to measure with (`no clean ADC lane`) each stop the scan honestly rather than clustering phantoms out of your supply rail.

## Power is wired for you

When a part is placed, its power pins get routed automatically: `VCC`-class pins connect to the rail on their half of the board, `GND`-class pins connect to ground. You wire the interesting stuff; the boring stuff is done.

The rails still obey **you** - nothing is hot until you turn a rail on, and the voltage is whatever you set. (Also worth knowing: most I2C modules are happiest with rails at `3.3V`.)

If you tap a power pin onto a row that's already connected to the *opposite* thing (say, VCC onto a grounded row), the Jumperless refuses to make that bridge and warns you instead - it will never short a rail to ground on your behalf.

## Living with placed parts

**Labels bloom, then hide.** Right after you place a part, its pins light up along the board edge in their class colors for a few seconds, then go dark. An idle board stays clean - labels come back when they're relevant (you tap the part, its net gets highlighted, or a warning is active).

**Tap a pin to ask about it.** With the probe switch on `Select`, tap any row a part lives on and the OLED shows the part name, the pin's label, and its class - `NE555 pin 3 OUT`, that kind of thing.

**Readouts speak your labels.** Highlight a net that lands on a part pin and the OLED says `SSD1306 SDA` instead of `Net 12`. Highlight a GPIO that's genuinely configured as I2C (checked against the actual RP2350 pin function register, not guessed) and it says `GPIO 7 SDA`.

**Warnings show, never block.** If a part's power pin ends up on a grounded net, or its ground pin on a hot rail, the part's pins light up in warning colors and the OLED tells you why (`VCC_TO_GND!`). That's it - the board never refuses your wiring, it just makes sure you know.

**Removing.** `Parts` > `Remove parts` splits the work between the control surfaces, the way you'd expect. The probe does the precise work: tap a leg of a placed part and just that leg is removed - its bridge, its net name, its entry in the part - and removing the last leg removes the part itself. The wheel does the coarse work: scroll through your placed parts (each one highlights on the board with its card on the panel) and a click removes the whole highlighted part. The scroll's last stop is `All`, which clears every part (it asks first - confirm with the probe's `Connect` button). Clearing the whole board (`x`) clears its parts too. Parts are saved with your slot, so they come back after a reboot.

## Breadboard Displays

*(Jumperless V5 only)*

Place a small I2C OLED (the 0.91" 128x32 SSD1306 is the well-tested one) through `Parts` > `Displays`, tapping each of its pins as prompted. Then:

1. The Jumperless routes the display's `SDA`/`SCL` to two of its own GPIOs through the crossbar - you never wire data lines.
2. Power rides the rails you already wired during placement - turn a rail on (3.3V is the happy voltage).
3. The moment the panel powers up, the board finds it and the boot animation starts playing on it, ambient - it keeps running while you use menus, probe around, and measure things.

The serial monitor narrates the lifecycle: `DISPLAY routed`, then `DISPLAY alive` when the panel answers. If you steal its GPIOs from a MicroPython script the display politely pauses (`DISPLAY paused`) and resumes when you release them.

## Terminal twins

Everything above works over serial too: the part pickers echo what they're showing, any "tap a row" prompt accepts a typed row number + enter, and placements print machine-readable lines (`PARTDB place ok=NE555 row=42`, `PARTPICK sig=SDA row=8`, `PARTPIN`/`PARTWARN` for inspects and warnings) so scripts and tools can follow along.
