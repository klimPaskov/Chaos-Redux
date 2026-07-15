# Fallout Engine Surface Proof

Status: implementation gate record for the installed Hearts of Iron IV build and the current Chaos Redux map surface.

This record separates proven engine behavior from design intent. A surface listed as unproven is not silently replaced by a weaker mechanic.

## Reference set

The proof pass used the required offline wiki pages in `paradox_wiki/`, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface modding, Scripted GUI modding, Map modding, State modding, Building modding, and Graphical asset modding.

The following official game documentation was used as the higher authority:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/dynamic_variables_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/scripted_guis/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/map_modes/documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/on_actions/_documentation.md`

## Exact thermonuclear province sweep

Verdict: exact native per-province call construction and installed-map coverage are proven. Runtime acceptance and bounded execution cost are not proven.

The engine does not expose `every_province`. That absence does not require a state-level substitute. The accepted manual-scenario plan explicitly permits a supported expansion of a verified province list into nuclear effects.

The exact route is:

1. Build a stable ledger from the installed map data.
2. Include only province ids that appear in a valid state `provinces` block and whose `map/definition.csv` type is `land`.
3. Expand the ledger into inclusive `for_loop_effect` ranges.
4. Pass each ledger value to the native `launch_nuke` effect with `nuke_type = thermonuclear_bomb`.
5. Advance a persistent batch cursor and begin the seven-day countdown only after issued, observed, state-count, and state-sum barriers all pass.

Current map audit:

- Chaos Redux has no `map/` override.
- Vanilla has 10,272 unique state-assigned province ids.
- 10,154 of those ids are land provinces in `map/definition.csv`.
- 118 state-assigned ids are non-land and are excluded.
- One land province in `map/definition.csv` is not assigned to a state and is excluded.

This route produces 10,154 actual thermonuclear launch calls. It does not use one strike per state, province modifiers, or variable-only fallout. The engine does not enumerate the provinces itself. The ledger is a version-pinned expansion of installed map data, while every result is still produced by the native `launch_nuke` effect.

The dormant implementation is split into 41 bounded effects. Batches 0 through 39 contain 250 exact ids. Batch 40 contains 154. Re-expanding all 533 emitted ranges produced 10,154 unique ids with zero order mismatches against the canonical ledger.

Installed-map hashes and the independent audit format are recorded in `FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md`. The canonical sorted valid-id hash is `A0F5504AEA22EC76D8C687228C9A4BF485B255C2F8CA9E7DB8A62CFB8D259949`.

Engine evidence:

- `effects_documentation.md`, `launch_nuke`, accepts a province target and an explicit `nuke_type`.
- `effects_documentation.md`, `add_to_array`, `for_each_loop`, and `for_loop_effect`, support scalar province-id storage and deterministic iteration.
- Vanilla `common/raids/nuclear_raids.txt` passes a variable-backed province id to `launch_nuke` and sets `nuke_type = thermonuclear_bomb`.

The ledger must be regenerated and reviewed if Chaos Redux adds a map override or the installed game map changes. The public scenario remains blocked until runtime review proves that every scripted launch is accepted, that the native callback occurs once inside the guarded window, and that 250 calls per batch are bounded.

## Exact seven-day delay

Verdict: proven, provided the delayed event is owned by a country guaranteed to exist for the full interval.

`effects_documentation.md`, `country_event`, defines `days` as an exact delay and treats months separately as 30 days. Vanilla `events/AAT_Denmark.txt` repeatedly uses `country_event = { id = ... days = 7 }`.

The dormant substrate schedules `chaosx.fallout.903` with `days = 7` and no random delay after the complete sweep verifier passes. It also stores the start day and exact end day. Only the engine-scheduled callback may submit the request. The host daily coordinator never submits or reschedules the countdown because an integer day cannot preserve the starting hour. Lost coordinator ownership and a callback after the stored end day fail closed. The offline Event modding reference notes that delayed country events stop counting while their target country does not exist, so recipient survival remains a runtime-sensitive property.

## Host authority and idempotency

Verdict: at-most-once daily simulation coordination is proven. Literal multiplayer lobby-host authority is not exposed by the documented script surface.

`common/on_actions/chaosx_on_actions_chaos_meter.txt` owns the existing country-scoped daily path with the project-defined `is_global_host` country flag. The live branch clears duplicate host flags. A non-host human may take the flag only when the flagged country is AI. `fallout_reconcile_coordinator` records `global.fallout_coordinator_last_reconcile_date` before manual, migration, phase-scheduling, or request work and rejects repeats of those transactions on the same global date. A later call may only repair the persistent coordinator target and clear a stale scheduled-recipient flag after host transfer. This follows the date-receipt pattern already used by Air Winter and natural Air Contamination sources. Fallout does not add another recurring world iteration.

No official trigger or scripted-GUI surface was found for identifying the actual network lobby host. The project flag supplies one synchronized simulation coordinator, not proven literal lobby ownership.

All request sources write to one global request ledger. The coordinator accepts the first valid request, records cause and intensity, and rejects duplicate transition starts. Manual, terminal-event, and Air Contamination callers do not own their own rewrite chains.

## Dormant living-world scheduler registry

Verdict: exact reveal-day arithmetic, aligned registry construction, stable index identity, dormant eligibility, structural transaction integrity, typed owner, actor, target, and reciprocal loss cancellation, and at-most-once dispatch command issuance are statically evidenced. Candidate selection, event scheduling, live event presentation, hidden AI mechanics, content-owned cleanup, survival aggregation, literal lobby-host ownership, and runtime save behavior are not proven.

A successful current-schema map return records `global.fallout_event_timeline_generation`, `global.fallout_event_timeline_start_date`, and `global.fallout_event_timeline_start_day`. The timeline trigger rejects a future date or day and requires the current transition generation. Elapsed campaign time is current engine day minus the frozen reveal day. Phase boundaries are exact through day 3650, with open continuation beginning on day 3651. Completed legacy Fallout saves receive no invented reveal receipt.

The existing coordinator calls the dormant reconciler inside its at-most-once global-date block. Registry construction first requires `fallout_successor_allocation_is_current`, then copies only `global.fallout_successor_assigned_countries`. Official `all_of`, `any_of`, `for_each_scope_loop`, and `for_loop_effect` documentation supports aligned arrays, matched index capture, and loop syntax. Each numeric index must equal its physical array position, and the country at that position must store the same index and generation. Explicit context-loaded receipts reject skipped invalid variable scopes. This rejects duplicate rows without a recurring `game:all_countries` candidate query. The ready flag is written last as the commit marker, then the initialization request is cleared. Later annexation does not rerun the successor-allocation barrier. One primary frozen registry country reconciles per date and one primary row is selected from each family. A proven bilateral pair may also mutate its exact reciprocal row. Full shape scans and selected identity proof are linear in those two local ledgers. Production-only full uniqueness gates are quadratic in each local ledger. Delayed and bilateral queue caps remain absent.

Country runtime rows initialize five orientation receipts, twenty nonnegative cooldown-family fatigue slots, one last-family hard veto, ordinary and quiet-period due days, and schema-2 aligned compact arc, delayed-result, and bilateral ledgers. A generation-bound monotonic allocator supplies tickets. Independent cursors, typed cancellation history, sequential arc stages, derived arc occupancy, cleanup flags, dispatch envelopes, and mirrored issuance receipts are validated against their source rows. Bilateral status changes snapshot both sides, write both payloads before either status, authenticate the initiator cleanup owner, and roll both rows back when two-direction reciprocal proof fails. A guarded schema-1 promotion proves the current map return, the full legacy registry, every preserved runtime invariant, and the required absence of later transaction fields before mutation. Lost owners cannot receive reservations or dispatch envelopes, but terminalization and cleanup remain available. Fatigue mutation, decay, and score magnitudes remain undefined because the accepted specs do not supply them. The ordinary trigger and every reservation producer require two activation flags that have no setter. Suffixes `100` through `122` have no event definitions and count as zero release-floor blocks.

The scheduler does not initialize survival values because the accepted specs do not define numeric source formulas. Only the schema and nine resource identities are reserved. The required state and country receipt transaction and pre-player-continuation transition barrier are absent. Schema 9 authenticates each frozen Air Winter input as either a current produced row or an explicit N/A row. It also freezes the live state category independently from Air Winter's historical restoration category. Structural arc, delayed-result, reciprocal bilateral, cancellation, cleanup-envelope, human-versus-AI routing, and dispatch-issuance contracts exist but remain dormant. The selected-country consumer mirrors the exact envelope, writes its issuance commit last, and formats the stored suffix into a `chaosx.fallout` country event through the documented `meta_effect` route. No candidate selector, event scheduler, living-world event definition, hidden AI resolution, or content cleanup consumer exists. `FALLOUT_EVENT_SCHEDULER_PROOF.md` records the full scheduler contract. `FALLOUT_AIR_WINTER_SNAPSHOT_PROVENANCE_PROOF.md` records the producer and lock contract.

## Destructive state rewrite receipts

Verdict: the grading, Deaths, modifier, category, permanent state-building removal, province supply-network selector, and live observation surfaces are documented. No exact precedent removes `supply_node` or `rail_way` through this selector. Immediate read after write timing and railway topology mutation are not explicitly guaranteed. Non-idempotent transactions record an issue barrier before mutation. The network transaction may retry only the idempotent set-to-zero operation until the exact result is visible. Every row fails closed when its stored request and observation differ.

World transition schema 11 captures player and world rows through one effect-chain epoch. The shared epoch records the transition generation and capture date. Air Winter opens a distinct producer generation for every attempt, including a retry on the same date. Valid state rows initialize and normalize through the Air Winter-owned producer, then copy only after the complete canonical row passes. Invalid states receive a typed N/A row without initialization. The synchronous capture proof compares the frozen produced payload to the live producer receipt. A separate category enum must match the live `has_state_category` result during capture. The Air Winter original category remains historical provenance and classifier memory. State rows also prove that stored owner and controller scopes equal the live owner and controller during capture. Player rows prove that every currently owned state has one matching origin row and that no extra origin row points back to the player. A retry discards and rebuilds both snapshot halves together. Blackout and world-end ownership are committed only after both halves pass. After lock, the existing monthly Air pass continues to collect contamination, but every Air Winter begin, state update, event dispatch, response refresh, and finalization call is paused while `fallout_transition_active` is set. This keeps the frozen climate and category inputs stable without adding a world iterator.

Grading uses only frozen request, nuclear, Air Winter, contamination, population, live category, building, resource, coastal, war, owner, and controller inputs. A calculation helper recomputes the expected score and survival value from those frozen inputs. The row requires both reconciliation receipts, the exact score band, grade from 0 through 5, altered-biosphere subtype consistency, survival range, and current generation. A failed grading row is safe to clear and rebuild because no destructive state effect has started.

Population intent remains the rounded grade percentage of frozen population. The committed amount is then clamped against live population above the protected floor. The state stores its live baseline and sets `fallout_population_loss_mutation_issued` before calling the population-only mutation helper. It reads population again and derives the observed loss. Only an exact observed delta is sent to `chaos_meter_register_deaths` with state population application disabled and Deaths reason `fallout_aftermath`. A separate Deaths input records the same observed loss in the state Deaths map ledger without applying population again. Stored total, sequence, and state-ledger deltas prove registration. Zero loss and the user-disabled Deaths setting have distinct stored outcomes. Recovery observes the one issued mutation and never calls it again. A mismatch leaves the blackout active and does not write a Deaths entry.

Physical collapse records an immediate total-level baseline, available level, rounded fractional request, post-removal total, and observed delta for infrastructure, civilian factories, military factories, air bases, and dockyards. `effects_documentation.md` lines 5838 through 5871 document `remove_building` in state scope and explicitly exclude recursive province-building removal. Vanilla `common/scripted_effects/CHI_scripted_effects.txt` lines 972 through 983 pass the variables `af_level` and `ic_level` to its `level` field. Each family must lose exactly the requested number of `building_level@type` levels before its receipt finalizes. Existing partial damage does not change the unit because the transaction observes total building levels. The issue flag is written before removal, so recovery never removes another level. Historical variable names containing `building_damage` are retained for save and code compatibility, but schema 11 defines them as permanent level-loss receipts.

Category rewrite calculates one target from the frozen live category. Grades 0 and 1 keep that category. Grades 2 and 3 lower an eligible urban or rural category by one step. Grades 4 and 5 target wasteland. The stored target must recompute exactly, match the live category, and have an enum rank no higher than the frozen baseline. This prevents the previous path from upgrading a state that Air Winter had already degraded. Grade 3 and above also requires the supply-collapse flag and grade modifier.

Province supply collapse uses `set_building_level`, not `remove_building`. The offline Effects reference documents `province = { all_provinces = yes ... level > 0 }` for `set_building_level`. Vanilla `common/decisions/GER.txt` lines 13348 through 13356 uses that exact reset shape for bunkers. The official building definitions classify both `supply_node` and `rail_way` as provincial buildings. Vanilla supplies a close `supply_node` selector precedent and approved mod `1458561226` supplies a close `rail_way` selector precedent under `add_building_construction`. No vanilla or approved-mod call was found that removes either family through `set_building_level`.

Grades below dead city record an explicit zero-request row and settle without an engine call. Dead-city and higher grades record the immediate live state aggregate as the exact request and commit an immutable row intent. Each family settles only after its aggregate reaches zero and the official `any_province_building_level` trigger finds no selected province above zero. An interrupted or delayed family remains unsettled and can repeat only the idempotent set-to-zero call. The world receipt is written only after every state row passes, and successor inventory, allocation, state-rewrite, and map-return gates require the durable receipt.

Schema-10 active transitions may promote only before successor allocation. Phase 2 can promote before grading mutation. Later eligible phases require current grading and exact live-to-frozen network equality for every destructive-grade state before schema promotion. Phase 3 continues to population loss and phase 4 executes physical collapse. A promoted phase 5 or 6 rewinds to physical collapse and invalidates derived government and conflict rows. Schema-10 phase 7 or 8 states, allocated states, unrelated errors, and ambiguous rows remain blocked. Completed schema-10 saves are not replayed. They remain complete with explicit legacy flags that state current-schema and supply-network receipts are absent.

The official documentation does not state whether `state_population_k` and `building_level@type` must expose a mutation immediately later in the same effect chain. It also does not prove that zeroing selected `rail_way` levels removes every cross-state network edge. No Hearts of Iron IV run was authorized. The next coordinator attempt can reconcile a delayed read from its stored baseline without repeating population, state-building, node, or railway loss. A value that still differs remains under blackout and cannot obtain the world network receipt. Accepted receipts remain durable after later demographic or construction changes. Immediate read timing, recruitable-manpower neutrality, and railway topology behavior remain unresolved runtime acceptance obligations. The complete network proof is recorded in `FALLOUT_SUPPLY_NETWORK_COLLAPSE_PROOF.md`.

## Winter mapmode

Verdict: proven.

Official scripted map-mode documentation supports state color layers, country background layers, daily updates, state tooltips, and a forced refresh effect. Chaos Redux already has working state mapmode precedents in `common/map_modes/chaosx_state_map_modes.txt`.

The Air Winter mapmode can therefore expose phase, trend, exposure, recovery, adaptation, food, shelter, reclamation, and category pressure without relying on a country-wide color.

The icon route is also statically proven. Vanilla's scripted-mapmode documentation resolves dedicated selected and deselected sprite names from the mapmode key. All six Air Winter icons use those exact names and decode to 20 by 18 pixels. The shared Chaos Redux strip is a coherent 380 by 18 texture with 19 exact 20-pixel frames. Its first 17 frames match vanilla, frame 18 owns Deaths, and frame 19 owns contaminated states. Air Winter requires no shared-strip frame. Exact hashes and decoded-frame comparison are recorded in `AIR_WINTER_MAPMODE_ICON_PROOF.md`.

## Normal-map climate route

Verdict: official effect signatures and the approved normal-mapped entity precedent prove the regional state-cue route. Runtime visual observation is outside this proof. Native runtime weather replacement is not claimed.

The normal-map prototype evaluates two independent script surfaces:

- A low-opacity player-context GUI grade attached to the main interface. Its visual elements use `alwaystransparent = yes`, which the offline Interface modding reference defines as click-through behavior. Full-screen sizing and click-through are separately documented, but no local precedent proves a parentless full-screen grade that stays behind every hardcoded window. The proof must therefore check interface tint, border readability, mapmode interaction, and open-window behavior before this surface is accepted.
- State-positioned, normal-mapped 3D entities created with the documented `create_entity` effect. The effect accepts state or province placement, scale, minimum zoom, a stable id, and a scripted visibility trigger. `destroy_entity` and stable replacement ids provide a lifecycle surface for thaw and cleanup.

The approved Kaiserreich reference implements runtime landmarks through `common/scripted_effects/00_ambient_object_effects.txt`, registers the matching entities under `gfx/entities/landmarks.asset` and `gfx/entities/landmarks.gfx`, and calls those helpers from live country events. Its compiled meshes bind diffuse, normal, and specular textures. This proves the runtime normal-mapped entity chain on the ordinary map.

The route can place coarse regional snow, frost, cold rain, ash, dead vegetation, frozen-water, and thaw cues on the ordinary map. Presentation class and phase decide which entity family is used. Desert and tropical states do not inherit universal snow. A state target chooses the entity center. It does not conform the mesh to state borders and does not rewrite the static terrain normal map. The implementation must therefore call this a normal-mapped entity route, not a terrain-normal or state-decal rewrite.

The official effect catalogue exposes `randomize_weather`, but it does not expose a state or strategic-region effect for forcing a selected weather type or replacing the native snow-cover simulation. The implementation therefore does not claim to rewrite native weather or water shaders. Military weather pressure is driven by the same state phase through documented modifiers while the supported entity layer supplies the matching normal-map cue.

Save recovery must derive from the saved state phase and presentation class because `on_startup` does not run when loading a save and no useful `on_load` route is documented. Runtime-created entity serialization is not documented. The lifecycle effect must therefore reconstruct the desired entity on every existing Air Winter coordinator pulse. Reusing a stable id is documented to replace an existing entity, making that reconstruction idempotent. Recovery is guaranteed on the first resumed coordinator pulse, not at the load screen. Entity ids have no documented reserved range, so Fallout and Air Winter require their own reviewed id ledger before rollout.

Multiplayer clients read the synchronized phase ledger and receive the same scripted effects. The bounded prototype supplies one coarse entity, one proof state, one reserved stable id, a create-or-replace helper, and a destroy helper. Zoom behavior, terrain intersection, visual replacement, and save recovery remain unobserved runtime properties and are not claimed.

## Blackout GUI and input control

Verdict: static evidence proves only that a non-transparent top-layer blocker can intercept pointer hits on controls beneath its own layer. Complete pointer priority over every hardcoded popup, complete keyboard capture, shortcut suppression, native exclusive input, pause control, and all-resolution coverage are not proven.

The official scripted-GUI schema binds `window_name` to an independent `containerWindowType`. The current `interface/fallout_world_end.gui` blackout root uses `windowType`, so its scripted-GUI binding is not structurally proven. Its fixed `10000` by `10000` blocker is not proof of coverage at every supported resolution. Root parentlessness places a structurally valid scripted GUI over most UI, but it does not prove priority over every hardcoded popup.

The official schema exposes context, window binding, parent attachment, visibility, effects, triggers, properties, dynamic lists, dirty updates, and AI controls. It exposes no modal, exclusive-input, keyboard-capture, shortcut-suppression, or pause surface. Vanilla `interface/frontend_friends_view.gui` describes an `event_trap` used with hardcoded `SetExclusive` to block input outside a native popup. `SetExclusive` is not exposed to scripted GUI.

Visibility and sequential text can be re-evaluated from synchronized global state only after the container binding is structurally valid. This can recover visual beat state. It cannot restore exclusive-input state because scripted GUI exposes no such state. The project-defined `is_global_host` remains a deterministic simulation coordinator rather than a proven literal lobby host, and it cannot suppress client-local keyboard input.

Converting the blackout root to a full-screen independent `containerWindowType` with percentage sizing is only a possible fallback for broader pointer coverage. It requires explicit user approval before any GUI change. It would not prove total pointer priority, keyboard capture, shortcut suppression, native exclusive input, or pause control. Pointer-only behavior is not approved as a substitute for the required blackout.

## Dynamic successor allocation

Verdict: the creation effect is documented, and the generation-bound pre-allocation inventory and separate post-allocation proof contract pass static structural review. Runtime validity, conflict-free successor selection, and materialization are not proven.

`create_dynamic_country` is documented in `effects_documentation.md`. It can create a country from a selected original or copy tag and run initialization effects. Fallout may use it only after the live conflict inventory records occupied countries, possible country scopes, known active event packages, player reservations, and exact safe-candidate states.

Derived inventory schema 1 records each current country, each possible country scope, and each state for the active transition generation. Current-row validation checks identity, original tag, capital consistency, human control, known package ownership, player reservations, and candidate membership. It never treats a possible country scope as a materialized country. It does not select a Fallout package, regional package, final package archetype, conflict result, or cleanup owner.

Successor allocation schema 2 records which inventory generation was consumed and validates the output world instead of requiring frozen owner rows to remain live. Static checks require every source to remain recorded, resolved, non-pending, and bound to the consumed generation. Resolution and cleanup generations must be current. Every non-retired source must name one output, and the output must link back with the same result, generation, and cleanup owner. Converted, released, and dynamically created results require distinct current-generation provenance receipts. Possible-country membership alone cannot prove release. A retired source must own no state, carry no committed assignment, and name no output. The proof also requires unique assigned country scopes, unique assigned capital states, exact live-landholder coverage, a preserved classifier origin, a separate final archetype, one of nine registered regions, a positive country-memory id, current country, focus, archetype, regional, and country-memory package generations, exact capital ownership and control, and a valid ordinary, player-reserved, or protected-event origin state. Each player-reserved source must name the same output as its player continuation primary target. The guarded finalizer is the only setter for `fallout_successor_allocation_complete`. No allocator calls it, so the proof remains fail closed.

The ledger's remaining engine-sensitive properties are dynamic-country membership in `game:all_possible_countries`, behavior of absent possible-country scopes, persistent `original_tag` storage, unusual dynamic or exile capital behavior, comparison and save behavior for scope-valued variables, and collection membership after tag mutation. The known package-ownership predicate is a reviewed snapshot, not an automatically complete registry. It must be re-audited before any ownership or tag mutation. The 99-successor matrix remains a candidate pool.

## Old-world diplomacy reset

Verdict: the documented engine can clear and validate a large proven subset. A complete exact reset is not proven.

The implemented coordinator transaction uses official effects for these surfaces:

- `end_exile` for governments in exile
- `recall_volunteers_from` for volunteers
- `cancel_purchase_contract` inside `every_purchase_contract`
- `set_collaboration` with zero value
- `remove_civil_war_target` followed by `white_peace`
- `white_peace` for remaining wars
- `end_puppet` from the actual overlord scope
- `dismantle_faction`
- `diplomatic_relation` with `active = no` for guarantees, military access, docking rights, market access, non-aggression pacts, and embargoes
- `remove_resource_rights` for every live country-state pair

Official validation triggers prove the absence of wars, civil-war links, factions, subjects, exiles, guarantees, military access, non-aggression pacts, embargoes, volunteers, collaboration values, purchase contracts, resource rights, and active peace conferences.

Docking rights have a complete static reset route without a readback trigger. Official `effects_documentation.md` defines `active = no` as cancellation of an existing diplomatic relation. The offline `Effects` page lists `docking_rights` as a supported relation token. Vanilla `events/AAT_Finland.txt` and `events/TAOG_Australia.txt` cancel that exact token with `active = no`. Fallout applies the inverse unconditionally across every ordered pair of live countries, which covers both relation directions even when no detector can identify the stored side. The coordinator records application and verification receipts bound to the current transition generation only after the exhaustive loop finishes. This proves exact static coverage from the effect contract and iterator domain. It does not claim runtime readback because the engine exposes no documented docking-rights trigger.

Market access has a complete static reset and validation route. Official `effects_documentation.md` defines `diplomatic_relation` with `active = no` as cancellation of an existing relation. Official `triggers_documentation.md` defines `has_market_access_with`. The official effect documentation does not enumerate the market token, and vanilla has no scripted cancellation example. Vanilla still identifies `market_access_rights` as the canonical relation token in `common/ai_strategy/DEN.txt`, `interface/international_market/international_market.gfx`, and diplomacy localisation. The approved Kaiserreich reference supplies the cancellation precedent in `common/scripted_effects/00_useful_scripted_effects.txt`. Its `clear_relations_with_PREV` helper guards on `has_market_access_with`, calls `diplomatic_relation` with `relation = market_access_rights` and `active = no`, and handles both relation directions. The same pattern appears in `common/scripted_effects/00_economic_sphere_scripted_effects.txt`. Fallout dismantles factions and subjects before applying that inverse across every country pair, records current-generation application and validation receipts, and proves global absence with the official trigger. No Hearts of Iron IV run was performed, so runtime execution remains an acceptance obligation rather than a claimed observation.

Resource rights also have a complete static reset and validation route. Official `effects_documentation.md` defines country-scoped `remove_resource_rights = <state>`. Official `triggers_documentation.md` permits country-scoped `has_resources_rights = { state = <state> }`. The offline `Effects` and `Triggers` pages document the same direction. Vanilla `common/on_actions/07_nsb_on_actions.txt` passes a state scope to the country-scoped inverse with `remove_resource_rights = PREV`. Fallout unconditionally issues that inverse for every live country-state pair, including states where the documented trigger cannot observe a grant because the state has no resources. It then records current-generation application and validation receipts and repeats the global pairwise query for every observable grant. This resolves old-world extraction grants without treating the detector's resource-free-state warning as proof of absence. It does not resolve ordinary factory-for-resource imports.

The following exact inverses are absent from official documentation:

- active lend lease
- ordinary resource imports and trade routes
- intelligence agencies, operatives, networks, decryption, and static intel
- expeditionary-force return
- active peace-conference termination

Expeditionary forces can be detected, but the transaction has no proven return effect and records a blocker when any are present. A broad army teardown is not an exact substitute. The accepted migration plan requires expeditionaries to return. Official `delete_units` selects a named division template, while `transfer_units_fraction` moves whole army, navy, air, stockpile, and leader categories without an expeditionary filter. Neither effect can isolate every received force and restore it to its recorded sender. A peace conference can be detected and causes the reset to wait. Lend lease has a complete ordered-country-pair readback through the official `is_lend_leasing` trigger. The offline `Triggers` page defines the trigger direction as the current country lending to the specified country. Vanilla uses the same form in `events/Spain.txt`, including `ROOT = { is_lend_leasing = PREV }` inside a country iterator and `is_lend_leasing = SPR`. The transaction checks every ordered country pair, records a current-generation verification receipt when no lease exists, and blocks when it finds one because no documented cancellation effect exists. Ordinary imports and the full intelligence state still have neither a complete documented enumerator nor an exact reset effect. Official documentation exposes `create_import`, but no cancellation effect. Vanilla and the approved reference mods contain no scripted import cancellation or zero-value deletion precedent. The executable token `cancel_imports` is not accepted as a script surface because it has no official documentation or live script use. Intelligence offers partial enumerators and effects, including agency presence, operative counts, network strength, decryption progress, and operative removal. Those surfaces cannot remove an agency, its upgrades, every network, decryption state, captured-operatives state, and static intelligence as one complete reset.

`fallout_old_world_diplomacy_full_reset_is_verified` requires explicit verified flags for every required surface. Map return cannot pass while any proof is missing. This is deliberate fail-closed behavior, not a substitute mechanic.

Primary anchors are `effects_documentation.md` entries for `diplomatic_relation`, `dismantle_faction`, `end_exile`, `end_puppet`, `every_other_country`, `every_purchase_contract`, `recall_volunteers_from`, `remove_civil_war_target`, `remove_resource_rights`, `set_collaboration`, `cancel_purchase_contract`, and `white_peace`. Validation uses the corresponding entries in `triggers_documentation.md`, including `civilwar_target`, `has_collaboration`, `has_market_access_with`, `has_military_access_to`, `has_non_aggression_pact_with`, `has_resources_rights`, `has_volunteers_amount_from`, `has_war_with`, `is_in_peace_conference`, `is_lend_leasing`, and `received_expeditionary_forces`. The offline wiki `Effects` page independently lists docking rights as a supported `diplomatic_relation` type, while listing `give_market_access` only as a creation effect. The offline wiki `Triggers` page independently documents the `is_lend_leasing` target and direction.

## Player continuation transaction

Verdict: the engine surfaces for snapshot, state reservation, materialization, capital assignment, and individual player switching are proven. Exact multi-client commit behavior and literal lobby ownership are not proven.

The transition snapshots every human-controlled country once with `is_ai = no`. It records the country scope, database id, former capital, original player-owned states, and transition generation. A landed source receives the former owned capital or lowest state id as its deterministic source anchor. A landless human remains a valid snapshotted source and receives no fabricated anchor.

Before the general pool is built, every snapshot-origin player state receives a current-generation reservation. The strongest hostable origin state is selected for in-place continuation. When no in-place target is ready, the source receives one explicit fragmented, refuge, altered, or emergency materialization row. The reservation ledger can therefore reach a future allocator without claiming that a missing destination already exists. Allocation initialization makes the consumed reservations immutable. Later drift owns `player_reservation_changed_after_allocation` and does not rebuild the ledger. Final planning remains incomplete until the allocator supplies an actual target and capital.

The live conflict ledger separately records every existing country, `game:all_possible_countries`, player-reserved states, and unreserved hostable states. A nonexistent static country in `game:all_possible_countries` is not treated as materializable by that fact alone. It needs an explicit release package or a documented dynamic-country creation route.

Official collections and array effects prove the ledger surfaces. `transfer_state`, `set_capital`, and `create_dynamic_country` prove the materialization primitives. Vanilla player-preservation chains prove `change_tag_from` for one player. Official country-tag aliases permit a variable-backed origin alias when a different successor must take over a player.

The current implementation only plans the proven surviving-tag branch. It reserves the former capital when hostable, otherwise the highest-survival owned state with the lowest state id as the final tie breaker. Fragmented, refuge, altered-transformation, and emergency-council branches remain uncommitted until their candidates are genuinely materialized and packaged. The continuation ledger does not claim completion in those cases.

No documented script surface distinguishes separate people sharing one cooperative country. `is_ai = no` identifies the human-controlled country scope. It does not identify individual co-op seats. An absent player can have a successor reserved, but scripted reassignment while disconnected is not proven. Vanilla proves individual tag switches, not several simultaneous multiplayer switches or save recovery during the commit barrier.

Map return requires equal snapshot, planned, and committed player counts, unique target verification, a valid package and focus layer on every destination, a hostable owned and controlled capital, a finished successor allocation, a clean diplomacy ledger, a complete state rewrite, and a zero transition-error count. A successful current-schema map return records the exact Fallout event timeline generation, date, and arithmetic day. The missing survival-resource barrier remains a release blocker. The blackout remains active when any implemented item fails.

## Open proof obligations

- Preserve the recorded normal-map runtime observation checklist without claiming that its visual checks were performed.
- Measure entity density and strike-batch execution cost on the current map.
- Prove a structurally valid all-resolution blackout binding and complete priority over every required hardcoded popup.
- Record whether a scripted surface exists for native exclusive input, complete keyboard capture, shortcut suppression, or pause control. None was found in the documented scripted-GUI schema.
- Record that no documented literal lobby-host trigger exists. `is_global_host` is a project simulation coordinator.
- Prove runtime save-load preservation for schema-2 transaction arrays, tickets, cursors, cancellation receipts, reciprocal scope values, dispatch envelopes, and issuance receipts.
- Implement and prove candidate selection, living-world event definitions, human choice resolution, hidden AI mechanical resolution, and content-owned cleanup before setting either activation flag.
- Re-run the province-ledger audit after any map-version change.
- Measure the one-time country-state resource-rights sweep in a separately authorized runtime pass. Static proof establishes full pair coverage, not frame-time cost.
- Resolve active lend-lease cancellation, ordinary trade, intelligence, and expeditionary return before enabling map reveal. An empty lend-lease surface already has exact current-generation readback proof. Docking rights have exhaustive generation-bound inverse application proof.
- Prove multiplayer continuation across distinct human countries, cooperative seats, disconnects, and save recovery before claiming host-authoritative player handoff.
