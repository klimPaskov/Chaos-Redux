# Event 006 Documentation Curator Handoff: KUB/ALT Correction

Timestamp: 2026-06-05 15:20:10 UTC

## Scope

Documentation-only cleanup for the user correction that Event 006 should stop expanding Kuban (`KUB`) and Altai (`ALT`). No gameplay, localisation, scripts, GUI, assets, spreadsheets, or binary files were edited.

## Files Changed

- `docs/events/006_independence_wave.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md`
- `docs/specs/006_independence_wave_specs/006_independence_wave_spec.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_145232_parent_event006_kuban_package_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_04_151704_parent_event006_altai_package_handoff.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_142822_parent_event006_catalog_125_focus_alignment.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_152010_documentation_curator_kub_alt_correction.md`

## Stale Claims Removed Or Superseded

- Removed KUB and ALT from the current verified package-anchor list in `docs/events/006_independence_wave.md`.
- Removed current Kuban Cossack Rada and Altai-Oyrot Kurultai package bullets from the Event 006 overview.
- Removed Kuban Black Sea Records and Altai-Oyrot Records from current starter-package route lists and formation-proof bullets in the Event 006 overview.
- Replaced KUB/ALT asset-planning text with a superseded note that no new KUB/ALT Event 006 flags, package icons, or overlay assets should be planned without explicit user request.
- Removed KUB/ALT from the implemented starter-package table in `006_independence_wave_country_packages.md`.
- Replaced package-spec implementation notes that accepted KUB/ALT as carriers with a superseded note.
- Reframed focus-tree KUB/ALT overlay rows as superseded historical candidate notes, not current overlay work.
- Added source-of-truth correction blocks to the event overview, country-package spec, focus-tree spec, and main Event 006 spec.
- Marked the 2026-06-04 Kuban and Altai parent handoffs as superseded historical tranche documentation.
- Marked the 2026-06-05 catalog 125-focus handoff as partially superseded where it mentioned current Kuban and Altai package summaries.

## Current Source Of Truth

The accepted current country-addition lane is niche generic Event 006 releases in underrepresented regions, especially Africa and South America.

Current examples:

- `ASN` Asante Council
- `KBN` Kanem-Bornu Authority
- `PLM` Palmares Council
- `AYM` Aymara Highland Congress

These releases should have unique flags, remain ordinary/generic Independence Wave releases, and share `independence_wave_liberation_provisional_tree`. They should not be promoted into bespoke package or formable overlays unless separately requested.

Event 006 evolution logs should remain tier-scoped only. Package-scoped evolution rows for every release remain out of scope.

Event 006 is still incomplete; this cleanup does not claim completion.

## Validation

Ran:

```text
rg -n "(KUB|Kuban|ALT|Altai).*(implemented|enabled|current|now receive|can be seeded)|(implemented|enabled|current|now receive|can be seeded).*(KUB|Kuban|ALT|Altai)" docs/events/006_independence_wave.md docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md docs/specs/006_independence_wave_specs/006_independence_wave_spec.md docs/plans/006_independence_wave_plans/subagent_handoffs
```

Result: remaining matches are superseded correction statements, historical candidate notes, historical/superseded handoff claims, or old audit evidence. No current source spec now says KUB or ALT are accepted current Event 006 package carriers.

Ran:

```text
rg -n "ASN|KBN|PLM|AYM|independence_wave_liberation_provisional_tree|niche generic" docs/events/006_independence_wave.md docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md docs/specs/006_independence_wave_specs/006_independence_wave_spec.md docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_145208_parent_event006_custom_generic_release_tranche.md docs/plans/006_independence_wave_plans/subagent_handoffs/2026_06_05_parent_event006_peripheral_host_release_gate.md
```

Result: source docs and recent parent handoffs now explicitly preserve the generic ASN/KBN/PLM/AYM lane and shared Liberation Provisional Tree behavior.

Ran:

```text
rg -n "[ \t]+$" <changed markdown files>
git diff --check -- docs/specs/006_independence_wave_specs/006_independence_wave_country_packages.md docs/specs/006_independence_wave_specs/006_independence_wave_focus_trees.md docs/specs/006_independence_wave_specs/006_independence_wave_spec.md
```

Result: no trailing whitespace in the changed Markdown files; tracked spec diff check passed.

## Remaining Parent Decisions

- Decide whether any gameplay/localisation/spreadsheet traces from the superseded KUB/ALT package tranches need removal or disabling. This curator pass intentionally did not edit those surfaces.
- Decide whether to update `docs/spreadsheets/chaos_redux_events_catalog.xlsx`; this documentation-only subagent scope did not edit the workbook.
- Decide whether old read-only audit handoffs that mention KUB/ALT as candidate research should remain as-is. They are not current source specs, but they still appear in broad grep output as historical audit evidence.
- Continue treating Event 006 as incomplete until the parent completes gameplay, localisation, assets, catalog alignment, audits, and validation.
