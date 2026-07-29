# Cunninghame Graham source-locked portrait trial 03

Status: **candidate awaiting independent identity, style, and provenance audit; not approved for runtime wiring**

This package retries the sourced real-male civic portrait for IW-001 Scotland after trial 02 failed the native-size likeness gate.

It contains no advisor, dossier, `_small`, female, fictional, flag, focus, decision, localisation, gameplay, interface, or runtime asset.

## Subject and role

- Event 006 package: IW-001, Scotland (`SCO` vanilla carrier used additively).
- Stable role: `SCO_independence_wave_civic_convention`, civic country leader.
- Subject: Robert Bontine Cunninghame Graham (1852–1936), Scottish politician and writer, founding president of the National Party of Scotland and first president of the Scottish National Party.
- Date caveat: the retained portraits show a younger or middle-aged Cunninghame Graham, so the repaint preserves the sourced age rather than inventing an unsourced 1936-age reconstruction.
- Ownership gate: accepted source research found no active vanilla or current Chaos Redux character owner; reference-mod same-person use is disclosure-only and grants no permission to copy art or sources.

## Archival identity sources

- Primary Commons/HathiTrust record: <https://commons.wikimedia.org/wiki/File:Photo_of_R._B._Cunninghame_Graham.jpg> and <https://babel.hathitrust.org/cgi/pt?id=coo1.ark:/13960/t6xw50w29;view=1up;seq=191;size=150>.
- Primary publication date and rights: no later than 1907, photographer unstated, Commons `PD-US-expired` and pre-1931 United States publication basis.
- Primary unchanged master: `source_masters/SCO_cunninghame_graham_hathitrust_1907.jpg`, `813x1101`, SHA-256 `401CC30D278122A6CC99B691E913A63C568A2EF82E1E0AE0513DC93F303D4FBB`.
- Primary explicit head-and-shoulders crop `(120, 120, 700, 900)`: `source_crops/SCO_cunninghame_graham_hathitrust_head_shoulders.png`, SHA-256 `BC30EE3CCF31D8E31656678BF8B703658189E83CB300889E3461BFBA9A73B56A`.
- Same-person Rijksmuseum record: <https://www.rijksmuseum.nl/en/collection/object/Portret-van-Robert-Bontine-Cunninghame-Graham--58d50c7b9bd272d04b216d7494101918>.
- Same-person source date and rights: circa 1881–1891, anonymous Bassano cliché maker, Rijksmuseum CC0/public-domain record.
- Same-person unchanged master: `source_masters/SCO_cunninghame_graham_rijksmuseum.jpg`, `3846x4852`, SHA-256 `5D646596028A8A069651207E2058E8B59BDF7276D28921FD2A1DDEFE2FF7ABE7`.
- Same-person explicit crop `(990, 735, 2900, 3310)`: `source_crops/SCO_cunninghame_graham_rijksmuseum_identity_crop.png`, SHA-256 `49CB8464CB15A451C16FC0728E60963B93E3E4742C86F07BC923C35B83586069`.

## Identity-preserving HOI4 repaint

- Image 1 is the HathiTrust identity crop, image 2 is the Rijksmuseum same-person cross-check, and image 3 is the style-only `den_thorvald_stauning.png` leader reference.
- The exact executed prompt is retained at `prompts/SCO_cunninghame_graham_identity_preserve_trial_03.txt`.
- The raw ImageGen result is `imagegen_results/SCO_cunninghame_graham_identity_preserve_trial_03.png`, `1086x1448`, SHA-256 `173D558845E33077A495739EE240DD53A0DD5DD37E96D719EDAB6849A5C2474E`.
- Deterministic `156x210` processing used the skill-local `retired_advisor_card_processor_REMOVED leader` mode, source kind `real`, full-result crop `(0, 0, 1086, 1448)`, and canonical vanilla leader review directory.
- The processed candidate is `processed_png/portrait_SCO_independence_wave_civic_convention.png`, SHA-256 `BD42DE868B423268B23B412F736923E987EF848F957FDDF5A0556A2487163259`.
- The direct source, rejected-trial, candidate, and canonical comparison is `contact_sheets/SCO_cunninghame_graham_source_trials_reference.png`, SHA-256 `5C45C141AAC5D5E238549AA18622EE7BA0BD7C343E97A33E04406B16D26CAD43`.
- The processor comparison is `contact_sheets/SCO_cunninghame_graham_processor_style_comparison.png`, SHA-256 `6661A60A8D1792A4CF982640C53111C9B409F347C89ECD726DF758A8CD5C27F6`.
- Processor metadata is retained at `metadata/SCO_cunninghame_graham_processing.json`.

Trial 03 narrows the face and beard relative to rejected trial 02 and keeps the sourced hair mass, nose, collar, cravat, age, and frontal pose.

Independent review must still reject it if the eyes remain too open or symmetric, the moustache or beard geometry drifts, the face reads as a generic Victorian man, or the HOI4 style obscures identity.

## Runtime gate

Do not copy, convert, register, or wire this candidate before an independent PASS.

IW-001 remains closed until both Cunninghame Graham and Victor Morven Fortune pass independent review, exact runtime DDS files are pixel-verified, and a fresh full package audit passes.
