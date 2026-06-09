# Event006 No More Flags Needed Achievement Handoff

## Scope

Implemented the Event 006 final-settlement achievement `cr_no_more_flags_needed` and its player decision gate. This is a bounded achievement/decision tranche. It does not claim full Event 006 completion.

## Changed files

- `common/achievements/chaos_redux_achievements.txt`
- `common/decisions/006_independence_wave_decisions.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_triggers.txt`
- `interface/chaosx_achievements.gfx`
- `localisation/english/006_independence_wave_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `docs/events/006_independence_wave.md`
- `docs/systems/custom_achievements.md`
- `docs/assets/006_independence_wave/achievement_icons/manifest.md`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet.png`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/raw_sources_64_contact.png`
- `docs/assets/006_independence_wave/achievement_icons/contact_sheets/achievement_icon_contact_sheet_all_states.png`

Asset subagent output:

- `docs/assets/006_independence_wave/achievement_icons/prompts/cr_no_more_flags_needed.txt`
- `docs/assets/006_independence_wave/achievement_icons/source_png/cr_no_more_flags_needed_source.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_no_more_flags_needed.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_no_more_flags_needed_grey.png`
- `docs/assets/006_independence_wave/achievement_icons/processed_png/cr_no_more_flags_needed_not_eligible.png`
- `gfx/achievements/cr_no_more_flags_needed.dds`
- `gfx/achievements/cr_no_more_flags_needed_grey.dds`
- `gfx/achievements/cr_no_more_flags_needed_not_eligible.dds`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_no_more_flags_needed_icon_handoff.md`

Localisation audit output:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_31_event006_final_settlement_localisation_audit_handoff.md`

## Gameplay behavior

- Added `independence_wave_certify_final_settlement` to the New States Congress category.
- The decision requires:
  - independent Event 006 release achievement eligibility
  - New States Congress delegates
  - League founder proof
  - integrated Regional Compact
  - recognized Compact Secretariat
  - anti-puppet clause
  - mass-wave host-survival proof
  - five mutual guarantees
  - three peaceful Border Commission resolutions
  - no dossier ultimatum
  - no patron-accepted route
  - no world-end bypass
  - no current war
- The decision spends command power through `custom_cost_trigger`/`custom_cost_text`, records `chaosx_iw_final_settlement_certified`, adds cohesion, legitimacy, and stability, and updates achievement tracking.
- Added achievement `cr_no_more_flags_needed`, which unlocks from the certified final-settlement proof and repeats the major disqualifiers.

## Assets

- `chaosx_icon_artist` produced the final achievement icon triplet with `fork_context=false`.
- Icon uses generic folded banners in a calm map room, with no real country flag or real national symbol.
- Registered `GFX_achievement_cr_no_more_flags_needed` and grey/not-eligible variants in `interface/chaosx_achievements.gfx`.

## Validation

- Brace balance passed for touched script/interface files.
- Unsupported inclusive-operator scan found no raw less-than-or-equal or greater-than-or-equal tokens in touched script, localisation, docs, or interface files.
- Localisation files remain UTF-8 with BOM and have no `:0` keys.
- Final-settlement cost text has base, `_blocked`, and `_tooltip` variants.
- `identify` and `file` validate the `cr_no_more_flags_needed` processed PNGs and DDS files as `64 x 64`.
- `git diff --check` passed.

## Remaining work

- League-war and human-renunciation achievement clusters remain follow-up work.
- The final-settlement decision uses explicit requirements and static cost text; a dynamic cost scripted-localisation helper could reduce future drift but was outside this bounded tranche.
