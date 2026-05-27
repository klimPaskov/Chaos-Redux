# Event 005 Country Package Portrait And Flag Audit

Date: 2026-05-27

Role: `chaosx_country_package_auditor` bounded country-package audit.

## Scope

Audited Event 005 country-package surfaces requested by the parent prompt:

- final clean merged spec parts 1, 6, and 7 under `tmp/soviet_collapse_final_clean_merged_spec_package/specs/`
- `docs/assets/005_soviet_union_collapse/manifest.md`
- `docs/assets/005_soviet_collapse/manifest.md`
- `common/country_tags/chaosx_countries.txt`
- `common/countries/*.txt` for Event 005 custom tags
- `history/countries/*.txt` for Event 005 custom tags
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/national_focus/005_soviet_collapse_*.txt`
- `common/ai_strategy/005_soviet_collapse.txt`
- `interface/005_soviet_collapse_custom_icons.gfx`
- `interface/005_soviet_collapse_factory_ancient_icons.gfx`
- `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`
- `localisation/english/chaosx_countries_l_english.yml`
- live portrait and flag files under `gfx/leaders/005_soviet_collapse/` and `gfx/flags/`

No gameplay, balance, MTTH, focus, decision, history, country, localisation, `.gfx`, flag, or portrait file was edited.

## Country Package Coverage Checklist

Source-complete in direct audit for these 32 custom Event 005 packages: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, and `NLC`.

Verified for all 32:

- tag registration in `common/country_tags/chaosx_countries.txt`
- referenced `common/countries/<name>.txt` file exists
- matching `history/countries/<TAG> - <name>.txt` file exists
- history leader or council exists through `create_country_leader`
- history leader portrait sprite resolves to an `interface/005_soviet_collapse*.gfx` sprite
- portrait texture path exists under `gfx/leaders/005_soviet_collapse/`
- base country localisation has `TAG`, `TAG_DEF`, and `TAG_ADJ`
- ideology localisation has `TAG_communism`, `TAG_democratic`, `TAG_fascism`, `TAG_neutrality`, plus `_DEF` and `_ADJ`
- party localisation has short and long keys for all four ideology groups
- base and ideology flags exist in normal, medium, and small folders
- focus files mention the tag and setup effects load the intended tree family

## File Surface Checklist

- Tag registration: `common/country_tags/chaosx_countries.txt:7-38`.
- Custom country definitions: `common/countries/Civilian Factory of Russia.txt` through `common/countries/Northern Lights Commune.txt`.
- History setup: `history/countries/<TAG> - <name>.txt` for all 32 custom packages.
- Portrait sprite definitions: `interface/005_soviet_collapse_custom_icons.gfx:3-26`, `interface/005_soviet_collapse_custom_icons.gfx:2672`, `2725`, `2770`, `2815`, `2860`, `2905`, and `interface/005_soviet_collapse_factory_ancient_icons.gfx:2-3`, `235-239`.
- Country localisation: `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` and `localisation/english/chaosx_countries_l_english.yml`.
- Focus loading and setup effects: `common/scripted_effects/005_soviet_collapse_effects.txt:13367-13893` for custom packages; `common/scripted_effects/005_soviet_collapse_effects.txt:6336-6468` for event-created ordinary/internal focus trees.
- Existing-tag route cosmetic flag: `common/national_focus/005_soviet_collapse_republics.txt:251-275` applies `UKR_BLACK_BANNER`.

## Missing Or Stale Country Package Surfaces

1. Newer generated ordinary/internal council portraits are not fully wired.
   - Live DDS files exist for `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` under `gfx/leaders/005_soviet_collapse/`.
   - No matching `GFX_portrait_<TAG>_*` sprite definitions were found in `interface/005_soviet_collapse_custom_icons.gfx`.
   - No matching `create_country_leader` branches were found in `soviet_collapse_apply_event_created_republic_council_leader` at `common/scripted_effects/005_soviet_collapse_effects.txt:8171-8240`.
   - The current active scripted generated council leader coverage is only `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`.
   - Handoff evidence for the unwired batch: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_27_event005_generated_republic_portrait_sidecar_promotion.md`.

2. First ordinary/internal council batch remains sidecar-only.
   - `UKR`, `BLR`, `KAZ`, `LIT`, `GEO`, `AZR`, `KYR`, and `TAT` have DDS-ready sidecar files in `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_2026_05_26/final_dds/`.
   - No live `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds`, sprite definition, or scripted `create_country_leader` branch was found for those eight generated council concepts.
   - Handoff evidence: `docs/plans/005_soviet_collapse_plans/subagent_handoffs/generated_republic_council_portraits_second_batch_2026_05_26.md`.

3. Top-level asset manifest is stale for the 2026-05-27 promoted ordinary/internal batch.
   - `docs/assets/005_soviet_union_collapse/manifest.md` records `MOL`, `UZB`, `TAJ`, `TMS`, and `FER`, but does not appear to record the later `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` live portrait promotion.
   - This is documentation drift, not a live file absence.

4. AI strategy references are incomplete for six custom packages.
   - `common/ai_strategy/005_soviet_collapse.txt` has no explicit tag mention for `CFR`, `MFR`, `KZR`, `SOG`, `KHW`, or `ALN`.
   - All six still inherit generic breakaway survival behavior through `has_country_flag = soviet_collapse_breakaway`, but Part 6 asks high-chaos and ancient actors to have route-valid AI.
   - This was not patched because the parent prompt forbids balance/MTTH work and only allowed narrow localisation, party-name, leader-name, and package-reference fixes.

## Map And State Setup Issues

No immediate map-safety issue was found in the scoped source audit.

- Custom setup effects explicitly set capitals before loading focus trees: `CFR` state `248`, `MFR` `252`, `OGB`/`KZR` `249`, `SOG` `586`, `KHW` `742`, `ALN`/`MRC` `232`, `KRS` `195`, `FTH` `200`, `BBH` `226`, `BSC` `742`, `RMC` `257`, `DSC` `217`, `NRF`/`ARD` `213`, `TNC` `585`, `ALA` `583`, `UDC` `223`, `SDZ` `248`, `GAC` `222`, `DHC` `218`, `KHC` `234`, `FEV` `408`, `SZA` `578`, `UWD` `582`, `IUL` `651`, `BAC` `657`, `PRA` `570`, `TSC` `576`, `ICD` `254`, and `NLC` `216`.
- Overlapping ancient/high-chaos capitals are an intended eligibility/spawn-priority surface per existing audits, not an immediate invalid setup finding.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

Positive findings:

- Custom-package history leaders use institutional or council names, matching the generated/symbolic portrait source mode: examples include `The Construction Board`, `The Arsenal Board`, `The Volga Restoration Council`, `The Itil Toll Council`, `Council of the City Registers`, `The Oasis Register Authority`, `The Alan Pass Council`, `The Sailors' Assembly`, and `Dead Convoy Admiralty`.
- Direct `identify` validation confirmed `KZR`, `SOG`, `OGB`, `KHW`, `ALN`, `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` live DDS files are `156x210`.
- Direct flag dimension validation confirmed the audited custom/cosmetic families `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `OGB`, `SOG`, `ALN`, `KHW`, `KZR`, and `UKR_BLACK_BANNER` have base normal `82x52`, medium `41x26`, and small `10x7` files.
- The explicit route cosmetic `UKR_BLACK_BANNER` has base plus four ideology variants in normal, medium, and small folders.

Findings:

- Generated one-person-framed council portraits for `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` currently have optional personal-name suggestions in the handoff but no accepted scripted leader implementation. If the parent wants these portraits to become one-person leaders rather than institutional councils, random regional naming needs scripted-effect work. Do not patch that piecemeal in history files.
- `UKR`, `BLR`, `KAZ`, `LIT`, `GEO`, `AZR`, `KYR`, and `TAT` first-batch generated councils are not live package references yet.
- No advisor/high-command audit was completed in this bounded pass beyond confirming no requested portrait or flag asset blocker for the custom package leaders/councils.

## Focus, Decision, Idea, And Asset Issues

- Focus loading exists for custom packages at `common/scripted_effects/005_soviet_collapse_effects.txt:13367-13893`.
- Event-created ordinary/internal tree loading exists at `common/scripted_effects/005_soviet_collapse_effects.txt:6336-6468`.
- The current active generated ordinary/internal council leader setup only covers `MOL`, `UZB`, `TAJ`, `TMS`, and `FER` at `common/scripted_effects/005_soviet_collapse_effects.txt:8171-8240`.
- The high-chaos/factory/ancient asset manifest claims broad completion, but the promoted 2026-05-27 ordinary/internal generated council batch is only recorded in a handoff, not the top-level manifest.
- Existing `docs/assets/005_soviet_collapse/manifest.md` is a bounded sidecar for `ALN`, `KHW`, `KZR`, `SOG`, `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, and `OGB`; it remains useful for flag/portrait review history but is not the full current source of truth.

## Starting Military, Technology, Industry, Supply, And Production Issues

No new starting military or industry blocker was found in this portrait/flag/package-reference audit.

- All custom history files audited set basic technology and politics.
- Custom setup effects call `soviet_collapse_setup_breakaway_country = yes`, which applies the dynamic breakaway package before loading custom focus trees.
- This pass did not rebalance unit counts, stockpiles, industry, supply, or production because the parent prompt explicitly excluded balance/MTTH files and limited patches to narrow country-reference surfaces.

## AI And Playability Issues

Finding: six custom tags lack explicit AI strategy mention in `common/ai_strategy/005_soviet_collapse.txt`.

- Missing explicit AI tag references: `CFR`, `MFR`, `KZR`, `SOG`, `KHW`, `ALN`.
- Existing generic fallback behavior: `soviet_collapse_breakaway_survival` applies to any country with `soviet_collapse_breakaway`.
- Why this matters: Part 6 asks factory states and ancient restorations to have route-valid AI for expansion, leagues, sponsors, and unique mechanics. Generic breakaway survival is not enough to prove the package-specific AI surface.
- Patch status: not patched in this subagent pass because adding AI strategy rows crosses the parent prompt's no-balance constraint.

## Handoff For Main-Agent Scripted Leader Work

If the parent wants generated one-person-framed portraits to use actual-ish personal names selected from a small regional pool, implement it as a deliberate scripted-effect slice:

- Add or extend a single helper near `soviet_collapse_apply_event_created_republic_council_leader`.
- Scope: country.
- Inputs: current tag, `soviet_collapse_event_council_leader_created` guard, accepted portrait sprite for the tag.
- Behavior option A: keep these as institutional council leaders and add the missing `.gfx` plus `create_country_leader` branches with institutional names.
- Behavior option B: create one-person leader branches with `random_list` name selection per regional pool before or inside `create_country_leader`; use the optional suggestions from the 2026-05-27 handoff only as seed material, not as the whole pool.
- Required `.gfx` additions if accepted: `GFX_portrait_EST_tallinn_continuity_committee`, `GFX_portrait_LAT_port_forest_continuity_council`, `GFX_portrait_ARM_mountain_emergency_council`, `GFX_portrait_KAR_border_timber_council`, `GFX_portrait_KOM_mine_river_committee`, `GFX_portrait_CRI_port_peninsula_committee`, `GFX_portrait_BSK_oilfield_workshop_council`, `GFX_portrait_YAK_lena_resource_board`, `GFX_portrait_BYA_baikal_relay_council`, and `GFX_portrait_TAN_steppe_compact_council`.
- Required doc update if accepted: `docs/assets/005_soviet_union_collapse/manifest.md`.

## Patch Status

Changed files:

- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_27_country_package_portrait_flag_audit.md`

Changed tags, state ids, leaders, parties, focus tree ids, localisation keys, or formable ids:

- None. This was an audit/handoff only.

Before and after behavior:

- Before: no additional gameplay, localisation, flag, portrait, focus, decision, AI, or scripted behavior changed.
- After: same in-game behavior; parent has a concrete country-package audit and scripted-leader handoff.

Validation run:

- Read required offline wiki pages and vanilla documentation sections for country creation, flags/cosmetic tags, focus loading, effects/triggers, localisation, AI strategy, and portraits through the local docs available in the repo and vanilla tree.
- `python3` direct source audit for 32 custom tags: tag registration, country file, history file, leader portrait sprite, portrait texture, localisation, party keys, flags, focus mentions, and AI mentions.
- `identify` dimension check for scoped live portrait DDS files.
- `identify` dimension check for scoped normal/medium/small flag TGA files.
- `rg` verification for setup effects, focus loading, cosmetic tag application, leader creation, and AI strategy tag mentions.

Skipped validation and why:

- No live in-game validation was run; this subagent can only perform source-level validation.
- No balance or MTTH validation was run because the parent prompt explicitly excluded those files.
- No scripted leader randomization patch was made because it requires gameplay-script changes outside the allowed narrow patch list.

Remaining setup or identity risks:

- Decide whether the 2026-05-27 promoted ordinary/internal generated council portraits should stay institutional councils or become named one-person leaders with regional random-name pools.
- Wire or explicitly reject the generated ordinary/internal council portrait batches so the sidecar files do not remain ambiguous.
- Add package-specific AI strategy coverage for `CFR`, `MFR`, `KZR`, `SOG`, `KHW`, and `ALN` in a main-agent balance-safe pass.
- Refresh `docs/assets/005_soviet_union_collapse/manifest.md` if the later ordinary/internal portrait promotion is accepted as active package state.
