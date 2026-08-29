# Event 006 evolution, League, and achievement audit handoff — 2026-08-29

## Disposition

The Event 006 evolution, League, and achievement source audit found no safe source-backed gameplay defect requiring a patch.

The only implementation change is a documentation correction in `docs/achievements/006_independence_wave/achievements.md`.

## Scope and identifiers audited

The five evolution registrations and stage flags are `has_independence_wave_replicable_independence_evolution`, `has_independence_wave_dormant_nations_evolution`, `has_independence_wave_armed_birth_evolution`, `has_independence_wave_sovereign_congress_evolution`, and `has_independence_wave_open_sovereignty_evolution`.

The corresponding delivery and lifecycle helpers are `independence_wave_apply_replicable_independence_to_country`, `independence_wave_apply_dormant_nations_to_country`, `independence_wave_apply_armed_birth_to_country`, `independence_wave_apply_sovereign_congress_to_country`, `independence_wave_apply_open_sovereignty_to_country`, `independence_wave_initialize_evolution_registry`, `independence_wave_activate_next_evolution`, and `independence_wave_cleanup_evolution_registry` in the canonical evolution effects file.

The formal and informal League lifecycle audited includes `independence_wave_open_regional_conference`, `independence_wave_open_charter_vote`, `independence_wave_proclaim_consultative_league`, `independence_wave_proclaim_formal_league`, `independence_wave_mark_league_durable`, `independence_wave_enter_league_crisis`, `independence_wave_reform_league`, `independence_wave_split_league`, `independence_wave_normalize_reformed_league`, `independence_wave_reunify_rival_leagues`, `independence_wave_dissolve_league_to_network`, `independence_wave_restart_informal_network`, and the generation-safe rival-bloc member and cleanup helpers in the Event 006 League effects files.

The sixteen achievement identifiers audited are `chaosx_006_one_state_to_statehood`, `chaosx_006_no_master`, `chaosx_006_peace_with_host`, `chaosx_006_break_reconquest`, `chaosx_006_found_league`, `chaosx_006_cross_regional_league`, `chaosx_006_rescue_member`, `chaosx_006_regional_formable`, `chaosx_006_volga_bulgaria`, `chaosx_006_assyria_survives`, `chaosx_006_small_to_major`, `chaosx_006_radical_bloc`, `chaosx_006_every_flag_survival`, `chaosx_006_balanced_patrons`, `chaosx_006_league_arbitrator`, and `chaosx_006_host_remnant`.

## Files changed

- `docs/achievements/006_independence_wave/achievements.md` now points to the canonical shared script-constants registry and merged Event 006 localisation file.
- The same document now records that all seven factual patron-client expulsion grounds are wired and that the generation-safe rival-bloc transaction is implemented in the Event 006 rival-bloc surfaces.
- This dated handoff records the audit evidence, limitations, and exact MCP blocker.

## Behavior impact

There is no runtime behavior change.

The corrected documentation matches the current source layout after the earlier evolution and achievement localisation registry merges.

The corrected status avoids describing the implemented rival-bloc contract as future work while retaining an honest follow-up note for typed probability evidence and live save/load validation.

## Source findings

The five evolution stages have one-stage-per-due-activation sequencing, enabled-stage gating, actor selection, deferred pre-fire logging, idempotent country delivery flags, and cleanup hooks in `common/scripted_effects/006_independence_wave_evolution_effects.txt` and `common/scripted_triggers/006_independence_wave_triggers.txt`.

The League state machine maintains informal network, consultative/formal/durable phases, crisis/reform/split/reunification transitions, cohesion, common cause, contribution, confidence, rescue, leadership, founder provenance, and generation-safe member arrays in `common/scripted_effects/006_independence_wave_effects.txt` and `common/scripted_effects/006_independence_wave_rival_bloc_effects.txt`.

The achievement effects and on-actions use bounded engine callbacks for wars, peace, state control, subject changes, annexation, rescue, arbitration, coercion, expulsion, scenario survival, host-remnant state, and generation cleanup without a daily, weekly, or monthly world scan.

The achievement definitions, final proof triggers, names/descriptions/tooltips, and normal/grey/not-eligible icon triplets cover all sixteen identifiers.

## Validation evidence

`python .tools/audit_event6_allocator.py` passed with 149 publishers, 40 runtime adapters, and 29 compatible reservation groups.

`python .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 intensity/type cells and eight edge cases.

`python .tools/audit_event6_flags.py --strict` reported 102 registered Event 006 tags, 102 complete flag families, and zero incomplete families.

`python .tools/audit_event6_country_api.py` passed with 242 broad tags, 191 resolved carriers, and zero missing or duplicate country APIs.

`python .tools/audit_event6_form16.py` passed the admitted ARM/GEO/AZR FORM-16 contract, including mutation and rollback cleanup checks.

A read-only PowerShell mechanical check found all sixteen achievement IDs in `common/achievements/chaos_redux_achievements.txt` and `localisation/english/006_independence_wave_l_english.yml`, all 48 normal/grey/not-eligible DDS files, and no legacy constants or localisation files at the removed paths.

## Evidence blockers

The active runtime exposes no `mcp__hoi4`, `hoi4_agent_tools`, `hoi4.probability_inspect`, or `chaosx_ai_probability_auditor` route, so the required fresh read-only event inspection/render and probability evidence could not be run in this handoff.

The current source-of-truth map records the latest Event 006 artifact attempt as `ARTIFACT_MANIFEST_INTEGRITY_FAILED` with zero usable artifacts, and earlier dated handoffs record only partial event inspection evidence.

No weighted logic was changed, so this handoff makes no new AI, MTTH, or probability claim.

Live Hearts of Iron IV execution and save/load validation remain outside this worker's permitted validation surface.

## Simplifications, omissions, and follow-up

No gameplay simplification, fallback asset, invented mechanic, decision-file edit, country-package edit, or weighted-logic adjustment was made.

The two package-specific achievements remain intentionally fail-closed behind their existing sourced portrait and origin-admission gates.

Parent follow-up is to rerun the mandatory Event 006 MCP inspections and probability comparison when those routes and valid artifacts are available, then perform the specified live save/load scenarios.
