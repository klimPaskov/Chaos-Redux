# Event 006 IW-009 Bavaria Friedrich Dollmann trial 03 independent portrait audit

Audit date: 2026-07-24.

Reviewer mode: independent read-only visual and provenance audit; the candidate producer did not approve this result.

## Scope and disposition

The audited candidate is `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/bavaria_dollmann_trial_03/`.

The linked immutable identity package is `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/bavaria_dollmann_source_retry/`.

The exact source crop and equality evidence are retained in `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/bavaria_dollmann_trial_02/source_crops/`.

The candidate is **APPROVED for parent-owned standard DDS conversion and runtime promotion after the consumer-localisation reconciliation noted below**.

No DDS, `.gfx`, runtime, gameplay, localisation, or candidate asset was edited by this audit.

## Separate verdicts

| Gate | Verdict | Independent finding |
| --- | --- | --- |
| Likeness and identity preservation | **PASS** | Native and 4x nearest-neighbour comparison of the unchanged master, exact crop, raw repaint, and processed candidate preserves Dollmann's long narrow face, close-set eyes, round wire spectacles, straight narrow nose, thin mouth, visible ears, age, serious expression, frontal/slightly off-axis pose, and source asymmetry. The candidate is still recognisably the same specific man rather than a generic officer. The cap shadow and low-resolution source soften some eye detail, but no face substitution, beautification, de-aging, genericization, or identity-bearing pose replacement was observed. Identity was judged independently and was not compensated by style quality. |
| HOI4 painted commander style and 156x210 framing | **PASS** | The raw repaint is a genuine restrained oil/gouache-style repaint rather than a filtered or merely resized photograph. The deterministic candidate is opaque `156x210`, head-and-shoulders, readable at native size, and visually consistent with the commander family represented by `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`. It has controlled painterly texture, a quiet period background, no UI frame, no text, no watermark, and no dossier-card treatment. The dark background and muted uniform differ from the lighter canonical references but remain within the HOI4 commander style band. |
| Provenance, rights, ownership, attribution, and evidence integrity | **PASS** | The unchanged master is the German Federal Archive image `Bundesarchiv, Bild 101I-052-1435-20`, with the Wikimedia record, official archive search record, `CC BY-SA 3.0 Germany` license, and required attribution `Bundesarchiv, Bild 101I-052-1435-20 / CC-BY-SA 3.0` retained in the linked source package. The master SHA-256 is `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12`. The exact crop rectangle is `(300,120)-(500,450)` against the `533x800` master. The trial-02 crop SHA-256 is `D3A70235D56B6E8255AF31BD8330975BD1FC42370D1278272262EE210B9CDF97`, the equality JSON SHA-256 is `6D87A0BA4C7494069D16F16A7D58AA7D62574266629F4A431AA0F0DF861991D8`, and the equality record reports `decoded_pixels_equal = true` with shared RGBA SHA-256 `1C910471860E2EDE9F5B446613FD419C24AFED8F60CC500337645181240FBFE9`. The source-package crop has a different PNG byte hash (`C19C7D634EE585CB32853ED1A0F28BC4D37724AEAC2F58FF2509E20DE6C9B071`) but direct Pillow comparison reproduced identical decoded RGBA pixels and the same master-rectangle hash, so there is no crop-pixel drift. The ownership scan found no Dollmann/Dollman character, recruitment, portrait, GFX, or localisation owner in current Chaos Redux, installed vanilla, or approved reference mods, and no transfer guard is needed. |
| Plausible role and stable consumer fit | **PASS with parent reconciliation** | Friedrich Karl Albert Dollmann is a real male Bavarian/German officer alive in 1936, and the documented alternate role `Bavarian Emergency Passes-and-Depots Commandant` is a defensible territorial-command abstraction rather than a claim of historical Gebirgstruppe service. The candidate maps cleanly to `BAY_independence_wave_mountain_commandant`, `GFX_portrait_BAY_independence_wave_mountain_commandant`, and the reserved full-size runtime texture `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`. The current parent-owned localisation still labels that key `Eugen Ritter von Schobert`; parent must change the display name and descriptor to Dollmann (or explicitly reject Dollmann as the selected identity) before promotion so the portrait cannot be shown under the wrong person. |
| Forbidden Event 6 advisor or `_small` assets | **PASS** | The trial-03 candidate package contains only the raw repaint, full `156x210` processed portrait, processor metadata, prompt, and commander review sheet. No advisor, high-command, officer-corps, dossier-card, operative, or `_small` derivative exists in trial 03, trial 02, or the linked Dollmann source/ownership package. The processor JSON has `role_family = commander`, `face_box = null`, `advisor_composition = null`, and `advisor_validation = null`, consistent with a full commander texture rather than an advisor card. |
| DDS and runtime promotion readiness | **PASS for conversion; runtime promotion conditional** | The candidate is a valid opaque RGBA `156x210` commander PNG with file SHA-256 `485F725555C9D6C71FCFA62742F6B724630E8573F874590C552643B6DF63D9E9`, decoded RGBA SHA-256 `4F5D42E55CE9183996BE4FCB26E6EC8873510783CC7D2D65E2A600AFBBD484C8`, and alpha range `255..255`. The stable sprite and reserved runtime texture are already documented and the `.gfx` consumer path is unchanged. No DDS exists in the candidate package, as required before independent approval. The parent may run the repository `convert_to_dds.py` workflow and wire the existing sprite only after reconciling the stale Dollmann/Schobert localisation identity and preserving the source attribution in durable documentation. |

## Visual comparison evidence

I inspected the unchanged `533x800` master, the `200x330` exact crop, the `977x1609` raw ImageGen repaint, the `156x210` processed candidate, the retained commander review sheet, and both selected canonical commander references at native size.

I also inspected temporary 4x nearest-neighbour copies of the master, exact crop, raw repaint, candidate, Montgomery reference, and Witzleben reference; those temporary files were created outside the repository and were not added to the candidate package.

The retained processor sheet is `review/BAY_friedrich_dollmann_commander_style_sheet.png`, `1344x464`, SHA-256 `DFE235A21279B827218A6D9F8C805A7D653289E20B0FD9B58C10032C8145E965`.

The sheet shows the processor input crop, candidate, Montgomery, and Witzleben at a review scale; the independent audit still compared the immutable master and exact crop separately rather than treating the processor sheet as provenance evidence.

The raw ImageGen result is SHA-256 `47D143EE3537DF7060B43EAE88C23CFBF03BDCDB900DBF9CF500949784EAD64D`.

The candidate's processor metadata records processor version `5.0`, role family `commander`, source kind `real`, processor crop `(70,80)-(954,1270)`, Python `3.9.12`, Pillow `11.1.0`, and `candidate_requires_visual_approval` before this audit.

## Exact artifact hashes and reference controls

| Artifact | Dimensions | SHA-256 |
| --- | ---: | --- |
| Immutable Bundesarchiv master | `533x800` | `15D387707C22E7B73B513961AAE7EB42F40E3E296FF4A68E8AAB6B5DA6E82E12` |
| Trial-02 exact crop used as identity input | `200x330` | `D3A70235D56B6E8255AF31BD8330975BD1FC42370D1278272262EE210B9CDF97` |
| Exact-crop equality JSON | schema 1 | `6D87A0BA4C7494069D16F16A7D58AA7D62574266629F4A431AA0F0DF861991D8` |
| Raw ImageGen repaint | `977x1609` | `47D143EE3537DF7060B43EAE88C23CFBF03BDCDB900DBF9CF500949784EAD64D` |
| Deterministic processed candidate | `156x210` | `485F725555C9D6C71FCFA62742F6B724630E8573F874590C552643B6DF63D9E9` |
| Candidate processing metadata | schema 5 | `7EEFCE17170EE5180A1CC1D09D39B2622D47FFBAE1424E6836A68C81914EA43C` |
| Commander review sheet | `1344x464` | `DFE235A21279B827218A6D9F8C805A7D653289E20B0FD9B58C10032C8145E965` |
| Canonical commander `eng_bernard_montgomery.png` | `156x210` | `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` |
| Canonical commander `ger_erwin_von_witzleben.png` | `156x210` | `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6` |

## Runtime and ownership boundary

The stable character token remains `BAY_independence_wave_mountain_commandant` and is generated as a male country leader/corps commander in `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`.

The stable sprite remains `GFX_portrait_BAY_independence_wave_mountain_commandant` in `interface/006_independence_wave_region_01_portraits.gfx`, with the reserved runtime texture `gfx/leaders/006_independence_wave/portrait_BAY_independence_wave_mountain_commandant.dds`.

The current localisation key `BAY_independence_wave_mountain_commandant` and descriptor still identify Eugen Ritter von Schobert, which is the sole parent-owned integration blocker recorded by this audit.

No advisor, dossier, `_small`, operative, gameplay, or unrelated Event 6 asset was created or changed.

## Promotion decision

**Promotion authorized for this candidate's image gates:** the independent likeness, HOI4 commander-style, provenance/rights/equality, role, and derivative-boundary gates pass.

**Promotion remains conditional at the consumer boundary:** before DDS conversion and runtime replacement, update the parent-owned localisation and any durable identity documentation so the stable BAY token names Friedrich Dollmann and uses the documented territorial-command caveat.

If the parent keeps the Schobert identity, this Dollmann candidate must be rejected from that consumer rather than shown under the wrong name; no silent identity substitution is authorized.

No fallback portrait, raw-photo resize, advisor card, `_small` derivative, or gameplay substitution is authorized by this audit.

