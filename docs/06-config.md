# Config File

To change any persistent settings, there's a `config` file. You can read it with `~` and edit settings by copying any of those lines, pasting it back, and changing the value to whatever you want it to be.

## Viewing Configuration

```c++
~

copy / edit / paste any of these lines 
into the main menu to change a setting

Jumperless Config:


`[config] firmware_version = 5.2.2.0;

`[hardware] generation = 5;
`[hardware] revision = 5;
`[hardware] probe_revision = 5;

`[dacs] top_rail = 3.50;
`[dacs] bottom_rail = 3.50;
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