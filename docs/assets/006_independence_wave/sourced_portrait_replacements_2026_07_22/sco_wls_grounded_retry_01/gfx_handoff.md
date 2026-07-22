# Event 006 Scotland/Wales portrait source handoff

This handoff is intentionally source-mode only. Do not wire a `.gfx` file from
this note until the parent agent completes the identity-preserving HOI4 portrait
pass and, for Robert Knox Ross, confirms the collection record's CC BY-SA 3.0 NL
metadata.

## Selected source inputs

| Consumer | Subject | Crop input | Proposed runtime path after parent processing | Suggested sprite |
|---|---|---|---|---|
| `portrait_SCO_independence_wave_civic_convention.dds` | Robert Bontine Cunninghame Graham | `review_crops/SCO/SCO_cunninghame_graham_hathitrust_1907_head_shoulders.png` | `gfx/leaders/SCO/portrait_SCO_independence_wave_civic_convention.dds` | `GFX_SCO_independence_wave_civic_convention` |
| `portrait_WLS_independence_wave_national_council.dds` | Saunders Lewis | `review_crops/WLS/WLS_saunders_lewis_ydrych_1916_head_shoulders.png` | `gfx/leaders/WLS/portrait_WLS_independence_wave_national_council.dds` | `GFX_WLS_independence_wave_national_council` |
| `portrait_WLS_independence_wave_mountain_commandant.dds` | Robert Knox Ross | `review_crops/WLS/WLS_robert_knox_ross_erfgoed_1944_head_shoulders.png` | `gfx/leaders/WLS/portrait_WLS_independence_wave_mountain_commandant.dds` | `GFX_WLS_independence_wave_mountain_commandant` |

The source masters remain at:

- `source_masters/SCO/SCO_cunninghame_graham_hathitrust_1907.jpg`
- `source_masters/WLS/WLS_saunders_lewis_ydrych_1916.jpg`
- `source_masters/WLS/WLS_robert_knox_ross_erfgoed_1944.jpg`

The parent should preserve these unchanged masters, use the crop only as the
identity-preserving edit input, compare the result against the appropriate
canonical leader/commander reference family, and record the final DDS hash and
attribution in the implementation-owned manifest. No `_small` or advisor sprite
is proposed.

## Alternate and blocked rows

- `WLS_gerard_bucknall_iwm_1944_alternate.jpg` and its mechanical crop are a
  rights-clear alternate only. The two-person source is visually weaker than the
  Ross portrait, so no runtime sprite is proposed.
- The Scotland territorial commander remains blocked. Do not wire McCulloch,
  Ironside, Dowding, or a generic/generated substitute without a new, explicitly
  rights-cleared source decision.

## Attribution strings to retain if approved

- Cunninghame Graham: `Photo of R. B. Cunninghame Graham`, HathiTrust scan,
  no later than 1907, public-domain basis recorded by Commons.
- Saunders Lewis: `Y Drych`, 3 February 1916, author not stated, public-domain
  pre-1931 publication basis; source page at the National Library of Wales.
- Robert Knox Ross: Erfgoed 's-Hertogenbosch collection record, `CC BY-SA 3.0 NL`
  as recorded by the collection listing; confirm the record before shipping and
  credit the institution.
- Gerard Bucknall alternate: No. 5 Army Film & Photographic Unit, Sgt Laing,
  IWM B 5468, 1944, UK Government/Crown copyright expiry/public-domain rationale.

