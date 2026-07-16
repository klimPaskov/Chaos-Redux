# Event 006 IW-010 Saar AJX asset completion handoff

Date: `2026-07-15`

Scope: three distinct fictional-human AJX political-advisor dossier cards and
one distinct Municipal Neutral Commission national-focus icon.

Status: `complete_and_wired`. The four runtime DDS files are installed, the
parent-owned live registrations are verified, and no asset-integration blocker
remains. This asset worker did not edit gameplay, localisation, interface,
character, event, focus, readiness-gate, RHI portrait, or BAY portrait files.

## Installed runtime files

| Runtime file | Size | SHA-256 |
| --- | ---: | --- |
| `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds` | `65x67` | `e2a8e4d56c9bd23ded9d07ec48fd3943e9da2a6a88cc0a6a7d8ea3a27d48bd5a` |
| `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds` | `65x67` | `a58836ebcb8c4b2af6dd82b2dda060b1cdf2c40cd18233bf98bdc271c189e22e` |
| `gfx/interface/ideas/006_independence_wave/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds` | `65x67` | `4c7a956a9f45005ac130bb1d6f3e965b3f32ba92237ec238775b445d745b3f80` |
| `gfx/interface/goals/006_independence_wave/goal_independence_wave_ajx_neutral_commission.dds` | `94x86` | `06063478a0d1a4e0cd562e1230f31cfa46eeb718814f11bcb83e86b6c059b613` |

Each runtime DDS is byte-identical to its package mirror, has the expected
uncompressed BGRA header and length, decodes pixel-identically to the processed
PNG, and has fully transparent corners.

## Verified parent-owned live integration

- `common/characters/006_independence_wave_saar_characters.txt`: all three
  approved AJX character keys consume their exact small-portrait handles; the
  two female characters use `gender = female` and the male character uses the
  default.
- `interface/006_independence_wave_region_01_portraits.gfx`: all three advisor
  sprites resolve to the installed DDS paths.
- `localisation/english/006_independence_wave_saar_l_english.yml`: all three
  character keys and descriptions are present.
- `events/006_independence_wave.txt`: AJX setup recruits all three advisors.
- `interface/006_independence_wave.gfx`: the neutral-commission base and shine
  sprites resolve to the installed focus DDS.
- `common/national_focus/006_independence_wave_focus.txt`:
  `independence_wave_ajx_appoint_neutral_commission_focus` consumes the new
  base sprite. The codification, security, and entrenchment nodes retain their
  specific shared Event 006 icons.

## Documentation synchronized by this asset tranche

- `docs/assets/006_independence_wave/manifest.md`;
- `docs/events/006_independence_wave/northern_western_europe_packages.md`;
- this package's `manifest.md`, `gfx_handoff.md`, metadata JSON records,
  validation JSON, checksum ledger, and this handoff.

## Complete package file inventory

The checksum ledger covers every package file below except the ledger itself.

- `ajx_asset_validation_2026_07_15.json`
- `checksums.sha256`
- `contact_sheets/advisor_portraits_decoded_contact_sheet.png`
- `contact_sheets/advisor_portraits_enlarged_nearest_contact_sheet.png`
- `contact_sheets/advisor_portraits_native_contact_sheet.png`
- `contact_sheets/advisor_reviews/advisor_AJX_independence_wave_cross_border_accounts_comptroller_processor_comparison.png`
- `contact_sheets/advisor_reviews/advisor_AJX_independence_wave_factory_security_inspector_processor_comparison.png`
- `contact_sheets/advisor_reviews/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent_processor_comparison.png`
- `contact_sheets/advisor_sources_contact_sheet.png`
- `contact_sheets/ajx_asset_completion_contact_sheet.png`
- `contact_sheets/canonical_all_three/advisor_AJX_independence_wave_cross_border_accounts_comptroller_canonical_all_three.png`
- `contact_sheets/canonical_all_three/advisor_AJX_independence_wave_factory_security_inspector_canonical_all_three.png`
- `contact_sheets/canonical_all_three/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent_canonical_all_three.png`
- `contact_sheets/focus/goal_independence_wave_ajx_neutral_commission_comparison.png`
- `decoded_png/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.png`
- `decoded_png/advisors/advisor_AJX_independence_wave_factory_security_inspector.png`
- `decoded_png/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.png`
- `decoded_png/focus/goal_independence_wave_ajx_neutral_commission.png`
- `final_dds/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.dds`
- `final_dds/advisors/advisor_AJX_independence_wave_factory_security_inspector.dds`
- `final_dds/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.dds`
- `final_dds/focus/goal_independence_wave_ajx_neutral_commission.dds`
- `gfx_handoff.md`
- `handoff.md`
- `manifest.md`
- `metadata/crops/advisor_AJX_independence_wave_cross_border_accounts_comptroller.json`
- `metadata/crops/advisor_AJX_independence_wave_factory_security_inspector.json`
- `metadata/crops/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.json`
- `metadata/focus/goal_independence_wave_ajx_neutral_commission.json`
- `processed_png/advisors/advisor_AJX_independence_wave_cross_border_accounts_comptroller.png`
- `processed_png/advisors/advisor_AJX_independence_wave_factory_security_inspector.png`
- `processed_png/advisors/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent.png`
- `processed_png/focus/goal_independence_wave_ajx_neutral_commission.png`
- `prompts/ajx_asset_prompts.md`
- `source_png/alpha_processed/goal_independence_wave_ajx_neutral_commission_alpha_master.png`
- `source_png/imagegen_raw/advisor_AJX_independence_wave_cross_border_accounts_comptroller_imagegen_raw.png`
- `source_png/imagegen_raw/advisor_AJX_independence_wave_factory_security_inspector_imagegen_raw.png`
- `source_png/imagegen_raw/advisor_AJX_independence_wave_mine_rail_dispatch_superintendent_imagegen_raw.png`
- `source_png/imagegen_raw/goal_independence_wave_ajx_neutral_commission_imagegen_raw.png`
- `visual_review_notes.md`

## Skills, simplifications, and blockers

- Skills used: `chaos-redux-event-assets` and official `imagegen`.
- Skills created or updated: none.
- Simplifications: none.
- Fallbacks: none.
- Missing requested asset outputs: none.
- Asset blockers: none.
- Gameplay readiness and FORM-04 completion remain separate parent-owned Event
  006 concerns and are not claimed by this asset handoff.
- Commit: none, as requested.
