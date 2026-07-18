# Fallout Ash-week orientation engine proof

Status: blocked partial pilot after static review

Date: 2026-07-18

## Scope

This record covers the engine-sensitive surfaces used by the approved dormant Ash-week orientation transaction and events `chaosx.fallout.62` through `chaosx.fallout.84`. It does not claim runtime observation. The user explicitly asked that Hearts of Iron IV not be run.

The orientation package remains outside the 660-event release floor until all 23 event blocks, callers, text, event log entries, event detail entries, AI parity, delayed results, assets, cleanup, and manual review are complete.

## Required references consulted

- Offline wiki pages under `paradox_wiki/` for data structures, triggers, effects, modifiers, localisation, scopes, on actions, event modding, decision modding, idea modding, AI modding, interface modding, and scripted GUI modding
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- Vanilla `events/AAT_Generic_Events.txt`
- Existing Chaos Redux state population and Deaths helpers in `common/scripted_effects/chaosx_dynamic_effects.txt`
- Existing Fallout registry, survival ledger, transition generation, and orientation receipt triggers

## Delayed country events

Official effect documentation defines `country_event` for country scope and documents `days` as the number of days to wait before firing. It also documents optional `random_days`. The orientation route uses fixed delays only. No `random_days` field is permitted.

Vanilla `AAT_Generic_Events.txt` provides fixed delayed country event precedents with one-day and two-day delays. The accepted orientation cadence uses the same event effect surface with delays of 2, 3, 4, 3, and 2 days.

The event identities are fixed and reserved. A search of vanilla, this repository, and the available approved reference mods found no precedent for constructing a `country_event` identity by substituting a variable into the namespace. The implementation therefore must use explicit fixed dispatch to `chaosx.fallout.62` through `chaosx.fallout.84`. A meta-built dynamic event identity is not accepted as proof.

## Persistent state targets

The offline Data structures page documents variables as scope references and the `var:` scope prefix. Existing repository precedents include state pointers such as `resources_found_selected_field` and owner pointers used by Air Winter. The orientation transaction uses the same engine surface.

Each country stores its exact state scope in the country variable `fallout_orientation_state_target`. An optional receiver is stored in `fallout_orientation_receiving_state_target`. These are country-owned pointers, so concurrent delayed transactions cannot overwrite one shared global event target. Root choice, delayed resolution, cleanup, and stale reconciliation address them with `var:` and clear the country variables after terminalization.

The source pointer is derived from `fallout_successor_assignment_capital_state`. It must equal the current assigned capital, remain owned and controlled by the country, pass the committed survival state row, and pass `fallout_successor_assignment_capital_row_is_current`. The optional receiver must be a different owned state. No arbitrary state or one-state-per-country approximation is accepted.

## Population loss and migration

Official effect documentation confirms that `add_manpower` supports state scope and changes local state manpower when used there.

Chaos Redux already owns `apply_exact_state_civilian_population_loss` in `common/scripted_effects/chaosx_dynamic_effects.txt`. The helper rounds the request, protects a specified living-population floor, clamps the request to the available state population, records the exact applied count, and routes logged losses through the Deaths API. Orientation population loss must use this helper on an authenticated bound state.

Country-proportion failures use the frozen post-rewrite country population to calculate the request. That population is derived by traversing `global.fallout_survival_ledger_states` in stable order and summing the country's live state populations. The applied request is then distributed through the same stable state array. Each state keeps one living person, state removal disables duplicate Deaths logging, and the country records the exact applied total through Deaths once. Event text and receipts distinguish requested deaths from applied deaths.

Evacuation uses one frozen source request. The source decrement must equal receiving-state population gain plus exact Deaths. The receiving-capacity clamp applies to the entire request before state population changes. The source retains at least one person. Success and partial shelter gains belong to the receiving state. Source exposure changes remain on the source state.

## Building damage and repair

Official effect documentation defines `damage_building` for state scope. This proves the failure route that damages one eligible infrastructure level.

Official effect documentation defines `add_building_construction` as starting building construction. It does not document that effect as repairing one damaged level. No engine-native effect or reviewed repository helper has yet been proven to restore exactly one damaged infrastructure level without adding a new building level.

The success result for sealing and heating the civic core therefore remains blocked at the exact repair requirement. `add_building_construction` is not an approved substitute. The transaction may not claim this branch complete until an exact surface is proven or the user explicitly accepts a simplification.

## Trigger purity

Scripted triggers are read-only conditions. Effects such as `set_temp_variable` do not belong in a scripted trigger. Branch-specific availability triggers must use explicit trigger clauses. They may not mutate a requested-branch variable while the engine is evaluating an option trigger.

## Commit ordering and save recovery

The accepted transaction order is:

1. validate the current generation, durable cause memory, and every required registry row
2. derive the exact successor capital, live Air Winter values, live population, resource extrema, and separate country and cause memories
3. write the pending transaction marker last
4. issue the root event once
5. accept one affordable branch and pay its exact cost
6. freeze the branch, due day, score inputs, and result event identity
7. schedule the result event
8. write the issued-result marker last
9. authenticate the delayed result against generation, component, mode, branch, due day, and event token
10. apply one deterministic outcome
11. record the component receipt
12. clear only the issued-event receipt before advancing

A save before result issue may repeat the issue attempt because the issued marker is absent. A save after issue sees the marker and cannot issue a second result. A stale generation cancels the pending transaction and may not record a current receipt. The reconcile helper exists, but no recurring caller is authorized or implemented yet.

This ordering is a static transaction proof. Runtime scheduling and save-load behavior remain unobserved because the game is not being run.

## Deterministic scoring

The accepted score starts at 50 and uses only frozen inputs. Resource bands, Recognition bands, regional match, archetype match, exposure pressure, recovery and adaptation support, and unresolved crisis pressure live in typed script constants. Recovery and adaptation are each bounded from 0 through 100 before freezing. Their combined support input is bounded from 0 through 200, multiplied by 0.06, and rounded once to produce 0 through 12.

Success begins at 70. Partial success begins at 45. Lower scores fail. Equal AI projections choose the lowest stable branch identity. The national AI route derives a separate need value for each branch from the lowest resource in that branch's exact cost set. Human and AI routes pay the same costs and call the same result effects.

No random list, random country, random state, random delay, or live result-time rescore is permitted.

## Timed country modifiers

Official `modifiers_documentation.md` defines every modifier token used by the dormant orientation package. The country-facing values are `stability_factor`, `consumer_goods_factor`, `production_speed_buildings_factor`, and `repair_speed_factor`. Army-facing values are `supply_consumption_factor` and `attrition`. The state and war-production value is `mobilization_speed`.

Vanilla dynamic modifiers provide direct structural precedents for mixing these country and military categories in a modifier attached to a country. `0_dynamic_modifiers.txt`, `bba_dynamic_modifiers.txt`, `SEA_dynamic_modifiers.txt`, and `wuw_dynamic_modifiers.txt` contain country dynamic modifiers with `mobilization_speed`, `supply_consumption_factor`, or `attrition`. The Fallout package follows that structure and keeps magnitudes in `common/script_constants/fallout_world_end_event_constants.txt`.

The operational modifiers are dedicated Fallout definitions. Their names and paths do not reuse zombie content or a super-event package.

## Dormancy proof

The orientation substrate has no caller. It must not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`. It must not create family fatigue, cooldown mutation, or ordinary scheduler tickets.

Successor allocation, player continuation, a live conflict ledger, all required regional and archetype rows, country-memory rows, and curated character or institution registries remain prerequisites for a future caller. Typed regional, archetype, and country-memory approval gates are unset. The exact state-result mapping gate is also unset, so components two through five cannot mutate isolated shadow values and present them as live Air Winter results.

## National-orientation pilot

Event blocks `chaosx.fallout.62` through `chaosx.fallout.65` form the first manually written pilot in `events/fallout_world_end_events.txt`.

- `62` is the visible human root with three cost-gated authority choices.
- `63` is the hidden AI root. It uses the same affordability trigger, deterministic score projection, exact costs, and branch effect wrapper as the human path.
- `64` is the visible delayed result. Its immediate effect authenticates the issued token, resolves one score band, applies one exact result, records the current-generation national receipt, and retains the durable authority memory needed by the text.
- `65` is the hidden AI result. It calls the same resolver as `64`.

The pair uses the dedicated `GFX_report_event_fallout_national_orientation` sprite and concrete regional, government-aware, cause-memory, resource, population, and outcome text. Cause memory is frozen separately from the successor country-memory id. The tooltip values read from the same typed script constants as the transaction.

The pilot remains outside the 660-event release floor. It has no caller, event-log row, event-detail row, or ordinary-scheduler activation. The rest of the 23-block Ash-week package also remains incomplete.

## Static inspection result

The required `hoi4.event_inspect` lint was invoked with a manifest limited to events `chaosx.fallout.62` through `chaosx.fallout.65`. The selector was accepted, but the inspector returned `EVENT_HELPER_PROJECTION_LIMIT` because the repository event graph exceeded its fixed projection ceiling of 200000 helpers. A second attempt with helper expansion disabled returned the same blocker. No lint pass is claimed.

Repository-local checks confirmed balanced script blocks, unique event identities for `62` through `65`, a UTF-8 BOM on the new English localisation, no orientation caller, no scheduler activation setter, and no setter for any blocked approval surface. These checks do not replace runtime proof or the blocked event inspector.

## Post-pilot live-ledger review

`FALLOUT_ORIENTATION_LIVE_LEDGER_NUMERICAL_CONTRACT_PROPOSAL.md` records a proposed opening Cohesion formula, persistent State Supply Access, a native local-supply translation, and direct Air Winter state ownership. These choices are not accepted implementation facts until the user approves them.

The accepted survival calculation already derives a temporary 0 through 100 Logistics signal from post-rewrite non-damaged infrastructure. It does not persist that signal. `fallout_orientation_state_supply` remains confined to the orientation helper file and has no native supply consumer. The existing `air_winter_local_supply_factor` is a phase-derived penalty input, not a 0 through 100 supply ledger.

The live Air Winter state values for Exposure, Recovery, Adaptation, Food Reserve, Shelter Capacity, Reclamation, and Water Security are proven. `air_winter_recovery_bonus` is a documented repository integration input to the state recovery calculation. Orientation ownership of that bonus still requires the proposed numerical contract.

The independent architecture evidence is recorded in `subagent_handoffs/fallout_orientation_live_ledger_architecture_2026-07-18.md`. Its read-only event inspection returned partial artifacts and the same fixed 200000-edge projection ceiling. No event lint pass is claimed.

## Unresolved blockers

- The exact one-level infrastructure repair surface is not proven.
- The durable opening value for Cohesion has not been accepted. The queued numerical contract proposes a formula, but gameplay must remain blocked until the user approves it.
- The nine regional orientation rows, twelve archetype rows, and manually reviewed country-memory overlays are not implemented. Their typed approval gates remain unset.
- Components two through five remain blocked by `fallout_orientation_state_result_surface_status`. Their current shadow state variables are not accepted substitutes for live Air Winter and post-transition Supply Access values. The queued numerical contract is not yet authority to replace them.
- No curated character or institution registry exists. The fifth component must fail closed and may not invent candidates.
- Successor materialization and live tag-conflict allocation are not proven, so no orientation caller may be wired.
- The stale-generation reconcile helper has no authorized recurring caller. No daily or monthly world-country iterator was added.
- Literal lobby-host identity is not exposed by a proven engine trigger.
- The narrow event-inspector lint is blocked by `EVENT_HELPER_PROJECTION_LIMIT` at the tool's fixed 200000-helper ceiling.
- Runtime save recovery, delayed dispatch, state migration, and event visibility have not been observed because the game is not being run.
