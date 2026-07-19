# GFX handoff — IW-093 / IW-098 fictional commanders

Suggested target: `interface/006_independence_wave_iw093_iw098_portraits.gfx` (existing Independence Wave portrait definition file). This handoff intentionally does not edit interface GFX.

| Proposed sprite | Texture path | Size | Use |
| --- | --- | --- | --- |
| `GFX_portrait_DOX_kwame_frimpong` | `gfx/leaders/006_independence_wave/portrait_DOX_kwame_frimpong.dds` | 156x210 | DOX Kwame Frimpong full commander portrait |
| `GFX_portrait_DOX_kwame_frimpong_small` | `gfx/leaders/006_independence_wave/portrait_DOX_kwame_frimpong_small.dds` | 65x67 | DOX Kwame Frimpong commander miniature |
| `GFX_portrait_DOX_kwaku_ntim` | `gfx/leaders/006_independence_wave/portrait_DOX_kwaku_ntim.dds` | 156x210 | DOX Kwaku Ntim full commander portrait |
| `GFX_portrait_DOX_kwaku_ntim_small` | `gfx/leaders/006_independence_wave/portrait_DOX_kwaku_ntim_small.dds` | 65x67 | DOX Kwaku Ntim commander miniature |
| `GFX_portrait_SOK_umaru_gwadabawa` | `gfx/leaders/006_independence_wave/portrait_SOK_umaru_gwadabawa.dds` | 156x210 | SOK Umaru Gwadabawa full commander portrait |
| `GFX_portrait_SOK_umaru_gwadabawa_small` | `gfx/leaders/006_independence_wave/portrait_SOK_umaru_gwadabawa_small.dds` | 65x67 | SOK Umaru Gwadabawa commander miniature |
| `GFX_portrait_SOK_bello_rabah` | `gfx/leaders/006_independence_wave/portrait_SOK_bello_rabah.dds` | 156x210 | SOK Bello Rabah full commander portrait |
| `GFX_portrait_SOK_bello_rabah_small` | `gfx/leaders/006_independence_wave/portrait_SOK_bello_rabah_small.dds` | 65x67 | SOK Bello Rabah commander miniature |

Copy-ready pattern (adapt to the established file's syntax):

```text
spriteType = {
	name = "GFX_portrait_DOX_kwame_frimpong"
	texturefile = "gfx/leaders/006_independence_wave/portrait_DOX_kwame_frimpong.dds"
}
```

The four small textures are direct face-and-shoulders crops from their matching approved full portraits. They are not advisor dossier cards and must not be routed through advisor processing or advisor sprite definitions.
