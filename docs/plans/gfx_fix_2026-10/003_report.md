# Event 003 Holy Realm report-photo repair

This is the photo-only section for the combined Event 003 report. The icons are owned by the separate icon worker and are not covered here.

## Accepted result

The former arhat and buddha report textures had the same SHA-256 as the refuge image and showed the same Potala Palace scene. They now use distinct staged documentary photographs: an anonymous monastic assembly in a hermitage cell and an anonymous crowd at a palace-courtyard ceremony. The parent reviewed the before-and-after sheet and accepted both photos on 2026-10-06.

## Photo assets

| Sprite | Prior runtime DDS SHA-256 | Selected source | Processed card | Final runtime DDS | Target .gfx |
| --- | --- | --- | --- | --- | --- |
| GFX_report_event_holy_realm_arhat | d2a3cc142aff30b65e6ca0b2a80dd851a17bae9b8b10c8b1d21ff8a1a2844978 | source_png/003_holy_realm/report_event_holy_realm_arhat_source.png; generated candidate exec-ab1a15bb-f561-478f-aca9-b84afc96b85d | processed_png/003_holy_realm/report_event_holy_realm_arhat.png | gfx/event_pictures/003_holy_realm/report_event_holy_realm_arhat.dds | interface/003_holy_realm.gfx |
| GFX_report_event_holy_realm_buddha | d2a3cc142aff30b65e6ca0b2a80dd851a17bae9b8b10c8b1d21ff8a1a2844978 | source_png/003_holy_realm/report_event_holy_realm_buddha_source.png; generated candidate exec-dca15c96-142e-470c-b7e7-27973a822b59 | processed_png/003_holy_realm/report_event_holy_realm_buddha.png | gfx/event_pictures/003_holy_realm/report_event_holy_realm_buddha.dds | interface/003_holy_realm.gfx |

Both full-canvas source photographs are 1536x1024 RGB with consumer_opaque backgrounds. The shared processor creates exactly 210x176 RGBA report cards with sepia tone, slight tilt, a thin edge, soft shadow, and transparent outer corners. The repository-standard DDS converter produced distinct one-level uncompressed BGRA textures, and both decoded DDS files match their processed PNGs pixel-for-pixel.

The selected scene prompts, generation rationale, original DDS backups, source and output hashes, alpha evidence, roundtrip checks, and before-and-after sheet are in docs/assets/gfx_fix_reports_2026-10/prompts/003_holy_realm_prompts.md, docs/assets/gfx_fix_reports_2026-10/notes/003_holy_realm/dds_validation.json, and docs/assets/gfx_fix_reports_2026-10/contact_sheets/003_holy_realm_before_after.png.

## Handoff boundary

These two report photos are complete for parent-owned wiring. The final Event 003 report should combine this section with the icon worker's separate package and should preserve the distinction between photo and icon ownership.

## Final static-icon integration

All fifteen assigned static/decision-use findings are addressed by fourteen DDS outputs.
The static 34x34 lotus serves the five concentration rows; the former 96px animated decision consumer is removed from those rows and the unused strip remains registered as a reserve.
Nine transparent 34x34 gold glyphs replace the opaque power and teaching thumbnails.
The two dedicated 72x88 BoP images preserve the lantern/letter and book/bomb motifs with 3px margins, and the two category images are 52x40.
The three existing BoP/doctrine sprite definitions point to those event-owned final paths, without changing any focus icon.
Five missing flag labels found by script_validate were localized; the post-check reports zero diagnostics, while argument/helper coverage remains partial.
Permanent source, lineage, native/contrast, strict DDS and round-trip proof is under evidence/003/.
No assigned art row is omitted; the large unused animation is not presented as a live GUI feature.

Orchestrator live check: use a fresh 1936 Holy Realm country, open Bodhisattva concentration decisions and inspect Begin Concentration Sequence plus Hold Intention/Energy/Mind/Investigation.
The bright 34px lotus must stay inside its 41px row, with no square background or neighboring-row overlap.
Open the Buddha powers and teaching decisions: their gold glyphs must have transparent unused canvas.
Open the Final Doctrine BoP: both 72px side icons must remain clear of the bar frame; check the two bespoke category headings and that the five requirement tooltips show prose rather than flag IDs.
Display Arhat and Buddha reports: their sepia pictures must be distinct from Refuge.

Skills used: event-assets, imagegen, decisions-missions, events writing guidance, subagents, shared-git-commit.
