# Event 015 Utopia Manifesto - Final Decisions and Missions Audit

**Date:** 2026-07-18  
**Auditor:** `chaosx_decision_mission_auditor`  
**Verdict:** **PASS - frozen source audit; no decision/mission source patch required.**

This is a fresh source audit of the complete Event 015 decision surface, including
the accepted exact-pair island-lease renewal correction of 2026-07-18. It does
not replace runtime validation; the limits are recorded below.

## Scope and frozen source anchors

Accepted inputs reviewed:

- `docs/specs/015_utopia_manifesto_specs/matrices/decision_mission_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/target_eligibility_matrix.md`
- `docs/specs/015_utopia_manifesto_specs/matrices/ai_strategy_matrix.md`
- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/island_lease_renewal_exact_pair_reservation_fix_2026_07_18.md`
- `docs/plans/015_utopia_manifesto_plans/015_utopia_manifesto_final_improvement_loop_closure_2026-07-18.md`

The following SHA-256 anchors were taken after the audit. Gameplay source was
not edited by this audit.

| File | SHA-256 |
| --- | --- |
| `common/decisions/015_utopia_manifesto_decisions.txt` | `e58b33608294970dc0f383c88c4660f36119800990bd90c5b08b7ec0c5556f28` |
| `common/decisions/015_utopia_manifesto_evolution_consumption_decisions.txt` | `aa8c813015cacbf2b5d588b82c39d3b440ed9e83f0009a6a048f83e5d0f82ed4` |
| `common/decisions/015_utopia_manifesto_prefire_evolution_decisions.txt` | `04c46f18ad0c23f70303d75d0d00bb45afcaaf9ab5d877ba01bfe1e9754e3347` |
| `common/decisions/categories/015_utopia_manifesto_categories.txt` | `feb02d3e2af05804a30d2c6ef4a1ebb647b3ced2dfe96cb6c8afed2e035a91e8` |
| `common/scripted_triggers/015_utopia_manifesto_triggers.txt` | `d84f8357ae4aa1cfb4e92cf11c07ad0f7894de9ae2972fcd2e492cb4250decdc` |
| `common/scripted_effects/015_utopia_manifesto_effects.txt` | `6d226343835f1de50f63a07378b7a84c7d04a91f44691c1643ca804b84b519c4` |
| `common/scripted_effects/015_utopia_manifesto_decision_effects.txt` | `5840256b6c6b33c5b6449d91d4e380f2f3a33da7f46f709d6b67e35f519cfd4c` |
| `common/scripted_effects/015_utopia_manifesto_evolution_consumption_effects.txt` | `9b28aa9d37c81ee2f1dbb2543c61abbd3f60463d9f42b8e13dc9407223be84f5` |
| `common/scripted_effects/015_utopia_manifesto_prefire_evolution_effects.txt` | `1d757540eab0082a09df425578e4208e09cb364832d7b170591ea763d50c60c4` |
| `common/on_actions/015_utopia_manifesto_on_actions.txt` | `73a06f68cc6ba23e61c51ba1c9610ff35586fee129623bea5f53478c09cf4037` |
| `events/015_utopia_manifesto.txt` | `32c7993f1ad23f74fcddedc81f119e367b038bc631b6ae48558360a940ece29f` |
| `common/script_constants/015_utopia_manifesto_decision_constants.txt` | `b54d543548255f116fe73aa055b274b845a4dbc7dba6fa0d8bcd083ea72df1d1` |
| `common/script_constants/015_utopia_manifesto_settlement_constants.txt` | `3080751492e6ac3c1c8983822cd6202d403f24833d242e02065fde3a41baaba4` |
| `common/script_constants/015_utopia_manifesto_evolution_consumption_constants.txt` | `2b883019089ac98ff550232fd9de3156b40a5bda3c170b05b74c9eb83059b6b2` |
| `common/scripted_triggers/015_utopia_manifesto_evolution_consumption_triggers.txt` | `285a2334ac19e694a1950513f3bf962697ffeda4a096ef0d3073bad8cb23fcb3` |
| `common/scripted_triggers/015_utopia_manifesto_evolution_delivery_triggers.txt` | `91229ea8fbcba5596f6c6b2d4affce10377d9a72b787c6a46c11a73d2bceb075` |

## Inventory and category lifecycle

The inventory is exact: **121 decisions and 44 missions**.

- Main decision file: 105 decisions, 40 missions.
- Evolution-consumption file: 15 decisions, 1 mission.
- Prefire-evolution file: 1 decision, 3 missions.

| Category | Decisions | Missions | Lifecycle and route lock result |
| --- | ---: | ---: | --- |
| Ledger | 27 | 13 | Ledger/foundation gate; callings, stores, property, and reserve actions clear their active flags and fail safely when the Ledger ends. |
| District | 10 | 3 | District phase/unlock gate; each map action is exact-state targeted and state-control loss clears Event 015 role/charter/penal runtime. |
| Island | 17 | 4 | District phase plus `choose_the_island`; one project record, exact island state/lessor checks, lease expiry/return/replan cleanup. |
| Necessary Ground | 21 | 7 | Necessary Ground unlock plus live deficit, candidate, target, state, integrity, peaceful ladder, and expiry gates. One active case is isolated by founder-side and target/state reverse arrays. |
| Stewardship | 11 | 4 | Only a valid active case may enter; provision, transport, charter, vote, autonomy, return, integration, and revolt all end or reconcile the case. |
| League | 13 | 5 | League unlock and live-member/partner arrays; invitation, technical, reserve, sponsorship, legitimacy, defense, and expulsion actions remove their pending/objective entries on every terminal path. |
| Defense | 5 | 4 | District/citizen-watch or auxiliary unlock gates; real military growth, guard, training, contract, and demobilization paths cannot create unpaid units. |
| Governance | 12 | 3 | Resolved-route or active-crisis gate; correction/repeal actions cancel if capital/Ledger conditions fail and cannot overlap formation proof. |
| Formation | 5 | 1 | Formation phase and resolved-route gates; proof mission is exclusive, cancellable, and blocks proclamation until its evidence is live. |

All 121 decisions have `visible`, `available`, and `ai_will_do` blocks. All 44
missions have activation, dynamic mission duration, cancellation trigger,
cancellation effect, and timeout effect. Every one of the 44 duration variables
has at least one source writer before activation.

The seven actions without a nominal PP cost are intentional non-reward state
selectors: the six Calling selectors and
`decision_utopia_clear_necessary_ground_target`. They only choose or clear a
current target; they do not grant material, territory, units, claims, or a
repeatable benefit.

## Mission-quality notes

| Family | Owner, category, and region | Requirement and duration | Success / failure / duplicate control |
| --- | --- | --- | --- |
| Ledger and Calling | Founder; national Ledger category | Live Ledger and selected shortage where applicable; dynamic survey/store/calling variables | Success applies bounded Ledger/calling changes; loss of the Ledger or shortage invokes family cleanup. One Calling mission flag and per-family cooldown prevent overlap/farming. |
| District and Penal Works | Founder with one exact owned/controlled core state; District category | Surveyed suitable state, live project obligations; `utopia_manifesto_district_days` | Full build, partial debt, or failure; state-control callback clears the exact project. Penal Works has equipment/manpower/reserve costs, exact-state population-loss accounting, completion/route-change/state-loss teardown. |
| Island | Founder with exact project state or exact lessor; Island category | Variant/ownership/lease validity; island and lease duration variables | Builds stage-wise or expires/returns lease. Primary state, lessor, and renewal reservation arrays prevent duplicate site or lessor use. |
| Necessary Ground | Founder, selected foreign country, and selected state; Necessary Ground category | Current deficit, domestic review, candidate validity, state relevance/integrity; case/term durations | Peaceful agreement, contract, association, lease, escalation, expiry, renunciation, and invalidation all remove wargoal/diplomacy/reverse links. One active case and exact country/state arrays prevent stale target reuse. |
| Stewardship | Founder plus the active case state/target; Stewardship category | Valid case, provision/route/charter proof, then vote or integration gates; `utopia_manifesto_stewardship_days` | Provision, transport, charter, autonomy, return, integration, or revolt. Failure restores/reconciles the exact state and clears temporary modifiers and runtime. |
| League | Founder plus tracked partner/member; League category | Initialized/stable League and exact candidate/member arrays; `utopia_manifesto_league_days` | Technical/reserve/invitation/sponsorship/legitimacy success has explicit response cleanup; cancellation/timeout removes the current pending target and objective flag. |
| Defense and paid growth | Founder; Defense category; auxiliary source is an eligible non-hostile neighbour | Focus/flag and dynamic material affordability; `utopia_manifesto_defense_days` | Unit/template growth is paid and rechecked at completion; the contract checks both formation and transfer obligations, then has demobilization/failure cleanup. No free unit loop. |
| Governance and Formation | Founder; national capital/proof state | Crisis/capital or resolved route/proof conditions; dynamic defense/repeal/formation durations | Capital loss, Ledger loss, crisis, or invalid proof fails safely; completion creates no repeating claim/core reward. |
| Evolution and prefire | Founder; the existing category appropriate to the staged evolution | Active enabled delivery, valid route/case/League/district state, material profile; policy/prefire durations | One active policy obligation; cancellation clears active variable/flag, timeout applies the supported interpretation only. Delivery triggers reject disabled evolutions at execution time. |

## Cost, requirement, tooltip, and AI findings

- Ordinary actions use centralized decision, settlement, Penal Works, or
  evolution constants. Costs are varied between PP, manpower, infantry/support
  equipment, motorized, trains, convoys, army XP, command power, stability,
  reserves, factories/proxies, local support, or map objectives as appropriate.
- Material custom cost triggers match their prepared payment helpers. The
  evolution dispatcher selects the matching material profile before it starts
  its shared obligation mission.
- `mission_utopia_raise_a_citizen_watch`,
  `mission_utopia_form_engineer_companies`, post-formation defense, and the
  auxiliary contract recheck paid military growth before granting their
  template/equipment outcome. A changed stockpile can fail the outcome but
  cannot create a free unit or equipment-farming loop.
- 43 targeted decisions were found. Every one has both `target_root_trigger`
  and `target_trigger`; target arrays are bounded to state, selected-candidate,
  recorded partner/member, lessor, or neighbour scopes.
- 218 player-facing requirement/cost tooltip keys referenced by these decision
  files resolve in Event 015 English localisation. All decision/mission name
  keys resolve. The nine reviewed Event 015 localisation files carry UTF-8 BOM.
- Every decision has an AI weight; 12 route/state AI strategies abort when their
  enable condition ends. Foreign targets are checked for existence, hostility,
  array membership, route/League/case validity, or exact reverse links before
  action.

## Necessary Ground, stewardship, associations, and cleanup

`utopia_manifesto_clear_active_need_case` removes the mission, exact active
wargoal, created diplomacy, country and state reverse links, case variables,
offer flags, and obsolete-review state. The case uses domestic-alternative
review, deficit/integrity/local-support checks, a peaceful-offer ladder, bounded
state-specific war-goal generation, expiry, and a renunciation path.

No Event 015 decision source grants a core or a claim. The only audited case
wargoal is the exact-state Necessary Ground war-goal; it is removed by
`utopia_manifesto_remove_active_case_wargoal` as part of close, expiry,
renunciation, invalidation, settlement, and stewardship terminal handling.

Stewardship tracks provision, transport, charter, vote, autonomy/association,
return, integration, and Assigned Colony separately. It restores/reconciles the
recorded target state on return/revolt where the original method requires it;
the revolt path captures exact target/state scopes before it clears runtime.

Association review events `chaosx.nr15.207` and `.221` are intentionally
target-wide rather than accidentally pair-ambiguous: the host has a single
non-reusable review slot and an association-founder count. A stale open review
is invalidated and cannot apply a withdrawal or continuation to a removed
association. If another live association remains, it receives a fresh schedule.
Association access/guarantee and charter state links retain creator arrays per
founder, so cleanup removes only the Event 015 relation owned by the exact
founder and preserves pre-existing or another founder's relation.

## Exact-pair island lease renewal - PASS

The 2026-07-18 reservation correction is present and internally coherent.

1. `decision_utopia_propose_island_lease_renewal` creates both directions of
   the exact pair: founder `...pending_targets` and lessor
   `...pending_founders`.
2. `utopia_manifesto_has_live_island_lease_renewal_request` and the inverse
   `...response` require the live lease, current lessor identity, both pending
   entries, no invalidation marker, and non-war status.
3. The lessor accepts/counters/refuses in `.213` only when the request is live.
   Each option nevertheless sends `.214` unconditionally.
4. `.214` applies an extension only through the inverse live-response trigger,
   then unconditionally clears the exact answer and reservation. A late human
   response is therefore inert while still releasing the non-reusable slot.
5. Lease return and variant replan invalidate an exact pair before links are
   removed. Invalidation retains the pending pair until the old popup resolves,
   so it cannot be mistaken for a newer lease generation.
6. Terminal runtime teardown snapshots both founder-side lessors and
   lessor-side founders/invalidations, removing both reverse directions.
7. `on_annex`, `.163`, and `.164` include the relevant reverse arrays. Lessor
   annexation, founder annexation, and founder-as-annexer paths therefore send
   the exact cleanup/reconciliation callback before local arrays are cleared.
8. Fresh lease creation clears the old renewal-attempt marker, so a later lease
   can schedule normally after a completed teardown.
9. Two founders sharing one lessor remain isolated by array value and the
   current single recorded lessor ID. Their answers and reservations are
   removed only for the current founder.
10. No numeric generation counter, fallback pair, or recurring world scan was
    introduced.

This is a source-level multiplayer/interleaving verdict. The deliberate
non-reusable reservation preserves correctness between delayed `.213` and
`.214`; it is not a fallback and is released on the stale response path.

## World iteration and on-action finding

There is no `on_daily`, `on_weekly`, or `on_monthly` Event 015 action. The
state-control hook uses the changed state's recorded reverse founder arrays and
delivers `.165` after one hour. The annexation hook snapshots exact founders and
partners before clearing links. The only `every_country` uses are explicit,
one-shot candidate preparation for the configured random-event actor, Necessary
Ground candidates, and League candidates/sponsors; they are not maintenance
on-actions and are gated by an explicit event/decision/phase transition.

## Issue list, sorted by severity

- **P0 / blocker:** none found.
- **P1 / gameplay break:** none found.
- **P2 / lifecycle, AI, cost, or exploit defect:** none found.
- **P3 / player-facing localisation or tooltip gap:** none found.
- **P4 / validation limit:** Event and GUI MCP inspections could not produce
  read-only artifacts because the workspace returned
  `ARTIFACT_STORAGE_LIMIT`. This affects only external artifact evidence, not
  source findings. No GUI patch was attempted.

## Changes and validation

Changed file from this audit only:

- `docs/plans/015_utopia_manifesto_plans/subagent_handoffs/decision_final_audit_2026_07_18.md`

Changed gameplay, mission, scripted-GUI, and localisation identifiers: **none**.

Before/after behaviour: **unchanged**; the audited source hashes above are the
frozen after-audit anchors.

Meaningful checks completed:

- Fresh parser inventory and structural check for 121 decisions / 44 missions.
- Full dynamic-duration writer audit for all 44 missions.
- Targeted-decision audit: 43/43 include root and target validation.
- Cost/tooltip localisation coverage: 218/218 referenced cost/requirement keys
  and 165/165 decision-or-mission name keys present.
- Source trace of Calling hysteresis/mutex; Necessary Ground teardown and
  exact-state wargoal; districts/Penal Works; stewardship; association `.207`
  / `.221`; League; paid military growth; evolutions; formation; on-actions;
  exact-pair lease reservation.
- Read-only MCP attempts: `hoi4.event_inspect` on `chaosx.nr15.213` and
  `hoi4.gui_inspect` on `utopia_manifesto_ledger_container`, both blocked by
  `ARTIFACT_STORAGE_LIMIT` with no artifact or source modification.

Skipped meaningful validation:

- Engine/runtime and multiplayer interleaving execution. Artifact storage
  prevented MCP-rendered evidence, and this subagent does not run an in-game
  session. The exact-pair verdict is consequently source-level, not a claim of
  observed runtime behaviour.

## Simplifications, omissions, and recommended follow-up

No gameplay simplification, fallback, or omission was made by this audit. No
decision source change is recommended from the frozen review. Once artifact
storage is available, a narrow read-only rerun of `.213` / `.214` and
`utopia_manifesto_ledger_container` is the only outstanding confidence step;
it should be recorded against this handoff rather than changing the design.

Skills applied: `chaos-redux-decisions-missions`, `chaos-redux-events`,
`chaos-redux-focus-trees`, and `chaos-redux-subagents`. Required offline Paradox wiki
pages and vanilla decision/on-action/script-constant documentation were
consulted; vanilla `common/decisions/SIA.txt` was used as the targeted-decision
precedent.
