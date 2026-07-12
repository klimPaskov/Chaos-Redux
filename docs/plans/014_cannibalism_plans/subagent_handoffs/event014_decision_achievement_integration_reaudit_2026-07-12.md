# Event 014 Decision and Achievement Integration Re-audit

Audit date: 2026-07-13
Requested report path date: 2026-07-12
Auditor: `event014_decision_final_audit`
Result: no remaining High or Medium integration defect; one local tracker-only defect patched

## Scope

This re-audit covered the parent-created staged achievement tracker together with the maintained-objective tranche:

- `common/decisions/014_cannibalism_achievement_tracker_decisions.txt`
- `common/decisions/categories/014_cannibalism_achievement_tracker_categories.txt`
- `common/scripted_localisation/014_cannibalism_achievement_tracker_scripted_localisation.txt`
- `common/achievements/chaos_redux_achievements.txt`
- `interface/014_cannibalism_achievement_tracker.gfx`
- `interface/014_cannibalism_achievements.gfx`
- `localisation/english/014_cannibalism_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- the four staged-visibility flag set/clear sites
- all six new maintained missions, the two pre-existing maintained missions, seven action families, bounded objective registries, aftermath category retirement, and compact vigilance resolution

Focus-closure and world-end implementation were not edited. No DDS was generated. No specification or spreadsheet was changed.

## Patch made

### Low: redundant AI evaluation on presentation-only tracker entries

File:

- `common/decisions/014_cannibalism_achievement_tracker_decisions.txt`

Before:

- Every tracker entry was permanently unavailable and had no effects, but also carried `ai_will_do = { base = 0 }`.

After:

- All eighteen redundant `ai_will_do` blocks were removed.
- All eighteen entries remain permanently unavailable through the read-only custom-trigger tooltip.
- The tracker has no cost, completion effect, removal effect, timeout effect, cancellation effect, cooldown, or AI behavior.

Reason:

- Availability already prevents interaction. Removing the AI blocks makes the category literally presentation-only and removes unnecessary AI evaluation and a repeated magic zero.

## Achievement registry and tracker parity

### Real achievement count

The Event 014 section of `common/achievements/chaos_redux_achievements.txt` contains exactly eighteen real achievements:

- five baseline achievements without `hidden = yes`
- thirteen late-route achievements with `hidden = yes`

The staged tracker contains exactly eighteen corresponding entries:

- entries 01-05 are baseline-visible
- entries 06-18 use thirteen public-stage gates

### Completion truth source

`common/scripted_localisation/014_cannibalism_achievement_tracker_scripted_localisation.txt` contains exactly eighteen status selectors and eighteen unique completion-trigger calls.

Every selector calls the same exact scripted completion trigger used by the matching real achievement's `happened` block. The comparison returned no missing, extra, or mismatched completion trigger.

The tracker therefore does not maintain a second completion ledger. It only renders `Completed` or `In Progress` from the real achievement contract.

### Read-only behavior

After the patch:

- eighteen of eighteen tracker entries are unavailable
- zero tracker entries contain a gameplay effect
- zero tracker entries contain an AI block
- zero tracker entries contain a cost or cooldown
- all eighteen icon references resolve to the matching registered Event 014 achievement sprite

## Public-stage and spoiler audit

The five baseline achievements expose only pre-reveal containment information.

The thirteen late entries open as follows:

| Tracker entries | Visibility gate | Earliest public meaning |
| --- | --- | --- |
| 06 | `achievement_cannibalism_exploitation_visibility_open` | First exploitation selection |
| 07 | `achievement_cannibalism_island_host_visibility_open` | First successful Island Host formation |
| 08-11 | `cannibalism_reveal_complete` | Hannibal Lecter and the unified Host are public |
| 12 | `achievement_cannibalism_convergence_visibility_open` | Convergence warning becomes public; its text does not name Hannibal or the Wendigo route |
| 13 | `cannibalism_reveal_complete` | Revealed Hannibal can be named |
| 14 | `achievement_cannibalism_wendigo_merge_occurred` | Wendigo merge is public |
| 15 | `cannibalism_reveal_complete` | Ordinary terminal route is public |
| 16 | `achievement_cannibalism_wendigo_merge_occurred` | Wendigo terminal route is public |
| 17 | `cannibalism_global_defeat_aftermath_eligible` | Reconstruction aftermath is active |
| 18 | `achievement_cannibalism_evolution_ii_visibility_open` | Network-stage state prevention is public |

No baseline or pre-reveal tracker localisation exposes Hannibal Lecter, the Wendigo merge, transformation anchors, or either terminal route.

The four dedicated visibility flags have one initialization clear and one first-stage set:

- `achievement_cannibalism_exploitation_visibility_open`
  - cleared in `cannibalism_initialize_achievement_runtime`
  - set in `cannibalism_achievement_record_exploitation`
- `achievement_cannibalism_island_host_visibility_open`
  - cleared in achievement runtime initialization
  - set only by the successful Island Host warlord-formation receipt
- `achievement_cannibalism_evolution_ii_visibility_open`
  - cleared in achievement runtime initialization
  - set by `cannibalism_open_evolution_ii`
- `achievement_cannibalism_convergence_visibility_open`
  - cleared in achievement runtime initialization
  - set by `cannibalism_begin_convergence_window`

None is cleared by an ordinary phase transition or Event 014 cleanup, so opened tracker history remains visible.

## Tag-transfer continuity

The achievement transfer helpers remain defined once each:

- `cannibalism_achievement_capture_current_player_ledger`
- `cannibalism_achievement_apply_captured_player_ledger`

Three capture/apply pairs remain wired across the actual player tag-transfer paths:

- selected unification host into CBL
- absorbed human warlord into the active unified host
- primary human warlord donor into the Wendigo merge host

The captured first-host flag, exploitation history, suppression/decisive-aid history, suppression count, isolated-node recovery count, and reconstruction contribution are still applied before `change_tag_from`. The tracker reads the same real completion triggers after transfer; it introduces no separate country-scoped state that could be lost.

## Maintained missions and action families

Exactly eight maintained mission families are present once each:

Existing:

- `cannibalism_restore_supply_corridor_mission`
- `cannibalism_rotate_compromised_formations_mission`

Objective tranche:

- `cannibalism_investigation_mission`
- `cannibalism_hold_prison_mission`
- `cannibalism_reach_island_mission`
- `cannibalism_break_network_mission`
- `cannibalism_stop_unification_mission`
- `cannibalism_stop_transformation_mission`

Each of the six objective-tranche missions still has:

- a runtime duration
- target/state persistence with node or actor generation validation where relevant
- capped progress
- completion, timeout, and cancellation handling
- distinct full, partial, and failure effects

Exactly seven action-gap decisions are present once each and remain live:

- `cannibalism_replace_compromised_officer_chain`
- `cannibalism_infiltrate_ritual_cell`
- `cannibalism_break_ritual_economy`
- `cannibalism_reconnoiter_silent_island`
- `cannibalism_liberate_feeding_state`
- `cannibalism_prepare_network_submission`
- `cannibalism_prepare_network_resistance`

All seven retain a real cost gate, payment effect, cooldown, completion effect, and action-specific AI behavior. The tracker AI removal does not touch gameplay decision AI.

## Bounded registry and aftermath audit

### Objective observer registry

`global.cannibalism_objective_countries` is:

- cleared on Event 014 initialization
- populated only for active ordinary responder objectives not already in the actor registry
- processed only through the existing Event 014 pulse
- skipped when the country becomes an Event 014 actor
- pruned when that country has no active maintained objective
- resized to zero during final Event 014 gameplay cleanup

No recurring whole-world on-action or whole-country scan was added by the objective or tracker tranche.

### Reconstruction participant retirement

`global.cannibalism_reconstruction_participants` is populated from the bounded defeat-contributor and former-feeding-state owner sets. It deliberately survives the immediate gameplay cleanup because reconstruction is initialized immediately before that cleanup.

Every compact terminal outcome:

- clears the participant's active reconstruction flag
- removes that country from the participant registry
- refreshes its aftermath idea
- checks the remaining bounded participant registry
- clears `cannibalism_reconstruction_system_active` only when no active participant remains

The international response reconstruction branch and reconstruction category both require the local participant flag, so completed countries retire from both surfaces immediately.

### Progress-backed compact partial

Ratification records a start date, zero elapsed progress, and a runtime duration. Timeout and cancellation calculate elapsed days from `global.date`, clamp them, and compare them against separate partial and full thresholds.

- full completion requires maintained vigilance and the full threshold
- partial completion requires the partial threshold and sets `cannibalism_compact_vigilance_partial`
- failure is reserved for progress below the partial threshold

Partial completion does not set the compact failure flag and does not satisfy the real compact-vigilance achievement trigger.

## Localisation and sprite integration

- All 41 tracker category/entry/status localisation keys exist exactly once.
- `localisation/english/014_cannibalism_l_english.yml` and `localisation/english/chaosx_achievements_l_english.yml` retain UTF-8 BOM encoding.
- All eighteen tracker icon names resolve to the completed Event 014 achievement sprite registrations.
- All 54 registered Event 014 achievement DDS references exist: completed, grey, and not-eligible variants for eighteen achievements.

## Intentional asset dependencies: 15 DDS files

These are pending dependencies, not completed assets and not accepted fallbacks.

Tracker category assets:

- `gfx/interface/decisions/014_cannibalism/decision_category_cannibalism_achievement_tracker.dds`
- `gfx/interface/decisions/014_cannibalism/cannibalism_achievement_tracker_category_panel.dds`

Objective decision assets:

- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_replace_compromised_officer_chain.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_infiltrate_ritual_cell.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_ritual_economy.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_reconnoiter_silent_island.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_liberate_feeding_state.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_prepare_network_submission.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_prepare_network_resistance.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_investigation_mission.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_hold_prison_mission.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_reach_island_mission.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_break_network_mission.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_stop_unification_mission.dds`
- `gfx/interface/decisions/014_cannibalism/decision_cannibalism_stop_transformation_mission.dds`

No DDS was generated, reused, or substituted during this audit.

## Remaining issues and completion status

- No High or Medium integration issue remains in the audited tracker/objective surface.
- The fifteen DDS dependencies above remain real blockers to asset-complete status.
- Focus-closure and world-end completion are outside this report and were not edited.
- No fallback or gameplay simplification was introduced.
- No commit was created.

## Skills used

- `hoi4-decisions-missions`
- `chaos-redux-events`
- `chaos-redux-event-assets`

No skill was created or updated by this audit.
