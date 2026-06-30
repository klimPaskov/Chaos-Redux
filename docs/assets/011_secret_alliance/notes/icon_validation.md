# Event 011 Secret Alliance icon validation

Validation scope: static icons created in the current icon pass only.

## Dimension checks

- `gfx/interface/decisions/secret_alliance/decision_category_secret_alliance_dossier.dds`: `52x40`
- `gfx/interface/decisions/secret_alliance/decision_secret_alliance_trace_pouches.dds`: `32x32`
- `gfx/interface/ideas/secret_alliance/idea_secret_alliance_coldness.dds`: `64x64`
- `gfx/interface/secret_alliance/secret_alliance_founder_badge.dds`: `32x32`
- `gfx/achievements/secret_alliance_open_file.dds`: `64x64`

## Transparency checks

- Decision, idea, emblem, and badge assets were generated on chroma-key backgrounds, stripped to alpha with the built-in imagegen helper, and normalized onto transparent final canvases.
- Contact-sheet spot checks were performed on `decision_secret_alliance_trace_pouches.png`, `decision_secret_alliance_radio_net.png`, `decision_category_secret_alliance_dossier.png`, `idea_secret_alliance_counter_office.png`, and `secret_alliance_pact_emblem.png`.

## Achievement checks

- Completed achievement icons were normalized to `64x64`.
- Grey variants were derived from the imagegen-backed base icons through grayscale conversion.
- Not-eligible variants were derived from the grey variants with centered red cross overlays.
- `secret_alliance_last_signature.png` uses the regenerated imagegen-backed source with blurred signature marks and no readable text.

## Contact sheets

- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_decision_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_idea_ui_icons_contact.png`
- `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_achievements_contact.png`

## Parent animation correction

The icon worker left animation packages blocked during the static icon pass. The parent implementation pass later discarded the earlier frame drafts and rebuilt these packages from imagegen source sheets:

- `secret_alliance_radio_pulse`, 8 frames
- `secret_alliance_thread_glow`, 8 frames
- `secret_alliance_seal_crack`, 10 frames
- `secret_alliance_border_warning`, 8 frames

The rebuilt packages include `source_sheet_imagegen.png`, extracted source frames, processed frames, static fallbacks, horizontal DDS sheets, GIF previews, and the combined contact sheet at `docs/assets/011_secret_alliance/contact_sheets/011_secret_alliance_animation_contact.png`.
