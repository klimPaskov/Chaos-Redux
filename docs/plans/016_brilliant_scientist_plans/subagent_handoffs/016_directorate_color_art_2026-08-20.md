# Event 016 Directorate color-art handoff

Date: 2026-08-20

## Scope and disposition

This bounded asset pass gives the accepted 500x360 Kruger Directorate display a stable four-color information hierarchy without adding interface elements or changing gameplay.

The built-in ImageGen source is retained at `docs/assets/016_brilliant_scientist/directorate_ui/color_refresh/source_png/directorate_background_color_source.png` with SHA-256 `AD8A8CDAF8FD6D19958BBD86CB5868C444A84A15DDDCAAF2AFD37CD57A04E99D`.

The prompt record is `docs/assets/016_brilliant_scientist/directorate_ui/color_refresh/prompts/directorate_background_color_source.txt`.

The generated source was processed deterministically into the locked 500x360 layout.
The title, close control, portrait, profile name, status line, and footer use source-derived quiet texture.
The four metric rows use low-strength source-derived color undertones: Mandate deep cyan-navy, Dependence dark amber-umber, Exposure dark crimson-burgundy, and Capacity dark emerald-forest.
No generated text, fake control, fake panel, or interactive geometry was retained inside a safe rectangle.

## Runtime files

The pass changes exactly these runtime DDS files under `gfx/interface/016_brilliant_scientist/directorate/`:

- `directorate_background.dds` — 500x360 — SHA-256 `380F0AF0B9A77D19A692B2A86B8D31D12BC14DA3B297F996A80B61A0F7563534`
- `meter_mandate_low.dds` — SHA-256 `D26841549965D96FDE6B7BE4BF950CA515041DFD6916F42941D04045B2A3A56F`
- `meter_mandate_moderate.dds` — SHA-256 `B9D9B5BFAE8C620D867D6B7F21D7CB17C804F85434CC3A3754B0B103557DF165`
- `meter_mandate_high.dds` — SHA-256 `B9C41B2A327A6C507A0D4F650FECC91AAA98AC03FF40DFB625CADFD563FCE49A`
- `meter_mandate_extreme.dds` — SHA-256 `6CC3FB039FAD8D88D414BD90805F16317871A9292B48AD641F19E9EFA2E1A70A`
- `meter_dependence_low.dds` — SHA-256 `B408EEFA0F114F897CCB1E669540D8BC3829EC2C45B8A10D9182350D11ED1BDD`
- `meter_dependence_moderate.dds` — SHA-256 `50E789CF5EBB9EEBA1D64F3104E0CB127C63E0F97FA8BE266F8C439215C61CAA`
- `meter_dependence_high.dds` — SHA-256 `6B5313AF07BBBD87936B29A685465EFCA029626B20E9044BFF2F74918A2AA1EF`
- `meter_dependence_extreme.dds` — SHA-256 `1A668C1F912E0D109232B265B459B554FE90B493AE3B29FB5DDE8B04C9E6F6FE`
- `meter_exposure_low.dds` — SHA-256 `5B3B25088617C01659022B33566C036E49769BB21A2F1884CFF88203203C7A92`
- `meter_exposure_moderate.dds` — SHA-256 `2AAF8A3085BE6D1FF41FD511816C24A236060BA6BC037D6FB1DD07BCDC82AFB9`
- `meter_exposure_high.dds` — SHA-256 `72AC178168EBCE30D0A52A041406344B6508BD63FB8F700E2E6E77827316E478`
- `meter_exposure_extreme.dds` — SHA-256 `EB6381B506C2A770B5D7B7816CA630D1568BA70E92E5C52E588F90432D66310F`
- `meter_capacity_low.dds` — SHA-256 `C2CEB3A47BDCA82954CA7E69B6FF234FA5E53202378F85DD996CBD57EC7994EE`
- `meter_capacity_moderate.dds` — SHA-256 `A16DF1F26952B14512DD6B3494C09F109E6A0DA57B38EEFBF6DA9AE1FD6CF2BC`
- `meter_capacity_high.dds` — SHA-256 `A1F0F5B12DD0300B1DC797CEC6C7BF83FA7F3E7C711451A59D4E17A0826E924D`
- `meter_capacity_extreme.dds` — SHA-256 `C0919D6767EBE35E4B53079394351134BE6F6290A52BECEC301BA75DEFF62C4A`

Every meter remains 112x34 and 15,360 bytes.
Only the fill and its existing tier marker/highlight colors changed; alpha, brass frame, canvas, fill length, and non-fill pixels remain unchanged.

## Visual and format evidence

- Native processed/source/DDS contact sheet: `docs/assets/016_brilliant_scientist/directorate_ui/color_refresh/contact_sheets/color_refresh_native_contact.png`
- Processed background: `docs/assets/016_brilliant_scientist/directorate_ui/color_refresh/processed_png/directorate_background.png`
- Decoded runtime background: `docs/assets/016_brilliant_scientist/directorate_ui/color_refresh/decoded_dds/directorate_background.png`
- Per-file metrics and DDS checks: `docs/assets/016_brilliant_scientist/directorate_ui/color_refresh/evidence/processing_metrics.json`

All seventeen outputs use the repository's one-level uncompressed legacy BGRA DDS layout.
The background is 720,128 bytes and every meter is 15,360 bytes, matching `128 + width * height * 4`.
Decoded runtime pixels match the processed PNGs exactly.

## Parent integration

The existing sprite names and `.gfx` paths remain unchanged, so no sprite registration edit is required.
The GUI/localisation owner must preserve the metric identities in player-facing labels and must review the composed MCP render rather than accepting this isolated asset contact sheet as final layout proof.

## Simplifications, omissions, and blockers

No fallback or placeholder was used.
No animation, extra control, tab, panel, or gameplay surface was added.
Live in-game appearance remains user-owned acceptance; the parent must retain the final MCP scripted-GUI render evidence.
