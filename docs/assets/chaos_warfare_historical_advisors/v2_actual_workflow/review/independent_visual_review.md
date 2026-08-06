# Independent Advisor-Card Visual Review

Review date: 2026-08-06.

Reviewer: parent integration review, performed separately from the `chaosx_portrait_creator` production session that generated the staged cards.

## Verdict

**PASS for the advisor-card asset and wiring gate.** This review does not claim that the wider CBRN system or the overall Chaos Warfare goal is complete.

## Evidence inspected

- Canonical advisor reference contact sheet: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/contact_sheet.png`.
- Canonical untouched template: `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/portraits/advisors/advisor_template.png`.
- Source portrait sheet: `../review/source_contact_sheet.png`.
- Native card sheet: `native_cards_contact_sheet.png`.
- Individual native cards: `../processed/*.png`.
- Individual nearest-neighbour 4x cards: `../review_4x/*_4x.png`.
- Full 4x card sheet: `v2_4x_contact_sheet.png`.
- Runtime DDS round-trip results recorded in `../manifest.md`.

## Review results

- All twelve cards use the same HOI4 advisor/theorist dossier family: dark irregular frame, paper tab, muted portrait treatment, and transparent outer corners.
- The canonical template remains the final top layer; no new frame, paper, emblem, shadow, or primitive replacement was drawn.
- All twelve identities remain readable at native and 4x review size.
- Headwear and clothing cues remain readable for Paul Fildes, Shiro Ishii, Masaji Kitano, and Franciszek Witaszek; the distinct eyewear and facial silhouettes remain readable for Florey, Fleming, Olson, and Baldwin.
- Ira Baldwin's leftward placement is intentional and keeps the face clear of the paper tab without exposing a generic or unrelated crop.
- No direct 156x210 portrait, plain 50x67 resize, generic advisor image, cross-type substitute, opaque-corner card, or unrelated Chaos Redux icon is present in the staged or live card set.
- The live DDS files are 65x67 one-level BGRA files and their decoded pixels equal the approved processed PNGs for all twelve cards.
- `interface/cbrn_historical_advisors.gfx` resolves every registered sprite to an existing card, and character wiring uses civilian-small for political advisors and army-small for theorists while retaining army-large scientist portraits.

The upstream historical identity and role evidence remains in `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-08-04_chaos_warfare_named_scientists_source_audit.md`. This review is limited to the advisor-card composition, native format, and runtime consumer wiring.
