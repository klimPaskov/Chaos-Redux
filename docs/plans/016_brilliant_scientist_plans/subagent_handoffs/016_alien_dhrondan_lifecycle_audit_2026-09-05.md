# Event 016 Alien Infantry and D'Rhondan lifecycle audit

Date: 2026-09-05

Owner: `/root/alien_dhronda_lifecycle_audit`

Status: bounded audit complete with one narrow P2 source refinement; no commit or staging performed by this subagent.

Scope: Alien Infantry contact receipts, ordinary and Event 019 deferred landings, cancellation and refund, rebellion pulse tiers, and D'Rhondan formation transfer. D'Rhondan focus rewards, unit and equipment definitions, GUI implementation, biological or Portal systems, foreign systems, portraits, catalogs, and the alien 3D runtime were not edited.

## Executive result

The confirmed local defect was in `dhrondan_rebellion_medium_tier_is_active`. Its arrival arm tested eight or more arrivals without using the declared nine-arrival ceiling, so ten or more arrivals with Chaos below 800 and strain below 50 fell through the resolver's low 10% branch. The worktree refinement at `common/scripted_triggers/016_dhrondan_contact_triggers.txt:177-201` now requires eight through nine arrivals for the arrival-based medium arm while retaining independent strain and Chaos medium arms.

The five source-counted contact receipts, invoking-country state registry, fixed API transaction, 90-day country-scoped pulse, and D'Rhondan transfer transaction were source-reviewed and no additional local P1/P2 defect was confirmed.

An exact-2,000-gun exception remains a cross-owner P2 integration issue: the voluntary landing decision routes through the Event 026 Black Friday adapter, whose dynamic amount path can quote a sale amount. The fixed API, Event 019 deferred commit, and D'Rhondan initial-force batch remain canonical 2,000-gun paths. Event 026 is outside this ownership boundary and was not edited.

At resume, the trigger file already had a related staged hunk using `dhrondan_arrival_count < constant:dhrondan_contact.rebellion_arrival_high_minimum`. The unstaged worktree refinement replaces only that upper-bound expression with the existing `rebellion_arrival_medium_maximum` check. The file therefore shows `MM`; the parent must resolve the staged/worktree state without resetting either side.

## Issue list sorted by severity

### P2 fixed: medium rebellion arrival band was not bounded

Before the refinement, the medium trigger's first OR arm was arrivals greater than or equal to eight with no upper bound. The resolver checks high, then medium, then low, so `ARRIVALS_10_CHAOS_799_STRAIN_49` was low 10% instead of the accepted low/medium/high partition.

After the refinement, the arrival arm is an AND of `rebellion_arrival_medium_minimum` and `rebellion_arrival_medium_maximum` using `check_variable` with `compare = less_than_or_equals`. Strain at least 50 and Chaos at least 800 remain independent medium inputs, and high remains arrivals at least 10 plus Chaos at least 800.

### P2 cross-owner blocker: Black Friday may vary the voluntary landing debit

`alien_infantry_begin_landing_reservation` calls the Black Friday reserve adapter from `common/scripted_effects/026_black_friday_effects.txt`. Its Event 026 sale branch can pass a dynamic amount to the Alien Infantry amount API, while the Event 016 contract calls for exactly 2,000 laser weapons.

This subagent did not edit Event 026 or force a bypass because that would overwrite another workstream's ownership and could change the accepted sale mechanic. Parent review is required before claiming exact 2,000 for every voluntary decision route.

### Evidence blockers, not source defects

The exposed MCP inventory has no `hoi4_decision_inspect` route and no callable `chaosx_ai_probability_auditor` route. Decision evidence therefore comes from the mandatory GUI inspect/render plus source review.

Focused event scans returned `EVENT_INSPECTED_PARTIAL` and the full Event 016 state-flow/render retries timed out with `tool call failed ... timed out awaiting tools/call after 180s`. The focused report has `helpers: 0` and thousands of unresolved workspace nodes, so it is not full helper or lifecycle proof.

The targeted map inspections for state 508 and connected/disconnected-state evidence timed out with the same 180-second server timeout. No map rewrite was attempted.

Current probability evaluate and before/after compare both returned `PROBABILITY_SURFACE_EMPTY`; the random-list adapter reported no weighted block for the supplied source overlay. No fresh normalized probability claim is made.

## Decision category lifecycle notes

`016_alien_infantry_landing_category` has one visible state-targeted landing action and one active landing mission. The category is visible only after contact and remains visible when empty, so the player can see the state and cooldown context without a wall of actions.

`016_dhrondan_contact_category` exposes the status row, two expedition actions, the Honor Accord action, two expedition missions, and one 90-day rebellion mission. It is visible for an active envoy route, pact, or expedition.

No category has more than six visible primary actions or more than three simultaneous active missions. No dedicated scripted GUI exists for these decisions, so no event-owned GUI worker or GUI rewrite was required.

## Contact, landing, and registry audit

`alien_infantry_has_contact` is the OR of the five independent receipt variables: Kruger pact, Mengele expedition, Event 019 provider 508, D'Rhondan sovereignty, and future source. Reconciliation computes the aggregate flag without deleting any receipt, so removing one source preserves the other four.

The ordinary reservation gate requires contact, no pending reservation, no cooldown, no world end, at least one valid controlled state, and at least 2,000 laser weapons. Reservation debits exactly 2,000, stores the selected state on the invoking country, starts a seven-day mission, and blocks a second pending reservation.

Cancellation clears the pending flag before refunding the saved transaction amount or the fixed 2,000 fallback, removes the mission, clears reservation metadata, and settles the Black Friday transaction once. State loss follows the same clear-before-refund ordering and applies the 30-day cooldown only after a successful arrival.

The registry helper saves the invoking country and selected state before entering state scope, then appends the selected state once to the invoking country's `alien_infantry_landing_state_registry`. Event 019 deferred mode commits the registry, marker, counters, cooldown, and D'Rhondan callback only after its outer transaction proof; rollback refunds the deferred 2,000 debit once.

Ordinary success creates exactly one locked D'Rhondan landing cohort at the saved state, verifies the division delta, registers the state, increments arrival, Alien Presence, Pact Strain, and landing history, settles the transaction, applies cooldown, and calls the D'Rhondan presentation callback. Deferred Event 019 success suppresses ordinary telemetry until commit.

## Rebellion pulse and probability boundaries

`dhrondan_refresh_rebellion_pulse` is country-scoped and creates at most one active 90-day mission after pact, six arrivals, strain 30, and Chaos 600 thresholds are met. It does not iterate the world.

The resolver is exclusive in order: high 40%, medium 20%, low 10%, and no revolt as the complement to 100%. High requires arrivals at least 10 and Chaos at least 800. The patched arrival-based medium tier is exactly arrivals 8 or 9; strain at least 50 or Chaos at least 800 independently selects medium unless high has precedence. Eligible arrivals 6 or 7 with strain 30-49 and Chaos 600-799 remain low.

The named source scenarios are `ARRIVALS_6_CHAOS_600_STRAIN_30`, `ARRIVALS_7_CHAOS_799_STRAIN_49`, `ARRIVALS_8_CHAOS_600_STRAIN_30`, `ARRIVALS_9_CHAOS_799_STRAIN_49`, `ARRIVALS_10_CHAOS_799_STRAIN_49`, `ARRIVALS_7_STRAIN_50`, `ARRIVALS_7_CHAOS_800`, `ARRIVALS_10_CHAOS_800`, and `ARRIVALS_12_CHAOS_900`. The prior accepted evidence records 10/20/40 conditional revolt weights at the corresponding boundaries; the current compare could not produce a surface after the source overlay.

## D'Rhondan formation transaction notes

Formation captures the current pact host's marked-state registry, selects a viable host-controlled marked capital first, and falls back to a passable host-owned marked state when a third party controls the first candidate. It transfers every still-host-owned marked state, gives D'Rhondan claims on marked states owned by others, preserves third-party controllers, restores host cores where required, and sets D'Rhondan capital without assuming connectedness.

Disconnected owned components are flood-filled within D'Rhondan's own state scope and receive one initial cohort per enclave. Remaining bounded cohorts deploy at the capital. Supplemental cohorts beyond the safety cap receive separately recorded 2,000-gun reservations as specified by the accepted formation contract.

Host cleanup removes exact D'Rhondan landing cohorts without refund and transfers all remaining host Alien Laser Weapon stockpile to D'Rhondan. The batch path suppresses ordinary landing telemetry and does not consume ordinary cooldown flags.

Formation initializes the existing D'Rhondan country idempotently, reconciles sovereignty, and uses global one-time guards for opening stockpile and initial force. Existing D'Rhondan joins the current country path and does not duplicate opening grant, force, or enclave cohorts.

## Mission quality notes

| Mission | Owner and category | Requirement and duration | Success | Failure and duplicate risk |
| --- | --- | --- | --- | --- |
| `alien_infantry_landing_mission` | Invoking country, Alien Infantry landing category | Valid reservation; seven days | One cohort, one registry append, telemetry, cooldown, callback | Cancellation/state-loss refund is once-only; timeout routes through the same API and pending flag blocks duplicates |
| `dhrondan_kruger_expedition_mission` | Kruger host, D'Rhondan contact category | Valid character obligation; 180 days | Pact establishment and cleanup | Invalid character or world end removes mission and restores the route; in-progress flag prevents duplicate expedition |
| `dhrondan_mengele_expedition_mission` | Mengele country, D'Rhondan contact category | Valid completed project route; 180 days | Pact establishment and cleanup | World end removes mission; in-progress flag prevents duplicate expedition |
| `dhrondan_rebellion_pulse_mission` | Pact host, D'Rhondan contact category | Six arrivals, strain 30, Chaos 600; 90 days | Exclusive revolt resolver and bridge event | Eligibility loss removes mission; triggered flag and active-mission check prevent duplicates |

## Cognitive load and player-facing clarity

The landing category presents one state-targeted action and one mission, with the selected state, 2,000-gun reserve, seven-day arrival, refund condition, and cooldown exposed through custom tooltips.

The contact category's status row names Alien Presence and Pact Strain and explains their thresholds and responses. Two expedition actions, Honor Accord, two expedition missions, and one pulse mission remain within the accepted density limits.

There are no raw unlabelled counter rows. Player-facing values have a stated meaning and response: Presence records successful arrivals, Strain controls the pact pressure threshold, Chaos supplies the world pressure threshold, and the 90-day pulse is the action window.

## Cost and requirement audit

The ordinary landing has one spendable cost, exactly 2,000 Alien Laser Weapons, shown with `£GFX_alien_laser_weapon_equipment_medium`; the seven-day reservation is a requirement/timer, not a second spendable cost.

Kruger and Mengele expeditions each spend 50 political power and 500 fuel using `£pol_power` and `£fuel_texticon`. Honor Accord spends 75 political power. No in-scope decision has more than four distinct spendable cost types.

The Black Friday dynamic amount exception is the only unresolved exact-cost integration point. It is recorded as a cross-owner blocker rather than silently reinterpreted.

## AI validity and route-lock notes

Landing AI requires contact, a valid controlled target, no pending reservation, no cooldown, no world end, and the fixed stockpile gate. Expedition AI checks the owning route, project and character state, in-progress flags, and world end. The rebellion mission has no target and is intentionally activated only by the country-scoped eligibility helper.

The expedition route helper prevents Kruger and Mengele from being active simultaneously and prevents a completed pact from reopening either route. No invalid country target, impossible border, or world-iterating lifecycle action was found.

The weighted random resolver uses the mandatory random-list inspection, but current dynamic evaluation could not bind the source helper to the MCP fixture. Do not treat the prior conditional artifacts as a current post-patch probability compare.

## Localisation and tooltip gaps

Landing cost and timer text use the equipment texticon and explain reservation, refund, arrival, Presence, Strain, and cooldown. Contact status and rebellion text state the six-arrival, strain, Chaos, 90-day, and 10/20/40 boundaries. No localisation change was required for the trigger-only patch.

The exact-cost Black Friday wording remains potentially inconsistent with the fixed Event 016 contract when a sale is active. Event 026 owner review is required for a final wording and behavior decision.

## Cleanup and exploit-risk notes

The pending flag is cleared before refund, transaction settlement is guarded, mission removal is explicit, and stale state targets are cleared when no reservation remains. One pending reservation and the 30-day cooldown prevent equipment-farming loops.

D'Rhondan cleanup removes host alien cohorts without refund and transfers the remaining laser stockpile once. Initial force and opening grant are globally guarded, enclave deployment is bounded, and existing-DHR reinitialization is idempotent.

## Changed files and identifiers

Changed in the worktree: `common/scripted_triggers/016_dhrondan_contact_triggers.txt`, identifier `dhrondan_rebellion_medium_tier_is_active`.

No localisation, decision, category, event, constant, scripted effect, on-action, country, focus, model, unit, or equipment file was changed by this subagent.

## MCP artifacts and validation

The mandatory GUI inspection used the standard `country_decisions` window with the `event016_contact_landing` scenario. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0947163cd5f8316574747e8ea3b4624661b71d940db05acace6e7bfc79a5e056/2d9cec8b836a1ff982227b7d214cfdcfe988230eca2c0415c67afb38064/gui-inspect.6e90e4b794584f61.json`.

The GUI render covered normal, active, warning, disabled, empty-list, and long-text states at 1920x1080. Representative artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/9d866b384aca036505c665e488f4a0b4d8d509e35bec50236cc56b67a62f1b48/country_decisions-full.png`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/918af2e949709f328c7024e743d985a3073b703cfbf5057672666ed8c52129e3/4c153c0587b6eb627ec07ee9932ac34e587ab9dbb7ddd9634795f68b650a2397/country_decisions-layout.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fb0b532de9e74688475876497e0c730054982a4cd72a32601fd26e213bebd66d/7e30e7ef36b6869b72f4615af001e0d39fb2c9379d0ca30e30d562c51a55e0e8/country_decisions-state-matrix.json`. The production route is an offline approximation with unrelated global diagnostics, so no GUI defect claim is made.

Current Event Inspector artifacts include the Event `.40` scan `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/74338c34fb39d863a8bcbe0bc0d6a36c9f9abae3ed71ca5bf970ce4d1c0e1e1b/1cf2b3c1a9c8555e3c1b80a0e7defe47cd0266ed24607e62569334eb6b2e1da9/event-scan-32f4ad8d847c.json` and focused `.47`/`.48` scans at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/920b0cac0a6c5c985dd0ac53aff4513b06bec34d8b5c8992a3e8c9a81ecb9898/c3893f050d11b9ab1e8f21f10fe11a9f1b6304f49066bd0e350346a93c7c21b3/event-scan-fa39cc8b8775.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/622b3276a728c7b7236dd2b4d2d6fbbcccb05cf9de1e80a3854b458cb0e98bd8/50ff51d057fba0b52b56a5fdb62263e02cf39d1a1349f1aab9883a8ebbb8bb65/event-scan-fa39cc8b8775.json`. These are `EVENT_INSPECTED_PARTIAL`, with focused/global lifecycle coverage deferred.

Probability source inspections returned artifacts `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7ef4eabeee5e4fe315f03cb3cb3e3b3ffc19a09b2e19a797114adb8f70b2faad/1959bee4a8d1d44a8b61c0c9e0fa240455cf644aaa813a06b0c03dc74bf806bf/probability-inspect-70b3532462ab.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/269cc27b641c07102b448c65a4964a2bc0421a4a6cac3e2e4b503a6be5b1bbc2/3346c151eaf2ddf971807fc1d6903cdd7e4b529434bd5efac97f6a06248cc64a/probability-inspect-7599a442e217.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29d927aa2a858132b63f032ccbef5caac87385578f0c95840b3c90336ea96b7e/4c826b2f0e5ca00e7783d3ac3d66b6ed16b276709dfb00e066f4f6bf6cce64a9/probability-inspect-9927b030ceeb.json`. The current evaluate returned `PROBABILITY_SURFACE_EMPTY`, and the before/after compare returned the same blocker after the 103.6-second server call.

The required map inspect for state 508 and related disconnected-state evidence timed out awaiting tools/call after 180 seconds. The decision inspector and named probability auditor routes were not exposed.

Targeted static validation confirmed that the trigger block contains both `rebellion_arrival_medium_minimum` and `rebellion_arrival_medium_maximum`, uses `compare = less_than_or_equals`, and retains independent strain and Chaos OR arms. No Hearts of Iron IV process was launched.

## Remaining issues and parent actions

Resolve the `MM` staged/worktree state in the trigger file while preserving concurrent work. Confirm whether Event 026's Black Friday discount is accepted for the voluntary landing route or must be excluded to certify exact 2,000-gun debits everywhere.

If MCP service capacity returns, rerun probability compare and sweep over the named revolt boundaries with the same scenario-set id, then perform the disconnected-state and existing-DHR map inspections. Do not claim those results from the partial or timed-out artifacts above.

No other simplifications were introduced by this audit. The listed MCP, cross-owner, and live-validation limits are explicit blockers, not substitutes for the requested lifecycle checks.

Plan handoff path: `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_dhrondan_lifecycle_audit_2026-09-05.md`.
