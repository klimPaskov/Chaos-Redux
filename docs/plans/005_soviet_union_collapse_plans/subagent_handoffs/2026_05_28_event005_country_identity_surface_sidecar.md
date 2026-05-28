# Event 005 Country Identity Surface Sidecar

Date: 2026-05-28

Scope: bounded country-package identity audit for Event 005 Soviet Collapse. This sidecar checked generated leader portrait classification against country history naming/metadata and checked existing-country base-flag override risk. No binary flags or portraits were generated or edited.

## Country Package Coverage Checklist

- Custom Event 005 tag registration checked in `common/country_tags/chaosx_countries.txt`: `CFR`, `MFR`, `OGB`, `KZR`, `SOG`, `KHW`, `ALN`, `KRS`, `FTH`, `BBH`, `BSC`, `RMC`, `DSC`, `NRF`, `TNC`, `ALA`, `UDC`, `SDZ`, `GAC`, `DHC`, `KHC`, `FEV`, `SZA`, `UWD`, `MRC`, `IUL`, `BAC`, `PRA`, `TSC`, `ICD`, `ARD`, `NLC`.
- Manifest-classified portrait risk set checked against current history files: `CFR`, `KRS`, `RMC`, `SDZ`, `TSC`, `UDC`, `SOG`, `ALN`, `KHW`, `KZR`, `OGB`.
- Existing-game Event 005 release/support flag override set checked: `UKR`, `BLR`, `KAZ`, `MOL`, `LIT`, `LAT`, `EST`, `GEO`, `ARM`, `AZR`, `UZB`, `KYR`, `TAJ`, `TMS`, `KAR`, `KOM`, `CRI`, `TAT`, `BSK`, `FER`, `YAK`, `BYA`, `TAN`.
- Cosmetic route flag checked as a separate non-base tag: `UKR_BLACK_BANNER`.

## File Surface Checklist

- Read: `AGENTS.md`.
- Read skills: `.agents/skills/chaos-redux-event-assets/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`.
- Consulted offline wiki pages: `Data structures`, `Triggers`, `Effect`, `Modifiers`, `Localisation`, `Scopes`, `On actions`, `Event modding`, `Decision modding`, `Idea modding`, `AI modding`, and `Country creation`.
- Consulted vanilla docs: `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `modifiers_documentation.md`, `loc_objects_documentation.md`, `loc_formatter_documentation.md`.
- Read current Event 005 surfaces: `history/countries/*` for the bounded tags, `localisation/english/005_soviet_collapse_custom_countries_l_english.yml`, `docs/assets/005_soviet_union_collapse/manifest.md`, `common/countries/cosmetic.txt`, and `gfx/flags*/` path inventory.

## Missing Or Stale Country Package Surfaces

- No missing history file was found for the 32 registered custom Event 005 tags.
- No stale existing-country base flag override path was found for the audited existing-game tags.
- `UKR_BLACK_BANNER` remains a separate cosmetic flag family, not a `UKR` base flag override.

## Map And State Setup Issues

- Not audited in this bounded sidecar. No map or state setup files were edited.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

- No current safe patch was needed.
- `KRS`, `RMC`, and `SDZ` are manifest-classified as male-presenting one-person portraits and currently use `soviet_collapse_male_single_person_leader_portrait` plus the single-person randomizer, with no `female = yes`.
- `TSC` and `UDC` are manifest-classified as female-presenting one-person portraits and currently use `female = yes`, `soviet_collapse_female_single_person_leader_portrait`, and the single-person randomizer.
- `CFR`, `SOG`, `ALN`, `KHW`, `KZR`, and `OGB` are manifest-classified as institutional/council portraits and currently keep fixed institutional names without gendered personal metadata or personal random-name calls.
- `ALN` current live history keeps `name = "The Alan Pass Council"` and does not contain `soviet_collapse_randomize_single_person_leader_name`.
- Localisation supports the institutional `ALN` identity with `ALN_leader_desc`, `ALN_neutrality_party`, and `ALN_neutrality_party_long`; no localisation patch was required.

## Focus, Decision, Idea, And Asset Issues

- Not patched. Focus, decision, idea, `.gfx`, scripted effect, scripted trigger, constant, music, and unrelated event files were intentionally not edited.
- Asset manifest identity rules for the checked portrait set are internally consistent with current history setup.

## Starting Military, Technology, Industry, Supply, And Production Issues

- Not audited in this bounded sidecar. No starting military, technology, industry, supply, or production setup files were edited.

## AI And Playability Issues

- Not audited in this bounded sidecar. No AI or playability files were edited.

## Existing-Country Base-Flag Override Check

- Direct path scan found no `gfx/flags/<TAG>.tga`, `gfx/flags/<TAG>_<ideology>.tga`, `gfx/flags/medium/<TAG>*.tga`, or `gfx/flags/small/<TAG>*.tga` for the audited existing-game tags.
- `common/countries/cosmetic.txt` defines `UKR_BLACK_BANNER` as a cosmetic country color entry only.

## Changed Files

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026_05_28_event005_country_identity_surface_sidecar.md`

## Changed Tags, State IDs, Leaders, Parties, Focus Tree IDs, Localisation Keys, Or Formable IDs

- None.

## Before And After Behavior

- Before: current live country history and localisation already matched the bounded portrait/name/gender and existing-country base-flag rules.
- After: no gameplay behavior changed. The parent now has a separate read-only sidecar handoff for the current country identity surface state.

## Validation Run

- `rg` audit of manifest-classified portrait tags against current `history/countries/*` confirmed expected `name`, `picture`, `female = yes`, `soviet_collapse_male_single_person_leader_portrait`, `soviet_collapse_female_single_person_leader_portrait`, and `soviet_collapse_randomize_single_person_leader_name` usage.
- `rg --files gfx/flags gfx/flags/medium gfx/flags/small` audit found no existing-game base or ideology flag override files for the audited existing-game tag set.
- `rg` in `localisation/english/005_soviet_collapse_custom_countries_l_english.yml` confirmed `ALN` institutional country/party/leader text exists.

## Skipped Validation

- No in-game validation was run.
- No binary flag or portrait validation was run because this sidecar was explicitly barred from editing or generating binary assets.
- No focus, decision, scripted effect, scripted trigger, constant, music, map, balance, AI, or military validation was run because those surfaces were outside scope.

## Remaining Setup Or Identity Risks

- This sidecar did not visually reclassify every generated portrait in the package; it used the current manifest and handoff classification for the active high-risk portrait set.
- Other custom tags with institutional-sounding placeholder names may still be intentional one-person portrait setups if their portrait art was classified outside the checked manifest risk set.
- The broader active worktree already contains unrelated dirty Event 005 changes. This sidecar did not revert or normalize them.
