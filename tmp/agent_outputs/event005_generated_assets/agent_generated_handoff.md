# Event 005 Generated Asset Sidecar Handoff

Date: 2026-05-25

Scope: bounded handoff for Event 005 Soviet Collapse generated fictional/council leader portrait concepts and generated or historically styled flag variant directions for `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, and `KZR`.

This sidecar did not edit gameplay, script, localisation, interface, `.gfx`, history, country, spreadsheet, active `gfx/flags/**`, or active `gfx/leaders/**` files. It creates handoff notes only.

## Sources read

- `AGENTS.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `/home/klim/.codex/skills/.system/imagegen/SKILL.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- `.agents/skills/chaos-redux-event-assets/assets/flags/`
- Existing Event 005 asset docs under `docs/assets/005_soviet_union_collapse/`
- Current dirty active files were inspected read-only under `gfx/flags/`, `gfx/flags/medium/`, `gfx/flags/small/`, and `gfx/leaders/005_soviet_collapse/`

The required offline HOI4 wiki pages and vanilla documentation files were opened for repository compliance. This sidecar does not change Clausewitz script.

## Current state notes

- The requested active flag families already have dirty working-tree files in normal, medium, and small folders. They were not overwritten.
- Header audit for the requested `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, and `KZR` families found all expected base plus ideology files present at normal `82x52`, medium `41x26`, and small `10x7`.
- Normal and medium TGAs in this requested set report `32` bpp and descriptor `0x08`.
- Small TGAs in this requested set report `8` bpp and descriptor `0x00`. Vanilla `small/SOV.tga` reports `32` bpp, so parent should decide whether this is acceptable in the existing Chaos Redux flag set or re-export the small variants to 32 bpp during integration.
- Current active leader DDS files for the ten requested tags exist at `156x210`: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, and `KZR`.
- Tracked `BEC`, `BLT`, `COU`, `ILU`, and `IRA` leader DDS files are deleted in the current working tree. Prior docs say they were inactive; do not regenerate them unless the parent restores those tags to active use.

## Portrait concept handoff

Use `$imagegen` for any replacement source art because these are fictional, collective, factory, security, high-chaos, or restoration leaders. Do not generate real-person likenesses.

Target workflow for any approved replacement: source PNG in `tmp/agent_outputs/event005_generated_assets/source_png/`, processed preview PNG in `tmp/agent_outputs/event005_generated_assets/processed_png/`, final parent export to `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds`, target `156x210`, contact sheet, manifest entry, and existing sprite name preserved.

| Tag | Portrait concept | Prompt direction |
| --- | --- | --- |
| `CFR` | Civilian construction directorate portrait | HOI4-style fictional council portrait of construction administrators around a concrete planning table, ration cards and bridge permits visible as shapes only, 1930s Soviet civilian workwear, subdued painterly bust framing, no readable text. |
| `KRS` | Kronstadt sailor soviet council | Fictional sailor-worker council chair in naval pea coat, Baltic port command room, signal flags and harbor maps as non-readable props, anti-Moscow soviet tone, subdued HOI4 portrait treatment. |
| `RMC` | Red Martyrs' resurrection cult authority | Fictional grim martyr-cult council portrait, red burial cloths, memorial candles, militarized commissar robes, gaunt but not caricatured, high-chaos death-state tone, no gore, no readable symbols. |
| `SDZ` | Security Directorate archive board | Fictional sealed security authority, archivist-officer at file cabinets and blackout window, internal troops implied by silhouettes, cold bureaucratic control, 1930s NKVD-adjacent uniforms without real likeness. |
| `TSC` | Tunguska Star Committee presidium | Fictional Siberian scientific committee leader, field telescope, radio equipment, burned-glass sample, winter observatory room, strange-science tone but period-authentic props. |
| `UDC` | Union Defense Committee emergency command | Fictional loyalist military-district council, staff officer and civilian commissar sharing a command map, field telephones and dispatch folders, emergency union continuity, grounded 1936-1945 military style. |
| `SOG` | Sogdian City League council | Fictional merchant-city register council, elder or clerk with trade-map backdrop, textile-roundel motifs as decorative shapes only, civic legal authority, no modern fantasy styling. |
| `ALN` | Alan Pass Principality council | Fictional mountain pass council regent, Caucasus pass map, keys and border ledgers as symbolic props, heavy wool cloak and officer side figures, highland legal-restoration tone. |
| `KHW` | Khwarazmian Oasis Authority | Fictional oasis register authority, irrigation ledger, water-right rods, canal map, Central Asian legal-administrative dress, restrained historical-restoration palette. |
| `KZR` | Khazar toll khaganate council | Fictional Volga-steppe toll council, seal/tamga-like non-readable emblem, river trade map, fur-lined administrative dress, restored toll sovereignty rather than fantasy monarchy. |

Blocked portrait concepts until parent activation: `BEC`, `BLT`, `COU`, `ILU`, and `IRA` should receive generated fictional council portraits only if those deleted tracked DDS files are restored to active use.

## Flag variant direction handoff

Base rule: preserve no-suffix base flags for all ten tags unless the parent explicitly says the base file is in scope. Generate or repair only ideology variants by default: `_communism`, `_democratic`, `_fascism`, and `_neutrality`.

Each ideology variant must be a distinct generated or historically grounded design. Do not produce recolors, filters, flipped copies, upside-down copies, one-shape edits, copied-emblem variants, or byte-identical files.

Target workflow for any approved replacement: generated/source PNG, processed normal/medium/small PNG previews, final TGA outputs in all three flag folders, contact sheet with labels, manifest entry, and orientation confirmation.

| Tag | Base preservation | Variant direction |
| --- | --- | --- |
| `CFR` | Preserve base unless the factory-state base is explicitly declared broken. | Civilian construction symbolism. Communism: builders' soviet and red scaffolding motif. Democratic: civic reconstruction board with bridge/house symbol. Fascism: authoritarian concrete ministry with severe vertical works emblem. Neutrality: technocratic construction directorate with neutral cement/blueprint palette. |
| `KRS` | Preserve base unless explicitly scoped. | Naval soviet symbolism. Communism: sailor-worker red fleet council. Democratic: free-port soviet assembly with harbor/star motif. Fascism: fortress-port command banner, harsh naval geometry. Neutrality: independent sailor council with anchor, waves, and signal shapes. |
| `RMC` | Preserve base unless explicitly scoped. | Martyr and reliquary symbolism, no gore. Communism: red memorial commune. Democratic: witness commune with memorial torch/ledger. Fascism: crimson reliquary state with severe shrine geometry. Neutrality: cult authority with burial cloth, star, and votive shapes. |
| `SDZ` | Preserve base unless explicitly scoped. | Archive, checkpoint, and security-control symbolism. Communism: red archive directorate. Democratic: witness-protection/security court emblem. Fascism: black-site directorate with locked file/seal motif. Neutrality: sealed zone authority with gate and dossier shapes. |
| `TSC` | Preserve base unless explicitly scoped. | Tunguska astronomy, radio, burned-glass, and taiga science motifs. Communism: scientific commune and red star-observatory. Democratic: observatory republic with civic instrument seal. Fascism: star directorate with severe celestial command mark. Neutrality: committee of instruments, pale sky and field-station symbols. |
| `UDC` | Preserve base unless explicitly scoped. | Loyalist emergency command and military-district continuity. Communism: union command soviet with red field signal. Democratic: provisional defense committee with shield/map motif. Fascism: emergency staff command, hard angular district emblem. Neutrality: military directory with dispatch seal and staff-map geometry. |
| `SOG` | Preserve historically grounded base unless explicitly scoped. | Sogdian textile and merchant-city motifs. Use pearl-roundel, paired birds, city-register, or caravan shapes. Keep variants historically styled and small-size readable, not modern national tricolors. |
| `ALN` | Preserve historically grounded base unless explicitly scoped. | Caucasus pass and Alano-Ossetian continuity motifs. Use mountain, pass key, guard spear, and white/red/gold language. Variants should signal ideology through composition and emblem, not palette-only changes. |
| `KHW` | Preserve historically grounded base unless explicitly scoped. | Oasis, water-rights, canal, coin/seal, and tamga-caution motifs. Avoid claiming a direct medieval flag. Keep crescent/water/roundel language abstract and non-readable. |
| `KZR` | Preserve historically grounded base unless explicitly scoped. | Steppe toll, Volga trade, tamga-like seal, river gate, and dual-field motifs. Avoid pretending to reproduce a directly attested Khazar state flag; document as historically grounded synthesis. |

## Orientation confirmation requirements

For every approved generated flag output, parent integration should record:

1. Normal output exists at `gfx/flags/<TAG>[_ideology].tga`, is `82x52`, and has expected orientation in a contact sheet.
2. Medium output exists at `gfx/flags/medium/<TAG>[_ideology].tga`, is `41x26`, and matches normal orientation.
3. Small output exists at `gfx/flags/small/<TAG>[_ideology].tga`, is `10x7`, remains readable, and matches normal orientation.
4. TGA header/origin convention is intentionally chosen and documented. Current requested-set normal/medium files are bottom-origin descriptor `0x08`; current requested-set small files are 8 bpp descriptor `0x00`, which needs parent acceptance or re-export.
5. Contact sheet shows normal/medium/small together for every base and ideology variant, with labels.
6. Hash audit confirms no byte-identical variants inside each tag family unless intentionally shared and explicitly documented.
7. Visual check confirms no upside-down copies, mirrored copies, accidental vertical flips, or base-flag overwrites.

## Parent integration steps

1. Decide whether the current dirty active flags are acceptable or whether any named family should be regenerated.
2. If regenerating, keep no-suffix base flags unchanged unless the base is explicitly in scope.
3. Use `$imagegen` for fictional/custom variants and `chaosx_asset_source_researcher` for historical or historically attested symbols if the design requires sourcing.
4. Export source PNG, processed PNG previews, final TGAs for flags or DDS for portraits, contact sheets, and manifest rows.
5. Preserve existing portrait sprite names and country-flag filenames. Country flags need no `.gfx` entries.
6. Update `docs/assets/005_soviet_union_collapse/manifest.md` and the main `gfx_handoff.md` only after final files exist and have been checked.

## Blockers and uncertainty

- No final asset files were produced in this pass because the requested active `gfx/flags/**` files are already dirty and the prompt forbids overwriting dirty flag files.
- The active ten requested leader portraits exist, so "missing leaders" is only confirmed for stale/deleted tracked tags `BEC`, `BLT`, `COU`, `ILU`, and `IRA`; their active gameplay status remains a parent-agent decision.
- Current small flag TGAs in the requested set are `8` bpp while vanilla `small/SOV.tga` is `32` bpp. This sidecar flags that as an integration uncertainty rather than changing files.
- Existing docs claim prior orientation correction work. This sidecar did not visually inspect the generated contact sheets in a GUI; it only audited file presence, dimensions, and headers.
