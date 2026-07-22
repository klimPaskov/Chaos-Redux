# Event 006 active-vanilla conflict retry — deferred GFX handoff

This handoff names the existing runtime consumers only. It does not create or
replace any `.gfx` definition, DDS, PNG, crop, or resize. A parent reviewer
must select a source master, perform the approved 156×210 leader portrait
processing, obtain independent visual/rights approval, and then wire the
exact output.

| Role | Proposed sprite | Deferred runtime DDS | Primary source master | Alternate source master(s) | Disposition |
|---|---|---|---|---|---|
| RHI civic/constitutional/patron | `GFX_portrait_RHI_independence_wave_provisional_directorate` | `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` | `source_masters/RHI/RHI_karl_jarres_bundesarchiv_1925.jpg` | `source_masters/RHI/RHI_wilhelm_marx_loc_1920.jpg`; Jarres LOC face reference `source_masters/RHI/RHI_karl_jarres_loc_undated.jpg` | Jarres `source_ready`; Marx `source_ready` alternate |
| BAY mountain/emergency command | `GFX_portrait_BAY_independence_wave_mountain_commandant` | `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds` | `source_masters/BAY/BAY_eugen_von_schobert_nac_1940.jpg` | `source_masters/BAY/BAY_ludwig_kuebler_circa_1941.jpg` | Schobert `source_ready`; Kübler `needs_review` on rights/provenance |
| SCO territorial/military command | `GFX_portrait_SCO_independence_wave_territorial_commandant` | `gfx/leaders/006_independence_wave/portrait_SCO_independence_wave_territorial_commandant.dds` | `source_masters/SCO/SCO_victor_fortune_iwm_1940_portrait.jpg` | `source_masters/SCO/SCO_archibald_rice_cameron_1929_commons.jpg`; Fortune contextual archive companions retained in the same folder | Fortune `source_ready`; Cameron `needs_review` on NPG/Commons rights conflict |

The parent must not use the old Adenauer, Franz Ritter von Epp, or Edmund
Ironside portraits for these consumers. No fallback or generated face is
authorized. The low-resolution Fortune close portrait is preserved as-is;
the 800×525 IWM scene and 580×609 51HD image are context companions, not
processed substitutes.
