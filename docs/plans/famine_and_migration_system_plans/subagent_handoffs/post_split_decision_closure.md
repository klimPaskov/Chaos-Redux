# Post-split decision closure handoff

> **Superseded incident-layer banner (2026-08-25):** Any incident-event, event-option, `famine_incident.1`, or `migration_incident.1` wording in this historical handoff is superseded. Current register helpers are accounting/presentation seams only, and the incident event files and constants were deliberately deleted.

> **Superseded historical identifier banner (2026-08-25):** Any `famine_incident.1`, `migration_incident.1`, or incident-option identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities document accounting/presentation seams only and the deliberate deletion of the incident event files and constants.

Owner: `/root/post_split_decision_closure`.

Scope: famine and migration decisions, the famine decision-owner trigger file, and decision-local audit evidence only.

## Outcome

The famine category keeps its existing phase lifecycle and now has four country-level response-role selectors that bound visible primary decisions to six or fewer in every combination of the accepted state-target roles.

The famine-to-migration evacuation adapter remains intact and still uses `migration_country_has_free_mission_slot`, `migration_mission_timing.evacuation_protection_days`, and `migration_claim_mission_slot`.

The relief-route repair decision now requires the canonical `civilian_transfer_route_damaged` proof in `visible`, `available`, `target_trigger`, and `remove_effect`, so a positive railway level alone cannot authorize repair or clear an intact route.

Four context-free condemnation calls were removed from decision-owned effects because their owner adapters require exact persisted proof bundles that these decisions do not own.

## Issues sorted by severity

High: `famine_repair_relief_route` previously treated any positive railway level as a repair target and unconditionally cleared the route-damage flag on removal.

High: the famine category had ten ordinary visible decisions with overlapping state-target conditions and no country-level role mutual exclusion, allowing more than six primary actions in a valid multi-state crisis.

High: `humanitarian_condemn_concealment`, `humanitarian_condemn_deliberate_starvation`, `humanitarian_condemn_violent_pushback`, and `humanitarian_condemn_forced_return` are not the current owner adapter contracts and did not supply their required exact receipt proof.

Medium: `common/scripted_effects/migration_destination_selection_effects.txt:149` still reads obsolete `migration_route_damaged`; this is outside the decision/trigger ownership granted for this patch and remains a parent-owned blocker.

Medium: `events/famine_incidents.txt` option `famine_incident.1.b` can call `famine_incident_suspend_extraction` without a state extraction check, and option `famine_incident.1.c` can call `famine_incident_conceal_shortage` without a concealment target check.

Medium: `events/migration_incidents.txt` options `migration_incident.1.b` and `migration_incident.1.c` have no context trigger before their departure-policy effects, so their state effect may be a no-op while the option-level political-power or stability changes still apply.

Low: GUI inspection is repository-wide and reports unrelated index-collision and diagnostic-truncation errors, so the existing shared scripted GUI cannot be treated as clean evidence for pixel fidelity.

## Changed files and identifiers

- `common/scripted_triggers/famine_decision_owner_triggers.txt`: added `famine_decision_has_reserve_response_target`, `famine_decision_has_sea_relief_target`, `famine_decision_has_evacuation_response_target`, and `famine_decision_has_concealment_response_target`.
- `common/decisions/famine_decisions.txt`: added role gates to `famine_emergency_airlift`, `famine_invite_relief`, `famine_requisition_safer_state`, and `famine_maintain_extraction`, and aligned `famine_conceal_crisis` visibility with its existing government availability requirement.
- `common/decisions/famine_decisions.txt`: tightened `famine_repair_relief_route` to canonical route damage and proof-gated its clear, relief-access mark, mission arming, and achievement receipt.
- `common/decisions/famine_decisions.txt`: removed the two missing famine condemnation calls without changing the concealment or extraction gameplay effects.
- `common/decisions/migration_decisions.txt`: removed the two missing migration condemnation calls and their orphaned temporary death-count assignments without changing transfer finalization, cleanup, or outcome effects.

## Decision category lifecycle notes

`famine_decision_category` remains hidden until `famine_decision_problem_is_active` finds a real food-stage problem or an owner phase flag, and `visible_when_empty = no` remains in force.

The existing famine phase flags are `famine_decision_emerging`, `famine_decision_active`, `famine_decision_resolution`, and `famine_decision_dormant`; the new selectors operate inside the existing problem/phase gate and do not create a combined famine-migration namespace.

`migration_decision_category` remains a separate category driven by `migration_decision_emerging`, `migration_decision_active`, `migration_decision_resolution`, and `migration_decision_dormant` through its existing owner triggers.

The migration category has four dedicated missions and keeps its owner-local mission flags and timing constants; no migration mission lifecycle or adapter contract was changed here.

## Famine cognitive-load and six-action proof

The visible famine primary actions are partitioned into six role slots rather than deleted: reserve or diplomatic land response (`famine_release_reserves` versus `famine_invite_relief`), direct land imports (`famine_emergency_imports`), route repair (`famine_repair_relief_route`), maritime response (`famine_escorted_relief_convoy` versus `famine_emergency_airlift`), movement (`famine_evacuation` versus `famine_requisition_safer_state`), and governance (`famine_conceal_crisis` versus `famine_maintain_extraction`).

`famine_decision_has_reserve_response_target` hides `famine_invite_relief` while any exact reserve-release target exists, so the reserve and diplomatic-land roles cannot add two entries to the same state combination.

`famine_decision_has_sea_relief_target` hides `famine_emergency_airlift` while any exact sea relief target exists, leaving airlift available as the fallback maritime role when no sea route is proven.

`famine_decision_has_evacuation_response_target` hides `famine_requisition_safer_state` while any evacuation target exists, leaving requisition available when evacuation is not a valid response.

`famine_decision_has_concealment_response_target` hides `famine_maintain_extraction` while an authoritarian concealment target exists, leaving extraction visible for wartime states without a proven concealment role.

The role selectors use `any_controlled_state` and mirror the existing target contracts, so they do not scan the world or invent a second state registry.

The six-slot proof is independent of how many controlled states provide candidates: each paired role contributes at most one visible identifier, while the unpaired import and repair actions contribute one each.

The famine category description already presents phase, food stage, reserves, relief access, and current priority through scripted localisation; no raw value dump or new player-facing value was introduced.

The migration category description separately presents phase, displacement load, reception capacity, border policy, and current priority; this patch did not merge those values into the famine category.

## Mission quality notes

`famine_mission_secure_relief_route` is famine-owned, state-scoped, requires `famine_mission_route_active`, a subject state, a deadline, and `famine_mission_route_success_proven`, succeeds only after the deadline with `civilian_transfer_route_damaged` absent, times out with stability and war-support penalties, and clears subject, proof, deadline, country flag, and mission-slot count on success, timeout, or cancellation.

`famine_mission_deliver_relief_before_reserves_fail` is famine-owned, state-scoped, requires `famine_mission_relief_active`, an exact subject state, deadline, reserve amount, and relief proof, succeeds only with reserve and food-pressure thresholds, times out with stability and war-support penalties, and clears its state variables and mission slot on every terminal path.

`migration_mission_hold_humanitarian_corridor`, `migration_mission_protect_evacuation_transport`, `migration_mission_prevent_reception_collapse`, and `migration_mission_prepare_safe_return_route` remain migration-owned with explicit state/cohort requirements, constant-backed timeouts, success and timeout effects, and owner-local cleanup; no duplicate mission flag or timing change was introduced.

All reviewed mission surfaces are non-selectable and use bounded owner slots; unresolved duplicate-risk is limited to the pre-existing incident-to-decision handoff, not a new mission activation path in this patch.

## Cost and requirement clarity

Famine decisions remain at three or four distinct spendable cost types: political power plus equipment and fuel for ordinary actions, with escorted convoy adding support equipment and airlift adding transport planes plus air experience.

`localisation/english/famine_l_english.yml:50-59` uses scripted texticon getters for every displayed spendable value, including the four-cost escorted convoy and airlift strings; no literal resource label was added.

Migration decision costs were not changed; the inspected set remains at no more than four spendable types, with medical reception and third-country resettlement being the four-cost upper cases.

Non-consumed requirements such as state safety, exact cohort proof, air-base availability, or route deadlines remain in trigger tooltips and are not silently converted into costs.

The repair requirement is now an authoritative state damage proof rather than a generic railway-level requirement, which aligns its visible requirement, target validity, and completion cleanup.

## AI validity and route-lock notes

No AI weights or probability-bearing factors were changed, so no new AI target or rank outcome was introduced by the role gates.

The famine AI blocks still use the existing constant-backed scores and exact state target triggers; hidden role siblings remain valid fallback decisions for subsequent state conditions rather than being deleted.

The famine-to-migration evacuation path still claims a migration mission slot only after exact transfer finalization and positive survivor credit, and it uses the migration timing/slot helpers supplied by the migration owner.

The canonical route flag is now used by the repair decision and the existing secure-route mission; the remaining obsolete consumer is the out-of-scope destination-selection effect noted above.

## Localisation and tooltip gaps

No new player-facing identifiers were introduced, so no localisation file change was required.

Existing category localisation remains phase-aware and uses concise state summaries; the new role selectors are hidden implementation triggers and do not require localisation keys.

The incident options remain a separate event-owned gap because their context-dependent no-op behavior cannot be corrected from a decision visibility block.

## Cleanup and exploit-risk notes

The repair removal effect now awards relief access, arms the route mission, and records the alternative-logistics achievement only inside the canonical damage-proof branch, preventing an intact route from being cleared or rewarded.

The condemnation call removal prevents an undefined or proofless effect from silently creating a source receipt; condemnation is intentionally pending until an owner caller persists the exact adapter bundle.

The existing mission success, timeout, cancellation, flag-clear, variable-clear, and slot-recount hooks were preserved.

Incident option no-op risks remain outside scope and should be fixed by adding state-context triggers or fail-closed option effects in the event-owned files.

## MCP evidence and fidelity findings

Probability source discovery artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3dba5e9beb70c3bd5c272f44b7dbe33ff0dcc87ef35bf4b17eb05947eea9a336/205440c14efcd670f3335da8624432820a4cb011a0a0b52910e8ea7f6dd4f018/probability-inspect-f9b797679fcf.json`.

Probability source inspection artifact for the ten famine decision IDs: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dd8165dac5489c831e3af57179bd860b9bd7bf42bbbeacf39da889091b6b637c/4605ea19e56ce99c164d8c5771c1e09a02940779eebfc67365046d66fe2207e2/probability-inspect-f9b797679fcf.json`.

The probability adapter inventory found `mission_ai_will_do` as the compatible weighted surface but no current candidates under the supplied source-only state, and no AI weight was patched; a probability compare was therefore not applicable to this visibility-only change.

Decision-specific MCP inspection is blocked because no `hoi4.decision_inspect` route is exposed in the installed tool inventory; the available weighted-source inspect was used instead and this source-only limitation is recorded.

Famine category GUI inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fd4fa8209bb7318584594d9d0143d5f35f52cdd10cf497b0f371a2f9a90dbd93/df6ea96536d073277f5efccbf6f3ec330230b75cdedc38f8502b5b3d83964818/gui-inspect.f629114b286b5b1a.json`.

Existing famine header scripted GUI inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3f04c68b34132119170c13e59c53648c790d40d7a533204359706d53be7dc666/8c64cc482b18fd19e7a047876320e3f495395004fd4a79bb0597b5a4814a1bfd/gui-inspect.f629114b286b5b1a.json`.

Famine category render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad693051604097ec88bc117aa5c4492c43f59b5ed4c7457b8981a18aa12b3d08/2d7b9237b89b9c4566779c8d1e42b091a952147e2929a0274d167441b6b3fa20/decision_category-full.svg`.

Existing famine header scripted GUI render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58d26352dfe0e2a7668e3692afe868ee8d2bf62f787b65872dfdbdf2a3d7aaf0/db6410dbab9f4c5bdbfd6bcac034bf4c5b93f53eb353356419b0b25b770fa6bf/famine_report_header_scripted_gui-full.svg`.

Both GUI inspections completed with the existing shared GUI source graph, but the MCP returned 2,000 retained blocking diagnostics dominated by unrelated index collisions and truncation; fidelity was approximated/missing rather than authoritative for the decision rows, and no GUI rewrite was requested or performed.

## Validation, skipped checks, and remaining work

Task-specific validation found balanced braces in the three touched script files, no remaining context-free condemnation names in either owned decision file, canonical route-flag references in the repair decision, and all four role helper references wired to their intended decisions.

The existing famine cost localisation was rechecked and every displayed spendable value uses a scripted texticon getter.

Skipped validation: no live Hearts of Iron IV launch was performed per repository instructions, no event files were edited because incident options are outside this decision-owned patch, no GUI rewrite or post-rewrite comparison was needed, and no probability compare was run because no AI weight changed and the source-only candidate pool was empty.

Remaining parent-owned work is to replace the obsolete `migration_route_damaged` consumer at `common/scripted_effects/migration_destination_selection_effects.txt:149`, decide where the exact famine/migration condemnation receipt bundle should be authored, and add fail-closed context triggers to the two incident option sets if their no-op behavior is not accepted.

Handoff path: `docs/plans/famine_and_migration_system_plans/subagent_handoffs/post_split_decision_closure.md`.
