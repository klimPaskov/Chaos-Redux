# Event 014 GUI, Animation, and Portrait GFX Handoff

Target registry: `interface/014_cannibalism.gfx` (read-only in this tranche). Target layout: `interface/014_cannibalism_frontline_hunger.gui` (read-only in this tranche).

The registered runtime stems, dimensions, frame counts, and sprite identifiers in those files are authoritative. `validation/gfx_handoff.tsv` records all 26 static GUI sprites, all 12 non-portrait animation pairs, both portrait animation pairs, exact runtime paths, exact sizes, FPS, looping/play-on-show behavior, and reveal/route gates.

Vanilla precedent inspected: `interface/alerts.gfx`, `interface/countrypoliticsview.gfx`, and `interface/leadergroups.gfx`. All animated sheets use the verified one-row horizontal `frameAnimatedSpriteType` layout; GIFs are review-only.

The registered ordinary portrait is 12 frames at 6 FPS and requires the public reveal surface. The transformed portrait is 16 frames at 6 FPS and additionally requires the Wendigo route. Neither protected legacy portrait file was overwritten.
