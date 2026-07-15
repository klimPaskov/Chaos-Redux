# Portrait Regeneration B Handoff

## Completed scope

- Regenerated all 28 Event 014 CBE-CBH Europe/default and regional warlord portraits as separate fictional built-in image-generation sources.
- Installed all 28 at their exact existing 156x210 live DDS paths.
- Enforced a fully bald, hairless final set across CBE, CBF, CBG, and CBH.
- Removed every prison, cell, bar, restraint, prisoner-uniform, and confinement cue from the CBG-CBH visual language.
- Generated a separate transformed Wendigo Hannibal static master with an open snowy battlefield backdrop, invented frost-collar anatomy, no antlers, and no actor likeness.
- Built 16 real generated source frames covering turn, inhale, jaw opening, full gape, distinct peak hold, staged close, locked stare, and loop bridge.
- Assembled the exact 2496x210 horizontal sheet and a looping near-6-fps GIF review.
- Replaced only `leader_ZZZ_hannibal_wendigo_static.dds` and `leader_ZZZ_hannibal_wendigo_sheet.dds`; the archival `hannibal_wendigo.dds` was preserved.

## Files and evidence

- Warlord package: `docs/assets/014_cannibalism/leader_portraits_refresh/cbe_cbh/`.
- Wendigo package: `docs/assets/014_cannibalism/leader_portraits_refresh/wendigo_hannibal/`.
- Warlord final contact sheet: `cbe_cbh/contact_sheets/processed_contact_sheet.png`.
- Wendigo source contact sheet: `wendigo_hannibal/contact_sheets/source_frames_contact_sheet.png`.
- Wendigo final contact sheet: `wendigo_hannibal/contact_sheets/processed_frames_contact_sheet.png`.
- Wendigo GIF: `wendigo_hannibal/previews/leader_ZZZ_hannibal_wendigo_preview.gif`.
- Exact existing sprite bindings: `cbe_cbh/gfx_handoff.md` and `wendigo_hannibal/gfx_handoff.md`.
- Detailed runtime-format and visual checks: both package `validation.md` files.
- Exhaustive package hash inventories: both package `hashes.sha256` files.
- Source prompt and frame design records: both package `prompts/` folders.

## Generation accounting

- 54 built-in image-generation invocations in total.
- 53 successful image-generation outputs.
- 45 selected source deliverables: 28 warlords, one Wendigo static, and 16 Wendigo frames.
- Eight successful but superseded candidates: six first-pass warlords replaced by strict hairless versions and two frame-015 bridge candidates replaced during loop audit.
- One failed/non-persisted early warlord attempt rejected before it produced a file.

## Validation result

- All 28 selected warlord sources, all 28 processed portraits, and all 28 live warlord DDS files are hash-unique.
- All 16 selected Wendigo source frames and all 16 processed frames are hash-unique.
- All final portraits and frames are 156x210.
- The Wendigo animation sheet is 2496x210; all 16 sheet slices match the processed frame masters pixel-for-pixel.
- All 28 warlord DDS payloads, the Wendigo static DDS, and the Wendigo sheet DDS decode pixel-identically to their processed PNG masters.
- The GIF contains 16 frames, loops indefinitely, and uses a 170/170/160 ms cadence averaging 5.993 fps; the existing in-game sprite remains exactly 6 fps.
- The final two loop transitions distribute the return-to-rest motion across the generated bridge.
- Parent visual review accepted the CBE-CBH contact sheet and the 16-frame Wendigo loop as bald, distinct, feral, HOI4-readable, and free of prison imagery.
- Existing `interface/014_cannibalism.gfx` wiring already matches every output and was not edited.
- `hannibal_wendigo.dds` SHA-256 is unchanged at `26d7566f7b93d17c4d7fde5b262ab8b6e4b04fba0b862315404d6a33abe34717`.
- Hash-inventory verification passed for all 142 CBE-CBH records and all 75 Wendigo records.

## Simplifications, omissions, and blockers

None. No placeholder, fallback, reused portrait, prison-host design, actor likeness, antler shorthand, transform-only animation, gameplay/localisation/GFX/spreadsheet/spec/flag edit, or unrelated texture edit was used. No Git commit was created; the parent agent retains final diff review and commit ownership.

## Skills used

- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `imagegen`
