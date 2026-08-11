# Event 005 Icon Regeneration Specialists Handoff

## Scope

This package replaces only the 18 Event 005 UWR/KMB decision DDS files and 2 Event 005 idea/national-spirit DDS files assigned to this specialist pass.

All 20 assets use one distinct built-in ImageGen generation call each, the flat `#00ff00` chroma-key workflow, `remove_chroma_key.py`, exact native canvases, and the repository DDS converter.

No `.gfx`, gameplay, localisation, focus, decision, or idea source file was edited.

## Existing wiring to preserve

Decision sprites remain in `interface/005_soviet_collapse_uwr_kmb_icons.gfx`.

Idea sprites remain in `interface/005_soviet_collapse.gfx`.

Runtime filenames and sprite names below are unchanged.

## Decision runtime handoff

| Consumer | Sprite | Runtime DDS | Size | Evidence |
| --- | --- | --- | ---: | --- |
| `uwr_authorize_field_release_raids` | `GFX_decision_005_uwr_authorize_field_release_raids` | `gfx/interface/decisions/005_soviet_collapse/decision_005_uwr_authorize_field_release_raids.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `uwr_dismantle_captured_blacksite` | `GFX_decision_005_uwr_dismantle_captured_blacksite` | `gfx/interface/decisions/005_soviet_collapse/decision_005_uwr_dismantle_captured_blacksite.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `uwr_expand_experiment_camp_registry` | `GFX_decision_005_uwr_expand_experiment_camp_registry` | `gfx/interface/decisions/005_soviet_collapse/decision_005_uwr_expand_experiment_camp_registry.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `uwr_exploit_captured_blacksite` | `GFX_decision_005_uwr_exploit_captured_blacksite` | `gfx/interface/decisions/005_soviet_collapse/decision_005_uwr_exploit_captured_blacksite.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `uwr_intake_prisoner_transports` | `GFX_decision_005_uwr_intake_prisoner_transports` | `gfx/interface/decisions/005_soviet_collapse/decision_005_uwr_intake_prisoner_transports.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `uwr_overclock_blacksite_network` | `GFX_decision_005_uwr_overclock_blacksite_network` | `gfx/interface/decisions/005_soviet_collapse/decision_005_uwr_overclock_blacksite_network.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `uwr_secure_captured_blacksite` | `GFX_decision_005_uwr_secure_captured_blacksite` | `gfx/interface/decisions/005_soviet_collapse/decision_005_uwr_secure_captured_blacksite.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_deepen_subsoil_extraction` | `GFX_decision_005_kmb_deepen_subsoil_extraction` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_deepen_subsoil_extraction.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_sell_coal_for_machines` | `GFX_decision_005_kmb_sell_coal_for_machines` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_sell_coal_for_machines.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_open_export_auction` | `GFX_decision_005_kmb_open_export_auction` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_open_export_auction.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_sign_resource_treaty` | `GFX_decision_005_kmb_sign_resource_treaty` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_sign_resource_treaty.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_trade_oil_for_trucks` | `GFX_decision_005_kmb_trade_oil_for_trucks` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_trade_oil_for_trucks.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_force_mining_concession` | `GFX_decision_005_kmb_force_mining_concession` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_force_mining_concession.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_integrate_conquered_basin` | `GFX_decision_005_kmb_integrate_conquered_basin` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_integrate_conquered_basin.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_establish_concession_authority` | `GFX_decision_005_kmb_establish_concession_authority` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_establish_concession_authority.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_establish_resource_corridor` | `GFX_decision_005_kmb_establish_resource_corridor` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_establish_resource_corridor.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_accept_machine_tool_bid` | `GFX_decision_005_kmb_accept_machine_tool_bid` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_accept_machine_tool_bid.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |
| `kmb_accept_armaments_bid` | `GFX_decision_005_kmb_accept_armaments_bid` | `gfx/interface/decisions/005_soviet_collapse/decision_005_kmb_accept_armaments_bid.dds` | 33x32 | `manifest.json` and `validation/qa_report.json` |

## Idea / national-spirit runtime handoff

| Consumer | Sprite | Runtime DDS | Size | Evidence |
| --- | --- | --- | ---: | --- |
| `uwr_experimental_warfare_republic` | `GFX_idea_uwr_experimental_warfare_republic` | `gfx/interface/ideas/005_soviet_collapse/idea_005_uwr_experimental_warfare_republic.dds` | 60x68 | `manifest.json` and `validation/qa_report.json` |
| `kmb_subsoil_quota_state` | `GFX_idea_kmb_subsoil_quota_state` | `gfx/interface/ideas/005_soviet_collapse/idea_005_kmb_subsoil_quota_state.dds` | 60x68 | `manifest.json` and `validation/qa_report.json` |

## QA

`validation/qa_report.json` records the source, processed, evidence DDS, runtime DDS, and decoded round-trip hashes for all 20 assets.

All 20 DDS files passed the legacy 128-byte header, 32-bit BGRA mask, texture-cap, exact-length, native-dimension, alpha-range, transparent-corner, and decoded round-trip checks.

The three detailed contact sheets compare native ImageGen source, processed alpha PNG, enlarged smooth native preview, and decoded DDS round-trip:

- `contact_sheets/decisions_uwr_contact_sheet.png`
- `contact_sheets/decisions_kmb_contact_sheet.png`
- `contact_sheets/ideas_contact_sheet.png`

`contact_sheets/overview_contact_sheet.png` provides the compact all-asset overview.

## Review state

Production is complete with no fallback, copied art, overlay-derived art, recolour, filter, primitive local drawing, or resized unrelated source.

Parent visual review of the contact sheets remains the normal final acceptance gate.
