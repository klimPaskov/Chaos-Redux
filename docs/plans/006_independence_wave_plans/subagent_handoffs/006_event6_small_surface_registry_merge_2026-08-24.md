# Event 006 small-surface registry merge — 2026-08-24

## Scope

This source-layout pass removes a second group of small Event 006 parser files without changing gameplay ownership, event IDs, portrait consumers, texture paths, or package admission.

The Join report, accept, decline, failure receipt, and scoped retry events (`chaosx.nr6.36` through `chaosx.nr6.40`) now live in the existing same-namespace `events/006_independence_wave_support_events.txt` registry. SCN-008 remains separate because it owns the `chaosx.triggerable_scenarios` namespace and launch-barrier contract.

The twelve small portrait sprite files for BRI, AXX, BAX, BBX, BOS, MNT, KOS, RUT, BSK, YAK, NAV/GLC, and MAC now live in `interface/006_independence_wave_portraits_registry.gfx`. Each section retains its original source marker, sprite identifier, and runtime DDS path. The larger IW-043/IW-058, IW-093/IW-098, Mediterranean, Pacific, and Region 01 portrait registries remain separate for package ownership and audit readability.

## Changed source

- `events/006_independence_wave_support_events.txt`
- `interface/006_independence_wave_portraits_registry.gfx`
- `docs/events/006_independence_wave/join_wave.md`
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`

The former files removed by this pass are:

- `events/006_independence_wave_join.txt`
- `interface/006_independence_wave_brittany_portraits.gfx`
- `interface/006_independence_wave_iw024_banat_portraits.gfx`
- `interface/006_independence_wave_iw027_thrace_portraits.gfx`
- `interface/006_independence_wave_iw028_epirus_portraits.gfx`
- `interface/006_independence_wave_iw029_bosnia_portraits.gfx`
- `interface/006_independence_wave_iw030_montenegro_portraits.gfx`
- `interface/006_independence_wave_iw031_kosovo_portraits.gfx`
- `interface/006_independence_wave_iw038_ruthenia_portraits.gfx`
- `interface/006_independence_wave_iw045_bashkiria_portraits.gfx`
- `interface/006_independence_wave_iw051_sakha_portraits.gfx`
- `interface/006_independence_wave_iberian_portraits.gfx`
- `interface/006_independence_wave_macedonia_portraits.gfx`

## Preservation checks

- The support registry keeps `add_namespace = chaosx.nr6` once and preserves all five Join event IDs and their executable bodies.
- The portrait registry has one outer `spriteTypes` container, twelve source sections, 22 unique sprite identifiers, and the same 22 runtime texture paths as the removed files.
- No portrait GFX name collides with any remaining Event 006 portrait registry.
- No country tag, character token, event target, decision, package gate, admission list, or DDS file is changed by this pass.

## Boundary

This is a source-layout consolidation only. It does not promote a package, change the 32/29/40/161 admission boundary, expose a pre-event surface, or claim live event/GFX parser or in-game evidence. Dated audits that cite the removed source paths remain historical traceability; current source-of-truth docs use the registries above.

## Engine-tool evidence

The required Event 006 MCP route was run against `chaosx.nr6.36` after the merge. `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics, and `hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics. The linked artifacts are the inspection lint report `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/da2c96696b96b79dbca279701b311f0de0d18900fc30e1562a330ffd25de3a6b/4fb2ca24aa9922002e0610d4c8696dd5284c89ba3758bdc869f1427884321fa2/event-lint-730923263b0a.json` and render manifest `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/65cfb7bd1236461a542194c25ac3a95807d49ea0a93618ef61fa78f0bba260ec/a840c6253ae3c90f86dbfa93b76099ea3f546214a19b8953bcdb5afbe45e2f11/event-overview-730923263b0a-manifest.json`. The tool deferred workspace-wide helper/lifecycle analysis, so this remains partial structural evidence rather than a whole-workspace acceptance claim.
