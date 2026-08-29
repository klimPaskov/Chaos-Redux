# Foreign Relief Donor Reachability Handoff

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

Date: 2026-08-24

Owner: `chaosx_scripted_system_architect`.

Status: implementation tranche applied for parent review. This handoff is not a final famine/migration completion claim.

## Exact files changed

- `common/script_constants/famine_migration_relief_constants.txt`
- `common/scripted_triggers/famine_migration_relief_triggers.txt`
- `common/scripted_effects/famine_migration_relief_effects.txt`
- `common/scripted_effects/famine_migration_relief_effects.md`
- `common/scripted_effects/chaosx_famine_migration_effects.txt` at the single producer `famine_migration_retire_recovered_state`
- `common/decisions/famine_migration_decisions.txt` only in `fm_emergency_imports`, `fm_escorted_relief_convoy`, `fm_emergency_airlift`, and `fm_invite_relief`
- `localisation/english/famine_migration_l_english.yml` only at `fm_invite_relief_desc`

No commit was made. No other decision, mission, phase/density gate, event, GUI, mapmode, on-action, workbook, asset, or configuration file was edited by this tranche.

## Identifier disposition

New constants are `famine_migration_relief_endpoint.minimum_naval_base_level`, `.minimum_air_base_level`, and the eight `famine_migration_relief_logistics.minimum_*` floors. Existing pool id `famine_migration_relief_pool.prob_relief_donor` remains the declared weighted pool.

New trigger contracts are `famine_migration_relief_donor_candidate_route_is_valid`, `famine_migration_relief_donor_selection_relation_is_valid`, and `famine_migration_relief_action_route_inputs_are_valid`. Existing candidate, contract, delivery, and cleanup predicates were tightened to use these contracts.

The existing effect names remain stable. `famine_migration_relief_register_donor_state` now persists endpoint capability only from live undamaged base facts; `famine_migration_relief_create_contract` writes `famine_migration_relief_action_route_proven` only after exact route, relation, endpoint, blockade, stock/capacity, and action-logistics validation. The active contract still stores exact donor state/country, actor, mode, amount, date, and generation.

## Producer census before and after

Before: one producer registered recovered states, `famine_migration_retire_recovered_state`, with positive owner-created reserve stock and land route input. No producer initialized relief stock; no producer supplied sea/air endpoint or route proof.

After: still one producer. It supplies sea endpoint input only for a positive, undamaged naval base and air endpoint input only for a positive, undamaged air base. The registration helper independently checks those facts, so a spoofed input cannot create endpoint capability. No producer supplies sea or air route proof. No helper writes initial reserve amount or promotes zero stock.

## Reachability proof

Land: `fm_invite_relief` is land-only and is visible/available/targetable only when `famine_migration_relief_has_land_candidate` finds a registered positive-stock donor with owner-proven land capability, relation/tie or exact wartime-corridor legality, recipient headroom, and the land logistics floor. `fm_emergency_imports` can use that persisted land contract or create the same exact land contract before cost. The prior unsupported STATE-scope `is_neighbor_of` trigger was removed; land uses the explicit owner-proven land capability instead of pretending the unsupported trigger is valid.

Sea: `famine_migration_relief_has_sea_candidate` requires recipient blockade proof, live undamaged recipient naval endpoint, exact registered donor stock and live undamaged donor naval endpoint, relation/tie or wartime-corridor legality, and convoy/escort/fuel floors. After selection, the action-owned route pending marker revalidates the exact donor and recipient and writes `famine_migration_relief_action_route_proven` only when the actor still has the sea logistics. There is no generic sea path or donor-wide sea route variable.

Air: `famine_migration_relief_has_air_candidate` is the corresponding blockade, undamaged air-endpoint, stock, relation, transport-plane, air-XP, and fuel gate. Contract creation writes the same recipient-local action proof only after exact donor binding and the air logistics gate. There is no generic air path or donor-wide air route variable.

Delivery revalidates the same exact source, recipient, actor, mode, owner/control, donor stock floor, live endpoint facts, blockade proof for sea/air, relation/tie or wartime corridor, and persisted action proof. Loss of any fact fails closed.

## Contract, cost, and reserve conservation proof

Each of the four decision `complete_effect` blocks sets a fixed mode and request amount, invokes selection/contract creation before charging costs, and charges costs only inside a valid-contract guard. A failed selector or lost action proof therefore charges no cost. Player and AI rows share candidate predicates; AI receives a zero factor when neither a mode-matching contract nor a current candidate exists.

`fm_invite_relief` creates only a land contract and leaves delivery to `fm_emergency_imports`; its delayed `remove_effect` no longer selects sea/air or silently falls back to air. `fm_emergency_imports` stays land-only. `fm_escorted_relief_convoy` and `fm_emergency_airlift` never release recipient local reserves; `fm_release_reserves` remains the local-release owner.

At delivery, `famine_migration_relief_deliver_contract` saves regular event targets and calls `famine_migration_transfer_food_reserves` with positive request, route, and actor proof. The shared primitive measures donor debit and recipient credit, rolls residuals back, and returns `famine_migration_food_reserve_transfer_result`, `...source_debit_output`, and `...destination_credit_output`. The relief helper marks access and recipient corridor proof only for valid result, minimum grant, and exact debit equals credit. It never mutates population, manpower, cohorts, deaths, or pressure directly.

## Cleanup and persistence

`famine_migration_relief_clear_selection` clears stale donor/actor/action-proof fields. `famine_migration_relief_clear_contract` clears active contract, action pending/proof, request, and selection fields while preserving successful corridor history. `famine_migration_relief_cleanup_contract`, `...cleanup_state`, `...unregister_donor_state`, `...clear_corridor_proof`, and `...clear_war_corridor_proof` are repeat-safe. Exact donor scopes persist as recipient-local variables; regular event targets exist only within the delivery chain. No recurring world scan was added.

## Policy, ties, and overrides

Donor selection has a complete declared pool with invalid rows at zero weight. Relation gates accept opinion, alliance, faction, subject, access, or guarantee; a wartime row requires an exact donor-owned recipient/actor/mode corridor proof. Persecution may use the canonical maintained `famine_migration_border_policy = constant:famine_migration_border_policy.humanitarian_open` override. The unproduced `famine_migration_relief_humanitarian_policy_active` flag is no longer consumed. Ideology is bounded preference only; persecution and war-corridor bonuses cannot rescue invalid route, stock, relation, or capacity.

## AI/probability evidence

The installed `hoi4_probability_inspect` route was callable for source discovery. The installed tool list exposed no callable `chaosx_ai_probability_auditor`, so the mandatory auditor evidence pass and same-named baseline/post `prob_relief_donor` comparison are blocked. The source artifact available to the parent is:

```text
hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a5cdd4cab94abac47b886fa7856bd2224857cfa4269ec542bd76ee83ab5ef8e0/02548e937ad4e2e7b4cb21542c9623f8965bdca1aa751fa67e62aec41e5d2925/probability-inspect-be8bf65bfbdf.json
```

The AI parity implemented here is source-level: the four rows use the same candidate predicates in visibility/targeting and zero-factor AI guards. It is not a replacement for the blocked engine probability compare.

## Validation, limitations, and remaining owner wiring

Targeted source inspection covered the reserve API, blockade proof, producer, four decision rows, endpoint trigger/effect docs, offline wiki, and vanilla trigger/effect/script-constant docs. Braces and unsupported comparison operators were checked on touched script files. The localisation file retained its UTF-8 BOM. No live game was launched.

The main engine limitation is that vanilla does not expose arbitrary distant sea-zone or air-path reachability as a trigger. The action-owned exact corridor is therefore intentionally the only truthful sea/air route contract. If an owner cannot provide exact endpoint facts, donor stock, relation/corridor legality, recipient blockade/local inadequacy/no-current-relief proof, and action logistics, the row remains invalid; there is no generic donor, land fallback, or silent path.

Parent owner wiring still includes final review of the four rows, live consumer validation, any required specification/system-doc synchronization, and the unavailable probability-auditor comparison. Preserve the audited phase/density gates and the current primary `cancel_if_not_visible = no` values exactly.
