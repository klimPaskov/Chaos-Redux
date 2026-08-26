# Event 006 frontier founding-mission setup-receipt audit

Date: 2026-08-26

Status: source-applied, bounded lifecycle repair; no files were staged or committed and whole Event 006 remains HOLD / PARTIAL.

## Scope and references

The gameplay scope was limited to the Kurdistan and Kuban founding missions in `common/decisions/006_independence_wave_frontier_decisions.txt` and this unique handoff file.

I read `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, the Event 006 decision/mission prompt, Parts 3 and 5 of the Event 006 specification, the current Event 006 resume packet, and the analogous IW-040, IW-045, and IW-007 receipt-guard handoffs.

I consulted all required offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding.

I consulted the vanilla decision documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/_documentation.md` and the relevant `effects_documentation.md` and `triggers_documentation.md` sections for `activation`, `cancel_trigger`, `activate_mission`, `remove_mission`, `has_country_flag`, and `has_active_mission`.

No decision-owned GUI surface was introduced or changed, so `hoi4.gui_inspect` and `hoi4.gui_render` were not applicable to this bounded lifecycle patch.

## Severity-sorted findings

### P1 — confirmed Kurdistan receipt-cancellation omission, fixed

`independence_wave_kur_hold_mountain_council` activation required `independence_wave_iw_060_setup_complete` at `common/decisions/006_independence_wave_frontier_decisions.txt:17-22`, but its `cancel_trigger` lacked the matching absence guard at the pre-patch `:25-36` block.

`independence_wave_setup_iw_060_kurdistan` clears that receipt before rebuilding at `common/scripted_effects/006_independence_wave_kurdistan_package_effects.txt:355-360` and restores it only inside the prepared-setup branch at `:420-424`; without the guard, an active founding mission could survive a failed or retried setup generation.

The patch adds `NOT = { has_country_flag = independence_wave_iw_060_setup_complete }` at `common/decisions/006_independence_wave_frontier_decisions.txt:28`.

### P2 — Kuban contract confirmed, preserved

`independence_wave_kub_hold_mounted_compact_together` already requires `independence_wave_iw_040_setup_complete` in activation at `common/decisions/006_independence_wave_frontier_decisions.txt:622-627` and already cancels when that receipt is absent at `:630-641`, specifically line `:633`.

`independence_wave_setup_iw_040_kuban` clears the receipt at `common/scripted_effects/006_independence_wave_kuban_package_effects.txt:360-365` and restores it only within `has_prepared_independence_wave_iw_040_package_setup = yes` at `:423-428`.

No Kuban decision change was needed.

### P3 — no further defect confirmed in this bounded contract

The package-local project-ready triggers also require the same setup receipts (`common/scripted_triggers/006_independence_wave_kurdistan_package_triggers.txt:55-60` and `common/scripted_triggers/006_independence_wave_kuban_package_triggers.txt:15-19`), while each package completion predicate requires its shared and package setup flags.

## Decision-category lifecycle notes

| Package | Category | Founding mission | Activation receipt | Setup clear / prepared restore | Receipt cancellation | Cleanup |
| --- | --- | --- | --- | --- | --- | --- |
| IW-060 KUR | `independence_wave_kurdistan_mountain_compact_category` | `independence_wave_kur_hold_mountain_council` | `independence_wave_iw_060_setup_complete` at `common/decisions/006_independence_wave_frontier_decisions.txt:19` | Clear `:357`; restore only under prepared proof `common/scripted_effects/006_independence_wave_kurdistan_package_effects.txt:420-421` | Added matching `NOT` guard at `common/decisions/006_independence_wave_frontier_decisions.txt:28` | `remove_mission` in `independence_wave_cleanup_iw_060_kurdistan` at `common/scripted_effects/006_independence_wave_kurdistan_package_effects.txt:440-444`; cleanup clears the receipt at `:467` |
| IW-040 KUB | `independence_wave_kub_mounted_compact_category` | `independence_wave_kub_hold_mounted_compact_together` | `independence_wave_iw_040_setup_complete` at `common/decisions/006_independence_wave_frontier_decisions.txt:624` | Clear `:362`; restore only under prepared proof `common/scripted_effects/006_independence_wave_kuban_package_effects.txt:424-425` | Existing matching `NOT` guard at `common/decisions/006_independence_wave_frontier_decisions.txt:633` | `remove_mission` in `independence_wave_cleanup_iw_040_kuban` at `common/scripted_effects/006_independence_wave_kuban_package_effects.txt:444-448`; cleanup clears the receipt at `:496` |

The founding missions are non-selectable, `available = { always = no }`, and use package-specific founding-crisis timeout constants. The existing package cancellation effects remain unchanged.

## Cognitive-load notes

This bounded audit adds no visible action, active mission, player-facing value, text, or category control.

Each audited category has one package-owned founding mission plus its existing project decisions; the patch does not add another action or another exposed value.

The founding mission presents the existing package crisis state and timeout, while the setup receipt is an internal lifecycle witness rather than a new player-facing number. Its significance is binary: the current generation exists or the mission is cancelled.

A full category-density, tooltip, and GUI visual audit is outside this receipt-only scope; no new cognitive-load issue was introduced by the one-line guard.

## Mission quality notes

| Mission | Owner / category | Region | Requirement | Duration | Success | Failure / cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `independence_wave_kur_hold_mountain_council` | IW-060 KUR / `independence_wave_kurdistan_mountain_compact_category` | Caucasus, Anatolia, and Mesopotamia package | KUR package, setup receipt, unresolved crisis flags; non-selectable mission waits on the existing compact conditions | `constant:independence_wave_kurdistan_duration.founding_crisis` | Existing cancellation branch marks `independence_wave_kur_compact_crisis_resolved` after stable compact, route government, capital, and state 421 control | Existing package failure branch and timeout call `independence_wave_kur_apply_project_failure`; receipt loss now also cancels through that existing path | None found; one founding mission for the KUR category and one cleanup removal |
| `independence_wave_kub_hold_mounted_compact_together` | IW-040 KUB / `independence_wave_kub_mounted_compact_category` | Eastern Europe and western former imperial Russia package | KUB package, setup receipt, unresolved crisis flags; non-selectable mission waits on the existing compact conditions | `constant:independence_wave_kuban_duration.founding_crisis` | Existing cancellation branch marks `independence_wave_kub_compact_crisis_resolved` after stable compact, route government, capital, and state 234 control | Existing package failure branch and timeout call `independence_wave_kub_apply_project_failure`; existing receipt-loss guard cancels through that path | None found; one founding mission for the KUB category and one cleanup removal |

The package failure helpers are already idempotent behind `independence_wave_kur_project_failure_applied` at `common/scripted_effects/006_independence_wave_kurdistan_package_effects.txt:105-117` and `independence_wave_kub_project_failure_applied` at `common/scripted_effects/006_independence_wave_kuban_package_effects.txt:109-121`.

## Cost and requirement clarity

The two founding missions have no `cost`, `custom_cost_trigger`, or spendable payment block, so each has a zero-cost-type audit and requires no cost texticon.

Their package, setup-receipt, capital-control, state-control, compact, and route checks are requirements or lifecycle conditions, not consumed costs.

The underlying KUR and KUB project decisions retain their existing cost tiers and icon-first localisation; this patch does not alter any cost, requirement, or payment effect.

## AI validity and route-lock notes

Both founding missions retain their existing urgent AI score constants, and no AI weight or route score changed.

The KUR and KUB package triggers retain exact package identity, anchor-state, former-host, force, route, and setup-completion gates. The new KUR guard only removes a mission when the generation receipt is absent; it does not widen package admission or route availability.

The direct MCP mission-weight inspection was read-only and returned `PROBABILITY_SOURCE_INSPECTED` with complete source-relative pools but zero available candidates because no typed campaign fixture satisfied the package gates. KUR artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6a010ef40f26c7d8731392098b922391523fbfc74784fb82fcbaad99de4e4d4a/75a24c918d1d5c8dc7fcae8b5b396d259ebff78acd358b7fd4c1263c0648bbb6/probability-inspect-3d5307da33c2.json` (12 candidates, 0 available, 16 required inputs, 0 unresolved inspect items).

KUB artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d52029c63a745739f954094f12583240c8dbb57d1161ee04a235769cc61575fa/2b6fb5b87fe0cd2e9c3c284e7d0328421851a8f403b038fdee465e97c86e3638/probability-inspect-3d5307da33c2.json` (11 candidates, 0 available, 14 required inputs, 0 unresolved inspect items).

No callable `chaosx_ai_probability_auditor` subagent route was exposed in this runtime. The direct MCP receipts are recorded as source-discovery evidence only and do not establish live mission selection probabilities or balance.

## Localisation and tooltip gaps

No localisation key changed or was added. Existing mission name, description, timeout, effect, and failure localisation remain in the frontier localisation registry.

No new player-facing receipt text was needed because setup-receipt loss is an internal cancellation condition and the existing cancellation/failure effects already explain the visible outcome.

A full localisation audit is not claimed.

## Cleanup and exploit-risk notes

Before the patch, a stale KUR founding mission could survive a setup reset or failed retry because activation and cancellation did not share the same receipt witness.

After the patch, KUR setup-receipt loss cancels the mission and invokes the existing package failure path; KUB already behaved this way.

Both package cleanup dispatches explicitly remove the founding mission and clear the setup receipt. The idempotent project-failure flags prevent repeated cancellation penalties from this path.

No reward loop, cost loop, cooldown, target, admission, route, or balance change was made.

## Changed files and identifiers

- `common/decisions/006_independence_wave_frontier_decisions.txt:28` — added `NOT = { has_country_flag = independence_wave_iw_060_setup_complete }` to `independence_wave_kur_hold_mountain_council.cancel_trigger`.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_frontier_receipt_audit_2026-08-26.md` — this handoff.

Changed gameplay identifier: `independence_wave_kur_hold_mountain_council.cancel_trigger`.

Confirmed unchanged identifier: `independence_wave_kub_hold_mounted_compact_together.cancel_trigger` already contains the matching IW-040 receipt guard.

## Before and after behavior

Before: KUR activation required the IW-060 setup receipt, but an active founding mission did not cancel when that receipt disappeared during setup reset or failed retry.

After: KUR activation and cancellation are symmetric; missing IW-060 setup receipt cancels the founding mission through its existing cancellation/failure handling.

KUB behavior is unchanged and already satisfies the same contract.

## Validation

- Focused source assertions passed for KUR and KUB activation receipts, matching cancellation guards, setup clear → prepared-proof → restore ordering, and exactly one setup writer per package receipt.
- `python -B .tools/audit_event6_allocator.py` passed with 149 publishers, 40 adapters, 32 attested packages, and the unchanged 3/4/5/7/10 ladder.
- `python -B .tools/audit_event6_country_api.py` passed with 242 broad rows, 191 unique carriers, zero missing, zero duplicates, and IW-031 crosswalk pass.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 registered and 102 complete flag families.
- `python -B .tools/audit_event6_form16.py` passed.
- `python -B .tools/audit_event6_gui_matrix.py` passed.
- `python -B .tools/audit_event6_scenario_matrix.py` passed for all 32 SCN-008 cells and eight edge cases.
- Post-change `hoi4.probability_inspect` completed read-only for the complete KUR and KUB mission candidate pools with no source diagnostics; both pools remained unavailable under empty fixtures, so no quantitative AI claim is made.

## Skipped meaningful validation

No probability evaluate, sweep, simulate, or before/after compare was run because this one-line patch changes no AI weight, modifier, timing, or candidate score, and the adapter reported zero available candidates without typed campaign fixtures.

No live game, save/load, runtime parser, or in-game mission-cancellation validation is claimed.

No `hoi4.gui_inspect`/`hoi4.gui_render` call was made because no GUI surface was in scope.

## Remaining risks and boundaries

Other project decisions in the two large package categories were not broadened or reworked; this handoff covers only the founding-mission setup-receipt contract requested by the parent.

The MCP mission adapter remains fixture-limited, and the unavailable `chaosx_ai_probability_auditor` route prevents a delegated typed probability audit; no balance conclusion is inferred.

The whole Event 006 implementation remains HOLD / PARTIAL, and live save/load evidence remains user-owned.
