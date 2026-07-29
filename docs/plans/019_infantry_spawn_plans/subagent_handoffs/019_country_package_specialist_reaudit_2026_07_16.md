# Event 019 country-package specialist re-audit

**Date:** 2026-07-16  
**Audit mode:** read-only gameplay re-audit; this file is the only edit  
**Scope:** Event 019 claimant and zombie/ghost/golem derivative country packages, with a targeted second pass over paid family reinforcement atomicity

## Disposition

- **Paid zombie/ghost/golem reinforcement transaction:** clean. The previously reported P1 atomicity finding is closed by the live patch.
- **Claimant, scenario, identity, focus/decision, registry, and lifecycle surfaces:** clean for the reviewed country-package scope.
- **Remaining blocker:** natural pressure-driven derivative release is still not implemented beyond candidate/region/transfer preflight. The documented engine surface has no division-scoped ownership-transfer effect. The exact recreate/delete substitute remains an unapproved fallback, so the source correctly stops before ownership mutation.
- **Overall package completion:** blocked by that natural-release transfer decision. No fixed-tag or other fallback was silently introduced.
- **Open severity count:** one P0/approval blocker; zero P1; zero P2.

## Targeted paid-reinforcement transaction re-audit

### Call paths

The three reviewed paid actions converge on `infantry_spawn_derivative_materialize_one_family_formation` in `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`:

1. `infantry_spawn_derivative_rally_zombie_band`
   - Debits the configured manpower and base infantry-equipment costs.
   - Calls the common materializer.
   - Applies cooldown and optional exact-template training authorization only after materialization success.
   - Refunds the direct debit only when `infantry_spawn_derivative_materialization_rollback_succeeded > 0`.
2. `infantry_spawn_derivative_manifest_paid_family_formation`
   - Evaluates and pays provider 502 (ghost) or provider 503 (golem) management costs.
   - Calls the common materializer.
   - Applies cooldown only after materialization success.
   - Calls the same provider's refund callback only when the rollback-success output is proved.

The decision callers are `infantry_spawn_derivative_rally_zombie_band_decision`, `infantry_spawn_derivative_manifest_ghost_host_decision`, and `infantry_spawn_derivative_bind_golem_host_decision` in `common/decisions/019_infantry_spawn_derivative_decisions.txt`.

### Ordering and publication

The live order is transactionally coherent:

1. The caller performs the family-specific debit.
2. The materializer completes non-mutating registry, state, ledger-alignment, and parent-isolation preflight.
3. It clears `infantry_spawn_request_payment_succeeded` and every generic `infantry_spawn_request_paid_*` temporary.
4. It calls `infantry_spawn_snapshot_management_request_transaction`, so the reusable management snapshot records the **post-family-payment** state.
5. It locks its own refund output, advances the country generation, allocates a monotonic generation UID, and publishes the generation with `infantry_spawn_append_current_generation_row` before appending subordinate rows.
6. It builds one registered-family lot and exact template, appends one selected-state row, invokes provider 501/502/503's one-unit callback, resolves the generation row, and verifies aligned ledgers plus exactly one lot and one unit in the current generation.
7. Only after that proof does it set materialization success and increment `infantry_spawn_derivative_reinforcement_count`.

The generic request-payment temporaries being zero is essential: the shared rollback's ordinary-request refund branch cannot double-refund the separate derivative payment.

### Object and ledger atomicity

The materialization path touches these persistent surfaces, all of which are inside the shared snapshot/rollback protocol:

- generation rows and the reusable pre-existing generation tail;
- selected-state rows;
- lot rows;
- template rows and template-component rows;
- unit rows and exact live division scopes;
- obligation rows;
- locked-template and spawn-only-template auxiliary arrays;
- transfer-eligible unit auxiliary rows;
- technology/pretechnology and achievement-pretechnology auxiliary rows;
- active lot/division, unresolved-generation, debt, liability, request, anomalous-request, country-stage, and selected-lot counters;
- ordinary-history lot/formation aggregates;
- generation-audit, invariant, deferred-processing, technology/pretechnology, achievement-history, and registry-materialization flags.

The lower `infantry_spawn_spawn_current_template_unit` helper already requires a one-division engine delta, captures the new division by excluding pre-create scopes, writes the exact Event 019 unit/delete-cohort/generation/lot/template/family identity, appends the unit and obligation rows, checks their alignment, and locally rolls back a partial unit transaction before raising the invariant flag.

On top-level failure, `infantry_spawn_rollback_management_request_transaction`:

- deletes every post-snapshot division by its unique create-unit cohort ID with `disband = no`;
- deletes every post-snapshot `Unbidden Muster <template UID>` template and its units, and proves each template no longer exists;
- truncates every main and auxiliary array named above to the snapshotted boundary;
- restores the pre-existing generation tail values;
- restores country counters, debt/liability, global lot/formation aggregates, prototype stockpiles, and snapshotted flags;
- proves exact array lengths, exact division count, exact snapshotted XP/manpower/fuel/covered-equipment balances, and both main- and claimant-ledger alignment;
- sets `infantry_spawn_request_rollback_valid = 0` and retains/raises the invariant failure if any proof fails.

The derivative materializer exposes rollback success only when that final proof remains valid. Monotonic generation, lot, template, unit, obligation, and delete-cohort allocators are deliberately not rewound; this leaves identity gaps but no live object, ledger, counter, or resource residue.

### Resource atomicity and fail-closed refunds

- **Zombie:** the shared snapshot records manpower and infantry equipment after the direct debit. Rollback must restore those post-debit balances exactly; only then does the caller add back the configured debit. A failed rollback therefore receives no refund.
- **Ghost:** political power and command power are debited by provider 502 before the snapshot. The materializer does not modify either balance. Provider 502 reverses the debit only after proved rollback.
- **Golem:** political power, command power, and `coal_golem_equipment_1` are debited by provider 503 before the snapshot. The materializer records a golem obligation but does not debit those balances. Provider 503 reverses the debit only after proved rollback.
- The engine-created division's starting manpower/equipment is part of the created division, not a second country-stockpile payment. Rollback uses `disband = no`, so deleting the failed object cannot manufacture a refund.
- Neither a failed materialization nor a failed rollback applies cooldown, training authorization, family-sustainment success, or reinforcement-count success.

**Verdict:** object, ledger, auxiliary-array, counter, and payment handling are atomic for the reviewed one-formation paths. Refund behavior is fail closed. The previous P1 is closed.

## Complete country-package re-audit

### Claimant identity and succession

- Claimant-route entry uses the persisted `infantry_spawn_derivative_claimant_uid`; route availability does not depend on `infantry_spawn_active_claimant_count` remaining nonzero after takeover.
- Appointment snapshots the entire claimant row boundary, active count, selected index, and claimant history/identity state. Failed character creation, lookup, promotion, or identity proof rolls the appended claimant row and route state back.
- Replacement uses the same claimant snapshot/rollback boundary. It does not retire the old claimant or consume continuity state until the replacement character and public identity are proved.
- `infantry_spawn_execute_selected_claimant_takeover` sets `infantry_spawn_active_claimant_count = 0`, correctly removing the ruler from the active field-claimant population while preserving takeover identity through the stable claimant UID.
- Claimant Guard generation snapshots the management transaction, proves generation/claimant success, and rolls back failed unit/ledger mutation. Its success-side XP debit, reinforcement count, sustainment flag, and cooldown occur only after the generation proof.

Primary evidence:

- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
- `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt`
- `common/scripted_triggers/019_infantry_spawn_derivative_package_triggers.txt`

### Scenario actor profile and ordinary-history isolation

- `infantry_spawn_scenario_commit_ordinary_actor_evolution_profile` freezes each completed ordinary scenario actor's applied evolution profile.
- Fresh ordinary actors receive the intended minimum profiles: localized I-II, regional I-II, continental I-III, global I-IV.
- A pre-existing same-tag actor retains any fully applied higher stage. This is documented minimum-profile behavior, not a partial-state leak.
- `infantry_spawn_has_evolution_i` through `_iv` read an actor's frozen applied flags while it is a scenario actor; forced scenario flags remain available for setup.
- Ordinary global evolution iteration is gated by `infantry_spawn_contributes_to_ordinary_evolution_history`. Scenario actors and derivatives return no, so they do not append to ordinary history totals.
- Derivative setup scrubs ordinary participation, evolution-applied, forced-evolution, and scenario-actor state before installing the private derivative identity.

Primary evidence:

- `common/scripted_effects/019_infantry_spawn_scenario_effects.txt`
- `common/scripted_triggers/019_infantry_spawn_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_evolution_effects.txt`
- `docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md`
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md`

### Identity matrix and public presentation

- The cosmetic classifier freezes one of seven origin regions before the first public identity is applied.
- Thirteen identity stems combine with seven regions for 91 exact regional cosmetic tags.
- Automated matrix audit result: 91 tags, 1,365 required base/DEF/ADJ plus four-ideology localisation keys, zero missing localisation keys; 273 regional normal/medium/small flags, zero missing files.
- `localisation/english/019_infrantry_spawn_l_english.yml` retains UTF-8 BOM (`EF BB BF`).
- Incomplete identity or region fails closed; there is no generic cosmetic fallback.

### Focus, decision, and family lifecycle

- `common/national_focus/019_infantry_spawn_derivative_focus.txt` contains 45 focuses: 30 shared focuses and five bespoke overlays for each of zombie, ghost, and golem families. Each family therefore has 35 reachable focuses before mutually exclusive route/doctrine choices are applied.
- The claimant, collective, and species route roots are mutually exclusive and shared downstream focuses accept the appropriate route alternatives.
- Family operation focuses unlock their corresponding zombie-training/zombie-rally, ghost-manifestation, or golem-binding decisions.
- Decision visibility and availability are family-specific, use the aligned-ledger/resource gates, and route to the exact provider-backed effects audited above.
- Defeat/annex handling is narrow (`on_capitulation` and `on_annex`), not a world-scan on action. It records the winner, invokes defeat handling once, migrates annex cleanup work, and finalizes derivative cleanup.
- Final cleanup removes derivative ideas, route/family flags, claimant state, cosmetic identity, private Event 19 ledger state, templates/units, and retry surfaces through the shared exact cleanup protocol.

Primary evidence:

- `common/national_focus/019_infantry_spawn_derivative_focus.txt`
- `common/decisions/019_infantry_spawn_derivative_decisions.txt`
- `common/on_actions/019_infantry_spawn_derivative_on_actions.txt`
- `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt`
- `common/scripted_effects/019_infantry_spawn_management_effects.txt`

### Recruitment and provider isolation

- Provider 501 exposes only the base `zombies` battalion and declares `trainable_and_spawnable`. Its generated template starts locked and `force_allow_recruiting = no`; the derivative authorization effect unlocks only exact generated base-zombie templates.
- Provider 502 exposes only `death_weak_ghost_host` and is `spawn_only`.
- Provider 503 exposes only `coal_golem` and is `spawn_only`.
- Ghost and golem templates remain locked and non-recruitable; no mutated zombie, stronger ghost, or unrelated golem package is exposed through Event 19.

### Registry one-file proof

The registry source search returned exactly one Event 19 family-registry implementation file:

`common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`

It contains the complete provider callback sets:

- provider 501: eligibility at line 4046, template at 4060, spawn at 4083, derivative setup at 4178;
- provider 502: eligibility at line 4211, template at 4225, spawn at 4248, derivative setup at 4334;
- provider 503: eligibility at line 4367, template at 4387, spawn at 4408, derivative setup at 4500.

Startup registration is wired into the existing source-event on-actions:

- provider 501: `common/on_actions/002_zombie_outbreak_on_actions.txt`, line 10;
- provider 502: `common/on_actions/010_death_on_actions.txt`, line 10;
- provider 503: `common/on_actions/005_soviet_collapse_on_actions.txt`, line 10.

The obsolete provider-specific registry effect, trigger, constant, and on-action files are absent/deleted in the live change set. No second Event 19 zombie/ghost/golem registry implementation remains.

## Remaining approval-blocked natural release

The specification requires a dynamic regional derivative actor, coherent territory, a leader, transfer of claimant/family formations, public identity, and war with the former parent (`docs/specs/019_infantry_spawn_specs/specs/019_infantry_spawn_spec_part_6_derivative_countries.md`).

The source currently provides strong preflight only:

- `infantry_spawn_select_natural_derivative_revolt_candidate` selects the dominant eligible family/claimant pressure;
- `infantry_spawn_build_natural_derivative_revolt_region` builds the connected safe non-capital state set;
- `infantry_spawn_prepare_natural_derivative_transfer_set` freezes and proves exact live unit, template, lot, generation, and delete-cohort identities;
- `infantry_spawn_prepare_natural_derivative_revolt_transaction` calls those helpers.

That transaction helper has exactly one repository occurrence: its definition. It has no caller, creates no dynamic country, transfers no territory, mutates no ledger ownership, starts no war, and installs no derivative package. The source comment explicitly stops before ownership mutation because the documented effects offer no division-scoped transfer operation. Recreating the units for a new dynamic country and deleting the originals could preserve the intended result only as a fallback transaction, and repository policy requires explicit user approval before that fallback can be implemented.

The `create_dynamic_country` call in `019_infantry_spawn_scenario_effects.txt` belongs to the separate triggerable-scenario path. It is not a natural-release caller or substitute. No permanent tag fallback is present.

**Required decision:** approve the exact recreate-then-delete transfer design (with full object/ledger/resource rollback proof), or provide/authorize another supported transfer mechanism. Until then, natural derivative release remains incomplete by design.

## Validation record

- Re-opened the live derivative materializer, management snapshot/rollback, lower unit transaction, providers 501/502/503, and the three decision callers after the patch.
- Compared `create_unit`, `delete_unit`, and `delete_unit_template_and_units` behavior against the current vanilla `documentation/effects_documentation.md` and the offline Effects wiki snapshot.
- Re-ran the one-file registry search and provider/startup callback location check.
- Re-ran the 91-tag localisation/flag matrix audit and the 45-focus count.
- Re-ran the natural-release call-site search: one occurrence, definition only.
- This was a static source re-audit. No gameplay source, localisation, asset, spreadsheet, or registry file was changed by this handoff.

## Files changed by this specialist

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_country_package_specialist_reaudit_2026_07_16.md`

## Skills and references used

- `chaos-redux-subagents` for ownership boundaries, audit reporting, and handoff placement.
- `chaos-redux-events` for Event 19 integration and completion standards.
- `hoi4-focus-trees` and `hoi4-decisions-missions` during the full country-package pass for reachability and decision-lifecycle review.
- Required offline Paradox wiki core pages plus Country creation, Cosmetic tag, National focus, Division, Equipment, and Technology references.
- Vanilla HOI4 effects/triggers/script-constant documentation and matching vanilla implementations.

## Simplifications, omissions, and blockers

- No fallback or simplification was used.
- The natural pressure-driven derivative release remains unimplemented because the only exact substitute for missing division-scoped transfer is approval-blocked.
- No other country-package omission was found in the reviewed live source.
