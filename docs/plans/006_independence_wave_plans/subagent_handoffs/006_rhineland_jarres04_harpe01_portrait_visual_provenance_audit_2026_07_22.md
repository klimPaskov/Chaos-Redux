# Event 006 IW-008 Rhineland portrait visual/provenance audit

Date: 2026-07-22
Scope: independent source, provenance, identity, style, ownership, and runtime-consumer audit of the two named candidate packages.
Owned change: this handoff only. No source master, crop, ImageGen result, processed PNG, DDS, `.gfx`, character, gameplay, localisation, or manifest outside this file was changed.

## Decision summary

Both packages remain closed for runtime wiring. The archival identities and rights chains are defensible, and both candidate PNGs are the required full `156x210` portrait canvas, but neither candidate clears every independent gate.

| Subject / candidate | Source and role gate | Full-size and native visual gate | Ownership gate | Final audit status | Runtime action |
|---|---|---|---|---|---|
| Josef Harpe, `rhineland_harpe_trial_01` | **Pass with disclosed caveat.** Direct Bundesarchiv original, CC-BY-SA 3.0, real German Army General der Panzertruppe, born Buer/Gelsenkirchen. Source date is 1943, later than the 1936 scenario start. | **Needs revision.** The bald round head, ears, broad nose, full cheeks, rounded jaw, and controlled smile remain recognisable, and the upper-cap emblem neutralisation is visually credible. The repaint still opens/symmetrises the eyes, smooths the source face, uses a dark olive/high-texture treatment unlike the quiet canonical commander family, and introduces uncertain warm/gold colour into source-grayscale cockade/decorations. | **Pass for Harpe.** No exact or variant subject owner in vanilla, current Chaos Redux, Kaiserreich `1521695605`, `2265420196`, or `1458561226`. The current RHI token is the intended consumer, not a second historical Harpe owner. | **`NEEDS_REVISION`** | Do not convert or wire. Retain source and candidate evidence; revise the finish and decoration treatment, then repeat full/native likeness review. |
| Karl Jarres, `rhineland_jarres_trial_04` | **Pass with date note.** Bundesarchiv 1925 CC-BY-SA 3.0 primary, LOC Bain no-known-restrictions facial cross-check, Rhenish civic/constitutional role, alive in 1936. | **Needs revision.** Trial 04 is materially better than trial 01/refined 02/revision 03: the face is longer, the eyes lower and somewhat asymmetric, the nose/jaw/age/guarded expression are closer. It still leaves the tall curled hat carrying too much likeness, hides the high receding forehead, broadens/smooths the native face, and remains generic when the hat is discounted. | **Pass for current scope; disclosure recorded.** Kaiserreich actively defines, recruits, localises, and portrait-owns `GER_karl_jarres`, but the accepted mutually-exclusive-mod policy makes a cross-mod same-person hit non-binding when no source or art was copied. Vanilla and current Chaos Redux have no separate historical Jarres owner. | **`FAIL` (blocked)** | Do not convert or wire. Trial 04 remains blocked on full/native likeness; the Kaiserreich person-owner hit is disclosure-only and no source/art was copied. No fallback is authorised. |

`PASS` below means evidence is acceptable for that individual gate only; it is not runtime approval. The final status is fail-closed when any required gate remains unresolved.

## Canonical references inspected

The complete `chaos-redux-event-assets` skill and the canonical reference library were read before review. The canonical root README states that reference PNGs are style-only and never runtime inputs. The role families and exact files inspected were:

- Leader contact sheet: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/contact_sheet.png` — `1200x498`, RGBA, SHA-256 `8966ae351d1fe8fc13d47ca1c59ec3d8a34da9101ce5fd65f7acff3421bd0401`.
- Commander contact sheet (required because Harpe is also a corps commander): `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png` — `1200x498`, RGBA, SHA-256 `d62a4b80265533c93669a5eef267dff8db2021a01c1f31dcb73102bf1cc20ca9`.
- `portraits/leaders/fin_carl_mannerheim.png` — `156x210`, RGBA, SHA-256 `7e78e33e0b691b96b584393f2d363c07a302320f7e6300bda0fff261aa98d49e`.
- `portraits/leaders/den_thorvald_stauning.png` — `156x210`, RGBA, SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`.
- `portraits/leaders/ice_sveinn_bjornsson.png` — `156x210`, RGBA, SHA-256 `860726d268873f21ae0dbd6fb170482f50fad6393882b97b2b7b7a1814189d14`.
- `portraits/leaders/ire_eamon_de_valera.png` — `156x210`, RGBA, SHA-256 `ff5f8689f1e8ea75bf88bea4c4a87dcf60518b1e062ea53be4a9ceff3509dcb0`.
- `portraits/leaders/afg_mohammed_zahir_shah.png` — `156x210`, RGBA, SHA-256 `f606bc3c6204e0dbd35d8edceb21f87ae6f93a0ae7ad657382c7e9043e8907a0`.
- Commander family examples `portraits/commanders/generic_africa_land_1.png`, `_2.png`, and `_3.png` are each full `156x210` RGBA portraits with hashes `17d875344719b09a03ef32cc3329971778a738c4ac20210f6cbb7394a1e7585f`, `9b1f5a32d255bc605978733798422a6315cecc5702f6f579da1fa2e2a11fbd606`, and `76731af64301c3c68eee012a9eb9f001f4a11561e42bbb13cae0949ea5535b0b` respectively.

The candidate sheets use leader-family references. Harpe's role additionally requires review against the commander family; the absence of a commander-family panel in his own sheet is recorded as a review gap, not silently treated as a pass.

## Josef Harpe — trial 01

### Package evidence and exact file measurements

All paths below are relative to `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/rhineland_harpe_trial_01/`.

| Evidence | Actual dimensions / mode | File SHA-256 | Review note |
|---|---:|---|---|
| `source_masters/RHI_josef_harpe_bundesarchiv_original.jpg` | `4637x7455`, L; 7,356,362 bytes | `5353200abd3584c52a4938f2a79bf62c15d1be6aad22d70e0c45f1a4181c1384` | Unchanged direct Bundesarchiv master. |
| `source_crops/RHI_josef_harpe_head_shoulders.png` | `4457x6000`, L; 10,772,531 bytes | `43c0b9a2f23a2253be9f850eba816672574b5b239498e1b10f48554f2e41b5e2` | Explicit source-pixel head-and-shoulders crop `(90,0,4547,6000)` from the `4637x7455` master. |
| `source_crops/RHI_josef_harpe_head_shoulders_emblem_neutralized.png` | `4457x6000`, RGB; 13,770,069 bytes | `ea2156cd4c9bcfcf48881ee6004068e5b7d3eca0463a98c524cb240ba9edaa8a` | Separate moderation input only; not source/identity evidence and not a runtime asset. |
| `imagegen_results/RHI_josef_harpe_identity_preserve_trial_01.png` | `1082x1454`, RGB; 2,495,326 bytes | `7ad008e1de5a57f77d10d4fb44fc1afa76d3d6b451601ac6439b437a73086a8c` | Identity-preserving ImageGen edit of the neutralized crop, not a generated-from-text identity. |
| `processed_png/portrait_RHI_independence_wave_river_commandant.png` | `156x210`, RGBA; alpha min/max `255/255`; 62,064 bytes | `d32ab4e289cc4bb9b2e98add0947e388bfd14a3f1040f390253d4aadda755950` | Full leader/commander texture, opaque background, no `_small` or dossier derivative. |
| `contact_sheets/RHI_josef_harpe_full_source_result_comparison.png` | `1560x458`, RGB; 461,142 bytes | `a3461d383a8e6fb61780214e662a7adc33eb9e9cf6ceee307bfea6680a346ef7` | Panels: unchanged source, neutralized moderation crop, ImageGen result, native candidate, style reference. |
| `contact_sheets/RHI_josef_harpe_source_result_reference.png` | `1344x464`, RGBA; 729,317 bytes | `ea15febfa7ea96222785b1bf1204c3e9a0033263f251a8a0e83301de222d5fe1` | Panels: source crop, processed candidate, Stauning, Mannerheim. |
| `prompts/RHI_josef_harpe_identity_preserve_trial_01.txt` | 1,472 bytes | `18cecfe24f2b6ac05c10ab5c8e6eb0f522372988cb1e36527f54c999ade8428d` | Explicitly prohibits a political cap symbol, face replacement, beautification, de-aging, extra people, and advisor framing. |
| `metadata/RHI_josef_harpe_processing.json` | 5,314 bytes | `3fcda0cffdb4ce65029f5209a8d419282407907d1980df4bd1d6135df45ecb6a` | `advisor_icon_processing.py` v5.0, leader mode, `source_kind=real`, crop `(1,0,1081,1454)`, `face_box=null`, `status=candidate_requires_visual_approval`; output and review hashes match the PNGs. |

The metadata's processor hash is the current leader processor (`c6e78c01c025ad57fef8dc25eb79bd216ff9809df27e4c758eb9ec72594a3963`) and its leader render version is `2.0`; the advisor-only v5 overlay/provenance contract is not applicable to this full leader texture.

### Archival provenance, rights, date, and role

- Attribution page: <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_146-1981-104-30,_Josef_Harpe.jpg>.
- Direct archive original: <https://bild.bundesarchiv.de/device_barch/dev1/2022/11-28/b2/97/file7nthh588rkij6p2a22kj.jpg>.
- Credit: `Bundesarchiv, Bild 146-1981-104-30 / Hoffmann, Heinrich / CC-BY-SA 3.0`.
- Source date: 1943; Heinrich Hoffmann. This is later than the 1936 game start and must stay disclosed. The source is valid identity evidence, but the visible late-war cap/uniform/decoration treatment must not be presented as an exact 1936 photograph.
- Josef Harpe (1887–1968) was a real German Army General der Panzertruppe and army/corps commander, born in Buer (now Gelsenkirchen, North Rhine-Westphalia). The Rhenish-Westphalian birthplace gives a defensible regional connection; it is not evidence that he specifically commanded Cologne's river crossings in 1936.
- The rights chain is defensible and the unchanged master is retained. The neutralized crop is a safety/moderation derivative, not a claim that the archival source lacked the original cap emblem.

### Visual findings

#### Cap-emblem neutralisation and identity safety

The disclosed neutralisation is local and credible. The unchanged master and unaltered crop visibly retain the original upper-cap political eagle; only the separate moderation input covers that upper-cap area with a feathered plain-dark wool patch. The ImageGen result has a plain dark cap crown, retains the cap silhouette, lower wreath/cockade, shoulders, collar, and source-supported Iron Cross, and does not add a replacement political emblem, text, flag, or invented insignia. The neutralisation therefore preserves the identity-bearing face and military silhouette without laundering the source history.

The output is not yet safe for admission without one narrow correction: the source is grayscale, while the generated lower wreath/cockade and related decorations receive warm/gold (and possibly reddish) colour and slightly different shapes. Those values are not independently established by the retained source. Treat them as uncertain source-supported decoration rendering, not as proven historical colour. A revision should keep the lower cockade's visible geometry but use neutral charcoal/silver/sepia values unless a separate uniform source establishes the colours.

#### Face and style

- At full ImageGen size, Harpe remains recognisable from the bald round head under the cap, small uneven eyes, broad nose, full cheeks, rounded jaw/chin, ears, frontal pose, and controlled closed-mouth smile. This is materially better than a text-generated substitute and the face is not replaced by a second person.
- The face nevertheless becomes smoother and more symmetrical than the source: the eyes open/equalise, the nose narrows, and the smile is a little cleaner. At native `156x210` the face still reads, but the cap and uniform carry a substantial portion of the identity.
- The finish is genuinely painted, not a raw photograph or a simple resize, but it uses conspicuous cross-hatched brush texture, dark olive-brown grading, and hard facial modelling. This is materially heavier/darker than both the canonical commander contact sheet and the quiet pale warm-grey leader references. A revision should soften the texture, move the background/value range toward the canonical family, and preserve the source face rather than polishing it.
- The contact sheets prove a full-size/native comparison, but Harpe's review sheet only shows leader-family style references. Because his live consumer is also an army corps commander, a revision needs direct commander-family comparison before admission.

### Ownership and stable consumer audit

Searches were run case-insensitively for `Josef Harpe`, `Josef Friedrich Harpe`, `Harpe Josef`, `josef_harpe`, `josef_friedrich_harpe`, `Friedrich Harpe`, and relevant name-order/transliteration forms in:

- Current Chaos Redux `common/characters`, `history/countries`, `common/country_leader`, `interface`, `gfx/leaders`, and English localisation: no historical person-owner hit. The current RHI token/localisation is the requested target consumer, not a second Harpe identity.
- Installed vanilla `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/` equivalent character/history/interface/portrait/localisation roots: no Harpe owner hit.
- Kaiserreich `1521695605`, approved reference `2265420196`, and approved reference `1458561226`: no exact Harpe owner hit. Incidental `Harpe`/`Sharpeville` prose in non-character files was excluded as a literal-word false positive.

The stable intended Chaos Redux consumer is already declared but not admitted by this candidate:

- Sprite `GFX_portrait_RHI_independence_wave_river_commandant` and texture path `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds` are in `interface/006_independence_wave_region_01_portraits.gfx:32-33`.
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:248-269` generates `RHI_independence_wave_river_commandant`, creates a male corps commander, and assigns this same full portrait to both `civilian.large` and `army.large`. No `_small`, advisor, dossier, theorist, high-command, or female consumer is authorized.
- The candidate package contains no DDS. The existing runtime DDS is a stale historical treatment, not trial 01: `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_river_commandant.dds` is `156x210`, 131,168 bytes, one-level uncompressed BGRA, alpha `255..255`, SHA-256 `33dcc5595610ac7069e01d6c7c2515657c1fd93d921e55fe8b3707b7914f0d1a`, and decodes pixel-identically to the old rejected `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/processed_png/RHI_josef_harpe.png` (RGBA `156x210`, SHA-256 `fb1051de7f2fd0214e753e00b8675d72788528a1b33f8366347d33002eaad853`). Do not count that old runtime file as this candidate's approval.
- Protected `gfx/leaders/006_independence_wave/portrait_RHI_josef_friedrich_matthes.dds` remains present and hash-identical to the protected value `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2`; this audit did not modify it.

### Harpe disposition

**`NEEDS_REVISION`; no runtime advancement.** The cap-emblem neutralisation itself is defensible and does not invent a replacement political symbol. The candidate still needs a source-faithful neutral decoration pass, a quieter commander-family finish, and a fresh full/native likeness review that does not let the cap do the identity work. No fallback or invented Harpe is authorised.

## Karl Jarres — trial 04

### Package evidence and exact file measurements

All paths below are relative to `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/rhineland_jarres_trial_04/`.

| Evidence | Actual dimensions / mode | File SHA-256 | Review note |
|---|---:|---|---|
| `source_masters/RHI_karl_jarres_bundesarchiv_1925.jpg` | `562x800`, L; 38,735 bytes | `72c952b0f1a1e3c08a16b20c123466b4bfc737d7c03ae63594cf7e6332c2c8d6` | Unchanged primary period-attire master, Bundesarchiv Bild 102-01175. |
| `source_crops/RHI_karl_jarres_hat_coat_reference.png` | `285x385`, L; 41,811 bytes | `eee97623c3ad294a14a933b1ab6c896cadaac2e225ab95a8ceb68c7f3ba9fb9b` | Explicit `(145,80,430,465)` crop for the same man's felt hat, overcoat, collar, and tie. |
| `source_masters/RHI_karl_jarres_loc_undated.jpg` | `1024x734`, L; 104,205 bytes | `d07eb103f4c5fdf13ca06c9d58fdea2f626c14f82060d2b2d92b740df633b36e` | Unchanged LOC Bain face-reference master. |
| `source_crops/RHI_karl_jarres_face_reference.png` | `420x530`, L; 112,300 bytes | `8b59e9b4975e0738411d2b35a860e6b07ef0a1fe72ca3ed86559d32fcf07cdcc` | Explicit `(310,35,730,565)` face-and-shoulders identity crop. |
| `imagegen_results/RHI_karl_jarres_identity_preserve_trial_04.png` | `1082x1454`, RGB; 2,246,450 bytes | `18c8a1f1d543a4817dc738750ae119d4dac09f118f192695bf0ebae88db970d1` | Source-locked edit using the LOC face source plus the Bundesarchiv hat/coat source. |
| `processed_png/portrait_RHI_independence_wave_provisional_directorate.png` | `156x210`, RGBA; alpha min/max `255/255`; 54,622 bytes | `ae34e21cf3b35ad034e222191313bd77e52eead12d26a6d2379b1fd064b9fa69` | Full country-leader texture, opaque background, no `_small` or dossier derivative. |
| `contact_sheets/RHI_karl_jarres_full_source_result_comparison.png` | `1560x458`, RGB; 488,321 bytes | `0c24f10c2799a050928a2c5efb17e818709f31b4477e7e2ff27309cd640aac37` | Panels: LOC face source, Bundesarchiv attire source, ImageGen result, native candidate, Stauning style reference. |
| `contact_sheets/RHI_karl_jarres_processor_style_comparison.png` | `1344x464`, RGBA; 684,195 bytes | `223c94ce6d3d2dc079965cb7dd03dd9e0e646293d3ef55c7c405eae8a1e12773` | Panels: source crop, processed candidate, Stauning, Mannerheim. |
| `prompts/RHI_karl_jarres_identity_preserve_trial_04.txt` | 1,694 bytes | `4bd6cc0c3bbab6e5aec19289ff05f1fdbb600d175b4ba5c56d5b284449c19378` | Explicitly locks long/narrow face, low hooded eyes, long nose, narrow jaw, guarded expression, hat/coat, and no invented props/insignia. |
| `metadata/RHI_karl_jarres_processing.json` | 5,354 bytes | `8b670f8862162f7d3ebc22fedd801e83413f1eb474173173b56070d6cad05a14` | `advisor_icon_processing.py` v5.0, leader mode, `source_kind=real`, crop `(1,0,1081,1454)`, `face_box=null`, `status=candidate_requires_visual_approval`; output and review hashes match the PNGs. |

### Archival provenance, rights, date, and role

- Primary source: <https://commons.wikimedia.org/wiki/File:Bundesarchiv_Bild_102-01175,_Karl_Jarres.jpg>, Bundesarchiv Bild 102-01175, dated 1925, photographer unknown, credit `Bundesarchiv, Bild 102-01175 / CC-BY-SA 3.0`, CC-BY-SA 3.0 Germany.
- Facial cross-check: <https://www.loc.gov/pictures/item/2014716741/> (`Dr. Jarres`, Bain News Service), no-known-restrictions route. The local record correctly discloses undated/early-20th-century uncertainty; it is not silently substituted for the 1925 primary.
- Karl Jarres (1874–1951) was born in Remscheid, served as mayor of Remscheid and Duisburg, and was Reich Interior Minister. This is a direct Rhenish civic/constitutional/patron role fit, and he was alive in 1936. The source dates are earlier than the scenario but period-appropriate; no postwar or modern material was used.
- Both unchanged masters, explicit crops, prompt, ImageGen result, and processed candidate are retained. Rights are defensible, but the derived image remains a source-locked repaint and must preserve attribution records.

### Trial 04 versus the three earlier rejected revisions

The earlier source/result files were also inspected, not treated as accepted alternatives:

| Revision | Full ImageGen master | Native review | Earlier independent finding |
|---|---|---|---|
| Trial 01 | `imagegen_sources/RHI/RHI_karl_jarres_hoi4_trial_01.png`, `1080x1456`, SHA-256 `2a3181b5736f30e60a4e1962646cd98918774ae36ab0e162c5c78db6de4311d3` | `processed_png/RHI/RHI_karl_jarres_hoi4.png`, `156x210`, SHA-256 `af560fe69f990e0e6da26f03c9fcc62f55f43077b514b0fb3b33fa3605ad9933` | Too youthful/wide-eyed; face broad, smooth, and generic; hat did most of the identity work. |
| Refined 02 | `imagegen_sources/RHI/RHI_karl_jarres_hoi4_refined_02.png`, `1080x1456`, SHA-256 `473e0574639ad7a8b32355a5d2c821c7982c0927607faf96884e8b9854dcc49f` | Same `156x210` native review SHA `af560fe69f990e0e6da26f03c9fcc62f55f43077b514b0fb3b33fa3605ad9933` | Improved eye/age continuity but still broad, smooth, symmetrical, and interchangeable without the hat. |
| Revision 03 | `imagegen_sources/RHI/RHI_karl_jarres_hoi4_revision_03.png`, actual `1081x1455`, SHA-256 `4276f09d7218c6ad09c6d2c91576d0f95521c06b897cd4d537a282c7249f4cff` | `processed_png/RHI/RHI_karl_jarres_hoi4_revision_03.png`, `156x210`, SHA-256 `90f395c882ba42f577a44228713125ff2d278698c970dce152348d90d80fe3c9` | Eyes and mouth improved, but face remained broad/near-symmetric; tall crown, curled brim, broad lapels, and cross-hatch still carried too much likeness. |
| Trial 04 | `imagegen_results/RHI_karl_jarres_identity_preserve_trial_04.png`, actual `1082x1454`, SHA-256 `18c8a1f1d543a4817dc738750ae119d4dac09f118f192695bf0ebae88db970d1` | `processed_png/portrait_RHI_independence_wave_provisional_directorate.png`, `156x210`, SHA-256 `ae34e21cf3b35ad034e222191313bd77e52eead12d26a6d2379b1fd064b9fa69` | Current candidate; improves several facial cues but remains below the independent likeness gate. |

Trial 04 does fix or materially improve some requested invariants: the face is less broad than trial 01/refined 02/revision 03; the eyes are lower and somewhat asymmetric; the nose is longer; the jaw is narrower; apparent age is older; and the expression is more guarded with a slight downward angle. It does **not** fully fix the decisive native-read problems:

- The high/receding forehead and close side hair that anchor the LOC source are largely hidden by the generated hat.
- The native face remains smoother and wider than the LOC reference, with eyes more open and less hooded, a shorter-looking nose, and a less distinctly downturned thin mouth.
- The generated felt hat retains a tall crown and broad curled brim. It remains the strongest likeness cue, so the candidate reads as a generic civic man when the hat is mentally discounted.
- Lapels and coat geometry remain broader/more dramatic than the Bundesarchiv attire crop, and the painterly cross-hatch/value treatment remains heavier than the quiet vanilla leader family.

The result is therefore a substantive improvement, **not a complete fix**. No face replacement or invented insignia was observed, but identity cannot be admitted on the hat alone.

### Ownership collision and stable consumer audit

Searches covered `Karl Jarres`, `Carl Jarres`, `Jarres Karl`, `karl_jarres`, `carl_jarres`, and relevant name-order/transliteration forms in current Chaos Redux, installed vanilla, and the three approved reference mods. Results:

- Current Chaos Redux: no separate historical `Karl Jarres` character owner. The current `RHI_independence_wave_provisional_directorate` token/localisation is the target consumer created by the package; it is not proof of a pre-existing Jarres person owner.
- Installed vanilla: no exact Karl/Carl Jarres character, recruitment, portrait, or localisation owner.
- Kaiserreich `1521695605`: **disclosure-only reference hit, not a binding collision under the accepted policy**. `common/characters/GER characters.txt:85-101` defines `GER_karl_jarres` with a civilian large portrait; `history/countries/GER - Germany.txt:286` recruits it; English localisation `KR_country_specific/GER - Germany l_english.yml:38-39` names/describes it; `interface/kaiserreich/portraits/GER_portraits.gfx:15-16` maps `GFX_portrait_GER_karl_jarres_civilian_large` to `gfx/leaders/GER/GER_karl_jarres.png`. The installed reference portrait is `156x210`, RGB, 45,649 bytes, SHA-256 `b03e714428e7e7d13d64800cc84e66df120488b77ab2380e843dc52ac7faf882`. No Kaiserreich source or art was copied into this package.
- Approved reference `2265420196`: no exact Jarres or Harpe owner in character/history/interface/leader roots.
- Approved reference `1458561226`: no exact Jarres or Harpe owner in character/history/interface/leader roots. Incidental `Sharpeville`/`Harpe` prose is not a person owner.

The Kaiserreich character is a real person owner even though the portrait treatment differs, so it is retained as a disclosure for reviewers. Under the accepted policy, cross-mod exclusivity binds country tags, not reuse of the same historical person across mutually exclusive mods when no source or art was copied; no guarded transfer/availability contract is required on this basis. Keep the vanilla/current Chaos Redux active-person ownership gate binding.

The stable intended Chaos Redux consumer is already declared but not admitted by trial 04:

- Sprite `GFX_portrait_RHI_independence_wave_provisional_directorate` and texture path `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` are in `interface/006_independence_wave_region_01_portraits.gfx:28-29`.
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt:230-244` generates the male country-leader token, assigns `civilian.large`, and `independence_wave_install_rhi_patron_government` promotes it as the patron route.
- The candidate package contains no DDS. The existing runtime DDS is **not Jarres**: `gfx/leaders/006_independence_wave/portrait_RHI_independence_wave_provisional_directorate.dds` is `156x210`, 131,168 bytes, one-level uncompressed BGRA, alpha `255..255`, SHA-256 `06c40e7d557cf7e5bfd719c2a576e15d86a435b8ea9757f1f91620bf0e61ac64`, and decodes pixel-identically to the old rejected `docs/assets/006_independence_wave/sourced_portrait_treatments_2026_07_22/processed_png/RHI_konrad_adenauer.png` (RGBA `156x210`, SHA-256 `0c2c9193ab1a857b1603c810f07e0731ff571ccfbbb929a6e60bedd38402fc71`). Do not count that old Adenauer file as trial 04 approval.
- Protected `portrait_RHI_josef_friedrich_matthes.dds` remains hash-identical as recorded above; this audit did not alter it.
- No `_small`, advisor, dossier, theorist, high-command, female, or alternate-country derivative is present or authorised in the candidate package or handoff.

### Jarres disposition

**`FAIL` (blocked); no runtime advancement.** Trial 04 is a better identity-preserving attempt than all three earlier rejected revisions, but it does not yet clear full/native likeness. The Kaiserreich `GER_karl_jarres` hit is disclosure-only under the accepted mutually-exclusive-mod policy, and no source or art was copied. Do not convert, copy, register, or wire this candidate; do not substitute a generic or generated Rhenish officeholder.

## Runtime and wiring boundary

Neither candidate may advance to runtime wiring in this audit. The package GFX handoffs are filename reservations only. If a future independent review admits a candidate, the parent implementation agent must:

1. Keep the exact stable sprite names and existing `interface/006_independence_wave_region_01_portraits.gfx` consumers.
2. Convert only the independently approved `156x210` PNG with `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`; the old runtime DDS files above are not approved replacements.
3. Keep Harpe as one full portrait assigned to the existing civilian/army-large consumer; do not create `_small` or advisor derivatives.
4. Treat Kaiserreich's `GER_karl_jarres` person-owner hit as disclosure-only under the accepted mutually-exclusive-mod policy (no source/art was copied); keep vanilla/current Chaos Redux active-person ownership binding before any reuse. No fallback, renamed clone, or generic substitute is authorised.
5. Reverify the protected Matthes runtime DDS SHA-256 `aa61cc3a12fb6670b690c7685feb9383383ce58599c9e6d6e7c14f20fab3bce2` after any parent-owned wiring.

## Simplifications, omissions, and blockers

- No simplification or fallback was used.
- Both source masters, explicit crops, moderation input (Harpe), ImageGen results, prompts, processor metadata, native PNGs, full comparison sheets, rights claims, date notes, and stable consumers were inspected.
- No final DDS was created by this audit. Existing runtime DDS files were read-only inspected and shown to be stale historical treatments, not approvals.
- Harpe is **not blocked by ownership**, but remains `NEEDS_REVISION` for source-faithful decoration neutralisation, commander-family style, and face-preservation review.
- Jarres is **blocked** by the remaining visual likeness gap. The Kaiserreich person-owner hit is disclosure-only under the accepted policy, and no source/art was copied; the source/rights chain itself remains defensible.
- The candidate packages contain no final runtime `.gfx` edits, no female/advisor/`_small` assets, and no gameplay changes.
