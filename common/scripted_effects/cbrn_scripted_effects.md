# CBRN scripted effects reference

This file documents reusable effects owned by the CBRN, protective-equipment, chemical-delivery, Chaos Warfare doctrine, and CBRN headquarters subsystems. They are intentionally excluded from the shared `chaosx_dynamic_effects` registry because their call sites remain inside the CBRN architecture.

## Placement rule

Keep a helper here when its inputs, ledgers, policy gates, equipment, consequences, or cleanup contract are CBRN-specific. Move a helper to the shared registry only after real call sites show frequent use by unrelated systems or event families. Do not add wrappers, aliases, estimators, proxies, or fallback implementations during a move.

Biological lifecycle, biological raid, and biological operative-release helpers remain owned by and documented with the biological subsystem rather than in either shared dynamic registry. Their subsystem-private interfaces are indexed below only so CBRN maintainers can find the delivery boundary.

## Source files

- `common/scripted_effects/cbrn_achievement_effects.txt`
- `common/scripted_effects/cbrn_action_record_effects.txt`
- `common/scripted_effects/cbrn_battlefield_operation_effects.txt`
- `common/scripted_effects/cbrn_biological_air_effects.txt`
- `common/scripted_effects/cbrn_camp_effects.txt`
- `common/scripted_effects/cbrn_chemical_raid_effects.txt`
- `common/scripted_effects/cbrn_chemical_doomsday_effects.txt`
- `common/scripted_effects/cbrn_chemical_state_effects.txt`
- `common/scripted_effects/cbrn_consequence_effects.txt`
- `common/scripted_effects/cbrn_designer_effects.txt`
- `common/scripted_effects/cbrn_diplomacy_effects.txt`
- `common/scripted_effects/cbrn_doctrine_effects.txt`
- `common/scripted_effects/cbrn_exposure_effects.txt`
- `common/scripted_effects/cbrn_hq_effects.txt`
- `common/scripted_effects/cbrn_occupation_effects.txt`
- `common/scripted_effects/cbrn_payload_effects.txt`
- `common/scripted_effects/cbrn_project_effects.txt`
- `common/scripted_effects/cbrn_protection_decision_effects.txt`
- `common/scripted_effects/cbrn_protection_effects.txt`
- `common/scripted_effects/cbrn_starting_protection_effects.txt`

## cbrn_append_unified_action_record

Appends one package-wide action row after an accepted deliberate Chemical action or deliberate biological seed has already been validated and resolved by its subsystem-specific pipeline.

Scope: attacker country.

Inputs: the normalized `cbrn_unified_record_*` temporary values listed in `common/scripted_effects/cbrn_action_record_effects.txt`, plus required `event_target:cbrn_unified_record_target_state`. `event_target:cbrn_unified_record_victim_country` is optional when the exact victim is already known.

Defaults: a missing target state fails closed and writes no record. When the caller does not supply an exact victim, the helper records the target state's owner; an unowned target records the attacker so the aligned country-scope array and Event Log payload never contain a numeric placeholder where a country scope is required.

Outputs: an immutable identity row in the aligned global CBRN action arrays, attacker mirrors for the latest row and UID, and one Event Log history entry carrying that row index.

Side effects: none outside record keeping and Event Log refresh. This helper does not deliver an agent, debit payload, calculate harm, infer a target, scan periodically, or estimate activity.

Example:

```txt
set_temp_variable = { cbrn_unified_record_weapon_class = constant:cbrn_action_record_weapon_class.chemical }
event_target:cbrn_selected_target_state = {
	save_event_target_as = cbrn_unified_record_target_state
}
cbrn_append_unified_action_record = yes
```

## Biological subsystem-private delivery effects

Source: `common/scripted_effects/biological_operation_effects.txt`. These helpers are not shared dynamic effects and must not be moved into `chaosx_dynamic_effects` without frequent, unrelated call sites.

### bio_operative_release_resolve

Operation-scope entry point for Anthrax, Plague, Tularemia, and Smallpox intelligence operations. The caller supplies the exact agent code. The native operation supplies ROOT as initiator, FROM as target country, and FROM.FROM as selected state. The effect first verifies that FROM still controls FROM.FROM, then records and validates the exact actor, victim, selected state, completed project, state profile, policy, and readiness before resolving abort, partial release, or full release. Partial and full releases enter `bio_lifecycle_dispatch_seed`; an abort records an attempted delivery without creating a biological-use history record. Theater Contamination and Terminal Hazard return a bounded amount of Command Power once after resolution without changing the physical equipment cost.

The operation engine does not expose the runtime amount charged by its `equipment` block. The exact native cost and `return_on_complete = no` are therefore authoritative, while the lifecycle's numeric payload fields remain zero for this route rather than recording a fabricated amount or proof. Defaults: invalid or incomplete native context fails closed with no seed, no inferred target, and no substitute payload debit. Side effects: records the exact attempt result and lifecycle consequences owned by the biological subsystem.

### bio_operative_release_on_operative_captured

Character-scope entry point called only from the current-version `on_operative_captured` hook. It reads `operative_leader_operation`, `operation_country`, and `operation_state` to recover the exact ordinary-agent operation, employer, victim, and selected state. A matching live seeded episode receives the confirmed-operative attribution floor and one-shot outbreak coverup consequence; otherwise the actual capture receives public-attempt and coverup records without weapon-use history.

The engine exposes no operation-instance identifier for deduplicating multiple captured operatives from the same operation. The ledger counts actual captured operatives, not inferred operation attempts, and each actual capture callback is consequential; this is not a timer or inferred duplicate. Defaults: any missing, mismatched, stale, zombie, or unsupported operation context fails closed. It performs no periodic search, target estimation, scope substitution, or fallback resolution.

Internal helpers calculate the three outcome weights, derive readiness weaponization and attribution-control concealment, record the exact attempt result, dispatch the exact seed, refund bounded doctrine Command Power, and distinguish a captured seeded episode from a captured no-release attempt. They are private implementation details of the two interfaces above.

## CBRN diplomacy and bilateral retaliation effects

Source: `common/scripted_effects/cbrn_diplomacy_effects.txt`.

### `cbrn_diplomacy_classify_retaliation_action`

Country-scope classifier for one exact chemical or deliberate biological action. The caller supplies `event_target:cbrn_retaliation_target_country` and may supply `cbrn_retaliation_action_proportionate_proof` only after proving a military target. Nerve suppression, doomsday delivery, and doomsday-severity actions are excluded.

The effect returns temporary `cbrn_action_retaliation_status` as none, authorized, or proportionate. It records last-retaliation history only when the current Retaliation Authority policy, live war, and country-ID-keyed bilateral right all match the exact target. It does not change payload, harm, evidence, attribution, Condemnation, or the first-use ledger.

### `cbrn_diplomacy_classify_biological_seed_retaliation`

State-scope biological adapter. It accepts only a deliberate ordinary-pathogen seed with exact actor and victim proof. Battlefield dissemination can supply proportionate proof only when the selected state still belongs to the exact victim and contains that controller's divisions. Strategic, covert, and civilian-target routes may be authorized but receive no participant-pressure mitigation. Accidents, spread, field tests, captured-facility releases, and doomsday batches remain unclassified.

### `cbrn_diplomacy_record_confirmed_cbrn_use`

Country-scope bilateral ledger entry for an exact confirmed offender. The caller supplies `event_target:cbrn_retaliation_target_country`, `cbrn_confirmed_use_action_date`, and `cbrn_retaliation_source_type`. It stores the earliest exact action date against the target's country ID and compares the reciprocal record.

The first victim receives a 365-day right keyed to the offender ID. A later strike cannot grant the original first user mitigation. Same-day ties revoke both directions because current script exposes day precision only. Existing death, evidence, attribution, contamination, medical, domestic, and weapon-use history is untouched.

Example:

```txt
event_target:cbrn_action_victim_country = {
	save_event_target_as = cbrn_retaliation_target_country
}
set_temp_variable = { cbrn_confirmed_use_action_date = cbrn_dispatch_current_day }
set_temp_variable = { cbrn_retaliation_source_type = constant:cbrn_diplomacy_source.chemical }
cbrn_diplomacy_record_confirmed_cbrn_use = yes
```

### Exact forensic liability effects

`cbrn_diplomacy_append_chemical_action_record` is state-scoped and is called once after exact Chemical liability has been calculated. It appends one exact action row to aligned persistent arrays containing the exact UID, actor, victim, action date, agent, class, route, severity, source label, explicit release status, native raid result where applicable, deaths, contamination, medical load, evidence, attribution, retaliation status, paid and unpaid Condemnation, paid and unpaid retaliation relief, row status, and confirmation-registration status. Accepted shared-dispatch actions record a real release. Failed or aborted chemical air raids record an explicit no-release attempt when they create evidence or Condemnation, so their liability is not left as an unaccountable aggregate. Rows are never overwritten or deleted; only their evidence, attribution, settlement, confirmation, and status fields advance. The state-level `cbrn_last_chemical_*` fields and actor-level latest-use fields remain compatibility and latest-display mirrors only; forensic settlement never reads them as the authoritative action record.

`cbrn_diplomacy_select_chemical_forensic_record` scans only the selected state's exact open rows and selects the greatest evidence value, preserving the older row on a tie. `cbrn_diplomacy_load_selected_chemical_record` loads that row and its exact actor and victim scopes. `cbrn_diplomacy_begin_forensic_publication` locks either that chemical row or one exact biological seed before the timed decision pays its cost, so later actions cannot replace the selected record.

`cbrn_diplomacy_expose_recorded_chemical_responsibility` is state-scoped. The caller supplies the loaded row and its resulting attribution band. The effect calculates the desired paid share from that action's own recorded total, paid, and unpaid Chemical liability, then asks `condemnation_expose_exact_hidden_source_amount` to settle only that delta. The actor's aggregate hidden Chemical bucket is a ceiling, never the source of the amount. Repeating the same evidence band exposes nothing twice.

`cbrn_diplomacy_register_newly_confirmed_chemical_record` records bilateral first use only for a row whose explicit release status proves agent release and when both exact countries still exist. A confirmed no-release attempt can expose its own liability but cannot create weapon-use history, treaty callbacks, or retaliation authority. A confirmed release record whose historical actor no longer exists is marked as historical and closed without applying country effects to a successor, controller, or proxy. `cbrn_diplomacy_advance_selected_chemical_record` advances one locked exact chemical row. `cbrn_diplomacy_observe_best_chemical_record` applies the observer evidence increment to the strongest open exact row. `cbrn_diplomacy_publish_best_forensic_record` advances only the locked chemical row or the locked biological seed if that seed remains current, then clears the publication lock.

`cbrn_diplomacy_project_chemical_record_for_condemnation_detail` is a read-only state-scope UI adapter. The caller supplies the offender's latest exact action UID, and the effect projects only the matching ledger row's state, date, agent, route, current evidence, current attribution, and recorded retaliation classification into ROOT's Condemnation-detail snapshot. A missing UID or row produces no display record; compatibility mirrors are not accepted as evidence or attribution.

`cbrn_diplomacy_reconcile_actor_generic_chemical_exposure` is country-scoped and is called only from an already targeted Condemnation inspection or observer disclosure. The actor's append-only state-and-UID registry visits its own exact chemical rows, and `cbrn_diplomacy_reconcile_exact_row_generic_exposure` applies the same caller-supplied disclosure fraction independently to each row's unpaid liability and retaliation relief while respecting the actor's aggregate exposure ceiling. The helpers return only the amounts actually reconciled to exact rows; unmatched aggregate liability remains hidden rather than being assigned to an inferred action. A fully paid open row becomes settled and decrements its state's open-record count.

### Material diplomacy actions

`cbrn_diplomacy_send_inspection_demand` and its timeout helpers consume exact equipment, preserve the demanding country, apply the sender cooldown, and resolve one native mission without duplicate refusal consequences. The target trigger requires the demander to be an active sanctions participant against that exact target.

`cbrn_diplomacy_begin_international_decon_mission` and `cbrn_diplomacy_complete_international_decon_mission` preserve the exact state, sponsor, and initial recipient, consume the full material bill, reduce only live contamination and medical saturation, and allow only evidence-band progression from an open exact chemical row. Exact humanitarian carve-out participants can sponsor decontamination and protective-equipment exports even when ordinary alliance access is absent. The mission revalidates the recorded provider, original recipient-controller, peace, and at least one continuing alliance, subject, inspection, observer, or exact humanitarian-corridor access route during cancellation and at completion. Loss of access cancels without refund.

These helpers do not scan all countries or states periodically, infer a target, substitute another state, fabricate material, or use a generic dynamic-effect registry.


## grant_random_chaos_special_project_available_tech

This country-scope effect grants one not-yet-owned biological, chemical, or weaponized-zombie special-project unlock to event-family routes explicitly integrated with the CBRN project pool. It is CBRN-owned and is not a shared cross-system dynamic effect.

Inputs: none.
Output: may complete one special project and set the matching delivery technology.
Side effects: clears and may set `chaos_random_special_project_granted`.

Current registry entries:

- `anthrax_bomb` -> `anthrax_bomb_delivery_systems`
- `plague_bomb` -> `plague_bomb_delivery_systems`
- `tularemia_bomb` -> `tularemia_bomb_delivery_systems`
- `smallpox_bomb` -> `smallpox_bomb_delivery_systems`
- `weaponize_the_zombies` -> `zombie_disease_bomb_delivery_systems`
- `sp_cw_sarin_program` -> `sarin`
- `sp_cw_soman_program` -> `soman`

When new chaos biological or chemical special projects are added, add their project and delivery tech to this effect so old focus and decision rewards keep rolling from the expanded project pool.

Example:

```txt
completion_reward = {
grant_random_chaos_special_project_available_tech = yes
}
```

## cbrn_initialize_country_data

Initializes and clamps the persistent national CBRN data model without iterating other countries.

Scope: country.

Inputs: none.

Defaults: Chemical Readiness `0`, readiness cap `19`, defensive-preparation policy, the minimal-program AI profile for an ordinary country, the no-program profile for an actual nonhuman country, full military filter condition, and zero decontamination, medical, biological-security, attribution-control, command-integration, issued-mask, distributed-mask, replacement-demand, reconditioning-cache, and protective-aid values.

Outputs: persistent country variables for Chemical Readiness and policy; the five national CBRN capacities; `cbrn_protection_program_profile`; model-specific military-issue ledgers; military filter condition; replacement demand and reconditioning cache; model-specific and aggregate civilian-distribution totals; and cumulative protective-aid export/receipt totals.

Side effects: existing values are preserved and clamped; readiness is additionally clamped to the current cap. It does not establish a program, grant equipment, distribute masks, award compliance credit, or schedule a pulse.

Example:

```txt
cbrn_initialize_country_data = yes
```

## cbrn_set_use_policy

Sets the national CBRN use-policy enum after validating the requested value.

Scope: country.

Input: temporary `cbrn_requested_use_policy`, from `constant:cbrn_use_policy.*`.

Defaults: invalid or absent requests change nothing.

Output: temporary proof `cbrn_policy_change_accepted` and persistent `cbrn_use_policy` on success.

Side effects: none beyond the accepted policy variable and proof. A live bilateral retaliation window is historical authorization evidence and is not erased by temporarily choosing another policy; every release still has to prove its exact target after Retaliation Authority is selected again. Decision costs, cooldowns, institutions, and stockpile gates remain caller responsibilities.

Example:

```txt
set_temp_variable = { cbrn_requested_use_policy = constant:cbrn_use_policy.limited_battlefield_authority }
cbrn_set_use_policy = yes
```

## cbrn_set_chemical_readiness_cap

Sets an institutional Chemical Readiness cap and immediately brings current readiness inside it.

Scope: country.

Input: temporary `cbrn_requested_readiness_cap`.

Defaults: an absent input changes nothing; country data is initialized first.

Outputs: persistent `chemical_readiness_cap` and possibly reduced `chemical_readiness`.

Side effects: both values are bounded to 0 through 100. Milestone, institution, equipment, and HQ callers own the requested cap.

Example:

```txt
set_temp_variable = { cbrn_requested_readiness_cap = constant:cbrn_readiness.operational_cap }
cbrn_set_chemical_readiness_cap = yes
```

## cbrn_modify_chemical_readiness

Adds a signed readiness change without allowing the value to exceed its institutional cap or fall below zero.

Scope: country.

Input: temporary `cbrn_readiness_delta`.

Defaults: an absent input changes nothing; country data is initialized first.

Output: persistent `chemical_readiness`.

Side effects: none outside the current country.

Example:

```txt
set_temp_variable = { cbrn_readiness_delta = 5 }
cbrn_modify_chemical_readiness = yes
```

## cbrn_calculate_action_protection

Resolves six equipment- and institution-backed protection layers into chemical-agent-class multipliers. Equipment snapshots treat usable coverage as the active score and weighted model quality as its ceiling: partial basic issue follows its actual coverage band, while full basic issue caps at 55 effective protection. The weighted skin, antidote, decontamination, medical, and warning layers can raise the shared result.

Scope: the attacker country or the enclosing effect chain; the helper uses temporary variables only.

Required temporary inputs:

- `cbrn_action_agent_class`
- `cbrn_protection_respiratory`
- `cbrn_protection_skin`
- `cbrn_protection_antidote`
- `cbrn_protection_decontamination`
- `cbrn_protection_medical`
- `cbrn_protection_warning`

Defaults: missing inputs or a non-chemical class leave the proof missing and return unprotected multipliers.

Outputs:

- `cbrn_action_effective_protection`, 0 through 100
- `cbrn_action_casualty_mult`
- `cbrn_action_disruption_mult`
- `cbrn_action_contamination_mult`
- `cbrn_action_protection_resolved_proof`

Side effects: none. The helper does not infer stockpile or issued coverage and does not consume filters. Stage 2 prepares its six inputs from real equipment and state/force coverage.

Example:

```txt
set_temp_variable = { cbrn_action_agent_class = constant:cbrn_agent_class.nerve }
set_temp_variable = { cbrn_protection_respiratory = 80 }
set_temp_variable = { cbrn_protection_skin = 70 }
set_temp_variable = { cbrn_protection_antidote = 60 }
set_temp_variable = { cbrn_protection_decontamination = 75 }
set_temp_variable = { cbrn_protection_medical = 75 }
set_temp_variable = { cbrn_protection_warning = 65 }
cbrn_calculate_action_protection = yes
```

### Internal protection-calculator helpers

`cbrn_reset_protection_outputs`, `cbrn_set_protection_weights_from_agent_class`, and `cbrn_set_casualty_mult_from_protection` are private steps used by `cbrn_calculate_action_protection`.

Scope: the enclosing effect chain; all working values are temporary.

Inputs: `cbrn_action_agent_class` plus the six protection-layer inputs documented above. The weight helper maps choking, blister, nerve, or incapacitating classes to the centralized six-layer table. The casualty helper reads the resulting effective score and the decontamination/medical support bands.

Defaults: reset returns zero effective protection, neutral casualty/disruption/contamination multipliers, and missing proof. An unrecognized class keeps those fail-closed defaults.

Outputs: temporary layer weights, `cbrn_action_effective_protection`, the agent-specific casualty multiplier, and the public protection outputs/proof written by the wrapper.

Side effects: none. These helpers do not inspect technology, create equipment, consume filters, or mutate a country or state.

Usage example: call only the public wrapper after supplying all six layers; it invokes the three internal helpers in the required order.

```txt
cbrn_calculate_action_protection = yes
```

## cbrn_prepare_chemical_action_record

Validates and calculates the normalized temporary record for one deliberate chemical action. It is the shared route interface, not a payload or consequence effect by itself.

Scope: attacker country.

Required regular event target and proof:

- `cbrn_action_target_state`
- `cbrn_action_target_state_supplied = constant:cbrn_proof.supplied`

Required temporary metadata:

- `cbrn_action_weapon_class`
- `cbrn_action_agent_class`
- `cbrn_action_agent`
- `cbrn_action_delivery_route`
- `cbrn_action_severity`

Nerve use through cylinder, projector, artillery, armored delivery, or air delivery additionally requires `cbrn_action_late_agent_route_authorized = constant:cbrn_proof.supplied`, set only by the mapped late technology/doctrine gate. Nerve Suppression accepts nerve agents only.

Required payload inputs: positive `cbrn_action_payload_required`, positive `cbrn_action_payload_consumed`, and `cbrn_action_payload_consumed_proof`. The proof is valid only after a real CBRN payload-debit helper removes equipment.

Required protection inputs: outputs and proof from `cbrn_resolve_action_target_protection`.

Required release input: positive `cbrn_action_release_efficiency_mult`. Release efficiency is separate from payload consumption: it records the share of consumed payload that the native route reports as released into the intended exposure.

Optional verified condition receipt: an adapter may set positive `cbrn_action_weather_mult`, `cbrn_action_terrain_mult`, `cbrn_action_target_density_mult`, `cbrn_action_command_mult`, `cbrn_action_evidence_control_mult`, and `cbrn_action_context_condemnation_mult`, together with `cbrn_action_forecast_confidence`, `cbrn_action_command_integration`, `cbrn_action_base_friendly_risk`, and `cbrn_action_conditions_resolved_proof`. These modifiers apply only when the complete receipt is verified. A route without the required current-version engine surface leaves the receipt missing; the calculator omits those modifiers and friendly-risk resolution instead of manufacturing neutral values, estimating target conditions, or rejecting an otherwise genuine selected-state release. Immediately before calculation, the public wrapper derives the doctrine Condemnation multiplier from the attacker country's Integrated CBRN Command mastery and clamps it to `0.70` through `1.00`; route adapters cannot select a different doctrine discount.

Defaults: none. Validation is fail-closed. The continuous ordinary-air route returns `unsupported_continuous_air_route`; no neutral condition or idle-aircraft estimator is substituted.

Outputs include `cbrn_action_result`, `cbrn_action_reject_reason`, victim event target/proof when known, payload ratio, clamped release efficiency, dose, disruption, military and civilian death fractions, exposed share, contamination points/duration, medical burden, evidence, attribution, Condemnation base, friendly risk, `cbrn_action_vehicle_sealing_applied`, and source label. The vehicle-sealing proof is set only when the attacker has `vehicle_overpressure_and_sealed_compartments` and the verified route is armored delivery; it reduces friendly crew exposure without changing target harm, evidence, attribution, or Condemnation.

Side effects: no persistent gameplay mutation. Rejected calls return zero consequence outputs. Accepted calls must immediately pass to `cbrn_dispatch_chemical_action_record` before the action context is reset.

Example:

```txt
random_owned_controlled_state = {
	save_event_target_as = cbrn_action_target_state
}
set_temp_variable = { cbrn_action_target_state_supplied = constant:cbrn_proof.supplied }
set_temp_variable = { cbrn_action_weapon_class = constant:cbrn_weapon_class.chemical }
set_temp_variable = { cbrn_action_agent_class = constant:cbrn_agent_class.choking }
set_temp_variable = { cbrn_action_agent = constant:cbrn_agent.chlorine }
set_temp_variable = { cbrn_action_delivery_route = constant:cbrn_delivery_route.cylinder_release }
set_temp_variable = { cbrn_action_severity = constant:cbrn_operation_severity.local }
# The real route adapter must set payload, protection, and release inputs here.
# It may add condition inputs only when a verified engine receipt exists.
cbrn_prepare_chemical_action_record = yes
```

### Internal chemical-action record helpers

The public action-record wrapper owns these private temporary calculators:

| Helper | Purpose and outputs |
| --- | --- |
| `cbrn_reset_action_outputs` | Resets every action result, proof, consequence output, attribution value, vehicle-sealing proof, and source label to its rejected, missing, unknown, or zero default. |
| `cbrn_set_route_profile_from_action` | Maps the validated delivery-route enum to disruption, civilian exposure, contamination, medical burden, evidence, Condemnation, and duration baselines. Unsupported routes retain zero values and are rejected before calculation. |
| `cbrn_set_agent_class_profile_from_action` | Maps the chemical class to disruption, persistence, medical, evidence, Condemnation, duration, and tactical/strategic lethality multipliers. |
| `cbrn_set_chemical_agent_profile_from_action` | Applies the distinct chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, malodor, or behavioral-agent potency, persistence, evidence, and source-profile values. |
| `cbrn_set_action_source_label` | Chooses battlefield, persistent-contamination, strategic-raid, or nerve-suppression source classification from the validated route and severity. |
| `cbrn_set_action_attribution_from_evidence` | Converts the current episode evidence score into unknown, suspected, probable, or confirmed attribution without changing evidence. |
| `cbrn_calculate_chemical_action_outputs` | Combines payload ratio, conditions, protection, route, class, agent, response choices, completed exact CBRN designer traits, offensive doctrine-posture multipliers, Condemnation-only doctrine mitigation, and confirmed-use floors into the normalized action outputs. Theater Contamination raises dose, contamination, and duration; Terminal Hazard raises operational effect, deaths, contamination, duration, and medical saturation while reducing Condemnation before unchanged public-harm floors. Stable Choking Fill lowers choking artillery dose; Persistent Agent Formulation increases blister contamination, duration, and evidence; Standardized Fuzes increases artillery evidence; Sealed Bomb-Bay Interfaces lowers chemical-air friendly risk; Precision Release lowers chemical-air civilian exposure and contamination. The target controller's Respiratory Care lowers choking deaths, Antidote Production lowers nerve-agent deaths, and Mobile Casualty Sorting lowers medical saturation. Lightweight and Long-Range Payload effects live on exact installed rack variants rather than this country-scope calculator. Designer traits never reduce evidence or Condemnation. |

Scope: attacker country/enclosing effect chain. Inputs are the temporary metadata and proof contract documented for `cbrn_prepare_chemical_action_record`. Defaults are fail closed: the reset helper runs first, and missing or invalid inputs leave a rejected record. Outputs are temporary only. Side effects: none. Offensive doctrine postures deliberately increase specified harm outputs; their Condemnation multiplier changes Condemnation only. Evidence, attribution, payload debit, and confirmed-use history remain untouched.

Usage example: route adapters must call the public wrapper, which validates the contract and invokes these helpers in order.

```txt
cbrn_prepare_chemical_action_record = yes
```

## cbrn_apply_state_contamination_delta_internal

Internal state-scope mutation used by the single consequence dispatcher and exact-state decontamination responses.

Inputs: temporary `cbrn_state_contamination_delta` and optional positive `cbrn_state_contamination_duration_input`.

Defaults: no delta means no severity change. A new duration extends to the longer active duration rather than adding a second independent timer.

Outputs: previous/new contamination values and classes in `cbrn_state_previous_contamination_value`, `cbrn_state_previous_contamination_class`, `cbrn_state_new_contamination_value`, and `cbrn_state_new_contamination_class`.

Side effects: updates lazy state variables `cbrn_chemical_contamination`, `cbrn_chemical_contamination_class`, and `cbrn_chemical_contamination_duration_days`; clears them below Trace. Its private `cbrn_refresh_state_contamination_class` step clamps the contamination meter, derives the class thresholds, and clears duration/class data when contamination falls below Trace. It does not register deaths, Air Cleanliness, Condemnation, or a scheduler by itself.

Example:

```txt
event_target:cbrn_action_target_state = {
	set_temp_variable = { cbrn_state_contamination_delta = cbrn_action_contamination_points }
	set_temp_variable = { cbrn_state_contamination_duration_input = cbrn_action_contamination_duration_days }
	cbrn_apply_state_contamination_delta_internal = yes
}
```

## cbrn_apply_state_evidence_delta_internal

Internal state-scope evidence mutation for the single consequence dispatcher and later evidence-resolution actions.

Input: temporary `cbrn_state_evidence_delta`.

Defaults: no input changes nothing.

Outputs: temporary `cbrn_state_attribution_output`; persistent `cbrn_evidence_quality` and `cbrn_attribution_state` when applicable. The private `cbrn_refresh_state_attribution` step clamps accumulated evidence and derives unknown, suspected, probable, or confirmed attribution without changing the evidence score.

Side effects: evidence is clamped to 0 through 100. Values below Suspected remain latent while the public attribution state is cleared. It does not add Condemnation or expose latent responsibility by itself.

Example:

```txt
event_target:cbrn_action_target_state = {
	set_temp_variable = { cbrn_state_evidence_delta = cbrn_action_evidence_points }
	cbrn_apply_state_evidence_delta_internal = yes
}
```

## cbrn_reset_action_context

Invalidates all public chemical-action proof variables and zeroes metadata/outputs after every consumer has finished reading one action record.

Scope: the enclosing effect chain.

Inputs: none.

Defaults: none.

Outputs: action variables reset to their `none`, zero, rejected, or missing-proof constants, including the one-shot dispatch proof and optional evidence-floor override.

Side effects: regular event targets are not manually cleared because they expire with the chain; reset proofs prevent stale targets from being accepted within a reused chain.

Example:

```txt
if = {
	limit = { check_variable = { var = cbrn_action_result value = constant:cbrn_action_result.accepted compare = equals } }
	cbrn_dispatch_chemical_action_record = yes
}
cbrn_reset_action_context = yes
```

## CBRN payload logistics

These country-scope effects are defined in `cbrn_payload_effects.txt`. They keep the strategic-agent, shell-filling, and air-payload ledgers separate and supply `cbrn_action_payload_consumed_proof` only after exact equipment removal. Missing technology, mismatched profile, insufficient stock, an unsupported route, or an in-progress line change fails closed and creates no exposure.

### Public payload effects

| Effect | Inputs, defaults, outputs, and side effects |
| --- | --- |
| `cbrn_initialize_payload_logistics` | Country scope. No inputs. Initializes persistent shell and air profile variables to `cbrn_agent.none`; creates no equipment. |
| `cbrn_set_default_payload_requirement_for_action` | Country/enclosing action chain. Reads `cbrn_action_delivery_route`; writes the centralized positive route cost and resets consumed amount/proof. Unknown routes remain at zero. |
| `cbrn_try_debit_action_payload` | Country scope. Requires validated chemical metadata, unlocked agent, ready matching profile, and exact stock at least equal to `cbrn_action_payload_required`. Debits the exact strategic-agent model, shared shell lot, or class-specific air lot and then writes consumed amount/proof. A failed gate removes nothing. |
| `cbrn_change_shell_filling_profile` | Country scope. Requires temporary `cbrn_requested_payload_agent`, its unlock, a different current profile, and no active shell reconfiguration. Applies the centralized switch loss to prepared shell stock, stores the new agent, sets the timed line-change flag, and returns `cbrn_payload_profile_change_accepted`. Completed Rapid Front Distribution multiplies the delay by 0.80 before rounding. |
| `cbrn_change_air_payload_profile` | Same contract for the air line. Wastage is removed only from the old class-specific air payload stock and the longer air reconfiguration delay is applied. Completed Controlled Dispersal multiplies that delay by 1.15 before rounding. |
| `cbrn_convert_selected_agent_to_shell_lots` | Country scope. Requires a selected ready shell profile and temporary positive `cbrn_payload_conversion_requested`. Clamps the input to exact selected-agent stock, debits that stock, applies the class-specific recovery ratio, adds shell lots, and returns completed proof plus actual input/output. |
| `cbrn_convert_selected_agent_to_air_payload_lots` | Same conversion contract for the selected air agent. Requires Chemical Air Interdiction and adds only the matching choking, blister, nerve, or incapacitating air lot. |
| `cbrn_migrate_legacy_payload_stockpiles` | Country scope, idempotent. Converts each legacy cylinder and experimental bomb model to its exact strategic-agent lot at the centralized save-preserving recovery ratio, selects deterministic initial profiles from recovered stock, and sets one migration flag. It must run only after every legacy consumer has moved to the shared pipeline. |

### Internal payload helpers

| Helper | Private responsibility |
| --- | --- |
| `cbrn_debit_strategic_agent_lots_internal` | Removes the exact chlorine, phosgene, mustard, lewisite, tabun, sarin, soman, malodor, or behavioral lot selected by action metadata. |
| `cbrn_debit_shell_lots_internal` / `cbrn_debit_air_payload_lots_internal` | Remove the route's shell lot or exact class-specific air lot after public stock validation. |
| `cbrn_remove_shell_profile_wastage_internal` / `cbrn_remove_air_profile_wastage_internal` | Apply bounded prepared-stock losses during profile changes without touching strategic agent stock. |
| `cbrn_read_selected_shell_agent_stock_internal` / `cbrn_read_selected_air_agent_stock_internal` | Read exact selected strategic-agent availability for conversion; unknown profiles return zero. |
| `cbrn_debit_selected_shell_agent_stock_internal` / `cbrn_debit_selected_air_agent_stock_internal` | Remove the exact conversion input selected by the persistent profile. |
| `cbrn_set_shell_conversion_recovery_internal` | Selects the choking, blister, nerve, or incapacitating shell-filling recovery ratio. Completed Stable Choking Fill multiplies chlorine or phosgene recovery by 1.05 and clamps the result to the valid zero-through-one range. |
| `cbrn_add_selected_air_payload_output_internal` | Adds only the class-specific air payload output that matches the selected agent. |

Example:

```txt
cbrn_reset_action_context = yes
set_temp_variable = { cbrn_action_delivery_route = constant:cbrn_delivery_route.artillery_fire_plan }
# Set the remaining static action metadata.
cbrn_set_default_payload_requirement_for_action = yes
cbrn_try_debit_action_payload = yes
```

## CBRN designer effects

These effects are defined in `cbrn_designer_effects.txt`. Country-scope module helpers grant hidden, unresearchable technologies that enable exact agent-specific Lightweight, Long-Range, or combined aircraft rack modules. State-scope helpers refresh only the exact contaminated state supplied by an existing consequence or state-control callback. No helper creates equipment, selects a state, or starts a periodic country scan.

| Effect | Inputs, defaults, outputs, and side effects |
| --- | --- |
| `cbrn_unlock_lightweight_aerosol_modules_for_available_agents` | Country scope. Intended for the Lightweight Payload Assemblies trait `on_complete` block. It checks each regular agent technology and both special projects, then grants only the corresponding hidden Lightweight module technologies. Missing agent access does nothing. The caller supplies the just-completed trait proof. |
| `cbrn_unlock_long_range_aerosol_modules_for_available_agents` | Country scope. Intended for the Long-Range Payload trait `on_complete` block. It grants exact Long-Range modules for available agents. When Lightweight Payload Assemblies was also completed, it additionally grants exact combined modules. Missing agent access does nothing. |
| `cbrn_sync_aerosol_designer_module_unlocks` | Country scope, idempotent. Reads both completed MIO traits and reruns the relevant direction helpers. Each chlorine, phosgene, mustard, lewisite, Tabun, Sarin, and Soman technology calls this after research so a trait completed earlier cannot bypass the agent gate. |
| `cbrn_unlock_malodor_aerosol_modules_after_project` | Country scope. Called only by the completed Malodor project output. Reads completed designer traits and grants the exact Malodor variant technologies without depending on whether the project-completed trigger has updated during its own output block. |
| `cbrn_unlock_behavioral_aerosol_modules_after_project` | Same contract for the completed Behavioral-Agent project and its exact rack variants. |
| `cbrn_designer_refresh_contaminated_state_vehicle_attrition` | State scope. Recomputes the legacy contamination modifier's truck-attrition input from the state's exact contamination strength and the current controller's completed Vehicle Recovery Teams trait. It is called by contamination application and the exact state-control-change hook, then forces the modifier to refresh. |
| `cbrn_designer_apply_blister_continuing_death_treatment` | State scope inside the existing chemical-contamination death pass. Requires an active contamination modifier, a persisted blister-agent class, and a current controller with Burn Treatment. It multiplies only the already-prepared continuing-death value; initial release deaths and non-blister contamination are unchanged. |

The hidden technology family is defined in `cbrn_aerosol_module_variant_technologies.txt`. Separate technology IDs preserve an exact AND gate between one agent and one physical rack direction. The module variants are defined in `chemical_air_bomb_variant_modules.txt`: Lightweight changes only that rack's weight, agility burden, and payload volume; Long-Range changes only the installed rack's range and maneuver burden; combined modules compose both. No helper applies a country modifier, ordinary-aircraft bonus, strategic dose proxy, friendly-risk proxy, or periodic unlock pulse.

Example from an agent technology:

```txt
on_research_complete = {
	cbrn_sync_aerosol_designer_module_unlocks = yes
}
```

## CBRN selected-state chemical-air raid adapter

`cbrn_resolve_chemical_air_raid_reservation` is the country-scope reservation effect in `cbrn_chemical_raid_effects.txt`. Ordinary selected-state chemical air raids reserve exactly 120 units of the matching choking, blister, nerve, or incapacitating air-payload archetype, while strategic chemical rocket raids reserve exactly 240 nerve-class units through native `essential_equipment`. Native collection is the debit; the helper must not call `cbrn_try_debit_action_payload` a second time.

Required temporary inputs are exact `cbrn_raid_agent`, one `cbrn_raid_engine_outcome` code for failure, limited success, success, or critical success, and optional `cbrn_raid_route` set to `strategic_chemical_raid` for the rocket route. The effect first resets the shared action context, copies the exact raid agent into it, records the selected route, derives the agent class, splits the engine failure result evenly between accepted Aborted and Failed outcomes, selects the centralized consumption and intended-dose bands, refunds the exact unused class-specific model, and records positive net consumption with native-reservation proof. Completed Controlled Dispersal narrows only the partial dose band to 0.45-0.60 and the catastrophic band to 1.15-1.30; payload consumption is unchanged. Partial, successful, and catastrophic results additionally return a positive release-efficiency multiplier and release proof. Aborted and failed results return zero release efficiency and no release proof.

Defaults: fail closed. An invalid agent or engine result leaves missing reservation proof and performs no refund. Outputs are temporary `cbrn_raid_result`, consumption/dose values, refund, reservation proof, release proof, and the shared action payload/release fields. Side effects are limited to returning unused payload stock; this effect does not select weather or terrain, resolve protection, contaminate a state, create deaths, add evidence, or apply Condemnation.

Internal helpers map the agent class, map native outcomes, select consumption/dose, and refund the exact model. They are not route entry points.

Example inside a native raid actor-country outcome block:

```txt
set_temp_variable = { cbrn_raid_agent = constant:cbrn_agent.sarin }
set_temp_variable = { cbrn_raid_engine_outcome = constant:cbrn_chemical_raid_engine_outcome.limited_success }
cbrn_resolve_chemical_air_raid_reservation = yes
if = {
	limit = { cbrn_chemical_air_raid_reservation_is_resolved = yes }
	# Continue through the exact-state condition and protection adapter.
}
```

## cbrn_resolve_chemical_air_raid_outcome

`cbrn_resolve_chemical_air_raid_outcome` is the public country-scope selected-state adapter for the active chemical air and strategic chemical rocket raid identifiers. The nine ordinary air wrappers are `cbrn_resolve_chemical_air_raid_chlorine_outcome`, `cbrn_resolve_chemical_air_raid_phosgene_outcome`, `cbrn_resolve_chemical_air_raid_mustard_outcome`, `cbrn_resolve_chemical_air_raid_lewisite_outcome`, `cbrn_resolve_chemical_air_raid_tabun_outcome`, `cbrn_resolve_chemical_air_raid_sarin_outcome`, `cbrn_resolve_chemical_air_raid_soman_outcome`, `cbrn_resolve_chemical_air_raid_malodor_outcome`, and `cbrn_resolve_chemical_air_raid_behavioral_outcome`. Strategic Sarin and Soman rocket outcomes use the Sarin or Soman wrapper with `cbrn_raid_route = strategic_chemical_raid`.

Required native raid inputs are `var:actor_country`, `var:target_state`, `var:victim_country`, and one engine outcome code. The adapter saves those scopes as regular event targets, resolves native reservation and salvage, resolves the target's military and civilian protection, records a supplied selected-state target proof, and derives release efficiency from the native partial, success, or catastrophic result. The installed raid surface exposes no verified live target-weather or state-terrain trigger, so the adapter supplies no environmental condition receipt and the shared calculator omits those optional modifiers.

Release-bearing results call `cbrn_prepare_chemical_action_record` and then `cbrn_dispatch_chemical_action_record` exactly once. If target, protection, release, or any other required shared proof fails, the adapter converts the result into a no-release attempt and calls `cbrn_dispatch_failed_chemical_air_raid_attempt`. Aborted and failed native results always use the no-release path. No branch searches another state, contaminates a region, infers idle aircraft activity, or refunds a failed native reservation.

Example from a native raid outcome:

```txt
hidden_effect = {
	set_temp_variable = { cbrn_raid_engine_outcome = constant:cbrn_chemical_raid_engine_outcome.success }
	cbrn_resolve_chemical_air_raid_sarin_outcome = yes
}
```

## cbrn_dispatch_failed_chemical_air_raid_attempt

Records one resolved Aborted or Failed chemical-air raid attempt without fabricating a release. This public country-scope effect lives in `cbrn_chemical_raid_effects.txt`.

Required inputs: a successful `cbrn_resolve_chemical_air_raid_reservation` result with positive native payload consumption, an Aborted or Failed no-release result, supplied exact-target proof, and regular event target `cbrn_action_target_state`.

Defaults: fail closed. Missing reservation proof, a release-bearing outcome, missing target proof, zero payload consumption, or an already supplied attempt-dispatch proof produces no mutation. The reservation helper and `cbrn_reset_action_context` invalidate the one-shot proof before a later attempt.

Outputs: supplied `cbrn_raid_attempt_dispatch_proof`, actual state evidence applied after the failed-aircraft floor, cumulative attribution, and separate actor/state attempted-operation history. Aborted attempts add a small latent evidence value; Failed attempts establish at least the centralized aircraft-wreckage evidence floor. The same contract applies to ordinary air and strategic rocket raid routes.

Side effects: schedules the existing targeted state evidence-decay job, adds chemical Condemnation at the cumulative visibility level, and appends one exact no-release forensic row containing the native Aborted or Failed result and the liability created by that attempt. Integrated CBRN Command modifies only the attempt's Condemnation base. The one-shot no-release proof prevents the shared Condemnation helper from recording repeat use, a non-use-pledge breach, a stockpile-restriction breach, recent weapon use, or `used_unconventional_weapon`. The explicit no-release row can expose responsibility for the attempt but cannot register confirmed weapon use, treaty callbacks, or retaliation authority. This path does not calculate exposure, damage units, create civilian or military deaths, contaminate the target, add medical saturation, consume masks or filters, or grant chemical-use achievements.

Example after native reservation resolution and exact target preservation:

```txt
if = {
	limit = { cbrn_chemical_air_raid_result_has_no_release = yes }
	cbrn_dispatch_failed_chemical_air_raid_attempt = yes
}
cbrn_reset_action_context = yes
```

## cbrn_dispatch_chemical_action_record

Consumes one accepted chemical action record exactly once. The public country-scope effect lives in `cbrn_consequence_effects.txt`.

Required inputs: an accepted result from `cbrn_prepare_chemical_action_record`, positive consumed payload with supplied debit proof, supplied exact-target proof, and regular event target `cbrn_action_target_state`. Route adapters may optionally set `cbrn_action_evidence_floor_override` for an engine-proven outcome such as recovered aircraft wreckage. The override can raise evidence only.

Defaults: fail closed. A rejected record, missing target, missing payload proof, zero consumption, or an already supplied `cbrn_action_dispatch_proof` produces no mutation. Continuous ordinary-air missions never become accepted records.

Outputs: supplied one-shot dispatch proof, raw exact civilian deaths returned by the shared Deaths helper, actual evidence delta after absolute floors, cumulative attribution, and inspectable actor/state history variables.

Side effects:

- applies dynamic `damage_units` organisation and strength ratios only to armies in the exact selected state; hostile and bounded friendly/blowback limits are separate;
- lets the existing country-casualty tracker record exact engine military losses instead of inventing an estimated death count;
- removes civilian population and writes one immediate chemical Deaths record from the calculated exact fraction;
- accumulates CBRN contamination and updates the canonical `chem_state_contamination` presentation modifier through the state-owned chemical helper; it does not call the retired legacy contamination or continuing-death helper;
- adds medical saturation, consumes civilian and military mask/filter stocks, applies cumulative evidence and attribution floors, and schedules state-scoped expiry/recovery/decay events;
- applies Condemnation with cumulative visibility, raw civilian deaths, contamination, severity, victim, strategic/mass-casualty floors, sanctions, and confirmed treaty breach;
- records permanent confirmed-use history. Doctrine can reduce only the Condemnation base before the public floor; it never changes the other outputs;
- applies first-exposure multipliers to the affected state and a short defender adaptation idea. Prior world use and real protection reduce this shock without benefiting the attacker.

Internal helpers are `cbrn_dispatch_set_source_and_context`, `cbrn_dispatch_set_evidence_floor`, `cbrn_dispatch_apply_first_exposure_shock`, `cbrn_dispatch_apply_unit_damage`, `cbrn_dispatch_apply_mask_losses`, `cbrn_dispatch_apply_state_consequences`, `cbrn_dispatch_apply_condemnation`, and `cbrn_dispatch_record_actor_history`. They share the validated temporary record and must not be called directly by route adapters.

The internal `cbrn_bind_action_victim_country` helper binds the selected state's controller for ordinary battlefield and strategic delivery. For the occupation-only `nerve_suppression` route it binds the selected state's owner, so evidence, retaliation, and Condemnation name the occupied population's country rather than the occupying actor.

Example:

```txt
cbrn_prepare_chemical_action_record = yes
if = {
	limit = { check_variable = { var = cbrn_action_result value = constant:cbrn_action_result.accepted compare = equals } }
	cbrn_dispatch_chemical_action_record = yes
}
cbrn_reset_action_context = yes
```

## CBRN equipment snapshots and protection resolution

### cbrn_initialize_state_protection

Initializes one state's persistent civilian respirator ledger.

Scope: state. Inputs: none. Defaults: zero model crates, zero fitting points and replacement demand, and full unused-filter condition. Outputs: initialized and clamped `cbrn_civilian_mask_*` variables. Side effects: no equipment is created or consumed.

Example:

```txt
FROM = { cbrn_initialize_state_protection = yes }
```

### cbrn_refresh_country_mask_snapshot

Rebuilds the current country's inspectable respirator snapshot from real stockpile models, explicit military-issue ledgers, equipment actually in divisions, deployed manpower, filter condition, and aggregate civilian distribution.

Scope: country. Inputs: live equipment and persistent ledgers. Defaults: absent ledgers are initialized to zero. Outputs include reserve crates by model, `cbrn_military_mask_requirement`, coverage, respiratory/skin/warning protection, the respiratory-and-skin `cbrn_military_blister_mask_protection` composite, profile-specific `cbrn_ai_military_mask_coverage_target` and `cbrn_ai_mask_reserve_target_crates`, and `cbrn_mask_total_accounted`. Side effects: only derived persistent snapshot variables are rewritten; no stock moves.

Example:

```txt
cbrn_refresh_country_mask_snapshot = yes
```

### chem_set_equipment_backed_mask_reduction

Adapts the shared field-army protective-equipment snapshot to the legacy cylinder-ability combat modifiers. It replaces the former technology-only 25/50/75-percent lookup.

Scope: army leader. Inputs: the owner country's refreshed `cbrn_military_respiratory_protection` and `cbrn_military_skin_protection`; temporary `chem_mask_blister_bonus` selects the blister composite when positive. Defaults: missing snapshot values produce zero mask mitigation. Output: temporary `chem_mask_reduction_fraction`, using the equipment-backed score directly as a percentage and clamped from zero to the centralized 75-percent legacy ceiling. Side effects: none; it neither creates nor consumes equipment.

The leader-daily preview adapter refreshes the owning country's snapshot once before rebuilding all cylinder previews. Each ability activation refreshes again and rebuilds its selected preview so deployed manpower, issued models, divisional equipment, and filter condition are current at use time.

Example:

```txt
set_temp_variable = { chem_mask_blister_bonus = 1 }
chem_set_equipment_backed_mask_reduction = yes
```

### cbrn_refresh_state_civilian_mask_snapshot

Rebuilds one state's effective civilian protection from population, distributed model crates, fitting points, filter condition, registration, civil-defence institutions, exact-state alert choices, and the controller's medical/decontamination capacity. Fitting- and filter-adjusted coverage continues to measure the share of the population reached; each respiratory, skin, or warning protection component uses the lower of that coverage and the weighted model-quality score. Partial issue therefore remains valuable while full basic issue cannot exceed its accepted 55-point respiratory ceiling.

Scope: state. Inputs: persistent state ledger and current controller. Defaults: zero coverage when population or usable stock is zero. Outputs include raw and effective coverage, respiratory/skin/warning protection, decontamination and medical protection, and `cbrn_civilian_mask_effective_coverage`. Side effects: only derived state variables are rewritten.

Example:

```txt
event_target:cbrn_action_target_state = {
	cbrn_refresh_state_civilian_mask_snapshot = yes
}
```

### cbrn_resolve_action_target_protection

Resolves both military and civilian protection for the exact `cbrn_action_target_state`, then runs the shared agent-class calculator for each population.

Scope: attacker-country action chain. Required input: a valid regular event target `cbrn_action_target_state` plus `cbrn_action_agent_class`. Defaults: invalid or missing protection data leaves the final proof missing. Outputs: military and civilian effective protection, casualty/disruption/contamination multipliers, and `cbrn_action_protection_resolved_proof`. Side effects: refreshes only target/controller snapshot variables and consumes no equipment.

Example:

```txt
cbrn_resolve_action_target_protection = yes
```

## CBRN military issue and state distribution

### cbrn_issue_requested_masks_to_military

Debits a requested number of real respirator crates, preferring sealed, advanced, improved, basic, then reconditioned models, and transfers them to non-reclaimable military-issue ledgers.

Scope: country. Input: temporary `cbrn_mask_issue_requested_crates`. Defaults: absent, negative, or unavailable stock produces zero issue. Outputs: temporary completed/remaining amounts and refreshed military coverage. Side effects: removes real equipment, updates model-specific issue ledgers and weighted filter condition, and reduces existing replacement demand.

Example:

```txt
set_temp_variable = { cbrn_mask_issue_requested_crates = 500 }
cbrn_issue_requested_masks_to_military = yes
```

### cbrn_issue_masks_to_field_army

Convenience country effect that requests one centrally tuned increment of uncovered deployed-army need and calls `cbrn_issue_requested_masks_to_military`.

Scope: country. Inputs: current deployed manpower and stock. Defaults: zero issue when there is no uncovered requirement. Output/side effects: those of the underlying issue helper.

### cbrn_distribute_requested_masks_to_state

Population-scales an exact state's requested civilian distribution, measures its remaining effective-coverage gap, grosses that gap up for the fitting and filter quality of the new issue, applies urban, infrastructure, combat, occupation, reserve, registration, civil-defence, applied-registration-technology, and simplified-filter cost/effectiveness modifiers, then debits the controller's real models oldest-first.

Scope: state. Required temporary inputs: effective target `cbrn_distribution_target_fraction`, `cbrn_distribution_base_cost_mult`, fitting-quality `cbrn_distribution_effectiveness_mult`, and percent filter condition `cbrn_distribution_new_filter_condition`. Defaults: inputs are clamped; a zero fitting or filter factor produces no useful distribution. Outputs: consumed stock, usable crates, fitting points, weighted filter condition, effective coverage, and remaining state demand. Side effects: the public wrapper binds the controller as both the real stock source and aggregate-ledger country, removes equipment from that country, updates model-specific state and controller aggregate ledgers, and never creates reclaimable national stock. Existing raw crates do not suppress a valid request when poor fitting or exhausted filters leave effective coverage below target.

Example:

```txt
set_temp_variable = { cbrn_distribution_target_fraction = 0.50 }
set_temp_variable = { cbrn_distribution_base_cost_mult = 1 }
set_temp_variable = { cbrn_distribution_effectiveness_mult = 1 }
set_temp_variable = { cbrn_distribution_new_filter_condition = 100 }
cbrn_distribute_requested_masks_to_state = yes
```

### cbrn_distribute_requested_external_masks_to_state

Uses the same population, fitting, filter, model-order, and effective-coverage transaction for protective aid supplied by a foreign country.

Scope: state. Required regular event target: `cbrn_distribution_external_supplier`, pointing to the actual donor country. Required temporary inputs are the same four distribution inputs as `cbrn_distribute_requested_masks_to_state`. Defaults: a missing donor, missing controller, empty donor stock, or zero useful delivery fails closed. Output: temporary `cbrn_external_distribution_proof`, plus the normal consumed and usable crate outputs. Side effects: debits the donor's real oldest-first stock while crediting the exact state's model ledgers and its current controller's aggregate distributed-stock ledgers. This split preserves later state-control transfer accounting and never treats the donor as the state controller.

Example:

```txt
save_event_target_as = cbrn_distribution_external_supplier
event_target:cbrn_occupation_target_state = {
	set_temp_variable = { cbrn_distribution_target_fraction = 0.35 }
	set_temp_variable = { cbrn_distribution_base_cost_mult = 1 }
	set_temp_variable = { cbrn_distribution_effectiveness_mult = 1 }
	set_temp_variable = { cbrn_distribution_new_filter_condition = 100 }
	cbrn_distribute_requested_external_masks_to_state = yes
}
```

### cbrn_distribute_priority_masks_to_state, cbrn_distribute_full_masks_to_state, and cbrn_distribute_emergency_masks_to_state

These state-scope wrappers supply the accepted 50-percent priority, 95-percent full, or 35-percent effective emergency targets. The shared helper derives the larger raw emergency allocation needed after reduced fitting quality and degraded filter condition; emergency issue also applies the 0.60 improvised baseline and 1.30 wastage. Defaults and side effects are those of `cbrn_distribute_requested_masks_to_state`.

### cbrn_debit_mask_stockpile_oldest_first

Debits a requested amount from real country stock in reconditioned, basic, improved, advanced, then sealed order.

Scope: country. Input: temporary `cbrn_mask_stock_debit_requested`. Defaults: request is clamped to available stock and zero. Outputs: `cbrn_mask_stock_debit_completed` and remaining request. Side effects: model-specific stock removal and snapshot refresh.

## CBRN filters, losses, reconditioning, and transfer

### cbrn_replace_military_mask_filters and cbrn_replace_state_civilian_mask_filters

Restore worn military or exact-state civilian filters using real national respirator crates. The state helper additionally scales cost with current chemical contamination. `rapid_filter_replacement` reduces the real replacement-crate debit by the centralized 30-percent efficiency gain in either scope.

Scope: country for military; state for civilian. Inputs: current issued/distributed crates and filter condition. Defaults: no worn filters or no reserve causes no restoration. Outputs: proportional restored condition and refreshed coverage. Side effects: oldest-first stock debit and reduced replacement demand.

### cbrn_apply_military_mask_loss and cbrn_apply_state_civilian_mask_loss

Apply explicit exposure/storage loss to issued military or distributed civilian stock. `military_filter_standardization` reduces both crate loss and filter-condition loss by the accepted 15 percent for military and civilian ledgers. Controlled Retaliation Doctrine and Mask Discipline apply their separate military-only consumption multipliers; they do not reduce civilian loss or exposure consequences.

Scope: country or state respectively. Inputs: temporary `cbrn_mask_loss_fraction` and `cbrn_mask_condition_loss`. Defaults: values are clamped to safe ranges. Outputs: model ledgers, filter condition, and replacement demand. Side effects: civilian loss also updates the controller's aggregate distributed totals; no lost equipment returns to stock.

Military-accounting boundary: the snapshot counts real model equipment already deployed in divisions through the documented `num_equipment_in_armies@<model>` read and combines it with the separate, non-reclaimable military-issue ledgers. `cbrn_apply_military_mask_loss` can debit the latter and degrade their shared filter condition, but the installed native script surface does not expose a current-version effect that removes one selected respirator model directly from deployed divisions. The system therefore records military issue loss honestly and never pretends that a stockpile debit removed fielded equipment; it also does not introduce a hidden unit estimator or synthetic deployed-equipment damage ledger.

### cbrn_apply_standard_chemical_mask_losses, cbrn_apply_persistent_chemical_mask_losses, and cbrn_apply_strategic_raid_mask_losses

State-scope wrappers selecting the centralized ordinary exposure, persistent-agent, or strategic-raid loss profile before calling `cbrn_apply_state_civilian_mask_loss`.

### cbrn_recondition_damaged_masks

Converts the national damaged/rejected-mask cache and replacement ledger into low-reliability `gas_mask_equipment_reconditioned` at the configured recovery ratio and per-action cap.

Scope: country. Inputs: `cbrn_reconditionable_mask_cache` and `cbrn_mask_replacement_demand`. Defaults: no source material produces no output. Output: temporary `cbrn_recondition_recovered`. Side effects: consumes source ledgers and adds real non-buildable reconditioned equipment.

### cbrn_apply_annual_mask_storage_loss

Applies model-specific annual warehouse losses, reduced by an established national reserve.

Scope: country. Inputs: current stock by model. Defaults: empty stock produces no loss. Outputs: total storage loss and replacement demand. Side effects: removes real stock and refreshes the snapshot.

### cbrn_transfer_state_civilian_mask_ledger

Transfers distributed civilian protection after `on_state_control_changed` without refunding either controller.

Scope: transferred state. Required regular event targets: `cbrn_old_state_controller` and `cbrn_new_state_controller`. Defaults: the caller only invokes it for a non-empty state ledger. Outputs: surviving state stock and controller aggregate totals. Side effects: clears projects and exact-alert responses, removes their dynamic modifiers, applies turnover/occupation survival and filter loss, charges lost stock to replacement demand, and moves aggregate ownership.

### cbrn_start_protection_maintenance_job

Starts one self-scheduled annual country maintenance event if no job is active.

Scope: country. Inputs: none. Defaults: repeated calls are idempotent through `cbrn_protection_maintenance_active`. Side effects: schedules `cbrn_protection.1` after the centralized annual interval. It creates no all-country periodic pulse.

## CBRN protection decision effects

### cbrn_debit_requested_support_equipment and cbrn_debit_requested_train_equipment

Country-scope bounded debits. Inputs are `cbrn_support_equipment_debit_requested` or `cbrn_train_equipment_debit_requested`; missing/negative requests become zero. Outputs are the matching `*_debit_completed` temporary variables. Side effects: removes only stock actually available.

### National project begin/complete effects

The following effects are paired decision handlers:

| Effects | Purpose and side effects |
| --- | --- |
| `cbrn_begin_national_respirator_reserve` / `cbrn_complete_national_respirator_reserve` | Debits support equipment, establishes the program/reserve, raises readiness, and starts maintenance. |
| `cbrn_begin_population_registration` / `cbrn_complete_population_registration` | Debits support equipment and manpower, applies population-fitting loss, establishes fitting/civil-defence flags only when masks remain, raises readiness, and records rejected stock for reconditioning. |
| `cbrn_begin_field_army_mask_issue` / `cbrn_complete_field_army_mask_issue` | Debits support equipment, then runs real field-army issue. |
| `cbrn_begin_mask_reconditioning` / `cbrn_complete_mask_reconditioning` | Debits support equipment, recovers reconditioned crates, and may fire the weighted defective-batch event. |
| `cbrn_begin_civilian_mask_industry_conversion` / `cbrn_complete_civilian_mask_industry_conversion` | Debits support equipment and converts the timed factory burden into a tuned basic-mask batch. |
| `cbrn_begin_simplified_filter_program` / `cbrn_complete_simplified_filter_program` | Debits support equipment, adds a basic batch, and starts a timed low-cost/lower-effectiveness filter program. |

Scope: country. Inputs/defaults are the real decision gates and centralized constants; direct calls bypass political-power/factory costs and therefore should remain inside the matching decisions. Outputs are persistent flags, stock, readiness, and maintenance state.

Example:

```txt
hidden_effect = { cbrn_begin_national_respirator_reserve = yes }
```

### State project begin/complete effects

`cbrn_begin_state_protection_project` and `cbrn_end_state_protection_project` own the timed exact-state project lock. `cbrn_complete_priority_state_distribution`, `cbrn_complete_full_state_distribution`, `cbrn_complete_emergency_state_distribution`, `cbrn_complete_occupied_state_distribution`, and `cbrn_complete_state_filter_replacement` call the corresponding real allocation/filter helper and cleanup. Emergency completion additionally applies its timed congestion modifier; occupied completion changes resistance/compliance only after attempting real distribution.

Scope: state. Input for begin: `cbrn_project_duration_days`. Defaults: duration is clamped. Side effects: state flags/modifiers and real controller stock consumption.

### cbrn_resolve_defective_reconditioned_batch

Removes the configured fraction of the recorded reconditioned batch, adds replacement demand, lowers readiness, and clears the event ledger.

Scope: country. Input: persistent `cbrn_reconditioned_batch_size`. Defaults: no recorded batch does nothing. Output: refreshed stock snapshot. Side effects: real reconditioned stock loss.

### cbrn_export_masks_to_protection_partner, cbrn_import_masks_from_protection_partner, and cbrn_license_respirator_design_from_partner

Country-scope procurement handlers using regular event target `cbrn_protection_trade_partner`. Invalid or stale partners fail closed. Export accepts a faction partner or exact humanitarian-carve-out recipient, sends a real 500-crate family shipment, records bilateral aid totals and recipient opinion, and gives a small capped decay credit only when the exporter already follows a verified Condemnation-compliance path; offense history is unchanged. Import remains restricted to an allied supplier, sends real partner stock to the caller, and marks the supplier with a timed allied-request production signal. Licensing grants one gas-mask research bonus from an eligible allied partner. All successful paths refresh relevant readiness and maintenance state.

## CBRN exact-state raid response adapter

### cbrn_calculate_state_raid_response_costs

State-scope population calculator for hospital/utility masks and support equipment, plus shelter support equipment and trains. Costs are clamped to centralized minima/maxima and stored as persistent state variables for decision display.

### cbrn_register_exact_state_chemical_raid_alert

Fail-closed state-scope public adapter for a verified current-version raid/operation hook.

Required temporary proof: `cbrn_exact_state_alert_verified = constant:cbrn_proof.supplied`. Optional input: `cbrn_raid_alert_duration_days`, clamped to 1Ã¢â‚¬â€œ30 days and defaulting to 7. Outputs: exact-state alert flag and response costs. Side effects: clears stale response choices before opening the new alert. It does not infer aircraft activity, create contamination, or estimate a continuous mission.

Example:

```txt
event_target:raid_target_state = {
	set_temp_variable = { cbrn_exact_state_alert_verified = constant:cbrn_proof.supplied }
	set_temp_variable = { cbrn_raid_alert_duration_days = 5 }
	cbrn_register_exact_state_chemical_raid_alert = yes
}
```

### cbrn_clear_exact_state_chemical_raid_alert

State-scope explicit alert cleanup. It clears only `cbrn_chemical_raid_alert_active`; timed response modifiers retain their own durations unless state control changes.

### Exact-state response effects

`cbrn_apply_hospital_utility_protection` and `cbrn_apply_civilian_shelter_movement` recalculate and debit their population-scaled real mask/support/train costs before setting timed protective flags/modifiers. `cbrn_apply_chemical_alarm` creates warning protection plus factory/movement disruption. `cbrn_apply_industrial_continuity_order` preserves local output while marking the shared exposure pipeline to increase civilian exposure. Missing equipment prevents the protected effects from being set.

## CBRN starting protection profiles

### cbrn_apply_starting_mask_profile

Applies one accepted 1936 country profile from temporary inputs: basic/improved stock, military issue target, already-issued civilian share, registration proof, and program-profile enum.

Scope: country. Required temporary inputs: `cbrn_starting_mask_basic`, `cbrn_starting_mask_improved`, `cbrn_starting_military_issue_target`, `cbrn_starting_civilian_distribution_target`, `cbrn_starting_registration_proof`, and `cbrn_starting_program_profile`. Defaults: the static caller supplies every value. Outputs: technology, exact tuned starting crates, reserve/registration flags, readiness, actual manpower-scaled military issue, actual population-scaled distribution across controlled core states, and maintenance scheduling. `cbrn_starting_civilian_distribution_target` is the share already issued at the 1936 bookmark, not the matrix's eventual civilian-coverage target; undistributed crates remain in the national reserve. Military targets above 100 percent represent replacement, training, and mobilization issue; protection remains capped while the extra issued ledger is retained. All issue and distribution are stock-limited, so unmet target demand creates no equipment. Side effects: a bounded one-time owned-state loop for that country; no periodic pulse.

### cbrn_apply_starting_imported_mask_profile

Country-scope wrapper for an imported emergency reserve. It sets the temporary import-only flag, calls `cbrn_apply_starting_mask_profile`, and clears the flag in the same effect chain. The country receives its real tuned crates, issue and distribution ledgers, reserve flag, readiness contribution, maintenance job, and profile-aware AI classification, but it does not receive free `basic_gas_masks` technology or the `cbrn_program_established` flag. Improved-mask technology is still granted only when the accepted profile contains a positive improved-mask stock.

### chaosx_apply_starting_cbrn_mask_profiles

Static startup dispatcher for the 30 explicitly mapped domestic-program tags plus imported emergency-reserve profiles for China, the Chinese regional powers, Manchukuo, Brazil, Argentina, Mexico, and Chile. It assigns all temporary inputs and calls the domestic or imported wrapper per existing country. Exact totals are gameplay tuning inside accepted historical bands; relative preparedness and confidence, not literal inventory certainty, control the profiles. Britain has the largest reserve and strongest starting civilian share. Imported profiles model access to crates without fabricating domestic respirator-production capability.

Example:

```txt
chaosx_apply_starting_cbrn_mask_profiles = yes
```

## CBRN occupation and nerve-suppression effects

These subsystem-specific effects live in `cbrn_occupation_effects.txt`. They are not part of the generic dynamic-effect library because their exact-state record, occupation-law, and evidence-row contracts are used only by the occupation CBRN surface.

### Authorization, law, and protective-aid effects

- `cbrn_occupation_authorize_coercive_security` and `cbrn_occupation_authorize_protected_administration` recheck their exact institutional gates and set only their named authorization flags.
- `cbrn_occupation_set_coercive_security_state`, `cbrn_occupation_set_protected_administration_state`, and `cbrn_occupation_clear_state_policy` are state-scoped law adapters for an exact occupied state.
- `cbrn_occupation_execute_external_protective_aid` is country scoped and requires the caller to bind `cbrn_occupation_target_state`. It binds the donor as `cbrn_distribution_external_supplier`, invokes the external mask transaction in the exact state, records consumed and delivered crates, updates donor and recipient history, and grants a bounded opinion record. Missing stock, target, controller, or distribution gap produces no equipment and no completion proof.

### Nerve-suppression transaction

`cbrn_occupation_execute_nerve_suppression` is country scoped. Required inputs are the regular event target `cbrn_occupation_target_state`, `cbrn_occupation_requested_agent` set to Sarin or Soman, and every exact condition variable required by `cbrn_occupation_action_conditions_are_supplied`. The target must retain CBRN Coercive Security, resistance, control, war ownership, a ready detachment, no allied force risk, an explicit target-loss clearance record, and no cooldown. The startup initializer clears every legacy release, weather, terrain, density, command, evidence-control, forecast-confidence, command-integration, and friendly-risk value; it never supplies a neutral receipt. The route therefore remains fail-closed until `cbrn_occupation_current_version_condition_hook_verified` is backed by a proven current-version exact-state provider.

The effect resets the shared action context, checks repeat use, debits the real agent payload first, debits masks, decontamination equipment, CBRN instruments, support equipment, trucks, and Command Power only after payload proof, resolves target protection, then calls the shared chemical action preparation and dispatch pipeline. Only a proven shared dispatch applies the temporary suppression modifier, state contamination and death history, trauma, cooldown, delayed backlash event, exact responsible-country pointer, exact chemical-record UID, and national repetition records. Rejected input produces no state consequence and never selects an alternate state or agent.

### Exact evidence and disclosure effects

`cbrn_occupation_select_exact_chemical_record`, `cbrn_occupation_advance_exact_chemical_record`, `cbrn_occupation_advance_exact_chemical_record_to_confirmed`, and `cbrn_occupation_suppress_exact_chemical_record_evidence` operate only on the chemical record UID stored by the exact occupation action. Missing or stale UID proof fails closed; no latest-row or same-country fallback exists. Evidence suppression never removes the row, actor, payload, deaths, contamination, attribution history, or use history.

`cbrn_occupation_apply_requested_coverup_action` dispatches one explicit state-scoped action enum to Seal State, Destroy Records, Admit Accidental Release, or Permit Inspection. Seal and record destruction reduce only the exact record's present evidence and create permanent concealment history plus hidden coverup liability. Admission and inspection advance the same exact record, publish discoverable coverup liability, end an active seal, and preserve every physical and historical consequence. Doctrine is applied only to the new contextual Condemnation amount; it never modifies evidence, attribution, casualties, contamination, trauma, medical history, domestic consequences, or action history.

### Delayed aftermath and cleanup effects

`cbrn_occupation_apply_delayed_backlash` is state scoped and runs only from the exact scheduled state event when the stored due day and responsible controller still agree. It applies bounded resistance and compliance backlash, an occupier-scoped dynamic modifier, and at most one eligible neighboring occupied-state spillover. `cbrn_occupation_decay_state_trauma` advances one exact state's annual self-scheduled trauma step. `cbrn_occupation_end_responsible_country_operational_modifiers` removes occupier-specific temporary benefits when control changes while retaining historical trauma, evidence, deaths, and responsibility. No helper performs a broad country or state pulse.

## Chaos Warfare doctrine effects

These country-scope effects are defined in `cbrn_doctrine_effects.txt`. They own institution, policy, mastery-record, technology-grant, and migration state. They never choose or consume a chemical payload and never dispatch exposure.

### Institutional value helpers

| Effect | Inputs, defaults, outputs, and side effects |
| --- | --- |
| `cbrn_doctrine_raise_readiness_to_minimum` | Country scope. Optional temporary input `cbrn_doctrine_requested_readiness_minimum`; absent input is a no-op. Initializes CBRN data, raises readiness only when below the request, and clamps to the current readiness cap. |
| `cbrn_doctrine_raise_decontamination_to_minimum` | Country scope. Optional temporary input `cbrn_doctrine_requested_decontamination_minimum`; absent input is a no-op. Initializes data, raises capacity only when below the request, and clamps to 0-100. |
| `cbrn_doctrine_apply_institutional_band` | Country scope. Optional temporary inputs `cbrn_doctrine_requested_readiness_cap` and `cbrn_doctrine_requested_readiness_minimum`. Applies whichever values exist through the shared readiness helpers; missing values do nothing. |
| `cbrn_doctrine_pay_command_power` | Country scope. Optional temporary input `cbrn_doctrine_command_power_cost`. Negates and debits that amount; callers must pass an affordability trigger first. Missing input is a no-op. |

Example:

```txt
set_temp_variable = { cbrn_doctrine_requested_readiness_cap = constant:cbrn_doctrine_readiness.protective_foundation_cap }
set_temp_variable = { cbrn_doctrine_requested_readiness_minimum = constant:cbrn_doctrine_readiness.protective_foundation_minimum }
cbrn_doctrine_apply_institutional_band = yes
```

### Adoption, establishment, and training

| Effect | Purpose and side effects |
| --- | --- |
| `cbrn_chaos_warfare_adopt` | Initializes the country model, records adoption/program/command flags and cumulative mask-production baseline, closes offensive authority, removes the legacy Concentration unlock, applies the 39/10 adoption band, unlocks Operations HQ plus Gas Mask/Decon support, and activates the bounded establishment mission. The public doctrine gate must pass first. |
| `cbrn_complete_chaos_warfare_establishment` | Records successful establishment, opens institutional authority, raises readiness to 20 and decontamination capacity to 20. The mission or remediation decision owns the exact stock/formation trigger. |
| `cbrn_fail_chaos_warfare_establishment` | Records failure, retains closed offensive authority, restores Defensive Preparation policy, and lowers readiness to at most 9 without removing the doctrine. |
| `cbrn_remediate_chaos_warfare_establishment` | Calls the successful-establishment effect after the delayed decision has re-proved every requirement and paid its costs. |
| `cbrn_begin_hazard_assault_training` | Requires the public training trigger. Debits 100 masks oldest-first and 10 Army Experience, records actual mask consumption, grants 0.25 daily Hazard Assault mastery for 30 days, and activates the matching mission. Because installed `add_daily_mastery` documentation demonstrates literal numeric fields only, the centralized amount and duration variables are rendered into that block through `meta_effect`; no parser support for direct variable tokens is assumed. It creates no exposure. |

Example:

```txt
available = { cbrn_can_begin_hazard_assault_training = yes }
complete_effect = { hidden_effect = { cbrn_begin_hazard_assault_training = yes } }
```

### Exact-state decontamination

`cbrn_apply_theater_decontamination_assignment` is state scoped. The caller must pass `cbrn_state_can_receive_theater_decontamination`; its country wrapper first charges 5 Political Power, 4 Command Power, 40 Decontamination Equipment, 100 Gas Masks, 20 Support Equipment, 2 Motorized Equipment, and 300 Fuel. Decontamination stock and masks are debited oldest-first, and any missing payment blocks the assignment. After payment, it refreshes the exact state's contamination class, selects 10/8/5/3 cleanup points for Trace-or-Local/Serious/Severe/Catastrophic, applies the Theater Contamination Doctrine 1.25 multiplier when present, calls `cbrn_apply_state_contamination_delta_internal`, records only the actual removed amount on the controller, and applies a 28-day state lock. Missing or clean state input produces no useful cleanup. It never alters evidence, attribution, deaths, Condemnation, or use history.

Example:

```txt
FROM = {
	cbrn_apply_theater_decontamination_assignment = yes
}
```

### Institutional claim effects

The four claim effects are country scoped and must be preceded by their corresponding `cbrn_can_claim_*` trigger. They set one persistent milestone, apply its readiness cap/minimum, and retry every doctrine-only technology whose independent gate is now true.

| Effect | Additional result |
| --- | --- |
| `cbrn_claim_protective_foundation` | Raises decontamination capacity to 30 and unlocks the Intelligence/Weather HQ Cell and Chemical Recon Detachment. |
| `cbrn_claim_delivery_integration` | Applies the 74/45 band and opens mapped offensive-HQ gates. |
| `cbrn_claim_theater_exploitation` | Applies the 89/65 band and opens exact-state theater gates. |
| `cbrn_claim_terminal_command` | Applies the 100/85 capstone band. |

### Doctrine technology grants and commissions

`cbrn_grant_available_doctrine_technologies` is a country-scope idempotent dispatcher. It evaluates every `cbrn_can_grant_*` trigger and silently grants only eligible Hazard Pioneer, Chaos Assault, Improved Chaos Assault, Chemical Artillery Shells, Armored Agent Delivery, Mobile Decontamination Columns, Chemical Air Interdiction, and Theater CBRN Headquarters technologies. A failed gate produces no grant. It does not grant Sealed Tank Crews, Persistent Agent Shell Filling, Nerve Suppression, or Biological Security Assault, which require explicit paid commissions.

The four country-scope commission completion effects are `cbrn_commission_sealed_tank_crews`, `cbrn_commission_persistent_agent_shell_filling`, `cbrn_commission_nerve_agent_suppression`, and `cbrn_commission_biological_security_assault`. Each rechecks its exact grant trigger and silently grants only its named technology. Missing prerequisites at completion fail closed; Political Power and Command Power are owned by the decision. In particular, the nerve-suppression commission requires the explicit occupation-policy authorization flag; no Chaos Warfare use-policy tier supplies it.

Example:

```txt
remove_effect = {
	hidden_effect = { cbrn_commission_sealed_tank_crews = yes }
}
```

### Track and mastery record effects

These country-scope effects translate current native doctrine state into stable flags used by institutions, policy, HQ, AI, and migration. They have no temporary inputs. Repeated calls are idempotent except that mapped technology dispatchers may grant a newly eligible technology.

- Adoption records: `cbrn_record_hazard_assault_adoption`, `cbrn_record_toxic_armored_adoption`, `cbrn_record_contaminant_fire_support_adoption`, and `cbrn_record_integrated_command_adoption`. Contaminant Fire additionally unlocks its ammunition train; Integrated Command unlocks Operations HQ.
- Hazard Assault rewards: `cbrn_record_infantry_mastery_one`, `cbrn_record_infantry_mastery_two`, `cbrn_record_infantry_mastery_three`, `cbrn_record_infantry_mastery_four`, and `cbrn_record_infantry_mastery_five`.
- Toxic Armor rewards: `cbrn_record_armor_mastery_one`, `cbrn_record_armor_mastery_two`, `cbrn_record_armor_mastery_three`, `cbrn_record_armor_mastery_four`, and `cbrn_record_armor_mastery_five`.
- Contaminant Fire rewards: `cbrn_record_combat_support_mastery_one`, `cbrn_record_combat_support_mastery_two`, `cbrn_record_combat_support_mastery_three`, `cbrn_record_combat_support_mastery_four`, and `cbrn_record_combat_support_mastery_five`. Levels 3-5 retain stable legacy operation flags while following the accepted payload pipeline.
- Integrated Command rewards: `cbrn_record_operations_mastery_one`, `cbrn_record_operations_mastery_two`, `cbrn_record_operations_mastery_three`, `cbrn_record_operations_mastery_four`, and `cbrn_record_operations_mastery_five`. These unlock mapped HQ companies, raise decontamination capacity at level 3, and retry doctrine technology grants.
- Native track completion records: `cbrn_record_native_infantry_track_complete`, `cbrn_record_native_combat_support_track_complete`, `cbrn_record_native_armor_track_complete`, and `cbrn_record_native_operations_track_complete`.

### Policy, Condemnation, and migration

`cbrn_change_chaos_warfare_use_policy` is country scoped. Required temporary inputs are those of `cbrn_set_use_policy` plus `cbrn_policy_command_power_cost`. When the shared setter accepts the request, it debits Command Power, applies a 90-day reassessment flag, updates peak policy, and records reached policy-history flags. Rejected policy input causes no debit or history change. It never sets `cbrn_nerve_suppression_policy_authorized`; the later CBRN Coercive Security occupation-policy surface owns that authorization.

`cbrn_set_doctrine_condemnation_mult_from_country` is country scoped and writes temporary `cbrn_action_doctrine_condemnation_mult` as 1.00, 0.90, 0.80, or 0.70 from Integrated Command mastery. The non-baseline values read the canonical `chem_integrated_operations.condemnation_mult` ladder also used by not-yet-migrated chemical and biological adapters, preventing parallel tuning tables during route migration. It clamps to the shared doctrine floor/ceiling and changes no persistent state. The helper is Condemnation-only and never touches evidence, attribution, deaths, contamination, medical saturation, domestic penalties, use counters, or history.

`cbrn_migrate_legacy_chaos_warfare` is an idempotent country-scope compatibility effect. For countries with Chaos Warfare, it initializes the model, removes the legacy Concentration unlock, reconstructs adoption and mastery flags from native doctrine state, restores the appropriate readiness cap, and retries legitimate doctrine technology grants. New games call it from `on_startup`; because that on-action does not run when a save is loaded, an old doctrine holder lacking `cbrn_chaos_warfare_adopted` receives the one-time zero-cost `cbrn_convene_institutional_review` decision instead. It does not auto-claim cross-track institutions, fabricate stock/formation proof, or grant a delivery consequence.

Example:

```txt
cbrn_set_doctrine_condemnation_mult_from_country = yes
# temporary cbrn_action_doctrine_condemnation_mult is now ready for the shared record
```

## CBRN Army Headquarters operation effects

These effects are defined in `cbrn_hq_effects.txt`. Character-scope effects expect a deployed army commander; `OWNER` is that commander's country. They never select a state, choose an agent, consume an unspecified payload, or call the shared exposure pipeline.

### Operation-state and preparation helpers

| Effect | Purpose, inputs, outputs, and side effects |
| --- | --- |
| `cbrn_hq_reset_operating_package` | Character-scope internal initializer with no required input. Sets every temporary operating-debit fieldÃ¢â‚¬â€masks, filter wear, decontamination equipment, instruments, support equipment, trucks, fuel, medical capacity, and manpowerÃ¢â‚¬â€to zero before a package setter fills the applicable fields. It changes no persistent value or stock by itself. |
| `cbrn_hq_set_committed_force_band` | Character scope. Reads exact `num_battalions` through the force-band triggers and stores the light, standard, or mass enum in `cbrn_hq_committed_force_band`. Missing/invalid army size falls into the mass fail-safe only after the activation trigger has established a deployed command. |
| `cbrn_hq_stop_operation_benefits` | Character scope. Removes every CBRN preparation/active status trait but deliberately retains the operation code and commitments until planned cleanup. This prevents a stale delayed event from crossing into a newer operation. |
| `cbrn_hq_clear_operation_state` | Character scope. Calls the benefit cleanup and clears operation code, committed force band, and remaining upkeep ticks. It is reserved for the planned final event. |
| `cbrn_hq_calculate_preparation_days` | Character scope. Required temporary inputs: base, minimum, and maximum preparation days. Reads owner Chemical Readiness, applies the centralized readiness multiplier, rounds, and clamps into the accepted range. |
| `cbrn_hq_apply_operations_section_preparation_discount` | Character scope. Inputs: calculated preparation plus the same minimum and maximum temporary bounds. Applies the Operations Section's ten-percent preparation reduction, then reclamps and rounds. Call only for abilities that require that company. |
| `cbrn_hq_apply_high_protection_preparation_discount` | Character scope. Refreshes the owner's real military-mask snapshot and applies the accepted five-percent preparation reduction only at the high-protection threshold, then reclamps. It does not change exposure protection itself. |
| `cbrn_hq_apply_operations_commander_preparation_discount` | Character scope. Inputs: calculated preparation plus minimum/maximum bounds. Applies the doctrine-independent commander's ten-percent reduction only when the leader has `chemical_operations_commander`, then reclamps and rounds. It changes no cost, duration, cooldown, or exposure output. The trait is manually assignable without the doctrine and can be granted by the active Chemical Operations Academy on leader creation or level-up. |
| `cbrn_hq_apply_offensive_doctrine_preparation_discount` | Character scope. Inputs: calculated preparation plus minimum/maximum bounds. Applies the mutually exclusive Theater Contamination or Terminal Hazard preparation multiplier, reclamps, and rounds. Call only from Prepare Chemical Offensive and Combined CBRN Overmatch; it does not accelerate protective, cleanup, medical, or containment orders and changes no cost, active duration, cooldown, or exposure record. |
| `cbrn_hq_add_preparing_trait_for_current_duration` | Character scope. Reads the exact rounded `cbrn_hq_preparation_days` value and injects it into the otherwise static timed-trait field through a CBRN-local meta effect. |
| `cbrn_hq_schedule_current_event` | Character scope. Requires `cbrn_hq_scheduled_event_id` from `cbrn_hq_event_id` and exact rounded `cbrn_hq_scheduled_event_days`. It binds the calling commander as `cbrn_hq_commander` and injects both values into the unit-leader event call because installed documentation does not verify bare dynamic durations for that field. Each event resumes inside that exact commander target before reading variables or changing traits. |
| `cbrn_hq_commit_preparation` | Character scope. Required temporary inputs: calculated preparation, active duration, full/native command-power costs, and an activation operating package. Stores the force band, debits the scripted CP remainder and real stores, applies the timed preparation trait, and schedules bounded preparation/final-cleanup events. Medical/manpower commitments recover on their planned date even if active benefits end early. |

### Model-aware operating-stock debit helpers

- `cbrn_hq_debit_decontamination_stock_oldest_first`: country scope; input `cbrn_hq_family_debit_requested`; outputs completed and remaining family debit; removes decontamination models 1 through 3 oldest-first.
- `cbrn_hq_debit_instrument_stock_oldest_first`: country scope; same contract for instrument models 1 through 3.
- `cbrn_hq_debit_command_power_remainder`: character scope; inputs full and native CP costs; subtracts only the non-native remainder from `OWNER` after clamping at zero.
- `cbrn_hq_debit_operating_package`: character scope; reads temporary mask, military-filter-condition, decon, instrument, support, truck, fuel, medical, and manpower amounts. It uses model-aware family helpers, routes every positive assigned filter debit through `cbrn_apply_military_mask_loss`, records the exact post-technology condition consumed in `cbrn_hq_filter_condition_consumption_total`, writes the other consumption ledgers, commits medical/manpower capacity, and schedules exact restoration events. The public and upkeep triggers fail closed unless the full issued-filter debit is affordable; zero inputs are no-ops.

### Activation and weekly package setters

Each setter resets all package fields before selecting the exact light, standard, or mass table. Activation setters also supply preparation, active duration, native CP, and full CP inputs. Weekly setters contain no medical or manpower recommitment.

| Operation | Activation setter | Weekly setter |
| --- | --- | --- |
| Chemical fire plan | `cbrn_hq_set_prepare_activation_package` | `cbrn_hq_set_prepare_upkeep_package` |
| Protective posture | `cbrn_hq_set_protective_activation_package` | `cbrn_hq_set_protective_upkeep_package` |
| Decontamination corridor | `cbrn_hq_set_decon_activation_package` | `cbrn_hq_set_decon_upkeep_package` |
| Sealed operational area | `cbrn_hq_set_seal_area_activation_package` | `cbrn_hq_set_seal_area_upkeep_package` |
| Antidote response | `cbrn_hq_set_antidote_activation_package` | `cbrn_hq_set_antidote_upkeep_package` |
| Infection corridor | `cbrn_hq_set_infection_activation_package` | `cbrn_hq_set_infection_upkeep_package` |
| Combined overmatch | `cbrn_hq_set_overmatch_activation_package` | `cbrn_hq_set_overmatch_upkeep_package` |

### Public ability-start effects

`cbrn_hq_start_prepare_chemical_offensive`, `cbrn_hq_start_theater_protective_posture`, `cbrn_hq_start_decontamination_corridor`, `cbrn_hq_start_seal_operational_area`, `cbrn_hq_start_mass_antidote_response`, `cbrn_hq_start_seal_infection_corridor`, and `cbrn_hq_start_combined_overmatch` are CHARACTER-scope one-time ability adapters. Their matching activation trigger must be checked first. Each stores a stable operation enum, selects the exact force-band package, calculates preparation, commits stock/CP, and schedules `cbrn_hq.1`. The two offensive preparations apply both the Operations Section and high-protection preparation adjustments. None dispatches exposure.

Example:

```txt
allowed = { cbrn_hq_can_activate_theater_protective_posture = yes }
one_time_effect = {
	hidden_effect = { cbrn_hq_start_theater_protective_posture = yes }
}
```

### Bounded upkeep effects

`cbrn_hq_debit_prepare_upkeep`, `cbrn_hq_debit_protective_upkeep`, `cbrn_hq_debit_decon_upkeep`, `cbrn_hq_debit_seal_area_upkeep`, `cbrn_hq_debit_antidote_upkeep`, `cbrn_hq_debit_infection_upkeep`, and `cbrn_hq_debit_overmatch_upkeep` select and debit one paid weekly installment from the force band stored at activation. The caller must first pass the corresponding upkeep trigger. Army reorganization after activation cannot reduce that package.

`cbrn_hq_schedule_next_upkeep_tick` schedules `cbrn_hq.2` through `cbrn_hq_schedule_current_event` only while the persistent finite tick budget is positive. `cbrn_hq_complete_upkeep_tick` decrements that budget and schedules the next tick when required. `cbrn_hq_fail_upkeep` removes active benefits and the tick budget while retaining the operation commitment until its already scheduled final cleanup. These targeted chains create no periodic country iteration.

## Exact-state CBRN battlefield operation effects

The four route effects in `cbrn_battlefield_operation_effects.txt` are CBRN-specific and stay outside the generic dynamic effect file. They are called by the state-targeted battlefield decisions and by no broad event pulse.

The begin effect saves the selected state into the country-scoped `cbrn_battlefield_active_state` variable before the timed operation leaves the selection chain. Resolution and cancellation read that persistent state pointer, while the short-lived `cbrn_battlefield_state_target` event target is retained only for the immediate begin-chain validation and cleanup path. This prevents a later decision or bounded event from depending on a regular event target that has already expired.

The installed build does not expose a verified state-scope weather and terrain condition hook for this timed Army Headquarters route. `cbrn_battlefield_current_version_condition_hook_verified` therefore remains `always = no`; the persistent state pointer does not relax that gate and does not act as an estimator or proxy.

| Effect | Scope and contract |
| --- | --- |
| `cbrn_initialize_battlefield_operation_selection` | Country scope. Initializes the selected chemical agent to an unlocked model and records a rejected last result. |
| `cbrn_battlefield_cycle_selected_agent` | Country scope. Cycles the explicit agent ladder without changing payload or consequence state. |
| `cbrn_battlefield_set_route_equipment_costs` | Country scope. Calculates the route-specific full or shortage equipment bill from centralized constants. |
| `cbrn_battlefield_pay_route_equipment` | Country scope. Debits model-aware masks, decontamination equipment, instruments, support equipment, chemical shell lots, projector chassis, armored chassis, motorized equipment, and fuel. |
| `cbrn_battlefield_begin_operation` | State-targeted decision scope. Revalidates the exact state, binds the victim, consumes the matching chemical payload, debits readiness and Command Power, and commits the finite operation ledger. |
| `cbrn_battlefield_resolve_operation` | Country scope with stored state target. Reconstructs the exact action record and sends it to the shared CBRN chemical exposure dispatcher. |
| `cbrn_battlefield_cancel_operation` | Country scope with stored state target. Records cancellation and clears the bounded ledger without inventing a payload refund. |
| `cbrn_battlefield_clear_operation_state` | Country scope. Clears state and country operation flags after resolution or cancellation. |

All route effects require the side-effect-free triggers in `cbrn_battlefield_operation_triggers.txt`. No effect selects an alternate state, estimates combat activity, or uses continuous-air activity as a proxy.

## Canonical chemical-state ledger effects

The state-owned chemical ledger is defined in `cbrn_chemical_state_effects.txt`. These helpers are private to the chemical exposure and recovery architecture; they are not generic dynamic effects.

| Effect | Scope and contract |
| --- | --- |
| `cbrn_chemical_set_air_contribution_from_class` | State scope. Converts the exact canonical contamination class into the configured Air Cleanliness contribution and applies only the delta to the state and global component totals. |
| `cbrn_chemical_update_state_receipt` | State scope. Replaces the canonical contamination class, refreshes the exact expiry and continuing-death schedule, updates the presentation modifier, and adjusts Air Cleanliness by the actual class delta. |
| `cbrn_chemical_cleanup_state_receipt` | State scope. Removes only the state-owned chemical receipt and its Air Cleanliness contribution, then clears the state-owned continuing-death schedule. An older cleanup event cannot erase a newer receipt. |
| `cbrn_chemical_rebuild_air_cleanliness_contributions` | Country scope. Explicit settings-reenable repair for states with live canonical chemical receipts. It is called only from the bounded repair path and is not a recurring world scan. |

The legacy `chem_state_contamination_*` variables and presentation modifier remain compatibility mirrors. The legacy `chem_apply_state_contamination` writer is structurally unreachable, and active shared chemical dispatch no longer mutates the legacy helper or applies a broad chemical pulse. The canonical state receipt is the only source for chemical Air Cleanliness, expiry, and continuing deaths.

## Biological Air Cleanliness receipts

`cbrn_biological_air_effects.txt` owns the biological component of Air Cleanliness. A state receives a configured contribution only while an active lifecycle episode exists, and the helper changes the global biological total by the exact state delta. Lifecycle cleanup and countermeasure transitions call the same state-owned cleanup path.

| Effect | Scope and contract |
| --- | --- |
| `cbrn_biological_set_air_contribution_from_agent` | State scope. Maps the selected agent and active lifecycle status to the centralized receipt contribution. Inactive or unknown episodes contribute zero. |
| `cbrn_biological_cleanup_air_receipt` | State scope. Removes only the biological receipt owned by the current lifecycle episode. It does not alter incubation, deaths, attribution, or treatment ledgers. |
| `cbrn_biological_rebuild_air_cleanliness_contributions` | Country scope. Explicit settings-reenable repair for active biological episodes; it is not a periodic country or world pulse. |

The biological effect does not reuse the chemical contamination ledger and does not turn weaponized zombies into ordinary pathogen receipts. Shared lifecycle helpers remain in the biological files.

## Chemical doomsday release adapter

`cbrn_chemical_doomsday_effects.txt` is the decision-owned batch adapter for the retained doomsday decision. It validates exact controlled states and the selected extreme-use policy, captures each agent's real restricted-site cylinder stock, consumes stock once, and dispatches each accepted state through `cbrn_prepare_chemical_action_record` and `cbrn_dispatch_chemical_action_record`. The batch Condemnation receipt is attached to accepted states after the shared action record has been created.

It never estimates a target, substitutes a state, dispatches from idle aircraft, or calls the retired direct contamination helper. Missing condition or target proof rejects the release. The stock-scaled Condemnation range is centralized in `cbrn_chemical_doomsday_constants.txt` and is gameplay tuning rather than a historical casualty estimate.

## CBRN achievement and preparation effects

`cbrn_achievement_effects.txt` records achievement receipts from actual readiness, protection, delivery, lifecycle, decontamination, medical, evidence, and consequence outcomes. It does not grant the underlying state and cannot be used as a gameplay shortcut.

`cbrn_starting_protection_effects.txt` initializes country-specific prepared reserves and the population-scaled military/civilian protection ledgers. The starting values are gameplay tuning with explicitly limited historical confidence; Britain is intentionally the strongest prepared First World War reserve in the accepted matrix.

## Camp, occupation, and headquarters adapters

`cbrn_camp_effects.txt` and `cbrn_occupation_effects.txt` remain route-specific adapters. Camp efficiency may be improved by the accepted terminal doctrine and extreme policy, but those effects do not create, reveal, or authorize camps or other extermination infrastructure. Nerve suppression consumes the exact restricted-site package and records protection failure, deaths, contamination, medical saturation, resistance trauma, evidence, attribution, and diplomatic consequence through the shared contract.

`cbrn_hq_effects.txt` owns Army Headquarters preparation and regimental-support operating packages. It debits essential equipment, filter wear, decontamination, instruments, transport, fuel, medical capacity, and manpower using finite preparation, active, upkeep, cooldown, and cleanup events. It is the theater layer; regimental support remains the division layer. None of these helpers performs a broad all-country periodic pulse.
