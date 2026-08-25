# Event 016 Alien Infantry and D’Rhondan API Audit

Date: 2026-08-25

Scope: read-only audit of the reusable Alien Infantry/D’Rhondan API, landing decisions, D’Rhondan transfer, Event 019 provider 508 integration, and CBRN project selection against the accepted Alien Infantry and Empire of D’Rhonda plan.

No gameplay files were edited. No small patch was applied. The only file created by this audit is this handoff.

## Executive result

The normal API path implements the accepted five-source numeric receipt model, exact 2,000-weapon reservation/refund, seven-day reservation expiry, state ownership/control targeting, D’Rhondan transfer conservation, and Event 019 spawn-only isolation. No P0 or P1 defect was found, and no broad `on_daily`, `on_weekly`, or `on_monthly` hook was found in the audited files.

The following latent or recovery risks should be addressed before treating the API as fully hardened:

- P2: a stale landing state variable can survive an invalid non-deferred spawn call.
- P2: Event 019 deferred materialization has no re-entry guard.
- P2: a global `dhrondan_origin_host` event target is written but never read or cleared.
- P3: Event 019 host cleanup conditionally skips the idempotent provider-508 revoke/reconcile when the receipt is already zero.
- P3: the public API has no matching helper reference document, although the system design docs describe the contract.

## Findings

### P2 — stale landing target is not cleared on invalid non-deferred spawn

Evidence: `common/scripted_effects/016_alien_infantry_api_effects.txt:331-369` places the shared spawn work, including target cleanup at `:487-492`, inside the outer gate that requires contact and a valid saved target. If a caller leaves `dhrondan_landing_state_id` set and calls `alien_infantry_spawn_landing_cohort` without contact or with an invalid target, the gate is skipped and the stale state ID remains.

The current decision path overwrites the target before a normal call (`common/decisions/016_alien_infantry_landing_decisions.txt:9-59`), and the Event 019 provider does the same (`common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:698-708`), so this is a latent API robustness issue rather than a demonstrated normal-path failure.

Minimal recommendation: add an unconditional final target clear for non-deferred calls, or route invalid exits through the existing target-clear helper. Preserve the target while Event 019 deferred mode is active because the provider transaction still needs it.

### P2 — Event 019 deferred materialization is re-enterable

Evidence: `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:698-708` sets `alien_infantry_event19_deferred_mode`, materializes a cohort/debit, and calls the shared spawn API. The shared API clears `alien_infantry_event19_deferred_debit_committed` at the beginning of each deferred call (`common/scripted_effects/016_alien_infantry_api_effects.txt:306-310`). The generic Event 019 path commits or rolls back only the currently recorded proof (`common/scripted_effects/019_infantry_spawn_generation_effects.txt:2196-2209`, `:2294-2295`, `:2360-2367`, `:2383-2399`).

If the provider materializer is re-entered before the outer transaction commits or rolls back, a second materialization can occur after the first proof has been cleared, while the later transaction cleanup observes only one proof. The normal dispatcher currently makes one provider call per request, so this is a defensive re-entry gap.

Minimal recommendation: guard the provider materializer with `NOT = { has_country_flag = alien_infantry_event19_deferred_mode }` or an equivalent API one-shot guard, and ensure stale mode is recoverable by the existing rollback path.

### P2 — dead global origin-host event target

Evidence: `common/scripted_effects/016_dhrondan_country_effects.txt:467-468` calls `save_global_event_target_as = dhrondan_origin_host` when the target is absent. Repository search found no consumer and no `clear_global_event_target = dhrondan_origin_host`.

Global event targets persist beyond the originating chain and can retain an obsolete first host. The active host-core restoration and transfer implementation is already in `common/scripted_effects/016_dhrondan_country_effects.txt:79-123` and does not use this target.

Minimal recommendation: remove the dead global target write, or document a real consumer and clear it at the end of the lifecycle. Do not leave an unbounded global pointer without a cleanup contract.

### P3 — conditional Event 019 cleanup misses stale-state reconciliation

Evidence: `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:51-65` calls the provider-508 revoke only when `alien_infantry_contact_receipt_event019_provider_508 > 0`. `alien_infantry_revoke_contact` is itself idempotent and reconciles (`common/scripted_effects/016_alien_infantry_api_effects.txt:80-131`, with reconciliation at `:172-215`).

If an interrupted or externally altered state has receipt zero but leaves contact active, pending reservation, or reservation metadata, the host cleanup skips the repair path. The ordinary source-revocation path is safe, so this is a recovery issue.

Minimal recommendation: call the idempotent provider-508 revoke unconditionally from this provider-owned cleanup, or call `alien_infantry_reconcile_country` after the conditional branch without touching other source receipts.

### P3 — missing public API helper documentation

There is no matching API helper markdown beside `common/scripted_effects/016_alien_infantry_api_effects.txt` or `common/scripted_triggers/016_alien_infantry_api_triggers.txt`. The contract is described in `docs/events/016_brilliant_scientist/systems/alien_infantry.md:23-35` and `docs/events/016_brilliant_scientist/systems/dhrondan_contact.md:32-50`, but those docs do not provide a complete per-helper reference with scope, inputs, outputs, defaults, side effects, and deferred transaction lifecycle.

Minimal recommendation: add a narrow API reference documenting `alien_infantry_grant_contact`, `alien_infantry_revoke_contact`, `alien_infantry_can_call_landing`, `alien_infantry_spawn_landing_cohort`, `alien_infantry_reconcile_country`, receipt ownership, reservation lifecycle, and Event 019 deferred commit/rollback requirements.

## Confirmed API invariants

### Source receipts and idempotence

`common/scripted_effects/016_alien_infantry_api_effects.txt:12-64` grants one selected numeric receipt and `:80-131` revokes only the selected receipt before reconciliation. The public trigger ORs the five positive receipts at `common/scripted_triggers/016_alien_infantry_api_triggers.txt:10-38`; source IDs are centralized at `common/script_constants/016_alien_infantry_api_constants.txt:8-18`.

Event 019 cleanup selects only provider 508 at `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:1950-1956`. Durable custom-technology/template flags are separate by design (`common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:273-283`; `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt:570-580`) and were not treated as receipt leaks.

### State targeting and reservation/refund

The valid-state trigger requires an impassable-free state owned and controlled by ROOT (`common/scripted_triggers/016_alien_infantry_api_triggers.txt:40-48`). The saved state ID is re-resolved and checked against the current country at `:50-57`; reservation validity is checked at `:59-66`.

The public call gate requires contact, no pending/cooldown/world-end state, at least 2,000 laser weapons, and a controlled state (`common/scripted_triggers/016_alien_infantry_api_triggers.txt:68-83`). Reservation begins by subtracting exactly 2,000 weapons and setting the seven-day pending reservation (`common/scripted_effects/016_alien_infantry_api_effects.txt:218-236`). Cancellation clears pending before refunding exactly 2,000, removes the mission, clears reservation days, and clears the target (`:238-252`). Reconciliation cancels invalid pending reservations and clears stale reservation data when no reservation remains (`:172-215`). The decision and mission wiring is at `common/decisions/016_alien_infantry_landing_decisions.txt:9-76`.

### D’Rhondan transfer and initial force

The transfer captures the host, marked states, viable capital, and initial-force counts at `common/scripted_effects/016_dhrondan_country_effects.txt:18-76`. It adds DHR cores and transfers or changes ownership while retaining host cores at `:79-88`, restores the host capital core and transfers host-owned marked states while claiming the remaining marked states at `:92-123`, deletes surviving host Alien Landing Cohort units without refund, and transfers the laser stockpile at `:127-137`.

The transaction lock, conservation checks, sovereignty receipt, and initial deployment are coordinated at `common/scripted_effects/016_dhrondan_country_effects.txt:424-500`. The initial-force branch uses temporary batch/initial modes and the shared spawn API (`:424-458`; `common/scripted_effects/016_alien_infantry_api_effects.txt:311-329`). The revolt trigger excludes DHR, requires a viable marked state, excludes world-end, and respects the transaction lock (`common/scripted_triggers/016_dhrondan_country_triggers.txt:23-37`). No broad world-iterating on_action was found.

### Event 019 isolation

Provider 508 is explicitly registered as spawn-only, family-only, and tied to the shared API at `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt:169-185`. It uses the shared landing template and records ten combat components rather than creating a second editable template (`:628-676`). Materialization, commit, and rollback are separated at `:698-719`.

The sustainment callback is an explicit no-op (`:744-749`); management exposes spawn only and disables training/sustainment/manpower-style paths (`:1094-1107`); payment is a no-op (`:1252-1254`); the pay callback records success without a resource debit (`:1610-1621`); refund cancels the reservation only after successful payment (`:1651-1660`). Provider setup and cleanup grant/revoke only the provider-508 receipt (`:1918-1923`, `:1950-1956`). No old Event 019 training/manpower callback is connected to this provider.

## Validation and evidence

- A comment/string-stripped brace scan over all ten requested source files ended at depth zero with no malformed block detected.
- `<=` and `>=` searches over the requested source files returned no matches.
- Broad `on_daily`, `on_weekly`, and `on_monthly` searches over the requested source files returned no matches.
- The required weighted inspection was run first for `common/scripted_effects/cbrn_project_effects.txt` with `hoi4_probability_inspect`. It returned `PROBABILITY_SOURCE_INSPECTED`, a complete nine-candidate pool, no diagnostics, and no unresolved inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ba3f44770f08d71e20b0b4a7b7abf983f797e0bbf5dad4931e953ab67fb1db94/b57ddac0f6d7cbe18b9c527093acd93a10f84146ec886f88ef28da658f17ffa9/probability-inspect-fcd942b6523a.json`.
- A read-only Event 019 `.47` state-flow inspection returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d89b3d78c57225491a7c74c1e7eb9b93ecb3cb321be8549d4ac720a58a5b302/69ce45d1dfaf51d04079a6d5d0f6ff730494ca8cbece81e11066ac41c6f42828/event-state_flow-7d541a2019d5.json`.

## Blockers and limitations

- The installed tool list did not expose `chaosx_ai_probability_auditor`, so no scenario-normalized probability audit or probability-compare pass can be claimed. The source-level probability inspection above is the available evidence.
- `hoi4.event_render` for `chaosx.nr16.47` timed out after 180 seconds, and a fresh narrow `hoi4.event_inspect` for `chaosx.nr16.40` also timed out. The `.47` partial inspection is therefore not a complete workspace-wide lifecycle proof.
- The requested path `common/events/016_brilliant_scientist_dhrondan_contact_events.txt` is absent. The audited event source is `events/016_brilliant_scientist_dhrondan_contact_events.txt`.
- No live game process was launched, and no gameplay files were changed, per the read-only audit scope.

## Recommended follow-up order

1. Add the non-deferred stale-target cleanup guard and an Event 019 deferred-materialization re-entry guard.
2. Remove or lifecycle-manage `dhrondan_origin_host`.
3. Make provider-508 cleanup reconcile stale state even when the receipt is already zero.
4. Add the public API helper reference documentation.
5. Re-run Event 019 MCP inspection/render and the probability auditor when those routes are available.

## Post-hardening MCP recheck

After the API hardening commit, a focused read-only `hoi4.event_inspect` state-flow query for `chaosx.nr16.47` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. The authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9615670971b6b02597130541b19f73cd9943e705bde9d735340e441fb6dd4091/3662a730e22bd755fa9457005f0562c968f16c2d6712b56dd90a906ab4bf93e2/event-state_flow-cf24a2714b30.json`. The analysis remained partial because the workspace-wide helper projection and lifecycle passes were deferred; this is engine evidence for the focused path, not complete Event 016 acceptance.
