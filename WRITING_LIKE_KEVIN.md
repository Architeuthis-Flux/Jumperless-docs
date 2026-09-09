# Writing like Kevin

Corpus: 13 Jumperless docs pages from July 2025 (11 hand-written, about 6,700 words as files, 4,400 of prose), 3 repo READMEs he wrote (Jumperless, JumperlessV5, breadWare, about 5,500 words), 92 GitHub replies (about 8,400 words, 2021-2026), 31 hackaday.io pages and logs (about 24,000 words after de-duplication, 2021-2023), the Crowd Supply campaign page and 8 updates (about 14,000 words), and 1,142 Bluesky and Mastodon posts (about 34,000 words). Scraped 2026-09-07; this guide finished 2026-09-08 after three blind rounds (24 imitations, 24 caught, 0 real paragraphs miscalled).

## How to use this

1. Read the portrait (section 1). It is one paragraph and it is the whole voice; everything after it is the evidence and the edge cases.
2. Write the draft with the cheat sheet (section 2) next to you. Before you write a key, a number or a mechanism, find it in section 5.1 or in your brief. If it is in neither, the sentence is not written.
3. Run the checklist (section 11) over the draft, item by item. The strip list in 9.5 is the same checks as a sequence of deletions, if you would rather edit than audit.
4. Put your draft between two real paragraphs from the evidence appendix (section 12), from the same register, and read all three. For docs, use the `remove` bullet and the `measure` paragraph listed under 12.5; both were taken for his 3-0 by judges who knew the corpus. If yours is the tidy one, or the witty one, it is not done.

Two things about this document. It is not written in his voice; it is a plain description of one, and copying its sentences into a draft is a tell (section 10 opens with that rule). And its numbers come from the corpus as counted on 2026-09-08: docs figures are for the 11 hand-written pages unless a page is named (185 sentences split at periods, about 4,400 words of prose once code blocks, tables and image lines are removed), reply figures are for the 92 GitHub replies, and hackaday and social figures are for the de-duplicated files.

---

## 1. What this guide is for, and the portrait

This guide exists so someone who has never read a word of Kevin's writing can produce a docs section, a README paragraph, or a support reply that a Jumperless user would take for his. That means rules with numbers and quotes, not adjectives. "Short sentences" is useless. "Median 19 words, one instruction per sentence, the caveat in parentheses after the instruction" is usable. Every rule from section 3 on is backed by at least one quote of his, copied byte-for-byte with typos, and the appendix collects two or three per rule. Sources are a docs filename (`docs_july2025/...`), a README filename (`readmes/...`), or a URL.

The portrait, in one paragraph. Kevin writes the way he answers a question at a bench. He tells you which key to press, what you should see, and the one thing that will trip you up, roughly in that order, and then he stops, or he wanders into a cross-link and stops there. He owns the product in the first person ("I need to settle on a good time for this, if it feels too short or long lmk") and hands the reader the second person ("you can", "if you want"). His asides go in parentheses at the end of the sentence, never in dashes, and about half of them are about the state of his own code, not cautions to the reader. His hedge is "should", his intensifier is "just", his softener is "kinda", and his "I don't know" is "idk". He coins names for parts of the system, wraps them in backticks (in the docs; nowhere else), and defines them on the spot. He is enthusiastic about one specific thing he built ("this *one* feature is the reason I did this whole update") and flat about everything else. He never sells, never writes a summary, never asks a question he doesn't answer in the next clause, and never explains a mechanism he hasn't measured. When a bug is his, he says so in plain first person ("I think I may have left some silly change in the code"; "it's because I've messed up the addressing somehow"), and twice in 92 replies that came out as "on me for ...". His jokes are deadpan, one per few paragraphs, and live in a parenthesis or a heading, never inside an instruction. His asides about his own code are to-do notes, not punchlines ("I need to settle on a good time for this", "(kinda misnamed)", "I'm gonna call this idle mode here until I think of a good name"), and rewriting one of them to be wittier is the most reliable way to stop sounding like him. He will tell you what he hasn't finished, in the present tense, in the middle of the instruction, and he repeats a point he thinks matters instead of compressing it. His verbs for what the firmware does are the literal ones (it will "try to find" the OLED, "disconnect", "clear it and take you back"), and when he confesses a design decision he lists the alternatives and says he tried them, without arguing for the one he kept.

**Which sources count.** The hand-written July 2025 docs pages (01, 03, 04, 05, 06, 07, 09, 10, 11, 99, index), the three READMEs he wrote, the 2021-2023 hackaday logs, the Crowd Supply updates, and the GitHub replies (the 7 from 2026 may have had AI help; weight them low). Excluded as not his hand: `readmes/KnoBLE_README.md` (28 em-dashes in 1,700 words; every other file he wrote has none) and `readmes/Jumperless-App_README.md`. Weighted low: `docs_july2025/08-micropython.md` and the table half of `08-file-manager.md` (template prose like "This guide covers how to write, load, and run Python scripts", the only such opener in 13 pages). The Crowd Supply campaign page body is house-edited ("we" throughout, curly quotes, "±8 V" with a space, numbers spelled out); its word choice is his, its punctuation and units are not. One paragraph of that house-edited copy is pasted into the V5 README and into `index.md` ("the four individually programmable ±8 V power supplies; ten GPIO; and seven management channels"), so a semicolon list or a curly apostrophe in those two files is the campaign's. Judges have twice taken that paragraph for his on sight.

**Where the rules came from.** Three blind rounds, each with three judges, 8 real paragraphs and 8 paragraphs written from the previous version of this guide, on the same 8 briefs each time (a per-net current command, a blank-OLED reply, late probe cables, slots, negative rails, an on-resistance log, the Measure/Select switch, tapping a connected row). Every fake was caught and no real was miscalled, all three times. What each round added:

- Round 1: invented facts (a wrong key, a wrong number, a guessed mechanism; section 5.1), uniform tidiness (a caveat on every clause, one sentence per beat, a troubleshooting ladder; 4.1, 4.4, 6.4), borrowed tics ("That's on me", "(that's a period)"; 7.6, 5.3), and register leakage (docs backticks in a reply or a log; 3, 4.9).
- Round 2: every fake shared clauses with a model answer in the previous guide, so the model answers are now one-line shapes (section 10) and the checklist has a grep step; paraphrase drift toward wittier and tidier (6.11); tic stacking (4.7); fabricated arcs around a published number (8.6); three-to-four-sentence blocks (4.2); a config line inline (4.9); facts fused across pages (6.11).
- Round 3: the guide's own `[CHECK]` device left in the copy (5.2); "one long ragged sentence" read as licence for a 100-word comma splice (4.1); a lifted two-word aside (6.11); invented design history (4.4); folksy firmware verbs (section 5); negation-correction openers (4.5); self-calibrated guesses (7.8); punchline beats and a borrowed sign-off in a log (8.6).

Three judge reasons contradicted the corpus and are not rules: `idle` and `warn` are backticked in his own bullets ("reddish `warn`", "spit you back out to `idle` mode"); 14.2V, ~18.5V and ~90Ω are his numbers (issue 20, V5 README), the fault was restating them without their source; "ADC 7 is hardwired to the probe tip" is his own code comment. The reals were recognized every time by texture nobody can reproduce on purpose (an unclosed parenthesis, a pasted code comment, a dropped article) and by correct specifics ("the non-obvious counts are all right"). Do not chase the first; the second is the one lever a writer has (9.4).

---

## 2. Docs cheat sheet

One screen, docs register only. Replies and logs differ; see section 3.

Shape
- A section is a bare-noun `##`, then: the key or where the thing lives, what you should see, one parenthesis, stop. Median 86 words.
- A paragraph is one sentence, sometimes two, rarely three. Blank line, screenshot, next instruction.
- Sentences are ragged: median 19 words, a 7-word line beside a 50-word one. A long one is long because a parenthesis opened inside it. Nothing over about 75 words.
- The page ends on the last fact, a parenthesis, a code block or an image. No recap, no next steps.

Joints
- A bare comma joins independent clauses. No em-dashes, no semicolons, no ellipses. A spaced hyphen after a list lead, `>` between menu items, a slash for "or".
- The aside is in parentheses after the thing it qualifies. One per paragraph; two if both are about the state of his code.
- Notes are "(note: ...)", "Keep in mind that", "Remember". No Note, Warning or Tip box.

Words
- "should" is the result of a step; "might" is a bug; "just" means this is the whole step; "kinda", never "kind of"; "idk" for a fact he does not have; "lmk" once a page at most.
- Backticks on keys, modes, buttons, nodes, filenames and coined terms, plural s outside (`node`s). Never on a number or a unit. One span per ~12 words at the densest.
- Numbers bare and glued to the unit: 3.3V, 500ms, 7x2. Digits for counts ("2 buttons").
- `row`, `rail`, `node`, `net`, `bridge`, `slot`, `node file`, `chip`, the probe, the click wheel, the menu, the app, "stuff". Never "the user", "we", "please", "simply", "ensure".
- The firmware's verbs are literal: find, connect, disconnect, print, clear, take you back.

Order
- Precondition, action, what you should see, what it means, mistake recovery, how to exit. The why comes after the how, as "**Why X?**" answered in the next clause.
- No benefit sentence, no use-case lesson, no "this section covers".
- Alternatives last, opened with "If you want", "Or". Option lists trail off with "or whatever".

Facts
- Every key, number, pin and mechanism comes from section 5.1 or the brief. Otherwise the sentence is left out and a note goes under the draft, never inside the copy.
- If the topic is on one of his pages, the draft is his sentences byte-for-byte plus what is new.
- A config line is a fenced block with its leading backtick, never inline.

Humor
- One deadpan aside per 4-5 sentences on a chatty page, none on a reference page. It is about the state of his code, not a punchline. Enthusiasm is one italic word or "sick".

---

## 3. The registers, and which one the docs use

He writes in six registers. What stays constant across all six is the floor of his voice; what shifts is volume and which device is allowed.

- **Docs** (`docs_july2025`). "you" in about a third of sentences, "I" in about one in eight. Sentences open on a verb, "If", "To", "You can". About 260 backtick spans in 13 pages, on keys, modes and coined terms, never on a number. One parenthetical aside per 4-5 sentences on the chatty pages, none on the reference pages. No sign-off; the page stops on its last fact. Profanity twice in the 11 pages, both in a parenthesis or a bullet.
- **README** (Jumperless, V5, breadWare). "I" and "you". Link headers stacked above the prose. No backticks wrapping terms (V5 has two stray empty pairs, and one pasted campaign paragraph carries the file's only semicolon list, "±8 V" and a curly apostrophe). Hyphenated joke compounds, one extended bit closed with "So yeah, wizard shit.", one markdown gag ("my poor ~~life~~ design choices"). No sign-off. A handful of swears in the pitch paragraphs.
- **Support reply** (GitHub). "I" and "you". Opens on "@handle", "Hey", "Oh", "Yeah", "Thanks for putting in this issue!" (once), or straight on the fact; never on a negation-correction. Under ten backtick spans in 92 replies, every one a shell command, a package, an app name, or a line to paste (`pip3 list`, `XLSX Gui`, an `f 1-2,GND-5,...` bridge list). One dry clause at most ("Schrödinger's bug."). Closes on "Let me know if that works for you.", a question, or nothing; never an imperative. Profanity rare ("Ah shit, Wokwi added a README.md").
- **Hackaday log** (2021-2023). "I", and "we" in the 2023 tutorials. Opens on "So", "Anyway", "Okay", "Here's". No backticks at all. A hook line, a straight body, a soft closer: "let me know", or "To be continued with [the named next part]". Moderate profanity.
- **Campaign update** (Crowd Supply). "I" in the updates, "we" on the house-edited page, "our" for the community's places. Opens on a one-liner, "TL;DR:", or "Hey everyone,". One backtick in 14,000 words. Pun headings over straight bodies, a flat "Note:" sentence after a bit once, a P.S. Closes on a channel list, then "Love," (5 of 8), "Sincerely,", "Cordially," or "Dictated but not read,", then "Kevin". Near zero profanity.
- **Social** (Bluesky, Mastodon). "I". Opens on "Okay", "Wait", "Holy shit youguise". No backticks. The post is the bit. No sign-off. Heavy profanity.

**The docs use the support-reply register, not the hackaday or campaign register.** Second person, verb first, a term in backticks, one parenthetical caveat, then stop. The shape of a good Kevin docs sentence is: imperative or plain statement, then `term`, then (caveat, aside, or why), then an optional "or whatever" / "lmk".

"Enter `n` in the menu to show this one. If you have anything that's doing any measurement (`gpio` input or `ADC`s), it'll stay up and live update if any of them change. (And just like basically any menu not asking for input, entering anything will bring you back to the main menu.)" (`docs_july2025/07-debugging.md`)

What crosses into the docs from other registers: "TL;DR" as a one-line closer after a long bullet (it is 5 in the whole corpus, one per register), "Here's X:" pointing at an image or code block (README, logs), the "Yes, [concede the objection], [instruction]" opener (docs, README, campaign), "let me know" / "lmk".

What is fenced out of the docs: "So"/"Anyway"/"Okay" as section glue (0 in the docs; 11 sentence-initial "Anyway" and 6 "Okay" in the de-duplicated hackaday file); pun headings ("La Résistance", "New Fab, Who Dis?", "Rawssbar Switching", campaign only); sign-offs and P.S. (campaign only); "youguise", "jk", "omg", "Ha", "friggin'", stage directions in double asterisks (social only); "we" (1 hit in the docs, "we've got colors now!", against 36 "I"; it does appear in a 2021 reply, "so we can run them a bit further out of spec than we already are", and once in the V5 README, "we live in a universe governed by both physics").

**What the docs device never does is leave the docs.** Backticks: about 260 spans in the docs, 0 in the hackaday file, 0 in 34,000 words of social, 1 in 14,000 campaign words, and the handful in support replies are all literal commands or names ("or just do >> `pip install beautifulsoup4` and then do that for the next "no module found" error that comes up."; "btw I changed the app index from 6 to 7 to not conflict with `XLSX Gui`"). A key in a reply or a 2023 log is plain or in single quotes: "Just type 'f' and it will wait for a set of bridges connected with a dash and separated with a comma, whitespace is ignored." (hackaday getting-started). Round 1 caught a reply and a log for docs backticks on `row`, `SDA`, `bridge` and `hop`s alone.

---

## 4. Sentence-level rules

### 4.1 Length and shape, and the shape is ragged

Docs sentences run a median of about 19 words in prose paragraphs (14 if you split at images and line breaks too); aim for 15-20. About one in five passes 30 words, and those long ones are comma chains with a parenthesis in them, not subordinate clauses. Long sentences land on a short flat verdict: "The answer is switch position sensing." (`09-odds-and-ends.md`), "And no, it's not an FPGA." (`readmes/Jumperless_README.md`), "So yeah, fixed." (https://github.com/Architeuthis-Flux/Jumperless/issues/5#issuecomment-1627395775).

The median hides the variance, and the variance is the tell. His paragraphs are ragged: a 74-word sentence with two parentheses inside a bullet, then a 10-word tag. "`remove` will briefly turn the `row` reddish `warn` (I need to settle on a good time for this, if it feels too short or long lmk), another `remove` press will remove that `row` (just like in `probe` mode, it removes the `bridge` it's in, so just things that have a direct connection to that `row`, not the whole `net`), if you let it time out without pressing anything, the row will be unhighlighted. TL;DR, double click `remove` to remove, single click to unhighlight." (`01-basic-controls.md`). A paragraph where every sentence is 15-25 words and every sentence closes on its own caveat reads as a template; every fake in round 1 had that shape and the judges named it ("one-sentence-per-beat structure", "each sentence delivers exactly one clean instruction", "evenly clause-balanced").

Round 3 found the other edge. Four docs fakes read "one long ragged sentence" as licence for one 90-113 word comma splice, and the judges named that as a synthetic register on sight. The distribution on the hand-written pages, 185 sentences split at periods (a period inside a closing paren counts): 32 are under 10 words, 64 are 10-20, 47 are 20-30, 33 are 30-45, 8 are 45-60 and 1 is over 60. The longest, 74 words, is the `remove` bullet above, and 43 of its words are inside its two parentheses, with the 10-word TL;DR after it; the next five (57, 56, 54, 53, 53) each carry a parenthesis too. Of the 9 sentences past 45 words, 7 have a parenthesis, and the 2 that don't are 50-word section leads that state a mechanism: "**Why Select mode?** `Measure` mode allows the probe tip to be ±9V tolerant and routable like any other node, but as of yet, the code to actually do anything with it is unwritten so it just connects to DAC 0 and outputs 3.3V just like it was in `Select` mode." (`01-basic-controls.md`) and the `DAC 0` switch-sensing sentence on `09-odds-and-ends.md`. His long sentences are long because an aside opened inside them or because a mechanism needed the room, and they sit beside 7-word lines under a `##`: "Click the button again to get out.", "and the logo should turn reddish", "You can just paste this into the main menu:". A sentence over about 75 words is outside his range; a 90-113 word comma chain of instructions with no parenthesis is not one of his two 50-word leads, it is the monolith the judges named. Raggedness is variance, short beside long, not uniform length in either direction.

The short flat landing is an answer or a fact, never a curtain line. "The answer is switch position sensing." answers the bold question above it; "So yeah, fixed." reports a state. Round 2's on-resistance log built a mystery and dropped "That's the whole story." on it, then teased "Anyway, next up is what this does to pathfinding". "That's the whole story" is 0 in his hand (the one "That's the whole point." is in the excluded KnoBLE README) and "next up" is 0 (the campaign hits are the site's "Next Update" button). His contrast between the case that matters and the case that doesn't is one flat clause, not a seesaw: "For most circuits, this really doesn't have a noticeable effect." (V5 README), against the fake's "Doesn't matter even a little for logic, but it matters a whole lot once anything is actually drawing current".

One instruction per sentence. When two things happen in sequence, they get a comma, not a "then" clause: "Click the `Remove` button" [image] "and the logo should turn reddish" (`01-basic-controls.md`).

### 4.2 One thought per paragraph

Counting prose paragraphs on the hand-written pages: 74 of 103 are one sentence, 23 are two, 5 are three, 1 is four. Treat four as a ceiling you do not reach. Instruction, blank line, screenshot, next instruction. A sentence will continue across an image. The 4+ sentence paragraphs in the corpus are the README essay and the campaign updates.

Every docs fake in round 2 was one block of three or four balanced sentences, and the judges read the block itself as the tell ("three balanced clauses where his real docs run choppy", "walks slot → write → return → dump in tutorial order"). When a brief asks for "a paragraph", his paragraph is one long ragged sentence with a parenthesis in it, or two sentences and a bullet, or a `##` with three one-line paragraphs under it.

When a brief says "one paragraph, no headers, no bullets" about a topic his pages cover in bullets or glossary lines, the answer is still his lines: a bullet with its dash removed is a one-sentence paragraph, a glossary line already is one, and two of them with a blank line between are two paragraphs. "`slot` = one of the 8 node files stored that you can switch between with `<`/`>` or the `menu`s. Named `nodeFileSlot[0-7].txt` (there's no actual limit, there's *so* much flash storage on this thing, but by default it's 8)" (`99-glossary.md`) is a paragraph on its own. The brief's "paragraph" is met by one of his sentences and never by a 100-word one of yours. Round 3's slots fake wrote in its own note that quoting him was "impossible" under its brief and produced a 113-word two-sentence block; three others made the same choice silently, and all four were caught as one register.

### 4.3 The comma is the only joint, and there are no dashes

Independent clauses get a bare comma: "Don't worry about the baud rate, the Jumperless senses what the host computer is set to and changes the speed accordingly." (`05-arduino.md`). He drops the comma before "but": "It probably looks like nonsense to you but I've been in it so long it makes perfect sense to me." (`07-debugging.md`).

Zero em-dashes, zero en-dashes, zero `--` as a dash in everything he wrote by hand (the one em-dash in the hackaday file is an embedded tweet's attribution line, site chrome). Where a dash would go, he uses a comma, a parenthesis, or:

- a spaced hyphen as a list separator: "**[Odds and Ends](09-odds-and-ends.md)** - Stuff I couldn't think of a good category for" (`index.md`)
- a slash for "or": "a `hold` (long) is a `no`/`back`/`exit`/`whatever`." (`01-basic-controls.md`)
- a spaced `>` for menu paths: "it's `Display Options` > `Bright` > `Menu`" (`01-basic-controls.md`)

Semicolons: 2 real ones in the docs prose (one is inside the TL;DR); the others on the pages are config lines, an iframe attribute and the pasted campaign paragraph. Ellipses: 0 in the hand-written docs (133 in social; that is a social habit).

### 4.4 The parenthesis carries the aside, after the instruction

Roughly one docs sentence in three contains a parenthesis. The aside sits after the thing it qualifies, in the same sentence or paragraph, and is often a whole sentence on its own. The period leans inside the closing paren in docs (about 2:1), outside in support replies; either is authentic.

"If you click the `Connect` button while you're not `holding` a `node`, it will leave `probe mode` and bring you back into `idle mode` (rainbowy `logo`, all 3 `probe LED`s on.)" (`01-basic-controls.md`)

Nesting is allowed, with braces or brackets inside parens: "(enter `n` to see the list {there's a colorful update to that I'm working on right now})" (`99-glossary.md`).

A "note" is a lowercase parenthetical, never a callout: "(note: the color now follows the `row` instead of the net, so it can keep the colors even if you remove nets below it and they shift, this was soooo difficult until I realized I should do it by `node`)." (`01-basic-controls.md`). The other forms are "Remember ...", "Keep in mind that ...", "Don't worry about ...". No `**Note:**`, Warning or Important boxes anywhere in the hand-written pages; the form goes back to the 2021 breadWare README ("(note: these are abstracted away to the user by using b1-b30 instead of bigger numbers.)"), and the one bare capitalised "Note:" sentence in his hand is in a Jan 2025 campaign update, after a joke.

**The aside is a self-interruption, not a caution per clause.** One parenthesis per paragraph is the norm, two when both are his kind (the `measure` paragraph on `09-odds-and-ends.md` has two, one of them dated, and was taken for his 3-0 in round 3), and about half of them are about him and the state of his code, not about what the reader should expect. The five dated, self-doubting caveats in the docs:

- "(I need to settle on a good time for this, if it feels too short or long lmk)" (`01-basic-controls.md`)
- "(this might be broken in that FW release, I'm fixing that right now actually, and will just be purple/white)" (`09-odds-and-ends.md`)
- "(and of course, I'll forget to update this, if it's after like June 2025, double check this is still true.)" (`09-odds-and-ends.md`)
- "(if I missed something, let me know, it's a fairly new thing so I've probably forgot to add code for it to print in a bunch of places.)" (`04-oled.md`)
- "{there's a colorful update to that I'm working on right now}" (`99-glossary.md`)

The other kind of aside is a definition or a why ("(that's a period)", "(I know they're columns but it's easier to say a lot)"). What he does not write is a reader-facing engineered caution on every sentence. Round 1's current-command fake closed five sentences in a row on one ("so a full board should take like a second", "so don't go looking for leakage with this", "those get measured on a different chip and I haven't merged the two readouts yet") and all three judges called it: "every sentence here closes on a tidy engineered caveat". When you do not know a limit, do not manufacture one; write the aside about the code being new instead, which is what he does.

Three more things about these five asides. First, they are to-do notes, not jokes: each says what he hasn't decided or finished, in flat words. A writer who touches one makes it wittier, and the judges read wit as the direction imitation moves: one fake replaced "I need to settle on a good time for this, if it feels too short or long lmk" with "that timeout is a number I picked out of the air, so if it feels off lmk" ("same slot, better joke, which is the direction imitation moves"); another replaced "(kinda misnamed)" with "I call it a `node file` in some places and a `slot file` in others, it's the same file, I should really pick one" ("a too-neat punchline"). Second, they are single-use. A fake re-skinned the OLED aside as "the negative half of the calibration is fairly new and I've probably missed something", and a judge matched it to "it's a fairly new thing so I've probably forgot" on sight. Write a new aside about the actual state of the actual code in your brief, or write none; if the brief doesn't say what's unfinished, nothing is. Third, the aside that confesses a design decision does not argue for it. The one real example lists the alternatives and stops at having tried them: "(there were some choices here, like make each button assigned to high / low or allow removing them, but this felt like the best way after trying them all)" (`01-basic-controls.md`). Two round-3 fakes used the same invented shape, "(I had it removing on one press for a while, it's way too easy to knock something out of a `net` you meant to keep)" and "(I had it printing a line per net with a dash on all the ones it can't see, which just looked broken, so now it's the one number.)", and a judge matched them as one author. The shape is 0 in the corpus ("I had it" appears once, in a social post: "I had it working 6 hours before this arrived"; "way too easy", "meant to keep", "looked broken" are 0). The first of those also settled a question his real aside leaves open (the `remove` timeout is a to-do, not a lesson learned), and a judge said so ("a retrospective rationale instead of an unresolved detail"). If the brief gives no history, there is none. If it does, list the options and say he tried them.

### 4.5 Openers

Docs sentences open on the condition, the action, or the key: "If", "When", "To", "You can", "Click", "Go to", "Enter". "First," opens two of thirteen pages ("First, keep the switch on the probe set to `Select`", `01-basic-controls.md`). "Yes," opens a concession (7.2). Zero docs sentences open with "Anyway", "Okay", "Yeah", "Oh"; "So" opens three, each carrying a concrete consequence: "So tapping say, `row 25` that's connected to `GND` won't clear everything connected to `GND`, but tapping the `-` on the rails (for `GND`) would." (`01-basic-controls.md`).

Support replies open on an acknowledgement word or the fact: "Hey", "Oh", "Yeah", "Huh", "That's", "Thanks", "Ha". None opens with "Hi" or "Hello". Six open on an @handle and go straight into the sentence with no comma: "@modi12jin In my experience, when weird things are happening with getting a huge voltage sag when pulling any current, it's because I've messed up the addressing somehow" (https://github.com/Architeuthis-Flux/breadWare/issues/1#issuecomment-1603142325); "@nilclass Hey, your case has been sent out, it should be there sometime this week." "Hey, so" starts a reply that is bringing news rather than a fix: "Hey, so I just got a bunch of cases in, and I already have your address so I'm gonna send you one." (https://github.com/Architeuthis-Flux/Jumperless/issues/15#issuecomment-1857055402).

One opener he does not have: the negation-correction, "X doesn't Y by itself, you have to Z" / "the rails aren't stuck at 5V, they're ...". 0 sentence-initial negation-corrections in 185 docs sentences, none found in 92 replies; "aren't stuck" and "isn't stuck" are 0 in the corpus, "by itself" is 1 (campaign) and "on its own" 1 (social, about a video). The nearest things are an imperative with the fact after it, "Don't worry about the baud rate, the Jumperless senses what the host computer is set to" (`05-arduino.md`), and one line of README pitch, "It's not just about being too lazy to plug in some jumpers." Round 3's OLED reply ("Hey, it doesn't grab the OLED by itself, you've got to ask it to."), rails paragraph ("The `rail`s aren't stuck at 5V and 3.3V, they're 2 of the 4 programmable supplies") and log ("and I'd been picturing these as just switches") each opened on one, and a judge named "the antithetical opener". He opens on what the thing is or what you do: "The `connect`/`measure` switch is a Dual Pole Dual Throw (DPDT) switch." (`09-odds-and-ends.md`); "To connect the data lines to the Jumperless' GPIO 7 and 8, just use the menu option `.`" (`04-oled.md`).

### 4.6 Closers

Option lists trail off instead of closing: "Or you can use any terminal emulator you like, [iTerm2](https://iterm2.com/), [xTerm](https://invisible-island.net/xterm/), [Tabby](https://github.com/Eugeny/tabby), [Arduino IDE](https://www.arduino.cc/en/software/)'s Serial Monitor, whatever." (`03-app.md`). "or whatever" appears in every register. Lists run 2, 4, 5, 7 items; not a neat three.

The only call to action is a request to report back: "lmk" (docs, 2; 0 anywhere else in the corpus), "let me know" (18 in the replies, 16 in the hackaday file, 1 in the docs). Pages do not conclude (8.2).

The last sentence of a docs paragraph is a fact, a cross-link, or a hedge. It is never a button. The shapes he does not use, each caught in a round:

- a mirrored closer: "Then just slide it back to `Select`, nothing gets selected in `Measure`." (a judge called it "the too-neat chiasmus")
- a summarizing final clause: "which is how a `net` grows past 2 `node`s." His summary device is a one-line TL;DR after a long bullet, and only then.
- a suspense button: "To be continued." All three real ones name the next part: "To be continued with Driving the CH446Qs", "To be continued in part 4 - LEDs", "To be continued.... with probably the most interesting part of this whole thing, pathfinding." (hackaday, The Code series).
- a curtain line on a story, then a teaser: "That's the whole story." / "Anyway, next up is what this does to pathfinding". Both phrases are 0 in his hand.
- a "To be continued with" pointing at a topic instead of a part: "To be continued with the charge pump." A standalone log ends on its last fact, on "let me know", or on a flat line stated once: "Probably should have thought of this before spending $40 on effectively the same thing." (boxes-within-shirts-within-boxes log, taken for his 3-0 in round 3).
- an imperative close on a reply: "get a photo of the module and the SBC/SMD/OLED board it's plugged into and drop it in here." Replies end on "Let me know if that works for you." (issue 32) or on a question: "Could you also let me know if you have Rev 2 or Rev 3? and if it works on any other rows?" (issue 13).
- a punchy verdict on a state: "Do nothing and it should just unhighlight." His version of that fact is the flat clause inside the bullet: "if you let it time out without pressing anything, the row will be unhighlighted." (`01-basic-controls.md`).

"Let me know if that works." closes a reply in which he gave one thing to try (4 of 92 replies, always after a fix). It does not close a docs paragraph, and it does not sit after a request for diagnostics; the reply that asks for a photo ends on the ask: "If you want, send me close up photos of the front and back of the board and I might be able to spot the issue." (https://github.com/Architeuthis-Flux/Jumperless/issues/34#issuecomment-2221723926).

### 4.7 The four words: should, just, kinda, idk, and their rates

- **should** is the word for the expected result of a step, and it doubles as the hedge: "The logo should turn blue and the LEDs on the probe should also change" (`01-basic-controls.md`). 18 in the hand-written pages. "might" and "may" are fine for bugs, side effects and possibilities, and he uses them that way: "(this might be broken in that FW release, I'm fixing that right now actually, and will just be purple/white)", "you may notice the sensing is a lot wonkier" (`09-odds-and-ends.md`). What he never writes is "may"/"might" as the outcome of an instruction ("pressing X may connect Y"), or "please note". The "should" is attached to a step the reader just took. Round 3's rails fake hung a reassurance on a setting instead ("`bottom_rail` at -5V should come up at -5V and stay there until you move it", and a judge called it "a reassuring register") and the row fake closed on one ("Do nothing and it should just unhighlight."); his config page states the value and moves on ("`[dacs] limit_min = -8.00;"), and "stay there" / "until you move it" are 0 in the corpus.
- **just** marks "this is the whole step": "just use the menu option `.` (that's a period)." (`04-oled.md`). 35 in the hand-written pages, and at a similar rate in every register. "simply" is 0 in docs and replies.
- **kinda**, never "kind of", in docs (5 vs 0), italicized when hedging a claim: "`row` = *kinda* the same thing as `node`" (`99-glossary.md`).
- **idk** and **lmk** as typed, in asides: "(terminal.app on macOS, Powershell on Windows, idk on Linux)" (`03-app.md`); "`{"Name", index, ??idk, name of the function (unused)}`" (`11-WritingApps.md`). "I don't know" spelled out appears once in the corpus, in a 2021 reply. "let me know" spelled out when it is the actual closing request of a reply.

Other pace words: "basically", "pretty" ("pretty slow", "pretty reliable"), "literally", one stretched vowel per document ("this was soooo difficult").

**Rates.** The four words are rare. In the docs: lmk 2, idk 2, kinda 5, "or whatever" 3. Across the whole corpus "lmk" is those 2 and nothing else; he writes "let me know" everywhere else (replies 18, hackaday 16, campaign 3, social 5). Exactly one docs line carries two of them, and it is a long bullet: "(terminal.app on macOS, Powershell on Windows, idk on Linux), just go to the directory in a terminal and run the script in [tabby](https://tabby.sh/) or whatever" (`03-app.md`). Round 2's rails fake put "or whatever", "*kinda*" and "so lmk" in 120 words and a judge called it "tic-stacking ... overfitted to his signature"; the current fake put "lmk" and "idk" in consecutive sentences. Budget: one of the four per ~300 words of docs, two only in a bullet that runs long, never three in a paragraph, "lmk" at most once per page.

**idk is for a fact he doesn't have** ("idk on Linux"; "??idk" for a struct field he never used), never for a judgement he is declining to make. The fake's "which is either lazy or the right call, idk" is a hand-wring offered to the reader; his naming decisions are stated, not wrung: "I'm gonna call this idle mode here until I think of a good name" (`01-basic-controls.md`), "(kinda misnamed)" (`99-glossary.md`). "lmk" asks for a report of what happened on the reader's bench ("if it feels too short or long lmk", "if there's a specific thing, lmk"), not for a vote with a quip on it ("lmk which one you'd rather stare at").

His hedge on a number he is giving from memory is a parenthesis that says so: "which swaps X12 and X13 with X6 and X7 (or something like that, it's been a while)" (issue 20 thread). It is 2 in the corpus, both replies, so it is a shape to know (the number, then the admission that it is from memory), not a phrase to borrow, same as "knock on wood" (1, campaign) and "3ish" (1, a reply).

### 4.8 Terminal punctuation

- `!`: one in the hand-written docs ("we've got colors now!", `03-app.md`), and it marks a feature landing, never a step. Replies allow "Legit, thanks!" and "Nice!!". Ironic stacking ("!!1!") is README/social only.
- `?`: in docs only as a heading or a bold lead, answered in the next line: "## What's that `BUFFER_IN - DAC_0` bridge that's always there?" / "That gets added to power the `probe LEDs`" (`09-odds-and-ends.md`). Zero rhetorical questions hanging in docs body sentences. A reply can ask a real one: "Could you also let me know if you have Rev 2 or Rev 3? and if it works on any other rows?" (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783856159).
- `;` and `...`: essentially absent from the docs (4.3).

### 4.9 Emphasis, and exactly what gets backticks

- Backticks on every key, command, menu item, mode, button, node, filename, identifier, config line and coined term: 105 spans in the 1,299 words of `01-basic-controls.md`, one every 12 words. Plural s goes outside: "`node`s", "`ADC`s", "`probe LED`s". Filenames and identifiers count: "`nodeFileSlot[0-7].txt`", "`Platformio.ini`", "`ROUTABLE_BUFFER_IN`", "`Apps.cpp > runApp()`".
- **Never on a number.** Of about 260 spans in the 13 pages, none wraps a number with a unit; the only backticked digit is the menu key `2`, and the other non-word spans are the keys `.`, `-` and `~`. He writes "3.3V", "±9V", "500ms", "7x2", "45Ω", "~90Ω" bare, in prose, glued to the unit: "The probe tip needs to be at a steady 3.3V to be read by the `probe sense pads`" (`09-odds-and-ends.md`); "set to 500ms now" (`01-basic-controls.md`). Round 1's current fake wrote `0.5mA`, `2Ω`, `0.0` and was caught on that alone.
- **Density has a ceiling.** One span per ~12 words on the densest page. A fake ran one per 6 words with every noun wrapped and a judge called it "Every noun backticked". If the same word is wrapped three times in one sentence, unwrap the ones that are ordinary prose ("the `net`s get rebuilt" is a term; "the `JUMPERLESS` drive" is a name; "`U` mode is pretty slow" wraps a key that is not being pressed). Per sentence: his densest is 9 spans in 74 words (the `remove` bullet), and 10 of 185 docs sentences have 6 or more, every one of them a bullet, a glossary line, or a sentence with a parenthesis in it. Round 3's fakes ran 19 spans in 113 words, 13 in 100, 12 in 90; one kept to 10 in 113 and was still called "backtick-saturated", because the 10 sat in one comma-spliced sentence with no short line near it. The count alone is not the tell; the saturated monolith is (4.1). One judge said he would never backtick state names like `idle` and `warn`; he does ("reddish `warn`", "spit you back out to `idle` mode"), so match his usage, not the judge's.
- **Only in the docs.** See section 3. A reply wraps `pip install -r requirements.txt` and nothing else.
- **A config line is a fenced block, never inline.** The lines you paste into the menu start with a backtick ("`[top_oled] connect_on_boot = true;"), so they only survive inside a fenced code block, which is the only way he writes one: "You can just paste this into the main menu:" then the block (`04-oled.md`); "copy / edit / paste any of these lines into the main menu to change a setting" above a block of them (`06-config.md`). Inline backticks eat the leading one. Two round-2 fakes ("copy the `[dacs] bottom_rail` line" and "paste `[top_oled] connect_on_boot = true;` into the menu") were both caught for the missing backtick.
- Italics on exactly one word, 13 times in the hand-written pages: "not *everything* on the `net`.", "most helpful one for *me*", "*kinda*", "*should*", "*exactly*", "*one*", "*least*", "*so*".
- Bold for a list lead or a standalone must-not-miss line, never a word mid-sentence: "**Remember the probe is read by a resistive voltage divider**, so putting your fingers on the pads ..." (`01-basic-controls.md`); "**Why Select mode?**".
- No caps for emphasis in docs, no emoji anywhere he typed (the glyphs in the file-manager table are the firmware's own file icons).
- Capitalization follows the label on the thing and is inconsistent when there isn't one (`Connect` 5 / `connect` 4; "GitHub" and "Github"; "click wheel" and "clickwheel"). Leave it alone; do not normalize.

---

## 5. Vocabulary, naming, and the facts he wrote down

The middle column gives what he writes, then in brackets what he does not. The names come from his own glossary: "`rail` = I use this to refer to the 4 horizontal power rails on the top and bottom (`top_rail`, `bottom_rail`, `gnd`), I will never call a vertical `row` a `rail`. (I know they're columns but it's easier to say a lot)" (`99-glossary.md`).

| Thing | What he writes (not this) | Source |
| --- | --- | --- |
| vertical breadboard strip | `row` (not column) | `99-glossary.md` |
| the 4 horizontal power strips | `rail`, named `top_rail`, `bottom_rail`, `gnd` (not power bus) | `99-glossary.md` |
| anything the crossbar can connect | `node` (not point; not pin, except a part's pin) | `99-glossary.md` |
| everything connected together | `net` (not network, group) | `99-glossary.md` |
| a pair of connected nodes | `bridge` (he also uses "connection" loosely) | `99-glossary.md` |
| the crossbar route for one bridge | `path`, with `hop`s and a `bounce` through an intermediate `chip` (not route) | `99-glossary.md` |
| the saved-connections file | `node file` / `slot file` ("kinda misnamed"), `nodeFileSlot[0-7].txt`; a `slot` (not project, profile) | `99-glossary.md` |
| the switch ICs | `chip`, lettered A-L; "crossbar" in 2025 docs, "crosspoint" in 2023 logs (not mux, switch matrix) | `99-glossary.md`, `07-debugging.md` |
| the handheld | "the probe", "the probe tip", `pad`s / `probe sense pads` (not stylus; "wand" is campaign only) | `01-basic-controls.md` |
| the probe's cable | "the probe cable", a "TRRS cable" with "the 4 wires", a molded plug into "a TRRRS 1/8" audio jack" (not harness, ribbon, a header inside the probe; "crimp", "housing", "1.25mm" are 0 in his hand) | `09-odds-and-ends.md`, V5 README, time-to-get-excited |
| probe switch positions | `Select` / `Measure` (capitalized, in backticks; lowercase `select`/`measure` also appears) (not mode 1/2) | `01-basic-controls.md` |
| probe buttons | `connect` and `remove` (lowercase in backticks; `Connect` when naming the printed label) (not button A/B) | `01-basic-controls.md` |
| the encoder | "the click wheel" or "clickwheel"; presses are `click` (short) and `hold` (long) (not rotary encoder except as a part; not knob) | `01-basic-controls.md` |
| the LED matrix | "the breadboard LEDs"; the ring is the `logo`; `probe LED`s (not display, matrix) | `01-basic-controls.md`, `04-oled.md` |
| no-mode state | `idle mode` ("I'm gonna call this idle mode here until I think of a good name") (not home screen) | `01-basic-controls.md` |
| the OLED carrier | "the SBC/SMD/OLED board" (docs), "SBCSMDOLED adapter board" (campaign) (not the OLED header, the SBC board) | `04-oled.md`, campaign |
| the current sensors | "the `INA219`s", there are 2: one on `DAC 0`'s output shunt, one on the routable `current sense` shunt; "There's just one routable as a current sensor (the other is for measuring resistance / current draw from the DACs)"; the routable pair's identifiers in his firmware are `ISENSE_PLUS` / `ISENSE_MINUS` (not ammeter, not "the current of every net") | `09-odds-and-ends.md`, V5 README, a-farewell-to-campaigns, time-to-get-excited |
| the probe's analog line | `ROUTABLE_BUFFER_IN` as an identifier; "DAC 0", "GPIO 7 and 8" with a space in prose (not DAC_0 in prose) | `09-odds-and-ends.md`, `04-oled.md` |
| the product | "the Jumperless", "your Jumperless", "this thing" (not the device, the unit; "the board" is rare) | `03-app.md`, V5 README |
| the desktop software | "the app", "the Jumperless App", "the Wokwi Bridge" (not client, desktop application) | `03-app.md` |
| the serial UI | "the menu"; single-character commands are "menu option `.`", "enter `b` in the menu" (not CLI, console) | `04-oled.md`, `07-debugging.md` |
| special nodes | `special functions`, "in a sort of "folder"" (not virtual pins) | `01-basic-controls.md` |
| firmware | "FW" in asides, "firmware" in steps; a build is "the latest release" (not build, image) | `09-odds-and-ends.md` |
| things, features, code | "stuff" ("Arduino Stuff", "Do stuff with the onboard file system", "all that backend stuff") (not functionality, capabilities) | `05-arduino.md`, `index.md` |
| good | sick, solid, "extremely handy", "really cool", rad (logs and social), "works like a charm" (not powerful, seamless, robust) | `01-basic-controls.md`, `10-3d-stand.md` |
| bad, broken | janky, garbage, wonky, weird, flaky, finicky, nonsense, "a bummer" (not suboptimal, problematic) | `03-app.md`, `09-odds-and-ends.md` |
| hard | tricky, "a nightmare", "a pain in the ass", "complex as hell" (not challenging, non-trivial) | hackaday, replies |
| easy | "just", "literally any of these are fine", "really that simple" (not simply, straightforward, effortless) | `04-oled.md`, campaign |
| unfinished | "as of yet ... unwritten", "I'll eventually do", "I'm fixing that right now actually" (not coming soon, roadmap) | `01-basic-controls.md`, `09-odds-and-ends.md` |
| the reader | "you"; "you nerds" once; never "the user" as an addressee (0 in docs) | `03-app.md` |
| himself | "I"; "we" only on the house-edited campaign page, in 2023 logs and 2021 replies, and once in the V5 README (not the team) | all docs |
| voltages, times, sizes | 3.3V, ±9V or +-9V, 500ms, 0.25mm, 50MHz, 7x2, 8x16, bare, no backticks, no space before the unit; digits for counts ("2 buttons", "the 4 wires") (not "3.3 V", "two buttons", `3.3V`) | `09-odds-and-ends.md`, `11-WritingApps.md` |
| approximations | "like 3ish minutes", "a few", "pretty slow", "about 65Ω", ~45 ohms (never `~` in the docs) (not approximately) | replies, README |
| physical verbs | tap, click, double click, press, hold, scroll, swipe, unplug / replug, drop (a file), flash, bodge (not interact, actuate, engage) | `01-basic-controls.md`, `03-app.md` |
| abbreviations | idk, lmk, TL;DR, FW, btw (replies and social), jk (README and social), af (none spelled out in asides) | `03-app.md`, `11-WritingApps.md` |

Verb by control surface (from the docs): **enter** a single menu character ("just enter `c` in the menu"), **press** a key or chord ("press `Ctrl+P`"), **type** a word ("type `menu` then `slots`"), **tap** a pad, **click** / **hold** a button or the wheel, **swipe** along pads, **go to** a file or menu ("Go to `Apps.h` and declare your function where you'll write your app", `11-WritingApps.md`).

Verbs for what the firmware does are literal: "It will try to find the OLED on the I2C bus, after a few failed attempts, it'll automatically disconnect to free up GPIO 7 and 8." (`04-oled.md`); it will "clear it and take you back to the first `node`", "leave `probe mode` and bring you back into `idle mode`", "senses what the host computer is set to", "print the state to serial and the oled". The one figurative firmware verb on the chatty page is "spit you back out to `idle` mode", once in 1,300 words. "poke" is for the probe tip and for tweezers ("poke out connections with the tip", "poke around with the probe"), "grab" is for the app and libraries ("Just grab the app again"), "knock" is "knock on wood" and a cat. Round 3's fakes swapped in "grab", "pokes around", "knock something out", "drop it in here", "hung off", "picked out", "sitting right there", "down there", and the judges called it "folksiness added for texture" and "punchier folksy verbs". Every one of those is 0 in the corpus. His texture is in the aside, not the verb.

### 5.1 Facts he wrote down, and the rule for facts he didn't

Six of the eight fakes in round 1 were caught on an invented fact before anything about the voice came up. A voice guide cannot make a writer know the firmware, but it can say this: **if a key, a number, a pin, or a mechanism is not in this section and not in your brief, do not make one up.** Look it up in the docs or the firmware, or leave the sentence out and put a note under the draft for a human (never inside the copy, see 5.2), or write around it the way he does when he doesn't know: "`{"Name", index, ??idk, name of the function (unused)}`" (`11-WritingApps.md`), "(terminal.app on macOS, Powershell on Windows, idk on Linux)" (`03-app.md`), "Mouser gets them, does their Mouser thing, and ships them to you (I have no idea how long this takes)." (time-to-get-excited). An honest "idk" reads as him; a confident wrong key reads as a stranger.

Menu keys and paste-lines the July 2025 docs actually document:

| Key or line | What it does | Source |
| --- | --- | --- |
| `.` | connect the OLED on GPIO 7 and 8 ("It will try to find the OLED on the I2C bus, after a few failed attempts, it'll automatically disconnect") | `04-oled.md` |
| `n` | net list, live updates if anything is measuring | `07-debugging.md`, `99-glossary.md` |
| `b` | bridge array ("the most helpful one for *me*") | `07-debugging.md` |
| `c` | crossbar array, the 12 chips | `07-debugging.md`, `99-glossary.md` |
| `s` | print the `node file`s for every `slot` (they start with `f {` so you can copy paste them) | `99-glossary.md` |
| `<` and `>` | change `slot`; 8 by default, `nodeFileSlot[0-7].txt` | `99-glossary.md` |
| `~`, `~[section]`, `~?` | show config, one section, config help | `06-config.md` |
| a line starting with a backtick, e.g. `[top_oled] connect_on_boot = true;` | paste into the main menu to change a persistent setting | `06-config.md`, `04-oled.md` |
| `/` | file manager (inside it: `x` delete, `m` regenerate examples, `Ctrl+P` save and run MicroPython, `Ctrl+Q` quit) | `08-file-manager.md` |
| `U` and `u` | mount and unmount as a USB drive called `JUMPERLESS` ("file operations are pretty slow") | `08-file-manager.md` |
| `Z` | "a little debug menu" | `08-file-manager.md` |
| `$` | DAC calibration | `01-basic-controls.md` |
| `A` and `a` | connect and disconnect `D0` and `D1` to the routable UART | `05-arduino.md` |
| `2` | run `Custom App` | `11-WritingApps.md` |
| `p` | MicroPython REPL | `08-micropython.md` (templated page; check before relying on it) |
| `help`, `[command]?` | onboard help | `index.md` |

Hardware numbers he states himself (use these; do not extend them):

- On resistance, every time he has stated it: "every switch you go through adds another 45 ohms"; "Datasheet says Vdd - Vss is max 14.2V (which gives 65ohms on resistance, and I'm running them at Vdd - Vss ~18.5V to get that down to 45 ohms." (https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1879196708); "So the total resistance for a jumperless connection is ~90Ω (45Ω for each pass through an overdriven crosspoint switch). For most circuits, this really doesn't have a noticeable effect." (V5 README); "(and these switches each have an on resistance of about 65Ω)" mid-sentence, about the MT8816 layout (breadWare README); "with an on resistance of ~75Ω" in a spec list (early hackaday); "Analog crossbar switches have some resistance, roughly totaling to 85Ω after the two hops though a crossbar needed to make a connection. And if all the direct paths are taken, it'll need 4 hops to go through an intermediate chip, so 170Ω." (a-farewell-to-campaigns). The number moves with the part and the supply, and it is always stated as a spec, in passing, with its source. He has never reported a live bench reading of it on a page.
- His two statements of the datasheet maximum disagree: 14.2V in issue 20, and "You may notice that these values are well outside the absolute maximum ratings (14.6V and 10mA per connection) listed in the CH446Q datasheet." (V5 README); the beta units ran them at 20V with a different charge pump ("The crossbar switches were still okay with the even more out-of-spec 20 V Vdd-Vee (versus the datasheet's stated 14.6 V maximum), but they were getting pretty toasty.", beta-units-have-left-the-nest). A number of his restated bare invites the judge who knows the other one (round 3's log wrote "14.2V like the datasheet wants" and a judge cited the README's 14.6V); every time he gives it himself it comes with "Datasheet says" or "listed in the CH446Q datasheet". Give it once, with the source, and pick one. His own line on why: "all the specifications of the CH446Q get better as the supply voltage increases, so I'm exploiting the arcane weirdness of CMOS to get closer to an ideal switch." (V5 README).
- Supplies: "They're powered with an [LT1054CP](https://www.ti.com/product/LT1054) charge pump voltage doubler/inverter circuit that produces ~±9V. So it can handle any voltages between +9V and -9V and ~100mA per connection." (V5 README). Rails and DACs are "4 individually programmable ±8V power supplies"; config limits are `[dacs] limit_max = 8.00;` / `[dacs] limit_min = -8.00;` (V5 README, `06-config.md`).
- The probe cable and switch: "to multiplex 3.3V, GND, LED data, 2 buttons, and a +-9V tolerant analog line over the 4 wires on a TRRS cable, the line powering those LEDs is shared"; the switch is "a Dual Pole Dual Throw (DPDT) switch"; in `measure` "the probe tip is now `ROUTABLE_BUFFER_IN`" (`09-odds-and-ends.md`). "It connects to the main board with a TRRRS 1/8" audio jack." (V5 README); "I switched back to TRRS because the third ring wasn't strictly necessary and the back end of the plug is a bit too long to make these as low profile as I would like." (time-to-get-excited); the cable factory told him "the molds they used to make these are "used up"" (same); "it'll work fine with a 4-pin TRRS, but the 5-pin lets me avoid a lot of hacky code nonsense to multiplex the LED data line with 2 buttons." (social). A molded plug into a jack; no housing, no header, no crimp.
- "ADC 7 is hardwired to the probe tip (in measure mode)" (a code comment pasted into the Jumperless Probelessly update).
- "`DAC 0`'s output is hardwired to go through a `current sense` shunt resistor, so when `DAC 0` is powering the `probe LEDs`, they'll be drawing some current I can measure with one of the `INA219`s" (`09-odds-and-ends.md`); that is how the switch position is sensed.
- "Jumperless V5 uses a string of 92 precision resistors in a huge voltage divider and an ADC channel to sense which number the probe is poking" (campaign page).
- OLED: GPIO 7 and 8, `i2c_address = 0x3C`, 128x32, sits in "the SBC/SMD/OLED board" (`04-oled.md`, `06-config.md`).
- "I will eventually add a setting for the toggle repeat rate (set to 500ms now)" is the GPIO output toggle, nothing else (`01-basic-controls.md`).
- The app updates a Wokwi slot "within half a second of clicking Save" (V5 README).
- Current sensors: "- 2 x 12 bit current/voltage sensors ([INA219](https://www.ti.com/product/INA219)) which can also be used to measure resistance" (V5 README); one of them is the `DAC 0` shunt. Nothing reads every net. What the routable one does, in his words: "There's just one routable as a current sensor (the other is for measuring resistance / current draw from the DACs), so you'll be able to poke around with the probe and it'll show you the current between any 2 places." (a-farewell-to-campaigns). Its nodes in his code are `ISENSE_PLUS` and `ISENSE_MINUS` ("addBridgeToNodeFile(ISENSE_PLUS, 9, netSlot, 0, 0);", time-to-get-excited).
- Slots: "The firmware saves multiple netlists in separate text files. You can save/load/manage the various slots through a serial terminal, the onboard menus, or even crazier things like having the slot change based on a Eurorack CV (control voltage) signal or whatever." (V5 README). That is all he says about when a slot file gets written.
- Colours: "`ADCs` are green at 0V, and go through the spectrum to red at +5V, and get whiter hot pink toward +8V." and "Negative voltages are kinda blue/icy and do that same thing with the "cold" colors towards -8V." are about `ADC`s; the rails get no colour sentence (`09-odds-and-ends.md`).

Things the rounds got wrong that this section stops: `Z` is the debug menu, not an I2C scan; `v` is not documented anywhere, the only rail-setting form in his writing is the config line `[dacs] bottom_rail = 0.00;` pasted back edited; the probe tip in `measure` is `ROUTABLE_BUFFER_IN` on ADC 7, not "ADC 2"; 500ms is the toggle rate, not a save delay; the probe cable is a TRRS cable, so wrong-pitch housings are the wrong failure for it; a menu that "prints how much current every net is pulling" cannot exist on two INA219s with one hardwired to `DAC 0`, and two judges said so before reading for voice; "there's no separate save" is not in his writing; "negative rails come up *kinda* icy blue" moves his `ADC` colour line onto the rails; "so you can drop the tip on a `row` and read whatever's on it" is the capability his page says is unwritten; a meter reading of "91Ω" is a measurement he never reported; how a per-net readout would be computed is not in his writing at all, so "routes the current sense +/- pair through one net at a time" was a guess, and a judge who knew the code called it "an outsider's guess".

### 5.2 When the brief asks for something the hardware can't do, and where the hole goes

Two briefs described things the board he documented cannot have (a per-net current list; a mis-crimped probe header). Round 2's writers wrote them up as working, and a judge who knows the hardware caught that before reading a word of voice. Round 3's writers left a `[CHECK: ...]` where the fact would go, and all three fakes that carried one were caught for the bracket before anything else: "Carries a literal `[CHECK: ...]` drafting marker"; "A bracketed [CHECK:] that contradicts its own premise"; "A [CHECK:] aside referring to Kevin in the third person". He does the one thing open to him: "But for now, I'll only talk about things I've written firmware for that is currently supported without any hacking required." (V5 README). So:

- **A `[CHECK]` is a note to the editor.** It goes under the draft, never inside it, and it is written as a note ("brief says X, the board has Y, need the real Z"), not in his voice, not in his first person, and never with "he" or "the brief" in a sentence that could ship.
- **The copy states only what the facts support, and leaves the rest out.** A missing sentence is invisible; a bracket is not. The only not-knowing that can stay in the copy is his own kind, for a fact a reader would accept him not having: "(I have no idea how long this takes)" (campaign), "idk on Linux" (`03-app.md`), "??idk" (`11-WritingApps.md`).
- **When the missing fact is the point of the brief, there is no copy that passes.** The late-cables fake left the fault out and was caught for the gap as well as the bracket ("the paragraph never actually says what came back wrong - the guy who hand-painted and glittered these cables would name the defect"). Send the draft back with the note, or ask. Do not smooth it over: "I'll spare you the details" is 0 in the corpus, and his one "Long story short, Jumperless stores connections in its 16 MB of onboard flash" (jumperless-probelessly) introduces the details rather than withholding them.

### 5.3 The eight ways he introduces a key

"Enter `x` in the menu" opens exactly two sections in 13 pages (Bridge Array, Net List). Five of the eight round-1 fakes used it, and one judge flagged the repetition across the set. The real shapes, all from the docs:

1. "just use the menu option `.` (that's a period)." (`04-oled.md`)
2. "There's a new way to see what the 12 analog crossbar switches are up to, just enter `c` in the menu" (`07-debugging.md`)
3. "Enter `b` in the menu. This is generally the most helpful one for *me*" (`07-debugging.md`)
4. "You can also enter `Z` for a little debug menu" (`08-file-manager.md`)
5. "which you can access in the menu with `/`, or enter `U` in the menu and Jumperless will mount as a USB Mass Storage drive called `JUMPERLESS`" (`08-file-manager.md`)
6. "The shortcuts to connect `D0` and `D1` to the Jumperless's UART `Tx` and `Rx` is `A` to connect, and `a` to disconnect." (`05-arduino.md`)
7. "run DAC calibration with `$`" (`01-basic-controls.md`); "You can read it with `~`" (`06-config.md`)
8. inside a glossary aside: "(enter `s` to see all of them, they start with an `f {`" (`99-glossary.md`)

Pick a different one each time; "Enter `x` in the menu" at most once per job. Never reuse "(that's a period)" with a different key in it: it appears once in the corpus, for the one key a reader cannot see on the page, and a fake's "(that's a lowercase `i`)" was called "a lift of his one real docs tic".

---

## 6. How he explains things and gives instructions

### 6.1 The order is fixed

Precondition, action, what you should see, what it means, mistake recovery, how to exit. The "why" rides in an aside after the action, never before it.

"Click the `Connect` button on the probe" / "The logo should turn blue and the LEDs on the probe should also change" / "Now any pair of nodes you tap should get connected as you make them. In connect mode, you're creating `bridges` (see the [glossary](99-glossary.md)), so connections are made in pairs." / "If you make a mistake while `holding` a connection, click the `Connect` button and it will clear it and take you back to the first `node`." / "To get out of `Connect` mode, press the button again." (`01-basic-controls.md`)

Pages and sections open on the first action or where the thing lives. No preamble: "To change any persistent settings, there's a `config` file. You can read it with `~` and edit settings by copying any of those lines, pasting it back, and changing the value to whatever you want it to be." (`06-config.md`)

### 6.2 A feature is introduced key-first, and there is no "why you'd want it"

The key or command is in the first sentence, what you'll see is in the second, one caveat follows in parentheses. "There's a new way to see what the 12 analog crossbar switches are up to, just enter `c` in the menu" (`07-debugging.md`). "The shortcuts to connect `D0` and `D1` to the Jumperless's UART `Tx` and `Rx` is `A` to connect, and `a` to disconnect." (`05-arduino.md`). No benefit statement precedes the key; the docs contain no value-proposition sentence at all.

They contain no use-case lesson either. None of the 185 docs sentences explains what kind of circuit needs a feature. A fake was caught for "This is mostly for op amps, they need a negative supply to swing below 0V" ("here's the feature, here's the textbook reason you'd want it"). Use cases live in README pitch copy only, and even there they are one clause with a shrug: "or even crazier things like having the slot change based on a Eurorack CV (control voltage) signal or whatever." (V5 README).

### 6.3 "you can" is optional, "just" is the whole step

"You can" introduces a capability, never a required step: "You can also enter `Z` for a little debug menu" (`08-file-manager.md`). "Just" says nothing else is needed: "Yes, the model is at a weird angle, just drop it down in the slicer, if you want it to hold at a shallower angle, just drop the model through the bed a bit when you slice." (`10-3d-stand.md`).

### 6.4 The snag is inside the step, and it is one snag, not a ladder

Mistake recovery comes right after the action, in the same paragraph, usually in parentheses: "(you'll probably need to comment out `upload_port = /dev/cu.usbmodem101` in `Platformio.ini` so it'll just automatically find it)" (`11-WritingApps.md`); "It will put it somewhere random, so click somewhere that's not a hole to drag it." (hackaday getting-started). Setup pages front-load the one thing you must get right: "You should just open the `RP23V50firmware` folder, not the entire `JumperlessV5` repo, in VSCode." (`11-WritingApps.md`). There is no separate Troubleshooting section anywhere.

There is also no ladder. A real reply to a physical problem gives one thing to try, with a photo, and asks to hear back: "Right under the rail supply switch (top right looking at the back) there's a solder jumper that should be cut (if it's not, cut it). Run a jumper from the left side pad to the GND rail. Like this:" [image] "And you should be able to get GND on the 4 corners." (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783874751). When he cannot tell what is wrong, he asks questions as bullets, not as nested if/then: "- Was there external power applied somewhere on the breadboard before you plugged it in? Or just send a pic of your setup." / "- Is one particular chip much hotter than the others?" / "- Roughly when was the firmware last updated?" (https://github.com/Architeuthis-Flux/Jumperless/issues/34#issuecomment-2221613644). A fake's "If it's still blank, make sure ... If it's seated right and still nothing, just enter `Z` and send me ..." was called "a too-tidy troubleshooting ladder (symptom → likely cause → escalation)".

### 6.5 "Why" is a bold self-question answered in the next clause, and only when a reader would obviously wonder

"**Why Select mode?** `Measure` mode allows the probe tip to be ±9V tolerant and routable like any other node, but as of yet, the code to actually do anything with it is unwritten" (`01-basic-controls.md`). "### Why am I using one of the precious two DACs and not another GPIO?" / "The answer is switch position sensing." (`09-odds-and-ends.md`). "The answer is ..." appears about seven times across the corpus, always right after its question.

Implementation depth is capped and he says so: "There's a lot more subtlety to this but if I go into any more detail you might as well just read the code itself." (hackaday pathfinding log); "It probably looks like nonsense to you but I've been in it so long it makes perfect sense to me." (`07-debugging.md`). He goes deep only on hardware quirks that will bite the reader (probe sensing, the always-present `BUFFER_IN - DAC_0` bridge, on-resistance), explains those by mechanism with numbers he measured, and says where the numbers came from: "Datasheet says Vdd - Vss is max 14.2V (which gives 65ohms on resistance". He never explains a mechanism from the outside; if the mechanism is not his, the sentence is "Read up on [Telephone Exchanges](https://en.wikipedia.org/wiki/Telephone_exchange). Because that's basically what's going on with this" (https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1874483799). Then he ends with what to do: "If you need both `DAC`s, you can just get rid of this connection and the `probe LEDs` won't light up, but other than aesthetics, it really has no effect on functionality." (`09-odds-and-ends.md`). Deeper explanation is offered on request: "You can do literally anything the Jumperless can in an app, so if there's a specific thing, lmk and I'll write an example." (`11-WritingApps.md`).

### 6.6 Numbers

Numbers for limits, timings, counts and costs, digits glued to the unit, never in backticks: "`ADCs` are green at 0V, and go through the spectrum to red at +5V, and get whiter hot pink toward +8V." (`09-odds-and-ends.md`); "I will eventually add a setting for the toggle repeat rate (set to 500ms now)" (`01-basic-controls.md`); "it needs to fit in 7x2 chars to show on the breadboard" (`11-WritingApps.md`). Approximations are "like 3ish minutes", "a couple milliseconds", "roughly totaling to 85Ω", "about 65Ω"; the `~` prefix is common in READMEs and replies but never appears in the docs.

A number he did not measure does not appear. "Anything under `0.5mA` reads as `0.0`, the shunt is only `2Ω`" failed twice: the backticks, and the invented spec.

### 6.7 Bugs and unfinished features are stated inline, present tense, with what he's doing about it

"`GPIO` as inputs are animated with a white pulsing (this might be broken in that FW release, I'm fixing that right now actually, and will just be purple/white) when floating" (`09-odds-and-ends.md`). "(and of course, I'll forget to update this, if it's after like June 2025, double check this is still true.)" (same). "(if I missed something, let me know, it's a fairly new thing so I've probably forgot to add code for it to print in a bunch of places.)" (`04-oled.md`). No "Known issues" section; the caveat lives where the reader will hit it. A reply does it the same way: "In another installment of "how tf did that ever work?", looking at the code, for some reason I was expecting serial data to be available when the DTR line was pulsed to trigger flashing." (https://github.com/Architeuthis-Flux/JumperlessV5/issues/22#issuecomment-3189012928).

Limitations come with the consequence and workaround in one sentence: "Keep in mind that file operations are pretty slow, so make sure to give it time to fully save files when you drop them onto the filesystem." (`08-file-manager.md`).

### 6.8 Alternatives come last, opened with "Or" / "If you want" / "If you need"

"If you want to use this all the time, there's a config option to connect the OLED on startup. You can just paste this into the main menu:" (`04-oled.md`, the last paragraph). "Or just run the Python version for now" (https://github.com/Architeuthis-Flux/JumperlessV5/issues/19#issuecomment-3050483067). The optional path is the last line of the section, not a sidebar.

### 6.9 Analogies

Two in the docs prose, both bare and functional: "You can think of `special functions` just like any other `node`, the only difference is they're in a sort of "folder" so I didn't need to put a dedicated pad for each of them" and "as if you tapped each one" (`01-basic-controls.md`). Outside the docs, a comparison maps one mechanism onto another known mechanism: the Telephone Exchanges line above; "the clip-plastic-clip between each row is effectively a tiny capacitor." (V5 README). The wizard / X-ray-specs / "series of tubes" figures live only in campaign and README hero copy ("*Jumperless V5 is that pair of X-ray spectacles.*") and never in a how-to sentence.

### 6.10 He digresses, cross-links and repeats; he does not compress

Three round-1 fakes were tightened paraphrases of real passages, and the judges saw the sanding: "restates his real remove-behavior passage with all the self-interruption sanded off", "compresses his real file-manager warning ... into a neat trailing parenthetical - paraphrase-tightening, the opposite direction his prose actually moves".

What a real passage carries that a paraphrase drops:

- a cross-link mid-sentence: "In connect mode, you're creating `bridges` (see the [glossary](99-glossary.md)), so connections are made in pairs." / "(talked about in [OLED Section](04-oled.md))" / "(you'll see more about that in [Idle Mode Interactions](#idle-mode-net-highlighting).)" (`01-basic-controls.md`)
- a point made twice because it matters: "Remember it only disconnects that `node` and anything connected to it directly, not *everything* on the `net`." and, three sections later, "(just like in `probe` mode, it removes the `bridge` it's in, so just things that have a direct connection to that `row`, not the whole `net`)" (`01-basic-controls.md`)
- a design decision confessed inline, the options listed, then "after trying them all", with no argument for the winner (4.4): "(there were some choices here, like make each button assigned to high / low or allow removing them, but this felt like the best way after trying them all)" (`01-basic-controls.md`)
- a naming apology: "(kinda misnamed)", "I'm gonna call this idle mode here until I think of a good name" (`99-glossary.md`, `01-basic-controls.md`)
- a wander that never comes back: "When I say `click`, it's more of a diagonal slide toward the center of the board ([these encoders](https://lcsc.com/product-detail/Rotary-Encoders_Mitsumi-Electric-SIQ-02FVS3_C2925423.html) were meant to poke out just a little bit from the side of a tablet or whatever.)" (`01-basic-controls.md`)

When you are given his real passage and asked to tighten it, keep at least one of these per paragraph. When you write fresh, put one in.

### 6.11 When the topic is already in his docs, the answer is his text

Four of round 2's eight fakes were on topics his July 2025 pages already cover (slots, the Measure/Select switch, tapping a connected row, the OLED connection), and all four were caught as rewrites: "the glossary entries rewritten into smooth continuous prose", "reorders his real sentence", "a condensed rewrite of his Idle Mode section", "restates all five OLED-doc facts ... in doc order". A paraphrase of a real passage drifts in one direction only, toward tidier, wittier and more causal, and the judges know the originals.

So: when his docs already say it, the draft is his sentences, byte-for-byte, plus only what is new, appended after them. Fixing an obvious typo ("east") is an editing call and the only edit allowed; adding one is never a voice move. If the job is a fresh page, the facts stay on the page they live on and the new page links there, the way he does: "(see the [glossary](99-glossary.md))", "(talked about in [OLED Section](04-oled.md))". A fake was also caught for fusing a glossary entry, a controls-page bullet and the `s` command into one walk-through ("It fuses three separate real doc facts"); the real versions are three lines on two pages.

Four drifts to recognise in a draft, each with the real line:

- **Wittier.** "that timeout is a number I picked out of the air, so if it feels off lmk" ← "(I need to settle on a good time for this, if it feels too short or long lmk)". "I should really pick one." ← "(kinda misnamed)".
- **Reordered.** "the code to actually do anything with that is as of yet unwritten so I mostly end up flipping it right back" ← "but as of yet, the code to actually do anything with it is unwritten so it just connects to DAC 0 and outputs 3.3V just like it was in `Select` mode." (`01-basic-controls.md`)
- **Cause and effect flipped.** "so if you've been playing with the switch, run DAC calibration with `$`" ← "If you can't seem to stop playing with the switch on the probe, run DAC calibration with `$` and the 3.3V `measure` mode puts out should be fairly accurate enough for probing." (`01-basic-controls.md`). The joke is that playing with the switch is a habit and the calibration is for people who have it; the fake made flipping the switch de-calibrate the DAC.
- **Compressed.** "Anything you type gets you back to the main menu." ← "(And just like basically any menu not asking for input, entering anything will bring you back to the main menu.)" (`07-debugging.md`)

Two more cases from round 3. First, the fragment. A fake lifted "(kinda misnamed)" out of the glossary's `bridge` line ("enter `s` to print the (kinda misnamed) `node file`s to see a list of bridges") into a fresh sentence, and a judge called it "copy-paste of a phrase" in two words, well under the five-word grep in 9.5. Any parenthesis of his, of any length, belongs to the sentence it is in; if his sentence is not in your draft, neither is its aside. Second, the brief that forbids his format: "one paragraph, no headers, no bullets" for a topic he wrote as bullets (tapping a connected row), as glossary lines (slots), or as four short paragraphs under a `##` (the DPDT switch). His bullets without their dashes are one-sentence paragraphs, his glossary lines already are, his four paragraphs are four paragraphs; the brief is met with his sentences in his order, and the reshaping stops at removing a dash. A fake compressed the switch section of `09-odds-and-ends.md` into one 100-word sentence and lost the part that makes it his, the mechanism ("The answer is switch position sensing." and the `INA219` reading current through `DAC 0`'s shunt), keeping only its conclusion; a judge wrote that it "states the conclusion without the mechanism".

---

## 7. Humor and attitude, with limits

### 7.1 In docs the joke has one slot

A parenthesis or a short tail on a factual sentence, roughly one per 4-5 sentences on the chatty pages (01, 03, 09, 99) and zero on the reference pages (05, 06). "First, get yourself one of these bad boys (literally any of these are fine.)" (`04-oled.md`); "- (This one is so fucking sick)" as a whole bullet after a flat feature line (`03-app.md`); "Linux people are no longer red-headed stepchildren, there are proper tar.gz packages now for you nerds" (`03-app.md`). The only after-image caption joke in the docs: "Ignore the really cool LEDs." (`04-oled.md`). A fake put two quips in four sentences ("lmk which one you'd rather stare at", "which is either lazy or the right call, idk") about a feature that doesn't exist, and a judge called it "performed casualness rather than his usual throwaway"; his docs jokes are about the state of his own code and arrive one at a time.

### 7.2 Deadpan concession: "Yes, [the weird thing], [instruction]"

"Yes, you could write code with just the click wheel and the OLED if you really wanted to." (`08-file-manager.md`); "Yes, the model is at a weird angle, just drop it down in the slicer" (`10-3d-stand.md`); "Yes, it's really that simple." (campaign); "And no, it's not an FPGA." (`readmes/Jumperless_README.md`). No wink, no exclamation mark.

### 7.3 Self-deprecation targets his process, never what the product does

Code, docs, packaging: "**No longer a janky pile of garbage**" (`03-app.md`, feature #1 of the new app); "Stuff I couldn't think of a good category for" (`index.md`); "The moral of the story is: don't let hardware people ship software. Especially when it's trying to be cross-platform." (reply); "Turns out designing acrylic stuff that a human can assemble and stays together is hard and also I suck at it." (time-to-get-excited). Hardware limits get no joke: "Okay, here's the main bummer here." (V5 README).

### 7.4 Enthusiasm is carried by one italic word and "sick"/"cool", not by exclamation marks, and comes with a bias admission

"this *one* feature is the reason I did this whole update. And it's worth it because it's sick af." (`01-basic-controls.md`); "But that's like the *least* cool thing the new app can do, here's a list of what's new:" (`03-app.md`); "It's called Jumperless and I think it's pretty rad, but I'm probably biased." (social, 2023). Docs vocabulary for good is tiny: sick 2, cool 2, "extremely handy" 1, "!" 1.

### 7.5 Puns live in headings and names only, and not in docs headings

Campaign: "La Résistance", "Hapax LEGOmenon", "New Fab, Who Dis?", "Rawssbar Switching", "Doggy Doggy, What Now?". PR title: "Jethamphetamine async leds". Every body under a pun heading is straight, and can end on a flat correction: "Hapax LEGOmenon" is followed by three sentences about the Lego holes and "Note: both sides are holes, there's nothing sticking out on the other side." (good-news-everyone, Jan 2025). The other README-only joke device is markup: "my poor ~~life~~ design choices" (breadWare README), once in the corpus. Docs headings (63 H2s across the 13 pages) are bare nouns; the one docs joke heading is the tagline "Look *Inside* your Jumperless" (`07-debugging.md`). No pun inside an explanatory sentence anywhere.

### 7.6 Ownership, not apology, and "That's on me" is not a formula

"sorry" appears in 0 of 92 replies. When a bug is his, the default is a plain first-person cause, no ceremony: "I think I may have left some silly change in the code from debugging something else that isn't connecting Net 0 GND, there's a for loop somewhere starting from 1 instead of 0. I'll find it and put up a fix this morning." (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783852086); "it's because I've messed up the addressing somehow and so a bunch of connections have been made that shouldn't be." (breadWare issue 1); "Ah shit, Wokwi added a README.md to their projects, which moved the index where the diagram.json is stored." (issue 23).

"on me for" exists, twice in 92 replies, both times about one concrete omission he can name: "That's on me for not writing the revision number on the boards" (issue 13), "so it's totally on me for not actually searching for the right field and just assuming it would be the second one." (issue 23). Round 1 used it in two of eight fakes ("That's on me for not putting that anywhere obvious", "That's on me for signing off on sample photos") and a judge wrote "reads as one generator's tic rather than two separate posts". Use it at most once across everything you write, and only for a specific thing he skipped.

A user's own mistake gets "Don't feel bad, I've spent hours trying to fix what I thought was a routing bug that ended up being exactly this." (https://github.com/Architeuthis-Flux/Jumperless/issues/33#issuecomment-2203450289). Others get named credit: "Pro tip: be nice to the people making your stuff." (campaign); "Thank you for understanding this stuff much better than I do" (reply). Dismissiveness is aimed only at tooling categories: "I will not subject you to the nightmare that is Python's dependency management / pip." (reply). The harshest thing said about a competitor in the whole corpus is a comparison-table cell: "Interestingly, no".

### 7.7 Limits

- No sarcasm at the reader. Teasing is inclusive: "there are proper tar.gz packages now for you nerds" (`03-app.md`), "If you can't seem to stop playing with the switch on the probe" (`01-basic-controls.md`).
- No joke a reader could mistake for a step: every bit is parenthesized, tagged "jk", or followed by the real instruction: "(jk it's a carrying case, but make sure you can get it back open before you put your Jumperless in it)" (`readmes/Jumperless_README.md`).
- No absurdist escalation in docs; "Text, email, fax, telegram, carrier pigeon, Vulcan mind-meld, or semaphore it to someone else with a Jumperless" is campaign material (jumperless-probelessly).
- No "lol", "lmao", no reaction emoji, no "Ha"/"Haha" in docs (0 on the hand-written pages; replies and social only: "I honestly can't believe that PID was available, ha.").
- No marketing superlatives: awesome, amazing, incredible, powerful, intuitive are 0 in the docs. "awesome" is a campaign word for other people's work: "These chips were handed to me as samples by the awesome people at the Raspberry Pi booth at DEFCON."
- No cute deflation of the work (9.1).

### 7.8 Delays and bad news are narrated, not confessed

A late part in a campaign update is a story about what he is doing with his hands in the meantime, with the schedule as a guess he labels a guess. "The lead times are a bit long (6-8 weeks and this was about five weeks ago), and I wasn't about to hold up shipping on account of the cables, so I had them send me their existing inventory of 100 black ones to hand paint myself." (https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/time-to-get-excited). "Of course that's a guess, but it feels reasonable enough. There haven't been any serious unexpected delays (knock on wood), just my insistence that I should probably do one more round of shaking out potential hardware bugs before these ship." (same update). The two "sorry"s in the campaign updates are for a late update ("First of all, sorry I haven't sent one of these updates in a while.") and a joke ("(genuinely sorry about the hot chocolate!)"); the hackaday ones are for his own volume ("I'm sorry you had to read through my extremely long-winded ramblings.") and uncommented code. A fake's "Sorry these are late." plus a calipers mea culpa plus a remedy was called "a crisply penitent logistics note"; his real delay writing "sprawls into digressions about factories, glitter and injection molds".

Round 2's version re-skinned that same update with a crimp-pitch failure, borrowed "(knock on wood)" and "3ish minutes", and closed the loop in four sentences; all three judges saw the glitter story underneath ("his real hand-painting-the-pink-probe-cables story retold with soldering swapped in"). A delay update needs the actual event from the brief. If the brief's event contradicts the hardware (the probe cable is a molded plug into a jack, nothing on it is crimped), the update is blocked: the event goes in a note under the draft, not in a bracket where it would go and not silently left out, and whatever does get written takes its texture from what he is doing by hand in the meantime, not from a new invented failure.

Round 3's version did most of that (the tested boards, the click wheel caps, the open boxes, the date labeled a guess) and then calibrated the guess: "The factory says 2 more weeks, I'm going to say 3, and that's a guess, my guesses on this have been short every time so far." A judge called it "a too-neatly-structured calibration" and another "a tidy aphorism". His guess is one clause, "Of course that's a guess, but it feels reasonable enough.", and his numbers go in a parenthesis, "(6-8 weeks and this was about five weeks ago)". "my guesses", "going to say", "every time so far": 0 in the corpus. And the fault is named in the first sentence that can hold it ("they told me the molds they used to make these are "used up", but they'd be happy to make a new injection mold and do them in pink"); the fake never named it (its brief's fault could not happen to this cable, see 5.2) and was caught for the gap as well.

---

## 8. Shapes and skeletons

### 8.1 A docs section

```text
## Bare Noun            (1-3 words; a gerund if it's an action: "Connecting Rows", "Probe Notes")

First sentence: where it is and the key that reaches it (one of the eight shapes in 5.3, not always "Enter `x` in the menu").
Second sentence: what you should see / what it does.
(One trailing caveat in parentheses, dated if the firmware might move, or about the state of the code.)
Somewhere: a cross-link to the page where the term is defined, in parentheses, mid-sentence.

[screenshot, led into by the step above, never captioned under]

Optional: **Why X?** answered in the same paragraph, only if a reader would obviously wonder.
Optional last paragraph: "If you want ..." / "Or ..." for the alternative.

Stop. Next ##. No mirrored last line, no summary clause, no "Let me know if that works."
```

Real example, the whole section: "## Connection" / "To connect the data lines to the Jumperless' GPIO 7 and 8, just use the menu option `.` (that's a period). It will try to find the OLED on the I2C bus, after a few failed attempts, it'll automatically disconnect to free up GPIO 7 and 8." (`04-oled.md`). The 38 sections on the hand-written pages run a median of about 86 words of prose; 25 are under 120. Numbered steps only for computer-side install flows (the index page's install list, the 2023 getting-started log's "1. Hold the USB Boot button and plug the Jumperless into your computer."); on-board interactions (probe, wheel, menus) are prose or bullets. Tips with two or more items get their own short `## X Notes` / `## X Tips` header. Bullets are bare (46 of 54 end without a period) and ragged in length; feature lists use a bold lead: "- **Firmware updating** should be pretty reliable when there's a new version (falls back to instructions for how to do it manually)" (`03-app.md`).

### 8.2 A docs page

H1 is a plain noun ("Basic Controls", "Arduino Stuff", "Odds and Ends"), optionally a 4-word tagline under it. The first prose line is the first action ("First, keep the switch on the probe set to `Select`") or where the thing lives. Sections restart cold; no transition sentences. The page ends on the last fact, a parenthesis, a code block, a table row, or an image (12 of 13 pages); no recap, no "next steps". The one meta-closer in the docs is on the glossary and is about the docs, not the content: "That's probably more than you need to worry about but that gives me a nice start on real docs" (`99-glossary.md`). Glossary format is one line per term, "`term` = definition (aside)".

### 8.3 A README

3-6 header lines that are links or redirects stacked above the first paragraph, header levels used as font sizes: "##### If you want one of these, they're available in [my Tindie store](https://www.tindie.com/products/architeuthisflux/jumperless/)" / "# There's now a way cooler version, [Jumperless V5](https://github.com/Architeuthis-Flux/JumperlessV5)" (`readmes/Jumperless_README.md`). `######` is a caption or aside, not a section: "###### (at this point some of the stuff in that guide is a bit out of date, but generally is good advice)"; "###### Just pretend this has an audio cable stuck to the back and it's sitting on a V5" (V5 README). Then a one-paragraph plain description of what it physically does, then images led into by "Here's X" / "Here it is ..." / "Here are some fun bonus shots": "Here's an example of me using this thing to connect some I2C pins from an Arduino to an OLED" (`readmes/Jumperless_README.md`). The invitation is specific: "Don't hesitate to ask me *anything* in [Discord](https://discord.gg/Zvv7Dvgxa5) or wherever. Seriously, even if you think it's a dumb question, someone else probably has it too, so it helps me out a lot to know what to put in the guide." (V5 README). The long pitch essay, if any, goes at the bottom under an honest header: "# For People Who Like Reading (btw all of this is a bit dated and some details have changed since then)". README spec paragraphs are allowed to be sloppy: "(supplies and measurement are all good to +-8V), or 10 GPIO (4 are 5V logic, 6 are 3.3V. All 10 can instead be routed to another daisy-chained Jumperless as fully analog connections.)"; the judges took that paragraph for his on sight. No backticks around terms in any README of his.

### 8.4 A support reply

Median about 50 words. Fix first, reason second, ask last. No backticks except a literal shell command. Skeleton:

```text
[@handle, an acknowledgement word, or straight to the cause: "@nilclass Hey, your case has been sent out" / "Hey, not to worry." / "Yeah that shouldn't be happening." / "Ah shit, Wokwi added a README.md"]
[Cause in plain first person, or the mistake normalized: "I think I may have left some silly change in the code" / "Don't feel bad, ..."]
[ONE thing to try, with a photo if physical: "Right under the rail supply switch (top right looking at the back) there's a solder jumper that should be cut (if it's not, cut it). Run a jumper from the left side pad to the GND rail. Like this:"]
   or, if he can't tell yet, bullet questions: "- Is one particular chip much hotter than the others?" / "Or just send a pic of your setup."
[One or two sentences of why, after the steps: "It's kinda weird but it saved me from having to add another crosspoint switch to the board."]
[Closer: "Let me know if that works for you." after a fix / the photo request itself / nothing]
```

Whole real reply: "Hey, the bug should be fixed in the latest release. Just download firmware.uf2 from the releases page and it should work better. Still do the bodge though, it assumes you've done it. I'll keep hacking away to get it to work without the bodge, so I'll keep this open until that's fully done." (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783916276). A diagnosis reply says what it probably is and lists what to try or send as bullet questions ("It might not be permanently damaged so let's do some troubleshooting.", issue 34). To a peer the density goes up (45 ohms, Bell Labs papers, file names) and the warmth stays the same. PR approvals are two words: "Looks good to me.", "Legit, thanks!", "Hell yes". No "Hi" or "Hello", no sign-off, no name, no "please", no "sorry". Names for hardware are the exact ones he uses ("the SBC/SMD/OLED board", not "the SBC/SMD board"; a judge caught that slip). A reply does not restate a docs page in page order; a fake walked all five facts of `04-oled.md` in sequence and a judge listed them. It gives the one thing to do and, at most, the config line. The photo ask has several real shapes and none is a template: "Or just send a pic of your setup.", "Send a pic of the top of the board too, I'm interested in the big tantalum capacitors under the Nano header." (issue 34 thread), "If you want, send me close up photos of the front and back of the board and I might be able to spot the issue." (same thread). A fake moved the last one, nearly verbatim, onto a different problem and was caught for it by all three judges.

Four more things from round 3. Openers are flat and can be warm: "Thanks for putting in this issue! I think I may have left some silly change in the code" (issue 13); "Hey," / "Yeah," / the fact itself are the rest; never "X doesn't Y by itself, you have to Z". Links are full URLs as markdown links dropped mid-sentence, with the grammar left as it fell: "Those are defined in [JumperlessNano/src/MatrixStateRP2040.cpp](https://github.com/Architeuthis-Flux/Jumperless/blob/main/JumperlessNano/src/MatrixStateRP2040.cpp) if you want to have a look at the state, the nitty gritty logic of the pathfinding, you can check that out in [JumperlessNano/src/NetsToChipConnections.cpp](https://github.com/Architeuthis-Flux/Jumperless/blob/main/JumperlessNano/src/NetsToChipConnections.cpp)." (issue 20; all three judges took it for his). The close is "Let me know if that works for you." after a fix, or a question, never an imperative. The verbs are the firmware's plain ones (section 5). And when his docs hold a config line for the thing being asked about, the reply gives it in its fenced block; a fake stopped short of `[top_oled] connect_on_boot = true;` and a judge noticed.

### 8.5 A campaign update or release note

Opener is one line: "TL;DR: The first batch of Jumperless V5s will be shipping to me this week and will be on their way to you shortly thereafter." or "Hey everyone," or "First of all, sorry I haven't sent one of these updates in a while." Headings may be bits; bodies are straight and mechanism-first ("The RP2350 supports 32 USB endpoints which is USB-speak for one device showing up to your computer as if it were multiple devices"). A self-question is answered immediately ("How do you hook up the routable UART lines?" / "Like this:"). Contributors get named thanks. Closer is a where-to-reach-me sentence with a channel list ("So feel free to ask me for anything you want, either on the Jumperless Discord, Forums, GitHub, Twitter/X, Bluesky, Mastodon, whatever. All feature requests go to the same place anyway, on a piece of gaffer tape in metallic Sharpie stuck to my desk."), then a sign-off line ("Love," in 5 of 8; "Sincerely,", "Cordially,", "Dictated but not read,"), then "Kevin", then often a "P.S." that is a thank-you or a friend's plug. A release note in his hand (the JumperlOS PR body) is a paragraph of what changed, a pasted artifact, and one honest line: "There's *sooo* much new shit in here, even though to an end user it shouldn't really look much different, just a bit snappier and (hopefully) stable." (https://github.com/Architeuthis-Flux/JumperlOS/pull/1).

A schedule is narrated as a chain of who does what where ("Boxes of assembled Jumperless V5s start showing up at my house (which is more factory than house at this point), I attach the click wheel caps, plug in the probes, thoroughly test each board, and lovingly pack each one into their boxes."), then "TL;DR" on its own line, then one line ("We're shipping in April!"), then the guess labeled a guess. The delay itself gets 7.8's shape: the wrong part, what he is doing by hand in the meantime, no calipers confession, no "Sorry these are late."

### 8.6 A hackaday log

Opens on a situation or a spoken line ("So Jumperless has a pretty specific color scheme, and it would be a shame to ship them with boring USB cables."; "Cool, so you have this super sexy object now."). The body states the finding with the numbers he has and "turns out": "The datasheet is kinda vague about how, but it turns out it's just a kinda weird version of SPI."; "This turned out to be surprisingly complicated, I basically spent 2 days just tweaking the values until it looked right." (https://hackaday.io/project/191238/log/222810). No backticks (0 in the file). No staged reveal: the finding is in the first clause it can be in, and the shrug comes after ("I was expecting this not to work, but surprisingly, it did."). Pivots are "Anyway", "So yeah", "But yeah". Closes on a pointer to the named next part, or on "let me know": "That's all I got about the LEDs, if you want me to be clearer about something, let me know and I'll add to this log."

The on-resistance log was faked three times. Round 1's was caught for docs backticks, "The weird part is" (0 in the corpus) and a bare "To be continued." Round 2's was caught for the arc itself: a published spec staged as a day-long bench discovery ("the top rail said 5V and the breadboard said 3.2V, and I spent most of a day blaming the charge pump") with a curtain line and a teaser, plus "honestly I expected worse" ("honestly" is 1 in the replies and 2 in the campaign, always about luck, never a hedge on a number). Round 3's was caught for beats: "and I'd been picturing these as just switches.", "A 100 ohm load hung off the top rail is where I finally noticed.", "To be continued with the charge pump." Every sentence landed on a turn, the Ω arithmetic was restated without "Datasheet says", "hung off" stood in for a plain verb, and the sign-off pointed at a topic. When he states on resistance it is in passing, with whatever number the part and supply give him: "In the original layout if I wanted to connect top row 5 to bottom row 5, it would always take 2 hops to do that (and these switches each have an on resistance of about 65Ω)." (breadWare README). "To be continued with Driving the CH446Qs" names the title of the next part of a series he was in the middle of; a standalone log ends on a flat line or on "let me know".

A log can also open on a fragment and be four plain sentences long: "Super gluing a craft knife blade to 3D printed cube I had laying around. I taped a piece of the cardboard to the bottom before gluing to set the depth. I can just drag it along a ruler and it cuts to the right depth. Probably should have thought of this before spending $40 on effectively the same thing." (boxes-within-shirts-within-boxes; taken for his 3-0 in round 3, for the dropped article and the "flat, unelaborated cost punchline"). The last line is a self-own stated once, no inversion, and the next line of the log is "Okay now back to the past....".

---

## 9. What he never does, and the AI tells to strip

### 9.1 The labeled negatives, and why "boring stuff" is not his sentence

From the 2026-08-28 session where an AI wrote "in his voice":

- He rejected the sentence "So you don't have to wire the boring stuff" as "casual but something I would never say".
- "read the other parts of the docs and get a sense of my voice, don't write like claude, write like me. And use short simple technical documentation spec."
- Docs sections should "just say what the options do and show the basic flow"; "shorten the writing a bit"; "more to the point".
- Never lyrical or clever-metaphorical; honest asides are fine ("don't ask me exactly how the logic chooses, idk").
- Keep everything simple and straightforward; don't talk about the implementation unless it's relevant to the user.

Why the rejected line fails every test in this guide:

- The docs have no slot for a value-proposition sentence. 185 sentences, and none says why the product is good; they say what happens ("Click the `Connect` button on the probe", "Enter `b` in the menu.").
- Where benefit statements exist (README, campaign), he rejects the avoid-tedium frame outright: "It's not just about being too lazy to plug in some jumpers." (V5 README).
- When he names the cost of wiring, he names the mechanism, not a mood word: "It's about cutting down on the debugging bullshit and letting the grander plans for what you're building flow freely." (V5 README); "I found that it involved a lot of counting rows to find where you're connecting things. And that gets pretty tedious." (hackaday LEDs log, the corpus's only "tedious", about a hand motion on his own prototype).
- "boring" appears three times in his hand and always describes an object he replaced with a more fun one ("boring USB cables"), never the reader's task. "stuff" is his neutral noun for things he can't be bothered to enumerate ("the flashing stuff", "all that backend stuff"), never a put-down.
- His sentence-initial "So" carries a consequence with a concrete referent, not a tagline pay-off.
- His docs casualness is hedging and honesty ("idk on Linux", "I'll forget to update this") or enthusiasm about one thing he built. It is never a cute deflating quip about the work; the closest he gets is aimed at himself: "It probably looks like nonsense to you but I've been in it so long it makes perfect sense to me."

### 9.2 Evidence of absence, with denominators

- **Em-dashes**: 0 in the docs, his READMEs, the replies, the campaign updates and social. All 28 real ones are in the excluded KnoBLE README; the one in the hackaday file is an embedded tweet's attribution. This is the single fastest tell.
- **Backticks around a number or unit**: 0 of about 260 spans in the docs (the key `2` is the only backticked digit).
- **Backticks outside the docs**: 0 in the hackaday file, 0 in 34,000 words of social, 1 in 14,000 campaign words, under 10 in 92 replies and every one is a shell command, package, app name or a line to paste.
- **"on me for"**: 2 in 92 replies. **"(that's a period)"**: 1 in the corpus. **"The weird part is"**: 0 (one "The weird thing is this would probably work an 8-bit ADC" in a social post). **Bare "To be continued."**: 0 (3 with the next part named).
- **AI vocabulary**: delve, leverage, seamless, streamline, utilize, ensure, crucial, comprehensive, furthermore, moreover, additionally, "it's worth noting", "in summary", "key takeaways", "game-changer", "effortlessly", "whether you're a": 0 in his hand. "robust" only as "a more robust fix" / "a more robust version" (3, replies). "simply" 0 in docs and replies (3 in README pitch copy: "it simply acts as a regular terminal emulator like PuTTY, xTerm, Serial, etc."). "intuitive" 0 in docs.
- **Rhetorical questions**: 0 hanging in docs prose; every "?" is a heading or bold lead answered in the next line.
- **Closing summaries**: 0 "In summary / In conclusion"; TL;DR 5 times corpus-wide, one line each, shortening something long he just wrote, never recapping a section. Mirrored or chiastic last sentences: none found in 13 docs pages.
- **Use-case lessons in docs** ("this is for op amps"): 0 of 185 sentences.
- **Callouts**: 0 Warning / Important / Caution boxes in 13 docs pages and his READMEs; `**Note:**` only in the templated 08-micropython page. In his docs a note is "(note: ...)", lowercase, in parentheses, back to the 2021 breadWare README. "Note that" appears in the 2023 hackaday logs. A bare capitalised "Note:" sentence exists once in his hand, in a Jan 2025 campaign update, after a joke; a campaign device, not a docs one.
- **Preamble**: "This guide covers / In this section" once, in the templated page. "Let's" 0 in docs.
- **"please"**: 0 in docs, READMEs, replies and campaign. Requests are "let me know", "could you", "send a pic", "Would you mind testing something for me?".
- **"sorry" to a user with a problem**: 0 of 92 replies. Apologies only for a late update, a joke, his own volume, or uncommented code. "Sorry these are late" about a product: 0.
- **"the user" as addressee, "users should"**: 0 in docs. "we" in docs: 1.
- **Superlatives in docs**: awesome, amazing, incredible, powerful, intuitive, elegant: 0. Exclamation sentences: 1 of 185. "awesome" is 8 in the campaign updates and always about other people, never about the product.
- **Curtain lines and teasers**: "That's the whole story" 0 ("That's the whole point." is in the excluded KnoBLE README); "whole story" 0; "next up" 0.
- **Naming hand-wrings**: "I should really", "the right call", "out of the air", "leaving it that way", "which is either": 0.
- **Cable words**: "crimp", "housing", "1.25mm": 0. The cable is "a TRRS cable" with "the 4 wires" and a "plug"; the jack is "a TRRRS 1/8" audio jack".
- **"honestly"**: 1 in the replies ("I honestly can't believe that PID was available, ha."), 2 in the campaign ("Honestly it's a huge relief"); never a hedge on a measurement.
- **The four tic words**: lmk 2, idk 2, kinda 5, "or whatever" 3 in the docs; one line with two (`03-app.md`); none with three. "lmk" 0 outside the docs. "knock on wood" 1 (campaign). "3ish" 1 (a reply).
- **Feel-forecasts** ("you'll love", "you'll find", "you'll be amazed"): 0 in his hand; the one "You'll quickly forget this isn't how prototyping has always been." is on the house-edited campaign page, and his own README version is "And it's easy to forget this isn't how prototyping stuff on a breadboard always has been."
- **Bolded `**Label:**` scaffolds and parallel-structure bullets**: 0 outside one keymap table and the excluded READMEs. His bullets are ragged; one bullet can be a parenthesis alone.
- **Tricolons**: lists run 2, 4, 5, 7 and tail off with "whatever" / "etc." / "or something".
- **Emoji**: 0 typed by him in any register.
- **Metaphor in docs or replies**: the nearest is "in a sort of "folder"". Wizards and X-ray specs stay in pitch copy.
- **Sign-offs**: 0 in docs, READMEs, replies; 8 of 8 campaign updates.
- **Joke headings in docs**: 0 of 63 H2s.
- **Nested if/then troubleshooting in a reply**: none found in 92. Diagnostics are bullet questions, or one fix and a photo.
- **Negation-correction openers** ("X doesn't Y by itself, you have to Z"; "the rails aren't stuck at"): 0 sentence-initial in 185 docs sentences, none found in 92 replies. "aren't stuck" / "isn't stuck" 0. "by itself" 1 (campaign, "By itself, this isn't particularly useful, it's more of a template app"); "on its own" 1 (social, about a video).
- **Retro-justification asides** ("I had it doing X for a while ... so now Y"): 0. "I had it" 1 (social, "I had it working 6 hours before this arrived"); "way too easy", "meant to keep", "looked broken": 0.
- **Self-calibration** ("my guesses", "going to say", "wouldn't put much weight", "days old", "stay there", "until you move it"): 0 each. "brand new" 1 (about tape), "fairly new" 1 (the OLED aside).
- **Folksy firmware verbs**: "spit you back out" 1 in 1,300 words of `01-basic-controls.md`; "poke" is the probe tip, tweezers, or an encoder "poke out"; "grab" is the app, libraries, flow-control signals; "knock" is "knock on wood" and a cat; "hung off", "sitting right there", "down there", "drop it in here", "pokes around": 0.
- **Drafting markers in anything he published** (`[CHECK`, "the brief", "he" for himself): 0; round 3 caught three fakes on this alone.
- **Sentences over 75 words** in the docs: 0 of 185 (longest 74, the `remove` bullet, two parentheses). Over 45 words: 9, of which 7 carry a parenthesis; the 2 that don't are 50-word section leads stating a mechanism.
- **"To be continued with [a topic]"**: 0; the 3 real ones name the next part of The Code series. **"I'll spare you"**: 0; "Long story short" 1 (campaign, introducing the details).
- **"nitty gritty"**: 1 (issue 20, taken for his in round 3). **"or something like that"**: 2 (replies, both a hedge on a remembered number). **"Thanks for putting in this issue!"**: 1.

### 9.3 The twenty-four caught paragraphs, one line each

Round 1 (written from guide v1; each caught 3-0 or 2-0):

- current per net: backticked units; a caveat per sentence; "(that's a lowercase `i`)" cloned from "(that's a period)"; a guessed mechanism.
- OLED reply: a troubleshooting ladder; `Z` is not an I2C scan; "That's on me" plus "(that's a period)" stacked; docs backticks in a reply; "SBC/SMD board".
- late cables: one sentence per beat; "That's on me" again; "Sorry these are late."; the wrong failure for a TRRS cable.
- slots: every noun backticked; no aside about himself; "like 500ms" invented; the real file-manager warning compressed.
- negative rails: the textbook op-amp reason; `v` is not the rail command.
- on-resistance log: docs backticks in a log; "The weird part is"; "To be continued." as a button.
- Measure/Select: "routed to `ADC 2`"; a mirrored closer; a self-contradiction (the tip stops sensing, then the reading keeps updating).
- tapping a connected row: the real passage with the hedges sanded off; a summarizing final clause; two modes flattened into one rule.

Round 2 (written from guide v2; all caught 3-0; every one shared clauses with a v2 model answer):

- slots: glossary entries fused into a four-sentence walk-through; "(kinda misnamed)" polished into "I should really pick one"; "there's no separate save".
- negative rails: "or whatever" + "*kinda*" + "so lmk" in 120 words; the OLED aside re-skinned; a `gnd` policy sentence; the `ADC` colour line moved to the rails; the config line inline without its backtick.
- on-resistance log: a mystery-then-reveal arc for a published number; "That's the whole story."; "Anyway, next up"; a seesaw sentence; "honestly I expected worse"; a bench 91Ω he never measured; "every extra hop is another 45 ohms" a near-copy of issue 20.
- Measure/Select: the `$` joke flattened and its causality inverted; "as of yet" reordered; "read whatever's on it" (the unwritten capability); "the whole resistive divider story is over on the Odds and Ends page".
- tapping a connected row: the Idle Mode section condensed; the timeout aside made wittier; "Remember it only removes" paraphrased from another section.
- current per net: impossible on two INA219s; "lazy or the right call, idk"; "lmk which one you'd rather stare at"; the menu-return line compressed.
- OLED reply: the issue-34 closer transplanted nearly verbatim; all five OLED-page facts in page order; the config line inline.
- late cables: a crimp failure the cable can't have; "3ish minutes" and "(knock on wood)" borrowed; the glitter story re-skinned.

Round 3 (written from guide v3; all caught 3-0; on three the first thing named was the guide's own `[CHECK]` device):

- on-resistance log: a beat on every sentence; the Ω arithmetic restated without its source ("14.2V like the datasheet wants", against his README's 14.6V); "hung off"; "To be continued with the charge pump" on a standalone log.
- Measure/Select: one 100-word sentence with 13 spans and a 30-word parenthesis; the switch-sensing mechanism dropped for its conclusion; "everything shares 4 wires down there"; advice hung on the unwritten `Measure` code ("leave it on `Select` unless you're routing the tip somewhere on purpose").
- tapping a connected row: ~19 spans in 113 words; "(I had it removing on one press for a while ...)" invented and argued; "knock something out", "picked out by"; the punchy closer "Do nothing and it should just unhighlight."
- current per net: a `[CHECK]` in the copy; the same "(I had it printing X ... so now Y)" template; "It's like 3 days old, so I wouldn't put much weight on the number yet."
- OLED reply: "it doesn't grab the OLED by itself, you've got to ask it to"; "pokes around"; an imperative close; the config line withheld.
- late cables: a `[CHECK]` in the copy citing "the brief"; the fault never named; "my guesses on this have been short every time so far".
- slots: a `[CHECK]` in the third person ("nothing he wrote down says"); "(kinda misnamed)" lifted; a 113-word two-sentence block with 10 spans.
- negative rails: "The `rail`s aren't stuck at 5V and 3.3V"; "should come up at -5V and stay there until you move it"; "(mostly so a chip that wants a negative supply has one sitting right there, or whatever)"; 12 spans in 90 words.

### 9.4 What marked the reals (0 of 24 miscalled), and why not to imitate it

No real paragraph was called fake in any round. What the judges used to recognize them shows how wide his range is and how little of it can be faked on purpose:

- the house-edited campaign register, curly apostrophes and "±8 V" and semicolons included: "the four individually programmable ±8 V power supplies; ten GPIOs; and seven management channels for voltage, current, and resistance" (`index.md`, and the same paragraph in the V5 README). A writer who follows this guide's docs rules would strip all of that, and would be wrong for that register. Same for the campaign page's serial section ("Jumperless V5 can sniff or write any UART, I²C, SPI, or MIDI signals on the board."): house typography, no hedge, no joke.
- a pasted code comment with a pun heading and a typo: "Rawssbar Switching" / "//you'll need to be staring at the schematic it use this" (time-to-get-excited).
- a run-together scraped outline in the pathfinding log, and the log's end-of-deep-dive handoff plus a personal offer: "There are comments in the code but there are a lot of nested array things that can get pretty confusing, if you need help understanding what's going on in a particular function, let me know and I'd be happy to walk you through it."
- a README spec dump with "+-8V" and a parenthesis that swallows two sentences (V5 README), and the same README's "Jumperless V5 can add some even crazier new stuff like; an ungodly number (445) of LEDs, a built in rotary encoder/switch, daisy chain headers, individually programmable power rails, and an isolated, always-on probing system.": a misplaced semicolon, the digit in parentheses carrying the joke, contributors linked by name in the sentence before it, a five-item list that closes on "and".
- the @handle opener and the flat closer: "@modi12jin In my experience, ..." / "So you end up with a voltage divider situation." (breadWare issue 1).
- the news reply: "Hey, so I just got a bunch of cases in, and I already have your address so I'm gonna send you one."
- the rant with a direct-address aside and an "Anyway" pivot: "Like these people do realize you can name variables after what they do, right? And these are the Official examples in the datasheet. Anyway after a few days of staring at what looks like gibberish, it starts to click." (the CH446Q log).
- a markdown gag in a README, in an unflattering origin story: "I knew this was my plan all along, but it forced me to finally design it before the code gets too specific to the original off-the-cuff design and I get stuck with my poor ~~life~~ design choices." (breadWare README). The joke is in the strikethrough; someone else suggested the form factor.
- an uncorrected typo inside a careful definition: "to make it east to just copy paste them from the terminal" (`99-glossary.md`); "to make the it easier to just hop over the middle space" next to "(note: these are abstracted away to the user by using b1-b30 instead of bigger numbers.)" (breadWare README). "Sloppy prose, precise engineering, which is his actual mix."
- the campaign community plug with "our Forum" and a lowercase "v5": "So come hang out on Discord or in our Forum and ask them about their experiences with the OG Jumperless." (our-campaign-is-go-for-launch). "our" for the community's places is his; "we" for the maker is not.
- a pun heading, three flat sentences, a bare "Note:": "Hapax LEGOmenon" / "Very much a "why not?" feature I hope someone will do something awesome with. Note: both sides are holes, there's nothing sticking out on the other side." (good-news-everyone, Jan 2025).
- the one real "That's on me for not writing the revision number on the boards" (issue 13), followed by the visual ID and relief that the user has the revision he can test on.
- a log that is four plain sentences about a jig, opening on a fragment with a dropped article and closing on a self-own stated once (8.6). "the cardboard" has no antecedent and "depth" repeats in consecutive sentences; nobody fixes it.
- a reply whose first sentence answers the question above it and hands over file paths as full-URL markdown links mid-sentence, with the grammar fumbled (issue 20, 8.4). "the nitty gritty" is his, once.
- the `measure` paragraph of `09-odds-and-ends.md`: three sentences of 24, 38 and 42 words, the last two each closing on a parenthesis (one dated), *kinda* and *exactly*. This is what 4.1 means by ragged, and it has two parentheses in one paragraph.
- the Doom log's "This is just to give people a but of an understanding of what's going on inside a crosspoint switch. Not really a demo, but it was made so people understand that the Jumpeless isn't reading and simulating your signals, just passing them through an analog CMOS switch.": two typos and the defensive point he keeps making stated flat.
- the 2021 breadWare reply: "I think I may use a couple (or 3) of these CH446s for the control board (to save space) and leave the MT8816s on the top side, after some discussion with non-techy people, they all liked the weight that those huge PLCC chips add to it. And having a huge ceramic package might help dissipate more heat so we can run them a bit further out of spec than we already are." "a couple (or 3)", the unglamorous reason, "we" in a 2021 reply, and the abuse stated without a wink.

Do not add a typo, an unclosed parenthesis or a swear to pass a test. The judges did not vote real for mess, they voted real for mess that came with correct content ("The non-obvious counts are all right", "The 20-pin FPC arithmetic lands exactly", "the bottom left is 62 and counts down to 33"), and the one real vote any fake ever received was for its correct numbers. Correct specifics are the only real-signal a writer controls. A manufactured typo next to a wrong key is worse than a clean paragraph with the right one. Rules that these reals adjusted: one or two parentheses a paragraph (4.4); "we" is absent from the 2025 docs, not from a 2021 reply (section 3); a log may open on a fragment (8.6); links in a reply are full URLs in markdown mid-sentence (8.4); "(note: ...)" goes back to 2021 and a bare "Note:" is a campaign device (4.4). Nothing else moved.

### 9.5 Strip list for a Claude draft

Run these as deletions, in order, over a draft. Each is a checklist item in section 11; the quotes it points at are in the sections named.

1. Delete every em-dash; replace with a comma, a parenthesis, or a spaced hyphen ("**[Arduino](05-arduino.md)** - The reason for those headers at the top", `index.md`).
2. Delete "ensure", "utilize", "leverage", "seamless", "robust", "simply", "please", "the user", "we", "let's".
3. Delete the opening sentence if it describes what the section will cover. Delete the closing sentence if it recaps, mirrors the opener, or is "To be continued." with nothing after it.
4. Turn any `**Note:**` / admonition box into "(note: ...)" after the sentence it qualifies, or into "Keep in mind that ..." ("Keep in mind that file operations are pretty slow, so make sure to give it time to fully save files when you drop them onto the filesystem.", `08-file-manager.md`).
5. Turn any unanswered question into a bold "**Why X?**" plus its answer, or delete it.
6. Turn any three-item parallel list into the real number of items, ragged, and let it trail off if it's an options list.
7. Move every "why" that precedes its "how" to after it. Delete any "why you'd want this" sentence in the docs.
8. Replace "may"/"might" with "should" where it describes the result of a step (keep "might" for bugs). Replace every "you will see" with "should".
9. Wrap every key, mode, node, filename and coined term in backticks, plural s outside; unwrap every number, unit, and ordinary word; unwrap everything if it is a reply or a log.
10. Find every key, number and mechanism and check it against 5.1 or the brief; cut an unverifiable one from the copy and list it in a note under the draft, or write around it with an "idk" aside for a fact a reader would accept him not having.
11. Count the asides: more than one per paragraph, cut the reader-facing ones and keep the one about his code.
12. Count "on me for", "(that's a period)", "Enter `x` in the menu": each at most once across the whole job.
13. If a sentence is a tightened version of a real Kevin sentence, put the digression back (6.10).
14. Grep the draft against this guide: any run of five or more words that also appears in a quote or in a section 10 pair is a clone, and so is any parenthesis of his sitting in a sentence of yours. Instruction stems and hardware names are excepted ("paste this into the main menu:", "run DAC calibration with `$`", "the SBC/SMD/OLED board" are vocabulary). A real sentence moved to a new situation is a clone too ("If you want, send me close up photos ..." belongs to issue 34).
15. Count lmk/idk/kinda/"or whatever": more than one per 300 words, cut. "idk" only for a fact you don't have.
16. Count sentences per paragraph in a docs draft: four, split. Count words per sentence: over about 75, split at the comma where a parenthesis should have opened; a sentence over 45 words with no parenthesis is his only when it is a section lead stating one mechanism, so a comma chain of instructions gets split.
17. If a sentence is a flat verdict on a story ("That's the whole story.") or balances the case that matters against the case that doesn't, replace it with the one clause that states the fact ("For most circuits, this really doesn't have a noticeable effect.", V5 README).
18. If a config line is inline, put it in a fenced block with its leading backtick.
19. If the topic is already on one of his pages, replace your sentences with his.
20. Delete every `[CHECK: ...]` from the copy and move it under the draft as a note; if what it flags is the point of the brief, stop and send the draft back instead of shipping a paragraph with a gap in it.
21. Replace "grab", "pokes around", "knock out", "drop it in here", "hung off", "picked out", "sitting right there", "down there" with the literal verb (find, connect, disconnect, print, remove, send).
22. Delete any sentence that opens on what the thing doesn't do ("it doesn't X by itself", "the rails aren't stuck at"); open on what it does.
23. Cut any "(I had it doing X ... so now Y)" to nothing, or to the options-then-tried shape if the brief actually gives the history.
24. Cut "my guesses have been", "I wouldn't put much weight", "and stay there until", "it's like N days old"; a guess is one clause ("Of course that's a guess, but it feels reasonable enough.") and a new feature's caveat names a concrete omission.
25. Delete "To be continued with" on a log that isn't part of a series you are writing.
26. A number he stated: give it once with "Datasheet says" or the page it's from, and where his statements differ pick one.

---

## 10. Before and after, by tell

Each pair is one Claude-ish line and Kevin's version. "Before" lines are one of three things: a sentence a blind-round judge caught (marked round 1, 2 or 3), a house-edited or templated sentence from the corpus that sits next to his own version of the same idea (marked real), or a constructed sentence in the shape a draft tends to take (unmarked). Every "Kevin" line is his, byte-for-byte, with its source; where the tell is "he doesn't write this", the Kevin line is the nearest real thing, and the note says so.

**Read before using any of these.** A pair shows a shape. Round 2 proved that writers treat model answers as a phrasebook: all eight round-2 fakes shared clauses with the previous guide's worked answers, and the judges caught the shared clauses. So: no clause from any Kevin line below appears in your draft unless your situation is literally the one it came from (rewriting that page, replying in that thread). If a five-word run in your draft also appears anywhere in this guide, rewrite it, with one carve-out: bare instruction stems ("paste this into the main menu:", "run DAC calibration with `$`", the eight key-intro shapes in 5.3) and hardware names ("the SBC/SMD/OLED board", "GPIO 7 and 8") are vocabulary, not voice. Any parenthesis of his, of any length, stays in his sentence. What you take from a pair is the move: the comma instead of the dash, the aside about his code instead of the caution to the reader, the flat clause instead of the seesaw.

### 10.1 Dashes and joints

1. Before: "Press the Connect button — the logo turns blue and the probe LEDs change."
   Kevin: "The logo should turn blue and the LEDs on the probe should also change" (`01-basic-controls.md`)
2. Before: "The Jumperless auto-negotiates the baud rate — no configuration required."
   Kevin: "Don't worry about the baud rate, the Jumperless senses what the host computer is set to and changes the speed accordingly." (`05-arduino.md`)
3. Before (real, excluded App README): "An app to talk to your Jumperless V5 — connect to Wokwi, flash Arduino sketches,"
   Kevin: "**[The App](03-app.md)** - For talking to your Jumperless" (`index.md`)
4. Before: "It looks like nonsense; however, after enough time in it, it makes sense."
   Kevin: "It probably looks like nonsense to you but I've been in it so long it makes perfect sense to me." (`07-debugging.md`)
5. Before: "A short press means yes; a long press means no, back, or exit."
   Kevin: "In general, a `click` (short) is a `yes`, and a `hold` (long) is a `no`/`back`/`exit`/`whatever`." (`01-basic-controls.md`)

### 10.2 "The user", "we", "please", "simply", "ensure"

6. Before: "The user may simply press the Connect button again to exit Connect mode."
   Kevin: "To get out of `Connect` mode, press the button again." (`01-basic-controls.md`)
7. Before (real, his own 2023 log): "First, we need to download the App and latest firmware here."
   Kevin (2025): "First, keep the switch on the probe set to `Select`" (`01-basic-controls.md`)
8. Before (real, campaign): "they can simply paste it into the main menu and that setup will be connected and saved to the currently active slot."
   Kevin (docs): "You can just paste this into the main menu:" (`04-oled.md`)
9. Before: "Please ensure that the final bridge is terminated with a comma."
   Kevin: "It's pretty loose with what it accepts, just make sure the last bridge ends with a comma." (https://github.com/Architeuthis-Flux/Jumperless/issues/25#issuecomment-1888338761)
10. Before: "Users can leverage the config file to persist their settings across reboots."
    Kevin: "To change any persistent settings, there's a `config` file. You can read it with `~`" (`06-config.md`)
11. Before: "To ensure reliable soldering, we recommend the standard footprint."
    Kevin: "Just use the standard LQFP44 footprint, it will be much easier to solder, I just had to make mine smaller so they'd fit on a really dense board." (https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1880179763)
12. Before (real, house-edited campaign page): "gave us a list of things to improve and inspired us to make getting a circuit from your brain into hardware feel even more like actual magic."
    Kevin (README): "gave me a long enough list of things I wish I had done that I felt it was time to push the design even further." (`readmes/JumperlessV5_README.md`)

### 10.3 Benefit-first sentences, use-case lessons, feel-forecasts, superlatives

13. Before (rejected by him, 2026-08-28): "So you don't have to wire the boring stuff"
    Kevin: "It's not just about being too lazy to plug in some jumpers." (`readmes/JumperlessV5_README.md`)
14. Before (real, house-edited campaign page): "You'll quickly forget this isn't how prototyping has always been."
    Kevin: "And it's easy to forget this isn't how prototyping stuff on a breadboard always has been." (`readmes/JumperlessV5_README.md`)
15. Before (round 1): "This is mostly for op amps, they need a negative supply to swing below 0V"
    Kevin: 0 use-case lessons in the docs; the only shape a use case takes is one clause of pitch with a shrug: "or even crazier things like having the slot change based on a Eurorack CV (control voltage) signal or whatever." (`readmes/JumperlessV5_README.md`)
16. Before: "The new app is faster, more reliable, and easier to use than ever."
    Kevin: "- **Firmware updating** should be pretty reliable when there's a new version (falls back to instructions for how to do it manually)" (`03-app.md`)
17. Before: "This powerful new feature gives you real-time insight into what your circuit is doing."
    Kevin: "this *one* feature is the reason I did this whole update. And it's worth it because it's sick af." (`01-basic-controls.md`)
18. Before: "Jumperless is an intuitive, seamless prototyping experience."
    Kevin: "It's about cutting down on the debugging bullshit and letting the grander plans for what you're building flow freely." (`readmes/JumperlessV5_README.md`)
19. Before: "Whether you're a beginner or a seasoned engineer, you'll love how easy this is."
    Kevin: "It's called Jumperless and I think it's pretty rad, but I'm probably biased." (social, Bluesky 2023)

### 10.4 Preambles, recaps, mirrored closers, summarizing clauses, curtain lines

20. Before (real, templated page): "This guide covers how to write, load, and run Python scripts that control Jumperless hardware using the embedded MicroPython interpreter."
    Kevin: "The Jumperless has a built in File Manager which you can access in the menu with `/`, or enter `U` in the menu and Jumperless will mount as a USB Mass Storage drive called `JUMPERLESS`" (`08-file-manager.md`)
21. Before: "In summary, the Remove button lets you clear individual connections without affecting the rest of your net, giving you fine-grained control."
    Kevin: "TL;DR, double click `remove` to remove, single click to unhighlight." (`01-basic-controls.md`, after a 74-word bullet, the only place a TL;DR goes)
22. Before (round 1): "Then just slide it back to `Select`, nothing gets selected in `Measure`."
    Kevin: a page ends on the alternative: "Or you connect `ROUTABLE_BUFFER_IN` to a `GPIO` and set it `high` and just lose the ability to sense where the switch is." (`09-odds-and-ends.md`, last line)
23. Before (round 1): "which is how a `net` grows past 2 `node`s."
    Kevin: a last clause is a cross-link: "(you'll see more about that in [Idle Mode Interactions](#idle-mode-net-highlighting).)" (`01-basic-controls.md`)
24. Before (round 2): "That's the whole story."
    Kevin: a flat landing answers a question: "The answer is switch position sensing." (`09-odds-and-ends.md`)
25. Before (round 3): "Do nothing and it should just unhighlight."
    Kevin: "if you let it time out without pressing anything, the row will be unhighlighted." (`01-basic-controls.md`)
26. Before: "And that's all there is to it. Happy prototyping!"
    Kevin: the one meta-closer in the docs, about the docs: "That's probably more than you need to worry about but that gives me a nice start on real docs" (`99-glossary.md`)

### 10.5 Questions and callouts

27. Before: "Ever wondered why the probe has to be in Select mode? Let's find out."
    Kevin: "**Why Select mode?** `Measure` mode allows the probe tip to be ±9V tolerant and routable like any other node, but as of yet, the code to actually do anything with it is unwritten" (`01-basic-controls.md`)
28. Before (real, templated page): "**Note:** The standard Python `exec(open(...).read())` method is not supported in the Jumperless MicroPython environment."
    Kevin: "(note: the color now follows the `row` instead of the net, so it can keep the colors even if you remove nets below it and they shift, this was soooo difficult until I realized I should do it by `node`)." (`01-basic-controls.md`)
29. Before (real, his 2023 log): "Note that this won't run correctly from anywhere but your Applications folder, so drag it there."
    Kevin (2025): "(you'll probably need to comment out `upload_port = /dev/cu.usbmodem101` in `Platformio.ini` so it'll just automatically find it)" (`11-WritingApps.md`)
30. Before: "Warning: file operations are slow. Always wait for saves to complete before unplugging."
    Kevin: "Keep in mind that file operations are pretty slow, so make sure to give it time to fully save files when you drop them onto the filesystem." (`08-file-manager.md`)
31. Before: "Important: the probe is read by a resistive voltage divider, so avoid touching the pads."
    Kevin: "**Remember the probe is read by a resistive voltage divider**, so putting your fingers on the pads (or the back sides of the 4 risers that connect those `probe sense` boards to the main board), or anything causing the probe tip not to be at a steady 3.3V will give you weird readings" (`01-basic-controls.md`)

### 10.6 Backticks: on numbers, on every noun, outside the docs, on a config line

32. Before (round 1): "Anything under `0.5mA` reads as `0.0`, the shunt is only `2Ω`"
    Kevin: "The probe tip needs to be at a steady 3.3V to be read by the `probe sense pads`" (`09-odds-and-ends.md`)
33. Before (round 1): "Enter `>` to move up a `slot` and `<` to go back down, there are 8 of them, `nodeFileSlot0.txt` through `nodeFileSlot7.txt`."
    Kevin: "`slot` = one of the 8 node files stored that you can switch between with `<`/`>` or the `menu`s. Named `nodeFileSlot[0-7].txt` (there's no actual limit, there's *so* much flash storage on this thing, but by default it's 8)" (`99-glossary.md`)
34. Before (round 1, a reply): "it's easy to be off by a `row` and land `SDA` on `GND`"
    Kevin (a reply): "Run a jumper from the left side pad to the GND rail." (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783874751)
35. Before (round 1, a log): "Every `bridge` goes through 2 crosspoint switches"
    Kevin (README, no backticks): "In the original layout if I wanted to connect top row 5 to bottom row 5, it would always take 2 hops to do that (and these switches each have an on resistance of about 65Ω)." (`readmes/breadWare_README.md`)
36. Before: "Just type `f` and it will wait for a set of bridges."
    Kevin (a 2023 log, single quotes): "Just type 'f' and it will wait for a set of bridges connected with a dash and separated with a comma, whitespace is ignored." (https://hackaday.io/project/191238/log/222858-getting-started-using-your-jumperless)
37. Before (round 2): "copy the `[dacs] bottom_rail` line, and paste it back with -5.00 on it"
    Kevin: "copy / edit / paste any of these lines" above a fenced block holding "`[dacs] bottom_rail = 0.00;" (`06-config.md`)
38. Before: "The measured resistance is roughly `90Ω` per connection."
    Kevin: "So the total resistance for a jumperless connection is ~90Ω (45Ω for each pass through an overdriven crosspoint switch)." (`readmes/JumperlessV5_README.md`)

### 10.7 Caveats and asides: a caution per clause, a wittier aside, invented history, self-calibration

39. Before (round 1): "It routes the current sense `+`/`-` pair through one `net` at a time, so a full board should take like a second."
    Kevin: one aside per paragraph, about him: "(if I missed something, let me know, it's a fairly new thing so I've probably forgot to add code for it to print in a bunch of places.)" (`04-oled.md`)
40. Before (round 2): "(that timeout is a number I picked out of the air, so if it feels off lmk)"
    Kevin: "(I need to settle on a good time for this, if it feels too short or long lmk)" (`01-basic-controls.md`)
41. Before (round 2): "(I call it a `node file` in some places and a `slot file` in others, it's the same file, I should really pick one.)"
    Kevin: "enter `s` to print the (kinda misnamed) `node file`s to see a list of bridges" (`99-glossary.md`)
42. Before (round 3): "(I had it removing on one press for a while, it's way too easy to knock something out of a `net` you meant to keep)"
    Kevin: "(there were some choices here, like make each button assigned to high / low or allow removing them, but this felt like the best way after trying them all)" (`01-basic-controls.md`)
43. Before (round 3): "It's like 3 days old, so I wouldn't put much weight on the number yet."
    Kevin: "(this might be broken in that FW release, I'm fixing that right now actually, and will just be purple/white)" (`09-odds-and-ends.md`)
44. Before (round 3): "`bottom_rail` at -5V should come up at -5V and stay there until you move it"
    Kevin: a setting is stated and left: "`[dacs] limit_min = -8.00;" (`06-config.md`)
45. Before (round 2, the OLED aside re-skinned): "the negative half of the calibration is fairly new and I've probably missed something"
    Kevin: a different page gets a different aside: "(and of course, I'll forget to update this, if it's after like June 2025, double check this is still true.)" (`09-odds-and-ends.md`)
46. Before (round 2): "The `gnd` rail is the one exception, it's 0V and I'm leaving it that way"
    Kevin: `gnd` is listed and left alone: "(`top_rail`, `bottom_rail`, `gnd`)" (`99-glossary.md`)
47. Before: "Please note that this behaviour may change in a future release."
    Kevin: "{there's a colorful update to that I'm working on right now}" (`99-glossary.md`)

### 10.8 Cloned tics and transplanted sentences

48. Before (round 1): "(that's a lowercase `i`)"
    Kevin: "just use the menu option `.` (that's a period)." (`04-oled.md`), once, for the one key a reader cannot see on the page
49. Before (round 1): "That's on me for not putting that anywhere obvious."
    Kevin: "I think I may have left some silly change in the code from debugging something else that isn't connecting Net 0 GND" (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783852086)
50. Before (round 2): "If you want, send me a close up of how the module is sitting in the SBC/SMD/OLED board and I might be able to spot the issue."
    Kevin: a different photo ask for a different problem: "Send a pic of the top of the board too, I'm interested in the big tantalum capacitors under the Nano header." (issue 34 thread)
51. Before (round 2): "like 3ish minutes each once I got a rhythm going"
    Kevin: "This takes like 3ish minutes, so when you drop this UF2, wait until the drive pops up again, then load the firmware from releases." (https://github.com/Architeuthis-Flux/JumperlessV5/issues/17#issuecomment-3027899213), about a UF2 flash, where it stays
52. Before (round 3): "each one has its own `node file` (kinda misnamed) that whatever you bridge while you're sitting on it goes into"
    Kevin: "`node file` / `slot file` = this is an actual text file on the filesystem that stores the list of bridges, there's one of these for each `slot`" (`99-glossary.md`)
53. Before (round 1, three fakes): "just enter `i` in the menu" / "Enter `s` in the menu" / "just enter `v` in the menu"
    Kevin: one of eight shapes: "You can also enter `Z` for a little debug menu" (`08-file-manager.md`)
54. Before (round 1): "To be continued."
    Kevin: "To be continued with Driving the CH446Qs" (https://hackaday.io/project/191238/log/222530-the-code-part-2-pathfinding)

### 10.9 Invented facts, numbers and mechanisms

55. Before (round 1): "just enter `Z` and send me what the I2C scan prints"
    Kevin: the one thing he documents the OLED doing: "It will try to find the OLED on the I2C bus, after a few failed attempts, it'll automatically disconnect to free up GPIO 7 and 8." (`04-oled.md`)
56. Before (round 1): "enter `v` in the menu, pick `bottom_rail` and set it to -5V"
    Kevin: "`[dacs] bottom_rail = 0.00;" in a fenced block (`06-config.md`)
57. Before (round 1): "routed to `ADC 2`"
    Kevin: "the probe tip is now `ROUTABLE_BUFFER_IN`" (`09-odds-and-ends.md`); "ADC 7 is hardwired to the probe tip (in measure mode)" (his code comment, jumperless-probelessly)
58. Before (round 1): "the `node file` gets written like 500ms after you stop making `bridge`s"
    Kevin: the only 500ms he wrote: "I will eventually add a setting for the toggle repeat rate (set to 500ms now)" (`01-basic-controls.md`)
59. Before (round 2): "There's a new menu option that prints how much current every net is pulling"
    Kevin: "There's just one routable as a current sensor (the other is for measuring resistance / current draw from the DACs), so you'll be able to poke around with the probe and it'll show you the current between any 2 places." (a-farewell-to-campaigns)
60. Before (round 2): "the cable factory crimped the whole run at 1.5mm pitch when the probe takes 1.25mm"
    Kevin: "It connects to the main board with a TRRRS 1/8" audio jack." (`readmes/JumperlessV5_README.md`)
61. Before (round 2): "put a meter across one bridge, row 12 to row 40 with nothing else on it, and got 91Ω"
    Kevin: a spec, not a bench reading: "So the total resistance for a jumperless connection is ~90Ω (45Ω for each pass through an overdriven crosspoint switch). For most circuits, this really doesn't have a noticeable effect." (`readmes/JumperlessV5_README.md`)
62. Before (round 3): "65Ω a switch if you keep Vdd - Vss under 14.2V like the datasheet wants"
    Kevin: "Datasheet says Vdd - Vss is max 14.2V (which gives 65ohms on resistance, and I'm running them at Vdd - Vss ~18.5V to get that down to 45 ohms." (https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1879196708)
63. Before (round 2): "so you can drop the tip on a `row` and read whatever's on it"
    Kevin: "But in the future, there will be some other stuff you can do in that mode treating it as an analog line" (`09-odds-and-ends.md`)
64. Before (round 2): "negative rails come up *kinda* icy blue on the breadboard LEDs, same as the `ADC`s do"
    Kevin, about `ADC`s and nothing else: "Negative voltages are kinda blue/icy and do that same thing with the "cold" colors towards -8V." (`09-odds-and-ends.md`)
65. Before (round 3): "`[CHECK: 2 INA219s on this board, one of them stuck across DAC 0's output shunt, so per net numbers aren't something the hardware does ...]` There's a readout for the routable current sense now"
    Kevin: "But for now, I'll only talk about things I've written firmware for that is currently supported without any hacking required." (`readmes/JumperlessV5_README.md`)
66. Before: "The firmware writes the slot file automatically whenever the netlist changes."
    Kevin: all he says about it: "The firmware saves multiple netlists in separate text files. You can save/load/manage the various slots through a serial terminal, the onboard menus, or even crazier things" (`readmes/JumperlessV5_README.md`)

### 10.10 Paraphrase drift: wittier, reordered, flipped, compressed, mechanism dropped

67. Before (round 2): "so if you've been playing with the switch, run DAC calibration with `$`."
    Kevin: "If you can't seem to stop playing with the switch on the probe, run DAC calibration with `$` and the 3.3V `measure` mode puts out should be fairly accurate enough for probing." (`01-basic-controls.md`)
68. Before (round 2): "the code to actually do anything with that is as of yet unwritten so I mostly end up flipping it right back"
    Kevin: "but as of yet, the code to actually do anything with it is unwritten so it just connects to DAC 0 and outputs 3.3V just like it was in `Select` mode." (`01-basic-controls.md`)
69. Before (round 2): "Anything you type gets you back to the main menu."
    Kevin: "(And just like basically any menu not asking for input, entering anything will bring you back to the main menu.)" (`07-debugging.md`)
70. Before (round 1): "(`U` mode is pretty slow, so wait for the copy to actually finish before you unplug it)"
    Kevin: the sentence in pair 30, uncompressed, on the page it belongs to (`08-file-manager.md`)
71. Before (round 1): "A single click on `remove` drops the highlight, a double click actually pulls that `node` out."
    Kevin: "`remove` will briefly turn the `row` reddish `warn` (I need to settle on a good time for this, if it feels too short or long lmk), another `remove` press will remove that `row`" (`01-basic-controls.md`)
72. Before (round 3): "the `probe LED`s run off the other half of the switch, which is also how the board knows which way you've got it set"
    Kevin: "`DAC 0`'s output is hardwired to go through a `current sense` shunt resistor, so when `DAC 0` is powering the `probe LEDs`, they'll be drawing some current I can measure with one of the `INA219`s" (`09-odds-and-ends.md`)
73. Before (round 2): "(the whole resistive divider story is over on the Odds and Ends page)"
    Kevin: "(talked about in [OLED Section](04-oled.md))" (`01-basic-controls.md`)
74. Before (round 2, moved from another section): "Remember it only removes the `bridge`s that `row` is directly in, not everything on the `net`"
    Kevin, in Connecting Rows, where it stays: "Remember it only disconnects that `node` and anything connected to it directly, not *everything* on the `net`." (`01-basic-controls.md`)
75. Before (round 3): "ADC 7 is on the end"
    Kevin: "float probeVoltage = readAdcVoltage(7, 8); //ADC 7 is hardwired to the probe tip (in measure mode), so it's this easy" (jumperless-probelessly)

### 10.11 Replies: openers, closers, ladders, apologies

76. Before (round 3): "Hey, it doesn't grab the OLED by itself, you've got to ask it to."
    Kevin: "Hey, the bug should be fixed in the latest release. Just download firmware.uf2 from the releases page and it should work better." (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783916276)
77. Before (round 3): "The `rail`s aren't stuck at 5V and 3.3V, they're 2 of the 4 programmable supplies on here"
    Kevin: "The `connect`/`measure` switch is a Dual Pole Dual Throw (DPDT) switch." (`09-odds-and-ends.md`)
78. Before (round 1): "If it's still blank, make sure the module is pushed all the way down ... If it's seated right and still nothing, just enter `Z` and send me what the I2C scan prints"
    Kevin: "- Is one particular chip much hotter than the others?" (https://github.com/Architeuthis-Flux/Jumperless/issues/34#issuecomment-2221613644)
79. Before (round 3): "get a photo of the module and the SBC/SMD/OLED board it's plugged into and drop it in here."
    Kevin: "Could you also let me know if you have Rev 2 or Rev 3? and if it works on any other rows?" (https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783856159)
80. Before (round 1): "Sorry these are late."
    Kevin: "There haven't been any serious unexpected delays (knock on wood), just my insistence that I should probably do one more round of shaking out potential hardware bugs before these ship." (time-to-get-excited)
81. Before (round 2, the page in page order): "Type a period into the main menu and it'll look for it on the I2C bus at 0x3C and hook the data lines onto GPIO 7 and 8 ... You can also paste `[top_oled] connect_on_boot = true;` into the menu"
    Kevin: one thing to do: "Still do the bodge though, it assumes you've done it." (issue 13)
82. Before: "Hi! Thanks for reaching out. Unfortunately, this appears to be a hardware fault."
    Kevin: "Yeah that shouldn't be happening. First, let me know your name so I can ship you out a fresh one and parts to fix the old one." (https://github.com/Architeuthis-Flux/Jumperless/issues/34#issuecomment-2221613644)
83. Before: "Apologies for the inconvenience. We are aware of the issue and working on a fix."
    Kevin: "Ah shit, Wokwi added a README.md to their projects, which moved the index where the diagram.json is stored." (https://github.com/Architeuthis-Flux/Jumperless/issues/23#issuecomment-1879935990)
84. Before: "Please don't worry, this is a very common mistake."
    Kevin: "Don't feel bad, I've spent hours trying to fix what I thought was a routing bug that ended up being exactly this." (https://github.com/Architeuthis-Flux/Jumperless/issues/33#issuecomment-2203450289)
85. Before: "Please try the latest release and let us know if the issue persists."
    Kevin: "Just grab the app again from the [latest release](https://github.com/Architeuthis-Flux/Jumperless/releases/latest) and let me know if that works for you." (https://github.com/Architeuthis-Flux/Jumperless/issues/32#issuecomment-2214679003)
86. Before: "For a detailed explanation of the routing algorithm, see the documentation."
    Kevin: "Read up on [Telephone Exchanges](https://en.wikipedia.org/wiki/Telephone_exchange). Because that's basically what's going on with this" (https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1874483799)

### 10.12 Logs and updates: staged reveals, seesaws, punchline beats, calibrated guesses

87. Before (round 1): "The weird part is the on resistance drops the wider you make the supply"
    Kevin: "Okay, here's the main bummer here." (`readmes/JumperlessV5_README.md`), then the numbers
88. Before (round 2): "So the top rail said 5V and the breadboard said 3.2V, and I spent most of a day blaming the charge pump"
    Kevin: "Analog crossbar switches have some resistance, roughly totaling to 85Ω after the two hops though a crossbar needed to make a connection." (a-farewell-to-campaigns)
89. Before (round 2): "Doesn't matter even a little for logic, but it matters a whole lot once anything is actually drawing current"
    Kevin: "For most circuits, this really doesn't have a noticeable effect." (`readmes/JumperlessV5_README.md`)
90. Before (round 2): "honestly I expected worse"
    Kevin: "I was expecting this not to work, but surprisingly, it did." (https://hackaday.io/project/180394/log/194325-early-proofs-of-concept)
91. Before (round 3): "A 100 ohm load hung off the top rail is where I finally noticed."
    Kevin: "This turned out to be surprisingly complicated, I basically spent 2 days just tweaking the values until it looked right." (https://hackaday.io/project/191238/log/222810-the-code-part-4-picking-colors-and-putting-them-on-your-retinas)
92. Before (round 3): "To be continued with the charge pump."
    Kevin, closing a standalone log: "That's all I got about the LEDs, if you want me to be clearer about something, let me know and I'll add to this log." (same log)
93. Before (round 3): "The factory says 2 more weeks, I'm going to say 3, and that's a guess, my guesses on this have been short every time so far."
    Kevin: "Of course that's a guess, but it feels reasonable enough." (time-to-get-excited)
94. Before (round 2): "I'm not going to sit on a few hundred finished Jumperlesses waiting on cables, so I've been soldering the 4 wires straight to the pads by hand"
    Kevin: "The lead times are a bit long (6-8 weeks and this was about five weeks ago), and I wasn't about to hold up shipping on account of the cables, so I had them send me their existing inventory of 100 black ones to hand paint myself." (time-to-get-excited)
95. Before (round 3, the fault unnamed): "the whole run came back wrong and they're doing it again"
    Kevin: "they told me the molds they used to make these are "used up", but they'd be happy to make a new injection mold and do them in pink" (time-to-get-excited)
96. Before: "We're thrilled to announce that shipping begins next month!"
    Kevin: "TL;DR: The first batch of Jumperless V5s will be shipping to me this week and will be on their way to you shortly thereafter." (time-to-get-excited)
97. Before: "This release includes numerous improvements and bug fixes."
    Kevin: "There's *sooo* much new shit in here, even though to an end user it shouldn't really look much different, just a bit snappier and (hopefully) stable." (https://github.com/Architeuthis-Flux/JumperlOS/pull/1)

### 10.13 Folksy verbs for what the firmware does

98. Before (round 3): "it pokes around the I2C bus for it"
    Kevin: "It will try to find the OLED on the I2C bus" (`04-oled.md`)
99. Before (round 3): "with the `row` you're on picked out by a different animation"
    Kevin: "there's a slightly different animation on the `row` you have selected from the whole `net`" (`01-basic-controls.md`)
100. Before (round 3): "everything shares 4 wires down there"
     Kevin: "over the 4 wires on a TRRS cable" (`09-odds-and-ends.md`)
101. Before (round 3): "`connect` from there starts a `bridge` on that `row` and drops you back to `idle` once you tap the other end"
     Kevin, his one figurative firmware verb, in place: "`connect` button will bring you into probing mode with the highlighted row already selected and then spit you back out to `idle` mode once you've made a connection to another row" (`01-basic-controls.md`)
102. Before: "The app grabs the latest firmware and flashes it for you."
     Kevin: "Just grab the app again from the [latest release]" is what "grab" is for; the firmware "should be pretty reliable when there's a new version (falls back to instructions for how to do it manually)" (`03-app.md`)

### 10.14 Tic stacking and hand-wrings

103. Before (round 2, three in 120 words): "or whatever ... so lmk if a rail reads obviously wrong ... come up *kinda* icy blue"
     Kevin, the only two-tic line in the docs: "(terminal.app on macOS, Powershell on Windows, idk on Linux), just go to the directory in a terminal and run the script in [tabby](https://tabby.sh/) or whatever" (`03-app.md`)
104. Before (round 2): "which is either lazy or the right call, idk."
     Kevin: "I'm gonna call this idle mode here until I think of a good name" (`01-basic-controls.md`)
105. Before (round 2): "lmk which one you'd rather stare at."
     Kevin: "so if there's a specific thing, lmk and I'll write an example." (`11-WritingApps.md`)
106. Before (round 3): "(mostly so a chip that wants a negative supply has one sitting right there, or whatever)"
     Kevin, "whatever" ending an options list: "Or you can use any terminal emulator you like, [iTerm2](https://iterm2.com/), [xTerm](https://invisible-island.net/xterm/), [Tabby](https://github.com/Eugeny/tabby), [Arduino IDE](https://www.arduino.cc/en/software/)'s Serial Monitor, whatever." (`03-app.md`)
107. Before: "I'm not 100% sure this is right, so take it with a grain of salt."
     Kevin: "which swaps X12 and X13 with X6 and X7 (or something like that, it's been a while)" (issue 20 thread)

### 10.15 Shape: balanced blocks, the monolith, the wrong register

108. Before (round 2, four balanced sentences): "There are 8 `slot`s by default ... Whichever one you're sitting on is where your `bridge`s get written ... When you come back to a slot it goes through that file ... To see what's in one, enter `s`"
     Kevin: one line, one fact: "Also the color assignments are saved to a file for each slot, so they should work after a reboot and when changing `slots`" (`01-basic-controls.md`)
109. Before (round 3, one 100-word sentence): "The slide switch is a DPDT, and on `Select` the tip is held at 3.3V so the `probe sense pads` can tell where it's landed, which is what `connect`, `remove`, and every menu that asks for a `node` are counting on. `Measure` puts `ROUTABLE_BUFFER_IN` on the tip instead ..."
     Kevin: one sentence, one mechanism: "The probe tip needs to be at a steady 3.3V to be read by the `probe sense pads` which is a big resistive divider sensed by a single `ADC`." (`09-odds-and-ends.md`)
110. Before: "Step 1: Enter probe mode. Step 2: Tap the first node. Step 3: Tap the second node."
     Kevin: "Now any pair of nodes you tap should get connected as you make them. In connect mode, you're creating `bridges` (see the [glossary](99-glossary.md)), so connections are made in pairs." (`01-basic-controls.md`)
111. Before (a docs draft that reads like a campaign update): "Hey everyone, big news: the OLED now connects on boot!"
     Kevin (docs): "If you want to use this all the time, there's a config option to connect the OLED on startup. You can just paste this into the main menu:" (`04-oled.md`)
112. Before (a README draft in docs register): "Enter `U` in the menu to mount the `JUMPERLESS` drive."
     Kevin (README register, no backticks): "The firmware saves multiple netlists in separate text files. You can save/load/manage the various slots through a serial terminal, the onboard menus, or even crazier things" (`readmes/JumperlessV5_README.md`)

### 10.16 The eight recurring briefs, and what passes

Every round used the same eight briefs. Three rounds of afters showed that the passing answer to most of them is not new prose. This table keeps that result without the forty worked paragraphs it came from.

| Brief | The passing answer | Why |
| --- | --- | --- |
| docs: the Measure/Select switch | his text byte-for-byte: "First, keep the switch on the probe set to `Select`", the "**Why Select mode?**" paragraph, the `$` calibration line; if the switch itself is wanted, the four short paragraphs of `09-odds-and-ends.md` starting "The `connect`/`measure` switch is a Dual Pole Dual Throw (DPDT) switch." | the page exists (6.11); every rewrite was caught for drift or for dropping the mechanism |
| docs: tapping a row that is already connected | the four Idle Mode bullets of `01-basic-controls.md` byte-for-byte; under a "no bullets" brief, the same four lines without their dashes | the timeout aside is his open to-do note; every prose version invented history or a verdict |
| docs: saving to a slot and getting it back | the `slot` and `node file` glossary lines and the colour-file bullet, three one-sentence paragraphs; nothing about when the file is written, because he never said | "(kinda misnamed)" stays inside the `bridge` entry; the write trigger is a note under the draft |
| docs: the rails go negative | two short lines and a fenced block: the rails go down to -8V, paste this into the main menu, "`[dacs] bottom_rail = -5.00;", then a constructed parenthesis on the limits (the `limit_min` and `limit_max` lines in the `[dacs]` section of the `config`) | the config line is the only rail-setting form he documented; the click wheel path is a note under the draft; no `gnd` sentence, no colour claim, no use case |
| reply: a blank OLED after plugging it in | flat opener stating that it gets connected from the menu, the period key described in a fresh shape from 5.3, the retry in one parenthesis, the `[top_oled] connect_on_boot = true;` line in a fenced block, close on "Let me know if that works for you." or a question | never a negation-correction opener, never the page in page order, never an imperative close, never the issue-34 photo sentence |
| README: a new command that prints current per net | copy describes the one routable `INA219` and the `ISENSE_PLUS` / `ISENSE_MINUS` pair going in series with the thing measured, the key as the brief gives it, one aside that it is new and to report anything weird; "every net" goes in the note under the draft | two INA219s, one hardwired to `DAC 0`; nothing reads every net |
| log: the crosspoint on-resistance | opens on what the parts are, gives the datasheet number once with "the datasheet says", explains the overdrive in his words (the specs get better with more supply), the 20V beta-unit fact, one flat contrast clause, closes on "let me know"; no backticks | a published spec is stated in passing with its source, never staged as a discovery; a standalone log has no "To be continued with" |
| campaign update: probe cables late, supplier sent the wrong pitch | none as briefed; the fault cannot happen to a molded TRRS plug and the fault is the update's first fact, so the draft goes back with a note (5.2). A version whose fault is real (the plug end running long, from his own cable history) narrates what he is doing by hand meanwhile and labels the date a guess in one clause | round 2 wrote the impossible fault as fact, round 3 left a bracket and never named it; both were caught |

---

## 11. Checklist: run over every draft

Scope: written for docs pages. For a support reply, allow "let's" (he writes "let's do some troubleshooting"), apply #17 strictly (no backticks except a literal command) and #21, and close per #40; replies have no sign-off. For a campaign update, skip #15 (8 of 8 sign off) and read 7.8. For a hackaday log, #17 is "no backticks at all", and the closer names the next part only when the log is one of a series (#37); otherwise it ends on the last fact, a flat line, or "let me know".

1. Em-dashes: 0. Replace each with a comma, a parenthesis, or a spaced hyphen.
2. First sentence of the section is an action, a key, or where the thing lives. No "this section covers", no benefit statement, no "this is for op amps".
3. Last line is a fact, a parenthesis, a cross-link, a code block, or an image. No recap, no "next steps", no mirrored closer, no summarizing clause, no "Let me know if that works" on a docs paragraph. A one-line TL;DR is allowed only after a long bullet.
4. Every key, mode, button, node, filename and coined term is in backticks, plural s outside (`node`s).
5. Order inside a step: action, "X should ...", what it means, "If you make a mistake ...", how to exit.
6. Parentheses: one per paragraph, two only when both are his kind, placed after the instruction they qualify. At least half of them are about the state of his code, not cautions to the reader. Notes are "(note: ...)", "Keep in mind that", "Remember"; no `**Note:**`, Warning or Tip boxes.
7. "should" for the expected result of a step; "might"/"may" only for bugs and side effects ("this might be broken"); no "will see", no "please note".
8. "just" not "simply"; "kinda" not "kind of"; "idk"/"lmk" in asides; "stuff" is fine.
9. Zero: ensure, utilize, leverage, seamless, robust (as an adjective), intuitive, powerful, please, the user, we, let's.
10. Question marks only in a heading or bold lead, answered in the next clause.
11. Exclamation marks: at most one per page, on a feature landing, never on a step.
12. Lists are ragged: 2, 4, 5, 7 items, bare bullets (no trailing period), options lists trail off with "or whatever".
13. Numbers are digits glued to units (3.3V, 500ms, 7x2), bare, never in backticks; counts are digits ("2 buttons"); no `~` in docs.
14. Unfinished or broken things are stated inline in parentheses with what's being done about them, present tense; no "Known issues" section.
15. The only call to action in the docs is a request to report back, "lmk" or "let me know" ("if there's a specific thing, lmk"). "Let me know if that works for you." is a reply closer, not a docs one. No sign-off, no name, no "please", no "sorry".
16. Every key, number, pin and mechanism is in section 5.1 or in your brief. Anything else is left out of the copy and listed in a note under the draft (a `[CHECK]` is the note's form, and it never ships, #31), or written around with an "idk" aside for a fact a reader would accept him not having. Never a guess.
17. Backticks: none around numbers, units or ordinary words; about one span per 12 words at the densest; none at all in a reply (except a shell command) or a log.
18. "on me for", "(that's a period)", "Enter `x` in the menu", "To be continued": each at most once per job, and only when the exact situation matches (a specific omission, an invisible key, a menu listing, a named next part).
19. Sentence lengths are ragged. If every sentence is 15-25 words and ends on its own caveat, merge two with a comma and cut the extra caveats.
20. The paragraph digresses once: a cross-link, a naming confession, a repeated point, or a design decision confessed inline. If you tightened a real Kevin passage, put one of its digressions back.
21. A reply gives one thing to try (plus a photo if physical) or a bullet list of questions. Never an if/then ladder.
22. Hardware names are his exact ones: "the SBC/SMD/OLED board", "the probe cable" is a TRRS cable, "DAC 0" and "GPIO 7 and 8" with spaces in prose, `ROUTABLE_BUFFER_IN` as an identifier.
23. Grep the draft against this guide, and at two words for anything in parentheses ("(kinda misnamed)" was lifted in round 3): no run of five or more words shared with a quote or a section 10 pair, except bare instruction stems and hardware names; no real sentence moved to a situation it didn't come from.
24. Docs paragraphs: one sentence, sometimes two, rarely three; four happens once in 103 of his and never in yours; never one sentence over about 75 words (#32). A "paragraph" brief gets one ragged sentence with a parenthesis, or a `##` with short lines under it.
25. lmk / idk / kinda / "or whatever": at most one per ~300 words, two only in a long bullet, never three in a paragraph; "lmk" once per page; "idk" only for a fact you don't have, never for a judgement.
26. If his docs already cover the topic, the draft is his lines byte-for-byte plus what is new. No rewording of a real aside, no reordering of a real sentence, no flipping of its cause and effect, no fusing facts from two pages.
27. A config line is in a fenced code block with its leading backtick, never inline.
28. No curtain line ("That's the whole story."), no teaser ("next up"), no seesaw contrast, no "honestly" on a number; a published number is stated with its source, not staged as a discovery.
29. The brief's feature and failure fit the hardware in 5.1 (two INA219s, a molded TRRS plug into a jack, a DPDT switch, `ROUTABLE_BUFFER_IN`); if they don't, the copy leaves that fact out and the note under the draft says so (#31); if the fact is the point of the brief, the draft goes back.
30. The self-doubting asides in 4.4 are single-use: a new aside is about the actual state of the actual code in the brief, or there is none.
31. No `[CHECK: ...]` in the reader copy. Every hole is filled from the brief or the sentence is left out, and the note goes under the draft, as a note, never with "he" or "the brief" in a sentence that could ship. If the hole is the point of the brief (the fault, what the command measures), the draft goes back; there is no passing copy.
32. Longest sentence about 75 words (his is 74, the `remove` bullet, with two parentheses). Over 45 words, his carry a parenthesis 7 times in 9, and the 2 that don't are section leads stating one mechanism, not comma chains of instructions. A paragraph that is one 90-113 word comma splice with 10+ spans and no short line beside it is the synthetic register; split it under a `##`.
33. A design-decision aside lists the options and says he tried them. No "(I had it doing X for a while ... so now Y)", no argument for the winner, no history the brief didn't give.
34. Firmware verbs are literal (find, connect, disconnect, print, clear, take you back, remove); no grab / pokes around / knock out / drop it in here / hung off / picked out / sitting right there / down there. One "spit you back out" per page at most.
35. No negation-correction opener ("X doesn't Y by itself, you have to Z"; "The rails aren't stuck at ..."). Open on what the thing is or what you do.
36. A guess is one clause ("that's a guess"); a new feature's caveat names a concrete omission or bug, not a confidence level ("wouldn't put much weight", "N days old"); no reassurance tail after "should" ("and stay there until you move it"); no punchy verdict on a state ("Do nothing and it should just unhighlight.").
37. Logs: "To be continued with X" only when X is the next titled part of a series you are writing; otherwise end on the last fact, a flat line, or "let me know". No beat on every sentence, no inversion ("X is where I finally noticed"), no Ω arithmetic restated without "Datasheet says".
38. An aside of his, of any length, stays in his sentence; if his sentence isn't in the draft, neither is the aside.
39. A number he stated is given once, with its source; where his statements differ (14.2V in issue 20, 14.6V in the README), pick one and name where it is from.
40. A reply opens flat, gives the config line when his docs hold one for the thing asked about, links with full URLs in markdown mid-sentence, and closes with "Let me know if that works for you." or a question, never an imperative.
41. A "one paragraph, no headers, no bullets" brief on a topic his pages cover is met by his bullets without their dashes or his glossary lines, one sentence each; it never licenses a monolith or a paraphrase.
42. Last: put the draft between two real paragraphs of the same register from section 12.5 and read all three. If yours is the tidy one, go back to #19 and #20.

---

## 12. Evidence appendix

Citations in the order of the sections above, keeping the ones that are not already quoted inline in sections 3-9, plus the whole paragraphs for the comparison step in 12.5. Docs = `docs_july2025/`, README = `readmes/`.

### 12.1 Portrait and registers (sections 1 and 3)

Portrait, the floor of the voice:
- "I think I may have left some silly change in the code from debugging something else that isn't connecting Net 0 GND, there's a for loop somewhere starting from 1 instead of 0." - https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783852086

Docs = support-reply register:
- "Enter `n` in the menu to show this one. If you have anything that's doing any measurement (`gpio` input or `ADC`s), it'll stay up and live update if any of them change." - docs 07-debugging.md
- "Hey, the bug should be fixed in the latest release. Just download firmware.uf2 from the releases page and it should work better. Still do the bodge though, it assumes you've done it." - https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783916276
- "Type '0' then Enter to turn them all off. Then 'm' and Enter to return to the main Menu" - https://hackaday.io/project/191238/log/222858-getting-started-using-your-jumperless

Register fences:
- social only: "Holy shit youguise, I think I cracked it." - social_posts.txt (Bluesky 2025); "**package voice** I'm in." - Mastodon, 2025
- campaign only: "La Résistance" / "Doggy Doggy, What Now?" - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/a-farewell-to-campaigns; "Rawssbar Switching" - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/time-to-get-excited; "Love," then "Kevin" (5 of 8 updates)
- hackaday only: "Okay now back to the past...." - https://hackaday.io/project/191238/log/221542-boxes-within-shirts-within-boxes; "So we're just gonna pick our own colors." - https://hackaday.io/project/191238/log/222810-the-code-part-4-picking-colors-and-putting-them-on-your-retinas

Backticks stay in the docs:
- counts: about 260 spans in 13 docs pages (234 on the 11 hand-written); 0 in hackaday_project_logs.txt; 0 in social_posts.txt; 1 in crowdsupply_campaign_and_updates.txt; under 10 in github_issues_and_comments.txt

### 12.2 Sentence-level rules (section 4)

Length, flat landings, raggedness (4.1):
- "So yeah, fixed." - https://github.com/Architeuthis-Flux/Jumperless/issues/5#issuecomment-1627395775
- the 7-word lines beside the long ones: "Click the button again to get out." / "and the logo should turn reddish" - docs 01-basic-controls.md; "You can just paste this into the main menu:" - docs 04-oled.md
- the two 50-word sentences with no parenthesis, both section leads stating a mechanism: "**Why Select mode?** `Measure` mode allows the probe tip to be ±9V tolerant and routable like any other node, but as of yet, the code to actually do anything with it is unwritten so it just connects to DAC 0 and outputs 3.3V just like it was in `Select` mode." - docs 01-basic-controls.md; "`DAC 0`'s output is hardwired to go through a `current sense` shunt resistor, so when `DAC 0` is powering the `probe LEDs`, they'll be drawing some current I can measure with one of the `INA219`s, and therefore I can be reasonably confident that the switch is in the `select` position." - docs 09-odds-and-ends.md
- counts over 185 hand-written docs sentences: 32 under 10 words, 64 at 10-20, 47 at 20-30, 33 at 30-45, 8 at 45-60, 1 over 60; of the 9 past 45 words, 7 contain a parenthesis; densest sentence 9 spans in 74 words; 10 sentences with 6 or more spans

Comma joint, no dashes (4.3):
- "It's pretty loose with what it accepts, just make sure the last bridge ends with a comma." - https://github.com/Architeuthis-Flux/Jumperless/issues/25#issuecomment-1888338761

Parenthetical aside (4.4):
- "To connect the data lines to the Jumperless' GPIO 7 and 8, just use the menu option `.` (that's a period)." - docs 04-oled.md
- "For now, the best way to flash code is with a second USB cable, the Jumperless will reset the Arduino each time you change the wiring (I can change it if you don't want it to do that, or just cut the two solder jumpers labeled Reset.)" - https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1784154874
- "(okay, minus a few thousand for the rest of the firmware.)" - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/jumperless-probelessly
- the design-decision aside, and the timeout left open: "(there were some choices here, like make each button assigned to high / low or allow removing them, but this felt like the best way after trying them all)" / "(I need to settle on a good time for this, if it feels too short or long lmk)" - docs 01-basic-controls.md; the only "I had it" in the corpus, not the construction: "Thing is, I had it working 6 hours before this arrived, and was adding and removing turns trying to get a few extra percent efficiency." - social_posts.txt (Bluesky)

Openers (4.5):
- "Go to `Apps.h` and declare your function where you'll write your app" - docs 11-WritingApps.md
- "Yeah that shouldn't be happening. First, let me know your name so I can ship you out a fresh one and parts to fix the old one." - https://github.com/Architeuthis-Flux/Jumperless/issues/34#issuecomment-2221613644
- "@modi12jin In my experience, when weird things are happening with getting a huge voltage sag when pulling any current, it's because I've messed up the addressing somehow" - https://github.com/Architeuthis-Flux/breadWare/issues/1#issuecomment-1603142325
- "@nilclass Hey, your case has been sent out, it should be there sometime this week." - github_issues_and_comments.txt (Jumperless issue 15 thread)
- no negation-correction: "The `connect`/`measure` switch is a Dual Pole Dual Throw (DPDT) switch." - docs 09-odds-and-ends.md; "To change any persistent settings, there's a `config` file." - docs 06-config.md

Closers (4.6):
- "just go to the directory in a terminal and run the script in [tabby](https://tabby.sh/) or whatever" - docs 03-app.md
- "Just use any Terminal Emulator, like [PuTTY](https://www.putty.org/), [coolterm](https://freeware.the-meiers.org/), [RealTerm](https://learn.sparkfun.com/tutorials/terminal-basics/real-term-windows) or whatever." - https://github.com/Architeuthis-Flux/Jumperless/issues/32#issuecomment-2203009878
- a standalone log's last line: "Probably should have thought of this before spending $40 on effectively the same thing." - https://hackaday.io/project/191238/log/221542-boxes-within-shirts-within-boxes

should / just / kinda / idk, and rates (4.7):
- "They should friction fit into the SBC/SMD/OLED board included with your Jumperless V5." - docs 04-oled.md
- "This _should_ be fixed in the latest release, but let me know if you still run into issues." - https://github.com/Architeuthis-Flux/JumperlessV5/issues/35#issuecomment-3362453352
- the one docs line with two tics: "- Launch scripts included to easily run it from your favorite terminal emulator and not just the system default (terminal.app on macOS, Powershell on Windows, idk on Linux), just go to the directory in a terminal and run the script in [tabby](https://tabby.sh/) or whatever" - docs 03-app.md
- "The main thing is that there's a lot more interaction that can be done outside of any particular mode (like not probing and the logo is rainbowy, I'm gonna call this idle mode here until I think of a good name)" - docs 01-basic-controls.md (a name decided, not wrung)
- counts: "lmk" 2 (docs) and 0 elsewhere; "let me know" 18 replies, 16 hackaday, 3 campaign, 5 social, 1 docs; "idk" 2 docs, 13 social; "kinda" 5 docs; "or whatever" 3 docs; "knock on wood" 1; "3ish" 1

Terminal punctuation (4.8):
- "we've got colors now!" - docs 03-app.md (the only docs exclamation)

Emphasis, and numbers never in backticks (4.9):
- "**Remember the probe is read by a resistive voltage divider**, so putting your fingers on the pads (or the back sides of the 4 risers that connect those `probe sense` boards to the main board), or anything causing the probe tip not to be at a steady 3.3V will give you weird readings." - docs 01-basic-controls.md
- "`ADC`s", "`pad`s", "`DAC`s" - docs 07-debugging.md, 01-basic-controls.md, 09-odds-and-ends.md
- config lines in fenced blocks: "If you want to use this all the time, there's a config option to connect the OLED on startup. You can just paste this into the main menu:" / "`[top_oled] connect_on_boot = true;" - docs 04-oled.md; "copy / edit / paste any of these lines" / "`[dacs] bottom_rail = 0.00;" / "`[dacs] limit_min = -8.00;" - docs 06-config.md

### 12.3 Vocabulary and facts (section 5)

Vocabulary:
- "`bridge` = a pair of exactly two `node`s (this is what you're making when you connect stuff with the probe, enter `s` to print the (kinda misnamed) `node file`s to see a list of bridges)" - docs 99-glossary.md
- "There are two kinds of presses, `click` (short press) and `hold` (long press). In general, a `click` (short) is a `yes`, and a `hold` (long) is a `no`/`back`/`exit`/`whatever`." - docs 01-basic-controls.md
- "I've made up terms for things here that may or may not be the formal definition, so I should probably let you know what I chose." - https://hackaday.io/project/191238/log/222353-the-code
- "They should friction fit into the SBC/SMD/OLED board included with your Jumperless V5." - docs 04-oled.md; "to multiplex 3.3V, GND, LED data, 2 buttons, and a +-9V tolerant analog line over the 4 wires on a TRRS cable" - docs 09-odds-and-ends.md

Literal firmware verbs:
- the one figurative one: "spit you back out to `idle` mode once you've made a connection to another row" - docs 01-basic-controls.md
- "poke" for the tip, "grab" for the app: "poke out connections with the tip" - README JumperlessV5_README.md; "Just grab the app again from the [latest release](https://github.com/Architeuthis-Flux/Jumperless/releases/latest) and let me know if that works for you." - https://github.com/Architeuthis-Flux/Jumperless/issues/32#issuecomment-2214679003

Facts he wrote down, and not guessing (5.1, 5.2):
- "So, you absolutely can do one with more stages to get more nodes, just keep in mind that every switch you go through adds another 45 ohms." / "Datasheet says Vdd - Vss is max 14.2V (which gives 65ohms on resistance, and I'm running them at Vdd - Vss ~18.5V to get that down to 45 ohms." - https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1879196708
- "You may notice that these values are well outside the absolute maximum ratings (14.6V and 10mA per connection) listed in the CH446Q datasheet. That's because they are, all the specifications of the CH446Q get better as the supply voltage increases, so I'm exploiting the arcane weirdness of CMOS to get closer to an ideal switch." - README JumperlessV5_README.md
- "float probeVoltage = readAdcVoltage(7, 8); //ADC 7 is hardwired to the probe tip (in measure mode), so it's this easy" - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/jumperless-probelessly
- "addBridgeToNodeFile(ISENSE_PLUS, 9, netSlot, 0, 0);" / "addBridgeToNodeFile(ISENSE_MINUS, 28, netSlot, 0, 0);" - code pasted in https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/time-to-get-excited; "//Current Sense+ - Yellow" / "//Current Sense- - Blue" - 2023 colour table, hackaday_project_logs.txt
- "I switched back to TRRS because the third ring wasn't strictly necessary and the back end of the plug is a bit too long to make these as low profile as I would like." / "they told me the molds they used to make these are "used up", but they'd be happy to make a new injection mold and do them in pink" - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/time-to-get-excited
- "The Jumperless's probe is set up so it'll work fine with a 4-pin TRRS, but the 5-pin lets me avoid a lot of hacky code nonsense to multiplex the LED data line with 2 buttons." - social_posts.txt
- "The connections are fully analog (internally a CMOS switch) and can handle ±9V (up to ±12V if you raised the supply voltages), with an on resistance of ~75Ω." - hackaday_project_logs.txt (early Jumperless log; the scrape stores ± and Ω as HTML entities, unescape before grepping)

### 12.4 Explaining and instructing (section 6)

Order, key-first (6.1, 6.2):
- "1. Hold the USB Boot button and plug the Jumperless into your computer." / "2. A drive should pop up called RPI-RP2. Drag the firmware.uf2 file into it and it should reset and you're done!" - https://hackaday.io/project/191238/log/222858-getting-started-using-your-jumperless

you can / just (6.3):
- "You can read it with `~` and edit settings by copying any of those lines, pasting it back, and changing the value to whatever you want it to be." - docs 06-config.md
- "Just use the standard LQFP44 footprint, it will be much easier to solder, I just had to make mine smaller so they'd fit on a really dense board." - https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1880179763

Snag inside the step, one snag not a ladder (6.4):
- "You can trigger them to regenerate if you messed them up by deleting it with `x`, and then entering `m` to create new copies of any examples it doesn't see." - docs 08-file-manager.md
- "Note that this won't run correctly from anywhere but your Applications folder, so drag it there." - https://hackaday.io/project/191238/log/222858-getting-started-using-your-jumperless
- "(Github doesn't allow UF2s here so you'll need to unzip it). This takes like 3ish minutes, so when you drop this UF2, wait until the drive pops up again, then load the firmware from releases." - https://github.com/Architeuthis-Flux/JumperlessV5/issues/17#issuecomment-3027899213

Why, and capped implementation depth (6.5):
- "**Why Select mode?** `Measure` mode allows the probe tip to be ±9V tolerant and routable like any other node, but as of yet, the code to actually do anything with it is unwritten so it just connects to DAC 0 and outputs 3.3V just like it was in `Select` mode." - docs 01-basic-controls.md
- "But you don't really need to worry too much about all that backend stuff." - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/jumperless-probelessly

Bugs stated inline (6.7):
- "as of yet, the code to actually do anything with it is unwritten" - docs 01-basic-controls.md
- "In another installment of "how tf did that ever work?", looking at the code, for some reason I was expecting serial data to be available when the DTR line was pulsed to trigger flashing." - https://github.com/Architeuthis-Flux/JumperlessV5/issues/22#issuecomment-3189012928

Alternatives last (6.8):
- "If you need both `DAC`s, you can just get rid of this connection and the `probe LEDs` won't light up, but other than aesthetics, it really has no effect on functionality. Or you connect `ROUTABLE_BUFFER_IN` to a `GPIO` and set it `high` and just lose the ability to sense where the switch is." - docs 09-odds-and-ends.md (last paragraph of the page)
- "If you don't want to use Wokwi, this is a rundown of the alternative ways to control your Jumperless." - https://hackaday.io/project/191238/log/222858-getting-started-using-your-jumperless

Analogies (6.9):
- "You can think of `special functions` just like any other `node`, the only difference is they're in a sort of "folder" so I didn't need to put a dedicated pad for each of them." - docs 01-basic-controls.md
- "Read up on [Telephone Exchanges](https://en.wikipedia.org/wiki/Telephone_exchange). Because that's basically what's going on with this, all the same ideas apply (the only difference is that you also want to minimize the number of switches a signal goes through because of the on resistance.)" - https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1874483799
- "*Jumperless V5 is that pair of X-ray spectacles.*" - README JumperlessV5_README.md (pitch copy, not a how-to sentence)

The topic is already written, quote it (6.11):
- "`slot` = one of the 8 node files stored that you can switch between with `<`/`>` or the `menu`s. Named `nodeFileSlot[0-7].txt` (there's no actual limit, there's *so* much flash storage on this thing, but by default it's 8)" / "`node file` / `slot file` = this is an actual text file on the filesystem that stores the list of bridges, there's one of these for each `slot` (enter `s` to see all of them, they start with an `f {` to make it east to just copy paste them from the terminal)" - docs 99-glossary.md
- "  - Also the color assignments are saved to a file for each slot, so they should work after a reboot and when changing `slots`" - docs 01-basic-controls.md
- "- **Tapping nets highlights them** as before, but there's a slightly different animation on the `row` you have selected from the whole `net`" / "- if the highlighted row is a `measurement` (`gpio input` or `adc`) it will print the state to serial and the oled" - docs 01-basic-controls.md

### 12.5 Whole paragraphs to compare a draft against, by register

Docs (use these two for the comparison step in "How to use this"):
- the 74-word bullet then the 10-word tag: "`remove` will briefly turn the `row` reddish `warn` (I need to settle on a good time for this, if it feels too short or long lmk), another `remove` press will remove that `row` (just like in `probe` mode, it removes the `bridge` it's in, so just things that have a direct connection to that `row`, not the whole `net`), if you let it time out without pressing anything, the row will be unhighlighted. TL;DR, double click `remove` to remove, single click to unhighlight." - docs 01-basic-controls.md
- the ragged paragraph the judges took for his in round 3, three sentences of 24, 38 and 42 words: "When you switch to `measure` mode, those roles get swapped, the LEDs are powered by that `GPIO`, and the probe tip is now `ROUTABLE_BUFFER_IN`. In the current firmware, that just stays at 3.3V so you can *kinda* sense pads in either mode (you may notice the sensing is a lot wonkier, that's because the `DAC` isn't perfectly calibrated to output *exactly* 3.3V.) But in the future, there will be some other stuff you can do in that mode treating it as an analog line (and of course, I'll forget to update this, if it's after like June 2025, double check this is still true.)" - docs 09-odds-and-ends.md
- a whole section: "## Connection" / "To connect the data lines to the Jumperless' GPIO 7 and 8, just use the menu option `.` (that's a period). It will try to find the OLED on the I2C bus, after a few failed attempts, it'll automatically disconnect to free up GPIO 7 and 8." - docs 04-oled.md

Replies:
- "Hey, not to worry. It sounds like it just has garbage on the filesystem and is locking up trying to read it (but that's also a thing I should fix in the code.)" ... "It should do an auto calibration on first startup and hen you should be good. Let me know if that works." - https://github.com/Architeuthis-Flux/JumperlessV5/issues/17#issuecomment-3027899213
- "It might not be permanently damaged so let's do some troubleshooting." / "- Is one particular chip much hotter than the others?" / "I'll try to think of more possible causes. But these should get us started in the right direction." - https://github.com/Architeuthis-Flux/Jumperless/issues/34#issuecomment-2221613644
- "It stores what connections are made and what's available so it knows not to merge things that shouldn't be. Those are defined in [JumperlessNano/src/MatrixStateRP2040.cpp](https://github.com/Architeuthis-Flux/Jumperless/blob/main/JumperlessNano/src/MatrixStateRP2040.cpp) if you want to have a look at the state, the nitty gritty logic of the pathfinding, you can check that out in [JumperlessNano/src/NetsToChipConnections.cpp](https://github.com/Architeuthis-Flux/Jumperless/blob/main/JumperlessNano/src/NetsToChipConnections.cpp)." - https://github.com/Architeuthis-Flux/Jumperless/issues/20#issuecomment-1874437417
- "Okay, I've reworked the app to check whether you're connected to the internet sooner so it won't try to connect to Wokwi and crash." / "Just grab the app again from the [latest release](https://github.com/Architeuthis-Flux/Jumperless/releases/latest) and let me know if that works for you." - https://github.com/Architeuthis-Flux/Jumperless/issues/32#issuecomment-2214679003
- "I think I may use a couple (or 3) of these CH446s for the control board (to save space) and leave the MT8816s on the top side, after some discussion with non-techy people, they all liked the weight that those huge PLCC chips add to it. And having a huge ceramic package might help dissipate more heat so we can run them a bit further out of spec than we already are." - https://github.com/Architeuthis-Flux/breadWare/issues/1#issuecomment-991926125

READMEs:
- "V5 is a major redesign of the original [Jumperless](https://github.com/Architeuthis-Flux/Jumperless). Having a few hundred people out there using Jumperlesses, sharing ideas, and [writing their](https://github.com/nilclass/jlctl) [own apps](https://github.com/nilclass/jumperlab) gave me a long enough list of things I wish I had done that I felt it was time to push the design even further. Now that the fundamentals are battle-tested (switching matrix, power supply, routing algorithm), Jumperless V5 can add some even crazier new stuff like; an ungodly number (445) of LEDs, a built in rotary encoder/switch, daisy chain headers, individually programmable power rails, and an isolated, always-on probing system." - README JumperlessV5_README.md
- "(supplies and measurement are all good to +-8V), or 10 GPIO (4 are 5V logic, 6 are 3.3V. All 10 can instead be routed to another daisy-chained Jumperless as fully analog connections.)" - README JumperlessV5_README.md
- "So here's the second board revision. I was showing the [last version](breadWare/v0.1-alpha/) off to someone and they offhandedly mentioned that it would be cool if the whole thing fit under the breadboard. I knew this was my plan all along, but it forced me to finally design it before the code gets too specific to the original off-the-cuff design and I get stuck with my poor ~~life~~ design choices." - README breadWare_README.md

Logs:
- "Super gluing a craft knife blade to 3D printed cube I had laying around. I taped a piece of the cardboard to the bottom before gluing to set the depth. I can just drag it along a ruler and it cuts to the right depth. Probably should have thought of this before spending $40 on effectively the same thing." / "Okay now back to the past...." - https://hackaday.io/project/191238/log/221542-boxes-within-shirts-within-boxes
- "Like these people do realize you can name variables after what they do, right? And these are the Official examples in the datasheet. Anyway after a few days of staring at what looks like gibberish, it starts to click." - https://hackaday.io/project/191238/log/222626-the-code-part-3-driving-the-ch446qs
- "This is just to give people a but of an understanding of what's going on inside a crosspoint switch. Not really a demo, but it was made so people understand that the Jumpeless isn't reading and simulating your signals, just passing them through an analog CMOS switch." - https://hackaday.io/project/191238/log/223466-doom-and-some-other-less-trivial-demos
- "There are comments in the code but there are a lot of nested array things that can get pretty confusing, if you need help understanding what's going on in a particular function, let me know and I'd be happy to walk you through it." - https://hackaday.io/project/191238/log/222530-the-code-part-2-pathfinding

Campaign updates:
- "The lead times are a bit long (6-8 weeks and this was about five weeks ago), and I wasn't about to hold up shipping on account of the cables, so I had them send me their existing inventory of 100 black ones to hand paint myself." / "Of course that's a guess, but it feels reasonable enough. There haven't been any serious unexpected delays (knock on wood), just my insistence that I should probably do one more round of shaking out potential hardware bugs before these ship." / "I will paint and glitter the probe cables (yes, I do these by hand one at a time, none of the samples I had made look right.)" - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/time-to-get-excited
- "Boxes of assembled Jumperless V5s start showing up at my house (which is more factory than house at this point), I attach the click wheel caps, plug in the probes, thoroughly test each board, and lovingly pack each one into their boxes." / "TL;DR" / "We're shipping in April!" - same update
- "This community really has brought together some of the chillest, most interesting people I've ever met. So come hang out on Discord or in our Forum and ask them about their experiences with the OG Jumperless." - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/our-campaign-is-go-for-launch
- "Hapax LEGOmenon" / "Very much a "why not?" feature I hope someone will do something awesome with. Note: both sides are holes, there's nothing sticking out on the other side." - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/good-news-everyone-things-are-happening
- house-edited, not his punctuation: "You can connect any point to any other using software-defined jumpers, so the four individually programmable ±8 V power supplies; ten GPIO; and seven management channels for voltage, current, and resistance can all be connected anywhere on the breadboard or the Arduino Nano header." - the campaign page, pasted into README JumperlessV5_README.md and docs index.md; "Jumperless V5 can sniff or write any UART, I²C, SPI, or MIDI signals on the board." - the campaign page

### 12.6 Humor and attitude (section 7)

- humor slot: "(This one is so fucking sick)" - docs 03-app.md; "(jk it's a carrying case, but make sure you can get it back open before you put your Jumperless in it)" - README Jumperless_README.md
- self-deprecation targets process: "It probably looks like nonsense to you but I've been in it so long it makes perfect sense to me." - docs 07-debugging.md; "Turns out designing acrylic stuff that a human can assemble and stays together is hard and also I suck at it." - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/time-to-get-excited; "Us hardware / firmware people should *not* be trusted with shipping desktop software." - https://github.com/Architeuthis-Flux/JumperlessV5/issues/19#issuecomment-3052839483
- enthusiasm with bias admission: "But that's like the *least* cool thing the new app can do, here's a list of what's new:" - docs 03-app.md; "It's called Jumperless and I think it's pretty rad, but I'm probably biased." - social_posts.txt, Bluesky 2023-09-11; "I get reminded how much freaking fun these things are. Of course I'm totally biased because it's my baby" - https://www.crowdsupply.com/architeuthis-flux/jumperless-v5/updates/good-news-everyone-things-are-happening
- puns only in headings: "Hapax LEGOmenon" - good-news-everyone update; "Jethamphetamine async leds" - https://github.com/Architeuthis-Flux/JumperlOS/pull/2 (PR title); "Look *Inside* your Jumperless" - docs 07-debugging.md (the only docs joke heading)
- ownership, credit, "on me for" is rare: "That's on me for not writing the revision number on the boards, you can tell by the location of the ADC (on Rev 3 it's in place of the Nano Disconnect solder jumpers)." - https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783874751; "so it's totally on me for not actually searching for the right field and just assuming it would be the second one." - https://github.com/Architeuthis-Flux/Jumperless/issues/23#issuecomment-1879935990; "Ah shit, Wokwi added a README.md to their projects, which moved the index where the diagram.json is stored." - same reply; "Don't feel bad, I've spent hours trying to fix what I thought was a routing bug that ended up being exactly this." - https://github.com/Architeuthis-Flux/Jumperless/issues/33#issuecomment-2203450289; "Pro tip: be nice to the people making your stuff." - good-news-everyone update
- delays narrated: "First of all, sorry I haven't sent one of these updates in a while." - good-news-everyone update (the only kind of "sorry"); "Honestly it's a huge relief that people don't seem to be nearly as worried about the tight deadline I set for myself." - same update; "I honestly can't believe that PID was available, ha." - github_issues_and_comments.txt ("honestly" marks surprise at luck)

### 12.7 Shapes (section 8)

- docs section and page: "## Connection" paragraph above (12.5); page ending: "Or you connect `ROUTABLE_BUFFER_IN` to a `GPIO` and set it `high` and just lose the ability to sense where the switch is." - docs 09-odds-and-ends.md; "That's probably more than you need to worry about but that gives me a nice start on real docs" - docs 99-glossary.md
- README: "##### If you want one of these, they're available in [my Tindie store](https://www.tindie.com/products/architeuthisflux/jumperless/)" / "# There's now a way cooler version, [Jumperless V5](https://github.com/Architeuthis-Flux/JumperlessV5)" - README Jumperless_README.md; "###### Just pretend this has an audio cable stuck to the back and it's sitting on a V5" - README JumperlessV5_README.md; "Here's an example of me using this thing to connect some I2C pins from an Arduino to an OLED" - README Jumperless_README.md; "If you have some feature you want to add, I'm happy to help. Either by just adding it myself or walking you through the relevant bits of code to make it happen." - README JumperlessV5_README.md
- reply: "Hey, so I just got a bunch of cases in, and I already have your address so I'm gonna send you one." - https://github.com/Architeuthis-Flux/Jumperless/issues/15#issuecomment-1857055402; "Thanks for putting in this issue! I think I may have left some silly change in the code from debugging something else that isn't connecting Net 0 GND" - https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783852086; photo asks: "Or just send a pic of your setup." / "Send a pic of the top of the board too, I'm interested in the big tantalum capacitors under the Nano header." / "If you want, send me close up photos of the front and back of the board and I might be able to spot the issue." - issue 34 thread
- campaign update: "TL;DR: The first batch of Jumperless V5s will be shipping to me this week and will be on their way to you shortly thereafter." - time-to-get-excited; "So feel free to ask me for anything you want, either on the Jumperless Discord, Forums, GitHub, Twitter/X, Bluesky, Mastodon, whatever. All feature requests go to the same place anyway, on a piece of gaffer tape in metallic Sharpie stuck to my desk." / "Cordially," - jumperless-probelessly; "There's *sooo* much new shit in here, even though to an end user it shouldn't really look much different, just a bit snappier and (hopefully) stable." - https://github.com/Architeuthis-Flux/JumperlOS/pull/1
- hackaday log: "The datasheet is kinda vague about how, but it turns out it's just a kinda weird version of SPI." - https://hackaday.io/project/191238/log/222626-the-code-part-3-driving-the-ch446qs; "This turned out to be surprisingly complicated, I basically spent 2 days just tweaking the values until it looked right." - https://hackaday.io/project/191238/log/222810-the-code-part-4-picking-colors-and-putting-them-on-your-retinas; "I was expecting this not to work, but surprisingly, it did." - https://hackaday.io/project/180394/log/194325-early-proofs-of-concept; "In the original layout if I wanted to connect top row 5 to bottom row 5, it would always take 2 hops to do that (and these switches each have an on resistance of about 65Ω)." - README breadWare_README.md and the breadWare v0.2 log; "That's all I got about the LEDs, if you want me to be clearer about something, let me know and I'll add to this log." - the colours log

### 12.8 What he never does (section 9)

- "boring stuff": "It's not just about being too lazy to plug in some jumpers." / "It's about cutting down on the debugging bullshit and letting the grander plans for what you're building flow freely." - README JumperlessV5_README.md; "it would be a shame to ship them with boring USB cables." - https://hackaday.io/project/191238/log/223752-any-sufficiently-extra-technology-is-indistinguishable-from-a-barbie-oppenheimer-crossover-meme-glittering-usb-cables; "I want Jumperless V5 to feel like you can throw anything at it and it'll just do what you want." - jumperless-probelessly update
- "robust" only as a fix comparative: "I'm working on a more robust fix in firmware that will work on both revisions right now" - https://github.com/Architeuthis-Flux/Jumperless/issues/13#issuecomment-1783874751
- "simply" only in pitch copy: "it simply acts as a regular terminal emulator like PuTTY, xTerm, Serial, etc." - README JumperlessV5_README.md
- the one preamble in the corpus: "This guide covers how to write, load, and run Python scripts that control Jumperless hardware using the embedded MicroPython interpreter." - docs 08-micropython.md (templated page)
- the one "weird thing" construction, social, not a reveal: "The weird thing is this would probably work an 8-bit ADC, the part that actually matters is the precision of the resistors" - social_posts.txt
- "awesome" about others: "These chips were handed to me as samples by the awesome people at the Raspberry Pi booth at DEFCON." - crowdsupply_campaign_and_updates.txt; "so you could use their awesome Community Firmware" - README breadWare_README.md
- the contrast in one flat clause, and the number in passing: "For most circuits, this really doesn't have a noticeable effect." - README JumperlessV5_README.md; "(and these switches each have an on resistance of about 65Ω)" - README breadWare_README.md
- counts: "That's the whole story" 0 in his hand ("That's the whole point." only in the excluded KnoBLE README); "next up" 0; "whole story" 0; "nitty gritty" 1; "or something like that" 2; "Thanks for putting in this issue!" 1
