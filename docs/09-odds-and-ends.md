# Odds and Ends

## Animations

The Jumperless uses LED animations to show the state of different components on the breadboard.

### Rail Animations

If it's a rail, those are animated and should be a continuous slow pulsing toward the top or bottom depending on the rail.

### ADC Animations

`ADCs` are green at 0V, and go through the spectrum to red at +5V, and get whiter hot pink toward +8V. Negative voltages are kinda blue/icy and do that same thing with the "cold" colors towards -8V.

### GPIO Animations

### Input Mode
`GPIO` as inputs are animated with a white pulsing (this might be broken in that FW release, I'm fixing that right now actually, and will just be purple/white) when floating, red for high, green for low

### Output Mode
`GPIO` outputs will be either green or red depending on their state 








## What's that `BUFFER_IN - DAC_0` bridge that's always there?

That gets added to power the `probe LEDs`, it's kinda weird, but to multiplex 3.3V, GND, LED data, 2 buttons, and a +-9V tolerant analog line over the 4 wires on a TRRS cable, the line powering those LEDs is shared.

The `connect`/`measure` switch is a Dual Pole Dual Throw (DPDT) switch. The probe tip needs to be at a steady 3.3V to be read by the `probe sense pads` which is a big resistive divider sensed by a single `ADC`.

When you have it in `select` mode, the probe tip is getting 3.3V from a `GPIO` on the RP2350B driven `high`, and the LEDs get their power from the analog line, which is `ROUTABLE_BUFFER_IN` connected to `DAC 0` set to 3.3V.

When you switch to `measure` mode, those roles get swapped, the LEDs are powered by that `GPIO`, and the probe tip is now `ROUTABLE_BUFFER_IN`. In the current firmware, that just stays at 3.3V so you can *kinda* sense pads in either mode (you may notice the sensing is a lot wonkier, that's because the `DAC` isn't perfectly calibrated to output *exactly* 3.3V.) But in the future, there will be some other stuff you can do in that mode treating it as an analog line (and of course, I'll forget to update this, if it's after like June 2025, double check this is still true.)

### Why am I using one of the precious two DACs and not another GPIO?

The answer is switch position sensing. You may notice there's no obvious way for the Jumperless to know where the switch is set, so I had to get creative on this one. `DAC 0`'s output is hardwired to go through a `current sense` shunt resistor, so when `DAC 0` is powering the `probe LEDs`, they'll be drawing some current I can measure with one of the `INA219`s, and therefore I can be reasonably confident that the switch is in the `select` position.

If you need both `DAC`s, you can just get rid of this connection and the `probe LEDs` won't light up, but other than aesthetics, it really has no effect on functionality. Or you connect `ROUTABLE_BUFFER_IN` to a `GPIO` and set it `high` and just lose the ability to sense where the switch is. 