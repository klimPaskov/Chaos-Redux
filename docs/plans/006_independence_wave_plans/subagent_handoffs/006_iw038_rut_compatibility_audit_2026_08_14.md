# IW-038 RUT compatibility audit — 2026-08-14

## Disposition

This read-only follow-up found no safe package-local preservation patch for the remaining vanilla CZE/MUN route surface.

No gameplay file was modified for this audit, and no central admission, attestation, preflight, Join, dispatcher, or vanilla file was changed.

The registered-tag audit obligation remains: preserve CZE release, OOB, player-switch, and RUT AI paths while branching them around a living Event 006-origin RUT.

## Source-backed route evidence

- `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md` records IW-038 as retired BLX to registered RUT and requires preservation of the CZE release, OOB, player-switch, and RUT AI paths around a living Event 006-origin RUT.
- `docs/specs/006_independence_wave_specs/research/006_tag_collision_and_reuse_audit.md` also requires package-origin gating and preservation of the normal vanilla branch when the package flag is absent.
- Vanilla `common/scripted_triggers/CZE_scripted_triggers.txt:166-190` defines `CZE_RUT_is_not_its_own_thing`; it requires `RUT = { exists = no }` and an `original_tag = RUT` absence check, so a living Event 006 RUT does not satisfy the CZE release-demand route.
- Vanilla `common/national_focus/czechoslovakia_mu.txt:1585-1697` defines `CZE_dismantle_poland`; both bypass and completion branches add RUT cores only inside `RUT = { exists = no }`, preserving cores when a living RUT carrier exists.
- Vanilla `events/MUN_Czechoslovakia.txt:5712-5895` defines `MUN_the_fall_of_the_republic.3`. Option `.3.a` and option `.3.c` both require `RUT = { exists = no }`; `.3.c` additionally transfers state 73, loads `RUT_fall_of_the_republic`, and runs `RUT = { change_tag_from = ROOT }`.
- Vanilla `events/MUN_Czechoslovakia.txt:5897-5941` defines `MUN_the_fall_of_the_republic.4`; its `random_country` targets any country with `owns_state = 73` and `original_tag = RUT`, which is the expected living-RUT ultimatum path.
- Vanilla `events/MUN_Czechoslovakia.txt:5943-6022` defines `MUN_the_fall_of_the_republic.5`; its resistance and concession options continue the normal living-RUT route through `.6` and `.7` rather than creating a second RUT identity.
- Vanilla `history/countries/RUT - Ruthenia.txt` remains untouched; its registered RUT history retains capital state 73, the vanilla RUT roster, and `CZE_back_against_the_mountains_RUT`.
- Vanilla `common/ai_strategy/RUT.txt` remains untouched; its ordinary RUT diplomatic and wartime strategies remain available to the registered RUT carrier.

## Current Chaos Redux boundary

- `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt:9-13` gates Event 006 RUT content by `original_tag = RUT`, the active-country predicate, and package ID `iw_038`.
- `common/scripted_triggers/006_independence_wave_ruthenia_package_triggers.txt:15-29` records the vanilla release fence through `has_independence_wave_rut_vanilla_release_fence`; the helper requires the package, `CZE_RUT_is_not_its_own_thing = no`, and state 73 owned and controlled by the Event 006 RUT carrier.
- `common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt:344-349` records the compatibility receipt only when that release fence passes; it does not mutate vanilla history, cores, OOB, character nationality, or AI strategy definitions.
- `common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt:351-422` performs package setup and installs the package-local RUT politics, routes, roster, force mapping, and AI profile only after the package initializer is admitted.
- `common/scripted_effects/006_independence_wave_ruthenia_package_effects.txt:436-504` removes only Event 006 RUT decisions, missions, ideas, flags, variables, additive characters, and Event 006 cosmetic tags; it does not remove the vanilla RUT idea, alter cores, alter history, or touch the vanilla RUT OOB.
- `common/ai_strategy/006_independence_wave_ruthenia.txt:21-69` contains package-gated Event 006 RUT strategy layers; it does not replace or remove the vanilla `RUT.txt` strategies.

## Why no local patch is justified

The CZE release and player-switch branches are already source-gated by living-RUT absence, so adding another package-local condition to those vanilla blocks would duplicate a vanilla condition without changing runtime behavior.

The MUN `.3.c` path is an entire vanilla effect sequence, and the package has no legal local call site that can prevent its `transfer_state`, `load_oob`, or `change_tag_from` effects when the vanilla event is intentionally invoked.

The MUN `.4` and `.5` paths intentionally target and resolve against a living registered RUT, so suppressing them from a package helper would break the required vanilla RUT ultimatum and AI path rather than preserve it.

The previously considered cleanup-origin guard is not applied here because `independence_wave_cleanup_iw_038_ruthenia` is called from shared lifecycle reset ordering and a new `independence_wave_active_origin` requirement would need a call-order proof; this audit does not authorize central lifecycle edits or a speculative cleanup change.

## MCP evidence

- Read-only `hoi4.event_inspect` namespace scan for `MUN_the_fall_of_the_republic` returned `EVENT_INSPECTED_PARTIAL` at workspace `mod_chaos_redux_ea3b2d67c2c0`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e29fd058d40737e15de0cc345a5ac584b6dc0dda1f2b6c91e80275a63cac58d5/b69ea42c9b0c5aca95805c572f482a032578ece3f21cb49abcc440302cb6adad/event-scan-741883f50501.json`.
- Read-only `hoi4.event_inspect` focused scan for `MUN_the_fall_of_the_republic.3` returned `EVENT_INSPECTED_PARTIAL` with the same event graph revision; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f58b641c5752d5cac87cff80acb140471c48e14f77342a0d2346dee6b8ad0e2c/98df33038ba72b5fa83e2132fd6d9094706b880b9db7d0971ee15253d32d2c44/event-scan-741883f50501.json`.
- Read-only `hoi4.map_inspect` selected state 73 and strategic region 9 and returned `MAP_INSPECTED`; artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/52943cb521192f7855363f4b80716fb9ec9c6f31ab82ea068a12b0eaaba6236e/96dd1d2ce32a7e20fc1f3e0c2da28f5c952a23211e3d1426e5eb855bb10a91fb/map-inspect.9697b693d9c28c90.json`.
- The map receipt passed state/region membership, network, adjacency, supply, and railway checks but reported unrelated workspace-wide building and port locator diagnostics; no map rewrite was made.
- The event receipts are partial because the large workspace analysis deferred broad helper projections; they supplied no blocker for the exact vanilla event source reviewed here, and this handoff makes no claim of live HOI4 runtime validation.

## Recommendation and blocker

Do not patch package-local RUT files for this audit tranche.

If the parent later requires interception of MUN `.3.c` after a living Event 006 RUT exists, it needs an explicitly approved vanilla event override or a central event-dispatch adapter that branches before the vanilla transfer/OOB/tag-change effects; both are outside this bounded audit and must not be inferred from this handoff.

No localization, portraits, flags, runtime assets, or unrelated packages were changed.
