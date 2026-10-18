# Shared ChaosX GFX cleanup report

Status: the three parent-assigned division-template emblem findings are implemented and parent-approved.
The three DDS outputs and their source/processing evidence were committed in `2fd2f9258d71a28e2cf8414755b00b83adffafce`.

## Scope and references

The parent-assigned sprite rows are `GFX_div_templ_47_small`, `GFX_div_templ_46_large`, and `GFX_div_templ_47_large`.

The raw `gfx_issues.json` group currently lists a different third row, `GFX_unit_cave_monster_brood_icon_medium`; this report follows the parent-named three-sprite scope, and that cave-monster entry is outside this handoff.

Before production, I inspected the exact mod sprite definitions in `interface/chaosx_gfx_cleanup.gfx`, installed vanilla `GFX_div_templ_0_large` and `GFX_div_templ_0_small` in `interface/subuniticons.gfx`, installed DDS textures `gfx/interface/counters/division_templates_large/custom_template_000.dds` and `.../division_templates_small/custom_template_000.dds`, the canonical `units/land/division_template_emblems/contact_sheet.png`, and mod sibling assets 044/045.

The canonical sample canvases are 76x42 large and 30x12 small. The vanilla 000 small glyph is light neutral and fills the 12px height; the 044/045 mod siblings use brighter green painted relief than the original 046/047 targets.

## Source and runtime crosswalk

| Sprite | Target `.gfx` and texture | Native ImageGen source and SHA-256 | Processed PNG and SHA-256 | Before DDS SHA-256 | Final DDS SHA-256 | Parent review |
|---|---|---|---|---|---|---|
| `GFX_div_templ_47_small` | `interface/chaosx_gfx_cleanup.gfx`; `gfx/interface/counters/division_templates_small/custom_template_047.dds` | `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/source_generated/custom_template_047_small_candidate_v2_source.png` (`3b35ac50bf4581087b2de2ff09f7156044cf0f07580c36deb6aa1fbda1f923f2`) | `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/processed/custom_template_047_small_candidate_v2.png` (`9c2fef31b1d3f7942fe6cfc9bc415446aa9bc817cbeb22e90ec00d1691e2406a`) | `3092743e203d9311dd7110534741e478c9fd2b3e128e81d23291fe1061cf0966` | `cee5cbd8cfcfb64c82b118dd3a96e407189a4053d9bfbd82e3909db8ca5950fd` | Parent approved v2 light-neutral trefoil on 2026-10-06. |
| `GFX_div_templ_46_large` | `interface/chaosx_gfx_cleanup.gfx`; `gfx/interface/counters/division_templates_large/custom_template_046.dds` | `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/source_generated/custom_template_046_large_candidate_v3_source.png` (`06da76f7fbb83f8e7a4ed3c8e721517be016d0a3d21e56765327d98fcd8e4a66`) | `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/processed/custom_template_046_large_candidate_v3.png` (`e28e17368ee3547886c97c1de6c12c764ba224a22bd83eb1f11b14032bf6a29d`) | `284c7c86d2b087e568975b94ffbff1cbce71619af64b9b940c2068d3a89de420` | `223d650bf44bf976c6b21274b6e6796e61be742411dd5d06db8d3a846733f957` | Parent approved v3 brighter flask and 36px height on 2026-10-06. |
| `GFX_div_templ_47_large` | `interface/chaosx_gfx_cleanup.gfx`; `gfx/interface/counters/division_templates_large/custom_template_047.dds` | `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/source_generated/custom_template_047_large_candidate_v3_source.png` (`e816aecde56545761965271cc987367e774ef57ea30fc82b35adac2c5ba8c148`) | `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/processed/custom_template_047_large_candidate_v3.png` (`2c70cf9188767af8b3be2f6d2bb1a3e298775858a1a5071c1b01c8774d0f224e`) | `ceecf68ac8d27209ef8c4e1b5c66c9a1411072164806be9cd4b4d6a51e8edfdd` | `9609d55f4a6563760fde4db233ce2028eb9c45eddf91b2d196411c1be0aa7f17` | Parent approved v3 brighter trefoil and 36px height on 2026-10-06. |

The accepted small 47 image keeps a 13x12 light-neutral trefoil centered on the 30x12 canvas. It has transparent corners and an alpha range of 0-255; 53 subject pixels have alpha at least 128 and 9 are fully opaque at native resolution.

The accepted large 46/47 images are fresh native-alpha ImageGen reconstructions from the original flask and trefoil identities. Their processed visible bounds are 27x36 and 39x36 respectively, centered on 76x42 canvases with transparent margins and no edge clipping.

## DDS and visual evidence

Each final DDS was produced with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py` using DirectXTex `texconv.exe` and passed the repository legacy BGRA header check, native dimensions, transparent-corner check, and exact pixel round-trip against its processed PNG.

The final round-trip evidence is `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/processed/division_template_dds_roundtrip_v3.json` (SHA-256 `af06b1e2fe04397d9ea03b80af9f1944c84caf26f6147c896526495cf5824102`).

The parent-review sheet is `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/contact_sheets/division_template_emblem_candidate_review_v3.png` (SHA-256 `b72a0c98febb3703cbb4c6939d8ccf9e2a29e22f4ff2789631dfc1af4d1512a7`). The final PNG/DDS sheet is `docs/assets/gfx_fix_shared_chaosx_gfx_cleanup/contact_sheets/division_template_emblem_dds_roundtrip_v3.png` (SHA-256 `6d08d5980db2cdaf465d9cca0bd23907789f5f4b11b0603f284d5279a565d01c`).

The first green ImageGen source for 47 small was rejected by the parent for being too dark; the v1 containment-only 46/47 large candidates were also rejected for remaining muddy. Those versions and prompt records remain preserved and are not installed.

No `.gfx`, GUI, gameplay, focus, decision, event, localization, or history file was edited. Existing sprite names and texture paths remain unchanged.

## Remaining checks

The engine selects these sprites through the division-template emblem surface; the installed vanilla pattern is `GFX_div_templ_0_large` and `GFX_div_templ_0_small` in `interface/subuniticons.gfx`. The parent owns final source/package integration, and the user owns live-game validation.
