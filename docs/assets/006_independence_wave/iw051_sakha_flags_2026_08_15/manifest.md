# IW-051 Sakha route flag package

This package contains four generated alternate-history route ladders for the
registered `YAK` carrier. They are route-specific cosmetics only; the vanilla
`YAK` base and ideology ladders remain untouched and no no-suffix override is
provided.

The native ImageGen masters are preserved under `source_png/imagegen_raw/`.
Each master contains the usable flag in a documented upper-left rectangle and
an unintended red remainder. `build_flags.py` records the per-route crop and
performs only fixed-palette resizing plus TGA/DDS encoding. The generated art
is not an attested universal 1936 Yakut flag and remains parent-review gated.

| Route | Runtime basenames | Normal | Medium | Small |
| --- | --- | --- | --- | --- |
| Civic constitutional autonomy | `YAK_INDEPENDENCE_WAVE_CIVICX` | `gfx/flags/YAK_INDEPENDENCE_WAVE_CIVICX.tga` | `gfx/flags/medium/YAK_INDEPENDENCE_WAVE_CIVICX.tga` | `gfx/flags/small/YAK_INDEPENDENCE_WAVE_CIVICX.tga` |
| Arctic council and river security | `YAK_INDEPENDENCE_WAVE_ARCTICX` | `gfx/flags/YAK_INDEPENDENCE_WAVE_ARCTICX.tga` | `gfx/flags/medium/YAK_INDEPENDENCE_WAVE_ARCTICX.tga` | `gfx/flags/small/YAK_INDEPENDENCE_WAVE_ARCTICX.tga` |
| Popular socialist councils | `YAK_INDEPENDENCE_WAVE_SOCIALISTX` | `gfx/flags/YAK_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `gfx/flags/medium/YAK_INDEPENDENCE_WAVE_SOCIALISTX.tga` | `gfx/flags/small/YAK_INDEPENDENCE_WAVE_SOCIALISTX.tga` |
| Emergency frontier command | `YAK_INDEPENDENCE_WAVE_EMERGENCYX` | `gfx/flags/YAK_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `gfx/flags/medium/YAK_INDEPENDENCE_WAVE_EMERGENCYX.tga` | `gfx/flags/small/YAK_INDEPENDENCE_WAVE_EMERGENCYX.tga` |

Machine-readable QA is in `metadata/flag_validation.json`, `metadata/dds_validation.json`, and `metadata/generation_evidence.json`. The contact sheet is `contact_sheets/iw051_sakha_flag_ladders_contact_sheet.png`. DDS files under `final_dds/` are evidence copies; HOI4 flag lookup uses the TGA ladders.

The prompt text was not present beside the supplied native masters, so the package records that limitation instead of inventing prompt provenance. A parent review must accept the generated route identity and prompt-evidence gap before any central admission or Join wiring.
