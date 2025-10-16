# Glossary of Terms

## Basic Concepts

`net` = a group of all the `node`s that are connected together (enter `n` to see the list)

`node` = anything the crossbar array can connect to, which includes everything on the breadboard and Nano header, as well as the internal `special function` `node`s like `routable GPIO`, `ADC`s, `DAC`s

`row` = *kinda* the same thing as `node` but I generally use it to mean stuff on the breadboard (so special function things like `routable GPIO`, `ADC`s, `DAC`s that don't have a set location are excluded)

`rail` = I use this to refer to the 4 horizontal power rails on the top and bottom (`top_rail`, `bottom_rail`, `gnd`), I will never call a vertical `row` a `rail`. (I know they're columns but it's easier to say a lot)

`bridge` = a pair of exactly two `node`s (this is what you're making when you connect stuff with the probe, enter `b` to see the bridge array)

`path` = the set of crossbar connections needed to make a single `bridge`, so it can have multiple `hop`s if it doesn't have a direct connection and needs to make a `bounce` through an intermediate `chip` (enter `c` to see the crossbar array)

## Hardware

`chip` = shorthand for the CH446Qs specifically, lettered A-L. The first 8 (A-H) are considered "breadboard `chips`", and the last 4 (I-L) are considered "special function" chips (enter `c` to see their connections)

`menu` = I generally mean the onboard clickwheel `menu` when I say this (`click` the wheel to enter those and `scroll` around.) Sometimes I mean the `main menu` which is the list of single character command that gets presented over serial.


## Slots and Files

`slot` = one of **10** saved circuit configurations (slots 0-9) that you can switch between. Use `<` to cycle forward through slots, or use the menus to jump to a specific slot. The **active slot** is the one currently loaded and affecting the hardware.

`slot file` = a YAML file on the filesystem that stores a complete circuit configuration including bridges, power settings, and colors. Located at `/slots/slotN.yaml` where N is 0-9. These files are human-readable and can be edited directly!

`active slot` = the currently loaded slot. Only the active slot affects the hardware. Use `Q` command to query which slot is active. When you make connections with the probe, they're saved to the active slot automatically.

## Slot Management Commands

- `<` = cycle to next slot (0→1→2...→7→0)
- `Q` = query which slot is currently active (returns `ACTIVE_SLOT:X`)
- `Y` = print YAML

## YAML Format

Slot files use YAML format with named nodes for readability:

```yaml
bridges:
  - {n1: 1, n2: 10, dup: 2, color: red}
  - {n1: NANO_D5, n2: GPIO_1, dup: 2}

power:
  topRail: 3.30
  bottomRail: 2.50
```

**Named nodes:** `NANO_D0-D13`, `NANO_A0-A7`, `GPIO_1-8`, `TOP_RAIL`, `BOTTOM_RAIL`, `GND`, `DAC0_5V`, `DAC1_5V`, etc.

You can view and edit these files in the [File Manager](08-file-manager.md) or via USB Mass Storage mode (`U` command).

## Wokwi Import

`W` = Import circuit from [Wokwi](https://wokwi.com) simulator

1. Design circuit on wokwi.com
2. Copy `diagram.json` content
3. Type `W` in Jumperless
4. Paste JSON content
5. Circuit is converted and saved to active slot

The parser automatically maps Wokwi breadboard pins, Arduino Nano pins, and logic analyzer channels to Jumperless nodes, and preserves your wire colors from Wokwi!

