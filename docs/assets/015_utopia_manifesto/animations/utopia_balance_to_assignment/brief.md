# Utopia Balance to Assignment — Animation Brief

- Asset: `utopia_balance_to_assignment`
- In-game use: state-driven threshold transition toward Assignment in the Commonwealth Ledger.
- Gameplay surface: `interface/015_utopia_manifesto_ledger.gui`; the existing Choice–Assignment threshold column is 158 pixels wide.
- Frame size: `158x24`.
- Frame count: `8` genuine built-in ImageGen-authored states.
- Horizontal sheet size: `1264x24`.
- Playback: `5 fps`, `looping = no`, `play_on_show = yes`.
- Anchor: center; the instrument body and camera remain fixed while its measuring grid physically organizes the tokens.
- Static fallback: processed frame 007, the completed Assignment state.
- Static sprite: `GFX_utopia_balance_to_assignment_static`.
- Animated sprite: `GFX_utopia_balance_to_assignment_animated`.
- Subject classification: symbolic, people-free, text-free late-1930s civic instrument.
- Visual action: a restrained brass-and-blackened-steel measuring rail extends a calibrated comb and physically sorts loose civic tokens into a measured grid.
- Palette: aged brass, dark bronze, charcoal ledger backing, parchment-beige highlights, restrained oxblood accents.
- Source mode: built-in ImageGen for every accepted frame. Frame 000 is a precise-object correction of a rejected initial draft; frames 001–007 are separate precise-object edits with the prior accepted state as the visual reference. Rejected drafts are documented but are not packaged as source frames.
- Mechanical processing only: shared crop, resize, mild resampling sharpen, sheet assembly, preview/contact-sheet creation, and DDS conversion. Processing must not invent any motion state.
- Local references inspected: `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`, `paradox_wiki/Scripted GUI modding - Hearts of Iron 4 Wiki.md`, vanilla `interface/powerbalanceview.gfx`, and the existing Event 015 Ledger animation packages.
- Final PNG sheet: `docs/assets/015_utopia_manifesto/animations/utopia_balance_to_assignment/sheets/utopia_balance_to_assignment_sheet.png`.
- Final static PNG: `docs/assets/015_utopia_manifesto/animations/utopia_balance_to_assignment/sheets/utopia_balance_to_assignment_static.png`.
- Final sheet DDS: `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_sheet.dds`.
- Final static DDS: `gfx/interface/015_utopia_manifesto/utopia_balance_to_assignment_static.dds`.
- Target GFX file: `interface/015_utopia_manifesto.gfx` (parent-owned wiring).
- Target GUI file: `interface/015_utopia_manifesto_ledger.gui` (parent-owned wiring).

The transition is intentionally non-looping: it communicates a threshold crossing and settles into a readable destination state instead of pulsing continuously.
