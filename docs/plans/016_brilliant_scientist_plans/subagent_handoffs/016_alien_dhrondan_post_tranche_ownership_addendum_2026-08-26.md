# Event 016 Alien Infantry and Empire of D'Rhonda Post-Tranche Ownership Addendum

Date: 2026-08-26

Status: Narrow addendum required, broad expansion remains closed

Owner: Parent Event 016 implementation agent

Planner mode: Read-only gameplay and asset audit with documentation-only output

## Disposition

The 2026-08-22 improvement-loop closure remains valid for broad scope.

Event 016 does not need another focus route, country, formable, scripted GUI, super-event, raid family, or parallel Alien Infantry system.

Two implementation tranches landed after that closure and introduced distinct ownership gaps that the earlier disposition could not cover.

The first is a severity-one cross-consumer contamination defect in the new sparse Alien Infantry landing registry.

The second is a severity-two lifecycle gap in the successful Portal Raider beachhead, which persists only as an undifferentiated state flag after the native raid outcome ends.

This addendum is therefore intentionally narrow.

It supersedes the earlier closure only for the ownership and acceptance work defined below.

No prior accepted expansion addendum remains open, and this file must not be used to reopen the dispositioned R1 through R7 proposals.

## Sources reviewed

The review inventoried and searched every Event 016 specification, plan, handoff, and implementation identifier, then directly reviewed the binding source-of-truth documents, current implementation files, and current handoffs governing the two accepted packages.

The principal binding and current documents were:

- `docs/specs/016_brilliant_scientist_specs/016_source_of_truth_map.md`
- `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`
- `docs/specs/016_brilliant_scientist_specs/acceptance/016_alien_dhrondan_acceptance_scenarios.md`
- `docs/specs/016_brilliant_scientist_specs/prompts/016_brilliant_scientist_improvement_loop_planner_prompt.md`
- `docs/plans/016_brilliant_scientist_plans/016_brilliant_scientist_improvement_loop_addendum.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_dhrondan_improvement_loop_closure_handoff_2026-08-22.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_api_audit_2026-08-25.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_api_reconciliation_2026-08-26.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_landing_state_registry_2026-08-26.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhr_route_consumers_2026-08-26.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_portal_lifecycle_patch_2026-08-26.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_focus_audit_2026-08-25.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhr_probability_audit_2026-08-25.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhrondan_country_audit_2026-08-25.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_dhr_event_completion_audit_2026-08-25.md`
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_firearm_meshy_rig_and_free_animation_2026-08-25.md`
- `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/job.yaml`

The current source files directly reviewed were:

- `common/scripted_effects/016_alien_infantry_api_effects.txt`
- `common/scripted_effects/016_dhrondan_country_effects.txt`
- `common/scripted_triggers/016_dhrondan_country_triggers.txt`
- `common/scripted_effects/016_brilliant_scientist_raid_effects.txt`
- `common/raids/016_brilliant_scientist_portal_raids.txt`
- `common/national_focus/016_dhrondan_focus_tree.txt`
- `common/decisions/016_dhrondan_country_decisions.txt`
- `common/scripted_triggers/016_dhrondan_country_triggers.txt`
- `common/scripted_effects/chaosx_dynamic_effects.md`

The engine basis came from the required offline Paradox Wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, focuses, countries, divisions, equipment, and technology.

The vanilla documentation basis included the native raid framework, decisions, on actions, units, equipment, special projects, scientist traits, AI strategies, script concepts, and script constants.

The native raid framework was also inspected through vanilla raid definitions, including outcome-owned formation destruction and native preparation, reservation, cancellation, outcome, cooldown, and raid-history behavior.

No historical or regional expansion is proposed because Alien Infantry, the Empire of D'Rhonda, and the Portal Raider package are fictional systems whose current defects are causal ownership defects rather than missing historical texture.

## Severity-one finding: the global landing registry breaks provider-neutral ownership

### Evidence

`alien_infantry_register_landing_state` at `common/scripted_effects/016_alien_infantry_api_effects.txt:300` writes every successful caller's selected state into `global.alien_infantry_landing_state_registry` at lines 308 and 314.

The helper is called after ordinary landing success at line 469 and after the Event 019 deferred commit at line 553.

Both success paths also set the unqualified state flags `dhrondan_landing_state` and `dhrondan_landing_history_recorded`.

`dhrondan_capture_revolt_inputs` at `common/scripted_effects/016_dhrondan_country_effects.txt:18` loops the same global array at line 30 and counts every registered state carrying `dhrondan_landing_state`.

`dhrondan_release_and_transfer_landing_states` at line 95 loops the same global array at line 111 and gives DHR a claim on every marked state not already owned by DHR.

`dhrondan_state_is_landing_site` at `common/scripted_triggers/016_dhrondan_country_triggers.txt:16` checks only the global state flag and has no pact-host or provider provenance test.

The current dynamic-effect documentation explicitly describes the array as sparse and global, so this is an implemented ownership choice rather than a stale comment.

### Consequence

If two independent countries use the provider-neutral Alien Infantry API, a revolt in country A can count country B's arrivals and claim country B's landing states.

The defect also crosses provider identities because Event 019 and any future source receipt write into the same global state set.

This violates the accepted rule that DHR receives or claims landing states belonging to its pact host, while the reusable Alien Infantry API remains isolated across consumers and providers.

The global array fixed the earlier world-state scan but replaced it with a cross-consumer causality defect.

### Required design

The landing registry must be a regular country-scoped array owned by the country that completed the landing transaction.

`alien_infantry_register_landing_state` must add the selected state scope to the caller country's `alien_infantry_landing_state_registry` only after a successful ordinary commit or successful Event 019 deferred commit.

The current `dhrondan_landing_state` and `dhrondan_landing_history_recorded` flags may remain historical state evidence, but neither flag may be sufficient to associate the state with an arbitrary revolt host.

`dhrondan_capture_revolt_inputs` and `dhrondan_release_and_transfer_landing_states` must iterate the current pact host's scoped registry.

The host-scoped array persists the association when a registered state is later occupied or changes ownership, which preserves the accepted lost-state claim behavior without admitting another consumer's state.

When DHR later completes its own landings, those states belong to DHR's own scoped registry and do not mutate the former host's registry.

Receipt revocation must not erase historical landing scopes, because a receipt controls future API access rather than reversing committed territorial history.

Do not add a parallel DHR-only ledger or recover a global `every_state` scan.

The existing successful-commit helper remains the single registry writer.

### Parent resolution required now

The parent must patch the registry ownership before treating the Alien Infantry API or DHR revolt transfer as accepted.

The parent must update `common/scripted_effects/chaosx_dynamic_effects.md` in the same gameplay change so it describes a caller-owned country array rather than a global array.

The parent must promote the ownership rule into `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md` and add the cross-country scenarios below to `docs/specs/016_brilliant_scientist_specs/acceptance/016_alien_dhrondan_acceptance_scenarios.md` if this design is accepted.

### Acceptance evidence required

1. Give country A and country B independent valid source receipts, equipment reserves, and eligible targets.

2. Complete one ordinary Alien Infantry landing for each country and prove that each country registry contains only its own selected state.

3. Trigger country A's DHR revolt and prove that country A's registered state contributes to the marked-state and initial-cohort calculations while country B's state does not.

4. Prove that DHR transfers a country A state still owned by country A and adds only a claim when that country A state has been lost.

5. Prove that country B's state receives no DHR core, claim, ownership, controller, capital, or cohort consequence from country A's revolt.

6. Repeat the test with one ordinary provider and the Event 019 provider so the deferred commit cannot cross-register a state.

7. Call the registration helper twice for the same successful transaction and prove the scoped array remains idempotent.

8. Revoke a receipt after a successful landing and prove the committed state remains in its original caller's registry but no new landing can be initiated through that receipt.

## Severity-two finding: a successful Portal beachhead has no exact post-outcome lifecycle owner

### Evidence

The native raid definitions in `common/raids/016_brilliant_scientist_portal_raids.txt` correctly own preparation, reservation, outcomes, cooldowns, history, and destruction of the assigned formation before reconstruction.

Successful and critical outcomes call `brilliant_scientist_portal_raid_establish_beachhead` at lines 231, 255, 468, and 495.

The helper at `common/scripted_effects/016_brilliant_scientist_raid_effects.txt:53` sets `brilliant_scientist_portal_beachhead_active` and `brilliant_scientist_portal_raid_breach_recorded` on the target state, changes the selected province controller, and creates the fixed Portal Breach Cadre.

The selected province is available only as a temporary raid variable during the outcome and is not persisted as the breach identity.

The target state does not persist the actor or original defender alongside the active marker.

A repository-wide consumer search found no transition or cleanup owner for `brilliant_scientist_portal_beachhead_active`.

The state flags `brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, `brilliant_scientist_portal_facility_extracted`, and `brilliant_scientist_portal_factory_extracted` also have no clear path, but their semantics and existing handoffs support permanent historical evidence rather than transient state.

### Consequence

The state can remain marked active after the exact breach province returns to the defender, after the relevant war ends, or after the attacker or defender becomes invalid.

The current state-level marker cannot distinguish two breach provinces if multiple successful raids target the same state.

Native raid `days_re_enable` controls raid reuse and does not own territorial cleanup after a successful outcome.

Adding an arbitrary expiry would erase a real surviving foothold and would conflict with the accepted decision to preserve raid history.

### Required design

The native raid framework remains the sole owner of preparation, reservation, cancellation, outcome selection, cooldown, and native raid history.

`brilliant_scientist_portal_raid_establish_beachhead` becomes the sole commit point for post-outcome beachhead state.

At commit, persist the exact breach province, attacking country, and original defending country in state-scoped values that remain resolvable after the raid effect chain ends.

Register the affected state in bounded actor-owned and defender-owned active-beachhead arrays so terminal cleanup never requires a daily, weekly, monthly, or global state scan.

Prevent a new Portal beachhead raid from selecting a state with `brilliant_scientist_portal_beachhead_active` until that breach is resolved.

Only one active breach may exist in a state.

Expose one normal state-targeted defender action named `brilliant_scientist_seal_portal_beachhead` after the original defender has regained control of the saved breach province.

The action lasts 21 days, costs 25 Command Power once, and cancels without clearing the breach if the defender loses the saved province before completion.

The action is unavailable while the attacker still controls the saved province.

AI should take the action with base willingness 100 whenever it is valid and has the required Command Power because it closes a hostile breach after territorial recapture rather than choosing between strategic branches.

The AI weight is provisional until inspected and evaluated through the mandatory probability workflow.

Successful sealing calls one idempotent cleanup helper that clears the active flag, exact province, actor, defender, and active-array membership.

The same helper must be callable by bounded war-end, actor-invalid, defender-invalid, and Event 016 terminal cleanup owners.

The parent must verify an engine-supported bounded war-relation hook before implementing automatic war-end cleanup.

If no supported hook can identify the saved relationship without polling, war-end cleanup remains blocked and must not be replaced by a whole-world on action.

Cleanup must not refund teleportation equipment, recreate or destroy formations, repeat extraction, reverse building removal, clear native raid history, or clear any permanent historical marker.

`brilliant_scientist_portal_raid_breach_recorded`, `brilliant_scientist_portal_raid_targeted`, `brilliant_scientist_portal_facility_extracted`, and `brilliant_scientist_portal_factory_extracted` are permanent history and are not lifecycle defects once that policy is promoted into the specs.

The state-targeted action uses the normal decisions interface and does not justify a dedicated scripted GUI.

### Parent resolution required now

The parent must accept, reject, or queue this lifecycle design explicitly before adding a cleanup patch.

If accepted, promote the transient-versus-permanent policy, exact saved identities, one-breach-per-state rule, sealing action, and cleanup contract into the applicable Portal Raider specifications and decision or mission map before implementation.

If queued, record the named future containment owner and leave `brilliant_scientist_portal_beachhead_active` as an acknowledged unresolved acceptance gap.

Do not claim Portal lifecycle completion while the active marker has no owner.

### Acceptance evidence required

1. Complete a successful beachhead raid and prove that the exact province, actor, defender, active state, and bounded registries agree.

2. Prove the assigned raid formation is destroyed once and one fixed Portal Breach Cadre is created once.

3. Prove the same state cannot receive a second active breach.

4. Prove the sealing action is hidden while the attacker controls the saved province.

5. Return the saved province to the defender, start the action, lose the province before day 21, and prove cancellation preserves the active breach.

6. Repeat without losing the province and prove the 25 Command Power cost is paid once and cleanup executes once.

7. Call the cleanup helper again and prove it is idempotent.

8. End the relevant war with an active breach and prove the supported bounded terminal owner clears transient state without touching permanent raid or extraction history.

9. Invalidate the attacker and defender in separate scenarios and prove the same cleanup contract executes without a global scan.

10. Prove cleanup neither refunds raid equipment nor changes extracted facilities, factories, native raid history, or unrelated state flags.

## Severity-three finding: five DHR support-route markers remain disconnected

The current 88-focus topology is complete and the accepted regime routes have direct rewards and existing downstream country or decision effects.

The 2026-08-26 route-consumer tranche connected the four world-order markers that gate real decisions.

Five support markers still have no downstream consumer:

| Marker | Writer | Current direct reward | Disposition |
| --- | --- | --- | --- |
| `dhrondan_alien_components_standardized` | `DHR_standardize_alien_components`, `common/national_focus/016_dhrondan_focus_tree.txt:592` | Laser-production helper | Remove the dead marker or document it as a reserved external API hook. |
| `dhrondan_laboratory_route_complete` | `DHR_a_two_world_research_complex`, line 641 | Laboratory-capacity helper | Remove the dead marker or document it as a reserved external API hook. |
| `dhrondan_predictive_warfare_perfected` | `DHR_perfect_predictive_warfare`, line 795 | Custom technology and predictive-command effects | Remove the dead marker or document it as a reserved external API hook. |
| `dhrondan_orbital_office_reassembled` | `DHR_reassemble_the_orbital_office`, line 812 | Orbital-support helper | Remove the dead marker or document it as a reserved external API hook. |
| `dhrondan_access_map_exchange_ready` | `DHR_exchange_maps_for_access`, line 953 | Diplomatic-credit helper | Remove the dead marker or document it as a reserved external API hook. |

These flags do not justify five more decisions or another route layer because the focuses already deliver their promised rewards.

This cleanup is safely queued after the severity-one registry fix.

The parent should prefer removal unless another package already has an accepted consumer contract.

## Hard blocker: Alien Infantry runtime acceptance remains incomplete

`docs/assets/016_brilliant_scientist/models_3d/alien_infantry/job.yaml:218` records `partial_quaternius_idle_move_attack_exported_reimported_runtime_blocked`.

Idle, move, and laser attack have exported and actual-byte reimported evidence.

Laser attack is not runtime wired because no supported stable muzzle locator is available.

Defend and death candidates were rejected, while support attack and retreat remain blocked.

The required distinct seven-action package, particle, light, audio synchronization, entity wiring, and runtime acceptance therefore remain incomplete.

This is not a design gap and must remain with the 3D pipeline owner.

No fallback, semantic action alias, transform-only animation, unsupported locator, or incomplete entity package is accepted by this addendum.

The parent must keep gameplay runtime acceptance blocked until the model package meets its existing gates.

## AI and probability evidence disposition

The mandatory probability route was started through `chaosx_ai_probability_auditor` for Alien Infantry landing and revolt inputs, DHR focus selection and route-support priorities, DHR decision and mission scores, and Portal Raider lifecycle behavior.

The auditor did not return before the parent-directed handoff deadline and was interrupted rather than delaying this addendum.

No weighted patch is accepted on the basis of that incomplete pass.

Existing 2026-08-25 DHR probability evidence confirms the scripted revolt tiers produce 0/100, 10/90, 20/80, and 40/60 revolt-versus-loyal outcomes in the evaluated scenarios.

The same handoff records incomplete focus, research, special-project, Event `.49`, landing adapter, and decision or mission surfaces.

The direct Portal probability inspection recorded in `016_portal_lifecycle_patch_2026-08-26.md` returned `INTERNAL_ERROR` and produced no usable artifact.

The proposed sealing-action willingness of 100 is therefore provisional and requires `hoi4.probability_inspect`, named human and AI scenarios, evaluation, and comparison after any owner-applied implementation.

No probability conclusion may be inferred from source-only inspection where the adapter route remains incomplete.

## MCP inspection and rendering evidence

Current same-day focus evidence already covers the accepted DHR tree after the route-consumer tranche.

`hoi4.focus_inspect` and `hoi4.focus_render` found 88 focuses, 102 connectors, zero crossings, zero intersections, zero DHR-specific diagnostics, and a stable rendered layout.

The exact artifact references are preserved in `016_dhr_route_consumers_2026-08-26.md` and `016_dhrondan_focus_audit_2026-08-25.md`.

The focused Event 019 inspection recorded in `016_alien_api_reconciliation_2026-08-26.md` produced partial state-flow evidence but could not project deferred scripted-effect boundaries as runtime proof.

The DHR country map audit inspected and rendered a selected static state, but the map adapter cannot execute the dynamic registered-state transfer transaction.

A fresh combined read-only event, focus, and map inspection batch was attempted during this pass, did not return within the bounded window, and was terminated at the parent's instruction not to delay the handoff.

Source inspection is not treated as replacement engine evidence for the new registry defect or the proposed Portal lifecycle.

Portal Warfare uses the native raid interface and the proposed sealing action uses the normal decisions interface, so no dedicated scripted GUI surface is in scope and GUI rendering is not applicable.

No new technology or doctrine tree surface is introduced by this addendum.

The installed package has no standalone Technology Tree Viewer, and the partial technology adapter evidence recorded by the DHR country audit remains a limitation rather than acceptance proof.

The active Portal breach is dynamic province control rather than a static map rewrite, so no declarative map rewrite is authorized or proposed.

## What the parent must resolve now

1. Replace the global Alien Infantry landing registry with caller-owned country-scoped registry behavior and rerun the cross-country acceptance matrix.

2. Decide and promote the Portal transient lifecycle contract before implementing cleanup, or explicitly queue it under a named future containment owner.

3. Keep the four Portal raid and extraction history markers permanent and document that policy instead of clearing them with the active breach.

4. Keep Alien Infantry model and runtime acceptance blocked until all existing action, muzzle, synchronization, entity, and reimport gates pass.

5. Rerun the required probability audit after any weight-bearing implementation and compare the same named scenarios before accepting changed tuning.

6. Do not mark Event 016 complete while severity-one registry isolation, the Portal active-state disposition, model runtime acceptance, and required engine evidence remain unresolved.

## What is safely queued or blocked

### Safely queued

- Remove or explicitly reserve the five unconsumed DHR support-route markers.
- Revisit generic DHR route-support AI priorities only after a complete focus-selection probability audit.
- Run final localisation, documentation, spreadsheet, and completion-audit reconciliation after the ownership fixes are implemented.

### Blocked

- Alien Infantry complete runtime acceptance is blocked by missing required actions, a supported muzzle locator, synchronization, and final entity wiring.
- Fresh post-change probability acceptance is blocked until the owner applies any registry or Portal lifecycle patch and the probability adapter completes.
- Dynamic map acceptance is blocked by the read-only adapter's inability to execute the revolt transaction and must not be replaced by static-state inference.
- Automatic Portal war-end cleanup is unresolved until the parent verifies a bounded engine-supported relation hook.

## Scope exclusions

Do not add another DHR route, another regime family, a second DHR country, a formable, a dedicated GUI, another raid family, or a super-event in response to these findings.

Do not add a second landing ledger beside the Alien Infantry API registry.

Do not add a global on-action scan for either landing states or Portal breaches.

Do not add arbitrary timed expiry to a live Portal foothold.

Do not connect the five support markers to shallow duplicate decisions merely to make the flags appear consumed.

Do not weaken any model or animation acceptance gate to close the documentation package.

## Promotion and closure rule

This file remains in `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/` until the parent dispositions both ownership findings.

If the registry design is accepted, promote its caller-owned array contract and cross-country scenarios into the Alien Infantry and DHR binding spec and acceptance document.

If the Portal lifecycle is accepted, promote it into the binding Portal Raider event, raid, and decision or mission specifications, then document the public cleanup helper in the permanent Portal Raider API documentation.

After implementation, rerun the event, focus, map, decision, country, localisation, completion, and probability audits that touch the changed identifiers.

The parent may restore the earlier broad closure only when the severity-one registry defect is fixed, the Portal lifecycle is implemented or explicitly queued with an owner and reason, the model/runtime gate remains honestly dispositioned, and no newly accepted addendum remains unresolved.

No gameplay, asset, spreadsheet, or skill file was edited by this planning pass.
