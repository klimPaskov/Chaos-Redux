# IW-005 Flanders Overlay Implementation Handoff

Date: 2026-07-16

Owner: `/root/event6_flanders_overlay`

Mode: patch-capable implementation

Commit: none, as requested by the parent

## Outcome

Implemented IW-005 as a complete additive package on living Belgium with the vanilla `BEL_flanders` cosmetic identity.

The implementation does not create or register a standalone Flemish country. It does not use `AEX`. It does not assign an Event 006 origin, change Belgium's focus tree, change Belgian history, alter state ownership or cores, change autonomy, replace characters, change leaders, or modify FORM-03 runtime files.

The package contains:

- exact one-time activation on `original_tag = BEL` plus `has_cosmetic_tag = BEL_flanders`
- exact route-state suspension and return through `on_daily_BEL`
- two visible values with centralized starts, bounds, gains, losses, and gates
- four costed foundation actions
- one explicitly activated and resumable corridor mission
- a four-stage idea lifecycle
- two mutually exclusive final institutions with distinct costs and tradeoffs
- nonzero action AI with a guarded mission-start strategy
- English localisation with constant-backed values
- a standalone system document

## Changed files

All implementation files are new and isolated.

1. `common/script_constants/006_independence_wave_iw005_flanders_constants.txt`
2. `common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt`
3. `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt`
4. `common/on_actions/006_independence_wave_iw005_flanders_on_actions.txt`
5. `common/decisions/categories/006_independence_wave_iw005_flanders_categories.txt`
6. `common/decisions/006_independence_wave_iw005_flanders_decisions.txt`
7. `common/ideas/006_independence_wave_iw005_flanders_ideas.txt`
8. `common/scripted_localisation/006_independence_wave_iw005_flanders_scripted_localisation.txt`
9. `localisation/english/006_independence_wave_iw005_flanders_l_english.yml`
10. `docs/events/006_independence_wave/systems/iw005_flanders_overlay.md`
11. `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw005_flanders_overlay_implementation_2026_07_16.md`

No shared FORM-03, formable-registry, focus-tree, country-tag, country-history, character, or asset file was edited.

## Main identifiers

### Hook and lifecycle

- `on_daily_BEL`
- `is_independence_wave_iw005_flanders_route_active`
- `is_independence_wave_iw005_flanders_overlay_active`
- `independence_wave_iw005_refresh_flanders_overlay`
- `independence_wave_iw005_initialize_flanders_overlay`
- `independence_wave_iw005_suspend_flanders_overlay`
- `independence_wave_iw005_pause_flanders_guard_mission`
- `independence_wave_iw005_resume_flanders_overlay`
- `independence_wave_iw005_resume_flanders_guard_mission`
- `independence_wave_iw005_refresh_flanders_idea_lifecycle`

### Lifecycle flags

- `independence_wave_iw005_flanders_overlay_ever_activated`
- `independence_wave_iw005_flanders_package_initialized`
- `independence_wave_iw005_flanders_overlay_active`
- `independence_wave_iw005_flanders_overlay_suspended`
- `independence_wave_iw005_factory_rail_guard_running`
- `independence_wave_iw005_factory_rail_guard_interrupted`
- `independence_wave_iw005_factory_rail_guard_completed`
- `independence_wave_iw005_factory_rail_guard_failed`

### Visible variables

- `independence_wave_iw005_civic_industrial_coordination`
- `independence_wave_iw005_scheldt_security`
- `independence_wave_iw005_guard_hold_days`

### Progress flags

- `independence_wave_iw005_municipal_factory_ledgers_compiled`
- `independence_wave_iw005_scheldt_rail_depots_secured`
- `independence_wave_iw005_defecting_regulars_vetted`
- `independence_wave_iw005_municipal_industrial_board`
- `independence_wave_iw005_scheldt_territorial_compact`

### Category, decisions, and mission

- `independence_wave_iw005_flanders_category`
- `independence_wave_iw005_compile_municipal_factory_ledgers`
- `independence_wave_iw005_secure_scheldt_rail_depots`
- `independence_wave_iw005_vet_defecting_regulars`
- `independence_wave_iw005_raise_factory_railway_guard`
- `independence_wave_iw005_hold_scheldt_guard_line`
- `independence_wave_iw005_charter_municipal_industrial_board`
- `independence_wave_iw005_entrust_scheldt_territorial_compact`

### Ideas

- `independence_wave_iw005_contested_civic_industrial_command`
- `independence_wave_iw005_coordinated_civic_industrial_command`
- `independence_wave_iw005_municipal_industrial_board`
- `independence_wave_iw005_scheldt_territorial_compact`

### Constant namespaces

- `independence_wave_iw005_flanders_value`
- `independence_wave_iw005_flanders_outcome`
- `independence_wave_iw005_flanders_duration`
- `independence_wave_iw005_flanders_cost`
- `independence_wave_iw005_flanders_modifier`
- `independence_wave_iw005_flanders_ai`

## Lifecycle proof

`on_daily_BEL` calls only `independence_wave_iw005_refresh_flanders_overlay`.

The route gate requires both:

```txt
original_tag = BEL
has_cosmetic_tag = BEL_flanders
```

First activation sets the permanent one-time flag, initializes the values once, and installs the idea matching current progress. Route loss removes only the four IW-005 ideas, hides the category through the route gate, and records a running guard mission as interrupted. It preserves the active mission, running flag, values, progress flags, final-institution choice, and guard hold days.

On the first suspended `on_daily_BEL` tick and every later one, the lifecycle extends that same active mission's timeout by the centralized one-day pause interval. The guard counter cannot advance or reset because the overlay-active proof is false. Route return restores the package flag and correct idea, then clears the interruption marker only when the original mission and running flag are both still present. An unexpectedly missing mission fails safely and must be recommitted; it is never reconstructed with a fresh deadline.

Official effects documentation defines `add_days_mission_timeout` in country scope, and vanilla China and Bulgaria pass country variables to its `days` field. IW-005 therefore loads the centralized pause interval into a temporary variable before extending the mission. Route loss was removed from `cancel_trigger`; only clearing the persistent running flag cancels the mission.

The official documentation does not specify whether mission timeout decrement or `on_daily_BEL` executes first. The source guarantees one extension call on the first observed suspended tick and every later tick, but static documentation cannot prove the last-day ordering edge without an executable trace. No restart or deadline-reset fallback is used.

## Playable and balance proof

The mandatory non-officer sequence reaches:

- start: 30 civic, 25 security
- ledger: +25 civic, +5 security
- depots: +5 civic, +25 security
- successful guard mission: +15 civic, +25 security
- result: 75 civic, 80 security

Both final choices are therefore reachable without the optional officer action:

- civic gate: 65 civic, 55 security
- security gate: 55 civic, 65 security

Taking the optional officer action changes the pre-capstone result to 70 civic and 100 security. It strengthens the military route while imposing the accepted civilian-authority tradeoff.

The mission requires 60 continuous days of Belgian ownership, Belgian control, and at least one Belgian division in each of states 6 and 977. Its timeout is 150 days. A timeout costs 5 percent national stability and requires a new material commitment, but it cannot permanently reduce either value below the final-institution gates.

No decision grants units, leaders, characters, political power, free equipment, free factories, free territory, or free cores.

## FORM-03 and external-system boundaries

FORM-03 already consumes a living `BEL` with `BEL_flanders` through its own sovereignty, invitation, connection, ownership, and control gates. The overlay does not duplicate or relax those gates.

The overlay does not write:

- Event 006 active-country arrays
- Event 006 origin or liberation-origin flags
- host, patron, or league values
- FORM-03 carrier or member flags
- LCX cosmetic state
- Soviet Collapse values, flags, events, or helpers

This preserves the accepted sovereign-delegation relationship without pretending that the Flemish delegation speaks for every Belgian institution.

## References consulted

Required offline wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and national focus modding.

Relevant vanilla documentation was consulted for effects, triggers, modifiers, script constants, and script concepts. Vanilla precedents included:

- `common/on_actions/00_on_actions.txt` for tag-specific daily hooks
- `common/decisions/GER.txt` for the existing `BEL_flanders` cosmetic application on Belgium
- `common/national_focus/belgium.txt` to confirm that Belgium retains a meaningful focus tree
- vanilla Belgian decisions for decision and mission structure

The installed workspace did not expose a callable HOI4 MCP domain tool in this subagent session, so validation was performed against source, official documentation, vanilla precedents, and repository patterns.

## Validation performed

- Confirmed all 40 new scripted trigger and effect definitions are unique in `common/`.
- Confirmed all seven decision and mission identifiers and all four idea identifiers are unique.
- Resolved all 91 unique IW-005 script-constant keys to definitions in the new constant file.
- Resolved all 38 required decision, category, tooltip, and idea localisation keys.
- Resolved every scripted-localisation target key.
- Resolved all three reused decision sprites and all three reused idea sprites through `interface/006_independence_wave.gfx`.
- Confirmed the localisation file is UTF-8 with BOM.
- Confirmed the mandatory action path reaches 75 civic and 80 security, which opens both institutional settlements.
- Rechecked mission presentation against the offline Decision Modding page and vanilla `CHI_holding_state_mission`. IW-005 leaves `is_good` at its default false value because its `available` block is the success gate and its timeout is failure. The vanilla Chinese mission uses `is_good = yes` for the opposite structure, where losing the state satisfies `available`, runs a punitive complete effect, and surviving to timeout grants the reward.
- Confirmed that the non-selectable IW-005 mission runs its success `complete_effect` when `independence_wave_iw005_guard_hold_days` reaches at least 60, while the 150-day `timeout_effect` remains the failure path.
- Confirmed from official effects documentation and vanilla variable-backed precedents that `add_days_mission_timeout` accepts a country or temporary variable. The suspended lifecycle calls it on the first and every later inactive-route daily tick without removing or reactivating the mission.
- Confirmed all six custom-cost families provide base, blocked, and tooltip localisation, and that exact displayed command power, manpower, Army Experience, train, infantry-equipment, and support-equipment totals satisfy their equality-safe affordability checks.
- Confirmed no new gameplay file contains `AEX`, a tag registration, a country release, a cosmetic-tag setter, a focus-tree loader, an origin assignment, a state transfer, a core change, an autonomy change, a capital change, character creation, or Soviet Collapse references.
- Confirmed the new on-action file contains only `on_daily_BEL` and no world-iterating daily, weekly, or monthly hook.

## Remaining risks

1. No HOI4 executable session was launched for this handoff. Mission activation, variable-backed timeout extension, suspension, and continuation were checked against official syntax, vanilla patterns, and repository precedents. Official documentation does not establish the relative ordering of mission-timeout decrement and `on_daily_BEL`, so a route loss observed with one day remaining requires an executable trace to prove which operation occurs first.
2. Historical working documents elsewhere in the Event 006 plans still contain superseded `AEX` language. They were intentionally left untouched because the accepted research-resolution and source-of-truth documents already supersede them, and the parent requested isolation from shared Event 006 surfaces. No runtime file introduced here uses that tag.
3. If another system deliberately removes `BEL_flanders`, the package suspends by design. It does not attempt to restore or police the vanilla route identity.

## Simplifications, omissions, and blockers

No design simplification or fallback was used.

- No new country, tag, history, focus tree, flag, portrait, leader, or unit was substituted for the accepted overlay.
- No host, patron, or league mechanic was invented for a non-origin country.
- No FORM-03 file was changed because the exact `BEL_flanders` consumer already exists.
- No new art was produced because vanilla `BEL_flanders` identity assets and existing Event 006 decision and idea sprites satisfy the package without placeholders.
- There are no implementation blockers in the delivered patch.

## Skills used

- `chaos-redux-events`
- `chaos-redux-decisions-missions`
- `chaos-redux-focus-trees`
- `chaos-redux-subagents`

No skill was created or updated. `chaos-redux-event-assets` was not used because no new or modified asset was needed.
