# IW-008 Rhineland river commandant sourced portrait retry

This package is a source-only retry for the grounded male `RHI_independence_wave_river_commandant` commander and country-leader portrait slot.

The selected identity is Gustav-Adolf von Zangen (7 November 1892 to 1 May 1964), a real German male officer who was alive and usable in the 1936 setting.

The source mode is `grounded_source_only` and `internet source image` because Rhineland is a grounded historical polity and the identity must remain a sourced real person.

The package is `needs_user_review` for the downstream identity-preserving HOI4 repaint and independent likeness/style/provenance audit, and it is not runtime-complete.

No ImageGen result, processed 156x210 candidate, DDS, `.gfx` edit, gameplay edit, localisation edit, or fallback was created in this retry.

## Candidate and role fit

Gustav-Adolf von Zangen is materially better role-fit than the rejected Josef Harpe trial because he served in the 9th Rheinische Infanterie-Regiment Nr. 160 from 1911 and later commanded the 15th Army on the Western Front and in the Netherlands.

His documented Westfront command and later retreat toward the Rhine provide a direct river-corridor and territorial-army connection for the emergency Rhenish commandant role, while the scenario only requires that the real man be alive and usable around 1936 rather than historically hold this alternate office.

The Federal Archives biographical record states that Zangen entered Wehrmacht service in 1936 and later held repeated troop commands, which keeps the identity period-usable without asserting that he historically commanded the fictional RHI government.

The source photograph is from November 1944 and therefore postdates the 1936 start, so the date is disclosed and the later uniform, decorations, and visible Nazi insignia are source evidence only.

The downstream portrait repaint must preserve Zangen's face and source-supported pose while neutralising unsupported or route-inappropriate insignia before any runtime admission.

## Immutable source master

| Field | Value |
| --- | --- |
| Path | `source_masters/RHI_gustav_adolf_von_zangen_bundesarchiv_1944.jpg` |
| Source page | <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_183-H28061,_Westfront,_Gustav_v._Zangen,_Albert_Speer.jpg> |
| Direct original | <https://upload.wikimedia.org/wikipedia/commons/9/99/Bundesarchiv_Bild_183-H28061%2C_Westfront%2C_Gustav_v._Zangen%2C_Albert_Speer.jpg> |
| Archive record | Bundesarchiv Bild 183-H28061, Westfront, Gustav v. Zangen, Albert Speer |
| Archive/provider | German Federal Archive (Deutsches Bundesarchiv), source collection Bild 183 Zentralbild |
| Photographer | Unknown author (`o.Ang.` in the archive metadata) |
| Source date | November 1944 |
| Original dimensions | `548x800` |
| Decoded mode/format | `L` grayscale JPEG |
| File size | `65,708` bytes |
| SHA-256 | `B3A829FC739F43262057C91F146FF03561508708208C6F350A36158D4AF78C0D` |
| Rights | CC BY-SA 3.0 Germany as recorded by Wikimedia Commons |
| Attribution | `Bundesarchiv, Bild 183-H28061 / CC-BY-SA 3.0` |
| License URL | <https://creativecommons.org/licenses/by-sa/3.0/de/deed.en> |
| Authenticity note | Wikimedia Commons records that the Federal Archive provided the image and guarantees an authentic representation from the original negative or positive or its digitisation. |

The unchanged JPEG is retained byte-for-byte from the direct Wikimedia Commons original and is not recoloured, retouched, resized, or overwritten.

## Explicit head-and-shoulders crop

| Field | Value |
| --- | --- |
| Path | `source_crops/RHI_gustav_adolf_von_zangen_head_shoulders.png` |
| Source master | `source_masters/RHI_gustav_adolf_von_zangen_bundesarchiv_1944.jpg` |
| Crop coordinates | `(left=180, top=140, right=365, bottom=330)` in source-master pixels |
| Crop dimensions | `185x190` |
| Decoded mode/format | `L` grayscale PNG |
| File size | `22,211` bytes |
| SHA-256 | `FC9C5F986F37C4F040A31F909FD5C03AF6C594D54BE295CA25373EAEC82C4D38` |
| Crop method | Direct source-pixel crop with Pillow `Image.crop`, no resampling, retouching, recolouring, or face alteration |
| Intended use | Immutable identity reference for the future HOI4 commander-family repaint and likeness review |

The crop is an explicit source-pixel head-and-shoulders evidence crop and is not a final runtime portrait.

## Ownership gate

The exact and variant searches used `Gustav-Adolf von Zangen`, `Gustav Adolf von Zangen`, `Gustav Adolf Karl Friedrich Ernst von Zangen`, `von Zangen`, `Zangen Gustav`, `Gustav_Adolf_von_Zangen`, `Gustav-Adolf_von_Zangen`, `gustav_adolf_von_zangen`, `gustav_von_zangen`, and `Gustav von Zangen`.

The roots checked in current Chaos Redux were `common/characters/`, `history/countries/`, `common/country_leader/` when present, `gfx/leaders/`, `interface/`, and `localisation/`.

The roots checked in installed vanilla were `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/`.

The roots checked in approved reference mod `1521695605` were its `common/characters/`, `history/countries/`, `gfx/leaders/`, `interface/`, and `localisation/` directories.

The roots checked in approved references `2265420196` and `1458561226` were the same character, history, leader, interface, and localisation directories.

All listed identity forms returned no exact or variant person-owner match in current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, `2265420196`, or `1458561226`.

No character definition, recruitment line, portrait texture, `.gfx` or interface consumer, leader/commander/operative officeholder consumer, or localisation owner was found for Zangen in those roots.

The same-person disclosure result is therefore no-hit in the approved reference mods, and no reference-mod art or source was copied.

This retry passes the subject-ownership gate for the requested stable RHI consumer, subject to rechecking before eventual runtime wiring.

## Stable consumer and processing boundary

The stable consumer remains character token `RHI_independence_wave_river_commandant` in `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`.

The consumer assigns the same full portrait to `civilian.large` and `army.large`, and no `_small`, advisor, dossier, high-command, theorist, operative, female, or alternate-country derivative is authorized.

The stable sprite is `GFX_portrait_RHI_independence_wave_river_commandant` in `interface/006_independence_wave_region_01_portraits.gfx`.

The reserved runtime texture path is `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds`, but this retry intentionally creates no DDS and does not change that file.

The future processor must use the unchanged source master and exact crop as identity inputs, compare against the canonical commander references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/`, produce a source-locked identity-preserving repaint, and stop for an independent likeness/style/provenance audit before conversion.

## Status and uncertainty

Status is `needs_user_review` rather than `complete` because the required ImageGen repaint and independent audit were explicitly out of scope for this source retry.

The source is high enough resolution for an attributed source master and clear face crop, but it is materially smaller than the rejected Harpe master at `548x800` and dates from November 1944 rather than the 1936 start.

The image visibly contains late-war uniform decoration and Nazi-era insignia, which must not be silently presented as 1936 route-authentic clothing or symbolism.

The source-rights chain is defensible under CC BY-SA 3.0 Germany, with attribution and license URL preserved above.

No simplification or fallback was used, and no runtime claim is made by this source-only package.
