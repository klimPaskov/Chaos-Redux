# Holy Realm Dhyana Seal Animation Brief

## Purpose

Create the animated `96x96` Dhyana Seal button/icon required by the Buddhahood GUI asset table. The meditation mechanic is implemented as a concentration decision sequence, so the seal is wired to the concentration sequence decision and its four hold-step decisions.

## Visual Direction

- Sacred seal icon for meditation and Dhyana concentration, not a character portrait.
- Blue-violet lotus seal with a pale inner orb, thin gold rim, and restrained breath-like glow.
- Reads clearly at `96x96`.
- No readable text, letters, numbers, flags, maps, weapons, blood, gore, faces, people, monsters, or modern UI.
- Calm meditation state, distinct from wrathful red, teaching green-gold, and Final Silence black.

## Technical Targets

- Source frames: separate generated PNGs, one per planned frame.
- Processed frames: `96x96` PNGs.
- Static fallback DDS: `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal.dds`.
- Final frame sheet: `768x96` DDS, 8 horizontal frames.
- Animated sprite: `GFX_decision_holy_realm_dhyana_seal_animated`.

## Required Outputs

- Source frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/source_frames/`
- Processed frames: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/processed_frames/`
- Sheet PNG: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/sheets/holy_realm_dhyana_seal_sheet.png`
- Preview GIF: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/previews/holy_realm_dhyana_seal_preview.gif`
- Contact sheet: `docs/assets/003_holy_realm_buddhahood/animations/holy_realm_dhyana_seal/previews/holy_realm_dhyana_seal_contact.png`
- Final DDS: `gfx/interface/decisions/holy_realm/dhyana_seal/holy_realm_dhyana_seal_animated.dds`

## References

- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Graphical asset modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Interface modding - Hearts of Iron 4 Wiki.md`
- `interface/003_holy_realm.gfx`
- `common/decisions/003_holy_realm_decisions.txt`
