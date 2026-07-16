# Event 006 Mediterranean portrait GFX handoff

Runtime registration file:
`interface/006_independence_wave_mediterranean_portraits.gfx`.

It defines exactly these eight large sprites:

- `GFX_portrait_COR_independence_wave_petru_santucci`
- `GFX_portrait_COR_independence_wave_pasquale_venturi`
- `GFX_portrait_ARX_independence_wave_antioco_melis`
- `GFX_portrait_ARX_independence_wave_vittorio_pala`
- `GFX_portrait_ARX_independence_wave_gavino_piras`
- `GFX_portrait_ASX_independence_wave_sebastiano_restivo`
- `GFX_portrait_ASX_independence_wave_vincenzo_lanza`
- `GFX_portrait_ASX_independence_wave_salvatore_licata`

Every sprite maps by basename to a 156x210 BGRA DDS under
`gfx/leaders/006_independence_wave/`. The matching character consumers are
listed in `manifest.md` and verified in `validation/validation_report.md`.

No `_small` or advisor-art registration belongs to this package. Commanders
use the same large sprite in their `civilian` and `army` portrait scopes.
