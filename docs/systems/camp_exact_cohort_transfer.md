# German exact-cohort transfer order

Acceptance basis: on 2026-09-26 the user chose to keep an explicit paid German transfer choice after camp administration begins, using a verified living occupation cohort instead of the old whole-state-population request.
The decision ID remains `germany_transfer_prisoners_to_experiment_site`, under `genocide_crisis_category`, as one national order.
It is available only under wartime Nazi authority and the required Mengele program, after the accepted 1943-05-30 gate, with a radical administration mandate and a supported, controlled state-88 killing center.
The country selects the first registered controlled occupied state with a preflight-proven living native occupation row belonging to the same original German authority.
The decision displays that current source and revalidates it before movement; enrollment, monthly processing and state-control changes refresh the bounded selection, while closure clears it.
Core-state fallback without such a row is excluded.

The decision and AI use the same country, source, destination and affordability triggers.
The custom cost quotes political power, army experience, support equipment and trains from `genocide_decision_cost` and `camp_rework_equipment_cost` script constants.
The former 10,000-manpower payment was retired because it was a fifth spendable cost and did not represent the living civilian movement receipt; this keeps the order within the decision action budget.
The inline decision cost shows at most three texticons; its hover lists all four costs and a scripted localisation status names the first insufficient resource with the required amount and matching icon.
The `ai_hint_pp_cost` field uses a matching file-scoped static constant because the decision documentation does not support a dynamic token there.
No native automatic `cost` is charged before execution.

On selection, `camp_occ_try_manual_auschwitz_transfer` stages state 88 as a short-lived event target, selects the country's current oldest eligible source and its exact native row, and preflights a one-person request to prove that row is live and aligned.
The selector and execution both require the configured living-row share to yield at least 1,000 whole people; a smaller remnant cannot consume a full transport order or its resources.
It requests at most `manual_auschwitz_living_share` of that living row, rounded down to whole people and bounded by refreshed site capacity, the current destination population-share headroom and the exact transfer limit.
`camp_occ_transfer_to_custody_exact` then measures one physical source debit, one destination credit and a custody bind with the original state, row root and authority.
It rolls back or quarantines a failed transaction; movement itself records no death.
After a valid bind, `camp_occ_apply_killing_arrival_loss` requests a bounded arrival-phase loss against that exact destination row, then records only the measured physical loss at state 88 as a subset of killing-center violence under the original authority.
Disabled or clipped death receipts leave survivors in custody and do not create a deferred loss.
Only a valid positive receipt lets `camp_rework_germany_apply_exact_cohort_transfer` pay the quoted resources, add source evidence, country accountability and report/crisis pressure, and write one institutional history entry.
Later deaths occur in the destination state through the existing custody role and preserve the original authority.
This order does not advance an institutional research program or grant a bonus.

The separate automatic August–September 1944 Łódź route retains its own date and once-only flag.
Both routes debit the same finite occupation membership and bind destination custody, so one person cannot be moved twice.
The manual order does not claim to represent the dated Łódź episode and does not set its historical flag.
The older helper ID remains as a compatibility alias to the exact paid action; its whole-state-population migration request is no longer called.

## UI and assets

The decision reuses `GFX_decision_germany_auschwitz_transfer` in `interface/camp_repression_rework.gfx`; it needs no new icon file or sprite name.
The Administration, Locations and Records window keeps its existing native elements and sprite definitions.
The decision title, description, custom cost, blocked cost, cost tooltip, requirements, source and effect text live in `localisation/english/chaosx_decisions_l_english.yml`.

## Validation and future work

The source-linked occupation scenarios check a partial living-row movement, conservation, no transport death, original responsibility on arrival and later destination deaths, and one success-gated payment path.
They also apply the manual and dated Łódź requests sequentially to the same living row and show that each reduces only the then-current membership without duplicating people.
In a synthetic 100,000-person source row with 20,000 places of destination headroom and arrival losses disabled, five accepted orders fill that headroom; later attempts move nobody and pay nothing. At current constants those five orders cost 175 political power, 25 army experience, 900 support equipment and 90 trains, with no transport death. When losses are enabled, measured arrival deaths may free resident places for later orders; the same one-payment-per-positive-transfer rule applies. This is a capacity and cost sensitivity, not a historical movement count.
They model engine primitives and cannot prove Clausewitz control, physical receipts, rollback or native decision behavior.
The HOI4 MCP probability adapter is score-only for this decision and cannot establish exact AI click probability from an incomplete wider candidate pool.
A dated source-control scenario and route-valid final GUI/decision consumer evidence remain part of the package acceptance work.
Future extensions may add separately sourced occupied origins or a clearer current transfer headroom preview, but must keep row identity, authority and the one-transaction payment contract.
The old state-targeted form could create more than six entries when many occupied sources had live rows; `occupation/manual_transfer_target_density_2026-09-26.md` records the source-level stress case and the user's compact national-order resolution. Native decision rendering still needs acceptance.
