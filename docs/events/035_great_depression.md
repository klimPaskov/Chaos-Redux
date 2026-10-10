# Event 35: Great Depression 2.0

Parent commit notice, 8 October 2026: the parent accepted the bounded source/deep-report review and published source implementation as `19d3d0a59a4b3a14b45bec4d86b02dd3179e1ec0` over 30 exact paths, with the real index reconciled.
This supersedes earlier Public Works source-commit, source-review and private-index preparation status below, retaining those statements as historical evidence rather than full acceptance.
The recorded 87-test pass in 82.667 seconds remains source evidence, while separate `populated_wks_v2` work continues in the full-balance queue and native execution/full Event 035 completion remain incomplete.
These five assigned documentation files are frozen after this commit-notice update for the parent's documentation follow-up commit.

## Overview

Event 35 is a Minor Repeatable, Chaos level 1, Low-severity member of the Negative Economy cluster.

Negative Economy (cluster ID 10) is a one-time cluster at Chaos level 1: Event 35 is its required Low trigger row and The Great Embargo (Event 50) its optional Medium row.
Both a random firing and a cluster firing pick one weighted country that is not already in a depression; a cluster pick keeps the cluster's pacing lane.
While no major power or player government could start a new depression (`great_depression_has_any_independent_target`), the shared event-pool evaluator marks Event 35 unavailable with reason `great_depression_target`, so neither the random pool nor the Negative Economy cluster draws it, and the Events and cluster tabs show why.
Event 34 collapse, contagion conversion, the Evolution III spread, and relapse start depressions directly and never roll the cluster.

The event targets one valid major or player country, including a non-major player, and rejects active depressions, special Chaos actors, nonhuman economies, incompatible crises, and countries without a usable civilian economy.

Independent firing uses `chaosx.nr35.1` and owns normal event pacing.

Event 34 collapse, financial contagion, worldwide conversion, and relapse use the reusable start-or-deepen contract and never consume normal pacing.

## Public crisis model

`great_depression_depression_severity` is the only persistent Event 35 number presented for direct player management.

Severity is bounded from 0 to 100 and is presented through scripted localisation with its current value, qualitative band, trend, next threshold, phase, leading causes, current doctrine, selected Depression Center, active objective, and relapse state.

Hidden pressure components describe unemployment, credit, freight, relief capacity, confidence, center conditions, exposure, and opening shocks without becoming additional public meters.

Threshold hysteresis prevents phase and band oscillation around boundary values.

The lifecycle moves through Panic and Contraction, Depression, Stabilization, and Recovery.

Maximum-severity, social, supplier, and national-breakdown consequences use receipt flags or receipt variables so that one crisis episode cannot apply the same maximum consequence repeatedly.

## Reusable crisis API

The public gateway is `great_depression_start_or_deepen` in `common/scripted_effects/035_great_depression_effects.txt`.

Callers supply a contract version, caller type, source event and episode, receipt id, pacing and history policy, severity input, evolution proof, and source-specific proof fields.

The contract fails closed when required evidence, source scopes, snapshots, relationship proofs, worldwide context, or relapse history is missing.

The current country is the synchronous transaction recipient even when the sender or global host remains `ROOT`.
Event 34 fields must match the frozen owner snapshot, contagion must prove both rows of the exact source-target pair, worldwide conversion must match the current global episode and pressure receipt, and relapse must match the country's completed episode and recovery window.
The caller can read the public result immediately after the helper returns.

Selection scores, center-registration status, deepening amounts, and humanitarian acknowledgements use caller-owned temporary result storage across helper returns.
Their existing formulas and owner authority remain unchanged.

A new crisis must have an owned, controlled, passable core industrial state before national setup begins.
Its requested evolution floor replaces the previous episode's floor, and evolution projection and logging wait until center registration succeeds.
Deepening preserves the active episode and its existing evolution floor.

The supported callers are independent Event 35 firing, Event 34 collapse, financial-contagion conversion, worldwide-depression conversion, and relapse.

An active compatible crisis is deepened in place, while an inactive compatible country receives a new globally unique episode id and a fresh episode ledger.

The active-country registry is sparse and bounded, and the shared global-host daily hook evaluates only registered Event 35 countries and registered global-pressure rows.

## Event 34 inheritance

Event 34 freezes its collapse snapshot before removing boom-only bonuses and calls Event 35 for the same country.

The snapshot carries Event 34 evolution, final and peak Overheating, landing result, reserve state, completed projects, inherited regions, shock evidence, repeat history, and the collapse receipt.

Baseline maps to Event 35 baseline, Evolution I maps to Financial Contagion, Evolution II adds Social Collapse, and Evolution III adds The Second Great Depression with a very-high starting Severity profile.

If Event 35 is already active, the inherited collapse deepens the existing episode and does not add another depression modifier.

Event 34 fills each snapshot field from the live boom, recording it as unavailable when the boom has not set it, and delivers its highest-ranked owned Industrial Region as the primary region inside the national call.
After an accepted national call, and while the Event 35 crisis is coherent, it registers every further Industrial Region (role primary) and every Evolution III spread state (role corridor) through `great_depression_register_inherited_region`, each under its own Event 34 region receipt with authentic profile, stage, protection, fragility, control and damage values.

Event 34 suppliers set their state with the order-books decisions. When Event 35 makes Offer Boom Supply Contract, open order books accept the contract (more Overheating, export orders and one rough landing upgraded to controlled), closed books refuse it, and from 70 Overheating upward every contract is refused automatically, so `industrial_boom_supplier_adapter_target_is_valid` fails and the offer row is hidden.

Event 34 retains the inherited-crash achievement `chaos_redux_034_the_long_fall`.

The public Event 35 report selects source-aware opening prose for the inherited hard landing, financial contagion, social collapse, worldwide contraction, relapse, and ordinary national paths while retaining the same Severity state readout.

## Recovery doctrines and decisions

The six recovery doctrines are Emergency Public Works, Rescue Strategic Industry, Stabilize Finance and Trade, Austerity and Retrenchment, Direct State Planning, and Let the Market Clear.

Each doctrine has its own mapped actions, AI preference profile, crisis legacy, and recovery tradeoffs.

The decision category contains 68 ordinary decisions and 17 missions.
Each action shows only in the phases where it can still change the outcome (doctrine choices while the doctrine is unassigned, openers early, working actions in Depression and Stabilization, closers in Stabilization and Recovery), evolution actions replace the general ones, and `.tools/test_event035_visible_actions.py` holds the visible counts to five national, five partner and six selected-center actions in an ordinary phase (six national actions in an emergency, six partner actions in the worldwide depression).
The merged families are Clearing Agreement, Protect the Home Market, Abandon the Distressed Market, Emergency Credit and Coordinated Public Works and Reconstruction.
Tooltips state effects as "eases faster" or "rises faster" and never print hidden component points.

Every doctrine has a state project and a Stabilization closer.
Stabilize Finance and Trade restores a selected Distressed, Idled, or Shuttered center through Restore Local Credit and Trade Connection, which needs a completed bank audit and runs the finance restoration project; the center reopens as restructured.

Bank Holiday and Audit funds a 21-day national examination, briefly restricts factory output and slows credit deterioration.
The non-selectable Audit and Reopen Viable Banks mission certifies a functioning productive base, Stability of at least the central audit threshold, and a country that has not capitulated.
It allows seven days beyond the examination interval to meet that viability proof; a failed audit renews panic rather than recording financial recovery.
Recapitalize Viable Institutions requires the successful audit from the same depression and funds a separate 42-day follow-up, with seven days of certification grace.
Durable credit relief begins only after this follow-up succeeds; the audit's completion alone grants no lasting credit treatment.
The durable guarantee requires audit and recapitalization proof during Stabilization.
Each funded program reserves one of the two supporting objective slots, even if its native mission needs restoration.
Native timers are synchronized to the original absolute deadline immediately after activation and during the existing bounded active-country receiver, so restoring a mission never restarts the work interval.
Cabinet Review and Emergency Policy Review withdraw unfinished financial work, reopen withdrawals prematurely and produce one renewed-panic consequence.
Completion, timeout and owner reconciliation share current-episode active markers; repeated or stale callbacks cannot grant another certification or pressure consequence.
Retirement and actor invalidation close active work without rewarding or punishing another episode.
The funding is charged once by the authorization action, with no second mission-completion charge.
Audit uses `GFX_decision_mission_great_depression_halt_the_panic`, recapitalization uses `GFX_decision_mission_great_depression_prevent_a_relapse`, and the temporary holiday uses the existing finance-legacy spirit icon; these are existing purpose-matched asset families, not resized cross-family art.
Rescue Strategic Industry closes its route in Stabilization or Recovery with exactly one of two decisions: End Rescue Dependence withdraws the essential orders for a lasting fiscal relief, while Retain a Bounded Arsenal Institution keeps them as a standing institution with a lasting fiscal upkeep and wartime supply relief.
Either closer counts as the durable recovery measure that Prevent a Relapse requires.

Dynamic costs are calculated from the usable economy and grouped into doctrine, policy, center, freight, relief, credit, industrial, contagion, social, liquidation, and global-recovery families.

No action charges more than four resource types.

The custom cost contract contains matching normal, blocked, and tooltip localisation keys and debits the same political power, manpower, fuel, trains, convoys, support equipment, civilian-factory commitment, stability, or war support shown to the player.

Inline costs show at most three quoted values, and their hover tooltips show every payment or capacity commitment with its resource icon.
Each amount uses its own affordability color, with insufficient resources in red and available resources in yellow.
Civilian capacity is frozen at the accepted payment quote, including Public Works, and later cost refreshes do not resize that commitment.
The internal `great_depression_committed_civilian` snapshot is removed with the active dynamic modifiers during crisis cleanup.

Countries responding to contagion exposure or worldwide pressure keep their commitment while any Event 35 crisis surface remains active.
When their last external surface closes, `great_depression_release_idle_civilian_commitment` releases the capacity after the current response lock has ended.
The hidden `chaosx.nr35.7` callback coalesces delayed reviews through `great_depression_civilian_release_queued`, and it never records a normal event firing, changes Chaos, or displays a popup.
National crises continue to use `great_depression_clear_dynamic_state` for their terminal cleanup.

The global host dispatches registered national maintenance through the hidden `chaosx.nr35.8` receiver, giving centre ownership, humanitarian attribution, and contagion-source helpers the affected country as `ROOT`.
The weighted independent selector preserves its chosen country through `chaosx.nr35.9`, which revalidates that country and calls the same start/deepen transaction without choosing another target.
Neither private receiver creates another normal pacing entry.

The selected-center flow uses state targets, one occupied action slot, cooldowns, project receipts, state status validation, and cleanup on transfer or crisis closure.

Historical completed work does not occupy the current project slot.
A distinct paid authorization allows mapped follow-on work or reopening after a fresh collapse while preserving earlier completion and one-shot reward history.
Selection and project proof require the state's exact registered episode; physical stage changes retain that proof.

Every paid decision and mission uses the same affordability predicate in its ordinary availability and custom-cost display.

Ordinary response missions activate without an entry debit, require affordability at completion, and debit their displayed mapped action cost exactly once on successful completion.
The bank audit and recapitalization missions instead certify work prepaid by their authorization actions; their mission rows state that no further payment is required.
Cancellation and timeout never create a second charge, and these funded bank programs have no separate unspent stockpile balance to refund.

The National Employment Guarantee cannot be started again while its automatic mission is active, and its bounded partial-timeout result is terminal for that episode so the partial relief cannot be farmed through repeated activation.

### Decision and mission tooltips

Every complete, timeout and cancel effect of the 79 decisions and 17 missions carries a custom effect tooltip.
The Severity change comes from `great_depression_apply_public_action_delta`, which prints `great_depression_severity_change_tt` from the same temporary value it adds; a partner's own Severity change appears under the partner.
`great_depression_prepare_action_tooltip_values` fills the numbers each tooltip prints from the same script constants the effect or the hidden pressure rebuild uses: hidden relief and pressure per Severity update, project and protection days, the project failure penalty, the whiplash and mandate durations, and the Policy Fatigue switch count.
A tooltip names each lasting consequence in plain words: pressure eased or added for each later Severity update and for how long, a project started with its length and failure penalty, a center written off, a mission requirement met, a partner affected, a worldwide contribution, or a recovery scar or political settlement the recovery can leave.
Two shared lines come from scripted effects: `great_depression_global_contribution_tt` inside `great_depression_increment_global_contribution`, shown only when the contribution counts, and `great_depression_partner_link_opened_tt` from `great_depression_show_partner_link_tooltip`, shown when a partner action opens a Financial Contagion link.
Payments, receipts, phase upkeep, Event 34 adapter calls, inherited-region dispatch and civilian-commitment release run inside `hidden_effect`, because the custom cost text and the tooltip already show what the player pays and gains.
`great_depression_commit_partner_action` commits the cost and Severity change outside its partner block so the tooltip shows them even before the partner is saved as an event target.

### Policy trade-offs

Retrench the Relief Administration, Ration Strategic Inputs and Withdraw Emergency Support each leave a lasting trade-off read by `great_depression_rebuild_hidden_components` for the rest of the episode.
Retrenchment releases the civilian capacity held by earlier paid measures until the next one and eases fiscal pressure by 2 on each update; in Stabilization or Recovery it also lowers Severity by 2 at once, while earlier it raises Severity by 2 and adds 1 social pressure on each update.
Rationing eases industrial pressure by 2 and adds 1 trade pressure; withdrawn support eases fiscal pressure by 2 and adds 1 demand pressure.
An Emergency Policy Review's whiplash lasts `great_depression_event.policy_whiplash_days` (42) days through a timed flag and a timed modifier.
The Maximum-Severity Emergency mission grants its larger relief through the `great_depression_mission_relief_override` input of `great_depression_mission_complete`.
Failed center projects count in the per-episode `great_depression_project_failure_count` that the National Employment Guarantee and the incident weights read.

## Depression Centers

A normal episode selects one to three Depression Centers, bounded by the central registry cap.

The center ledger keeps aligned state, stage, project, loss receipt, factory baseline, project timing, owner, and Event 35 loss arrays.

Mapped center statuses include distressed, idled, shuttered, abandoned works, protected, public works active, reopened, and hollowed industrial district.

Mapped projects include emergency public works, strategic-industry rescue, credit clearing, austerity administration, state coordination, controlled liquidation, freight restoration, reopening, and center protection where their doctrine and state gates permit them.

Structural projects freeze their required work at authorization from the central 133-day anchor and bounded contributions from actual building damage, Severity, infrastructure, war and earlier failed projects.
Required work is limited to the central 245-day maximum, with certification beginning 42 work days short of completion.
Protection remains a separate 42-day treatment and supplies no reopening proof or shortened reopening deadline.
Action forecasts include the action's immediate Severity change, matching the work accepted after payment.
Later improvements do not erase already accepted work, while interrupted control extends the stored calendar due date without advancing work.
The owner activates the selected-center mission through the existing objective gates, captures its exact site and episode, binds a paid structural authorization and synchronizes the native timer immediately.
The bound deadline is the project's due date plus the central grace interval.
Historical or unbound completion flags cannot complete the objective, and premature, repeated or stale timeout callbacks add no pressure.
Losing authority cancels the mission without a failure consequence while the local transfer contract retains accepted work.
Returning centers reuse their exact existing row, including at full capacity, without duplicating arrays or increasing the cap.
Source retirement preserves only an exact, still-open transfer to a different owner, leaving the local work and receipts available for successor adoption.
Malformed active work with missing required duration or an inconsistent certification cut cannot reserve a successor's active project slot.

### Regional Works Program

Convert Works into Lasting Capacity is offered during Stabilization for a current completed Public Works authorization.
The selected center must retain its completed-works receipt, positive paid authorization, current episode and a recognized work kind, with no active plan or closed conversion receipt.
Its entry checks current material affordability again before payment.
Reopened centers without completed work, failed work, prior-episode receipts and Panic-stage governments cannot start that conversion.
The closer's AI blocker uses this same eligibility contract, preserving the existing numeric weights and allowing a valid Relief Coalition willingness score of 34 in the declared source case.
These entry guards do not establish the pending physical legacy, emergency-capacity closure or integrated material-refund outcomes.

Launch Regional Works Program selects a real need in an owned, controlled and currently registered Distressed, Idled, Shuttered, Reopened or Abandoned center, excluding Liquidated sites and occupied project slots.
Its frozen need follows this priority: damaged infrastructure, damaged railway facilities, damaged port facilities, inadequate infrastructure, an eligible neighboring capital-linked railway, missing coastal port facilities, wartime anti-air protection, abandoned works, or locally needed housing and employment recovery.
The action prepares the exact site before payment and binds its original payer, episode, fresh payment count/day and unspent authorization after the paid project starts.
Preparation, binding and current-plan proof require an existing normal civilian actor, special/nonhuman exclusions and coherent crisis state, preventing direct completion through stale crisis flags.
The final `great_depression_project_has_public_works_result` guard permits its non-Public-Works branch only when no active Public Works plan and no paid Public Works receipt remain.
Changing a paid ready project's type to finance therefore grants no map, finance or completion award, while ordinary other projects retain their contract after `great_depression_clear_public_works_plan` removes those markers.
`GetGreatDepressionWorksNeed` displays the frozen paid need ahead of the current preview, and the tooltip names `[FROM.GetName]` with the accepted controlled-work duration and result requirement.
Repair administration accelerates native repairs, while certification requires reduced damage and preserved total facility levels.
Construction issues at most one physical level per globally allocated episode after accepted work and checks actual total and usable capacity, with no extra level when external construction already meets the target.
Rail issuance and proof use the same frozen adjacent partner, current ownership/control, capital network and restricted route.
Coastal port facilities establish local capacity without certifying sea access, convoy availability or an international shipping route.
Housing and abandoned-site conversion change the physical center stage and ledger to Reopened and prove a reduction in the same local demand contribution that the national pressure rebuild consumes.
Those local outcomes grant no factory or building slot.

Suspension removes repair administration, and legitimate resume restores it after the stage transition.
The repair updater may remove a term only for the current state owner or recorded plan owner, so a stale or foreign ROOT cannot strip another owner's valid repair administration.
Transfer retains the original payer, accepted need, baseline and work, and marks issuance spent for the successor only when authorization and the pre-transfer episode both match.
The project proof deadline and bound native mission share the legitimately extended project due date plus 28 days, with failure retiring the exact mission and charging the shared consequence once.
Durable issuance and local-recovery history survive transient cleanup.
The [October 8 documentation handoff](../plans/035_great_depression_plans/subagent_handoffs/public_works_documentation_2026-10-08.md) records implemented bounded source under U1, with the parent's final guarded-source 87-method pass in 82.667 seconds recorded, including 21 Public Works methods, the same 512 local combinations and eight invalid-actor cases, foreign-ROOT retention and paid-project type reinterpretation with no award.
The earlier 86-method pass in 102.797 seconds remains historical and is superseded only as the current test boundary.
Parent bounded source/deep-report review is accepted and native repair-family reference reads are complete, with source published as `19d3d0a59a4b3a14b45bec4d86b02dd3179e1ec0`.
The same-nine-WKS comparison is terminal partial, analysis `probability-7cae77ee230c7184e69c9508`, with 57 unresolved native inputs and zero-eligible placeholders that prove no actual exclusion, score delta or normalized probability.
The input gap remains subject to fixture-support versus fixture-construction clarification, while full balance, native execution, campaign acceptance and event completion remain open.
The parent's narrow `.8` trace and state render completed partial, with the current render selecting one node, zero helpers and 46,254 omitted nodes.
Current render resources remain unavailable, so visual inspection and full lifecycle proof remain unresolved, and the matching before/after `.8` comparison proves no event delta as recorded in the documentation handoff.
It supersedes the prior source-no-map finding only, while Part 3 reserved/unspent refunds, lasting-capacity closure, inherited consumers, full acceptance and native/live evidence remain open.

Every mapped project type has a producer.
Finance restoration starts from Restore Local Credit and Trade Connection.
A successful Keep Essential Freight Moving mission restores basic transport and supply for the selected center: it starts transport integration on a closed center with no running project, or moves the project already running there several weeks closer to completion, once per project.
Coordinated Public Works and Reconstruction starts international reconstruction on the selected closed center, including an abandoned one that was not liquidated, when no other center project is running.
The AI, which does not keep a selected center, uses one valid center of its own for both producers.
The inherited-liability consumer adds ongoing hidden pressure for inherited regions.
Hidden inherited rows stay national pressure: there are no paid actions on hidden rows, no secured-value salvage and no multi-region priority, and corridor recovery runs through the visible centers.

Factory loss is delayed until sustained severe failure or a deliberate liquidation action.
A center written off by Abandon Depression Center or Auction or Reorganize Failed Assets carries the `great_depression_center_liquidated` flag and adds only `demand_liquidated_center` (1) to hidden demand pressure on each update, instead of the full abandoned and hollowed weight that a center lost to sustained failure keeps.

Factory-loss receipts compare against the frozen center baseline, remain capped, and prevent duplicate physical losses.

State transfer revalidates ownership, removes invalid active projects, preserves applicable scars and legacies, and keeps the aligned registry coherent.

Terminal cleanup touches only registered states whose current center episode still matches the closing country.
A center recorded under another country's episode retains its own flags and projects.

Repeat episodes retain bounded doctrine legacies and recovery scars while applying diminishing returns to repeated relief.

## Recovery and its aftermath

`great_depression_try_complete_recovery` closes an episode in one transaction: it resolves the Strong, Uneven, or Hollow result, freezes the episode summary, evaluates achievements, records the refire memory, applies the recovery legacy, clears the active crisis state, and finally queues the national recovery report.

The frozen summary (`great_depression_freeze_episode_summary`) keeps the final doctrine, the doctrine switch count, and one final outcome per registered center in `great_depression_last_completed_center_outcome_entries`, using the center-stage values for reopened, restructured, liquidated, and abandoned.
The outcome is read from the center's own flags while its episode id still matches, so a state now recorded under another country's episode is left unclassified.
The counts `great_depression_last_completed_final_reopened_count`, `_restructured_count`, `_liquidated_count`, and `_abandoned_count` feed the report.

`chaosx.nr35.11` is the national recovery report.
It fires one day after the episode closes, uses `GFX_report_event_great_depression_recovery`, and is guarded by `great_depression_recovery_report_pending` plus the frozen episode id, so it appears once per completed episode and never on relapse, conversion, or deepening.
Its title, description, and option text follow the frozen Strong, Uneven, or Hollow result through `GetGreatDepressionRecoveryTitle`, `GetGreatDepressionRecoveryDescription`, and `GetGreatDepressionRecoveryOption`.
The description states the reopened, restructured, liquidated, and, for a hollow recovery, abandoned center counts and the peak Severity, names the institution the final doctrine leaves behind and its lasting weakness (`GetGreatDepressionRecoveryInstitution`), and names the lasting cost (`GetGreatDepressionRecoveryLoss`: the Event 35 factory levels lost, idle abandoned works, or no loss).
The single option shows the recovery ideas the country now holds through `great_depression_show_recovery_report_ideas`, and its AI weight is `great_depression_event_option_weight.recovery_report`.

### Episode cleanup

`great_depression_clear_episode_action_flags` ends the conditions and action results that belong to one national episode: clearing agreement, boom supply contract, foreign support, supplier contract, emergency credit request, trade failure, lost import contract, supplier collapse, Event 34 supplier pressure, the containment receipt with its episode id, and socialized occupied industry.
It runs with `great_depression_clear_market_exit_state` in `great_depression_reset_episode_policy_state` (episode start) and in `great_depression_clear_dynamic_state` (abort, invalid retirement, and recovery cleanup), so the recovery outcome, the political aftermath, and the country scar have already read them before they clear.
A later episode therefore starts without trade relief from an old clearing agreement, accepts a new Event 34 boom supply contract, and cannot complete Keep Essential Freight Moving or the Maximum-Severity Emergency on an old agreement.
Containment Line counts only a containment action whose `great_depression_containment_action_episode_id` matches the current episode, written by `great_depression_record_containment_action`.
The lost import contract on a partner is a timed flag (`import_shift_pressure_days`) and also clears in the partner's own episode cleanup.
Durable memory such as recovery legacies, scars, refire memory, and the last-recovery facts stays by design.

### Recovery legacies

A completed episode leaves at most one doctrine legacy, chosen from the final doctrine by `great_depression_add_recovery_legacy`, which first removes every other legacy.
Each legacy pairs a benefit with a countervailing cost, and in every later episode `great_depression_apply_recovery_legacy_pressure` (called by `great_depression_rebuild_hidden_components`) eases one hidden pressure and adds a weakness only under the condition that exposes it.
The offsets are the `legacy_*` keys of `great_depression_hidden_component`, so no doctrine route grants immunity.

| Legacy | Idea benefit and cost | Later-episode relief | Later-episode weakness |
| --- | --- | --- | --- |
| Public Works | infrastructure construction speed, higher consumer goods | demand stress | fiscal stress while Severity is at or above Deep Depression |
| Strategic Industry | military factory output, slower civilian factory construction | industrial stress | demand stress in peacetime |
| Finance and Trade | trade opinion, higher minimum export | credit stress | trade stress while Financial Contagion, foreign exposure, or worldwide pressure is active |
| Austerity | lower consumer goods, lower stability | fiscal stress | social stress while a registered center is Idled, Shuttered, or Abandoned |
| Direct State Planning | building construction speed, larger line-change efficiency loss | trade stress | fiscal stress in Stabilization and Recovery |
| Market-Clear | lower consumer goods, lower starting production efficiency | industrial stress while stability is above the medium floor | demand stress while a registered center is Idled, Shuttered, or Abandoned |

`great_depression_resolve_recovery_outcome` sets `great_depression_recovery_hollow` for a Hollow result and clears it for a Strong or Uneven one, so the latest recovery decides whether the country is more exposed to contagion conversion and worldwide pressure.

`great_depression_post_recovery` is the temporary safeguard: it is added when an episode closes with the recovery watch running, removed when the watch expires, and removed when any new episode, including a relapse, is committed.

### Country recovery scars

Besides the hollow-recovery scar, `great_depression_apply_country_scar` gives at most one country scar per recovery, earned only from receipts the closing episode recorded.
The actions that can leave a scar write an episode receipt when they are taken: Emergency Credit taken from a partner writes `great_depression_scar_debt_episode_id`, Accept External Supervision and Request Foreign Support write `great_depression_scar_foreign_episode_id`, and Establish Emergency Production Board, Ration Strategic Inputs and Restrict Capital Outflows write `great_depression_scar_controls_episode_id`.

| Scar | Earned when | Cleared by a later strong recovery |
| --- | --- | --- |
| Debt Overhang | emergency credit in this episode with no public-obligation restructuring or international debt conference | under Austerity or Finance and Trade |
| Foreign Credit Dependence | external supervision or foreign support in this episode | under Finance and Trade or Direct State Planning |
| Emergency Controls | emergency controls in this episode and Remove Emergency Controls never taken | under Let the Market Clear, or one that removed the controls |
| Labor Bitterness | security forces or broken occupations that did not already become the Labor Scar aftermath | under Emergency Public Works, or one that left a Social Compact |
| Policy Fatigue | `great_depression_country_scar.policy_fatigue_switches` or more doctrine switches | with no doctrine switch |

The first match in that order is earned, and a newly earned scar replaces any older one, so scars never stack.
The recovery report's option shows the scar the episode left.
The five scar spirits use their own Event 35 national-spirit art (see Presentation and asset wiring).

### Lasting district outcomes

After the summary is frozen, `great_depression_apply_durable_state_outcomes` gives at most two registered centers a lasting district outcome (accepted addendum B3), reading only the frozen center arrays.
The Recovered Industrial District (`great_depression_state_recovered_district`) goes to the owned, reopened or restructured center with the highest-value completed structural project, scored by `great_depression_state_outcome` (lasting capacity highest, then international reconstruction, public works and transport integration, strategic rescue and finance restoration, then asset reorganization and trusteeship); short treatments never earn it.
The Scarred Industrial District (`great_depression_state_scarred_district`) goes to another owned center with the largest unrepaired Event 35 factory loss, and an abandoned or liquidated center qualifies even without a factory loss.
When no scar is due, a second distinct structural project can keep a second Recovered Industrial District.
A state never receives both, and a later episode's outcome for the same state replaces the earlier one, which is how a scar can be repaired.
The two modifiers use their own names and the reopened and hollowed center icons, so the episode cleanup in `great_depression_clear_center_physical_stage` leaves them in place.
The recovery report names the districts through `GetGreatDepressionRecoveryDistricts`.

## National Breakdown and Social Collapse

Baseline National Breakdown opens only after sustained severe failure and runs through a warning, prevention mission, proof gate, and one recorded outcome in `chaosx.nr35.6`.

The baseline outcome always offers an emergency settlement and cabinet replacement. Its AI weights are `45` and `35`; the remaining `20` weight belongs to civil conflict only when the strict force, territory, leadership, capacity, shared-adapter, and recent-war gates succeed. The shared Event 21 civil-conflict adapter is fail-closed, and a rejected handoff resolves through the idempotent non-war emergency outcome.

Social Collapse adds organized actors, sector conflict, national unrest, government crisis, and revolutionary breakdown states.

Coup, separatist, and civil-conflict outcomes require distinct actor, severity, duration, stability, territorial, government, and shared-system gates.

The coup and regional-autonomy branches use `chaosx.nr35.4` and `chaosx.nr35.5`; failed extreme routes do not invent a fallback faction or civil war.

When Social Collapse activates on a crisis already under way, `great_depression_queue_social_collapse_activation_report` chooses the primary movement through the deterministic `great_depression_select_social_actor` and queues `chaosx.nr35.13` once per episode, with the social-collapse picture.
The report names the movement family (trade-union coalition, communist councils, syndicalist occupation, nationalist mass movement, military emergency faction, traditional authority, regional autonomy, business and creditor coalition, or rural protest) through `GetGreatDepressionMovementFamily`, and the incident ladder later uses the same movement.
A disabled evolution never activates, so it queues no report.

An emergency mandate carries the Emergency Government spirit (`great_depression_emergency_government`) for exactly as long as it runs.
A successful coup, an emergency dictatorship, or Form an Emergency Government adds it, and the mandate's success, failure or cancellation, Remove Emergency Controls, recovery, or a rolled-back opening removes it.
Remove Emergency Controls also ends the mandate itself, since it already dissolves the emergency government the mandate needs.

When an episode that went through Social Collapse closes, `great_depression_apply_political_aftermath` chooses one political aftermath from how the movement was answered, in this order: Emergency Rule for an emergency government that settled, Planning Settlement for socialized occupied industry, Corporate Rescue Order for guaranteed property and credit, Regional Autonomy for recognized councils or autonomy, Labor Scar for security forces, broken occupations or rejected autonomy, and Social Compact for a negotiated strike settlement or employment compact.
A new aftermath replaces the previous one, and an episode that earned none keeps the old one.
In later episodes `great_depression_apply_political_aftermath_pressure` shifts hidden social stress by the `aftermath_*` keys of `great_depression_hidden_component`: Corporate Rescue Order and Labor Scar raise it, and the other four lower it.
The recovery report's option shows the aftermath the episode left.
The seven spirits use their own Event 35 national-spirit art, registered under their sprite names in `interface/035_great_depression.gfx`.

## Bounded incident pools

`common/scripted_effects/035_great_depression_incident_effects.txt` owns the ordinary incident clocks, state and partner selectors, complete candidate pools, receipt history, and qualitative application adapters.

The baseline pool contains factory gate closures, unpaid wages, freight yards idle, local credit cooperatives, municipal relief failure, successful reopening shifts, skilled workers leaving, unfinished works abandoned, regional aid requests, and war-orders revival.

The Financial Contagion pool contains correspondent failure, foreign-currency obligations, trade-credit withdrawal, bank holidays, debt conferences, rescue-loan failure, supplier concessions, capital flight, clearing blocs, coordinated rescue, and partner abandonment.

Social Collapse uses six stage-one families—local strike committee, unemployed march, plant-closure wage dispute, relief offices overwhelmed, veterans demanding employment, and regional council retrenchment refusal—followed by sector strike, factory occupation, coordinated layoff refusal, business lockout, relief demonstration, and security-force refusal at stage two.

Stage three adds general strike, nationwide factory occupation, hunger riots, mutiny or refusal, emergency cabinet collapse, and rival movements.

Stage four adds cabinet authority loss, recovery-program failure, army emergency powers, parallel administration, regional secession threat, and foreign-patron conditions on aid.

The final rung chooses among coup attempt, regional uprising, separatist conflict, full civil war, negotiated power transfer, emergency dictatorship, and revolutionary coalition, while retaining the existing strict political and Event 021 gates.

Only one due review runs for a registered active country during the weekly pulse. A candidate must retain a usable owned and controlled state or a proved contagion relationship, the last family is cooled down, the aligned receipt ledger has capacity, and a no-op branch defers the review when no candidate is valid.

Incident outcomes change the public Severity through the same clamped action path and expose only a qualitative current incident. Routine incidents do not delete factories or add Chaos; sustained center failure, deliberate liquidation, shared humanitarian pressure, and one-shot abnormal outcomes remain owned by their existing guarded systems.

## Financial Contagion

Financial Contagion activates only at Rising Chaos and spreads through proved relations such as faction, war, overlord, trade, guarantee, and neighboring economic links.

The sparse relationship ledger records source country, source episode, source receipt, qualitative exposure stage, and relationship type on the receiving country, with aligned target rows on the source.

Exposure is qualitative and bounded.

Partner actions can support, supervise, clear, supply, withdraw, contain, or convert a relationship according to the mapped target gates.

Provider support is counted once per globally unique source episode through a bounded receipt set, so one partner cannot farm a source while remaining able to support another valid episode.

Conversion calls the fail-closed API with the proved source and receipt and deepens an existing compatible crisis rather than duplicating it.

Event 34 suppliers enter through the supplier adapter and retain their own Overheating and contract-risk rules.

### Market exits and supply-gap purchases

Abandon the Distressed Market (with its quiet form) and Exploit Supply Gap trade a bounded, current-episode benefit for the acting country against a cost carried by the partner. None of them raises the actor's own Severity.

| Action | Actor benefit (current episode) | Partner cost |
| --- | --- | --- |
| Abandon | credit and trade relief for `abandon_relief_days`, and the link stops carrying the actor's weekly pressure to the partner | Severity shock if the partner is in its own depression; otherwise an existing exposure link rises one stage or a new link opens at Dependent; `great_depression_market_abandoned` opinion of the actor |
| Withdraw (the quiet form of Abandon, used when the partner is an ally, faction member, subject or overlord) | smaller trade relief for `withdraw_relief_days`, no diplomatic cost | smaller Severity shock if the partner is in its own depression; a new link opens only at Pressured |
| Exploit | industrial relief for `exploit_relief_days`; while Social Collapse is active, hidden social stress takes part of it back | Severity pressure on the partner and `great_depression_supply_gap_exploited` opinion of the actor |

All values live in `great_depression_market_exit`. The relief windows are `great_depression_market_abandon_relief_*`, `great_depression_market_withdraw_relief_*`, and `great_depression_supply_gap_relief_*` (due day plus episode id), read by `great_depression_rebuild_hidden_components` through the `*_relief_is_active` triggers. An abandoned partner joins the bounded `great_depression_severed_partner_countries` array, which `great_depression_process_contagion_network` skips. `great_depression_clear_market_exit_state` clears every window and the severed list at episode start, abort, retirement, and recovery cleanup.

The contagion row of a market exit is marked abandoned through the temporary input `great_depression_partner_outcome_hostile`, and the opening stage of a new link through `great_depression_partner_link_stage`. `great_depression_raise_partner_exposure_link` raises an existing link by `great_depression_partner_link_raise` and applies it once through `great_depression_apply_exposure`, so the ordinary conversion rules decide whether the partner falls into its own depression.

AI: liquidation gamblers and fiscal retrenchers still favour these exits, and abandonment gains weight when the partner is near paralysis, but the AI never abandons or exploits a faction member, ally, overlord, or subject (`great_depression_ai_partner_is_close_ally`) or a major partner.

When Financial Contagion activates on a crisis already under way, `great_depression_queue_contagion_activation_report` queues `chaosx.nr35.12` for the origin once per episode, a day later, with the contagion picture.
It freezes the partner count and the partner at the highest exposure stage when it is queued, so the report names the most exposed partner and how many partner economies are tied to the origin, or says that none is tied closely enough yet, and it never shows conversion odds.
An episode that opens with the evolution already active is covered by its opening report instead.

When a partner first joins the origin's material exposure set, `great_depression_queue_exposed_partner_report` queues `chaosx.nr35.14` for that partner.
The targeted value `great_depression_exposure_report_chain_<chain episode>` holds the unique spreading-chain episode, so the same chain reports to a partner once across its descendants.
The partner keeps a pending batch of origins and relationships capped at the contagion source cap, and origins reaching it before delivery are summarized in one report.
The report names the origin and the relationship (shared border, alliance, faction, overlord and subject, emergency agreement, or supply contract), describes the local bank and trade pressure, and points to the exposed-economy responses without treating the partner as being in a depression.

The first contagion conversion that opens a full depression from one source episode is marked by `great_depression_mark_first_contagion_spread`.
The source and converted descendants carry `great_depression_spread_news_sent`, and the converted country's opening report immediate sends `chaosx.nr35.15` once for the chain, naming the newly struck country and the origin.
Later conversions from the same chain use country reports and history without ordinary national news, and a deepened crisis never counts as a first spread.

## The Second Great Depression

Evolution III activates one global lifecycle at Totalen Chaos.

Activation itself grants zero Chaos.

The first concrete bounded worldwide-pressure application emits one announcement, one super-event, and one guarded abnormal-outcome Chaos receipt.

Worldwide pressure is lighter than a national crisis and is tracked in a bounded registry of valid normal civilian economies.

Worldwide conversion uses the preserved global activation source, one globally unique conversion receipt, a conversion interval, a cursor, and the Event 35 fail-closed API.

International recovery requires material contributions from distinct countries, recipient improvement, sustained proof, and no final supplier collapse.

Supplier risk can reset recovery proof without replaying the worldwide shock or creating a second global episode.

The global lifecycle progresses through shock, contraction, coordination, recovery, international reconstruction, and retirement.

`great_depression_queue_global_news` sends three world news events, each once per global episode id, so a stage that falls back and returns never replays it, and none while The Second Great Depression evolution is switched off: `chaosx.nr35.16` when the world enters International Reconstruction, `chaosx.nr35.17` when the global episode retires, and `chaosx.nr35.18` for the first supplier collapse of the episode, naming the supplier.
The reconstruction and end news name the country where the worldwide depression began only when the activation source was known, through `global.great_depression_news_origin`, which is copied before retirement clears the global event target.
They describe the world economy and never imply that every country is in a national depression.
All three use the registered news picture, because the report pictures have report dimensions.

### Global Recovery Conference

A country in its own depression convenes the conference during Fragmented Recovery or International Reconstruction, when its phase is Stabilization or Recovery or its Severity trend is falling (`great_depression_can_start_global_recovery_conference`).
Only one conference meets in each global episode (`global.great_depression_conference_episode_id`). Convening pays the reconstruction quote, changes no Severity, records the convener, and opens the bounded participant arrays `global.great_depression_conference_participants` and `_participant_weights` with the convener as the first seat.
Countries in their own depression, countries with an open contagion exposure, Industrial Boom suppliers, and countries that contributed to the worldwide recovery in this episode see Join the Global Recovery Conference (`great_depression_conference_join_surface_is_ready`, which also opens the decision category for them). Joining pays the reconstruction quote through `great_depression_can_pay_conference_share`, outside the national and exposure slots, and is closed to countries that withdrew from their international commitments.
The daily global pulse resolves the conference on its due day (`duration_days`) through `great_depression_resolve_recovery_conference`. It succeeds when the participants that still have a viable economy reach `success_participant_minimum` countries, `success_major_minimum` majors, and `success_industrial_weight_minimum` industrial weight (civilian factories twice, military factories and dockyards once, at most 100 per country).
Success during Fragmented Recovery starts a stopped recovery proof or moves a running one `proof_advance_days` forward, and during International Reconstruction it brings retirement the same number of days closer; every other proof condition still applies. Participants in a depression lose `participant_severity_relief` Severity, and the others gain `great_depression_recovery_conference_dividend` for `dividend_days`.
Failure during Fragmented Recovery stops the proof and returns the world to the Worldwide Depression stage, with one guarded Chaos change of `failure_chaos` per global episode; failure during International Reconstruction restarts the wait before retirement. Either failure queues the world news `chaosx.nr35.19` once per global episode through `great_depression_queue_global_news`, naming the convener, and never while the evolution is switched off.
`great_depression_clear_recovery_conference` closes a conference without an outcome when its global episode ends, retires, or the evolution is switched off, and the global ledger reset clears the once-per-episode receipts.
Values live in `great_depression_conference`.

### Competitive devaluation and withdrawal from international commitments

Competitive Devaluation or Currency Break costs the market-clearing quote (political power, stability, war support), is available once per country in each global episode (`great_depression_devaluation_global_episode_id`), and gives standard Severity relief at once plus a trade-relief window for `devaluation_relief_days`.
`great_depression_apply_devaluation_partner_pressure` then marks up to `devaluation_partner_cap` partners, first the actor's contagion exposure targets and then registered worldwide-pressure countries with a proved relationship, with `great_depression_currency_pressure_due_day` for the current global episode.
A marked partner adds `devaluation_partner_exposure_score` to its worldwide classification and, if it is in a national depression, `devaluation_partner_trade_stress` to its hidden trade stress.
Each devaluation adds `devaluation_recovery_drag_days` to `global.great_depression_global_recovery_drag_days`, capped at `recovery_drag_maximum_days`, and the international-reconstruction proof must hold that much longer. The drag resets with the global ledgers.

Withdraw from International Commitments costs the policy-review quote (political power and stability) instead of the reconstruction quote.
`great_depression_remove_global_contribution` removes the country's row and recorded industrial weight from the global contribution ledger, removes its contribution receipts, and clears its contribution flags.
It keeps `great_depression_international_debt_conference_complete`, because the debts rescheduled at that conference stay rescheduled and the flag also spares the Debt Overhang scar; it clears `great_depression_reconstruction_employment_fund`, so the fund's demand relief ends with the country's share of the common fund.
It also takes the country's seat and industrial weight off an open Global Recovery Conference through `great_depression_remove_conference_participant`.
`great_depression_commitments_withdrawn_global_episode_id` closes every global contribution decision for the rest of that global episode through `great_depression_global_commitments_are_open`, and `great_depression_increment_global_contribution` refuses a withdrawn country.
The same check is part of the International Reconstruction mission's activation and context, so the mission, whose objective needs a contribution, ends without a penalty instead of timing out.
The decision tooltip names the ended fund, the conference seat, and the ended mission when they apply.
The country's civilian commitment is released, it gets light Severity relief at once, and a fiscal-relief window runs for `withdrawal_relief_days`.

Neither action raises the actor's Severity. Values live in `great_depression_currency_action`.

### Economic blocs

Two bounded global member sets record the blocs: `global.great_depression_clearing_bloc_members` and `global.great_depression_protectionist_bloc_members`, each capped at `great_depression_bloc.member_cap` (12).
The Clearing Agreement (Financial Contagion, and a supplier in The Second Great Depression) puts both the actor and the partner into the clearing bloc, counts once per global episode toward the worldwide recovery during the worldwide depression, and the clearing-bloc incident puts the crisis country and its incident partner there.
`great_depression_join_clearing_bloc` records `great_depression_clearing_bloc_due_day` for `clearing_term_days` (365) and adds the timed `great_depression_clearing_bloc_membership` modifier (trade opinion +10%); a member that joins again renews its term.
While a member is in its own depression, `great_depression_rebuild_hidden_components` gives it the clearing trade relief, and a member under worldwide pressure subtracts `clearing_exposure_relief` from its worldwide exposure score.
The daily global pulse (`great_depression_process_economic_blocs`) removes clearing members whose term has run out or which no longer exist.

Protect the Home Market closes the actor's foreign exposure, and during the worldwide depression it also puts the actor into the protectionist bloc for the rest of the global episode without raising the actor's Severity.
Members carry `great_depression_protectionist_bloc_membership` (trade opinion -20%, consumer goods +2%, factory output growth +2%), which stands for the trade outsiders take elsewhere.
A member under worldwide pressure subtracts `protectionist_exposure_shield` from its worldwide exposure score, which can drop it into a lighter contraction tier, and a member in its own depression adds `protectionist_global_pressure_factor` (0.15) instead of the ordinary worldwide pressure factor (0.35) to each Severity update during the early worldwide stages.
Each member lengthens the international-reconstruction proof by `protectionist_drag_days_per_member` (10) days, at most `protectionist_drag_maximum_days` (40), computed from the current member count so the drag falls when members leave.
The protectionist bloc ends at global retirement, at the start of a new global episode, and when no worldwide episode is active or the evolution is switched off.

A new national episode removes the country from both blocs in `great_depression_reset_episode_policy_state`, so no membership carries relief into a later national episode; the country can rejoin.
Clearing membership is not ended by global retirement or by recovery, because the payments arrangement keeps a post-crisis purpose until its term runs out.

`great_depression_check_bloc_formation` counts living members and majors after every join; at `formation_member_minimum` (3) members with at least `formation_major_minimum` (1) major, `great_depression_queue_global_news` sends `chaosx.nr35.20` (A Clearing Bloc Forms) or `chaosx.nr35.21` (A Protectionist Bloc Forms) once per global episode, naming the country whose action formed the bloc and the member count, never outside a worldwide episode or while the evolution is switched off.
The Clearing Agreement needs room for every newcomer (`great_depression_clearing_bloc_can_take_pair`): a bloc below `pair_room_limit` (11) members takes two newcomers, and a bloc below `member_cap` takes one when the other country already belongs, so a decision never leaves one of the two countries outside.
The protectionist bloc joins one country at a time and refuses a member beyond `member_cap`.
The AI prefers blocs with close allies, does not spend an action renewing a clearing pair that is already in the bloc, and does not raise a protectionist wall during Fragmented Recovery or International Reconstruction.

## Shared-system adapters and Chaos accounting

Event 35 uses owner adapters for humanitarian pressure, occupation, Deaths, Condemnation, environmental effects, event history, evolutions, clusters, Event 21 civil conflict, Event 34 suppliers, and the shared Chaos meter.

Evolution activation and lifecycle bookkeeping do not add Chaos.

Guarded Event 35 Chaos receipts are reserved for concrete abnormal outcomes such as maximum national failure, national breakdown, extreme social outcomes, civil conflict, worldwide pressure, supplier collapse, or the end of the worldwide depression.
The first worldwide wave adds `worldwide_wave_chaos` (10).
A spreading chain of Financial Contagion pays `contagion_conversion_chaos` (2) once and `contagion_chain_milestone_chaos` (3) when the same chain converts its `contagion_chain_milestone_conversions`-th (3) economy; the global chain ledger keeps the `contagion_chain_ledger_cap` (16) most recent chains.
National recovery adds or removes no Chaos, and security responses create no Event 35 deaths: deaths reach the Deaths ledger only through famine and Event 21.

Shared owners put pressure on a depression through their own public state and Event 35 writes nothing back:

- A Depression Center where the famine owner reports a visible food problem adds `famine_demand_pressure` and `famine_social_pressure` (1 each) to the hidden update, holds reopening certification (the project pauses and fails after `center_project_pause_fail_days` of continuous hold), and is the only place the hunger-riot incident can occur.
- A center in a state with severe chemical contamination or the nuclear fallout modifier cannot certify reopening until the owner clears it.
- Condemnation sanctions against the country (`great_depression_trade_isolation_is_active`, the read Event 50 will join) add `sanction_trade_pressure` to hidden trade stress and make the Finance and Trade doctrine pay `sanction_cost_factor` (1.25) times the convoys and political authority.

Global and local receipt totals are kept separately so that the event cannot duplicate shared sources or replay the same outcome.

## AI and weighted logic

AI doctrine and action behavior is split among relief coalition, strategic mobilizer, financial stabilizer, state coordinator, fiscal retrencher, and liquidation gambler profiles.

Affordability, urgency, wartime industry needs, financial pressure, center condition, partner safety, supplier Overheating, and locked-state gates modify action choices.

The baseline, Financial Contagion, Social Collapse stage, and final Social Collapse outcome pools use centralized common, uncommon, rare, major, severe, positive, and no-incident weights with target validation and last-family cooldowns.

Event choice weights in `great_depression_event_option_weight` cover the crisis report, coup response, regional-autonomy response, and National Breakdown outcomes, and the single-option recovery, contagion, social, exposed-partner, and world-news events read their own keys there.

The named probability scenarios are defined in `docs/specs/035_great_depression_specs/035_great_depression_ai_probability_matrix.md`. The implementation report records the current evidence boundary: source and candidate-pool inspection succeeded, but the MCP transport closed before the required named evaluations, sweeps, sequence checks, and same-scenario comparison completed.

## Achievements

Event 35 owns six achievement contracts: Back to Work, Every Center Reopened, Containment Line, Social Peace, Lean but Standing, and Recovery of Nations.

Each contract is driven by durable proof written by Event 35 evaluators and is exposed through eligible, grey, and not-eligible assets. The contracts are grouped in the single root Chaos Redux achievement registry, which owns `unique_id = chaos_redux_achievements`.

Event 34's Long Fall remains owned by Event 34 but shares the Event 35 asset package and collapse proof.

## Presentation and asset wiring

`interface/035_great_depression.gfx` registers the decision category, every decision and mission sprite, condition and legacy sprites, center-status sprites, evolution sprites, and the seven achievement texture triplets. The achievement contracts are grouped in `common/achievements/chaos_redux_achievements.txt`, and `interface/035_great_depression_achievement_aliases.gfx` supplies the ID-aligned inherited Event 34 sprite names.

`interface/chaosx_pictures.gfx`, `interface/035_great_depression.gfx`, and `interface/chaosx_super_events.gfx` register the six scene images, category picture, and super-event image.

Together with six event/news images, the decision-category picture, and the super-event image, the Event 35 visual package contains 80 runtime DDS files: the original 68 plus the twelve national-spirit icons below.

The Emergency Government spirit, the six political aftermath spirits, and the five country recovery scars have their own Event 35 art under `gfx/interface/ideas/035_great_depression/`, 60x68 with a two-pixel transparent guard, and keep their sprite names:

- `idea_035_great_depression_emergency_government.dds`: decree with red wax seal held down by a steel helmet, brass desk stamp.
- `idea_035_great_depression_aftermath_social_compact.dds`: worker and employer handshake over a signed agreement and pen.
- `idea_035_great_depression_aftermath_emergency_rule.dds`: stack of stamped permits under a rubber stamp with a commissioner armband.
- `idea_035_great_depression_aftermath_planning_settlement.dds`: factory under a plain red banner with a cogwheel and a planning ledger.
- `idea_035_great_depression_aftermath_corporate_rescue_order.dds`: green company safe bound by a sealed government ribbon, bonds and gold on top.
- `idea_035_great_depression_aftermath_regional_autonomy.dds`: provincial town hall with three plain pennants on a regional map fragment.
- `idea_035_great_depression_aftermath_labor_scar.dds`: broken blank picket sign, trampled cap and police truncheon on cobblestones.
- `idea_035_great_depression_scar_debt_overhang.dds`: loan ledger and bonds chained with a padlock and iron ball, spilled coins.
- `idea_035_great_depression_scar_foreign_credit_dependence.dds`: balance scale where one foreign coin and a top hat outweigh export crates and grain.
- `idea_035_great_depression_scar_emergency_controls.dds`: padlocked iron factory gate with a stamped permit and ration coupons.
- `idea_035_great_depression_scar_labor_bitterness.dds`: three grim workers with folded arms before a cold factory chimney.
- `idea_035_great_depression_scar_policy_fatigue.dds`: sagging pile of crossed-out programmes, spilled ink, snapped pen and a slumped homburg.

Each was generated as an original painted icon with a genuinely transparent background through the gptimage route of the user's ChatGPT image model (native alpha passed on every source, so no background removal was used), fitted with Lanczos resampling, converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`, and validated as one-level BGRA DDS with exact alpha round trips. The prompts, sources, processed PNGs, review sheet, DDS validation and reference scan are in the local `docs/assets/035_great_depression/` workspace (`source_png/ideas_round2/`, `processed_png/ideas_round2/`, `audit/idea_round2/`). The two lasting district modifiers reuse the reopened and hollowed center icons.

The regular icon families are eight decision/category icons under `gfx/interface/decisions/035_great_depression/`, eight mission icons in the same folder, three evolution icons in the same folder, twenty-four condition, legacy, emergency-government, aftermath and scar icons under `gfx/interface/ideas/035_great_depression/`, and eight state-status icons under `gfx/interface/state_modifiers/035_great_depression/`.

The idea or national-spirit textures use the installed 60x68 `national_spirit_ideas_grid` canvas, and the three evolution textures are consumed by the existing event-log evolution-detail image bridge.

The complete per-file visual audit, source-to-runtime crosswalk, orphan scan, repair evidence, and current review disposition are in `docs/assets/035_great_depression/audit/asset_audit.md`.

The achievement family contains eligible, grey, and not-eligible files for each of the six Event 35 contracts and Event 34 Long Fall under `gfx/achievements/`.

The scene files are `report_event_great_depression.dds`, `report_event_great_depression_boom_collapse.dds`, `report_event_great_depression_contagion.dds`, `report_event_great_depression_social_collapse.dds`, `report_event_great_depression_recovery.dds`, and `news_event_great_depression.dds` under `gfx/event_pictures/035_great_depression/`, plus `decision_cat_picture_great_depression.dds` and `gfx/super_events/035_great_depression/super_event_great_depression.dds`.

The super-event uses visible slot `105`, playback ID `106`, the researched Roosevelt quote, the Keynes reaction, and the unique CC0 recording of Chopin's *Funeral March in C minor, Op. posth. 72 no. 2* performed by Aya Higuchi.

The runtime audio is `sound/035_great_depression/super_event_106_second_great_depression.wav`, while the source, processed OGG, rights evidence, and checksums remain under `docs/assets/035_great_depression/`.

## Localisation, logs, and catalog

`localisation/english/035_great_depression_l_english.yml` owns event, decision, mission, cost, status, evolution, achievement, news, and super-event text.

The seven achievement contracts expose the engine-facing `_NAME` and `_DESC` keys in the shared registry without unreferenced lower-case title or description aliases.

The Event Log shows the catalog Details text for Event 35, and a row opened from History also names the affected country and its Depression Severity when the crisis struck.

Financial Contagion, Social Collapse, and The Second Great Depression show their type, title, body, summary, stage, and tier in the History, Evolutions, and Event Details tabs, and Event Details lists all three as evolution rows the player can switch off.

A random or cluster firing leaves one history row: the shared dispatcher records it, and an hour later Event 35 fills in the selected country and the Severity it started with, whichever order the engine runs the dispatcher and the event in. If the dispatcher left no row, Event 35 records a full row instead. Inherited, conversion, and relapse starts record their own row.

The catalog source is `docs/spreadsheets/chaos_redux_events_catalog.xlsx`.

Event 35 is recorded as Minor Repeatable, Chaos level 1, Negative Economy cluster member, and Low severity, and the three catalog CSVs are export-only derivatives.

## Test-country support

`chaosx_cxt_extension_event035_great_depression_apply` is the package-owned idempotent setup effect, and `chaosx_cxt_extension_event035_great_depression` is its matching modifier-free hidden-idea carrier.

`common/on_actions/035_great_depression_cxt_on_actions.txt` registers its hidden-idea carrier during startup and through the narrow `on_daily_CXT` fallback.

The setup records the package's inert readiness and public-range contract without starting a depression, assigning an economy, or creating runtime acceptance fixtures.

## Future plans and suggestions

Future depth can add more doctrine-specific event prose, more regional center descriptions, additional historically grounded supplier relationships, and country-specific AI preferences without changing the single public Severity contract.

Any future expansion should preserve the fail-closed caller proofs, aligned bounded registries, one-shot consequence receipts, owner adapters, and the separation between national crisis severity and lighter global pressure.

No dedicated scripted GUI is required by the current package; if one is introduced later, it must remain Event 35-owned and use the mandatory event UI worker and MCP visual workflow.

## Report and news pacing

The opening report is sent once per national episode.
Deepening changes the crisis category and history without repeating the opening report.
An independent or Event 34 inherited start outside a worldwide depression sends one national news.
A financial contagion chain sends one world news when its first secondary depression begins, and descendants share that announcement guard.
Worldwide conversions send local reports and leave world coverage to the one global onset news, the super-event, and the separate guarded world-stage outcomes.
An exposed country receives one report per spreading chain, with simultaneous independent origins summarized together.
Delivery consumes the pending batch immediately, so closing a report does not schedule another popup.
A rejected human firing receives `chaosx.nr35.22`, explaining why no viable independent country can begin a fresh depression.

The rejected-firing report reuses `GFX_report_event_great_depression`, registered in `interface/chaosx_pictures.gfx`, and needs no new artwork.
Source tests in `.tools/test_event035_reports.py` cover 28 worldwide conversions, a branching financial chain, deepening replay, repeat national episodes, and exposure aggregation.
They record native event scheduling and do not emulate the game's delayed delivery or rendering.
Future review should preserve these limits when another cross-country entry is added.

## Conference supplier quotes

The Event 034 supplier adapter prepares the same scaled material quote used by other reconstruction participants, including suppliers without an at-risk contract.
The conference refreshes its registered at-risk suppliers' quotes when it opens.
The join action spends political power, fuel, and convoys, commits civilian capacity, and takes one conference seat.
Exact quoted reserves satisfy the availability check.
The Event 034 owner's late-entry hook remains required for a newly viable boom country with no earlier Event 035 quote or contract.

## Compact category and test-package upkeep

The national category shows Severity and direction, the recovery phase and doctrine, and the selected center in three lines.
Hovering the active depression spirit explains the chief pressures and next threshold.
The mission rows retain their named objectives and timers.
The source text budget is reviewed, while native wrapping and hover placement remain live checks.
The CXT daily fallback registers an unseen Event 035 package and marks it pending for Apply Registered Systems, without applying content by itself.
The source execution suite checks nested registration output storage, one-time registration, inert daily replay, and player-triggered application.

The asset audit's absent `icon_manifest.json` reference is reconciled to the existing `docs/assets/035_great_depression/manifest.md`.
The existing decoded runtime inventory contains 80 DDS entries with zero decode errors.
All twelve additional spirit icons retain their source/processed PNGs, registered 60x68 RGBA DDS files, and source-specific review sheet.
Their producer records `gptimage MCP`; this pass reuses the files and does not certify equivalence to a current native ImageGen call.
The local asset docs remain under the repository's ignored asset-workspace policy, with these durable facts recorded here.
