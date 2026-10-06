# Focus filter reference evidence

The exact consumer is the focus-search toolbar, so the relevant family is the installed focus-filter texture set, not the larger national-focus medallions.

The canonical `icons/national_focus/contact_sheet.png` was inspected first for general HOI4 focus-interface shading and transparent-canvas context; its 16 references are 100x88 medallions and were not used as source art.

The canonical `gfx_references/CATALOG.md` has no dedicated focus-search filter family, so the two review-only vanilla contact sheets were made from the exact installed DDS inputs listed below before inspecting each reference individually.

The installed consumer definition is `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/interface/nationalfocusview.gfx:257-305`; it defines the vanilla political, research, industry, stability, war-support, manpower, and territory filter sprites in that span.

`hoi4.source_lookup` confirmed `game:interface/nationalfocusview.gfx`, `GFX_FOCUS_FILTER_POLITICAL` at lines 257-260, with source revision `f09dbe6ec779ffa71b065d1cf944510f76172b920f2577f9ac6145b21c913969`.

| Vanilla sprite | Installed texture | Inspected native properties |
| --- | --- | --- |
| `GFX_FOCUS_FILTER_POLITICAL` | `gfx/interface/focusview/filter/pol_power_icon.dds` | 27x27 RGBA, alpha 0-255, 3044 bytes |
| `GFX_FOCUS_FILTER_RESEARCH` | `gfx/interface/focusview/filter/research_icon.dds` | 27x27 RGBA, alpha 0-255, 3044 bytes |
| `GFX_FOCUS_FILTER_STABILITY` | `gfx/interface/focusview/filter/stability_icon.dds` | 27x27 RGBA, alpha 0-255, 3044 bytes |
| `GFX_FOCUS_FILTER_WAR_SUPPORT` | `gfx/interface/focusview/filter/war_support_icon.dds` | 27x27 RGBA, alpha 0-255, 3044 bytes |
| `GFX_FOCUS_FILTER_MANPOWER` | `gfx/interface/focusview/filter/manpower_icon.dds` | 27x27 RGBA, alpha 0-255, 3044 bytes |
| `GFX_FOCUS_FILTER_ANNEXATION` | `gfx/interface/focusview/filter/territory_icon.dds` | 27x27 RGBA, alpha 0-255, 3044 bytes |

The offline wiki section `Search filters` in `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:455-512` was read at revision `bd989a13237c464f140a0aa671cc42c30a48e84a27dae791b8914654fb9c6203`; it identifies the search-menu consumer and the `GFX_` plus filter-id sprite naming rule.

`hoi4.reference_search` found no relevant installed game-document section for focus-filter texture sizing; the installed GFX and DDS files above supplied the direct game reference.

The vanilla filter contact sheets are `vanilla_filter_reference_sheet.png` and `vanilla_filter_reference_detail.png`; both contain review-only renderings of installed textures and neither is runtime art.
