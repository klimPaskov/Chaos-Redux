# Scripted system architecture plan

Status: historical planning architecture. Implemented architecture is current at engine-compatible gameplay commit `407b9a05`, atop balance freeze `1c87d923`; current runtime and completion facts override proposed helper names or pending language below.

This is an implementation architecture handoff, not Clausewitz code. Final helper names may be adjusted to existing repository conventions after inspection.

## State ownership

### Target country state

The target country should own or reference:

- event active flag
- fixed target identity marker
- current baseline phase
- current evolution stage
- Evidence
- Preparedness
- current recent-operation family
- selected suspect ID or target pointer
- public reveal state
- target-war state
- scenario origin and intensity when applicable

### Global event state

The system needs one active Event 011 context unless the existing event framework explicitly supports parallel targets. Global state should own:

- active target event target
- member registry or aligned country markers
- founder order
- sponsor and second-major identity
- faction leader identity
- hidden doctrine
- Cohesion
- Readiness
- Alertness
- War Pressure
- public faction created state
- super-event fired state
- reveal route
- scenario type and launch bypass

### Member country state

Each active or former member should own:

- current member flag
- founder flag when applicable
- recruit order
- primary motive
- commitment band
- confirmed-by-target state
- turned-channel state
- delayed-call or compromised-plan state
- invalidated or exited state
- prewar sponsor obligation or promised spoils when relevant

### Suspect state

Suspect confidence can live on candidate countries so selected-target decisions can read it directly. Keep separate flags for possible, plausible, likely, and confirmed display bands only if the GUI needs flags. Otherwise calculate bands from one value.

## Proposed helper map

| Proposed helper | Scope | Inputs | Output and side effects | Main call sites |
| --- | --- | --- | --- | --- |
| secret_alliance_can_be_target | Country trigger | Candidate target | Valid target boolean, including founder pool size | event weight and manual fire |
| secret_alliance_is_valid_member_candidate | Candidate country trigger with target context | target, stage, sponsor mode | Candidate validity | founder and recruit selection |
| secret_alliance_score_candidate | Effect or scripted value pattern | target, candidate, desired role | Temporary weighted score | founder, recruit, sponsor selection |
| secret_alliance_initialize | Global or target effect | target, opening evolution | Clears stale state, selects doctrine and founders, seeds values | entry event and scenario wrapper |
| secret_alliance_assign_motive | Candidate country effect | target and candidate context | Sets one motive and initial commitment | founder and recruit setup |
| secret_alliance_register_member | Candidate country effect | role and recruit order | Adds member state and adjusts values | founding and recruitment |
| secret_alliance_remove_member | Candidate country effect | exit reason | Clears active state, records former status, adjusts cohesion | validity cleanup, defection, settlement |
| secret_alliance_refresh_member_validity | Global effect | current target | Removes dead, absorbed, target-aligned, or impossible members | before operations, recruitment, reveal, war calls |
| secret_alliance_choose_operation | Global effect | stage, doctrine, target vulnerabilities | Selects one valid weighted family | operation pulse |
| secret_alliance_resolve_operation | Target and member context | operation type, primary actor | Full, partial, or failure outcome and memory | operation events and decisions |
| secret_alliance_try_recruit | Global effect | stage and sponsor context | Selects candidate and resolves approach | recruitment pulse and evolution entry |
| secret_alliance_update_cohesion | Global effect | reason and magnitude band | Changes Cohesion with caps and history | disputes, operations, diplomacy, exposure |
| secret_alliance_update_readiness | Global effect | preparation layer and magnitude | Changes Readiness and layer state | intelligence and military operations |
| secret_alliance_add_evidence | Target effect | evidence class, quality, actor | Changes Evidence and suspect confidence with anti-duplication | investigations, leaks, failed operations |
| secret_alliance_update_preparedness | Target effect | component and duration | Changes Preparedness and maintained project state | protection and emergency decisions |
| secret_alliance_set_selected_suspect | Target effect | selected candidate | Stores selected target and activates relevant decisions | scripted GUI or selector decision |
| secret_alliance_clear_selected_suspect | Target effect | none | Clears selected state and target flags | close, invalidation, reveal |
| secret_alliance_can_force_reveal | Target trigger | Evidence, confirmed members, route state | Reveal-action availability | dossier and conference decisions |
| secret_alliance_refresh_reveal_leader | Global effect | active members | Saves valid faction leader | all reveal paths |
| secret_alliance_reveal | Global effect | reveal route and war context | Forms faction, adds valid members, converts values, fires super-event, closes hidden systems | hostile war, pact reveal, forced reveal, scenario |
| secret_alliance_join_target_war | Member effect | target war and side | Adds every valid active member to hostile target war | reveal after war begins |
| secret_alliance_convert_prewar_state | Global and target effect | values and compromised flags | Creates Resolve, opening coordination, target advantages, delayed calls | reveal |
| secret_alliance_refresh_coalition_resolve | Global effect | war outcomes, member state, sponsor condition | Updates visible Resolve and fracture eligibility | war pulses and events |
| secret_alliance_try_member_exit | Member effect | motive, Resolve, war cost, offers | Defection, delay, withdrawal, or refusal outcome | separate terms and war crises |
| secret_alliance_end | Global effect | termination reason | Clears runtime state and preserves history and achievement facts | collapse, target removal, settlement |
| secret_alliance_launch_scenario | Global effect | type, intensity, target | Builds public coalition, forms faction, starts war, fires super-event | scenario confirmation |

## Tuning constant groups

Proposed categories:

- `secret_alliance_stage_thresholds`
- `secret_alliance_evolution_pacing`
- `secret_alliance_operation_pacing`
- `secret_alliance_cohesion_changes`
- `secret_alliance_readiness_changes`
- `secret_alliance_evidence_quality`
- `secret_alliance_preparedness_components`
- `secret_alliance_recruitment_weights`
- `secret_alliance_sponsor_weights`
- `secret_alliance_reveal_conversion`
- `secret_alliance_resolve_changes`
- `secret_alliance_scenario_scale`
- `secret_alliance_ai_weights`

Use file-scoped literals only for fields that reject shared constants. Mirror those literals with documented shared tuning when duplication is unavoidable.

## Membership registry options

### Preferred approach

Use country flags and country variables for durable membership, plus event targets for current target, leader, sponsor, selected candidate, and temporary operation actor. Iterate over a narrow saved member array if the repository already has a proven dynamic array pattern.

### Avoid

- scanning every country every day
- storing tags as free-form localisation strings
- relying only on temporary variables
- leaving global event targets uncleared
- assuming a country remains valid after faction or subject changes

## Event target plan

| Event target | Persistence | Purpose | Cleanup |
| --- | --- | --- | --- |
| secret_alliance_target | Global while event active | Fixed target | event end |
| secret_alliance_sponsor | Global while active and valid | First major sponsor | sponsor exit or event end |
| secret_alliance_second_major | Global while active and valid | Evolution III second major | member exit or event end |
| secret_alliance_leader | Global after selection | Reveal faction leader | faction end or event end |
| secret_alliance_operation_actor | Regular chain target | Current operation member | automatic chain end |
| secret_alliance_recruit_candidate | Regular chain target | Current invitation target | automatic chain end |
| secret_alliance_selected_suspect | Prefer country flag plus stored ID or proven global target | Human-selected suspect | selector close, invalidation, reveal |
| secret_alliance_war | Do not store as opaque target unless needed | Target war context | reveal or war end |

## Reveal transaction

The reveal helper must behave like one transaction.

1. Confirm event active and not already public.
2. Refresh active membership.
3. Verify at least one valid active member remains.
4. Save reveal route and hostile-war context.
5. Select leader.
6. Create the faction once.
7. Add every valid active member.
8. Apply public faction identity.
9. Convert prewar values.
10. Fire super-event once.
11. Join target war immediately when hostile war already exists.
12. Start countdown only when reveal precedes war.
13. Replace hidden category state with public coalition state.
14. Record history and evolution context where applicable.
15. Clear temporary recruitment, operation, and selected-suspect state.

It must be idempotent so guarantee chains, war joins, event pulses, and scenario launch cannot create duplicate factions or repeated super-events.

## Human-country handling

Human candidates must branch to explicit invitation events. Acceptance records commitment and future reveal obligation. Refusal cannot be overridden by AI logic. A human country becoming invalid before reveal must receive clear cleanup or withdrawal handling.

## Evolution logging plan

Before each true evolution record:

- event ID 11
- one stable evolution type for the pact escalation track
- stage 1, 2, or 3
- display tier
- actor only when the stage belongs to a specific sponsor or coalition leader and the UI benefits from it

Set enable checks in the same limit that records and unlocks the evolution. Baseline phase changes do not call the evolution logger.

## Scenario plan

The scenario wrapper sets a tightly scoped launch flag, builds the selected composition, calls the same public reveal helper, starts war, then clears the bypass. It must not leave the normal event marked as having passed through baseline or evolutions unless the event-log design explicitly records scenario origin.

## Cleanup plan

Cleanup must cover:

- current and former member runtime flags
- sponsor and leader targets
- suspect confidence and selected target
- operation and mission flags
- maintained Preparedness projects
- hidden ideas and dynamic modifiers
- AI strategies
- scenario bypass
- public countdown
- temporary war-call flags
- stale faction identity after dissolution

Preserve:

- fired-event history
- evolution history
- reveal route history
- achievement facts that require aftermath evaluation
- confirmed responsibility needed for settlement text

## Validation notes

Task-specific checks should prove:

- three-founder pool failure returns unavailable rather than selecting invalid countries
- no member can be registered twice
- a member entering any normal hostile target war calls the reveal transaction
- every active valid member joins that war once
- an invalid member is removed before reveal
- scenario and normal reveal use the same conversion logic
- repeated reveal calls do not repeat the super-event or faction creation
- selected suspect and global targets clear at termination
- disabled evolutions do not set evolution-completion state
