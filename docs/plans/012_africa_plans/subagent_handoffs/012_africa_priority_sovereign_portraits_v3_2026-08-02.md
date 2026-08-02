# Event 12 Africa sovereign portraits v3 handoff — 2026-08-02

## Disposition

Installed as a runtime asset refresh and kept promotion-gated. This handoff supersedes the v2 visual description for the sixteen priority sovereign identities. It does not change country tags, cosmetic identities, character identifiers, `.gfx` registrations, gameplay files, focus loading, or model surfaces.

## Runtime contract

The sixteen stable sprite names and DDS paths remain unchanged:

`gfx/leaders/012_africa/priority_members/portrait_012_africa_priority_<asset>_sovereign.dds`

The refreshed set covers `asante`, `oyo`, `sokoto`, `kanem_bornu`, `manden`, `kongo`, `buganda`, `aksum`, `harar`, `kilwa`, `nubia`, `luba`, `lunda`, `great_zimbabwe`, `merina`, and `zulu`. The Event 006 niche carriers remain the only tag carriers; no Event 012 tag or cosmetic carrier was added.

## Visual direction and review

Each portrait is a single decorated African king or queen in a restrained HOI4 painted treatment: simple woven or draped regalia, bounded bead/metal adornment, readable facial silhouette, and one flat matte background. The v3 pass removes council/delegation compositions, modern props, text, gore, scenic settings, and sacred-object motifs. The set remains fantastical through material, colour, silhouette, and sovereign styling without caricaturing African identities. No portrait is used to imply forced migration or a collective institution.

The source masters, processed PNGs, DDS conversion inputs, decoded DDS review images, v3 prompt records, and contact sheets are retained under the ignored asset workspace:

- `docs/assets/012_africa_priority_portraits/source_generated_v3/`
- `docs/assets/012_africa_priority_portraits/processed_png_v3/`
- `docs/assets/012_africa_priority_portraits/final_dds_v3/`
- `docs/assets/012_africa_priority_portraits/decoded_v3/`
- `docs/assets/012_africa_priority_portraits/comparison_v3/`
- `docs/assets/012_africa_priority_portraits/prompts_v3/sovereign_v3_prompt_records.md`
- `docs/assets/012_africa_priority_portraits/metadata_v3/processing.json`

## Conversion evidence

- 16 source masters, 16 processed PNGs, 16 final DDS inputs, and 16 decoded-DDS review images were produced.
- Every processed PNG is 156×210 RGBA with opaque alpha (`255..255`); the DDS header review reports `DDS `, 156×210, and 131,168 bytes for each runtime file.
- The 16 stable runtime DDS files match their corresponding v3 conversion outputs byte-for-byte. The runtime files are the only tracked files changed by the asset pass.
- The v3 decoded contact sheet was reviewed for plain matte backgrounds, single-sovereign composition, readable silhouettes, and removal of the earlier council/scenic/sacred-object treatment.

## Remaining boundaries

This refresh supplies portraits only. The 16 model-required visual rows remain deferred and no 3D unit/model files were created. Portrait recruitment still requires the existing package promotion, ratification, carrier provenance, and gameplay acceptance gates. Native-speaker review of the two requested Afaan Oromoo flavour strings remains unresolved and is unrelated to these visuals.
