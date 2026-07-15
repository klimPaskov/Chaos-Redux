# Event 006 Brittany portrait manifest

## Scope

This package supplies the two Event 006 `BRI`-specific human portrait hooks. The accepted vanilla Breton political leaders and advisors remain on their official Hearts of Iron IV portraits. The normal Brittany flag family is the vanilla Gwenn-ha-du family and requires no duplicate mod files.

## Final assets

| Use | Source | Processed PNG | Final DDS | Sprite | SHA-256 |
|---|---|---|---|---|---|
| Fictional civic federalist Tangi Kerbrat | `source_png/portrait_BRI_independence_wave_civic_leader_source.png` | `processed_png/portrait_BRI_independence_wave_civic_commission.png` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_civic_commission.dds` | `GFX_portrait_BRI_independence_wave_civic_commission` | `64AE374585C2A8B3A26BBD9A1E8880E182FDAFA93540BFB84E6C6D87647AB6B4` |
| Fictional coastal commandant Jodoc Tanet | `../source_png/generated_nwe/registered_command_portraits/portrait_BRI_territorial_defence_commander_source.png` | `processed_png/portrait_BRI_independence_wave_coastal_commandant.png` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant.dds` | `GFX_portrait_BRI_independence_wave_coastal_commandant` | `F1603D707170002E7729C535E6DDD990CDFCC7E03F221684E1E6C821F12366C1` |
| Jodoc Tanet army-small dossier | Same source as above | `processed_png/portrait_BRI_independence_wave_coastal_commandant_small.png` | `gfx/leaders/006_independence_wave/portrait_BRI_independence_wave_coastal_commandant_small.dds` | `GFX_portrait_BRI_independence_wave_coastal_commandant_small` | `12C1A20D2CC1234895E7AF557BDA9BAF7CDCA58593527194B5EDAD3AF058684` |

Source SHA-256 values:

- Tangi Kerbrat ImageGen source: `A0A11A95778E3CA3BD32D731B739BC05AE9272BADC5126D8EC11F72D3D252522`
- Jodoc Tanet ImageGen source: `36649988955A9DAAE3192EA27FA4252105F7C6B10272E651D9968F67A0972D2E`

Sprite registration is in `interface/006_independence_wave_brittany_portraits.gfx`.

## Generation and processing record

The civic portrait was generated with OpenAI ImageGen on 2026-07-15 as one invented Breton civilian administrator. The brief required one person only, a sober late-1930s civic suit, Atlantic port context, a discreet ermine-pattern lapel pin, no real-person resemblance, and HOI4 oil-painted portrait treatment. The generated original remains in the Codex image store and a frozen copy is preserved in this package.

The exact civic prompt is preserved in `prompt.md`.

The coastal commandant source was independently generated with ImageGen for the northern and western European registered-command roster. It depicts one invented territorial officer and is retained without identity claims.

Both large portraits were processed with `.tools/process_hoi4_portrait.py` at
156 by 210. The commander small portrait is an independently composed `65x67`
dossier card produced from the approved source with
`.tools/process_hoi4_portrait.py advisor`, crop `[240, 80, 940, 940]`, and the
approved frame and paper overlays. `.tools/convert_to_dds.py` produced the
uncompressed DDS export, and the DDS was decoded back to PNG for verification.
The complete correction record and retained final DDS are in
`../army_small_dossier_correction_2026_07_15/`.

Visual review sheets:

- `review_sheets/portrait_BRI_independence_wave_civic_commission_review.png`
- `review_sheets/portrait_BRI_independence_wave_coastal_commandant_review.png`

Decoded DDS checks:

- `decoded_dds/portrait_BRI_independence_wave_civic_commission_decoded.png`
- `decoded_dds/portrait_BRI_independence_wave_coastal_commandant_decoded.png`
- `decoded_dds/portrait_BRI_independence_wave_coastal_commandant_small_decoded.png`

Combined decoded-runtime contact sheet:

- `contact_sheets/006_bri_runtime_portraits_contact_sheet.png`

The two large-portrait review sheets and the corrected dossier card were
visually approved on 2026-07-15. The civic slot is a distinctive single human
portrait. The earlier four-person institutional image is not wired to the
package.

Exact sprite-to-consumer wiring is recorded in `gfx_handoff.md`.

## Rights and research limitation

François Debeauvais is not represented. The available 1928 group source is weak and the sharper 1932 to 1933 candidates do not have a defensible United States public-domain basis. No Debeauvais DDS or sprite was created, and no unrelated real person was substituted. This is a rights blocker for any future request to add him as a named human leader.

## Reused visual assets

- Vanilla `BRI` Gwenn-ha-du flags for all standard sizes and ideologies.
- Vanilla official portraits for Yann-Morvan Gefflot, Morvan Marchal, Olier Mordrel, and Maurice Duhamel. The Event 006 package selects no fascist route, so Olier Mordrel is never installed by package logic.
- Vanilla official generic advisor dossier sprites for the existing `BRI` advisor roster.
- Existing Event 006 focus and decision icons. No new icon DDS is required by this package.
