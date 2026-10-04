# Event 014 actual raid-target owner proposal

Date: 2026-10-04.

Disposition: accepted and queued.

Acceptance basis: the parent explicitly accepted the existing March state-target strike with the current preparation modifier, costs, duration, cooldown, and recoveries as full-field implementation on 2026-10-04, and set `0.50` as the damage amount in the existing fixed-point Warlord decision constants group.

The accepted requirement is the Event 014 part 6 field for a selected raid or infiltration target and its Warlord command raid-target card.

The target uniqueness and damageability checks below are implementation guards for the accepted action; target fixtures must prove their exact behavior before the owner patch.

The implementation is queued while `01a10386` owns the Event 014 effects, triggers, constants, and localisation patch through its commit, while `01a10385` completes the current-source probability baseline and target fixtures, and while the data worker's accepted receipt hooks are integrated.

This handoff is read only for runtime source and writes only this handoff plus its evidence under `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-10-04_actual_raid_target_owner_proposal/`.

## Recommended implementation

Adapt the existing `cannibalism_march_raid_supply_depot` decision into a native state-targeted action for an enemy supply-node state directly adjacent to a state controlled by the March Host.

The target state must contain exactly one `supply_node` and at least one non-damaged level; the installed building definition makes each supply node provincial, while state-scope `damage_building` searches the first matching province building.

When selected, apply the parent-accepted `0.50` `damage_building` amount to the sole supply node in that state, then apply the existing country-scoped March Supply Raid Operation as preparation and campaign support.

The installed `supply_node` definition omits the building `value` health field, so the receipt and tooltip report `0.50` damage units and do not call it 50 percent of health.

Record the stable selected state, operation kind, result, date, `ROOT` generation, and the controller's current country generation when it is a registered Event 014 actor through data worker `01a103a4-2c1c...`'s proposed receipt contract so `GetCannibalismUiRaidTarget` reads a real operation receipt.

The card should identify this as a March supply-hub strike and report the actual result; the source only damages the target's supply node, so the card and tooltip must not say the depot was seized or supplies were captured.

Keep the existing decision ID, two existing spendable cost types, cost amounts and gates, 30-day re-enable value, base operation duration and route bonuses, recovery contract, and AI expression.

Do not add a mission for this immediate target action; the target-state damage resolves in the paid decision transaction and the existing modifier remains the operation-preparation period.

The exact target-trigger, effect-order, receipt, stale-target, payment, and localisation patch map is in [proposed_source_patch.md](2026-10-04_actual_raid_target_owner_proposal/evidence/proposed_source_patch.md).

## Existing target audit

The best semantic reuse check was the paid `cannibalism_infiltrate_ritual_cell` decision, which already uses `state_target = yes`, a real `FROM` state, an affordability gate, a state-specific cooldown, and a state-specific effect.

That infiltration decision belongs to `cannibalism_containment_decisions_visible` during Evolution I and targets a `ROOT`-controlled state with an active cell and node generation; the Host Command Ledger belongs to a registered Warlord before the public reveal.

The ritual target is a real infiltration target for that ordinary containment action, but it is not the hostile supply target of the current March Warlord action; reusing it in the Host card would show a historical, different-kind action and would not provide a March operation target.

`cannibalism_unified_collapse_enemy_front` selects a real country target for the unified campaign route, while `cannibalism_wendigo_launch_terminal_hunt` selects a country for the separate post-reveal Wendigo mission; neither selects a supply-node state for this Warlord action.

The continental and naval hunt decisions start untargeted operations, convoy harvest consumes prior receipts, and battlefield harvest records a defeated country after victory rather than a paid raid selection.

The Warlord's state-targeted recruitment and controlled-state decisions prove a native map-selector precedent, but their selected states do not become raid targets.

## Issue list by severity

1. **Critical - the existing March action has no actual target or local outcome.** `cannibalism_march_raid_supply_depot` at `common/decisions/014_cannibalism_decisions.txt:2569-2588` has no `state_target`, `target_trigger`, or saved target; `cannibalism_begin_march_supply_raid_operation` at `common/scripted_effects/014_cannibalism_effects.txt:17109-17120` only pays the existing contract, grants the acting country a timed modifier, and applies focus-based recoveries.

2. **High - the accepted command card has no real target source.** `interface/014_cannibalism_frontline_hunger.gui:132-153` has no raid-target card, `common/scripted_guis/014_cannibalism_scripted_gui.txt:157-183` has no target getter binding, and current source has no `GetCannibalismUiRaidTarget` definition; the 2026-10-03 Data API view-only state selection is explicitly insufficient for this requirement.

3. **High - state-scope building damage can otherwise strike an ambiguous or fully damaged province building.** Vanilla `supply_node` is a province building, and installed `damage_building` documentation says a state target searches for the first matching province building; the proposal gates to one supply node and one non-damaged level before payment.

4. **High - an infiltration receipt is not an authentic current March target.** The paid ritual-infiltration selector is from a different phase, country role, and target kind; the card should display it only if the parent separately accepts a historical infiltration receipt and labels it as such.

5. **Medium - preparation and outcome are conflated by the present name and tooltip.** The current effect tooltip describes only the temporary operation modifier and route recoveries, while the decision title promises a supply-depot raid; the target strike and preparation modifier need distinct wording.

6. **Medium - target-candidate AI behavior and stale-target handling are unmeasured.** The current AI score is known, but a native per-state target pool changes candidate eligibility and distribution; the existing decision-inspection route returned partial coverage and no target candidates.

7. **Low - the inline cost repeats the literal word `Larder` after its custom texticon.** Both existing spendable values have matching texticons and the action has only two spendable types, but the redundant label should be removed when the owning localisation line is next changed.

8. **Evidence blocker - the current production GUI render is available as an artifact link but its PNG could not be read.** The exact resource error and inspect/render artifact references are recorded in the evidence file; no pixel review or visual acceptance is claimed.

## Category lifecycle

The decision appears in the existing Warlord decision category only when either the network or endgame command phase is open, the actor has the March Host origin, and March actions are open.

The existing `cannibalism_warlord_focus_march_raid_the_depots` unlock opens the depot-raid family; this proposal does not change focus integration or create another category.

The decision currently re-enables after the existing 30-day constant, while its base operation modifier lasts 30 days and existing focus contracts can extend that duration.

The Warlord command GUI is a player display; AI must use the same native targeted decision and the same target predicate.

The new card is informational and does not add another gameplay action, button, tab, or phase.

## Cognitive load and player-facing values

The current command window shows Larder, Frenzy, Alignment when Evolution II is active, and raised-formation capacity; its raid-target card is absent.

The new target card should expose one actual state, the action kind, and the committed result in a short line, with the operation-preparation duration in a separate concise tooltip.

Do not add raw state IDs, target scores, extra target counters, damage formulas, or an unrelated controlled-state selection to the card.

The target has clear significance because the selected state contains the enemy supply node that the paid action damages; the existing modifier separately describes the Host's preparation period.

The source-only current window shows no buttons, and this target extension adds none; the decision-category action count therefore stays unchanged.

The single normal render scenario did not provide Larder, Alignment, or formation-capacity values, so the MCP fidelity report leaves those visible values unresolved; their on-screen effect has not been pixel-reviewed in this proposal.

## Mission quality

No new mission is proposed because the selected state receives its outcome synchronously in the existing paid decision.

The operation owner remains the March Warlord; the target is a hostile supply-node state bordering a state controlled by that Warlord; the current 30-day preparation modifier remains the existing duration.

Success is a valid target strike followed by the existing preparation modifier and one durable target receipt.

If the target or owner generation fails the completion-time recheck, the effect must abort before payment; if a failure is detected after debit, it must refund the exact stored quote and suppress the modifier, recovery, and success receipt.

Partial success is not a separate branch for this immediate damage action; the receipt should say the supply node was struck, not that it was destroyed or seized.

The existing native 30-day re-enable value remains the sole operation cooldown; use a transaction-in-progress guard around payment and resolution to prevent a reentrant duplicate without extending the accepted cooldown to the full preparation duration.

## Cost and requirement clarity

The existing cost is Larder `35` plus command power `10`; the command-power affordability gate is `> 9.99`, and the payment helper debits each existing cost once.

`texticon cannibalism_larder_texticon` and `texticon command_power` are the matching displayed icons; there are two spendable types and no population, equipment, manpower, or hidden fifth cost.

No cost amount or cost type changes are proposed.

The new state requirements are non-consumed: a passable hostile state on the March Host's adjacent front, exactly one supply node in that state, and one non-damaged supply-node level at the time of availability and completion.

Use the existing cost predicate for display, availability, and payment; show the target requirement in concise text rather than exposing the raw scripted trigger.

## AI validity and route locks

The current AI score is base `60` in peace and `150` at war under the existing `2.50` urgent factor; the read-only auditor reports these as exact raw scores for declared scenarios, not selection probabilities.

Keep the existing base and war factor unchanged and give the AI no separate target-scoring path; use the same target trigger and completion-time validation as the player.

The hostile-owner and front-adjacency checks prevent peace-time, self-owned, allied, impassable, detached, and supply-node-free states from becoming candidates; the unique-node guard prevents the documented state-scope first-match behavior from hiding which hub receives the strike.

If an Event 014 country owns or controls the target, capture and recheck its live actor generation; a recycled tag must not resolve an old target receipt to the new actor.

The baseline candidate pool was reported incomplete and empty by the probability adapter, so it proves no dominance, starvation, or rank stability across actual candidates.

Because multiple-hub states are filtered to preserve an unambiguous state-level strike, the parent target fixtures must show whether any unique, damageable front hub is available; if the target pool is empty, record that gap and obtain an accepted exact-province path rather than reverting to an unfiltered first-match strike.

Before the state-target gate is applied, the parent must finish the current-source baseline for the target fixtures; after the owner patch, `chaosx_ai_probability_auditor` must compare the exact before and after decision sources with the same named scenario set.

The baseline two-case scenario names are `event014_march_raid_supply_depot_peace_costs_satisfied` and `event014_march_raid_supply_depot_war_costs_satisfied`; the four-case Larder sweep is identified by scenario hash `2b35d95f291835467efa6a8334395e69c05305077b3181e924f4636468d821bf` in the evidence record.

Do not invent the sweep's omitted scenario IDs or claim full target-pool coverage from these score-only results.

## Localisation and tooltip gaps

`cannibalism_march_raid_supply_depot_effect_tt` currently promises the March Supply Raid Operation and route bonuses but has no target or local outcome; update it only with the actual supply-node strike and separate preparation benefit.

Show success tooltip text only after the target strike succeeds; a stale-target abort or refunded result must not display success wording.

The card's target reader must identify a March supply-hub strike; any reused ritual infiltration result must retain its literal infiltration kind.

Remove the repeated literal `Larder` from the inline cost when updating its localisation, while preserving both cost texticons and the existing values.

Do not show a raw `event_target`, state number, generation number, score, or internal status enum to the player.

## Cleanup and exploit risk

Use a per-owner durable receipt through the accepted Event 014 data owner rather than a global event target; the execution-local `FROM` scope is not itself a persistent UI record.

Keep target state and both relevant actor generations with the receipt; on an invalid owner generation, show the stable state and historical result without resolving the reused country tag.

Clear the receipt with the existing Warlord slot or actor-generation reset and replace it only after a later strike succeeds; no periodic cleanup or world iteration is needed.

The state building has finite health and the current decision remains costed and cooldown-limited, so the proposal adds no equipment or population yield loop; repeated attacks still need a same-state repair/re-attack review during parent balance testing.

The existing operation recovery contract can award route-based Larder or equipment on focus unlocks, but those recoveries must not be described as loot from the selected target.

## Files, identifiers, and behavior handoff

This subagent made no runtime source, localisation, scripted-GUI, layout, or asset edits.

At the final read-only status check, the shared tree showed uncommitted modifications to the Event 014 effects, triggers, constants, and English localisation files in the source owner's stated write set; their current contents were not inspected or reviewed in this handoff.

The only gameplay identifiers in the proposal are the existing `cannibalism_march_raid_supply_depot`, `cannibalism_begin_march_supply_raid_operation`, and `cannibalism_march_supply_raid_operation`, plus provisional `cannibalism_warlord_march_raid_target_is_valid`, `cannibalism_warlord_decision.march_raid_supply_node_damage`, and `cannibalism_ui_record_march_raid_target` names.

The data reader remains the proposed existing `GetCannibalismUiRaidTarget`; the existing view-only selector must not be presented as a raid target.

Before: clicking the untargeted decision pays the existing Larder and command-power amounts, starts a country modifier, and may grant focus-based operation recoveries, with no target identity or state outcome.

After the proposed change: clicking a valid map-targeted enemy supply node pays the same amounts, damages that selected state, records that target and result, and starts the same modifier for the same current duration; invalid targets do not charge or publish success.

No additional raid-action family, event chain, category, mission, native raid type, or GUI system is proposed.

## Validation and remaining blockers

Completed read-only checks include exact source inspection, the required narrow `hoi4.decision_inspect` attempt, exact `hoi4.source_lookup`, a current-source probability baseline through `chaosx_ai_probability_auditor`, and matching-scenario `hoi4.gui_inspect` plus one `hoi4.gui_render` for the existing command window.

The probability baseline is score-only and has an incomplete candidate pool; no `probability_compare` was run because no source patch exists.

The GUI render artifacts were returned, but binary image reads failed twice with `MCP error -32603: Artifact provenance manifest is unavailable`; visual geometry, clipping, and click regions therefore remain unreviewed and no renderer defect is dismissed.

The exact-ID decision inspector returned a partial global index with 218 unresolved definitions; no broader retry was made after that required narrow attempt.

No game was launched and no runtime scenario, click, cost debit, building damage, or cooldown behavior was tested.

The parent-selected `0.50` damage amount is recorded, but its fraction of total supply-node health is unverified because the vanilla definition omits `value`; the target-gate candidate pool, single-node/non-damaged trigger fixtures, owner-generation refund path, native cooldown after an aborted completion, repeated strikes during repair, and pixel-level GUI review remain open.

The parent must finish and record the no-target, one unique damageable hub, multiple-hub state, fully damaged hub, recycled Event 014 controller, and resource-boundary fixtures before applying the decision target gate.

At the last status check, effects, triggers, constants, and English localisation were modified in the owner's stated write set, while the decision file remained clean; this subagent did not inspect those in-progress edits.

The parent should reconcile `01a10386`'s committed patch with this accepted target contract, apply or review the still-needed decision entry, and complete the same-scenario probability comparison before the UI worker implements the card.

The only plan handoff written is this file; no broader plan or new Event 014 mechanic is added.

## Parent reconciliation, 2026-10-04

Disposition: `implemented` in the March raid commit of the Event 014 takeover, round 1.
The decision is state-targeted with `cannibalism_warlord_march_raid_target_is_valid` as its `target_trigger`, rechecks target and costs before payment, applies `0.50` through the shared `damage_state_building_dynamic` helper with `token:supply_node`, keeps the costs, re-enable value, modifier, recoveries and AI expression, and writes the Host receipt read by the Warlord command window.
Deviation recorded as agent decision D6: a Host-wide cooldown flag backs the per-state re-enable of a targeted decision, so the raid cadence stays at one strike per re-enable period.
No refund path is needed because every check runs before the single debit, and the transaction runs inside one effect so no reentrancy guard is needed.
The same-scenario comparison is recorded in `2026-10-04_march_raid_probability_compare.md`.
