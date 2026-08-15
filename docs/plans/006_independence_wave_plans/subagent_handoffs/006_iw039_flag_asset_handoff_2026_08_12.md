# IW-039 Cossack Don flag asset handoff — 2026-08-12

## Scope and disposition

This handoff covers only non-portrait identity art for Event 006 package `IW-039` (`Cossack Don`, carrier `DON`). The asset pass is **fail-closed for new runtime art**. The installed vanilla `DON` flag ladder is a defensible `existing_base_reuse` candidate, but no mod override, route-specific flag, emblem flag, DDS, `.gfx`, or gameplay file was added.

## Evidence package

The temporary source and QA package is retained at:

`docs/assets/006_independence_wave/iw039_don_flag_reuse_2026_08_12/`

It contains exact installed source TGAs under `source/`, lossless PNG previews for all normal/medium/small variants, `contact_sheet.png`, `research/Flag_of_Don_Cossacks.svg`, the research-only Don Host coat-of-arms reconstruction, `manifest.md`, and `gfx_handoff.md`.

The handoff's exact proposed basenames are `DON`, `DON_communism`, `DON_fascism`, and `DON_neutrality` in the vanilla flag roots. All 12 source files pass the required dimensions (82x52, 41x26, 10x7) and type-2 32-bit bottom-left TGA origin checks. The source and preview SHA-256 values are recorded in the package manifest and gfx handoff.

## Historical/provenance result

- FOTW's [Don Cossacks' flags page](https://www.fotw.info/flags/ru_cdon.html) documents the blue/yellow/red tricolor, its 1918 Krasnov-era development, and the Don Cossack/Kalmyk/nonresident color interpretation.
- [Wikimedia Commons' `Flag_of_Don_Cossacks.svg`](https://commons.wikimedia.org/wiki/File:Flag_of_Don_Cossacks.svg) is a public-domain dedication by Riwnodennyk dated 4 May 1918, but it is a modern flat reconstruction, not an untouched period artifact. It is retained as geometry evidence only.
- [Wikipedia's Don Cossacks entry](https://en.wikipedia.org/wiki/Don_Cossacks) cross-checks inauguration at Novocherkassk on 4 May 1918 under Ataman Pyotr Krasnov and the blue/yellow/red fields.
- The [Don Host coat-of-arms reconstruction](https://commons.wikimedia.org/wiki/File:Cort_of_arms_of_Vsevelikoe_Voisko_Donskoe.png) is retained as research-only. Its 2010 rendition and indirect source chain are insufficient for a runtime charge without an accepted route design and heraldic review.

## Runtime boundary

If the parent later admits IW-039 as the vanilla `DON` carrier, use the installed tag ladder by exact basenames and do not point any runtime consumer into `docs/assets/`. No `.gfx` sprite is needed for country flags and no DDS conversion is appropriate. If the parent chooses a cosmetic tag or route-specific identity, route a separate strict flat ImageGen package through the event-assets workflow; do not repurpose the research shield or edit the tricolor locally.

## Blockers and parent actions

1. The package preflight still leaves vanilla `DON` capital 218 versus Event 006 compact 245|238 unresolved, while Event 005 `DHC` claims 218|238. No route-specific flag or emblem may be generated until the parent accepts one identity/capital/ownership matrix.
2. Existing ideology overlays are gameplay assets, not historical Don Republic standards; they must not be cited as 1936 source evidence.
3. The parent owns final admission, runtime wiring, preservation of ordinary vanilla DON release behavior outside Event 006 origin scope, and any future cosmetic-tag flag decision.

No stage or commit was performed by the asset worker.
