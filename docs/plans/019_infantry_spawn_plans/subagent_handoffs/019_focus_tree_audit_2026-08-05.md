# Event 019 derivative focus tree audit

Date: 2026-08-05  
Role: `chaosx_focus_tree_auditor`  
Scope: `common/national_focus/019_infantry_spawn_derivative_focus.txt`, its planning sidecar, and directly associated Event 019 focus localisation and icon references.

## Verdict

The authored Event 019 derivative tree has complete route coverage for the accepted package: 45 unique nodes, 54 prerequisite connectors, 45 AI blocks, 45 availability blocks, 45 completion rewards, 45 title keys, 45 description keys, 45 reward-tooltip keys, and 45 base-plus-shine focus icon pairs.

The expansion diagram's bounded-submission and conquered-integration outcomes are represented by sequential focuses plus decisions rather than a mutually exclusive focus fork. Both operations are present and feed the outward campaign and Regional Predator gates, so this accepted implementation shape is not counted as a missing route.

The sidecar source hash was the only file-level defect found in scope. It now matches the active focus source after an existing parent edit at the top of the focus file. Applying the fresh sidecar exposes five MCP layout warnings because the sidecar's supported `autoPosition.mode = auto` re-centers the authored branch coordinates; no authored geometry was changed in this audit.

## Files changed by this audit

- `common/national_focus/019_infantry_spawn_derivative_focus.focus-plan.json`: replaced only `sourceHash` with the active source SHA-256 `74038225fc4020c70b18a9a719545443c86d9e6d8beccc0741c552515c86faf3`.
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_focus_tree_audit_2026-08-05.md`: this handoff.

`common/national_focus/019_infantry_spawn_derivative_focus.txt` already had an unrelated parent change that replaces the unsupported script-constant country score token with a file-scoped constant at lines 1-23; this audit did not alter or revert it.

## Route coverage

| Route surface | Focus IDs and source lines | Coverage and behavior |
| --- | --- | --- |
| Opening survival | `infantry_spawn_derivative_hold_the_first_ground` through `infantry_spawn_derivative_name_the_future_host`, lines 35-134 | Five-node linear trunk secures the package, records the host, inventories districts, restores orders, and opens the hierarchy choice. |
| Hierarchy | `crown_the_claimant`, `convene_the_host_council`, `obey_the_family_instinct`, and descendants, lines 136-316 | Three symmetric mutually exclusive roots with three-focus payoffs; claimant breakaways are blocked from Collective and Species roots. |
| Sustainment | `mark_the_muster_depots` through `outlast_the_former_state`, lines 318-434 | Six-focus support lane unlocks depots, workshops, sustainment sites, family sustainment, fragmentation control, and former-parent command-net operations. |
| Military method | `make_an_army_of_the_host` through `a_method_fit_for_the_host`, lines 436-535 | Hierarchy capstones use an intentional AND prerequisite; Concentrated Host, Scattered Bands, and Captured Auxiliaries are mutually exclusive; the join uses one OR prerequisite block. |
| Expansion and integration | `read_the_neighboring_frontiers` through `become_the_regional_predator`, lines 537-640 | Five sequential focuses unlock frontier survey, warned local submission, conquered-district integration, outward campaign, and a hard-gated regional capstone. |
| Zombie overlay | Five IDs at lines 643-751 | Family opener, three route-locked transformation outcomes, and an OR-prerequisite capstone. |
| Ghost overlay | Five IDs at lines 754-861 | Family opener, three route-locked transformation outcomes, and an OR-prerequisite capstone. |
| Golem overlay | Five IDs at lines 863-969 | Family opener, three route-locked transformation outcomes, and an OR-prerequisite capstone. |

The tree totals 30 shared focuses plus five focuses for each of zombie, ghost, and golem. A nonhuman derivative therefore sees 35 focus-scale pieces before the hierarchy, military-method, and family transformation commitments remove alternatives. The claimant wrapper intentionally sees the 30 shared focuses and uses claimant continuity, guard, governance, sustainment, integration, and submission decisions as its adapted surface.

The Regional Predator availability block at lines 622-633 requires the active package, one consolidated hierarchy route, completed family or claimant transformation, sustainable reinforcement, resolved former-parent pressure, a regional territorial foothold, the centralized controlled-state threshold, and the centralized recorded-war-victory threshold.

## Missing or simplified content

- No requested hierarchy, sustainment, military-method, family, expansion, or capstone route is absent from the live source.
- The route-map drawing shows bounded expansion and conquered integration as two visual arms, while the live source implements `infantry_spawn_derivative_issue_the_submission_terms` followed by `infantry_spawn_derivative_absorb_the_conquered_districts` in one sequence and exposes the actual target choice through the warned decision surface. This accepted route shape does not bypass the former-parent or Regional Predator gates.
- Scenario claimant wrappers with `family_id = none` intentionally do not expose a nonhuman family overlay. They remain a separate claimant package boundary and cannot satisfy a family identity capstone without the claimant continuity path described by the package triggers.
- No fallback, placeholder, or unrelated focus content was introduced.

## Icon coverage

| Asset surface | Result | Evidence |
| --- | --- | --- |
| Focus icon references | 45 unique source icons | `common/national_focus/019_infantry_spawn_derivative_focus.txt`, all focus blocks. |
| Base SpriteTypes | 45/45 present | `interface/019_infantry_spawn.gfx:205-383`. |
| Shine SpriteTypes | 45/45 present | `interface/019_infantry_spawn.gfx:658-702`, each using `gfx/FX/buttonstate.lua`. |
| DDS textures | 45/45 present and valid | `gfx/interface/goals/019_infantry_spawn/`; all have native 100x88 dimensions matching vanilla goal textures. |
| Base/shine texture pairing | 45/45 exact pairs | Static parse found no missing or duplicate base/shine IDs and no texture mismatch. |

## Localisation and reward mismatch list

The Event 019 localisation file `localisation/english/019_infrantry_spawn_l_english.yml:882-1060` resolves all 45 title keys, all 45 `_desc` keys, and all 45 `_tt` keys. The reward-tooltip keys are unique, and their wording matches the corresponding route transition, flag, idea, decision unlock, resource, or capstone gate.

There is no unresolved localisation/reward mismatch. `inventory_the_seized_districts` and `mark_the_muster_depots` intentionally expose the same `Secure a Muster Depot` decision flag from two support lanes; the repeated unlock text is a minor hover-redundancy risk, not a missing effect.

## AI behavior gaps

No focus-level AI gap was found. Every focus has a nonzero constant-backed `ai_will_do` at `common/national_focus/019_infantry_spawn_derivative_focus.txt`, with route-aware preference or avoidance modifiers on all three hierarchy roots, all three military methods, and all nine family transformation choices.

The linked AI strategy file defines 22 self-removing profiles and 51 strategy entries at `common/ai_strategy/019_infantry_spawn_derivative_ai_strategy.txt`. Every profile has `abort_when_not_enabled = yes`; profiles cover opening survival, claimant/collective/species routes, governance subroutes, and zombie/ghost/golem family behavior.

The probability adapter discovered all 45 national-focus candidates without source diagnostics. A minimal empty-state evaluation correctly returned the two opening focuses as never eligible because the supplied scenario omitted package flags and variables; it is not a meaningful gameplay ranking and is not used as a defect claim. A full dynamic-state probability run was skipped because the required claimant, family, package, route, and former-parent variables are runtime transaction state rather than a stable manifest scenario.

## High-priority fixes first

1. Completed in this audit: refresh the sidecar `sourceHash` so the planning metadata is source-bound again.
2. Parent review requested: with the sidecar now applied, MCP emits `FOCUS_LAYOUT_SIBLING_ANCHOR_DEVIATION` for the zombie, shared-root, and ghost cohorts and `FOCUS_LAYOUT_SIBLING_ASYMMETRY` for the shared-root cohort. The auto layout shifts the displayed coordinates by -2 columns to bounds -12..12, while authored source coordinates remain -10..14. No authored geometry rewrite was authorized or performed.
3. Optional future design pass only: split the sequential submission/integration lane into a visible focus fork if the route map's two-arm diagram is intended to be literal rather than conceptual.

## Validation evidence

### Static source checks

- Brace-aware parse found 45 focus blocks, 45 unique IDs, 45 unique coordinate pairs, no unresolved prerequisite references, 45 availability blocks, 45 completion rewards, and 45 AI blocks.
- Localisation parse found 45/45 titles, 45/45 descriptions, and 45/45 reward-tooltip keys with no duplicate custom reward tooltip IDs.
- Icon parse found 45/45 base sprites, 45/45 shine sprites, 45/45 DDS files, valid DDS headers, and uniform native 100x88 dimensions.
- AI parse found 22 profiles, 51 strategy entries, and no profile missing `abort_when_not_enabled = yes`.

### HOI4 MCP inspect

`hoi4.focus_inspect` returned `FOCUS_INSPECTED` with 45 focuses and 54 connectors. The final applied-sidecar layout reports zero connector crossings, zero connector-through-node intersections, zero long connectors, 28 same-row pairs with no spacing violations, and five Event 019 layout warnings listed above. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5fec41f005edf548ec968ee71f6e59a7584e2e51b062b34e8ab5f736f97fbcd3/3a505342dd375cce3caad74f56fcfbc78c0f077d517fc8daf239e241b158d32f/focus-inspect.c3ddae83df05360d.json`.

The same inspect scan also reported 14 unrelated missing generic continuous-focus sprites from `game:common/continuous_focus/generic.txt`; none references Event 019 and none was changed in this scope.

### HOI4 MCP render

`hoi4.focus_render` returned `FOCUS_RENDERED` with HTML, SVG, JSON, source-map, and fresh planning-sidecar artifacts. The render preserved the same 54 connector checks and five Event 019 sidecar-layout warnings. HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fc7212013b726f7266e5992f1e74db488a7e854ea730118ffe8d8e524434ae4d/9033c4a50b5ef86eb9bdf5979134afe3407b3ee641219fb128ffdf7939992f49/infantry_spawn_derivative_focus_tree.focus.html`. SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c8b3755e9cf3bccb1806cb6ca5ae0fabeeac2dbd2fa031a266c508c4f23b0c18/02064fc061e20ea3384573f1c24d5bf27c6fa01566ae68c65ece889612658ef5/infantry_spawn_derivative_focus_tree.focus.svg`. JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f711d0090052e98b1e9db78db6a3c64a8923a06ab07a128ad62e4c75056d2fd/e0fce48da9db31e68ba990bb99788e219216331065d1d12f72c410cbe4f4b270/infantry_spawn_derivative_focus_tree.focus.json`.

## Skipped validation and remaining risks

- No in-game launch or save test was performed, per repository rules.
- No full dynamic probability ranking was claimed because the adapter requires runtime package and route state that was not safely inferable from static files.
- The MCP sidecar auto-layout warnings remain a presentation risk until the parent decides whether to accept the tool's recentering or maintain a separate authored-layout metadata mode.
- The sequential expansion lane and claimant-wrapper boundary are documented design choices; changing either would be a broader route redesign outside this narrow audit.

No gameplay fallback or unapproved simplification was introduced by this audit; the sequential expansion shape was pre-existing and accepted.

No commit was created because the parent owns final review and the shared worktree contains concurrent changes.
