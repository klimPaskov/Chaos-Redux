# IW-179 FSM Micronesia Kabua Kabua source-closure handoff

Status: **BLOCKED / no production-safe grounded portrait source**.

## Scope and package boundary

This bounded pass covers only sourced visual evidence for `FSM_independence_wave_inter_island_congress_chair` / `GFX_portrait_FSM_independence_wave_inter_island_congress_chair`.

No gameplay, map, host-survival, focus, decision, mission, AI, FORM-48, character, localisation, interface, GFX, ImageGen, crop, processed PNG, DDS, or runtime file was edited.

The existing fictional Elias Kihleng portrait remains untouched and must not be promoted as a grounded replacement.

The prior package audit `subagent_handoffs/006_event6_fsm_micronesia_civic_source_clearance_2026_07_24.md` remains the source of truth for the already-implemented gameplay surfaces and their withdrawn visual admission.

## Candidate evaluated: Kabua Kabua

Kabua Kabua (c. June/July 1910–8 October 1994) was a Marshallese paramount chief (`Iroijlaplap`) and jurist.

The identity and role lead is [Kabua Kabua](https://en.wikipedia.org/wiki/Kabua_Kabua), which records that he served as a leading judge from the 1930s, became chief magistrate of Jaluit in 1937, and later served in the Congress of the Marshall Islands and as president of its Council of Iroij.

Micronesian Seminar independently captions a later corroborating photograph as [Kabua Kabua addressing the first Marshall Islands Congress in 1953](https://micsem.org/media/photos/tranquil_50/33.htm), credited to the Guy Howe Collection.

This makes him a strong adult-male, Micronesian, inter-island-government/congress-chair analogue for a 1936 alternate-history civic role, but he is Marshallese rather than Pohnpeian or Caroline-Islander.

## Archival source record

The [Micronesian Seminar photo-search record](https://micsem.org/library/search-photos-results?subject=Kabua%20Kabua) identifies `RR01026` as “From L-R: Carl Cominic, Kabua Kabua, Zebedy Tarkwon, ?” from the Robert Reimers Collection, dated c1930.

The record labels the object `Digital, Not Restricted` and names Kabua Kabua in the image, but it is a four-person group photograph rather than an attributable head-and-shoulders portrait.

The publicly retrievable image is the [MicSem proxy thumbnail](https://micsem.org/library_img/photo/thumbnails/rr/01/rr_01_026_tmb.jpg), which is 120×91 RGB JPEG, SHA-256 `1EA0E66227A54E56F403F1E1F3A1F627E158BD24508D7C5F653E9FA8F749C812`.

The search page points at the original host path `https://micronesian.matrixmarketers.com/library_img/photo/thumbnails/rr/01/rr_01_026_tmb.jpg`, but the matrixmarketers host was unreachable during this pass; only the MicSem proxy thumbnail could be downloaded.

Guessed full-size path families on the MicSem host returned 404, and no public object record or original scan was exposed.

## Gate review

| Gate | Result | Evidence and disposition |
| --- | --- | --- |
| Attributable real male identity | **Lead only** | The record names Kabua Kabua and places him second from left, while the c1930 group image does not provide an individual portrait. |
| Adult and 1936 plausibility | **Pass as role lead** | Born c1910, so approximately 20–26 during the c1930–1936 window; his documented judging and later Congress/Council of Iroij service make the alternate congress-chair role institutionally plausible. |
| Regional fit | **Needs review / weak** | Marshallese is Micronesian and the civic role is closely analogous, but FSM IW-179 is anchored on the Caroline Islands and Pohnpei/Carolinian identity remains preferred. |
| Period fit | **Promising but incomplete** | The object is dated c1930, before the 1936 world state; no exact capture date or photographer credit is supplied beyond the Robert Reimers Collection. |
| Source resolution and crop gate | **Fail** | 120×91 thumbnail, four-person composition, and no retrievable original cannot support the unchanged-source head-and-shoulders crop, decoded-pixel JSON equality proof, or independent likeness audit. Do not upscale or feed this thumbnail to ImageGen. |
| Reuse rights | **Unresolved** | “Not Restricted” is catalog metadata only; no explicit license or written reuse permission was found, and MicSem footer wording says © 2010–2019 all rights reserved. Treat this as a rights-clarification lead, not a production license. |
| Grounded portrait source mode | **Blocked** | Identity, source resolution, and rights are not jointly cleared; no generated, generic, female, or fallback portrait is allowed. |

## Existing corroborating image (not a production source)

MicSem's [1953 Congress page](https://micsem.org/media/photos/tranquil_50/33.htm) serves a 230×454 color image at `https://micsem.org/media/photos/tranquil_50/photos/33_02.jpg` and captions Kabua addressing the first Marshall Islands Congress.

That later image corroborates the institutional role and identity but is postwar, low resolution, and carries no explicit reuse license beyond the site context, so it is not an accepted 1936 portrait source.

## Downstream package state

No immutable full-resolution source master, explicit crop coordinates, exact-crop JSON, source-locked repaint, processed 156×210 PNG, independent likeness/style/provenance audit, DDS, contact sheet, or `gfx_handoff.md` was produced for Kabua Kabua.

No sprite name or runtime path is approved.

Do not alter the current FSM character, portrait, GFX, localisation, or runtime binding on the basis of this candidate.

## Required next input

Promotion requires either a repository-supplied full-resolution `RR01026` original with written reuse permission or an explicit reusable license, or a different named adult male Pohnpeian/Carolinian/Micronesian civic or traditional figure with an attributable archival image and defensible rights.

If MicSem supplies the `RR01026` original and permission, preserve the immutable source, run the exact head-and-shoulders crop/equality gate, obtain an independent likeness/style/provenance PASS, and only then continue to deterministic HOI4 processing and DDS conversion.

Until that evidence arrives, IW-179 remains visually **BLOCKED / fail-closed** and no package admission or FORM-48 readiness change is justified.

## Files and evidence retained

- `docs/assets/006_event6_micronesia_civic_source_clearance/source/rr_01_026_tmb.jpg` — downloaded MicSem proxy thumbnail, 120×91, SHA-256 `1EA0E66227A54E56F403F1E1F3A1F627E158BD24508D7C5F653E9FA8F749C812`; rejected evidence only.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw179_micronesia_kabua_kabua_source_closure_2026_08_01.md` — this source handoff.

