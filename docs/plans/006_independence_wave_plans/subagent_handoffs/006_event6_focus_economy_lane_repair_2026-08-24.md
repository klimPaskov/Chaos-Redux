# Event 006 focus economy-lane spacing repair

## Scope

This bounded parent-owned patch repairs the authored economy lane in `common/national_focus/006_independence_wave_focus.txt` without changing focus IDs, prerequisites, rewards, availability, costs, localisation, AI, or route logic.

The three contiguous focuses are now placed at `x = 32`, `y = 4`, `y = 5`, and `y = 6` respectively: `independence_wave_build_regional_transport_authority`, `independence_wave_establish_customs_service`, and `independence_wave_activate_package_economic_program`.

## Engine evidence

The pre-change `hoi4.focus_inspect` receipt reported 184 focuses, 195 connectors, zero crossings, zero node intersections, and seven authored layout diagnostics, including the regional transport-to-customs economy-lane detour.

The post-change `hoi4.focus_inspect` receipt succeeded with status `FOCUS_INSPECTED`, code `ok`, no blockers, 184 focuses, 195 connectors, zero crossings, zero node intersections, `longConnectorCount = 3`, and six authored layout diagnostics.

The post-change inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c0e68452933823b38c3ff01e63678e9bbf20ad112b9d71ab78a20e38b678c5a1/c8743fb75daf51bb07e272ab6ad802c5d1ec5e4d583a879bb37e771006db1250/focus-inspect.690e185771651b9d.json`.

The post-change `hoi4.focus_render` receipt succeeded with source-linked HTML, SVG, JSON, source-map, and plan artifacts and retained the same six authored layout diagnostics.

The post-change HTML artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a3864d32c4c50573e4c3de5f3eeb6422aab1b99d8f0fe478b5d54807dc31c2ae/d6073cf9d633d6f2e2e1cc3818b4d243a90547f94f7c66125508515ee712e776/independence_wave_focus_tree.focus.html`.

The post-change SVG artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/962730c91f6e0f38a4d0c2ac12cbe523ce7a3f7384a24152f02a61bd0099d53d/e9c07d867076318e0ef5ddf27b347d6b131ec00f767133807303ec867c57294e/independence_wave_focus_tree.focus.svg`.

The post-change JSON artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/493950d1c1c5084d04884d507a060567a162714ac1cc3fb9d5d5ffe37d900470/2ea3ef889e4e380dba89ace213620c936b5f5a80da57279f6722841454feacf5/independence_wave_focus_tree.focus.json`.

The rendered source dimensions are 21424 by 2440, and the source render hash is tied to this coordinate patch.

## Remaining warnings and boundary

Six authored layout warnings remain: the economic-program-to-treasury detour, the border-guard-to-military-archetype detour, three long military-archetype connectors, the former-host-to-successor-ledger connector, and the postwar-integration-to-regional-identity detour.

Fourteen unrelated vanilla continuous-focus icon diagnostics remain outside the Event 006 authored surface.

The focus surface therefore remains `HOLD`; this handoff records a spacing repair only and does not claim focus-tree completion, lint/validate acceptance, gameplay execution, or live visual acceptance.

## Validation and follow-up

The source edit is limited to three coordinate values, preserves the graph's zero-crossing and zero-intersection metrics, and reduces the authored diagnostic count from seven to six.

Resolve the remaining authored warnings through a separately inspected route-layout tranche rather than moving convergence nodes or rewriting military branches without a new plan and before/after MCP evidence.
