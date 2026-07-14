# Event 016 Scripted-System Architecture Handoff

## Status and ownership

This handoff records the completed Event 016 scripted-system architecture tranche. It implements reusable constants, triggers, effects, and MTTH entries only. The parent agent still owns event scripts, decisions, special projects, character and trait definitions, KRG creation, focus content, shared registries, shared Fallout wiring, localisation, assets, AI, achievements, audits, and final enablement.

Owned files:

- `common/script_constants/016_brilliant_scientist_constants.txt`
- `common/scripted_triggers/016_brilliant_scientist_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_effects.txt`
- `common/mtth/016_brilliant_scientist_mtth.txt`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_scripted_system_architecture_handoff.md`

No shared gameplay file was edited in this tranche.

## Fixed reservations and identity contract

The owned constants establish these binding identifiers:

| Surface | Reservation |
| --- | --- |
| Event ID and evolution type | `16` |
| Project families | `15` distinct families |
| Persistent project stages | Theory, Prototype, Deployment, Weaponization |
| Logged evolutions | Exactly four, stages and tiers I through IV |
| World-end scenarios | `11` Laboratory World; `12` Strategic Singularity |
| Visible super-events | `90` recognition, `91` KRG formation, `92` global threat, `93` Laboratory World, `94` Strategic Singularity, `95` qualifying defeat |
| Achievements | Exactly seventeen stable enum entries |
| Character | Only `KRG_warren_kruger` |

Event 020 retains world-end scenario 10. Concurrent Event 015 occupies visible super-events through 89. The earlier Event 016 proposals at 85-90 and 88-93 are superseded.

The fixed role modifiers are centralized under `constant:brilliant_scientist_identity.*`:

- `advisor_research_speed_factor = 1.0`
- `special_project_speed_factor = 1.0`
- `scientist_breakthrough_bonus_factor = 1.0`
- `scientist_research_bonus_factor = 1.0`
- `scientist_xp_gain_factor = 2.0`
- `facility_supply_consumption_factor = -0.5`

The parent-owned advisor trait `brilliant_scientist_research_director` must be the only Event 016 source of `research_speed_factor = 1.0`. Public and secret recruitment use the same character, advisor role, scientist role, and idea token. Do not add a second +100% country idea.

If a parent-owned trait field is proven not to parse a `constant:` token, mirror the corresponding value with one named file-scoped `@` constant in that trait file and document the exception. Do not silently hardcode the value.

The advisor role uses `slot = theorist` and `ledger = army`. This is a deliberate, engine-supported tradeoff: Kruger occupies the normal theorist slot and is classified in the Army ledger even though his country modifier is cross-domain. He cannot stack with another active theorist in that slot.

The scientist role sets all six live specializations to exactly `constant:brilliant_scientist_value.five`: nuclear, naval, air, land, biowarfare, and chemical warfare. It creates no replacement, clone, random scientist, or second Warren Kruger token.

## Fire-once host selection

`brilliant_scientist_is_eligible_host` is the single eligibility contract for automatic selection and later transfer recipients. A candidate must:

- exist, not be capitulated, and not be a subject;
- control its capital;
- own and control at least `constant:brilliant_scientist_host_selection.minimum_core_states` core states;
- have at least one separate valid owned, controlled core primary facility state;
- not be a special chaos country, actual nonhuman country, KRG, or a country under world end;
- have no Event 016 host-history, former-host, rejection, expulsion, killing, transfer-away, loss, departure, or received-by-transfer history.

The minimum core-state count and the one-valid-site gate are intentionally separate. The two counted core states are not both required to satisfy the facility-state trigger.

The one-shot resolver is `brilliant_scientist_prepare_random_event_fire`. It outputs:

- temporary `brilliant_scientist_prefire_ready`;
- regular event target `brilliant_scientist_prefire_host`;
- temporary evolved-opening stage and tier.

Host selection mirrors the verified Fury weighted-scope pattern: each eligible country receives a bounded whole-number weight, is duplicated into a temporary array by `while_loop_effect`, and is selected by `random_scope_in_array`. The pool and every temporary counter are cleared afterward. The explicit `every_country` scan runs only when the fire-once dispatcher evaluates Event 016; no periodic on-action invokes it.

The weight includes:

- research slots and electronics/computing technology;
- a technological-gap bonus when the candidate lacks both electronics/computing while an enemy or neighbor has either;
- weak-industry pressure and high-industry capacity;
- controlled urban capacity;
- war pressure, major status, special-project facilities, government structure, and chaos tier;
- actual persistent science-chaos history flags: `bioweapon_available`, `used_bioweapon`, `germany_mengele_facility_built_from_demand`, `mengele_clone_army_facility_built`, `holy_realm_thermonuclear_doctrine`, `nlc_doctrine_scientific_refuge_organized`, and `resources_found_first_battle_analyzed`.

There is no dead Event 016-only history-weight flag.

## Opening history actor rebinding

The generic random-event system records the history row before the opening choice resolves. The initial prefire host is therefore not necessarily the final accepting host when the player sends Kruger away.

The owned contract is:

1. `record_events_log_history_entry` appends all aligned Event Log history arrays.
2. Immediately after the append block, its Event 016 branch calls `brilliant_scientist_bind_opening_history_sequence = yes`.
3. That helper stores the just-created `global.events_log_history_sequence` in `global.brilliant_scientist_pending_history_sequence` and sets `brilliant_scientist_history_actor_rebind_pending`.
4. The final accepting country calls `brilliant_scientist_initialize_host_state`.
5. Initialization calls `brilliant_scientist_finalize_opening_history_actor`, locates the exact row by both sequence and Event ID 16, replaces `global.events_log_history_actor_entries^index` and `global.events_log_history_has_actor_entries^index`, then clears pending state only after a successful match.

Required shared call site, after all `record_events_log_history_entry` arrays have appended:

```txt
if = {
	limit = { check_variable = { event_id = constant:brilliant_scientist_event.id } }
	brilliant_scientist_bind_opening_history_sequence = yes
}
```

`events_log_set_default_actor_for_current_event` should still map Event 016 to `brilliant_scientist_prefire_host`. The sequence rebind is what makes the send-away route truthful.

## Initial send-away route

`brilliant_scientist_select_initial_send_away_recipient` is separate from post-appointment transfer. It:

- can run only in a human rejecting country;
- saves regular target `brilliant_scientist_send_away_rejector`;
- selects a never-hosted eligible recipient through a bounded weighted temporary pool;
- excludes the rejector and every country with Event 016 host history;
- outputs regular target `brilliant_scientist_send_away_recipient` and temporary selected state;
- never changes nationality, roles, current-host state, or project ledgers.

The weight prioritizes an allied or same-faction country welcoming scientific refugees, an ideologically compatible independent competitor, a technologically pressured neighbor, a major, an active special-project facility holder, and a country under war pressure. Every otherwise valid country retains a positive base weight.

The parent event must fire the recipient appointment event from the same effect chain. It must not call `brilliant_scientist_transfer_kruger_atomically` because Kruger has not yet received nationality or roles.

## Host state and facility selection

`brilliant_scientist_initialize_host_state` establishes:

- host/current-host history and the persistent global current-host target;
- public or secret recruitment posture;
- visible Mandate, Dependence, Exposure, and Project Capacity;
- hidden Independent Capacity and Grievance;
- temporal synchronization/debt state, project ledgers, terminal/origin defaults, a primary facility, derived Government Control, and opening history-actor finalization.

Primary and secondary facility selectors use weighted temporary state arrays, not uniform state selection. Both require owned, controlled core states and score:

- infrastructure;
- civilian and military factories;
- raw state population and urban category;
- capital status as a conservative victory-point concentration signal;
- supply nodes and railways;
- anti-air and land/coastal forts;
- existing nuclear, air, land, or naval special-project facilities;
- foreign-border exposure versus an interior site;
- coastal exposure;
- public route preference for visible urban/transport access;
- secret route preference for defended, less urban sites.

The secondary selector excludes the primary state and adds network/security weight. Both pools, counts, and weight variables are cleared after selection.

`brilliant_scientist_clean_invalid_facility_targets` clears captured, destroyed, or otherwise invalid targets. Later foreign/enclave laboratories may use the broader non-core `brilliant_scientist_is_valid_facility_state`; appointment and transfer primary/secondary sites may not.

## Fixed identity and atomic transfer

`brilliant_scientist_transfer_kruger_atomically` runs on the old host with regular target `brilliant_scientist_transfer_recipient`. All validation occurs before the first mutation. It requires:

- the single fixed character to exist in the current host;
- `KRG_warren_kruger` not to be an active scientist on a special project;
- no confirmed death, confinement, or character transaction lock;
- a never-hosted eligible recipient.

The transaction then:

1. sets country and global transaction locks;
2. snapshots the old host and posture;
3. deactivates/removes advisor and scientist roles;
4. reconciles the old institutional portfolio down to independently replicated stages;
5. removes old current-host/facility state and records departure;
6. calls `set_nationality` exactly once on `KRG_warren_kruger`;
7. initializes the recipient, re-adds the same roles, reconstructs only Kruger's personal carried portfolio, restores continuity/portrait state, and installs the new global current-host target;
8. clears locks and returns temporary `brilliant_scientist_transfer_committed`.

Kruger's personal history is stored on character flags. Institutional project history remains in country arrays. No duplicate character is created.

## Fifteen-family project ledger

The family enum is exactly:

1. computation
2. electronics
3. materials
4. rocketry
5. high energy
6. biomedical
7. teleportation
8. cloning
9. robotics
10. paleogenetics
11. xenobiological synthesis
12. biological weapons
13. alien arms
14. temporal
15. singularity

Paleogenetics and xenobiological synthesis are separate families and have separate personal-history flags, stage entries, burden profiles, and duration tables.

Country arrays maintain current stage, independently replicated stage, suspended, damaged, dismantled, published, and stolen history. Family IDs are one-based; the shared index loader derives the zero-based array index. No semantic array index is hardcoded. Kruger inheritance uses one dynamic `entries^brilliant_scientist_project_index` writer after selecting each family's highest personal flag.

The cost loader accepts temporary `brilliant_scientist_project_family` and `brilliant_scientist_requested_project_stage`. It returns rounded temporary burdens for civilian/military factories, support equipment, trucks, trains, fuel, manpower, Army/Air/Navy XP, political power, strategic-resource units, capacity, and reference duration.

Important native-project clock rule: `brilliant_scientist_cost_duration_days` is informational and parity data for UI/decision planning only when the family uses a native special project. It must not stack with native project `complexity` or `prototype_time`. The native special-project clock is authoritative.

## Evolutions and MTTH

The owned files provide exactly four once-only evolution wrappers and eight MTTH entries: prefire and active intervals for I-IV. Each wrapper places every persistent chronology/unlock write behind the shared disabled-evolution check and its once-only flag. `brilliant_scientist_record_prefire_evolved_opening` records each enabled stage up to the selected opening stage rather than skipping chronology.

The MTTH entries centralize chaos, posture, value, project, crisis, and stabilization factors. They are consumed by targeted events or decisions only. This tranche adds no daily, weekly, monthly, or other periodic whole-world on-action.

Parent Event Details wiring must add exactly four stable Event 016 preview rows and route their recorded actor to the actual current host/KRG actor.

## Foreign interaction

Foreign interest is persistent per country and bounded to 0-100. It scores major status, proximity, faction relationship, host exposure, advanced projects, and war relation. The foreign-actor selector now weights its temporary pool by the exact stored interest value after the observation gate; it is not uniform.

One selector intentionally remains uniform: `random_owned_controlled_state` inside `brilliant_scientist_select_foreign_target_state`. This chooses a generic staging/operation state after the foreign actor has already been selected. It is not a host laboratory, primary/secondary facility, or facility-growth decision, and the architecture assigns no semantic advantage among its valid states.

Invitation, joint-lab, protection, theft, sabotage, extraction, and assassination gates are separate and share the same actor/target cleanup contract.

## Temporal contract

Temporal use is exact per named target, not a generic use counter.

- Caller input: temporary `brilliant_scientist_temporal_target_id`.
- Binder: `brilliant_scientist_bind_temporal_target`.
- Current persistent binding: `brilliant_scientist_temporal_bound_target_id`.
- Immutable used ledger: country array `brilliant_scientist_temporal_used_target_ids`.
- Commit: `brilliant_scientist_commit_bounded_temporal_action`.

The binder rejects non-positive, out-of-range, or previously used IDs. A successful commit spends synchronization capacity, adds bounded temporal debt, appends the exact target ID, records a persistent scar, and clears the current binding. Anchor loss clears authentication and the current binding but never erases debt, used IDs, or scars.

Stabilization is a targeted timed country flag/mission contract. It consumes the primary facility, opens the weakness window, and has no passive debt decay or periodic world scan.

## KRG formation and capped forces

The owned triggers accept only verified multi-state formation inputs. Charter, enclave, rebellion, multi-site, and institutional-capture routes all require the parent territory planner to provide viable selected states and host-survival counts. There is no one-state or generic-country fallback.

`brilliant_scientist_calculate_formation_power_score` consumes territory/facility counts, project stage, Independent Capacity, Grievance, Dependence, and Mandate. `brilliant_scientist_load_capped_force_count` converts a project stage and requested force family into a bounded spawn count. It never spawns units itself; parent country/unit code must enforce templates, equipment ratios, and scenario-specific placement.

## Terminal contracts

Laboratory World and Strategic Singularity are mutually exclusive commitments.

The singularity component enums are:

- `constant:brilliant_scientist_singularity_component.command_core`
- `constant:brilliant_scientist_singularity_component.power_link`
- `constant:brilliant_scientist_singularity_component.containment_lattice`
- `constant:brilliant_scientist_singularity_component.temporal_authenticator`
- `constant:brilliant_scientist_singularity_component.delivery_architecture`
- `constant:brilliant_scientist_singularity_component.fail_deadly_governor`

Arming-state enums run from dormant through theory, components, construction, arming, armed, disarming, verified nonterminal, and terminal.

`brilliant_scientist_prepare_singularity_terminal_commit` deliberately stops before shared mutation. When ready, it returns:

- `brilliant_scientist_terminal_commit_ready`;
- exact deficit to `constant:chaos_meter_tier_range.tier_final.plus` in `brilliant_scientist_singularity_chaos_deficit`;
- Event 016 chaos-history reason reservation in `brilliant_scientist_singularity_chaos_history_reason`;
- regular source target `brilliant_scientist_terminal_source_actor`.

The parent source-aware Fallout adapter must then:

1. set `chaos_change` to the returned deficit;
2. set `chaos_history_reason`, `chaos_history_reason_custom`, `chaos_history_target_count`, and regular `chaos_history_actor` from the Event 016 source;
3. call shared `add_chaos_meter_value`;
4. commit the canonical Fallout consequences with Event 016 source context and visible super-event 94;
5. mark Event 016 singularity terminal state only after the canonical path accepts it.

Ordinary Event 016 contamination must use the generic contamination path. It must not carry the singularity source context or Event 016 terminal reason.

The Laboratory World preparer likewise stops before the shared scenario registry and presentation calls. The parent must use world-end scenario 11 and visible super-event 93. Strategic Singularity uses world-end scenario 12 and visible super-event 94.

`constant:brilliant_scientist_singularity.chaos_history_reason = 216` is an Event 016-local reservation only. The parent must collision-scan and register the shared chaos-history reason and localisation before calling it.

## Exact parent integration checklist

1. Add the Event 016 availability branch to the active random-event pool using `brilliant_scientist_automatic_event_is_available`.
2. In the no-cluster dispatcher, call `brilliant_scientist_prepare_random_event_fire`; dispatch `chaosx.nr16.1` in `event_target:brilliant_scientist_prefire_host` only when ready.
3. Map Event 016's initial Event Log actor to `brilliant_scientist_prefire_host`.
4. Add the post-append `record_events_log_history_entry` call to `brilliant_scientist_bind_opening_history_sequence` exactly as shown above.
5. Create/recruit only `KRG_warren_kruger`, set recruitment posture, call `brilliant_scientist_initialize_host_state`, then `brilliant_scientist_add_kruger_roles` and the appropriate evolved-opening recorder.
6. For player rejection, set rejection history, call `brilliant_scientist_select_initial_send_away_recipient`, and immediately fire the recipient appointment event in the same chain. Do not call atomic transfer.
7. Define the parent-owned advisor/scientist traits with the identity constants and ensure no second +100% research-speed source exists.
8. Route post-appointment moves only through `brilliant_scientist_transfer_kruger_atomically`.
9. Make decisions/projects call the family/stage ledger effects and use the native-clock rule above.
10. Schedule the four MTTH/evolution readiness paths through targeted events or missions; add exactly four Event Details preview rows.
11. Use the foreign interest/actor/action gates from decisions and targeted events, not a periodic world scan.
12. Feed only parent-verified multi-state territory into the KRG formation gates.
13. Register world-end scenarios 11/12, visible super-events 90-95, and all seventeen achievements in their shared owners.
14. Implement the source-aware canonical Fallout adapter and register chaos-history reason 216 only after collision review.
15. Keep Event 016 default-disabled until event scripts, decisions, AI, KRG, focus content, terminal paths, localisation, assets, achievements, docs, workbook alignment, and required audits are complete.

## Conservative engine-safe scoring interpretations

These points are explicit so they are not mistaken for hidden fallbacks:

- HOI4 exposes raw state population and urban category but no stable general state-scope trigger for the aggregate value of every victory point in a state. Facility weighting therefore uses population/urban category directly and `is_capital = yes` as the conservative high-VP concentration signal.
- HOI4 has no general diplomatic `is_rival` trigger. The send-away pool represents an ideologically compatible rival as a same-government candidate that is neither an ally nor in the rejector's faction.
- Border risk is an adjacent state not owned by the host; isolation is the absence of such an adjacent foreign-owned state. No unsupported path-distance calculation is attempted.
- The selected foreign actor's generic staging state remains uniform for the reason documented in the foreign-interaction section.

These interpretations affect selection weights only. They do not remove a route, mechanic, actor, facility, or outcome.

## Validation and evidence

- The host and send-away pool implementation mirrors `common/scripted_effects/007_fury_effects.txt` weighted duplication and `random_scope_in_array` structure.
- Dynamic indexed array reads/writes mirror live Event 006 and Chaos Meter precedents; portfolio inheritance contains no literal `^0` through `^14` writes.
- Country-to-state `is_owned_and_controlled_by = PREV` follows the live Event 018 trigger pattern; the minimum core-state count and valid-site gates were reviewed as separate conditions.
- A full owned effects/triggers/MTTH scan found no gameplay numeric literals outside script-constant declarations and no scoped temporary variables.
- Primary and secondary facilities and all country actor selections are weighted. The sole uniform selector is the explicitly documented generic foreign staging-state selector.
- Raw brace counts are balanced in all four Clausewitz files, and no duplicate top-level owned identifier was found.

## Remaining risks and blockers

- Parent-owned trait/character files must load the exact tokens referenced here: `KRG_warren_kruger`, `brilliant_scientist_research_director`, and `brilliant_scientist_polymath`.
- Parent special-project definitions must confirm the custom biowarfare and chemical-warfare specializations remain named `specialization_biowarfare` and `specialization_cw`.
- Shared history actor binding, dispatcher, Event Details, scenario registry, Fallout, chaos-history reason/localisation, super-event, achievement, and final settings wiring remain parent-owned and incomplete until integrated.
- Super-event IDs 90-95, world-end IDs 11-12, chaos-history reason 216, KRG, and every shared key need one final live collision scan immediately before shared registration.
- This architecture does not by itself implement or balance the player-facing Event 016 event/decision/project/focus package.

## Simplifications, omissions, and fallbacks

No accepted Event 016 subsystem was simplified or replaced in this architecture tranche. No fallback country, one-state KRG formation, duplicate scientist, generic temporal use counter, transform-only identity, uniform host/facility selector, alternate Fallout outcome, reduced project list, reduced evolution list, reduced super-event list, or reduced achievement list was introduced.

The parent integration work listed above remains required; this handoff does not claim Event 016 as a whole is complete.
