# Event 006 Railway Finisher Focus Audit

Audit timestamp: 2026-06-04 13:44:46 UTC

Role: `chaosx_focus_tree_auditor`

## Verdict

PASS for the bounded Event 006 Independence Wave railway finisher tranche.

## Changed Files

None for gameplay, localisation, specs, docs, assets, or flags.

This handoff was added:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_134446_event006_railway_finisher_focus_audit.md`

## References Consulted

- Offline Paradox wiki snapshot:
  - `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Effect - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/Idea modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/AI modding - Hearts of Iron 4 Wiki.md`
  - `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`
- Vanilla docs:
  - `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/common/script_constants/documentation.md`
- Project guidance:
  - `AGENTS.md`
  - `hoi4-focus-trees`
  - `chaos-redux-events`
  - `chaos-redux-subagents`

## Findings

1. `independence_wave_railway_league` is reachable only from the Event 006 railway path and after existing route proof.
   - Focus prerequisite is `independence_wave_railway_dispatch_ministry` in `common/national_focus/006_independence_wave_focus.txt:526`.
   - Availability requires `is_independence_wave_railway_package = yes` and `has_country_flag = independence_wave_timetable_authority_proclaimed` in `common/national_focus/006_independence_wave_focus.txt:527-530`.
   - The proclamation flag is set by `independence_wave_proclaim_timetable_authority_effect` in `common/scripted_effects/006_independence_wave_effects.txt:4948-4949`.
   - The decision that calls the proclamation effect is visible only for railway packages with bridge guard proof in `common/decisions/006_independence_wave_decisions.txt:3869-3874`.
   - The trigger behind proclamation requires railway hub control, junction committee proof, bridge guard proof, independence, legitimacy, and militia thresholds in `common/scripted_triggers/006_independence_wave_triggers.txt:1394-1401`.

2. No Event 005/PRA/Soviet Collapse coupling was found in the touched gameplay/localisation surface.
   - `rg -n "(Event 005|Event005|PRA|Soviet Collapse|soviet_collapse|PRA_)" common/national_focus/006_independence_wave_focus.txt common/script_constants/006_independence_wave_constants.txt common/scripted_effects/006_independence_wave_effects.txt localisation/english/006_independence_wave_l_english.yml` returned only separation comments/docs-localisation, not runtime dependencies.
   - The focus file explicitly says the tree avoids Event 005 route flags and Soviet Collapse helper/formable logic in `common/national_focus/006_independence_wave_focus.txt:8-10`.
   - The scripted effects header says the Event 006 helpers do not read Event 005 state in `common/scripted_effects/006_independence_wave_effects.txt:4-5`.

3. The prerequisite, available, bypass, and AI pattern matches nearby railway-package focuses.
   - `independence_wave_junction_committee_manifest`, `independence_wave_bridge_guard_mandate`, and `independence_wave_railway_dispatch_ministry` use the same package gate plus proof-flag bypass pattern in `common/national_focus/006_independence_wave_focus.txt:441-516`.
   - `independence_wave_railway_league` follows the same structure with package gate, bypass on its completion flag, `available_if_capitulated = yes`, completion helper, and scoped AI modifiers in `common/national_focus/006_independence_wave_focus.txt:519-543`.
   - The corrected live coordinate is `x = 8`, `y = 11` in `common/national_focus/006_independence_wave_focus.txt:523-524`.

4. Rewards are centralized through script constants and use valid HOI4 effect scopes.
   - New constants are present in `common/script_constants/006_independence_wave_constants.txt:1097-1100`.
   - The focus calls one scripted effect in `common/national_focus/006_independence_wave_focus.txt:535-537`.
   - The effect sets a completion flag, adds cohesion and legitimacy from constants, adds train equipment with constant amount, then scopes rail construction through `random_owned_controlled_state` before calling `add_building_construction` in `common/scripted_effects/006_independence_wave_effects.txt:4994-5008`.
   - Vanilla docs confirm `add_equipment_to_stockpile` is country-scope and `amount` may be a variable/constant-backed value; `add_building_construction` is state-scope.

5. Localisation and docs are aligned.
   - Localisation keys are present without `:0` in `localisation/english/006_independence_wave_l_english.yml:417-418`.
   - The localisation file is UTF-8 with BOM per `file localisation/english/006_independence_wave_l_english.yml`.
   - Event docs describe the railway finisher and rewards in `docs/events/006_independence_wave.md:128`.
   - The focus-tree spec records the railway finisher in `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md:514-527`.
   - Actual focus count is 110 by `rg -n "focus = \\{" common/national_focus/006_independence_wave_focus.txt | wc -l`; docs record 110 focuses in `docs/events/006_independence_wave.md:158`.

6. No unsupported operator, localisation key format, or asset-reference issue was found in the touched surface.
   - `rg -n "(<=|>=|:0)"` over the audited focus/constants/effects/localisation/docs files returned no matches.
   - The focus reuses `GFX_focus_independence_wave_railway_yard` in `common/national_focus/006_independence_wave_focus.txt:521`.
   - That sprite is registered in `interface/006_independence_wave_icons.gfx:214-217`.

## Coordinate Check

Current live coordinate scan confirms:

- `(8,11)` contains only `independence_wave_railway_league`.
- `(10,11)` contains `independence_wave_send_permanent_delegation`.
- Remaining duplicate coordinates are pre-existing overlay-family overlaps outside this tranche and do not include `independence_wave_railway_league`.

## Validation Commands

- `rg --files paradox_wiki | rg 'Data structures|Triggers|Effects|Modifiers|Localisation|Scopes|On actions|Event modding|Decision modding|Idea modding|AI modding|National focus'`
- `rg --files '/home/klim/projects/Hearts of Iron IV/documentation' | rg 'focus|effect|trigger|locali[sz]ation|script_constant|script_concept'`
- `rg -n "independence_wave_(repair_the_rail_yard|junction_committee_manifest|bridge_guard_mandate|railway_dispatch_ministry|proclaim_timetable_authority|integrate_corridor_timetables|railway_league|send_permanent_delegation|formation_ledger|reveal_the_formation_ledger)" common/national_focus/006_independence_wave_focus.txt`
- `rg -n "independence_wave_focus_(junction_committee_manifest|bridge_guard_mandate|railway_dispatch_ministry|proclaim_timetable_authority|integrate_corridor_timetables|railway_league)|railway_league_|package_route_train_gain|package_route_building_level" common/scripted_effects/006_independence_wave_effects.txt common/script_constants/006_independence_wave_constants.txt`
- `rg -n "GFX_focus_independence_wave_railway_yard|GFX_focus_independence_wave_military_supply|GFX_focus_independence_wave_formation_ledger" interface common/national_focus/006_independence_wave_focus.txt`
- `file localisation/english/006_independence_wave_l_english.yml`
- `rg -n "(<=|>=|:0)" common/national_focus/006_independence_wave_focus.txt common/script_constants/006_independence_wave_constants.txt common/scripted_effects/006_independence_wave_effects.txt localisation/english/006_independence_wave_l_english.yml docs/events/006_independence_wave.md docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `rg -n "(Event 005|Event005|PRA|Soviet Collapse|soviet_collapse|PRA_)" common/national_focus/006_independence_wave_focus.txt common/script_constants/006_independence_wave_constants.txt common/scripted_effects/006_independence_wave_effects.txt localisation/english/006_independence_wave_l_english.yml`
- Coordinate scan with a small read-only Python parser over `common/national_focus/006_independence_wave_focus.txt`.

## Residual Risks

- This audit did not run HOI4 itself.
- The repository working tree is heavily dirty/untracked; unrelated Event 005/Event 006 changes were not audited.
- Existing duplicate coordinates in overlay-family rows remain outside this tranche.
