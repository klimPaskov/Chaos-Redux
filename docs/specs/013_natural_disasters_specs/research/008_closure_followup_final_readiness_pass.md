# Event 013 Natural Disasters, closure follow-up and final readiness pass

This pass continues from the expanded package closure handoff rather than the superseded continuation prompt. It does not reopen broad design. It records the final planning stance, adds traceability files, and points the next agent toward implementation.

## Decision from the closure handoff

The previous closure file says broad planning expansion can stop. I followed that decision. This pass does not add more disaster families, focus trees, country packages, formables, relief tags, normal-disaster custom GUIs, final localisation, final super-event titles, final quotes, final cultural remarks, or final audio selections.

The useful next step is not more event design. The useful next step is implementation readiness. The package therefore gains a source-of-truth map, a readiness ledger, and a resume prompt for the coding pass.

## What this pass adds

| Added file | Purpose |
| --- | --- |
| `docs_alignment/013_source_of_truth_and_disposition_map.md` | States which files are accepted source design, which files are support material, and which prompts are superseded. |
| `matrices/013_implementation_readiness_ledger.md` | Converts the spec into implementation gates, forbidden simplifications, and evidence requirements. |
| `prompts/natural_disasters_implementation_resume_prompt.md` | Gives the next coding agent a bounded start prompt that begins from closure instead of restarting planning. |
| `research/008_closure_followup_final_readiness_pass.md` | Records this pass and its no-new-design decision. |
| `research/009_third_pass_validation_notes.md` | Records package checks run after adding the readiness files. |

## Rechecked source requirements

| Requirement | Status in package after this pass |
| --- | --- |
| Fresh Event 013 design | Preserved. |
| No old Natural Disasters logic | Preserved as a coding constraint. |
| No old Earth Earthquake logic | Preserved. Event 046 remains placeholder and whole-earth rupture belongs in Event 013 Evolution III. |
| Event 099 handling | Preserved as placeholder or narrow bridge into dust and sandstorm family. |
| Event 051 heat separation | Preserved as a non-stacking requirement. |
| One Event 013 history row per firing | Preserved and elevated into readiness ledger gate. |
| Individually triggerable disaster families | Preserved and elevated into readiness ledger gate. |
| Reliable delayed reports | Preserved and elevated into readiness ledger gate. |
| Reliable aftermath notifications | Preserved and elevated into readiness ledger gate. |
| Significant Deaths-system losses | Preserved and elevated into readiness ledger gate. |
| Baseline, Evolution II, and Evolution III damage scale | Preserved. |
| Direction-only localisation | Preserved. |
| Non-trivial achievements | Preserved. |
| Frame-sheet animation with static fallbacks | Preserved and elevated into readiness ledger gate. |

## Anti-bloat result

No additional broad design surface is recommended. Adding more planning before implementation would likely make Event 013 harder to build and audit. The best follow-up is a coding pass that maps live repo files, checks offline wiki and vanilla precedent, creates reusable helpers, then implements the disaster engine in staged tranches.

## Remaining blockers outside this package

| Blocker | Why it remains |
| --- | --- |
| Live repository inspection | This environment only has uploaded files and package zips. It does not expose the live Chaos Redux repository path. |
| Offline Paradox wiki and vanilla HOI4 files | They are not available in this container, so implementation syntax precedent cannot be checked here. |
| Project subagents | I could not actually spawn the project Codex subagents in this environment. The package contains routing prompts instead. |
| Final assets | Asset generation, sourcing, DDS conversion, manifests, and frame sheets are implementation tasks for asset subagents. |
| Final super-event quote, remark, and audio research | These remain blocked by design until the super-event research workflows verify sources and licenses. |
| Final localisation | The package intentionally provides direction only. Implementation must write and audit final player-facing text. |
| Spreadsheet update | The spreadsheet should be updated only after final in-game wording exists. |

## Recommended next action for implementation

Start with the reusable dynamic disaster call contract. Do not begin by writing individual news events or isolated disaster popups. Once the call contract, target selection, severity model, deaths and building damage paths, delayed report ledger, aftermath category notification, and cleanup lifecycle exist, implement disaster families in groups and audit each tranche against the readiness ledger.
