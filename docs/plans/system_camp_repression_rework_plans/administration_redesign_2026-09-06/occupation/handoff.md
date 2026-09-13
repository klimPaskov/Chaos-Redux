# Occupation module handoff

Disposition: implemented accounting and lifecycle API; historical full-period calibration and MCP evidence blocked.
Acceptance basis: parent task and accepted_implementation.md; parent explicitly accepted source ceilings with present-population-share geographic apportionment, one-time historical seed scans, and external-loss exposure retirement before distinct campaign receipts.

## Owned changes

- `common/script_constants/camp_administration_occupation_constants.txt`: source ceilings, receipt bounds, finite-exposure fraction, deterministic consequence fractions and cause/profile enums.
- `common/scripted_effects/camp_administration_occupation_effects.txt` and paired `.md`: one-time geographic source snapshots, bounded registries, callbacks, exact death adapter, symmetric cause/month/cumulative projections, immutable responsibility, outside-loss reconciliation and release/closure.
- `common/scripted_triggers/camp_administration_occupation_triggers.txt`: geography, regime/chronology/enacted-policy checks, current authority and retention.
- `localisation/english/camp_administration_occupation_l_english.yml`: records labels identifying Jewish victims of Nazi persecution and Chinese civilians under Japanese occupation, plus separate exposure and survivor labels.
- This `occupation/` folder: arithmetic tests, machine-readable results and handoff.

No shared accounting, registry framework, GUI, settings, MCP configuration, technology, probability source or other owner's file was edited.
No commit was made, per parent instruction.

## Parent integration

Integration owner reports `camp_occ_historical_setup` wired once after the existing startup migration; no ROOT country is required.
It reports `camp_occ_on_state_control_changed` wired in the actual changed state scope, and `camp_occ_monthly_country` after foundation processing inside the existing bounded country dispatcher.
Retention uses `camp_occ_country_has_records`, covering both eligible and admitted rows.
`camp_occ_close_country` is available for reform, annexation and special-country terminal cleanup.
These call sites remain integration-owned and require the parent's final diff review.
No event targets are modified by this module.

Foundation and occupation use disjoint reservations: occupation enrollment excludes current detainees; foundation admissions exclude `camp_occ_remaining_k`.
The national country owner confirmed it will apply the same reservation when enrolling historically bounded custody/labor cohorts.
Outside changes can reduce occupation exposure conservatively but cannot produce attributed occupation deaths or a second population debit.

## Validation evidence

`transaction_proof_and_calibration.md` contains the reviewed sequential receipt proof, dated trajectory evidence, divergent paths, and the precise remaining historical acceptance constraint.
The parent-authorized follow-up replaces blanket occupation-law suppression with conservative external-receipt retirement before each separate campaign debit.
Run `python docs/plans/system_camp_repression_rework_plans/administration_redesign_2026-09-06/occupation/test_occupation_accounting.py`.
`accounting_results.json` records 16 source-linked arithmetic scenarios with zero failures and zero errors at the recorded run.
The model checks reduced engine receipts, population/custody floor, unknown outside losses, capture/annexation blame retention, repeated month, release without resurrection, interleaved core/custody/campaign receipts, deaths masked by population growth, fixed-origin partial control, dated Hungarian and China-region trajectories with divergent controls, single physical debit/non-debit projection, and finite million-scale capacity.
This is a source-linked accounting model, not execution of Clausewitz or proof of runtime control flow.
The single population-changing call site was inspected directly against the existing shared API.
The shared receipt is measured from state population; the shared API's precomputed request output is not trusted as actual loss.
Integer-person request rounding is constrained never to exceed the requested cohort slice.

The first capacity test incorrectly assumed the maximum unblocked European scenario was below six million; actual source arithmetic demonstrated approximately 6.376 million.
The test was corrected to distinguish capacity from historical calibration, not to force a preferred historical total.
The source ceilings sum to 9,064,960 people; the 100-million China-region illustrative scenario over 96 months produces approximately 8.242 million incremental deaths before other external causes.
Neither figure is a validated historical campaign total.

Required source references were read: offline Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding and AI modding; installed effects/triggers/script concepts/script-constants documentation; and vanilla GER scripted effects' bounded state-array precedent.
Skills used: events, decisions-missions, state-ledgers and subagents.
No skill was created or modified.

## MCP blockers

`mcp__hoi4_agent_tools__hoi4_event_inspect` request: mode `scan`, selector `{file: "events/chaosx_genocide_events.txt"}`, maxNodes/maxEdges 12, expandHelpers false.
Result: `timed out awaiting tools/call after 180s`; no artifact or engine evidence returned.
`mcp__hoi4_agent_tools__hoi4_map_inspect` request: stateIds `[85,87,88,608,614]`, includeOverview false, queryLimit 5.
Result: `timed out awaiting tools/call after 180s`; no artifact or engine evidence returned.
No standalone GUI/focus surface was designed or edited here.
No weighted/AI/random helper is present: monthly fractions are deterministic arithmetic, so there is no probability adapter or AI balance patch in this module.
Parent event and map evidence remains required; source review is not equivalent to the unavailable MCP evidence.

## Simplifications, omissions and blockers

Historical six-million Holocaust calibration is incomplete.
The state-share mapping uses circa-1933 national source ceilings and in-game European owned-state population shares, not a verified state Jewish population distribution or a migration model.
The selected source entries leave a gap relative to the approximately 9.5-million continental estimate.
Early persecution, all deportation/cross-state movement, additional source-country coverage and exact cause allocation remain outside these implemented rows.
Direct control only is supported; Japanese subject control and foreign collaborator responsibility are not collapsed into Japanese or German authority.
Closed rows cannot be reactivated under a new perpetrator; this preserves finite identity and original blame but omits a subsequent distinct persecution episode.

Generic deprivation remains with shared accounting; the campaign pulse is active in occupied territories after external-loss reconciliation.
The greatest of net population decline, positive territorial death-ledger growth, and current noncustody membership shortfall removes exposure without another debit or attribution.
The measured campaign transaction follows against that residual population, and its state-ledger projection advances the observation baseline so it cannot be reconsumed.
This provides disjoint finite receipts for generic occupation, custody and campaign losses without changing the shared core.
Combined China historical totals still cannot be called calibrated from illustrative affected-population shares and stress-input outside losses alone.
Shared combat, occupation, famine and other losses remain with their owners; no national all-cause total is relabeled as perpetrator responsibility.
Outside population decline removes exposure conservatively and can undercount survivors; it is never credited as a death by this authority.
The 90-percent China-region source share is explicitly model tuning, not an archival statistic.
MCP event/map inspection did not complete, and actual engine execution was not performed.
Parent GUI records wiring and final integration review remain outstanding.

These are reported limits, not completion of the accepted historical coverage requirement.
