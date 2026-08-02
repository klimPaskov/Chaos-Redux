# IW-043 CHU Ishaki portrait repaint handoff v01

Date: 2026-08-03.

Scope: source-locked, identity-preserving HOI4-style male country-leader portrait evidence for the proposed `CHU_independence_wave_federal_presidium` consumer.

The producer used the existing archival Gayaz Ishaki source package and an explicit head-and-shoulders crop. ImageGen produced a source-locked repaint using the canonical HOI4 leader references for style only. The original-size repaint, deterministic `156x210` review candidate, native/4x review sheet, prompt, processing metadata, and hashes are retained in the ignored event workspace at `docs/assets/006_independence_wave/iw043_chu_portrait_repaint_2026_08_03/`. The durable ComfyUI source/prompt pair is under `docs/assets/portraits/006_independence_wave/` and is not runtime storage.

## Evidence state

| Gate | State | Boundary |
| --- | --- | --- |
| Grounded male identity | Evidence complete | Gayaz Ishaki is a real interwar Tatar political organiser. The subject is not a generated person. |
| Exact source crop | PASS | The existing crop JSON records the crop rectangle and decoded-pixel equality. |
| HOI4-style repaint | Producer evidence complete | The raw repaint preserves the source face, hair, moustache, collar, tie, and shoulders. An independent likeness/style audit is still required. |
| Original-size master | Present | The processed original-size PNG is byte-identical to the raw ImageGen result. |
| `156x210` candidate | Present | Candidate is review-only and has no DDS conversion. |
| Rights/provenance | `needs_user_review` | Commons public-domain templates are present, but photographer and first-publication jurisdiction are not established. |
| Runtime consumer | Blocked | No DDS, `.gfx`, character, localisation, or admission change is authorized by this handoff. |

## Runtime and role restrictions

The proposed consumer is country-leader/institutional only. Do not create an advisor, commander-small, dossier, operative, generic, duplicate, or `_small` derivative. Do not wire the durable ComfyUI pair or the event-scoped workspace into runtime. CHU remains outside the exact Event 006 content-attestation set until the rights decision, independent portrait audit, and full country-package audit pass.

## Required next evidence

1. An independent reviewer must inspect the unchanged source, exact crop, raw repaint, `156x210` candidate, and HOI4 leader references at native and at least 4x nearest-neighbour scale.
2. The reviewer must issue separate likeness, style, provenance, and role findings.
3. The project owner must resolve the unknown photographer and first-publication jurisdiction before DDS conversion or runtime promotion.
4. If those gates pass, the parent may convert the candidate to the existing proposed DDS path and update the character/GFX consumer, package readiness receipt, and admission audit together. No fallback identity is authorized.

No gameplay files were changed by this portrait tranche. Whole-event completion remains blocked by the CHU source gate and the wider package, capacity, formable, asset, audio, catalog, AI, and balance gates recorded in the current Event 006 completion authority.
