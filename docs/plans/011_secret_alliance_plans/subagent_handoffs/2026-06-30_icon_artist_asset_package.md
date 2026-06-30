# Event 011 Secret Alliance icon-artist handoff

Scope completed:
- Decision category icon
- Five decision icons
- Five idea icons
- Eight achievement icon triplets
- Three small animated sprite packages with static fallbacks

Changed files:
- `docs/assets/011_secret_alliance/build_assets.py`
- `docs/assets/011_secret_alliance/manifest.md`
- `docs/assets/011_secret_alliance/gfx_handoff.md`
- `docs/assets/011_secret_alliance/prompts/generated_prompts.md`
- `docs/assets/011_secret_alliance/source_png/*`
- `docs/assets/011_secret_alliance/processed_png/*`
- `docs/assets/011_secret_alliance/contact_sheets/*`
- `docs/assets/011_secret_alliance/animations/secret_alliance_hidden_seal/*`
- `docs/assets/011_secret_alliance/animations/secret_alliance_evidence_meter_highlight/*`
- `docs/assets/011_secret_alliance/animations/secret_alliance_crisis_frame/*`
- `gfx/interface/decisions/011_secret_alliance/*`
- `gfx/interface/ideas/011_secret_alliance/*`
- `gfx/interface/animated/011_secret_alliance/*`
- `gfx/achievements/sa_*.dds`

Sprite names and sizes:
- `GFX_decision_category_secret_alliance` -> `32x32`
- `GFX_decision_secret_alliance_investigate` -> `32x32`
- `GFX_decision_secret_alliance_security` -> `32x32`
- `GFX_decision_secret_alliance_split` -> `32x32`
- `GFX_decision_secret_alliance_border_watch` -> `32x32`
- `GFX_decision_secret_alliance_confront` -> `32x32`
- `GFX_idea_secret_alliance_friction` -> `64x64`
- `GFX_idea_secret_alliance_bureau` -> `64x64`
- `GFX_idea_secret_alliance_prepared_network` -> `64x64`
- `GFX_idea_secret_alliance_exposed_member` -> `64x64`
- `GFX_idea_secret_alliance_patron_shield` -> `64x64`
- `GFX_secret_alliance_hidden_seal` / `GFX_secret_alliance_hidden_seal_animated` -> `36x36` frames, `288x36` sheet, `8` frames
- `GFX_secret_alliance_evidence_meter_highlight` / `GFX_secret_alliance_evidence_meter_highlight_animated` -> `36x36` frames, `288x36` sheet, `8` frames
- `GFX_secret_alliance_crisis_frame` / `GFX_secret_alliance_crisis_frame_animated` -> `36x36` frames, `288x36` sheet, `8` frames

Source mode:
- Static transparent icons: generated through built-in `image_gen` on flat chroma-key backgrounds, then alpha-cleaned locally.
- Achievement icons: generated full-frame square artwork.
- Animated sprites: generated as real `4x2` eight-frame source sheets, then sliced into per-frame source PNGs and rebuilt into HOI4 horizontal sheets.

Validation:
- Verified representative processed PNG sizes: `32x32`, `64x64`, `36x36`, and `288x36`.
- Verified representative DDS sizes with Pillow: decision, idea, achievement, static animated fallback, and animated sheet.
- Review contacts: `docs/assets/011_secret_alliance/contact_sheets/secret_alliance_icons_contact.png`, `secret_alliance_achievements_contact.png`, `secret_alliance_animation_statics_contact.png`.

Risks / uncertainty:
- `secret_alliance_evidence_meter_highlight` is a compact highlight marker rather than a long meter strip because the parent handoff did not provide exact scripted-GUI meter geometry.
- No `.gfx` or `.gui` files were touched. The parent still needs to wire all listed sprites.
