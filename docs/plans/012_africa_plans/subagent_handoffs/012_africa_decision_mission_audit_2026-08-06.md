# Event 012 Africa decision and mission audit

Date: 2026-08-06.

## Outcome

The active Charter runtime is one quoted action ledger, not 102 independent political-power stores.

The audited matrix has 102 unique action IDs from 1 through 102, and every row has a selector, action constant, profile dispatch, duration/objective dispatch, and full, partial, and failure receipt.

The acceptance ledger currently classifies 96 action concepts as `implemented` and Actions 71 through 76 as `blocked_with_gate`.

Two narrow fixes were applied: the RSA first-proof mission now uses the vanilla-supported `var:` dynamic timeout syntax, and four existing sponsorship fulfilment result tooltips now appear before their decision effects run.

No decision-owned GUI rewrite was made.

## Files changed and identifiers

- `common/decisions/012_africa_rsa_decisions.txt`: `africa_rsa_first_proof_mission` now uses `days_mission_timeout = var:africa_rsa_first_proof_days`.
- `common/decisions/012_africa_decisions.txt`: `africa_world_fulfil_diplomatic_sponsorship`, `africa_world_fulfil_material_sponsorship`, `africa_world_fulfil_military_sponsorship`, and `africa_world_fulfil_ideological_sponsorship` now call their existing `custom_effect_tooltip` keys.
- `docs/plans/012_africa_plans/subagent_handoffs/012_africa_decision_mission_audit_2026-08-06.md`: this handoff.

Before the RSA change, the mission used a bare variable token even though the same value is set as a scoped normal variable.

After the change, it uses the `var:` form used by vanilla dynamic mission durations, including `CHI_improving_neglected_countryside_mission_time` in `common/decisions/CHI_decisions.txt`.

Before the sponsorship change, all four actions had localisation that described their result, but none invoked those tooltips from their `complete_effect` blocks.

After the change, the material action exposes its one-time infantry-equipment, support-equipment, and convoy delivery, while the other three expose their mediation, defence-compact, and congress outcomes.

## Issues, sorted by severity

### High: three decision refreshes still iterate every country

`africa_refresh_bounded_african_target_roster` and `africa_refresh_bounded_external_target_roster` in `common/scripted_effects/012_africa_effects.txt` use `every_country` to fill the player roster.

`africa_refresh_priority_member_natural_disaster_targets` in `common/scripted_effects/012_africa_action_effects.txt` likewise uses `every_country` to build the priority member's hostile-enemy roster.

They are explicit decision effects rather than periodic on-actions and each uses an array-cap guard, but they remain whole-world iterations.

Repository guidance requires explicit approval before such an iteration is retained or introduced.

Do not replace these with an unbounded alternative in this audit.

The parent needs to either explicitly approve these three player-initiated scans or commission a bounded roster-source redesign under `docs/plans/012_africa_plans/`.

### High: row-specific targeted mission duration is not backed by a vanilla `FROM` precedent

The four shared missions `mission_africa_action_short`, `_medium`, `_long`, and `_epic` read `days_mission_timeout = FROM.africa_active_action_duration_days` in `common/decisions/012_africa_decisions.txt`.

The target record correctly snapshots each matrix row's default duration, minimum, maximum, and objective before the mission is activated.

Vanilla confirms dynamic mission timers with `var:<variable>` and tag-qualified variables, but this audit found no vanilla `days_mission_timeout = FROM.<variable>` precedent.

The existing duration contract document already records parser confirmation as outstanding.

Changing this safely would alter the shared targeted-mission architecture, so this audit does not substitute a fixed timer or weaken row-specific duration contracts.

Runtime parser and displayed-duration evidence remains required before accepting the 102-row timer contract as engine-proven.

### Medium: Event 012 Charter GUI MCP target evidence remains unavailable

The target `hoi4.gui_inspect` call for `africa_charter_window` returned `INTERNAL_ERROR` without an artifact.

The target `hoi4.gui_render` call for the normal, disabled, locked, empty-list, full-list, and long-text states at 1920 by 1080 and 1366 by 768 timed out after 180 seconds.

The broad workspace inspection did complete, but it is not an Event 012 visual-fidelity substitute.

Source review found no gameplay execution hidden in the GUI, so no blind GUI rewrite was appropriate.

### Intentional gated content: Actions 71 through 76 are unavailable by design

Actions 71 through 73 remain behind `africa_fictional_pathogen_review_authorized`, which has no approved setter or Event 013 disease API.

Actions 74 through 76 remain behind `africa_strange_formation_package_ready`.

The recently added strange-force data package deliberately provides no ready-gate setter, template consumer, or free-unit fallback while model and entity acceptance remains incomplete.

These are real completion blockers, not defects to bypass with a generic unit, target, or weather fallback.

## Decision category lifecycle notes

`africa_charter_council_category` owns the human cursor, selected action, re-quoted cost, state selection, launch decisions, and the four shared target missions.

The lifetime is select family or action, choose one bounded target or host, generate a quote, revalidate at launch, reserve and pay, copy an immutable record to the target, activate one shared mission when needed, resolve full, partial, failure, or cancellation, then clear the record and release capacities.

The categories for protection, accession, congress, integration, economy, diaspora, rival blocs, high chaos, Scramble, world order, constitutional crises, post-unification, host recovery, and regional restorations only select a profile and do not create their own parallel stores.

Action 102 `promote_priority_member_package` remains a normal regional-restorations selector and exact target validation path, with no duplicate Charter-window page or separate promotion store.

`africa_priority_member_category` has a distinct package, political-settlement, League-role, overlap, withdrawal, mechanic, reinforcement, and post-settlement lifecycle.

`africa_rsa_crisis_category` retains its first-proof and post-victory recovery lifecycle, separate from the generic 102-action runtime.

## Mission quality notes

| Owner and category | Region and requirement | Duration and success | Failure, cancellation, and duplicate risk |
| --- | --- | --- | --- |
| Host, Charter Council shared short/medium/long/epic missions | Exact active target from one of the four duration arrays, current host generation, exact objective, and current state target where required | Row-specific target snapshot supplies duration and objective, then `africa_resolve_action` applies full or partial results | Cancels on Event 012 closure, stale host generation, target capitulation, or target loss; cleanup removes the exact mission/array entry and returns reservations, preventing duplicate active records |
| Priority member withdrawal mission | Priority package, withdrawal flag, and leaving or rival relationship | Constant withdrawal window; peaceful completion renews no relationship and moves to the departure outcome | Cancels when withdrawal/relationship context vanishes and uses `africa_priority_member_cancel_withdrawal`; no repeatable mission spawn is exposed |
| RSA first-proof mission | Continental-coalition civil-war corridor proof | `africa_rsa_first_proof_days` set by the RSA initialization contract; secure corridor completes the proof | Civil-war or coalition loss cancels, and timeout fails the proof; cleanup removes any active mission before crisis teardown |
| Scramble recognition, coalition, intervention, and aftermath windows | The current Scramble phase only | Phase constants advance recognition to coalition, coalition to intervention, and intervention to aftermath | A phase change cancels the old window; unresolved intervention launches its constrained expedition outcome, while aftermath either ratifies, closes, or records prolonged negotiation |
| World sponsorship obligation missions | Installed target package and current sponsorship mode | One public obligation window with material, diplomatic, military, or ideological fulfilment | Default converts the package into the recorded rival outcome, removes the targeted obligation, and clears the bounded target entry |

## Costs and requirement clarity

The Charter quote derives costs from profile component flags and central action-cost constants rather than assigning flat political-power exchanges per action.

The re-quote formula considers the target's factory and state scale, selected-state count, burden, pressure, active action count, confidence, overlay, route, access, and war risk, then clamps the multiplier before payment.

Payment and availability cover political power, command power, manpower, fuel, stability, war support, infantry equipment, support equipment, motorized equipment, trains, convoys, civilian capacity, and intelligence capacity.

Weather actions add a separately reserved caller cost before launch and share the same action record, so the normal commitment and Event 013 cost cannot diverge after the player confirms.

Action 102 evaluates the selected target's promotion conditions before the action begins, rather than treating the selector as a free country-package grant.

The sponsorship patch makes the existing four fulfilment outcomes visible at the moment of commitment without changing their cost, requirement, or effect logic.

## AI validity and route-lock notes

Individual Charter selectors correctly use zero AI weight because the host controller dispatches through `africa_ai_run_profiled_action_cycle`, the bounded early-action pool, and the existing late Actions 77 through 92 pool.

The host controller revalidates the selected target, action-specific requirements, phase, quote cost, action capacity, and state cursor before it calls the shared launch effect.

Priority-member Rain and Drought AI refreshes the same hostile-enemy array used by the player, selects one valid enemy, and then enters the same host-owned record, reservation, cooldown, target recheck, Event 013 bridge, and cleanup path.

The natural-disaster bridge uses the exact selected enemy and rechecks active war, actor eligibility, reserve, and cooldown before calling Event 013.

No fallback target is selected after the quoted target becomes invalid.

The required independent probability audit was routed to `chaosx_ai_probability_auditor` for the profile dispatcher, target selection, natural-disaster action selection, and outcome weights.

The auditor did not return scenario evidence or an MCP artifact after three 60-second waits and was interrupted rather than leaving this bounded audit indefinitely open.

No probability, balance, or relative-frequency conclusion is claimed from source review alone.

The parent must use its active Event 012 probability-audit handoff or rerun this exact route with `hoi4.probability_inspect` and same-scenario comparison evidence before accepting weighted AI balance.

## Localisation and tooltip notes

All 102 matrix selectors have a title and description in English localisation.

All 101 `custom_cost_text`, `custom_effect_tooltip`, and `custom_trigger_tooltip` keys referenced by the three Event 012 decision files resolve in English localisation.

The four sponsorship fulfilment tooltip keys already existed in `localisation/english/012_africa_world_sponsorship_l_english.yml`; this audit wired them rather than adding duplicate text.

The Charter GUI renders data labels, candidate selection, family-page selection, diaspora selectors, and state selection only.

It does not execute an action directly, so the normal decision launch buttons retain the single cost, tooltip, AI, and cleanup owner.

## Cleanup and exploit-risk notes

`africa_cleanup_action` removes the exact shared mission, all duration-band and active-target references, active project state flags, target-side action variables, natural-disaster reservation flags, and global target pointers.

It restores civilian and intelligence reservations, decrements active action count safely, writes the target cooldown, and preserves only the last action outcome and objective needed by result surfaces.

Annexation cleanup uses the generation receipt to avoid refunding a successor host and removes stale project state only when both generations match.

The priority-member natural-disaster route clears its explicit enemy roster, target validation flags, member-active flag, reserves, and global action-target pointers on both failed launch and normal cleanup.

The full Event 013 bridge applies its cooldown whether the nature call succeeds, is rejected, or the shared action resolves without reaching the bridge, preventing reserve/cooldown abuse.

No duplicate action store, free-unit loop, core-spam path, or hidden execute button was found in the audited decision surface.

## GUI MCP evidence and fidelity

Whole-workspace `hoi4.gui_inspect` completed with status `GUI_INSPECTED` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f7b5c1f94d5af036adb457349ce74587948ac8e962f2386fb28fb8527c2b8185/28863e212151fbdd5e8f092dfa5bcf7757b2a8741e3a26cb515ffc7b6d4f963a/gui-inspect.24884dade31da7fc.json`.

That artifact is workspace-global and contains unrelated diagnostics, so it is provenance evidence only.

The specific `africa_charter_window` inspect call failed with `INTERNAL_ERROR` and returned no artifact.

The specific render call timed out after 180 seconds and returned no render artifact.

Source evidence is `common/scripted_guis/012_africa_charter_scripted_gui.txt`, `interface/012_africa_charter_gui.gui`, and `localisation/english/012_africa_charter_gui_l_english.yml`.

No visual-fidelity conclusion is claimed until a target-scoped inspect and render complete.

## Validation and remaining work

The matrix reconciliation found 102 unique IDs, and all 102 rows matched a selector, constant, profile dispatch, duration/objective dispatch, and all three disposition receipts.

The 102 selector title and description keys were present in English localisation, and all 101 custom decision tooltip/cost keys resolved.

The two local patches were reviewed against the vanilla dynamic-mission precedent and their pre-existing localisation keys, then passed a scoped `git diff --check`.

No Hearts of Iron IV process was launched because live validation belongs to the user.

Meaningful validation still skipped: target-scoped GUI inspect/render is blocked as recorded above, the `FROM` mission-duration grammar needs engine evidence, and this subagent's required independent probability audit produced no MCP result before interruption.

## Simplifications, omissions, and blockers

No fallback, fixed-timer substitute, model-gate bypass, generic unit substitute, or additional decision system was introduced.

The six gate-blocked high-chaos actions remain unavailable until their approved external packages provide valid setters and consumers.

The three player-initiated whole-world target refreshes require parent approval or a separately designed bounded replacement before they can be presented as compliant with repository iteration policy.
