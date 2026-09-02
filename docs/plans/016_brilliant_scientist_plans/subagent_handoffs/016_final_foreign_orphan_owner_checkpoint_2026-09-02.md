# Event 016 foreign orphan settlement checkpoint

## Status and scope

This is a bounded continuation of foreign receipt checkpoint `892996690509da646c3dcfa1a912096327f7b862`.
The parent implemented actor-owned annex and terminal settlement after reviewing `016_final_foreign_orphan_design_2026-09-02.md`.
Independent source review in `016_final_foreign_orphan_postpatch_review_2026-09-02.md` accepts the current-valid-receipt source paths across all eleven operation types, with the native scope-lifetime and MCP limits below still open.
This is not whole-foreign-system acceptance or Event 016 completion.

No operation cost, duration, outcome formula, AI weight, option text, project reward, model, or asset was changed.
No fallback, country scan, recurring scheduler, game launch, or external provider request was introduced.

## Changed surfaces

- `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt`: original-host scope receipt, private record/finish/cancel cores, non-destructive incoming registry rebuild, and country-owned irreversible cleanup.
- `common/scripted_triggers/016_brilliant_scientist_foreign_triggers.txt`: actor-owned scope/id receipt predicate.
- `common/on_actions/016_brilliant_scientist_project_on_actions.txt`: documented annexed `FROM` and civil-war pre-annex `FROM` hooks.
- `common/scripted_effects/016_brilliant_scientist_effects.txt`: terminal cleanup before foreign context is cleared.
- `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`: promoted orphan ownership and nested-context contract before source edits.
- `docs/events/016_brilliant_scientist/systems/foreign_operations.md`: private helper scope, history, cleanup, and evidence contract.
- The design, independent review, and this parent checkpoint handoffs retain decisions and limitations.

## Settlement contract

Each successful start stores the original country pointer in `brilliant_scientist_foreign_operation_host_scope`, paired with the existing numeric host id.
Ordinary callbacks retain their original regular actor/host targets and fixed expected operation.
Private cleanup never recreates those targets or changes that expected-operation temporary.

The private record core writes one aligned actor row and one aligned original-host row, guarded by the existing recorded flag.
An unresolved cancellation receives the cancellation result and zero detection.
A previously recorded real result and its history remain unchanged.
Only the ordinary record wrapper dispatches recognition and reaction presentation, and only with a living non-terminal response context.

The private finish core records the same eleven type-specific resolved-target receipts, clears its live flag, rebuilds its original host's incoming registry, and clears its pointer last.
Registry reconstruction keeps each actor with a matching live pointer/id exactly once.
It derives the actual count and assassination marker rather than decrementing a possibly stale counter or clearing another assassin's marker.
The maximum-two start rule is unchanged; an unexpected historical excess is represented by its true count rather than hidden by clamping.

Irreversible country cleanup handles its own outgoing receipt, then a separate unique snapshot of its incoming actors.
Each matching actor settles against its own original-host pointer.
Nested registry reconstruction uses different temporary names from the outer cleanup snapshot.
Stale entries for another host are pruned only from this host's registry and do not cancel that actor's current operation.
Ordinary relationship cleanup remains untouched so transfer, defection, extraction, and assassination can finish producing their outcome.

## References and design dispositions

The parent consulted the offline Data structures, Scopes, On actions, Effects, and Triggers references, the installed effects/triggers documentation, and vanilla on-action documentation.
Installed `on_annex` documentation supplies ROOT annexer and FROM annexed; the civil-war pre-annex hook explicitly runs before the country is annexed.
The Event 006 former-host scope variable and Event 015 snapshot-before-registry-mutation pattern supplied repository precedents.

The design's initial `exists = yes` cleanup gate was rejected: it would exclude the annexed country merely because it no longer owns territory.
Cleanup enters the documented scope and validates its receipt/pointer/id, not territorial existence.
The initial per-entry decrement/deferred-mode approach was replaced with clear-live-before-rebuild ordering and distinct snapshot names.
No undocumented regular-target clearing, temporary-variable clearing, or parameter-substitution syntax was introduced.

## MCP evidence

Both source inspections were narrow `.100` downstream traces with depth 2, 30 nodes, 60 edges, helper expansion disabled, and refresh enabled.

| Evidence | Result | Revision / artifact |
| --- | --- | --- |
| Before inspect | `EVENT_INSPECTED_PARTIAL`; validation false | `3237301e947374484a4e3989e24f59d677c110075673b4a555a02fb02a907dfc`; [trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/53584ae540693252c7a36f5e5b84e237aad8980af742683b906656b8f1103928/a81cae7ebfafdba8bb5d16d697c22aea5bf9c1b1ccbf4b4acbceeade93a19c5b/event-trace-3237301e9473.json) |
| After inspect | `EVENT_INSPECTED_PARTIAL`; validation false | `27c77545e9241b4398d074f7bae0aaedf8ebba6790c26141f6e3508bf4238175`; [trace](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7ccff6447dc64632805eb791addb40b3e720e6b2511b669773bc19068ba6b49/f611a7ea3f0cb37f891bacbf5467fb0e7b3a8bcdb7d0e1a7f0b4cabb58ad64c2/event-trace-27c77545e924.json) |
| Before options render | `EVENT_RENDERED_PARTIAL`; seven selected nodes | [manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0b58b10f222b018094e98927a29440802dfbf25ae86e7d56fc7a412cf9301f53/4856611716b4de01ea6dc53691e29f1909cd8175b19d87b965aa31a89369ad9d/event-options-3237301e9473-manifest.json); [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/668305875b838f1a1ee906710f1ee07013a453774e156862a066f48bec5b66f4/63149b455153ab630602f614d767830212b038e8df7ced1b3c04cffac03b178c/event-options-3237301e9473.png) |
| After options render | `EVENT_RENDERED_PARTIAL`; seven selected nodes | [manifest](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5a8c1277fdf938b9a3a6e974c8795bd1da515b12aa5693c1ead6d0fc69738af1/750543c49762cd5ff68000e4e2527742f36ef55910bb0de27b093045b48ee150/event-options-27c77545e924-manifest.json); [PNG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/78bc14b57c9f3a8c14b27e28881bd5d5e3cd787ea1984570d84264d032d0a30b/e74e79657bfc715dbe0d7b569467939df504f58800cc2c6c531f45a557ab1fea/event-options-27c77545e924.png) |

Both renders retain layout hash `3838ce44ec8e7259bf263a21dfdd18aae2561fc4f12416e726c5132c95936b8f`.
This is bounded event-graph evidence, not an in-game GUI render or proof of private helper execution.
MCP reports helper projections and lifecycle passes deferred for the large workspace, and its validation result is false.
The parent did not use these render hashes as visual or transaction acceptance.

The cached-revision comparison of these exact revisions returned `EVENT_REVISION_NOT_CACHED`.
An artifact-backed comparison using the two returned trace resources returned `EVENT_GRAPH_ARTIFACT_INVALID`, with the explanation that the report uses an unsupported graph schema version.
Neither failed comparison produced an acceptance artifact.
No success is inferred from unchanged option layout or unchanged weighted source.

## Required source traces and open acceptance

Independent review covers all eleven operation types, intact completion, unresolved cancellation, recorded success preservation, actor annexation, host annexation, terminal cleanup, duplicates/count drift, two-assassin marker retention, stale entries belonging to another host, and nested caller target/temporary preservation.
The source trace also confirms that private cleanup cannot reach recognition news, super-events, foreign reactions, or other resource effects.
The reviewer withdrew the maximum-count clamp finding after the owner confirmed that the accepted reconciliation contract records true retained cardinality and enforces the two-operation limit only at the start gate.
Clamping only the counter would misrepresent three retained live entries, while dropping a valid third entry would lose receipt ownership.
No reachable non-annex country-destruction call site was identified; the possibility of a native unenterable scope remains an explicit broader coverage limit, not a demonstrated regression in these hooks.

Ordinary post-annex FROM/data lifetime remains an engine-ordering acceptance question.
The civil-war pre-annex route is documented, but the source and partial MCP graph do not establish every native annex timing.
The current stored pointer is created at every accepted start; this patch does not fabricate missing historical pointers or silently repair corrupt mismatched pointers.

Whole foreign balancing, all scenario-weight comparisons, final model packages, focus and GUI acceptance, presentation, catalog, and the rest of the final completion plan remain open.
No in-game completion is claimed.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or changed by this receipt patch.
