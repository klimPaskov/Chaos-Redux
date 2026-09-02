# Event 006 documentation reconciliation — 2026-09-03

Date: `2026-09-03` (Europe/Kyiv).

Owner: `chaosx_documentation_curator`.

Scope: bounded current-authority reconciliation for Event 006 after the DM-03 anchor/local-peace repair and the IW-015 GLC portrait and country-package evidence updates.

Verdict: `DOCS-ONLY / CURRENT AUTHORITY RECONCILED / HOLD-PARTIAL PRESERVED`.

This pass changed no gameplay, localisation, assets, spreadsheets, generated configs, GUI, GFX, country history, central attestation, allocator, or package-admission file, and performed no staging or commit action.

## Files changed

- `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`: the current authority override is dated 2026-09-03, records the source-complete DM-03 helper repair, records the current IW-015 GLC portrait and package handoffs with exact source, flag, binding, GFX, and runtime paths, preserves the 32/29/40/161 boundary, clarifies that live runtime and save/load observation are optional future QA under Part 7, and updates the queued portrait-terminology item.
- `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md`: the current authority override receives the same DM-03 and IW-015 evidence, updates the documented Event MCP date, applies the Part 7 live-runtime wording, and points the queued terminology decision to the 2026-09-03 GLC portrait gate.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_documentation_reconciliation_2026-09-03.md`: this dated reconciliation receipt.

## Source-of-truth decisions

- Accepted Event 006 specifications remain the design authority, including Part 7's rule that source/static evidence controls completion while live or in-game execution, save/load behavior, runtime consumer observation, and player-owned evidence are optional future QA and not completion blockers (`docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_7_ai_balance_assets_and_acceptance.md:758`).
- The source map and resume packet are the current routing summaries, while the dated handoffs remain bounded evidence and do not override the accepted specifications.
- DM-03 is source-complete for its decision surface through `is_independence_wave_register_population_anchor_secure` in `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, with activation and cancellation requiring exact anchor ownership/control and `has_war = no`; the local-peace mapping is intentionally country-level because HOI4 has no native per-state war trigger.
- IW-015 portrait authority is `subagent_handoffs/006_event6_iw015_glc_portrait_gate_2026-09-03.md`, whose verdict is `NO-CHANGE / CURRENT CONSUMER RECONCILED / LIFECYCLE TERMINOLOGY HELD FOR PARENT`; the existing vanilla GLC liberal Castelao consumer, durable source, source-placeholder archive, portrait GFX, and runtime DDS are recorded without relabelling or promotion.
- IW-015 package authority is `subagent_handoffs/006_iw015_glc_country_package_audit_2026-09-02.md`, whose verdict is `NO-CHANGE / FAIL-CLOSED`; the installed binding remains state 171 with `RG-171`, the accepted opening identity remains the vanilla GLC flag family, and no custom Event 006 GLC flag or central admission is implied.
- No allocator count, attestation count, adapter count, reservation group count, deterministic Join order, package promotion, or whole-event disposition changed.

## Plan and handoff disposition

| Evidence or plan | Disposition | Current decision |
| --- | --- | --- |
| `subagent_handoffs/006_event6_dm03_anchor_peace_gate_2026-09-03.md` | `IMPLEMENTED / SOURCE-COMPLETE` | The named helper closes the DM-03 anchor/local-peace source gap without changing admission or counts; the country-level peace limitation remains documented. |
| `subagent_handoffs/006_event6_iw015_glc_portrait_gate_2026-09-03.md` | `NO-CHANGE / CURRENT CONSUMER RECONCILED / LIFECYCLE TERMINOLOGY HELD FOR PARENT` | Castelao remains the existing vanilla GLC leader consumer, and the source-placeholder versus styled-final vocabulary remains unresolved by parent decision. |
| `subagent_handoffs/006_iw015_glc_country_package_audit_2026-09-02.md` | `NO-CHANGE / FAIL-CLOSED` | IW-015 remains adapter-only because independent flag/rights, portrait lifecycle/rights, typed probability, and central attestation/Join evidence are not complete. |
| Older portrait consumer, wiring, and no-additive-roster handoffs | `DATED PROVENANCE / RETAINED` | No older handoff was deleted, merged, or silently rewritten; the latest GLC portrait gate is the package-specific current authority. |

No accepted plan was promoted, rejected, superseded, or newly queued by this documentation pass.

## Open contradictions and blockers

- The 2026-08-30 wiring matrix calls the selected grounded input `source_placeholder`, while the older 2026-08-26 supplied-output audit calls the same physical runtime output `styled_final`; the 2026-09-03 portrait gate preserves both labels and leaves the lifecycle decision to the parent.
- Commons' unknown-author and structured-unknown-date caveats leave independent Castelao rights/date acceptance unresolved despite the period-compatible 1930 source record.
- The package audit accepts the vanilla GLC flag family for opening identity but records no independent opening-flag identity or rights receipt, so the package remains fail-closed.
- The required `chaosx_ai_probability_auditor` route is unavailable in this runtime, so no quantitative IW-015 AI or balance claim is made and no package promotion follows.
- IW-015 is absent from central content attestation and deterministic Join, so its adapter presence and package-local source coverage do not admit it.
- Event MCP evidence remains partial with helper/lifecycle expansion deferred, and no live engine or save/load completion claim is made; those observations are optional future QA under Part 7 rather than current completion blockers.

## Duplicate, superseded, and stale-document audit

- No documentation file was deleted or merged, and older dated history remains available for provenance without being treated as current authority when superseded.
- The older `styled_final` and current `source_placeholder` portrait records are intentionally retained as an explicit contradiction instead of being smoothed into one lifecycle label.
- Targeted searches found no stale prompt filename or instruction requiring a duplicate IW-015 implementation in the source map, resume packet, or the selected current handoffs, so no prompt file was changed.
- Unrelated dated history, accepted specifications, manifests, source packages, and spreadsheet references were left unchanged.

## Markdown hard-wrap audit

No new or changed Markdown hard-wrap issue was found in the reconciled sections or this handoff; each added prose sentence remains on one physical line, and headings, list items, and the disposition table preserve their deliberate structure.

## Validation

- Focused `rg` checks confirm that both current-authority documents reference the 2026-09-03 DM-03 handoff, the 2026-09-03 IW-015 portrait handoff, the 2026-09-02 IW-015 package handoff, the GLC source/GFX/runtime paths, the vanilla flag-family paths, and the unchanged 32/29/40/161 boundary.
- Focused `rg` checks confirm that the stale current-authority phrase `live runtime remain open` and the old queued portrait-terminology wording no longer occur in the reconciled authority sections.
- `git diff --check --` was run against the two reconciled documents, and a targeted whitespace check was run against this new handoff.
- A narrow read-only `hoi4.event_inspect` scan for `chaosx.nr6.1` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6640393d40478234b9a54bafb7d6c2d0a9b7e123747a73984566b96e51a3936/aff51520c4ce3001bd13c68d4ff1b3ccff741918dea889209ed4cc3dbb610a54/event-scan-18bf807c8be3.json`; this remains evidence only and was not promoted into a new source-of-truth claim.
- No gameplay, asset, localisation, spreadsheet, live-game, save/load, or quantitative probability validator was run because this task was restricted to documentation wording and the required probability auditor route is unavailable.

## Parent decisions required

1. Choose the authoritative lifecycle vocabulary for the GLC Castelao consumer and decide whether the current supplied painted DDS can be accepted under the portrait contract.
2. Provide or reject the independent opening-flag identity and rights receipt required by the IW-015 package contract.
3. Run the named IW-015 probability scenarios through `chaosx_ai_probability_auditor` when that route is callable, then obtain the required comparison before any weighted-logic or admission change.
4. Preserve the current fail-closed package and whole-event HOLD/PARTIAL decisions until the static identity, rights, probability, and central-attestation gates are independently cleared; treat live runtime/save-load observation as optional future QA under Part 7.

## Scope result

The documentation set now identifies the completed DM-03 source repair and the latest IW-015 GLC evidence without changing gameplay intent, allocator arithmetic, package admission, or promotion status.
