# Saunders Lewis GFX handoff (source-only)

No GFX file was edited and no DDS was produced in this source-only handoff.

## Stable consumer

| Consumer | Existing sprite | Existing runtime target | Source reference |
| --- | --- | --- | --- |
| `WLS_independence_wave_national_council` | `GFX_portrait_WLS_independence_wave_national_council` | `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `source_crops/WLS_saunders_lewis_geoff_charles_1973_head_shoulders.png` |

If a later ImageGen output passes the likeness and era review, keep the existing consumer and sprite names. Convert the approved deterministic 156×210 PNG with the repository-standard DDS converter, place the resulting large portrait at the runtime target above, and update only the owning GFX surface in the parent gameplay handoff. Do not wire this source crop directly as a runtime DDS.

## Attribution

Any adapted output based on this source must retain attribution to Geoff Charles and the National Library of Wales, link [the Commons source](https://commons.wikimedia.org/wiki/File:Saunders_Lewis_(1520393).jpg) and [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), and disclose changes. The date mismatch means this handoff is `needs_user_review`.
