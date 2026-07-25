# IW-002 Wales alternative sourced portrait clearance — 2026-07-25

This package contains two newly cleared, attributed male source candidates for the existing WLS Event 6 civic and mountain-commandant portrait consumers. It stops at immutable source masters and exact decoded-pixel crops. It does not contain ImageGen results, processed `156x210` portraits, DDS files, advisor or dossier assets, `.gfx` edits, localisation edits, or gameplay edits.

## Requirement and runtime crosswalk

| Requirement | Candidate | Reserved consumer | Status | Downstream boundary |
| --- | --- | --- | --- | --- |
| WLS civic or national leader | W. J. Gruffydd | `GFX_portrait_WLS_independence_wave_national_council` → `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_national_council.dds` | `needs_user_review` | Parent must reconcile the current `Saunders Lewis` localisation with any accepted identity before wiring. |
| WLS military, territorial, or mountain commander | Brigadier Lewis Pugh Evans VC | `GFX_portrait_WLS_independence_wave_mountain_commandant` → `gfx/leaders/006_independence_wave/portrait_WLS_independence_wave_mountain_commandant.dds` | `needs_user_review` | Parent owns character identity, localisation, source-locked repaint, independent review, and DDS conversion. |

## Candidate A — W. J. Gruffydd (civic)

- Identity: William John Gruffydd (1881–1954), Welsh scholar, poet and political figure.
- Source page: [W. J. Gruffydd.jpg](https://commons.wikimedia.org/wiki/File:W._J._Gruffydd.jpg).
- Direct unchanged master: `source_masters/w_j_gruffydd_original.jpg` (`3070x3962`, SHA-256 `b484a6e364adb0b006a8d67a5cdb8d5bc5beaddfc1f8582d3073a2aa87bbb313`).
- Archive and attribution: Cardiff University, archive item [CUA00764](https://archive.org/details/CUA00764), credited on Commons to Cardiff University.
- Photograph date: 1946.
- License: CC BY-SA 4.0, with attribution and ShareAlike obligations; preserve the source credit in every downstream provenance record.
- Lossless decoded master: `source_master_png/w_j_gruffydd_civic_master.png` (`3070x3962`, SHA-256 `46f597bb57013b01f10570d3d11670f664791ee490b4e0a8d97548dce24e3f13`).
- Exact crop: `source_crops/w_j_gruffydd_civic_crop.png`, rectangle `(left=0, top=190, right=2874, bottom=3590)`, `2874x3400`, SHA-256 `45a690657916cd18932dd1a525b8746f26f99a0a3f601fe2595027269081554b`.
- Crop evidence: `source_crops/w_j_gruffydd_civic_crop.json` records `decoded_pixels_equal: true`; the decoded master rectangle and crop output share RGBA SHA-256 `bc2c84041eab0636b7f78579997d65a760ea09f91fd36e6d10e897a437702a5c`.
- Visual fit: very high-resolution, evenly readable face with distinctive round glasses, bald crown, pronounced brow and nose, visible shoulders and period civilian jacket.
- Era note: the source is postwar (1946), not a 1936 photograph. It is a strong identity geometry candidate but remains `needs_user_review` until the parent accepts a period-adjusted, identity-preserving treatment.
- Ownership: no meaningful owner found in the current repository, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226` for `Gruffydd`, `William John Gruffydd`, `W. J. Gruffydd`, or `WJ Gruffydd`.

## Candidate B — Brigadier Lewis Pugh Evans VC (commander)

- Identity: Lewis Pugh Evans VC (1881–1962), Welsh-born British Army officer and later brigadier.
- Identity evidence: [biographical record](https://en.wikipedia.org/wiki/Lewis_Pugh_Evans) identifies his birth at Abermad, Cardiganshire, Wales, and later service as Military Liaison Officer at the Headquarters of the Wales Region during the Second World War.
- Source page: [Lewis Pugh Evans VC IWM HU 93411.jpg](https://commons.wikimedia.org/wiki/File:Lewis_Pugh_Evans_VC_IWM_HU_93411.jpg).
- Direct unchanged master: `source_masters/lewis_pugh_evans_iwm_hu93411.jpg` (`605x800`, SHA-256 `fdfde87660f50eb9a2112186878fb8ee93b7c1f0e2cb9f533ca9b2c41c26012c`).
- Archive and attribution: Imperial War Museums, collection no. 2500-02, HU 93411; Commons attributes the photograph to H. Walter Barnett.
- Photograph date: circa 1918.
- License: Public domain under the Commons `PD-Old` record; retain the Commons and IWM provenance even though attribution is not required.
- Lossless decoded master: `source_master_png/lewis_pugh_evans_commander_master.png` (`605x800`, SHA-256 `e63102da467856b28a7e14659b100f870b2897bb5cd1232aceac6e54fd19a1f7`).
- Exact crop: `source_crops/lewis_pugh_evans_commander_crop.png`, rectangle `(left=60, top=20, right=580, bottom=730)`, `520x710`, SHA-256 `7c12c4c993cba694c495267c1bd9bc285151fd9ce88c01c53d1b83d789d2ebb4`.
- Crop evidence: `source_crops/lewis_pugh_evans_commander_crop.json` records `decoded_pixels_equal: true`; the decoded master rectangle and crop output share RGBA SHA-256 `c3ee9bee1d58e2a84edc7afb56446a390ee9efbf3b7be0b68ab1cc849de1fd38`.
- Visual fit: single-person portrait with clear eyes, ears, jaw, moustache, cap, tunic, rank/medal bars and shoulders. The geometry is strong enough for source-locked commander repainting without reconstructing hidden detail.
- Era note: the source is a circa-1918 uniform portrait; Evans was alive at 55 in 1936. Downstream aging or period adjustment must preserve the facial geometry, moustache, asymmetry, and source-visible clothing constraints.
- Ownership: no meaningful owner found in the current repository, installed vanilla, Kaiserreich `1521695605`, or approved mods `2265420196` and `1458561226` for `Lewis Pugh Evans` or `Pugh Evans`.

## Comparison exclusions

- David Rhys Grenfell and George Cornwallis-West were not retried. Their earlier source photographs remain excluded because the parent reported repeated ImageGen likeness failures: enlarged or regularized eyes, broadened or frontalized faces, and altered moustaches.
- Aneurin Bevan was visually strong and period-matching, but Kaiserreich `1521695605` actively owns `ENG_aneurin_bevan`, recruits him, and supplies an army-small portrait consumer and localisation. He is not safe to clone without a guarded transfer contract.
- William Ambrose Bebb was visually clear and circa 1930, but Kaiserreich `1521695605` owns `WLS_ambrose_bebb` and its portrait/localisation consumers.

## Exact crop and provenance rule

Both crops were created with `.agents/skills/chaos-redux-event-assets/tools/extract_portrait_source_crop.py` using Pillow as the only decode/crop backend. The crop JSON files are retained beside the PNGs and prove exact decoded-pixel equality. The JPEG masters, decoded PNG masters, crop PNGs, metadata JSON, source page snapshots and contact sheet are distinct files; no source master was overwritten.

## Downstream handoff boundary

The parent may use either candidate only after accepting the era and license notes. The next stage must use the exact crop as the sole identity input for source-locked identity-preserving ImageGen, compare the raw result and deterministic `156x210` candidate against the unchanged source and the role-specific canonical references, obtain an independent likeness/style/provenance audit, and convert to DDS only after PASS. Raw source photos and merely resized crops are not runtime portraits.

