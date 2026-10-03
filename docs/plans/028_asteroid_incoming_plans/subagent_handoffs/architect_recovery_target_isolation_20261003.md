# Event 028 recovery target isolation handoff, 2026-10-03

## Disposition and authority

Source patch implemented for parent review.
MCP lifecycle, render, comparison, and declared-scenario validation remain blocked or unresolved, so this handoff makes no package completion claim.
The parent prompt authorized the bounded recovery-pointer repair, monotonic protection setters, and exact mission localisation.
Subsequent parent messages authorized the actual localisation file, the three protection descriptions, and the narrow annexation hook plus mineral-gated achievement resets.
Baseline supplied by the parent: `f48758822`.
Other shared worktree edits were preserved.

Skills used: `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.
All 23 files under `docs/specs/028_asteroid_incoming_specs` were read.
No skill was changed.

## Files and owned changes

| File | Change |
| --- | --- |
| `common/scripted_effects/028_asteroid_incoming_recovery_effects.txt` | Country reservation, finish dispatch, terminal cleanup, native mission cancellation, invalid-pointer cleanup, mission outcomes using country variable scopes, and monotonic protection updates |
| `common/scripted_triggers/028_asteroid_incoming_triggers.txt` | Pending-project concurrency gate, country-local pointer validation, paid-project FROM match, five exact-state objective predicates, and original-target receipt check for regional recovery |
| `common/decisions/028_asteroid_incoming_decisions.txt` | Seven guarded start payments and delayed finish/cancel paths, five guarded mission outcomes |
| `common/scripted_localisation/028_asteroid_incoming_scripted_localisation.txt` | Only `GetAsteroidIncomingDecisionTargetState` target selector |
| `localisation/english/028_asteroid_impact_l_english.yml` | Target value, country project/mission blocked reason, and three protection descriptions |
| `common/on_actions/028_asteroid_incoming_on_actions.txt` | Recovery cancellation in annexed FROM, with the parent's five hold-reset statements guarded by active minerals |

The on-actions file already contained the parent's hold-reset block when ownership expanded.
That parent work is preserved and guarded, and the original-target annexation disqualifier is preserved.
The other parent-owned runtime, ideas, Air Cleanliness, CXT, shared files, assets, and workbook were not edited.

## Helper map and documentation

This handoff documents the event-owned helpers within the authorized write set.
No generic helper or central router was introduced, and no shared dynamic-effects registry was edited.

| Helper | Scope and inputs | Outputs and side effects | Call sites and defaults |
| --- | --- | --- | --- |
| `asteroid_incoming_save_recovery_target` | Selected state, with decision actor in ROOT, after action and affordability validation | Writes `ROOT.asteroid_incoming_recovery_target_state = PREV` and country flag `asteroid_incoming_recovery_project_pending` | Seven paid project start callbacks. No default target and no global target writes. Refuses invalid state, dead actor, pending project, or active mission |
| `asteroid_incoming_recovery_project_target_is_valid` | Country with pending receipt and original decision target in FROM | Read-only exact FROM match to `var:ROOT.asteroid_incoming_recovery_target_state`, live country, current control, affected non-crater state | Seven delayed project cancel/finish paths |
| `asteroid_incoming_recovery_callback_matches_target` | Country with terminal decision callback and state in FROM | Read-only absent-pointer or exact FROM match, preventing a stale callback from clearing a later reservation in another state | Seven cancel and seven remove callbacks |
| `asteroid_incoming_decision_target_pointer_is_valid` | Country with persistent state variable | Read-only control check against PREV inside the variable state scope, avoiding an unrelated outer ROOT during national refresh | Project finish, five mission cancellation paths, mission outcome helpers, target-name selector, national recovery refresh |
| `asteroid_incoming_finish_recovery_project` | Country, original state in FROM, one project-specific active receipt | Revalidates exact reservation, releases pending flag, dispatches one state action, consumes project receipt, retains pointer only if that action activates a mission | Seven project remove effects. No refund or second payment. Invalid reservation performs cleanup only |
| `asteroid_incoming_clear_recovery_target` | Country, including an annexed country scope | Clears its pointer, generic pending flag, seven project flags, five mission ready flags, five completion days, and three prepared-response commitment flags | Project cancellations, non-mission finish, mission success/failure, runtime cancellation. Idempotent. No refunds, state repair, mitigation, success grants, or foreign-country mutations |
| `asteroid_incoming_cancel_recovery_runtime` | Country | Removes all five native missions with `remove_mission`, then clears local receipts and pointer | Annexed FROM and invalid-pointer branch of existing national recovery refresh. Native removal runs no complete or timeout effect |
| Existing `asteroid_incoming_recovery_mission_success`, `asteroid_incoming_outer_mission_success`, `asteroid_incoming_regional_mission_success` | Country with valid pointer. Caller must retain matching ready receipt and revalidate its objective | Existing bounded repairs and legacy flags apply to its exact state only, followed by local cleanup | Corresponding guarded mission complete effects |
| Existing `asteroid_incoming_recovery_mission_failure` | Country | Applies existing failure pressure only when the actor still controls the valid pointer state, then local cleanup | Guarded mission cancel/timeout effects. Lost-control, invalid, or absent pointer cannot penalize another actor's state |
| Parent `asteroid_incoming_refresh_national_dust_protection` | Country, current protection marker idea and global stage | Parent-owned six compensation variables and hidden dynamic modifier | Called after filters, emergency rail protection flag, factory hardening, and transport protection. No duplicate compensation implementation |

Usage for the paid state project remains `FROM = { asteroid_incoming_save_recovery_target = yes }` before the manual debit.
The country then receives exactly one project-specific active flag.
At native delayed removal, its guarded callback calls `asteroid_incoming_finish_recovery_project = yes`.
A terminal lifecycle caller in a disappearing country uses `asteroid_incoming_cancel_recovery_runtime = yes`.

## Exact project and mission IDs

| Decision ID | Project receipt suffix | Follow-up mission |
| --- | --- | --- |
| `decision_asteroid_incoming_deploy_mobile_hospitals` | `mobile_hospitals_project_active` | `asteroid_incoming_rescue_route_mission` |
| `decision_asteroid_incoming_open_emergency_rail_corridor` | `rail_corridor_project_active` | `asteroid_incoming_rescue_route_mission` |
| `decision_asteroid_incoming_clear_unstable_debris` | `debris_project_active` | `asteroid_incoming_stabilize_damaged_zone_mission` |
| `decision_asteroid_incoming_distribute_emergency_filters` | `filters_project_active` | None |
| `decision_asteroid_incoming_rebuild_supply_spine` | `supply_spine_project_active` | `asteroid_incoming_reconnect_national_network_mission` |
| `decision_asteroid_incoming_restore_outer_ring_industry` | `outer_industry_project_active` | `asteroid_incoming_restore_outer_ring_mission` |
| `decision_asteroid_incoming_rehouse_displaced_workers` | `rehousing_project_active` | `asteroid_incoming_rebuild_regional_economy_mission` for the original target country only |

Every receipt suffix above is prefixed with `asteroid_incoming_`.
Five matching ready flags are `asteroid_incoming_rescue_route_mission_ready`, `asteroid_incoming_stabilize_zone_mission_ready`, `asteroid_incoming_network_mission_ready`, `asteroid_incoming_outer_ring_mission_ready`, and `asteroid_incoming_regional_economy_mission_ready`.
Completion-day variables are `asteroid_incoming_rescue_mission_complete_day`, `asteroid_incoming_stabilize_mission_complete_day`, `asteroid_incoming_network_mission_complete_day`, `asteroid_incoming_outer_mission_complete_day`, and `asteroid_incoming_regional_economy_mission_complete_day`.

All five mission success callbacks recheck ready receipt and exact objective before the helper and success flags.
All five cancel triggers also reject a missing ready receipt.
Rescue and network retain the existing capital railway requirement.
Regional recovery also rejects loss of `asteroid_incoming_original_target_country`.
An absent completion-day variable cannot act as a day-zero success.

## Constants and tuning

No constants, AI weights, costs, restore fractions, objective thresholds, or mission durations were changed.
Existing recovery duration constants remain rescue 150 days, stabilization 120, network 180, outer ring 270, regional economy 365, and failure pressure 90.
The existing paid project commitment remains 30 days.
Existing protection level constants remain basic 1, organized 2, and hardened 3.
The protection setters apply only upward changes to the level and corresponding visible marker, then call the parent's stage-aware compensation helper.
Filters cannot replace organized or hardened protection, and transport cannot replace hardened protection.
No new tuning table is required.

All 21 `ai_will_do` blocks in the decision source compare identically to supplied baseline commit `f48758822`, after line-ending normalization.
Availability intentionally changes while a project is pending in the acting country.
That source comparison establishes unchanged weight text, not numerical campaign selection evidence.

## Target lifecycle, cleanup, and migration

The mission target is a normal variable owned by the acting country, containing the engine state scope value.
It survives separate callbacks and events without a global event target or temporary variable.
The variable is read through `var:asteroid_incoming_recovery_target_state`.
Localisation reads `[?ROOT.asteroid_incoming_recovery_target_state.GetName]` only when the country-local pointer predicate passes.

A pending project blocks all seven state project starts in that country through the existing no-active-recovery gate.
The guard is checked in availability, custom cost, and the payment-time branch.
Other countries retain their own gates, pointers, and mission receipts.
No shared state reservation flag was added.

At finish, the callback must still belong to the reserved project, FROM must match the saved state, and the state must remain a controlled, affected, passable non-crater state.
The original action helper separately revalidates repairability and its one-time state receipt.
Invalid or already-resolved work produces no repair or mission grant.
Terminal project callbacks also check their FROM against the current pointer before calling cleanup, so an old row cannot clear a later reservation for a different state.
Once a mission begins, that pointer is retained until its terminal callback.
Success, cancellation, timeout, annexation, and invalid-target refresh release only the owning country's runtime state.

Upfront resource expenditure remains committed work.
Cancellation gives no automatic refund and no success reward.
No refund ledger or refund path was introduced, so repeated cancel/timeout paths cannot refund twice.
Prepared-response commitment flags clear at every terminal cleanup, while the already-used first-response receipt remains consumed.

Filters and the three crater-controller helpers no longer write or clear a mission target.
The two old global-target clears in parent-owned `common/scripted_effects/028_asteroid_incoming_effects.txt` remain inert legacy cleanup.
No active mission is reconstructed from the old global pointer because its country ownership cannot be established safely.
A mission with no country-local pointer cancels without a success grant.

Annexation uses the existing `on_annex` block's FROM country.
Recovery cancellation remains independent of minerals.
The five parent hold-reset statements execute only with `asteroid_incoming_minerals_active`, so a pre-impact or miss annexation creates no Event 028 hold-progress variables.
The original-target annexation disqualifier remains outside that mineral guard.

## Localisation keys

Changed keys are `asteroid_incoming.decision_target_state.value`, `asteroid_incoming_blocked_active_mission_tt`, `asteroid_incoming_dust_protection_basic_desc`, `asteroid_incoming_dust_protection_organized_desc`, and `asteroid_incoming_dust_protection_hardened_desc`.
The protection descriptions state 15, 30, and 45 percent reduction of active dust penalties and show the parent's current country fields for factory output, construction, efficiency growth, supply consumption, air missions, and weather penalty.
Signed percentage formatting preserves two decimal places, with favorable negative supply/weather compensation colored through the reverse-sign formatter.
No new icon is required.
The requirement-flags localisation file was not edited.

## Meaningful source validation

An in-memory interpreter of the actual source's supported variable, flag, country/state scope, boolean, helper, idea, and cleanup subset ran these named checks.
Unsupported source operations throw rather than silently passing.
This is source evidence and is not an HOI4 engine run.

| Scenario | Declared case and result |
| --- | --- |
| `AST_REC_RESERVE` | GER reserves state 64 and FRA state 17 independently. A second pending reservation in GER is refused. Country pointer validation also passes with an unrelated outer ROOT |
| `AST_REC_CONTROL_LOSS` | Wrong FROM and state 64 changing controller to FRA reject GER's finish predicate. GER's failure cannot apply pressure to the foreign state and cannot clear FRA's pointer |
| `AST_REC_CANCEL` | Two repeated country cleanup calls remove all five missions and GER receipts while FRA keeps its reservation |
| `AST_REC_PROTECTION` | Basic, organized, and hardened starting levels remain monotonic through transport, filters, and factory hardening, with matching marker ideas and refresh calls |
| `AST_REC_CALLBACK_COVERAGE` | All seven paid project callbacks bind before debit and guard cancellation/removal. All five success callbacks revalidate their ready receipt and exact objective |
| `AST_REC_ANNEX` | Without minerals, annex cleanup clears recovery but creates no hold-progress variables. With minerals, all five hold statements reset, original-target disqualification remains, and the annexer's reservation is preserved |
| `AST_REC_STALE_CALLBACK` | Reviewed absent-pointer/own-target/different-target predicate cases and all 14 native terminal guards. A previous row for state 64 cannot clear a later same-family project reserved for state 17 |

The interpreter does not model native scheduling, resource debit, building repair rewards, the parent's compensation calculation, game localisation rendering, or campaign hooks beyond the explicitly invoked annex effect.
Those results are not presented as engine behavior.

## MCP evidence and exact gaps

Live tools exposed source lookup, decision inspection, event inspection/render/compare, and mechanic tests.
No server health/version route was exposed for HOI4, and no native MCP task or job/helper-expansion route was used.

`hoi4.source_lookup` returned the pre-edit `asteroid_incoming_save_recovery_target` definition at `mod:common/scripted_effects/028_asteroid_incoming_recovery_effects.txt:193-198`.
Revision was `65d14d6e763e5db4d997dfaac602a126f68bacfff02cf83ddf80fbd693ff61de`.
Definition coverage was complete for that query, but reference coverage was incomplete with 17,480 unresolved indexed references.
This established the original global-pointer implementation, not lifecycle correctness.

`hoi4.decision_inspect` inventory returned `DECISION_ANALYZED_PARTIAL`, `complete = false`, and 218 unresolved definitions across the workspace.
The full 6,263,297-byte report was retrieved using verified 30,000-byte resource ranges and inspected in memory.
It contains all five country missions and all seven paid state projects.
Inventory alone does not evaluate their timing or country scopes.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb17cc0bc7a9f759e7e5e8576c17a7d53e82b43a1b0cdda93e2745649ea16fff/bce7025ee0daf4bdd555e417682088666a6c249ccffe9286227d2d08d0b8bbea/decision-ff70dfcf7976efe72d13ccd6.json`.
Initial larger range transport was truncated despite claiming its requested range.
Smaller verified ranges recovered the complete JSON.
No final cryptographic hash calculation was performed on the downloaded report.

| Route | Exact status |
| --- | --- |
| `hoi4.reference_context`, `hoi4.reference_search` | Parent reported hangs/timeouts at 600 seconds and explicitly authorized pertinent local-document fallback. Not retried here |
| `hoi4.reference_read` | Exposed, not invoked because local sections were used under the granted reference fallback |
| `hoi4.event_inspect` | Corrected narrow event selector `{ kind: "event", eventId: "chaosx.nr28.1" }`, trace with depth 3 and 30 nodes, timed out awaiting tools/call after 600s |
| `hoi4.event_render` | Same selector, targets view, depth 3 and 30 nodes, timed out awaiting tools/call after 600s |
| `hoi4.decision_inspect` declared scenario | Rescue mission, scenario `AST_RECOVERY_BASELINE`, actor GER with explicitly incomplete state, timed out awaiting tools/call after 600s. No scenario pass claimed |
| `hoi4.mechanic_test` | `AST_RECOVERY_CLEAR_COUNTRY`, repeated source-backed cleanup with seeded pointer/day/flags and cleanup assertions, timed out awaiting tools/call after 600s |
| `hoi4.event_compare` | Skipped because no graph-bearing baseline was returned by the required event routes. Structural delta evidence remains source-only |
| Probability audit | Read-only `chaosx_ai_probability_auditor`, agent `01a1002f-8381-7a53-b654-fa0b1b1dec12`, returned unchanged weight text for all seven project and five mission blocks against `f48758822`. Its probability_inspect timed out after 600s, and later decision evaluation and mission inspection remained pending. All four named probability scenarios remain unresolved |

Early rejected requests were schema probes and produced no analysis.
The corrected event selector uses `eventId`, source lookup limits are 80 lines and 20 references, and decision inspect requires declared scenarios in inspect mode.
The mechanic test fixture uses source `{ kind: "scripted_effect", id: "asteroid_incoming_clear_recovery_target" }`, schemaVersion 1.0, and typed assertions.
Unsupported assertion property names were removed before the timed-out request.
No validation error was treated as successful evidence.

### Follow-up typed decision scenarios

After the parent's request to use the current typed decision route, its live schema was read again and two inspect calls were submitted with explicit GER/FRA country scopes, FROM state 64, state 17, and controller maps.
The project source ID is `decision_asteroid_incoming_deploy_mobile_hospitals`.
The mission source ID is `asteroid_incoming_rescue_route_mission`.
Both calls use `refresh = true` and `closedFlags = true`, without candidate overrides.
GER has declared manpower 100,000, support equipment 10,000, trucks 10,000, fuel 100,000, and trains 1,000 unless the scenario changes them.
States 64 and 17 have declared infrastructure and railway levels 3, supply-node level 1, preimpact infrastructure/railway receipts 5, and the affected-state flag.
FRA has its own pointer to state 17 and pending hospital-project receipt in every case, enabling the country-isolation question.
These are declared analysis fixtures and do not describe an observed game state.

| Scenario | Fixture difference |
| --- | --- |
| `AST_REC_TWO_COUNTRIES_PENDING` | GER also has pointer 64 and pending hospital-project receipt, with states controlled by GER/FRA respectively |
| `AST_REC_OTHER_COUNTRY_PENDING` | GER has no pending project, while FRA retains its independent pointer and pending receipt |
| `AST_REC_EXHAUSTED_STOCKPILE` | GER's declared manpower, support equipment, trucks, fuel, and trains are zero |
| `AST_REC_LATE_INVALIDATION` | GER retains a pending pointer to state 64, but its controller map assigns that state to FRA |
| `AST_REC_CONTROL_LOSS` | GER retains the rescue ready flag and day-150 pointer receipt, but FRA controls state 64 |
| `AST_REC_ANNEX_CLEANUP` | GER is declared nonexistent with no ready or pointer receipt, and FRA controls both states. This inspects the post-cleanup decision state, rather than executing annexation |
| `AST_REC_NORMAL_FINISH` | GER controls pointer state 64, has rescue ready receipt and completion day 150, declares current day 150 and capital 64 |

Both requests passed argument validation, then independently returned `tool call failed for hoi4_agent_tools/hoi4.decision_inspect: timed out awaiting tools/call after 600s`.
Neither returned an analysis artifact, scenario hash, or source revision.
All seven follow-up scenarios therefore remain unresolved in MCP evidence.
Unsupported stockpile aliases, global-day interpretation, state-pointer typing, and native lifecycle execution must remain unresolved if the returned report cannot bind them.
No elapsed wait or schema acceptance is treated as a scenario pass.

## Local reference citations

The parent's later update reports successful idea reference_context and a pending section_read.
That separate parent result does not establish that this worker's decision/reference context requests or engine validation succeeded.
The local citation evidence below remains the source fallback authorized for this repair.

All paths below are Windows files.
Vanilla documentation is the primary syntax authority, with the offline wiki consulted in parallel.
No Paradox wiki web request was made.

| Source | Read spans or exact precedent | SHA-256 |
| --- | --- | --- |
| `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 264-327 event targets, 426-479 persistent variables and var scopes | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 254-271 ROOT, FROM, PREV and var scopes | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` | 336-356 delayed decision cancellation, 461-478 mission lifecycle | `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162` |
| `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 701-712 variable effects | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 569-573 has_variable and check_variable | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| `paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 185-212 percentage/sign formatting, 529-544 variable namespaces, 670-691 scripted selectors | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| `paradox_wiki\On actions - Hearts of Iron 4 Wiki.md` | 253-260 annex scope contract, 363-379 example | `6822ADC85A374A1C1364F2DEF6F32C6D66DA9FB0280319DDD6AF4B84B33D882A` |
| `documentation\effects_documentation.md` | 661-670 activate_mission, 2773-2783 clear_variable, 6083-6092 remove_mission, 7888-7909 set_variable | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| `documentation\triggers_documentation.md` | 5006-5013 has_variable | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| `documentation\script_concept_documentation.md` | 216-245 script constants | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| `common\script_constants\documentation.md` | Full schema and examples | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| `common\decisions\_documentation.md` | Full native actor/FROM and evaluation cadence contract | `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019` |
| `common\scripted_effects\ITA_scripted_effects.txt` | 1941-1967, country variable stores PREV state scope | `FF43BBAC27B77AA276F90CB7FA925ABA52DCDD1A5FCCE8ABE739D33A64AA23ED` |
| `common\decisions\AST.txt` | 1-86, delayed action cancellation and mission cancel_effect | `AAD50DA745F5A93C5F7470E06ED990A49A5416C81810849C8A2312600E81F4F2` |
| `common\on_actions\00_on_actions.txt` | 1611-1637, ROOT winner and FROM annexed | `52A751456F1774AD5001C86D41D4E46494F751D79B6C224B6CD4C0EEBB615EB9` |
| `localisation\english\aat_focus_l_english.yml` | 604, country variable GetName precedent | `4C71795443A0A408453A048B5ECACA2D15DCEE79B1D21013588F4F604D541F26` |

Vanilla-relative rows resolve under `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\`.
Wiki-relative rows resolve under the Chaos Redux repository.
Existing Event 020 state-variable scope patterns were inspected in `020_black_plague_response_action_effects.txt:1471-1560` and `020_black_plague_shared_response_triggers.txt:159-198`.
The shared `chaosx_dynamic_effects.txt` and matching markdown registry were inspected before adding event-owned lifecycle helpers.
None supplied an existing matching project reservation API.

## Unresolved requirements and risks

Final reviewed source SHA-256 identities:

| Owned source | SHA-256 |
| --- | --- |
| Recovery effects | `74CE4D5EA35D22894713B88AFA32C97E9FA1F6C1C2BB000035A0AC6E7CB1C34F` |
| Triggers | `EFA22ACB10085504B65E1C7DF95E47931E2B980D9A3780312CE0B65F885EC08F` |
| Decisions | `518D44DB1E6ACE74CD28070D2570134070267869F71394B441B63E4F39619ACC` |
| Scripted localisation | `BDAB2A007C10AD56103075828165BA3CD6A9BF438698FBDAA8F2003694F24A44` |
| English localisation | `D8F775F806E99FE79BCBECAFE0674BC93934A05D7848E6456D59BEA5AE821B4F` |
| On actions | `A3030B946719966CBD7329DEC2786D7F40FFE984E5BF88BA6732CADDBC614CDA` |

- The four timed-out lifecycle/render/scenario routes leave engine-facing MCP validation unresolved. Source checks are not equivalent evidence.
- Native ordering when the completion-day threshold and mission timeout coincide remains unverified. The existing duration model was preserved without tuning changes.
- No native save/reload, annexation callback timing, delayed decision removal timing, cost debit, repair reward, or localisation render was observed.
- The parent still owns final event integration, event documentation, catalog alignment, compensation arithmetic evidence, and package review.
- No dedicated GUI, asset, workbook, AI weight, CXT, or broad on-action redesign was added.
- No accepted recovery mechanic was simplified in this patch. The explicitly authorized local-reference fallback was used for unavailable reference retrieval. Required MCP results are reported blocked rather than replaced.
- No commit was created while required validation remains unresolved and parent review is pending. The parent must isolate these changes from its own on-actions and other shared worktree work before committing a completed plan.

The local source patch is ready for parent review with the limits above.
