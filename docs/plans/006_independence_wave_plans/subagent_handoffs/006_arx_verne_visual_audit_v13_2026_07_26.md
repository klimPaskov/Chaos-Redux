# Event 006 ARX Vernè commander visual audit v13

Date: 2026-07-26

Status: **PARTIAL / candidate-only**.

This bounded audit covers the source, exact crop, raw source-locked ImageGen
repaint, deterministic 156x210 candidate, processor review sheet, and the nine
canonical commander references. It does not authorize a DDS, `.gfx` edit,
character edit, or runtime admission.

## Evidence inspected

- Unchanged source: `docs/assets/006_independence_wave/sourced_portrait_replacements_2026_07_26/arx_verne_commander_v1/source/ARX/Vittorio_Verne_source.jpg`.
- Exact crop and equality proof: `crops/ARX/Vittorio_Verne_archival_crop.png` and `metadata/ARX/Vittorio_Verne_archival_crop.json`.
- Raw source-locked repaint: `repaints/ARX/Vittorio_Verne_identity_preserve_imagegen.png`.
- Deterministic candidate: `processed/ARX/Vittorio_Verne_156x210.png`.
- Processor contact sheet: `review/Vittorio_Verne_processor_review.png`.
- Role-specific full-size commander reference pack under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/army_large/`.
- Source/rights/role evidence in `006_arx_roster_source_audit_2026_07_26.md`.

## Separate gates

| Gate | Result | Evidence |
|---|---|---|
| Attributed source and rights | PASS (bounded) | Wikimedia Commons source audit records `PD-Italy` and `PD-1996`; retain source page and hashes |
| Exact head-and-shoulders crop | PASS | Pillow equality JSON reports decoded-pixel equality and the recorded `(7,0,193,250)` crop |
| Male commander role | PASS | Candidate is a sourced male Italian officer; role is a commander slot |
| HOI4 native framing/canvas | PASS (bounded) | Deterministic candidate is 156x210 and fits the commander reference family |
| Identity likeness | PASS (bounded visual review) | Face, hat, uniform, and source-visible features remain recognizable in the repaint; no generic replacement was observed |
| HOI4 painted style | PASS (bounded visual review) | Restrained painted treatment, controlled contrast, period uniform, and subdued background match the commander family |
| Provenance/ownership | PASS (bounded) | Source and consumer ownership are recorded; no competing Chaos Redux/vanilla character owner was found |
| Runtime consumer | NOT RUN | Existing `ARX_gavino_piras` remains fictional and unwired; this candidate is not a replacement yet |
| Complete ARX package | BLOCKED | Crown/council role still lacks a rights-clear sourced male portrait, so one commander candidate cannot admit IW-018 |

The visual gates above are bounded evidence, not the parent package admission
decision. A future reviewer must repeat the comparison if the source,
repaint, crop, or processor changes.

## Required next step

Keep the candidate in `candidate_requires_visual_approval`/package-blocked
state until the ARX crown/council role has a source-ready male subject and the
parent country-package audit rechecks all live roles, flags, history, setup,
formable hooks, localisation, and runtime hashes together. Do not create a DDS,
edit `interface/006_independence_wave_mediterranean_portraits.gfx`, or change
`common/characters/006_independence_wave_mediterranean_characters.txt` from
this handoff alone.
