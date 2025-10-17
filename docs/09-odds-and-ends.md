# Odds and Ends

## What's New in JumperlOS 5.4.0.4

JumperlOS is now a proper operating system with a priority-based task scheduler! This is a huge refactor from the original firmware:

- **Priority-based task scheduler** - Each component has a `service()` routine that checks whether it should do anything, replacing the old busy-wait loop
- **Live updating** - Edits to the YAML state files will live update with new connections (whether you're editing them in the onboard editor or as a mounted USB MSC device on your computer)
- **Better fonts** - New fonts available: `Berkeley`, `Iosevka`, `Pragmat[ism]`
- **YAML connection files** - More permissive of malformed syntax
- **Unified syntax highlighting** - Works consistently in `eKilo`, `python`, and normal input after `>`

The JumperlOS firmware repo is at [https://github.com/Architeuthis-Flux/JumperlOS](https://github.com/Architeuthis-Flux/JumperlOS)

---

## Safety Info

Here's an image of the little card that should have been inside your box

![Safety info Never put voltages above +9V or below -9V anywhere on this board. Don't use unpowered, the crossbars need power to block voltage too. Don't power externally, use the internal power supplies (rails / DACs). It can be powered from the 5V and GND pins on the Nano header or the FPC adapter instead of USB. External signals are okay, as long as the board remains powered.This board gets fairly warm in normal operation from the LEDs, if it ever gets hot, unplug it immediately and let me know. When the switch on the probe is set to Select Mode,
it should only be used on the gold probe sense pads.The probe tip in Select Mode is always at 3.3V. Don't stab yourself or others with the probe, unless it's in self-defense. Do not eat your Jumperless V5. When in doubt, don't hesitate to ask!](https://github.com/user-attachments/assets/d7f13c5b-da36-488d-81e4-cf43be6adb30)




- Never put voltages above +9V or below -9V anywhere on this board.

- Don't use unpowered, the crossbars need power to block voltage too.

- Don't power externally, use the internal power supplies (rails / DACs).

- It can be powered from the 5V and GND pins on the Nano header or the FPC adapter instead of USB.

- External signals are okay, as long as the board remains powered.

- This board gets fairly warm in normal operation from the LEDs, if it ever gets hot, unplug it immediately and let me know.

- When the switch on the probe is set to Select Mode, it should only be used on the gold probe sense pads.

- The probe tip in Select Mode is always at 3.3V.  

- Don't stab yourself or others with the probe, unless it's in self-defense.

- Do not eat your Jumperless V5.

- When in doubt, don't hesitate to [ask!](https://discord.gg/TcjM5uEgb4)



There are a lot of exceptions to these if you know what you're doing. It's pretty hard to permanently damage this board.

Some things (usually external power with the Jumperless off) can cause lockup on the [analog CMOS switches](https://tinyurl.com/24xrspea), but the current limiting resistors on their power supply pins generally keep them from drawing so much current that they permanently break. In situations where one chip is getting crazy hot, the first thing to try is to unplug the Jumperless, let it cool down, and try it again (obviously, change whatever you think was causing it). Most of the time they go back to normal after some rest.


Don't let any of this scare you, I'd rather you just pretend it's indestructable and use it with reckless abandon. So if you manage to break anything, just let me know and I'll send out a fresh one and a return label, no questions asked*.

*Actually, a ton of questions asked, so we can figure out how it happened and maybe prevent it from happening to someone else. But the point is I don't care if it's clearly your fault and not some manufacturing defect, I will make sure you have a working Jumperless.

<img width="6535" height="1030" alt="Artboard 21" src="https://github.com/user-attachments/assets/e3b4c4a7-47de-4571-8b44-b7829961199a" />
It's even printed on the box

---


## Bandwidth

Michael has done some [awesome work characterizing the bandwidth of the Jumperless](https://codeberg.org/multiplex/jumperless-wigglyvolts).

![](https://codeberg.org/multiplex/jumperless-wigglyvolts/media/branch/main/screenshots/IMG_2886.jpeg)

The TL;DR is just the physical breadboard puts the 3dB rolloff t ~13MHz, and a signal passing through the crossbar matrix brings it down to around ~8MHz. 

It makes sense these are pretty high, these CH446Qs were originally made for switching video signals so bandwidth was pretty important when they were designing them. Keep in mind this isn't a hard limit, it's just where the signal gets attenuated by the (arbitrarilyish) defined 3dB, so your signal's amplitude is reduced by √2.

---

![HeroNew](https://github.com/user-attachments/assets/8eb56a45-aa24-4dd0-8528-8c3656c0b4ae)
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

---

## What's that `BUFFER_IN - DAC_0` bridge that's always there?

That gets added to power the `probe LEDs`, it's kinda weird, but to multiplex 3.3V, GND, LED data, 2 buttons, and a +-9V tolerant analog line over the 4 wires on a TRRS cable, the line powering those LEDs is shared.

The `connect`/`measure` switch is a Dual Pole Dual Throw (DPDT) switch. The probe tip needs to be at a steady 3.3V to be read by the `probe sense pads` which is a big resistive divider sensed by a single `ADC`.

When you have it in `select` mode, the probe tip is getting 3.3V from a `GPIO` on the RP2350B driven `high`, and the LEDs get their power from the analog line, which is `ROUTABLE_BUFFER_IN` connected to `DAC 0` set to 3.3V.

When you switch to `measure` mode, those roles get swapped, the LEDs are powered by that `GPIO`, and the probe tip is now `ROUTABLE_BUFFER_IN`. In the current firmware, that just stays at 3.3V so you can *kinda* sense pads in either mode (you may notice the sensing is a lot wonkier, that's because the `DAC` isn't perfectly calibrated to output *exactly* 3.3V.) But in the future, there will be some other stuff you can do in that mode treating it as an analog line (and of course, I'll forget to update this, if it's after like June 2025, double check this is still true.)

##### A side effect of needing a crossbar connection to light the probe is that the LEDs in `Select` Mode act as a test of whether the Jumperless is properly making connections.

### Why am I using one of the precious two DACs and not another GPIO?

The answer is switch position sensing. You may notice there's no obvious way for the Jumperless to know where the switch is set, so I had to get creative on this one. `DAC 0`'s output is hardwired to go through a `current sense` shunt resistor, so when `DAC 0` is powering the `probe LEDs`, they'll be drawing some current I can measure with one of the `INA219`s, and therefore I can be reasonably confident that the switch is in the `select` position.

If you need both `DAC`s, you can just get rid of this connection and the `probe LEDs` won't light up, but other than aesthetics, it really has no effect on functionality. Or you connect `ROUTABLE_BUFFER_IN` to a `GPIO` and set it `high` and just lose the ability to sense where the switch is. 

---

## AI Generated Wiki

If you want to read a wiki generated by AI and ask it questions about how this thing works and how to use it, [**DeepWiki**](https://deepwiki.com/Architeuthis-Flux/JumperlessV5/1-overview) was surprisingly accurate (enough.) 

The docs on this site are more about how to *use* your Jumperless, this is more geared toward helping understand the circuitry and code.

---

## Onboard Help 

Use `help` or `[command]?` for onboard documentation

![Screenshot 2025-07-04 at 5 52 32 PM](https://github.com/user-attachments/assets/522bfcb4-f836-464c-bcdf-1b302d05005b)

---

## [GitHub Releases](https://github.com/Architeuthis-Flux/JumperlessV5/releases)

If you want more info about each feature when I was particularly excited about it, I usually write about the new features in the [Release notes on Github](https://github.com/Architeuthis-Flux/JumperlessV5/releases).

---

## Schematic

Here's the schematic that's printed on the inner flap of the box
![](https://github.com/user-attachments/assets/1c91a76d-cacf-40f0-a87b-c952787abb6f)

If you want look at the schematic and PCB together and don't feel like downloading the whole thing and opening it in KiCad, [you can open it in the browser with KiCanvas here](https://kicanvas.org/?github=https://github.com/Architeuthis-Flux/JumperlessV5/blob/main/Jumperless23V50/MainBoard/JumperlessV5r6/JumperlessV5r6.kicad_pro)


