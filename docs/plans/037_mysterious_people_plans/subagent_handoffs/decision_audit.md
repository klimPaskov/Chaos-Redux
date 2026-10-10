# Event 037 Mysterious People: decision category audit and patch handoff

Status: patched locally, not committed, not launched in game. Disposition: implemented for the patched items; remaining risks listed below are unresolved.

## Scope and sources

Reviewed: `common/decisions/037_mysterious_population_decisions.txt`, `common/decisions/categories/037_mysterious_population_categories.txt`, `common/scripted_effects/037_mysterious_population_decision_effects.txt`, `common/scripted_effects/037_mysterious_population_effects.txt`, `common/scripted_triggers/037_mysterious_population_triggers.txt`, `common/script_constants/037_mysterious_population_constants.txt`, `common/dynamic_modifiers/037_mysterious_population_dynamic_modifiers.txt`, `common/mtth/037_mysterious_population_mtth.txt`, `localisation/english/037_mysterious_population_l_english.yml`, the spec part 4 (`docs/specs/037_mysterious_people_specs/specs/037_mysterious_people_spec_part_4_decisions_missions_and_ai.md`), and the decisions skill with its cost-payment and category-presentation references.

Sources read directly: `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` (mission `available`, `is_good`, `selectable_mission`), vanilla `common/decisions/_documentation.md` (target scopes and daily target checks), vanilla `AST.txt` mission with `is_good = yes`, vanilla `documentation/dynamic_variables_documentation.md` (reader names), vanilla `documentation/effects_documentation.md`, and repo precedents (`days_re_enable = constant:`, `target_array = <name>`, `custom_cost_trigger` with `set_temp_variable`).

Not run: the `hoi4.*` MCP reference, decision-inspect, and probability routes were not invoked in this pass; source reads were used instead. No game was launched. No commit was made.

Existing AI scenarios reused: `docs/specs/037_mysterious_people_specs/quality/037_mysterious_people_probability_scenarios.md` (EV37-POL-001 to 004, EV37-ACT-001, 002, 003, 005, 007). Each was checked by hand against the current `ai_will_do` blocks and still holds. No `ai_will_do` value or weight was changed, so no re-route to `chaosx_ai_probability_auditor` was needed.

## Issues, sorted by severity

1. High. Hotspot action rows were gated by the daily `target_trigger`, not by live visibility. `mysterious_people_requisition`, `mysterious_people_emergency_housing`, `mysterious_people_roads_water`, and `mysterious_people_new_city` used `mysterious_people_hotspot_actions_are_shown` in `target_trigger`, which the decisions documentation says is checked once per day. A human's selection therefore reached the action rows only at the next daily target refresh, and closing the selection kept the rows visible until then. The close row (`mysterious_people_close_hotspot`) had the same gap through `target_root_trigger` and `target_trigger`. Patched (see Patches 1 and 2).
2. Medium. `mysterious_people_absorb_mission` set `is_good = yes`. The offline wiki states that `is_good = yes` relabels `complete_effect` as "Effects when failed", and vanilla uses it for timeout-as-good missions with `available = always no`. This mission completes on goal (success) and fails on timeout, so its success tooltip would be mislabelled. Patched (Patch 3).
3. Medium. Projects (`mysterious_people_emergency_housing`, `mysterious_people_roads_water`, `mysterious_people_new_city`) failed closed only on owner or controller change. The spec requires running projects to fail closed when the country stops using normal civilian systems. Patched (Patch 4).
4. Medium. Quotes went stale after a civilian transfer. `mysterious_people_on_civilian_transfer` reduced the origin backlog without refreshing the state quotes or the national values, so the displayed project quote could differ from the factories committed on click, and the Registration Drive quote and national pressure lagged until the monthly pulse. Patched (Patch 5).
5. Low. A duplicate tuning constant. `@MYSTERIOUS_PEOPLE_DRIVE_COOLDOWN = 180` duplicated `constant:mysterious_people_decision.drive_cooldown_days`. Patched (Patch 6).
6. Low, unpatched. Hard-coded values in localisation (percentages, day counts, the project slot cap of 3, and "180 days" in the stance tooltip) and the category `priority = 120` literal duplicate the constants. Listed under Unpatched risks.

## Patches (before and after)

Changed files:
- `common/decisions/037_mysterious_population_decisions.txt`
- `common/scripted_effects/037_mysterious_population_effects.txt`

Pre-patch copies are in the session scratchpad (`037_decisions_before.txt`, `037_effects_before.txt`). The patch script is `patch_037_decisions.py` in the same scratchpad. Line endings were kept as CRLF.

Patch 1. `mysterious_people_close_hotspot`.
- Before: `target_root_trigger = { is_ai = no has_variable = mysterious_people_selected_state }`, `target_trigger = { FROM = { has_state_flag = mysterious_people_selected_@ROOT } }`, no `visible`.
- After: `target_root_trigger = { is_ai = no }`, `target_trigger = { FROM = { mysterious_people_state_is_hotspot = yes } }`, `visible = { mysterious_people_category_is_relevant = yes FROM = { has_state_flag = mysterious_people_selected_@ROOT } }`.
- Behaviour: the close row appears on the selected hotspot as soon as it is selected, and disappears on close. AI never sees it (`is_ai = no` in `target_root_trigger`).

Patch 2. `mysterious_people_requisition`, `mysterious_people_emergency_housing`, `mysterious_people_roads_water`, `mysterious_people_new_city`.
- Before: `target_trigger = { mysterious_people_hotspot_actions_are_shown = yes FROM = { mysterious_people_state_is_hotspot = yes } }`. No live selection gate in `visible`.
- After: `target_trigger = { FROM = { mysterious_people_state_is_hotspot = yes } }`, and `visible` begins with `mysterious_people_hotspot_actions_are_shown = yes`.
- Behaviour: every hotspot is a target candidate for the daily check, and the live `visible` gate shows only the selected hotspot's rows for humans. AI still sees all hotspots, because `hotspot_actions_are_shown` is true for AI. AI candidate set and every `ai_will_do` block are unchanged.

Patch 3. `mysterious_people_absorb_mission`.
- Before: `is_good = yes`.
- After: line removed (default `is_good = no`).
- Behaviour: the success effects are labelled as success and the timeout as failure.

Patch 4. Project `cancel_trigger` in `mysterious_people_emergency_housing`, `mysterious_people_roads_water`, `mysterious_people_new_city`.
- Before: `cancel_trigger = { FROM = { NOT = { is_owned_and_controlled_by = ROOT } } }`.
- After: `cancel_trigger = { OR = { FROM = { NOT = { is_owned_and_controlled_by = ROOT } } NOT = { mysterious_people_country_can_use_mechanic = yes } } }`.
- Behaviour: the existing `cancel_effect` (`mysterious_people_end_project`) releases the factories, with no refund, when the country loses normal civilian systems or the state changes hands.

Patch 5. `mysterious_people_on_civilian_transfer`, origin block (effects file).
- Before: the origin block ended with `mysterious_people_clamp_state_ledger = yes`.
- After: `mysterious_people_refresh_after_state_action = yes`.
- Behaviour: the origin state's quotes and rate, its pressure, and the owner's national recount, pressure, modifier, and drive quote refresh at the departure. The helper is the same one used after every other ledger action.

Patch 6. `mysterious_people_registration_drive`.
- Before: `days_re_enable = @MYSTERIOUS_PEOPLE_DRIVE_COOLDOWN` with a local `@MYSTERIOUS_PEOPLE_DRIVE_COOLDOWN = 180`.
- After: `days_re_enable = constant:mysterious_people_decision.drive_cooldown_days` (value 180, unchanged). The local constant is removed.

Verification of the patches (source checks, not game): a diff against the pre-patch copies shows only the intended changes; brace count in the decisions file is 243 open and 243 close; no LF-only lines; no `<=` or `>=` in the decisions file.

## Category lifecycle

The category is visible only while `mysterious_people_category_is_relevant` holds: newcomers exist and there is unsettled backlog, a running project, or a pending mission. The stance rows hide after a choice and during the 180-day lock. The Registration Drive row shows whenever there is unsettled backlog, and the 180-day cooldown is `days_re_enable`. A hotspot row appears only for a hotspot, and its actions appear only after the human selects that hotspot. Projects are removed by `remove_effect` on completion, or by `cancel_trigger` (owner, controller, or mechanic loss) with `cancel_effect`.

## Cognitive load

Visible rows when nothing is selected: up to two stance rows (both visible until one is chosen; one row afterwards), one Registration Drive row, and up to eight hotspot rows. In the worst case that is eleven rows. The spec accepts eight hotspots, so this is a design question rather than a patch. Recommend the parent decide whether the hotspot list counts as one target selector (the reusable selected-target pattern in the decisions skill) or as eight rows. Selected-hotspot view: up to four actions plus the close row, which is within the six-action budget.

Visible values: the header (newcomers, pressure with stage, stance) is in the category description. Each value has a stated meaning in the category text. Pressure stage names are plain. The stance rows show the settlement factor and the 180-day lock.

## Mission quality

Absorb the Newcomers: owner Event 037; category `mysterious_people_category`; region is the whole country (national pressure); requirement is national pressure below the lower bound of the stage the mission started in; duration 180 days (`constant:mysterious_people_mission.duration_days`); success is a 180-day doubled workforce bonus and a census count; failure is -5% stability for 90 days. Duplicate risk: none (one mission per country, guarded by `mysterious_people_mission_pending`).

## Cost and requirement clarity

Cost-count audit (spendable costs per displayed action):
- Stance (Open Integration and Restricted Registration): 1 (political power 50, native `cost`).
- Registration Drive: 1 (political power, scaled from 30 to 90).
- Requisition Empty Property: 0 spendable (stability -2% is a consequence, not a payment).
- Emergency Housing: 2 (political power, civilian factories).
- Roads and Water: 2 (political power, civilian factories).
- Build a New City: 2 (political power, civilian factories).
- Absorb the Newcomers: 0 (failure stability is a consequence).

All are within the four-cost budget. Texticons: `£pol_power` and `£civ_factory` are used in every displayed cost key. `£civ_factory` is used in vanilla localisation (`localisation/braz_por/...`), and `£pol_power` is a vanilla texticon. Every custom-cost base (`mysterious_people_drive_cost`, `mysterious_people_housing_cost`, `mysterious_people_roads_cost`, `mysterious_people_city_cost`) has its `_blocked` and `_tooltip` keys. Debit: one political-power debit per action in `complete_effect` (`add_political_power` of the stored quote, negated). Factory commitment: `mysterious_people_start_project` stores the factories on the state and `mysterious_people_refresh_project_commitment` drives the `mysterious_people_projects` dynamic modifier (`civilian_factory_use`). Affordability: `mysterious_people_can_afford_project` and `mysterious_people_can_afford_drive` feed both `available` and `custom_cost_trigger`.

## AI validity and route lock

Scenario checks against current source (no weights changed):
- EV37-ACT-001 (infrastructure 2): Roads ×2 below 5 versus Housing ×0.3, so Roads leads.
- EV37-ACT-002 (infrastructure 6): Housing leads, because Roads ×0.3 at or above 5.
- EV37-ACT-003 (war, fewer than 10 free factories): project factors are 0; Drive and Requisition ×3.
- EV37-ACT-005 (Evolution III, 30 factories): New City is not zeroed by the factory floor of 25.
- EV37-ACT-007 (stability above 50%, Overcrowded): Requisition ×0.1.
- EV37-POL-001 to 004: the stance formulas give the expected leaders.

Route locks: all four hotspot action rows and the close row require a hotspot (AI evaluates hotspots directly) and ownership and control (`available`). The selected-target flag is `mysterious_people_selected_@ROOT` on the state. AI never gets the close or select rows (`is_ai = no`).

Spec gap, unpatched: the spec says projects are weighted by the hotspot's pressure and population. Current weights use tiers (emergency ×2, urban at 1,000k people ×2, industrial ×1.5, capital ×3), not a continuous pressure or population term. Changing this would be an `ai_will_do` change and would require routing to `chaosx_ai_probability_auditor`; it was left for the parent.

## Localisation and tooltips

All decision title, description, `_tt`, `_start_tt`, `_done_tt`, `custom_cost_text` base, `_blocked`, `_tooltip`, mission, and category keys resolve in `037_mysterious_population_l_english.yml`. Scripted localisation names used by the decisions (`GetMysteriousPeopleStage`, `GetMysteriousPeopleStance`, `GetMysteriousPeopleStateCause`, `GetMysteriousPeopleProjects`, `GetMysteriousPeopleTopHotspot`, `GetMysteriousPeopleNewcomers`, `GetMysteriousPeopleUnsettled`, and others) are defined in `common/scripted_localisation/037_mysterious_population_scripted_localisation.txt`. All eleven icons are defined in `interface/037_mysterious_population.gfx`. Tooltips state the actual thresholds and consequences (for example, the 25%, 30%, 50% settlement bonuses and the 90, 150, and 300-day commitments). The category picture (`GFX_mysterious_people_category_picture`) is allowed by the presentation gate: the category uses ordinary decision rows and a basic value header. The picture reference contact sheet was not inspected in this pass.

## Cleanup and exploit risk

Cleanup: projects release factories on completion, owner or controller change, and mechanic loss; selections clear on pulse when the state stops being a hotspot, or on manifestation; the mission ends on goal, on timeout, or on mechanic loss, and clears its pending flag.

Exploit checks: Registration Drive cooldown is 180 days; Requisition is once per state per year; each project is once per state; at most three projects run per country, so factory commitment is bounded. Requisition also needs Overcrowded at the state, which bounds it.

## Unpatched risks (unresolved)

1. Hotspot row count (eleven visible rows at worst). Design question for the parent.
2. Pressure and population weighting is tier-based, not continuous (see AI section). Weight change would require auditor routing.
3. Owner change while a state is selected: the country's `mysterious_people_selected_state` persists until the next monthly pulse, so the select rows stay hidden for the old owner until then. Live gates limit the impact.
4. Mission ends by goal completion (success) when the country has no unsettled newcomers, because pressure drops to 0. There is no separate cancel on zero backlog. The spec says the mission "ends" there, so the parent should confirm that success is intended.
5. Targeted `custom_cost_trigger` and `hidden_trigger` read `FROM` and use `set_temp_variable`. Repo precedent exists (for example `common/decisions/005_soviet_collapse_decisions.txt`), but no vanilla precedent was found in this pass. Live behaviour is for the user to verify.
6. Hard-coded numbers in tooltips and category text (for example "20%", "-2%", "90 days", "3" project slots, "180 days"). They would drift if constants changed. Category `priority = 120` duplicates `constant:mysterious_people_decision.category_priority`. `@MYSTERIOUS_PEOPLE_STANCE_PP = 50` duplicates `constant:mysterious_people_decision.stance_pp`, which appears unused.
7. Building amounts in the effects file (`@MYSTERIOUS_PEOPLE_ROADS_INFRASTRUCTURE` and related) mirror decision constants. The file says building effects reject constants, so this stays duplicated.
8. Select and close rows and the stance `available` gate have no effect or custom tooltip. Low severity, navigation only.
9. Stance re-choice: after the 180-day lock, the chosen stance's row hides and the other row appears. The parent should confirm this is the intended switch path.
10. Race between completion and cancel on the same day cannot be checked without the engine.

## Validation limits

Source-only checks above. No game launch and no in-game testing. Decision-AI classification (`hoi4.decision_inspect`) and probability routes were not run. The patched files are untracked new Event 037 work, so there is no git diff baseline; the pre-patch copies in the scratchpad serve as the baseline.
