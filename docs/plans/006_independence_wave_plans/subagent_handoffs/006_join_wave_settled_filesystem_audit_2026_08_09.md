# Event 006 Join the Independence Wave — settled-filesystem audit

Status: patched and re-audited on 2026-08-10, including the post-fix cleanup-order and baseline-safety pass. No commit or staging performed. This handoff covers only the Event 006 Join-the-Independence-Wave conversion path and its narrow shared zero-host branches.

## Superseding IW-040 promotion override (2026-08-12)

IW-040 Kuban was content-attested and inserted immediately after IW-038 and before IW-033 in the deterministic probe. The pre-IW-044 parity in this handoff was 30 Join candidates, 30 content-attestation IDs, and 30 reservation wrappers across the 30/27/163/38 authority. The 2026-08-13 IW-044 promotion supersedes that count with 31 Join candidates, 31 content-attestation IDs, and 31 reservation wrappers across the 31/28/162/39 authority; IW-044 is immediately after IW-040 and before IW-033. The 28-ID counts and order in the dated body below remain historical evidence for the pre-IW-040 source.

## Superseding IW-045 promotion override (2026-08-14)

IW-045 Bashkiria is now content-attested and inserted immediately after IW-044 and before IW-033 in the deterministic probe. The current source therefore has 32 Join candidates, 32 content-attestation IDs, and 32 matching reservation wrappers across the 32/29/161/40 authority. The 31-ID count in the preceding override and all older counts in the dated body remain historical evidence for the pre-IW-045 source.

## Scope and source of truth

The audit covered `common/scripted_effects/006_independence_wave_join_effects.txt`, `common/scripted_triggers/006_independence_wave_join_triggers.txt`, `common/on_actions/006_independence_wave_join_on_actions.txt`, `events/006_independence_wave_join.txt`, `localisation/english/006_independence_wave_join_l_english.yml`, `docs/events/006_independence_wave/join_wave.md`, and the shared branches in `common/scripted_effects/006_independence_wave_package_planner_effects.txt`, `common/scripted_effects/chaosx_liberation_release_effects.txt`, and `common/scripted_triggers/chaosx_liberation_release_triggers.txt`.

The required Chaos Redux skills were read: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`. The required offline Paradox wiki pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Vanilla documentation was checked for event timeout/default-option behavior, event targets, scoped on_actions, variables, `change_tag_from`, release effects, and script constants.

## Issues found and fixes

### Medium — stale hidden report could clear another plan's global join context

Before this audit, `independence_wave_join_clear_runtime` and the surrounding `clr_global_flag = independence_wave_join_conversion_active` calls were unconditional. A delayed `.37` or `.38` could therefore clear `global.independence_wave_join_active_plan_id`, `global.independence_wave_join_offer_source`, or the conversion flag after a newer coordinator ledger had replaced the old one.

Patched in `common/scripted_triggers/006_independence_wave_join_triggers.txt` and `common/scripted_effects/006_independence_wave_join_effects.txt`:

- Added `is_independence_wave_join_plan_ledger_owned` to require local/global plan-ID equality plus Event 006 ownership and the current source country.
- Added `is_independence_wave_join_plan_identity_owned` for the stronger active-conversion/active-plan guard used by current-plan validation and open-plan failure handling.
- Captured `independence_wave_join_plan_id` immediately after allocation begins, before any package probe, so no-package cleanup has an identity to prove.
- Made `independence_wave_join_clear_runtime` clear global conversion, offer-source, and active-plan markers only when the ledger and any active-plan marker both still belong to the local source.
- Removed the duplicate unconditional conversion-flag clears from offer failure, accept success/failure, stale accept, and decline paths.
- Stale hidden accept/decline paths now no-op while another plan is active or has a different ledger ID. If no competing ledger remains, they clean their local receipt and reset only their matching old plan.
- Added the missing selected-package source-ID revalidation to `is_independence_wave_join_current_plan`.

### Low — zero-host guard was dead code

`is_independence_wave_join_zero_host_conversion` and `independence_wave_join_zero_host_allowed` were set and cleared but not consumed by a shared validator. The guard is now meaningful without affecting allocation: `liberation_release_prepare_host_capitals_for_execution` requires both the active join context and the accepted source's `zero_host_allowed` flag before skipping ordinary capital relocation. Reservation and exact-footprint probing continue to use the broader plan-context guard so the complete source footprint can be tested before player consent.

### High - qualified source could miss its only contention callback

Before the completion-audit patch, a qualifying source was simply skipped when the shared Event 005/006 coordinator was valid or active. The scoped callback set now queues one hidden `chaosx.nr6.40` retry under `independence_wave_join_retry_pending`, with the seven-day interval centralized at `constant:independence_wave_join.retry_days`. The retry clears its queue key, refreshes the source baseline, and invokes the normal offer path only while the source remains eligible and threshold-qualified. If the coordinator is still busy, the helper requeues only when the flag is absent; if the coordinator is free, ordinary allocation proceeds. Offer, success, decline, failure, and ineligibility cleanup all clear the retry state, and no periodic/world scan was added.

### High - peaceful/non-core first loss could be underestimated

War-entry observation records the exact pre-loss owned-state baseline for both belligerents. The `on_state_control_changed` callback re-evaluates the old controller and current owner without adding a synthetic owned-state loss because the callback also fires for control-only changes. Core-state reconstruction in `independence_wave_join_update_peak_baseline` remains nested under `NOT has_variable = independence_wave_join_peak_owned_state_count`, making it the bounded last-resort first-observation fallback.

### High - decline/failure cleanup could reset before guarded Join cleanup

The matching decline path and the guarded open-plan failure path now clear the contribution, abort while the Join plan identity still exists, run the owner/equality-guarded `independence_wave_join_clear_runtime`, and only then reset the shared coordinator. The visible report's pending flag is part of the matching decline predicate, so cleanup remains reachable. This ordering prevents an abort/reset from deleting the ledger proof before the global Join markers are cleared and prevents an old report from touching a newer plan.

## Verified lifecycle and transaction contract

- Scoped callbacks only: `on_war_relation_added`, `on_state_control_changed`, `on_peaceconference_ended`, `on_capitulation_immediate`, `on_release_as_free`, and `on_release_as_puppet`. The Join path adds no daily, weekly, monthly, yearly, or game-start scan; contention is handled by one country-local `.40` retry flag/event.
- Source eligibility remains living, independent, at peace, non-Event-005/006 origin, non-Event-006 registry-owned, non-Event-012 Africa carrier, not pending/active, and not on cooldown.
- Baseline uses the largest observed owned-state count. War entry records both belligerents before losses, state-control changes re-evaluate affected countries without manufacturing ownership changes, and only an otherwise unobserved country uses the bounded core-state fallback. The offer requires at least two lost states and a 50% reduction, using centralized constants.
- Candidate order is deterministic and exactly matches the shared content-attestation trigger: 28 IDs — IW-001, 002, 004, 006, 007, 008, 009, 010, 012, 014, 017, 018, 019, 023, 024, 026, 027, 028, 029, 030, 031, 033, 041, 070, 071, 072, 173, and 184. Every ID has one `independence_wave_reserve_package_iw_*` wrapper.
- Each candidate is probed in the ordinary shared allocator with extended territory and viable force settings. The exact proof requires one selected row, a state-row delta equal to current `num_owned_states`, and no remaining unreserved owned state. Failed candidates roll back and reopen the contribution before the next trial.
- Acceptance revalidates the plan ID, active plan ID, Event 006 owner, source country, selected package, selected count, phase, and offer-source country. It locks and executes through the ordinary Event 006 package setup, generic focus assignment, force/package mechanics, final validation, origin/history, and commit pipeline. Human-only `change_tag_from = ROOT` remains the final post-commit effect.
- Decline and timeout retain the old government, clear the matching coordinator contribution, write history, and apply the centralized 90-day cooldown. Failure receipts remain `chaosx.nr6.39`; compensating rollback is used where safe, while finalization failure remains fail-closed.
- No decision, mission, scripted GUI, AI weight, random pool, or weighted target was introduced by this path. Therefore no decision category lifecycle, mission owner/category/region/duration/success/failure matrix, or probability comparison applies to the Join conversion itself.

## Localisation and UI review

`events/006_independence_wave_join.txt` defines `chaosx.nr6.36` (20-day report), hidden accept `.37`, hidden decline `.38`, failure receipt `.39`, and hidden contention retry `.40`. The first visible option is decline, so vanilla timeout behavior defaults to retention/cooldown. The retry is hidden and has no player-facing localisation; existing title, description, options, tooltip, and history payload keys remain present in UTF-8 BOM `localisation/english/006_independence_wave_join_l_english.yml`. No dedicated scripted GUI is introduced.

## Validation evidence

### Static and source checks

- `python .tools/audit_event6_allocator.py` passed after the IW-031 promotion: 149 publishers, 28 attested packages, 25 compatible reservation groups, and all reported allocator witness/capacity checks.
- A focused parity script confirmed exact equality of the 28 Join candidate IDs, the 28 content-attestation IDs, and the available wrapper set; no candidate is missing or extra. IW-031 is probed immediately after IW-030, matching its numeric order.
- A focused Join source check confirmed the retry event `.40`, single-flight flag/guard, zero references to the removed synthetic state-loss capture, owner/equality-guarded cleanup before reset on matching decline/open-plan failure, and core fallback only under no prior peak. The scoped callback file contains no periodic callback token. Modified Clausewitz blocks have balanced braces (Join effects 297/297; triggers 35/35; on-actions 25/25; events 20/20).

### Mandatory HOI4 MCP event evidence

Fresh post-fix evidence was collected for `chaosx.nr6.36` and hidden `.40` in workspace `mod_chaos_redux_ea3b2d67c2c0`. The final focused lint/options revision is `53a767c5012bf86517e556e90f78047efea681342277a5d2813f07ffef0c5f15` (graph `cf99bd44a1d512f1e2dae932df4620b38cc19524bac01092fe94a54ca70231a9`).

- Lint/inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5723cecab4ab76dc0d4e3bcd201483c416d649a9b3acbd366347a603f55056b9/bb2be739b70c19f3b0af63ae71cf6ad3f283ef44cff269718323ea0a98ed6987/event-lint-53a767c5012b.json`
- Hidden retry trace: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6906ca23d094484dda6860214f6bab1258528957ab404f7b63f2941a39ef9bc/9fadda33fca5fdd3fa8b6429832452ff76365c19a8e7b4a797908a8a1aa0f5df/event-trace-53a767c5012b.json`
- Report options manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b8f72570846b186c0d607c6de3736b9b7e7faa7cf9b2216820c13ea46c08e597/cd6ba7367d155ec664b0abc405a27968a951a92f8ca1cf35b607002b2c7a2e78/event-options-53a767c5012b-manifest.json`
- Report options JSON/SVG/PNG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9e3105c464c218cf9b07371eb9c53bc87b30eb035ea2f8afa87cc4a93f021220/6de6ffe4313c4ffa1916bf0e08c7c017a919f0a4b7ab2d39bd6f7097a2273e40/event-options-53a767c5012b.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0e4b629b119f64280fc652a724fe8f1b00dd65d519570b1ffec55b0754120ffb/6c374f53d9201509b4f649fc681db4f892079da8d91054ca8f265d96b4dd7a77/event-options-53a767c5012b.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/32c4c3589e16fa5bfe61701ec4032413f3f0069fd627667e7ad29164d3271614/58e16106a3c659219fff436d27d9e89ccd25baac6294b27c3d7bab3a672ca454/event-options-53a767c5012b.png`.

The MCP route reported `EVENT_INSPECTED_PARTIAL`/`EVENT_RENDERED_PARTIAL` because workspace-wide helper projections were deferred. There were no blocking diagnostics; the partial result is not treated as a substitute for live gameplay validation. No Hearts of Iron IV executable was launched.

## Changed files and remaining work

Changed by this audit:

- `common/scripted_effects/006_independence_wave_join_effects.txt`
- `common/scripted_triggers/006_independence_wave_join_triggers.txt`
- `common/on_actions/006_independence_wave_join_on_actions.txt`
- `events/006_independence_wave_join.txt`
- `common/script_constants/006_independence_wave_constants.txt`
- `common/scripted_effects/chaosx_liberation_release_effects.txt` (one execution-time zero-host guard line; concurrent shared edits preserved)
- `docs/events/006_independence_wave/join_wave.md`
- this handoff

No player-facing localisation key was required for hidden `.40`; the existing Join localisation remains unchanged. No decision, mission, package-wrapper, focus, force, AI, or GUI source was otherwise changed. No unresolved in-scope ordering or baseline-safety defect remains after stale-plan hardening, scoped contention retry, guarded cleanup-before-reset ordering, and removal of the unverifiable synthetic state-loss increment. Remaining evidence limits are the MCP partial-helper projection and the required parent/user live validation; no simplification or unapproved fallback was introduced.
