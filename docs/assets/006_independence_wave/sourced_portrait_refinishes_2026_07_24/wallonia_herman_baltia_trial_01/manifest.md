# AFX Herman Baltia identity-preserving portrait trial 01

Status: `rejected_identity_runtime_hold`.

This package applies the mandatory sourced-person portrait chain to Baron Herman Baltia for the existing Event 006 Wallonia commander consumer.

No DDS was created or wired.

## Stable consumer

| Field | Value |
|---|---|
| Character | `AFX_walloon_reserve_commander` |
| Sprite | `GFX_portrait_AFX_walloon_reserve_commander` |
| Runtime DDS | `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` |
| Role family | Army commander |
| Gender gate | Male |

This is a full-size commander portrait only.

It does not create an advisor portrait, advisor icon, dossier, or `_small` derivative.

## Historical role decision

Herman Baltia was a Belgian lieutenant-general who commanded the Arlon-based 10th Line Regiment, the formation lineage transformed into the 1st Regiment of Chasseurs Ardennais in 1933.

He was alive in 1936 but retired and seventy-two years old.

The parent accepted him as a defensible alternate-history senior territorial and reserve-command abstraction for AFX Wallonia because of the direct Arlon and Chasseurs Ardennais lineage.

This package does not claim that Baltia commanded an independent Walloon state in 1936 or that the 1909 source uniform is a 1936 uniform.

## Mandatory source chain

### 1. Archival male photograph

| Field | Value |
|---|---|
| Master | `source_masters/AFX_herman_baltia_1909_master.jpg` |
| Dimensions | 389 x 473 |
| SHA-256 | `73597E416240754B2F5A9C78AAC4798287B58642F1ABD93C920F3020D95A1B66` |
| Source page | [Wikimedia Commons: General Baltia Herman](https://commons.wikimedia.org/wiki/File:General_Baltia_Herman.jpg) |
| Direct upload | [Original upload](https://upload.wikimedia.org/wikipedia/commons/e/eb/General_Baltia_Herman.jpg) |
| Caption / date | `Major Baltia 1909` |
| Rights | Public domain / Public Domain Mark 1.0; Commons also records `PD-old` |

The master is the direct archival upload retained unchanged.

### 2. Explicit head-and-shoulders crop

| Field | Value |
|---|---|
| Crop | `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` |
| Master rectangle | `left=20, top=12, right=373, bottom=473` |
| Dimensions | 353 x 461 |
| SHA-256 | `442658EC257566827290B77D7D3B8E7AF208CF9A999FFC1086DD61BC059BCB59` |
| Method | Direct source-pixel crop without resampling, retouching, repainting, synthesis, or colourisation |

The crop preserves the complete head, neck, and both shoulders and remains the sole identity authority for the repaint.

### 3. Identity-preserving ImageGen repaint

| Field | Value |
|---|---|
| Input | Archival crop only |
| Prompt | `identity_repaint_prompt.md` |
| Prompt SHA-256 | `68710A71B2D3EEFE15AA38B7DF0B7220B2BDF0CA106FD12503B32D85A4466B2A` |
| Raw repaint | `imagegen_results/AFX_herman_baltia_identity_preserve_trial_01.png` |
| Raw dimensions | 1098 x 1433 |
| Raw SHA-256 | `EBC8CAADC8F4438B50D6A444136EC0D5235A57C153C7D9317938CE32FA2E10A0` |

The prompt makes the archival crop the sole identity and composition authority.

It explicitly preserves Baltia's narrow forehead, receding wavy hair, long lean face, unequal deep-set eyes, long straight nose, asymmetrical handlebar moustache, ears, expression, head angle, neck length, and shoulder slope.

It permits only a restrained HOI4-style repaint and a symbol-free Belgian field-service tunic below the neck.

### 4. Deterministic 156 x 210 processing

| Field | Value |
|---|---|
| Processor | `retired_advisor_card_processor_REMOVED` |
| Processor version | 5.0 |
| Processor SHA-256 | `1ADB521B43238EE971E093DAE90007C4C44C600435EBB897C6482BA3B64B96EC` |
| Positional mode | `leader` |
| Role family | `commander` |
| Repaint crop | `left=17, top=0, right=1081, bottom=1433` |
| Output | `processed_png/portrait_AFX_walloon_reserve_commander.png` |
| Output dimensions | 156 x 210 |
| Output SHA-256 | `A0ABD0E129F150F534B024C06FFB66D14D8E4DFDC86BDB581252588D769244A7` |
| Metadata | `processing_metadata.json` |
| Metadata SHA-256 | `D367E37C34575856E4F1F147EF8BEEA9729024ECB6404F9A0E391D415D78E4B4` |
| Review sheet | `review/AFX_herman_baltia_commander_style_sheet.png` |
| Review SHA-256 | `5C840F3C55000CEEE680D3EDEA39E35163031439FB85F593020EED3D1A28423B` |

The processor recorded the commander reference family explicitly.

The canonical reference images are `eng_bernard_montgomery.png` with SHA-256 `39B03871D7451CA96712A5CCF3C056528693F82642776E6C5E297E041943944E` and `ger_erwin_von_witzleben.png` with SHA-256 `10F4A1108F9D440213F70FB5802349A2291F298F9D132644241119561577D5B6`.

The processor performs crop, grade, and export only.

It does not synthesize or redraw the subject.

## Independent audit gate

An independent reviewer must compare the archival master, the explicit source crop, the raw ImageGen repaint, the 156 x 210 processed PNG, the prompt, the processing metadata, and the commander references.

The reviewer must return separate verdicts for:

- source provenance and rights;
- male-subject compliance;
- historical role and alternate-history abstraction;
- explicit head-and-shoulders crop;
- identity and likeness preservation;
- HOI4 commander style;
- framing at 156 x 210;
- ownership and stable-consumer fit;
- absence of advisor, dossier, and `_small` assets.

Any failed identity or style verdict keeps the candidate rejected and unwired.

Only a complete independent pass permits deterministic DDS conversion and sprite wiring.

## Independent audit result

Audit date: 2026-07-24. Reviewer: independent sourced-visual audit subagent. Full evidence and the exact source-only retry requirements are recorded in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_baltia_trial01_independent_audit_2026_07_24.md`.

| Gate | Verdict | Evidence summary |
|---|---|---|
| Provenance and rights | **PASS** | The unchanged `389 x 473` Commons upload hash matches `73597E...A1B66`; the page records Public Domain Mark 1.0 / `PD-old`; the prompt, raw result, crop, metadata, and review hashes all match the package ledger. |
| Male-subject compliance | **PASS** | The master, crop, raw repaint, and candidate show one male subject; the stable character is `gender = male`; no female metadata or opposite-gender name pool is used. |
| Historical role fit | **PASS** | Baltia's Arlon-based 10th Line and Chasseurs Ardennais lineage supports the parent-approved alternate-history territorial/reserve abstraction; the retirement-at-1936 and 1909-uniform caveats remain explicit. |
| Head-and-shoulders crop | **PASS** | Independent pixel comparison proves `master.crop((20,12,373,473))` equals the `353 x 461` crop exactly with no differing pixels. |
| Identity and likeness preservation | **FAIL (non-compensable)** | At native and disposable 4x nearest-neighbour review, the repaint regularizes the source's unequal deep-set eyes, broadens/softens the long narrow facial planes, shortens/broadens the straight nose, changes the asymmetric handlebar-moustache curls, fills the receding wavy hairline, and rounds the long jaw/chin. These are immutable source-visible identity traits. |
| HOI4 commander style | **PASS** | The candidate is a restrained painted `156 x 210` commander portrait with modeled planes, a period plain tunic, quiet background, and no raw-photo finish, text, watermark, UI, modern prop, emblem, or unsupported insignia. Its darker brown grade is still readable and within the subdued commander family. |
| `156 x 210` framing | **PASS** | Candidate is an opaque RGBA `156 x 210` PNG with one full head-and-shoulders subject, safe head/shoulder margins, and no border or dossier frame. |
| Ownership / stable-consumer fit | **FAIL (runtime transfer not cleared)** | No exact or variant Baltia owner was found in current Chaos Redux, vanilla, or the approved reference roots, but the existing `AFX_walloon_reserve_commander` token still localizes as `Marcel Delcourt` and an older DDS remains at the stable path. Parent-owned identity-transfer localisation and replacement of that stale runtime asset are required before wiring. |
| Advisor / dossier / `_small` absence | **PASS** | This trial contains no advisor, dossier, high-command, operative, or `_small` file; the character definition exposes only the full `civilian.large` and `army.large` slots. |

The independent result is **rejected and unwired** because the identity gate and runtime-transfer consumer gate fail. The style pass does not compensate for either failure. The processor sheet is a `1344 x 464` 2x style sheet whose first panel is a crop of the processor input (the raw ImageGen result), not the immutable archival crop; the archival master and crop were inspected separately, and no processor sheet is treated as automatic approval.

For a source-only retry, use the unchanged master and exact crop as the sole identity authority and preserve the narrow forehead, receding wavy side-parted hair, long lean face, unequal deep-set eyes and heavy lids, long straight narrow nose, asymmetric upward-curled handlebar moustache, unequal ears, long jaw and rounded-pointed chin, stern reserved expression, head angle, neck length, and shoulder slope. Do not use this failed repaint or any generated substitute as an identity source. Keep the commander role, male-only metadata, and full-size `156 x 210` surface; do not create a DDS, `_small`, advisor, or fallback asset until a fresh independent identity audit passes and the parent clears the name transfer.

## Current runtime state

- DDS created: no.
- GFX edited: no.
- Gameplay edited: no.
- Localisation edited: no.
- Advisor asset created: no.
- Independent audit: rejected; identity and runtime-transfer gates failed.
- Existing stale runtime DDS at the stable path is not this candidate and is not approved by this trial.
- Fallback used: no.
