# Event 028 completion audit, 2026-10-06

## Scope and authority

This is a read-only audit by `chaosx_event_completion_auditor` for the Event 028 parent.
The only file written by this auditor is this handoff.
No gameplay, shared UI, assets, workbook, CSV, Git index, or commits were changed, and the game was not launched.
The shared tree was changing during inspection, so the citations below describe the observed sources and the parent must bind its final acceptance to its final source revision.

Inputs were `AGENTS.md`, `C:\Users\klimp\Videos\chaos_redux_trailer\records\cx\phase2_history\028.md`, `C:\Users\klimp\Videos\chaos_redux_trailer\records\cx\inbox\028.txt`, the current Event 028 source, its source specification index and Parts 3, 5, and 8, its tuning and integration definitions, and the existing completion, capital, presentation, province-damage, resume, and agent-decision records.
Skills applied were `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, and the shared-window evidence rules of `chaos-redux-scripted-gui`.
Recovery, weighted logic, and asset production remain with the other assigned auditors.
The parent owns the priority-1 forecast-news repetition and super-event serialization repair.
No broad expansion is recommended by this handoff.

## Completion by surface

| Surface | Status | Evidence and limit |
| --- | --- | --- |
| One strongest footprint profile | Implemented in source | `028_asteroid_incoming_effects.txt:174-267` appends one row per state, replaces only with a higher profile, and uses the shorter ring only for an equal profile. The runtime applies states through one transaction-time state iterator. |
| Unit strength and organisation damage | Implemented in source, native outcome unverified | Runtime helper `asteroid_incoming_damage_units_in_state` uses the documented `org_damage`, `str_damage`, `ratio`, `army`, `navy`, and `state` fields under a supported STATE scope. It is called once from the guarded strongest-profile application before aggregation and reports. |
| Persistent scientific crater profiles | Implemented in source | `asteroid_incoming_assign_crater_site_profile` rolls only when its state variable is absent. The main centre and committed fragment centres call it. No reset of that profile variable was found in the reviewed transaction cleanup. Random weights require the separate probability auditor. |
| Population and Deaths | Implemented in source, native receipt unverified | Effects `asteroid_incoming_apply_population_receipt:496-563` reads `state_population_k`, converts to people, invokes the shared population-loss contract, then records the observed before/after difference. The earlier 2.147-million ordinary-variable claim is incorrect. |
| Owner/controller incident aggregation | Implemented in source | Effects `asteroid_incoming_aggregate_current_state:1449-1519` sends the single measured state loss to the owner, and to the controller only when distinct. The state-aggregated flag prevents a second addition. Global deaths are accumulated once per physical state, rather than by summing both country copies. |
| Opening snapshot and impact evolution toggles | Implemented in source | Entry `.1` captures both thresholds once. `asteroid_incoming_choose_fragment_sites` rechecks type 2801's disabled flag at impact. Resolver `.4` rechecks type 2802's disabled flag and requires committed fragments. A miss never reaches footprint application or evolution logging. |
| Locked resolver and orphan watchdog | Implemented in source, native scheduling unverified | Both chooser and locked target receive `.4`; the completed/resolution-started flags make a second callback inert. The global-host monthly achievement hook calls `asteroid_incoming_resolve_orphaned_transaction` outside its impact/achievement guard, so it can resolve a lock whose two callbacks were lost. |
| Capital fallback | Implemented policy, native move unverified | Capital helper selects surviving settled territory, then controlled owned territory, any owned territory, then controlled territory. It verifies `set_capital` by reading `capital_scope`. If no move succeeds, the country remains at the crater and receives the full government-dislocation burden. The locked coordinates remain unchanged. |
| Buildings and main-crater clearance | Partial and blocked | The observed general helper still uses state-only `remove_building` for provincial types. The parent has accepted a bounded cohort adapter during this audit, but its implementation and final review are separate from the earlier source claims. Railway-network destruction and queued construction/project cancellation remain distinct blockers. |
| Registration, default enable, event logs, and evolution previews | Implemented in source, shared-window visual proof missing | ID 28 is in `global.major_events`, the prefire dispatcher, automatic availability, and the reworked default-enabled allowlist. `chaosx_events_log_effects.txt:828-829` binds the opening history sequence and `2884-2892` adds both evolution previews. Scripted localisation has all four outcome rows and both evolution names/details. Old missing-registration/default/log claims are stale. |
| CXT extension | Implemented in source | The modifier-free carrier matches the idempotent `_apply` effect. Startup registers through one bounded country. The tag-specific daily fallback calls `chaosx_test_country_sync_registered_content`, whose current shared body only sets the pending flag at `chaosx_test_country_effects.txt:483-485`. It grants no periodic fixture content. |
| Nuclear-system separation | Partial | State markers and the Event 028 visual guard exist, but the tracked Event 042 `on_nuke_drop` hook still lacks the matching exclusion in the source observed by this audit. |
| Parchment text | Source audit passed, visual proof absent | The prescribed colour checker returned zero hits. A broader getter and localisation-reference closure is recorded below because `--event 028` alone does not include the shared news file. |
| Assets, recovery balance, catalog, super-event delivery | Outside this bounded pass | Their assigned owner evidence must be incorporated by the parent. This handoff does not imply those surfaces are complete. |

## Concrete defects and blockers

### B01. Provincial building damage remains incomplete in the observed general helper

`common\scripted_effects\028_asteroid_incoming_effects.txt:592-608` calls `remove_building` with an explicit state and no province.
It is also used for provincial forts, naval bases, facilities, camps, landmarks, canals, dams, and supply buildings.
Installed `documentation\effects_documentation.md:5838-5873` distinguishes state and province targeting and explicitly states at 5869-5871 that province buildings are not recursively found without province targeting.
The existing `province_damage_capabilities_20261004.md:13-17,25-28` already records this unresolved adapter and does not claim implementation.

The extra main-centre helper zeroes only naval bases, land forts, and coastal forts with all-province setters.
Its state-only `damage_building` calls for supply nodes and railways do not prove destruction of the entire network.
Installed effects documentation at 3412-3413 says that a state-only provincial-building damage search selects the first matching province.
Reading a state `building_level@type` before and after does not establish a sum over provinces because installed `dynamic_variables_documentation.md:1096-1103` leaves the provincial aggregation semantics unspecified.
Actual level receipts and destruction-derived dust therefore remain unverified for provincial types.

The parent explicitly accepted during this audit an ascending exact-original-level cohort adapter for ordinary provincial types, with main-centre zeroing and per-province rounded losses.
Offline Effects wiki 3615 supports a province selector whose inner level comparison is below, at, or above the existing level.
For nonnegative destruction fraction d no greater than 1, `L - round(L*d)` cannot raise a processed province into any later, larger original-level cohort.
This gives a valid host arithmetic proof of single processing, conditional on exact native equality and all-match setter semantics.
Per-province rounded loss differs from rounding a state total, for example four level-1 forts at d=0.225 lose zero in the cohort interpretation, compared with one level when rounding their aggregate.
The parent must record that severity interpretation under inbox G6 and verify the actual setter and readback behaviour.

### B02. Railways require separate network treatment

The current installed and mod building inventory contains 63 real building types, exactly matching the 63 selected-building tokens in the Event 028 helper.
There are 43 provincial and 20 state types.
Only `bunker`, `coastal_bunker`, and `naval_base` have provincial cap 10, while the other 40 declarations have cap 1.
The excluded 12 spawn-point records are entity placements rather than building types.

`rail_way` is an exception to using this provincial cap as a cohort bound.
Installed `common\buildings\00_buildings.txt:115-123` declares `province_max = 1`, while installed `common\defines\00_defines.lua:4263` sets `MAX_RAILWAY_LEVEL = 5`, and offline Building modding 334 lists railway level 5.
Building modding 362 explicitly warns that normal building operations do not all apply to railways and supply nodes and that ordinary construction or other building-related effects can crash.
Installed `build_railway` at effects documentation 2535-2570 is additive and supplies no documented destructive operation.
The project's existing `fallout_consolidated_effects.txt:43317-43324` rail setter is a source precedent, not native evidence of network removal.
No narrow documented alternative for exact railway graph destruction or loss counting was established in this audit.
Do not treat a cap-1 provincial setter as proof that a level-5 railway edge was destroyed.

### B03. Queue and active-project cleanup is a disclosed substitute

Part 3 requires incompatible state projects to be cleared or invalidated.
The agent-decision record at 170-174 substitutes wasteland slots and minus 100 percent construction speed for a construction purge, and explicitly leaves native behaviour unverified.
No documented construction cancellation or special-project abort effect was found in the installed effect registry search.
Suppression can keep a queue dormant without deleting it and does not establish active facility-project cleanup.
This remains blocked pending an exact supported API, integration evidence, or an explicitly recorded final disposition of that requirement.
The parent has confirmed that it will not describe suppression as purging queues.

### B04. Tracked Event 042 still counts the asteroid visual as a nuclear achievement input

`common\on_actions\042_equipment_from_heavens_on_actions.txt:22-28` checks only `ROOT.efh_ach_nuclear_active` before invoking the nuclear achievement helper.
It has no `FROM = { NOT = { has_state_flag = asteroid_incoming_visual_strike_state } }` exclusion and no visual-active guard.
`git ls-files` confirms that this file is tracked, so the previous untracked-file restriction is stale.
A marked Event 028 main or fragment visual can satisfy this hook when its launcher holds the Event 042 route flag.
The Event 042 owner or parent must apply and verify the bounded marker exclusion.
This auditor made no cross-owner edits.

### B05. Source claims exceed the current validation evidence

The hidden-event scheduling, late-annexation behaviour, native unit ratios, capital fallback acceptance, provincial getter semantics, complete railway removal, project/queue invalidation, and final shared-log layout have not been observed by this auditor in the engine.
The fresh focused event routes deliberately exclude helpers and lifecycle projections.
Their `missing_helper` nodes represent this boundary and are not evidence that the source helpers are absent.
Shared Event Log, Event Details, Settings, and super-event windows do not become Event 028-owned GUIs merely because Event 028 appears in them.
No `chaosx_event_ui_worker` handoff is required for those shared surfaces, but their missing matching state/resolution/hierarchy/click-region render evidence still prevents visual completion claims.

## Verification of prior claims

The unit-damage field names and STATE call scope are valid according to installed effects documentation 3417-3438 and the offline Effects wiki 365.
All seven strength and organisation pairs live under the `fixed_point` schema at constants 470-490 and decline through each main or fragment ring.
The main pair is 0.75/0.95, then 0.45/0.75, 0.25/0.50, and 0.08/0.25.
Fragments use 0.35/0.65, 0.20/0.40, and 0.05/0.20.
The helper applies navies only at the main centre and catastrophic ring, with all armies in the selected state eligible regardless of country.
The accepted `launch_nuke` visual can cause additional native province damage, as the agent-decision record explicitly discloses, so these ratios are the script pass rather than promised final combined losses.

The three crater profile ids and their integer weights are correctly defined under the `int` schema at constants 239-251.
Surveyed marker variants and profile-specific research categories exist in the crater helper.
There is no new armour change in those flavour markers.
Probability and asset proof for the profile family remain with the assigned specialists.

The takeover review's assertion that ordinary variables overflow around 2.147 million is rejected.
Offline Data structures 427 defines ordinary variables up to approximately 2.147 billion, while 1485,1591,1596,1689 describe the earlier overflow of deprecated dynamic manpower/population getters.
Event 028 reads `state_population_k` rather than the deprecated people getter before converting to an ordinary variable.
A 3-million-person state therefore does not exhibit the alleged ordinary-variable overflow merely because its value is expressed in people.
Truly exceeding the 2.147-billion ordinary-variable range remains a real boundary, but no current Event 028 scenario above that bound was supplied or established here.

Opening thresholds and impact toggles match the explicit accepted policy in `agent_decisions_2026-10-04.md:135-140`.
At impact, disabling Fragmentation prevents both evolved packages, while disabling Minerals leaves enabled fragmentation intact and suppresses mineral activation.
Enabling a threshold-ineligible evolution during the lock does not create a new opening snapshot.
The monthly watchdog is called by `asteroid_incoming_update_achievements` before its impact-only branch, and the global host invokes that hook even when the Chaos Meter is disabled.
The capital no-alternative case has a recorded policy at agent-decision 159-165 and an implemented failure burden, so old F02's missing-policy statement is stale.

## G1, G7, and force-trigger applicability

The prescribed command `python C:\Users\klimp\Videos\chaos_redux_trailer\tools\report_colour_audit.py --event 028` returned `total keys with colour: 0`.
The audit script filters event filenames by the supplied prefix, so this invocation alone does not inspect Event 028 news in the shared news file.
An additional read-only closure followed scripted `Get*` substitutions and `$localisation_key$` references from report/title/description roots.
Its final full-news result is recorded in the evidence follow-up below.
Permitted colours on dark decision, option, tooltip, and log consumers are not parchment defects unless a parchment getter reaches them.

The literal inbox G7 defines the MCP GUI scenario shape, including `scenario.id`, `windowName`, and explicit resolutions.
G8 requires mutually exclusive visibility flags to be declared explicitly rather than leaving unknown flags visible.
Neither rule authorizes inventing a new event-owned UI or equates a source row-height check with a successful render.

Force-trigger applicability is a separate issue in the inbox's 2026-10-04 live board finding.
The entry and reopened board use the same persisted `asteroid_incoming_board_ready` flag for description and options, and the source distinguishes an already locked or resolved chain from a target-pool failure.
The event disqualifies achievements for manual/force launches.
The global fire-once transaction gates should not be removed to permit a second physical disaster from a repeated debug firing.
The parent is supplying the matching locked/resolved plain descriptions during this audit.

## Accepted-plan dispositions and stale records

| Record or requirement | Disposition supported by current evidence |
| --- | --- |
| F02 late-capital-loss policy | Implemented in source with native move/failure limits recorded. |
| F04 opening thresholds and impact toggles | Implemented in source according to the agent-decision policy. |
| F19 event history, Details, and evolution previews | Implemented in source, visual acceptance unresolved. |
| Round-3 unit-damage and persistent-profile requirements | Implemented in source, native outcomes and specialist proof remain incomplete. |
| Province-damage capabilities handoff | Parent accepted and queued during this audit, with exact selector/native getter limits. Its earlier research status is not implementation proof. |
| Main-crater queue and railway completion | Blocked as described above. The suppression substitute must remain disclosed. |
| Event 042 marker guard | Blocked until the owner or parent applies the bounded integration change. |
| Forecast/news delivery repair | Parent-owned active work, outside this audit's implementation claim. |
| `resume_20261004.md` old default/physics/evolution/capital claims | Superseded by current source and takeover decisions for the specific claims reviewed here. Other asset/recovery/catalog evidence must be reconciled by their owners. |
| `agent_decisions_2026-10-04.md` global accepted-and-implemented label | Does not override the explicitly unverified provincial, rail, queue, or runtime requirements. |

Implementation evidence establishes what exists, rather than design approval.
The current parent's scoped authority and inbox G6 support the newly accepted bounded adapter design.
No unspecified addendum is promoted into an accepted spec by this audit.

## Meaningful remaining native cases

1. Put armies of different countries in every main and fragment profile, including an overlap state, and observe one strongest script damage pass there. Compare navy loss at the main centre and Ring 1 with untouched navy in outer profiles, accounting separately for the native visual's province effect.
2. Save and restore the locked trajectory and persistent crater material, then re-enter the resolver. Targets, material ids, counts, and original physical losses must persist without another roll or damage pass.
3. Annex the target during the lock, then separately both resolver recipients. The stored state remains the strike, the surviving callback resolves on schedule, and the global-host monthly watchdog resolves an overdue orphan once.
4. Disable each evolution during the lock independently, lower Chaos after its opening snapshot, and verify the accepted snapshot/toggle split and exact evolution-history rows.
5. Occupy an affected state before impact. The state loses population/buildings once, both distinct live holders receive one aggregate report, and the worldwide death count uses the physical state once.
6. Remove all settled capital alternatives during the lock, then test controlled-owned, occupied-owned, controlled-unowned, and no-alternative fallbacks. A refused move must produce the retained-at-crater burden and close the relocation achievement.
7. For ordinary provincial cohorts, use multiple level-1,2,3,10 buildings, exact equality, repeated provinces at the same original level, and fraction endpoints. Compare actual getter readback with the explicit sum. A main clear must leave every ordinary provincial type at zero.
8. Separately verify level-5 railway edges, multiple supply nodes, ongoing construction, repairs, and active special projects. A zero building getter or disabled construction speed alone does not establish network or queue deletion.
9. Fire a main and fragment visual for a launcher holding the Event 042 nuclear route. No nuclear achievement input, generic nuclear response, nuclear Deaths/Chaos entry, or fallout path may be produced.
10. Review the shared history rows and Event Details at 1920x1080/UI scale 1 with long state names and every actual outcome, plus matching evolution rows/toggles and click regions. Use explicit G7/G8 scenario objects and retain before/after source/artifact identities.

These are exact unverified cases for parent evidence tracking, not a request that this auditor launch the game.
Event 028 is not declared complete by this handoff.

## MCP evidence

Fresh narrow `hoi4.event_inspect` succeeded with selector `{kind: 'event', eventId: 'chaosx.nr28.1'}`, mode `trace`, downstream direction, depth 3, nodes 18, edges 30, and helpers disabled.
It returned `EVENT_INSPECTED_PARTIAL`, focused analysis, revision `0c60ff8924e5dca69dfb472ccf9f47940f2a3b808e3c8e7a02227ad8dde6ac5f`, and zero indexed helpers.
The complete trace artifact was recovered in 37 ordered byte ranges and its 1,098,491 bytes were verified against SHA-256 `aa7742ec914779baa759b9f349fe93e66cb24046f34a85cbdbfb6c46e61cbd85`.
It has `complete = false`, 14 selected nodes, 13 selected edges, no trace truncation, and eight selected helper placeholders.
Its explicit blocker is `EVENT_FOCUSED_ANALYSIS_DEFERRED: Large event workspaces defer workspace-wide helper projections and lifecycle passes; direct source evidence remains available.`
The first 1,048,575-byte resource response silently returned only 35,220 decoded bytes despite its declared range, so it was rejected and replaced by validated 30,000-byte chunks.
No broad scan, refresh, state-flow, helper-expansion, jobs, or native tasks were requested.

Trace URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aa7742ec914779baa759b9f349fe93e66cb24046f34a85cbdbfb6c46e61cbd85/85a8f506d5efee1cca79f468469ca4ebfdd279a25d71da901dd9668a4676fd47/event-trace-0c60ff8924e5.json`.

Fresh matching `hoi4.event_render` succeeded as `EVENT_RENDERED_PARTIAL`, neighborhood view, focused analysis, revision `4875713bbb0a2288e5e7f1373900f1bf93fa0dad12c74ecfe377da1a1f7821b0`, 14 selected nodes, and the same helper/lifecycle boundary.
Render data URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3febd94024b5cbc354e4b0deab402fd289279bfe5e1df0e91c957d60ccc8bce6/cce69c04c389baef7d9a23c26ce455220d48fdab1878a350895f920a6c02b753/event-neighborhood-4875713bbb0a.json`.
Render image URI: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0fb629213c5deb7663583f5eb22a0acd02a447c3c981147541845f0b06064d3a/95822aecf150d1767598c68897c64954c9783fb3cd7eeffbbffea8cf7d6f1669/event-neighborhood-4875713bbb0a.png`.
This is a structural event-chain render, not a game popup or shared-GUI visual acceptance result.

`hoi4.source_lookup` found one unshadowed `asteroid_incoming_damage_units_in_state` definition at runtime 1397-1456 under revision `c47c79a3a7228e89960fb344b91a231de9e83925747f8e4cf5589df71c469e23`.
Its source excerpt stopped at 1418, so the remainder was read locally.
A revision-bound continuation was rejected with `SOURCE_REVISION_STALE`, current revision `0d9f4e5254ed6b3bf302fd6d61b62133018458ab164a64c8c023cdb1e40a0f4d`, while the parent edited the shared source.
The final direct-source lookup and matching compare/check results are recorded in the follow-up below.

Reference context/search/read routes are available and healthy, superseding the takeover's old invalid-selector claims for this connected tool surface.
The context result omitted Event modding, Triggers, On actions, and Localisation at its limit, so it does not prove those sections were covered.
The relevant unit command was read through both live reference routes and local source, while the other precise rules were read from the cited local files.
Installed effects section id `18641e38451cc27ae099c3494821f95d915a5e8211c49121b5916a177af53a6b`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, lines 3417-3438, had no continuation.
Offline Effects section id `b0ebfd26b6e68fab1054aee1ef500d591233a9492198a62a55603642fe27ffb4`, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`, line 365, had no continuation.

The probability pass is assigned to the parent's separate `chaosx_ai_probability_auditor`.
No probability, balance, or gameplay-completion claim is inferred from this source audit.

## Evidence follow-up

The mandatory compare was attempted with `before = { revision: '0c60ff8924e5dca69dfb472ccf9f47940f2a3b808e3c8e7a02227ad8dde6ac5f' }`, the same event selector, `maxChainNodes = 18`, `maxRenderNodes = 18`, and `render = true`.
It produced no compare result or artifact.
The exact client error was `tool call error: tool call failed for hoi4_agent_tools/hoi4.event_compare`, caused by `timed out awaiting tools/call after 600s`.
No input acceptance, structural delta, successful comparison, or runtime result is inferred from that timeout.
This is the recorded comparison-route blocker, and no broad refresh or alternate full analysis was substituted.

`hoi4.script_validate` checked a STATE-scoped `damage_units` body using the installed game documentation and returned `SCRIPT_CHECK_PARTIAL`.
`valid = null`, `parametersChecked = false`, and `checksPerformed = [syntax, command_kind, declared_scope]`.
It found one supported command and one `SCRIPT_ARGUMENT_BLOCK_UNCHECKED` finding, with no omitted findings and no truncation.
The installed documentation registry revision was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
The command kind and STATE scope are supported, but this does not validate variable argument parsing or damage semantics.
The field review against installed effects 3417-3438 and the offline Effects row 365 remains separate evidence.

Fresh `hoi4.source_lookup` completed the actual damage-call tail at runtime 1430-1459 under revision `1f5ea43da02e555180b5770e25caf83323697d0eccc40969568fc71ea25abe87`.
The current full definition spans 1400-1459, has one unshadowed definition, and the returned tail has `nextLine = null`.
This resolves the earlier excerpt gap while retaining the stale-revision rejection as evidence of concurrent parent edits.

The render PNG was retrieved in two ordered byte ranges, decoded to 55,799 bytes, checked for its PNG signature, and verified against SHA-256 `0fb629213c5deb7663583f5eb22a0acd02a447c3c981147541845f0b06064d3a`.
Visual review showed the entry, five option nodes, and eight unresolved helper placeholders, consistent with the focused trace boundary.
It supplies no screenshot of the Event 028 popup, shared Event Log, or Event Details.

The final broader G1 closure covered 30 report/title/description roots, including Event 028 news ids 29,30,32,92,93,94,96,97, 106 reachable localisation keys, and 17 scripted getters.
It found zero actual section-sign colour characters and zero missing keys.
The parent's locked/resolved descriptions were present at that final check.
A semicolon in the newly supplied locked description was sent to the parent as a small prose-rule correction.

The effects source still contained the general state-only building removal and the tracked Event 042 hook still lacked its marker exclusion at the final direct source check.
The ordinary-province cohort adapter is therefore `accepted and queued` for this handoff, rather than marked implemented from a proposed design.
Post-adapter source/native acceptance remains parent-owned follow-up work.

## Source identity snapshot

R is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
V is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Each root and suffix below forms an exact Windows path.
These are the observed pre-adapter bytes during the parent's active repair, rather than a claim that subsequent parent edits retained these hashes.

| Root and suffix | SHA-256 |
| --- | --- |
| R\events\028_asteroid_impact.txt | `6C2A51FEBA04C626CF1DD367374513017D40F663A7433D597B9EAD1BCB1C1CBF` |
| R\common\scripted_effects\028_asteroid_incoming_effects.txt | `4E67E89EC7E67617982CD824321212FEF4336CF0C7C1E6E3868C454D2500799B` |
| R\common\scripted_effects\028_asteroid_incoming_runtime_effects.txt | `5AE3A5DC5237824D95540C5C92D761044CFC512852B623361BE34F06C4EB9C67` |
| R\common\scripted_effects\028_asteroid_incoming_capital_effects.txt | `F3EA14533AA1D3A49F4ACDD00F7FF9CF583A34CFF210C69A6D3031926B7C1CD3` |
| R\common\script_constants\028_asteroid_incoming_constants.txt | `58EB86BE326DC8E6F3494E810490E51024E2226CD33D81715F58C6FE685CCA64` |
| R\common\scripted_triggers\028_asteroid_incoming_triggers.txt | `9BB79C16954A2F27A564A62DB3DE846E6F6F9272BCD9CF57C519EB86B3EDAA41` |
| R\common\on_actions\042_equipment_from_heavens_on_actions.txt | `9FFAD434930986F43E57D90B28DC57F36A592D37FBEDFC6944E6DE5DB060C54C` |
| R\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| R\paradox_wiki\Building modding - Hearts of Iron 4 Wiki.md | `1E5FB5410A26AF12B5B791B193F8F602C4EF8A3614ED897AE4C67084477F7BFC` |
| V\common\buildings\00_buildings.txt | `9FA27D266F726DE04C71311551698C6466257636DCC34D2573A3568D397BD539` |
| V\common\script_constants\documentation.md | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |

The next bounded actions are to apply and review the ordinary provincial adapter, resolve the railway and queue/project disposition honestly, exclude asteroid visuals from the tracked Event 042 hook, and attach the assigned probability/assets/recovery and shared-GUI evidence.
This audit is complete as an evidence handoff, while the event remains partial with the blockers and limits above.
