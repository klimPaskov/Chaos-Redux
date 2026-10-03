# Prospective reception lifecycle plan handoff

Date: 2026-10-03.
Disposition: accepted and queued by the parent for implementation review; implementation remains parent-owned.

## Files changed

- `docs/plans/famine_and_migration_system_plans/prospective_reception_lifecycle_plan_20261003.md` — implementation-ready plan for the existing migration first-host deadlock.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/prospective_reception_lifecycle_plan_20261003.md` — this review handoff.

No gameplay, localisation, GUI, assets, mapmode, event, CXT, workbook, or probability source files were changed.
No commit was created.

## Audited identifiers and behavior

The plan keeps the existing `migration_negotiate_corridor`, `migration_open_reception`, `migration_accept_corridor_offer`, `migration_reject_corridor_offer`, `migration_mission_hold_humanitarian_corridor`, `humanitarian_corridor_prepare_contract`, `humanitarian_corridor_submit_offer`, `humanitarian_corridor_accept_offer`, `humanitarian_corridor_reject_offer`, `humanitarian_corridor_expire`, `humanitarian_corridor_cleanup`, and sparse migration scheduler surfaces.
Its only proposed helper additions are bounded prep/offer predicates, a preparable second pass inside existing neighbor destination selection, and one shared inclusive affordability predicate for the existing open-reception action.

Before, corridor preparation requires positive reception capacity before submitting a host offer, while the dormant host's paid reception action requires an active migration phase and is suppressed during any pending offer.
After the planned change, a validated evacuation request can reach one exact adjacent safe host while capacity is still absent; the host may pay the existing three-resource preparation action or reject; acceptance remains unavailable until current services, policy, hazard, route, cohort, actor, and full amount headroom are all proven.
Pending intent changes no population, cohort destination, service proof, reception load, or capacity.
After host acceptance, the existing sparse spontaneous owner executes the exact corridor transfer for the accepted live row; no manual organized-evacuation click is required for this lane.
Only the existing exact civilian-transfer transaction moves people and credits measured survivors.

The plan preserves the three canonical migration values (Displacement Load, Reception Capacity, and Border Policy), the existing problem-gated migration category, both start-available mapmodes, and the six-action/three-mission surface limits.
The pending response phase uses at most preparation/rejection before readiness and acceptance/rejection after readiness.
No GUI inspection is required because no GUI layout or scripted-GUI behavior is changed.

## Severity-sorted findings

1. Critical: the dormant safe-host first-service deadlock is present and remains unrepaired in source. The source requires capacity to create the offer that would reveal the paid capacity action.
2. High: current `migration_negotiate_corridor` is enemy-front-only even though the corridor contract already recognizes neutral, neighbor, and faction-partner relations; it cannot represent the ordinary spontaneous foreign request.
3. High: spontaneous processing runs under a global-host `ROOT`. Any corridor caller from that registered-state loop must use the saved `migration_spontaneous_origin_owner` for requester identity and relation checks.
4. High: current offer acceptance clears host mirrors outside the successful inner acceptance branch. The parent should acknowledge and clear only the exact matching generation after acceptance, or use terminal cleanup while preserving the source obligation.
5. High: `humanitarian_corridor_front_destination_is_safe` checks only `load < capacity`; the exact incoming cohort amount is not compared with headroom, and `migration_apply_reception_delta` accepts positive credits without a capacity check. The plan adds a narrow request-size headroom gate before acceptance and transfer.
6. High: `migration_open_reception` uses strict `>` thresholds and lacks one inclusive affordability helper shared by `available`, `custom_cost_trigger`, and ready/blocked cost text. Exact nominal funds can fail the cost gate.
7. Medium: the raw offer flag can expose the category without the existing large/repeated/sustained issue threshold. The plan removes that raw reveal and adds `humanitarian_corridor_offer_reveal_is_valid` over the exact current row; a tiny first offer alone remains hidden.
8. Medium: the paired spontaneous-movement Markdown says cohort records are created only after survivor credit, but current source stages a row before transfer and aborts it on failure. The implementation must document the deliberate retained pending-row branch and duplicate prevention.

## Category, cognition, mission, costs, and text

Category lifecycle remains hidden while stable and quiet, emerging only from current `migration_decision_threshold` evidence or a qualifying repeated/large request.
The host increments its existing `migration_incident_count` once when a distinct valid evacuation offer generation is first mirrored, then refreshes the existing phase helper; two separate valid small offers may reveal through the existing incident threshold.
No new counter, event, or pacing surface is created.
The one incoming request adds no public value, meter, mission, or custom window.
The category retains only Displacement Load, Reception Capacity, and Border Policy.

The proposed request phase exposes at most three primary actions and adds no mission.
The existing corridor mission is `migration_mission_hold_humanitarian_corridor`, with `migration_mission_timing.secure_corridor_timeout = 120`, exact finalized-operation success, existing timeout consequences, and the shared maximum of three active missions.
Its duplicate risk remains governed by the existing country flag, exact cohort/generation subject, and mission-slot helper.

`migration_open_reception` has three spendable cost types: 20 political power, 100 support equipment, and 500 fuel.
All three already use icon-first ready/blocked selectors with `£pol_power`, `£support_equipment_text_icon`, and `£GFX_fuel_texticon`.
Factory count, state control, food, route infrastructure, and hazards are requirements, not spendable costs.
The action should require at least one actual service amount or reception-policy change, debit once, refund all three values after any failed paid setup or insufficient full-row headroom, and roll back only receipts created by that click.
No separate free service or capacity grant is recommended.

Existing accept/reject localisation already names the requester, origin, and front, and the open-reception description says preparation alone does not open a route.
Add only the short request-specific target/blocked explanation needed to identify the selected host and confirm that preparation itself moves no people.
The paired spontaneous and corridor helper documentation needs the current staging and retained-request lifecycle recorded.

## AI and probability evidence

No numeric AI weights were changed or selected.
The source-only probability inventory reports these current decision weight families: `migration_decision_ai.negotiate_corridor_*`, `humanitarian_corridor_ai.accept_*`, `humanitarian_corridor_ai.reject_*`, and `migration_decision_ai.open_reception_*`.
The candidate target set changes in the preparable second pass, so implementation still requires an immutable before-source, named baseline, owner patch, and same-scenario `hoi4.probability_compare` through `chaosx_ai_probability_auditor`.

Existing named cases: `prob_corridor_acceptance`, `prob_humanitarian_border`, `prob_capacity_exhausted_border`, `prob_destination_selection_internal`, and `prob_destination_selection_persecution`.
A normal-neighbor/preparation case should be added as an owner-reviewed acceptance fixture before implementation; no unsupported typed scenario fields may be invented.

The baseline auditor's first decision `hoi4.probability_inspect` timed out after 600 seconds; its narrower retry returned `JOB_WORKER_FAILED` / “The isolated worker stopped without publishing a result,” with zero artifacts and no diagnostics.
The separate `custom_weighted_pool` inspection for `migration_destination_selection_effects.txt` also timed out after 600 seconds with no artifact or analysis ID.
Its complete candidate pool cannot be built from the CSV alone because current selection dynamically reads neighboring states, owner/controller, route, food, hazards, border policy, capacity/load, and hosted-cohort history.
No ranking, candidate-completeness result, numeric probability, or comparison artifact exists at handoff.
`probability_evaluate` and `probability_sweep` were skipped because no inspect artifact was returned and the five CSV cases contain narrative setup/ordering text but no schema-confirmed actor/target IDs, exact origin/candidate states, offer ID/deadline, or capacity/history revisions.
`probability_render` was skipped because there is no analysis artifact ID.
`probability_compare` is future owner work after the selector patch; no source changed here.
The narrow live reference and decision-inspect calls initially returned argument-validation errors; corrected requests both timed out after 600 seconds and produced no artifact.
Local offline wiki and installed decision documentation were read directly, so source-only review is not represented as MCP engine evidence.

The probability auditor's source-only score inventory found `migration_negotiate_corridor` bases/factors of 12, 4 (trapped origin), and 2 (democratic government); accept bases/factors of 20, 2 (humanitarian-open policy), 1.5 (democratic), and 0.5 (hostile requester); reject bases/factors of 10, 2 (hostile requester), and 0.5 (humanitarian-open policy); and open-reception bases/factors of 10, 4 (active displacement), 3 (democratic), and 0.2 (war).
These values are source inventory only and do not establish comparative willingness or probability.

Offline reference evidence read directly: installed `common/decisions/_documentation.md` lines 1–48 (SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`), installed `common/decisions/AST.txt` lines 118–128 for the `AST_seize_local_leadership_in_state_major` state-target/`target_array` precedent (SHA-256 `AAD50DA745F5A93C5F7470E06ED990A49A5416C81810849C8A2312600E81F4F2`), and offline `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md` lines 513–608 for targeted and state-targeted decision semantics (SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`).

## Audited source snapshot hashes

| Source | SHA-256 |
| --- | --- |
| `common/decisions/migration_decisions.txt` | `5000DD59578763690E391A22C8F09E7BCC0FC16E8AA063CE068B2D6104BAA0D7` |
| `common/decisions/categories/migration_decision_category.txt` | `43E1EE749E97EF952E9B6CBDD66339346970AC4F308E30CA17E9DA6D4A6BF5FB` |
| `common/scripted_effects/migration_spontaneous_movement_effects.txt` | `154A0E413A16A4A57E5872B86EE81FCE5DF5D169EFCF9FDA3CFACD7FFA648A4B` |
| `common/scripted_triggers/migration_spontaneous_movement_triggers.txt` | `203AB382550841974D83950F2FD841F0299EB75F28C1B811BB4DBC3B6F156CE5` |
| `common/scripted_effects/migration_destination_selection_effects.txt` | `F20084BF1FE1B12A885710B0A3E081E251F3AEFD3505ACA4C65925421CAEB9FF` |
| `common/scripted_triggers/migration_destination_selection_triggers.txt` | `3C4AAC5707EC80279477005E22980723CC5846ABA200228395A16C117B06141D` |
| `common/scripted_effects/humanitarian_corridor_effects.txt` | `7FC7A1C0CFB850830D6EA87CDBD45765AE58A1193B7C86263DC8D3D85EAB8568` |
| `common/scripted_triggers/humanitarian_corridor_triggers.txt` | `624546039563AE3A75F83C0EEFB3B858ECF3E1C3B20215053F6BF0A51684C27C` |
| `common/scripted_effects/migration_capacity_effects.txt` | `62CE76598B5EE2FCD7517613370C52A8899B23347DF289872C44B31DB1AE607B` |
| `common/scripted_triggers/migration_core_triggers.txt` | `00031F2DBCC7549E0D1FD2EBD40613809EB97332D9CD4B8EC68F8266BC7864FE` |
| `common/scripted_effects/migration_decision_phase_effects.txt` | `1EC09B2A4062AA4338CCF7149B26398382DC99E51BED44B24CF04498E440F2D7` |
| `common/scripted_triggers/migration_decision_owner_triggers.txt` | `5CCADBD726127EC7C9083035F2B09B68AEF0BED5BE2461DC08C12849808C0823` |
| `localisation/english/migration_l_english.yml` | `666285358803ED7D387E8C5F44641332D842916DD989562EDB8D7035015F3402` |
| `common/scripted_localisation/humanitarian_cost_scripted_localisation.txt` | `73022A01B7FC1521DE409B97395C628A3373A86B8F687D7AF6C489EC730551D1` |

## Cleanup, route locks, and unresolved items

Use existing sparse callbacks and route generation, not periodic world scans.
Rejection, expiry, stale actor, annexation, host control changes, closed borders, and route loss clear only the matching corridor contract and preserve the real origin cohort/trapped obligation.
Retries reuse the same cohort row but allocate a fresh monotonic route generation; a terminal generation is never reused.
The request-generation mirror must match before cleanup can clear a host's fields.
One pending offer per host remains the capacity limit.

`humanitarian_corridor_operation.relief` is a separate corridor owner surface; this plan authorizes only evacuation requests and explicitly leaves any relief-only category exposure for separate parent cleanup.
No free native shelter/medical proof, inferred route, destination transfer, service amount, capacity term, event/pool/pacing effect, or additional player value is accepted.

Task-specific implementation checks still owed by the parent include full multi-host candidate-pool baseline/compare, origin-owner targeting under the global-host scheduler, no-duplicate live-row staging/reuse/abort, pending offer expiry and generation cleanup, paid setup success/refund, exact capacity headroom, and ordinary internal-first preservation.
User/orchestrator live play remains outside this subagent plan.

## Skills used

Used `chaos-redux-decisions-missions`, `chaos-redux-state-ledgers`, and `chaos-redux-subagents`.
No skill was created or updated.
