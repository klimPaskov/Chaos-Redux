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

After the reversion, a fresh read-only MCP inspection restored the accepted baseline: 184 focuses, 223 connectors, 49 crossings, 18 node intersections, 27 long connectors, and 14 blocking diagnostics. The restored layout hash is `a7bd7fe6afd3db003f656ef344cedcc280edb3c30cb5e0c5f12cab316890acb1`. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/833dd6610a3319acef695202ff5bd8fb813b3d91394aeaa7d23c811e52e62c52/5fab31c7903fbe8c0b6407002110fc83d29076b06b81296ee706b5005dba2e7c/focus-inspect.06a4600113a059c6.json`.

## Files and commits

- Restored source: `common/national_focus/006_independence_wave_focus.txt`.
- Historical candidate and offline audit: `006_shared_focus_geometry_repair_2026_07_26.md` and commit `f8ca54d24`.
- This reversion handoff records the failed candidate; it does not delete or rewrite the historical handoff.

No new focus node, route, prerequisite, reward, AI behavior, icon, localisation, asset, or fallback was introduced.

## Remaining validation

Run `hoi4.focus_inspect` and `hoi4.focus_render` against the restored baseline if a new coupled geometry design is prepared. Do not treat the offline zero-of-thirteen pair result from `f8ca54d24` as an engine acceptance result.

Event 006 remains **HOLD / incomplete**.
