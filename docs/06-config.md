# Config File

To change any persistent settings, there's a `config` file. You can read it with `~` and edit settings by copying any of those lines, pasting it back, and changing the value to whatever you want it to be.

## Viewing Configuration

```
~

copy / edit / paste any of these lines 
into the main menu to change a setting

Jumperless Config:


`[hardware] generation = 5;
`[hardware] revision = 5;
`[hardware] probe_revision = 5;

`[dacs] top_rail = 0.00;
`[dacs] bottom_rail = 0.00;
`[dacs] dac_0 = 3.33;
`[dacs] dac_1 = 0.00;
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

`[routing] stack_paths = 1;
`[routing] stack_rails = 2;
`[routing] stack_dacs = 0;
`[routing] rail_priority = 1;

`[calibration] top_rail_zero = 1634;
`[calibration] top_rail_spread = 20.60;
`[calibration] bottom_rail_zero = 1614;
`[calibration] bottom_rail_spread = 20.73;
`[calibration] dac_0_zero = 1635;
`[calibration] dac_0_spread = 20.53;
`[calibration] dac_1_zero = 1625;
`[calibration] dac_1_spread = 20.80;
`[calibration] probe_max = 4060;
`[calibration] probe_min = 19;

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

`[gpio] direction = 0,1,1,1,1,1,1,1,0,1;
`[gpio] pulls = 0,0,0,0,0,0,0,0,2,2;
`[gpio] uart_tx_function = off;
`[gpio] uart_rx_function = passthrough;

`[serial_1] function = passthrough;
`[serial_1] baud_rate = 115200;
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
`[top_oled] gpio_sda = MCP_2;
`[top_oled] gpio_scl = MCP_3;
`[top_oled] sda_row = D2;
`[top_oled] scl_row = D3;
`[top_oled] connect_on_boot = false;
`[top_oled] lock_connection = false;

```

## Configuration Help

There's also a `help` you can get to by entering `~?`
```
         ~ = show current config
~[section] = show specific section (e.g. ~[routing])
         ` = enter config settings
        ~? = show this help

    `reset = reset to defaults   //editor's note: this doesn't clear the calibration or hardware version, to clear that, you can use `reset_all `reset_calib `reset_hardware
    ~names = show names for settings
  ~numbers = show numbers for settings

    config setting format (prefix with ` to paste from main menu)

`[serial_1]connect_on_boot = true;

``` 