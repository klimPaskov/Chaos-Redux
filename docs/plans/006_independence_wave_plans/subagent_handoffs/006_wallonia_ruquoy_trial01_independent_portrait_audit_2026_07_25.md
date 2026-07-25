# Event 006 AFX Wallonia Louis Ruquoy trial 01 independent portrait audit

Audit date: 2026-07-25.

Reviewer mode: independent read-only sourced-visual, provenance, likeness, and consumer-boundary audit; the candidate producer did not approve this result.

The audited candidate is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_25/wallonia_ruquoy_trial_01/`.

The linked source-clearance and corroboration package is `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_commander_retry_03/`.

Source-candidate disposition: **PASS for all independent source, crop, identity, style, framing, role, ownership-search, and forbidden-derivative gates; parent-owned DDS conversion and runtime promotion remain conditional on consumer identity reconciliation.**

No DDS, `.gfx`, gameplay, localisation, runtime, or candidate asset was edited by this audit.

## Scope and separate verdicts

I compared the unchanged Agence Rol/BnF master, explicit crop and equality JSON, raw ImageGen result, deterministic `156x210` candidate, processing metadata, commander review sheet, corroborating *Le Pays de France* and *Le Miroir* sources, and the canonical commander references at native size and temporary `4x` nearest-neighbour enlargement.

| Gate | Verdict | Independent finding |
| --- | --- | --- |
| Provenance, public-domain status, and attribution | **PASS** | The immutable master is the unchanged `8419x6051` Agence Rol press photograph from Bibliotheque nationale de France, Gallica item `btv1b531010537`, dated 12 March 1923. The retained Commons API and page snapshots identify `Agence Rol. Agence photographique (commanditaire)`, credit BnF, and mark the image Public domain under PD France, PD-1996, and PD US expired. The preserved attribution is `Agence Rol / Bibliotheque nationale de France, Gallica, item btv1b531010537.` The archive title/default caption foregrounds Henri Maglinse, but the full caption order identifies the center figure as general Rucquoy; that uncertainty is explicitly retained rather than hidden. |
| Grounded male-subject compliance | **PASS** | The master, crop, raw repaint, and processed candidate each show the same single adult male. The character definition sets `gender = male` and only full `civilian.large` and `army.large` slots for `AFX_walloon_reserve_commander`; no female metadata, female name pool, advisor card, or opposite-gender pairing is present. |
| Hainaut/Walloon identity and commander-role fit | **PASS with retirement caveat** | The retained French-language identity snapshot records Louis Hubert baron Ruquoy/Rucquoy as born 3 November 1861 at Frasnes-lez-Buissenal in Hainaut, a Belgian lieutenant-general who commanded the 5th Army Division and became Chief of the General Staff on 6 January 1917. He was alive throughout 1936 but pensioned on 1 January 1927. The candidate therefore fits a senior Walloon Defence Council veteran, reserve, or strategic-security commander abstraction; it must not be described as an active 1936 General Staff appointment or a documented historical 1936 Walloon government office. |
| Explicit head-and-shoulders crop and decoded equality | **PASS** | The trial crop is `1750x1900` from half-open master rectangle `(3300,1000,5050,2900)`. Independent Pillow comparison against the trial master produced `decoded_pixels_equal = true`, zero differing pixels, and shared RGBA digest `ed034beac18575bf34e9d4f3801698846256e50caa89106e2f36eb17910be58d`. The trial master, crop, and JSON are byte-identical to the corresponding source-clearance files, even though the normalized JSON command records the clearance-package paths. No resize, retouch, recolour, or replacement was found in the immutable crop. |
| Identity and strict likeness preservation | **PASS** | Native and temporary `4x` nearest-neighbour comparison of the unchanged master, exact crop, raw repaint, and processed candidate preserves the locked broad square head, high forehead under the cap, heavy brows, hooded eyes and source gaze, broad nose, very broad upturned handlebar moustache, full cheeks and jowls, broad jaw and rounded chin, unequal ears, near-frontal/slight offset, stern expression, cap, collar, shoulders, and source-visible uniform. The LPDF frontal crop corroborates the same cap, broad face, ears, eyes, nose, and moustache; the *Le Miroir* profile crop corroborates the nose, cheek/jowl, jaw, moustache, cap, and period uniform geometry. No genericization, beautification, symmetrization, face substitution, hidden invented facial detail, de-aging, or identity-bearing pose replacement was observed. Identity was judged independently and was not compensated by style quality. |
| HOI4 painted army-commander style | **PASS** | The raw result is a genuine restrained painted repaint rather than a filtered or merely resized photograph. The candidate has subdued oil/gouache brush texture, muted interwar Belgian military palette, quiet dark background, readable face at runtime size, and period commander seriousness. The canonical `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png` references establish the family; the candidate's darker background and uniform remain within that commander style band. There is no text, watermark, UI border, modern prop, photorealistic finish, dossier frame, or extra subject. Source-visible cap, collar, sleeve, and uniform markings are retained without a separate invented emblem or unsupported role costume. |
| Full-size commander framing and processing | **PASS** | `processed_png/portrait_AFX_walloon_reserve_commander.png` decodes as opaque RGBA `156x210`, with complete cap, head, neck, both shoulders, upper torso, safe top and side margins, and no frame or dossier treatment. The processor metadata records version `5.0`, `role_family = commander`, `source_kind = real`, deterministic `156x210` output, and `candidate_requires_visual_approval` before this independent audit. |
| Ownership search and stable AFX consumer mapping | **PASS with parent reconciliation** | The source ownership audit searched `Louis Hubert Ruquoy`, `Louis Rucquoy`, `Louis Ruquoy`, `Ruquoy`, and `Rucquoy` across current Chaos Redux, installed vanilla, Kaiserreich `1521695605`, and approved references `2265420196` and `1458561226`; no live character, leader, commander, operative, portrait, GFX, or localisation owner was found. The existing consumer is unambiguous: `history/countries/AFX - Wallonia.txt:18` recruits `AFX_walloon_reserve_commander`; `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-62` defines the male character with the existing full `civilian.large` and `army.large` sprite; and `interface/006_independence_wave_region_01_portraits.gfx:14-15` maps `GFX_portrait_AFX_walloon_reserve_commander` to the stable runtime texture path. The parent must reconcile `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4`, which still displays `Marcel Delcourt`, before showing this portrait under Ruquoy. No guarded transfer is required for the researched person because the ownership search found no existing Ruquoy/Rucquoy owner. |
| Forbidden advisor, dossier, operative, `_small`, female, generic, and fallback derivatives | **PASS** | The trial directory contains only the prompt, manifest, source master, exact crop and JSON, raw ImageGen result, deterministic full portrait and metadata, and commander review sheet. No file or reference contains `advisor`, `dossier`, `operative`, `_small`, `female`, `generic`, or `fallback`; the processor metadata has `role_family = commander`, `face_box = null`, `advisor_composition = null`, and `advisor_validation = null`. The candidate is a full commander texture and not a resized or relabelled small surface. |
| Conversion and runtime promotion readiness | **PASS for parent-owned conversion; runtime conditional** | The candidate is an opaque, valid `156x210` commander PNG and no DDS exists in the trial package. The parent may run the repository `convert_to_dds.py` workflow only after updating the player-facing token to Ruquoy, preserving the source attribution in durable documentation, and completing the fresh IW-006 country-package audit. The existing DDS at `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` is a prior runtime artifact with SHA-256 `C75E081B57EAC880A55772B96AC0D0A77E4B5FA2BA2CCE74A4D46A46F17EDE9A`; it is not this candidate and was not approved or modified by this audit. |

All source-only portrait gates pass. The only remaining promotion condition is parent-owned consumer reconciliation so the stable AFX token cannot present Ruquoy's face under the stale `Marcel Delcourt` display name.

## Visual comparison evidence

The retained processor sheet is `review/AFX_louis_ruquoy_commander_style_sheet.png` (`1344x464`, SHA-256 `D835EAE207E0294A77FE0411E4FC7BF126F8AFB2B0685A28FBCA3DC7C7C7DCCC`). Its first panel is the processor input crop of the raw ImageGen result rather than the immutable archival crop, so it was not treated as provenance evidence.

I separately inspected the unchanged `8419x6051` master, `1750x1900` exact crop, `1080x1456` raw repaint, `156x210` candidate, the LPDF and *Le Miroir* masters and exact crops, the source-comparison contact sheet, and both canonical commander references at native size.

I also inspected temporary `4x` nearest-neighbour enlargements of the master, crop, raw result, candidate, Montgomery reference, and Witzleben reference outside the repository, then removed those temporary files. No comparison image was added to the trial package or used as a runtime asset.

The retained source-comparison sheet is `docs/assets/006_independence_wave/sourced_portrait_clearance_2026_07_25/walloon_commander_retry_03/contact_sheets/ruquoy_commander_source_comparison.png`. The retained coordinate and corroboration grids are `ruquoy_rol_grid.png` and `ruquoy_miroir_grid.png` in that same clearance package.

## Exact artifact hashes and reference controls

| Artifact | Dimensions | SHA-256 |
| --- | ---: | --- |
| Immutable Agence Rol/BnF master | `8419x6051` | `BF11028C9B7DA593062F4EB8730417C760748D10A5C6DE8493CBBB8BC667C7AC` |
| Trial exact crop | `1750x1900` | `4AAF3591D040A9E6423803715404030148A2FCB0CC38801118BCE9C398B6CA6A` |
| Trial crop-equality JSON | schema 1 | `20E883A2F308F583FB71667D02479B1D873508E87AA8A02F8DD170A9239744E9` |
| Raw ImageGen repaint | `1080x1456` | `332B6AC29CB09ECB9D339B18914B5E6CC60006A9A17DF371DE57E898C4B2B624` |
| Deterministic processed candidate | `156x210` | `FAFFBFE12921431353C962215C04F8E69FF40B8CAA083C61FC8F46719A477EC0` |
| Candidate processing metadata | schema 5 | `11744FC9D2653B18B9F022826B26ECB304529B9A265B4292EB5C5405CE7C1F57` |
| Commander review sheet | `1344x464` | `D835EAE207E0294A77FE0411E4FC7BF126F8AFB2B0685A28FBCA3DC7C7C7DCCC` |
| Prompt | markdown | `FFC4D0920B694972C2BCF841597E8079CA345A9F1DF09A799371845472192B42` |
| Canonical commander `eng_bernard_montgomery.png` | `156x210` | `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` |
| Canonical commander `ger_erwin_von_witzleben.png` | `156x210` | `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6` |

The trial master, crop, and equality JSON are byte-identical to `source_masters/ruquoy_rol_1923_group.jpg`, `source_crops/ruquoy_rol_1923_head_shoulders.png`, and `source_crops/ruquoy_rol_1923_head_shoulders.json` in the clearance package. The selected clearance source hash is `BF11028C9B7DA593062F4EB8730417C760748D10A5C6DE8493CBBB8BC667C7AC`, and the selected source API snapshot records SHA-1 `5a6b5182b300f19424430db751dfb7fcc3d9c0c3`, `8419x6051`, and Public domain.

The corroborating LPDF master is `202x360`, SHA-256 `068BBB3DD518FD6A9FFF0B7B63E5891C8483DBBAC265D12AB1342140F9F55352`, with an exact `172x273` crop and CC BY-SA 3.0 Garitan attribution. The corroborating *Le Miroir* master is `3036x3769`, SHA-256 `CCFDEDFBE71F66B612E235AEA0F637A35F5DF06687EDCA70A49F9F7CC59611AB`, with an exact `750x1450` crop; its Commons page carries a disputed-copyright-information warning, so it remains comparison evidence only and is not the selected identity or rights source.

## Runtime and ownership boundary

The stable AFX character token remains `AFX_walloon_reserve_commander`, recruited from `history/countries/AFX - Wallonia.txt:18` and defined as a male corps commander and country-leader-capable character in `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-75`.

The stable sprite remains `GFX_portrait_AFX_walloon_reserve_commander` in `interface/006_independence_wave_region_01_portraits.gfx:14-15`, with reserved runtime texture `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds`.

The current localisation key `AFX_walloon_reserve_commander` still identifies Marcel Delcourt. Parent-owned integration must rename that display identity to Louis Hubert baron Ruquoy/Rucquoy and preserve the retirement/alternate-history caveat before the candidate is shown in game; this audit makes no such edit.

No advisor, dossier, `_small`, operative, gameplay, GFX, localisation, or unrelated Event 006 asset was created or changed.

## Promotion decision

**Promotion authorized for this candidate's source-only image gates:** the independent likeness, strict feature-lock, HOI4 commander-style, provenance/rights/attribution, exact-crop equality, role, stable-consumer mapping, and forbidden-derivative gates pass.

**Promotion remains conditional at the consumer boundary:** before DDS conversion and runtime replacement, update the parent-owned localisation and durable identity documentation so the stable AFX token names Louis Hubert baron Ruquoy/Rucquoy and uses the documented retired-veteran Walloon commander abstraction. Then run the fresh IW-006 country-package audit and prove the converted DDS against this exact PNG.

No fallback portrait, raw-photo resize, generated generic face, opposite-gender pairing, advisor card, `_small` derivative, or unrelated consumer substitution is authorized by this audit.

## Simplifications, omissions, and blockers

No visual or provenance simplification was made and no requested source-only evidence was omitted.

The source candidate is not blocked by rights, crop equality, likeness, role fit, style, framing, ownership search, or forbidden-derivative checks.

The sole parent-owned promotion condition is the stale `Marcel Delcourt` localisation/identity reconciliation on the stable AFX token; no gameplay, GFX, localisation, DDS, or runtime file was touched here.
