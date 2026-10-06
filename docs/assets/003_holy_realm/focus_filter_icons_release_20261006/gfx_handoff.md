# GFX handoff: Event 003 Holy Realm focus-search filters

Status: The twelve icons are complete, parent-reviewed, and installed at the exact paths already registered in `interface/003_holy_realm_focus_filter_icons.gfx`.

Consumer canvas: 27x27 transparent RGBA, one static image per filter sprite.

The existing parent-owned .gfx definitions were verified and left unchanged; no additional sprite definitions are needed.

| Filter ID | Registered sprite | Exact installed DDS path | Reviewed docs candidate | Installed SHA-256 | GFX mapping |
| --- | --- | --- | --- | --- | --- |
| `FOCUS_FILTER_THR_PEACE` | `GFX_FOCUS_FILTER_THR_PEACE` | `gfx/interface/focusview/filter/003_holy_realm/filter_thr_peace.dds` | `dds/filter_thr_peace.dds` | `d779157595d6fa0277ae457b0dbf1fae0927d567a7e68bb3720ecd3ed6860f85` | Exact existing mapping verified |
| `FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE` | `GFX_FOCUS_FILTER_THR_FINAL_SILENCE_PRESSURE` | `gfx/interface/focusview/filter/003_holy_realm/filter_thr_final_silence_pressure.dds` | `dds/filter_thr_final_silence_pressure.dds` | `c17d0922d756430a073d2602945da1c243bffe2f66e920b77685b559ec6534bd` | Exact existing mapping verified |
| `FOCUS_FILTER_THR_MANDALA_INTEGRATION` | `GFX_FOCUS_FILTER_THR_MANDALA_INTEGRATION` | `gfx/interface/focusview/filter/003_holy_realm/filter_thr_mandala_integration.dds` | `dds/filter_thr_mandala_integration.dds` | `305df146c88989b0ab68e56b40e0e527d454251243b7a0ae58c45cca4357f479` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_MEDITATION` | `GFX_FOCUS_FILTER_HOLY_REALM_MEDITATION` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_meditation.dds` | `dds/filter_holy_realm_meditation.dds` | `384d40e1a853a311161bd4eaccae7cb0900b1151ca456bbb54d63278533fa398` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_SANCTUARY` | `GFX_FOCUS_FILTER_HOLY_REALM_SANCTUARY` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_sanctuary.dds` | `dds/filter_holy_realm_sanctuary.dds` | `6f2b6c8deaa92d1bf1b1ed7bc50bbcdb223b256a3f81da51faadb45f208730ad` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_ANTI_CHAOS` | `GFX_FOCUS_FILTER_HOLY_REALM_ANTI_CHAOS` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_anti_chaos.dds` | `dds/filter_holy_realm_anti_chaos.dds` | `e219a5e9618a7dac25d4f8c6d37e88f5fdcfa5336fa0dd68b946b3d03afea0a8` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_BODHI` | `GFX_FOCUS_FILTER_HOLY_REALM_BODHI` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_bodhi.dds` | `dds/filter_holy_realm_bodhi.dds` | `8752b1617eef3338950dd5d91dc0c5b1c118c7ffb695b7dee9ec5d2dcb2bcb37` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_TEACHING` | `GFX_FOCUS_FILTER_HOLY_REALM_TEACHING` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_teaching.dds` | `dds/filter_holy_realm_teaching.dds` | `58730b846a770be8990b9408cf8dc3314ecff9c7211c2dd97e642bc669e852ff` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_GOVERNANCE` | `GFX_FOCUS_FILTER_HOLY_REALM_GOVERNANCE` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_governance.dds` | `dds/filter_holy_realm_governance.dds` | `acb05f5cefb9789d4e1013ddeab0879b4e21907a98e98defc62a64d1891a68d5` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_COMPACT` | `GFX_FOCUS_FILTER_HOLY_REALM_COMPACT` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_compact.dds` | `dds/filter_holy_realm_compact.dds` | `b090b5550ad655c10a6a9b417ffd97b2de5b1df1e3a65e0b66f2983c7c5b46b8` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_NIRVANA` | `GFX_FOCUS_FILTER_HOLY_REALM_NIRVANA` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_nirvana.dds` | `dds/filter_holy_realm_nirvana.dds` | `06c2cc3950703cac401c2e90d03eefa23830f5e99326a04fe393193a57e48e9f` | Exact existing mapping verified |
| `FOCUS_FILTER_HOLY_REALM_HIDDEN` | `GFX_FOCUS_FILTER_HOLY_REALM_HIDDEN` | `gfx/interface/focusview/filter/003_holy_realm/filter_holy_realm_hidden.dds` | `dds/filter_holy_realm_hidden.dds` | `54db2b587c6e6b458316be0459a9a2bf97c9b9ababd30149931239d1897ec2aa` | Exact existing mapping verified |

Every installed file is byte-identical to its reviewed docs candidate; full source, preview, candidate, runtime, prompt, and contact-sheet hashes are recorded in [manifest.md](manifest.md) and [processing_metadata.json](notes/processing_metadata.json).

The parent accepted the native and enlarged contact sheets on 2026-10-06; the native sheet is [here](contact_sheets/focus_filters_native_27x27.png) and the enlarged comparison is [here](contact_sheets/focus_filters_enlarged_4x_comparison.png).

No fallback removal or visual substitute was used; all twelve sources have native ImageGen alpha and were independently generated for their own filter subject.

No GFX, focus, localization, gameplay, GUI, spreadsheet, or shared files were edited by this asset worker.
