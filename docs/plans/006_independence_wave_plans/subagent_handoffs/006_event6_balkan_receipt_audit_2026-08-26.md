# Event 006 Balkan founding-mission receipt audit

Date: 2026-08-26.

Status: Bounded source audit complete; eight local guards applied; no live-game or save/load completion claim.

## Scope and result

This audit covers the Banat, Bosnia, Epirus, Macedonia, Montenegro, Thrace, Transylvania, and Kosovo founding missions in `common\decisions\006_independence_wave_balkan_decisions.txt`.

The activation receipt and setup-effect lifecycle were already present for all eight packages.

All eight founding `cancel_trigger` blocks were missing the matching setup-receipt absence predicate, so each could leave a stale mission active while its setup receipt was absent during a rebuild or failed preparation.

The owned decision file now adds exactly one `NOT = { has_country_flag = <package>_setup_complete }` clause to each existing cancellation `OR` block.

No costs, AI weights, admission checks, route checks, project effects, or balance values were changed.

## Severity-ordered issue list

1. High, fixed: the eight founding missions checked package identity, stable ledgers or compact state, and capital control, but did not cancel when their own setup-complete receipt was absent.

2. Informational, unresolved outside this bounded patch: each ordinary decision category contains the founding mission plus roughly ten or eleven project decisions, and this source-only audit does not prove how many are simultaneously visible after their existing gates evaluate.

3. Informational, unresolved outside this bounded patch: receipt loss is an internal lifecycle state and has no new player-facing cancellation explanation; no localisation change was authorized for this guard-only repair.

## Contract matrix

| Package and owner | Category / founding mission | Activation receipt line | New cancel guard line | Setup effect clear / prepared restore | Complete wrapper receipt |
|---|---|---:|---:|---|---|
| Banat / AXX | `independence_wave_axx_banat_council_category` / `independence_wave_axx_hold_banat_council_together` | decision line 26 | decision line 35 | `common\scripted_effects\006_independence_wave_balkan_package_effects.txt` lines 321, 323, 374-375 | `common\scripted_triggers\006_independence_wave_balkan_package_triggers.txt` lines 186-189 |
| Bosnia / BOS | `independence_wave_bos_drina_council_category` / `independence_wave_bos_hold_drina_council_together` | decision line 241 | decision line 250 | `common\scripted_effects\006_independence_wave_balkan_package_effects.txt` lines 780, 782, 837-838 | `common\scripted_triggers\006_independence_wave_balkan_package_triggers.txt` lines 381-384 |
| Epirus / BBX | `independence_wave_bbx_epirus_council_category` / `independence_wave_bbx_hold_epirus_council_together` | decision line 487 | decision line 496 | `common\scripted_effects\006_independence_wave_balkan_package_effects.txt` lines 1242, 1244, 1295-1296 | `common\scripted_triggers\006_independence_wave_balkan_package_triggers.txt` lines 577-580 |
| Macedonia / MAC | `independence_wave_mac_vardar_council_category` / `independence_wave_mac_hold_vardar_council_together` | decision line 719 | decision line 728 | `common\scripted_effects\006_independence_wave_balkan_package_effects.txt` lines 1701, 1703, 1748-1749 | `common\scripted_triggers\006_independence_wave_balkan_package_triggers.txt` lines 769-772 |
| Montenegro / MNT | `independence_wave_mnt_mountain_compact_category` / `independence_wave_mnt_hold_mountain_compact_together` | decision line 1162 | decision line 1171 | `common\scripted_effects\006_independence_wave_balkan_package_effects.txt` lines 2153, 2155, 2188-2189 | `common\scripted_triggers\006_independence_wave_balkan_package_triggers.txt` lines 981-984 |
| Thrace / BAX | `independence_wave_bax_thrace_council_category` / `independence_wave_bax_hold_thrace_council_together` | decision line 944 | decision line 953 | `common\scripted_effects\006_independence_wave_balkan_package_effects.txt` lines 2588, 2590, 2641-2642 | `common\scripted_triggers\006_independence_wave_balkan_package_triggers.txt` lines 1177-1180 |
| Transylvania / TRA | `independence_wave_tra_danube_council_category` / `independence_wave_tra_hold_border_council_together` | decision line 1418 | decision line 1427 | `common\scripted_effects\006_independence_wave_balkan_package_effects.txt` lines 2972, 2974, 3013-3014 | `common\scripted_triggers\006_independence_wave_balkan_package_triggers.txt` lines 1360-1363 |
| Kosovo / KOS | `independence_wave_kos_cantonal_compact_category` / `independence_wave_kos_hold_cantonal_compact_together` | decision line 1630 | decision line 1639 | `common\scripted_effects\006_independence_wave_kosovo_package_effects.txt` lines 263, 265, 298-299 | `common\scripted_triggers\006_independence_wave_kosovo_package_triggers.txt` lines 180-183 |

Every activation receipt is the same flag tested by its setup effect and its complete wrapper.

Every setup effect clears that receipt before the package initialization/rebuild path and restores it only inside `has_prepared_<receipt>_package_setup = yes`.

Every new cancellation clause is inside the existing `OR` and leaves the package-loss, stable-state, route, and capital-control predicates unchanged.

## Before and after behavior

Before this patch, a setup retry cleared the package receipt, but the founding mission's cancellation block did not test that receipt, so an already active mission could survive until another cancellation condition fired.

After this patch, the daily mission cancellation check has a fail-closed receipt branch for every package, while the mission remains eligible for activation only when the receipt exists and its existing resolved/failed flags are absent.

The existing stable-state cancellation still marks success, and the existing timeout, package-loss, and capital-loss paths still apply the package failure effect.

## Decision-category lifecycle notes

The eight categories are ordinary decision categories with one timed founding mission and package-specific project decisions.

The founding missions use `available = { always = no }` and are activated by scripted setup, so the receipt-bearing `activation` block is the lifecycle gate rather than a player-click requirement.

The setup effects remain idempotent at source level: they clear the package receipt before rebuilding and publish the receipt only after the prepared-package predicate succeeds.

The new cancellation guards close the stale-active-mission gap during receipt absence without adding a second mission, a new flag, or a new cleanup path.

## Cognitive-load notes

- Visible actions: the source categories expose the founding mission plus about ten or eleven project IDs per package, with existing `visible` and `available` gates; this task did not redesign category density or claim a live simultaneous-visible count.
- Active missions: the audited surface has one founding mission per package; project serialization and any shared active-project cap remain unchanged and were not part of this receipt repair.
- Player-facing values: the founding mission blocks contain no new numeric ledger display; package ledgers, thresholds, and route values remain in the existing category/project surfaces.
- Text density: no category, mission, project, or localisation prose was changed; no new wall of text was introduced.
- Value significance: setup receipts are internal lifecycle flags, not player-facing values; their significance is now enforced by activation and cancellation rather than exposed as a raw number.
- Remaining UX uncertainty: the installed MCP event renderer does not establish ordinary decision-category wrapping or simultaneous project visibility, so a separate GUI/category review would be needed for that question.

## Mission quality notes

| Mission | Regional surface | Duration constant | Success condition | Failure condition / duplicate risk |
|---|---|---|---|---|
| AXX Banat Council | Banat / Balkans-Danube | `independence_wave_banat_duration.founding_crisis` = 420 days | Stable Banat ledgers through existing `has_stable_independence_wave_axx_ledgers` cancellation path | Timeout, package loss, or capital-control loss apply existing failure; receipt guard plus resolved/failed flags prevent stale/repeated activation |
| BOS Drina Council | Drina / Balkans-Danube | `independence_wave_bosnia_duration.founding_crisis` = 420 days | Stable Bosnia ledgers through existing `has_stable_independence_wave_bos_ledgers` path | Timeout, package loss, or capital-control loss apply existing failure; receipt guard plus terminal flags prevent stale/repeated activation |
| BBX Epirus Council | Epirus / Balkans-Danube | `independence_wave_epirus_duration.founding_crisis` = 330 days | Stable Epirus ledgers and the existing government-route requirement | Timeout, package loss, or capital-control loss apply existing failure; receipt guard closes setup-retry duplication risk |
| MAC Vardar Council | Vardar / Balkans-Danube | `independence_wave_macedonia_duration.founding_crisis` = 420 days | Stable Macedonia ledgers through existing `has_stable_independence_wave_mac_ledgers` path | Timeout, package loss, or capital-control loss apply existing failure; receipt guard plus terminal flags prevent stale/repeated activation |
| MNT Mountain Compact | Montenegro mountains / Balkans-Danube | `independence_wave_montenegro_duration.founding_crisis` = 540 days | Stable Montenegro compact through existing `has_stable_independence_wave_mnt_compact` path | Timeout, package loss, or capital-control loss apply existing failure; receipt guard closes setup-retry duplication risk |
| BAX Thrace Council | Thrace / Balkans-Danube | `independence_wave_thrace_duration.founding_crisis` = 360 days | Stable Thrace ledgers through existing `has_stable_independence_wave_bax_ledgers` path | Timeout, package loss, or capital-control loss apply existing failure; receipt guard plus terminal flags prevent stale/repeated activation |
| TRA Danube Council | Transylvania / Danube border | `independence_wave_transylvania_duration.founding_crisis` = 420 days | Stable settlement through existing `has_stable_independence_wave_tra_settlement` path | Timeout, package loss, or capital-control loss apply existing failure; receipt guard closes setup-retry duplication risk |
| KOS Cantonal Compact | Kosovo cantons / Balkans-Danube | `independence_wave_kosovo_duration.founding_crisis` = 570 days | Stable Kosovo compact and the existing government-route requirement | Timeout, package loss, or capital-control loss apply existing failure; receipt guard closes setup-retry duplication risk |

The package owner is the carrier tag shown in the table, and each mission's category, package predicate, capital scope, duration constant, success predicate, and failure effect remain package-specific.

## Cost and requirement clarity

The eight changed founding mission blocks have no `custom_cost_trigger` or spendable cost field, so their changed cost count is zero and texticon coverage is not applicable.

The category project cost rows were not modified, and no literal resource name or fifth cost was introduced by this patch.

The receipt is a non-consumed setup requirement, not a spendable cost; it remains separated from the existing project costs and route requirements.

## AI validity and route-lock notes

All eight founding missions retain `ai_will_do = { base = constant:independence_wave_decision_ai.urgent }`; no AI weight or target was edited.

Existing Epirus and Kosovo stable-success route-government conditions remain intact, as do each package's package predicate and capital-control cancellation checks.

The probability route was used for discovery with `mission_ai_will_do` against `common\decisions\006_independence_wave_balkan_decisions.txt`.

The probability artifact reports `PROBABILITY_SOURCE_INSPECTED`, 86 candidates, zero unresolved constructs, and zero currently available candidates for the selected adapter.

No probability compare was run because this patch changes no weighted surface, so the mandatory before/after balance comparison contract was not triggered.

## Localisation and tooltip gaps

No localisation IDs, mission names, descriptions, effect tooltips, icons, or texticons changed.

The new receipt predicates are internal trigger logic and do not create a separate player-facing blocked-reason string.

The existing mission and project localisation remains the source of player-facing lifecycle context; a future UX pass may decide whether receipt-loss cancellation needs a custom explanation, but that is outside this one-line guard scope.

## Cleanup and exploit-risk notes

The new guards cause a founding mission to cancel when its own setup receipt is absent, reducing the chance that a pre-rebuild mission survives into an unprepared package state.

Existing cancel and timeout effects still set the package-specific resolved or failed flags and apply the existing project-failure effect; no cleanup hook was changed.

No free-unit loop, equipment loop, war-goal spam, core spam, cooldown bypass, or cost exploit was introduced by the eight trigger-only additions.

## Validation and evidence

Focused source assertions passed for all eight missions, confirming activation receipt, matching cancel guard, setup clear-before-prepared ordering, restore inside the prepared-success block, and complete-wrapper receipt.

The following Event 006 static validators all exited 0: `python -B .tools/audit_event6_allocator.py`, `python -B .tools/audit_event6_country_api.py`, `python -B .tools/audit_event6_flags.py --strict`, `python -B .tools/audit_event6_form16.py`, `python -B .tools/audit_event6_gui_matrix.py`, and `python -B .tools/audit_event6_scenario_matrix.py`.

The allocator, country API, strict flag, FORM-16, Statehood Ledger semantic matrix, and SCN-008 scenario matrix validators reported their existing passing summaries.

Post-change Event MCP lint returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics at revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9` and graph hash `4b0d98848c436e8f6c8363056e3ae62cfad7785e4b2f1396ac9f1439f91de8df`.

Event lint artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7d0942708485a6ab32c4eb5450d41efa820af03407cd8fb1a6fdd163f0216c98/c76dae46d429e917516dfc3ae8b012cb35d286393e854f34677dc06b8ac5b6c5/event-lint-744cd12bca3e.json`.

Post-change Event MCP options render returned `EVENT_RENDERED_PARTIAL` with zero blockers and the same graph revision.

Event render manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/767514063ed7d3413bde1e6c7eba788f66417c1f1bc38fc30718131618139266/2f82baed9b9ee877c89f83e1472c642296f10c5be62f14b5b8776866d95bfe1c/event-options-744cd12bca3e-manifest.json`.

Event render JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/215827c721443e89339f437d0095f57190131cc3b77d85f04cf591ffb9bc287a/071370ef50297e911a872e8a643a071433dd86f4ac05efe06861b76d83e31a5a/event-options-744cd12bca3e.json`.

The MCP partial status reflects its known large-workspace deferral of helper projections and lifecycle passes, not a blocking diagnostic; one initial render request exceeded the server's 240-node limit and was retried successfully at the supported limit.

Probability artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/186e77fa39cfdd6f687262cb57a38f9df62bdc7c030976cbafc8f6150a233fec/2afac5805ef03a6cf2c1ef72d8e7a0f6cd4f4c5572cc2341e86048f8710459e6/probability-inspect-674c8d80374b.json`.

## References consulted

Required repository guidance was read from `AGENTS.md`, `.agents\skills\chaos-redux-decisions-missions\SKILL.md`, `.agents\skills\chaos-redux-events\SKILL.md`, and `.agents\skills\chaos-redux-subagents\SKILL.md`.

The required offline Paradox wiki pages were read for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, and the related GUI pages.

Relevant vanilla documentation was read from the installed Hearts of Iron IV documentation for effects, triggers, script concepts, localisation formatting, and localisation objects.

The current Event 006 specifications, source-of-truth map, package manifest, decision/mission matrix, package notes, and prior receipt-guard handoffs were consulted before editing.

## Skipped meaningful validation and remaining risks

No live Hearts of Iron IV run, save/load cycle, or in-game cancellation timing claim is made, per the repository boundary for agents.

No `hoi4.gui_inspect`, `hoi4.gui_render`, or `hoi4.gui_rewrite` call was required because this patch changes no decision-owned GUI surface.

No decision-specific or mission-specific MCP inspector is exposed by the installed server; Event MCP lint/render and the probability source-discovery route were used instead.

The Event MCP report remains partial for its large-workspace helper/lifecycle projection, although it has zero blocking diagnostics.

The ordinary category's simultaneous project visibility, in-game tooltip wrapping, and save/load behavior remain for parent/live review.

No separate broad plan was written; this file is the unique bounded handoff requested for the receipt audit.

## Changed files and ownership

Gameplay change: `common\decisions\006_independence_wave_balkan_decisions.txt`, exactly eight added cancellation guards for the eight mission IDs in the contract matrix.

Documentation handoff: `docs\plans\006_independence_wave_plans\subagent_handoffs\006_event6_balkan_receipt_audit_2026-08-26.md`.

The gameplay file was not staged or committed by this subagent.
