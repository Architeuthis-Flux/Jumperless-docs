# Jumperless Documentation Review & Recommendations

## Summary

Review of Jumperless-docs against current firmware implementation (JumperlOS) to identify missing, outdated, or incomplete documentation.

**Date:** October 2024  
**Firmware Version:** 5.2.x  
**Docs Repository:** github.com/Architeuthis-Flux/Jumperless-docs

---

## ✅ Well-Documented Features

These features are properly documented and up-to-date:

1. **Basic Controls** (01-basic-controls.md) ✅
   - Probe usage (connect/remove modes)
   - Click wheel interactions
   - Special functions (DAC, GPIO, UART)
   - Idle mode net highlighting
   - Color picker
   - GPIO toggle functionality

2. **The App** (03-app.md) ✅
   - Installation guide for all platforms
   - Arduino flashing from Wokwi
   - Local Arduino sketch support
   - Terminal compatibility

3. **Arduino Features** (05-arduino.md) ✅
   - UART passthrough
   - Quick connection shortcuts (A/a commands)
   - Automatic flashing
   - Commands from routable UART

4. **Configuration** (06-config.md) ✅
   - Config file format
   - Viewing configuration (~)
   - Editing settings
   - Configuration help (~?)

5. **Debug Views** (07-debugging.md) ✅
   - Crossbar array view (c command)
   - Bridge array view (b command)
   - Net list view (n command)

6. **File Manager** (08-file-manager.md) ✅
   - Navigation controls
   - File operations
   - Text editor (Kilo-based)
   - USB Mass Storage mode
   - MicroPython examples

7. **Glossary** (99-glossary.md) ✅
   - Key terms defined
   - Net, node, row, rail, bridge, path
   - Slot files mentioned

---

## ⚠️ Missing Major Features

These features are implemented in firmware but not documented in user docs:

### 1. **Wokwi Diagram Import (W Command)** - MISSING

**Implementation:** Fully functional in firmware  
**Command:** `W`  
**Documentation:** CodeDocs/WOKWI_PARSER_GUIDE.md exists, but no user-facing docs

**What's missing:**
- How to import Wokwi diagrams via `W` command
- Paste mode vs file mode
- Supported Wokwi components (breadboard, logic analyzer, Arduino Nano)
- Wire color preservation from Wokwi
- Rail voltage detection from text labels
- Pin mapping (Wokwi pins → Jumperless nodes)

**User workflow:**
```
1. Design circuit in Wokwi.com
2. Copy diagram.json content
3. Type W in Jumperless
4. Paste JSON
5. Circuit applied to hardware
```

**Where to document:** Needs new section "02-importing-from-wokwi.md" OR subsection in 03-app.md

---

### 2. **Slot System** - INCOMPLETE

**Implementation:** 10 slots (0-9) with YAML format  
**Current documentation:** Mentioned in glossary only

**What's missing:**
- **How many slots:** Glossary says 8, firmware has 10 (0-9)
- **Slot cycling commands:** `<` and `>` not documented
- **Slot management:** Load, save, delete operations
- **Slot query:** `Q` command returns active slot
- **Slot notifications:** `SLOT_CHANGED:X` messages
- **YAML format:** Slot files are now YAML, not just text
- **Active vs inactive slots:** Only active slot affects hardware

**User workflows:**
```
# Cycle through slots
< or >    # Move to next/previous slot

# Query active slot
Q         # Returns ACTIVE_SLOT:X

# Load specific slot
l 5       # Load slot 5

# View all slots
s         # Show slot list

# Save to slot
(after making connections)
Connections auto-save to active slot
```

**Where to document:** Needs section "02-slots-and-states.md" OR expand glossary into full section

---

### 3. **State Management & YAML Format** - MISSING

**Implementation:** Complete state system with YAML files  
**Documentation:** None in user docs

**What's missing:**
- **File format:** Slot files are YAML (.yaml), not .txt
- **File location:** `/slots/slotN.yaml`
- **YAML structure:** bridges, power, config, display sections
- **Node names:** Named nodes (NANO_D5, TOP_RAIL, GPIO_1, etc.)
- **Manual editing:** Users can edit YAML files directly
- **Auto-refresh:** Changes to slot files auto-apply
- **Legacy migration:** Old .txt files auto-migrate to YAML

**YAML example:**
```yaml
version: 2
sourceOfTruth: bridges

bridges:
  - {n1: 1, n2: 10, dup: 2, color: red}
  - {n1: NANO_D5, n2: GPIO_1, dup: 2}

power:
  topRail: 3.30
  bottomRail: 2.50
  dac0: 3.33
  dac1: 0.00
```

**Where to document:** Section "02-slots-and-states.md" with YAML format reference

---

### 4. **Active-Only Updates** - MISSING

**Implementation:** Only active slot receives updates from apps  
**Documentation:** None

**What's missing:**
- App only updates currently active slot
- Wokwi diagrams can be saved to inactive slots without affecting hardware
- Zero-copy parsing for inactive slots (memory optimization)
- Need to cycle to slot to activate it

**User impact:**
- Safer - can't accidentally modify wrong slot
- Faster - no unnecessary hardware updates
- More predictable behavior

**Where to document:** Section "02-slots-and-states.md" or 03-app.md

---

### 5. **AsyncPassthrough Details** - INCOMPLETE

**Implementation:** Async UART passthrough with ring buffer  
**Current documentation:** Basic passthrough mentioned in 05-arduino.md

**What's missing:**
- Sync vs async passthrough modes
- Configuration: `async_passthrough` setting
- Performance characteristics
- Flood handling
- When to use each mode

**Config example:**
```
[serial_1] function = passthrough;
[serial_1] async_passthrough = true;
```

**Where to document:** Could expand 05-arduino.md OR add advanced section

---

### 6. **Service Architecture** - MISSING (Advanced)

**Implementation:** Priority-based service system  
**Documentation:** None in user docs

**What's missing:**
- What services are (background tasks)
- Service priorities (CRITICAL, HIGH, NORMAL, LOW)
- ProbeButton service (ultra-responsive button)
- When services run
- Why this matters (never misses button presses)

**User impact:**
- Explains why button is so responsive
- Explains why system doesn't freeze
- Background for custom app development

**Where to document:** Optional - advanced section OR 11-WritingApps.md

---

## 🔧 Outdated Information

Information that needs updating:

### 1. **Slot Count**
- **Current docs:** "8 slots (0-7)" in glossary
- **Actual:** 10 slots (0-9)
- **Fix:** Update glossary and any mentions of slot count

### 2. **File Format**
- **Current docs:** "nodeFileSlotN.txt" text format
- **Actual:** `/slots/slotN.yaml` YAML format
- **Fix:** Update all file format references

### 3. **Probe Switch Behavior**
- **Current docs:** "Measure mode code is unwritten" (01-basic-controls.md line 11)
- **Status:** Still accurate? Needs verification
- **Fix:** Verify current behavior and update

### 4. **Flash Mode API**
- **CodeDocs:** Describes flash mode API (`setFlashMode()`)
- **Status:** PROPOSED but not implemented
- **Fix:** CodeDocs correctly marked as "not implemented" - no user doc change needed

---

## 📝 Recommended New Documentation

Suggested new documentation files to add:

### Priority 1: Essential Features

**1. `02-slots-and-states.md`** - Slot system
```markdown
# Slots and States

## What are Slots?
10 saved circuit configurations (slots 0-9)

## Switching Slots
< = next slot
> = previous slot
Q = query active slot

## YAML Format
Manual editing guide

## Wokwi Import
Link to Wokwi section
```

**2. `02.5-importing-from-wokwi.md`** - Wokwi import
```markdown
# Importing from Wokwi

## What is Wokwi?
Online circuit simulator

## The W Command
How to import diagrams

## Supported Components
Breadboard, Arduino Nano, Logic Analyzer

## Pin Mappings
Wokwi → Jumperless translation

## Wire Colors
Color preservation
```

### Priority 2: Nice to Have

**3. Expand 05-arduino.md** - Add passthrough details
- Async vs sync modes
- Configuration options
- Performance notes

**4. Expand 11-WritingApps.md** - Add service architecture
- How services work
- Service priorities
- ProbeButton example

---

## 🎯 Quick Wins

Easy updates that would have big impact:

1. **Update glossary** - Fix slot count (8 → 10)
2. **Add W command** - Single paragraph in 03-app.md about Wokwi import
3. **Add < command** - Single paragraph about slot cycling
4. **File format note** - Mention YAML in 08-file-manager.md

---

## 📚 Documentation Organization

### Current Structure (Good)
```
01 - Basic Controls (probe, clickwheel, interactions)
03 - The App (installation, features)
04 - OLED (external display)
05 - Arduino (passthrough, flashing)
06 - Config (persistent settings)
07 - Debugging (views: crossbar, bridge, net)
08 - File Manager (filesystem, editor, USB)
08 - MicroPython (scripting)
09 - Odds and Ends (misc)
10 - 3D Stand (hardware)
11 - Writing Apps (development)
99 - Glossary (terms)
```

### Proposed Additions
```
01 - Basic Controls ✅
02 - Slots and States ⚠️ NEW
02.5 - Importing from Wokwi ⚠️ NEW (or subsection of 03)
03 - The App ✅ (expand with Wokwi details)
04 - OLED ✅
05 - Arduino ✅ (expand with passthrough details)
...
```

**Alternative:** Instead of new files, expand existing ones:
- Add Wokwi import to 03-app.md
- Add slot management to existing glossary or 07-debugging.md
- Add YAML details to 08-file-manager.md

---

## 🔍 Cross-Reference Opportunities

Documentation should link between related topics:

1. **App → Wokwi Import**
   - 03-app.md mentions Wokwi, should link to W command details

2. **Slots → File Manager**
   - Slot files visible in file manager
   - Can edit YAML manually

3. **Glossary → Full Sections**
   - Glossary mentions slots, should link to full slot documentation

4. **Arduino → Config**
   - Passthrough settings in config file
   - Link between 05-arduino.md and 06-config.md

5. **Basic Controls → Slots**
   - Making connections affects active slot
   - Should mention slot system

---

## ✨ Documentation Quality

**Strengths:**
- ✅ Excellent visual aids (screenshots, diagrams)
- ✅ Practical examples and workflows
- ✅ Good coverage of basic features
- ✅ Friendly, accessible tone
- ✅ Video demonstrations where helpful

**Areas for Improvement:**
- ⚠️ Missing coverage of slot system
- ⚠️ No Wokwi import documentation
- ⚠️ File format transition (txt → YAML) not explained
- ⚠️ Some outdated information (slot count)
- ⚠️ Advanced features not documented (services, async passthrough)

---

## 🎬 Action Items

### Immediate (High Priority)

1. **Update glossary** - Fix slot count and file format
2. **Document W command** - Add Wokwi import section
3. **Document < command** - Add slot cycling
4. **Document Q command** - Add slot query

### Short Term (Medium Priority)

5. **Create slots documentation** - Full section on slot system
6. **Explain YAML format** - User-editable format guide
7. **Expand Arduino docs** - Passthrough modes
8. **Add Wokwi pin mappings** - Reference table

### Long Term (Nice to Have)

9. **Service architecture** - Advanced topics
10. **State management internals** - For developers
11. **Memory management tips** - For custom apps
12. **Troubleshooting guide** - Common issues and fixes

---

## 📊 Statistics

**Current Documentation:**
- Total files: 15 markdown files
- Well-documented: 7 major features
- Missing: 6 major features
- Outdated: 3 items

**Comprehensive Firmware Docs (CodeDocs):**
- Total: 14 files (after consolidation)
- Comprehensive guides: 4
- Feature-specific: 4
- Reference: 3
- Supporting: 3

**Gap:** Firmware has excellent technical docs, user docs need feature coverage updates

---

## 🤝 Recommendations for Kevin

### Must Do
1. Add **Wokwi import (W command)** documentation - this is a marquee feature!
2. Add **slot cycling (< command)** documentation - users need to know about this
3. Update **slot count** (8 → 10) in glossary
4. Explain **YAML format** for advanced users who want to edit files

### Should Do
5. Create dedicated **slots section** (02-slots-and-states.md)
6. Add **Q command** (query active slot) for app developers
7. Document **active-only updates** behavior
8. Add **node name reference** (NANO_D5, GPIO_1, etc.)

### Nice to Have
9. Expand **Arduino passthrough** with async mode details
10. Add **service architecture** for app developers
11. Create **troubleshooting section** with common issues
12. Add **YAML examples** for common patterns

### Format Options
**Option A:** Create new files (02-slots-and-states.md, 02.5-importing-from-wokwi.md)  
**Option B:** Expand existing files (add to 03-app.md, expand glossary)  
**Option C:** Hybrid (Wokwi in app.md, slots get own section)

**My recommendation:** Option C - Keep app.md focused, give slots their own section since it's fundamental to the system

---

## 🎓 Documentation Principles

These docs follow good principles:
- ✅ User-focused (not implementation-focused)
- ✅ Practical examples
- ✅ Visual aids
- ✅ Progressive disclosure (basic → advanced)
- ✅ Consistent tone and style

Continue these practices when adding new sections!

---

**Next Steps:** Review this document, prioritize action items, and create new documentation sections for missing features.

