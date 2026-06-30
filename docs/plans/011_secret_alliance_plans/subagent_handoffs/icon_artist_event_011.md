# Event 011 icon artist handoff

Scope: static icon asset package only for Event 011 Secret Alliance.

## Files created

- `docs/assets/011_secret_alliance/source_png/decision_category_secret_alliance_dossier_source.png`
- `docs/assets/011_secret_alliance/source_png/decision_secret_alliance_*.png`
- `docs/assets/011_secret_alliance/source_png/idea_secret_alliance_*.png`
- `docs/assets/011_secret_alliance/source_png/secret_alliance_*_badge_source.png`
- `docs/assets/011_secret_alliance/source_png/secret_alliance_pact_emblem_source.png`
- `docs/assets/011_secret_alliance/source_png/achievement_secret_alliance_*_source.png`
- `docs/assets/011_secret_alliance/processed_png/decision_category_secret_alliance_dossier.png`
- `docs/assets/011_secret_alliance/processed_png/decision_secret_alliance_*.png`
- `docs/assets/011_secret_alliance/processed_png/idea_secret_alliance_*.png`
- `docs/assets/011_secret_alliance/processed_png/secret_alliance_pact_emblem.png`
- `docs/assets/011_secret_alliance/processed_png/secret_alliance_*_badge.png`
- `docs/assets/011_secret_alliance/processed_png/achievement_secret_alliance_*{,_grey,_not_eligible}.png`
- `docs/assets/011_secret_alliance/dds/decision_category_secret_alliance_dossier.dds`
- `docs/assets/011_secret_alliance/dds/decision_secret_alliance_*.dds`
- `docs/assets/011_secret_alliance/dds/idea_secret_alliance_*.dds`
- `docs/assets/011_secret_alliance/dds/secret_alliance_pact_emblem.dds`
- `docs/assets/011_secret_alliance/dds/secret_alliance_*_badge.dds`
- `docs/assets/011_secret_alliance/dds/achievement_secret_alliance_*{,_grey,_not_eligible}.dds`
- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_decision_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_idea_ui_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_achievements_contact.png`
- `docs/assets/011_secret_alliance/prompts/icon_artist_prompts.md`
- `docs/assets/011_secret_alliance/notes/icon_validation.md`
- `docs/assets/011_secret_alliance/manifest.md`
- `docs/assets/011_secret_alliance/gfx_handoff.md`

Final gameplay DDS outputs from this pass:

- `gfx/interface/decisions/secret_alliance/decision_category_secret_alliance_dossier.dds`
- `gfx/interface/decisions/secret_alliance/decision_secret_alliance_*.dds`
- `gfx/interface/ideas/secret_alliance/idea_secret_alliance_*.dds`
- `gfx/interface/secret_alliance/secret_alliance_pact_emblem.dds`
- `gfx/interface/secret_alliance/secret_alliance_*_badge.dds`
- `gfx/achievements/secret_alliance_*{,_grey,_not_eligible}.dds`

## Sprite names

- `GFX_decision_category_secret_alliance_dossier`
- `GFX_decision_secret_alliance_trace_pouches`
- `GFX_decision_secret_alliance_turn_courier`
- `GFX_decision_secret_alliance_radio_net`
- `GFX_decision_secret_alliance_guard_rail`
- `GFX_decision_secret_alliance_harden_plants`
- `GFX_decision_secret_alliance_quiet_talks`
- `GFX_decision_secret_alliance_exit_offer`
- `GFX_decision_secret_alliance_safehouses`
- `GFX_decision_secret_alliance_war_case`
- `GFX_idea_secret_alliance_coldness`
- `GFX_idea_secret_alliance_subversion`
- `GFX_idea_secret_alliance_counter_office`
- `GFX_idea_secret_alliance_public_hostility`
- `GFX_secret_alliance_pact_emblem`
- `GFX_secret_alliance_founder_badge`
- `GFX_secret_alliance_patron_badge`
- `GFX_secret_alliance_wavering_badge`
- Final achievement family pattern after parent review: `GFX_achievement_secret_alliance_<key>{,_grey,_not_eligible}`

## Validation

- Read the requested spec prompt, asset matrix, achievement prompt, and the icon reference folders before generation.
- Used built-in `image_gen` for all source art.
- Used chroma-key removal only for transparent icon families.
- Verified representative final DDS dimensions with `ffprobe`.
- Built three contact sheets for decision icons, idea/UI icons, and achievements.

## Remaining blockers

- `radio pulse`, `seal crack`, and `border warning frame` animated packages were not completed in this pass.
- Reason: to avoid transform-only or inconsistent motion, those assets need a dedicated frame-animation run with real per-frame source art, processed frames, sheet DDS files, preview GIFs, and updated handoff notes.

## Parent follow-up

- Wire the static sprites above in `interface/011_secret_alliance.gfx`.
- Parent copied the imagegen-backed achievement outputs to the achievement-id filenames used by `interface/chaosx_achievements.gfx`.
- Do not treat the omitted Event 011 animated or non-icon surfaces as validated by this handoff.
