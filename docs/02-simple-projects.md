# Simple First Projects

These are tiny beginner projects for a Jumperless V5. They use the onboard MicroPython API to make the software jumpers for you, so the only physical parts you need to plug in are the components.

For the scripts below, run them from [JumperIDE](https://ide.jumperless.org/) or from the MicroPython REPL. They call `nodes_clear()` so each project starts from a clean board; save any slot you care about before running them.

The row numbers here are just examples. If you put a part somewhere else, change the matching row numbers in the script.

## 1. Blink an LED

Parts: one LED and one resistor.

Physical setup:

1. Put one end of the resistor in row `10` and the other end in row `11`.
2. Put the LED `+` leg (anode, usually the longer leg) in row `11`.
3. Put the LED `-` leg (cathode, usually the shorter leg) in row `12`.

```jython
import time

nodes_clear()
connect(GPIO_1, 10)
connect(GND, 12)
gpio_set_dir(1, True)

while True:
    gpio_set(1, True)
    time.sleep(0.5)
    gpio_set(1, False)
    time.sleep(0.5)
```

What should happen: the external LED blinks on and off once per second.

## 2. Button Turns an LED On

Parts: the LED circuit from project 1, plus one pushbutton.

Physical setup:

1. Leave the LED and resistor in rows `10`, `11`, and `12`.
2. Put a pushbutton between rows `20` and `21`.

```jython
import time

nodes_clear()
connect(GPIO_1, 10)
connect(GND, 12)
connect(GPIO_2, 20)
connect(GND, 21)

gpio_set_dir(1, True)
gpio_set_dir(2, False)
gpio_set_pull(2, 1)

while True:
    pressed = not bool(gpio_get(2))
    gpio_set(1, pressed)
    time.sleep(0.02)
```

What should happen: the LED turns on while the button is pressed.

## 3. Fade an LED

Parts: the LED circuit from project 1.

Physical setup: leave the LED and resistor in rows `10`, `11`, and `12`.

```jython
import time

nodes_clear()
connect(GPIO_1, 10)
connect(GND, 12)
gpio_set_dir(1, True)
pwm(1, 1000, 0)

while True:
    for level in range(0, 101):
        pwm_set_duty_cycle(1, level / 100)
        time.sleep(0.01)
    for level in range(100, -1, -1):
        pwm_set_duty_cycle(1, level / 100)
        time.sleep(0.01)
```

What should happen: the LED smoothly gets brighter and dimmer.

## 4. Three-LED Traffic Light

Parts: three LEDs and three resistors.

Physical setup:

1. Red LED: resistor row `10` to `11`, `+` row `11`, `-` row `12`.
2. Yellow LED: resistor row `20` to `21`, `+` row `21`, `-` row `22`.
3. Green LED: resistor row `30` to `31`, `+` row `31`, `-` row `32`.

```jython
import time

nodes_clear()
connect(GPIO_1, 10)
connect(GPIO_2, 20)
connect(GPIO_3, 30)
connect(GND, 12)
connect(GND, 22)
connect(GND, 32)

for pin in [1, 2, 3]:
    gpio_set_dir(pin, True)

while True:
    gpio_set(1, True);  gpio_set(2, False); gpio_set(3, False)
    time.sleep(2)
    gpio_set(1, False); gpio_set(2, True);  gpio_set(3, False)
    time.sleep(0.5)
    gpio_set(1, False); gpio_set(2, False); gpio_set(3, True)
    time.sleep(2)
```

What should happen: the red, yellow, and green LEDs cycle like a traffic light.

## 5. Read a Potentiometer

Parts: one 10k potentiometer.

Physical setup:

1. Put one outside leg in row `30`.
2. Put the middle leg in row `31`.
3. Put the other outside leg in row `32`.

```jython
import time

nodes_clear()
dac_set(TOP_RAIL, 3.3)
connect(TOP_RAIL, 30)
connect(ADC0, 31)
connect(GND, 32)

while True:
    voltage = adc_get(0)
    print("pot = " + str(round(voltage, 3)) + "V")
    time.sleep(0.25)
```

What should happen: turning the knob prints a voltage from about 0V to about 3.3V.

## 6. Simple Night Light

Parts: the LED circuit from project 1, one photoresistor, and one 10k resistor.

Physical setup:

1. Leave the LED and resistor in rows `10`, `11`, and `12`.
2. Put the photoresistor between rows `30` and `31`.
3. Put the 10k resistor between rows `31` and `32`.

```jython
import time

nodes_clear()
dac_set(TOP_RAIL, 3.3)

connect(GPIO_1, 10)
connect(GND, 12)
connect(TOP_RAIL, 30)
connect(ADC0, 31)
connect(GND, 32)

gpio_set_dir(1, True)

while True:
    voltage = adc_get(0)
    gpio_set(1, voltage < 1.5)
    print("light sensor = " + str(round(voltage, 3)) + "V")
    time.sleep(0.1)
```

What should happen: the LED turns on when the photoresistor gets darker. If it works backward with your photoresistor, swap the photoresistor and 10k resistor positions.

## 7. Beep a Piezo

Parts: one passive piezo buzzer or piezo disc. Do not drive a normal speaker directly from a GPIO pin.

Physical setup:

1. Put the piezo positive leg in row `40`.
2. Put the piezo negative leg in row `41`.

```jython
import time

nodes_clear()
connect(GPIO_1, 40)
connect(GND, 41)

while True:
    pwm(1, 2000, 0.5)
    time.sleep(0.2)
    pwm_stop(1)
    time.sleep(0.8)
```

What should happen: the piezo beeps once per second.

## What to Read Next

- [Basic Controls](01-basic-controls.md) explains how to make and remove connections with the probe and clickwheel.
- [MicroPython](08-micropython.md) explains how to run scripts on the board.
- [MicroPython API Reference](09.5-micropythonAPIreference.md) lists every hardware function used above.
- [Odds and Ends](09.8-odds-and-ends.md) has the hardware overview and safety notes.
