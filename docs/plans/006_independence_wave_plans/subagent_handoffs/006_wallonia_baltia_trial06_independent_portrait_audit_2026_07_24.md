# IW-006 Wallonia Herman Baltia trial 06 independent portrait audit

Audit date: 2026-07-24.

Reviewer: `/root/event6_wallonia_baltia_trial06_portrait_audit`, independent of the producing asset worker.

Audit scope: read-only review of `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wallonia_herman_baltia_trial_06/` against the unchanged archival master, self-bound exact crop and equality JSON, direct source-locked trial-06 ImageGen repaint, deterministic `156x210` commander candidate, prompt, processor metadata, commander style sheet, and canonical commander references.

Final disposition: `FAIL`; trial 06 remains export-only and is not authorized for DDS conversion, localisation transfer, or runtime wiring.

The unchanged master, exact crop, raw trial-06 repaint, processed candidate, style sheet, and canonical commander references were inspected at native size and in disposable nearest-neighbour enlargements. The enlargements were created outside the repository at `C:\Users\klimp\AppData\Local\Temp\chaosx_trial06_audit_20260724\` and are not package assets.

Identity is a separate non-compensable gate, so the candidate cannot be promoted even though its role, framing, provenance, and painted treatment are usable.

## Verdicts

| Gate | Verdict | Independent evidence |
|---|---|---|
| Provenance and rights | **PASS** | `source_masters/AFX_herman_baltia_1909_master.jpg` is the unchanged direct upload identified by the manifest as Wikimedia Commons `File:General Baltia Herman.jpg`, with `Public Domain Mark 1.0` and `PD-old` categories on the live Commons page. The downloaded direct original at `https://upload.wikimedia.org/wikipedia/commons/e/eb/General_Baltia_Herman.jpg` returned the same `389x473` bytes and SHA-256 `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66` as the retained master. The source caption is `Major Baltia 1909`; the package preserves the source URL, rights note, and historical-uniform caveat. |
| Exact crop and self-bound equality | **PASS** | `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` uses the repository Pillow crop utility, binds the trial-06 master/output paths, records rectangle `(20,12,373,473)`, `353x461` output, and `decoded_pixels_equal: true`. Independent Pillow decoding reproduced the rectangle exactly: expected and actual RGBA payload hash `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326` over `162733` pixels. No resampling, recolouring, retouching, or hidden source replacement was found. |
| Male and historical commander-role fit | **PASS** | The unchanged photograph, raw repaint, and candidate show one male officer. `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-63` sets `AFX_walloon_reserve_commander` to `gender = male` and exposes only full `civilian.large` and `army.large` portraits. The source package grounds Herman Baltia as a Belgian lieutenant-general who commanded the Arlon-based 10th Line Regiment, whose lineage became the 1st Regiment of Chasseurs Ardennais in 1933. The manifest correctly limits the Event 006 position to an alternate-history territorial/reserve-command abstraction: Baltia was retired and seventy-two in 1936, and the 1909 uniform is not presented as a 1936 uniform. |
| Exact identity and likeness | **FAIL (non-compensable)** | At native and nearest-neighbour enlarged inspection, trial 06 materially changes the source-visible identity. The archival man has a narrow elongated skull, high sparse receding hairline, small unequal deep-set eyes, long narrow nose, hollow asymmetric cheeks, compact ears, thin unequal moustache curls, narrow jaw and small chin, long narrow neck, restrained expression, frontal angle, and narrow shoulders. The raw repaint and `156x210` candidate broaden and round the skull and lower face, fill and lower the hairline, enlarge and nearly equalize the eyes, shorten and widen the nose, fill and symmetrize the cheeks, enlarge the visible ear, thicken and regularize the moustache, broaden the jaw and chin, shorten/broaden the neck, and widen/straighten the shoulder geometry and epaulettes. The frontal angle and generally restrained mouth are only approximate; they cannot compensate for the facial-geometry drift. The prompt requires literal preservation of these traits, but the generated result does not preserve them strongly enough for an identity gate. |
| HOI4 painted commander style | **PASS** | The candidate is a restrained oil/gouache-style full commander portrait with muted period colour, matte brush texture, controlled contrast, subdued neutral painted background, readable face, and no text, watermark, dossier frame, UI, glow, scenery, or cinematic treatment. The style sheet compares the processor input crop and candidate with canonical full `156x210` commander references `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`; both references were also inspected at native size and enlarged. The style sheet's first panel is explicitly `processor input crop`, not the immutable archival crop, so this style PASS does not replace the separate source/crop/likeness review. |
| `156x210` framing and readability | **PASS** | `processed_png/portrait_AFX_walloon_reserve_commander.png` decodes as opaque RGBA `156x210` with alpha range `255..255`. It keeps a safe top margin, both epaulettes and shoulders, collar, medal, and a readable face inside the full commander canvas. It is not a `65x67` dossier card and does not use a fabricated `50x67` commander texture. |
| Subject ownership across current project, vanilla, and approved mods | **PASS (no external Baltia owner found)** | Exact and variant searches for `Herman Baltia`, `Baltia Herman`, `Herman_Baltia`, `Baltia_Herman`, `General Baltia`, `General_Baltia`, `general_baltia`, `AFX_walloon_reserve_commander`, and `GFX_portrait_AFX_walloon_reserve_commander` found no Herman/Baltia character, portrait, leader, commander, operative, or officeholder owner in the current project's `common`, `history`, `interface`, `gfx`, or `localisation` roots, installed vanilla roots, or approved reference roots `1521695605`, `2265420196`, and `1458561226`. The only current-project AFX owner is the existing stable token in `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-63`, recruited by `history/countries/AFX - Wallonia.txt:18`, and registered by `interface/006_independence_wave_region_01_portraits.gfx:14-15`; no second Herman/Baltia character or portrait consumer was found. |
| Guarded Marcel Delcourt -> Herman Baltia stable-token transfer | **FAIL (not cleared)** | `manifest.md` documents the intended single-token/single-sprite transaction, but trial 06 contains no implemented or independently testable transfer/availability guard. The stable token still resolves to `Marcel Delcourt` at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4`, and the Emergency Works Command description still names Marcel Delcourt at line 91. The existing token remains recruited and consumed by the current AFX package, `GFX_portrait_AFX_walloon_reserve_commander` still points to the untouched runtime DDS at `interface/006_independence_wave_region_01_portraits.gfx:14-15`, and no parent-owned atomic localisation/runtime transaction has removed the old player-facing identity. Intended transfer documentation is not proof of an implemented guard, so this gate remains fail-closed. |
| Absence of advisor, dossier, operative, commander-small, and `_small` derivatives | **PASS** | A recursive trial-06 package check found no filenames containing `advisor`, `dossier`, `operative`, `commander-small`, or `_small`. The package contains only the archival master, exact crop and JSON, prompt/manifest, raw ImageGen repaint, full commander candidate and metadata, and commander style sheet. Processor metadata leaves advisor composition, validation, overlay, and provenance fields `null`; the current AFX runtime surface has the full commander DDS only and no AFX `_small` derivative. |

## Retained artifact hashes and dimensions

| Artifact | Dimensions and mode | SHA-256 |
|---|---|---|
| `source_masters/AFX_herman_baltia_1909_master.jpg` | `389x473` RGB | `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` | `353x461` RGB | `4980ac2a82fae576809adc1b10141ca711118bbbc58548c63942e4650a7a25a1` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` | JSON, schema `chaos-redux-portrait-source-crop-v1` | `2e960a1ff38011a0ecb5befaf4d4cdf02c22ef87cd4a618ad875acc9a37794b0` |
| Exact crop decoded RGBA payload | `353x461`, `162733` pixels | `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326` |
| `identity_repaint_prompt.md` | UTF-8 Markdown | `9899380b659c7dffa91c9696e97e509bd8cc6266642c3f2935ae4ce8563e470e` |
| `imagegen_results/AFX_herman_baltia_identity_preserve_trial_06.png` | `1097x1434` RGB | `db85a4450ea86ba83d6bee5a6f484f19d6f5b14b8228aaf974695f7839ebdfde` |
| Raw repaint decoded RGBA payload | `1097x1434` | `0bf3f3809fb448ca51e4d68a44610587d473c91a83646e3b819cf2b708f39d8a` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png` | `156x210` RGBA, alpha `255..255` | `612b1cb2f08c75e6a5cd1fa6fdd5c05034c94195530dcab1fb30d5fb3960cb94` |
| Candidate decoded RGBA payload | `156x210` | `cd517bf9fe01cd3352b248afca3772090d03a24cb084223bedbd853ebd1bb7ed` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png.json` | JSON, metadata-integrity payload verified | `d18fac17074d2941dfe38a0ec8a71031c195d27a9dcde6fa8b76d02712cb719a` |
| `review/AFX_herman_baltia_commander_style_sheet.png` | `1344x464` RGBA, alpha `255..255` | `0469ea18c77e574b2d7c197d055aa32053bd55c2068fded725d40ea20ef1b790` |
| Style-sheet decoded RGBA payload | `1344x464` | `dff6e38a47d85a80570a77aa90351ef9df8699e1ead0b315e501290dda0446fc` |
| Canonical `eng_bernard_montgomery.png` | `156x210` RGBA | `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e` |
| Canonical `ger_erwin_von_witzleben.png` | `156x210` RGBA | `10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6` |

The trial-06 processor metadata records processor version `5.0`, role family `commander`, source kind `real`, raw repaint crop `(16,0,1081,1434)`, processor SHA-256 `1adb521b43238ee971e093dae90007c4c44c600435ebb897c6482ba3b64b96ec`, and status `candidate_requires_visual_approval`. The metadata's domain-prefixed decoded RGBA hashes independently recompute for the raw repaint (`0bf3f3809fb448ca51e4d68a44610587d473c91a83646e3b819cf2b708f39d8a`), candidate (`cd517bf9fe01cd3352b248afca3772090d03a24cb084223bedbd853ebd1bb7ed`), and style sheet (`dff6e38a47d85a80570a77aa90351ef9df8699e1ead0b315e501290dda0446fc`).

## Blockers and allowed next step

The identity gate is the primary non-compensable blocker, and the guarded stable-token transfer remains an independent runtime blocker. No DDS conversion, DDS equality proof, localisation transfer, GFX change, character change, or runtime wiring is authorized from trial 06.

The parent may retain trial 06 as export-only evidence and request another source-locked repaint whose narrow elongated skull, high sparse hairline, small unequal deep-set eyes, long narrow nose, hollow cheeks, compact ears, thin unequal moustache, long narrow neck, restrained expression, head angle, and shoulder proportions survive native and nearest-neighbour enlarged review. A new run should continue to use the immutable archival crop as the sole identity authority; the canonical commander references remain style-only.

Before any promotion, the parent must implement and review one atomic guarded transaction that retains `AFX_walloon_reserve_commander` and `GFX_portrait_AFX_walloon_reserve_commander`, removes the old `Marcel Delcourt` player-facing identity from every live surface, records Herman Baltia's historical-role disclosure, prevents duplicate or simultaneous ownership, converts only an independently approved `156x210` PNG, proves the DDS decoded-pixel equality, and then requests a fresh full IW-006 package audit.

## Audit boundary and changed files

No gameplay, runtime, GFX, localisation, source asset, processed asset, metadata, or DDS file was modified.

No audit simplification or fallback was used; the likeness gate was evaluated independently and fail-closed.

The only repository file created by this audit is `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_baltia_trial06_independent_portrait_audit_2026_07_24.md`.
