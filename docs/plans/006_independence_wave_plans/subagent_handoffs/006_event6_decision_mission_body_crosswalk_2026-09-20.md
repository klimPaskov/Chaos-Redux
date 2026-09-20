# Event 006 decision and mission body crosswalk

Date: 2026-09-20.

Disposition: **implemented as current source evidence; no gameplay patch justified**.

## Scope

This parent-owned crosswalk revalidated the 80-row accepted matrix in `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv` against the current decision registries after the bounded IW-179 repair and the SCN-008 repair.

The detailed row-to-identifier, owner, cost-family, gate-to-terminal, cleanup, and localisation mapping remains in `subagent_handoffs/006_event6_decision_mission_matrix_implementation_receipt_2026-08-26.md`. This receipt re-read all mapped source bodies and records current structural results without replacing that detailed semantic table.

## Current revalidation

All 62 shared `DM-01` through `DM-62` rows resolve to the expected identifiers in `common/decisions/006_independence_wave_decisions.txt`. All 18 `FORM03-D01` through `FORM03-D18` rows resolve to the expected identifiers in `common/decisions/006_independence_wave_form03_decisions.txt`.

All 80 rows have a category context, a visible or activation gate, an availability gate, an AI block, and at least one terminal effect path. All 80 have a lifecycle marker: timed rows expose a removal, mission-timeout, re-enable, or cancellation path, while instant rows use the accepted `fire_only_once` contract or a timed state flag. The five instant rows without a decision timer or cancellation block are DM-14, DM-22, DM-27, DM-38, and DM-55; their bounded one-shot or timed treaty effects are the lifecycle mechanism, not missing mission cleanup.

All 80 title and description keys resolve in the current English decision/formable localisation set. Seventy-nine rows expose a custom cost text with matching base, `_tooltip`, and `_blocked` keys. FORM03-D11 is the intentional prepaid selectable objective and has no custom cost row.

The current structural result is 80/80 rows revalidated, 62/62 shared rows, 18/18 FORM-03 rows, and 79/79 custom-cost localisation triplets. No identifier mismatch, absent gate, missing terminal path, missing AI block, missing lifecycle marker, or localisation defect was proven. No decision, mission, cost, category, AI, or localisation source was changed by this crosswalk.

## MCP evidence

The focused read-only `hoi4.event_inspect` lint for `common/decisions/006_independence_wave_decisions.txt` returned `EVENT_INSPECTED_PARTIAL` at source revision `7bc390e9516d5b5dfe63dbd72b96eddd673953d1ad2177f259c603cef9509573`, graph hash `7515b51df827657755d7d03350ee5786cd35f05604a1ce64ad805354fb596225`, zero blocking diagnostics, and zero skipped sources. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1878d5a49caf50e6850672363eb0ec0646c0e9551277395343a07e0fc23363b2/3616ac777b794bbb13f601433fb807a7c213d585cc4cc5fada6bbb7c1abd7b90/event-lint-7bc390e9516d.json`.

The matching read-only options render returned `EVENT_RENDERED_PARTIAL` at the same revision with layout hash `dc7c6b2fdb9a3143f5ed65837542c0750cbf4453a8736f2c704ed2e8aa231e38`, 24 selected nodes, and 42,772 omitted nodes. Manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8892a330684f89093808150b701432e0b951cd50fde280dbc269685cec68647/bb6cdcabcf0cc20cc0dd1a1771a8769044e7ede9fa3e11c2c98036f024d68fa1/event-options-7bc390e9516d-manifest.json`.

The MCP evidence is structural and partial. Its deferred helper/lifecycle projections, native decision-row rendering, typed probability inputs, live execution, and save/load behavior remain open.

## Remaining design and validation limits

The crosswalk does not approve the unresolved generic diplomatic-light transport equality mismatch, the FSM category's simultaneous-action density, or the ordinary FSM receipt-loss atomicity question recorded in the IW-179 audit. It does not provide a quantitative AI or probability conclusion because the required campaign fixtures and same-scenario comparison baseline remain unavailable.

The whole Event 006 disposition remains **HOLD / PARTIAL** at the unchanged 32 content-attested packages, 29 compatible reservation groups, 40 runtime adapters, and 161 unattested selectable rows. No package admission, central allocator, Join, formable reachability, identity, portrait, flag, GUI, asset, audio audition, or live-runtime gate is widened by this crosswalk.
