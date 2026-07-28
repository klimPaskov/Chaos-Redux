# Event 006 pre-wave crisis architecture audit

> Dated-snapshot notice (2026-07-28): The focused `006_automatic_ladder_host_crisis_completion_audit_2026_07_28.md` supersedes this audit's Command Power cost-trigger and active-category findings with source-repair evidence. Retain this file for its presentation-race, requester-disappearance, pressure-semantics, and runtime-evidence risks; it is not the current authority for the repaired cost/visibility surfaces.

## Scope and evidence

This audit covers the host-facing crisis surfaces in `common/script_constants/006_independence_wave_crisis_constants.txt`, `common/scripted_triggers/006_independence_wave_crisis_triggers.txt`, `common/scripted_effects/006_independence_wave_crisis_effects.txt`, `common/decisions/categories/006_independence_wave_crisis_categories.txt`, `common/decisions/006_independence_wave_crisis_decisions.txt`, and `events/006_independence_wave.txt` (`chaosx.nr6.3`). The event-chain inspection was read-only; its partial report is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9cef3e69c750ae2eb81fc8fdddf6b516b9ed9282560a6fbcc1fb6ba33b02992f/eb017b468b2d9c0fd73f855e573d189e4b325ae3b438718ac0aa5f2f07160e2a/event-scan-b475d0375104.json`.

## Architecture result

The bounded shape is sound: the trigger is country-scoped, the 35% stability and resistance-over-50 thresholds are centralized, the action is a 120-day selectable mission with a 365-day country cooldown, and no broad `on_daily` or `on_monthly` loop was introduced. The timeout queues the existing Event 006 root transaction rather than adding a second release algorithm. `chaosx.nr6.3` consumes the queue, retries a busy coordinator for fourteen one-day attempts, and delegates to `independence_wave_prepare_and_execute_standalone_incident`, preserving the existing host-survival, protected-remnant, anchor, reservation, exact-count, rollback, and synchronized-commit gates. Failure applies the configured stability/war-support/resistance consequence and does not directly mutate ownership. The live allocator audit passes with the current 6/8/10/14/20 ladder and World Collapse 20.

## Findings requiring parent disposition

1. **Cost trigger gap (repair recommended).** `can_pay_independence_wave_crisis_cost` delegates to `can_pay_independence_wave_security_standard_cost`, which checks manpower, Army Experience, infantry equipment, and support equipment but not Command Power. `independence_wave_pay_crisis_cost` subtracts the standard Command Power amount and the localisation promises that cost. Add the Command Power threshold to a crisis-specific cost trigger or explicitly remove that charge from the effect/text.

2. **Coordinator presentation race (repair recommended).** The first branch of `chaosx.nr6.3` checks the global queue, requester flag, and `can_liberation_release_reset_plan`, then starts a standalone plan. The reset trigger permits the `committed` phase, so a queued crisis can start another plan while `independence_wave_joint_presentation_pending` or `soviet_collapse_joint_opening_presentation_pending` is still delivering a previous joint incident. Mirror the existing scenario/collision transaction barrier in the crisis consumer and retry while either presentation flag is set. Also gate terminal `world_end` explicitly if the coordinator contract does not do so elsewhere.

3. **Requester disappearance can strand the global queue (runtime risk).** The delayed `country_event` is owned by the requester country, while the queue is a global flag. If the requester ceases to exist before `chaosx.nr6.3` runs, the event can remain on the non-existing country's backlog and leave `independence_wave_crisis_release_queued` set, blocking every later crisis. A bounded callback/target cleanup or another stable consumer is needed; do not solve this with a broad world-iterating on action.

4. **Pressure semantics need an explicit design check.** `has_independence_wave_crisis_occupation_pressure` tests `any_controlled_state` that is *not* owned by ROOT and has resistance above 50. This is severe resistance in a foreign state controlled by the crisis country, matching the current localisation and docs. It is not an owned host state occupied by an enemy. If “badly occupied” means the latter, the trigger is inverted and this path cannot release that anchor under the existing owner-and-controller safeguards.

5. **Wave cardinality is intentionally ordinary, not host-targeted.** The crisis queues the regular 6/8/10/14/20 Event 006 target and does not force a release from the triggering host. The existing allocator can fail closed when the attested pool cannot satisfy the current exact count, producing the blocked consequence. This matches the requested queued-ordinary-allocator architecture, but it does not provide a guaranteed one- or two-country host-specific release; retain that distinction in player-facing docs.

6. **Category visibility is a minor UI consideration.** The category is visible only while `can_independence_wave_open_crisis` is true. The selectable mission correctly uses `activation` rather than a mission `visible` trigger, but `independence_wave_pay_crisis_cost` sets `independence_wave_crisis_active`, which makes the category condition false while the 120-day mission is running. Confirm that the active mission remains discoverable in the intended decision surface; if not, expose the category while the mission is active without weakening activation/availability gates.

## Validation

`python -B .tools/audit_event6_allocator.py` passed: 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked packages, 11 attested packages across 10 compatible reservation groups, Event 005-first ordering, and the 6/8/10/14/20 automatic ladder with World Collapse 20. The offline Paradox wiki and vanilla `effects_documentation.md`, `triggers_documentation.md`, and decision documentation were consulted. No gameplay files were edited during this audit.

## Disposition

**Architecture: PARTIAL / needs parent repair for the cost-trigger gap and presentation-race guard.** The bounded mission/queue design and ordinary allocator reuse are otherwise acceptable. The requester-disappearance cleanup and pressure-semantics points remain explicit follow-up risks rather than hidden assumptions.
