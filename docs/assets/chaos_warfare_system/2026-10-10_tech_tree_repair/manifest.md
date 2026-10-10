# CBRN technology card art, 10 October 2026

Ten 64x64 research-card paintings for the rebuilt chemical warfare folder. Created with the gptimage MCP (ChatGPT Images, high quality, 1024x1024 request, native transparent background), then cropped to the painted bounds, fitted to a 60-pixel longest edge on a transparent 64x64 canvas, and converted with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.

Generation sources, processed PNGs and the review sheet are working files under the ignored `.tmp/tech_tree_repair_2026-10-10/`; only the final DDS files are tracked.

| Technology | Sprite | Final DDS | Source sha256 (first 16) |
| --- | --- | --- | --- |
| `chlorine_gas` | `GFX_chlorine_gas_medium` | `gfx/interface/technologies/chlorine_gas_tech.dds` | `d55b0ad3b3eed429` |
| `phosgene` | `GFX_phosgene_medium` | `gfx/interface/technologies/phosgene_gas_tech.dds` | `2c27687b44defb33` |
| `mustard_gas` | `GFX_mustard_gas_medium` | `gfx/interface/technologies/mustard_gas_tech.dds` | `6d74c66230f908e8` |
| `lewisite` | `GFX_lewisite_medium` | `gfx/interface/technologies/lewisite_gas_tech.dds` | `77f5ba9fc7da0d17` |
| `tabun` | `GFX_tabun_medium` | `gfx/interface/technologies/tabun_ga_vector_tech.dds` | `4d1046a39a8b3d69` |
| `sarin` | `GFX_sarin_medium` | `gfx/interface/technologies/sarin_gas_tech.dds` | `0ce1c2c8185f47fa` |
| `soman` | `GFX_soman_medium` | `gfx/interface/technologies/soman_gas_tech.dds` | `2c8e9de52290f949` |
| `livens_projector_tech` | `GFX_livens_projector_tech_medium` | `gfx/interface/technologies/livens_projector_tech.dds` | `58e42820ce1e3f05` |
| `improved_livens_projector` | `GFX_improved_livens_projector_medium` | `gfx/interface/technologies/livens_projector_improved_tech.dds` | `6baa54e0fd2cfaa6` |
| `advanced_livens_projector` | `GFX_advanced_livens_projector_medium` | `gfx/interface/technologies/livens_projector_advanced_tech.dds` | `9131a0534d30716a` |

Each source was checked for real zero-alpha corners before processing, and every final DDS decodes as 64x64 RGBA. The previous agent cards shared one cylinder painting; each agent now shows its own munition or apparatus. The Livens equipment sprites keep their 94x45 paintings at `gfx/interface/technologies/livens_projector*.dds`, which the equipment consumer expects; only the technology cards were repointed.
