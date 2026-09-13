# Integration completion continuation

Disposition: implemented bounded source continuation; event MCP evidence remains queued with the parent.
Acceptance basis: parent delegation to finish generic national reform and monthly country attribution within `accepted_implementation.md`.
This continuation supersedes the old handoff's generic selected-site payment description for `generic_dismantle_detention_network` and its description of monthly execution without an event recipient boundary.
No commit was created, as requested.

## Changed files

- `common/scripted_effects/camp_administration_integration_effects.txt`: `camp_admin_generic_reform` marks `camp_rework_reformed_legacy`, clears the obsolete `camp_rework_dismantlement_in_progress` flag and refreshes existing country-specific ideas after finite closure and unregistering.
- `common/scripted_effects/camp_administration_integration_effects.md`: documents the hidden event boundary, generic triggers/quote/cache/effect, snapshot cleanup, tuning and existing reform idea projection.
- This handoff and `integration_finish_validation.json` record the continuation evidence.

Previously present implementation was preserved in the integration triggers, native decision, dispatcher and `events/camp_administration_country_events.txt`.
No constants, targets, localisation, GUI, event, on-action, shared framework or accounting files were changed by this continuation.

## Public API and call sites

All generic reform calls require the actual country as ROOT.
`camp_admin_generic_reform_visible` selects eligible generic countries outside bespoke civil kits with active sites and reform authority.
`camp_admin_generic_reform_available` validates every site's initialization, open status, control and responsibility, incompatible closure activity and inclusive PP affordability.
`camp_admin_generic_reform_quote = yes` computes temporary `camp_admin_reform_quote_pp` from shared command constants without payment.
`camp_admin_generic_reform_refresh_quote = yes` publishes `camp_admin_generic_reform_pp` for the parent's interface refresh.
`camp_admin_generic_reform = yes` owns fresh validation and exactly one political-power debit.
The native `generic_dismantle_detention_network` and public generic dispatcher already call the same effect; the parent owns the GUI action-2 wrapper and getter.
The localisation owner must keep the existing cost/effect keys and native decision wording aligned with national immediate release.
The quote can include quarter PP increments, so integer-only display loses payment precision; this was reported to the parent for the text pass.

The live quote is `clamp(5 + 0.25 * camp_active_site_count, 5, 20) * 3` under current centralized tuning.
Examples are 15.75 PP for one site, 18 for four, and 60 for sixty or more.
There is no manpower debit or equipment purchase at reform authorization.
The existing native `ai_hint_pp_cost = 60` is a fixed engine hint and does not debit another payment.

Reform snapshots the bounded active-state array, records closures, ends the regional campaign before `camp_admin_begin_reform`, captures finite replacement targets before survivor release, and only then unregisters states.
The snapshot is cleared at both ends.
The foundation owns subsequent paid civilian replacement; the active-country retention trigger includes `camp_admin_civilian_states` so removing active sites does not terminate those projects.
This national path removes no buildings and does not invoke the old delayed mission completion effect.
The completed-reform projection removes obsolete generic network ideas and idempotently grants the existing reform idea, whose only factors are stability and political power.
Expansion remains frozen and replay is blocked by `camp_admin_reforming`.

## Monthly actor and mortality evidence

The bounded global dispatcher invokes `camp_admin_integration_monthly_country` once per registered country.
That adapter fires hidden, triggered-only `camp_administration_country.1` in the actual recipient country.
Its immediate effect is the sole call site for `camp_admin_integration_monthly_country_recipient`, which therefore rebases ROOT before legacy registration and country preparation.
The recipient stores its calendar guard before country preparation and all monthly callbacks.
The legacy monthly state entry delegates to the same adapter and contains no percentage-death transaction.
The global pulse contains no old active-state mortality iteration.
No new global recurring hook was introduced.

## Validation and limitations

`integration_finish_validation.json` records thirteen source-contract checks, five independent quote arithmetic examples and hashes of the inspected scripts.
Checks cover the recipient boundary, guard ordering, one bounded monthly driver, retired mortality stream, one validated payment, no manpower/equipment/building authorization cost, regional-close/release/unregister ordering, target capture before finite release, no population creation, native shared gates, inclusive affordability, persistent expansion freeze and snapshot cleanup.
These checks passed; they are source-contract and arithmetic evidence, not HOI4 execution.
The initial source extractor assumed top-level decision indentation and failed to locate the nested decision; it was corrected to accept leading whitespace before the completed checks were recorded.

The prior event-inspect request timed out after 180 seconds without an artifact.
For this continuation, the parent explicitly reserved the MCP service for GUI session 46716 and required event work to wait for a queue slot.
No new event call has been submitted while that reservation is active; hidden-event inspection/render evidence remains parent-coordinated and unresolved.
GUI comparison, localisation review, native decision probability comparison and full twelve-month economy/casualty execution remain with their assigned owners.
No source-only result is presented as equivalent engine evidence.
No gameplay simplification or fallback was introduced by this continuation.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skill was created or updated.
