# Event 021 generated event-art handoff

> **Current status.** This original production handoff is retained for provenance. The current `interface/021_random_civil_war.gfx` contains the report, news, and category sprite registrations, and the referenced runtime files resolve. User live-session consumer validation remains pending.

## Handoff status

The original handoff recorded all four requested static non-portrait assets as complete and ready for parent-owned `.gfx` registration.

The worker did not edit gameplay, localisation, decisions, events, AI, workbook, GUI, or interface GFX files.

The original parent action was to review the contact sheet and add the sprite definitions in the suggested target GFX file; current source wiring has since been recorded in `interface/021_random_civil_war.gfx`.

## Runtime assets — original handoff snapshot

| Asset ID | Final DDS path | Sprite name | Target `.gfx` | Target canvas | Use notes |
| --- | --- | --- | --- | --- | --- |
| `report_event_021_random_civil_war_opening` | `gfx/event_pictures/021_random_civil_war/report_event_021_random_civil_war_opening.dds` | `GFX_report_event_021_random_civil_war_opening` | `interface/021_random_civil_war_event_pictures.gfx` | `210x176` | Opening report card; generated rail-yard barracks-gate rupture with divided formations and civilians. |
| `news_event_021_multi_front_war` | `gfx/event_pictures/021_random_civil_war/news_event_021_multi_front_war.dds` | `GFX_news_event_021_multi_front_war` | `interface/021_random_civil_war_event_pictures.gfx` | `397x153` | Multi-front news strip; grayscale period junction scene with distinct armed groups at foreground, bridge, and station-square positions. |
| `news_event_021_global_fracture` | `gfx/event_pictures/021_random_civil_war/news_event_021_global_fracture.dds` | `GFX_news_event_021_global_fracture` | `interface/021_random_civil_war_event_pictures.gfx` | `397x153` | Global Fracture news strip; grayscale single international-station scene with displaced civilians, military columns, border inspection, and delegations. |
| `decision_category_picture_021_civil_war` | `gfx/interface/decisions/021_random_civil_war/decision_category_picture_021_civil_war.dds` | `GFX_decision_cat_picture_021_civil_war` | `interface/021_random_civil_war_event_pictures.gfx` | `114x101` | Static category `picture` field art; opaque sepia rail-signal, torn-standard, barricade, and divided-command composition. |

## Ready-to-copy sprite definitions — historical proposal

```text
spriteTypes = {
	spriteType = {
		name = "GFX_report_event_021_random_civil_war_opening"
		texturefile = "gfx/event_pictures/021_random_civil_war/report_event_021_random_civil_war_opening.dds"
	}
	spriteType = {
		name = "GFX_news_event_021_multi_front_war"
		texturefile = "gfx/event_pictures/021_random_civil_war/news_event_021_multi_front_war.dds"
	}
	spriteType = {
		name = "GFX_news_event_021_global_fracture"
		texturefile = "gfx/event_pictures/021_random_civil_war/news_event_021_global_fracture.dds"
	}
	spriteType = {
		name = "GFX_decision_cat_picture_021_civil_war"
		texturefile = "gfx/interface/decisions/021_random_civil_war/decision_category_picture_021_civil_war.dds"
	}
}
```

The category picture sprite intentionally follows the established Chaos Redux `GFX_decision_cat_picture_*` naming pattern for the larger decision-category picture family.

The report and news sprites intentionally follow the established event-scoped `GFX_report_event_*` and `GFX_news_event_*` naming patterns.

## Evidence paths

The manifest is at `docs/assets/021_random_civil_war/manifest.md`.

The prompt records are under `docs/assets/021_random_civil_war/prompts/`.

The untouched ImageGen source masters are under `docs/assets/021_random_civil_war/source_png/`.

The processed PNG previews are under `docs/assets/021_random_civil_war/processed_png/`.

The evidence DDS copies are under `docs/assets/021_random_civil_war/final_dds/`.

The review contact sheet is `docs/assets/021_random_civil_war/contact_sheets/021_random_civil_war_static_art_contact_sheet.png`.

The validation facts and hashes are recorded in the manifest.

## Historical parent-owned integration note — superseded

At the original handoff checkpoint, the checkout did not contain exact Event 021 runtime event or decision-category identifiers for these working asset IDs, so the parent was asked to bind the four stable sprite names to the final implemented consumers. The current GFX file uses `GFX_decision_category_picture_021_civil_war` for the category picture, while the ready-to-copy block above retains the original proposed `GFX_decision_cat_picture_021_civil_war` name for provenance.

The proposed GFX target is `interface/021_random_civil_war_event_pictures.gfx`, following the event-specific pattern used by the existing Event 020 event-picture registry.

If the parent deliberately keeps category-picture registrations in the existing shared registry, the category sprite can instead be placed in `interface/chaosx_decision_category_pictures.gfx` without changing its sprite name or texture path.

No runtime reference points into `docs/assets/`.

## Review and validation

The canonical report, news, and decision-category-picture families were inspected before generation.

The category-picture consumer was inspected in installed Vanilla `interface/countrydecisionview.gui`, Vanilla `interface/decisions.gfx`, the relevant Vanilla decision-category consumer, and the Chaos Redux category-picture registry.

The report preview passed the report-card checks for exact dimensions, transparent corners, soft tilt, readable crop, and no hard photo clipping.

Both news previews passed exact dimensions, opaque alpha, and grayscale treatment.

The category preview passed exact `114x101` dimensions and opaque alpha.

All four DDS outputs passed strict legacy-header, exact-length, declared-dimension, alpha-range, and decoded round-trip checks.

No fallback removal, source substitution, or optional route art was used.
