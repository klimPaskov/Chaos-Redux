# Event 012 Tier A identity icon follow-up handoff — 2026-08-09

## Outcome

Created six distinct fictional Tier A package identity families for Pan, Gorilla Kingdom, The Green, Living Rivers, Stoneborn, and Ancient Hosts. Each package has a 94x86 focus/goal surface and a 32x32 decision surface with source PNG, alpha intermediate, processed target PNG, final DDS, decoded DDS PNG, contact-sheet evidence, manifest entry, and GFX handoff notes.

Pan is a lean great-ape Pan-genus engineer with subtle horns, pointed ears, tool satchel, pliers, and fieldworks. Gorilla Kingdom is a broad, heavily armored mountain gorilla; the two identities are visually distinct.

## Files

- `docs/assets/012_africa/tier_a_identity_icons/manifest.json`
- `docs/assets/012_africa/tier_a_identity_icons/gfx_handoff.md`
- `docs/assets/012_africa/tier_a_identity_icons/prompts/tier_a_icon_prompt_record.md`
- `docs/assets/012_africa/tier_a_identity_icons/contact_sheet_focus.png`
- `docs/assets/012_africa/tier_a_identity_icons/contact_sheet_decision.png`
- `docs/assets/012_africa/tier_a_identity_icons/contact_sheet_focus_roundtrip.png`
- `docs/assets/012_africa/tier_a_identity_icons/contact_sheet_decision_roundtrip.png`
- `gfx/interface/goals/012_africa/tier_a/`
- `gfx/interface/decisions/012_africa/tier_a/`

## Validation

The six focus DDS files are 94x86 and the six decision DDS files are 32x32. Every DDS has DDS magic, a 124-byte header, a 32-byte uncompressed BGRA pixel format, masks `0xff0000/0xff00/0xff/0xff000000`, texture caps `0x1000`, and exact payload length. Every decoded DDS equals its exact-size processed PNG pixel-for-pixel.

Canonical focus and decision contact sheets were inspected before processing. The generated contact sheets show source, processed, and decoded round trips for all twelve assets.

## Consumer and seal gate

The current implementation audit found only dormant fictional sovereign portrait consumers in `common/characters/012_africa_fictional_characters.txt`. No focus or decision currently points at these package icon IDs, and no 64x64 package-seal consumer exists. Therefore no package seal DDS was created, and no duplicate registrations were added to the parent’s committed `interface/012_africa_strange_force_icons.gfx` registry.

## Parent integration boundary

No gameplay, localisation, or `.gfx` file was edited. If package focus or decision consumers become real, parent should register the proposed IDs from `gfx_handoff.md` in the existing registry or a clearly owned follow-up file, preserving the no-duplicate rule. The runtime roots to promote are `gfx/interface/goals/012_africa/tier_a/` and `gfx/interface/decisions/012_africa/tier_a/`.

No simplification was made to the requested focus or decision surfaces. The explicit limitation is that no 64x64 seal was produced because no current seal consumer exists.
