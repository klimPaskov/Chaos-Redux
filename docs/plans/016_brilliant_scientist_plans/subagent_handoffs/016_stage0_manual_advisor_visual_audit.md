# Event 016 Stage-0 Manual Advisor Card Visual Audit

- Reviewer role: independent visual auditor (not the card producer)
- Review date: 2026-07-29
- Asset under review: `idea_doctor_warren_kruger_stage_0.dds`
- Runtime path: `gfx/interface/ideas/016_brilliant_scientist/idea_doctor_warren_kruger_stage_0.dds`
- Approved identity source requested for comparison: `gfx/leaders/KRG/leader_doctor_warren_kruger_stage_0.dds`
- Canonical role references inspected before individual comparison: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/contact_sheet.png`, with `generic_europe_1.png` as the named family reference.

## Verdict

**FAIL — independent visual approval is blocked.** The canonical advisor contact sheet and `generic_europe_1.png` were inspected, but the runtime DDS and approved identity DDS could not be decoded by the available visual inspection path in this audit turn. The asset therefore fails closed under the advisor-card visual gate; no positive visual claim is made from dimensions or filenames alone.

| Gate | Verdict | Evidence / reason |
|---|---|---|
| Kruger identity and readability at native 65x67 and 4x nearest-neighbour | FAIL (unverified) | Runtime card and approved identity DDS were not visually decoded, so identity continuity and face readability cannot be approved. |
| Frame and paper composition | FAIL (unverified) | The canonical family shows a dark irregular dossier frame, attached paper panel, and compact head-and-shoulders composition; the runtime card could not be compared at native or 4x size. |
| Transparent corners and edge artifacts | FAIL (unverified) | Corner alpha, fringe, holes, and texture continuity could not be visually checked from the final DDS. |
| Vanilla-family fit | FAIL (unverified) | Canonical advisor family was inspected, but the final card could not be compared against its frame silhouette, paper geometry, palette, and scale. |
| Original template face leakage in the replaced portrait window | FAIL (unverified) | The final card and source identity DDS could not be viewed side by side; template-face leakage is therefore not ruled out. |

## Required correction

Re-run this audit with a DDS-capable visual decode or an independently generated native/4x comparison sheet that includes the final runtime DDS, the approved Kruger identity DDS, and the canonical advisor references. Do not treat a PNG preview, header check, or producer-created evidence as a substitute for this visual gate. The card remains `needs_user_review`/not approved until every gate above receives a direct visual PASS.
