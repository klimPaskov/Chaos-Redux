# Event 006 northern/western Europe advisor visual review

Review date: `2026-07-15`

## Approval result

All twelve candidates are approved. Each depicts a different fictional institutional specialist, survives the independent head-and-shoulders crop, remains readable at native `65x67`, and matches the subdued advisor-dossier grammar of the canonical vanilla references.

No candidate required a fallback, leader-art reuse, transform-only imitation, local face construction, or alternate conversion route.

## Source-master review

- Twelve independent official ImageGen calls produced twelve high-resolution masters.
- The dossier frame and paper/seal treatment are separate original ImageGen assets retained under `.agents/skills/chaos-redux-event-assets/assets/advisor_dossier_overlays/`; the processor only crops, grades, composites, validates, and exports those approved layers.
- Each master has a different face, age profile, hair treatment, clothing silhouette, institutional backdrop, and role cue.
- The set has six male-presenting and six female-presenting portraits. Gender presentation is explicit in crop metadata and must guide later generated-character names.
- Every source is period-appropriate and civilian/institutional. No modern clothing, modern object, medals, flags, propaganda pose, UI border, dossier paper, or readable generated text appears.
- The palette is restrained: charcoal, brown, olive, navy, maroon, cream, and weathered neutral interiors. None reads as glossy modern concept art.

## Crop review

Every crop rectangle was chosen directly from its own ImageGen master and recorded in processor metadata. The rectangles are not copied from a leader-size crop and no `156x210` leader output exists in this tranche.

At native and 5x nearest-neighbour review:

- all heads remain inside the portrait window;
- all eyes remain readable;
- the paper overlay does not hide the primary eye line or distinguishing facial feature;
- every card keeps a clear upper-torso or shoulder cue;
- no crop exposes generated text or modern detail;
- no face is stretched, padded, or visibly over-smoothed;
- silhouettes and expressions remain distinct across all twelve.

## Canonical advisor comparison

Every processed final was compared separately against:

1. `generic_europe_1.png`
2. `generic_female_europe.png`
3. `generic_asia_1.png`

Per-asset comparison sheets live under `contact_sheets/canonical_all_three/`. The review found:

- correct `65x67` canvas and compact head-and-shoulders scale;
- transparent outer corners;
- dark bevelled card with restrained warm edging;
- paper overlay occupying the lower-right dossier area;
- non-readable paper marks rather than invented text;
- subdued painted faces with enough contrast for HOI4 UI;
- slightly cleaner source detail than the older vanilla examples, but no photographic or glossy finish;
- no border break, frame shift, clipped eye, or missing paper layer.

## Per-asset disposition

| Stable stem | Review disposition |
| --- | --- |
| `advisor_RHI_independence_wave_municipal_customs_administrator` | Approved: round spectacles, receding hair, moustache, and burgundy tie remain readable; restrained municipal-office palette. |
| `advisor_RHI_independence_wave_rail_works_liaison` | Approved: auburn rolled hair and green jacket provide a distinct silhouette; paper does not obscure the expression. |
| `advisor_RHI_independence_wave_river_defense_planner` | Approved: square face and weathered engineering-office background read clearly at native size. |
| `advisor_BAY_independence_wave_district_finance_administrator` | Approved: rectangular spectacles, silver-streaked hair, and navy jacket survive the tight crop. |
| `advisor_BAY_independence_wave_estates_constitutional_liaison` | Approved: silver hair, pince-nez, and black constitutional-jurist silhouette remain distinct from the other male advisors. |
| `advisor_BAY_independence_wave_alpine_supply_inspector` | Approved: weathered cheeks and heavy wool coat communicate the alpine logistics role without costume exaggeration. |
| `advisor_SCO_independence_wave_shipping_authority_commissioner` | Approved: salt-and-pepper hair, close moustache, and charcoal tweed read as a sober shipping authority official. |
| `advisor_SCO_independence_wave_industrial_reconstruction_secretary` | Approved: copper waved bob, freckles, and brown wool jacket remain legible and period-authentic. |
| `advisor_SCO_independence_wave_territorial_defense_planner` | Approved: angular face, grey hair streak, and olive-grey field jacket keep a quiet defense-planning identity. |
| `advisor_WLS_independence_wave_bilingual_civil_service_commissioner` | Approved: oval spectacles, braided crown, and maroon jacket remain readable; the portrait supports a female name pool. |
| `advisor_WLS_independence_wave_coal_rail_organizer` | Approved: broad weathered face, curly dark hair, and worn blue work jacket remain distinct at native size. |
| `advisor_WLS_independence_wave_mountain_defense_planner` | Approved: short curls, narrow face, and charcoal service coat create a clear small-size silhouette without insignia. |

## DDS review

The decoded-DDS contact sheet is pixel-identical to the approved processed PNG set. Each runtime DDS has the expected `65x67` dimensions, alpha-bearing uncompressed BGRA header, exact `17,548`-byte length, and package/runtime byte equality.

## Remaining integration boundary

The art tranche is complete, installed, and registered. Runtime character handles exist in `common/characters/006_independence_wave_nwe_advisors.txt`; their sprite definitions are present in the dedicated `interface/006_independence_wave_nwe_advisors.gfx` registry. That parent-owned wiring is documented in `gfx_handoff.md`; the asset subtask itself intentionally made no `.gfx` edit.
