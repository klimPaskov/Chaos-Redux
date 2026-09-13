# Event 023 decision and mission audit final handoff

Status: **NOT READY** for parent sign-off.

Audited snapshot: shared worktree on 2026-09-01.

Mode: read-only audit; no gameplay, localisation, asset, or source file was changed; no commit was created.

## Scope and evidence basis

I read `AGENTS.md`, the Event 23 specification folder, especially `023_sov_nuclear_bombs_decision_map.md`, `023_sov_nuclear_bombs_decision_mission_prompt.md`, Part 9, and Part 10, the required Chaos Redux decision/mission, event, and subagent skills, the required offline Paradox wiki pages, and the relevant vanilla documentation and precedent files.

The inspected source surfaces were `common/decisions/023_sov_nuclear_bombs_decisions.txt`, `common/decisions/categories/023_sov_nuclear_bombs_categories.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt`, `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt`, `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt`, `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt`, the Event 23 cost triggers/effects/constants, `events/023_soviet_nukes.txt`, `common/on_actions/023_sov_nuclear_bombs_on_actions.txt`, `common/on_actions/005_soviet_collapse_on_actions.txt`, the Event 23 localisation and scripted localisation, and `interface/023_sov_nuclear_bombs.gfx`.

The older handoff at `docs/plans/023_sov_nuclear_bombs_plans/subagent_handoffs/023_decision_mission_auditor.md` was reconciled against the current source. Items that are already fixed are listed below and are not repeated as current blockers.

No live Hearts of Iron IV session, save/reload cycle, or consumer campaign was run. Source inspection and MCP output are not a substitute for that user-owned validation.

## MCP evidence

- `hoi4.probability_inspect` with `decision_ai_will_do` against `common/decisions/023_sov_nuclear_bombs_decisions.txt` completed with `PROBABILITY_SOURCE_DISCOVERED`, zero decision candidates, and a suggested mission adapter with 78 candidates. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/90e02e69c58d07ce8cf97542cd359b19018a086af773a454734b5a04fac1ac34/1f9027965e4e8b64c92aefa941396fa2db3eff5fbaabde3b46877e7a35089d79/probability-inspect-2b9fe4347f0de43a69e631e6f078d9c9da338cab118d8c69417693fd18153756.json`.
- `hoi4.probability_inspect` with `mission_ai_will_do` completed with 78 candidates, 15 required inputs, and no unresolved parser inputs. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9de8210df2e4c2432a19766a2b497dc59d86d9760247cbb6004140ec802ff0a6/34919803aae0c985291e142d8be106bacf81c9f8d75a724e006dd358f90e5df1/probability-inspect-2b9fe4347f0de43a69e631e6f078d9c9da338cab118d8c69417693fd18153756.json`.
- A mission evaluation using the exact 11 Event 23 mission IDs and three named audit fixtures completed with `PROBABILITY_ANALYZED`, 33 candidate/scenario rows, and zero unresolved inputs. All three fixtures were empty adapter states, so all 11 IDs reported `PROBABILITY_OUTCOME_NEVER_ELIGIBLE`; this is structural score evidence only and is not a campaign balance conclusion. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4e848b5e91afbb3a58539a9bfafbf0486c6cb94fac365849969322e9dd7dcd02/c46bbdbf9804f7bbf69a760c8dd1a59dc251d8e7fa484de3b05b9b1fd10c712b/probability-abfe517d072cb595106aa9f7.json`.
- `hoi4.probability_inspect` for the Event 23 test `random_list` completed with `poolComplete=true`, three candidates, zero unresolved inputs, and no available adapter candidates. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8e644c1417e0ac2347ff2b24a024dfff568e4fa2c5ec4fed4b69aeccc947ae66/0f550e7930ceb8eac8d2b07695cc402f10a7717b8d2bfd6f7532443dda74a7b9/probability-inspect-73fde4afb0c2c0.json`.
- `hoi4.gui_inspect` and `hoi4.gui_render` were run for the ordinary `decision_tab` at 1920x1080 and 1280x720 across normal, disabled, active, long-text, and missing-localisation states. The inspect reported zero inspected Event 23 elements because this surface has no Event 23-owned scripted GUI; the render returned global graph diagnostics and no actionable Event 23 geometry or click-region evidence. The result is not a visual pass. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/596c4d85701c8d8b1629750fcb9694439a34a8b2604178f5fcb3e80914aec540/da3abe5b0b15c86e15637c99a00fe2b932bd096e54edbc7da3ea8384e3ee806f/gui-inspect.d40733c1fbf763f9.json`; render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8b1d562d46310a5b677e0bb26248444ceee08074740bebf29a27bb39451bdc6/de31b43b3ee4366b25756b637f29608007fc7cf87e589de825becdfbe92ace2c/decision_tab-full.svg`.
- `hoi4.event_inspect` traces for `chaosx.nr23.1` and `chaosx.nr23.120` returned `EVENT_INSPECTED_PARTIAL` because the workspace event graph has unrelated global diagnostics and a partial trace limit. The traces were used as wiring evidence only, not as an engine clean-pass claim. Artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3b703f8a53e6742eb441fa0c51c01a065a674b3b990b53d72fbaa2e05b098207/43c3178c1d6882371248e8f884b46d0b65c8d1eb2a1eb2552c3ff384dfdd0ec7/event-trace-7994e7bb6ce7.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d8b1fce8f299971f460fa5c23f9afdcf49a67d48af9ffb860e06a660ba6a3b8f/43a0e5d695c14f48658f763e91dc2598f8c2ce1877e199a35adbace2cc6ffdde/event-trace-7994e7bb6ce7.json`.
- No `hoi4.probability_compare` was run because this was a read-only audit with no owner-applied balance patch and therefore no valid before/after pair. No probability sweep was run because no numeric tuning range was being changed.

## Reconciliation with the older handoff

The following older findings were rechecked and are resolved in the current source.

- Delivery crews and command exercise are now bounded missions with explicit completion, timeout, and dedicated cancellation helpers at `common/decisions/023_sov_nuclear_bombs_decisions.txt:1036-1066` and `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1248-1325`.
- Ultimatum, strike-preparation, and retaliation cancellation routes are separated at `common/decisions/023_sov_nuclear_bombs_decisions.txt:1100-1129` and `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1654-1752`.
- Selected collapse restoration now uses `sov_nuclear_bombs_collapse_resolution_authorized` before finalization at `common/decisions/023_sov_nuclear_bombs_decisions.txt:827-849`.
- The category header has one compact posture/public-knowledge status line at `localisation/english/023_soviet_nukes_l_english.yml:60-61`.
- World-threat refresh calls are present after demonstration, ultimatum, strike, and major-exchange source changes at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:462-475`, `670-690`, and `962-984`.
- Cost localisation now matches the five bounded profiles and uses texticons at `localisation/english/023_soviet_nukes_l_english.yml:90-94`.
- Partial settlement repeat protection and explicit demand direction wrappers are present at `common/decisions/023_sov_nuclear_bombs_decisions.txt:452-492` and `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1364-1396`.
- Strike-preparation completion rechecks the prepared strike before proceeding at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1654-1671`.
- Dismantlement cancellation releases the shared reservation through the dedicated cancel path at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1840-1905`.
- Limited-strike target validation excludes Soviet-owned or Soviet-controlled self-targets at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:403-417`, and the native-use on-action is state-scoped at `common/on_actions/023_sov_nuclear_bombs_on_actions.txt:20-66`.
- The current retaliation mission duration is 30 days through `constant:sov_nuclear_bombs_duration.hotline_mission` at `common/decisions/023_sov_nuclear_bombs_decisions.txt:1116-1129`; no 45-day source mismatch remains.

These resolved items are not current blockers.

## Findings by severity

### Critical

#### C1. Retaliation timeout can release without the exact major-strike gate

`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1716-1738` calls `sov_nuclear_bombs_execute_shared_action` directly when the retaliation mission completes or times out. It does not recheck `sov_nuclear_bombs_event_has_valid_major_strike_target`, the major-exchange/first-use world gate, or a target-specific route profile immediately before release. The shared runtime contract at `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:28-132` checks that the staged state is still owned or controlled by the staged target and that the target exists, but it does not require the target to remain a hostile nuclear major or to satisfy Event 23's exact release gate.

This allows a target that becomes peaceful, loses nuclear-major status, or otherwise leaves the retaliation scenario to remain eligible for a generic staged native action. A generic runtime rejection is not equivalent to the missing strategic recheck because the native launch path is the commit point and has no scripted success return, as documented at `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:368-370`.

Recommended bounded fix: snapshot the retaliation state and target at authorization, then perform a fail-closed recheck of the staged state, hostile war relation, nuclear-major condition, world gate, route, readiness, integrity, and active reservation immediately before `execute_shared_action`; release the reservation and close the mission on any failure.

### High

#### H1. Active missions can operate on a mutable selected-state pointer

The operational and collapse state selectors remain targetable without `sov_nuclear_bombs_event_no_active_project` at `common/decisions/023_sov_nuclear_bombs_decisions.txt:72-106`. Their global `sov_nuclear_bombs_selected_state` target can therefore be replaced while a custody mission is running. `sov_nuclear_bombs_complete_rail_security` uses the current selected target for restoration and outcome flags at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1771-1807`; `sov_nuclear_bombs_complete_joint_custody_transfer` uses it for the custody result at `1810-1829`; and dismantlement marks the current selected target after executing the separately staged action at `1854-1882`.

Recommended bounded fix: lock all selectors while any Event 23 project or reservation is active, or snapshot each mission's exact state and use that immutable mission target for every completion, timeout, cancellation, and reward path.

#### H2. The active-project cap is not enforced by every mission starter

The shared `sov_nuclear_bombs_event_no_active_project` helper covers the mission flags at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:453-469`, and most normal decision/effect paths use it. The emergency hotline decision omits it at `common/decisions/023_sov_nuclear_bombs_decisions.txt:608-619`, and `sov_nuclear_bombs_prepare_hotline` starts the retaliation mission without the helper at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:835-843`.

The ordinary Soviet path is usually single-project gated, but the hotline can be opened over an existing production, test, ultimatum, rail, or other project. The source therefore cannot claim a central maximum-three active-mission contract, and the exception can leave multiple cleanup paths live at once.

Recommended bounded fix: apply one central no-active-project/mission-conflict guard in the hotline decision and effect, and make every direct or callback mission activation use the same guard.

#### H3. Joint-custody completion can award success on an invalid or empty site

`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1810-1829` conditionally sets the site joint-custody flags only when the selected site is registered and has a transferred device at `1813-1819`, but it unconditionally grants integrity, records the mission, records custody resolution, and clears the selection at `1821-1828`. A missing, annexed, or zero-device selected site can therefore receive the success reward and completion record. If the selected event target disappears before completion, the outer guard fails and the active mission flag is not cleared.

Recommended bounded fix: fail closed on missing or invalid mission targets, clear the mission and selection, record a failure/cancellation result, and grant the integrity/reconciliation reward only after the exact registered transferred site has passed at completion.

#### H4. Rail and recovery-raid completion do not revalidate the exact collapse site

`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1771-1807` checks only the current operation type and, for recall/raid restoration, whether the current selected state is Soviet-owned or controlled. It does not recheck registered storage, transferred-device count, the collapse crisis, or the original mission target before awarding `sov_nuclear_bombs_rail_corridor_secured` or `sov_nuclear_bombs_recovery_raid_completed` and their readiness/integrity changes.

Recommended bounded fix: use the mission target snapshot and require the full collapse-site and transferred-custody predicate at completion; otherwise clear the mission with a failure result and no reward.

#### H5. Dispersal can be repeated and can reward a no-op package

The dispersal decision remains visible and available without a `reserve_dispersed` or package cooldown guard at `common/decisions/023_sov_nuclear_bombs_decisions.txt:143-158`. The helper moves one assigned device immediately when it finds a source, but when no alternate source exists it clears the destination flag and still applies the country-level dispersal outcome and readiness/integrity changes at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1154-1194`. The source predicate at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:479-486` only requires one assigned device anywhere and does not require a distinct valid destination.

This permits repeat/cycling dispersal actions and a successful-looking no-op, contrary to the map's bounded package, two-valid-state requirement, transit lifecycle, and each-device-once cleanup.

Recommended bounded fix: make the operation one-shot or mission-backed, require a distinct source and destination with a successful transfer, and suppress the outcome/reward on a no-op.

#### H6. Reactor construction grants production capacity at queue time

`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1102-1130` queues a vanilla reactor construction at `1116-1120`, then immediately increments the Event 23 reactor count, consumes the entitlement, marks fissile production complete, and grants readiness/integrity at `1122-1129`. `sov_nuclear_bombs_event_has_production_capacity` then accepts the incremented count at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:328-333`.

The player can therefore assemble against the new event-owned capacity before the vanilla construction is complete. Recommended bounded fix: keep an explicit pending entitlement/construction marker and award Event 23 capacity and completion rewards only from the construction-completion path, while preserving the invalid-placement non-consumption rule.

#### H7. Test, hardening, and reactor site gates omit required combat and site-quality checks

The shared test-site predicate at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:100-107` checks ownership, control, passability, and missing/dismantled flags but not no-active-combat or remote/low-population quality. The survey decision uses it directly at `common/decisions/023_sov_nuclear_bombs_decisions.txt:265-281`. Hardening similarly checks registered Soviet ownership/control but not no-active-combat or the selected site's risk inputs at `125-140`, and reactor placement has no no-active-combat or transfer-risk gate at `190-205`.

Recommended bounded fix: add narrow state predicates for no active combat, valid remote test quality, and no transfer risk, and recheck them in the matching completion/effect helpers rather than relying only on the initial selector.

#### H8. Certification, safety overrule, and retaliation authorization have shallow final gates

Technical certification is available unconditionally while a limited strike is prepared at `common/decisions/023_sov_nuclear_bombs_decisions.txt:507-519`, and its effect only sets flags and modifiers at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1481-1487`. Safety overrule is available for any war at `common/decisions/023_sov_nuclear_bombs_decisions.txt:521-532` and its effect has no doctrine, readiness, or confirmed-crisis check at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1489-1495`.

Retaliation authorization checks the target and no-active-project state but not an unreserved device at `common/decisions/023_sov_nuclear_bombs_decisions.txt:682-693`; the effect can pay the strategic cost and stage a mission without `sov_nuclear_bombs_event_has_unreserved_device` at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1558-1566`.

Recommended bounded fix: add the exact device, route, target, doctrine, readiness, integrity, and crisis predicates to both the decision and effect paths, and fail closed with cost/reservation cleanup if staging cannot succeed.

#### H9. Delivery-route validation is generic rather than target-specific

`common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:47-53` defines a route as strategic-bomber technology, any strategic-bomber stockpile, and any owned airbase. The same helper is used by limited/major strike gates at `403-427`, while the runtime action validator at `common/scripted_triggers/023_sov_nuclear_bombs_runtime_triggers.txt:44-132` only checks the native route token. No fuel, range, target reachability, air-superiority, or target-specific route check is present.

Recommended bounded fix: retain the bounded route helper but add a target-scoped capability predicate before reservation and again before release, including the current route's fuel/access/range conditions that the chosen delivery mode actually supports.

#### H10. AI target scoring and route-safe target selection are not implemented or evidenced

The state-target decisions provide trigger-valid target pools but only flat country-scope `ai_will_do` blocks, with no `target_score` or target-specific modifiers, for example at `common/decisions/023_sov_nuclear_bombs_decisions.txt:366-381`, `664-693`, and `725-740`. The source discovery route could not expose decision candidates and redirected to the mission adapter; the mission evaluation was score-only under empty fixtures. This means the required AI behavior of seeing all valid targets through complete scoring, preferring safe/meaningful targets, and avoiding invalid route/war/custody states is not demonstrated.

Recommended bounded fix: add target-aware scoring over the complete trigger-valid pool, including war relation, target value, route reachability, nuclear-major profile, site risk, and current crisis context, then run the same named probability scenarios through a before/after `probability_compare` after an owner-applied patch.

### Medium

#### M1. Partial-settlement demand adjustment is unreachable after the current cleanup

The raise/narrow decision requires both `sov_nuclear_bombs_coercion_open` and `sov_nuclear_bombs_coercion_settlement_open` at `common/decisions/023_sov_nuclear_bombs_decisions.txt:466-492`. The partial-response branch clears `sov_nuclear_bombs_coercion_open` and sets only the settlement flag at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:770-777`. The result is that the explicit demand direction wrappers exist, but the player cannot reach them through the partial-settlement lifecycle.

Recommended bounded fix: either retain the coercion context while settlement is open or change the adjustment visibility/availability predicate to the intended settlement state, while keeping private/public escalation and the one-response limit mutually exclusive.

#### M2. The response event shows all six outcomes without campaign-state filtering

`events/023_soviet_nukes.txt:158-219` presents acceptance, partial settlement, delay, refusal, exposure, and foreign support with no option-specific `trigger` blocks. This does not filter the response set by actual guarantees, foreign support, stability, route exposure, or target diplomatic state as required by the decision mission prompt.

Recommended bounded fix: add state predicates or dynamic response localisation so only campaign-valid outcomes are selectable, and keep the target-side six-flag cleanup before each new ultimatum at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:691-697` complete for all six response flags.

#### M3. One user-facing decision has missing localisation

`common/decisions/023_sov_nuclear_bombs_decisions.txt:384-386` references `sov_nuclear_bombs_close_coercion_target` and `sov_nuclear_bombs_close_coercion_target_desc`, but neither key is present in `localisation/english/023_soviet_nukes_l_english.yml` through line 316. The decision can therefore expose raw localisation keys.

Recommended bounded fix: add both keys in the existing Event 23 localisation file with concise target-close text.

#### M4. Long requirements have no custom trigger tooltip layer

`common/decisions/023_sov_nuclear_bombs_decisions.txt` contains no `custom_trigger_tooltip` entries. Several target, readiness, integrity, custody, route, and settlement gates are long compound predicates, so the player receives no precise blocked-reason presentation beyond the general decision description. This is especially visible for final authorization, collapse recovery, and target selectors.

Recommended bounded fix: add concise dynamic requirement tooltips for the blocked conditions and keep spendable costs separate from non-consumed requirements.

#### M5. The compact header omits current target, site, deadline, and phase context

The header correctly exposes operational devices, readiness, integrity, posture, and public knowledge at `localisation/english/023_soviet_nukes_l_english.yml:60-61`, but it does not expose the currently selected target/site, active mission deadline, reservation state, or current phase. The category therefore satisfies the permanent four-value requirement but still makes active target and deadline significance harder to read.

Recommended bounded fix: append one compact dynamic context line that appears only when a target, site, reservation, or mission deadline exists; do not create a new GUI.

#### M6. The Event 23 response and action source contains an unbounded world scan

`common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:137-145` uses `any_country` for the opposing nuclear-major gate, and `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:962-984` uses `every_country` to play major-exchange audio. The Event 5 callback scans were checked separately and are bounded to saved targets/states in `common/on_actions/005_soviet_collapse_on_actions.txt:15-43` and the runtime snapshot helpers.

Recommended bounded fix: replace recurring/global scans with a cached opposing-major target or a bounded event-entry update, and route major-exchange audio through an approved bounded consumer path. This is a performance/scope issue, not evidence that the bounded Event 5 bridge is wrong.

#### M7. Custom cost gates are strict `>` while payment spends the displayed amount

The visible cost profiles at `localisation/english/023_soviet_nukes_l_english.yml:90-94` match the payment helpers at `common/scripted_effects/023_sov_nuclear_bombs_cost_effects.txt:9-36`, and there are only two, three, three, three, and four spendable types respectively. However, the trigger gates at `common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt:9-37` use strict `>` comparisons, so a profile displaying 35 PP or 20 command power requires one additional unit under literal comparison semantics.

Recommended bounded fix: align the custom trigger threshold with the displayed consumed amount using the project's supported greater-than-or-equals pattern, or deliberately display the actual threshold if one spare unit is required. No live test was run to infer a different engine convention.

#### M8. Centralization and several support actions are immediate flat exchanges rather than the mapped lifecycle

`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1133-1203` makes audit, hardening, dispersal, and centralization immediate modifier/flag operations. In particular, centralization at `1197-1203` only sets a flag and adds integrity/readiness, while the map defines hardening and dispersal as timed/finite operations and centralization as a time-bearing support decision. This keeps the source shallow and makes repeated state significance less legible.

Recommended bounded fix: use existing mission/cooldown primitives for the bounded operations, centralize tuning in constants, and preserve the current four cost-profile limit.

### Low

#### L1. Tuning literals remain in local helpers despite shared constants

`common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1133-1151` contains literal audit/hardening values such as `2`, `9`, and `-3`, while related tuning constants exist in `common/script_constants/023_sov_nuclear_bombs_constants.txt`. This is not a new mechanic blocker, but it weakens the required single-source tuning discipline.

Recommended bounded fix: replace the local literals with the existing constants in the same bounded decision pass.

#### L2. Breakaway operationalization mission visibility is flag-only

The mission definition at `common/decisions/023_sov_nuclear_bombs_decisions.txt:1148-1162` has only the active flag in `visible` and `activation`, and no actor/crisis/custody guard. Its starters have stage-specific guards at `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1908-1939`, but its completion at `1942-1980` can still advance technical or command stages if the crisis disappears before timeout.

Recommended bounded fix: include the breakaway actor/crisis and stage validity in mission activation/completion, and convert an invalid crisis into a clean cancellation rather than advancing the stage.

## Decision category lifecycle notes

- Opening and doctrine selection are present as four mutually exclusive choices at `common/decisions/023_sov_nuclear_bombs_decisions.txt:10-69`. The category is visible for the active Soviet actor or a breakaway custody crisis at `common/decisions/categories/023_sov_nuclear_bombs_categories.txt:9-20`.
- The permanent header is ordinary category localisation rather than a custom GUI. It exposes operational devices, readiness, integrity, posture, and knowledge, but not active target/deadline context.
- Phase 1 custody actions are present at `111-187`. Audit, hardening, dispersal, centralization, and delegation exist, but hardening/dispersal/centralization are immediate and the selected-site/combat/cooldown contract is incomplete.
- Phase 2 production and delivery actions are present at `190-262`. Delivery crews and command exercise now have bounded missions, while reactor completion timing and site gates remain open issues.
- Phase 3 test actions are present at `265-363`. The selected test target and one proof-test mission exist, but the site predicate omits combat/quality checks and the source outcome pool is limited to success, failure, and accident.
- Phase 4 target/coercion actions are present at `366-504`. The selector, private signal, ultimatum, demonstration, limited strike, settlement, demand wrappers, and back-down routes exist, but the visible action count breaches six and the partial-settlement adjustment path is unreachable.
- Phase 5 authorization actions are present at `507-605`. Final authorization has a strong click-time predicate, while certification, safety overrule, redirection, and retaliation completion need stronger profile-specific rechecks.
- Phase 6 exchange actions are present at `608-722`. Hotline, stand-down, limit, preserve, retaliation, suspension, and moratorium actions exist, but hotline bypasses the project lock and retaliation authorization lacks device gating.
- Phase 7 collapse-custody actions are present at `725-851`. The selected depot, recall, rail, joint custody, raid, disable, destroy, and authorized restoration routes exist, but completion target drift, invalid-site rewards, and visible action density remain.
- Phase 8 moratorium actions are present at `853-940`. Seal, dismantlement selection, dismantlement, observers, restraint, and reactivation exist, with dedicated dismantlement cancellation and ledger release, but several map-described time-bearing actions are immediate.
- Breakaway custody-only decisions are present at `944-1016`, and the four staged operationalization stages share one bounded mission definition. The breakaway path does not use the native launch adapter, but mission activation/completion still needs actor/crisis invalidation cleanup.
- The 11 mission definitions are present at `1020-1194`; detailed lifecycle notes are below.

## Cognitive-load audit

The counts below include target selectors that remain visible in the same category. They are source-level maxima, not GUI-rendered campaign counts.

| Surface | Maximum visible primary actions | Active-mission observation | Cognitive-load finding |
| --- | ---: | --- | --- |
| Doctrine opening | 4 mutually exclusive | None | Clear enough; four choices share one cost profile and distinct effects. |
| Phase 1 | 6: operational selector, audit, harden, disperse, centralize, delegate | Normal project lock on most actions | At the hard limit with no spare capacity; dispersal and hardening significance is under-explained by immediate effects. |
| Phase 2 | 6: operational selector, reactor, assembly, delivery crews, command exercise, authentication | Assembly/crew/exercise use bounded flags and mission activation | At the hard limit; reactor queue-time rewards make the visible production state misleading. |
| Phase 3 | Up to 5: operational selector, survey, three test profiles | One proof-test mission | Within the limit, but site quality and blocked conditions are not visible enough. |
| Phase 4 | At least 7: operational selector, close, private, public ultimatum, demonstration, limited strike, back down | One ultimatum/strike/test project normally | Definite six-action breach; partial-settlement demand controls are unreachable after the current cleanup. |
| Phase 5 | Up to 6 after certification: operational selector, authorize, hold, redirect, reduce, abort | Strike-preparation mission is one project | At the limit; final context needs target/deadline/reservation clarity. |
| Phase 6 | Up to 6 before/around retaliation: operational selector, hotline, limit, preserve, target selection/authorization, suspend | Hotline can bypass the project lock | At the limit with an unsafe exception to the active-project contract. |
| Phase 7 | At least 7 after depot selection: collapse selector plus recall, rail, joint, raid, disable, destroy; up to 8 if operational selector remains open | Rail/joint missions use current selected target | Definite six-action breach and target-drift risk. |
| Phase 8 | Up to 5 normal moratorium actions | Dismantlement mission is bounded | Within the limit; immediate support actions reduce lifecycle clarity. |
| Breakaway custody | 5 custody-only decisions | One staged operationalization mission | Action count is acceptable; mission invalidation is incomplete. |

Player-facing values are operational devices, readiness, integrity, posture, knowledge, selected target/site, reservation, active mission, deadline, and phase. The first five are visible in the category header; selected target/site, reservation, deadline, and phase are not consistently surfaced. Every spendable cost is icon-first, but several non-consumed gates are not given custom blocked-reason tooltips.

## Mission quality notes

| Mission id | Owner, category, region | Requirement and duration | Success, timeout, failure, cancellation | Duplicate or stale-target risk |
| --- | --- | --- | --- | --- |
| `sov_nuclear_bombs_device_assembly_mission` | SOV; production; no map region, production ledger | Production flag and actor/capability checks; 120 days at `1020-1034` | Complete and timeout register a bounded batch; invalid capability rejects; dedicated cancellation clears amount at `1056-1100` | Normal decision is project-gated; no staged map target. |
| `sov_nuclear_bombs_delivery_crews_mission` | SOV; production/delivery; route-global | Delivery flag and route; 90 days at `1036-1050` | Completion/timeout recheck actor and route, then certify or fail; dedicated cancellation at `1278-1300` | Normal duplicate flag guard is present; route is generic rather than target-specific. |
| `sov_nuclear_bombs_command_exercise_mission` | SOV; production/command; route-global | Exercise flag and route; 60 days at `1052-1066` | Completion/timeout recheck actor and route, then apply success or failure; dedicated cancellation at `1302-1325` | Normal duplicate flag guard is present; no explicit target snapshot. |
| `sov_nuclear_bombs_proof_test_mission` | SOV; test; selected test state | Prepared test and staged reservation; 120 days at `1068-1082` | Completion/timeout executes shared action and receipt; failure/accident are in the three-result pool; cancellation releases the reservation at `604-629` | Target can enter combat after staging because the completion path uses generic runtime validation. |
| `sov_nuclear_bombs_ultimatum_response_mission` | SOV; coercion; selected target country | Pending target response; 14 days at `1084-1098` | Event response or timeout resolves; dedicated cancel clears all six target flags at `810-832` | Current cancel path is sound, but new ultimatum setup clears only four flags at `691-697`, allowing stale exposed/foreign-support flags on reuse. |
| `sov_nuclear_bombs_strike_preparation_mission` | SOV; authorization; staged exact target state | Prepared strike; 7 days at `1100-1114` | Completion/timeout rechecks `event_has_valid_prepared_strike`; invalid state calls abort/recover; cancellation releases the reservation | Preparation target is safer than before, but selector drift remains possible for surrounding decision state. |
| `sov_nuclear_bombs_retaliation_window_mission` | SOV; retaliation; staged major target state | Authorized retaliation or hotline; 30 days at `1116-1130` | Hotline resolves separately; retaliation completion/timeout executes or cancels at `1716-1738` | Critical missing exact major-strike/world-gate recheck before release. |
| `sov_nuclear_bombs_rail_corridor_security_mission` | SOV; collapse custody; selected depot | Recall, rail, or raid operation; 120 days at `1132-1146` | Completion applies operation flags and rewards; cancellation clears operation at `1754-1761` | Completion reads mutable selected state and does not fail closed on target invalidation. |
| `sov_nuclear_bombs_breakaway_operationalization_mission` | Breakaway actor; collapse custody; selected transferred depot | Stage flag only; 180 days at `1148-1162` | Completion advances technical, command, or delivery stage; cancellation pauses at `1763-1769` | Mission visibility lacks actor/crisis/custody guard; stage can advance after crisis loss. |
| `sov_nuclear_bombs_joint_custody_transfer_mission` | SOV; collapse custody; selected transferred depot | Joint-custody flag; 120 days at `1164-1178` | Site state is conditional, but integrity/reward/recording is unconditional at `1810-1829`; cancellation clears selection | Invalid or empty target can receive success; missing target can leave the mission flag active. |
| `sov_nuclear_bombs_dismantlement_inspection_mission` | SOV; moratorium; staged assigned site | Dismantlement flag and reservation; 180 days at `1180-1194` | Shared demolition commits or dedicated cancel releases at `1854-1905` | Cancellation is fixed; completion still marks the mutable selected target rather than the staged action site. |

## Cost and requirement clarity

The five cost profiles are bounded at 2, 3, 3, 3, and 4 spendable types, so no current decision exceeds the four-type limit and no hidden fifth cost was found.

The current cost localisation uses `£pol_power`, `£command_power`, `£support_equipment_text_icon`, `£manpower_texticon`, `£GFX_train_texticon`, `£GFX_fuel_texticon`, and `£convoy_texticon` at `localisation/english/023_soviet_nukes_l_english.yml:90-94`; no literal spendable resource name is used in those profiles.

The profile-to-payment mapping is structurally aligned between `common/scripted_triggers/023_sov_nuclear_bombs_cost_triggers.txt:9-37` and `common/scripted_effects/023_sov_nuclear_bombs_cost_effects.txt:9-36`, subject to the strict-`>` threshold issue in M7.

Non-consumed requirements are less clear. Route, readiness, integrity, exact target status, war relation, nuclear-major status, site custody, and settlement verification are spread across long predicates without custom trigger tooltips. Final authorization is the strongest gate at `common/decisions/023_sov_nuclear_bombs_decisions.txt:535-546` and `common/scripted_effects/023_sov_nuclear_bombs_event_effects.txt:1673-1713`; retaliation timeout does not inherit that strength.

## AI validity and route-lock notes

All mapped ordinary decisions and missions contain an `ai_will_do` block, but most are flat base weights with only country-level modifiers. The state-target decisions do not score the complete valid target pool by target value, distance/range, route quality, war relation, custody risk, or escalation context.

The generic command target predicate is safe against impassable, missing, dismantled, and non-owned/non-war states at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:55-72`. The limited strike predicate correctly excludes Soviet self-targets at `403-417`, and the major predicate requires a nuclear-major target at `419-427`.

The remaining route lock is too broad because any strategic-bomber equipment and any Soviet airbase satisfy `event_has_delivery_route` at `47-53`. Target-specific reachability, fuel/access, and air conditions are absent.

`sov_nuclear_bombs_event_target_is_nuclear_major` and `sov_nuclear_bombs_event_has_other_nuclear_major` use native `num_of_nukes` and technology checks at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:122-145`, not the Event 23 operational ledger. This can treat a country as an available nuclear major even when it has no Event 23-compatible operational route or ledger state; the target gate should be intentional and documented.

## Localisation, tooltip, GFX, and GUI notes

- The missing close-coercion name and description in M3 are current localisation blockers.
- No `custom_trigger_tooltip` entry exists in the Event 23 decision file, leaving long compound requirements opaque.
- The compact category header is a good density improvement, but it needs one dynamic context line for selected target/site, reservation, deadline, or phase.
- `interface/023_sov_nuclear_bombs.gfx` contains 52 texture references and a read-only path scan found all 52 referenced files present.
- There is no Event 23 `.gui` file or Event 23 scripted-GUI surface. The ordinary category is intentionally engine-owned; no `chaosx_event_ui_worker` handoff is required.
- GUI MCP rendering returned global graph diagnostics and zero inspected Event 23 elements, so no production visual pass is claimed.

## Cleanup, exploit, and ledger notes

The runtime ledger architecture is structurally sound at source level. Reconciliation sums operational, assigned, reserved, transferred, dismantled, missing, and expended buckets at `common/scripted_effects/023_sov_nuclear_bombs_runtime_effects.txt:55-99`; reservation release has assigned, transferred, and operational rollback branches at `314-365`; commit updates the exact source bucket at `371-460`.

The source-level reservation/cancellation paths are therefore a provisional conservation pass, not save/reload proof. No live save/reload or engine consumer validation was performed. The major remaining ledger risks are the dispersal no-op/repeat path, reactor queue-time capacity, invalid joint/rail completion rewards, and the retaliation timeout's unvalidated native release.

Event 5 custody callbacks were checked as bounded to saved release targets and state snapshots in `common/on_actions/005_soviet_collapse_on_actions.txt:15-43` and the Event 23 runtime bridge. No new whole-world Event 5 loop was found. Event 23 still has the global `any_country`/`every_country` concerns in M6.

No free native launch path was found for breakaway actors; breakaway actions remain custody-only. The breakaway mission's missing crisis invalidation is still a cleanup risk.

## Accepted decision-map coverage checklist

- [x] Four custody doctrine choices exist at `common/decisions/023_sov_nuclear_bombs_decisions.txt:10-69`.
- [x] One ordinary decision category and static category picture exist at `common/decisions/categories/023_sov_nuclear_bombs_categories.txt:9-20` and `interface/023_sov_nuclear_bombs.gfx:1-6`; no new scripted GUI is required by the specification.
- [~] Phase 1 audit, harden, disperse, centralize, and delegate actions exist at `111-187`, but the map's timed/cooldown/combat/dynamic-storage behavior is incomplete.
- [~] Phase 2 reactor, assembly, delivery crews, command exercise, and authentication actions exist at `190-262`, but reactor rewards happen at queue time and site/route gates are incomplete.
- [~] Phase 3 survey, instrumented, concealed, public, evacuation, cancellation, and investigation actions exist at `265-363`, but test-site combat/quality gates and richer outcome significance are incomplete.
- [~] Phase 4 target selection, private signal, public ultimatum, wartime demonstration, limited strike, partial settlement, demand adjustment, and back-down actions exist at `366-504`, but the visible action count exceeds six, response filtering is absent, and demand adjustment is unreachable after partial cleanup.
- [~] Phase 5 certification, overrule, final authorization, hold, redirect, remote demonstration, and abort actions exist at `507-605`, but certification/overrule gates and timeout/release rechecks are incomplete.
- [~] Phase 6 hotline, stand-down, retaliation profile, reserve preservation, retaliation selection/authorization, suspension, and moratorium actions exist at `608-722`, but the hotline bypasses the project lock and retaliation lacks a final device/target gate.
- [~] Phase 7 collapse selector, recall, rail security, joint custody, recovery raid, disable, destroy, and authorized restoration exist at `725-851`, but visible actions exceed six and completion rewards can use invalid or mutable targets.
- [~] Phase 8 seal, dismantlement selection, dismantlement, observers, restraint, and reactivation exist at `853-940`, with dedicated dismantlement cleanup, but time-bearing behavior is simplified and target/context presentation is thin.
- [~] Breakaway custody-only secure, technical access, command formation, delivery integration, and return decisions exist at `944-1016`; the native launch boundary is respected, but operationalization mission invalidation is incomplete.
- [x] All 11 mapped mission IDs are declared at `1020-1194`, with explicit complete, timeout, and cancel effects.
- [~] The normal project helper lists all mission flags at `common/scripted_triggers/023_sov_nuclear_bombs_event_triggers.txt:453-469`, but the hotline path bypasses it, so the active-project cap is not accepted.
- [x] Cost-count and texticon coverage pass structurally at `localisation/english/023_soviet_nukes_l_english.yml:90-94` and the cost trigger/effect files, subject to M7 threshold alignment.
- [~] Source-level reservation/release/reconciliation is coherent, but save/reload and native launch consumer behavior remain unvalidated.
- [~] Event response and evolution/report wiring exists in `events/023_soviet_nukes.txt` and the Event 23 effects, but the event trace was partial and response options are not state-filtered.
- [~] AI weights exist, but complete target scoring and scenario-specific balance evidence are missing.

## Recommended fix order

1. Close C1 by revalidating the staged retaliation target, war/world gate, route, device, and custody state immediately before native release.
2. Add selector locking or immutable mission target snapshots, then fail closed for rail, joint-custody, dismantlement, and collapse-site completion.
3. Apply the central project lock to hotline and every direct/callback mission activation, and enforce the intended active-mission cap.
4. Fix dispersal no-op/repeat behavior and reactor queue-time capacity before balance review.
5. Repair the partial-settlement visibility state, response filtering, missing localisation keys, and custom trigger tooltips.
6. Add exact combat/site-quality and target-specific delivery route gates, then add AI target scoring and run a before/after probability comparison with the named scenarios.
7. Replace or bound the Event 23 world scans and migrate remaining local tuning literals to constants as a bounded cleanup pass.

## Simplifications, omissions, and blockers

- Status is NOT READY; no source patch was applied because this audit was explicitly read-only.
- No live game, campaign, native `launch_nuke` consumer, or save/reload validation was performed.
- No probability comparison or sweep was performed because there was no owner-applied patch and no valid before/after balance pair.
- The GUI render could not provide Event 23-specific visual evidence because the category is ordinary engine-owned and the global GUI graph returned unrelated diagnostics; this is recorded as an evidence limitation, not a visual pass.
- The event trace was partial because of the workspace graph and trace limits; it does not certify full event execution.
- No separate broad mechanic plan was written. The remaining source issues are bounded to Event 23 decision/mission, cleanup, route, AI, and localisation surfaces, but they must be resolved before parent sign-off.

Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`, plus the required offline wiki and vanilla documentation workflow. No skill was created or updated.
