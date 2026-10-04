# Event 014 hidden-hoard decision icons

Date: 2026-10-04.
Owner: implementing agent (Event 014 takeover, round 1).
Disposition: `implemented`.

## Assets

| Decision or mission | Sprite | Runtime texture | Native source | Processed PNG |
| --- | --- | --- | --- | --- |
| `cannibalism_unified_investigate_hidden_hoards` | `GFX_decision_cannibalism_unified_investigate_hidden_hoards` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_investigate_hidden_hoards.dds` | [investigate_hidden_hoards_src.png](2026-10-04_hidden_hoard_icons/investigate_hidden_hoards_src.png) | [processed](2026-10-04_hidden_hoard_icons/decision_cannibalism_unified_investigate_hidden_hoards.png) |
| `cannibalism_unified_seize_hidden_hoard` | `GFX_decision_cannibalism_unified_seize_hidden_hoard` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_seize_hidden_hoard.dds` | [seize_hidden_hoard_src.png](2026-10-04_hidden_hoard_icons/seize_hidden_hoard_src.png) | [processed](2026-10-04_hidden_hoard_icons/decision_cannibalism_unified_seize_hidden_hoard.png) |
| `cannibalism_unified_hoard_seizure_mission` | `GFX_decision_cannibalism_unified_hoard_seizure_mission` | `gfx/interface/decisions/014_cannibalism/decision_cannibalism_unified_hoard_seizure_mission.dds` | [hoard_seizure_mission_src.png](2026-10-04_hidden_hoard_icons/hoard_seizure_mission_src.png) | [processed](2026-10-04_hidden_hoard_icons/decision_cannibalism_unified_hoard_seizure_mission.png) |

The sprites are registered in `interface/014_cannibalism.gfx` beside the other unified decision icons.

## Production route

- Generator: the connected `gptimage` ImageGen route (`generate_image`, 1024x1024 request, high quality, returned 1254x1254 RGBA), one call per icon.
- Style reference: [style_refs.png](2026-10-04_hidden_hoard_icons/style_refs.png), the purge-rival, centralize-Larder, ration-audit and absorb-warlord decision icons upscaled for palette, texture and edge treatment only; the prompts forbid copying their objects.
- Subjects: an open ledger with a magnifying glass and a rusted key (investigation); a forced iron-banded strongbox with a crowbar, broken padlock, ration tins and a grain sack (seizure); a steel helmet on a chained cellar hatch with a bayonet rifle (seizure mission).
- Every prompt requested a real transparent background and forbade text, frames, medallions, borders, glows and white outlines.
- Native alpha was validated before processing: all four corners are zero alpha and the alpha channel spans 0 to 255.
- Processing: crop to the alpha bounding box, centre on a square, step down with Lanczos, a light unsharp mask, 30x30 subject centred on a transparent 32x32 canvas, written as uncompressed A8R8G8B8 DDS with the same 128-byte header as the existing unified icons (4224 bytes).
- No background removal or other fallback was needed.

## Review

[icon_contact_sheet.png](2026-10-04_hidden_hoard_icons/icon_contact_sheet.png) shows the three new icons beside three existing unified icons at native size and 3x, on a dark and a light background.
Each subject keeps one clear silhouette at 32x32, sits on clean transparent corners without a halo, and matches the set's rust, iron and dried-blood palette.
The seizure-mission icon carries the most detail of the three; its helmet and diagonal rifle still read at native size.
In-game decision-list appearance remains for live verification.
