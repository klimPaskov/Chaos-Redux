# IW-006 Wallonia Herman Baltia trial 04 independent portrait audit

Audit date: 2026-07-24.

Reviewer: `/root/event6_wallonia_baltia_trial04_portrait_audit`, independent of the producing asset worker.

Audit scope: read-only review of `docs/assets/006_independence_wave/sourced_portrait_refinishes_2026_07_24/wallonia_herman_baltia_trial_04/` against the unchanged archival master, explicit crop and equality record, raw source-locked ImageGen repaint, deterministic `156x210` commander candidate, prompt, processor metadata, commander style sheet, and the two cited full-size commander references.

Final disposition: `FAIL`; trial 04 remains export-only and is not authorized for DDS conversion, localisation transfer, or runtime wiring.

The unchanged master, crop, raw repaint, candidate, and references were inspected at their native sizes and in disposable `4x` nearest-neighbour enlargements.

Identity is a separate non-compensable gate, so the candidate cannot be promoted even though its role, framing, and painted treatment are usable.

## Verdicts

| Gate | Verdict | Independent evidence |
|---|---|---|
| Provenance and source equality | **FAIL (record binding)** | The trial-04 master is the unchanged public-domain Commons upload `source_masters/AFX_herman_baltia_1909_master.jpg`, `389x473` RGB, SHA-256 `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66`, as declared in `manifest.md`. The retained crop is byte-identical to the same rectangle from the trial-04 master, and the decoded RGBA payloads independently hash to `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326`. However, `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` records both its `master.path`, `output.path`, and normalized command under `wallonia_herman_baltia_trial_03/`, not `wallonia_herman_baltia_trial_04/`. The trial-03 and trial-04 files currently share the same hashes, but the trial-04 equality record is not self-contained or correctly bound under the fail-closed provenance gate. |
| Explicit head-and-shoulders crop | **PASS** | `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` is `353x461` RGB and records rectangle `(20,12,373,473)` from the `389x473` master. Direct Pillow decoding of the trial-04 master and retained crop produced equal pixels for all `162733` RGBA pixels. The crop keeps the head, neck, collar, both epaulettes, and both shoulders without resizing, recolouring, enhancement, or retouching. |
| Male-only and commander role fit | **PASS** | The master, crop, raw repaint, and candidate show one male officer. `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-63` sets `AFX_walloon_reserve_commander` to `gender = male` with only `civilian.large` and `army.large` commander surfaces. The documented historical role is a Belgian lieutenant-general tied to the Arlon 10th Line Regiment and the later Chasseurs Ardennais lineage, while the package explicitly limits the Event 6 position to an alternate-history territorial/reserve-command abstraction and does not claim that the 1909 uniform is a 1936 uniform. |
| Identity and likeness preservation | **FAIL** | At native and `4x` nearest-neighbour inspection, the repaint does not preserve the source-locked facial geometry. The source has a narrow elongated skull and jaw, a high sparse receding hairline, small deep-set eyes with visible size/height asymmetry, a long narrow nose, hollow cheeks, a narrow rounded chin, compact ears, and thin unequal upswept moustache curls. The raw repaint and processed candidate broaden and round the skull/jaw, fill the cheeks, enlarge and nearly symmetrise both eyes, broaden and shorten the nose, round and widen the chin, thicken and regularise the moustache, enlarge/protrude the visible ear, and make the sparse hairline fuller and more regular. The neutral frontal pose is retained, but the eye enlargement changes the expression and the neck is broader/shorter than the source. These are material identity changes rather than permissible painted-style variation. |
| HOI4 painted commander style | **PASS** | `processed_png/portrait_AFX_walloon_reserve_commander.png` is a full `156x210` restrained oil/gouache-style portrait with muted period colour, matte brush texture, controlled contrast, dark neutral background, and no text, watermark, frame, UI, or cinematic treatment. The style sheet compares it against the two cited full-size commander references, `eng_bernard_montgomery.png` and `ger_erwin_von_witzleben.png`, each `156x210`; their recorded hashes match the skill-local canonical and quick-reference copies. |
| Framing and readability at `156x210` | **PASS** | The processed candidate decodes as opaque RGBA `156x210` with alpha minimum and maximum both `255` and no transparent pixels. The head has safe top margin, both shoulders and epaulettes remain inside the canvas, and the face, collar, medal, and shoulder silhouette remain readable at native size. The candidate has no dossier frame or card treatment. |
| Ownership and guarded transfer integrity | **FAIL (not cleared)** | Exact and variant searches in current project character/history/GFX/interface/localisation roots and installed vanilla roots found no active Herman Baltia/Baltia character or portrait owner. The stable token is nevertheless already owned by `AFX_walloon_reserve_commander` at `common/characters/006_independence_wave_wallonia_frisia_characters.txt:53-63`, recruited by `history/countries/AFX - Wallonia.txt:18`, and registered by `interface/006_independence_wave_region_01_portraits.gfx:14-15`. Player-facing localisation still names that token `Marcel Delcourt` at `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml:4`, and the Emergency Works Command description repeats that name at line 91. `manifest.md` proposes a guarded transfer but this trial contains no explicit transfer/availability contract and no localisation or cleanup change that clears the old identity. Under the fail-closed reuse gate, absence of an origin owner is not itself a guarded transfer contract. |
| Absence of advisor, dossier, operative, and `_small` derivatives | **PASS** | The trial-04 workspace contains only the master, exact crop and JSON, raw repaint, full commander candidate and metadata, prompt/manifest, and commander style sheet. No trial-04 path or file contains `advisor`, `dossier`, `operative`, or `_small`; processor metadata has `advisor_composition`, `advisor_validation`, and overlay fields set to `null`. No new derivative was created or wired by this audit. |

## Retained artifact hashes and dimensions

| Artifact | Dimensions and mode | SHA-256 |
|---|---|---|
| `source_masters/AFX_herman_baltia_1909_master.jpg` | `389x473` RGB | `73597e416240754b2f5a9c78aac4798287b58642f1abd93c920f3020d95a1b66` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.png` | `353x461` RGB | `4980ac2a82fae576809adc1b10141ca711118bbbc58548c63942e4650a7a25a1` |
| Crop decoded RGBA payload | `162733` pixels | `b3e0a376db6422eab69cf85ef3192a461ff2588d59b379b31e4265b59c5cb326` |
| `source_crops/AFX_herman_baltia_1909_head_shoulders_crop.json` | JSON | `4eef10b5531c8c1660d684af5f35826204bce36f7d2ce4435a0c5871e48ac3ad` |
| `imagegen_results/AFX_herman_baltia_identity_preserve_trial_04.png` | `1081x1455` RGB | `263e508706059ad2b63ad615a8f7d17b8075e3d52442f6a89b63c924ff59b961` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png` | `156x210` RGBA | `d6b617411d67535e3e4f5bdb90333569b37e07027b185cc14831bb1f2a4aed10` |
| `processed_png/portrait_AFX_walloon_reserve_commander.png.json` | JSON | `23b0b71b700550050103550e8cf69aa50e1f3e221bc0cdc187336aff167f7514` |
| `review/AFX_herman_baltia_commander_style_sheet.png` | `1344x464` RGBA | `29bd756f435fcbfd3d039fc98f286e903f9eec7822efe6ac9d1b3a4094149200` |
| Canonical `eng_bernard_montgomery.png` | `156x210` RGBA | `39b03871d7451ca96712a5ccf3c056528693f82642776e6c5e297e041943944e` |
| Canonical `ger_erwin_von_witzleben.png` | `156x210` RGBA | `10f4a1108f9d440213f70fb5802349a2291f298f9d132644241119561577d5b6` |

The existing runtime DDS at `gfx/leaders/006_independence_wave/portrait_AFX_walloon_reserve_commander.dds` remains untouched and is not this trial candidate.

## Required next step

Do not convert or wire trial 04 and do not rename `AFX_walloon_reserve_commander` from `Marcel Delcourt` based on this candidate.

Correct the trial-local crop JSON so its master, output, and normalized command paths point to `wallonia_herman_baltia_trial_04/`, while retaining the same exact decoded-pixel equality proof and hashes.

Regenerate the source-locked repaint from the unchanged archival crop until the narrow skull/jaw/chin, high sparse hairline, small unequal deep-set eyes, long narrow nose, hollow cheeks, compact ears, exact moustache asymmetry, neck length, and shoulder proportions survive both native and `4x` review without identity drift.

Before any promotion, document an explicit guarded stable-token transfer/availability contract that prevents simultaneous ownership, then obtain a fresh independent audit with separate provenance, likeness, style, role, framing, male-only, ownership, and consumer-boundary PASS results.

## Audit boundary and changed files

No gameplay, runtime, GFX, localisation, source asset, processed asset, metadata, or DDS file was modified.

The only repository file created by this audit is this handoff: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_wallonia_baltia_trial04_independent_portrait_audit_2026_07_24.md`.
