# Event 021 lifecycle helper handoff

Date: 2026-09-02.

Status: the four requested lifecycle helpers are implemented in the three new source/documentation files, and this handoff records the integration boundary for the parent-owned successor promotion.

## Files changed

- common/scripted_effects/021_random_civil_war_lifecycle_effects.txt
- common/scripted_effects/021_random_civil_war_lifecycle_effects.md
- common/scripted_triggers/021_random_civil_war_lifecycle_triggers.txt
- docs/plans/021_random_civil_war_plans/subagent_handoffs/lifecycle_helpers_2026-09-02.md

No existing file, constant, call site, achievement hook, on-action hook, or parent effect was edited.

## Helper map

event021_refresh_target_pool_membership is a country-scope effect. It reuses the existing target-preparation effect, validates the current country against the registered-country receipt and automatic-target trigger, and transitions global.random_civil_war_live_target_count exactly once from the old candidate-flag receipt to the new valid state. Invalid, non-human, unregistered, annexed, and zero-weight candidates receive minimum weight and have candidate/ready receipts cleared. It is consumed by the existing bounded parent review paths.

event021_handle_annexed_country is a country-scope effect called with the annexed country as FROM by the existing on_annex callback. It repairs the registered-country, Critical queue, exposure, CXT, active-theater, and aligned front registries with reverse index removal, cursor repair, and count derivation. It clears only exact country-linked global pointers and preserves unrelated theaters.

event021_cleanup_absorbed_event6_adapter is a country-scope adapter effect used by the existing Event 006 absorbed-member path. It delegates bounded Event 021 cleanup and clears only transient Event 021 adapter bridge receipts plus the two explicit adapter bridge flags. Event 006 identity, package ids, origin history, and all independence_wave_* package state remain intact.

random_civil_war_front_capacity_available is a side-effect-free country trigger. It follows the existing fail-open initialization contract and checks only the published active-front count against the published front cap.

## Successor transfer contract

The cleanup helper explicitly distinguishes annex teardown from a surviving same-crisis successor through the vanilla on_annex contract: ROOT is the annexer/successor and FROM is the disappearing country.

Transfer is accepted only when ROOT exists, carries random_civil_war_successor_claimed, carries random_civil_war_host_country_scope, and that pointer still identifies the current FROM country. ROOT and FROM must also both carry a nonmissing random_civil_war_crisis_id with equal values. With that proof, host-linked front rows are rebound to ROOT; surviving actors keep their role receipts, their crisis-host pointers are rebound, and the optional aligned front_hosts row is replaced at the same index. The old active-theater row is rehomed to ROOT when at least one front row is rebound, and the global host pointer is rebound only when it pointed to FROM.

When rebinding actor pointers, the successor actor's immediate-opponent pointer to FROM is cleared rather than set to ROOT, preventing a self-opponent receipt. Other surviving actors whose immediate-opponent pointer names FROM are rebound to ROOT.

Without that exact proof, the effect treats the transaction as ordinary teardown and removes rows linked to the disappearing country. It does not guess that an unrelated annexer is a successor.

The parent-owned ordinary promotion sequence must therefore be:

1. Keep the old Event 021 host available as the explicit predecessor.
2. Promote the surviving successor and preserve random_civil_war_host_country_scope pointing to the old host; retain the same nonmissing random_civil_war_crisis_id on both countries.
3. Set random_civil_war_successor_claimed on the successor before white peace or annexation.
4. Perform white peace and other parent-owned old-host terminal handling without clearing the host pointer, crisis id, or successor receipt.
5. Execute annex_country while the successor proof and the old-host/front receipts still exist.
6. Allow on_annex to invoke FROM = { event021_handle_annexed_country = yes }.
7. Only after the callback, clear any remaining successor-transfer receipt and continue parent-owned history/achievement cleanup.

The parent history-only successor helper does not certify front transfer by itself. If parent ordering clears the predecessor pointer, crisis id, or successor receipt before the annex callback, the helper intentionally falls back to teardown; front transfer cannot be made safe from history fields alone. These are the remaining caller obligations for the parent promotion path, not a reason to delete host-linked rows unconditionally.

## Proven war-continuity boundary

The source proves actual war relations, but not automatic war inheritance across this succession. Ordinary Event 021 branches create the civil war with `start_civil_war`; Event 006 actor paths create a country war with `declare_war_on` and then require `has_war_with` before registering the front. Parent ordinary cleanup also explicitly calls `white_peace` against the immediate opponent and old host, which confirms that these relations are handled as explicit wars rather than as registry metadata.

`event021_parent_prepare_annex_successor` only preserves the successor/history receipts, and `event021_handle_annexed_country` only rebinds script scopes and aligned front/theater rows. Neither lifecycle path calls `add_to_war` or `declare_war_on`. The vanilla `annex_country` documentation covers annexation and optional `transfer_troops`, but does not document transfer of the disappearing country's remaining wars to `ROOT`.

The current Event 021 external-war state cannot fill that gap: `random_civil_war_external_war_at_opening` is a historical boolean, while the evidence strength/until values and capitulation flag do not identify an enemy country or a war id. `random_civil_war_immediate_opponent_scope` is one opponent pointer and is not a complete external-war roster.

This is an explicit unresolved integration blocker. Do not claim surviving-front war continuity from scope rebinding, `annex_country`, or `transfer_troops = yes`. If continuity is required, the parent must add a bounded pre-annex war-transfer step that records every required enemy while the predecessor/actor exists, applies the documented `add_to_war` or `declare_war_on` operation with the correct war context, and verifies `has_war_with` after annexation. The exclusive lifecycle files cannot safely invent that roster or redeclare those wars.

The parent `on_annex` sequence remains: `ROOT` must be the ordinary opposition successor, `FROM` the explicit same-crisis government predecessor, the matching nonmissing crisis id and successor host pointer must survive through annexation, and `FROM = { event021_handle_annexed_country = yes }` must run before those transfer receipts are cleared. The separate war-transfer step must occur before any old-host war relation is destroyed and must not be replaced by registry cleanup.

## Contracts and limitations

The front registry uses global.random_civil_war_front_ids as the authoritative row count and removes or preserves every known aligned metadata array at the same index. The helper assumes the existing append contract keeps these arrays aligned. It does not invent missing metadata rows or perform a world scan to repair a pre-existing misalignment.

The target aggregate is initialized to zero only when absent and is reconciled for the current country. It does not reconstruct unobserved receipts from the world, so a missing aggregate in an existing save remains bounded migration work owned by the parent/core lifecycle.

The Event 006 marker distinction is intentional: random_civil_war_event6_origin is a transient selected actor/front-role flag and is cleared during teardown, while random_civil_war_event6_origin_recorded is the durable canonical Event 006 origin receipt and remains intact, together with Event 006 package identity and independence_wave_* content.

The latest stale-target review is addressed: `event021_lifecycle_successor_transfer` starts at zero and is set to one only inside the successful current ROOT/FROM proof, never from a later `has_event_target(event021_lifecycle_successor)` check that could observe an earlier annex in the same effect chain.

No constants were added or changed, and no weighted balance target was selected. Existing shared constants are used for zero, one, and minimum target weight.

## Validation and evidence

Completed source evidence includes the required AGENTS and Chaos Redux event/subagent skill reads, the offline wiki core pages, and the vanilla documentation for effects, triggers, scopes, event targets, arrays, and script constants.

The read-only Event 021 trace inspection was run before implementation with artifact revision c9e9ac572a640a5ffaf82e4cd3c6b88ce5293ff4ded2a168fb5fb0beb1576d9c; the read-only Event 021 target render was run before implementation with artifact revision 3122085528c97a38ad6a9df398c0d5be505e333a1b1d1d28ff2531524414055b. Both returned partial workspace projections with zero blocking diagnostics, while helper/lifecycle projections were deferred.

Post-change trace inspection returned EVENT_INSPECTED_PARTIAL at revision 23d07f38466bd55877a4f79f36a99c34bb9b7f0790f582a264bb307cc60e4646 with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4192b3fd73be2addb08ff0c2f8cf331424ee0ae9ee8ca403119c9de1fa7efd65/ab7586e79ca61e2b2a0cacb77f68139ceb60894bf484b5c251aa39e5026f0609/event-trace-23d07f38466b.json. Post-change target rendering returned EVENT_RENDERED_PARTIAL at the same revision with manifest hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4903f54f7086dad5ac850216ac10bc7063e0c835a0795eec8334d7d7f6806999/cdae919ee17e6320b45276087ceb42a929067f03c4fb970b09f887c9149e6b1c/event-targets-23d07f38466b-manifest.json. Both reported zero blocking diagnostics, but the service deferred workspace-wide helper/lifecycle projections and returned helpers = 0 for the focused event view, so these artifacts do not certify helper expansion.

The post-change event comparison was first attempted without a baseline and returned EVENT_COMPARISON_BASELINE_REQUIRED: Provide a cached revision, graph artifact, or proposed source overlay. A later explicit comparison using before revision 23d07f38466bd55877a4f79f36a99c34bb9b7f0790f582a264bb307cc60e4646 with refresh true and render false returned EVENT_REVISION_NOT_CACHED, so no semantic before/after comparison is claimed.

A final bounded trace refresh after the stale-target fix returned EVENT_INSPECTED_PARTIAL at revision 18bf807c8be35655138be368b38a6ff43f90d4c9ac0a1470ca1d9d44f43afd8f with artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/47f8e16216d3e4315b5d6364546aadf0a2e65aead417d16eea9dc0b6a90cf18e/cedd9af747bfefff6df2da5c14f110bdd9e2b600998d3ac4b8f6874e41b49a39/event-trace-18bf807c8be3.json. It again reported zero blocking diagnostics while deferring workspace-wide helper/lifecycle projections, so it confirms the focused event surface was re-read but does not certify helper expansion.

The required probability inspection and the read-only chaosx_ai_probability_auditor pass found no declared candidate manifest, scenario fixture, or balance surface for this lifecycle trigger. A weighted comparison was therefore not applicable and no balance choice was made.

Live game execution and runtime fixture validation remain with the parent/user. The highest-value fixture is ordinary successor promotion with one primary and multiple secondary unresolved fronts, followed by assertions that front rows, actor host pointers, active-theater membership, global host pointer, registered/queue rows, cursors, and counts remain coherent. A separate absorbed Event 006 fixture must verify package identity and unrelated Event 006 content survive.

That successor fixture must separately prove each surviving actual war relation with `has_war_with`; front-row rebinding, `transfer_troops = yes`, or an external-war history flag is insufficient evidence. The current source has no enemy roster for this proof, so parent-owned war-transfer wiring is required before claiming full surviving-front continuity.

No commit was created because the task explicitly forbids commits.

## Parent follow-up

The parent should review the post-change event trace/render and certify the callback ordering above. Parent-owned achievement/history, opening-receipt, rollback, state-control, capitulation, and terminal-flag work was deliberately not touched in this tranche.
