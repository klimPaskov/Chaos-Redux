# System Camp Repression Rework Report and Super-Event GFX Handoff

## Handoff result

All 17 runtime DDS files exist at the exact paths listed below. The shared working tree already contains matching sprite definitions:

- report sprites in `interface/camp_repression_rework.gfx`;
- super-event sprites in `interface/chaosx_super_events.gfx`.

This asset worker did not edit either `.gfx` file. The definitions were read back after asset production and currently resolve to the delivered DDS paths.

## Report-event sprites

| Stable sprite ID | Live consumer or package role | Runtime DDS path | Dimensions | Current GFX file | Wiring disposition |
| --- | --- | --- | ---: | --- | --- |
| `GFX_report_event_auschwitz_discovery` | Auschwitz evidence discovery in `chaosx_genocide.56` | `gfx/event_pictures/system_camp_repression_rework/report_event_auschwitz_discovery.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and consumed by `events/genocide_crisis_events.txt`. |
| `GFX_report_event_pingfang_authority` | `events/japan_ishii.txt`, `japan_ishii.1` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_authority.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_kwantung_medical_bypass` | `events/japan_ishii.txt`, `japan_ishii.2` | `gfx/event_pictures/system_camp_repression_rework/report_event_kwantung_medical_bypass.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_pingfang_outbreak` | `events/japan_ishii.txt`, `japan_ishii.3` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_outbreak.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_pingfang_discovery` | `events/japan_ishii.txt`, `japan_ishii.4` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_discovery.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_pingfang_retreat` | `events/japan_ishii.txt`, `japan_ishii.5` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_retreat.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_pingfang_tribunal` | `events/japan_ishii.txt`, `japan_ishii.6` | `gfx/event_pictures/system_camp_repression_rework/report_event_pingfang_tribunal.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_soviet_famine_warning` | `events/soviet_gulag.txt`, `soviet_gulag.1` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_famine_warning.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_soviet_famine_crisis` | `events/soviet_gulag.txt`, `soviet_gulag.2` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_famine_crisis.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_soviet_administrative_breakdown` | `events/soviet_gulag.txt`, `soviet_gulag.3` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_administrative_breakdown.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_soviet_famine_relief` | `events/soviet_gulag.txt`, `soviet_gulag.4` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_famine_relief.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |
| `GFX_report_event_soviet_records_discovered` | `events/soviet_gulag.txt`, `soviet_gulag.5` | `gfx/event_pictures/system_camp_repression_rework/report_event_soviet_records_discovered.dds` | `210x176` | `interface/camp_repression_rework.gfx` | Registered and referenced. |

## Super-event sprites

| Visible slot | Stable sprite ID | Runtime DDS path | Dimensions | Current GFX file | Wiring disposition |
| ---: | --- | --- | ---: | --- | --- |
| `12` | `GFX_super_event_angel_directorate` | `gfx/super_events/system_camp_repression_rework/super_event_angel_of_death_directorate_revolt.dds` | `457x328` | `interface/chaosx_super_events.gfx` | Existing sprite path currently points to the delivered replacement art. Do not create a duplicate sprite ID. |
| `74` | `GFX_super_event_camp_global_discovery` | `gfx/super_events/system_camp_repression_rework/super_event_global_discovery.dds` | `457x328` | `interface/chaosx_super_events.gfx` | Registered and mapped by `GetSuperEventImage`. |
| `75` | `GFX_super_event_camp_soviet_famine_catastrophe` | `gfx/super_events/system_camp_repression_rework/super_event_soviet_famine_catastrophe.dds` | `457x328` | `interface/chaosx_super_events.gfx` | Registered and mapped by `GetSuperEventImage`. |
| `76` | `GFX_super_event_camp_pingfang_exposure` | `gfx/super_events/system_camp_repression_rework/super_event_pingfang_exposure.dds` | `457x328` | `interface/chaosx_super_events.gfx` | Registered and mapped by `GetSuperEventImage`. |
| `77` | `GFX_super_event_camp_colonial_reckoning` | `gfx/super_events/system_camp_repression_rework/super_event_colonial_reckoning.dds` | `457x328` | `interface/chaosx_super_events.gfx` | Registered and mapped by `GetSuperEventImage`. |

## Germany audit conclusion

`GFX_report_event_auschwitz_discovery` is included. It is the only Germany report identity explicitly required by the accepted major-country package and missing as dedicated art when this pass began.

The dedicated Auschwitz sprite is registered and used by the live `chaosx_genocide.56` discovery event. Other Germany/Mengele events retain their appropriate existing report identities; no package-required Germany report sprite remains unconsumed.

## Parent integration notes

1. Keep every sprite ID and runtime path in the tables stable.
2. Do not add a second `GFX_super_event_angel_directorate` definition; slot `12` already uses that stable ID.
3. Keep slots `74` through `77` mapped to the four `GFX_super_event_camp_*` IDs already present in `GetSuperEventImage`.
4. Decide which dedicated German discovery event should use `picture = GFX_report_event_auschwitz_discovery`. The art and sprite definition are ready.
5. No localisation key is embedded in any image, and no localisation edit is required merely to display these textures.

## Review and validation references

- Manifest: `docs/assets/system_camp_repression_rework/manifest_report_super_event.md`
- Exact prompts: `docs/assets/system_camp_repression_rework/prompts/report_super_event_imagegen_prompts.md`
- Report contact sheet: `docs/assets/system_camp_repression_rework/contact_sheets/report_event_processed_contact_sheet.png`
- Super-event contact sheet: `docs/assets/system_camp_repression_rework/contact_sheets/super_event_processed_contact_sheet.png`
- UI mask previews: `docs/assets/system_camp_repression_rework/contact_sheets/super_event_ui_mask_preview_contact_sheet.png`
- Validation note: `docs/assets/system_camp_repression_rework/validation_report_super_event.md`

## Blockers

No asset-production or runtime-consumer blocker remains.
