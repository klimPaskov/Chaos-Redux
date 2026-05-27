# Event 005 Country Flag, Portrait, And Leader Consistency Sidecar

Date: 2026-05-27

Role: Chaos Redux country package subagent, bounded audit plus handoff.

## Scope

Audited Event 005 Soviet Collapse country-package sidecar surfaces for flags, portraits, and leader consistency only.

Read and applied:

- `AGENTS.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-event-assets/SKILL.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md`
- `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_7_assets_achievements_validation.md`
- offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Country creation
- vanilla docs: `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `common/characters/_documentation.md`, and `common/decisions/_documentation.md`

No binary assets, focus files, decision files, balance files, MTTH files, country history files, localisation files, or `.gfx` files were edited.

## Country Package Coverage Checklist

Audited custom/Event 005 package tags:

`CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, `NLC`.

Direct source audit found no missing custom package entries for:

- tag registration
- common country file reference
- history country file
- `create_country_leader` portrait reference
- matching portrait sprite definition
- base country localisation: `TAG`, `TAG_DEF`, `TAG_ADJ`
- ideology localisation: `TAG_communism`, `TAG_democratic`, `TAG_fascism`, `TAG_neutrality`, plus `_DEF` and `_ADJ`
- party localisation: short and long party keys for all four ideology groups
- normal, medium, and small base/ideology flags

## File Surface Checklist

Audited surfaces:

- `common/country_tags/chaosx_countries.txt`
- `common/countries/*.txt` for the 32 custom Event 005 packages
- `history/countries/<TAG> - *.txt` for the 32 custom Event 005 packages
- `common/scripted_effects/005_soviet_collapse_effects.txt`, only leader-name and event-created council helper blocks
- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`
- `gfx/leaders/005_soviet_collapse/*.dds`
- `gfx/flags/<TAG>*.tga`
- `gfx/flags/medium/<TAG>*.tga`
- `gfx/flags/small/<TAG>*.tga`
- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
- `docs/assets/005_soviet_collapse/manifest.md`
- relevant existing handoffs under `docs/plans/005_soviet_collapse_plans/subagent_handoffs/`

## Missing Or Stale Country Package Surfaces

1. Live generated ordinary/internal council portrait DDS files are still unwired.
   - Live DDS files exist under `gfx/leaders/005_soviet_collapse/` for `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN`.
   - No matching `GFX_portrait_<TAG>_*` sprite definitions were found in the Event 005 `.gfx` files.
   - No matching `create_country_leader` branches were found in `soviet_collapse_apply_event_created_republic_council_leader`.
   - Existing handoff source: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_27_event005_generated_republic_portrait_sidecar_promotion.md`.

2. First-batch ordinary/internal council portraits remain sidecar-only.
   - Sidecar DDS files exist for `UKR`, `BLR`, `KAZ`, `LIT`, `GEO`, `AZR`, `KYR`, and `TAT` under `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_2026_05_26/final_dds/`.
   - No live `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds`, Event 005 sprite definition, or scripted leader branch was found for those eight generated council concepts.
   - Existing handoff source: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/generated_republic_council_portraits_second_batch_2026_05_26.md`.

3. Orphan leader DDS files remain under the Event 005 leader folder.
   - Live DDS with no Event 005 `.gfx` portrait texture reference: `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS`, plus the ten promoted ordinary/internal DDS listed above.
   - `BEC`, `BLT`, `COU`, `ILU`, and `IRA` are documented in older generated portrait handoffs, but no current gameplay or `.gfx` references were found in the scoped search. Treat these as stale asset surface until the parent either wires or removes them.

4. Top-level asset manifest drift remains.
   - `docs/assets/005_soviet_union_collapse/manifest.md` records the older custom/release council coverage and the `MOL`, `UZB`, `TAJ`, `TMS`, `FER` release council correction.
   - It does not clearly reconcile the later `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, `TAN` live DDS promotion or the eight sidecar-only `UKR`, `BLR`, `KAZ`, `LIT`, `GEO`, `AZR`, `KYR`, `TAT` generated councils.

## Map And State Setup Issues

No map/state setup issue was found in this bounded flags/portraits/leaders pass.

This audit did not rebalance ownership, controller setup, cores, claims, capitals, victory points, supply, railways, ports, buildings, or resources. Previous country package setup remains the source for map details, and this sidecar only confirms that no flag/portrait/leader inconsistency implies a new invalid map state.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

Positive findings:

- Custom package leaders use institutional/council names where the portrait concept is a governing body or symbolic authority, including factory boards, councils, directorates, congresses, and admiralty bodies.
- The active `MOL` and `TAJ` gender/name mismatch reported in the prior sidecar is already patched in `common/scripted_effects/005_soviet_collapse_effects.txt`: both now use male name pools and no longer force `female = yes`.
- Active explicit female custom leader pools remain confined to `BAC`, `NLC`, `TSC`, `UDC`, and `UWD`, matching the prior sidecar's portrait review.
- Direct SHA-256 comparison found zero duplicate hashes among `57` live Event 005 leader DDS files.
- Direct SHA-256 comparison found zero vanilla leader DDS hash matches for live Event 005 leader DDS files.
- `identify` reported no non-`156x210` live Event 005 leader DDS files.

Findings:

- The live generated ordinary/internal portrait files for `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` cannot affect gameplay yet because no sprite or `create_country_leader` branch references them.
- If the parent promotes those portraits as one-person leaders instead of institutional councils, the optional personal-name suggestions in `2026_05_27_event005_generated_republic_portrait_sidecar_promotion.md` should be expanded into small regional random pools before use. Do not use a single fixed name unless the design explicitly wants a named fictional individual.
- No advisor or high-command portrait pass was completed beyond the requested country leader/council surface.

## Focus, Decision, Idea, And Asset Issues

- No focus, decision, idea, or balance files were edited.
- Existing route cosmetic flag rule is respected in current live files: no default mod-side base/ideology flag overrides were found for existing vanilla-supported tags `SOV`, `RUS`, `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, or `TAN`.
- The explicit Ukraine route cosmetic `UKR_BLACK_BANNER` has base plus four ideology variants in normal, medium, and small folders.
- Scoped custom/cosmetic flag audit found:
  - missing flag files: `0`
  - invalid dimensions: `0`
  - invalid TGA bpp/origin: `0`
  - exact duplicate flag hash groups: `0`
  - grayscale same-tag RMSE pairs below `0.08`: `0`
- This supports the user correction that ideology flags are not simple byte copies or obvious grayscale-identical recolor passes, but final visual distinctiveness remains a human art review call.

## Starting Military, Technology, Industry, Supply, And Production Issues

Not re-audited in depth in this sidecar because the task was limited to flags, portraits, leaders, and country package consistency.

No new starting military, technology, industry, supply, or production issue was introduced because this pass did not edit gameplay files.

## AI And Playability Issues

No AI strategy patch was made.

Known prior country-package risk remains: factory/ancient tags such as `CFR`, `MFR`, `KZR`, `SOG`, `KHW`, and `ALN` rely on broad breakaway survival behavior unless package-specific AI strategy rows are added. That is a playability gap from the Part 6 package checklist, but it is outside this prompt's no-focus/no-decision/no-balance sidecar scope.

## Exact Asset Queue If Needed

No generated-art worker queue is needed for the currently audited flag and portrait consistency issues:

- custom flags are present, correct-size, bottom-origin 32bpp TGAs across normal/medium/small
- active custom/council portraits are unique and not vanilla hash matches
- `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` release council portraits are already wired

Parent wiring queue, if accepted:

1. Promote or reject sidecar-only ordinary/internal councils for `UKR`, `BLR`, `KAZ`, `LIT`, `GEO`, `AZR`, `KYR`, and `TAT`.
2. Wire the already-live but unused `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` DDS files through `interface/005_soviet_collapse_custom_icons.gfx` and `soviet_collapse_apply_event_created_republic_council_leader`, or remove them from the live leader folder if they are not accepted.
3. Decide whether those ten portraits represent institutional councils or one-person fictional leaders. If one-person, add gender-matched random regional name pools before creating leaders.
4. Reconcile or remove stale orphan DDS files for `BEC`, `BLT`, `COU`, `ILU`, `IRA`, `LID`, `RCD`, `RLD`, `SEP`, and `TRS`.
5. Update `docs/assets/005_soviet_union_collapse/manifest.md` after the parent decides which generated council batches are live implementation.

## Patch Status

Changed files:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_27_country_flag_portrait_leader_consistency_sidecar.md`

Changed tags, state ids, leaders, parties, focus tree ids, localisation keys, or formable ids:

- None.

Before and after behavior:

- Before: no gameplay behavior changed by this sidecar.
- After: no gameplay behavior changed by this sidecar; parent has a current consistency handoff and wiring queue.

## Validation Run

- Read required repository instructions, skills, clean spec parts 6 and 7, offline wiki references, and vanilla documentation.
- `python3` custom-package source audit for the 32 Event 005 custom tags covering tag registration, history files, localisation keys, party keys, leader portrait references, and sprite definitions.
- `python3` direct TGA header audit for custom/cosmetic flag families across normal, medium, and small folders.
- `python3` SHA-256 audit for Event 005 leader duplicate hashes and vanilla leader hash matches.
- `identify -format '%f %wx%h\n' gfx/leaders/005_soviet_collapse/*_leader.dds | awk '$2!="156x210" {print}'` returned no non-156x210 rows.
- ImageMagick-backed grayscale RMSE scan found no same-tag normal flag pairs below `0.08`.
- `rg` verification for generated council portrait references, existing-tag flag overrides, and leader-name helper blocks.

## Skipped Validation

- No in-game parser/load validation was run from this sidecar.
- No live-session portrait gender review was possible; gender conclusions rely on the current prior portrait sidecar and the scripted `female = yes`/name-pool surface.
- No focus/decision/balance validation was run because those files were explicitly out of edit scope.
- No binary asset generation, conversion, or replacement was attempted.

## Remaining Setup Or Identity Risks

- Event 005 should not be claimed complete from this sidecar. The broader Part 7 focus icon uniqueness blocker remains tracked elsewhere.
- Ordinary/internal council portrait promotion needs a parent decision: institutional council leaders versus one-person fictional leaders with regional random name pools.
- `docs/assets/005_soviet_union_collapse/manifest.md` should be updated after the parent accepts or rejects the currently unwired generated council batches.
- Stale orphan leader DDS files should be reconciled to avoid future audits counting unused assets as live country package coverage.
