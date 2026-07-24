# IW-006 Wallonia Herman Baltia trial 05 independent portrait audit

Audit date: 2026-07-24.

Reviewer: `/root/event6_wallonia_baltia_trial05_portrait_audit`, independent of the producing asset worker.

Audit scope: read-only review of `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wallonia_herman_baltia_trial_05/` against the unchanged archival master, self-bound exact crop and equality JSON, rejected trial-04 raw corrective canvas, raw trial-05 repaint, deterministic `156x210` commander candidate, prompt, processor metadata, commander style sheet, and canonical commander references.

Final disposition: `FAIL`; trial 05 remains export-only and is not authorized for DDS conversion, localisation transfer, or runtime wiring.

The unchanged master, exact crop, trial-04 canvas, raw trial-05 repaint, processed candidate, style sheet, and canonical commander references were inspected at native size and in disposable `4x` nearest-neighbour enlargements. The `4x` files were created outside the repository for this audit and are not package assets.

Identity is a separate non-compensable gate, so the candidate cannot be promoted even though its role, framing, provenance, and painted treatment are usable.

## Verdicts

| Gate | Verdict | Independent evidence |
|---|---|---|
| Provenance and self-bound crop equality | **PASS** | `source_masters/AFX_herman_baltia_1909_master.jpg` is the unchanged direct archival upload identified by the manifest as `General_Baltia_Herman.jpg`, Public Domain Mark 1.0 and `PD-old`, with `389x473` RGB SHA-256 `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66`. `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` binds its master, output, metadata, and normalized command to the trial-05 folder, records rectangle `(20,12,373,473)`, and reports `decoded_pixels_equal: true`. Independent Pillow decoding reproduced the `353x461` crop and equal RGBA payload hash `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326` over `162733` pixels. The prompt and manifest identify the archival crop, not the generated canvases or style references, as the sole identity authority. |
| Male and historical commander-role fit | **PASS** | The unchanged photograph, repaint, and candidate show one male officer. `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-63` sets `AFX_walloon_reserve_commander` to `gender = male` and exposes only full `civilian.large` and `army.large` portraits. The manifest grounds Herman Baltia in the Belgian lieutenant-general, Arlon 10th Line Regiment, and later Chasseurs Ardennais lineage, while explicitly disclosing that the Event 6 position is an alternate-history territorial/reserve-command abstraction, that Baltia was retired at the 1936 start, and that the 1909 uniform is not claimed as a 1936 uniform. |
| Trial-04 corrective canvas and source locking | **PASS (source-mode contract only)** | `identity_repaint_prompt.md` names the exact trial-05 archival crop as Image 1 and the rejected trial-04 raw repaint as Image 2, explicitly saying Image 1 is the sole identity and geometry authority and Image 2 is only a prior painted canvas to correct. The canonical `ger_erwin_von_witzleben.png` input is explicitly style-only. This arrangement satisfies source locking in principle because the rejected repaint is not declared an identity source. It does not excuse inherited geometry drift, and the separate likeness gate below fails. |
| Identity and likeness preservation | **FAIL (non-compensable)** | At native and `4x` inspection, trial 05 remains materially unlike the archival man. The source has a narrow elongated skull, high sparse receding hairline, small deep-set unequal eyes, long narrow nose, hollow cheeks, narrow jaw and chin, thin unequal moustache curls, compact ears, a restrained neutral expression, a frontal head angle, long narrow neck, and narrow shoulder proportions. Trial 05 still enlarges and nearly symmetrises the eyes, broadens and rounds the skull, cheeks, jaw, and chin, shortens and broadens the nose, thickens and regularises the moustache, makes the visible ear more prominent, fills and lowers the hairline, and shortens/broadens the neck. The head-to-shoulder silhouette is serviceable, but the facial geometry and expression drift are identity changes rather than permissible painterly variation. |
| HOI4 painted commander style | **PASS** | The processed candidate is a restrained oil/gouache-style full commander portrait with muted period colour, matte brush texture, controlled contrast, dark neutral painted background, and no text, watermark, dossier frame, UI, glow, or cinematic effects. The style sheet compares the processor input crop and candidate with `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`; both canonical role references are full `156x210` commander portraits. The first style-sheet panel is labelled `processor input crop`, not the immutable archival crop, so the independent review retained the separate source/crop comparison required by the skill. |
| `156x210` framing and readability | **PASS** | `processed_png/portrait_AFX_walloon_reserve_commander.png` decodes as opaque RGBA `156x210` with alpha minimum and maximum both `255`. The candidate keeps a safe top margin, both epaulettes and shoulders, collar, medal, and a readable face inside the full commander canvas. It is not a `65x67` dossier card and does not use a fabricated `50x67` commander texture. |
| Ownership search | **PASS (no external Baltia owner found)** | Exact and variant searches for `Herman Baltia`, `Baltia Herman`, `Herman_Baltia`, `Baltia_Herman`, `General Baltia`, `General_Baltia`, `general_baltia`, and `AFX_walloon_reserve_commander` found no Herman/Baltia character, portrait, leader, commander, operative, or officeholder owner in current project character/history/GFX/interface/localisation roots, installed vanilla roots, or approved reference roots `1521695605`, `2265420196`, and `1458561226`. The only current-project owner is the existing AFX token defined in `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-63`, recruited by `history/countries/AFX - Wallonia.txt:18`, and registered by `interface/006_independence_wave_region_01_portraits.gfx:14-15`; no second character or portrait consumer was found. |
| Guarded Marcel Delcourt -> Herman Baltia stable-token transfer | **FAIL (not cleared)** | `manifest.md` states the desired single-token/single-sprite transaction, removal of the old identity from all live surfaces, and prevention of simultaneous origin/target ownership, but this trial contains no implemented or independently testable transfer/availability guard. The stable token still resolves to `Marcel Delcourt` at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4`, and `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:91` still describes the Emergency Works Command as led by Marcel Delcourt. The existing token is recruited and used by scripted triggers/effects, while the same stable sprite still points at the old runtime DDS; no parent-owned atomic localisation/runtime change has cleared the old player-facing identity. Documentation of intended conditions is useful but is not proof that the guarded transfer is implemented, so this gate remains fail-closed. |
| Absence of advisor, dossier, operative, and `_small` derivatives | **PASS** | The trial-05 workspace contains only the archival master, exact crop and JSON, prompt/manifest, raw trial-04 and trial-05 repaint evidence, full commander candidate and metadata, and commander style sheet. A recursive package check found no filenames containing `advisor`, `dossier`, `operative`, or `_small`, and no DDS exists under the trial-05 folder. Processor metadata leaves advisor composition, validation, overlay, and provenance fields `null`; the current Event 6 commander surface remains full-size only. |

## Retained artifact hashes and dimensions

| Artifact | Dimensions and mode | SHA-256 |
|---|---|---|
| `source_masters/AFX_herman_baltia_1909_master.jpg` | `389x473` RGB | `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` | `353x461` RGB | `4980ac2a82fae576809adc1b10141ca711118bbbc58548c63942e4650a7a25a1` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` | JSON, schema `chaos-redux-portrait-source-crop-v1` | `da3860b85391b835f8410b0d6bc2fce120d43c081f293c9539b3368f896431b3` |
| Exact crop decoded RGBA payload | `353x461`, `162733` pixels | `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326` |
| `wallonia_herman_baltia_trial_04/imagegen_results/AFX_herman_baltia_identity_preserve_trial_04.png` | `1081x1455` RGB | `263e508706059ad2b63ad615a8f7d17b8075e3d52442f6a89b63c924ff59b961` |
| `identity_repaint_prompt.md` | UTF-8 Markdown | `57b24418470c7e1d1ffefed8415811dad93d24cd2fa399f77426d25b5783be87` |
| `imagegen_results/AFX_herman_baltia_identity_preserve_trial_05.png` | `1073x1466` RGB | `e675b7ff05bb8f04377d34724052ead29add59dddf1dc3f121301b518c11085f` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png` | `156x210` RGBA, alpha `255..255` | `2273df89b12fb2066c602bc9318fb39027c450741ac9cdff089bffc240e0a154` |
| Candidate decoded RGBA payload | `156x210` | `42b06717ae3ce325672501493237180b728547ad5489c13e5533301f4221d503` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png.json` | JSON, metadata-integrity payload verified | `f20bba7ad872cef942a815f8cbc1ba0d8be6ee05c62eebc6ecf41b2c22c413b1` |
| `review/AFX_herman_baltia_commander_style_sheet.png` | `1344x464` RGBA, alpha `255..255` | `0edfdf62da09c604abeecbf6fc421f5c37117b950254dd22245cdc4ce77ebc61` |
| Style-sheet decoded RGBA payload | `1344x464` | `1e7bb8374f3cb351f078f4094707b566325af19554a6cd992bba9ba8f384677c` |
| Canonical `eng_bernard_montgomery.png` | `156x210` RGBA | `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e` |
| Canonical `ger_erwin_von_witzleben.png` | `156x210` RGBA | `10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6` |

The trial-05 processor metadata records processor version `5.0`, role family `commander`, source kind `real`, crop `(100,0,973,1176)` on the raw repaint, processor SHA-256 `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`, and a valid canonical metadata-integrity payload hash `0cd0d30ca2c848b751eed9bcaf19c7dd1c96a1dbc581273ffa5e438d8d8eaaaa`.

The raw trial-05 decoded RGBA integrity digest independently recomputes to `d0f6e8a82e913c68c50b0d4c1d8afc0541a6cd2b30446a3b840cc9f752ab39cc`, matching the metadata; the candidate digest independently recomputes to `42b06717ae3ce325672501493237180b728547ad5489c13e5533301f4221d503`, also matching the metadata.

## Blockers and allowed next step

The identity gate is the primary non-compensable blocker, with the guarded stable-token transfer still uncleared as a separate runtime blocker. No DDS conversion, DDS equality proof, localisation transfer, GFX change, character change, or runtime wiring is authorized from trial 05.

The parent may retain trial 05 as export-only evidence and generate another source-locked repaint whose narrow elongated skull, high sparse hairline, small unequal deep-set eyes, long narrow nose, hollow cheeks, compact ears, thin unequal moustache, long narrow neck, restrained expression, head angle, and shoulder proportions survive native and `4x` review. A new run may use the trial-04 repaint only as a declared corrective canvas if the unchanged archival crop remains the sole identity authority, but a direct repaint from the immutable crop is safer because trial 04's rejected geometry drift remains visible in trial 05.

Before any promotion, the parent must implement and review one atomic guarded transaction that retains `AFX_walloon_reserve_commander` and `GFX_portrait_AFX_walloon_reserve_commander`, removes the old `Marcel Delcourt` player-facing identity from every live surface, records Herman Baltia's historical-role disclosure, prevents duplicate or simultaneous ownership, converts only the independently approved `156x210` PNG, and then requests a fresh full IW-006 package audit.

## Audit boundary and changed files

No gameplay, runtime, GFX, localisation, source asset, processed asset, metadata, or DDS file was modified.

No audit simplification or fallback was used; the likeness gate was evaluated independently and fail-closed.

The only repository file created by this audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_baltia_trial05_independent_portrait_audit_2026_07_24.md`.
