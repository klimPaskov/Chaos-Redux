# Event 012 manual scenario Gods-of-Africa handoff — 2026-09-05

## Scope and disposition

This handoff records the narrow runtime repair that connects `SCN-011` Africa Is One to the Event 012-owned Gods of Africa lifecycle. The change is implemented in `common/scripted_effects/012_africa_triggerable_scenario_effects.txt`; the `World Is One` branch remains separate and does not start the tribute loop.

## Implemented contract

After the manual Africa Is One opening applies its continental package, it sets the existing `africa_evolution_i_logged` chronology receipt without replaying the ordinary Evolution I popup or reward package. It then calls `africa_gods_of_africa_begin_consolidation`, which reuses the normal owner-local initializer, generation identity, 180-day consolidation delay, and delayed activation gates. The existing Scramble callback remains queued afterward, so the scenario still follows the ordinary Event 012 response surface.

This keeps the manual scenario's intentional prerequisite bypass bounded to launch setup while preserving the Gods runtime contract: no second host, no separate global tick, no immediate activation, and no World Is One tribute loop.

## Validation evidence

- Focused `hoi4_event_inspect` lint for `chaosx.nr12.1` returned `status = ok`, `code = EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and revision `b21215aa484b34e2e808a18e534ffb74072b27ebe8a9f4994cfa673400443ef2`.
- Focused `hoi4_event_inspect` lint for `chaosx.nr12.309` returned `status = ok`, `code = EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and the same revision.
- Focused `hoi4_event_render` options output for `chaosx.nr12.1` returned `status = ok`, `code = EVENT_RENDERED_PARTIAL`, zero blocking diagnostics, and layout hash `8f4af934527836f1332b00388e891792008e2ede78b1c732d14780daba331b41`.
- The edited Clausewitz source has balanced braces and no unsupported `<=` or `>=` operators.

## Limits

No live HOI4 launch or save-state playback was performed. The MCP reports are bounded workspace evidence and defer the large workspace helper/lifecycle projection; user-owned live scenario validation remains open.
