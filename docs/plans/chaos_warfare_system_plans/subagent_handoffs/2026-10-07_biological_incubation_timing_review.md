# Biological incubation timing architecture review

Date: 2026-10-07.
Disposition: proposed helper accepted for parent implementation within the bounded timing repair.
Acceptance basis: parent supplied the exact faithful fix and requested read-only source review.
Owned change: this handoff only.

## Finding and proposed helper contract

The proposed `bio_lifecycle_queue_incubation_event_internal` is a faithful solution to the current premature meta-argument capture.
The current scheduler initializes `bio_incubation_days` to zero before its outer meta effect.
The outer argument `BIO_INCUBATION_DAYS = "[?bio_incubation_days|.0]"` is evaluated when that effect builds its code, which precedes the getter call inside the built code.
The due-day calculation consequently uses the getter's computed delay, while the scheduled event receives the previously captured zero.
`bio_lifecycle_activate_current_agent` requires current day at least the saved due day and contains no early-callback requeue path.
The early callback can therefore leave the existing incubation-scheduled flag set without a later activation callback.
This is a source/reference inference rather than observed engine execution.

| Contract field | Required behavior |
| --- | --- |
| Helper name | `bio_lifecycle_queue_incubation_event_internal`. |
| Source and scope | `common/scripted_effects/biological_lifecycle_effects.txt`, current exact state. |
| Inputs | Existing caller-owned, unscoped `bio_active_agent` and `bio_incubation_days`, with delay already drawn, rounded and clamped. |
| Outputs | None. |
| Side effect | One state event `cbrn_bio_lifecycle.<agent>` with literal integer `days` built from the computed delay. |
| Call site | Replace only the current `state_event` statement inside `bio_lifecycle_schedule_incubation_for_current_agent` with this helper call. |
| Preserved sequence | Existing guard, set scheduled flag, getter, set due day, add computed days, then queue helper. |
| Removed argument | Only the outer scheduler's premature `BIO_INCUBATION_DAYS` substitution. Keep outer agent substitution for flag and due-day names. |

The new helper should contain only the inner `meta_effect` that builds a static state-event ID and static integer delay at helper execution time.
It must read the computed delay rather than make a fresh random draw or calculate a second due day.
The scheduler already declares all three getter outputs, so its delay survives the returning getter under the existing conservative helper-frame model.
The queue helper has no returned temporary output and needs no new output storage.

## Reuse and acceptance concerns

The existing neutral registry `chaosx_dynamic_effects.txt` has no state-event dispatcher.
Its date-offset helpers calculate calendar values and are not suitable queue replacements.
The neighboring tick scheduler demonstrates the required late capture pattern by computing its ID and delay before its meta effect.
Copy that small local pattern into the owner helper rather than creating a generic event administration layer.

Direct variable `days = bio_incubation_days` is not sufficiently established by the supplied installed state-event documentation and the offline warning.
The proposed literal injection avoids relying on that uncertain field behavior.
The supplied vanilla variable-days precedent is a country event, so it does not prove state-event variable support.

Parent documentation should put the full helper contract in the biological owner document.
The shared `chaosx_dynamic_effects.md` registry overview restricts its declaration contracts to neutral helpers in the matching source file, so the appropriate shared addition is an owner-index link to this biological API rather than treating it as a neutral registry declaration.
No constant, threshold, persistent target, state flag, or tuning-table change is needed.

## Neighboring exact-source checks

`bio_lifecycle_schedule_tick_for_current_agent` computes `bio_tick_event_id`, adds the existing ten-offset, assigns `bio_tick_days`, and rounds it before evaluating its meta arguments.
It does not have the incubation scheduler's capture-order defect.
Its native event IDs correspond to the four existing tick events `.11` through `.14`.

The eight lifecycle event entries explicitly set the agent selector before activation or tick processing.
Their exact-state scopes are retained by the proposed queue helper.
`activate_current_agent` retains its incubating, scheduled, and due-day guards, clears schedule state only after acceptance, then performs detection and tick scheduling.
The cleanup helper clears both schedule flags and due-day fields for the current agent.
There is no basis here to add a retry pulse, loosen early activation, change duplicate guards, or add a persistent callback epoch.

The proposed repair prevents newly scheduled early callbacks but does not itself provide recovery for an already stranded incubation record.
No recovery mechanism is proposed by this review.
Native queue rounding, exact callback time, and engine execution remain unproved.
No other concrete neighboring capture-order defect was found in the two schedulers inspected.
This does not certify the complete delayed lifecycle, protection, mortality, spread, or tick transactions.

## Evidence and limits

Read actual source lines 635-705, 901-932, cleanup schedule references around 2531-2535, and tick acceptance references around 2647-2651.
Read `events/biological_lifecycle_events.txt:15-94` for the four activation and four tick entries.
Read the neutral helper registry overview and relevant date-offset documentation.
No gameplay files, tests, Git index, or commits were changed.
No additional MCP calls were made, as requested by the parent.

Direct local reference reading confirms installed `effects_documentation.md:4833-4852` builds and runs meta-effect strings, and `8096-8128` documents numeric state-event delays.
Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:4617-4682` describes replacing meta arguments when constructing the effect.
The parent owns the full citation revisions, reference evidence, domain inspection, implementation, and independent timing fixture.

| Source snapshot | SHA-256 |
| --- | --- |
| `common/scripted_effects/biological_lifecycle_effects.txt` | `3d611e3424da6f221446810f6f4ad49e4065b1a8c066bcf7bec3989038a5d3cc` |
| `events/biological_lifecycle_events.txt` | `1660b03f645ae77ca378263c9f6ae0caa6eefb68eec334544279c102410155ec` |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | `dd9f1d4144575753fe2de087991f9499b4618384ab36c52cb18f00738a09e131` |

No fallback or gameplay simplification was introduced.
The proposed source timing repair is suitable for parent implementation with the stated contract and independent validation.
