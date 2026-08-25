# Event 016 Alien Infantry API Reconciliation Handoff

Date: 2026-08-26.

Owner: `chaosx_scripted_system_architect`.

Scope: reusable Alien Infantry contact, landing, Event 019 provider 508 transaction, D’Rhondan bootstrap, reservation/refund, stale target cleanup, and bounded-iteration audit against the accepted Alien Infantry/D’Rhonda addendum.

Status: API reconciliation is complete with two narrow fixes applied. One pre-existing D’Rhondan world-scan blocker remains intentionally unpatched because replacing it requires an accepted bounded registry or an explicit design exception.

## Executive result

The public API preserves independent numeric receipts for Kruger, Mengele, Event 019 provider 508, D’Rhondan sovereignty, and future consumers.

The reservation path debits exactly 2,000 `alien_laser_weapon_equipment_1`, holds the seven-day pending mission, and refunds exactly one reserve after clearing the pending flag first.

The Event 019 provider 508 path remains spawn-only and isolated from generic training, manpower, ordinary infantry equipment, and sustainment.

The deferred Event 019 commit now trusts the persistent `alien_infantry_event19_deferred_debit_committed` flag and no longer depends on a temporary result surviving a nested or delayed scripted-effect boundary.

The normal landing reservation now clears a selected state and orphaned reservation duration when availability or target validity fails between decision availability and completion.

The shared spawn result is now a country-scoped `alien_infantry_landing_spawn_succeeded` variable reset on every call, so the bounded D’Rhondan bootstrap callers can read it after the nested API effect returns.

No new ledger, native CBRN fallback, provider alias, global event target, broad on-action, or world-scan replacement was added.

## Required source and engine evidence

The required repository instructions and skills were read before the audit: `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-state-ledgers/SKILL.md`, `.agents/skills/chaos-redux-mtth/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The required offline wiki references were consulted for data structures and temporary-variable lifetime, event targets, scopes, triggers, effects, modifiers, localisation, on actions, event modding, decisions, ideas, AI, and state modding.

The temporary-variable rule that affected this audit is in `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:412-417`: a temporary variable defined inside a scripted effect is not guaranteed to remain available outside that scripted effect, while a temporary variable defined before the call is carried into it.

The required vanilla documentation was read from `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation`, including `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, and `common/script_constants/documentation.md`.

The engine references confirm that `save_event_target_as` is chain-local, global targets require explicit cleanup, `has_event_target` is the reader, `state_population_k` is state-local, and `add_manpower` is available in state and country scopes.

The accepted design and implementation references were read: `docs/specs/016_brilliant_scientist_specs/specs/016_alien_infantry_and_dhronda_addendum.md`, `docs/events/016_brilliant_scientist/systems/alien_infantry.md`, `docs/events/016_brilliant_scientist/systems/dhrondan_country.md`, `common/scripted_effects/016_alien_infantry_api_effects.txt`, `common/scripted_triggers/016_alien_infantry_api_triggers.txt`, `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`, `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`, `common/scripted_effects/016_dhrondan_contact_effects.txt`, `common/scripted_effects/016_dhrondan_country_effects.txt`, and the Event 019 generation and scenario transaction effects.

## Narrow patches applied

### Persistent Event 019 commit proof

`common/scripted_effects/016_alien_infantry_api_effects.txt:513-533` no longer gates `alien_infantry_commit_event19_landing` on `alien_infantry_landing_spawn_succeeded` as a temporary variable.

The commit gate requires the persistent deferred-mode flag, the persistent proven-debit flag, and the saved landing state.

The provider materializer and generic Event 019 transaction already set and retain those flags through the same-tag setup and delayed rollback paths.

This preserves exactly one cohort and exactly one proven 2,000-weapon debit while allowing commit after Event 019 ledger proof.

The API documentation now states that the persistent debit receipt is authoritative for commit and rollback.

### Failed reservation target cleanup

`common/scripted_effects/016_alien_infantry_api_effects.txt:220-242` now has a fail-closed branch for `alien_infantry_begin_landing_reservation`.

When the country-level eligibility or saved state target is no longer valid, the helper clears `dhrondan_landing_state_id` and `alien_infantry_landing_reservation_days` without debiting equipment or activating the mission.

This closes the availability-to-completion race without changing the accepted state selection or reservation design.

### Cross-script spawn result

`common/scripted_effects/016_alien_infantry_api_effects.txt:306-315,442` now writes `alien_infantry_landing_spawn_succeeded` as a regular country variable, reset to zero at the start of each spawn call and set to one only after the create-unit delta proves exactly one cohort.

The D’Rhondan bootstrap callers at `common/scripted_effects/016_dhrondan_country_effects.txt:408-449` retain their existing bounded loops and now read a result that is safe across the nested scripted-effect boundary.

The API and dynamic-effect documentation were updated to describe this result as country-scoped and per-call reset.

## Reusable helper map

| Helper | Scope | Inputs | Outputs | Side effects | Main call sites |
| --- | --- | --- | --- | --- | --- |
| `alien_infantry_grant_contact` | COUNTRY | Temporary `alien_infantry_contact_source_id` set to a source constant. | One selected receipt set to one; aggregate contact reconciled. | Ensures operational technology, locked template, counters, and contact flag. | Kruger/Mengele contact effects, DHR sovereignty bootstrap, Event 019 provider registration and derivative setup. |
| `alien_infantry_revoke_contact` | COUNTRY | Temporary `alien_infantry_contact_source_id` set to the owner’s source constant. | Only the selected receipt set to zero; reconciliation rerun. | Safe idempotent cleanup; never clears another receipt. | Event 019 runtime and derivative cleanup, project-force teardown. |
| `alien_infantry_reconcile_country` | COUNTRY | Existing source receipts, pending flag, reservation metadata, and state target. | Contact-active flag and initialized landing counters. | Rebuilds or relocks the shared template while contact remains, restores technology/production entitlement, cancels invalid pending reservations, and clears stale target metadata when no pending reservation remains. | Grant/revoke helpers, DHR start-revolt bridge, Kruger state carrier reconciliation. |
| `alien_infantry_begin_landing_reservation` | COUNTRY | Saved `dhrondan_landing_state_id`; valid contact, target, stockpile, cooldown, and world-end gates. | Pending flag and seven-day reservation duration on success. | Debits exactly 2,000 laser weapons once and activates the mission; failed entry clears target metadata without debit. | `common/decisions/016_alien_infantry_landing_decisions.txt:9-35`. |
| `alien_infantry_cancel_landing_reservation` | COUNTRY | Pending landing state. | Cleared pending flag, mission, duration, and state target. | Refunds exactly one 2,000-weapon reserve after clearing pending, so repeated cancellation cannot double refund. | Decision cancellation, mission cancellation, reconciliation, Event 019 pre-materialization refund callback. |
| `alien_infantry_spawn_landing_cohort` | COUNTRY | Contact, valid saved state, stockpile or prior pending reservation, optional DHR batch/initial inputs, optional Event 019 deferred inputs. | Country-scoped one-or-zero `alien_infantry_landing_spawn_succeeded`. | Creates exactly one locked cohort, debits or consumes exactly one reserve, marks state and history for ordinary mode, records deferred debit proof for Event 019, clears ordinary target, and refunds failed direct/pending materialization. | Landing mission timeout, DHR initial component/capital deployment, Event 019 provider 508 materializer. |
| `alien_infantry_commit_event19_landing` | COUNTRY on Event 019 generation country | Persistent deferred mode, persistent proven-debit flag, and saved state target. | Deferred state/history/telemetry/cooldown callback applied once. | Clears deferred transaction flags, deletion id, and state target after commit. | Event 019 provider callback and generic management/scenario commit points. |
| `alien_infantry_rollback_event19_landing` | COUNTRY on Event 019 generation country | Persistent deferred mode and proven-debit flag after Event 019 exact cohort deletion proof. | Cleared deferred transaction. | Refunds only the proven 2,000-weapon debit, then clears flags, deletion id, and state target. | Event 019 unit transaction rollback and same-tag retry rollback. |

## Constants and tuning table plan

The existing table remains the single tuning source in `common/script_constants/016_alien_infantry_api_constants.txt`.

Source IDs are `kruger_pact = 1`, `mengele_expedition = 2`, `event019_provider_508 = 3`, `dhrondan_sovereignty = 4`, and `future = 5`.

Landing values are zero, one, negative-one, reserve equipment 2,000, reservation duration seven days, default cooldown 30 days, network cooldown 24 days, guarded descent cooldown 18 days, near-space cooldown 12 days, presence gain one, strain gain five, arrival gain one, and history gain one.

Decision AI values are centralized as standard base 10 with the existing network, reserve-priority, guarded-descent, and near-space factors.

No constants were added, renamed, or duplicated by this reconciliation.

## Contact receipts and migration from duplicated logic

The API is the only source that writes the five `alien_infantry_contact_receipt_*` variables.

The call-site inventory found only valid source constants at `common/scripted_effects/016_dhrondan_contact_effects.txt:242,249`, `common/scripted_effects/016_dhrondan_country_effects.txt:476`, `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:60,1924`, and the provider-508 teardown at `:1956`.

Project-force teardown at `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:51-60` now revokes provider 508 unconditionally inside the exact teardown scope, so a stale or partially initialized package still reaches idempotent API reconciliation.

Event 019 setup and derivative setup use provider 508 receipt three, while cleanup revokes only provider 508 receipt three.

The former standalone alien project-force spawn path delegates to the shared template and landing reconciliation instead of maintaining a second unit or contact ledger.

D’Rhondan contact and sovereignty paths use the same API and do not directly mutate receipt variables.

No native CBRN project-family fallback was added.

## Reservation, refund, and Event 019 transaction evidence

The normal decision requires aggregate contact, a valid selected target, at least 2,000 laser weapons, no pending landing, no cooldown, and no world-end flag.

The decision saves `dhrondan_landing_state_id` and the begin helper debits exactly one reserve before setting `alien_infantry_landing_pending` and the seven-day mission duration.

The mission cancel path checks contact, state ownership/control, impassability, and world-end validity through `alien_infantry_landing_reservation_is_valid`.

Cancellation clears the pending flag before refunding, so repeated callbacks cannot refund twice.

Ordinary direct spawn debits only when the pending flag is absent, and a failed create-unit delta refunds the same direct debit.

Event 019 provider 508 receives the exact engine deletion ID and origin state at `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:698-710`.

The materializer guard at `:703-710` prevents a second provider callback while deferred mode remains active.

The generic unit transaction deletes the exact injected cohort before provider rollback and calls the shared provider rollback hook at `common/scripted_effects/019_infantry_spawn_generation_effects.txt:2198-2209,2383-2399`.

The same-tag rollback path proves package objects absent before calling `alien_infantry_rollback_event19_landing` at `common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2266-2305`.

The same-tag commit path calls `alien_infantry_commit_event19_landing` only when the persistent outer transaction and debit receipts are present at `:2739-2749`.

Event 019 management request and muster-board commit paths call the provider commit after their ledger proof, while the provider payment callback remains a zero-cost transaction gate and does not apply a second equipment debit.

## Event targets and cleanup plan

`dhrondan_landing_state_id` is a country-scoped regular state-id variable used as the selected-state pointer; it is not a global registry and does not encode physical population or unit data.

The normal decision, DHR bootstrap, and Event 019 materializer overwrite this pointer immediately before the shared spawn call.

The API clears it after ordinary success, ordinary failure, cancellation, invalid reservation, failed reservation entry, deferred commit, and deferred rollback.

Event 019 uses chain-local `infantry_spawn_current_origin_state` and `infantry_spawn_generation_country` event targets for the provider call, and the provider stores only the injected engine deletion ID as a regular country variable for delayed cleanup.

No global event target is created by the Alien Infantry API.

The former dead `dhrondan_origin_host` global target is absent after the prior hardening commit.

No global target cleanup helper or cross-country pointer was added in this pass.

## Provider 508 isolation

`chaos_unit_family_provider_508_register` declares `spawn_only` availability and the family-only Event 019 lot policy at `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:169-185`.

Its management evaluator exposes only `can_spawn`, with training, sustainment, and training-use outputs zero at `:1097-1111`.

Its sustainment callback and generic payment path are explicit no-ops, while the shared API owns the exact laser reserve.

Its custom equipment publisher exposes only `alien_laser_weapon_equipment_1`.

Its setup and cleanup callbacks preserve the provider-specific source receipt and do not borrow another family’s template, equipment, manpower, progress, or presentation.

## Bounded iteration audit and blocker

The Alien Infantry API, API triggers, decision, Event 019 adapter, Event 019 provider transaction, and D’Rhondan contact effects contain no `on_daily`, `on_weekly`, `on_monthly`, `every_country`, or `every_state` surfaces except the two D’Rhondan country calls listed below.

The exact remaining broad scans are `common/scripted_effects/016_dhrondan_country_effects.txt:29`, which counts every marked landing state globally, and `:107`, which claims every marked landing state outside DHR globally.

Those scans are inside one-time revolt setup rather than a recurring on-action, but they still violate the accepted no-broad-world-iteration boundary for this audit.

Replacing them with `every_owned_state` would change the intended global count/claim behavior, and inventing a sparse registry would create a second landing-state ledger without an accepted design addendum.

This subagent therefore left both scans unchanged and records them as a parent-level design blocker requiring either an accepted landing-state registry plan or an explicit approval for the one-time global scans.

All other D’Rhondan component and enclave passes use `every_owned_state` on the current DHR country and remain bounded to the active country.

## Weighted logic evidence

The D’Rhondan rebellion pulse in `common/scripted_effects/016_dhrondan_contact_effects.txt:344-369` was inspected as a weighted surface without changing its tuning.

The required first-pass MCP call was `hoi4.probability_inspect` with `adapter = random_list` and source `common/scripted_effects/016_dhrondan_contact_effects.txt`.

The MCP result was `PROBABILITY_SOURCE_INSPECTED` with no diagnostics, a complete discovered source, two candidate branches, and no available adapter candidates under the requested narrowed adapter.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c5658084050657fb49830c24776e1b2f4122e6848c78ca7a588971ac46cf699f/e86a3fb913e434c643ee812b830771c66da5b11249920e542af49c101b65f8bd/probability-inspect-4ecd98b765f6.json`.

The installed MCP tool surface did not expose `chaosx_ai_probability_auditor`, so the required auditor evidence pass and probability compare could not be routed.

This weighted helper was not patched; no balance claim is made from source-only analysis.

## MCP event evidence

The focused read-only event inspection for `chaosx.nr16.47` used `mode = state_flow`, selector kind `event`, `expandHelpers = true`, and bounded depth/node/edge limits.

The result was `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, while the workspace-wide helper projections were deferred and the inline source inventory was truncated by the MCP configuration.

Focused rerun artifact (the MCP source revision and graph hash remained unchanged after the local edits): `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d2003fbda939789cc15d52065099176d41fddd7c631068d45e8e39c716d33e86/ea9c0720f6da6b5016373c9467c7141277dd8da84392b476eaa4e5175dd5570f/event-state_flow-cf24a2714b30.json`.

The event artifact reports `blockingDiagnostics = 0`, but its `validation.passed` field is false because large-workspace helper projections were deferred, so it is evidence of a focused graph read rather than full completion proof.

No GUI or map surface is introduced by this API change, so no GUI or map rewrite was requested.

The prior focused Event 016 evidence and render timeout remain relevant: the prior `.47` render exceeded its 180-second limit, and the fresh `.40` inspection also timed out.

## Files changed in this pass

- `common/scripted_effects/016_alien_infantry_api_effects.txt`: failed-reservation cleanup, country-scoped spawn result, and persistent Event 019 commit proof.
- `common/scripted_effects/016_alien_infantry_api_effects.md`: API contract wording for source receipts, stale target cleanup, and persistent Event 019 commit proof.
- `common/scripted_effects/chaosx_dynamic_effects.md`: one Alien Infantry output-contract line updated; unrelated concurrent edits in this shared documentation file were preserved.
- `docs/events/016_brilliant_scientist/systems/dhrondan_country.md`: bootstrap result lifetime wording updated.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_api_reconciliation_2026-08-26.md`: this handoff.

No API constants, source call-site files, Event 019 provider registration, D’Rhondan country gameplay routes, decisions, missions, or broad iteration files were otherwise changed.

## Scoped validation

`git diff --check` was run on the API effect, API markdown, and D’Rhondan country documentation files.

A targeted receipt-writer audit found `alien_infantry_contact_receipt_*` writes only in `common/scripted_effects/016_alien_infantry_api_effects.txt`.

A targeted bounded-surface audit found the two known D’Rhondan `every_state` scans at lines 29 and 107 and no other broad iterator in the reviewed Alien Infantry/Event 019/contact files.

The focused MCP probability and event inspections above were run read-only.

No Hearts of Iron IV process was launched, and no live-save or game-log validation was performed.

## Remaining concerns and follow-up

The broad D’Rhondan scans at `016_dhrondan_country_effects.txt:29,107` remain a blocker against a strict no-world-iteration completion claim.

The MCP probability auditor route is unavailable in this runtime, so weighted balance compare evidence remains pending.

The event MCP route returned a partial focused artifact rather than full workspace validation, and the prior event render timed out.

The API does not delete an existing `D’Rhondan Landing Cohort` template when all receipts are removed; it relocks or recreates the shared template while contact exists and clears stale reservation/target metadata. No supported delete-template effect was found, and no destructive template cleanup was invented.

The API still intentionally retains the country-scoped last-call spawn result until the next spawn call or explicit owner cleanup; it is not a ledger receipt and is reset before every spawn attempt.

The D’Rhondan rebellion pulse and AI factor tables were not retuned.

No simplification or fallback was introduced in the patched API paths.
