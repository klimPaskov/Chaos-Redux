# Event 005 focus selector repair handoff

Date: 2026-08-05.

Scope: safe focus-tree eligibility/loader alignment and deterministic focus-localisation collision repair.

Changed files:

- `common/scripted_effects/005_soviet_collapse_effects.txt`.
- `common/national_focus/005_soviet_collapse_republics.txt`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt`.
- `localisation/english/005_soviet_collapse_l_english.yml`.

The regional loader accepts `soviet_collapse_event_created_republic` or the paired `soviet_collapse_breakaway` plus `soviet_collapse_active_origin` state, while continuing to reject active Independence Wave origins.

The regional tree headers use the same event-created or active-breakaway-origin rule for Ukraine, generic breakaway, internal republics, Baltic, Caucasus, Central Asia, Moldova, Belarus, and Kazakhstan.

The eight previously tag-only custom splinter selectors now require `soviet_collapse_high_chaos_successor`: UWR, KMB, PRA, ILX, IKX, DSC, NRF, and ICD.

Seven custom focus IDs previously collided case-insensitively with lower-case idea localisation keys. They now declare explicit `text = <focus>_focus` keys, with matching `_focus` and `_focus_desc` localisation entries, preserving the idea keys and focus-specific descriptions. A case-insensitive localisation scan reports zero duplicate keys.

Validation evidence: file-level `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for the republic and custom files, and MCP `hoi4.focus_render` returned `FOCUS_RENDERED` for `UWR_soviet_collapse_focus_tree`, `soviet_collapse_breakaway_focus_tree`, `ILX_soviet_collapse_focus_tree`, and `NRF_soviet_collapse_focus_tree` with no render blockers.

The MCP map inspection resolved all twelve sampled successor setup states (248, 252, 195, 217, 247, 569, 585, 583, 827, 232, 256, and 249), with no unknown state IDs. The workspace map is not globally clean: the same inspection reported 2,654 omitted map errors, principally invalid building positions and floating-harbor sea adjacency, so country ownership, capitals, ports, supply, and railway runtime behavior remain unproved.

Weighted validation: `hoi4.probability_inspect` succeeded for all four focus files with zero unresolved source inputs, but every candidate pool is incomplete (`poolComplete = false`). A baseline empty-state evaluation returned only partial analyses with unresolved inputs (1,149 republic, 2,625 custom, 340 factory, and 84 ancient candidates); this is not campaign balance evidence. A sweep was rejected because no declared ranges were provided. Full country-package runtime scenarios and all focus-depth, layout, reward, icon, and protected binary-asset work remain open.

Remaining risks: the tree package still has widespread MCP layout warnings, reused icon assignments, shallow ancient and custom routes, queued UWR/KMB depth, and the no-touch flag/binary-asset boundary remains active.
