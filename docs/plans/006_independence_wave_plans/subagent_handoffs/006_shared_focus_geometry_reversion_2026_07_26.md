# Event 006 shared-focus geometry candidate reversion

Date: 2026-07-26.

## Result

The coordinate candidate from `f8ca54d24` is reverted from the runtime source because the authoritative post-edit `hoi4.focus_inspect` and `hoi4.focus_render` result retained all fourteen blocking diagnostics and worsened aggregate crossing metrics.

The shared tree is restored to the pre-candidate coordinates. Focus IDs, prerequisites, mutual exclusions, rewards, icons, localisation, AI weights, and the accepted AGX overlay remain unchanged.

## Authoritative comparison

| Metric | Pre-candidate baseline | `f8ca54d24` candidate | Disposition |
| --- | ---: | ---: | --- |
| Regular focuses | 184 | 184 | restored baseline |
| Connectors | 223 | 223 | restored baseline |
| Connector crossings | 49 | 60 | candidate rejected |
| Node intersections | 18 | 8 | improvement insufficient |
| Long connectors | 27 | 35 | candidate rejected |
| Blocking diagnostics | 14 | 14 | candidate rejected |

The candidate relocated the blocking crossings rather than closing them. The current source therefore does not claim a focus-layout pass. The original fourteen-diagnostic geometry remains an explicit blocker and requires a new coupled reflow followed by authoritative inspect and render.

## Files and commits

- Restored source: `common/national_focus/006_independence_wave_focus.txt`.
- Historical candidate and offline audit: `006_shared_focus_geometry_repair_2026_07_26.md` and commit `f8ca54d24`.
- This reversion handoff records the failed candidate; it does not delete or rewrite the historical handoff.

No new focus node, route, prerequisite, reward, AI behavior, icon, localisation, asset, or fallback was introduced.

## Remaining validation

Run `hoi4.focus_inspect` and `hoi4.focus_render` against the restored baseline if a new coupled geometry design is prepared. Do not treat the offline zero-of-thirteen pair result from `f8ca54d24` as an engine acceptance result.

Event 006 remains **HOLD / incomplete**.
