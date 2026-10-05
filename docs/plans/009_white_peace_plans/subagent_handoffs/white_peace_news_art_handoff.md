# Event 009 White Peace News Art Handoff

Status: Asset production and Event 009 owner GFX/event integration are complete. Native-size preview review found no visual defect. Live news-window presentation and root-parent review remain unverified.

The generated alternate-history news photograph shows two separate 1930s-style army detachments lowering rifles and returning toward their own previous earthwork positions, with the old checkpoint road between them. The final image is a full-canvas opaque monochrome `397x153` PNG/DDS pair.

## Produced files

- Source PNG: `docs/assets/009_white_peace/source_png/news_event_009_white_peace_source.png`.
- Exact generation prompt: `docs/assets/009_white_peace/prompts/news_event_009_white_peace.txt`.
- Processed native-size preview: `docs/assets/009_white_peace/processed_png/news_event_009_white_peace.png`.
- DDS-decoded round-trip PNG: `docs/assets/009_white_peace/roundtrip/news_event_009_white_peace_dds_roundtrip.png`.
- Round-trip QA record: `docs/assets/009_white_peace/notes/dds_roundtrip.md`.
- Manifest: `docs/assets/009_white_peace/manifest.md`.
- GFX handoff: `docs/assets/009_white_peace/gfx_handoff.md`.
- Final runtime DDS: `gfx/event_pictures/009_white_peace/news_event_009_white_peace.dds`.

## Prompt and provenance

The exact prompt is stored at `docs/assets/009_white_peace/prompts/news_event_009_white_peace.txt` and the selected source candidate is the native ImageGen output copied from `C:/Users/klimp/.codex/generated_images/01a10d38-2a70-76c2-a7c2-9f4730e27149/exec-f6aa9284-523f-4b66-be65-9c0523258733.png`.

Source mode is `generated`; this no-gain armistice scene is alternate history and cannot be represented by an authentic archival photograph. The selected source is RGB `2019x779`, with no alpha channel, and its SHA-256 is `6D45B5D95C31F7F6AA86E7AD38C1C3A2C36F02CD59A523AB6A52FB44B9537481`.

The canonical news-event reference family was inspected at `.agents/skills/chaos-redux-event-assets/assets/gfx_references/event_art/news/`, including its contact sheet and `news_event_004.png`; references guided canvas and monochrome documentary treatment only.

## QA and identifiers

The processed preview is `397x153` RGB with SHA-256 `6A6C2389E7F26C1AEFE31D1E4E24651911D03EB1854165155A0474FABFC1DFF3`.

The runtime DDS passed the legacy BGRA header and dimension checks at `397x153`; its file size is `243092` bytes, alpha is fully opaque `(255,255)`, and its decoded pixels match the processed PNG exactly. Runtime DDS SHA-256 is `CC342B4AFEF77C62BD94D15FF157977A309205AD62487A380C014416B3346E85`.

Changed asset identifier: `news_event_009_white_peace`; sprite identifier: `GFX_news_event_009_white_peace`.

Target registry: `interface/009_white_peace_event_images.gfx`; the sprite resolves to the final DDS and news events `chaosx.nr9.7` through `.10` consume it with `major = yes`.

A contact sheet was not produced because this package contains one requested image and no retained alternatives; the asset skill requires a sheet for packages containing many images.

The repository root `.gitignore` excludes `docs/assets/` at line 80, so this evidence package is present in the shared workspace but absent from ordinary `git status`; the parent can decide whether to retain it as temporary review evidence or force-add selected files.

No asset-production simplifications or content blockers remain. The event-window render is unavailable, so the parent and user retain the final runtime visual review.
