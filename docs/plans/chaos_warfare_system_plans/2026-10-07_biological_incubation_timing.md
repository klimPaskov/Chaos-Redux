# Ordinary biological incubation timing

Disposition: source implementation and bounded timing tests reviewed; native event-queue execution remains unverified.
Acceptance basis: the approved CBRN plan requires reliable native operation outcomes and automatic outbreak progression, with no extra administration or worldwide polling.
The [architecture review](subagent_handoffs/2026-10-07_biological_incubation_timing_review.md) accepts the exact late-construction helper within that contract.

## Behavior and source

`common/scripted_effects/biological_lifecycle_effects.txt` contains the only gameplay change.
`bio_lifecycle_queue_incubation_event_internal` builds the literal event ID and delay after the existing getter has completed and the due day has been recorded.
The guarded scheduler calls this private helper instead of capturing a zero-valued delay before calculation.
The original eligibility check, scheduled flag, single random draw, rounded/clamped delay, due-day assignment, state scope and duplicate guards retain their order.
Every original definition except the two scheduler edits is AST-identical; the getter, constants and event definitions are unchanged.

The complete public/private API contract is in [biowarfare_system.md](../../systems/cbrn_warfare/biological_warfare/biowarfare_system.md#incubation-scheduling-api), with an owner-index entry in `common/scripted_effects/chaosx_dynamic_effects.md`.
No new native callback, persistent variable, target, timer, random distribution, equipment cost, policy, category, player action, icon or periodic world iterator is introduced.
No public event/detail wording changes, so no catalog workbook/export change is part of this repair.

## Meaningful tests

The parent reviewed the source patch and reran `node docs/testing/2026-10-07_biological_incubation_timing_source_tests.js`.
All 20 cases pass, including twelve agent/sample probes that reproduce the original zero-delay event with a future stored due day and a rejected early callback.
The repaired queue uses the actual getter result and the same due-day offset.

| Agent | Minimum sampled roll | Midpoint sampled roll | Near-maximum sampled roll |
| --- | ---: | ---: | ---: |
| Anthrax | 5 days | 8 days | 10 days |
| Plague | 4 days | 6 days | 8 days |
| Tularemia | 5 days | 8 days | 11 days |
| Smallpox | 12 days | 17 days | 21 days |

These are deterministic source fixtures using existing gameplay constants and modeled rounding, not observed engine timing or a sampled probability distribution.
The suite also covers no redraw/requeue/due-date overwrite, absent incubation, early/exact/duplicate activation, the existing weekly tick, and independent agent records in one state.
Detection, modifier and air-contribution hooks are explicit no-op boundaries; native event execution is captured rather than performed.
The [independent handoff](subagent_handoffs/2026-10-07_biological_incubation_timing_source_checks.md), [results](../../testing/2026-10-07_biological_incubation_timing_source_results.json), and exact byte archives under `docs/testing/2026-10-07_biological_incubation_timing/` retain the source identities and fixture limits.
The earlier 150-case caller-storage suite is frozen evidence for its own source revision; this separate timing suite covers the intentional subsequent scheduler change.

## References and MCP

Installed `documentation/effects_documentation.md:4833-4852`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents building and running meta-effect strings; lines 8096-8128 document literal native state-event delays.
Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:4617-4682`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, describes argument replacement during construction.
Its state-event entry at line 3350 lists variable delays but warns of possible bugs.
Vanilla `common/scripted_effects/SOV_scripted_effects.txt:20-29` uses variable days for a country event; that is not proof of state-event variable support.
The repair therefore retains literal state-event construction and moves it to the correct execution boundary.
The neighboring tick scheduler already calculates its meta arguments before construction and has no equivalent ordering defect.

The before-event trace for `cbrn_bio_lifecycle.1` is partial; complete artifact selection coverage has not been read.
Its narrow matching comparison returned `EVENT_REVISION_NOT_CACHED`, including the requested render.
The [installed route review](subagent_handoffs/2026-10-07_mcp_event_comparison_route_review.md) establishes that trace reports cannot supply the required graph baseline; a scan graph was not captured before this edit.
Canonical before-to-after graph/render proof is therefore unavailable from that trace.
The supported archived-source overlay was submitted with the exact before file, current expected hash and reversed direction, without altering the working tree.
That read-only comparison timed out awaiting `tools/call` after 600 seconds and returned no comparison artifact or backend task handle.
The [exact receipt](../../testing/2026-10-07_biological_incubation_timing/reverse_comparison_receipt.json) records this observation; backend completion is unknown and no duplicate retry was launched.
The queue-helper snippet passes command-kind/scope recognition but returns `SCRIPT_CHECK_PARTIAL`, `valid=null`, with the meta argument block unchecked.
References were read directly; the command check is not argument or engine proof.
The [probability audit](subagent_handoffs/2026-10-07_biological_incubation_probability.md) selected the exact getter and source line through `source_lookup` and `probability_inspect(adapter=direct_random)`.
It surfaced no candidate for `set_temp_variable_to_random`, so no artificial pool, numeric distribution or before/after weighted comparison is claimed.
Exact requests, resource identities, source revisions and outcomes are retained in the evidence folders.

## Omissions and acceptance limits

Native queue execution, actual rounding/time of delivery and wider lifecycle effects remain unverified.
Automatic recovery for an already stranded scheduled record is not implemented by this repair and remains queued for the existing bounded lifecycle hooks.
The repair preserves activation's strict due-day guard and adds no retry pulse or inferred receipt to conceal those gaps.
The broader CBRN goal remains incomplete, including other biological callers, chemical integration, native payment/cancellation and separate presentation/balance gates.
No gameplay simplification or substitute mechanic is introduced.
Skills used: events, native raids, subagents and shared Git commit; reusable meta-argument timing guidance is recorded separately by the skill maintainer.
