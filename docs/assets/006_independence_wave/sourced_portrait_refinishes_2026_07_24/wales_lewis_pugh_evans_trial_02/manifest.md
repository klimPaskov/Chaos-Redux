# IW-002 Wales Lewis Pugh Evans portrait trial 02

Status: `blocked`.
Independent audit verdict: **FAIL** — residual likeness drift remains in the source-locked repaint and processed commander candidate; keep this trial unwired.

This trial is a source-only identity retry after trial 01 failed exact likeness and commander-family evidence.

It remains deliberately unwired.

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

## Explicit archival head-and-shoulders crop

- Crop: `source_crops/WLS_lewis_pugh_evans_iwm_hu93411_head_shoulders.png`.
- Source-pixel coordinates: `(left=95, top=25, right=540, bottom=505)`.
- Dimensions: `445x480`.
- SHA-256: `B16812C1B58AF568EAC7E74EC64E592CC34DD793CC2DB3A8D261D85168A2C064`.
- Contents: cap, unobstructed face, neck, both shoulders, collar, and upper tunic.
- Use boundary: immutable identity evidence only; never a runtime portrait.

## Source-only ImageGen repaint

- Raw result: `imagegen_results/WLS_lewis_pugh_evans_identity_preserve_trial_02.png`.
- Dimensions: `1208x1302`.
- SHA-256: `5F61603CCEA5C3BF302DDC2D37184654CBDB14573D0A080D8E9EE3D0789B45D2`.
- Identity and composition input: only the exact archival Evans crop above.
- External style-reference images supplied to ImageGen: none.
- Prompt: `identity_repaint_prompt.md`.
- Prompt SHA-256: `5C2B19A64D7E4108F1DE4ABC444279C85066F7856F9515F95EA717784F56BDA0`.

Trial 02 removes external portrait faces from the generation input and explicitly preserves the source's narrow eyes, ear asymmetry, long nose, pencil moustache, lean face, pointed chin, age lines, gaze, and expression.

The independent likeness gate must determine whether the output actually obeys those constraints.

## Deterministic 156x210 commander processing

- Processor: `.agents/skills/chaos-redux-event-assets/tools/advisor_icon_processing.py`.
- Processor positional mode: `leader`, the backward-compatible full-size `156x210` export mode.
- Required role family: `commander`.
- Processor SHA-256: `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC`.
- Raw-result crop: `(left=120, top=0, right=1088, bottom=1302)`.
- Output: `processed_png/portrait_WLS_independence_wave_mountain_commandant.png`.
- Output dimensions: `156x210`.
- Output SHA-256: `3758F42C8E0C2A8DA2AEC8BF097C69C22DB2388C46D12EEB24C9260DC2D2EE44`.
- Processing metadata: `processing_metadata.json`.
- Commander review sheet: `review/WLS_lewis_pugh_evans_commander_style_sheet.png`.
- Commander references selected by the processor:
  - `eng_bernard_montgomery.png`, SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E`;
  - `ger_erwin_von_witzleben.png`, SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`.

The review sheet's first panel is the processor input crop from the raw ImageGen result.

It is not the archival source crop and cannot replace provenance or likeness evidence.

## Required independent gate

An independent auditor must directly compare the immutable archival master and crop, raw ImageGen result, processed candidate, and commander references at native size and at least 4x nearest-neighbour.

The auditor must separately record:

- provenance and rights;
- male-only and role fit;
- archival source-crop compliance;
- identity and likeness preservation;
- HOI4 painted commander style;
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
