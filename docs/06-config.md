# Config File

To change any persistent settings that apply to the Jumperless as a whole, there's a `config` file. You can read it with `~` and edit settings by copying any of those lines, pasting it back, and changing the value to whatever you want it to be. 

## Viewing Configuration

```jython
~

copy / edit / paste any of these lines 
into the main menu to change a setting

Jumperless Config:


`[config] firmware_version = 5.4.0.5;

`[hardware] generation = 5;
`[hardware] revision = 5;
`[hardware] probe_revision = 5;

`[dacs] set_dacs_on_boot = false;
`[dacs] set_rails_on_boot = true;
`[dacs] probe_power_dac = 0;
`[dacs] limit_max = 8.00;
`[dacs] limit_min = -8.00;

`[debug] file_parsing = false;
`[debug] net_manager = false;
`[debug] nets_to_chips = false;
`[debug] nets_to_chips_alt = false;
`[debug] leds = false;

`[routing] stack_paths = 2;
`[routing] stack_rails = 3;
`[routing] stack_dacs = 0;
`[routing] rail_priority = 1;

`[calibration] top_rail_zero = 1650;
`[calibration] top_rail_spread = 21.50;
`[calibration] bottom_rail_zero = 1650;
`[calibration] bottom_rail_spread = 21.50;
`[calibration] dac_0_zero = 1650;
`[calibration] dac_0_spread = 21.50;
`[calibration] dac_1_zero = 1650;
`[calibration] dac_1_spread = 21.50;
`[calibration] adc_0_zero = 9.00;
`[calibration] adc_0_spread = 18.28;
`[calibration] adc_1_zero = 9.00;
`[calibration] adc_1_spread = 18.28;
`[calibration] adc_2_zero = 9.00;
`[calibration] adc_2_spread = 18.28;
`[calibration] adc_3_zero = 9.00;
`[calibration] adc_3_spread = 18.28;
`[calibration] adc_4_zero = 0.00;
`[calibration] adc_4_spread = 5.00;
`[calibration] adc_7_zero = 9.00;
`[calibration] adc_7_spread = 18.28;
`[calibration] probe_max = 4060;
`[calibration] probe_min = 12;

`[logo_pads] top_guy = uart_tx;
`[logo_pads] bottom_guy = uart_rx;
`[logo_pads] building_pad_top = off;
`[logo_pads] building_pad_bottom = off;

`[display] lines_wires = wires;
`[display] menu_brightness = -10;
`[display] led_brightness = 10;
`[display] rail_brightness = 55;
`[display] special_net_brightness = 20;
`[display] net_color_mode = rainbow;
`[display] dump_leds = ;
`[display] dump_format = image;

`[gpio] direction = 1,1,1,1,1,1,1,1,0,1;
`[gpio] pulls = 0,0,0,0,0,0,0,0,2,2;
`[gpio] uart_tx_function = uart_tx;
`[gpio] uart_rx_function = uart_rx;

`[serial_1] function = passthrough;
`[serial_1] baud_rate = 115200;
`[serial_1] async_passthrough = true;
`[serial_1] print_passthrough = false;
`[serial_1] connect_on_boot = false;
`[serial_1] lock_connection = false;
`[serial_1] autoconnect_flashing = true;

`[serial_2] function = off;
`[serial_2] baud_rate = 115200;
`[serial_2] print_passthrough = false;
`[serial_2] connect_on_boot = false;
`[serial_2] lock_connection = false;
`[serial_2] autoconnect_flashing = false;

`[top_oled] enabled = false;
`[top_oled] i2c_address = 0x3C;
`[top_oled] width = 128;
`[top_oled] height = 32;
`[top_oled] sda_pin = 26;
`[top_oled] scl_pin = 27;
`[top_oled] gpio_sda = GP_7;
`[top_oled] gpio_scl = GP_8;
`[top_oled] sda_row = D2;
`[top_oled] scl_row = D3;
`[top_oled] connect_on_boot = false;
`[top_oled] lock_connection = false;
`[top_oled] show_in_terminal = false;
`[top_oled] font = jokerman;

END

```



## Configuration Help

There's also a `help` you can get to by entering `~?`

```c++
~?

Help for command: ~



                              Read config 
                          ~ = show current config
                     ~names = show names for settings
                   ~numbers = show numbers for settings
                 ~[section] = show specific section (e.g. ~[routing])


                              Write config 
`[section] setting = value; = enter config settings (pro tip: copy/paste setting from ~ output and just change the value)


                              Reset config
                     `reset = reset to defaults (keeps calibration and hardware version)
            `reset_hardware = reset hardware settings (keeps calibration)
         `reset_calibration = reset calibration settings (keeps hardware version)
                 `reset_all = reset to defaults and clear all settings
         `force_first_start = clears everything to factory settings and runs first startup calibration


                              Help
                         ~? = show this help



``` 


# State File


For things specific to the current `state` of the Jumperless, there's a YAML file that contains all the connections, colors (optional), `rail` / `DAC` voltages, `GPIO` directions and pulls, stuff like that. The idea is this defines a complete setup of a particular circuit that can be switched between in different `slots`. The Jumperless always boots at `Slot 0`, and you can switch to other `slots` with `<` (cycle through them) or selecting one with the `click menu` with `Slots` > `Load` > `0-7` (it will show a preview of each one.) To save a copy of the currently `active slot`; `Slots` > `Save` > `0-7` will save a copy of the `active slot` to another `slot` and also make that target slot the `active`.


```yaml

╭────────────────────────────────────╮
│      Current YAML State (RAM)     │
╰────────────────────────────────────╯

Active Slot: 0
Dirty Flag: NO (saved)

─── YAML Output ───

version: 2
sourceOfTruth: bridges

bridges:
  - {n1: 38, n2: 44, dup: 2}
  - {n1: 21, n2: 28, dup: 2}
  - {n1: 48, n2: 55, dup: 2}
  - {n1: 4, n2: 2, dup: 2}
  - {n1: BUFFER_IN, n2: DAC0, dup: 1}

nets:
  - {num: 4, nodes: [DAC_0, BUF_IN], name: "DAC 0", anim: true}
  - {num: 6, nodes: [38, 44], color: pink}
  - {num: 7, nodes: [21, 28], color: blue}
  - {num: 8, nodes: [48, 55], color: green}
  - {num: 9, nodes: [4, 2], color: amber}

power:
  topRail: 3.30
  bottomRail: 2.50
  dac0: 3.30
  dac1: 0.00

config:
  routing: {stackPaths: 2, stackRails: 3, stackDacs: 0, railPriority: 1}
  gpio:
    direction:    [1,1,1,1,1,1,1,1,1,1]
    pulls:        [0,0,0,0,0,0,0,0,0,0]
    pwmFrequency: [1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00]
    pwmDutyCycle: [0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50,0.50]
    pwmEnabled:   [0,0,0,0,0,0,0,0,0,0]
  uart: {txFunction: 0, rxFunction: 1}
  oled: {connected: false, lockConnection: false}


─── Memory Usage ───
Connections: 5
State RAM: ~58048 bytes


```

### Source of Truth

Because the information in here is *sort of* redundant (the connections could be computed from just the `bridges` or the `nets` section on their own), there's a field called `sourceOfTruth` which is the section that actually gets parsed and then the other section is written with the computed values. (I haven't done much testing on changing this to `nets` so I'd probably just leave it on `bridges` for now.)

There's some weirdness with how colors are applied, since the `source of truth` is the bridges, and the things that actually get colored are the `nets`, it'll take the colors from the `bridges` (if specified) and try to apply them to the `nets`. But since nets always have a single color (to show that they're connected), if you have `bridges` with different colors in the same `net`, it'll just pick one (don't ask me exactly how the logic chooses, idk.) 

If you specify a color to a `net` even with `sourceOfTruth: bridges` it should respect the `net` assignment over the `bridge` assignment.

## Switching Between Saved Circuits (Slots)

The Jumperless has **8 slots** (0-7) where you can save different circuit configurations. Think of them like presets or save files.

**Quick slot cycling:**
- Type `<` in the terminal to cycle to the next slot
- The circuit will instantly change to match the new slot!

**Other slot commands:**
- `l 5` - Load slot 5 specifically
- `Q` - Query which slot is currently active
- `s` - Show a list of all saved slots

When you make connections with the probe, they're automatically saved to whichever slot is currently active. See the [Glossary](99-glossary.md) for more details about slots.
