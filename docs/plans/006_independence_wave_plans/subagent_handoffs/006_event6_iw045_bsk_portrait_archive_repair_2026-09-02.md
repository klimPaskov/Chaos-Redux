# Event 006 IW-045 Bashkiria portrait archive repair handoff

Date: 2026-09-02

Status: complete; source-placeholder evidence recovered.

## Scope

This bounded repair reconciles the missing processed evidence recorded by the existing IW-045 Bashkiria portrait handoffs. It restores only the exact source crop, machine metadata, provenance record, review record, and manifest under the already accepted flat Event 006 portrait archive. It does not alter runtime DDS/GFX, character identity, gameplay, localisation, source attribution, or rights conclusions.

The archive parent remains `docs/assets/portraits/006_independence_wave/` with exactly one child directory, `processed/`. The processed directory remains flat with no subfolders and no retained `156x210` PNG.

## Recovered evidence

- `docs/assets/portraits/006_independence_wave/processed/iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_source_crop.png`: RGB `1125x1514`, 1,815,599 bytes, SHA-256 `0b8bc295b95910e750944ac48a41644ffae74e327764d5aa36b735961e1993e3`.
- `docs/assets/portraits/006_independence_wave/processed/metadata__iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_source_crop.json`: `chaos-redux-portrait-source-package-v1`, exact crop rectangle `[372,401,1497,1915]`, one accepted face box `[810,676,250,306]`, crop equality verified by RGBA SHA-256 `474dbf8c8e566f393d68292f62d9a6004705fd39c3002cbec7df3aecec78ca77`.
- `docs/assets/portraits/006_independence_wave/processed/metadata__iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin.txt`: grounded source-placeholder provenance and lifecycle contract, SHA-256 `99b437377ab591deff2addc1a69ca37f3cfc0c72c05af043bb1298c43cea93f8`.
- `docs/assets/portraits/006_independence_wave/processed/metadata__iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_manifest.json`: `chaos-redux-portrait-source-manifest-v1`, SHA-256 `816b4306c03a79e272894f797554e71d17da17bcd9ff01deb5c8990e02a26669`.
- `docs/assets/portraits/006_independence_wave/processed/BSK_yakov_bykin_review.md`: framing, provenance, archive/runtime boundary, and lifecycle review, SHA-256 `25ab2f87a1807e475cd34fbd317fa2ce2607a60f78238f9d07e8e20a3e75d072`.

## Source and lifecycle evidence

The unchanged source master remains `docs/assets/portraits/006_independence_wave/iw045_bsk_yakov_bykin_source_placeholder_2026_08_14__BSK_yakov_bykin_original.jpg`, RGB `1986x3178`, 1,184,558 bytes, SHA-256 `882608cf2ea282f5a603cc1c917f2b13a8b813d5c79857ee3d3e6a6c4fd02ddb`.

Existing IW-045 handoffs attribute the grounded source to Wikimedia Commons file “Быкин Яков Борисович, 1912”, uploaded/attributed to MDobrom, with the Commons-declared CC BY-SA 4.0 status. Attribution and share-alike obligations remain open; this repair adds no identity or rights claim. The source-placeholder state remains active until the user supplies an explicitly requested styled final. RunPod was not operated.

## Runtime boundary

The existing runtime consumer remains `gfx/leaders/006_independence_wave/portrait_BSK_independence_wave_yakov_bykin.dds` through `GFX_portrait_BSK_independence_wave_yakov_bykin`. The on-disk DDS is `156x210`, 131,168 bytes, SHA-256 `5dfe39dd9a7c72a1ac360ee3695b4779be67c10bad783458025433fdb0665e88`; it was not created or modified by this repair. No DDS output was produced in this archive-only reconciliation, and no `.gfx`, character, gameplay, or localisation file was edited.

## Validation

The active `extract_portrait_source_crop.py` package stage reproduced the accepted detector crop and recorded OpenCV YuNet evidence. The restored PNG was opened successfully and matches the accepted crop rectangle and RGBA equality hash. JSON metadata and manifest parse successfully. A recursive archive check found no filename containing `156x210`, no directory below `processed/`, and exactly one archive child directory (`processed`).

No blockers remain for this archive repair. Live in-game admission and any future styled-final replacement remain parent/user-owned lifecycle checks.
