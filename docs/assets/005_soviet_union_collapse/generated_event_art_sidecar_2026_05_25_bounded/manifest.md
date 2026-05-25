# Event 005 Generated Event Art Sidecar - Bounded Pass

Related event: 005 Soviet Union Collapse

Source mode: `$imagegen`

Scope: generated fictional/council leader portrait candidates and fictional route/ideology flag candidates for custom splinter tags. This pass intentionally did not edit gameplay, localisation, `.gfx`, focus, idea, decision, event, history, or live country definition files.

Important safety note: the live files for the requested tags under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` were already modified in the worktree before this pass. To avoid overwriting base flags or mixing ownership with existing changes, this package keeps flag outputs under this sidecar folder as review candidates.

## Leader Portrait Candidates

### KRS Council Leader

- Asset type: fictional collective leader portrait
- Intended use: Kronstadt Free Soviet council-style leader portrait candidate
- Source mode: `$imagegen`
- Prompt summary: HOI4-style fictional council portrait for the Kronstadt Free Soviet, centered 1930s naval delegate with two half-shadowed delegates, period clothing, subdued painterly realism, no text or modern props.
- Source PNG: `source_png/KRS_council_leader_source.png`
- Processed PNG: `processed_png/KRS_council_leader.png`
- Final DDS candidate: `final_dds/KRS_council_leader.dds`
- Target size: 156x210
- Proposed live path if approved: `gfx/leaders/005_soviet_collapse/KRS_leader.dds`
- Source rationale: fictional/council leader for a high-chaos splinter tag, appropriate for generation.
- Status: handed_off

### RMC Cult Regent Leader

- Asset type: fictional high-chaos leader portrait
- Intended use: Red Martyrs Resurrection Cult leader portrait candidate
- Source mode: `$imagegen`
- Prompt summary: HOI4-style fictional cult-regent portrait, gaunt commander in worn 1930s field coat, two silent acolyte-officers behind him, eerie but grounded, no gore, no text or modern props.
- Source PNG: `source_png/RMC_cult_regent_leader_source.png`
- Processed PNG: `processed_png/RMC_cult_regent_leader.png`
- Final DDS candidate: `final_dds/RMC_cult_regent_leader.dds`
- Target size: 156x210
- Proposed live path if approved: `gfx/leaders/005_soviet_collapse/RMC_leader.dds`
- Source rationale: fictional/high-chaos leader for an invented splinter tag, appropriate for generation.
- Status: handed_off

## Route/Ideology Flag Candidates

Generated source sheet: `source_png/requested_custom_splinter_flag_sheet_source.png`

Contact sheet: `contact_sheets/event005_bounded_generated_route_flags_normal.png`

The flag sheet was prompted as ten distinct fictional flat flag designs in this order: KRS, UDC, SDZ, RMC, TSC, CFR, SOG, ALN, KHW, KZR. Each candidate was cropped from the generated source sheet, resized into the normal/medium/small HOI4 flag sizes, and kept as a candidate route/ideology flag rather than copied over live files.

For each tag below:

- Processed PNG path: `processed_png/<TAG>_generated_route_flag.png`
- Normal TGA candidate: `final_tga/normal/<TAG>_generated_route.tga`
- Medium TGA candidate: `final_tga/medium/<TAG>_generated_route.tga`
- Small TGA candidate: `final_tga/small/<TAG>_generated_route.tga`
- Target sizes: 82x52, 41x26, 10x7
- Orientation: upright; hoist side treated as left in source order and output contact sheet.
- Status: handed_off, needs review before live replacement

Candidate tags:

- KRS: maritime revolutionary council route flag candidate.
- UDC: emergency defense committee route flag candidate.
- SDZ: security cordon zone route flag candidate.
- RMC: red martyr resurrection cult route flag candidate, no gore.
- TSC: Tunguska star committee route flag candidate.
- CFR: factory republic route flag candidate.
- SOG: Sogdian city league route flag candidate.
- ALN: mountain pass principality route flag candidate.
- KHW: oasis authority route flag candidate.
- KZR: Khazar toll khaganate route flag candidate.

Generation prompt summary: ten distinct fictional alternate-history Soviet-collapse splinter flag designs, arranged in a 2x5 sheet with no labels, no readable text, no real historical state flags, no Nazi/fascist symbols, no hammer-and-sickle, no swastikas, no modern logos, crisp geometry, limited colors, readable at small HOI4 sizes.

## Validation Notes

- Reference folders inspected: `.agents/skills/chaos-redux-event-assets/assets/flags`; `.agents/skills/chaos-redux-event-assets/assets/portraits` was absent.
- Existing Chaos Redux portraits inspected under `gfx/leaders/005_soviet_collapse/`.
- Existing flag paths inspected under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- No no-suffix base flags were created or overwritten.
- No live ideology flags were overwritten by this sidecar pass.
- DDS candidate dimensions confirmed: 156x210.
- TGA candidate dimensions confirmed: normal 82x52, medium 41x26, small 10x7.
- TGA orientation header uses bottom-left origin like the existing checked `gfx/flags/KRS.tga` origin convention; visual orientation is confirmed by contact sheet.

## Blockers And Uncertainty

- Live flag assets for the requested tags were already dirty before this pass, so final candidates were not copied into `gfx/flags/`.
- The generated ten-flag source sheet is useful as a bounded review package, but it is not a full four-ideology-per-tag replacement set. Each candidate should be reviewed before deciding whether it becomes a route flag, an ideology variant seed, or a rejected draft.
- ALN, KHW, KZR, and SOG can imply historically grounded motifs. These candidates avoid known historical symbols; if exact historically attested symbols are desired, route those specific requests to `chaosx_asset_source_researcher`.
