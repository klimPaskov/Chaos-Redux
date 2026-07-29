# David Kalākaua Kawānanakoa source-locked portrait trial 01

Status: `rejected_identity_runtime_hold`

## Immutable archival source

- Subject: David Kalākaua Kawānanakoa (1904–1953), male Hawaiian political figure and the exact vanilla HAW neutrality leader.
- Source master: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_22/pacific_asante_sokoto/HAW_david_kalakaua_kawananakoa_1925_original.jpg`
- Source dimensions: `1109×1700`.
- Source SHA-256: `E23304AFA45091FA6B7FF0179CAA688BCD7EE0027306B22E853A14C1344DA909`.
- Canonical source page: <https://commons.wikimedia.org/wiki/File:David_Kalakaua_Kawananakoa.jpg>
- Archived original: <https://upload.wikimedia.org/wikipedia/commons/archive/e/eb/20180819043404%21David_Kalakaua_Kawananakoa.jpg>
- Provenance: George F. M. Nellist (ed.), *The Story of Hawaii and Its Builders*, Honolulu Star-Bulletin, 1925, p. 560; caption identifies David Kalākaua Kawānanakoa. The credited photographer is unknown.
- Rights: United States public domain because the 1925 publication predates 1 January 1931.

## Explicit head-and-shoulders crop

- Crop rectangle in source pixels, left/top/right/bottom: `(245, 170, 945, 1112)`.
- Crop: `source_crops/HAW_david_kalakaua_kawananakoa_1925_head_shoulders.png`.
- Crop dimensions: `700×942`.
- Crop SHA-256: `A17E6323055F7490DB7DEB768C409A466D501888FD242B3CECC390A4AF22F6E2`.
- The crop is source-pixel evidence only and is not a runtime portrait.

## Source-locked repaint

- Prompt: `prompts/HAW_david_kalakaua_kawananakoa_trial_01.md`.
- Identity input: the exact crop above.
- Style-only references: `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/afg_mohammed_zahir_shah.png` and `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/leaders/ire_eamon_de_valera.png`.
- Raw ImageGen result: `imagegen_results/HAW_david_kalakaua_kawananakoa_identity_preserve_trial_01.png`, `1073×1466`, SHA-256 `84CBE0D5083EC2C2E7F361874867DAE0E05C06F528F000DE435D274CB1576F01`.
- Deterministic processing used `retired_advisor_card_processor_REMOVED` in `leader` mode, source kind `real`, the raw-result crop `(0, 10, 1073, 1455)`, and `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/leaders/`.
- Deterministic `156×210` candidate: `processed_png/portrait_HAW_david_kalakaua_kawananakoa.png`, SHA-256 `88EA77261859DE81D1E5082802EA83DA3C79C646C2E200CA0495C9401887F607`.
- Processor metadata: `metadata/HAW_david_kalakaua_kawananakoa_processing.json`, SHA-256 `0C6D9AB93845841A5C66A4B8DFA0622E2AC369E5E81915E01B68BA33E081FDBE`.
- Processor comparison sheet: `review_sheets/HAW_david_kalakaua_kawananakoa_processor_style_comparison.png`, SHA-256 `710B281C326101FE643D35DE5D9079036F17DBF6A5441AB91C923C16355862A4`.
- Independent audit: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_hawaii_kawananakoa_trial01_independent_audit_2026_07_24.md`.
- Audit reviewer/date: `chaosx_country_package_auditor`, 24 July 2026.
- Provenance verdict: `PASS_WITH_CAVEATS`.
- HOI4 style verdict: `PASS`.
- Framing verdict: `PASS`.
- Male-only verdict: `PASS`.
- Consumer-boundary verdict: `PASS`.
- Identity/likeness verdict: `FAIL`. The archival source clips identity-bearing highlights, and the repaint reconstructs missing geometry instead of preserving only source-visible facial evidence.
- Runtime verdict: `HOLD`.
- DDS conversion and runtime wiring: forbidden. A style pass cannot compensate for the failed likeness gate.

## Consumer boundary

The only proposed Event 6 consumer is the existing vanilla David Kalākaua Kawānanakoa country leader during exact IW-173 HAW setup.
The Event 6 implementation must not edit vanilla HAW history.
This rejected trial may not supply a portrait override.
No advisor, dossier, `_small`, commander, operative, or unrelated HAW consumer is authorized.
