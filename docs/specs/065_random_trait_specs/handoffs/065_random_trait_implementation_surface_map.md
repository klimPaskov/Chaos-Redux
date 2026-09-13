# Event 065 Implementation Surface Map

## Ownership map

| Surface | Expected path or area | Required change | Primary owner | Validation |
| --- | --- | --- | --- | --- |
| Root event | `events/065_random_trait.txt` | Replace current fanout and option-owned mutation with authoritative executor and human report | Main implementation agent | `hoi4.event_inspect`, render, compare |
| Event constants | `common/script_constants/065_random_trait_constants.txt` | Event ID, Evolution type, weights, Chaos milestones, report statuses, debug limits | Main implementation agent | Source review, constant reference scan |
| Generated constants | Event-owned generated constants file | Pool counts, version, checksum, group totals | Registry generator | Check mode |
| Event effects | `common/scripted_effects/065_random_trait_effects.txt` | World pass, rolls, ledgers, counters, reports, milestones | Main implementation agent | Event inspection and tests |
| Event triggers | `common/scripted_triggers/065_random_trait_triggers.txt` | Registry validity, leader eligibility, stage availability, saturation | Main implementation agent | Trigger inspection |
| Generated pool | Event-owned generated scripted-effects file | One canonical runtime branch per source trait | Registry generator | Manifest cross-check, probability audit |
| Generated names | Event-owned generated scripted-localisation file | Registry index to localized trait name | Registry generator | Missing branch scan, rendered report |
| Generator | `.tools/generate_random_trait_registry.py` | Parse sources, resolve load order, emit registry and runtime files | Main implementation agent | Unit tests, check mode |
| Classification data | `.tools/data/065_random_trait_featured_overrides.csv` | Reviewed non-stacking featured reasons | Design owner and implementation agent | Stale row check |
| Index history | `.tools/data/065_random_trait_registry_index_history.csv` | Append-only source ID to index history | Registry generator | Migration check |
| Event localisation | `localisation/english/065_random_trait_l_english.yml` | Global report, result states, option, tooltips, fallbacks | Main implementation agent, then localisation auditor | Encoding and render audit |
| Event name mapping | `localisation/english/chaosx_event_names_l_english.yml` | Preserve accepted Event 65 name | Main implementation agent | Key scan |
| Picture GFX | `interface/chaosx_pictures.gfx` | Preserve or repair sprite binding | Main implementation agent | GFX consumer inspection |
| Report image | `gfx/event_pictures/065_random_trait/report_event_leader_trait.dds` | Validate or replace final `210x176` DDS | Asset worker | Metadata, preview, in-game render |
| Asset provenance | Temporary `docs/assets/065_random_trait/`, then permanent docs | Source, processed preview, manifest, review, handoff | Asset worker and main agent | Asset skill checklist |
| Repeatable registration | `common/scripted_effects/chaosx_logic_effects.txt` | Preserve Event 65 repeatable membership | Main implementation agent | Pool initialization inspection |
| Event dispatch | Shared event ID dispatch | Verify Event 65 root remains the single entry point | Main implementation agent | Event compare |
| Event history | Shared event-log effects and selectors | One global row, result status, actor handling | Main implementation agent | Event Log render and source audit |
| Event Details | Shared details effects and localisation | Premise, counts, Evolutions, pool size, cluster | Main implementation agent | Details render |
| Evolution settings | Shared Evolution constants, effects, triggers, UI selectors | Event 65 enabled state, thresholds, history, persistence | Main implementation agent | Boundary tests |
| Randomizations cluster constants | `common/script_constants/event_cluster_constants.txt` | Reserve final ID, tuning, participation | Main implementation agent | Collision scan |
| Randomizations cluster logic | Shared cluster effects and triggers | Cluster registration, member loading, availability, outcome | Main implementation agent | Direct and cluster compare |
| Cluster UI and log | Shared cluster selectors and localisation | Name, details, member severity, result row | Main implementation agent | Cluster render |
| Event docs | `docs/events/065_random_trait/` | Overview, mechanics, registry summary, test notes | Documentation worker | Cross-surface audit |
| System docs | Event-system and cluster docs | Add Event 65 and Randomizations contracts | Documentation worker | Link and mapping check |
| Authoritative workbook | Current Chaos Redux XLSX | Event row and cluster row | Spreadsheet worker | Export diff |
| CSV exports | Catalog exports | Regenerate from XLSX | Spreadsheet worker | Export script |
| Debug hooks | Existing debug pattern | Force stages, pool overrides, counters, cleanup | Main implementation agent | Debug scenario matrix |
| Probability evidence | Event plan handoff area | Exact distributions and comparisons | Probability auditor | Required artifact set |
| Completion evidence | Event plan handoff area | Pass, fail, blocked, needs user review | Completion auditor | Acceptance matrix |

## Narrow subagent scopes

### Repo explorer

Read-only.

Inspect Event 65 and connected shared systems.

Do not edit.

### Scripted-system architect

Read-only planning.

Resolve registry, ledger, dispatcher, report storage, and cluster architecture.

Do not edit gameplay source.

### Asset worker

Write only Event 65 source assets, processed assets, DDS, manifest, and handoff.

Do not edit event logic.

### Probability auditor

Read-only.

Inspect and evaluate actual weighted logic.

Do not choose new balance targets or edit source.

### Localisation auditor

Patch only Event 65 localisation and directly linked scripted localisation after inspection.

Do not change gameplay meaning.

### Documentation and spreadsheet worker

Update permanent documentation and the authoritative workbook after implementation evidence.

Do not implement gameplay.

### Improvement-loop planner

Read-only design review.

Produce an addendum or closure handoff.

Do not implement suggestions.

### Completion auditor

Read-only.

Compare all implementation surfaces with the accepted specification and acceptance matrix.

## Shared-file caution

Event 65 touches several shared files.

The main agent must inspect current consumers before editing:

- event pool registration
- event dispatch
- event log
- Event Details
- Evolution settings
- cluster constants
- cluster member loading
- cluster settings
- cluster localisation selectors
- workbook export scripts

A shared-file edit must preserve unrelated event behavior.

The completion report needs a focused regression list for every shared file changed.
