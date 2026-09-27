# Bounded CBRN documentation reconciliation

**Disposition: implemented (documentation only); parent integration and engine validation remain open.** This pass changed only living Markdown guides under `docs/systems/cbrn_warfare/`. It did not change gameplay, localisation, assets, skills, spreadsheets, Event 020 or Event 026 docs, or the U.S. 1939 mustard correction. The parent requested no commit.

## Source-of-truth map

| Claim | Authority or evidence | Current boundary |
| --- | --- | --- |
| Three MIO families, six named historical organizations, two fictional advanced organizations, and force-scaled historical masks | The user's 2026-09-20 overhaul request and 2026-09-25 follow-up, recorded in `docs/specs/chaos_warfare_system_specs/specs/13_2026_09_20_accepted_cbrn_overhaul.md` | Accepted design; the `2026-09-20_cbrn_overhaul_requirement_ledger.md` and `2026-09-25_cbrn_overhaul_completion_report.md` distinguish source implementation from remaining consumer evidence. |
| Scientist dates, fields, skills, and later trait awards | The accepted overhaul's date-appropriate roster requirement, the 2026-09-27 scientist correction notes, and the completion report's current source count | Implemented in source as 67 definitions with 39 direct and 28 dated recruitment paths; native recruitment and project selection are unverified. |
| DuPont polymer-clothing signature | `docs/specs/chaos_warfare_system_specs/corrections/2026-09-27_dupont_polymer_mio_signature.md` and the current completion report | Implemented in source; native MIO card fit and combined production effects remain unverified. |
| Event 020 cancellation, Event 026 post-sale successful-raid credit, same-mask hazard cap, and random project repeat guard | The linked 2026-09-27 corrections and current completion report | Kept as source-backed implementation with the ledger's stated engine, visual, and probability limits; no new completion claim was made here. |

## Files changed and dispositions

| File | Disposition and evidence |
| --- | --- |
| `docs/systems/cbrn_warfare/cbrn_historical_scientists.md` | Reconciled living source guide. Corrected Maass, Koizumi, Olson, Rosebury, Fred, Muromtsev, and Tarbell rows; dated later inhumane traits for Hirt, Bickenbach, Rose, and Mrugowsky; corrected AST/CAN callbacks, advisor dates, bookmark exclusions, and 39/28 recruitment counts from the accepted scientist correction notes. Preserved approved portrait status. Engine outcomes remain unverified. |
| `docs/systems/cbrn_warfare/cbrn_designers.md` | Added an explicit historical-snapshot notice directly under the superseded six-family heading. The current three-family source contract, DuPont correction, and existing MIO visual limit above it remain the active account. No old design section was deleted. |
| `docs/systems/cbrn_warfare/overview.md` | Replaced the apparent five-tab GUI status with links to the accepted amendment, ledger, and completion report, and marked the old six-family, six-HQ, readiness-animation asset list and future-stage list as historical planning material. The old list remains for provenance and is not a current requirement. |
| `docs/plans/chaos_warfare_system_plans/subagent_handoffs/2026-09-27_cbrn_bounded_documentation_reconciliation.md` | This handoff records the source map, document dispositions, and limits for parent review. |

No plan or addendum was promoted, rejected, or marked fully complete. The six-family content remains **superseded** by the accepted overhaul amendment and current three-family account. The scientist correction notes remain **implemented in source** with native recruitment and project behavior unresolved. The Event 020, Event 026, hazard, and random-project corrections were left unchanged because the current ledger and completion report already state the latest source behavior and validation limits. No prompt was edited; the previously superseded six-family and readiness instructions in the overview now have a local warning.

## Contradictions, duplicates, and hard wraps

The living scientist roster previously gave several obsolete skills, fields, and static inhumane traits, while its advisor paragraph retained old Blome, Witaszek, and Mairanovsky gates. Those contradictions were corrected from the dated source notes. The overview's apparent current six-family and six-HQ asset requirements and five-tab GUI wording were demoted to historical planning status. The designer guide's six-family prose was already under a superseded heading; the added notice makes its present-tense sentences explicitly archival. No duplicate document was merged or deleted. No accidental mid-sentence Markdown hard wraps were found in the changed passages; table rows, headings, and paragraph boundaries were preserved.

The remaining person-specific scientist role, skill, and trait proposals in the source-audit handoffs are unresolved. Native recruitment at the 1936 and 1939 bookmarks, project-scientist selection, MIO list/detail fit, MIO effect aggregation, and Event 020/026 native lifecycle behavior still need owner and parent review. This pass made no decision about the U.S. 1939 production-line question.

## MCP and validation evidence

The connected `hoi4.gui_inspect` route accepted a targeted `industrial_organization_detail` request and returned `GUI_INSPECTED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b920df19830b19c64e0be8d860d18baa5617f40d49190925fb4e597de115bb52/9cce17106bdc4d5828a8a92bfaf9d021761fdfe039eb85f6573067c46ec0541f/gui-inspect.1872b5e91ef0d783.json`. This response exposed an artifact but no model-visible element count or native card render, so it does not establish MIO visual fit. The earlier designer guide's GUI inspection likewise reports zero inspected elements. Tool exposure and this successful route call establish only the route's availability, not service-wide health or a standalone viewer. The completion report's partial event, technology, GUI, and probability artifacts were preserved as bounded evidence; this pass made no new gameplay or weighted-logic conclusion. The separate `chaosx_ai_probability_auditor` random-project handoff reports nine unchanged source weights but a partial four-scenario comparison with 78 unresolved items.

Targeted searches for obsolete scientist rows, six-family claims, readiness-animation language, and current evidence status informed the patch. The final diff was reviewed for the four owned Markdown files. No native game launch, workbook read, broad repo audit, new event/technology/weighted scenario, or native MIO panel render was performed because this was a wording-only reconciliation of existing source-backed findings. The parent retains final source and required MCP review; the user retains live-game validation.

## Parent decisions and risks

The parent should keep the current ledger's partial statuses until the owners provide matching native consumer and scenario evidence. The remaining scientist audit proposals need individual acceptance; their presence in a handoff is not approval. If a current asset or prompt still instructs work from the old six-family or five-tab plan, reconcile that specific file against the accepted amendment before assigning implementation. The historical overview list is preserved intentionally and must not be used as a fresh work queue.
