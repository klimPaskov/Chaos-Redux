# Current famine and migration mapmode projection audit

Date: 2026-10-03.
Disposition: implemented narrow presentation corrections, with mandatory MCP map execution evidence blocked.
Acceptance basis: the parent authorized endpoint selector corrections and expanded bounded ownership to corridor terminal-operation provenance, live/terminal display guards, paired helper documentation, and one tooltip label.
The parent reviewed the source diffs and accepted their scope and behavior before this handoff.
This is not a completion claim for the full famine and migration system.

## Completed corrections and files

| File | Change |
| --- | --- |
| `common/map_modes/chaosx_state_map_modes.txt` | Migration live corridor offer/operation and preparation branches require an evacuation operation. Failed terminal borders require a recorded terminal evacuation operation. |
| `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` | Origin-role text recognizes positive outstanding flight population as well as pressure. Destination-role text recognizes positive reception load. Migration preparation, route, generation, live corridor and terminal corridor text require evacuation provenance. Owner/controller detail remains restricted and includes proven terminal evacuation history. Zero reception initialization alone no longer selects exact detail. |
| `common/scripted_effects/humanitarian_corridor_effects.txt` | Preparation clears the previous terminal status/operation pair. Cleanup snapshots a recognized live evacuation/relief operation beside terminal status before clearing live fields. |
| `common/scripted_effects/humanitarian_corridor_effects.md` | Added Mapmode operation provenance contract, defaults, lifecycle, side effects and relief example. |
| `localisation/english/chaosx_map_modes_l_english.yml` | Existing key `migration_state_map_mode_detail_authorized` labels the two counters `Flight pressure` and `Awaiting departure`. Existing key `migration_state_map_mode_corridor_generation_recorded` says `Current evacuation corridor` without exposing the internal generation integer. |
| `docs/plans/famine_and_migration_system_plans/subagent_handoffs/current_mapmode_projection_audit_20261003.md` | This handoff. |

No famine or migration core file, population formula, transfer primitive, AI weight, GUI layout, asset, category, event ID or pacing surface was edited.
There are still exactly three canonical values per mechanic and the two independent mapmode IDs.
No mechanical simplification, substitute route, placeholder asset, world scan, third mapmode, or compatibility alias was introduced.
No commit was made, as required by the parent.

## Proven defects and before/after behavior

1. The main exodus role already accepted positive flight pressure or positive `migration_state_flight_population`, but the origin endpoint selector accepted only pressure.
An active registered flight obligation with zero current pressure could therefore show an exodus fill and `Origin unknown` together.
`GetMigrationStateMapModeOriginRole` now uses the same positive pressure-or-flight-population predicate under the existing displacement flag.

2. Reception host text recognized a positive state reception ledger, but the destination endpoint selector recognized only return and resettlement.
A proven arrival could show `Current host` with `Destination unknown`.
`GetMigrationStateMapModeDestinationRole` now includes the same active-reception and positive-state-load predicate.
Primary role priority is unchanged.

3. The migration mapmode's corridor top-layer branches and corridor selectors accepted relief operations.
Preparation could also display relief as migration preparation.
All those migration consumers now require evacuation operation provenance.
Famine continues to consume famine-owned route and delivered-relief receipts, rather than acquiring migration ledgers.

4. Cleanup clears the live operation, so guarding terminal status with that live field would discard the intended historical migration display.
The corridor owner now snapshots the terminal operation only when the live operation is a recognized evacuation or relief token.
An unproven operation defaults absent and cannot qualify migration terminal display.
Preparation resets the previous pair so an old failure cannot override a later live offer.

5. The authorized-detail selector accepted the existence of `migration_state_reception_load` even when it was initialized to zero.
The initializer writes this zero ledger at `migration_core_effects.txt:1660-1665`.
A relief-only state with that default could select unrelated exact migration detail.
The detail context now requires positive load or another existing genuine migration context.
The owner/controller authorization gate is unchanged.
A recognized terminal evacuation pair can select owner/controller detail after live corridor fields are cleared so the terminal border retains an explanation.

6. `migration_state_flight_population` is an outstanding registered flight obligation.
`migration_apply_flight_request` adds the requested amount at `migration_core_effects.txt:748-750`, and `civilian_transfer_reconcile_obligations` subtracts the settled amount at `civilian_transfer_effects.txt:562-571`.
The tooltip label `Departed` incorrectly implied completed physical movement.
Its existing formatted variable and key remain the same, with the label `Awaiting departure`.
The caller is `GetMigrationStateMapModeDetail` through `migration_state_map_mode_tooltip_delayed` at English mapmode localisation lines 153 and 155.
The parent's localisation audit also accepted `Flight pressure` for the first counter because it describes pressure rather than a second waiting population.
The corridor generation key now says `Current evacuation corridor`, with status still shown separately, so a prepared or pending operation is not described as an open route.
Removing the internal receipt integer from this display is a player-facing wording correction, not a mechanic simplification.

## Current producer, scope and cleanup evidence

The August 26 claim that reception, overcrowding and return setters were absent is rejected.
Current `migration_refresh_reception_context` sets or clears reception and overcrowding from state load and owner-country load/capacity at `migration_core_effects.txt:1004-1039`.
`migration_apply_reception_delta` updates both state and OWNER country ledgers at `:1065-1100`.
`migration_record_state_return_projection` writes the return amount/flag at `:1133-1148`.
`migration_record_transfer_projection` records measured origin/debit/share and destination credit/share at `:826-869`.
Its sole current transfer call is behind cohort-update and exact-finalizer validation at `civilian_transfer_effects.txt:861-875`.

Both mapmodes evaluate state layers through FROM.
The installed mapmode documentation explicitly describes the initial scope as the player and FROM as the rendered state for `type = state`.
Both public detail keys show qualitative stage or role only.
Exact detail requires state owner or controller equal to ROOT.
Migration exact state load remains distinct from `FROM.owner` country totals and capacity, matching the OWNER-based reception accounting rather than CONTROLLER.
Control changes do not change that ledger ownership contract.

The migration main-fill/role priority remains trapped, overcrowded, organized evacuation, exodus, preparation, return readiness, returned outcome, resettlement, transit, reception.
The state defaults in `migration_initialize_state` are zero-only and do not create role flags.
Guarded retirement at `migration_cleanup_state_registration`, `:2047-2081`, clears role flags and latest transfer projections only when migration obligations are absent.
No retirement path was changed here.
Country retirement preserves historical integration/resettlement totals and removes only live capacity/selection state at `:605-650`.
Famine initialization at `famine_core_effects.txt:795-856` creates stable/zero defaults, and recovery retirement at `:1824-1860` uses the famine-owned cleanup.
No missing producer or unauthorized core correction was inferred from a getter alone.

All 15 migration mapmode selectors have consumers in the public/authorized mapmode localisation family.
The owner-national integration fallback in `GetMigrationStateMapModeFlowIdentity` explicitly describes national integration with destination unknown and does not claim a state transfer.
No dead-selector removal was warranted.

## Helper map and tuning

| Helper/selector | Scope | Inputs | Output and side effects | Call sites |
| --- | --- | --- | --- | --- |
| `humanitarian_corridor_prepare_contract` | Origin state | Existing validated preparation inputs | Clears last terminal status/operation before starting the new contract. No added transaction effects. | Existing corridor preparation owners. |
| `humanitarian_corridor_cleanup` | Origin state | Live status and recognized live operation | Writes `humanitarian_corridor_last_terminal_operation` beside last status. Missing/invalid operation clears previous provenance for a new status. Existing live cleanup remains unchanged. | Existing finalize, expiry, rejection, invalidation and attack cleanup owners. |
| `GetMigrationStateMapModeOriginRole` | State | Displacement flag and positive pressure or reserved flight amount, plus existing trapped/preparation/mission flags | Existing recorded/unproven key. No mutation. | Authorized movement line. |
| `GetMigrationStateMapModeDestinationRole` | State | Positive reception, return or resettlement ledger with its existing role flag | Existing recorded/unproven key. No mutation. | Authorized movement line. |
| Migration preparation/route/generation/corridor/detail selectors and mapmode branches | State | Live evacuation operation, or proven terminal evacuation pair | Existing display branches, with public/authorized restriction retained. No gameplay mutation. | Existing mapmode fill, border and delayed tooltip. |

No helper name, constants category, tuning value, ratio, threshold, or duration was added or changed.
The new normal variable is `humanitarian_corridor_last_terminal_operation`, containing only an existing operation constant.
No event target, global target, global array, or scheduler was added.
Existing chain-local target and sparse-runtime contracts are unchanged.
There is no broad helper migration.
The only owner-to-consumer migration is the terminal operation snapshot consumed by existing mapmode presentation.

### Terminal lifecycle source trace

| Sequence | Expected source result |
| --- | --- |
| Evacuation cleanup with recognized live status | Snapshot evacuation, then clear live operation and status. Migration terminal presentation may qualify. |
| Relief cleanup with recognized live status | Snapshot relief, then clear live operation and status. Migration terminal presentation fails closed. |
| New status with missing/invalid operation | Clear older operation snapshot, retain new status without proven operation. Migration terminal presentation fails closed. |
| Second cleanup after terminal cleanup | Live status is absent, so the snapshot block is skipped and the existing pair remains. |
| New preparation after any terminal pair | Clear both terminal fields before setting the new live operation. An old failed border cannot override the new offer. |

The existing end of `humanitarian_corridor_cleanup` clears `humanitarian_corridor_status` at current line 1049.
The concern that a second cleanup could erase the new snapshot by copying a surviving live status is therefore rejected against the current source.
The patch did not alter status clearing or transactional completion conditions.

## Source-based scenario validation

The final selectors were tokenized from the actual source and their declared trigger predicates were evaluated with a small read-only in-memory interpreter.
Unsupported predicates would stop the check rather than being treated as true.
This is source Boolean evidence, not HOI4 execution or MCP dynamic map rendering.
No test script or report generator was installed.

The 31-case endpoint/corridor matrix used these exact inputs and expected outcomes.
All unspecified flags and variables are absent.
The endpoint cases set reception, flight pressure and flight-population variables to zero unless overridden, except the retired case which has no variables.

| Case | Input | Expected origin endpoint | Expected destination endpoint |
| --- | --- | --- | --- |
| pressure_only | displacement active, flight pressure 100 | recorded | unproven |
| reserved_flight_only | displacement active, state flight population 100 | recorded | unproven |
| reception_only | reception active, state reception load 100 | unproven | recorded |
| reception_resettlement_overlap | reception/resettlement active, reception load 100, resettled population 50 | unproven | recorded |
| zero_initialized | no flags, three zero ledgers | unproven | unproven |
| retired | no flags or ledgers | unproven | unproven |

The 10 live corridor cases are the Cartesian product of the five status rows below with live operation evacuation=1 or relief=2.

| Status/value | Required live state flag | Evacuation output | Relief output |
| --- | --- | --- | --- |
| prepared=1 | preparation_pending | corridor_prepared | corridor_none |
| offer_pending=2 | offer_pending | corridor_offer_pending | corridor_none |
| accepted=3 | response_accepted | corridor_accepted | corridor_none |
| operation_pending=4 | operation_pending | corridor_operation_pending | corridor_none |
| mission_active=5 | mission_active | corridor_mission_active | corridor_none |

Each live flag above has the prefix `humanitarian_corridor_`.
Each output has the prefix `migration_state_map_mode_`.

The 15 terminal cases are the Cartesian product of completed=6, rejected=7, expired=8, invalidated=9, disqualified=10 with terminal operation absent, evacuation=1, or relief=2.
They have no live flags/status/operation.
Only terminal evacuation selects the corresponding `migration_state_map_mode_corridor_<status>` key.
Absent/relief provenance selects `migration_state_map_mode_corridor_none` for every status.

Ten additional final-source cases checked overlapping primary role and disclosure:

| Case | Expected result |
| --- | --- |
| Resettlement and reception overlap, positive ledgers | Main role remains resettlement. |
| Reception active/load 100, owner viewer | Authorized detail. |
| Reception active/load 100, controller viewer | Authorized detail. |
| Reception active/load 100, unrelated viewer | Public detail. |
| Owner viewer, reception-load zero default only | Public detail. |
| Owner viewer, relief contract only plus reception-load zero | Public detail. |
| Owner viewer, rejected evacuation terminal pair | Authorized detail. |
| Unrelated viewer, same terminal pair | Public detail. |
| Owner viewer, rejected relief terminal pair | Public detail. |
| Owner viewer, rejected terminal status without operation provenance | Public detail. |

All 41 final-source selector cases matched the expected keys.
No cost, balance, weight, population or reception formula was evaluated or changed by this matrix.

## Mandatory MCP attempts and exact limits

The live tool inventory exposes `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.map_inspect`, `hoi4.map_render`, `hoi4.mechanic_test`, and `hoi4.scenario_test`.
No `hoi4.script_validate` route was exposed in the connected inventory.

The initial parallel map/reference batch used map context, `scripted map modes` reference search and `map_inspect({lookupOnly:true,stateIds:[64],includeOverview:false})`.
That orchestration remained pending without delivered results and was terminated after prolonged waiting.
This is recorded as an abandoned pending request, not a returned timeout or successful inspection.

The narrower retry `map_inspect({lookupOnly:true,query:"64",queryLimit:1,includeOverview:false})` returned the exact error:

```text
tool call error: tool call failed for hoi4_agent_tools/hoi4.map_inspect
Caused by: timed out awaiting tools/call after 600s
```

The focused source lookup for `GetMigrationStateMapModeOriginRole` with `kind = scripted_localisation` returned `status=ok`, `code=OK`, zero definitions, zero artifacts, and revision `bcb661e2c2c5f10ef154908d7b9310e2b6b590cde713430cac3aa4a4c514e430`.
It is an index lookup miss for that kind, not proof that the getter is absent.
The source definition was read directly.
A retry without a kind, a narrower localisation context, and a one-hit installed-documentation search remained pending without delivered results and were terminated at the parent's handoff boundary.
These are abandoned pending requests, not returned timeout errors or successful reference retrievals.
No returned reference citation ID was available to call `reference_read`, so the pertinent local sections were read and hashed directly.
No MCP source revision or artifact is invented for those pending calls.

Live input validation confirms that `mechanic_test` accepts only effect or advance_days steps.
An effect source requires `kind` in scripted_effect/event_option/decision/focus_reward and an `id`, not path/identifier.
Scenario state is a typed record map, not a flat variables object.
Assertions require supported discriminators such as equals/conservation/cleanup rather than a variable discriminator.
`scenario_test` accepts mechanic/package/tool domains, not a scripted_localisation domain.
These requests were rejected during input validation and produced no execution artifact.
Do not reuse old flat scenario-state fixtures as if they satisfy the current route.
A full typed fixture must be confirmed through the connected schema before any cleanup execution claim.

The exposed map-render layer enum contains province/state/strategic-region/terrain/continent/owner/controller/cores/claims/coast.
It does not contain a custom scripted-mapmode layer or a tooltip execution option.
No direct scripted-localisation execution route was exposed.
These capability limits and the returned map timeout leave custom state colors, dynamic tooltips, selected button behavior and live consumer evidence unresolved.
No GUI layout changed, so old static button evidence was not regenerated or represented as dynamic proof.
No game was launched and no logs were read.

## References read directly

Paths below are relative to the mod root unless prefixed with the installed-game root.
The installed-game root is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.

| Source | Read span | SHA-256 |
| --- | --- | --- |
| Installed `common\map_modes\documentation.md` | 1-101, especially 34-43 and 90-96 | FE0A32E55F8F409DF104C9F386F607767D795193046E1DE509FAC75A46EC6392 |
| Installed `documentation\triggers_documentation.md` | 2110-2138 and 5006-5014 | 7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29 |
| Installed `documentation\effects_documentation.md` | 2773-2783 and 7888-7910 | 2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF |
| Installed `common\scripted_localisation\WTT_infiltration_localisation.txt` | 1-70, state-local first-match/default precedent | 57E654F0AEAB237F36BCE220BC6BE2F15DE903B3696F68FC48CE7FDDD2064B39 |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 534-536 and 656-689 | 1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064 |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 255-267, ROOT/THIS/PREV/FROM | 18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49 |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 436-450, normal/temporary variable scope | 62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4 |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 704-726, variable set/clear | 997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 569-589, variable existence/comparison | ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06 |

The parent-named source-of-truth map, completion report, mapmode validation, August 26 mapmode/completion/replay handoffs, coding prompt and prepared surface map were read.
The actual prepared file is `docs/specs/famine_and_migration_system_specs/famine_and_migration_system_implementation_surface_map.md`.
Old handoffs are under `subagent_handoffs\`, and the mapmode definitions live in the shared `chaosx_state_map_modes.txt` file.
Initial shortened path assumptions were corrected before any absence conclusion was accepted.

## Final source identities

| File | SHA-256 at handoff preparation |
| --- | --- |
| `common/map_modes/chaosx_state_map_modes.txt` | CA8FAC1EB0048319189BAFC43568ABE11A2FA0ED30B62FB2C8611A052B69A888 |
| `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` | F50E68EF4D157709B333207A8290AF0A440BA94353B7FA63C4CE406C1F539329 |
| `common/scripted_effects/humanitarian_corridor_effects.txt` | 7FC7A1C0CFB850830D6EA87CDBD45765AE58A1193B7C86263DC8D3D85EAB8568 |
| `common/scripted_effects/humanitarian_corridor_effects.md` | 3803B1AF89467B46AFDEF5782EF5FA3F6D9566D12C6AB6620C732F59378B6508 |
| `localisation/english/chaosx_map_modes_l_english.yml` | 1943DACAE6526EB7B707CF31624CBD06D19B42920F219B1D48FACADA60379AE6 |

## Parent review and remaining work

The source-level scope/role/provenance corrections are implemented and documented.
Mandatory dynamic map/tooltip execution remains blocked by unavailable route capability and a returned 600-second map timeout.
MCP effect execution was not claimed from rejected or pending requests.
The parent owns final diff review, localisation/privacy audit, integration and shared-tree commit.
The user/orchestrator owns live HOI4 consumer validation.
The full system remains incomplete according to its existing completion report and external-owner blockers.

Skills used: chaos-redux-events, chaos-redux-subagents and chaos-redux-state-ledgers.
No skill was created or updated by this bounded audit.
