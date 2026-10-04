# Event 021 Decision and Mission Audit — 2026-09-25

## Status and scope

This is a read-only audit of the current Event 021 decision category, its 18 decisions and three selectable missions, related parent/treaty logic, constants, AI strategy, localisation, callback wiring, and the decision/action-family crosswalk.

No gameplay source, localisation, GUI source, or existing documentation was changed; this requested handoff is the only file written by this audit.

The current surface is not code-complete-for-test-entry because a source-valid exposure/evolution-III combination can show seven primary decisions against the six-action limit, and the sponsor disengagement owner/phase contract needs parent resolution.

This handoff is not runtime acceptance: HOI4 was not launched, and phase presentation, mission operation, balance, and player-facing visual quality remain unverified in a live game.

Design recommendations below remain unresolved proposals unless the parent explicitly accepts them; source implementation evidence does not establish design approval.

## Findings by severity

### P1 — Evolution-III prevention overlaps the regional exposure category and can expose seven actions

`event021_country_can_manage_exposure` admits a normal human country with neighbor exposure, no active local civil war, and a live registered source crisis (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:748-768`).

In that state, `event021_open_relief_corridor`, `event021_monitor_border`, `event021_support_government`, `event021_support_opposition`, and `event021_offer_mediation` can all be visible before the shared one-neighbor-action flag is set, provided both side targets are valid and viable (`common/decisions/021_random_civil_war_decisions.txt:179-213,379-423,476-483,537-543`).

Separately, `event021_country_can_prevent_fracture` explicitly includes neighbor exposure as a qualifying Evolution III cause (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:932-947`); that makes `event021_review_loyalty` and `event021_protect_communications` visible in the same state (`common/decisions/021_random_civil_war_decisions.txt:90-100,690-699`).

The shared action-use flag hides only the three mutually exclusive border/support/mediation choices after one is taken; it does not reduce the initial five exposure choices plus two prevention choices to six.

This is a source-level worst-case of seven visible primary actions, not a claim that every save reaches it; target validity, dynamic visibility, and the actual in-game list need scenario and live confirmation.

Recommendation: make prevention and exposure visibility mutually exclusive or otherwise cap this combined state at six without merging civilian relief with armed support; add a named worst-case source scenario and verify the resulting category with the available GUI route and user-owned live play.

The crosswalk currently states that the category exposes “only three to five relevant primary actions” (`docs/events/021_random_civil_war/decision_action_family_crosswalk.md:1-3`), so its count is incomplete for this overlap and needs reconciliation after a parent decision.

### P2 — Sponsor disengagement is gated by settlement state although its commitment is created by exposure actions

The exposure-side government/opposition support actions call `event021_prepare_exposure_sponsor_commitment`, which records `random_civil_war_sponsor_commitment_active` on the exposed neighbor and paired recipient/front/date/amount receipts (`common/scripted_effects/021_random_civil_war_decision_effects.txt:244-290`; `common/scripted_effects/021_random_civil_war_evidence_effects.txt:447-458`).

The only visible `event021_end_sponsor_commitment` requires `event021_country_can_manage_settlement` plus that sponsor flag (`common/decisions/021_random_civil_war_decisions.txt:583-590`); settlement management requires a settlement-phase, pending, or talks-open flag and does not include ordinary exposure (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:955-963`).

The normal exposure trigger excludes an active local crisis (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:748-768`), and this audit found no source path connecting the exposed sponsor’s newly created commitment to that sponsor’s own settlement phase. The commitment’s ordinary creating action therefore does not itself make the disengagement action visible.

The action’s AI score boosts `random_civil_war_negotiator_profile` only (`common/decisions/021_random_civil_war_decisions.txt:612-615`), while exposure support gives `random_civil_war_opportunistic_sponsor_profile` a distinct role and action weight (`common/ai_strategy/021_random_civil_war_ai_strategy.txt:122-139`; `common/decisions/021_random_civil_war_decisions.txt:470,531`).

Recommendation: parent should resolve whether disengagement belongs to the exposed sponsor during the exposure window or to a specific settlement signatory/obligation owner; then align its visibility, proof ownership, tooltip, and role AI. Do not infer that adding the action to exposure is accepted design.

Severity is P2 because the ordinary action path can leave a temporary commitment to expire automatically rather than exposing the promised player response; the exact intended treaty owner remains uncertain from source alone.

### P2 — Hold-the-capital mission tooltip omits a second start gate

The mission’s selectable `available` test requires the capital to be controlled by ROOT, have infrastructure above zero, and have a supply node, and it additionally requires either `event021_capital_defense_active` or `event021_capital_held` (`common/decisions/021_random_civil_war_decisions.txt:780-792`).

`event021_hold_capital_requirement_tt` explains the control, infrastructure, and supply-node conditions but omits the capital-defense/held requirement (`localisation/english/021_random_civil_war_l_english.yml:153-154`).

Recommendation: explain the additional start gate in the mission requirement text or a concise custom tooltip, and verify that selecting the mission communicates the full condition.

### P3 — Mission cancellation can leave an active marker until broader cleanup

Disposition: superseded by `event021_mission_cancel_marker_repair_2026-09-25.md` (implemented). The three missions now clear only their own active marker in `cancel_effect`; runtime cancel callbacks remain Needs Testing.

Each mission’s `cancel_trigger` has a cancellation path, but the mission blocks contain no `cancel_effect`; the active markers are cleared by the success/timeout resolvers and by `event021_cleanup_decision_state` (`common/decisions/021_random_civil_war_decisions.txt:794-801,859-874,903-910`; `common/scripted_effects/021_random_civil_war_decision_effects.txt:449-615`).

For example, the rail mission cancels when either rail-repair receipt appears, while the reconstruction decision can set those receipts during an active mission (`common/decisions/021_random_civil_war_decisions.txt:859-874`; `common/scripted_effects/021_random_civil_war_decision_effects.txt:201-219`).

The stale marker is normally made irrelevant by the corresponding receipt or terminal cleanup, which removes all three missions and clears all three active flags (`common/scripted_effects/021_random_civil_war_parent_effects.txt:7239-7241,7296`; `common/scripted_effects/021_random_civil_war_decision_effects.txt:571-615`).

Recommendation: test every cancel route for marker residue and consider a marker-only cancel cleanup if the engine supports it; do not run failure rewards on cancellation.

### P3 — Annex-successor source comments and helper documentation contradict the pre-annex call site

Disposition: resolved in current documentation and call-site contract. The parent helper documentation now records both natural pre-annex and `on_annex` contexts; see `common/scripted_effects/021_random_civil_war_parent_effects.md`. Runtime ordering remains Needs Testing.

`on_civil_war_end_before_annexation` explicitly calls `event021_parent_prepare_annex_successor` on ROOT before the country is removed (`common/on_actions/021_random_civil_war_cxt_on_actions.txt:44-50`), and the helper checks that the current ROOT is the matching opposition actor while FROM is its matching government host (`common/scripted_effects/021_random_civil_war_parent_effects.txt:4922-4951`).

The helper comment calls the function “on_annex only,” and its paired documentation says it is restricted to `on_annex` (`common/scripted_effects/021_random_civil_war_parent_effects.txt:4922-4924`; `common/scripted_effects/021_random_civil_war_parent_effects.md:142-146`).

The offline On actions reference documents ROOT as winner and FROM as annexed country for both `on_civil_war_end_before_annexation` and `on_annex`, so current caller scopes match the helper’s guards; the comment/docs are stale, not evidence of a demonstrated scope defect.

Recommendation: align the helper comment and documentation with both call sites and retain a natural-victory test proving FROM is still present at the pre-annex boundary.

## Decision category lifecycle and cognitive load

There is one ordinary category, `event021_civil_war_crisis_category`, with one static picture, one icon, `visible_when_empty = no`, and a phase/source predicate; it has no `scripted_gui` block (`common/decisions/categories/021_random_civil_war_categories.txt:9-21`).

The category art is registered at `interface/021_random_civil_war.gfx:10-18`, and the referenced static DDS exists at `gfx/interface/decisions/021_random_civil_war/decision_category_picture_021_civil_war.dds`.

Opening/front, exposure, prevention, reconstruction, and settlement visibility are delegated to named scripted triggers rather than a permanently visible wall of buttons (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:748-768,909-947,955-970`; decisions file above).

The category’s strongest documented content gap is cross-phase concurrency: Evolution III prevention can be visible alongside exposure, defeating the crosswalk’s three-to-five action count and exceeding the six-action ceiling in the valid target case described above.

The ordinary surface defines 18 decisions overall, but the count is not itself the simultaneous cognitive load: most actions are phase- or role-gated. Current source supports one to five common-phase actions in the sampled opening/front/reconstruction/settlement combinations, up to two missions during the settlement-to-reconstruction transition, and the seven-action exposure/prevention worst case.

The category displays one primary numeric value, State Authority, formatted as an integer; its bands are Cohesive, Contested, Failing, and Collapse, with centralized breakpoints at 69, 39, and 14 respectively (`localisation/english/021_random_civil_war_l_english.yml:10-20`; `common/script_constants/021_random_civil_war_constants.txt:214-216`; `common/scripted_localisation/021_random_civil_war_localisation.txt:9-56`).

Each band supplies the next threshold or current collapse condition and an action response, so the displayed value has a clear meaning and response; its qualitative consequence is also reinforced by action and mission text.

Dynamic phase, focus/target, and strongest-pressure summary are adjacent to the single numeric value (`localisation/english/021_random_civil_war_l_english.yml:10`; `common/scripted_localisation/021_random_civil_war_localisation.txt:60-140`), rather than exposing a raw row of counters.

The category description is a compact but information-dense paragraph containing value, band, guidance, phase, focus, and summary. Its text appears semantically useful, but visual wrap, clipping, background rendering, scaling, and click regions are not certified because the mandatory ordinary-category MCP render did not materialize the category elements.

The local GUI inspect was requested for `event021_civil_war_crisis_category` under scenario `E021-DECISION-CATEGORY-2026-09-25`; it returned `GUI_INSPECTED`, zero inspected elements, 0 modeled/1 approximated/1 missing fidelity counts, and `validation.passed = false` with project-wide graph diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b14c3ca2666ec8d95c72b508d3e2c96d42c3d692e084974073acd3ad81dd5225/9298e5f6a34f21afe50c242ee7794c1d54804b6d5efd92414e765c11e50f7417/gui-inspect.a6cd265ac259ee8d.json`.

The matching 1920×1080, UI-scale-1 render returned `GUI_RENDERED`, but the linked SVG was only 661 bytes, the response contained no rendered `data`, and `validation.passed = false`; therefore it is not usable production visual evidence. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ef75a6a7ef175373b04e952f07db1c5485b233c549b09cce1f12071075d1eb7/4203e314c8ec357b66793b75ef01ce56c19a09bbdfee2338f82ebe15d46fcf97/event021_civil_war_crisis_category-full.svg`.

## Mission quality

All three missions are selectable and use `activation`, `available`, `complete_effect`, `timeout_effect`, and `cancel_trigger`, with no `visible` trigger; this follows the offline mission guidance that `visible` does not control mission visibility. The completion effect marks the selected mission active, while the timed resolver owns success/failure outcomes.

| Mission | Owner, phase, and region | Requirement and duration | Success / failure | Cancel and duplicate-risk notes |
| --- | --- | --- | --- | --- |
| `event021_hold_the_capital_mission` (`common/decisions/021_random_civil_war_decisions.txt:764-809`) | Current crisis country; opening or active fronts; current capital state. | Capital controlled by ROOT, infrastructure > 0, supply node > 0, and either capital-defense-active or capital-held; 150 days (`common/script_constants/021_random_civil_war_constants.txt:568`). | Success clears active marker, records success, and improves authority/side leverage; timeout failure clears active, records failure, lowers authority, and raises pressure/claimant leverage (`common/scripted_effects/021_random_civil_war_decision_effects.txt:449-475`). | Cancels when crisis management ends or settlement resolves. One-shot success/failure flags prevent repeat. Tooltip gap noted above; no explicit cancel cleanup. |
| `event021_secure_rail_spine_mission` (`common/decisions/021_random_civil_war_decisions.txt:811-881`) | Reconstruction country; stored opening-front core state. | State remains owned and controlled by ROOT, is in the opening-core array, and has a supply node or infrastructure > the centralized gate; 30 days (`common/script_constants/021_random_civil_war_constants.txt:569-571`). | Success conditionally repairs one infrastructure, records repaired/secured receipts, recovers trains, and improves authority/pressure; timeout failure records failure and worsens authority/pressure (`common/scripted_effects/021_random_civil_war_decision_effects.txt:477-519`). | Cancels if reconstruction ends or either shared rail receipt appears. The one-time country receipt and paired state receipts prevent a second infrastructure award; action-versus-mission order still needs test. |
| `event021_hold_settlement_terms_mission` (`common/decisions/021_random_civil_war_decisions.txt:883-915`) | Settlement-obligation owner; obligation itself is the target, no state region. | Live obligation and recorded hold-until deadline, objective not already met/failed; 180 days (`common/script_constants/021_random_civil_war_constants.txt:570`). | Success confirms the current obligation when its objective/hold condition is satisfied; timeout records failure/breach and invokes parent obligation review (`common/scripted_effects/021_random_civil_war_decision_effects.txt:521-568`; `common/scripted_effects/021_random_civil_war_parent_effects.txt:5281-5340`). | Cancels when settlement management or the active obligation ends. Objective-met/failed flags and parent review prevent duplicate fulfilment; no explicit cancel cleanup. |

The ordinary maximum is one active mission per phase; settlement application sets both settlement and reconstruction phase state before `chaosx.nr21.9` moves the lifecycle into reconstruction, so the settlement-terms and rail missions can overlap during that transition. This is two of three, within the 1–3 cap, but must be checked at the event boundary (`common/scripted_effects/021_random_civil_war_parent_effects.txt:5443-5577`; `events/021_random_civil_war.txt:119-130`).

## Cost and requirement clarity

All 18 visible decisions use source-backed affordability gates, custom cost text, and manual debits; the displayed gate values are centralized in `event021_action_cost` and the matching effect debits use the corresponding negative values (`common/script_constants/021_random_civil_war_constants.txt:398-499`; `common/decisions/021_random_civil_war_decisions.txt:16-758`; `common/scripted_effects/021_random_civil_war_decision_effects.txt`). No action exceeds four distinct spendable resource types, and the emergency settlement is the maximum at four.

Every displayed spendable value is icon-first in `localisation/english/021_random_civil_war_l_english.yml:41-148`; the icon coverage is `£command_power` for command power, `£pol_power` for political power, `£army_experience` for army XP, `£infantry_equipment_text_icon` for infantry equipment, `£GFX_motorized_equipment_text_icon` for motorized equipment, `£GFX_train_texticon` for trains, `£manpower_texticon` for manpower, and `£convoy_texticon` for convoys. No literal resource names or fifth hidden spend were found.

| Decision identifier | Distinct spendable types | Displayed texticon set |
| --- | ---: | --- |
| `event021_secure_arsenals` | 3 | command power, infantry equipment, trains |
| `event021_defend_capital` | 3 | command power, infantry equipment, manpower |
| `event021_review_loyalty` | 3 | command power, army XP, political power |
| `event021_seize_depot` | 3 | command power, infantry equipment, motorized equipment |
| `event021_open_relief_corridor` | 3 | political power, motorized equipment, convoys |
| `event021_offer_emergency_settlement` | 4 | political power, command power, infantry equipment, manpower |
| `event021_reconstruct_administration` | 3 | political power, trains, manpower |
| `event021_integrate_formations` | 3 | army XP, infantry equipment, manpower |
| `event021_set_priority_front` | 1 | command power |
| `event021_monitor_border` | 3 | command power, motorized equipment, convoys |
| `event021_support_government` | 3 | political power, infantry equipment, convoys |
| `event021_support_opposition` | 3 | political power, infantry equipment, convoys |
| `event021_offer_mediation` | 3 | political power, command power, convoys |
| `event021_end_sponsor_commitment` | 2 | political power, command power |
| `event021_complete_disarmament` | 3 | army XP, infantry equipment, manpower |
| `event021_complete_coalition_governance` | 2 | political power, command power |
| `event021_protect_communications` | 2 | command power, trains |
| `event021_review_regional_administration` | 2 | political power, manpower |

The action payment rows show icon-plus-quantity, while requirement text separates non-spendable target/phase conditions from the payment. Cost tooltip prose is explanatory rather than a substitute for the visible cost row.

`event021_complete_coalition_governance` currently reuses the mediation cost constants, which are numerically consistent but couple two independently named actions for future balance tuning (`common/decisions/021_random_civil_war_decisions.txt:655-682`; `common/script_constants/021_random_civil_war_constants.txt:473-478`).

## Aid, actor roles, route locks, and awards

Civilian relief is separate from armed support: `event021_decision_open_relief_corridor` sets relief state and does not set `random_civil_war_neighbor_armed_support` (`common/scripted_effects/021_random_civil_war_decision_effects.txt:90-109`).

Government/opposition support sets the armed-support flag, transfers 100 infantry equipment to the selected live side or a redirected actor, records sponsor/recipient receipts, and charges 150 infantry equipment plus political power and convoys; `event021_neighbor_action_used` limits the border action to one (`common/scripted_effects/021_random_civil_war_decision_effects.txt:293-371`; `common/script_constants/021_random_civil_war_constants.txt:459-472`; `common/decisions/021_random_civil_war_decisions.txt:415-535`).

Mediation is its own action, clears armed-support and civilian-relief availability, and consumes the same one-neighbor-action receipt (`common/scripted_effects/021_random_civil_war_decision_effects.txt:374-392`).

The one-neighbor-action flag, relief one-use/recent flags, monitoring/mediation recent flags, sponsor duration, and exposure cooldown constrain repeat use (`common/decisions/021_random_civil_war_decisions.txt:179-213,379-413,537-570`; `common/scripted_effects/021_random_civil_war_effects.txt:1199-1241`; `common/script_constants/021_random_civil_war_constants.txt:271,514,549,559`). The 100-unit support transfer is less than its 150-unit infantry cost; no free-unit or repeated equipment-award loop was found in the inspected action path.

Source AI is actor-aware at the qualitative level: government/claimant roles affect capital and rail mission scores; exposure containment/mediator/sponsor roles alter neighbor choices; negotiator/hardliner roles influence settlement choices; invalid support targets and invalid priority-front depots are guarded by zero-weight modifiers or target gates (`common/ai_strategy/021_random_civil_war_ai_strategy.txt:1-150`; `common/decisions/021_random_civil_war_decisions.txt:138-176,250-261,415-535,612-615,764-915`).

The support target triggers require live, valid, viable government or claimant actors; the priority-front depot trigger checks the current state owner/control, opening-core membership, and supply node or military factory (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:770-815,896-907`). The selected priority state and id are now mirrored into normal variables consumed by the depot target/localisation path and are cleared with the target (`common/scripted_effects/021_random_civil_war_effects.txt:1026-1047`).

The mandatory independent probability audit was routed to `chaosx_ai_probability_auditor` agent `01a0d873-3893-7aa3-927c-80065fb39714` with `fork_context = false`. Its source inspections found 18 decision candidates and three mission candidates, but zero candidates available in the unbound source-only inspection and 12 decision/three mission runtime inputs still required; source hash prefix was `2e3a02e6`.

Decision source-inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4b493cae7017e6ea105292e43811ac75e0c2de23286d8bae835e9b1e3cbe22ae/151d7fa2f16bed950a4c193f8c03dd250311e2fd3f6e5d87471568c0a46b4d20/probability-inspect-2e3a02e6a44b.json`.

Mission source-inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df2f373013ff7588f8d5cb8d0ee6713e3c2f896a54555fece87732c3b65d6f2c/7f30ee86720db75363e976acb06d8ab9f21da8c532ab64c0e2ff589b5b795a2e/probability-inspect-2e3a02e6a44b.json`.

The decision and mission evaluations covered the same nine named scenarios: `event021_government_opening`, `event021_opposition_opening`, `event021_command_claimant_multifront`, `event021_containment_neighbor`, `event021_neutral_mediator`, `event021_opportunistic_sponsor`, `event021_settlement_negotiator`, `event021_reconstruction_successor`, and `event021_global_prevention`.

Every fixture bound only the country actor and role/phase flags; all had empty `state` and `scopes`, so no dynamic variables, country identity, targets, resource gates, state arrays, or mission-specific variables were provided.

Decision evaluation returned `PROBABILITY_ANALYZED_PARTIAL` for 18 candidates × 9 scenarios (162 rows); eligibility remained unresolved for all candidates/scenarios, with 48 unresolved items in the summary. Analysis ID: `probability-5b5562f10fad6cb77423fc20`; scenario hash: `4afe5550de327642cfacda4ca52fc056efd97cb3cc51fdb9f45dc3e18ef7f11c`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d86b9dd3ca3b41a1812123ae2439e79f788fe711a77be8a088ee49a3d60799ce/1d8d8d7e5286147cb38a5e384b90eaa8d2bd7db60ef0038589525bfba5613cec/probability-5b5562f10fad6cb77423fc20.json`.

Mission evaluation returned `PROBABILITY_ANALYZED_PARTIAL` for three candidates × nine scenarios (27 rows), with six unresolved summary items. `hold_the_capital` was false across these empty fixtures; this is not evidence of global starvation. Analysis ID: `probability-f8127983931b567452715c12`; scenario hash: `5d27181b443afde458cd76b875ca35ab03a4034f88cbc17123f2f6b9b950c3bb`. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8101679e6a362ab6fd032fecd30ecb70f68a451348512b5e4e5188f642fcfe83/bbf7b44df29e2f3dd62b897fbc9b3c45dbe527cc57d40bfde4c438edc7fe4d8b/probability-f8127983931b567452715c12.json`.

These are score traces only, not action probabilities or complete eligible-choice rankings; raw mission scores of 1 and role/phase-adjusted 1.5 do not establish a valid AI race while availability is unresolved.

The `ai_strategy_factor` adapter returned `PROBABILITY_SOURCE_DISCOVERED` / `no_weighted_surfaces` with zero candidates, so the role-specific `ai_strategy` entries were not quantitatively evaluated. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2c984b5d1a0d0f6d82c0451574dfeda598479ee89ac50c24cc2c19a1d8415397/415cd1ad1197891b0bfec1f03a9922a54aa4e23dbbcf26c5cf4d0572639bf43d/probability-inspect-74d73084d977.json`.

Both decision and mission sweeps returned `PROBABILITY_SWEEP_RANGE_REQUIRED` for `constant:event021_ai.priority_major` in `event021_government_opening`; the adapter requires a numeric range, numeric alternatives, or a numeric state value. There is no rank-reversal evidence. A mission probability render returned `PROBABILITY_ANALYSIS_STALE` with analysis revision prefix `ffe85c13` against current revision prefix `fa645666`; no compare or candidate-patch pass was run because this was a baseline audit.

Therefore actor-role source logic has been reviewed, but numerical balance, invalid-target weight, and scenario acceptance remain unresolved. Parent follow-up needs typed country/target/state/resource/variable fixtures and range inputs before drawing AI-selection conclusions.

## Localization, dynamic text, and integration

The category dynamic text names State Authority, reports its band and next threshold/action guidance, then names phase, current focus, and a concise pressure summary (`localisation/english/021_random_civil_war_l_english.yml:10-20`; `common/scripted_localisation/021_random_civil_war_localisation.txt:9-140`). Target text has a safe fallback, and priority-front setters now populate the mirrored state/id variables that the localization consumes.

Most decision effect descriptions state the real operation and principal consequence; paid actions have a visible numeric payment row. Special target/availability conditions use dedicated custom trigger tooltips for the depot, support sides, capital, rail, and settlement paths rather than exposing long hidden-trigger blocks. The known mission tooltip gap is the capital-defense/held gate above; text density and actual wrapping remain visually unverified because ordinary-category GUI evidence was unavailable.

Settlement actions are tied to the selected obligation rather than a generic passive menu; parent application prepares treaty/signatory obligations and settlement state, then `chaosx.nr21.9` clears settlement phase and advances reconstruction (`common/scripted_effects/021_random_civil_war_parent_effects.txt:5281-5591`; `events/021_random_civil_war.txt:119-130`). Parent obligation review records missed, fulfilled, breached, and recurrence state before reconstruction resolution (`common/scripted_effects/021_random_civil_war_parent_effects.txt:5281-5340,7075-7193`).

Parent terminal cleanup removes all three missions, clears decision state and targets, and tears down the relevant crisis/exposure registries (`common/scripted_effects/021_random_civil_war_parent_effects.txt:7197-7310`; `common/scripted_effects/021_random_civil_war_decision_effects.txt:571-615`). Exposure invalidation uses paired cleanup: the actual recipient is cleared through the stored recipient pointer before the sponsor/current exposed country and pointer are cleared (`common/scripted_effects/021_random_civil_war_effects.txt:1199-1276`; `common/scripted_effects/021_random_civil_war_parent_effects.txt:6843-6853`).

The source callback review found no broad world-scan callback in this decision lifecycle. `on_capitulation` invokes the external-defeat recorder on ROOT, whose documented contract is the defeated country, with FROM the victor (`common/on_actions/021_random_civil_war_cxt_on_actions.txt:40-42`; `common/scripted_effects/021_random_civil_war_achievement_effects.txt:176-203`). Annex callbacks use the documented winner/annexed ROOT/FROM pairing and explicit crisis/host guards (`common/on_actions/021_random_civil_war_cxt_on_actions.txt:44-64`; `common/scripted_effects/021_random_civil_war_parent_effects.txt:4922-4951`). These are source-scope checks, not engine execution proof.

## Prior finding dispositions and crosswalk status

| Prior 2026-09-20 statement/finding | Current disposition | Current-source evidence |
| --- | --- | --- |
| Priority-front global target was not mirrored for normal decision/localisation consumers. | `implemented`; stale as a defect. | `event021_set_priority_front` mirrors state/id and the clear helper removes them (`common/scripted_effects/021_random_civil_war_effects.txt:1026-1047`). |
| Regional-exposure cleanup left sponsor/recipient commitment fields stale. | `implemented`; stale as a defect. | Current paired pointer cleanup clears both sponsor and actual receiver receipts before removing exposure scope (`common/scripted_effects/021_random_civil_war_effects.txt:1199-1276`; `common/scripted_effects/021_random_civil_war_parent_effects.txt:6843-6853`). Expiry and source-invalidating runtime order still need tests. |
| Reconstruction action and rail mission could award duplicate infrastructure in one stored state. | `implemented`; the duplicate-infrastructure defect is stale. | Both rail receipts block repair in the action and mission; either receipt cancels the mission (`common/scripted_effects/021_random_civil_war_decision_effects.txt:201-219`; `common/decisions/021_random_civil_war_decisions.txt:821-871`). Test both orderings because reward selection/order is still unverified. |
| Three-to-five visible actions is sufficient across phases. | `unresolved`; the old count missed concurrent exposure and Evolution III prevention visibility. | Current trigger/visibility composition admits seven under the target conditions listed in P1; crosswalk lines 1-3 needs parent reconciliation. |
| Decision/mission AI probability and role validity were not certified. | `unresolved`; not stale. | The independent audit returned partial evaluations with all candidate eligibility unresolved under empty state/scope fixtures; sweeps lacked numeric ranges and the strategy-factor adapter found no weighted surfaces. No numerical acceptance is claimed. |

The audited crosswalk remains an implementation mapping, not acceptance evidence. Its decisions-to-families mapping is useful, but its visible-action count is unresolved until the overlap is addressed and retested (`docs/events/021_random_civil_war/decision_action_family_crosswalk.md`).

## Required test scenarios before acceptance

1. Construct an Evolution II exposed neighbor under Evolution III prevention, with a live registered crisis and both a viable government and viable opposition target; prove no more than six primary actions are visible after parent resolution and no spend/action-use gate is misleading.

2. Exercise the same exposure state with invalid, dead, annexed, or nonviable government/claimant targets; verify support actions disappear or receive zero AI score and no invalid country receives equipment or receipts.

3. For each actor role, inspect decision and mission scores in the nine named scenarios in the probability evidence section. Bind actual country identity, `hidden_trigger`, capital/target scopes, state arrays, resource gates, settlement obligation, and rail mission variables; provide numeric ranges for `constant:event021_ai.priority_major`, then rerun evaluate/sweep with identical typed scenarios. Do not treat the present empty fixtures or raw score ranking as runtime probability certification.

4. Test the sponsor path in both support directions: charge the sponsor, transfer exactly 100 infantry equipment to the intended live recipient, confirm armed-support versus relief state separation, verify paired ids/dates/front/amount receipts, then expire exposure and invalidate/annex the source and prove both ends clear without erasing durable treaty/achievement records.

5. Resolve the sponsor-disengagement owner/phase contract: after a normal support commitment, prove whether and when the action becomes visible, whether it satisfies the intended sponsor-repayment obligation, and whether its AI actor profile can select it. Include a no-local-settlement exposure sponsor and a settlement owner with unrelated prior sponsor state.

6. Test rail mission/action order both ways, including action after mission selection and mission selection after action; prove one infrastructure increment at most, no duplicate rail/authority/train award, correct cancellation, and active-marker cleanup.

7. For all three missions, test activation, selecting/starting, successful timeout, failed timeout, every cancel trigger, terminal removal, and attempted reactivation. Include the capital mission’s four start gates and the settlement/reconstruction overlap where two missions may coexist.

8. Exercise every decision at exactly sufficient resources, one unit below each spendable gate, hidden trigger/custom cost display, and repeated-use/cooldown states; verify displayed texticons/quantities match the debit and that no action exceeds four distinct spendable types.

9. Test authority values on both sides of 69, 39, and 14 and at collapse; verify band/guidance/response and the strongest-pressure summary update after actions and mission outcomes.

10. Run ordinary category visual checks in user-owned live play at a representative resolution and long-text state because MCP did not render this category; inspect clipping, wrapping, the single static picture, text legibility, phase visibility, and action/mission list density.

11. Test natural civil-war victory through `on_civil_war_end_before_annexation` and subsequent `on_annex`, ensuring ROOT/FROM are the intended winner/loser before and after removal; separately test external versus internal claimant capitulation classification.

## Validation performed and limitations

Read the repository `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-scripted-gui/SKILL.md`.

Consulted the required offline Paradox wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding; relevant mission, texticon, callback-scope, and event-target sections were checked. Consulted installed vanilla decision documentation and relevant official vanilla documentation/examples for decision, mission, effect, trigger, localisation, scope, script constants, on-action, and AI behavior.


The read-only `hoi4.event_inspect` trace targeted `chaosx.nr21.9`, downstream, depth 2, maximum 24 nodes/40 edges, helper expansion disabled, refresh enabled. It returned `EVENT_INSPECTED_PARTIAL`, no blocking diagnostics, and validation false because the large-workspace helper/lifecycle projections were deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bb122a6dcd6e4b3c83be9551951341949360c22ffa0d1e1cff914fe1ef7881be/14e0d09a54ab1e7bb24233f148623a8fc09d16da560a67c401dac357b5f0ce23/event-trace-f50fb76d44de.json`.

The bounded read-only `hoi4.event_render` options view for the same event used downstream direction, depth 1, 24 nodes, and no helper expansion. It returned `EVENT_RENDERED_PARTIAL` with three selected nodes; validation remained false because workspace-wide helper/lifecycle passes were deferred. JSON artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8177c1d47e6961f966036a88ee4cc3ed13b735617fb4411af2eb6b5eae1729cf/acd1465cdb098beda7bf8d2a0b1b81cb95d288096112d809b2b3e9223575f8bf/event-options-f50fb76d44de.json`; diagram: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9343eb0ce5d96d6de20b04250a0891e9aeb6d3fa3ff43502a9dcc11552c57f43/c19ae777a194d243297cb1fdfa004ed6796724dbacc6f80446ef90ec5506eef5/event-options-f50fb76d44de.svg`.

The mandatory decision-category GUI inspect/render route was attempted and returned zero modeled category elements plus a non-usable render artifact; it cannot certify ordinary decision-category alignment, clipping, background, or click areas. No GUI patch was authorized or made, and the category has no scripted GUI window.

The mandatory probability auditor returned partial inspect/evaluate evidence for all 18 decisions, three missions, and nine scenarios. It could not bind the required dynamic state/scope inputs, both score pools retained unresolved eligibility, both sweeps lacked numeric ranges, and the AI-strategy-factor adapter found no weighted surfaces; the artifacts and exact results are recorded in the AI section above. Quantitative decision/mission weight validation is therefore not complete.

No game executable was started. No source parser, live scenario, or user gameplay acceptance is claimed; the parent/user owns runtime acceptance.

No files were staged or committed, and `.git/index.lock` was not accessed.

## Handoff summary

Read-only audit completed for the requested source surfaces, with one P1 action-density finding, two P2 gameplay/tooltip findings, and two P3 lifecycle/documentation findings recorded above.

Current-source priority-front, sponsor paired-cleanup, and rail duplicate-infrastructure fixes were verified; their prior 2026-09-20 defect findings are stale as source defects, but their runtime regression tests remain required. The independent probability audit completed only as a partial score trace, not balance acceptance.

Do not describe this event as runtime-accepted or code-complete-for-test-entry until the P1 surface count and sponsor disengagement contract are resolved, typed probability fixtures and numeric sweeps replace the partial AI traces, and the listed user-owned live checks are complete.

## Parent dispositions after current-source recheck

Date: 2026-09-25. These dispositions supersede the stale P1/P2 conclusions above where explicitly noted. They are source-based findings, not live runtime acceptance.

| Finding | Parent disposition | Current evidence and limit |
| --- | --- | --- |
| P1: seven visible exposure/prevention actions | `superseded`; the claimed overlap is not source-valid. | `event021_country_can_prevent_fracture` (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:939-963`) excludes the uncommitted exposure phase with `NOT { AND { event021_country_can_manage_exposure = yes; NOT { has_country_flag = event021_neighbor_action_used } } }`. Before the shared action flag is set, at most five exposure actions can show. Once that flag is set, border monitoring, both support choices, and mediation hide (`common/decisions/021_random_civil_war_decisions.txt:379-423,478-546`), while the relief action remains separately gated; the two prevention actions can then appear. The source maximum is five, consistent with `docs/events/021_random_civil_war/decision_action_family_crosswalk.md`. The ordinary-category native rendering and live phase transition remain Needs Testing. |
| P2: sponsor disengagement unavailable during exposure | `superseded`; the audit misidentified the decision owner and phase. | The action `event021_end_sponsor_commitment` is the supported settlement signatory's sponsor-repayment obligation, not an exposure-stage control for the external sponsor. `event021_country_can_resolve_sponsor_repayment` requires the live settlement obligation and linked sponsor scope (`common/scripted_triggers/021_random_civil_war_parent_triggers.txt:999-1009`); the effect clears the exact matching sponsor commitment and received receipt (`common/scripted_effects/021_random_civil_war_decision_effects.txt:396-429`). This matches the master spec's postwar sponsor-withdrawal obligation and the action-family crosswalk. The sponsor path's actor-specific AI and receipt expiry still require the listed scenario tests. |
| P2: capital mission requirement tooltip omits defense gate | `superseded`; current localization states the gate. | `event021_hold_capital_requirement_tt` says the capital must have an active capital-defense order or a recorded held-capital defense (`localisation/english/021_random_civil_war_l_english.yml:153`). The tooltip and actual mission availability still need native UI/runtime review. |
| Probability evidence is incomplete | `unresolved`. | The prior probability MCP fixtures left dynamic targets, state, scope, and resources unbound and sweeps without numeric ranges. No new probability comparison was run for this source-only adjudication. |

The corresponding crosswalk already documents the dynamic five-action phase sequence and recipient-side settlement owner. This parent recheck changes no gameplay source and does not waive the live category, sponsor, mission, or probability tests.
