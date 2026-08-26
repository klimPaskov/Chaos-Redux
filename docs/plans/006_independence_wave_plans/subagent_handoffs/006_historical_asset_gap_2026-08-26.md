# Event 006 historical asset gap handoff

Audit date: 2026-08-26 (Europe/Kyiv).

Scope: read-only non-portrait audit of the Event 006 flag, symbol, report, news, and super-event asset boundary. No gameplay, GFX, or runtime asset files were edited, and no live rendering is claimed.

## Selected gap: ASX S.015 flag is used as a universal identity

The highest-impact gap is the Sicily/IW-019 `ASX` flag ladder. The pixel package is complete, but the delivered design reconstructs the surviving 1848 S.015 constitutional-independence national colour and is explicitly documented as route-specific. The current runtime basename is the unsuffixed `ASX`, and the same ladder is present under `ASX_democratic`, `ASX_communism`, `ASX_fascism`, and `ASX_neutrality`. The Event 006 ASX package currently exposes five mutually exclusive governments, so the S.015 design can be shown for constitutional, labor, traditional-crown, emergency-military, and patron-client outcomes even though the asset handoff forbids that use.

This is an improper source-to-consumer assignment rather than a missing raster. Source rights are documented, the current consumer is deterministic, and the parent can repair the ownership boundary without researching a new historical object first.

## Contract and source evidence

The parent asset prompt requires researched historical flags and symbols to be reconstructed as clean flat geometry, requires normal/medium/small HOI4 files, and requires source URLs, authors, archives, dates, licenses, uncertainty, final paths, and proposed basenames. This is recorded in `docs/specs/006_independence_wave_specs/prompts/independence_wave_asset_prompt.md:133-149` and `:203-214`.

The Event 006 Part 7 rules require every country flag family to have 82x52, 41x26, and 10x7 files, require historically attested symbols to be sourced and documented, require fictional or alternate route flags to be generated, and require ideology and route variants to be distinct designs rather than recolors. This is recorded in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md:517-526`.

The registry row is `ASSET-044,country flags,flag family,"82x52, 41x26, 10x7",sourced for historical identities, generated for fictional variants,...,gfx/flags roots,flags`. The core report/news/super-event rows are generated and do not create a competing historical source obligation for this gap.

The controlling historical object is the Italian Ministry of Culture catalog record for S.015, object `0100215963`: <https://catalogo.beniculturali.it/detail/HistoricOrArtisticProperty/0100215963>. The package records the catalog metadata as CC BY 4.0 and states that no catalog image was copied.

The retained layout reference is `docs/assets/006_independence_wave/mediterranean_danube_flag_sources_2026_07_15/source_images/sicily_1848_national_flag_reference.svg`, an SVG with `viewBox="0 0 3000 2000"`, 16,818 bytes, SHA-256 `f5f7c72dc612749c2028217c897a047f60a07812d7f5088e4737b538991a67a8`, attributed to Manny Mannheimer and later Wikimedia Commons contributors under CC BY-SA 4.0. The package requires attribution and share-alike compliance for this reference, but the SVG is only a modern layout aid and is not evidence of a 1936 flag.

The package also records the Archivio di Stato di Palermo General Parliament of Sicily decree collection as link-only, all-rights-reserved factual evidence for the March-April 1848 adoption sequence. No archive scan is copied into the runtime asset.

The source-to-runtime package is `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/` and is duplicated for FORM-05 review in `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/`.

| Artifact | Dimensions / format | SHA-256 | Role |
| --- | --- | --- | --- |
| `source_png/ASX_sicily_1848_s015_imagegen_raw.png` | 1536x1024 opaque PNG, official ImageGen output | `e52afc6d064ddd20d8acf5e112e5b6e02e932440ac83c7311214f267f4fbef36` | Immutable generated source master. |
| `source_png/ASX_sicily_1848_s015_imagegen_flat_master.png` | 1536x1024 opaque PNG | `617992ae27926f78ff201de965d56cb61a1129bd3812eb47114dd09fc89a03db` | Fixed-palette flat master. |
| `processed_png/normal/ASX.png` | 82x52 opaque PNG | `8b5319041d1b033a28ebfd94414343a548be702e14d1e8012a2862382bce8f86` | Normal-size preview. |
| `processed_png/medium/ASX.png` | 41x26 opaque PNG | `f87d8a78506f2e156854824c8bd00f5bc8ebbab810740289fbbe866d840cead4` | Medium-size preview. |
| `processed_png/small/ASX.png` | 10x7 opaque PNG | `818ceec50a66d32f5388bbb86e2dbfea829e9bbaa9225f3828a78098c8d67c9b` | Small-size preview. |
| `gfx/flags/ASX.tga` | 82x52, uncompressed 32-bit BGRA TGA, bottom-left origin, 8-bit alpha, 17,074 bytes | `075949cf85ca8a382922e97a087c09ad0350575a64197763995122789f5151af` | Current unsuffixed runtime flag. |
| `gfx/flags/medium/ASX.tga` | 41x26, uncompressed 32-bit BGRA TGA, bottom-left origin, 8-bit alpha, 4,282 bytes | `aebdb7cf57aef5ad88249c2cef1291346bc2a7ea808ca1129846d851218f2613` | Current unsuffixed runtime flag. |
| `gfx/flags/small/ASX.tga` | 10x7, uncompressed 32-bit BGRA TGA, bottom-left origin, 8-bit alpha, 298 bytes | `8b9158f6defc4408683a369d5a2cd10aa846ac0fb1ca0bafe63441892803c425` | Current unsuffixed runtime flag. |

The current normal, medium, and small ASX ladders are also byte-identical under all four ideology basenames. The current normal hash `075949cf85ca8a382922e97a087c09ad0350575a64197763995122789f5151af`, medium hash `aebdb7cf57aef5ad88249c2cef1291346bc2a7ea808ca1129846d851218f2613`, and small hash `8b9158f6defc4408683a369d5a2cd10aa846ac0fb1ca0bafe63441892803c425` are shared by `ASX`, `ASX_democratic`, `ASX_communism`, `ASX_fascism`, and `ASX_neutrality` at their respective sizes.

The flag family uses TGA filename lookup, so no DDS or `spriteType` is required for this selected asset. A DDS conversion would be the wrong runtime format for this consumer.

## Current consumer evidence

The country tag map binds `ASX` to the Sicily shell at `common/country_tags/006_independence_wave_countries.txt:21`, with the shell in `common/countries/006_independence_wave_ASX.txt` and the dormant history file `history/countries/ASX - Sicily.txt`.

The ASX package trigger is `is_independence_wave_asx_package` at `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:21-25`.

The route-government trigger accepts five ASX route flags at `common/scripted_triggers/006_independence_wave_mediterranean_package_triggers.txt:94-102`: constitutional, popular-council/labor, traditional, emergency-military, and patron-client.

The corresponding five install effects are `independence_wave_install_asx_constitutional_government`, `independence_wave_install_asx_labor_government`, `independence_wave_install_asx_traditional_government`, `independence_wave_install_asx_military_government`, and `independence_wave_install_asx_patron_government` at `common/scripted_effects/006_independence_wave_mediterranean_package_effects.txt:454-517`.

The FORM-05 trigger set explicitly treats `ASX` as a live founding carrier at `common/scripted_triggers/006_independence_wave_form05_triggers.txt:89-112`, `:157-162`, and `:223-236`; the league formation effect later changes the formed identity to `MIX` at `common/scripted_effects/006_independence_wave_form05_effects.txt:328-334`.

No `ASX_*X` cosmetic flag basename is currently installed. The only runtime consumer for this historical reconstruction is therefore the unsuffixed `ASX` filename family plus its four identical ideology copies.

The package handoff explicitly says the opposite of the current route surface: `docs/assets/006_independence_wave/mediterranean_danube_generated_flags_2026_07_15/gfx_handoff.md` labels the S.015 tricolour “constitutional-independence-route art only,” asks the parent either to constrain ASX to that route or to create a specific cosmetic tag, and forbids silent use for neutral, crown, labor, military, fascist, or client routes.

The later FORM-05 manifest repeats the historical classification at `docs/assets/006_independence_wave/form05_mediterranean_assets_2026_07_16/manifest.md:49-66`, but its “complete flag ladders” section at `:79-94` intentionally duplicates the S.015 design to every base and ideology basename. That is the exact source-to-consumer contradiction to repair.

## Exact owner patch

1. Keep the current reviewed S.015 source package and attribution record, but stop treating `ASX.tga` as a universal historical or neutral Sicilian flag.

2. Add one parent-approved cosmetic tag whose basename ends in `X` for the constitutional route. Recommended stable basename, pending parent approval, is `ASX_INDEPENDENCE_WAVE_CONSTITUTIONALX`; its runtime files would be `gfx/flags/ASX_INDEPENDENCE_WAVE_CONSTITUTIONALX.tga`, `gfx/flags/medium/ASX_INDEPENDENCE_WAVE_CONSTITUTIONALX.tga`, and `gfx/flags/small/ASX_INDEPENDENCE_WAVE_CONSTITUTIONALX.tga`. The current parent/runtime basename remains `ASX` until that owner decision is made.

3. In the parent-owned ASX route installation, set that cosmetic tag only when `has_independence_wave_constitutional_route = yes` and clear it when the route changes or the country is removed. Do not silently copy the S.015 triplet to labor, traditional-crown, emergency-military, patron-client, fascist, or generic neutrality consumers.

4. Give every other ASX route either its own sourced/generated and separately documented flag family or an explicit `needs_user_review` gate. Do not use the current S.015 triplet as a historical substitute for those routes.

5. Reconcile the two package manifests and hash ledgers after the owner selects the final runtime basename. The later FORM-05 manifest records the current small TGA hash `8b9158f6defc4408683a369d5a2cd10aa846ac0fb1ca0bafe63441892803c425`, while the earlier Mediterranean package ledger records a superseded small hash; the final owner patch should leave one authoritative source-of-truth row and preserve the historical package hashes as dated evidence.

## Disposition

Status: **needs_owner_review / blocked for universal runtime use**.

The ASX source, processed PNG previews, current TGA ladder, dimensions, rights notes, contact sheets, and package handoffs already exist. No new image generation or historical web research is required for this gap. Completion requires the parent to resolve route ownership and update the consumer/manifests; this audit does not claim live rendering or gameplay validation.

