# IW-030 Montenegro identity amendment and portrait promotion plan

Date: 2026-08-01.

## Decision

The user approved continued work on the researched Mitar Martinovic lead. This is an explicit Event 006 roster amendment, not a relabel of `MNT_kristo_popovic`. The vanilla `MNT_kristo_popovic` character remains untouched for ordinary Montenegro and other origins. Event 006 may use the new stable character key `MNT_mitar_martinovic` after the full sourced-real-person portrait gate passes.

Mitar Martinovic (1870–1954) is a documented Montenegrin divisional general, former prime minister and minister of war, and commander of the Lovcen Detachment. His 1912 archival portrait is a period-appropriate male source for a country-leader/corps-commander identity in the Event 006 setting.

## Source chain

- Immutable master: `docs/assets/006_independence_wave/iw030_mnt_portrait_source_research_v87_2026_08_01/source_masters/mnt_mitar_martinovic_1912_chronicle.jpg`.
- Exact head-and-shoulders crop: `source_crops/mnt_mitar_martinovic_1912_head_shoulders.png`.
- Crop equality evidence: `crop_metadata/mnt_mitar_martinovic_1912_crop.json`.
- Source and role research: the v87 Montenegro source handoff and its cited 1914–1918 Online and World Statesmen records.
- Identity-preserving HOI4 repaint: `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_repaint_raw.png`.
- Deterministic native candidate: `generated_portraits/portrait_MNT_mitar_martinovic_hoi4_156x210.png` and `generated_portraits/portrait_MNT_mitar_martinovic_processing.json`.

## Runtime boundary

The new character must be recruited by the Event 006 Montenegro roster event and promoted only by the Event 006 constitutional/traditional government routes. It must define civilian and army large portraits using one stable sprite. The existing Popovic, Jovanovic, and Dukanovic keys are not silently renamed or overwritten. Jovanovic and Dukanovic remain separate evidence-only candidates until their independent rights decisions are resolved.

The package remains outside content attestation until the independent likeness/style/provenance audit passes and every live MNT roster consumer has an accepted non-generic portrait path. No DDS or `.gfx` wiring is authorized before that PASS.

## Pending gate

`event6_mnt_portrait_likeness_audit_v89` must record separate likeness, style, source-linkage, and provenance verdicts against the archival master, exact crop, raw repaint, native candidate, and the curated HOI4 leader/commander references. A failed or unresolved gate keeps the MNT package fail-closed.
