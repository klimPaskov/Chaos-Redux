# Event 012 W5 B1 atomic certification blocker handoff

Status: queued and intentionally not implemented in gameplay source.

Owner scope audited: `common/scripted_triggers/012_africa_world_order_triggers.txt` and `common/scripted_effects/012_africa_world_order_effects.txt`.

## Finding

The current source has no authoritative runtime receipt that can certify all six political package surfaces before Action 85 installation.

The existing `africa_world_package_implementation_ready` writer in `africa_world_commit_package_successor` is successor-only continuity transfer and must remain separate from initial certification.

The existing `africa_world_package_roster_review_noted` flag is the Event 12.110 player docket acknowledgement, not a W0-W4 implementation review receipt.

The six `africa_*_high_chaos_package_reviewed` global flags are route-specific high-chaos focus and AI gates, not package certification receipts and not valid substitutes for grounded political proof.

## Existing scriptable proof map

The frozen roster is represented by the host-owned `africa_world_package_candidates` array, `africa_world_package_candidate_count`, `africa_world_package_pending_count`, `africa_world_package_absent_count`, `africa_world_package_resolved_count`, and `africa_world_package_roster_disposition_count` variables, plus `africa_world_package_roster_documented`, `africa_world_package_roster_partial`, `africa_world_package_roster_incomplete`, and `africa_world_package_roster_complete` flags.

`africa_world_register_current_candidate` admits a candidate only when the existing candidate base proves a live, non-subject, non-Africa, non-special-chaos country with a controlled capital and a generic or explicitly approved focus surface.

`africa_world_package_is_candidate` and `africa_world_package_has_valid_identifier` prove the candidate flag and the six-value continent identifier range.

`africa_world_package_route_is_grounded`, `africa_world_package_shared_lanes_are_proven`, and `africa_world_package_ratification_is_proven` are installed-actor checks and therefore cannot certify a pre-install candidate without changing the lifecycle or inventing pre-install flags.

`africa_world_initialise_package_polity_foundation` and constituent protocol helpers are also installed-actor lifecycle surfaces and do not expose a candidate registration receipt.

## Missing authoritative receipt categories

No existing flag, array, variable, or event target was found for any of the following pre-install proofs:

- one grounded route registration receipt for each of the six continent packages;
- one constituent protocol registration receipt for each package;
- one AI eligibility or external-route-plan registration receipt for each package;
- one focus-tree registration receipt for each package beyond the generic/replacement admission check;
- one idea-sprite registration receipt for each package;
- one identity/flag registration receipt for each package;
- one localisation, asset, or documentation acceptance receipt;
- one global W0-W4 review acceptance receipt that could represent the named audit evidence without a numeric human-review variable.

The source files and documentation do show package focus trees, ideas, flags, AI plans, and W0-W4 gameplay helpers, but static existence is not an allowed runtime proof for this trigger and the script cannot inspect human visual/localisation/documentation review.

## Required future helper map

Once the owning package audits provide authoritative receipts, add `africa_world_all_package_runtime_surfaces_are_certified` in the trigger owner file.

| Helper | Scope | Inputs | Output | Side effects | Callsite |
| --- | --- | --- | --- | --- | --- |
| `africa_world_all_package_runtime_surfaces_are_certified` | Event 12 host country | Host roster arrays and counters, six candidate scopes, exact future W0-W4 receipt identifiers | Boolean all-six certification proof | None; it must remain a pure trigger | Reviewed post-`africa_world_finalize_package_roster` freeze point and the setter recheck |
| `africa_world_certify_all_package_runtime_surfaces` | Event 12 host country | The trigger above and the frozen `africa_world_package_candidates` array | None; readiness flags on all six or none | Sets only `africa_world_package_implementation_ready` on current candidates; no install, transfer, route, sovereign, or terminal mutation | Immediately after the reviewed roster freeze, before Action 85 installation |

The trigger must run in Event 12 host scope, require an exact six-entry candidate array, exactly one candidate for each of Middle East, Europe, Asia, North America, South America, and Oceania, zero absent/resolved or installed entries, valid live candidate scopes, controlled non-African capitals, and no successor, exile, breakup, terminal, protocol-pending, partial-ready, or high-chaos substitution state.

The trigger must check the exact receipt identifiers supplied by the W0-W4 package owners rather than infer completion from tags, focus visibility, default variables, current control, or asset existence.

Once the trigger is authoritative, add `africa_world_certify_all_package_runtime_surfaces` in the effect owner file.

The effect must recheck the trigger, then set `africa_world_package_implementation_ready` for every current candidate in one bounded `for_each_scope_loop` pass or set none; it must not install a package, transfer territory, complete a focus, set a route outcome, grant sovereign proof, or set `africa_the_world_super_event_package_ready`.

Call the effect only from the reviewed post-`africa_world_finalize_package_roster` freeze point after the main agent accepts W0-W4 gameplay, AI, localisation, assets, and documentation evidence.

Keep Action 85 and `africa_world_install_current_package` as the only installation lifecycle, keep `africa_world_commit_package_successor` as the only successor readiness transfer, and leave Action 90 behind its separate terminal presentation gate.

## Constants, targets, cleanup, and migration plan

No new constants are needed for the blocker handoff. The existing `africa_world_order.required_package_count`, `africa_world_continent.*`, and `africa_value.zero` constants are sufficient for the eventual six-slot proof.

No event target is needed for initial certification because the host-owned candidate array is already the durable bounded roster. Do not add a global event target for receipts unless a later design proves persistence beyond the roster transaction and provides an explicit cleanup owner.

No cleanup change is authorized in this queued tranche. Future replacement or loss handling must re-run the full all-six proof after re-nomination and must not leave five ready candidates plus a substitute.

The migration is therefore deferred: first register authoritative receipts in their existing owning systems, then add the trigger, effect, and reviewed post-freeze callsite, then run the all-six/five-candidate/lost-candidate/successor/terminal gate scenarios before changing any readiness consumer.

## Validation and limitations

Read-only source inspection confirmed the roster arrays, candidate admission checks, installed-actor proof boundaries, successor-only readiness writer, Action 85 installer gate, and separate terminal gate.

The required offline Paradox wiki data-structures, triggers, effects, scopes, event, decision, idea, localisation, on-action, modifiers, and AI pages were consulted alongside the vanilla trigger/effect/script-constant documentation.

The read-only HOI4 event inspector was not used to claim certification because this tranche owns no event-chain edit and the blocker is an absent receipt contract rather than an unresolved event edge.

No gameplay source was changed, no readiness flag was set, no fallback was introduced, and no unsupported receipt or setter was fabricated.

The exact remaining blocker is the absence of authoritative pre-install identifiers for grounded route, constituent protocol, AI, focus, idea, identity, localisation/asset/documentation acceptance, and global W0-W4 review. The parent agent owns receipt acceptance and the later implementation tranche.
