# CBRN research cost review

Disposition: implemented bounded source calibration, with native field precision and calendar rounding unresolved; matching probability replay and a reverse structural technology comparison are retained as partial evidence.
The parent accepted five-decimal downward cost factors on 2026-10-08 as the closest bounded source representation of the user's 50/75/100 base-day instruction over the installed 110 base cost.
Native cost-field precision and calendar completion rounding remain explicitly unproved.
This is a cost calibration, not an observed exact-calendar-day claim.
The parent authorized application after its technology pre-scan and the auditor's live-source 25+2 candidate baseline were captured.
Gameplay changes are confined to `common/technologies/chaosx_technologies.txt` and `common/technologies/cbrn_regimental_support_technologies.txt`.
This report and `docs/testing/2026-10-08_cbrn_research_cost_review/` contain the research, source checks, and immutable before/after evidence.
The completed reconnaissance report and reconnaissance gameplay values remain untouched.

## Confirmed effective base and acceptance basis

Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/defines/00_defines.lua:706-710` sets `NTechnology.BASE_TECH_COST = 110` and describes multiplication by technology cost and ahead-of-time penalties.
Its SHA-256 is `405a24ce579815443cafe052cff1361e20c712ca8182e3f10ccbf45330dd4be4`.
The other two installed base define files, the installed DLC loose define surface, the one installed DLC ZIP archive, and the mod define file contain no overriding technology base cost.
`common/defines/chaos_redux_defines.lua` is empty, SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
`descriptor.mod` declares no dependencies and replaces only loading-screen assets.
`effective_defines.json` retains the scanned definition files, exact match lines, revisions, and DLC archive coverage.

Offline `paradox_wiki/Defines - Hearts of Iron 4 Wiki.md:647` also records 110.
Offline `Technology modding:248` still describes cost 1 as 100 base days, and its reference at line 810 repeats the obsolete define value 100.
The installed define governs this calculation.
Consequently the frozen before-source .5/.75/1 factors yield 55/82.5/110 unmodified base-day costs.

The parent states the original direct user instruction requires 50/75/100 base days and takes precedence over the relative percentage wording in accepted spec 13 at line 55.
The existing requirement ledger `docs/plans/chaos_warfare_system_plans/2026-09-20_cbrn_overhaul_requirement_ledger.md:18` independently retains that 50/75/100 base-day requirement.
The parent owns reconciliation of that spec wording and other authoritative documentation.
An implementation should describe these as base-day targets, with representation tolerance and native rounding uncertainty, rather than relabeling them relative percentage bands.

## Frozen researchable mapping

All 27 entries have a technology folder and lack an unconditional research prohibition or project-only marker.
Researchability here means the authored ordinary research surface, subject to its existing prerequisite and `allow` gates.
It does not mean every country can research all entries immediately.
The exact IDs, file paths, definition and cost-field line numbers, resolved costs, and exclusions are frozen in `research_cost_inventory.json`.

| File and frozen before factor | Target base days | Exact researchable IDs |
| --- | ---: | --- |
| `common/technologies/chaosx_technologies.txt`, `@CBRN_TECH_COST_BASIC = .5` | 50 | `pathogen_handling_protocols`, `bio_surveillance_networks`, `livens_projector_tech`, `chlorine_gas`, `basic_gas_masks`, `field_decontamination_kits`, `chemical_detection_paper` |
| Same file, `@CBRN_PROTECTION_TECH_COST_STANDARD = .75` | 75 | `sealed_containment_laboratories`, `rapid_outbreak_response`, `phosgene`, `mustard_gas`, `dimercaprol`, `improved_livens_projector`, `improved_gas_masks`, `mobile_wash_columns`, `mobile_sampling_laboratories` |
| Same file, `@CBRN_PROTECTION_TECH_COST_ADVANCED = 1` | 100 | `fail_safe_containment_facilities`, `integrated_epidemic_control`, `lewisite`, `tabun`, `advanced_livens_projector`, `advanced_gas_masks`, `sealed_assault_protection`, `rapid_decontamination_plants`, `theater_cbrn_command_set` |
| `common/technologies/cbrn_regimental_support_technologies.txt:185`, `@CBRN_REGIMENTAL_TECH_COST_NORMAL = .75` | 75 | `field_epidemiology_teams` |
| Same file at line 227, `@CBRN_REGIMENTAL_TECH_COST = 1` | 100 | `mobile_cbrn_hospitals` |

Counts are seven basic, ten standard, and ten advanced.
The shared `chaosx_technologies.txt` file's unrelated technologies and `@CHAOS_ASSAULT_TECH_COST` consumers are outside this correction.
The HQ, project-equipment, and aerosol-module-variant technology files expose only grant-only markers in the reviewed package and require no research cost correction.

Two byte-exact source snapshots are retained under `before_source/`, with paths and matching source/snapshot hashes in `before_source_manifest.json`.
The main file revision is `d52d48eb5796c120e5bd465dddcd5527a6597f7a60cf68f871c6240d05b1f5c1`.
The regimental file revision is `45826eb81040942fdc2fe9b32c61fdb9be09f625ce37ae655ac6e761415c6cb4`.

## Accepted factor representation and limits

| Target | Exact ratio | Accepted downward literal | Decimal source base cost | Shortfall |
| --- | --- | --- | --- | --- |
| 50 days | `50 / 110` | `.45454` | `49.9994` days | `.0006` day |
| 75 days | `75 / 110` | `.68181` | `74.9991` days | `.0009` day |
| 100 days | `100 / 110` | `.90909` | `99.9999` days | `.0001` day |

These are five-decimal floors of the exact ratios and each stays below its target by less than .001 day in decimal source arithmetic.
The tolerance is a numeric representation of the accepted target, not a newly selected research duration.
Upward decimal rounding is unsuitable for this source guard because it can produce a value slightly above an integer-day boundary.

Installed `documentation/script_concept_documentation.md:228-249` demonstrates fixed-point constants with `pi = 3.14159`.
Offline `Data structures:425-434` explicitly documents five-decimal accuracy and truncation for the variable system at line 427.
Neither section specifies the native technology `research_cost` reader's precision.
The inspected installed technology sources contain no `research_cost` literal with four or more decimal places.
No inspected local section proves native calendar completion or tooltip rounding.
Therefore the accepted factors establish a bounded source representation, without proving exact observed 50/75/100-day completion.
For example, a hypothetical three-decimal round-to-nearest reader would turn the first two factors into .455/.682 and yield 50.05/75.02 source days.
That reader is a counterexample to a guaranteed-native claim, not an established engine behavior.
The parent accepted the five-decimal representation with this uncertainty and no alternate duration fallback was implemented.

## Implemented scoped correction

1. The main file's existing basic/standard/advanced research constants resolve to `.45454/.68181/.90909`.
2. File-local `@CBRN_GRANTED_TECH_COST_BASIC = .5` and `@CBRN_GRANTED_TECH_COST_ADVANCED = 1` preserve hidden-marker raw costs.
3. Seven hidden basic-marker `research_cost` fields use the basic grant constant: `civil_defence_fitting_and_registration`, `military_filter_standardization`, `rapid_filter_replacement`, `vehicle_overpressure_and_sealed_compartments`, `portable_anemometer`, `meteorological_stations`, and `upper_air_soundings`.
4. The project-only `sarin` and `soman` raw cost fields use the advanced grant constant.
5. In the regimental file, `@CBRN_REGIMENTAL_TECH_COST_NORMAL = .68181` supplies Field Epidemiology Teams.
6. File-local `@CBRN_REGIMENTAL_RESEARCH_COST_ADVANCED = .90909` supplies only Mobile CBRN Hospitals' research cost.
7. The regimental `@CBRN_REGIMENTAL_TECH_COST = 1` and its seven hidden consumers retain their original values.

No CBRN research cost mirrors were found in `common/script_constants/`, so no shared cost mirror needs correction.
Do not introduce shared `constant:` tokens into these native cost fields because their support has not been established.
No helper, event target, variable lifecycle, cleanup hook, global define, research speed, chronology, grant, stat reward, or AI coefficient change is needed.
The source correction affects all 27 researchable costs while preserving the resolved raw cost and complete body of every hidden or unrelated technology.
All non-cost fields of the 27 corrected technologies also retain their original ASTs.

The final gameplay hashes are:

| File | After SHA-256 |
| --- | --- |
| `common/technologies/chaosx_technologies.txt` | `4f3743d8d911b2b818cc0d3093417f4b8c2ad21330e00a8fdbba9f62e9e7c998` |
| `common/technologies/cbrn_regimental_support_technologies.txt` | `d1f9f1e0444b899019264d73025bd951f84e5e754ebf7cc8cb30cbc8752d3eb6` |

`after_source/` and `after_source_manifest.json` retain matching byte-exact final snapshots.
The local `.gitattributes` disables newline conversion for both snapshot directories.
The before snapshots and their manifest remain unchanged.
Earlier reconnaissance and force-audit source hashes remain historical evidence of their captured states and are not claimed to match these final cost-calibrated files.

## References and validation handoff

`reference_and_source_lookup.json` retains successful MCP reference_context/search/read results and exact vanilla/mod source lookups.
Installed define files were read directly because the reference index does not include that Lua source as installed documentation.
Both installed and offline required source kinds were covered by the technology context, with no omitted required source kind.
`script_doc` was unavailable and no native source coverage is claimed.

Revision-bound sections read through MCP:

- Offline Technology modding, lines 244-253, revision `c5428838db20c4c812c66aff82cbafc58db3b73453c30436bce0d97436170bee`.
- Offline Defines, line 647, revision `61ae03fd36bcbe2ab6ca1304b013d3f432b88e6592856fffdd2685f792e87fcc`.
- Installed script-concept fixed-point example, lines 228-249, revision `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`.
- Offline Data structures variable precision, lines 425-434, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.

Live source_lookup resolved `basic_gas_masks` at `mod:common/technologies/chaosx_technologies.txt:982-999` without override/shadowing findings.
It resolved vanilla `construction1` at `game:common/technologies/industry.txt:1672-1684`, where `research_cost = 2` is separate from `start_year`, categories, and placement.
The lookup revisions are retained in the evidence bundle, and vanilla file SHA-256 is retained in the inventory revision list.
These establish exact source precedent and field placement, not native rounding.

Completed research checks: installed/DLC/mod base define coverage, 27 ordinary recipient mapping, 21 excluded cost-bearing grant markers, hidden/unrelated alias risk review, no shared cost mirror found, byte-exact before snapshots, and exact downward decimal arithmetic.

Command from the mod root:

```powershell
node docs/testing/2026-10-08_cbrn_research_cost_review/source_tests.js
```

All 40 task-specific checks passed with result `passed_source_calibration_native_precision_unproved`.
The test reads actual source with the bounded Clausewitz parser pattern already used by the October 7 doctrine audit, without a runtime VM or new general framework.
When run in an extracted candidate tree, both edited technology files are read from that tree; untouched repository inputs are checked against hash-guarded captured files with only CRLF/LF conversion permitted.
Installed game definitions remain external inputs, and immutable before snapshots retain strict byte hashes.
It confirms all 27 exact candidate IDs against both the frozen inventory and the probability auditor's 25+2 candidate baseline, all 27 effective cost factors, exact downward ratios, and under-target shortfalls smaller than .001 day using integer decimal arithmetic.
The frozen before source reproduces all 27 over-costs.
Whole normalized AST comparison covers all 50 technology bodies in the two edited files, allowing only the 27 researched cost fields to change.
The remaining 23 technology bodies are fully preserved after constant resolution.
Every AI block is preserved both as raw tokens and after constant resolution, and an exact permitted raw-AST patch comparison rejects any collateral constant or field edit.
All 21 excluded cost-bearing markers retain their full resolved bodies and costs, including byte-hash preservation for the separate untouched HQ and project-equipment files.
`source_test_results.json` records named checks, final source revisions, all 27 cost rows, and preservation counts.

The parent's technology pre-scan revision is `4d8ab41c2e52c7d5690399e37155cd68388182e2b6347ebd787d21717fb60a23`.
The probability auditor captured live canonical-source inspection, evaluation, and rendering for the same 25+2 candidates before this patch, with six year-bound named scenarios.
`docs/testing/2026-10-08_cbrn_research_cost_probability/scenario_plan.json` records scenario hash `6af9cf175c3e31a2977acb6971aa71414d2ca9bff98567194e20dad5633fd467` and explicit unresolved external factors.
Its doctrine/context names are labels, with no fabricated doctrine, project, actor, or prerequisite state.
The original scenario hash is historical and does not establish identity with the saved fixture.
The probability auditor's captured exact-fixture replay in `docs/testing/2026-10-08_cbrn_research_cost_probability/reconciliation.json` reproduces scenario hash `9014abc855784fcdc7f9cba67f0c7d33afff123b1402db73949c381209e7c004` in both frozen-before evaluations and both comparisons.
Those comparisons report zero adapter-exposed score changes, with source numeric expressions and native external research factors still unresolved.
The parent's `docs/testing/2026-10-08_cbrn_research_cost_review/parent_technology_comparison.json` records a partial reverse comparison from current sources to virtual original costs, with zero added, removed, renamed, moved or regression counts.
The full comparison artifact could not be read because its provenance manifest was unavailable; numeric metadata deltas are therefore not claimed from that receipt.
Authoritative spec and guide corrections are recorded in `docs/plans/chaos_warfare_system_plans/2026-10-09_research_costs_and_numeric_text.md`.
These partial comparisons and source tests do not establish native calendar rounding or normalized overall research selection.
No index change, commit, game launch, or log search was performed by this worker.
No fallback or simplification was implemented.
Native field precision and calendar rounding remain the known limitation.
Skills applied: `chaos-redux-events` and `chaos-redux-subagents`, with no skill changes.
