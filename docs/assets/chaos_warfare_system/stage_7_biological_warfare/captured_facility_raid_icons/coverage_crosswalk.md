# Requirement-to-runtime coverage crosswalk

| Requirement id | Intended purpose | Source package / manifest entry | Runtime asset | Sprite handoff | Status |
|---|---|---|---|---|---|
| `bio_facility_secure_preserve_raid` | Secure and preserve a captured biological facility; containment, evidence custody, and controlled access | `source_png/bio_facility_secure_preserve_raid_source.png` → `processed_png/bio_facility_secure_preserve_raid.png`; `manifest.md` entry | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_secure_preserve.dds` | `GFX_raid_type_icon_bio_facility_secure_preserve` in `gfx_handoff.md` | handed_off |
| `bio_facility_destroy_safely_raid` | Methodically neutralize a captured biological arsenal chamber while maintaining containment | `source_png/bio_facility_destroy_safely_raid_source.png` → `processed_png/bio_facility_destroy_safely_raid.png`; `manifest.md` entry | `gfx/interface/raids/stage_7_biological_warfare/raid_type_icon_bio_facility_destroy_safely.dds` | `GFX_raid_type_icon_bio_facility_destroy_safely` in `gfx_handoff.md` | handed_off |

The parent agent owns live raid definitions and `.gfx` registration. This package contains the exact final paths and copy-ready sprite entries without editing those consumers.
