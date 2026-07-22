# Biological Stockpile Risk Icon Visual Validation

## Review evidence

- Contact sheet: `../contact_sheets/bio_stockpile_risk_icons_contact_sheet.png`
- Exact-size processed PNGs: `../processed_png/`
- Alpha metrics: `alpha_metrics.json`
- DDS header and decode validation: `dds_validation.json`
- SHA-256 records: `hashes.sha256`

The contact sheet was inspected over a checker background. Each processed PNG was also opened individually at its exact target canvas before DDS handoff.

## Visual findings

| Asset | Target | Exact-size read | Transparency review | Result |
| --- | ---: | --- | --- | --- |
| Controlled | 60x68 | Intact shielded cylinder, calm symmetry, cool status lamp | Transparent corners; no visible key fringe | handed_off |
| Strained | 60x68 | Crowded multi-canister rack, taut clamps, one amber lamp | Transparent corners; no visible key fringe | handed_off |
| Dangerous | 60x68 | Cracked outer shell, intact inner canister, diagonal brace, warning lamp | Transparent corners; no leak or exposed contents | handed_off |
| Critical | 60x68 | Warped door and failed rack, skewed structure, dark red emergency geometry | Transparent corners; no exposed contents | handed_off |
| National arsenal designation / relocation | 32x32 | Locked vault and canister rack behind a precise locator silhouette | Transparent corners; readable at 32x32 | handed_off |

The four idea icons remain distinguishable by structure and silhouette, not by color alone. The decision icon was reviewed as a separate 32x32 composition and is not a resized idea asset.
