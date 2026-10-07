# Riches Found controller idea artwork

The seven controller-stage ideas use one existing, distinct idea-family image per stage.
This repair changes their native `picture` lookup tokens only.
Idea IDs, stage selection, localisation, economic values, textures and sprite aliases remain unchanged.
It adds no idea or evolution and does not alter the single-controller-idea contract.

## Native lookup contract

HOI4 prepends `GFX_idea_` to an idea's `picture` value.
The previous seven values already included that prefix, requesting unregistered double-prefixed aliases.
The corrected values below name the suffix, resolving to their existing sprites in `interface/029_riches_found.gfx`.
Neither the double-prefixed aliases nor the idea-ID default aliases are registered in the inspected mod interface sources.

| Country idea ID | Correct `picture` token | Existing sprite | Existing DDS basename under `gfx/interface/ideas/029_riches_found/` |
| --- | --- | --- | --- |
| `riches_found_idea_windfall_receipts` | `riches_found_windfall_receipts` | `GFX_idea_riches_found_windfall_receipts` | `riches_found_idea_windfall_receipts.dds` |
| `riches_found_idea_managed_revenue` | `riches_found_managed_revenue` | `GFX_idea_riches_found_managed_revenue` | `riches_found_idea_managed_revenue.dds` |
| `riches_found_idea_resource_dependence` | `riches_found_resource_dependence` | `GFX_idea_riches_found_resource_dependence` | `riches_found_idea_resource_dependence.dds` |
| `riches_found_idea_captured_revenue_state` | `riches_found_captured_revenue_state` | `GFX_idea_riches_found_captured_revenue_state` | `riches_found_idea_captured_revenue_state.dds` |
| `riches_found_idea_gold_sick_administration` | `riches_found_gold_sick_administration` | `GFX_idea_riches_found_gold_sick_administration` | `riches_found_idea_gold_sick_administration.dds` |
| `riches_found_idea_infernal_accounts` | `riches_found_infernal_accounts` | `GFX_idea_riches_found_infernal_accounts` | `riches_found_idea_infernal_accounts.dds` |
| `riches_found_idea_reformed_settlement` | `riches_found_reformed_settlement` | `GFX_idea_riches_found_reformed_settlement` | `riches_found_idea_reformed_settlement.dds` |

All seven current DDS files decode at 64×64.
Their decoded RGBA pixels exactly match the individual PNGs under `docs/assets/029_riches_found/notes/decoded_icon_dds/idea/`.
The parent opened all seven of those exact runtime-equivalent images at native size and compared the idea-family reference sheet.
They show distinct windfall, administered revenue, dependence, captured authority, compulsive administration, infernal accounting and reformed-settlement subjects.
This establishes the reviewed lookup-to-current-texture chain, not final provenance or complete visual-family acceptance.
Historical generation requests remain unavailable for this family, and composition density, source/native/enlarged comparisons and consumer-level live appearance remain part of the full asset audit.

## Reference evidence

Offline `Idea modding - Hearts of Iron 4 Wiki.md:65-101`, revision `a6405eb98a02a9de4689b7c0ef80b5a887b6c6c747d3907f68c109ed3fd099ac`, documents the automatic prefix and default idea-ID lookup.
The revision-bound MCP reference read completed for that entire section.
Installed `common/ideas/afghanistan.txt:222-235` uses `picture = generic_democratic_drift_bonus` for `AFG_democratic_influence`.
Installed `interface/ideas.gfx:594-597` registers the corresponding `GFX_idea_generic_democratic_drift_bonus` and its DDS.
MCP source-location lookup identifies that idea and picture field with revision `10bd4d4c06fb0336607da8e741a375ddaa5be19c4a530608eb6f677b186f8efe`.
The installed idea file SHA-256 is `6552a3a0f024e52b941426e5b02cc2aec3129306139ccf31b6d75f7697cf6d30` and the installed sprite registry SHA-256 is `73b5be871c2e1d1df14b4bf8b6456c5231f5305742dcd41051074b56c330544f`.
No dedicated idea-picture documentation file was found in the installed `documentation/` or `common/ideas/` documentation-name inventory.
The exact installed consumer/registry pair is retained as the native precedent, not represented as a missing-documentation retrieval success.

The pre-edit Event029 idea file is retained in `docs/plans/029_riches_found_plans/evidence/2026_10_07_helper_output_before/common__ideas__029_riches_found_ideas.txt`, SHA-256 `b0400ae250ec13a910f2210d8dd444391b39cbff66368ec395c19acc0f6ab297`.
The unchanged Event029 sprite registry SHA-256 at review is `5a88367893053398eaa9ad99285f475461d08583f211055b49eae68590f567d3`.
The source audit found seven failed previous explicit lookups and seven resolved corrected lookups.
No new sprite, texture, portrait, flag, focus icon, animation, audio, unit or model was produced.

## Remaining acceptance

The three distinct evolution icon aliases still require an accepted live consumer.
This idea-token correction does not make those evolution assets consumed or convert them into extra country ideas.
It also does not complete the remaining decision, mission, category, modifier, report or achievement asset-family reviews.
No HOI4 launch, country-politics render or live appearance proof is claimed.
Any future artwork repair must preserve the exact family and sprite contract above and use the event-assets production and review workflow.
