# IW-045 Bashkiria shared focus hooks handoff — 2026-08-14

## Scope and ownership

This bounded patch wires the five IW-045 Bashkiria (BSK) package helpers into the existing `independence_wave_focus_tree` framework. It owns only the shared focus call sites and this handoff. It does not create a BSK focus tree, package root, central adapter or attestation, Join/dispatcher surface, localisation, icon, AI, decision, or event content.

## Changed file and identifiers

Changed file:

- `common/national_focus/006_independence_wave_focus.txt`

Every call uses the exact guard `original_tag = BSK` together with `is_independence_wave_bashkiria_package = yes`:

| Shared focus anchor | BSK helper effect | Source line |
| --- | --- | ---: |
| `independence_wave_prepare_capital_administration` | `independence_wave_bsk_focus_convene_frontier_congress` | 118 |
| `independence_wave_inventory_the_state` | `independence_wave_bsk_focus_secure_oilfield_communities` | 163 |
| `independence_wave_bind_the_first_oath` | `independence_wave_bsk_focus_integrate_frontier_guards` | 189 |
| `independence_wave_define_former_host_policy` | `independence_wave_bsk_focus_settle_former_host_ledgers` | 1421 |
| `independence_wave_recognize_fellow_new_states` | `independence_wave_bsk_focus_open_volga_ural_corridor` | 1692 |

The helper names are the stable IDs supplied by the parent and the IW-045 country-core owner. Their definitions and the `is_independence_wave_bashkiria_package` scripted trigger remain country-core owned.

## Route behavior before and after

| Full-framework focus | Before | After |
| --- | --- | --- |
| `independence_wave_prepare_capital_administration` | No BSK package call. | An active BSK package invokes `independence_wave_bsk_focus_convene_frontier_congress`. |
| `independence_wave_inventory_the_state` | No BSK package call. | An active BSK package invokes `independence_wave_bsk_focus_secure_oilfield_communities`. |
| `independence_wave_bind_the_first_oath` | No BSK package call. | An active BSK package invokes `independence_wave_bsk_focus_integrate_frontier_guards`. |
| `independence_wave_define_former_host_policy` | No BSK package call. | An active BSK package invokes `independence_wave_bsk_focus_settle_former_host_ledgers`. |
| `independence_wave_recognize_fellow_new_states` | No BSK package call. | An active BSK package invokes `independence_wave_bsk_focus_open_volga_ural_corridor`. |

All existing shared rewards, prerequisites, availability checks, layout, mutual exclusions, AI weights, localisation keys, and icon references are unchanged.

## Required source review

The offline National focus modding, Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding wiki snapshots were consulted. The vanilla `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md` were also consulted, along with vanilla national-focus examples. The focus syntax follows the existing IW-038/IW-040/IW-044 guarded `if` calls inside `completion_reward.hidden_effect` blocks.

## MCP evidence

The required post-change `hoi4.focus_inspect` completed successfully for `independence_wave_focus_tree` in workspace `mod_chaos_redux_ea3b2d67c2c0`:

- Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7eb9c40c6da1c1cb3d5348a567a7ec7703140f57deb4b9693998e530cf7e3cad/8920e363468c4bb0282be66a454bfc12671b208407c4c41fa6506395da8a8d64/focus-inspect.1d663c14d63236ce.json`
- Graph: 184 focuses, 206 connectors, zero connector crossings, zero focus-node intersections, unchanged layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`.
- Diagnostics: the five new helper references are reported as `FOCUS_GAMEPLAY_REFERENCE_PARTIAL` because the MCP shared source inventory does not yet include the country-core helper definitions. The remaining layout and continuous-focus diagnostics are pre-existing and outside this hook patch.

The required post-change `hoi4.focus_render` also completed successfully:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/358b3dc17b715efcd1fcc11593c8aa74f6ca5530b0f1cd2da6d44349a617ed6e/35a7b0a6595151b523de20a43f37dd94fe9f16b9b2b82c8540b11c2962a8d2fd/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c51a07eee7fcbe60e40231211902e20aa68aff6e2313b7484db6ee1705a5bf19/dfb7d7118d5178397991ada29dc23bc9df1a79c17d5a16c63c808ed62e69a7cf/independence_wave_focus_tree.focus.svg`
- JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5b0609274b53f1d83de68e930ec177b1044424337373ca1618ef6883b4fff55f/5f06c0ec4e37087298fa9306b5eaf247f8e008c71e647340538c1bdb33e65c4a/independence_wave_focus_tree.focus.json`

For the before/after comparison, the current shared-focus baseline in `006_current_focus_layout_audit_2026_08_13.md` records the same 184-focus, 206-connector, zero-crossing, zero-node-intersection graph and layout hash before these calls. This patch does not alter focus geometry, so no `hoi4.focus_rewrite` was needed.

## Validation limits and follow-up

The helper definitions and `is_independence_wave_bashkiria_package` trigger were not present in the MCP inventory during this focus pass; their existence, body behavior, and package activation semantics remain unresolved here and must be validated by the IW-045 country-core owner after those sources land. The parent must preserve the exact BSK guard and keep central admission/Join fail-closed until the package-core gates are independently complete.

No live HOI4 launch, save/load, or in-game focus completion was performed; those checks belong to the user/runtime validation boundary.

No localisation keys or icon IDs changed, so no localisation or asset validation was required for this narrow patch.
