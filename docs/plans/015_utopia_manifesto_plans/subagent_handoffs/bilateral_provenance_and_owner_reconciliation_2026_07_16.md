# Event 15 Bilateral Provenance and Owner Reconciliation

## Scope

This tranche hardens multiplayer ownership of Necessary Ground diplomacy and post-case terms. It prevents one founder's cleanup from revoking another founder's relationship, preserves diplomacy that existed before Event 15, and reconciles owner changes without an all-country scan.

## Exact relationship sources

- Ordinary case-created access records exact founders on the target and is revoked only for the attributed founder.
- Island leases keep distinct lessor, access, compact, and lease-state founder indexes. Renewal responses are founder-and-lessor scoped.
- Settlement agreements keep exact partner and state founder indexes; the shared state package remains until the final founder leaves.
- Long-supply contracts keep exact partner and state founder indexes plus a separate resource-rights provenance index.
- Association duties keep an exact active-duty founder index before converting to the durable charter indexes.
- Generic case compacts, island compacts, settlement compacts, supply compacts, and autonomy pacts have separate sources. External recognition clears only when no live source or other external-network basis remains.

## Cross-source diplomatic co-ownership follow-up

Access and founder-to-partner guarantees now use exact target-side creator arrays across active cases, island leases, associations, stewardship autonomy, and League defense. `utopia_manifesto_has_event15_access_creator_for_root` and `utopia_manifesto_has_event15_founder_guarantee_creator_for_root` are the reusable partner-scope gates; saved-pair equivalents cover target-rooted withdrawal callbacks.

A source claims an existing relation only when another exact Event 15 creator already owns that founder-partner pair. An unattributed pre-existing relation remains unclaimed. Teardown removes the current source before testing the gate and revokes the actual relation only after the final Event 15 creator disappears. Case-to-island conversion transfers both access and guarantee provenance rather than destroying and recreating it. Association withdrawal uses the same saved-pair cleanup as founder-driven teardown, and annexation clears the two additional case and island guarantee arrays after exact founder callbacks run.

The association review is target-wide and generation-safe. Hidden `.207` owns a non-reusable delayed reservation and always releases it. Visible `.221` opens only for a still-live association; teardown invalidates an already open human popup, and a later association waits for a fresh full-duration reservation. Its public wording is founder-neutral because a target may have more than one valid association founder.

## Resource-rights safety

Long supply tests `has_resources_rights` for the exact founder before granting rights. Event 15 records provenance only when it creates the agreement. Cleanup calls `remove_resource_rights` only for an exact attributed founder-state pair whose rights still exist, preserving any agreement that predated Event 15.

## Ownership and terminal reconciliation

- Hidden bridge `.165` receives state-control snapshots for active cases, association charters, settlements, supply contracts, and island leases.
- The bounded Event 15 actor pulse `.150` reconciles owner-only changes that do not fire a controller-change hook.
- The peace-conference callback invokes the same actor-scoped reconciler immediately for affected Event 15 actors.
- Annexation snapshots exact reverse links before terminal target cleanup, then fails or removes each affected term independently.
- Active stewardship succession revokes only diplomacy attributed to the old target before installing the surviving successor.

No daily, weekly, monthly, or all-country iteration was introduced.

## Files changed

- `common/scripted_effects/015_utopia_manifesto_effects.txt`
- `common/scripted_effects/015_utopia_manifesto_decision_effects.txt`
- `common/scripted_triggers/015_utopia_manifesto_triggers.txt`
- `common/on_actions/015_utopia_manifesto_on_actions.txt`
- `events/015_utopia_manifesto.txt`
- `docs/events/015_utopia_manifesto.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/completion_coverage_matrix.md`

## Validation and remaining proof

Structural source checks confirm balanced event, effect, trigger, and on-action blocks. Final confidence remains subject to the current decision, country-package, and event-completion re-audits after the League package is frozen. A fresh MCP event lint could not write its artifact because the workspace artifact-retention limit was already reached; existing static evidence remains available.
