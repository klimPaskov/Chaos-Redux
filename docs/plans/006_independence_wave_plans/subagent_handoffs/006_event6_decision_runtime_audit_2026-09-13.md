# Event 006 decision and mission runtime audit

Date: 2026-09-13 (Europe/Kyiv).

Disposition: **Implemented one narrow strict-origin repair. HOLD / PARTIAL remains.**

Owner: `event6_decision_runtime_audit`.

This handoff covers the Event 006 decision categories, missions, admitted package decision registries, shared decision triggers and effects, cost localisation, and the two linked decision-owned GUI surfaces.

No package was admitted, no category was added, no pre-event pressure or queue was added, no fallback was introduced, and no League lifecycle caller was added.

## Source-level outcome

The current worktree contained an uncommitted widening in `common/scripted_triggers/006_independence_wave_triggers.txt` that allowed `is_independence_wave_event021_package_country = yes` to satisfy both `is_independence_wave_event6_local_content_active` and `is_independence_wave_event6_player_surface_allowed`.

That widening could publish Event 006 categories, decisions, missions, and their costs to an origin-neutral Event 021 adapter package, contrary to the accepted active-origin-only boundary.

The narrow repair restored `is_independence_wave_event6_local_content_active` to `exists = yes` plus `is_independence_wave_active_country = yes` at `common/scripted_triggers/006_independence_wave_triggers.txt:20-23`.

The narrow repair restored `is_independence_wave_event6_player_surface_allowed` to the active-origin predicate plus the four existing adapter-receipt exclusions at `common/scripted_triggers/006_independence_wave_triggers.txt:77-83`.

The separate internal `is_independence_wave_package_content_active` bridge at `common/scripted_triggers/006_independence_wave_triggers.txt:25-49` was preserved.

The concurrent `is_independence_wave_package_origin_compatible` addition at `common/scripted_triggers/006_independence_wave_triggers.txt:51-71` was left untouched.

Because the widened clauses existed only as another agent's uncommitted working-tree edit, the restored clauses have no net diff against `HEAD`. The working-tree transition is the relevant before-and-after evidence.

## Severity-sorted issue list

### P1 resolved: Event 021 adapter could publish Event 006 decision surfaces

Before repair, both shared player-surface helpers accepted `is_independence_wave_event021_package_country = yes` without `is_independence_wave_active_country = yes`.

After repair, the Event 021 setup and completed-adapter receipts remain available only through the internal package-content bridge, while Event 006 decision categories and decisions require a real active Event 006 origin.

The repair preserves the exact no-pre-event contract and does not change the 32 content-attested package boundary.

### P1 open: Whole-event admission is still intentionally incomplete

The current authority remains 32 content-attested selectable packages across 29 compatible reservation groups and 40 runtime adapters, with 161 selectable rows still unattested.

The eight adapter-only rows remain fail-closed as IW-013 NAV, IW-015 GLC, IW-043 CHU, IW-058 ASY, IW-093 DOX, IW-098 SOK, IW-177 FIJ, and IW-179 FSM.

No decision or mission edit can close package identity, asset, force, formable, host, focus, probability, and central-attestation gaps for those rows.

### P1 open: Typed AI and mission probability evidence remains incomplete

The shared decision probability inspection found 13 candidates, 89 required inputs, zero available candidates, and `poolComplete = false`.

The shared mission probability inspection found 64 candidates, 54 required inputs, zero available candidates, and `poolComplete = false`.

The Balkan mission inspection found 86 candidates, 17 required inputs, zero available candidates, and `poolComplete = false`.

The Balkan decision inspection returned the exact MCP `INTERNAL_ERROR` blocker with no artifact.

The named `chaosx_ai_probability_auditor` route is not exposed in this runtime, so the direct read-only MCP inspections are evidence of adapter discovery only and do not establish quantitative AI balance.

### P2 open: GUI evidence is structurally complete but visually unresolved

The status window inspection reports 48 inspected elements and no missing resources, but it retains 63 nonblocking overlap findings, four missing static-fallback warnings, unresolved dynamic state, and unsupported offline blendframe behavior.

The formable state-puzzle inspection reports 93 inspected elements and no missing resources, but it retains 521 overlap findings and unresolved summary values for FORM-01, FORM-02, and FORM-03.

The status render returned `validation.passed = false` because the response exceeded the wire budget, while the formable render returned `validation.passed = true` with the same response-truncation warning.

No GUI layout edit was made because these are shared event-owned windows and the visible warnings require the parent or the dedicated event UI owner to resolve with coherent fixtures and matched comparisons.

### P2 open: League transition reachability remains unresolved

The decision source contains League and network actions with route and member gates, but current authority still records authored League transitions without normal-play callers and a missing durability-mission setter.

Adding callers or inventing a mission outcome is outside this bounded decision audit.

### P3 reviewed and not patched: no additional package project lock

The current static crosswalk records 75 Event 006 mission blocks with package activation surfaces and 43 explicit package active-project serializations.

The remaining meaningful exceptions are the two generic shared founding or settlement missions covered by the central active-founding helper and the intentional ICE persistent harbour deadline.

No additional lock is safe without inventing a package-local mission or changing accepted mechanics.

## Decision category lifecycle notes

The founding category exposes the shared DM-01 through DM-05 flow and the attached Statehood Ledger status GUI only after the strict active-origin gate.

The government, security, host-relations, network, League, evolution, package, overlay, and formable categories use active-origin or player-surface gates and retain their existing setup, route, phase, and cleanup predicates.

The formable categories attach `independence_wave_formable_state_puzzle_scripted_gui` and keep state-puzzle actions behind their family readiness and transaction locks.

The allocator validator still reports no pre-event category, mission, cost, queue, or pressure surface and the exact automatic ladder of 3, 4, 5, 7, and 10.

## Cognitive-load notes

The shared source keeps phase and route gates on the ordinary categories instead of exposing every package row at once.

The current source crosswalk does not show a new category with more than six visible primary actions, but direct runtime category density and affordability remain unverified because the installed MCP exposes no decision inspector.

The Statehood Ledger status surface intentionally retains five named values, which is an accepted exception, but its dynamic tab isolation, click regions, blendframes, and representative populated fixtures remain unresolved.

The decision descriptions provide duration, objective, and visible consequence text for the reviewed DM and package actions.

The shared category descriptions expose legitimacy, recognition, capacity, security, instability, charter, confidence, patron capture, revisionist pressure, and completed-action values, so the values have stable labels and thresholds, but the GUI warning and overlap findings prevent a visual acceptance claim.

## Mission quality notes

| Mission | Owner, category, and region | Requirement and duration | Success and failure | Duplicate risk and status |
| --- | --- | --- | --- | --- |
| `independence_wave_secure_provisional_capital` | Released Event 006 country, Emergency Founding, capital and supply node | Material reservation, controlled capital, garrison, equipment, and train or motorized transport gates with the founding duration constant | Timeout secures the capital and applies founding deltas. Capital, control, or garrison loss cancels into relocation and government failure | Hidden starter, `fire_only_once`, active-founding gate, and cleanup are present. Source-complete after the material repair |
| `independence_wave_establish_revenue_service` | Released Event 006 country, Emergency Founding, capital economic anchor | Administration light or standard cost, controlled capital, stable enough country, and the founding duration constant | Completion establishes revenue service and capacity. Timeout sets the salary crisis and applies negative deltas | `fire_only_once`, completion and crisis flags, and active-founding activation guard prevent duplicate reward chains |
| `independence_wave_axx_hold_banat_council_together` | IW-024 AXX, Banat council category, package capital region | Setup receipt, stable AXX ledgers, controlled current capital, and the Banat founding-crisis duration constant | Cancellation resolves only on stable ledgers and control. Other cancellation and timeout paths apply package project failure | Founding crisis is intentionally separate from ordinary project serialization and has explicit failure cleanup |
| Representative admitted package project actions | Admitted package category, package anchor and former-host route | Package-specific route, capital, host, ledger, cost, and active-project helper gates with centralized duration constants | Completion applies the package route or ledger reward. Cancellation and timeout call the package failure helper where the matrix requires it | 43 package mission or project surfaces are explicitly serialized, and the remaining exceptions are documented rather than patched speculatively |
| `independence_wave_ice_hold_the_harbour` | IW-012 ICE, North Atlantic category, harbour survival region | ICE setup, harbour crisis state, and persistent harbour-crisis duration constant | Stable harbour state resolves the crisis. Loss of the required state sets the failure branch | Intentionally outside ordinary package active-project locks because it is a persistent survival deadline |

The mission source uses distinct completion, timeout, cancellation, and cleanup effects for the reviewed surfaces.

No passive counter-only mission or free equipment loop was found in the admitted source review.

## Cost and requirement clarity

The shared cost families use centralized constants and matching gate, display, and payment helpers in `common/scripted_triggers/006_independence_wave_decision_triggers.txt`, `common/scripted_effects/006_independence_wave_decision_effects.txt`, and `common/script_constants/006_independence_wave_decision_constants.txt`.

Administration actions use command power, manpower, and civilian-factory capacity.

Diplomatic actions use command power plus an either-or convoy or train requirement.

Security actions use command power, manpower or army experience, infantry equipment, and support equipment, with the reviewed major palettes capped at four spendable groups.

Strategic actions use stability, command power, either-or transport, and civilian-factory capacity, which remains four displayed groups.

The strategic, border, integration, corridor, rescue, sponsorship, reclamation, safe-reserve, and provisional-capital strings reviewed in `localisation/english/006_independence_wave_decisions_l_english.yml:25-135` use texticons for spendable values.

A read-only localisation scan found no cost key in that file that names a spendable resource without a corresponding texticon.

The remaining member-count, state-control, route, and host requirements are non-consumed requirements and are kept separate from the displayed debit where the reviewed tooltip contract provides a separate line.

No action with more than four distinct spendable cost types was promoted or patched in this audit.

## AI validity and route-lock notes

The reviewed selectable timed decisions and missions retain `ai_will_do` blocks using the centralized urgent, high, standard, and modifier constants.

Package decisions retain package identity, current-capital, route, host, recognition, member, and active-project gates appropriate to their category.

The strict origin repair changes only player-surface eligibility and does not change any AI weight or candidate ranking.

The incomplete MCP candidate pools prevent claims about relative package choice, starvation, dominance, rank reversal, or timing balance.

No `probability_compare` was created because no owner-approved weighted patch was made.

## Localisation and tooltip gaps

The reviewed cost keys, blocked keys, decision names, descriptions, effect tooltips, and mission text resolve in the Event 006 localisation surfaces.

The cost strings use dynamic constants and texticons, including the strategic repair retained from the earlier bounded lifecycle work.

The shared category and package descriptions remain dense in places, and custom trigger tooltip coverage is not complete for every route and package requirement.

Those clarity gaps are parent-owned wording work because a safe local rewrite would need the full representative decision and mission fixture set.

## Cleanup and exploit-risk notes

The reviewed package project cancellations call package failure helpers and the shared cleanup paths clear stale project, setup, route, and mission state where the current matrix requires it.

The opening DM-01 material is reserved and paid through its country-scoped starter effect, which avoids a free mission or refund loop.

The active-project locks, founding helper, completion flags, and one-time markers prevent simultaneous reward projects and repeated completion in the reviewed admitted packages.

The Event 021 strict-origin repair removes the observed adapter-to-Event-006 surface leak without changing the internal setup bridge.

The ICE persistent deadline and generic shared founding or settlement missions remain intentional lifecycle exceptions.

## Required source and reference review

`AGENTS.md` was read before source review.

The `chaos-redux-decisions-missions`, `chaos-redux-events`, `chaos-redux-scripted-gui`, and `chaos-redux-subagents` skills were read and applied.

The offline Paradox wiki pages for Data Structures, Triggers, Effects, Modifiers, Localisation, Scopes, On Actions, Event Modding, Decision Modding, Idea Modding, AI Modding, Interface Modding, and Scripted GUI Modding were consulted.

The installed vanilla documentation for effects, triggers, modifiers, script concepts, dynamic variables, localisation formatting, and scripted GUIs was consulted.

Vanilla decision and mission precedent was reviewed in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\ARG.txt` and the installed decision documentation.

## MCP evidence

### Weighted logic

Shared decision inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/44c1bc093f0de1318a9b0ba19330c7e5a211e9331f67cb1ef32ac22b6ed24524/b47192b4fba6ce0537cccc2e4ddbeebbaed4a1aa5586f5056ad817472957bd9a/probability-inspect-6b200254863e.json`.

Shared mission inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/df72cf595d608bcdbf33087734fff2f08f08a613366e771209ac5632824f3e4e/d1c181d401613b935c30f627703ade23e6a9d1681166a02d75f7038744151e82/probability-inspect-6b200254863e.json`.

Balkan mission inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/69983d9797069cc98e85eb9c5d762140155db12d2e80e27bb5470ba4e3c99d34/d188cc1e3b9d40e30bbaf8c9e209b21edb653dae5913fc09128c8206988d2e39/probability-inspect-db997a9e70ea.json`.

The Balkan decision inspect returned `INTERNAL_ERROR` with `Unexpected internal error` and no artifact.

The one-scenario shared decision evaluation returned `PROBABILITY_ANALYZED_PARTIAL` with five unresolved inputs and one intentional `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` warning for the hidden automatic DM-01 mission candidate.

Evaluation artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/00ad1ff7c5da037169d5851472cd0311da5baa24ec1d477da4d2bb475dfbab44/eb92ae3a9e09d51a40e745056814cca08e1394309ceb358a26ca0b50486dc55c/probability-41b23d2a4e00cc955934085f.json`.

No named `chaosx_ai_probability_auditor` collaboration route was callable from this task runtime, so no auditor-owned scenario matrix or compare claim is made.

### Decision-owned GUI inspection and rendering

The pre-repair status inspection returned `GUI_INSPECTED` with source revision `cddd27b9b2c3db9d16752e6b1678cbebf51f780dd9cd5fb3c6eee0eb4c2283fb` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/50eda0d42c9d048c06680b3935ec775a84946cf091a668b56f90089fd773ce7d/2a71011e9be99bbb6e7d469048f4ed6c1bd6b3674ec2abb6d66f9b1c900a3f0a/gui-inspect.cddd27b9b2c3db9d.json`.

The post-repair status inspection returned `GUI_INSPECTED` with the same source revision and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63101ee3ab1cdfb555c150b81df0dcb6c820e7aa777a8207090cbbeb950d6959/69d96b4875e724e9db8df81e5a047aa0f59231584979244a1cc5c8d77e5bae2a/gui-inspect.cddd27b9b2c3db9d.json`.

The post-repair status render returned `GUI_RENDERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c7e16cf09518e23ca3fb5593aa8c3af1f18934c15f4a2cdb3e23c0bb8557350e/63eccce59f82bdf67f54b5f9a13fdf7ecabb6a5781314ae0d019193b78009d24/independence_wave_status_window-full.svg`.

The pre-repair formable inspection returned `GUI_INSPECTED` with source revision `49a1697849d6fbfd513a438e5e866c141be9360d1e4c64cdd7b6d803cbdbfcf5` and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f57b5ab7122b11c32e120d309a77d879eda91866792ce84f5d4f13cc41f42767/77956ac556e01b39881ac3dfc893a360b166165adff0ae09a413b0092fec8f90/gui-inspect.49a1697849d6fbfd.json`.

The post-repair formable inspection returned `GUI_INSPECTED` with the same source revision and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7f8d293b77474a2399c1ebd04e04ed4f2f458bc9a7c741c21d99cab5d74746ef/89ef121e552a452c3cc0a769c2415b3b0a0ceefbd1ff1fb206b2a79d41b2cff9/gui-inspect.49a1697849d6fbfd.json`.

The post-repair formable render returned `GUI_RENDERED` with artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/40c9c1dc4076a3127c8f1c89cd80eff2796faa2f10621ee3623f182d7fe1c690/55e9671b9defddef03fd8fe5b41f66792c01f8552e21c23223dc8ba44aba621f/chaosx_independence_wave_formable_state_puzzle_w-full.svg`.

The GUI source revisions remained unchanged across the gate repair, confirming that no layout or asset source was modified by this patch.

## Validation

`python -B .tools/audit_event6_allocator.py --strict` passed with 149 publishers, 126 automatic or high-chaos candidates, 138 SCN-ranked candidates, 40 adapters, 32 attestations, 29 groups, the static 20-country witness, exact 3/4/5/7/10 counts, and no pre-event surface.

`python -B .tools/audit_event6_country_api.py` passed with 242 unique broader surfaces, 191 resolved carriers, zero missing definitions, zero duplicates, and the IW-031 crosswalk pass.

`python -B .tools/audit_event6_flags.py --strict` passed all 102 Event 006 tag families.

`python -B .tools/audit_event6_form16.py` passed the ARM, GEO, and AZR identity, state, consent, mutation, rollback, and readiness contract.

`python -B .tools/audit_event6_gui_matrix.py` passed the five tab contracts, frame families, cleanup variables, and static or animated sibling pairs.

`python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 player-facing cells and eight edge cases.

A direct source assertion confirmed that neither strict player-surface helper contains `is_independence_wave_event021_package_country`, that both require `is_independence_wave_active_country = yes`, and that the four adapter exclusions remain on `is_independence_wave_event6_player_surface_allowed`.

## Changed files and identifiers

Gameplay file touched by this repair: `common/scripted_triggers/006_independence_wave_triggers.txt`.

Repaired identifiers: `is_independence_wave_event6_local_content_active` and `is_independence_wave_event6_player_surface_allowed`.

The file also contains the concurrent `is_independence_wave_package_origin_compatible` addition, which was not changed by this audit.

Documentation file created by this repair: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_runtime_audit_2026-09-13.md`.

No files were staged or committed.

## Skipped meaningful validation and blockers

No live Hearts of Iron IV launch, save/load run, or in-game Event Log observation was performed because live consumer validation belongs to the user under `AGENTS.md`.

No `hoi4.gui_rewrite` was used because this repair changed only a scripted trigger and did not authorize a GUI layout edit.

No full probability scenario matrix, sensitivity sweep, or same-scenario comparison was claimed because the adapters reported incomplete candidate pools and required inputs, and the named probability-auditor route was unavailable.

The GUI renders were read-only production evidence, but the status render exceeded the MCP wire budget and the linked source graph retains overlap, dynamic-value, fallback, and blendframe warnings.

## Remaining risks and recommendations

The parent should review the concurrent `is_independence_wave_package_origin_compatible` helper against the accepted Event 021 bridge contract before promoting any Event 021 package surface.

The parent should retain the strict active-origin gates until an accepted design explicitly authorizes a separate Event 021 player surface.

The parent should keep the 32/29/40/161 boundary, the exact 3/4/5/7/10 ladder, and the no-pre-event surface unchanged while closing package, GUI, League, and probability evidence.

No additional decision or mission gameplay patch is recommended from this audit.
