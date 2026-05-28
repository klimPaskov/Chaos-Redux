# Event 005 Country Asset And Name Audit Refresh

Date: 2026-05-28

Scope: country-package asset/name audit only for Event 005 Soviet Collapse. No balance, MTTH, focus reward, decision, map, military, or AI behavior edits were in scope. No binary asset regeneration was performed.

## Country Package Coverage Checklist

- Custom Event 005 one-person portrait tags checked: `ALA`, `ARD`, `BAC`, `BBH`, `BSC`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KRS`, `MRC`, `NLC`, `NRF`, `PRA`, `RMC`, `SDZ`, `SZA`, `TNC`, `TSC`, `UDC`, `UWD`.
- Custom Event 005 institutional/factory/ancient portrait tags checked: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`.
- Vanilla-supported or existing release/support tags checked for council naming and no default flag override: `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, `TAN`.
- User-complaint/high-risk custom ideology flag families checked for presence: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR`, `OGB`, plus `PRA`, `MFR`, and route/cosmetic family `UKR_BLACK_BANNER`.

## File Surface Checklist

- Read required repo guidance: `AGENTS.md`.
- Read required skills: `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`.
- Consulted required offline wiki pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, and National focus modding.
- Consulted vanilla docs: `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`.
- Read clean merged specs: `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_final_clean_merged_part_6_countries_splinters_restorations.md` and `part_7_assets_achievements_validation.md`.
- Audited current implementation surfaces: `history/countries/<TAG> - *.txt`, `common/scripted_effects/005_soviet_collapse_effects.txt`, `interface/005_soviet_collapse_custom_icons.gfx`, `interface/005_soviet_collapse_factory_ancient_icons.gfx`, `docs/assets/005_soviet_union_collapse/manifest.md`, `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28*/`, `gfx/leaders/005_soviet_collapse/`, `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.

## Missing Or Stale Country Package Surfaces

- No missing audited live leader DDS file was found for the scoped custom, existing-release council, or recently promoted republic council tags.
- No audited leader DDS decoded outside `156x210`.
- No duplicate SHA-256 hash group was found in the audited live leader DDS subset.
- No missing high-risk custom ideology flag file was found. Checked tags have base plus `_communism`, `_democratic`, `_fascism`, and `_neutrality` in normal, medium, and small folders.
- No mod-side default/base or ideology flag override file was found for the audited existing vanilla-supported tags. `UKR_BLACK_BANNER` remains a separate cosmetic/route family.

## Map And State Setup Issues

- Not audited by this bounded task. No map or state setup files were edited.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- Female-presenting one-person portraits are guarded correctly: `BAC`, `NLC`, `TSC`, `UDC`, and `UWD` set `female = yes`, set `soviet_collapse_female_single_person_leader_portrait`, and use only female-gated random-name pools.
- Male-presenting one-person portraits are guarded correctly: `ALA`, `ARD`, `BBH`, `BSC`, `DHC`, `DSC`, `FEV`, `FTH`, `GAC`, `ICD`, `IUL`, `KHC`, `KRS`, `MRC`, `NRF`, `PRA`, `RMC`, `SDZ`, `SZA`, and `TNC` set `soviet_collapse_male_single_person_leader_portrait`, do not set `female = yes`, and use only male-gated random-name pools.
- Institutional/factory/ancient tags are guarded correctly in current history: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, and `ALN` keep institutional names and do not call `soviet_collapse_randomize_single_person_leader_name`.
- The random-name helper defensively marks institutional tags as already randomized if accidentally called, preventing personal names for `CFR`, `MFR`, `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `ALN`, `KHW`, `KZR`, `OGB`, and `SOG`.
- Existing-release council helper `soviet_collapse_apply_event_created_republic_council_leader` uses institutional names for `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN`.
- Visual spot-checks matched metadata expectations: `custom_country_leaders_labeled.png` shows `BAC`, `NLC`, `TSC`, `UDC`, and `UWD` as female-presenting one-person portraits; `KRS`, `RMC`, and `SDZ` as male-presenting one-person portraits; and `CFR`/`MFR` as factory/institutional portraits. `event005_vanilla_supported_release_council_portraits.png` uses council/institutional names.

## Focus, Decision, Idea, And Asset Issues

- No focus, decision, idea, or asset wiring changes were made.
- Recent user-complaint/high-risk flag families are present in all checked active paths: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR`, `OGB`, `PRA`, `MFR`, and `UKR_BLACK_BANNER`.
- `UKR_BLACK_BANNER` is applied as a cosmetic route tag from `common/national_focus/005_soviet_collapse_republics.txt` and does not create a default `UKR` flag override.

## Starting Military, Technology, Industry, Supply, And Production Issues

- Not audited by this bounded task. No starting army, technology, industry, supply, stockpile, or production files were edited.

## AI And Playability Issues

- Not audited by this bounded task. No AI strategy, focus AI, decision AI, or playability balance files were edited.

## Changed Files

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_country_asset_name_audit_refresh.md`

## Changed Tags, State IDs, Leaders, Parties, Focus Tree IDs, Localisation Keys, Or Formable IDs

- None. No gameplay identifiers, tags, states, leaders, parties, focus tree ids, localisation keys, scripted helpers, or formable ids were changed.

## Before And After Behavior

- Before: gameplay and assets were already in the current dirty worktree state.
- After: no gameplay or asset behavior changed. The parent now has a fresh audit confirming the current portrait/name guard and high-risk flag presence state.

## Validation Run

- `git status --short`: confirmed a heavily dirty shared worktree before this pass; treated existing Event 005 changes as other work.
- Leader metadata audit script:
  - female tags: `BAC NLC TSC UDC UWD`
  - male tags: `ALA ARD BBH BSC DHC DSC FEV FTH GAC ICD IUL KHC KRS MRC NRF PRA RMC SDZ SZA TNC`
  - institutional tags: `ALN CFR KHW KZR MFR OGB SOG`
  - `leader_metadata_issues 0`
- Random-name pool parser:
  - `random_name_pool_counts {'female': 15, 'male': 60, 'institutional': 0, 'unexpected': 0}`
  - `random_name_gate_issues 0`
- Release council helper extract: `MOL`, `UZB`, `TAJ`, `TMS`, `FER`, `EST`, `LAT`, `ARM`, `KAR`, `KOM`, `CRI`, `BSK`, `YAK`, `BYA`, and `TAN` all had institutional leader names.
- Existing vanilla-supported flag override check: no output, meaning no audited `gfx/flags/<TAG>.tga` or ideology override files exist for the scoped existing tags.
- High-risk custom ideology flag presence check: `missing_count=0`.
- `identify` flag dimension spot-check for high-risk families: no bad-size output; checked standard `82x52`, `41x26`, and `10x7` paths.
- `identify` leader dimension check for audited leaders: no bad-size output; checked `156x210`.
- SHA-256 duplicate check for audited leaders: no duplicate output.
- Visual spot-checks:
  - `docs/assets/005_soviet_union_collapse/contact_sheets/custom_country_leaders_labeled.png`
  - `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_live_audit_refresh/contact_sheets/priority_portraits_labeled_contact.png`
  - `docs/assets/005_soviet_union_collapse/contact_sheets/event005_vanilla_supported_release_council_portraits.png`
  - `docs/assets/005_soviet_union_collapse/generated_event_art_sidecar_2026_05_28_live_audit_refresh/contact_sheets/ukr_black_banner_route_flags_normal_labeled_contact.png`

## Skipped Validation

- No in-game validation was run.
- No asset regeneration, DDS/TGA conversion, or broad visual replacement pass was run because the scope explicitly forbade regenerating large asset batches.
- No balance, MTTH, focus, decision, map, starting military, technology, industry, supply, production, AI, or playability validation was run because those surfaces were out of scope.

## Remaining Setup Or Identity Risks

- This pass did not audit the full country package checklist from the spec beyond asset/name/flag safety, so map setup, starting setup, military viability, decisions, focus depth, and AI remain outside this handoff.
- Institutional council portraits sometimes use a visible chair or speaker. Current gameplay keeps institutional names as required; if a later pass deliberately reclassifies any of those portraits as personal leaders, it must add matching gender metadata and remove institutional-name assumptions.
- Visual uniqueness is ultimately an art-direction call. This pass verified presence, dimensions, no existing-country default overrides, and spot-checked the complaint families; it did not regenerate art or claim every flag is final art-direction approved.

## Plan Handoff Path

- This file is the handoff: `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_country_asset_name_audit_refresh.md`
