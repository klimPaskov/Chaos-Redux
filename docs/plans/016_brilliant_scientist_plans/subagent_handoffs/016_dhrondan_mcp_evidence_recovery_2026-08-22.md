# Event 016 Alien Infantry and D’Rhonda MCP evidence recovery

> Historical MCP recovery snapshot superseded for Alien Infantry provider/runtime status by the accepted V13 package and static runtime promotion recorded in `docs/assets/016_brilliant_scientist/models_3d/alien_infantry/attempts/v13_firearm_preset/final_manifest.md` and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_alien_infantry_meshy_runtime_promotion_2026-08-26.md`. Retain the partial event/technology/map artifacts and their limits, but do not use its pre-promotion missing-package or approval blocker as current status.

Date: 2026-08-22

Owner: parent implementation agent

Scope: read-only recovery of previously timing-out Event, technology, state-flow, and map evidence. No gameplay, localisation, asset, probability, GUI, or map source changed.

## Result

The bounded MCP retry produced current artifacts for both Alien Infantry hidden technologies, Events `.40`, `.46`, `.47`, `.48`, Event 019 `.1`, Event `.46` state flow, Event `.47` downstream trace, and the static state-layer map.

Every Event and technology route returned status `ok` with the expected `*_PARTIAL` code, no blockers, and only `MCP_INLINE_FILES_TRUNCATED`. Validation remains partial because the server deferred workspace-wide helper or lifecycle projection. The artifacts are real structural evidence, but they are not a substitute for dynamic engine execution or user-owned in-game acceptance.

## Technology evidence

| Surface | Inspection | Render | Result |
| --- | --- | --- | --- |
| `brilliant_scientist_alien_infantry_tech` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5f76cae7b3decaacf071b21c19fbcb7e5d1dd092f5e2ef97f76acf97a430bb2a/24e76d05d4fe495c3bd372034603f425d5c3a44f145491364fd9d4d40334a75b/technology-explain-517708b76c53.json` | PNG SHA-256 `9066BA6E0B99EC48D62A0108DC4C22D7166851CB4847135D0E869A9BCCA20418` | Inspect and render returned `ok`, `TECH_INSPECTED_PARTIAL` and `TECH_RENDERED_PARTIAL`, with no blockers. |
| `brilliant_scientist_alien_predictive_warfare_tech` | `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1a9e1771d26390a05320058b5767dae69b584318fda0d538662dab581e231a4c/6e1467b705035850efacdba43d3764f05210b75df86c355cc67a74fc2a5b0adb/technology-explain-517708b76c53.json` | PNG SHA-256 `2D71CB7D2907BF17DC08D75538A8064F2A67255588E4FE03A772FFF073F3909A` | Inspect and render returned `ok`, `TECH_INSPECTED_PARTIAL` and `TECH_RENDERED_PARTIAL`, with no blockers. |

The installed technology adapter does not model Special Project definitions as technologies. A bounded unlock query for `sp_dhrondan_envoy_craft` returned an artifact with no targets or unlock rows and `complete = false`: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0cbfee1ae4364da1c67cf1596cc88f32e19fe3ec04493c582e242b8af1bcb99e/25f212b74a5fbd40761b24e5582bd77f5513340efd1693219ac6430ed7f405ef/technology-unlocks-517708b76c53.json`. This confirms the adapter boundary and does not validate the Special Project.

## Event evidence

| Surface | Inspection artifact SHA-256 | Render PNG SHA-256 | Additional evidence | Result |
| --- | --- | --- | --- | --- |
| `chaosx.nr16.40` | `432DA5F4B74D992386EAF22C1E670AEFB2C573FB844919527B186AE72C04526D` | `BB632E0556BD074D5FA307BBE1037A0EBFA840A2DB54A3BA1B9A4A361CCC291D` | None | Lint and option render returned `ok` with no blockers. |
| `chaosx.nr16.46` | `89A474510660032C5542801D5EE4CD7E6BEDD738FAFC8E00236A09904F522231` | `90D31DF7273AF7B812E86ECE6C9225684A7448487B0F5FD408519BE3DC65F0D1` | State-flow artifact SHA-256 `31765B8319759A698FE9C7C4521BFD8115D6C621A84EE149DFB4FC590D02A753` | Lint, option render, and bounded state flow returned `ok` with no blockers. The previous artifact-storage failure did not recur. |
| `chaosx.nr16.47` | `578CB9D4B8940C85BFB2399DE0E4A3D51884F10C253D084BB291CB4F7CBCB85B` | `DC7E3BB172161257FC63D8F0CA5B685C83E50C94CAE1BCA0271EFA74DB091199` | Downstream trace artifact SHA-256 `AB07F5A4B0A8D0843F0795975ECDFDAE3C8E3DAE1C6B6BDD620E5B165F767FBB` | Lint, option render, and bounded helper-expanded trace returned `ok` with no blockers. |
| `chaosx.nr16.48` | `D7DE62DA3B4CBB4324CD5F8E9395A1EE9403572A371A280935EE1A0B152BB13D` | `A894E438EFC4F1FDCA4A07A688AFFE767FF67449C2E2CBEC769BF160933F58F8` | None | Lint and option render returned `ok` with no blockers. |
| `chaosx.nr19.1` | `BE3BB6054F9584F1D2446D6698C785562C68A263C070E5B47AA788684E469E6C` | `FEA431EAD850402404BA4DCF6A1E343361A6953AFBAF992D185ED0E47E2A9F52` | None | Lint and option render returned `ok` with no blockers. |

The Event reports remain incomplete for full helper execution because the workspace-wide lifecycle projection is deferred. The `.47` trace improves source-linked coverage of the rebellion bridge, but it does not execute dynamic state IDs, transfer ownership, select a capital, prove enclave placement, or conserve equipment in the game engine.

## Map evidence

`hoi4.map_render` succeeded for the static state layer at scale 1 with coastline overlay. The PNG SHA-256 is `4EAF3E38B3CA2B30147F0B469EA118C90B5FA8E84813B9159BE3A11C8D316341`, and the tool returned `MAP_RENDERED`, status `ok`, and validation passed.

A bounded state inspection also returned the selected state record, but its workspace-wide map diagnostics included unrelated position and floating-harbor rows from `map/buildings.txt`. That inspection does not establish or reject the DHR transfer helper. The map renderer is static and cannot represent the runtime marked-state selection, third-party controller preservation, lost-state claim conversion, disconnected-component discovery, or later uprising join behavior.

## Comparison boundary

Fresh `hoi4.event_compare` and `hoi4.tech_compare` calls without a preserved pre-implementation graph returned `EVENT_COMPARISON_BASELINE_REQUIRED` and `TECH_COMPARISON_BASELINE_REQUIRED`. Attempts to use current lint and overview artifacts as substitute baselines returned `EVENT_GRAPH_ARTIFACT_INVALID` because those artifacts do not carry the comparison graph schema. No synthetic before-and-after claim is made. The current renders, inspections, state-flow report, and trace remain post-implementation structural evidence only.

## Meshy read-only recovery check

Task `01a02497-1fb9-7a1b-bec6-ec388d54a016` remains `SUCCEEDED` at 100 percent and reports exactly 30 consumed credits. The live Meshy balance was 626 credits on 2026-08-22. The candidate remains rejected because it omits the required laser rifle. A successful rejected task is not eligible for a failed-task refund, and no verified free correction operation exists in the locked route.

No paid provider call, Blender modification, model fallback, manual rifle construction, rigging, animation, export, or runtime entity wiring was performed.

## Remaining blockers

1. The accepted rifle-bearing `alien_infantry_entity`, seven genuine actions, packed materials, PDX export and reimport, synchronized sound bindings, and live runtime consumer remain blocked pending user approval for the proposed approximately 30-credit Meshy recovery or separate approval of another explicit recovery design.
2. The accepted text simultaneously caps the initial DHR army at fifteen cohorts and requires one cohort in every disconnected enclave. A host with more than fifteen disconnected viable components cannot satisfy both rules. Parent implementation preserves the hard cap until the user chooses the priority.
3. Dynamic DHR transfer and equipment conservation remain source-audited and partially MCP-mapped, not engine-executed.
4. User-owned in-game acceptance remains outstanding.
