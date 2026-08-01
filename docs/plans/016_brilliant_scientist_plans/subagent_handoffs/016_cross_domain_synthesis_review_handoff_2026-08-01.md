# Event 016 cross-domain synthesis review handoff

Date: 2026-08-01

## Scope

This tranche adds the explicit host-side review required before the Paleogenetics and Xenobiological Synthesis ledgers can interact. It is ordinary Directorate content, not an evolution, Event Log entry, super-event, new project family, or 3D model package.

## Implemented surfaces

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt` centralizes the 120-day clock, two-civilian-factory burden, Political Power, Support Equipment, Motorized Equipment, fuel, manpower, outcome deltas, AI factors, and the synthesis-program modifier values.
- `common/scripted_triggers/016_brilliant_scientist_synthesis_triggers.txt` requires a live current host, valid primary facility, both prototype receipts, no active project or incident, and the concrete review inventory.
- `common/scripted_effects/016_brilliant_scientist_synthesis_effects.txt` resolves the three guarded outcomes once, records country and Kruger-character receipts, moves all six Directorate state values through the existing helpers, refreshes project pressure/counts/ideas, and applies or removes the persistent controlled-program modifier.
- `common/decisions/016_brilliant_scientist_directorate_synthesis.txt` adds `brilliant_scientist_convene_cross_domain_review` to the existing Directorate category with a real timed decision and cancellation contract.
- `events/016_brilliant_scientist_synthesis_events.txt` adds ordinary report `chaosx.nr16.14` with separate-ledger, authorize, and dismantle choices.
- `common/dynamic_modifiers/016_brilliant_scientist_directorate_modifiers.txt` defines `brilliant_scientist_host_synthesis_program`, which increases special-project speed while consuming facility supply, consumer goods, and detection capacity.
- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` supplies the decision, cost, report, options, and tooltips.
- `common/scripted_effects/016_brilliant_scientist_country_effects.txt` and `common/scripted_effects/016_brilliant_scientist_effects.txt` carry or clear completed, pending, and in-progress receipts through transfer, sovereignty formation, transformed hosts, and former-host reconciliation. A pending review is rescheduled on the new carrier; completed history is not replayed.
- `docs/events/016_brilliant_scientist/overview.md` and `docs/events/016_brilliant_scientist/systems/projects.md` document the player flow, ledger separation, costs, modifier, and persistence contract.

## Runtime contract

The authorize option sets `brilliant_scientist_synthesis_validated` and both ledger receipts and adds the persistent host programme. The preserve and dismantle options set `brilliant_scientist_synthesis_countermeasure_ready`; dismantling never creates a project reward. `brilliant_scientist_cross_domain_review_completed` plus `brilliant_scientist_personal_host_synthesis_review_completed` are the one-time receipts and guard every path.

## Validation performed

Static validation still required before commit: Clausewitz brace balance and unsupported-operator scan for all touched script files, UTF-8 BOM verification for the localisation file, duplicate-key scan, event-ID uniqueness for `chaosx.nr16.14`, and focused `hoi4.event_inspect` lint. No model or final art production was performed.

## Remaining risks

- The host decision and event use the existing generic Directorate dossier and research icon; bespoke cross-domain art is intentionally deferred.
- Quantitative balance and live in-game acceptance remain user-owned and are not claimed here.
- The wider Event 016 spec still has queued country-specific flavour, bespoke project/news/remnant presentation, full Kruger State/content audits, and deferred seven route-specific 3D unit packages.
