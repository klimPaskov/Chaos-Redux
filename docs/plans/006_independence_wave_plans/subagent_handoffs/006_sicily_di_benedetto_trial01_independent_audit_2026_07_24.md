# Event 006 Sicily Di Benedetto trial-01 independent portrait audit

Audit date: 2026-07-24.
Auditor: independent sourced-portrait reviewer `/root/event6_di_benedetto_reaudit`, separate from the producer.
Scope: `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_22/sicily_di_benedetto_trial_01/` only.
Subject: grounded historical male Vincenzo Di Benedetto for the ASX Sicily emergency army-command portrait.
The package is male-only and contains no advisor, dossier, `_small`, female, navy, or alternate portrait asset.

## Transformation-chain evidence

The unchanged archival source master is `source_masters/ASX_vincenzo_di_benedetto_senate_pd.gif`, native `314x401` grayscale GIF, SHA-256 `ec033b2fcd0dc44441a57c93b12b8c9d64828cf72bd3dd2ad646d40480169553`.
The current Wikimedia Commons file page identifies the image as a Senate of the Republic of Italy portrait, author unknown, taken before 1942, and labels it CC BY 3.0 Italy with PD Italy and PD-1996/US status.
Release use therefore requires attribution to `senato.it` and the Commons source page `https://commons.wikimedia.org/wiki/File:Senatore_Vincenzo_Di_Benedetto.gif` plus the unchanged direct master URL `https://upload.wikimedia.org/wikipedia/commons/3/32/Senatore_Vincenzo_Di_Benedetto.gif`.
The explicit crop is `source_crops/ASX_vincenzo_di_benedetto_source_crop.png`, box `(8,0,305,401)` from the `314x401` source, native `297x401` RGB PNG, SHA-256 `596393635ff9c0dc2511a4319b4583c2f33da7c2a7488c81eee386f941239617`.
Independent decode comparison found the retained crop pixel-identical to `master.crop((8,0,305,401))` with no difference bounding box.
The source-only evidence preview is `processed_previews/ASX_vincenzo_di_benedetto_source_locked_156x210.png`, `156x210` RGB, SHA-256 `0c7a9d51fa13a9ab27cca02f3b09026851ca67d3f9df7549c66ad4c1aed2ae18`.
The raw source-locked ImageGen repaint is `imagegen_results/ASX_vincenzo_di_benedetto_identity_preserve_trial_01.png`, native `1080x1457` RGB, SHA-256 `01404a3c74f670dcc238f6b2d68a69ae50f538cf4f48c82b19d548964aed5671`.
The retained prompt is `prompts/ASX_vincenzo_di_benedetto_identity_preserve_trial_01.txt`, SHA-256 `857f7936a1eeae6c744b60aab2523a961455f4d7c79d71e07bbab77b1db09120`, and it explicitly locks the archival crop as the sole identity input and the commander reference as style-only.
The deterministic processor metadata is `metadata/ASX_vincenzo_di_benedetto_processing.json`, SHA-256 `77d24eb657ddfc9b8c711c89349638bb826a42dad2ee35564c7bf1606f78e716`.
The metadata records processor `advisor_icon_processing.py` version `5.0`, current processor SHA-256 `c6e78c01c025ad57fef8dc25eb79bd216ff9809df27e4c758eb9ec72594a3963`, `source_kind = real`, crop `(0,1,1080,1455)`, and output size `156x210`.
The processed candidate is `processed_png/portrait_ASX_independence_wave_vincenzo_di_benedetto.png`, opaque `156x210` RGBA, SHA-256 `37d7256285abef55cb9b81ee6a3ac04aae8e337297120a85de6c99c489e77108`.
The metadata decoded-RGBA hashes for the raw input, processed candidate, and retained review sheet were independently recomputed as `994494d3d7f455a3e58d6ea0274333c46e6dd80a086e613cd84da7844d4ddc73`, `e51a7defcdb93546a09beae0ebe1ab4c347e5315512c899cbbf6c14b7a1c0a8b`, and `119a3f31b2f4cec7c2e630760e6762d3897a1907eb2167ecb3a21cfbab56e810`, respectively.
All eight entries in `hashes.sha256` match current bytes, including `comparisons/source_style_comparison.png` SHA-256 `f7f6e555e4967206dc995a5f3c4e115d06e5f9b6dc0166a8064b3ea9a2db2627`, `comparisons/ASX_vincenzo_di_benedetto_result_reference.png` SHA-256 `6603e51f0ff2ec3cec76fe2e570917ebcda8688b147f803c91748bfaa3a59a76`, and `comparisons/ASX_vincenzo_di_benedetto_archival_result_comparison.png` SHA-256 `7c52d1bd089271ae57f9fbb0291579ce1f03e945faec36d072be509718587665`.
The retained sheets were inspected at native display size, and disposable local-only `4x` nearest-neighbour enlargements were generated from the exact source master, crop, raw result, processed candidate, and role references for the independent enlarged inspection.

## Role-reference evidence

The canonical commander family contact sheet is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/contact_sheet.png`, SHA-256 `1a64051c0ef9c8a67a4e2ffd12a150f27a8a208f0affd37dc5964f8e2606227f`.
The curated commander family contact sheet is `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/contact_sheet.png`, SHA-256 `ab02faef684f7b8b62806ec98edb671b61a37dd806762d604155db3119c3c8de`.
The inspected canonical navy commander reference is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/generic_africa_navy_2.png`, native `156x210`, SHA-256 `a608d7554187cd944130862e09ed4279fd5311f16a6735d07cf357148d11250f`.
The matching curated navy commander copy is `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/generic_africa_navy_2.png`, native `156x210`, byte-identical SHA-256 `a608d7554187cd944130862e09ed4279fd5311f16a6735d07cf357148d11250f`.
The inspected canonical land commander reference is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/commanders/ita_pietro_badoglio.png`, native `156x210`, SHA-256 `9f4f2a5a8d3260ab24866821d3c4edfc75d7bdb1cd0444124d518f7854890e9f`.
The inspected leader-family style reference is `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`, native `156x210`, SHA-256 `08732002182bdcb2bff3d78b142cc2b3d75adbdb29d4115f9e89ca5bdc6a21b6`.
No reference PNG was copied, recoloured, traced, or wired, and any reference-mod identity use is disclosure-only rather than a source or art license.

## Independent verdicts

Provenance: PASS, because the unchanged attributed Senate master, exact pixel-verified crop, source-locked raw repaint, deterministic processor metadata, candidate hash, current source rights, and complete package hash ledger are all present and consistent.
Exact likeness and identity: PASS, because native and `4x` nearest-neighbour comparison retains the long narrow head, close-set shadowed eyes beneath heavy straight brows, long rounded-tip nose, swept moustache, narrow jaw, closed serious mouth, tilted broad hat, straight frontal pose, collar, patterned tie, suit lapels, and source asymmetry without genericization, beautification, symmetrization, face substitution, re-aging, or facial-hair/pose drift.
HOI4 commander style: PASS, because the candidate is a full opaque `156x210` portrait with modeled facial planes, restrained brush texture, controlled desaturated warm-gray painted background, readable silhouette, and a clearly painted rather than photographic or filter-only finish that sits within the inspected commander family.
Role fit: PASS with an explicit wording constraint, because Di Benedetto had a senior Sicilian/Italian army career but the source is civilian and the 1930s record places him at disposal or unemployed, so the only authorized description is `retired Sicilian general recalled for the synchronized independence emergency` rather than an active historical 1936 command claim.
Ownership and exclusivity: PASS, because exact and variant `Di Benedetto`, `Vincenzo Di Benedetto`, `vincenzo_di_benedetto`, `Dibenedetto`, and related name-order searches found no character, recruitment, portrait, interface, GFX, or localisation owner in current Chaos Redux or installed vanilla roots, and no same-person runtime owner was found in the approved reference mods.

## Runtime authorization and hold

All five required verdicts are PASS, so DDS conversion is authorized from the exact processed candidate through `.agents/skills/chaos-redux-event-assets/tools/convert_to_dds.py`.
The authorized runtime output path is `gfx/leaders/006_independence_wave/portrait_ASX_independence_wave_vincenzo_di_benedetto.dds`, and the authorized sprite is `GFX_portrait_ASX_independence_wave_vincenzo_di_benedetto`.
Wiring is authorized only for the full ASX Sicily army/corps-command large portrait consumer and must preserve the male metadata, civilian suit, source attribution, and emergency role wording.
No advisor, dossier, `_small`, navy, female, alternate, generic, fallback, or reference-mod-derived asset is authorized.
No DDS exists yet, and this audit did not create or modify any DDS, GFX, gameplay, character, history, localisation, manifest, or source asset file.

## Simplifications, omissions, and blockers

No unauthorized simplification, fallback, substitute identity, unsupported insignia, or source/art copy was used.
The repaint is mildly warm-gray or sepia while the archival master is grayscale, but the treatment is low-saturation painted styling and does not alter the source-visible civilian clothing or identity landmarks.
The parent must retain `senato.it` attribution and must not rewrite the role as an active 1936 historical command.
If any future byte replacement changes the source master, crop, raw repaint, processed candidate, or role wording, this PASS is void and the chain must be independently re-audited before DDS conversion or wiring.
