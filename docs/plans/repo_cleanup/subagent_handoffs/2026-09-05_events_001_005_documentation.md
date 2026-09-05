# Events 001 to 005 documentation reconciliation

Date: 2026-09-05.
Disposition: implemented within this bounded documentation scope.
Current gameplay, balance, asset presentation, and package acceptance remain outside this completion claim.
The [central cleanup record](../documentation_state.md) owns broader status and continuation.

## Ownership and reading

The documentation curator `early_events_docs_c02` fully read the eight originals before editing and supplied a read-only closeout after the parent reclaimed the files.
The parent reviewed the exact source deltas, requested preservation corrections, and integrated the final wording.
This handoff is parent-authored from that confirmed read ledger because the curator closed without saving its reserved handoff.
The curator reported full prerequisite reads of AGENTS.md, the subagent and event skills, required offline wiki and vanilla documentation, the central cleanup record, Event 005 source map, relevant Event 003 and 005 handoffs, and specification entry records.
Those prerequisite reports do not mean every package interior or gameplay file was fully read.

| Original source | Bytes | SHA-256 | Task disposition |
| --- | ---: | --- | --- |
| `docs/events/001_communism_spread/overview.md` | 26299 | `236e7e4de44a2ef5e3600eb726c4148f31bbae216c87627b301dceda975c5e85` | Implemented documentation repair |
| `docs/events/002_zombie_outbreak/overview.md` | 48078 | `0878d056e71b889df19845a66286ebd586af38ed3ab7208add798451f110bb4a` | Implemented documentation repair |
| `docs/events/003_holy_realm/overview.md` | 52679 | `9d4c6e5b55b1af9153a3f93f9f648c65c845be3c84e799c8544eacca54e7360a` | Implemented documentation repair |
| `docs/events/003_holy_realm/systems/buddhahood_progression.md` | 16214 | `f6f5c4a42c4ee03afe7f9284b7a81e21a2a03bff283399657e5532742d39119f` | Implemented documentation repair |
| `docs/events/004_random_war/overview.md` | 7019 | `9fe575a18f62b30a9107dace1adcb0f83418966c1610022a93ef80ec9cd18615` | Fully read and unchanged by this task |
| `docs/events/005_soviet_collapse/overview.md` | 33441 | `7f285cf860077ccd54f93363ad2d4dd3cf802bd0cfcb005628621ecb70a55949` | Implemented documentation repair |
| `docs/events/005_soviet_collapse/patron_rivalry_and_reconsolidation.md` | 4042 | `6a03e4f29cf2a3b36bab891836f79ee86db69fb5c4a24479634bbe55d040de9f` | Implemented documentation repair |
| `docs/events/005_soviet_collapse/successor_relations.md` | 4434 | `34e6ed6a775f9c9673c3529fb051f8d5b21ca2a352da7071093856375c85ea13` | Implemented documentation repair |

The original source bytes and task-specific review candidates are retained in the external continuation02 review directory named by the parent session.
Event 004 was reported concurrently changed during the curator run, but the final parent comparison matched the captured original exactly.
It is excluded from this task's commit.

## Changes and evidence

| Source | Repair and retained facts |
| --- | --- |
| Event 001 overview | Replaced update-history prose with direct descriptions while retaining the former monthly updater, the retired weekly stability and war-support penalties, the generic industry event, and the former generic suppression loop as historical facts. Timing values, state levels, intervention restrictions, and named event identities remain intact. |
| Event 002 overview | Removed update-history filler and corrected the annexation sentence. Preserved the single-outbreak limit, seven-day global cooldown, country-risk flow, controlled-territory checks, and League entry and departure constraints. The reviewed proximity wording does not introduce a new comparison with distant threats. |
| Event 003 overview | Linked the Buddhahood companion without interrupting the variable list. Distinguished missing review archives from runtime asset locations, retaining original archive paths and the curator-verified Git deletion `87d441ac75`. |
| Buddhahood companion | Retained the earlier CC0 statement as historical licensing evidence and attributed track-specific current rights records to the canonical audio catalog. Preserved the CC BY 3.0 attribution requirement and the earlier animation-frame evidence. Marked future proposals unresolved, including the Final Silence audio recommendation that conflicts with the overview's terminal Fallout routing. |
| Event 005 overview | Added companion navigation, identified the deleted `docs/assets/005_soviet_union_collapse/` and generated-handoff archive through `79bb425aa6`, and distinguished the current audio-evidence folder from missing animation review material. Preserved the exact four-cause release classification and other gameplay descriptions. |
| Event 005 overview status | Attributed the 43-tree and 1,760-focus figures and completion assertions to their retained package snapshot. Replaced the immediate 43-tree `hoi4.focus_rewrite` instruction with an unresolved historical recommendation pending owner verification of whether it already ran. The cleanup grants no gameplay rewrite authorization. |
| Patron Rivalry and Successor Relations companions | Added reciprocal overview links and clarified their documented scope without introducing a second system or changing the requirements. |

The parent also corrected the shared-selector source owner and vanilla popup-asset ownership in the already-read miscellaneous-settings record.
Exact source-path and Git evidence is appended to the existing [settings handoff](2026-09-05_settings_chaos_documentation.md).

## Validation and limits

The parent compared the full task delta against the captured originals, retained every fenced code block, and checked that no original event, scenario, or sprite identifier disappeared.
The new relative navigation links resolve to the companion files.
The preservation review caught and corrected lost historical detail, an invented proximity comparison, a weakened closed release-cause list, and ambiguous licensing and animation wording before integration.

No fresh Event 001 to 005 MCP inspection, render, probability comparison, focus rewrite, or live-game validation was performed in this documentation batch.
Runtime claims retained from the package documents are not independently revalidated here.
Missing source archives do not prove that runtime assets are absent, and retained licensing statements do not constitute a fresh rights review.
The Holy Realm Final Silence versus Fallout recommendation and Soviet focus-rewrite status remain unresolved.
No fallback, deletion, design promotion, gameplay change, or production simplification was introduced.

## Continuation

Preserve these reviewed entry documents and consult their linked package authority records before working on implementation.
The remaining package interiors still need bounded full reads and evidence-backed dispositions.
Skills used by the curator: `chaos-redux-subagents` and `chaos-redux-events`.
No skill was created or changed by this batch.

## Commit isolation

The original Event 005 working copy already contained an uncommitted Event 023 custody-bridge section absent from the tracked source.
The task commit excludes that entire inherited section and leaves it in the working tree.
One sentence-punctuation repair inside it therefore also remains uncommitted with its owning work.
No Event 023 implementation or acceptance is attributed to this cleanup.
