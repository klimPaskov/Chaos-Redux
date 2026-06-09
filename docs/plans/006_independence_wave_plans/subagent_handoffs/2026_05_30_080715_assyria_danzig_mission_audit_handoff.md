# Event 006 Assyria/Danzig Mission Audit Handoff

Timestamp: 2026-05-30 08:07:15 UTC

## Scope

Audited the narrow parent patch for Event 006 Independence Wave post-formation timed missions:

- `independence_wave_integrate_assyrian_recognition_congress`
- `independence_wave_integrate_danzig_free_city_charter`
- `has_independence_wave_assyrian_congress_failure`
- `has_independence_wave_danzig_charter_failure`
- `independence_wave_finish_assyrian_recognition_integration`
- `independence_wave_discredit_assyrian_recognition_congress`
- `independence_wave_finish_danzig_free_city_integration`
- `independence_wave_discredit_danzig_free_city_charter`

No flags, flag asset files, focus trees, Event 005 files, or broader Event 006 surfaces were edited.

## Files Changed

- Added this handoff only: `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_05_30_080715_assyria_danzig_mission_audit_handoff.md`

No gameplay, localisation, docs, asset, flag, or scripted helper files were changed.

## Findings

High severity: none found in the Assyria/Danzig mission blocks.

Medium severity: none found in the Assyria/Danzig mission blocks.

Low severity / out of scope: `independence_wave_integrate_corridor_timetables` still uses the older railway mission shape without the newer `selectable_mission = no`, wrapped failure tooltip, or `hidden_effect` presentation used by Assyria, Danzig, Buganda, and Sokoto. This was not patched because the prompt limited fixes to the touched Assyria/Danzig mission blocks and explicitly excluded broader Event 006 work.

## Decision Category Lifecycle Notes

Owner: Event 006 released country.

Category: `independence_wave_formation_ledger_category`.

Assyria lifecycle:

- Opens through the Assyrian recognition congress package.
- `independence_wave_proclaim_assyrian_recognition_congress` sets the proclamation flag.
- `independence_wave_integrate_assyrian_recognition_congress` activates after proclamation if the mission has not already integrated or failed.
- Mission failure completes early if Assyria becomes a subject or loses Mosul ownership/control.
- Mission success fires on timeout if Assyria remains independent and keeps Mosul.

Danzig lifecycle:

- Opens through the Danzig Free City board package.
- `independence_wave_recognize_danzig_free_city` sets the charter recognition flag.
- `independence_wave_integrate_danzig_free_city_charter` activates after recognition if the mission has not already integrated or failed.
- Mission failure completes early if Danzig becomes a subject or loses city ownership/control.
- Mission success fires on timeout if Danzig remains independent and keeps the city.

Both missions use `selectable_mission = no`, so they behave as auto-resolving timed objectives rather than player-clicked failure buttons.

## Mission Quality Notes

Assyria:

- Owner: ASY Event 006 release.
- Category: `independence_wave_formation_ledger_category`.
- Region/state requirement: Mosul, state `676`.
- Requirement: own and control Mosul, remain independent.
- Duration: `@independence_wave_assyrian_integration_days = 105`.
- Success: `independence_wave_finish_assyrian_recognition_integration` sets integrated flag, stage variable, cohesion gain, old-state memory gain, and a Mosul infrastructure improvement when valid.
- Failure: `independence_wave_discredit_assyrian_recognition_congress` sets failed flag and adds pressure.
- Duplicate risk: low, because activation checks both integrated and failed flags.

Danzig:

- Owner: DNZ Event 006 release.
- Category: `independence_wave_formation_ledger_category`.
- Region/state requirement: Danzig, state `85`.
- Requirement: own and control Danzig, remain independent.
- Duration: `@independence_wave_danzig_integration_days = 95`.
- Success: `independence_wave_finish_danzig_free_city_integration` sets integrated flag, stage variable, cohesion gain, foreign-attention gain, and a Danzig infrastructure improvement when valid.
- Failure: `independence_wave_discredit_danzig_free_city_charter` sets failed flag and adds pressure.
- Duplicate risk: low, because activation checks both integrated and failed flags.

## Cost and Requirement Clarity Notes

- No click cost is required for either post-formation mission; the mission is an ongoing timed objective.
- Failure requirements are wrapped in custom trigger tooltips:
  - `independence_wave_integrate_assyrian_recognition_congress_failure_tt`
  - `independence_wave_integrate_danzig_free_city_charter_failure_tt`
- Player-facing mission descriptions name the state condition plainly rather than exposing raw trigger blocks.
- Duration uses local decision-file constants, matching the existing `days_mission_timeout = @...` pattern in this file.

## AI Validity and Route-Lock Notes

- The missions are auto-resolving and do not need `ai_will_do` blocks.
- Activation is route-locked by package triggers and proclamation/recognition flags:
  - `is_independence_wave_assyria_package = yes`
  - `is_independence_wave_danzig_free_city_package = yes`
  - relevant proclaimed/recognized flag
- Failure triggers are local and valid for the live tag owner:
  - subject status
  - loss of state ownership/control
- No dead-country target or unsafe external target was found in the Assyria/Danzig mission behavior.

## Localisation and Tooltip Gaps

No missing Assyria/Danzig mission localisation keys were found for names, descriptions, failure tooltips, failure effect tooltips, or success effect tooltips.

Checked keys:

- `independence_wave_integrate_assyrian_recognition_congress`
- `independence_wave_integrate_assyrian_recognition_congress_desc`
- `independence_wave_integrate_assyrian_recognition_congress_failure_tt`
- `independence_wave_integrate_assyrian_recognition_congress_failure_effect_tt`
- `independence_wave_integrate_assyrian_recognition_congress_success_effect_tt`
- `independence_wave_integrate_danzig_free_city_charter`
- `independence_wave_integrate_danzig_free_city_charter_desc`
- `independence_wave_integrate_danzig_free_city_charter_failure_tt`
- `independence_wave_integrate_danzig_free_city_charter_failure_effect_tt`
- `independence_wave_integrate_danzig_free_city_charter_success_effect_tt`

## Cleanup and Exploit-Risk Notes

- Integrated and failed flags prevent repeat activation.
- Failure effects add pressure but do not grant equipment, manpower, free claims, cores, or war goals, so no farming loop was found.
- Success effects grant one local infrastructure improvement through `random_owned_controlled_state` with a state/core limit, so the reward stays bounded to the intended state.
- No cleanup hook gap was found inside the Assyria/Danzig mission blocks.

## Concrete Recommended Fixes

No Assyria/Danzig gameplay fixes are recommended from this narrow audit.

Optional follow-up for parent scope, not patched here:

- Consider bringing `independence_wave_integrate_corridor_timetables` in `common/decisions/006_independence_wave_decisions.txt` in line with the newer Buganda/Sokoto/Assyria/Danzig mission pattern by adding `selectable_mission = no`, wrapped failure tooltip, and hidden-effect presentation.

## Validation

Ran scoped validation:

- Brace balance on touched Clausewitz files:
  - `common/decisions/006_independence_wave_decisions.txt`: `brace_balance=0`
  - `common/scripted_triggers/006_independence_wave_triggers.txt`: `brace_balance=0`
  - `common/scripted_effects/006_independence_wave_effects.txt`: `brace_balance=0`
  - `common/script_constants/006_independence_wave_constants.txt`: `brace_balance=0`
- Unsupported operators: no `<=` or `>=` found in scoped files.
- Localisation `:0` scan: no `:0` keys found in `localisation/english/006_independence_wave_l_english.yml`.
- Localisation encoding: file reports UTF-8 with BOM; first bytes `efbbbf`.
- Timed flag / mission constant misuse: no `days = constant:/@` or `days_mission_timeout = constant:` patterns found.
- Unary variable negation scan: no `= -variable_token` or `value = -variable_token` patterns found in scoped Clausewitz files.
- Assyria/Danzig mission localisation key coverage: all checked keys present.

## Skipped Validation

- Did not run a full HOI4 launch or in-game scenario validation.
- Did not run repository-wide validation because the prompt requested a narrow Assyria/Danzig mission audit and the Event 006 files are already dirty/untracked parent work.

## Remaining Risks

- Railway mission presentation remains older than the Assyria/Danzig/Buganda/Sokoto pattern, but this is outside the requested patch scope.
- The surrounding Event 006 decision file contains unrelated indentation irregularities from existing dirty work. Brace balance is clean, and the Assyria/Danzig blocks themselves are formatted consistently.
