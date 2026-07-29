# Cunninghame Graham source-locked portrait trial 02

Status: **candidate awaiting independent visual and provenance audit; not approved for runtime wiring**

This package retries the sourced real-male civic portrait for IW-001 Scotland after trial 01 failed likeness review. It contains no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-001, Scotland (`SCO` vanilla carrier used additively).
- Stable role: `SCO_independence_wave_civic_convention`, civic country leader.
- Subject: Robert Bontine Cunninghame Graham (1852-1936), Scottish politician and writer, founding president of the National Party of Scotland and first president of the Scottish National Party.
- Date caveat: both retained portraits show a younger, middle-aged Cunninghame Graham. The repaint deliberately preserves the sourced age rather than inventing an unsourced 1936-age reconstruction. He remained alive at the 1936 start boundary and died in March 1936.
- Ownership gate: accepted source research found no active vanilla or current Chaos Redux character owner. Independent audit must recheck before approval.

## Archival sources

### Primary identity source

- Commons/HathiTrust record: <https://commons.wikimedia.org/wiki/File:Photo_of_R._B._Cunninghame_Graham.jpg> and <https://babel.hathitrust.org/cgi/pt?id=coo1.ark:/13960/t6xw50w29;view=1up;seq=191;size=150>.
- Publication: no later than 1907; photographer not stated. The accepted source package records Commons `PD-US-expired` and the pre-1931 United States publication basis.
- Unchanged master: `source_masters/SCO_cunninghame_graham_hathitrust_1907.jpg`, `813x1101`.
- Master SHA-256: `401CC30D278122A6CC99B691E913A63C568A2EF82E1E0AE0513DC93F303D4FBB`.
- Explicit crop `(120, 120, 700, 900)`: `source_crops/SCO_cunninghame_graham_hathitrust_head_shoulders.png`.
- Crop SHA-256: `BC30EE3CCF31D8E31656678BF8B703658189E83CB300889E3461BFBA9A73B56A`.

### Same-person cross-check

- Rijksmuseum object: <https://www.rijksmuseum.nl/en/collection/object/Portret-van-Robert-Bontine-Cunninghame-Graham--58d50c7b9bd272d04b216d7494101918>.
- Institutional IIIF original: <https://iiif.micr.io/CsVbW/full/max/0/default.jpg>.
- Date: circa 1881-1891; anonymous Bassano cliché maker; Rijksmuseum CC0/public-domain record.
- Unchanged master: `source_masters/SCO_cunninghame_graham_rijksmuseum.jpg`, `3846x4852`.
- Master SHA-256: `5D646596028A8A069651207E2058E8B59BDF7276D28921FD2A1DDEFE2FF7ABE7`.
- Explicit crop `(990, 735, 2900, 3310)`: `source_crops/SCO_cunninghame_graham_rijksmuseum_identity_crop.png`.
- Crop SHA-256: `49CB8464CB15A451C16FC0728E60963B93E3E4742C86F07BC923C35B83586069`.

## Source-locked repaint

- Image 1: HathiTrust facial identity crop.
- Image 2: Rijksmuseum same-person identity/costume cross-check.
- Image 3 style-only reference: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/den_thorvald_stauning.png`.
- Prompt: `prompts/SCO_cunninghame_graham_identity_preserve_trial_02.txt`.
- Retained ImageGen result: `imagegen_results/SCO_cunninghame_graham_identity_preserve_trial_02.png`.
- ImageGen result SHA-256: `B0AB6C888E123C8F60B1CF6822ED3D1DDB0817EDF827A79760A6DD6A1B44DD32`.
- Finish command: skill-local `retired_advisor_card_processor_REMOVED leader`, source kind `real`, explicit crop `(1, 0, 1081, 1454)`, canonical vanilla leader reference directory.
- Processed `156x210` candidate: `processed_png/portrait_SCO_independence_wave_civic_convention.png`.
- Processed candidate SHA-256: `83EFE010CCC536BC0DE51A12D474BDABC6B4E34220958C233E13C6E656D7FF03`.
- Full source/result sheet: `contact_sheets/SCO_cunninghame_graham_full_source_result_comparison.png`.
- Processor/style sheet: `contact_sheets/SCO_cunninghame_graham_processor_style_comparison.png`.
- Processor metadata: `metadata/SCO_cunninghame_graham_processing.json`.

Trial 02 uses two independent source reproductions to lock the same man's unusual hair silhouette, long narrow face, eyes, nose, curled moustache, pointed beard, expression, collar, and cravat. Trial 01 remains rejected. Independent review must reject trial 02 if the face becomes generic, the hair/beard are caricatured, sourced age is misrepresented, or native-size recognition fails.

## Runtime gate

Do not copy, convert, register, or wire this candidate before an independent PASS. IW-001 remains closed until both the civic portrait and a sourced Victor Morven Fortune territorial-command portrait pass independent review, exact runtime DDS files are pixel-verified, and a fresh full package audit passes.
