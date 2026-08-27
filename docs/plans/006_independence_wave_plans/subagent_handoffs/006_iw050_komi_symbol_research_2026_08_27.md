# IW-050/KOM Komi identity-symbol source audit — fail-closed handoff

Audit date: 2026-08-27.

Owner scope: source-only research for a non-portrait Komi national or route identity asset. No source image was downloaded or archived, and no PNG, TGA, DDS, contact sheet, ImageGen output, `.gfx` entry, flag, event, localisation, gameplay, or spreadsheet file was created or edited.

## Exact gate result

**BLOCKED / fail closed for new IW-050 neutral or route-specific visual identity art.** The bounded review found no defensible pre-1936 or 1936 neutral Komi national flag or emblem source, and the accepted addendum names no route identifier that could authorize a later institutional variant.

No next asset production is authorized. The parent may consider ordinary registered `KOM` ladder reuse only after the official ladder is stable and the parent explicitly accepts that its identity and origin match the Event 006 opening. A later 1937+ Komi ASSR route would require an accepted spec amendment naming the route, date boundary, institution, runtime basename, and rights treatment before any asset worker is routed.

## Accepted Event 006 identity and installed context

- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:51` defines `IW-050` as Komi, registered carrier `KOM`, compact anchor state `397`/Syktyvkar, reservation group `RG-397`, and `reuse_registered_tag`.
- `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:51` requires a sourced identity-valid base flag or a separately sourced historical route; it forbids an invented historical flag presented as authentic.
- `docs/plans/006_independence_wave_plans/006_event6_improvement_addendum_2026_08_24.md` remains **QUEUED / EVIDENCE-BLOCKED** and explicitly forbids a new neutral 1936 flag, cosmetic tag, generated emblem, or route ladder while the gates are open.
- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv:51` keep IW-050 package-local and bind the compact opening to state `397`; states `262` and `581` are optional later extensions, not admitted opening entitlements.
- Installed vanilla `history/countries/KOM - Komi Republic.txt` sets capital `397`, starts politics on `1936.1.1`, and recruits `KOM_pavel_murashev`; `common/characters/KOM.txt` defines the exact male character, but its portrait is a generic Europe token and remains the separate portrait-worker gate.
- Installed vanilla `history/states/397-Syktyvkar.txt` is SOV-owned with SOV and KOM cores; `262-Torzhok.txt` and `581-Northern Urals.txt` are also SOV-owned with KOM cores and remain optional extensions under the current binding.

## Current installed vanilla KOM ladder

The inspected source root was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/gfx/flags/`, including `medium/` and `small/`. The current files are a fresh local snapshot and were not copied.

| Installed path | Dimensions | TGA header | SHA-256 | Observation |
| --- | ---: | --- | --- | --- |
| `gfx/flags/KOM_communism.tga` | 82x52 | type 2, 32-bit, descriptor `0x08`, 17,100 bytes | `30ff8121e5099723e0cd3411a9a2c44fc4192549038a1b42f059d91358724aee` | current communist member |
| `gfx/flags/KOM_democratic.tga` | 82x52 | type 10, 32-bit, descriptor `0x28`, 3,588 bytes | `f550493e3ca57bab7337088291f5ade36937729c0f1f234b44276dba5187fb24` | byte-identical to current fascist and neutrality members |
| `gfx/flags/KOM_fascism.tga` | 82x52 | type 10, 32-bit, descriptor `0x28`, 3,588 bytes | `f550493e3ca57bab7337088291f5ade36937729c0f1f234b44276dba5187fb24` | byte-identical to current democratic and neutrality members |
| `gfx/flags/KOM_neutrality.tga` | 82x52 | type 10, 32-bit, descriptor `0x28`, 3,588 bytes | `f550493e3ca57bab7337088291f5ade36937729c0f1f234b44276dba5187fb24` | byte-identical to current democratic and fascist members |
| `gfx/flags/medium/KOM_communism.tga` | 41x26 | type 2, 32-bit, descriptor `0x08`, 4,803 bytes | `af1828d2c31ad7bfdfcafa1833a5425a0a159b09e55395a0f5d8fe19ab6f8f9c` | current communist member |
| `gfx/flags/medium/KOM_democratic.tga` | 41x26 | type 10, 32-bit, descriptor `0x28`, 1,528 bytes | `bb75c7a96eb014a2b06718f3a1ce12d03b03ec38dad41958005a3395e6f0b65e` | byte-identical to current fascist and neutrality members |
| `gfx/flags/medium/KOM_fascism.tga` | 41x26 | type 10, 32-bit, descriptor `0x28`, 1,528 bytes | `bb75c7a96eb014a2b06718f3a1ce12d03b03ec38dad41958005a3395e6f0b65e` | byte-identical to current democratic and neutrality members |
| `gfx/flags/medium/KOM_neutrality.tga` | 41x26 | type 10, 32-bit, descriptor `0x28`, 1,528 bytes | `bb75c7a96eb014a2b06718f3a1ce12d03b03ec38dad41958005a3395e6f0b65e` | byte-identical to current democratic and fascist members |
| `gfx/flags/small/KOM_communism.tga` | 10x7 | type 2, 32-bit, descriptor `0x00`, 298 bytes | `0e644d5734c4160f9805fec653e88c4f8d62055a185952bac388bc85c711658c` | current communist member |
| `gfx/flags/small/KOM_democratic.tga` | 10x7 | type 10, 32-bit, descriptor `0x28`, 279 bytes | `414a3624def506bc11f06349f18f15fa0667d94fad14432a54f83b8ff0af3e1a` | byte-identical to current fascist and neutrality members |
| `gfx/flags/small/KOM_fascism.tga` | 10x7 | type 10, 32-bit, descriptor `0x28`, 279 bytes | `414a3624def506bc11f06349f18f15fa0667d94fad14432a54f83b8ff0af3e1a` | byte-identical to current democratic and neutrality members |
| `gfx/flags/small/KOM_neutrality.tga` | 10x7 | type 10, 32-bit, descriptor `0x28`, 279 bytes | `414a3624def506bc11f06349f18f15fa0667d94fad14432a54f83b8ff0af3e1a` | byte-identical to current democratic and fascist members |

Decoded RGBA pixels are identical across all four ideology members at each of the three sizes. The current path therefore has complete dimensions but not a clean stable ideology ladder for Event 006 acceptance, and it conflicts with the earlier all-type-2 snapshot recorded in `006_iw050_komi_symbol_research_2026_08_14.md`. Re-hash again after the official source path is stable; do not treat the current mixed encoding or the prior snapshot as an admitted runtime asset.

The repository files `gfx/flags/KOM_democratic.tga`, `gfx/flags/medium/KOM_democratic.tga`, and `gfx/flags/small/KOM_democratic.tga` are separate Event 005-era overrides with no independent historical source packet. Their current SHA-256 values are `f9885cb8634035f8bc5a65a3b864c2ed999ee724f6bbff5e0370fb02e19c5a7b`, `b6f6faca5cc5fd1bcca3920adcc2129e37ff236f597e75a96d797bf08e7d98c2`, and `2584c1b7abed646f7dd14bc98ae1350e90786221904c875bd93270d22a7b284`; they are not an IW-050 source or admission receipt.

## Sourced candidate review

The canonical reference root was inspected at `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/`. Its `flags/contact_sheet.png` shows the normal, medium, and small review family, but it contains no KOM-specific review PNG. The existing 2026-08-14 symbol handoff was rechecked, and the Commons metadata was refreshed through the named source pages.

| Candidate | Source and rights evidence | Date/identity fit | Gate disposition |
| --- | --- | --- | --- |
| [Flag of the Komi ASSR (1937)](https://commons.wikimedia.org/wiki/File:Flag_of_the_Komi_ASSR_(1937).svg) | Wikimedia Commons metadata: reconstruction by Helgo13, `2019-05-17`, based on the Constitution of Komi ASSR, stated `Public domain` / `PD-RU-exempt (flags)`, remote SHA-1 `856333903cd513bd5852cb00becabbee5b6bcb55`. | The constitutional design is explicitly 1937 and is an RSFSR/ASSR institutional flag with inscriptions, one year after the 1936 opening. | **Not admissible** as the neutral opening flag; candidate only for a separately named later socialist/ASSR route. |
| [Flag of the Komi ASSR (1937–1938)](https://commons.wikimedia.org/wiki/File:Flag_of_the_Komi_ASSR_(1937-1938).svg) | Wikimedia Commons metadata: reconstruction by Jeromi Mikhael, `2018-10-31`, own work based on the Constitution of the Komi ASSR, stated `Public domain` / `PD-RU-exempt (flags)`, remote SHA-1 `cf97dd8e9bcf7717acb80456e4f1bddb98737ea9`. | Later constitutional ASSR identity; not a 1936 neutral Komi national design. | **Not admissible** without a later route amendment naming the institutional identity and date boundary. |
| [Emblem of the Komi ASSR (1937–1978)](https://commons.wikimedia.org/wiki/File:Emblem_of_the_Komi_ASSR_(1937%E2%80%931978).svg) | Wikimedia Commons metadata: Kaidor, `2018-10-13`, stated `Public domain` / CC0 dedication, remote SHA-1 `86a95a8b9d1e2ac5d6798d017d6f758c10ad7279`. The page identifies adapted vector elements, so the vector is not an archival scan. | Institutional ASSR emblem beginning in 1937 and continuing through 1978; wrong for a neutral Jan-1936 opening. | **Deferred route reference only**, not an admitted asset. Parent must accept a named later institutional route before production. |
| [Flag of the Komi ASSR (1938–1954)](https://commons.wikimedia.org/wiki/File:Flag_of_the_Komi_ASSR_(1938-1954).svg) | Wikimedia Commons metadata: reconstruction by Jeromi Mikhael, `2018-10-31`, based on the constitutional description, stated `Public domain` / `PD-RU-exempt (flags)`, remote SHA-1 `26eeb11f57006423acc860de5dac72c4461422e3`. | Later than the opening and still Soviet ASSR institutional identity. | **Rejected** for IW-050 opening; possible only under an explicitly dated later route. |
| [Flag of Komi](https://commons.wikimedia.org/wiki/File:Flag_of_Komi.svg) | Wikimedia Commons metadata: V. Ya. Serditov, design dated `1997-12-17`, stated `Public domain`, remote SHA-1 `4d0669da39450a7bc282452002d54e1ba9485d92`. | Modern Komi Republic state flag, not a period source for 1936. | **Rejected** for opening or historical route. |
| [Flag of the Komi Voityr](https://commons.wikimedia.org/wiki/File:Flag_of_the_Komi_Voityr.svg) | Wikimedia Commons metadata: ProjectHorizons, `2022-11-15`, stated `CC BY-SA 4.0`, remote SHA-1 `e281f47b704bdb5688e0b1d7874555b4d7d35974`. | Explicitly an organizational flag used alongside the modern Republic flag; not a state or 1936 institution. | **Rejected**; cannot be relabelled as neutral Komi. |
| [Komi Nordic cross flag](https://commons.wikimedia.org/wiki/File:Komi_Nordic_cross_flag.svg) | Wikimedia Commons metadata: ProjectHorizons, `2019-10-09`, stated `CC BY-SA 4.0`, remote SHA-1 `df9651b27b94bcf6ddf1d204d8d24e083de54ae1`. | Modern activist proposal; no 1936 attestation and no accepted route owner. | **Rejected** unless a future high-chaos/alternate-history amendment names the route and rights treatment. |

No pre-1936 Komi national flag, Komi Autonomous Oblast flag, or contemporaneous Komi national emblem was located in the bounded source set. The 1936 Presidential Library record, [From Komi Autonomous Oblast to Komi ASSR](https://www.prlib.ru/item/750113), is a 1936 Syktyvkar publication about the transition to the ASSR, but it exposes no reproducible symbol or image licence. The [1937 Constitution of the Komi ASSR catalogue record](https://naukaprava.ru/catalog/3561/3564/43687?view=1) is the usable institutional design lead, but it confirms the post-opening date rather than a 1936 national flag.

## Runtime and production handoff

- Do not create a new `KOM` flag family, route emblem, source archive, processed PNG, DDS, contact sheet, or `.gfx` handoff from this audit.
- Do not copy or process the Commons SVGs, the current mutable vanilla files, or the Event 005 repository override into a runtime path.
- Ordinary `KOM` reuse remains a parent decision only after a stabilized re-hash and an explicit identity/origin match finding; this does not authorize new production.
- The 1937 ASSR flag and 1937–1978 emblem are defensible rights-labelled design references for a separately approved later institutional route, not for the Event 006 opening. Any such route must be named and accepted before routing to `chaosx_generated_event_art` or another asset producer.
- The Event 006 source-of-truth and addendum remain unchanged: IW-050 stays package-local, absent from central attestation and Join, and fail-closed on symbol/identity evidence.

## Evidence limitations

The Codex web search route did not return a completed result in this run, so no search-result claim is used. Commons page/API metadata and the repository's prior source handoff are the provenance basis for the candidate table. No local source files were archived, so no archived-source hash or processed-asset QA can be claimed.

## Parent decision required

**No next asset production is authorized.** Parent may either stabilize and accept the installed ordinary `KOM` ladder for the existing opening identity, or keep IW-050 blocked. A later 1937+ ASSR flag/emblem remains a needs-user-review design option only after a named route and accepted spec amendment.
