# Event 32 specification, part 8: Implementation contract

This part owns the runtime boundaries Event 32 must keep.
The current file list, API reference and event ID map are maintained with the source, not copied here:

- runtime files: `docs/events/032_missiles/overview.md`, section Runtime files
- country, site, operation and warning APIs: `docs/events/032_missiles.md` and `common/scripted_effects/032_missiles_effects.md`, `032_missiles_operations_effects.md`, `032_missiles_scenario_effects.md`
- tuning: `common/script_constants/032_missiles_constants.txt` plus the recovery, scenario and survey constant files

## Ownership

Event 32 keeps its private runtime in `032_missiles_*` files and touches shared files only for established framework integration:

- random-event registration, the repeatable-event array and the reworked-event default-enable allowlist
- event name and debug selectors
- Event Logs history, Event Details and the five evolution rows
- the triggerable scenario registry
- shared CBRN, Deaths, Air Cleanliness and Condemnation entry points
- the authoritative catalog workbook

A helper becomes shared only after demonstrated cross-system reuse, and then lives in the owning shared system with its documentation.
Shared chemical, biological or nuclear logic never moves into Event 32 files.

## Namespace and event IDs

Namespace `chaosx.nr32` and entry event `chaosx.nr32.1` are fixed.
Implemented IDs: `.1` entry, `.2` country report, `.3` first news, `.4` scenario setup failure report, `.5` to `.9` hidden receivers (`.5` recipient, `.6` scenario setup, `.7` controller refresh, `.8` evolution access refresh, `.9` disaster receiver), `.30` to `.32` payload orders, `.40` posture, `.60` and `.69` incident reports, `.80` to `.90` warning and retaliation, `.190` to `.193` evolution observation and legacy cleanup, `.201` to `.205` native evolution clocks.
New IDs must be collision-checked against `events/032_missile_crisis.txt` and `events/032_missiles_evolution_events.txt` and added to the event doc.

## Core API contract

These named entry points are the stable contract other systems and scenarios call:

- recipient validation: `missiles_is_valid_recipient`
- program setup: `missiles_initialize_or_advance_program`, `missiles_normalize_technology_stage`, `missiles_apply_next_technology_step`, `missiles_apply_mature_program_package`
- operations: `missiles_preflight_operation`, `missiles_commit_operation`, `missiles_resolve_operation`, `missiles_abort_operation`, `missiles_cleanup_operation`
- incidents: `missiles_allocate_incident_id`
- sites and succession: `missiles_handle_site_control_changed`, `missiles_scuttle_site`, `missiles_split_program_after_civil_war`, `missiles_finalize_civil_war_split_child`, `missiles_finalize_planned_inheritance`, `missiles_cleanup_removed_country`
- natural disasters: `missiles_natural_disaster_damage_site` (queue only) and receiver `chaosx.nr32.9`

Every transaction returns its exact applied amount, fails closed on unproven scope, and is idempotent per receipt.

## Constants, flags and variables

All tuning lives in script constants; file-scoped `@` constants are used only where a field rejects `constant:` tokens.
Flags hold true or false state; numeric variables hold counts, ids and scores.
Temporary variables are never scoped through `ROOT.` or `PREV.`.
Persistent concurrent operations, sites and incidents use country and state ids, arrays and variables; a global event target is used only for one unique pointer with a named cleanup point.

## Event dispatch

The global entry uses one country loop at firing time because Event 32 explicitly affects every valid country.
It must not add `on_daily`, `on_weekly`, `on_monthly` or another recurring all-country on-action without separate user approval.
Event-scoped `on_state_control_changed`, `on_war_relation_added` and `on_peace` hooks are bounded to programs and registered sites.

## Prepared operation state machine

States: none, selecting, resources reserved, preparing, ready, committed, resolving, completed, aborted, invalidated.
Every transition has one entry effect, one exit effect, a resource rule, a site-allocation rule, a target validity rule, a visible decision set and a cleanup rule.
Impossible transitions are rejected.

## Incident state machine

States: created, evidence pending, warning active, response preparing, response committed, consequences applied, closed.
Rogue incidents keep their own site pointer (`missiles_rogue_site_state`) and close their own record only while they are the current incident.

## Evolution runtime

Each track has an unlock flag, the shared enable gate, an eligibility trigger, a native MTTH clock, a recorded flag, the canonical log context, behaviour helpers and disable behaviour.
Disabled tracks never arm, record or adopt.
Disabling an active track suspends decisions, AI behaviour, preparation, commitment, rogue activity and retaliation responses while keeping adoption history, reserve and physical payload custody.

## Operation adapter

Decision: the scripted strike adapter is the full supported route.
Basis: parent review of `docs/plans/032_missiles_plans/subagent_handoffs/032_native_raid_parity_audit_2026-10-03.md` under the user's full Event 32 implementation authorization.
The documented RaidInstance API exposes actor, victim, target state and province, but its starting-point gate identifies only the source controller country, so it cannot authenticate the frozen launch state or multi-site allocation.
No native raid definition or raid icon is added.
A future native adapter needs an authenticated launch-state and instance-receipt contract and must keep custody and consequence parity.

## Shared CBRN adapters

Event 32 calls the existing chemical, biological, nuclear, thermonuclear, Condemnation, Air Cleanliness and Deaths entry points.
A missing route is added to the owning shared system with purpose, scope, inputs, outputs, defaults, side effects and an example.
The chemical measured reservation (`docs/systems/cbrn_warfare/chemical_payload_reservations.md`) is the precedent.

## AI implementation

AI decisions use the same ability and payment triggers as player decisions.
The human selected-target state never blocks AI from seeing all valid targets.
Weighted surfaces follow part 6.

## Localisation

Event 32 localisation lives in `localisation/english/032_missile_crisis_l_english.yml`, `032_missiles_decisions_l_english.yml`, `032_missiles_achievements_l_english.yml` and `032_missiles_requirement_flags_l_english.yml`, with scripted localisation in `common/scripted_localisation/032_missiles_*.txt`.
Visible text follows part 7 and the `chaos-redux-events` writing rules: dynamic targets, states, values and posture; precise blocked reasons; concise value tooltips; Event Details wording aligned with the workbook.

## Save compatibility

The legacy event (two technologies and two capital rocket-site levels in one global loop) is fully replaced.
No silent migration of legacy rocket sites is attempted; the rework assumes a new campaign.

## Performance budget

- one global recipient transaction per firing
- no recurring global country scan
- one prepared operation per country
- one active rogue crisis per country and a global rogue cap
- one active warning per country per root
- retaliation caps from part 3
- bounded drift pools and barrage failure rolls
- one coalesced evolution observation per change boundary
- exact cleanup after country or state change
- no GUI polling beyond ordinary decision and scripted-localisation evaluation

## MCP and subagent use

Use the HOI4 MCP routes that answer a concrete question, under the CLAUDE.md retry limit.
Event and technology inspect/render artifacts exist; their compare routes failed with recorded errors (`032_missiles_test_results.md`), and source review is not presented as engine evidence.
Project subagents are spawned with a fully self-contained prompt and no inherited parent context, following `chaos-redux-subagents`.

## Explicit implementation boundaries

Do not add any of these without a new accepted design:

- country package, national focus tree, faction or formable nation
- leader, portrait or flag
- custom unit or custom 3D model
- animated sprite
- dedicated event-owned scripted GUI
- event-owned super-event or campaign terminal branch
- new chemical or biological agent
- free nuclear or thermonuclear stockpile
- generic all-country periodic scanner
