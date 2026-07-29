# IW-002 Wales Lewis Pugh Evans portrait trial 01

Status: `blocked`.
Independent audit verdict: **FAIL** — exact likeness and commander-family evidence gates do not pass; keep this trial unwired.

This trial follows the required archival-to-runtime chain and remains deliberately unwired.

No DDS, `.gfx` edit, gameplay edit, localisation edit, advisor portrait, dossier portrait, `_small` derivative, or fallback was created.

## Archival identity source

- Identity: Lewis Pugh Evans, Welsh-born British Army officer and commander of the 159th Welsh Border Infantry Brigade from 1933 to January 1938.
- Immutable master: `source_masters/WLS_lewis_pugh_evans_iwm_hu93411_c1918.jpg`.
- Master SHA-256: `FDFDE87660F50EB9A2112186878FB8EE93B7C1F0E2CB9F533CA9B2C41C26012C`.
- Source page: <https://commons.wikimedia.org/wiki/File:Lewis_Pugh_Evans_VC_IWM_HU_93411.jpg>.
- Archive: Imperial War Museums, `HU 93411`.
- Photographer: Henry Walter Barnett.
- Date: circa 1918.
- Rights record: Wikimedia Commons Public Domain/Public Domain Mark; preserve the IWM/Barnett credit and the source package's territorial-rights caveat.
- Recommended credit: `Imperial War Museums, HU 93411; photograph by Henry Walter Barnett`.

The copied master is byte-identical to the independently researched source package at `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_24/wls_lewis_pugh_evans_source_retry/`.

## Explicit head-and-shoulders crop

- Crop: `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png`.
- Source-pixel coordinates: `(left=95, top=25, right=540, bottom=505)`.
- Dimensions: `445x480`.
- SHA-256: `B16812C1B58AF568EAC7E74EC64E592CC34DD793CC2DB3A8D261D85168A2C064`.
- Contents: cap, unobstructed face, neck, both shoulders, collar, and upper tunic.
- Use boundary: immutable identity evidence only; never a runtime portrait.

## Source-locked ImageGen repaint

- Raw result: `imagegen_results/WLS_lewis_pugh_evans_identity_preserve_trial_01.png`.
- Dimensions: `1023x1537`.
- SHA-256: `EBEDCB468C4BB724324277C922605BA538F6762230159025AABA04771BC4CFB8`.
- Identity input: the explicit Evans crop above.
- Style-only inputs:
  - `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/eng_bernard_montgomery.png`
  - `.agents/skills/chaos-redux-event-assets/assets/leader_portraits/commanders/ger_erwin_von_witzleben.png`
- Prompt: `identity_repaint_prompt.md`.
- Generation boundary: Image 1 supplied identity; Images 2 and 3 supplied style only.

## Deterministic 156x210 processing

- Processor: `retired_advisor_card_processor_REMOVED`, `leader` mode.
- Raw-result crop: `(left=0, top=80, right=1023, bottom=1457)`.
- Output: `processed_png/portrait_WLS_independence_wave_mountain_commandant.png`.
- Output dimensions: `156x210`.
- Output SHA-256: `EC90604F265225A6ED65BEC91612F4C7191D9AFEBDAF742C1F3F039D189D0091`.
- Processing metadata: `processing_metadata.json`.
- Style sheet: `review/WLS_lewis_pugh_evans_style_sheet.png`.

The processor's raw-result crop is a finishing crop, not the archival source crop.

The independent auditor must compare the immutable archival master and explicit source crop directly against both the raw ImageGen result and the 156x210 candidate.

## Required independent gate

An independent auditor must separately record:

- provenance and rights;
- male-only and role fit;
- source-crop compliance;
- identity and likeness preservation;
- HOI4 painted style;
- head-and-shoulders framing;
- ownership and consumer safety;
- absence of advisor, dossier, `_small`, and fallback derivatives;
- runtime verdict.

Only a full PASS authorizes DDS conversion and wiring.

The stable consumer remains:

- character token: `WLS_independence_wave_mountain_commandant`;
- full sprite: `GFX_portrait_WLS_independence_wave_mountain_commandant`;
- reserved runtime texture: `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds`.

Until the audit passes, this package is source evidence and a candidate only.
