# Event 014 Static GUI and Non-Portrait Animation GFX Handoff

Target registry: `interface/014_cannibalism.gfx` (read-only in this tranche). Target layout: `interface/014_cannibalism_frontline_hunger.gui` (read-only in this tranche).

The registered runtime stems, dimensions, frame counts, and sprite identifiers in those files are authoritative. `validation/gfx_handoff.tsv` records all 26 static GUI sprites and all 12 non-portrait animation pairs, including exact runtime paths, sizes, FPS, looping/play-on-show behavior, and reveal/route gates.

Vanilla precedent inspected: `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, and `interface/leadergroups.gfx`. All animated sheets use the verified one-row horizontal `frameAnimatedSpriteType` layout; GIFs are review-only.

Portrait sprites and reveal gates are documented by the authoritative refreshed packages under `../leader_portraits_refresh/`.
