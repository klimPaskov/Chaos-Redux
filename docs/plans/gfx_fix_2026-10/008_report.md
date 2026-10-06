# Event 008 Tensions Rising news-photo repair

## Accepted result

The smeared lower-left newspaper stacks are removed while the original street-checkpoint photo, guard, railings, and crowd remain. The parent reviewed the before-and-after contact sheet and accepted the crop on 2026-10-06. The acceptance basis is the user's current authorized GFX-repair scope and the parent's visual review on that date.

## Source, crop, and final texture

| Item | Evidence |
| --- | --- |
| Sprite | GFX_news_event_tensions_red_line |
| Existing runtime path | gfx/event_pictures/008_tensions_rising/news_event_tensions_red_line.dds |
| Target .gfx | interface/008_tensions_rising_event_images.gfx |
| Original runtime DDS backup | docs/assets/gfx_fix_reports_2026-10/notes/008_tensions_rising/runtime_before/news_event_tensions_red_line_before.dds |
| Original DDS SHA-256 | ba6b06cf5582cbfc353a43e96cf1cd3d2acec34d85e62e63261993cf9ae095ae |
| Retained source PNG | docs/assets/gfx_fix_reports_2026-10/source_png/008_tensions_rising/news_event_tensions_red_line_source.png |
| Source PNG SHA-256 | 91153b1adca978f2e916595bcd4219ecc500a08f070ffb34dfceaf694f204ac4 |
| Source and final size | 397x153 |
| Crop box | x=148, y=0, right=397, bottom=96, giving a 249x96 crop |
| Deterministic processing | Convert to grayscale, apply contrast 1.08, and resize with Lanczos to 397x153. |
| Processed PNG SHA-256 | 1ed98fab03e3439048c75add8669e73909774ae0fabbf5c52995806aa70143d2 |
| Final runtime DDS SHA-256 | 8ee8e9178461da4298da1ee453e92b98d4a6323f29262975481bc5d6fda0af9a |
| DDS roundtrip | Pixel-exact to the processed PNG; one-level uncompressed 32-bit BGRA; alpha is fully opaque. |

The review-plan alternative allowed a sharp upper-right crop of the existing image. The selected crop excludes the blurred paper stacks and keeps the guard and gathered crowd. The before-and-after comparison is docs/assets/gfx_fix_reports_2026-10/contact_sheets/008_tensions_rising_before_after.png, and the full processing and DDS record is docs/assets/gfx_fix_reports_2026-10/notes/008_tensions_rising/dds_validation.json.

## Handoff

The main agent can keep the current sprite definition and consume gfx/event_pictures/008_tensions_rising/news_event_tensions_red_line.dds through interface/008_tensions_rising_event_images.gfx. No GFX file was edited.

Permanent source, before/after comparison and DDS evidence are retained in `docs/plans/gfx_fix_2026-10/evidence/008/`.
The assigned finding is implemented without a substitute image or omitted asset.

Consumer audit: this news sprite has no current event or GUI consumer; Event 008 country reports use GFX_report_event_tensions_rising.
The corrected 397x153 image remains a registered reserve pending the requested disposition.
There is no live Red Line news popup to test; the permanent native before/after sheet proves the crop without inventing a new popup.

Skills used: event-assets, subagents, shared-git-commit.
