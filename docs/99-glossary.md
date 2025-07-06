# Glossary of Terms

`net` = a group of all the `node`s that are connected together (enter `n` to see the list {there's a colorful update to that I'm working on right now})

`node` = anything the crossbar array can connect to, which includes everything on the breadboard and Nano header, as well as the internal `special function` `node`s like `routable GPIO`, `ADC`s, `DAC`s

`row` = *kinda* the same thing as `node` but I generally use it to mean stuff on the breadboard (so special function things like `routable GPIO`, `ADC`s, `DAC`s that don't have a set location are excluded)

`rail` = I use this to refer to the 4 horizontal power rails on the top and bottom (`top_rail`, `bottom_rail`, `gnd`), I will never call a vertical `row` a `rail`. (I know they're columns but it's easier to say a lot)

`bridge` = a pair of exactly two `node`s (this is what you're making when you connect stuff with the probe, enter `s` to print the (kinda misnamed) `node file`s to see a list of bridges)

`path` = the set of crossbar connections needed to make a single `bridge`, so it can have multiple `hop`s if it doesn't have a direct connection and needs to make a `bounce` through an intermediate `chip` enter `b` to see them

`node file` / `slot file` = this is an actual text file on the filesystem that stores the list of bridges, there's one of these for each `slot` (enter `s` to see all of them, they start with an `f {` to make it east to just copy paste them from the terminal)

`slot` = one of the 8 node files stored that you can switch between with `<`/`>` or the `menu`s. Named `nodeFileSlot[0-7].txt` (there's no actual limit, there's *so* much flash storage on this thing, but by default it's 8)

`menu` = I generally mean the onboard clickwheel `menu` when I say this (`click` the wheel to enter those and `scroll` around)

`chip` = shorthand for the CH446Qs specifically, lettered A-L. The first 8 (A-H) are considered "breadboard `chips`, and the last 4 are considered "special function" chips (enter `c` to see their connections)

That's probably more than you need to worry about but that gives me a nice start on real docs 