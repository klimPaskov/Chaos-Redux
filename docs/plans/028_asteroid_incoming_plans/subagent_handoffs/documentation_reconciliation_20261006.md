# Event 028 documentation reconciliation, 2026-10-06

Disposition: implemented documentation handoff; full Event 028 implementation and validation remain incomplete.
Acceptance basis: the parent reports the user's explicit G6 authorization to correct weak design and source logic within the existing Event 028 workstream, recorded in `../agent_decisions_2026-10-05.md`.
This curator wrote only this file and made no gameplay, localisation, GUI, asset, workbook, CSV, Git-index, or commit changes.
Other agents' work and historical documents remain untouched.

## Source-of-truth map and dispositions

| Record or surface | Disposition and evidence |
| --- | --- |
| `docs/specs/028_asteroid_incoming_specs/028_asteroid_incoming_spec_index.md` | Source-design navigation, read without promoting unspecified claims into accepted design. Explicit user decisions and scoped parent G6 decisions supply acceptance independently of the spec location. |
| `docs/events/028_asteroid_incoming/overview.md` and `../agent_decisions_2026-10-05.md` | Implemented current-behaviour documentation supported by source commit `17aae2d2b215353fb033ee53a4891e0072d01075`, with native and cross-owner limits retained. The decision record supplements the October 4 record. |
| Delivery, recovery ranking, crater action stages, expiry, national mission guards, ordinary provincial damage, and prose repair | Implemented in `17aae2d2b215353fb033ee53a4891e0072d01075`, under the parent's scoped G6 acceptance. This establishes source delivery, not observed native outcomes. |
| Retained mission scopes | Implemented parent G6 design dispositions: reconnect the pre-impact rail network and saved hub; use Ring 2's 60 percent infrastructure/factory gates; measure surviving affected holdings under current control while retaining anchor/hub control requirements. The broader earlier audit wording is superseded for these specific design claims; no second pressure metric or frozen full-country incident membership is invented. |
| `docs/events/028_asteroid_incoming/assets/material_profiles.md` | Implemented, parent artwork accepted and wired by `820efb3bf2b300e1499d0a1870571589f41be7c1`. All three profile markers have distinct sprites and runtime DDS paths; armour is unchanged. Parent native-size and 4x art review is recorded; native state-window presentation remains unobserved. |
| `docs/events/028_asteroid_incoming/assets/material_profile_source_manifest_20261006.md` and `profile_icons_20261006.md` in this folder | Implemented producer evidence, superseded only for pending parent review, shared fragment-icon assignment, and unwired-consumer statements by `material_profiles.md` and commit `820efb3bf`. The permanent manifest already carries that historical-snapshot notice. Preserve the ignored source workspace `docs/assets/028_asteroid_incoming/profile_icons_20261006/` while the event remains incomplete. |
| `../resume_20261004.md` | Historical resume, superseded for current disabled-default, 24/32/46-of-52 tranche, pending decision promotion, unresolved capital-policy, physics, evolution, recovery, and log-integration claims by current source and permanent records. Its chronology and unrecovered-master evidence remain historical evidence. It is untracked in the observed tree and was not edited. Historical counts are not a current requirement-to-runtime coverage audit. |
| `recovery_audit_20261006.md` | Implemented read-only snapshot, superseded for missing national completion guards and shared profile icons by the two later commits. Its narrower mission-scope objections have explicit parent G6 dispositions above; native lifecycle evidence remains unresolved. |
| `completion_audit_20261006.md` | Implemented read-only snapshot. Its ordinary-province adapter is implemented in later source, replacing its accepted-and-queued status; its railway, supply-network, queue/project, cross-owner, and native evidence limits remain open. |
| `localisation_audit_20261006.md` | Implemented source/text audit; final presentation acceptance unresolved. Its final source-confirmed prose corrections supersede its initial wording recommendations. |
| `probability_audit_20261006.md` | Implemented specialist source audit, blocked for usable MCP analysis/comparison evidence. Preserve its exact named scenarios and `../audit_inputs/probability_baseline_20261006/` snapshots; unchanged score blocks do not prove unchanged availability or balance. |
| `../takeover_status_2026-10-06.md` | Parent-owned current-status destination, pending creation at this curator's path check. The overview already links it; its existence and final contents require parent review. |

## Current contradictions and stale instructions

- `overview.md`, Opening AI, still describes friendly ground through control alone, while its final lifetime paragraph, the finishing decision record, and current source include ownership as well as control. Parent should align that older paragraph with the accepted source predicate.
- `localisation_audit_20261006.md`, Dynamic text and consistency, still calls the confirmation duration hardcoded after Final parent patch status independently confirms dynamic duration. The later confirmed correction controls that disposition.
- `profile_icons_20261006.md` still describes pending parent review/wiring and fragment-icon reuse. Treat it as producer history using the superseding material-profile record rather than reopening completed art production.
- `resume_20261004.md` contains several successive counts and obsolete next-step instructions. Use the current overview, decision record, permanent asset records, and parent status instead of restarting completed tranches; do not erase its chronology.
- The reviewed scope supplies no newly accepted expansion plan or stale named coding prompt requiring a new assignment. No source spec was rewritten or proposal promoted, and no duplicate document was deleted or merged.

## Open gates and validation limits

Complete railway/supply-network demolition and construction/special-project queue purge remain blocked or unproven; ordinary provincial zeroing/cohort damage and rebuilding suppression do not establish those results.
The tracked `common/on_actions/042_equipment_from_heavens_on_actions.txt` still lacks the asteroid visual marker exclusion in the inspected hook; this remains another owner's integration task.
Catalog alignment remains accepted and queued with its owner until final localisation facts are applied to the authoritative workbook and its exports are regenerated.
The probability specialist obtained no usable comparisons or analysis artifacts; scenario inputs and valid adapter-specific before/after comparisons remain unresolved as documented in its handoff.
Parent-reported shared GUI inspection timed out after 600 seconds, and `gui_render` returned `JOB_WORKER_EXIT` without artifacts; required matched presentation proof remains blocked.
The temporary saved `asteroid_incoming_forecast_delivery_count` remains pending the native L1 check and subsequent removal.
Parent read-only save metadata records `qa_001_fresh_head.hoi4`, USA, `1936.1.1.12`, version `v1.19.2.0.a729`; metadata does not establish delivery, damage, or UI behaviour, and no game was launched.

The curator independently called exposed `hoi4.event_inspect` with event `chaosx.nr28.1`, downstream depth 1, six nodes, eight edges, helpers disabled, and no refresh.
It returned `EVENT_INSPECTED_PARTIAL`, source revision `52ca4d64b9bf62ec0730dd697ab2eca271703e78a1de3392c9867fe9d29cc874`, graph hash `57a7ed06b7c4eb980dc522f973b69668bc78875ea134e78e200baaef383ddee4`, and one blocking diagnostic in its summary.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8ad4ae525ae472614d853a5d98ebcfaa4291e5001641fd9479bfa29c11265a8/6991977fddda5ea594ba3f0ceb40fcc3674ec01e624e13b566070bc4cd969fdf/event-trace-52ca4d64b9bf.json`.
The full linked artifact was not retrieved by this curator, so its diagnostic details and complete coverage are not claimed.
The existing completion and localisation handoffs retain earlier partial event renders and the failed event comparison; these do not establish native popup fitting or successful final-source comparison.
Tool exposure was checked separately from this successful partial event response; probability and GUI failures do not establish general service health, and no standalone viewer availability is inferred.

## Patch handoff and parent review

Checks read the two commit inventories and current mission-start guards, ordinary-province adapter, profile sprite assignments, and Event 042 hook against the named documents.
The three national start helpers in `common/scripted_effects/028_asteroid_incoming_recovery_effects.txt` now read `asteroid_incoming_network_reconnected`, `asteroid_incoming_outer_ring_restored`, and `asteroid_incoming_regional_economy_complete`.
The ordinary adapter is `common/scripted_effects/028_asteroid_incoming_province_effects.txt`, with its registered type checks in `common/scripted_triggers/028_asteroid_incoming_province_triggers.txt`.
No accidental mid-sentence hard wraps were identified in the reviewed documentation slices; this new handoff keeps each prose sentence on one physical line and preserves headings, list items, and table rows.
No gameplay tests, binary-asset inspection, workbook reads/exports, GUI retry, or new probability audit were performed within this documentation-only assignment.
Parent should review this ledger, finish the pending status file, correct the two current prose inconsistencies when within its write scope, and retain every open gate in its final report.
No simplification was introduced by this curator; the recorded narrower mission scopes are explicit parent G6 dispositions, and the broader Event 028 goal remains incomplete.
The parent reports using events, decisions-missions, event-assets, super-events, scripted-gui, save-inspection, subagents, shared-git-commit, and ImageGen via the artist during the full pass; no skills were updated.
This curator applied subagents, events, event-assets, and the relevant decision/GUI evidence rules only.
