# Event 037 scene art handoff

Status: complete. All three final DDS files are produced and validated. No `.gfx`, script, localisation, or other gameplay file was edited. Nothing was committed.

## Final outputs

| Asset | Final DDS | Size | Sprite | Status |
| --- | --- | --- | --- | --- |
| Report picture | `gfx/event_pictures/037_mysterious_population/mysterious_people_manifestation.dds` | 210x176 | `GFX_report_mysterious_people_manifestation` | complete |
| Decision category picture | `gfx/interface/decisions/037_mysterious_population/mysterious_people_category_picture.dds` | 114x101 | `GFX_mysterious_people_category_picture` | complete |
| News picture (replaced) | `gfx/event_pictures/037_mysterious_population/news_mysterious_population.dds` | 397x153 | `GFX_news_mysterious_population` | complete |

The DDS headers are uncompressed 32-bit BGRA with one level. Each file length equals 128 + w*h*4. Each decoded DDS matches its processed PNG exactly.

## News review decision

Verdict: replaced. The previous image showed a large-headed grey figure with a rifle in a mountain setting. That suggests an alien or non-human origin, which the premise forbids. The replacement shows ordinary 1930s families greeted in a market square with bread, water, and blankets, in black and white with opaque background. The original is backed up at `docs/assets/037_mysterious_people/scenes/sources/original_news_mysterious_population.dds`.

## Deviations and gaps

- The report picture uses the vanilla report-card treatment, a tilted card with transparent corners. The brief asked for opaque full-canvas art, but the vanilla report references and the skill's report-card rule both use transparent corners, so the reference governs. Category and news are opaque, as their reference families are.
- The image tool returned 1536x1024 for every call, even when a different size was requested. Each source was cropped and resized locally to its canvas. This is recorded in the manifest.
- Each asset has one candidate, so no contact sheet was made. No candidates were rejected.
- Not checked: in-game rendering. The user's live validation is the final check.

## Evidence locations

- Manifest: `docs/assets/037_mysterious_people/scenes/manifest.json`
- GFX handoff: `docs/assets/037_mysterious_people/scenes/gfx_handoff.md`
- Sources: `docs/assets/037_mysterious_people/scenes/sources/`
- Processed previews: `docs/assets/037_mysterious_people/scenes/processed/`
- Review sheet: `docs/assets/037_mysterious_people/scenes/review/scenes_review_enlarged.png`
