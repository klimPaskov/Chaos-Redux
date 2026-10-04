# Famine and migration agent decisions, 2026-10-04

Disposition: accepted and recorded by the implementing agent under the user's grant of full design authority for the takeover from the stopped Codex thread.
Each entry states the decision and its basis.
No workbook or exported CSV was edited, and no catalog change is pending.

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
