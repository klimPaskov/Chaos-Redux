# Event 19 and Event 67 Generalissimo Bridge Handoff

## Scope and result

This tranche adds the bounded Event 19 claimant integration with Event 67,
Generalissimo. It changes only existing Event 19 claimant gameplay, AI,
localisation, and documentation surfaces. It does not edit Event 67, any Event
19 registry, scenario, management, ledger, or standardization file, or any
parent-event progression system.

## Verified external identity

`events/067_generalissimo.txt` provides the complete live identity contract:

- `global.generalissimo_country` receives the selected country's `THIS.id`.
- `global.generalissimo` receives the selected army leader's character ID.
- Event 67 scopes `var:global.generalissimo` to grant the Generalissimo roles.

Event 19 now accepts that record only when both globals exist, the recorded
country ID equals the current country ID, and an active army leader owned by the
current country has the exact recorded character ID. The dynamic character-ID
test mirrors Event 19's existing claimant lookup through `meta_trigger` and
`has_id`. A stale global after death, retirement, or departure therefore does
not create a live Generalissimo relationship.

No live top-level runtime identifiers were found for Event 127 Warlords or Event
131 Widespread Mutiny. There are no `chaosx.nr127` or `chaosx.nr131` event
scripts, no registrations, and no `chaosx.event_name.127` or
`chaosx.event_name.131` localisation entries. The settings and debug scripted
localisation contain orphan selectors for those two event-name keys. Other
numeric 127/131 and `warlords` occurrences belong to unrelated subevents,
provider tokens, map identifiers, or Event 14 content. No identifiers were
invented and no runtime bridge was added for either absent event.

## Implemented behavior

- `infantry_spawn_country_has_valid_event67_generalissimo` validates the Event
  67 country and live character together.
- `infantry_spawn_selected_claimant_is_event67_generalissimo` detects an exact
  match between the selected claimant UID and the Event 67 character ID.
- `infantry_spawn_selected_claimant_rivals_event67_generalissimo` detects a
  different selected claimant beneath the valid Generalissimo.
- An exact Generalissimo claimant selects emergency command powers during war
  when affordable, otherwise a political seat when affordable, otherwise a
  formal appointment.
- A rival claimant selects a subordinate commission under strong Muster
  Control. Weak control or high claimant influence selects a parallel command
  when affordable. Resource-aware alternatives prevent an unaffordable bridge
  demand from being issued when the other command relationship can be paid.
- Accepting subordinate command spends Army Experience and Command Power,
  reduces claimant influence, raises Muster Control, and recognizes the
  claimant.
- Accepting parallel command spends Political Power and Command Power,
  increases claimant influence, lowers Muster Control, and recognizes the
  claimant.
- Refusing either new demand has its own influence and Muster Control result.
  Both results end in the existing countermanded status and shared demand
  cleanup.
- Scripted AI favors preserving an exact Generalissimo claimant, favors a
  subordinate settlement, and is substantially more willing to refuse a
  parallel command. Decision AI weights mirror those priorities.
- `infantry_spawn_resolve_selected_claimant_natural_takeover` sends a natural
  one-state takeover by a rival of a living Generalissimo to the existing
  failed-coup effect. Natural takeovers by the Generalissimo or without a valid
  Event 67 relationship keep the existing takeover effect.
- Direct scenario code still calls
  `infantry_spawn_execute_selected_claimant_takeover` directly, so scenario
  takeovers are unchanged.

Demand codes `7` and `8`, all costs, thresholds, outcome deltas, and AI weights
are centralized under `infantry_spawn_generalissimo_*` script-constant
categories. No new idea, country flag, timed state, asset, or UI sprite was
introduced, so there is no added lifecycle cleanup or asset handoff.

## Player-facing surfaces

The claimant warning event and Muster Board now state the current demand and the
verified Generalissimo relationship. The accept and refusal tooltips expose the
two new resource prices and their influence and Muster Control consequences.
Scripted localisation maps both new demand codes and all three relationship
contexts.

New localisation keys:

- `infantry_spawn_claimant_demand_subordinate_command`
- `infantry_spawn_claimant_demand_subordinate_command_desc`
- `infantry_spawn_claimant_demand_parallel_command`
- `infantry_spawn_claimant_demand_parallel_command_desc`
- `infantry_spawn_claimant_generalissimo_context_exact`
- `infantry_spawn_claimant_generalissimo_context_rival`
- `infantry_spawn_claimant_generalissimo_context_none`

## Files changed

- `common/script_constants/019_infantry_spawn_claimant_constants.txt`
- `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_effects.txt`
- `common/decisions/019_infantry_spawn_claimant_decisions.txt`
- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt`
- `localisation/english/019_infrantry_spawn_l_english.yml`
- `docs/events/019_infantry_spawn/overview.md`
- this handoff

## Review and validation evidence

- Verified Event 67's country and character assignments directly in
  `events/067_generalissimo.txt`.
- Verified all new demand codes are covered by selection, affordability,
  acceptance dispatch, refusal results, scripted localisation, and player
  tooltips.
- Verified the natural crisis resolver uses the new wrapper while the two
  direct scenario takeover calls remain direct.
- Verified the bridge creates no parent-event count, stage, evolution,
  super-event, or world-end writes.
- Verified the repository still contains exactly one Event 19 registry code
  file: `019_infantry_spawn_unit_registry_effects.txt`.
- Reviewed the tuning as three distinct AI cases. The exact Generalissimo can
  reach a 75 percent scripted acceptance weight during war under strong control
  and is capped by the existing 90 percent ceiling under acute pressure. The
  subordinate demand adds 25 acceptance points, while the parallel demand
  removes 25 points. This preserves refusal risk without making either route
  automatic.

## Simplifications, omissions, and blockers

None. The requested Event 67 bridge is fully implemented within the granted
surface. Event 127 and Event 131 were not simplified or substituted; their
verified lack of live runtime identifiers is documented explicitly. No commit
was created.
