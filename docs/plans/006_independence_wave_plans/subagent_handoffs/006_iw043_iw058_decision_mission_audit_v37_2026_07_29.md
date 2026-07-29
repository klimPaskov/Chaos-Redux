# IW-043 / IW-058 decision and mission audit v37

## Scope and outcome

Audited only the CHU/IW-043 and ASY/IW-058 decision categories, their timed decision lifecycles, target validation, FORM-12/FORM-13/FORM-18 transaction actions, the IW-058 sovereign-autonomy terminal choice, cleanup, AI gates, and decision-cost localisation.

No critical, high, or moderate gameplay defect was found in this bounded surface.

One low-severity localisation defect was corrected: 26 package-specific cost tooltips prefixed their icon-first requirement lists with `Requires`, despite the matching decision custom-cost pattern using the list itself as the requirement display.

No decision-owned scripted GUI is present in either category, so no `hoi4.gui_inspect`, `hoi4.gui_render`, or GUI artifact applies.

## Issues, sorted by severity

### Low — fixed: package custom-cost tooltips included redundant prose prefixes

The 12 IW-043 and 14 IW-058 `*_cost_*_tooltip` keys in `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml` began with `Requires` before an already self-explanatory icon and amount list.

The cost list now starts directly with the first icon and retains every command-power, manpower, equipment, train, convoy, and civilian-factory value.

This was a presentation-only correction; no decision cost, availability check, transaction, AI score, or duration changed.

## Decision-category lifecycle notes

| Surface | Owner and region | Requirement and duration | Success and failure handling | Duplicate-risk control |
|---|---|---|---|---|
| IW-043 local settlement actions | CHU, Middle Volga | Package identity, route, state-control, institution, and stockpile gates; 120-day river actions, 150-day standard actions, and 180-day settlement actions | Paid package transactions commit only after the matching operation validates; timeout and cancellation roll back operation state, release bound force state where applicable, and clear current-action flags | Receipt/current-action flags and operation-specific availability gates prevent a second simultaneous action |
| FORM-12 accession congress | CHU federal route, Middle Volga | Exact carrier, attested FORM-12 surface, invitation and consent ledger, distinct controlled anchors, and 180 days | Begins a paid transaction, finalizes through `independence_wave_iw_formable_finalize_signature_congress`, then either commits carrier-only formation and fires `chaosx.nr006.4313` or rolls back the operation | The failed/invalid path resets the proposal and applies the central 45-day retry cooldown |
| FORM-13 compact congress | CHU restoration route, Middle Volga | Exact carrier, attested FORM-13 surface, invitation and consent ledger, distinct controlled anchors, and 180 days | The same transaction and finalizer contract fires `chaosx.nr006.4314` only after the exact proof succeeds | The failed/invalid path resets the proposal and applies the central 45-day retry cooldown |
| IW-058 local settlement actions | ASY, Mosul and the Mesopotamian corridor | Exact package, Mosul control, community/Church/security prerequisites, stockpile and factory gates; 120-day anchor actions, 150-day institution actions, and 180-day settlement actions | Success paths validate the live scope before applying records; timeouts and cancellation paths clear transaction and force-operation state | Current-action, route, force-binding, and receipt flags prevent duplicate force or record loops |
| Named diaspora and external-guarantee actions | ASY, bounded external target list | Target must exist, be reachable, sovereign, at peace with ASY, and pass the package-specific partner trigger; 150 days | `chaosx.nr006.5805` and `.5807` revalidate the saved normal event target before granting market access or a guarantee | The regional global target is cleared before a valid named partner is saved, and package cleanup clears it again |
| FORM-18 federal congress | ASY, Mesopotamian corridor | Exact carrier, attested FORM-18 surface, negotiated or earned defensive method policy, invitation/consent ledger, distinct anchors, and 180 days | The paid transaction commits only through the shared signature finalizer and then fires `chaosx.nr006.5812`; invalid finalization rolls back and resets the proposal | The 45-day retry cooldown, receipt checks, formable-active gate, and terminal-settlement mutex prevent repeats and cross-route overlap |
| Sovereign autonomy compact | ASY non-guardianship route, Mesopotamia | Valid former host or named regional guarantor, all five settlement records, Mosul control, no client state, and 180 days | The finalizer rechecks the locked counterpart and all treaty records before committing the autonomy mode | A started compact intentionally retains its receipt and closes the competing federal terminal route for the package generation; this is the accepted terminal-choice contract, not an orphaned flag |

The staged FORM-12/FORM-13/FORM-18 integrations use 90-day charter and 120-day defense/revenue actions rather than passive missions, and their carrier/subject gates remove stale surfaces without creating units, subjects, cores, annexations, or state transfers.

## Cost and requirement clarity

- The 26 package-local custom-cost IDs all retain matching base, blocked, and tooltip localisation.
- The two shared standard-cost IDs used by the six staged integration actions resolve from `localisation/english/006_independence_wave_decisions_l_english.yml`.
- Costs are varied by action: command power is combined with manpower, equipment, support equipment, trains, convoys, or a civilian-factory commitment where the operation logically consumes those resources.
- Factory-bound actions use the matching `civilian_factory_use` modifier and availability requirement, including the Diaspora liaison and corridor fortification actions.
- Durations and retry timing read `common/script_constants/006_independence_wave_iw043_iw058_constants.txt`; no task-local duration magic number was introduced.

## AI validity and route-lock notes

- The audited actions use positive AI weights only after their package prerequisites and readiness checks, while default unavailable or unsafe states remain blocked by decision triggers.
- IW-058 target actions use bounded lists plus `is_independence_wave_iw058_diaspora_reach` or the matching external-partner condition, reject subjects and war targets, and revalidate the saved event target in the outcome event.
- `has_independence_wave_iw058_open_terminal_settlement_choice`, `can_finalize_independence_wave_iw058_form18_terminal_settlement`, and `can_finalize_independence_wave_iw058_sovereign_autonomy_terminal_settlement` form a reciprocal route lock.
- FORM-12/FORM-13/FORM-18 continue to require exact active carrier/package identities and cannot use the generic formable family as a substitute.

## Localisation and tooltip notes

- Updated the 26 IW-043/IW-058 package-specific `*_cost_*_tooltip` keys to icon-first strings.
- The localisations still state exactly the resources enforced by their transaction helper or custom cost trigger.
- The IW-043 and IW-058 category descriptions expose the intended live package values and progress context.
- No missing package-local custom cost, custom trigger, or custom effect key was identified during source review.

## Cleanup and exploit-risk notes

- CHU and ASY package cleanup remove their decisions, close the matching formable proposal, clean transaction ledgers, release only package-owned force provenance, and clear package-scoped event targets.
- `independence_wave_cleanup_iw058_assyria` clears the regional settlement-partner global event target, while the named-guarantee event clears it before saving a new eligible partner.
- `independence_wave_write_iw058_host_conflict_survived` clears the reclamation/security crisis flags only after the achievement proof gate passes; the survivor decision establishes that proof before it calls the writer.
- No paid decision creates a free-unit, equipment, core, annexation, subject, state-transfer, or war-goal loop in the audited surface.
- The terminal settlement receipts deliberately enforce exclusivity rather than leaving a recoverable alternate terminal action after commitment.

## Changed files and identifiers

1. `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
   - Updated all `independence_wave_iw043_cost_*_tooltip` and `independence_wave_iw058_cost_*_tooltip` keys.
   - Before: each tooltip began with `Requires` followed by the resource list.
   - After: each tooltip begins directly with the exact resource icon and amount list.

2. `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw043_iw058_decision_mission_audit_v37_2026_07_29.md`
   - Records this audit and narrow localisation fix.

No decision, scripted effect, scripted trigger, event, formable adapter, scripted GUI, or workbook file changed.

## Meaningful validation

- Verified all 28 `custom_cost_text` IDs referenced by the decision file resolve with base, blocked, and tooltip keys across the IW-043/IW-058 package localisation and the shared Independence Wave decision localisation.
- Verified the 26 local package cost tooltips no longer contain the removed `Requires` prefix and that the touched English localisation remains UTF-8 with BOM.
- Re-read all paid congress start, timeout, cancellation, and finalization paths; each uses a receipt/current-action guard and the matching rollback or proposal-reset helper.
- Confirmed both targeted ASY outcome events require a saved target that still exists and is at peace before applying their successful result.
- Confirmed the terminal mutex guards the initial visibility gate and the two reciprocal finalization gates.

## Skipped validation and remaining issues

- No live game execution, save-state simulation, or GUI render was performed; the parent explicitly scoped this audit to static evidence and no decision-owned scripted GUI exists.
- A malformed narrow `hoi4.event_inspect` selector did not yield an MCP artifact, so source review is the evidence for event-target revalidation in this handoff.
- No remaining issue was found inside the requested decision and mission surface.
- Existing broader package admission, asset, portrait, and whole-event runtime-closeout work remains outside this audit scope.

## Plan handoff

No new plan handoff was needed because the only issue was fixed locally and no broad mechanic gap was discovered.
