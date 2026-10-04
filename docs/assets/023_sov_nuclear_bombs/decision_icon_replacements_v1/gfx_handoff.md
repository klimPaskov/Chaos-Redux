# Event 023 decision-icon promotion handoff, 2026-10-03

These six 33x32 RGBA decision icons are `fixed (parent DDS/native approved/runtime promoted)` following the parent's explicit 2026-10-03 source, native, RGBA, DDS, and storage-edge acceptance.
The parent copied all six selected DDS files to the existing runtime destinations and archived the prior runtime files under `runtime_before_promotion/`.
Actual live consumer validation and MCP category acceptance remain pending.
The parent reported an absent namespace and current handshake gap in its own context.
In this curator session `mcp__hoi4_agent_tools__hoi4_decision_inspect` was exposed, but its read-only category inventory call timed out awaiting `tools/call` after 600 seconds and returned no artifact.
Tool exposure and a validation response do not establish service health, a standalone viewer, or current consumer acceptance.
The package DDS files remain retained selected copies, and each matches the corresponding runtime file by SHA-256.

| Decision-icon basename | Existing sprite | Selected package DDS | Promoted runtime DDS | Existing registration |
| --- | --- | --- | --- | --- |
| sov_nuclear_decision_accounting | GFX_decision_sov_nuclear_decision_accounting | dds/sov_nuclear_decision_accounting.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_accounting.dds | interface/023_sov_nuclear_bombs.gfx line 24 |
| sov_nuclear_decision_storage_hardening | GFX_decision_sov_nuclear_decision_storage_hardening | dds/sov_nuclear_decision_storage_hardening.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_storage_hardening.dds | interface/023_sov_nuclear_bombs.gfx line 44 |
| sov_nuclear_decision_reactor_construction | GFX_decision_sov_nuclear_decision_reactor_construction | dds/sov_nuclear_decision_reactor_construction.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_reactor_construction.dds | interface/023_sov_nuclear_bombs.gfx line 42 |
| sov_nuclear_decision_device_assembly | GFX_decision_sov_nuclear_decision_device_assembly | dds/sov_nuclear_decision_device_assembly.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_device_assembly.dds | interface/023_sov_nuclear_bombs.gfx line 31 |
| sov_nuclear_decision_delivery_preparation | GFX_decision_sov_nuclear_decision_delivery_preparation | dds/sov_nuclear_decision_delivery_preparation.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_delivery_preparation.dds | interface/023_sov_nuclear_bombs.gfx line 29 |
| sov_nuclear_decision_command_exercise | GFX_decision_sov_nuclear_decision_command_exercise | dds/sov_nuclear_decision_command_exercise.dds | gfx/interface/decisions/023_sov_nuclear_bombs/sov_nuclear_decision_command_exercise.dds | interface/023_sov_nuclear_bombs.gfx line 26 |

The sprite names and runtime basenames are locked and must remain unchanged. The existing registrations already point to the exact runtime paths above. No new sprite definition is proposed. Do not point a runtime texture at docs/assets/.

The parent completed source and native DDS review before promotion.
The main contact sheet is review/contact_sheet.png. Each DDS has an exact RGBA round-trip PNG plus native neutral-background, 4x nearest-neighbour, and 4x smooth previews under review/. The storage alpha-lineage comparison is review/storage_hardening_edge_lineage_4x.png.

Storage hardening uses `source_png/sov_nuclear_decision_storage_hardening_v2.png` for its selected processed PNG and promoted DDS.
The parent accepted v2's low-alpha upper-edge antialiasing after actual RGBA pixel proof, decoded DDS review, and neutral-composited native and 4x previews including bilinear enlargement.
Storage v1, v3, and v4 remain retained and unselected, with the documented v3/v4 fringe findings preserved in the manifest.

Full exact prompts, call IDs, source hashes, crop bounds, alpha bounds, DDS hashes, and selection states are in [manifest.md](manifest.md) and [prompts/generation_trace.md](prompts/generation_trace.md).
For each basename the current processed input is `processed_png/<basename>.png` and the current selected DDS is `dds/<basename>.dds`.
All six runtime files are 4352-byte, exact 33x32 legacy BGRA32, one-level mipless DDS with preserved native alpha, as verified by the parent.
No GFX edit was needed because the existing sprite-to-runtime chain is unchanged.
The [current reconciliation handoff](../../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_six_decision_icon_promotion_documentation_2026-10-03.md) records the six promotion hashes and six archive/legacy-mirror matches.
The legacy source, processed, and DDS mirrors remain historical archives rather than current inventory for these six icons.

The [historical producer handoff](../../../plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_production_decision_icon_replacements_v1_2026-10-03.md) remains unchanged.
Its pending-promotion and pending-edge-acceptance instructions are `superseded` as current status by this dated handoff and the current reconciliation ledger.
The parent owns source integration and final review, and the user owns live-game consumer validation.
The other Event 23 families, seven selected achievement triplets, and 75-asset total retain their previous inventory.
Full Event 23 asset review remains incomplete.
