# Event 016 Directorate ImageGen art repair handoff

## Scope

This tranche replaces the Event 016 Directorate full background and compact header with native ImageGen-derived artwork while preserving the existing sprite identifiers and live GUI dimensions.

## Runtime files

- `gfx/interface/016_brilliant_scientist/directorate/directorate_background.dds`: `500x620`, SHA-256 `67F61250E94FB09C21BB247C84007F2962ADD93D933817EFA710C71AE5A469CD`, consumed by `GFX_kruger_directorate_background`.
- `gfx/interface/016_brilliant_scientist/directorate/directorate_compact_header.dds`: `500x58`, SHA-256 `F9ADEB2EE628DBBC5FD3F343E3D831930B133259E100932D2B92C43565791624`, consumed by `GFX_kruger_directorate_compact_header`.

No `.gfx` identifiers or GUI consumers changed. The two stable runtime filenames were already registered in `interface/016_brilliant_scientist_directorate.gfx` and consumed by `interface/016_brilliant_scientist_directorate.gui`.

## Source and processing evidence

The fictional laboratory-dossier source was generated with native ImageGen and retained at `docs/assets/016_brilliant_scientist/directorate_ui/source_masters/directorate_background_master_v2.png`, SHA-256 `C748CECBB9D01ABF2B85F8B2D8A8987070D15ECE46F22C8CAA108039B471CF30`. The prompt is retained at `docs/assets/016_brilliant_scientist/directorate_ui/background_refresh/prompts/directorate_background_v2.txt`.

The first processed candidate was rejected because generated machinery entered the accepted profile and content rectangles. The accepted processing preserves the generated frame while clearing the exact live bays with a subdued texture sampled from the same generated field. It does not substitute primitive UI art or reuse the former runtime background.

The reviewed bay map is:

- header `x38-462 y8-65`;
- profile `x38-163 y72-289`;
- telemetry `x169-464 y72-225`;
- government control `x169-464 y228-292`;
- navigation/content `x38-462 y301-542`;
- footer `x38-449 y552-604`.

The accepted contact sheet is `docs/assets/016_brilliant_scientist/directorate_ui/background_refresh/contact_sheets/directorate_background_refresh_contact_sheet.png`, SHA-256 `B2EBFE40F1D9D1203FB1D6808EEA5333A918B73CEB6E3CBC4A1C07D32A4570E2`. The installed DDS files were decoded directly after installation and visually reviewed against the same map.

## Disposition

The two runtime assets are wired and parent-reviewed. No fallback, placeholder, borrowed art, generated text, portrait work, gameplay edit, or additional unwired sprite was introduced. Final live consumer acceptance remains user-owned.
