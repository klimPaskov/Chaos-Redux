# Event 011 graphics review

Acceptance basis: the user's assigned graphics plan requires removal of the two superseded 32×32 category sprites and textures.

Implemented: removed the stale `GFX_decision_category_011_secret_alliance_foreign_interference` and `GFX_decision_category_011_secret_alliance_coalition_crisis` registrations from `interface/011_secret_alliance.gfx` and their two textures.
The live category file already uses the matching `GFX_decision_category_repair_011_secret_alliance_*` sprites in `interface/visual_consistency_repair.gfx`.
No gameplay design was changed.

Consumer evidence: exact-name and path search across `interface`, `common`, `events`, and `localisation` found only the two retired registrations.
The replacement category identifiers and artwork remain intact.
Review evidence: original external `gfx_review/011_*.jpg` and reviewed replacement `docs/plans/gfx_fix_2026-10/evidence/011_after_1.jpg`.
Both assigned findings are addressed without substituting artwork.

Live check for the orchestrator: in a 1936 human country, start Secret Alliance through Settings, open Foreign Interference, then reach Coalition Crisis and open that category.
Both headers should show their existing full-size category pictures, with no small duplicate or missing icon.

Skills used: event-assets, subagents, shared-git-commit.
