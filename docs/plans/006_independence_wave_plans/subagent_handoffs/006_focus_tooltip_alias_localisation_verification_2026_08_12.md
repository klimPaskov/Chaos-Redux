# Event 006 Focus Tooltip Alias Localisation Verification

Date: 2026-08-12

## Scope and concurrent-work note

This read-only verification covers the nine focus-ID completion-tooltip aliases assigned for the shared Event 006 focus tree.

The requested localisation edits and `006_focus_tooltip_alias_completion_2026_08_12.md` appeared in the shared worktree during this audit. They were preserved as concurrent work and were not rewritten or claimed by this verification.

## Verified keys

- `independence_wave_focus_build_permanent_foreign_service_tt` mirrors `independence_wave_build_permanent_foreign_service_tt`.
- `independence_wave_focus_discover_regional_identity_tt` mirrors `independence_wave_discover_regional_identity_tt`.
- `independence_wave_focus_coordinate_reclamation_fronts_tt` mirrors `independence_wave_coordinate_reclamation_fronts_tt`.
- `independence_wave_form03_open_charter_convention_tt` mirrors `independence_wave_form03_open_charter_convention_effect_tt`.
- `independence_wave_form03_define_public_service_guarantees_tt` mirrors `independence_wave_form03_define_public_service_guarantees_effect_tt`.
- `independence_wave_form03_establish_delta_works_board_tt` mirrors `independence_wave_form03_establish_delta_works_board_effect_tt`.
- `independence_wave_form03_build_federal_appeals_and_examinations_tt` mirrors `independence_wave_form03_build_federal_appeals_and_examinations_effect_tt`.
- `independence_wave_form03_harmonize_corridor_standards_tt` mirrors `independence_wave_form03_harmonize_corridor_standards_effect_tt`.
- `independence_wave_form03_submit_low_countries_compact_tt` mirrors `independence_wave_form03_submit_low_countries_compact_effect_tt`.

## Localisation audit result

- Missing keys: none among the nine assigned aliases.
- Duplicate keys: none among the nine assigned aliases. Each has exactly one definition across the two affected English localisation files.
- Scripted localisation issues: none in scope. The aliases do not introduce scripted-localisation calls.
- Dynamic text: the ratification tooltip preserves its existing duration and threshold constants. No additional dynamic text is needed for the other eight aliases because they mirror established, mechanically accurate completion text.
- Cross-surface mismatches: none found between an alias and its established completion tooltip.
- Encoding: `localisation/english/006_independence_wave_focus_l_english.yml` and `localisation/english/006_independence_wave_form03_l_english.yml` both retain UTF-8 BOM.
- Prose quality: no in-scope vagueness, bloat, obvious explanation, repetition within a displayed string, overcomplication, em dash, semicolon, staged contrast, staccato chain, or implementation-history wording requires another rewrite. Source and alias duplication is deliberate key compatibility, not repeated text on one player-facing surface.
- Sourced quotations: none of the nine tooltips contains an attributed or sourced quotation.

## Before and after display

Before the concurrent patch, the nine focus IDs lacked their `<focus_id>_tt` aliases even though each focus completion reward already pointed to a separately named, localised custom effect tooltip.

After the concurrent patch, every assigned focus ID has a single `_tt` alias with the same player-facing effect text as its established completion tooltip. Gameplay behavior, focus definitions, AI, icons, route gates, and central package authority are unchanged.

## References and validation

The offline `Localisation`, `National focus modding`, and `Effects` wiki pages confirm UTF-8 BOM focus localisation and localised `custom_effect_tooltip` usage. The installed vanilla `documentation/effects_documentation.md` documents simple localisation-key use for `custom_effect_tooltip`, and vanilla `common/national_focus/generic.txt` provides completion-reward precedents using separately localised custom effect tooltips.

A targeted source check found exactly one definition for every alias and source key, exact text equality for all nine alias/source pairs, and UTF-8 BOM on both affected localisation files. It also found no em dash or semicolon in the nine alias strings.

Fresh `hoi4.focus_inspect` for `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree` failed before inspection with code `ARTIFACT_MANIFEST_INVALID` and blocker message `Artifact provenance manifest is invalid` in workspace `mod_chaos_redux_ea3b2d67c2c0`. No MCP localisation-coverage or overflow evidence is claimed. A render was not attempted because the mandatory starting inspection route could not create a valid artifact-backed focus workspace.

## Remaining blockers and follow-up

The parent should retain the concurrent localisation patch and its implementation handoff. Focus-tree localisation coverage and overflow should be re-inspected and rendered after the MCP artifact provenance manifest is repaired.

No wording decision, missing mechanic, dynamic-localisation repair, sourced-quotation exception, or new design handoff remains in this bounded localisation tranche.
