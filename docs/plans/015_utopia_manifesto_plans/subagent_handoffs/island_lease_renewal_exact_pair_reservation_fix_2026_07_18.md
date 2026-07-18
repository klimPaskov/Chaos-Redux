# Event 15 island lease renewal exact-pair reservation fix

## Scope and outcome

The island lease renewal exchange now reserves the exact founder and lessor pair before event `chaosx.nr15.213` opens. A cancelled or replanned lease invalidates that request without releasing its reservation. The stale popup can still resolve through `chaosx.nr15.214`, but it cannot apply an answer to a later lease generation. Terminal and annexation cleanup remove both sides of every outstanding reservation.

This implementation uses country-scope arrays instead of numeric generation counters. It preserves simultaneous requests between different founder and lessor pairs while preventing a second outstanding request for the same pair.

## Files changed

- `common/decisions/015_utopia_manifesto_decisions.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `events/015_utopia_manifesto.txt`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/island_lease_renewal_exact_pair_reservation_fix_2026_07_18.md`

`common/scripted_effects/015_utopia_manifesto_decision_effects.txt` was inspected because it owns ordinary island runtime cleanup. No edit was required there.

No localisation, focus, asset, workbook, shared dynamic-helper, or source-spec file was changed.

## Helper map

| Identifier | Scope contract | Inputs | Outputs | Side effects | Call sites |
| --- | --- | --- | --- | --- | --- |
| `utopia_manifesto_has_live_island_lease_renewal_request` | Lessor is current scope and `ROOT`, founder is `FROM` | Current lease flags and provenance, lessor pending and invalidated founder arrays, founder lessor and pending target arrays, exact lessor ID, war state | Boolean trigger result | None | Event `.213` trigger and all three option effects |
| `utopia_manifesto_has_live_island_lease_renewal_response` | Founder is current scope and `ROOT`, lessor is `FROM` | Reverse form of the same exact-pair state | Boolean trigger result | None | Event `.214` response application guard |
| `utopia_manifesto_clear_root_island_lease_response` | Lessor is current scope, exact founder is `ROOT` | Founder identity | Removes pair-specific accept, counter, and refuse entries | Clears aggregate response flags only after their matching arrays become empty | Invalidation, `.214`, annex cleanup, terminal cleanup |
| `utopia_manifesto_clear_root_island_lease_renewal_reservation` | Lessor is current scope, exact founder is `ROOT` | Founder identity and previous lessor scope | Removes founder from lessor pending and invalidated arrays, removes lessor from founder pending target array | Releases only the exact pair slot | `.214`, annex cleanup, terminal cleanup |
| `utopia_manifesto_invalidate_root_island_lease_renewal_request` | Lessor is current scope, exact founder is `ROOT` | Both reservation directions | Clears any recorded answer and marks the founder invalidated on the lessor | Leaves both pending directions intact until popup resolution | `utopia_manifesto_return_island_project_lease` |
| `utopia_manifesto_clear_all_island_lease_renewal_reservations` | Current country may be a founder, a lessor, or both | All local pending, invalidated, and answer arrays | Clears local arrays and removes the current country from every reachable reverse array | Uses deduplicated temporary snapshots and clears aggregate response flags | `utopia_manifesto_clear_all_runtime_state` |

The reservation itself is deliberately direct and adjacent to the decision call site. `decision_utopia_propose_island_lease_renewal` first adds the lessor to the founder's `utopia_manifesto_island_lease_renewal_pending_targets`, then adds the founder to the lessor's `utopia_manifesto_island_lease_renewal_pending_founders`, then fires `.213`.

## State and cleanup lifecycle

### Reservation

- Founder array: `utopia_manifesto_island_lease_renewal_pending_targets`
- Lessor array: `utopia_manifesto_island_lease_renewal_pending_founders`
- Lessor invalidation array: `utopia_manifesto_island_lease_renewal_invalidated_founders`

The targeted decision rejects a target when either pending direction already records the same pair. It also rejects an invalidated entry, which prevents a cancelled request from being recreated before its old popup resolves.

### Live answer

Event `.213` can write accept, counter, or refuse state only when the canonical exact-pair trigger remains true. Every option always notifies the founder through `.214`. Event `.214` applies an answer only when its reverse-scope exact-pair trigger remains true. It then clears the pair's answer state and reservation regardless of whether the response was valid or stale.

### Cancellation and replan

`utopia_manifesto_return_island_project_lease` invalidates every recorded lessor pair before removing the lease relationship and lessor targets. Ordinary island replanning reaches that return helper through `utopia_manifesto_clear_island_project_runtime`. The pending slot remains occupied, so a recreated lease cannot consume the old popup's answer.

### Terminal cleanup

`utopia_manifesto_clear_all_runtime_state` first performs ordinary island cleanup, which invalidates an open request, then calls the aggregate reservation cleanup. The aggregate helper follows founder-side pending targets and lessor-side founder arrays in both directions before clearing local state. No global event target or world-iterating on action was added.

### Annexation cleanup

The existing `on_annex` founder snapshot now includes lessor pending and invalidated founder arrays before the annexed country's arrays are cleared. `utopia_manifesto_has_recorded_league_relation_for_root` also recognizes both reservation directions, allowing event `.163` to reach a founder whose only remaining link is an outstanding renewal slot.

`utopia_manifesto_handle_annexed_league_partner` clears the exact reservation from the annexed lessor and removes that lessor from the founder's pending target array. When the annexed country is the Event 15 founder, event `.164` reaches `utopia_manifesto_clear_all_runtime_state`, which follows the retained founder pending targets and removes the founder from each live lessor's arrays.

The existing regular event target `utopia_manifesto_annexed_league_partner` is reused only inside the annex effect chain. No new persistent or global event target was needed.

## Constants and tuning

No constants were added or changed. The fix changes request identity and cleanup, not cost, duration, AI weight, lease length, or ledger magnitude. Existing Event 15 script constants remain the only numeric tuning inputs used by the touched logic.

## Completed migration

1. Replaced flag-only request identity with exact founder and lessor reservation arrays.
2. Added canonical request and response triggers for the two event scope directions.
3. Split answer cleanup from reservation cleanup.
4. Changed lease return from immediate answer cleanup to invalidation with retained reservation.
5. Made `.213` response writes conditional while keeping `.214` notification unconditional.
6. Made `.214` apply only a live response and always release the exact pair slot.
7. Added reverse cleanup for terminal state and both annexation directions.

## Meaningful validation

- Confirmed the decision reserves both array directions before firing `.213`.
- Confirmed all three `.213` options contain an exact live-request guard and all three unconditionally fire `.214`.
- Confirmed `.214` evaluates the reverse live-response trigger before any lease extension or refusal consequence, then clears answer state before the reservation.
- Confirmed lease return invokes invalidation before clearing `utopia_manifesto_island_project_lessor_targets`.
- Confirmed `on_annex` snapshots pending and invalidated founders before clearing the annexed lessor arrays.
- Traced accept, counter, refuse, cancellation, same-pair replan, different-pair replan, founder terminal cleanup, lessor annexation, and founder annexation through the exact scope transitions.
- Checked balanced script blocks in all five changed gameplay files.
- Audited every pending and invalidated array read, add, remove, and clear call site in the scoped files to verify reverse-link symmetry.

## Artifact references and unsupported analysis

The implementation was checked against these required references:

- `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, especially arrays, event targets, and array scopes
- `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/On actions - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md`
- `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- Vanilla targeted-decision precedent in `common/decisions/SIA.txt`
- Vanilla annex on-action precedent in `common/on_actions/16_taog_on_actions.txt`
- Existing Chaos Redux shared helper registry in `common/scripted_effects/chaosx_dynamic_effects.txt` and `common/scripted_effects/chaosx_dynamic_effects.md`

Read-only HOI4 MCP inspection of event `.213` was attempted. It failed before producing an event artifact because the MCP artifact store returned `ARTIFACT_STORAGE_LIMIT`. No MCP-rendered event graph or comparison result is available for this handoff. Runtime popup timing and live engine execution were not available in the agent environment, so validation is limited to the documented engine contracts, vanilla precedents, static scope tracing, and task-specific structural assertions.

## Risks and follow-up

- The parent must review this narrow patch together with the concurrent Event 15 worktree because the owned files already contain unrelated changes.
- The implementation relies on the existing immediate event dispatch contract for the decision-to-`.213` chain and the existing `.163` and `.164` annex bridges.
- This change does not alter player-facing text because the behavior and visible choices are unchanged.

No fallback, simplification, placeholder, world iteration, or numeric generation counter was introduced.
