# Event 006 Release Resolver Audit

Subagent: `chaosx_scripted_system_architect`
Mode: bounded read-only audit, except this handoff
UTC timestamp: 2026-06-05 07:33:53

## Scope

Audited the Event 006 Independence Wave instant-release resolver and tier evolution event-log wiring for blockers that could cause:

- `chaosx.nr6.1` to release zero countries when valid ordinary releasables exist
- failed releases to be counted as successes
- stale protected or reduced state flags to block later candidates
- evolution logs to be recorded once per wave instead of only milestone tiers

Event 006 was treated as independent from Event 005. I did not recommend Event 5 state dependencies.

## References Checked

- Offline wiki core pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding.
- Vanilla documentation:
  - `/home/klim/projects/Hearts of Iron IV/documentation/effects_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/triggers_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/documentation/script_concept_documentation.md`
  - `/home/klim/projects/Hearts of Iron IV/common/script_constants/documentation.md`
- Vanilla release precedents:
  - `/home/klim/projects/Hearts of Iron IV/events/SEA_Nat_China.txt:2335` uses `ROOT = { release = event_target:CHI_country_to_be_liberated }`.
  - `/home/klim/projects/Hearts of Iron IV/events/TOA_Brazil.txt:2378` uses `ROOT = { release = event_target:BRA_country_to_be_liberated }`.

The vanilla docs confirm `release` is a country-scoped effect and supports event targets as release targets. The current resolver mirrors the precedent by executing `release = event_target:independence_wave_current_candidate` from the selected host country scope.

## Findings

### Remaining blocker: Event 5-origin state flags still exclude candidates and hosts

`common/scripted_triggers/006_independence_wave_triggers.txt:14-22` defines `has_independence_wave_soviet_collapse_runtime_state` from `soviet_collapse_*` country flags. That trigger is then used to reject candidates in `can_independence_wave_use_candidate_tag` at `common/scripted_triggers/006_independence_wave_triggers.txt:55-57` and to reject potential hosts in `can_independence_wave_host_release_current_candidate_safely` at `common/scripted_triggers/006_independence_wave_triggers.txt:864-869`.

This is not a suggested dependency; it is an existing dependency-like exclusion. If ordinary releasable candidates or their hosts carry those Event 5-origin flags, Event 006 can skip them before the release resolver runs. In a state where the ordinary releasable set is mostly or entirely flagged this way, `chaosx.nr6.1` can release zero countries despite otherwise valid releasable cores.

Suggested narrow patch for parent: remove the `has_independence_wave_soviet_collapse_runtime_state` trigger from Event 006 release candidate and host gates, or replace it with an Event 006-owned exclusion flag only when a tag was already created by Event 006. This keeps Event 006 independent from Event 5.

### Parent patch addresses failed releases being counted as successes

`events/006_independence_wave.txt:95-126` now calls `release = event_target:independence_wave_current_candidate`, then only runs truce, host aftermath, released-country setup, `independence_wave_register_successful_release`, and congress opening inside an `exists = yes` check at `events/006_independence_wave.txt:96-115`.

The failed-release branch at `events/006_independence_wave.txt:117-126` only restores reduced release cores. This addresses the concrete risk that a no-op release could increment `global.independence_wave_actual_release_count` or add the candidate to release arrays.

### Parent patch addresses current protected-state stale flag leakage

`events/006_independence_wave.txt:88-94` reserves one host survival state only after `independence_wave_protected_host_state` exists. `common/scripted_effects/006_independence_wave_effects.txt:1842-1857` now clears `independence_wave_host_survival_reserved` on that protected state before clearing the event target.

This addresses the current-wave stale protected flag risk that could block a later candidate via `common/scripted_triggers/006_independence_wave_triggers.txt:888-893`.

### Reduced-core cleanup is currently paired with success and failure branches

`common/scripted_effects/006_independence_wave_effects.txt:191-269` masks non-anchor release cores before release. `common/scripted_effects/006_independence_wave_effects.txt:271-301` restores masked cores and clears the reduced-release anchor. Both the successful path and failed no-op path call this restore helper from `events/006_independence_wave.txt:107-110` and `events/006_independence_wave.txt:117-125`.

I did not find a remaining intra-wave reduced-core flag blocker in the audited resolver path.

### Tier evolution log spam appears fixed in the current working tree

`events/006_independence_wave.txt:149-154` still calls `independence_wave_record_tier_evolution_log_entry` after any successful wave. However, the helper now gates each milestone with one-shot global flags:

- Gathering storm: `common/scripted_effects/006_independence_wave_effects.txt:5932-5940`
- Rising cascade: `common/scripted_effects/006_independence_wave_effects.txt:5942-5953`
- Old names: `common/scripted_effects/006_independence_wave_effects.txt:5955-5963`
- Impossible statehood: `common/scripted_effects/006_independence_wave_effects.txt:5965-5973`

`common/scripted_effects/006_independence_wave_effects.txt:5919-5925` prepares tier `0-5`, but `independence_wave_record_tier_evolution_log_entry` records only tiers 1-5 and has no tier-0/calm-world record path. This matches the constraint that calm world is normally not an evolution tier and the minimum milestone starts at gathering storm.

## Remaining Blockers

1. Event 5-origin `soviet_collapse_*` flags still gate Event 006 candidate and host eligibility. This violates Event 006 independence and can cause zero releases in Event 5-contaminated state.

No remaining blocker found for failed release success counting, current-wave protected/reduced state cleanup, or per-wave tier evolution log duplication in the current audited files.

## Validation Commands Run

- `sed -n` on required offline wiki pages under `paradox_wiki/`
- `rg -n "release|save_event_target|exists|has_event_target"` on vanilla documentation
- `rg -n "release =|release_puppet|release_autonomy|release_on_controlled"` on vanilla `events/` and `common/`
- `nl -ba events/006_independence_wave.txt`
- `nl -ba common/scripted_effects/006_independence_wave_effects.txt`
- `nl -ba common/scripted_triggers/006_independence_wave_triggers.txt`
- `nl -ba common/script_constants/006_independence_wave_constants.txt`
- `nl -ba common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `nl -ba common/scripted_localisation/006_independence_wave_scripted_localisation.txt`
- `nl -ba localisation/english/006_independence_wave_l_english.yml`
- `rg -n "record_events_log_evolution_entry|independence_wave_record_tier_evolution_log_entry|independence_wave_host_survival_reserved|independence_wave_reduced_release_core_masked"`
- `git diff -- events/006_independence_wave.txt common/scripted_effects/006_independence_wave_effects.txt`
- `git status --short`

No gameplay files were edited and no in-game validation was run in this read-only audit.
