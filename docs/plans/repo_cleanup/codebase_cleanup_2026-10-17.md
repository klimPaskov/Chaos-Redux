# Codebase cleanup — 2026-10-17

Repository-wide dead-code, duplication and reference-integrity cleanup, run with the `chaos-redux-codebase-cleanup` skill and `.tools/audit_script_references_static.py`.
Base commit `b4dc57c08`; cleanup commits `4e9041c37` to `c36f19699` (9 commits, 266 files, about 12,000 lines removed and 2,300 added).
Disposition: implemented for the committed groups; the design decisions listed below are unresolved.
Validation limits: every removed name was re-searched across script, interface, localisation, docs, skills and tools with zero live references; brace balance, BOM and line endings were checked on every touched file; touched `.tools/test_*` suites pass; no in-game run was made.

## Commits

| Commit | Area | Summary |
|---|---|---|
| `4e9041c37` | Event 006 | 281 byte-identical per-package helpers replaced by shared effects and triggers in the Event 006 decision helper files; dead aliases, triggers, selectors and 8 constant categories removed. |
| `59edbf0cf` | CBRN | 3 dead trigger files, 28 constant categories and 2 opinion modifiers removed; identical helper pairs delegate to one body; always-true/false sabotage flag checks removed; chemical doomsday requirement tooltips added. |
| `c60c53bde` | Core systems | Dead crisis-pressure, scenario and settings helpers, the outdated welcome event and an empty scenario stub removed; Fury payments, death-environment multipliers and startup facility/grant helpers shared; dynamic effects index completed. |
| `62ac8d64f` | Fallout | 31 dead target triggers removed; 41 callback admission triggers delegate to delayed-result triggers; shared pilot roster; Event 243 factory-removal marker set as the flag its guard reads. |
| `12e4560f6` | Humanitarian | 30 unused scripted-localisation selectors with 92 keys, two famine aliases, one runtime effect and two constant categories removed. |
| `c266656ee` | Events 021+ | 44 triggers, 3 effects, 29 selectors with 55 keys and 22 constant categories removed; Event 027 Special Forces steps shared; Event 039 and Event 025 identical effects merged. |
| `f7229cfe3` | Tooling | `audit_script_references_static.py` and the `chaos-redux-codebase-cleanup` skill. |
| `6f37b6085` | Events 001–020 | Dead selectors (178 keys), effects, triggers and 50 constant categories removed; retired Event 013 per-family reports, Event 005 custom successor events and 622 orphaned Event 005 sprites removed; two identical pairs merged; Black Plague royal basin flag fixed. |
| `c36f19699` | Localisation | 56 requirement flags shown in decision, mission and focus tooltips localised. |

## Behaviour changes

- `black_plague_rat_transfer_to_king` sets `black_plague_royal_basin`, the flag the Crown Strike target, royal-seal and aftermath checks read; the previously set name was never read.
- `fallout_event_243_apply_factory_commitment` sets the country flag its guard and cleanup read instead of a variable of the same name; the only caller already ran once, so play is unchanged.
- Requirement tooltips show text instead of raw flag identifiers.

## Audit before and after

| Measure | Before | After |
|---|---|---|
| Exact clone groups (effects and triggers) | 186 | 99 |
| Unreferenced events (literal and built ids) | 1,410 literal-only | 15 |
| Exposed requirement flags | 56 | 0 |

The remaining `dead` counts are verified keeps: the generated per-state registry triggers (5,405), names built at runtime, documented APIs and hooks, CXT setup, generated catalogs, trigger names that double as tooltip keys, and code in files with other uncommitted work.

## Design decisions needed

Lost wiring or regressions:
- Fallout `chaosx.fallout.852` to `858` (The First Regional Standard) were overwritten by commit `edb4ee710`; restore from `d1e42a5d4`. `events/fallout_world_end_events.txt` has other uncommitted work.
- Event 021 critical-launch helpers have no caller and nothing fires `chaosx.nr21.18`, although the docs say the scheduler does both.
- `chaosx_bioweapon.207`/`.208` (first smallpox use and arrival news) and `chaosx_contamination.5`/`.6` (nuclear winter news) lost their callers in `de656ed03`.
- `chaosx.news.84` lost its only caller in `ebc2199c5`.
- Camp checks of `camp_rework_pingfang_anchor` and related flags never pass since the legacy setters were removed in `1850d88c3`, including the Japan and Manchukuo subject-authority branch.

Flags checked but never set (feature never applies):
- `cbrn_achievement_covert_coverup_history` (cover-up exclusion of the "Clean Hands, Dirty Work" achievement), `cbrn_active_distribution_disruption` (mask distribution cost multiplier), `smallpox_vaccination_protection_active` (vaccination never reduces contamination).
- `chaos_meter_deaths_details_open` (Deaths details view never refreshes live).
- `germany_mengele_civil_war_country` / `germany_mengele_post_coup_state` (the faction uses `germany_mengele_faction`).
- `black_plague_rat_brood_succession_crisis` (the brood succession decision is unreachable).
- `fallout_event_{614,621,740,747}_target_invalidated` (siblings 579, 586, 600 and 607 set theirs).
- `missiles_special_payload_compromised`.
- Event 006 `recognition_blockade_active`, `permanent_border_war_active`, the IW-046 Chuvashia flag and two league-collapse flags; `independence_wave_iw093_government_route_locked` looks like a typo for the shared route lock.

Unwired features:
- Event 039 `murder_mystery_focus_veiled_compact` has no caller, so the Necessary Hypocrisy achievement cannot be earned.
- Event 029 mine quarantine and exhaustion are set only by two unwired effects.
- Event 012 `africa_breach_first_proof_*` helpers have no caller.
- The migration closed-border report scene is complete but never triggered.
- 32 fallout event-log blocks are never called while sibling chains use theirs.

Consolidation proposals left for their owners:
- Event 19 providers carry byte-identical `pay_management_action`, `refund_management_action` and `get_equipment_token` hooks (8 copies each); shared defaults behind one-line wrappers would save about 140 lines.
- `black_friday_cbrn_decon_sale_source_is_active` duplicates `cbrn_protective_aid_sale_source_is_active`; `020_black_plague_scenario_effects.txt` writes `global.chaos_meter_value` directly.

## Not cleaned, with reason

- Files with other uncommitted work at the time of the cleanup (Event 005, 014, 019, 021, 023, 033, 038 and others); each subsystem handoff lists the dead code found there for a later pass.
- Unreferenced sprites outside the removed Event 005 routes: the asset audit does not model implicit engine naming, so they stay.
- 239 image files left orphaned by the removed Event 005 and Event 013 sprites are listed in the cleanup scratch folder and were not deleted.
- `chaosx_nr25_incident` is declared in both Event 025 field and incident constants files with disjoint keys; it loads without error and was left as it is.
- `docs/events/005_soviet_collapse/overview.md` and `common/scripted_effects/cbrn_scripted_effects.md` contain stale references but have other uncommitted work.
