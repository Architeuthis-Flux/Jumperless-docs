# Basic Controls

![guide-42](https://github.com/user-attachments/assets/e35c42e0-b23a-4203-a836-44f0991db7fc)

----

## The Probe
First, keep the switch on the probe set to `Select`
![ProbeSelect](https://github.com/user-attachments/assets/1155f75a-f800-4bc0-ba6d-49e603ad39e2)

**Why Select mode?** `Measure` mode allows the probe tip to be ±9V tolerant and routable like any other node, but as of yet, the code to actually do anything with it is unwritten so it just connects to DAC 0 and outputs 3.3V just like it was in `Select` mode. But the DAC is much worse at matching the RP2350B's idea of what 3.3V is *exactly*, so probing will be flaky and may be off from the rows you're tapping in `Measure`.

## Connecting Rows

Click the `Connect` button on the probe
![connectButton](https://github.com/user-attachments/assets/faedd0af-8ea6-4454-8f33-01ff478bb9e7)

The logo should turn blue and the LEDs on the probe should also change
![connect](https://github.com/user-attachments/assets/2040417f-64c3-41dd-a3d6-8c900e15445b)

Now any pair of nodes you tap should get connected as you make them. In connect mode, you're creating `bridges` (see the [glossary](99-glossary.md)), so connections are made in pairs. When you've tapped the first `node` in a pair, the `logo` and `Connect` text on the probe will brighten to show that you're "`holding`" a connection, and the next thing you tap will connect to that first `node`. 

If you make a mistake while `holding` a connection, click the `Connect` button and it will clear it and take you back to the first `node`. 
If you click the `Connect` button while you're not `holding` a `node`, it will leave `probe mode` and bring you back into `idle mode` (rainbowy `logo`, all 3 `probe LED`s on.)


To get out of `Connect` mode, press the button again.

### Encoder Connections

You can also make connections using just the clickwheel, without needing to touch the probe to the breadboard:

**To activate:**
- Navigate to: `Click` > `Connect` > `Add` (or `Remove`)  
- OR just turn the clickwheel while already in probe mode

**How it works:**
1. Turn the clickwheel to scroll through all available nodes:
   - Breadboard rows (1-60)
   - Nano header pins (D0-A7)
   - Rails (Top, Bottom, GND)
   - DAC (0, 1) 
   - ADC (0-4, Probe)
   - GPIO (1-8)
   - UART (TX, RX)
   - Current sense (I+, I-)

2. Click the encoder button to select the highlighted node
3. Hold the encoder button to exit

The cursor will automatically hide after 5 seconds of inactivity. This is especially useful when you need precise control or want to access special functions without tapping pads.

## Removing Rows

Click the `Remove` button
![removeButton](https://github.com/user-attachments/assets/7fc020b7-f5ce-48f6-99eb-4e9a753a0329)

and the logo should turn reddish
![remove](https://github.com/user-attachments/assets/297e169f-f9f5-4151-8fa2-de41ab14492f)

Now you can swipe along the `pad`s or tap them one at a time. Remember it only disconnects that `node` and anything connected to it directly, not *everything* on the `net`. So tapping say, `row 25` that's connected to `GND` won't clear everything connected to `GND`, but tapping the `-` on the rails (for `GND`) would.

The special functions work the same way, tap the pad, pick one, and it will remove it. Click the button again to get out.

## Probe Notes

**Remember the probe is read by a resistive voltage divider**, so putting your fingers on the pads (or the back sides of the 4 risers that connect those `probe sense` boards to the main board), or anything causing the probe tip not to be at a steady 3.3V will give you weird readings. 

If you can't seem to stop playing with the switch on the probe, run the app `probe calib` and tap around on the board while turning the clickweel until the place you tapped is always spot on (do this with the switch in both modes), and hold the clickwheel button to save. This adjusts the nominal 3.3V `measure` mode puts out should be fairly accurate enough for probing.


## The Click Wheel

![wheel copy](https://github.com/user-attachments/assets/d69a5425-7131-46e3-8c17-a38819edfc16)

There are two kinds of presses, `click` (short press) and `hold` (long press). In general, a `click` (short) is a `yes`, and a `hold` (long) is a `no`/`back`/`exit`/`whatever`. 

When I say `click`, it's more of a diagonal slide toward the center of the board ([these encoders](https://lcsc.com/product-detail/Rotary-Encoders_Mitsumi-Electric-SIQ-02FVS3_C2925423.html) were meant to poke out just a little bit from the side of a tablet or whatever.)

To get to the menu, `click` the button and scroll through the menus, `click` will bring you into that menu, `hold` will take you back one level. If you have trouble reading stuff on the breadboard LEDs, everything is copied to the Serial terminal and the OLED (talked about in [OLED Section](04-oled.md)), and adjusting the brightness may help; in the menus, it's `Display Options` > `Bright` > `Menu` and then scroll around until you find a level you like, then `click` to confirm. 



## Special Functions

To connect to `special functions`, tap the corresponding `pad` near the logo, it will show you a menu on the breadboard and terminal to choose them.

![gpioTapped](https://github.com/user-attachments/assets/0b0c45ff-b98e-4a45-87b3-d3cc5c7a4544)


You can think of `special functions` just like any other `node`, the only difference is they're in a sort of "folder" so I didn't need to put a dedicated pad for each of them. 

```jython
DAC Pad
 └─ 0 1 [Tap pads below selection]¹
  └─ -8V  !:.:!  +8V [Tap bottom pads or use clickwheel to select a voltage] > [click probe Connect button to confirm]²
   └─ [Tap a row to connect it to] (or if you were already "holding" a node, it'll connect there)³
```

![This is what prints in the terminal](https://github.com/user-attachments/assets/fc9be8f8-f99c-48cd-8e00-07fdcb426f99)

(This is an ASCII version of what will show on the breadboard LEDs)
¹![You can press R in the main menu to toggle this view](https://github.com/user-attachments/assets/856525f4-425e-4442-9597-8e5b4f72a2c8)

²![You can press R in the main menu to toggle this view](https://github.com/user-attachments/assets/06804d5e-2b10-45ef-ae55-4a49c2f14033)


³![You can press R in the main menu to toggle this view](https://github.com/user-attachments/assets/32c3b184-45d6-476e-b0e9-19a294b2ae3f)




```jython
GPIO Pad
 └─ ⁱ1⁰ ⁱ2⁰ ⁱ3⁰ ⁱ4⁰ 
    ₁5₀ ₁6₀ ₁7₀ ₁8₀ [Tap pads to choose which `GPIO` (left side for input, right side for output)]
     └─ [Tap a row to connect it to] (or if you were already "holding" a node, it'll connect there)
```

¹![You can press R in the main menu to toggle this view](https://github.com/user-attachments/assets/33018aec-be8a-4bc0-b309-baeddad4db66)


The 4 `user pads` will be remappable in the future, but for now, `top_guy` is `routable UART Tx` and `bottom_guy` is `routable UART Rx`, and `buiding` pads are `Current sense` + and -.

The **building pads** have multiple functions:
- In `idle mode`: Override colors for net highlighting (see [Idle Mode Interactions](#idle-mode-net-highlighting))
- In `connect`/`remove` mode: Access **Current Sense (I+/I-)** with marching ants visualization!

![userPads](https://github.com/user-attachments/assets/6925e9ed-fb6b-46a2-b377-205107df6a78)

### Current Sensing with Marching Ants

When you tap either building pad in connect or remove mode, you'll get access to the current sense inputs (I+ and I-). When both I+ and I- are connected to different nets in your circuit:

1. A virtual wire appears between the closest breadboard nodes on each net
2. Animated "marching ants" flow along this wire showing current direction
3. The animation automatically picks the optimal breadboard positions for visualization

This gives you real-time visual feedback of where current is flowing in your circuit!

**Important:** I+ and I- are shorted together internally through a 2Ω shunt resistor. Connect them in series with your circuit, not across it!

---

## Idle Mode Net Highlighting

The main thing is that there's a lot more interaction that can be done outside of any particular mode (like not probing and the logo is rainbowy, I'm gonna call this idle mode here until I think of a good name)
![idle](https://github.com/user-attachments/assets/304d787a-c5f5-4da0-bd95-1a82bcdf83c1)

Here's what's new (all of this is in idle mode):

### Basic Interactions

- **Tapping nets highlights them** as before, but there's a slightly different animation on the `row` you have selected from the whole `net`
- **The click wheel scrolls through highlighting `rows`** as if you tapped each one



### Row Selection Actions

With a `row` selected, here's what you can do:

<!---
### Rail Voltage Adjustment

**Rail / DAC voltages change with `slots`** - each slot can have its own power supply configuration!

If the highlighted `row` is a `rail` (top or bottom) or `DAC`, `click` the clickwheel and then scroll the wheel (or use the probe on the bottom row) to adjust the voltage. 

`Click` the wheel to confirm, `hold` to cancel the adjustment.

**Tip:** You can also tap the `DAC` or `rail` pads to highlight them, then click the encoder to adjust the output directly without connecting anything. Short `hold` the clickwheel button to confirm.

--->
#### Connect Button
- `connect` button will bring you into probing mode with the highlighted row already selected and then spit you back out to `idle` mode once you've made a connection to another row, or click `connect` again to exit

#### Remove Button

- `remove` will remove the highlighted `node`

<!---
#### Color Picker
- tapping the `building top` pad with something highlighted will open the `color picker`, (note: the color now follows the `row` instead of the net, so it can keep the colors even if you remove nets below it and they shift, this was soooo difficult until I realized I should do it by `node`). 
  - Also the color assignments are saved to a file for each slot, so they should work after a reboot and when changing `slots`
  - In the `color picker`, short clicking the probe buttons will zoom in and out, long press will confirm. The click wheel is similar, except you toggle `zoom` and `scroll` modes with short presses and long press to confirm
  - Here's a demo on YouTube
  [![Here's a demo on YouTube](https://img.youtube.com/vi/shE6NSFrH5w/3.jpg)](https://www.youtube.com/watch?v=shE6NSFrH5w)
--->
### Measurement Display
- if the highlighted row is a `measurement` (`gpio input` or `adc`) it will print the state to serial and the oled

### Output Toggle
- if the highlighted row is an `output` (`gpio output`, I'll eventually do `dacs` too) clicking the `connect` button will toggle it `high` / `low`. The `remove` button will *just* unhighlight the net (there were some choices here, like make each button assigned to high / low or allow removing them, but this felt like the best way after trying them all). I will eventually add a setting for the toggle repeat rate (set to 500ms now) and a way to set it freewheeling as a clock.




<!-- ## GPIO Selection Shortcuts

- when selecting `gpio` in `probing` mode (tap the bottom of the 3 pads by the `logo`), there are shortcuts for `input` and `output`, the blue line on the left is `input`, red square on the right is `output`. Tapping right in the middle of a number will take you to the written out `input` / `output` on the top and bottom selector.  -->