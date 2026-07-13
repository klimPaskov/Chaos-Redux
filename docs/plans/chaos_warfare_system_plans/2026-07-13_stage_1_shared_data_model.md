# Chaos Warfare Stage 1 shared data model

Date: 2026-07-13

Status: implemented in isolated helper files; not yet connected to live delivery routes.

## Authority and scope

This tranche implements Stage 1 of `handoffs/staged_implementation_plan.md`: shared constants, readiness, policy, protection, contamination classes, evidence, attribution, a normalized temporary action record, source labels, and cleanup. It does not activate new attacks, alter legacy delivery effects, create equipment, or dispatch consequences. That activation belongs to the ordered equipment, route-migration, and consequence stages.

The accepted doctrine rule is that doctrine may reduce Condemnation impact while evidence, attribution, and confirmed-use history remain intact. Strategic and mass-casualty confirmed-use floors remain in the shared calculation. The numbered-spec rule separating doctrine from camp/genocide infrastructure is unchanged.

## Files and ownership

| File | Ownership |
| --- | --- |
| `common/script_constants/cbrn_system_constants.txt` | Shared enums, ranges, profile tables, caps, and scheduler bounds. |
| `common/scripted_triggers/cbrn_triggers.txt` | Readiness, policy, state, action metadata, payload-proof, protection-proof, condition-proof, and continuous-air rejection gates. |
| `common/scripted_effects/cbrn_protection_effects.txt` | Country initialization, readiness/cap mutations, policy mutation, and layered chemical protection calculation. |
| `common/scripted_effects/cbrn_exposure_effects.txt` | Temporary chemical action record, fail-closed validation, normalized outputs, lazy contamination/evidence state helpers, and action cleanup. |
| `common/scripted_effects/chaosx_dynamic_effects.md` | Public and internal effect contracts. |
| `common/scripted_triggers/chaosx_dynamic_triggers.md` | Reusable trigger contracts. |

The separate constants file is the unified cross-system source for new CBRN code. Legacy chemical and biological constants remain authoritative for unmigrated call sites until their stages replace or adapt them. No duplicate live calculator is active in Stage 1.

## Constants table

| Family | Accepted values or range | Use |
| --- | --- | --- |
| `cbrn_weapon_class` | chemical, biological, weaponized zombie | Keeps ordinary biological and zombie records distinct. |
| `cbrn_agent_class` | choking, blister, nerve, incapacitating, biological, weaponized zombie | Shared class routing. |
| `cbrn_agent` | nine chemical identities, four ordinary biological identities, one separate zombie identity | Stable action metadata. |
| `cbrn_delivery_route` | cylinder, projector, artillery, armor, exact-state air raid, strategic raid, covert, suppression, recognized unsupported continuous mission, biological routes, accident, doomsday | Preserves route identity and blocks unsupported air behavior. |
| `cbrn_use_policy` | defensive, retaliation, limited battlefield, strategic release, unrestricted | One multi-state national policy variable. |
| `chemical_readiness` | 0 to 100 | Main national value. |
| readiness thresholds | 20, 40, 60, 80 | Limited, operational, integrated, and full bands. |
| default readiness cap | 19 | A paper program cannot accumulate operational readiness before later milestone/cap grants. |
| national capacities | 0 to 100 | Decontamination, medical, biological security, attribution control, and command integration. |
| chemical contamination | 0 to 100 | Lazy state value. |
| contamination thresholds | 1, 10, 25, 50, 75 | Trace, Local, Serious, Severe, Catastrophic. |
| evidence | 0 to 100 | Lazy state/action value. |
| attribution thresholds | 20, 45, 75 | Suspected, Probable, Confirmed. |
| public attribution multipliers | 0.10, 0.25, 0.60, 1.00 | Matrix-aligned public share before unpaid latent responsibility logic. |
| protection bands | 25, 50, 75, 90 | Matrix-aligned layer result bands. |
| contamination duration | 1 to 720 days | Bounded state episode duration. |
| tactical/strategic/nerve death caps | 0.15%, 0.75%, 1.50% of state population | Per-operation safeguards before independent repeat attacks. |
| doctrine Condemnation multiplier | 0.70 to 1.00 for the doctrine component | Implements the accepted mitigation rule. Context can separately apply retaliation or target-relation multipliers. |

Route and agent profile values use matrix midpoints or values inside accepted bands. Condemnation starts from route identity, then applies an agent-class multiplier before context and doctrine: choking is baseline, blister is higher, nerve is highest, and incapacitating agents are lower. These are first-pass gameplay tuning, not historical measurements. They remain subject to the required Stage 14 weak/normal/high-chaos scenario runs.

## Persistent state ownership

### Country scope

| Identifier | Owner | Cleanup or cap |
| --- | --- | --- |
| `cbrn_program_established` | Program decision/doctrine migration | Country flag; removed only by an explicit conversion/retirement path. |
| `chemical_readiness` | CBRN core | Clamped to `chemical_readiness_cap`. |
| `chemical_readiness_cap` | Milestones, institutions, and later equipment/HQ checks | 0 to 100; default 19. |
| `cbrn_use_policy` | Program-management decisions | Valid enum only. |
| `cbrn_decontamination_capacity` | Protection/HQ/technology integration | 0 to 100. |
| `cbrn_medical_capacity` | Medical decisions, support equipment, trucks, and treatment technology | 0 to 100. |
| `cbrn_biological_security` | Biological safety and response systems | 0 to 100. |
| `cbrn_attribution_control` | Program, intelligence, and doctrine inputs | 0 to 100; cannot erase confirmed history. |
| `cbrn_command_integration` | Army HQ and doctrine integration | 0 to 100. |
| `cbrn_retaliation_authorized` | Confirmed-use/retaliation window | Country flag with later targeted expiry/cleanup. |

### State scope

State values are created only when a state is affected. Stage 1 does not initialize every state.

| Identifier | Owner | Cleanup |
| --- | --- | --- |
| `cbrn_chemical_contamination` | Shared consequence dispatcher | Cleared below Trace. |
| `cbrn_chemical_contamination_class` | Classification helper | Cleared with contamination. |
| `cbrn_chemical_contamination_duration_days` | Targeted contamination job | Extended to the longer active duration, capped at 720; not stacked into independent loops. |
| `cbrn_evidence_quality` | Evidence/attribution record | Retains latent values below Suspected; later expiry/record resolution owns removal. |
| `cbrn_attribution_state` | Evidence classification helper | Cleared while evidence is Unknown. |

Civilian protection, local decontamination progress, medical saturation, biological contamination, movement controls, outbreak stages, and responsible-actor persistence are reserved for their equipment, consequence, and biological stages. They are not initialized with guessed defaults here.

## Chemical action-record contract

`cbrn_prepare_chemical_action_record` is country scoped on the attacker. It is a calculator and validator, not a delivery effect.

### Required target

The caller saves the exact state as regular event target `cbrn_action_target_state` and sets `cbrn_action_target_state_supplied = constant:cbrn_proof.supplied` in the same effect chain. The helper derives `cbrn_action_victim_country` from the current controller when available. Regular event targets expire with the originating chain; the numeric proof prevents a stale target in a reused chain from being accepted.

### Required metadata

- `cbrn_action_weapon_class`
- `cbrn_action_agent_class`
- `cbrn_action_agent`
- `cbrn_action_delivery_route`
- `cbrn_action_severity`

Agent and class must match. A continuous-air mission route is recognized but always rejected with `unsupported_continuous_air_route`.

Agent and route must also match the delivery matrix. Nerve use through cylinder, projector, artillery, armored, or air delivery requires a later-route authorization proof set by the mapped technology/doctrine gate. Nerve Suppression accepts nerve agents only.

### Required payload proof

- `cbrn_action_payload_required`
- `cbrn_action_payload_consumed`
- `cbrn_action_payload_consumed_proof = constant:cbrn_proof.supplied`

The proof may be set only by the CBRN payload-debit helper introduced with real payload equipment. A route adapter cannot mark a reservation, estimate, or inferred stock loss as consumption. Both required and consumed values must be positive. The normalized payload ratio is capped at 1.

### Required protection proof

The equipment/coverage layer supplies six 0-to-100 values:

- `cbrn_protection_respiratory`
- `cbrn_protection_skin`
- `cbrn_protection_antidote`
- `cbrn_protection_decontamination`
- `cbrn_protection_medical`
- `cbrn_protection_warning`

`cbrn_calculate_action_protection` produces effective protection plus casualty, disruption, and contamination multipliers and sets `cbrn_action_protection_resolved_proof`. Gas masks are therefore strong against choking agents but cannot stand in for skin protection, decontamination, antidotes, or medical response.

### Required condition proof

The verified route context supplies:

- weather multiplier
- terrain multiplier
- target-density multiplier
- command multiplier
- evidence-control multiplier
- context Condemnation multiplier
- doctrine Condemnation multiplier, independently bounded to 0.70 through 1.00
- forecast confidence
- command-integration value
- base friendly-exposure risk
- `cbrn_action_conditions_resolved_proof = constant:cbrn_proof.supplied`

No neutral weather or terrain fallback is hidden in the helper. Each route must obtain or deliberately define its supported context before setting the proof.

### Outputs

Accepted calls return:

- normalized payload ratio and dose multiplier
- military disruption
- military death fraction among the affected force
- civilian exposed share and state-population death fraction
- contamination points and duration
- medical-saturation points
- evidence points and attribution state
- Condemnation base after the accepted context/doctrine multiplier and confirmed-use floor
- friendly-exposure risk
- source label
- victim event target when known

`cbrn_action_result` and `cbrn_action_reject_reason` are always populated. Rejected calls return zero consequence outputs and change no persistent state.

## Mandatory final ordering

The route migration must preserve this sequence:

1. Resolve exact actor, victim, and target state and pass `cbrn_chemical_action_static_metadata_is_valid`.
2. Calculate required payload.
3. Debit real payload equipment and set the debit proof.
4. Resolve equipment-backed military/civilian protection and set the protection proof.
5. Resolve verified weather, terrain, density, forecast, command, evidence, retaliation, doctrine, and target context; set the separately bounded doctrine and context multipliers; then set the condition proof.
6. Call `cbrn_prepare_chemical_action_record`.
7. If accepted, apply disruption and friendly blowback, register military and civilian deaths once, mutate contamination/medical/evidence state once, update Air Cleanliness on class crossing, add the correct Condemnation/atrocity context once, and persist the operation/evidence record.
8. Call `cbrn_reset_action_context` after every consumer has read the outputs.

No delivery route may retain an independent death, contamination, evidence, medical, or Condemnation calculator after migration.

## Existing adapter boundary

The later consequence dispatcher will reuse, not clone:

- `chaos_meter_register_state_civilian_deaths_percent`
- `air_contamination_apply_delta_bp`
- `condemnation_add_source`
- `chem_warfare_register_attack_use` during compatibility migration
- `bio_register_condemnation_source` for biological records

The internal state mutation helpers in `cbrn_exposure_effects.txt` deliberately do not call these adapters. Only the final dispatcher may call them, using previous/new class values to prevent double counting.

## Continuous-air decision

Installed 1.19.2 documentation and vanilla files expose no verified ordinary mission hook proving eligible chemical activity. The action enum retains `continuous_air_mission` solely to return a stable rejection reason. Exact-state raid routes remain supported. No estimator, region pressure, based-aircraft count, or idle-aircraft path exists in the new core.

## Specialist review status

The requested scripted-system architect was launched without inherited context. Its broad CBRN prompt was rejected by the subagent safety filter, so it returned no architecture finding. This is recorded as unavailable, not passed. The main implementation reviewed the accepted specs, current helpers, official engine docs, and vanilla patterns directly. A narrower architecture audit remains required in Stage 13 after the live call graph exists.

## Migration sequence

1. Add real protective and payload equipment plus issue/debit helpers.
2. Validate protection against legacy routes without activating duplicate consequences.
3. Migrate one delivery route at a time to the action-record contract.
4. Remove that route's independent consequence calculator only after its adapter is verified.
5. Add the single consequence dispatcher and persistent evidence records.
6. Remove the unsupported air estimator and its scheduled event path.
7. Retain old public identifiers only as thin compatibility wrappers until every caller and template is migrated.

## Stage 1 exit evidence

- Shared constants and enums are centralized.
- Country data initializes lazily and readiness cannot exceed its cap.
- Protection is class-sensitive and requires six explicit layers.
- Action preparation rejects missing exact targets, payload debit, protection, or conditions.
- Continuous ordinary-air missions cannot be accepted.
- State contamination and evidence helpers are lazy and non-duplicating.
- No on-action, decision, event, equipment, UI, or legacy delivery file is changed by this tranche.
- No fallback or estimator is introduced.
