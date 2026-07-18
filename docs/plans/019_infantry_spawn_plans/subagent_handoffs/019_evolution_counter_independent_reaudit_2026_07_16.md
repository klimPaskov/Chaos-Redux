# Event 019 evolution counter independent re-audit

Date: 2026-07-16  
Role: independent read-only counter audit  
Scope: live Event 019 evolution counter rewrite, lifecycle maintenance, and recovery behavior

## Superseding verdict

**PASS. The fixes resolve both prior P1 findings and the prior P2 finding.**

This report supersedes the earlier FAIL verdict in this file.

Severity count after re-audit:

- P0: 0
- P1: 0
- P2: 0

The maintained counter design preserves the original world war-share population, keeps participant pressure independent, avoids a recurring country scan, and fails closed when receipt ownership cannot be proven. No new counter, lifecycle, scope, or syntax defect was found in the requested fix surface.

## Prior findings resolved

### Resolved P1: delayed annex cleanup cannot subtract old receipts from rebuilt counters

The new `infantry_spawn_prepare_evolution_counter_unregistration_epoch` effect at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:220` through `:268` separates three safe cases:

- A current-epoch country proceeds to ordinary exact subtraction.
- A country with a known older epoch clears all old receipts, including the legacy participant war receipt, adopts the current epoch, and proceeds without subtracting any rebuilt counter.
- A country with no recorded epoch and no receipt adopts the current epoch without touching a counter.

Missing epoch ownership with a live receipt remains ambiguous and calls the invariant failure path. This is the correct fail-closed result.

Both public unregistration helpers call the epoch preparation effect before entering their current-epoch implementation at `019_infantry_spawn_evolution_effects.txt:272` through `:279` and `:378` through `:385`. A repository-wide caller search found no external call to either `_current_epoch` helper. Their only calls are from those wrappers.

The ordinary annex retry remains exact. `infantry_spawn_finalize_annexed_ordinary_country_cleanup` at `common/scripted_effects/019_infantry_spawn_management_effects.txt:7731` through `:7740` commits only after participant unregistration succeeds. Failed cleanup is retained in the annexer's persistent retry queue at `:7801` through `:7804`, and the queue re-enters the exact annexed country scope at `:7863` through `:7879`.

Old annex retry sequence:

1. A current-epoch receipt underflow leaves its offending receipt intact, clears global counter readiness, and prevents cleanup commit.
2. The annexed country remains in the exact retry queue.
3. A later manifestation increments the epoch and rebuilds counters from currently existing countries.
4. The queued annexed country now has a known old epoch. Epoch preparation clears every old receipt without executing a subtraction and moves its `epoch_seen` value to the rebuilt epoch.
5. The current-epoch helper sees no receipt, reports success, and allows ordinary cleanup to commit.

The rebuilt counter snapshot is therefore not modified by stale annexed evidence.

### Resolved P1: dependent underflow stops later and parent removal

Participant unregistration at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:281` through `:375` removes derived receipts in this order:

1. anomalous preservation
2. claimant crisis
3. severe congestion
4. low control
5. participant parent

Every phase after the first requires `infantry_spawn_evolution_participant_unregister_succeeded > 0`. Any underflow sets that temporary to zero, preserves the offending receipt, marks the global invariant failure, and blocks every later phase. The participant parent at `:357` through `:374` cannot be removed after a dependent failure.

World unregistration at `:387` through `:423` removes war membership before world-country membership. The parent block at `:405` through `:422` is gated by `infantry_spawn_evolution_world_unregister_succeeded > 0`, so a war receipt underflow preserves the world-country parent.

Combined unregistration at `:425` through `:441` calls the world hierarchy only after participant unregistration succeeds. This preserves the intended dependency ordering across both trees.

### Resolved P2: stable ordinary population no longer uses the transient creation flag

`infantry_spawn_is_ordinary_evolution_counter_country` at `common/scripted_triggers/019_infantry_spawn_triggers.txt:61` through `:73` now excludes only:

- non-existing countries
- derivative countries
- persistent scenario actor, breakaway, takeover, and setup-bypass identities

It no longer excludes `infantry_spawn_derivative_creation_in_progress`. That transient flag still appears in unrelated transaction-safety triggers, but it cannot change maintained world evolution membership. The world denominator therefore matches the approved stable population during a derivative creation transaction or failure lock.

## Receipt inventory proof

`infantry_spawn_has_any_evolution_counter_receipt` at `common/scripted_triggers/019_infantry_spawn_triggers.txt:78` through `:89` contains the full receipt set:

- world-country
- world-war
- participant
- low control
- severe congestion
- claimant crisis
- anomalous preservation
- legacy participant-only war receipt

All live receipt writes and clears found in the repository are confined to `common/scripted_effects/019_infantry_spawn_evolution_effects.txt`. No unlisted receipt writer bypasses the inventory trigger or epoch wrappers.

## Recovery matrix

| Recovery case | Result | Reason |
| --- | --- | --- |
| Existing country with old receipts during manifestation | Pass | Rebuild synchronization clears old receipts before deriving current membership. |
| Receipt-free tag released after a rebuild with stale `epoch_seen` | Pass | Out-of-rebuild synchronization adopts the current epoch, then registers current world membership. |
| Receipt-free tag released after a rebuild with no `epoch_seen` | Pass | The complete receipt trigger proves there is no ownership evidence, so the tag adopts the current epoch safely. |
| Annexed country with old receipts in the exact retry queue | Pass | Epoch preparation discards old receipts without subtraction, then permits cleanup commit. |
| Current-epoch dependent underflow | Pass, fail closed | The offending receipt and every later parent remain, readiness clears, and the later manifestation rebuild repairs the maintained snapshot. |
| Missing epoch with live receipt | Pass, fail closed by design | Ownership is ambiguous, so readiness clears and no receipt or counter is changed. |
| Old receipt-bearing tag released before its exact cleanup retry | Safe quarantine | Release reconciliation closes readiness. The exact retry can discard the known old receipt without subtraction, and the next manifestation restores readiness. |

Current receipt writers cannot create a missing-epoch live receipt. Registration first passes country epoch synchronization, which records the current epoch before any receipt is added. The missing-epoch live-receipt branch therefore protects legacy or damaged state rather than a normal lifecycle state.

## Population, due path, and scan behavior

The two approved populations remain independent:

- World-country and world-war counters reproduce the original global war-share calculation.
- Participant and participant-derived counters include only ordinary Event 019 participants and do not feed the world war-share denominator.

The recurring due helper at `common/scripted_effects/019_infantry_spawn_evolution_effects.txt:1516` contains no country iteration. Country pulses call only country-local reconciliation and the leased due helper. The only counter rebuild scan remains the already-authorized manifestation `every_country` pass at `common/scripted_effects/019_infantry_spawn_core_effects.txt:493`. The four later `every_country` blocks at evolution-effect lines `:1420`, `:1441`, `:1462`, and `:1483` are one-time stage activation applications, not recurring sampling or repair.

The due path still requires counter readiness, no rebuild in progress, no invariant failure, and an idle scenario transaction before loading the maintained snapshot.

## On-action and scope review

The lifecycle hooks at `common/on_actions/019_infantry_spawn_derivative_on_actions.txt:9` through `:131` retain the correct country scopes:

- `on_war` and `on_peace` reconcile the directly affected country when boolean `has_war` changes.
- Release and government-change hooks reconcile the released or changed ROOT country.
- `on_annex` unregisters FROM before later cleanup and reconciles ROOT only while counters remain ready.
- `on_subject_annexed` unregisters ROOT. Receipt guards keep a second hook idempotent on a healthy current epoch.

The new helpers remain in country scope, use unscoped temporary variables correctly, and access global counter variables explicitly. The complete receipt trigger is also country-scoped. The wrapper calls do not introduce a ROOT, FROM, PREV, or event-target scope transition.

No unsupported Clausewitz construct or malformed block was found in the reviewed counter, trigger, management, or on-action surfaces. The HOI4 MCP lint request again returned `ARTIFACT_STORAGE_LIMIT`, so the engine-level artifact lint remains unavailable. The verdict is based on direct source review against the offline wiki, current vanilla documentation, vanilla on-action precedents, and focused source hygiene checks.

## References consulted

- Repository `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding
- Vanilla `common/on_actions/_documentation.md`
- Vanilla `documentation/effects_documentation.md`
- Vanilla `common/on_actions/00_on_actions.txt` precedents
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_evolution_counter_architecture_2026_07_16.md`
- Live Event 019 evolution, pulse, core, management, trigger, and on-action sources

## Changes made

No gameplay, localisation, spreadsheet, or asset file was edited. This audit only superseded the verdict and evidence in this handoff report.

Skills used: `chaos-redux-events`, `chaos-redux-subagents`.
