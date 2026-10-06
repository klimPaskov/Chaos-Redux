# Event 010 graphics review

Acceptance basis: the user's assigned October graphics fix plan explicitly allows deletion of the three overlay families when unwired and requires removal of the superseded category sprite.

Implemented: removed `GFX_decision_category_death_country` and its 32×32 texture, plus the coastal-risk, wither-target, and compact-warning animated/static registrations and their six textures from `interface/010_death.gfx`.
The live category uses `GFX_decision_category_repair_death_country` in both category definitions, with its existing 52×40 replacement texture in `interface/visual_consistency_repair.gfx`.
No gameplay design was changed.

Consumer evidence: exact-name and path search across `interface`, `common`, `events`, and `localisation` found only the retired registrations for the removed families.
The MCP `source_lookup` baseline for `GFX_death_coastal_risk_pulse` returned its sole definition at `mod:interface/010_death.gfx:24–29`, revision `28aef0bca0675ef2ca9c40e93e57cfdb42ad03c4b37ac52229503c4e14fc4373`, and zero resolved references.
Its global reference completeness was false, so the direct scoped source search is also retained as consumer evidence.

Review evidence: the original external `gfx_review/010_*.jpg` sheets and the reviewed replacement `docs/plans/gfx_fix_2026-10/evidence/010_after_1.jpg`.
All four assigned findings are addressed by removing unused assets; no substitute animation was introduced.

Live check for the orchestrator: use a 1936 human country, fire Death through Settings, open its Decisions category, and confirm that the book category icon remains visible at the normal category size and that no dark-square overlay appears in the Black Atlas.

Skills used: event-assets, frame-animation for classification of the retired families, subagents, shared-git-commit.
