# WLS George Cornwallis-West identity-preserving portrait trial 02

Status: `rejected_export_only`.

Trial 02 is a new source-locked ImageGen repaint made directly from the unchanged archival crop after trial 01 failed likeness.

It is not derived from the rejected trial-01 repaint.

No DDS, GFX, localisation, gameplay, or package-attestation change is authorized unless an independent reviewer passes every gate.

## Stable consumer and ownership boundary

| Field | Value |
| --- | --- |
| Package | IW-002 Wales, carrier `WLS` |
| Character | `WLS_independence_wave_mountain_commandant` |
| Sprite | `GFX_portrait_WLS_independence_wave_mountain_commandant` |
| Proposed identity | Major George Frederick Myddleton Cornwallis-West |
| Role family | Army commander and emergency-route country leader |
| Gender gate | Male |
| Authorized surfaces after approval | Full-size `civilian.large` and `army.large` through the same sprite |

The parent-owned promotion must retain the stable token and sprite, replace the generic player-facing identity and DDS in one transaction, and create no second character, advisor, dossier, operative, commander-small, or `_small` derivative.

## Archival identity source

| Field | Value |
| --- | --- |
| Source page | <https://commons.wikimedia.org/wiki/File:Georgecornwalliswest.jpg> |
| Photographer | Henry Walter Barnett |
| Rights | Public domain according to Commons, with the recorded PD-Art jurisdiction caution retained |
| Master | `source_masters/WLS_george_cornwallis_west_master.png` |
| Master dimensions | `1080x1371` |
| Master SHA-256 | `DBA6C6BC4B5A261C4E761323944BC2D504B0F3DE992F0D8301F2D28535E5ED2C` |
| Exact crop | `source_crops/WLS_george_cornwallis_west_head_shoulders.png` |
| Crop rectangle | `(40,40,1040,1320)` |
| Crop dimensions | `1000x1280` |
| Crop SHA-256 | `3483095E908CD993D46469D4033AABA4AD8CF7009E3BD7D8BA69F890CEA066C4` |
| Equality JSON | `source_crops/WLS_george_cornwallis_west_head_shoulders.json` |
| Equality JSON SHA-256 | `DE41A70749692A499E28EADD58CDA2639C38007699C41809236877B4CB80489B` |
| Decoded-pixel equality | `true` |

The exact-pixel crop utility created and self-bound the crop without resampling, enhancement, recolouring, or retouching.

The portrait preserves Cornwallis-West at the photographed age and does not fabricate a 1936-age face.

## Trial-02 repaint and deterministic processing

| Field | Value |
| --- | --- |
| Prompt | `identity_repaint_prompt.md` |
| ImageGen input | The exact archival crop above, and no rejected portrait |
| Raw repaint | `imagegen_results/WLS_george_cornwallis_west_identity_preserve_trial_02.png` |
| Raw dimensions | `980x1605` |
| Raw SHA-256 | `A148918B39692E6BE29DED3FDA2998B07B87CF5FCB55529A62AE5E1E0AE39E93` |
| Deterministic raw crop | `(0,30,980,1349)` |
| Candidate | `processed_png/portrait_WLS_independence_wave_mountain_commandant.png` |
| Candidate dimensions | `156x210` |
| Candidate SHA-256 | `B2AE3AA92304B5F16235BB95EB3FFA23BA662E0470874C7A943BE940540D9BE7` |
| Candidate decoded RGBA SHA-256 | `A52BBE4CA47150B93407AFC99D3F37AEFF773D15FADBD7F37B16DB42C67161C0` |
| Metadata | `processed_png/portrait_WLS_independence_wave_mountain_commandant.png.json` |
| Metadata SHA-256 | `BF2173164F092F4329E09E81941AE48BC32D8326768E422F9F191021404F8180` |
| Review sheet | `review/WLS_george_cornwallis_west_commander_style_sheet.png` |
| Review-sheet SHA-256 | `292BD1C99F685DBA7B8B58033FB5C51BC0C140343CF9E0CDE2460D34949C2807` |

The processor only cropped, graded, resized, and exported the candidate.

## Independent audit gate

The independent reviewer must compare the unchanged master, exact crop and equality JSON, prompt, raw repaint, native `156x210` candidate, metadata, and commander references at native size and a disposable nearest-neighbour enlargement.

Likeness is a separate non-compensable gate.

The audit must test Cornwallis-West's exact head angle and gaze, eyelid opening, small unequal eyes, forehead and hairline, narrow cheeks, long nose, ear geometry, thin moustache, jaw, chin, expression, neck, shoulders, uniform, medals, and insignia.

The independent audit at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wales_trial02_independent_portrait_audit_2026_07_24.md` returned a non-compensable likeness `FAIL`.

The repaint again enlarged, brightened, and regularized the eyes, frontalized the head and gaze, filled the lower face, and thickened, curled, and symmetrized the moustache.

Trial 02 is rejected and export-only.

It supplies no DDS, GFX, localisation, gameplay, or package-attestation authority.
