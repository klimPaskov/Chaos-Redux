# Event 014 CBA-CBD Warlord Portrait ImageGen Handoff

Status: complete. All 28 CBA-CBD regional/default warlord portraits were independently regenerated with built-in ImageGen, processed to 156x210, converted to the existing live DDS paths, visually reviewed as a complete set, and documented on 2026-07-15.

## Outcome

- Four tags covered: CBA, CBB, CBC, and CBD.
- Seven portrait slots per tag: Europe/default, Africa, Asia, Middle East, North America, Oceania, and South America.
- Final selected sources: 28 independent built-in ImageGen PNGs with 28 unique SHA-256 hashes.
- Final processed portraits: 28 unique 156x210 PNGs.
- Final live textures: 28 unique 156x210 DDS files at the exact pre-registered paths.
- Every portrait has distinct face anatomy, build, clothing, expression, action, prop, environment, and silhouette.
- Every action remains legible in the native-size 28-up contact sheet.
- The corrected CBA Asia, CBB Asia, and CBB Oceania portraits are fully bald.
- CBA South America retains the required visible skull-lick action with tongue-to-temple contact.
- No portrait contains a prison, cell, bars, cage, prisoner uniform, restraint, or confinement setting.

The final visual sheet is:

docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/contact_sheets/cba_cbd_warlords_contact_sheet.png

The final scalp/face sheet is:

docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/contact_sheets/cba_cbd_baldness_audit_contact_sheet.png

## Distinct final actions

| Tag | Europe/default | Africa | Asia | Middle East | North America | Oceania | South America |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CBA | Bites a dog tag | Sniffs a torn glove | Pulls a false-teeth chain from his mouth with pliers | Whispers into a jawbone-like relic | Wrings a ration cloth beneath his mouth | Stares cross-eyed at a tooth in his palm | Licks a skull at the temple |
| CBB | Bites a papier-mâché hand | Caresses a carved feast mask | Bites a carved tooth bead from a taut cord | Paints his cheek while watching a mirror shard | Uses a hollow bone-like relic as a telescope | Chews a stitched ration-puppet arm | Slurps from a paper skull-cup through its eye socket |
| CBC | Screams into a paper skull used as a telephone | Gnaws an oversized carved wooden molar | Licks an empty ration spoon | Rubs a tarnished coin across his lips | Balances a tooth-shaped token on his tongue | Plays a bone-like whistle | Sews a grin onto a cloth ration puppet |
| CBD | Drops a tooth-shaped token into a tiny cup | Threads tooth-shaped tokens on wire with pliers | Files a resin crooked-smile trinket | Arranges resin molars along a steel collar | Kisses a wire-framed paper skull on its painted teeth | Bites a counting-frame wire with carved teeth clenched in his mouth | Pours resin tooth tokens into his open mouth |

## Source generation and quality gate

All final calls used the three canonical vanilla leader portraits under .agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ as style-only references. Prompts required a fictional adult male, restrained HOI4 portrait finish, open ruined environment, regional plausibility without caricature, face-adjacent disturbing action, and absolute exclusion of prisons, text, flags, real-person likenesses, and graphic injury.

Generation accounting:

- 28 selected successful outputs.
- 10 additional successful outputs rejected during native-size visual review and independently regenerated.
- 5 non-persisted moderation-blocked attempts retried once with non-graphic artificial-prop wording.
- 43 total built-in portrait invocations.
- 38 persisted generated-output PNGs: 28 selected and 10 visually superseded.

Moderation request IDs:

- 6613135f-0ec8-449e-8903-1aa8a1d4c5b8: initial CBA North America/South America/Oceania group.
- 7e5fbfb6-958a-4c58-8fb5-c81e963485e9: later partially persisted CBD group; CBD default and Africa persisted, while Asia and Middle East were retried individually.

No moderation retry exceeded one additional attempt. No alternate source route, CLI generator, local procedural art, other model, derivative portrait, or transformed-copy fallback was used.

The exact final generated-output filenames, prompt deltas, source dimensions, source SHA-256 values, superseded outputs, and retry accounting are recorded in:

docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/prompts/warlord_prompts.md

## Processing and installation

Every selected source was processed with:

- .tools/process_hoi4_portrait.py leader
- explicit full-source crop from the selected master dimensions
- source-kind fictional
- the canonical leader reference directory
- 156x210 processed output
- processor version 2.0 metadata
- one per-portrait 1344x464 review sheet

Every processed PNG was converted with:

- .tools/convert_to_dds.py
- width 156
- height 210

No interface edit was required. interface/014_cannibalism.gfx already registers the complete GFX_portrait_<TAG>_warlord family and its regional suffixes against the exact live DDS paths.

## Changed files

Asset package:

- 28 files under docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/source_png/
- 28 files under docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/processed_png/
- 28 files under docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/metadata/
- 28 files under docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/review_sheets/
- 2 files under docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/contact_sheets/
- docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/manifest.md
- docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/prompts/warlord_prompts.md
- docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/baldness_audit.md
- docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/gfx_handoff.md
- docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/validation.md

Live textures:

- 28 leader_CBA_warlord*.dds through leader_CBD_warlord*.dds files under gfx/leaders/014_cannibalism/

Handoff:

- docs/plans/014_cannibalism_plans/subagent_handoffs/event014_warlord_portraits_cba_cbd_imagegen_2026-07-15.md

No gameplay, interface registration, localisation, script, spreadsheet, flag, or unrelated texture file was edited.

## Validation evidence

- Exact package counts: 28 source, 28 processed, 28 metadata, 28 review, and 28 live DDS files.
- Hash uniqueness: 28/28 source, 28/28 processed, and 28/28 DDS hashes are unique.
- Final processed size: 156x210 for all 28.
- Decoded DDS size/mode: 156x210 RGBA for all 28.
- DDS byte size: 131,168 bytes for all 28.
- Review sheet size: 1344x464 for all 28.
- Final native-size whole-sheet visual review passed: no action is cropped away; all 28 read as distinct; hair corrections are bald; no prison imagery appears.

Exact final processed and DDS SHA-256 values are recorded in:

docs/assets/014_cannibalism/leader_portraits_refresh/cba_cbd/validation.md

## Skills and references used

- imagegen
- chaos-redux-event-assets
- chaos-redux-subagents
- Offline Paradox wiki core pages plus Portrait Modding and Graphical Asset Modding
- Vanilla leader portrait references and registration precedents
- Event 014 asset inventory, country-package matrix, regional name localisation, scripted portrait selection, and existing sprite registration

## Simplifications, omissions, and blockers

None. All 28 requested portraits, source masters, processed PNGs, metadata records, review sheets, contact sheets, final DDS files, prompt/source provenance, hash evidence, and handoff documentation are complete. No fallback or simplification was used.
