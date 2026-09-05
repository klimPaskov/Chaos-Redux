# Shared event-system documentation review

Date: 2026-09-05.
Disposition: implemented bounded documentation review, parent-reviewed.
Acceptance basis: the user's documentation cleanup request and approval to apply full reading separately to bounded batches.
The curator confirmed complete reads of all eleven continuation02 originals and authored ten initial documentation patches before its interrupted assignment closed.
Its late read-only closeout identified those edits and their MCP provenance.
The parent fully read all eleven resulting documents, reviewed the complete original-to-curator diffs, and applied the additional conflict and prose repairs described here.
All eleven documents received an owned change after the combined review.

## Source ledger

Hashes identify the original full-read continuation02 baselines.
The implementation-facing descriptions remain source claims, with current behavior and acceptance limited by the named evidence.

| Document | Documentation disposition | Original SHA-256 |
| --- | --- | --- |
| [crisis_rescue.md](../../../systems/event_system/crisis_rescue.md) | implemented documentation review | `5b15abc263ce9b9e869ca0b01c4cec0687fb8cdf191af5c5fdf533c422c4026d` |
| [dynamic_major_event_weights.md](../../../systems/event_system/dynamic_major_event_weights.md) | implemented documentation review | `494bc0858fff285d13a8f63e113424d099b45aab143555d5bb28b204bd024be3` |
| [event_chaos_levels.md](../../../systems/event_system/event_chaos_levels.md) | implemented documentation review | `7afd1c21b126ae18520e6dfa6ba4b7f92c1449b340b43818e08cf9ba208c1f7e` |
| [event_clusters.md](../../../systems/event_system/event_clusters.md) | implemented documentation review | `4b9a0d1994497f3905ce3812a64a5559fa5ee4b5c1297c02846bc053e4ab0aef` |
| [event_clusters_spec.md](../../../systems/event_system/event_clusters_spec.md) | implemented documentation review | `65c89ed2fc0535d6e288ad79986c83884760285151b434316ecedba690fd9c2c` |
| [events_log_evolutions_and_clusters.md](../../../systems/event_system/events_log_evolutions_and_clusters.md) | implemented documentation review | `8fed1a59ddcb34eb5f96f3a981e57c531fbd88d9bcd4d953430e77a0d1c5f5c1` |
| [events_log_window.md](../../../systems/event_system/events_log_window.md) | implemented documentation review | `3c7aae9aa5e168d3ad2dcc93bf5208b62df9b2c646cf621dd12b168c9b2b8714` |
| [events_log_world_end_scenarios.md](../../../systems/event_system/events_log_world_end_scenarios.md) | implemented documentation review | `a03fcfcb447adeaf39593ff9195ef6ab445011ee62cffbabb8b2ad27a531bd65` |
| [individual_crisis_targeting.md](../../../systems/event_system/individual_crisis_targeting.md) | implemented documentation review | `edd968ba82d1415011c7b04145c1b092fbda32cfe74abe279fda5bbae509dc7d` |
| [README.md](../../../systems/event_system/README.md) | implemented documentation review | `599f236a36af842ac7185b987f72de46c4d1942fe20c7abd0c9a07259fab8cc5` |
| [triggerable_scenarios.md](../../../systems/event_system/triggerable_scenarios.md) | implemented documentation review | `60680d54b0778cd952428ccc2f9f0c61602c90f06d4a31f4fb41feee361b8ab6` |

## Reviewed changes and unresolved decisions

The contract candidate and package index distinguish acceptance claims from implementation descriptions.
The original cluster handoff's recorded user approval is retained, but no missing decision text is invented.
The fixed membership matrix contains 75 rows across 18 fixed clusters, so the spec's two stale 82-row references were corrected to 75.
Logical duplicate slots, values, IDs, tables, and formulas were preserved.

The parent added specific unresolved conflicts beside the affected contracts: Negative Economy level 2 versus level 1, Severe-member floor T3 versus Acid Rain participation from T1, generic minor cluster pacing versus the Acid Rain Major exception, and inconsistent worked-example populations.
These are contradictions between recorded inputs and rules, not newly calculated probabilities or balance decisions.
The original examples remain intact and need reconciliation before scenario-specific probability evaluation.

The world-end catalog's blanket supersession claim was replaced with a historical integration boundary.
Hidden-row visibility and Final Silence retirement still conflict across the retained prompt, registry handoff, world-end catalog, Event Log description, and triggerable scenario record.
No visibility rule, scenario identity, or terminal mapping was chosen through cleanup.
The scenario record also identifies unreconciled SCN-008 publisher counts and separate raw-runtime versus workbook identity claims.

The prose pass removed authored semicolons, with sentence breaks and list punctuation only.
The style-only stage preserved the complete ordered word sequences after case normalization.
Code examples, formulas, numerical values, field names, and tables retain their content.
Package workbook/status and Event 019 audit claims are attributed to their historical records instead of promoted into present completion.

## Path evidence

The source CSV `C:/Users/klimp/Downloads/chaos_redux_clusters_catalog_updated_v2.csv` was absent at its exact recorded location.
The workbook and exported CSV are related catalog surfaces, not verified replacements for that original source.

Git records deletion of `common/scripted_effects/fallout_world_end_effects.txt` in commit `8cea20fda6c51ac49de670fc323dae306e0d1e3f`.
The related `common/scripted_effects/fallout_consolidated_effects.txt` and `events/fallout_world_end_events.txt` exist.
This establishes paths and historical deletion, not a one-to-one replacement or current runtime ownership audit.

The old Event 019 `regional_variants/` archive and both related `regional_full_flag_raw/` and `regional_spot_colour_masters/` archive paths were absent when checked.
Their path history remains in the scenario note.
The runtime `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/` directories exist, but their asset contents were not revalidated.
No archive was deleted or moved by this cleanup.

## Returned MCP evidence

The shared-event curator reported `PROBABILITY_SOURCE_INSPECTED` for `common/scripted_effects/chaosx_event_cluster_effects.txt`, with `poolComplete=false`, zero candidates, zero unresolved inputs, and `availableAdapters=[]`.
The exposed adapter name was `custom_weighted_pool`.
Source revision: `1d86199a66e9a4a08cd1700a3c48898b408e33865ddb07936e2fead6591a86c9`.
Source hash: `4a7b9de6b059a75ce473dcb5e69cbcbfc95c5cc666106713cc201ac500d21865`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1fabbbfcac38825b8b39d3ef539f39c1d9b49c7b5f891e59f580a9cc32837c0f/fde0dd32884edc99b6b3fba386f6a73cc59bbaefaa0099760e305c8479c17fd5/probability-inspect-4a7b9de6b059.json`.

This is a reported source-discovery result, not candidate evaluation, simulation, sequence analysis, a probability-auditor comparison, or balance acceptance.
The parent reviewed the closeout and retained its exact artifact identity without independently reading the full artifact payload.
The curator's narrow Event 12 inspection and Event Log inspection under `event_log_shared_architecture_baseline` stalled without returned results.
Those stalled probes do not establish that the service is universally unavailable.
Late settings and shared-plan closeouts returned other partial or diagnostic artifacts, recorded in their own handoffs.

## Retained earlier MCP descriptions

The following original descriptions were replaced by dated and attributable evidence pointers in their source pages.
They remain exact historical quotations here, including their earlier success and adapter-limit claims.
No current service-health or visual acceptance is inferred from them.

### event_chaos_levels.md

> The HOI4 MCP event route currently returns partial coverage, and the probability inspector discovers no compatible adapter for the scripted-variable Random Stuff pool.

> The shared GUI routes render successfully without a selected Random Stuff runtime state, so this document does not claim full engine or branch-specific visual evidence.

### event_clusters.md

> The HOI4 MCP event route currently returns partial coverage, and the probability inspector discovers no compatible adapter for the scripted-variable Random Stuff pool.

> The shared Event Log and Settings GUI routes render successfully, but their synthetic scenarios do not inject a selected Random Stuff runtime state; these pages therefore do not claim full engine or branch-specific visual evidence.

### event_clusters_spec.md

> The HOI4 MCP event route currently returns partial coverage, while the probability inspector discovers no compatible adapter for the scripted-variable Random Stuff pool and therefore cannot run evaluate, sweep, simulation, sequence, or comparison passes.

> The shared Event Log and Settings GUI routes inspect and render successfully, but their synthetic scenarios do not inject a selected Random Stuff runtime state, so this documentation does not claim full engine or branch-specific visual evidence.

### events_log_evolutions_and_clusters.md

> The HOI4 MCP event route currently returns partial coverage, and the probability inspector discovers no compatible adapter for the scripted-variable Random Stuff pool.

> The shared Event Log and Settings GUI routes render successfully, but their synthetic scenarios do not inject a selected Random Stuff runtime state, so this document does not claim full engine or branch-specific visual evidence.
> 

### events_log_window.md

> The HOI4 MCP event route currently returns partial coverage, and the probability inspector discovers no compatible adapter for the scripted-variable Random Stuff pool.

> The shared Event Log and Settings GUI routes render successfully, but their synthetic scenarios do not inject a selected Random Stuff runtime state, so this documentation does not claim full engine or branch-specific visual evidence.
> 

## Remaining scope and validation limits

All eleven source documents were fully read by both the curator and parent.
The curator additionally reported required instruction, wiki, vanilla, and named handoff reads.
Only named source checks and returned MCP summaries above support this review.
No gameplay, GUI layout, localisation, workbook, export, binary asset, provider policy, or runtime configuration was changed.
No game was launched.
No design simplification was introduced, and no plan was promoted into an accepted specification.
Current probability, GUI acceptance, missing archive provenance, source-contract exceptions, and identity decisions remain unresolved.
The broader repository documentation remains outside this completed reading set.
Skills used: chaos-redux-subagents and chaos-redux-events, with the previously reviewed GUI ownership guidance.
No skill was created or updated in this eleven-document pass.

## Commit isolation

The reviewed worktree already contained uncommitted catalogue matrices, semantic-ID migration descriptions, and SCN-015/016/018 additions before this assignment.
The cleanup commit preserves the prior Git versions of those unrelated bodies while adding the reviewed evidence boundaries and applicable prose repairs.
Its conflict annotations describe the captured working-tree documents, not a claim that every underlying matrix or scenario body is tracked by this commit.
The 75-row text correction and punctuation inside those inherited uncommitted sections remain in the worktree for integration with their owning content changes.
No inherited gameplay or catalog semantics are folded into this cleanup commit.
The fully read pre-existing untracked individual-crisis targeting document is included as a source record, with its existing fixed-target adapter gap and all numerical values preserved.
