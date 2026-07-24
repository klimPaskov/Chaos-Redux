# IW-008 RHI river commandant source processing handoff

This handoff covers the source-only Gustav-Adolf von Zangen retry for the grounded male `RHI_independence_wave_river_commandant` identity.

The selected source master is `source_masters/RHI_gustav_adolf_von_zangen_bundesarchiv_1944.jpg` and the exact identity crop is `source_crops/RHI_gustav_adolf_von_zangen_head_shoulders.png` with crop `(180,140)-(365,330)`.

The source master is an unchanged `548x800` grayscale JPEG from Bundesarchiv Bild 183-H28061, dated November 1944, with SHA-256 `B3A829FC739F43262057C91F146FF03561508708208C6F350A36158D4AF78C0D`.

The crop is a direct no-resample `185x190` grayscale PNG with SHA-256 `FC9C5F986F37C4F040A31F909FD5C03AF6C594D54BE295CA25373EAEC82C4D38`.

The requested stable runtime consumer is character `RHI_independence_wave_river_commandant`.

The requested stable sprite is `GFX_portrait_RHI_independence_wave_river_commandant`.

The parent-owned `.gfx` consumer remains `interface/006_independence_wave_region_01_portraits.gfx`, and the reserved runtime texture remains `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds`.

No DDS is present or proposed in this source-only retry.

No ImageGen output, processed `156x210` candidate, final portrait PNG, `.gfx` edit, gameplay edit, localisation edit, or fallback is present.

The next processing pass must use the exact crop as the identity reference, use the canonical full commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/` for style only, remove unsupported late-war insignia without changing identity, and retain all source hashes.

The real-person portrait gate remains pending the mandatory source-locked identity-preserving repaint and an independent reviewer who is not the producer.

The parent agent must not convert or wire this candidate until separate likeness, style, provenance, ownership, and era-fit review records a pass.

The source-rights attribution to retain is `Bundesarchiv, Bild 183-H28061 / CC-BY-SA 3.0` under <https://creativecommons.org/licenses/by-sa/3.0/de/deed.en>.

The source page is <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H28061,_Westfront,_Gustav_v._Zangen,_Albert_Speer.jpg> and the direct original is <https://upload.wikimedia.org/wikipedia/commons/9/99/Bundesarchiv_Bild_183-H28061%2C_Westfront%2C_Gustav_v._Zangen%2C_Albert_Speer.jpg>.

The package is `needs_user_review` and source-ready for the parent-owned downstream portrait pipeline, not runtime-ready.
