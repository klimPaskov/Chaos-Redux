# Fallout Living-World Scheduler Proof

## Status

The living-world scheduler has a dormant numerical and transaction-integrity substrate. It records the reveal timeline, freezes a stable post-allocation country registry and pacing size, initializes country runtime rows, and implements activation-gated deterministic candidate review for crisis, routine, and broadcast openings. It also exposes five-part orientation, anti-repetition, ordinary-opening, arc, delayed-result, bilateral, cancellation, cleanup, routing, exact dispatch-issuance, and issued reciprocal terminalization contracts. Five global-survival pilot rows now have a Fallout-owned generation-bound producer for the food, produced-water, native-rail, Air Winter well, and Animal Feed chains. Major-arc and relationship candidates fail closed because their reviewed rows do not yet freeze the complete atomic class-reservation payload. The pilot producer remains dormant and is not a living-world caller.

The activation flags `fallout_event_scheduler_activation_approved` and `fallout_event_scheduler_active` have no setter. Suffixes `100` through `126`, `1009` through `1018`, and `153` through `174` are dormant typed reservations. Defined event blocks in those ranges: `59`. Countable blocks toward the 660-block release floor: `0`.

## Accepted numerical-contract tranche

The user approved `FALLOUT_EVENT_SCHEDULER_NUMERICAL_CONTRACT_PROPOSAL.md` on 2026-07-18. The accepted values are promoted into the source specs and implemented as typed script constants and dormant scheduler receipts.

- Frozen pacing size is small for 1 through 3 states, medium for 4 through 9, and large for 10 or more. The state count is copied from the committed survival row during dormant promotion and is not recomputed from later ownership.
- AI review uses the frozen registry count. Counts 1 through 30 process one row, 31 through 60 process two, 61 through 90 process three, and 91 or more process four through a stable cursor.
- Phase and size cooldowns are `24/18/14`, `28/24/20`, `32/28/24`, `34/30/26`, `36/32/28`, `38/34/30`, `40/36/32`, and `46/42/38` days from first season through open continuation.
- Every ordinary opening carries visible-budget cost 1 through 4. Ordinary cadence is base cooldown multiplied by cost. Crisis breaks use 42 days multiplied by cost. Human-visible delayed and bilateral rows may extend a local due day by one current base cooldown and cannot shorten it. Hidden result and cleanup rows use zero visible cost.
- Crisis break eligibility requires normalized pressure of at least 80, the exact current survival resource named by the row, a seven-day visible-popup gap, and 180 days since the previous used break. A lower-pressure crisis waits for ordinary cadence.
- Broadcasts carry cost 1, obey a global 30-day minimum, and extend every current human successor by one current base cooldown without shortening an existing due day.
- Cooldown-family fatigue is bounded from 0 through 100. An issued opening adds 60 once, decay is one per elapsed day, and index zero is explicitly fixed at zero.
- Candidate scoring uses the accepted phase, region, government, memory, winter, crisis, character, bilateral, route, prior-choice, war, severity, pressure, player-relevance, state-value, authored-adjustment, fatigue, repetition, and arc-capacity contributions. Resource pressure is `2 * clamp(50 - current, 0, 50)`. Air Winter phases 0 through 6 map to `0, 15, 30, 45, 65, 85, 100`. The score is rounded once at the end.
- Player relevance is derived rather than trusted. A human recipient is 100, an AI recipient with an exact current human bilateral partner is 50, and every other implemented row is 0. The accepted 25-point human-owned war or mission target requires a typed relationship receipt that does not yet exist, so that case remains fail-closed.
- Exact ties resolve by score, then crisis, major arc, relationship, routine, broadcast, lower candidate identity, lower target identity, and lower partner registry index. The selector contains no random or MTTH route.
- Two visible state-history slots provide the 90-day penalty and 120-day third-use veto. A row requesting the exception must target a current state and prove `is_capital = yes` at eligibility time. It retains the 35-point penalty. The active-siege branch remains fail-closed until Fallout owns a typed current-siege receipt. Nonrepeatable completion memory is permanent. Repeatable rows have a 90-day hard lock and a 50-point penalty through day 365.
- Hard row caps are three major arcs, eight delayed rows, and six bilateral rows per participant. New delayed and bilateral rows accept due days only from 1 through 730 days after creation. Exact retries are checked before new-row capacity, so reaching a cap does not invalidate an existing receipt.
- Human and AI lanes reconcile their current transaction rows before review. Human review is sourced only from the frozen committed-player array and requires current human control. AI review requires current AI control. Selected control mode is stored in ordinary, arc, delayed, bilateral, dispatch, and issuance receipts.
- Due work and cleanup reconcile before new selection. Delayed and bilateral due rows use the same `global.num_days` clock as their reservation and reconciliation paths. A new ordinary opening is issued on its commit day after its durable payload and cooldown receipts are written. Same-day retries reuse the exact ticket and cannot emit a second command.
- Empty schema-1 ordinary receipts behind an older ready header and completely empty current child ledgers may promote only while both activation flags are absent. Numerical initialization, fatigue issue memory, reviewed-candidate receipts, completion memory, bilateral memory, pending rows, or nonempty rows make promotion fail closed.

The numerical substrate does not define or call living-world event blocks. It does not earn release-floor credit.

## Owned files in this tranche

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`
- `common/scripted_effects/fallout_world_end_well_queue_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_well_queue_event_triggers.txt`
- `common/dynamic_modifiers/fallout_world_end_well_queue_dynamic_modifiers.txt`
- `common/scripted_effects/fallout_world_end_animal_feed_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_animal_feed_event_triggers.txt`
- `common/dynamic_modifiers/fallout_world_end_animal_feed_dynamic_modifiers.txt`
- `events/fallout_world_end_events.txt` event suffixes `153` through `174`
- `interface/fallout_world_end.gfx` Well Queue report sprite registration
- `localisation/english/fallout_world_end_well_queue_l_english.yml`
- `localisation/english/fallout_world_end_animal_feed_l_english.yml`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `docs/assets/fallout_well_queue/manifest.md`
- `docs/assets/fallout_well_queue/gfx_handoff.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/01_living_world_event_ecosystem.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/03_fallout_timeline_and_campaign_pacing.md`
- `docs/specs/air_cleanliness_fallout_specs/specs/12_event_content_budget_and_acceptance.md`
- `docs/specs/air_cleanliness_fallout_specs/matrices/fallout_run_event_budget_matrix.md`
- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_EVENT_SCHEDULER_NUMERICAL_CONTRACT_PROPOSAL.md`

The existing project coordinator call and on-action host are reused without modification by this tranche. No new on-action file, sound, or scheduler caller is added. The Well Queue event blocks, localisation, event-log route, and dedicated report art remain dormant until the activation and manual-review gates are opened.

## Reveal timeline transaction

A successful current-schema map return writes all three identity receipts:

- `global.fallout_event_timeline_generation`
- `global.fallout_event_timeline_start_date`
- `global.fallout_event_timeline_start_day`

It then sets `fallout_event_scheduler_initialization_pending`. The project coordinator calls `fallout_event_scheduler_reconcile` inside the existing at-most-once global-date transaction. A successful registry commit or dormant schema promotion clears the pending flag. The separate initialization status remains at orientation pending until future orientation content completes its receipts. No new daily or monthly on-action is added.

`fallout_event_map_return_receipts_are_current` requires completed Fallout, a successful map-return receipt, an inactive transition, the current transition generation, and start date and day values that are not in the future. Elapsed time is recomputed as current engine day minus the frozen reveal day. The exact phase bands are:

| Phase | Inclusive elapsed-day range |
| --- | ---: |
| Ash week | 0 through 7 |
| First season | 8 through 90 |
| First winter year | 91 through 365 |
| Consolidation | 366 through 730 |
| Rival orders | 731 through 1460 |
| New states | 1461 through 2190 |
| Soot retreat | 2191 through 2920 |
| Second world | 2921 through 3650 |
| Open continuation | 3651 onward |

The phase receipt records the transition generation and exact update day. Completed legacy Fallout saves do not receive a fabricated reveal day or scheduler request.

## Registry commit transaction

Registry construction begins only when `fallout_successor_allocation_is_current` passes. The builder copies the final deterministic order of `global.fallout_successor_assigned_countries`. It does not construct a second world-country pool.

Three aligned arrays retain country, transition generation, and stable zero-based index. Each country row stores the same generation and index. Validation proves:

- equal array lengths
- source count equal to the committed successor assignment count
- reciprocal membership between the source and registry arrays
- each stored numeric index equal to its real array position
- the country at that position stores that same index and generation
- current runtime schemas and bounded row values

The numeric index proof makes a duplicate country fail because one country cannot hold two different stable indexes. `fallout_event_scheduler_registry_ready` is written only after the complete uncommitted payload passes. It is the registry commit marker. Later annexation does not delete the frozen identity row or force the committed source allocation to be rebuilt.

## Country runtime row

Each committed registry member receives versioned runtime receipts for the scheduler, orientation, ordinary opening, arc slots, delayed queue, and bilateral ledger. The initialized row contains:

- active major-arc count of zero with a maximum of three
- twenty cooldown-family fatigue entries, including the unused index zero
- a last-family value used as a hard immediate-repeat veto
- an ordinary cooldown day
- a seven-day reveal quiet-period day
- five independent orientation receipts
- fourteen aligned compact major-arc arrays initialized empty
- seventeen aligned compact delayed-result arrays initialized empty
- sixteen aligned compact bilateral arrays initialized empty
- independent arc, delayed-result, and bilateral reconciliation cursors
- a generation-bound global ticket allocator with no ticket reuse
- cancellation history receipts
- one fixed ordinary-opening receipt with a generation, ticket, stable key, separate human and AI tokens, opening branch, due day, family identities, and optional typed target
- one structural dispatch envelope with a ready flag written last
- one exact dispatch-issuance receipt with its issued flag written last
- cleanup tokens, cleanup owners, and derived cleanup-pending flags

The five orientation components are national orientation, capital condition, immediate resource crisis, government archetype, and first character or institution. Ordinary-event eligibility requires all five current-generation receipts.

The ordinary cooldown helper and the four reservation APIs are unreachable from gameplay because every producer requires both activation flags, a generation-current ordinary-receipt registry proof, and a living owner. No file sets those flags and no event calls the APIs. The fixed ordinary receipt admits one outstanding opening per country without consuming a major-arc slot. It writes its pending flag last, accepts exact payload retries without allocating another ticket, and rejects a request key already owned by the delayed or bilateral ledger. Once its dispatch is issued, the fixed receipt becomes a blocking tombstone. Generic reconciliation cannot clear it after owner or target loss. Only the exact issued event may consume it or cancel it through the issued wrapper. Mutable actor, target, parent, and due-day checks apply only when a transaction is first created. An exact retry is authenticated from its existing immutable payload even after time advances or its subject is lost. Major arcs use derived occupancy for three compact slots. Arc stages advance one step at a time. Typed cancellation outcomes carry an aligned cancellation reason and exact retries do not duplicate history. The shared cancellation receipt also records the transaction source, so an ordinary retry cannot authenticate a delayed or bilateral cancellation with the same ticket and reason. Delayed rows retain separate human and AI tokens, a due day, visible cost, frozen control mode, target identity, outcome, cancellation reason, and cleanup token. An issued delayed row is also a blocking tombstone. Public ticket-only terminalizers reject it, and reconciliation preserves it after owner or target loss until the exact token-authenticated wrapper resolves, cancels, or releases it. Bilateral reservation writes one ticket to both countries, proves opposite roles, exact back-references, participant-specific visible cost and control mode, and the initiator cleanup owner, then rolls both rows back when the second commit cannot be proven. Bilateral status changes snapshot both rows, write both payloads before either status, prove both reciprocal directions, and restore both snapshots before recording an error when commit proof fails. An issued bilateral response is a blocking tombstone across both public pair terminalizers. Generic orphan reconciliation cannot clear the local issued row. Exact response wrappers authenticate the mirrored event token before resolving or cancelling both current reciprocal rows. If reciprocal proof has already been lost, the exact issued cancellation wrapper may terminalize only its authenticated local orphan. Public cleanup release rejects an issued local row. Exact cleanup release authenticates the issued cleanup token before removing that row. Each accepted issued path consumes its envelope in the same effect chain, and no detached acknowledgement API exists. Fatigue decay, opening mutation, completion memory, state repetition, pair-family memory, score calculation, candidate selection, crisis-break receipts, broadcast receipts, and deterministic human and AI review are implemented behind the unset activation gates. The survival identity stage remains transition owned and the scheduler only consumes its committed ledger.

Terminalization and cleanup remain callable without the activation gate so a disabled scheduler can recover existing rows. Public mutation and release APIs require the current frozen country identity, complete aligned family receipts, a current ticket, and exact cleanup tokens where applicable. Invalid arc actors receive typed cancellation receipts. Unissued delayed rows whose target or owner is lost also receive typed cancellation receipts. The same applies to unissued reserved or response-pending bilateral rows whose reciprocal or owner is lost. Issued ordinary, delayed, and bilateral rows retain their envelope until their exact event wrapper consumes it. A country that no longer exists cannot receive a new reservation or dispatch envelope. Resolved rows accept only success, partial, or failure. Cancellation outcomes require a typed nonzero reason through cleanup.

The selected country consumer accepts only a current registry row whose envelope still matches its exact ordinary, delayed, or bilateral transaction. Visible and hidden AI envelopes require both activation flags. Exact hidden-cleanup envelopes remain issuable after deactivation so committed rows can finish cleanup. The consumer copies source, ticket, generation, mode, event token, branch, target type, and target into an issuance receipt, records the engine date and day, and writes `fallout_event_dispatch_issued` last. Only then does a `meta_effect` construct and run `country_event = { id = chaosx.fallout.[FALLOUT_EVENT_ID] }`. Later coordinator passes accept the persisted receipt as current and do not emit that envelope again. Future ordinary content must commit any required child transaction before it calls the exact consume wrapper, or revalidate a stale subject and call the issued cancellation wrapper. Both wrappers authenticate the mirrored token and clear the envelope before releasing the fixed receipt. Issued delayed result, cancellation, and cleanup wrappers expose the same token-authenticated terminalization contract. Issued bilateral response, cancellation, orphan cancellation, and cleanup wrappers authenticate the exact event token and consume the envelope inside the reciprocal or local terminal transaction. No issued source permits a second acknowledgement. No event block calls any of these content-facing wrappers in this tranche.

This is a compatible extension of schema 2. An old schema-2 country row can promote only an exactly absent ordinary receipt while both activation flags remain unset. The one-time promotion iterates the numeric frozen-registry index array. Each index must match its stored index and generation, load the exact country context, and prove the promoted or newly initialized receipt. The proven count must equal the frozen registry count before the generation-bound global commit receipt is written. It does not rewrite compact arc, delayed, or bilateral rows or touch an existing envelope. An empty envelope and an unissued ready envelope require every issuance field to be absent. Existing schema-2 rows therefore retain their original empty or unissued meaning. The new transaction-source history field is required only when cancellation count is nonzero. Legitimate dormant schema-2 rows have zero cancellations because production was unreachable. Any unproven nonzero source-free history fails closed. No pre-existing consumer could have emitted an ordinary event because source token `ordinary_event` did not exist. A receipt mismatch clears no unrelated envelope and records the owned `ordinary_receipt_mismatch` or `dispatch_issue_receipt_mismatch` scheduler error. The static proof establishes command issuance and at-most-once coordinator behavior. It does not claim that an event popup was displayed.

Every public scripted effect that returns a temporary receipt requires the outer caller to create that temporary variable first. This follows the documented temporary-variable lifetime rule. All internal callers pre-seed outputs before they inspect them. No external gameplay caller exists in this tranche.

## Dispatch issuance state proof

| State | Envelope commit | Issuance commit | Valid next action |
| --- | --- | --- | --- |
| Empty | ready flag absent and all payload fields absent | issued flag and all receipt fields absent | a reconciled transaction may publish one envelope |
| Ready, unissued | ready flag present with an exact current transaction payload | issued flag and all receipt fields absent | the selected-country consumer may issue once |
| Ready, issued | ready flag present with the same payload | issued flag present with the complete mirrored identity and non-future date and day | ordinary content may commit a child and consume or cancel a stale subject through the issued wrapper, delayed content may use an atomic issued terminalizer, or bilateral content may use its exact issued response, cancellation, or cleanup wrapper |
| Consumed | envelope and issuance data cleared together | absent | the ordinary receipt is empty or the compact row has advanced to its terminal state |
| Partial or mismatched | any mixed shape | any mixed shape | fail the country row and preserve the transaction for diagnosis |

The ready flag and issued flag are separate commit markers. This distinction is what makes a save between command issuance and event resolution recover without a second command. Issued ordinary, delayed, and bilateral receipts remain pending even when their subject becomes invalid, so generic reconciliation cannot erase an unresolved engine event. After successful consumption, a replay of the issued wrapper fails closed instead of reporting a second success. It cannot repeat the state mutation or cancellation history. The coordinator advances its registry cursor after the issue attempt only when no owned scheduler error exists.

## Survival ledger boundary

The accepted resource identities are Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition. Cohesion and Reclamation are not resource entries.

The accepted transaction contract requires state rows with immutable producer inputs and country rows with immutable initial values, raw aggregation numerators and denominators, and separate mutable values. Each row binds to the transition generation. The global commit covers the exact finalized successor assignment and every included state. [FALLOUT_SURVIVAL_NUMERICAL_CONTRACT_PROPOSAL.md](FALLOUT_SURVIVAL_NUMERICAL_CONTRACT_PROPOSAL.md) records the accepted numerical formulas and commit order. [FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md](FALLOUT_SURVIVAL_NUMERICAL_TRANSACTION_PROOF.md) records the implementation and static arithmetic cases.

Survival initialization belongs inside the blackout after successor allocation and before player continuation. The live transition stages exact country and state identity rows, calculates state resources, aggregates country resources through frozen ownership, replays all arithmetic, and writes the global ready flag last. Resource identity arrays fix the accepted order, while aligned global arrays prove physical indexes and all-and-only scope coverage. The scheduler consumes this committed ledger but never creates or repairs it.

Registry schema 2 binds the scheduler registry to the survival schema, generation, and country count. A missing ledger records `survival_ledger_not_current`. The scheduler does not create, repair, or default survival values. Full details are in `FALLOUT_SURVIVAL_LEDGER_IDENTITY_TRANSACTION_PROOF.md`.

## Recurring mutation and read cost

The recurring reconciliation path performs timeline arithmetic and checks the frozen registry arrays. It selects one primary registry country per coordinator date, reconciles its fixed ordinary receipt at constant cost, and selects one primary compact row from each family through independent round-robin cursors. Full local receipt scans validate row shape once per family. Selected ticket, key, actor, and cross-family uniqueness checks are linear in the selected country local ledgers. Reciprocal proof scans the exact partner ledger once to find the matching row, then runs one selected partner uniqueness scan. A verified reciprocal partner may also be mutated by a bilateral status or cleanup transaction. The recurring read cost is therefore linear in the two local ledger sizes, with one fixed ordinary receipt, one primary compact row per family, and at most its exact reciprocal row eligible for mutation.

Compact-ledger reservation production uses stronger full-ledger uniqueness gates. These scan each local row against its family identities, which is quadratic in that local ledger. Bilateral production performs the gate for both participants. The fixed ordinary reservation uses current-row validation and linear local key and ticket membership checks instead. These producers are dormant and are not part of the recurring reconciliation path. Major arcs are capped at three, delayed rows at eight, and bilateral rows at six per participant. The reconciler does not build a global candidate pool. The successor-allocation barrier is evaluated only before the initial registry commit. A successful commit clears the initialization-pending flag and prevents that allocation proof from becoming a recurring annexation barrier.

The preceding one-country description is the base transaction-reconcile lane. When activation is approved, every current human row is reconciled before human selection and the stable AI cursor reconciles and reviews one through four current AI rows according to the frozen registry-count band. Each country scans only its manually reviewed local candidates. No recurring path constructs a whole-world candidate pool.

## Engine references

The installed official documentation is the primary syntax reference:

- `documentation/triggers_documentation.md` documents `all_of`, the matched value and index outputs of `any_of`, temporary-variable operations inside trigger evaluation, and the country-only scope of `exists`.
- `documentation/effects_documentation.md` documents `for_each_scope_loop`, `for_loop_effect`, `save_event_target_as`, `country_event`, and `meta_effect`.
- `documentation/script_concept_documentation.md` and `common/script_constants/documentation.md` document typed script constants.
- the offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` documents arrays, numeric array indexes, scope arrays, and temporary-variable lifetime.

The exact installed documentation surfaces used for the numerical tranche are `script_concept_documentation.md:216-226` for script constants, `triggers_documentation.md:1036` for `all_of`, `triggers_documentation.md:1515` for `any_of`, `triggers_documentation.md:2110` for `check_variable`, `triggers_documentation.md:5336-5343` for the state-scope `is_capital` trigger, `triggers_documentation.md:7440` for trigger-side `round_temp_variable`, `triggers_documentation.md:7482` for trigger-side `set_temp_variable`, `effects_documentation.md:2943` for `country_event`, `effects_documentation.md:4296` for `for_each_scope_loop`, `effects_documentation.md:4312-4328` for the default exclusive `for_loop_effect` end comparison, `effects_documentation.md:4833` for `meta_effect`, `effects_documentation.md:6476` for `round_temp_variable`, and `effects_documentation.md:7820` for `set_temp_variable`. The offline `Data structures - Hearts of Iron 4 Wiki.md` sections at lines 254, 415-417, and 817 onward cover event targets, unscoped temporary-variable lifetime, and arrays.

Repository precedents are `006_independence_wave_effects.txt` and `006_independence_wave_triggers.txt` for aligned scope registries and reciprocal row validation, plus `020_black_plague_effects.txt` for delayed scheduler state. Dynamic event dispatch precedents are `013_natural_disasters_effects.txt`, `air_cleanliness_winter_event_effects.txt`, and `fallout_manual_scenario_effects.txt`. Each formats an integer variable into a namespaced `country_event` id through `meta_effect`. The Fallout substrate retains separate schema and identifier ownership.

A refreshed exact read-only `hoi4.event_inspect` trace for `chaosx.fallout.62` used selector `{ kind: event, eventId: chaosx.fallout.62 }`, depth 2, 24 nodes, and 48 edges. The installed service returned `EVENT_HELPER_PROJECTION_LIMIT` at its fixed 200,000-helper ceiling before scanning a file or producing an artifact. This is a tooling limit and is not used as engine proof.

The reciprocal-row trigger does not promise to preserve its temporary validation index when a nested partner check fails because trigger evaluation may short-circuit. Every current false path aborts or resets the index before reuse. Future callers must follow the same rule.

An independent read-only completion audit found no P0 issue. Its initial pass identified the bilateral due-clock mismatch, the under-constrained empty numerical promotion, and the unauthenticated capital-or-siege recurrence bit. The implementation was corrected. A focused re-audit then returned no P0 through P3 finding on those surfaces, the human and AI lane comments, structural balance, activation setters, reviewed-candidate setters, or reserved suffixes `100` through `126`. The reviewed-candidate pilot was statically reconciled separately in `FALLOUT_REVIEWED_CANDIDATE_PILOT_PROOF.md`. These audits do not replace runtime proof and do not remove the blockers below.

## Fail-closed boundaries and activation blockers

The initialization and transaction effects record one owned error for reveal, allocation, registry, row-shape, ordinary-receipt, or reciprocal failure. Invalid dynamic country and state scopes require explicit context-loaded receipts, so a skipped variable scope cannot satisfy the proof. Country-row and orientation mismatches fail their eligibility triggers. A guarded one-time migration promotes paired runtime-schema-1 and registry-schema-1 rows only when the map-return receipt and a fully current committed survival ledger are current, both activation flags are absent, every preserved cooldown, fatigue, date, orientation, registry, and source field passes the current invariant, and every transaction array, cursor, history field, cleanup flag, ticket header, and envelope is absent or empty as required. The schema-1 migration initializes the empty ordinary receipt before committing the current registry. Existing schema-2 rows use the narrower absent-receipt promotion, which leaves all prior transaction payloads untouched. That promotion accepts either registry schema 1 or 2 only while dormant, so a current runtime row can acquire its fixed receipt before schema-1 registry-binding eligibility is evaluated. The binding transaction then writes registry schema 2, invokes the idempotent promotion again, and requires the full current payload before it clears initialization. The binding still requires the registry ready flag, absent activation flags, no scheduler error, current map-return receipts, a full survival ledger, and agreement across every indexed registry, allocation, and survival row. These checks run before any gameplay producer can pass. Frozen country identities may be annexed without invalidating source membership, while invalid dynamic scopes still fail closed. The scheduler does not repair a missing reveal date, substitute a lost actor or bilateral target, invent a survival value, or select an unreviewed successor.

The following work remains blocked or absent:

- Numeric initialization and aggregation rules for Food, Clean water, Medicine, Scrap, Fuel, Power, Filters, Shelter capacity, and Recognition are implemented. Cohesion and Reclamation remain separate mechanics. Scheduler activation and event content remain absent.
- World transition schema 12 authenticates frozen Air Winter rows with an Air-owned producer schema and generation, the frozen live category, accepted specialty buildings, coal, population, building, and supply receipts. Valid rows use exact produced values. Invalid rows use a typed N/A payload and are excluded from country coverage.
- Structural transaction families and deterministic crisis, routine, and broadcast selection are implemented but dormant. The reviewed candidate pilot producer is present for three ordinary global-survival rows, while the full candidate matrix, living-world event caller, human-choice caller, hidden AI result caller, content-owned cleanup execution, and scheduler debug presentation remain absent.
- Exact bilateral wrappers and issued-orphan retention are implemented without gameplay callers. Activation remains blocked until reviewed bilateral event content invokes those wrappers and proves its human, hidden AI, stale-subject, delayed-result, and cleanup paths.
- Fifteen dormant Ash-week orientation pilot, result, closure, and cleanup blocks exist without a caller or complete matrix. They remain uncounted.
- Major-arc and relationship candidates fail closed until reviewed rows freeze the complete atomic class-reservation payload.
- Delayed and bilateral rows do not yet own actor fields, so cross-ledger independent-actor exclusion remains blocked.
- Pair-family memory is not yet an atomic reciprocal reservation and stale pair-memory rows are not yet pruned.
- Current-capital recurrence exceptions use the documented live state trigger. Active-siege exceptions remain fail-closed because no typed current-siege producer receipt exists.
- Literal multiplayer lobby-host identity remains unavailable in the documented script surface. The live authority is the project coordinator.
- No runtime observation was performed. HOI4 was not launched.

These omissions keep both scheduler activation flags unset and keep every reserved living-world event outside the release-floor count.

## Orientation event-surface correction

The capital condition and first character or institution event surfaces are now
defined at `chaosx.fallout.66` through `.69` and `chaosx.fallout.78` through
`.81`. The Ash-week orientation package has 23 defined blocks of 23 reserved
identities. They remain dormant and uncounted because the host-authoritative
caller, complete manual coverage, candidate installation audits, event logs,
event details, and runtime proof are still absent.

The orientation result surface now has a dormant Fallout memory history at
`9110`. Its 45 payloads distinguish every component, branch, and outcome, and
the writer rejects duplicate rows for the same component and transition
generation. This improves observability but does not activate the scheduler
or add release-floor credit.
