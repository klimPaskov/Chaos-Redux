# SCN-008 success-only result localisation cleanup — 2026-09-26

**Disposition:** implemented at source level; visible outcome remains success-only. This is a parent follow-up to the 2026-09-25 SCN-008 completion audit, which identified failure-only fallback text in the delayed result event’s scripted localisation. No gameplay effect, event trigger, report timing, release path, or blocked-row ledger content changed.

## Acceptance basis

The user approved the full Event 006 specification. Part 6 and the accepted P0 publication rule require the delayed 80 result to describe a committed scenario; a failed or rolled-back generation publishes no report or ledger. The event trigger in events/006_independence_wave.txt:582-589 requires the committed and result-pending flags and excludes both failure flags.

## Parent source change

In common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt, the summary-outcome helper no longer has a failed-transaction fallback. The event-only GetIndependenceWaveScenarioFailureReason helper was renamed GetIndependenceWaveScenarioCommitStatus and returns only the committed status. localisation/english/006_independence_wave_scenario_l_english.yml now calls that helper, and the unused independence_wave_scenario_summary_outcome_failed key was removed.

Rejection-reason localisation remains because GetIndependenceWaveScenarioLedgerReason uses those keys for blocked candidate rows in a committed scenario ledger. This cleanup does not erase internal allocation diagnostics or alter the committed blocked-row list.

## Validation and limits

- The repository localisation audit parsed 336 files and 72,396 keys. It found zero parse errors, duplicate keys, missing BOMs, missing English headers, encoding artifacts, undefined event roots, missing event title/description keys, and unlocalized requirement flags.
- The same repository-wide audit still reports 262 undefined key bindings and 22,918 dead keys. This narrow SCN-008 cleanup did not classify those totals by event, so it makes no claim that all repository-wide key warnings are resolved.
- Fresh narrow MCP lint/render for chaosx.triggerable_scenarios.80 returned EVENT_INSPECTED_PARTIAL / EVENT_RENDERED_PARTIAL at revision 8a5cedb08380551e7c0198dd1817e7d8d19a1fd88bee7c8afa36e7d87ec082e7, with zero blocking diagnostics, zero skipped sources, zero helper projection, 8,910 unresolved nodes, and 42,824 omitted render nodes. These routes inspect/render the event/on-action projection and do not render the scripted-localisation text; they are structural evidence only.
- No game was launched. No transaction, event order, save/load boundary, or live player-facing result was executed.

Event 006 and SCN-008 remain HOLD / PARTIAL. Current runtime scenario outcomes, helper/lifecycle coverage, and full-cell receipts remain open.
