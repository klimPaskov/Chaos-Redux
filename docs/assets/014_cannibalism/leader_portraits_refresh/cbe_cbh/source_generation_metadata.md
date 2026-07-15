# Event 014 CBE-CBH image-generation provenance

Generation date: 2026-07-15.

All 28 installed CBE-CBH masters are separate fictional portraits created through built-in ImageGen. Each accepted call is preserved verbatim under `prompts/generated/`; each selected output was copied unchanged to its exact `source_png/<stem>_source.png` path before deterministic finishing.

## Style-only references

Every call used the same three canonical vanilla leader portraits for painted finish, restrained framing, and value range only:

- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/ire_eamon_de_valera.png`
- `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/fin_carl_mannerheim.png`

No referenced identity, face, clothing, pose, or insignia was copied. The accepted prompts explicitly require opaque matte oil/gouache, simplified painted facial planes, muted 1930s-1940s values, low photographic microdetail, period material culture, and no modern equipment, prison setting, or living Indigenous sacred motif.

## Generation accounting

- Selected masters: 28.
- First-call selections: 25.
- Persisted visual supersessions: three. The first CBG default and CBG Africa candidates were rejected after native-size comparison because their finish remained too smooth and glossy; both were independently regenerated with a stricter coarse matte-gouache treatment. The first selected CBH Africa candidate was superseded after the whole-set audit found its two-handed tooth-row silhouette too close to CBG South America; the accepted replacement uses one sleeve-pinned charm and a distinct profile pose.
- Total built-in calls: 31.
- Fallbacks: none. No CLI generation, local procedural drawing, sourced-photo substitution, transformed old portrait, alternate model, or reused portrait was accepted.

The per-stem source SHA-256, explicit crop, processor version, output path, and final visual-approval record live in `metadata/`. Package-wide source, processed, review-sheet, documentation, and DDS hashes are recorded in `hashes.sha256`. The final style and action review surfaces are `contact_sheets/cbe_cbf_hoi4_repaint_contact_sheet.png` and `contact_sheets/cbg_cbh_hoi4_repaint_contact_sheet.png`.
