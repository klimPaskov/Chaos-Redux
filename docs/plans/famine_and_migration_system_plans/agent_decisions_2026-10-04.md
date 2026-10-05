# Famine and migration agent decisions, 2026-10-04

Disposition: accepted and recorded by the implementing agent under the user's grant of full design authority for the takeover from the stopped Codex thread.
Each entry states the decision and its basis.
No workbook or exported CSV was edited; pending catalog changes are listed in `catalog_changes_pending.md`.

## Lead decisions, round 1

1. **Adopt and finish the stopped thread's legacy-cost tranche and reception-intent draft rather than discarding them.**
   Basis: both are parent-accepted designs (`legacy_cost_affordability_parent_acceptance_20261003.md`; the receiver-front plan in `subagent_handoffs/migration_mapmode_reception_lifecycle_20261003.md`), and the game already ran the working tree.
   Result: published in `fa46d0deb` (costs) and `705cd90c4` (intent).
2. **Adopt the three population-loss caller output declarations.**
   Basis: they are correct under the current and the pending shared `apply_exact_state_civilian_population_loss` contract.
   Result: the shared helper owner had already published exactly these hunks in `0cfdf83c2`, so no further commit was needed; the Event 012 Gods hunks and other owners' files stay untouched.
3. **Implement a generic hostile-capture and liberation adapter in `on_state_control_changed`.**
   Basis: ordinary wars otherwise create no refugees or occupation hunger (Parts 3 and 4, integration matrix War and Occupation rows). Flight is state population times a bounded constant share, following the committed `on_nuke_drop` precedent, and famine uses the existing food-observation queue with the occupation-law profile. This overrides the earlier "no population proxy" blocker.
   Result: `3f7d984e6`.
4. **No generic strategic-bombing adapter.**
   Basis: the installed documentation and vanilla on_actions expose no bombing callback, and polling would be a forbidden world scan.
5. **Events 118, 120 and 131 are not created.**
   Basis: they have no source, the catalog already marks them unavailable, and new event design is outside this system.
6. **Event-specific hooks for Events 5, 6, 14, 15, 21, 28, 33, 50 and 95 stay with those owners.**
   Basis: other owners' files are not edited; wars those owners create are covered by the generic capture adapter.
7. **Relief-obstruction condemnation counts the refused corridor's measured transfer people, or the interrupted relief contract's covered population.**
   Result: `e5e7354b2`, refined in `90ea4334c`.
8. **Integration is one whole-cohort settlement.**
   It debits once, writes the row as completed with zero people and credits integration only afterwards, with no partial integration and no new status.
   Result: `c3de4fd62`.
9. **The six dated checkpoint documents are not reconciled as pure documentation.**
   The permanent `docs/systems` pages and the API Markdown pairs were updated together with each source change instead.
10. **HOI4 MCP use stays narrow.**
    Only scenario calls with FROM-state bindings, never `refresh=true` and never repository-wide queries.

## Implementation decisions

### Legacy decision costs (`fa46d0deb`)

- **Readable requirements.** Each visible `available` requirement that relies on a hidden scripted trigger is wrapped in one `custom_trigger_tooltip` with plain text: one target key per action, one key per policy or mission success condition, and four shared migration keys (`migration_reception_host_tt`, `migration_reception_load_tt`, `migration_reception_state_host_tt`, `migration_free_mission_slot_tt`). Basis: the acceptance requires readable requirements; per-action grouping keeps the tooltip short while hiding private receipt flags.
- **Duplicate cost checks removed from `available`.** The bare train, aircraft and air-experience component checks repeated the hidden full-bundle check and rendered nothing; the custom cost line already shows each resource in red or yellow. The airlift aircraft tooltip now reads the central quote instead of a fixed number.
- **Receipt fallback on removal.** All 20 delayed actions now consume their own paid flag, payer and (for relief) contract generation and donor when the receipt guard fails because the state became invalid or uncontrolled, and cancellation clears the relief metadata too. Basis: otherwise a stale receipt blocked later activation of the same action on that state.
- **Relief work-guard fix.** The saved donor was compared from inside the donor's scope against a variable stored on the famine state, so the guard could never pass and paid relief never delivered. It now reads `var:PREV.famine_relief_donor_state`.
- **Unused tuning removed.** The 54 unused `@..._NEG` and resource macros and the whole `famine_relief_logistics` category were deleted; `@FAMINE_PP_*`, `@MIGRATION_PP_*` stay for `ai_hint_pp_cost`, and `@MIGRATION_SUPPORT_LIGHT` stays for the workers' non-spend requirement.

### Receiver-front reception intent (`705cd90c4`)

- **Front control change prunes its own rows.** A front that changes hands drops the rows of any receiver that no longer owns and controls it, walking only that state's rows. Basis: country mirrors hold one slot, so an older agreed corridor could otherwise leave a stale row until its own terminal.
- **Plain legend.** The map-mode description says that our receiving states show a requested, funded or agreed reception before anyone arrives.

### Integration settlement (`c3de4fd62`)

- The settlement lives in a new `migration_integration_effects.txt` with its own Markdown, and the `migration_request_integration` adapter now routes through it so the bare national-credit helper is never an integration path.
- The integrating country must own and control the host state, because the debited national reception ledger belongs to the owner.
- The decision gains a plain effect tooltip, and the fee stays paid upfront as accepted.

### Hostile capture adapter (`3f7d984e6`)

- Hostile means the new controller is at war with the owner and is not the owner, a faction partner, the owner's overlord or its subject.
- Tuning (`humanitarian_capture_pressure`): base share 0.03 of live population; multiplier clamped to 0.5-2.0 from a neutral 1.0; shared ruling ideology -0.40 only without harsh conduct; fascist or communist occupier of a different ideology +0.40; protective occupation -0.30, extraction or forced labour +0.40, collective punishment, population transfer or exterminatory +0.80; protected origin share 0.20; minimum request 1000 people; minimum state size 100k; per-state cooldown 30 days. Basis: the spec's rule that actual conduct outweighs abstract ideology, the 0.05 nuclear-strike precedent for a harsher shock, and the spontaneous-movement floor and minimum.
- The request uses the existing `war` pressure source, which the map mode and reports already label, so no new text is needed.

### Relief-obstruction condemnation (`e5e7354b2`, `90ea4334c`)

- Corridor rejection condemns the receiving country; a response-deadline expiry condemns it only when the deadline passed while the origin, counterpart and offered route were otherwise still acceptable.
- A relief contract counts as interrupted when the donor state is now held by a country at war with the relief actor; that capturing country is condemned at delivery failure and when a paid relief decision finds its contract no longer current.
- Covered population is the famine state's live population scaled by the contract amount against the reserve import it was sized for, capped at the whole population.

## Probability evidence for the changed eligibility surfaces

- `hoi4_decision_inspect`, mode `inspect`, decision `famine_release_reserves`, named scenarios `cost_stock_exact`, `cost_stock_one_short` and `cost_stock_late_deficit`, actor GER, FROM bound to state 64 with famine flags and variables: `DECISION_ANALYZED_PARTIAL`, source revision `a17cb9a45faa0e7aae7454702a08db770c6814cf903a13fd5cd79c254bb93b2b`, report hash `3714aebd709d517cf7dce368622a4deb5a8c3d0b2c645bbafc5338a2bf2b2015`.
  All three scenarios return eligibility false with the same six unresolved inputs (`scope_exists`, `state_population_k`, `OWNER`, `CONTROLLER`, `is_controlled_by`, `has_war`), and the cost reads `DECISION_COST_UNRESOLVED` because the custom payment sits behind the activation guard. The route therefore cannot separate the three cost cases.
- An earlier `famine_emergency_airlift` inspect on the same route returned the same partial code with `scope.has_equipment` among 95 unresolved inputs.
- `hoi4_probability_inspect` with adapter `decision_ai_will_do` and a path source returned `INTERNAL_ERROR` with no artifact; without a source it was rejected as invalid arguments.
- `hoi4_probability_compare` with snapshot-path before and path after selectors was rejected as invalid arguments; the live schema does not expose the selector or scenario-set shape.
- Recorded blocker: the same-scenario before and after comparison against `validation_baselines/legacy_cost_affordability_20261003/` cannot run on the exposed routes. No numeric AI weight changed, and no finding required one.

## Remaining work and live-game checks

- needs_live_game: decision tooltips and cost colours, paid receipts and the five refunds, intent colours and hover text, integration settlement, capture flight and food assessment, and the two condemnation seams.
- The mandatory numeric probability comparison stays blocked on the MCP routes above.
- Event-owner-specific hooks remain with their owners (decision 6).

## Round-1 review decisions

Disposition: accepted and implemented by the round-1 reviewer under the same grant of design authority.

11. **Local integration is offered only where the settlement can run.**
    The decision targeted any controlled state and checked only that both reception loads were positive, while the settlement debits the owner's state and national ledgers and requires the integrating country to own and control the host and both ledgers to cover the whole hosted group.
    A hosted group in an occupied state, or a ledger that did not cover the group, therefore took the fee and settled nothing.
    The new `migration_local_integration_host_can_settle` trigger carries the settlement's own ledger conditions into `visible`, `available`, `target_trigger` and the start preflight.
12. **Corridor refusal condemns only a receiver that could have accepted.**
    Rejection and an unanswered lapse were condemned even when the receiver's front was unsafe or its reception capacity could not hold the request, so a receiver without room was condemned whichever way it answered.
    The specification asks for a proven, deliberate obstruction, so `famine_condemn_corridor_obstruction` also requires `humanitarian_corridor_full_request_headroom_is_valid`; a stale capacity revision fails closed and condemns nothing.
13. **Plainer intent and integration text.**
    The three receiver-front intent lines and the integration effect tooltip were reworded so they say what has and has not happened yet.
14. **Country-wide policy decisions never read a selected state.**
    The cost tranche added `FROM = { is_controlled_by = ROOT }` to the `available` blocks and start preflights of `migration_open_departure_routes`, `migration_restrict_departure` and `migration_controlled_medical_reception`, which have no `state_target`, so `FROM` is not a state there and the three decisions could never be taken.
    The checks were removed from both places; the preflights keep every country condition and the fee bundle, which matches the decisions as they stood before the tranche.
15. **The refusal decision warns about condemnation.**
    `migration_reject_corridor_offer_desc` now says that refusing, or leaving the request unanswered, while the civilians are starving and we have room for all of them is condemned as obstruction of relief, so the consequence from decision 12 is visible before the player chooses.

Probability evidence for decision 14: `hoi4_decision_inspect`, mode `inspect`, decision `migration_open_departure_routes`, scenario `open_departure_country_wide` (actor GER), returned `DECISION_ANALYZED_PARTIAL` at source revision `7465d9e9edb0e09c27c76935fc7c1465c8c2412831d54f03017d1130d73b10d0`, report hash `f220318323df323feb99ab9b6102b5b01f346ff09da173c5b2eaa02bd0757e97`, with the coverage check failing on unbound inputs, so it is not engine evidence. No `ai_will_do` value changed; the change restores eligibility, and the same-scenario numeric comparison stays blocked as recorded above.

## Round-2 decisions

Disposition: accepted and implemented by the round-2 implementing agent under the same grant of design authority.

16. **The cohort visit-history ledger is initialized at runtime start, outside the one-shot guards.**
    `migration_cohort_arrays_are_aligned` includes `migration_cohort_history_arrays_are_aligned`, which needs `global.migration_cohort_history_count`, but only the history writers created it, after a cohort already existed, so no cohort could ever be recorded in a fresh campaign (B040: Ethiopian states 842 and 843 with 42,043 and 27,127 flight pressure moved nobody in four months).
    `migration_initialize_cohort_history` is idempotent, so it is now called after the guarded blocks of `humanitarian_initialize_runtime` and `migration_initialize_runtime`, and again at the top of `migration_record_displaced_cohort`, which covers campaigns where the runtime flags were already set.
    No world-scan repair was added, following lead decision 4; new campaigns are the validation target.
    The aligned branches of the state and country cohort reconcilers now also clear `migration_cohort_registry_misaligned` and `migration_country_cohort_registry_misaligned`, so a state that was flagged while the history count was missing recovers on its next reconcile and its integration, resettlement, return and Camp repression decisions reappear.
    Source trace for the hostile-capture spontaneous path: `migration_process_spontaneous_movement_owner` selects a destination with `migration_destination_selection_history_required` at zero (new flight needs no history), then `migration_record_displaced_cohort` passes `migration_cohort_arrays_are_aligned` (all live and history arrays empty, both counts zero), writes cohort 1, and `migration_record_cohort_history_visit` appends the origin receipt with a valid record result; `civilian_transfer_execute_transaction` then runs with the spontaneous-exodus role, whose history preflight result defaults to valid, and its row check passes the same alignment trigger.
    The two history preflights (`migration_destination_selection_prepare_history_exclusion` and `migration_decision_preflight_destination_history`) still require a positive history count, which is correct because they run only for an already recorded cohort, whose origin receipt makes the count positive.

17. **The food-security score is recalibrated so blockade, occupation, shock and reactivated-profile famines reach their stages (B040 root cause).**
    The old score divided the weighted sum by 7.15, the sum of the weights, so it was a weighted mean: a full blockade topped out near 22 (stable) and catastrophic famine needed every component at 100.
    Accepted changes, all tuning in `famine_core_constants.txt` and `famine_adapter_constants.txt`:
    - `pressure_normalizer` 7.15 to 2.50; weights and stage thresholds unchanged.
    - A first reserve refresh seeds half of the reserve target (`initial_target_share` 0.50) instead of zero; an owner-supplied initial amount or positive saved stock still wins.
    - The reserve is drawn by the stage share of the stored unrelieved shortage (`famine_food_deficit_score`, the sum before relief and exhaustion), now 0.25/0.50/0.75/1.00 of daily need with the old need factor removed, and by at least 0.60 of daily need while the new `famine_blockade_isolation_proof` holds; only a settled stable state replenishes.
    - New reserve-exhaustion term (`famine_apply_reserve_exhaustion`): with a real shortage (deficit at supply strain) or a proven blockade and fewer than 7 reserve days, unmet need rises by up to 55 in proportion to the missing days.
    - The blockade local-supply clause holds with fewer than 7 reserve days alone, or fewer than 14 while production pressure is at least 20; blockade duration pressure caps at 40 and also raises vulnerability; one relief delivery suspends the blockade for 35 days.
    - The committed stage moves one step at a time in both directions; famine and catastrophic recovery windows are 21 and 30 days.
    - Mortality: acute 0.0003 per 14 days, famine 0.0008 per 7 days, catastrophic 0.0020 per 3 days, with the product of the five cause factors capped at 2.5 (`maximum_severity_factor`), so stacked causes no longer multiply a pulse tenfold.
    - Occupation: extraction law pressure 20 to 30; collective-punishment laws use extraction 45 with the forced-labour vulnerability (30) and governance (25) pressures; exterminatory laws use the new extraction pressure 45. Basis: the profile enum orders collective punishment and exterminatory conduct above forced labour, which the old constants inverted.
    - Nuclear strike food share 0.05 to 0.15 of the struck population.
    - The extra stable-stage shock decay applies only while the last score is below supply strain, so an escalating shock is not erased before its candidate window.
    - The Ethiopia profile (271, 842) is a dynamic policy analogue (Part 5): it now needs ETH or ITA ownership or control plus harsher-than-standard occupation or a live food shock, with the 1936-1942 window and the plain state-of-war gate removed. Basis: the Italo-Ethiopian war exists at the 1936 start, and under the new score the old gate would have imposed a famine at game start, which Part 5 forbids.
    - `famine_state_can_retire` keeps a state registered while its stored shortage is at supply strain, so a buffered shortage can drain its stock instead of retiring.
    - The CXT fixture wrote temporary inputs that the surface adapter never read; it now writes three state inputs (`famine_cxt_fixture`) with relief and an empty reserve that settle in supply strain without mortality.
    Scratch model (not committed; a day-by-day Python mirror of `famine_evaluate_food_security` with these constants, 1M population unless stated, 240 days, no relief unless stated):

    | Scenario | Highest stage | First day of each stage | Deaths |
    | --- | --- | --- | --- |
    | Peacetime ordinary state | stable | - | 0 |
    | Island at war, working port, convoys and escorts | stable | - | 0 |
    | Proven island blockade, 6 days of reserve | famine | strain 12, acute 40, famine 89 | 7.2% |
    | Island cut off with the seeded reserve | famine | strain 25, acute 52, famine 101 | 6.3% |
    | Blockade, relief delivery at day 95 | famine, lifted to acute day 116 and strain day 138 | | 1.2% |
    | Blockade, relief delivery at day 50 | acute, lifted to strain day 71 | famine only at 174 after relief lapsed | 2.6% |
    | Blockade with Air Contamination 75 | catastrophic | strain 7, acute 22, famine 49, catastrophic 100 | 33.8% |
    | Dense 3M state, blockade, Air 75, camps | catastrophic | catastrophic 82 | 38.2% |
    | Standard occupation | stable | - | 0 |
    | Extraction occupation | acute | strain 20, acute 63 | 1.5% |
    | Forced-labour occupation | acute | strain 7, acute 29 | 2.4% |
    | Collective-punishment occupation | famine | famine 46 | 10.2% |
    | Exterminatory occupation | famine | famine 45 | 10.2% |
    | Nuclear strike, intensity 1 | acute | strain 7, acute 55 | 1.3% |
    | Thermonuclear strike | acute | acute 22 | 2.4% |
    | Leningrad, Bengal, Henan, Greece, Ethiopia profiles | famine | strain 7, acute 22, famine 44 | 9.8-10.2% |
    | Spain profile | acute | acute 25 | 2.1% |
    | Soviet memory profile with a live shock | acute | acute 54 | 1.8% |
    | Irish memory profile with a live shock | strain | strain 44 | 0 |
    | Bengal profile with sustained relief | acute | acute 28 | 1.4% |

    At the 1936 start no historical anchor passes its gate (Soviet and Irish memory need a live shock, the other windows open in 1939 or later or need harsh occupation, and Ethiopia is gated as above), so all 52 anchors stay stable.
    The protected floor is applied to every pulse; the largest modelled loss leaves 62 percent of the population.
    Probability route: `hoi4_decision_inspect`, mode `inspect`, decision `famine_release_reserves`, scenario `acute_stage_buffered_shortage` (actor GER, FROM state 64 in acute shortage with stored deficit, reserve and flags), returned `DECISION_ANALYZED_PARTIAL` at source revision `59f0014f84e743176e47abedf6db4d80f0be31933b0b96344d62536d44effe49`, report hash `6e922435370a3af160a26c8566430b44af7a6276c77293245b418022ece47d3c`, with the decision-coverage check failing on unbound inputs; this is the existing blocker and not engine evidence.
    Known limits: `famine_local_war_context_proven`, `famine_outbreak_context_proven` and `famine_disaster_context_proven` are read by the collector but no owner sets them, so war, outbreak and disaster context add nothing yet; the wartime-window profiles (Leningrad, Bengal, Greece, Dutch, Java, Vietnam, Henan, Spain) still open on the owner being at war anywhere, so they now reach famine in most campaigns where that owner fights in the window unless relief is used. Tightening those gates to local evidence is recommended as follow-up design work.

18. **The Hunger Lines scenario starts famine and flight in the regions it seizes (B040).**
    Neither `famine_request_scenario_pressure` nor `migration_request_scenario_pressure` had a caller, so a launched SCN-010 produced no food stage, no map colour and no famine decisions.
    Following lead decision 3, a new famine-owned `famine_apply_hunger_lines_scenario_pressure` (`famine_adapter_effects.txt`) reads only Event 014's node registry `global.cannibalism_node_states` and the launch intensity it records in `global.cannibalism_scenario_last_intensity`, and one minimal edit in the shared `trigger_selected_chaosx_scenario` declares `cannibalism_scenario_setup_result` before `trigger_cannibalism_scenario` and calls the adapter only when that result is positive. Event 014's own files and localisation are untouched.
    Per live node state, by intensity (low/medium/high/maximum): a scenario food request of 6/8/10/12 percent of the population, a scenario food context of 14/18/22/26 on production, transport, governance and vulnerability that the surface collector applies until `famine_scenario_food_context_until_date` (120 days), and a migration scenario flight request of 2/3/4/5 percent capped above a 20 percent protected share and skipped below 1,000 people. A state whose context window is still open is skipped, so a relaunch cannot stack pressure; a failed launch sends nothing.
    Basis for the sizing: intensity, not Field Hunger, because Field Hunger is a country meter of the host actors and the four Field Hunger launch values (58 to 86) are too close to spread the stages; the scratch model under decision 17's constants gives low: supply strain day 7 (acute shortage only on day 63 once the reserve is gone), medium: acute shortage day 49, high: acute shortage day 24, maximum: famine day 44, all recovering after the context ends.
    The flight shares sit below and around the hostile-capture base share (0.03) and the nuclear share (0.05), since the scenario's flight is terror and hunger rather than a front passing through.
    The SCN-010 catalog text change is queued in `catalog_changes_pending.md` for the Event 014 owner.
    Also in this change: `famine_cleanup_state_registration` clears the new `famine_food_deficit_score` and `famine_food_exhaustion_need` with the other components.
    needs_live_game: the launch path itself (Event 014 setup result, node registry contents, map-mode colours and the famine category reveal for the affected owners).
