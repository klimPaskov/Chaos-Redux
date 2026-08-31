# Event 006 decision visibility and cost audit

Date: 2026-08-31

Scope: Event 006 decision and mission visibility, pre-event exposure, player-facing cost localisation, and decision-owned GUI evidence. This audit did not launch Hearts of Iron IV and did not modify gameplay, localisation, interface, event, country, or scripted-effect source files.

Disposition: PARTIAL / HOLD for parent review. The pre-event surface is correctly fail-closed and the ordinary cost rows are compact and icon-first, but several accepted Event 006 surfaces still exceed the four-spendable-type contract or use a native flat political-power cost. The required probability worker route is unavailable in this runtime, and the current GUI render exposes defects that are outside this decision/localisation-only patch boundary.

Follow-up (2026-08-31): the parent applied `006_event6_iw095_security_cost_readability_repair_2026-08-31.md`. The two IW-095 security decisions now use the four-resource security cost row and disclose their retained one-factory duration reservation in the decision descriptions. The first finding below is therefore an audit baseline for the pre-repair source; no gameplay payment or reservation was removed.

## Severity-sorted findings

1. High — `independence_wave_cost_security_standard_factory` displays and reserves five distinct spendable types for `iw095_organize_civic_guard` and `iw095_authorize_emergency_directorate` in `common/decisions/006_independence_wave_decisions.txt:4082` and `:4248`: manpower, army experience, infantry equipment, support equipment, and a civilian-factory commitment. The matching normal and blocked rows are icon-first at `localisation/english/006_independence_wave_decisions_l_english.yml:50` and `:104`, but localisation must not conceal the fifth charge; the gameplay owner must reduce the action to at most four spendable types or split the commitment into a clearly separate phase.

2. High — `independence_wave_formable_commit_cost_revolutionary` and `independence_wave_formable_commit_cost_military` expose seven spendable resource families in `localisation/english/006_independence_wave_formable_registry_l_english.yml:29-30`: stability, command power, transport, manpower, army experience, infantry equipment, and support equipment. They are selected dynamically by `GetIndependenceWaveFormableCommitCostText` and consumed by `independence_wave_formable_pay_selected_commit_cost`; this requires a gameplay-owner balance decision, not a cosmetic shortening of the row.

3. Medium — six route-opening decisions in `common/decisions/006_independence_wave_iw093_iw098_decisions.txt:102,160,219,699,754,810` use native `cost = constant:...conference_political_power_cost` with a 100 political-power charge and no `custom_cost_text`. Native decision cost rendering is compact, but this contradicts the Event 006 design contract's “no flat political power cost” guidance and should be migrated by the gameplay owner only if the route retains an explicit payment and matching blocked/effect text.

4. Medium — the category declarations contain seven or eight child actions in some states: security has seven, host relations seven, network seven, and patrons eight in `common/decisions/006_independence_wave_decisions.txt` (the other shared categories contain three to six). Most extras are phase, target, route, or mission-cap gated, but no current engine decision projection proves that every phase stays at six or fewer visible primary actions; retain this as a state-matrix review item.

5. Medium — the mandatory current render for `independence_wave_status_window` reports `GUI_TAB_STATE_CONFLICT` and an incomplete state matrix, plus static-fallback warnings for four animated sprites. This is an event-owned scripted GUI surface and is outside the requested decision/localisation patch boundary; route the exact GUI identifiers to `chaosx_event_ui_worker` before accepting the window as visual evidence.

6. Low — `independence_wave_cost_patron_balance` deliberately has `Start:` and `Later:` rows because it represents staged charges, but its repeated command-power and transport entries are dense. It remains readable and icon-first; do not remove the labels without changing the staged-payment contract.

## Decision-category lifecycle notes

- The Event 006 specification explicitly requires no pre-event category, mission, pressure meter, cost, queue, or history indication in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md:9-15`.
- The shared founding, government, security, and host-relations category gates in `common/decisions/categories/006_independence_wave_categories.txt:51-74` require `is_independence_wave_package_content_active = yes` (host relations also requires a living former host).
- Recognition and patron categories use `is_independence_wave_provisional_or_later`; that trigger is itself package-active gated in `common/scripted_triggers/006_independence_wave_decision_triggers.txt:14-30`.
- Network, league, borders, formables, and high-chaos categories require active/provisional/recognized/regional phase predicates and their unlock flags in `common/decisions/categories/006_independence_wave_categories.txt:80-125`; these predicates resolve through the package-active contract rather than stability, resistance, occupation, or host-pressure heuristics.
- `is_independence_wave_active_country` and `is_independence_wave_package_content_active` are origin/adapter predicates in `common/scripted_triggers/006_independence_wave_triggers.txt:9-46`; neither opens a player surface for generic world-state pressure.
- The public Event 006 paths set `independence_wave_event6_runtime_unlocked` only after committed release/report delivery in `events/006_independence_wave.txt:35-58`. This is consistent with the required post-event reveal.
- The scenario ledger is separately gated by the committed global flag, the local display flag, and a non-empty blocked-package list in `common/decisions/categories/006_independence_wave_categories.txt:639-651`; its three navigation controls have zero cost and `ai_will_do = { base = 0 }`, so they are not a passive political-power store.
- No `common/decisions/006_independence_wave_crisis*.txt` files are present, and the focused allocator validator reports the pre-event crisis surface as retired with no category, mission, cost, or queue.

## Cognitive-load notes

- Shared category child counts from the current source are founding 5, government 6, recognition 6, security 7, host relations 7, patrons 8, network 7, league 6, borders 5, formables 4, high-chaos 3, and scenario ledger 3.
- The over-six categories use target validity, route flags, phase thresholds, one-shot flags, and active-mission caps to suppress most children, but the source-only count is not an engine guarantee; the parent should require a scenario projection for the simultaneous-visible maximum.
- Central missions are serialized by `activation` and `has_independence_wave_active_*_mission` checks, with DM-01 through DM-05 in the founding block, DM-17, DM-20, and DM-23 in security, DM-30 in host relations, DM-35 in patrons, and DM-45 in the league block. Package files add 86 `days_mission_timeout` sites, including 18 explicitly selectable missions.
- The central player-facing values are legitimacy, recognition, government capacity, security, and instability; the founding and government category descriptions expose those values in `localisation/english/006_independence_wave_decisions_l_english.yml:2-5`, while the league and high-chaos descriptions expose league cohesion, common cause, patron capture, shared reserve, member confidence, revisionist pressure, and completed actions at `:14-17`.
- Each displayed central value has a named consequence in the decision descriptions and specification, but the league category still exposes eight simultaneous numeric lines; a compact meter or threshold presentation remains preferable if the GUI owner revisits that surface.
- Decision descriptions are generally one concise consequence sentence and do not expose raw trigger blocks. `independence_wave_cost_reclamation_front_tooltip` appends two requirement counts after the icon row, which is useful but should remain visually separated from spendable costs.

## Mission quality notes

- DM-01 `independence_wave_secure_provisional_capital` is a passive opening mission intentionally opened by `independence_wave_start_provisional_capital_mission`; its source has a reserved-cost disclosure, capital-control and garrison cancellation, timeout success, failure event, and one-shot AI weight in `common/decisions/006_independence_wave_decisions.txt:21-82`.
- DM-02 through DM-05 use explicit `activation`, selectable mission state, dynamic material affordability, bounded timeout, success and timeout effects, cancellation, and one-shot flags in the founding block. This satisfies owner/category/region-or-capital/requirement/duration/success/failure shape at source level for the central opening sequence.
- DM-17, DM-20, DM-23, DM-30, DM-35, and DM-45 follow the same active-mission serialization pattern, with route or phase gates and timeout/cancel effects. DM-17 and DM-20 share the security mission-cap predicate, while DM-23 additionally requires recognition, the professional-army unlock, and DM-17 completion.
- The package missions use country-specific owner, capital/state or regional target predicates and package constants for duration. Static review found no new generic pre-event mission surface, but the large package pool still needs the unavailable worker-mediated probability/availability pass before balance completion.
- Missions generally clear active flags on success, timeout, or cancel and apply bounded failures. Duplicate-risk review remains most important where package overlays and generic categories can both be present; package triggers consistently include package-active predicates, while invitation candidate categories intentionally rely on post-event carrier/invitation proofs.

## Cost and requirement clarity

- A focused source scan found 699 `custom_cost_text` consumers across 26 Event 006 decision/category files and 192 unique custom-cost keys. The 37 Event 006 English localisation files contain a normal, `_blocked`, and `_tooltip` triplet for every discovered custom-cost key; no triplet was missing.
- Explicit central cost rows use the correct texticons for stability, command power, manpower, army experience, infantry equipment, support equipment, civilian factories, fuel, convoys, and trains. Dynamic transport selectors resolve to convoy/train icon rows through `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt:165-194`.
- Normal and blocked rows are compact icon-first sequences separated by `·`, `/`, or a necessary staged newline. No central row spells out a resource name in place of its texticon.
- `independence_wave_cost_security_standard_factory` is the confirmed five-type exception and must not be “fixed” by deleting the factory token from localisation while its modifier remains in the decision.
- The two revolutionary/military formable rows are confirmed seven-type exceptions and must be simplified in the formable payment owner, not hidden behind `GetIndependenceWaveFormableCommitCostText`.
- `independence_wave_cost_selected_formable_commit_blocked` is a generic blocked explanation rather than the exact selected-family charge. A dynamic blocked selector would improve precision, but it belongs with the formable payment/localisation owner and was not changed here.
- The three scenario-ledger `cost = 0` controls at `common/decisions/006_independence_wave_decisions.txt:953,990,1020` are navigation controls and intentionally do not consume a resource.
- Native political-power costs remain in the six IW-093/IW-098 route-opening decisions listed above. Transcaucasus package effects also subtract political power for several custom-cost rows; those rows are already represented with icon-first custom localisation, so replacing them cosmetically would risk desynchronizing payment effects.

## AI validity and route-lock notes

- Central AI blocks use shared constants and route/phase/resource gates; target decisions use `target_root_trigger` and `target_trigger` checks for living former hosts, patrons, network members, league members, and valid states.
- The source retains zero AI weight for scenario-ledger navigation, which is appropriate for player-owned display controls.
- Package and formable invitation triggers include exact carrier, generation, family, member, consent, anchor, and route checks. Invitation candidates do not need to be active Event 006 origins themselves because invitations are issued post-event by an active carrier; a blanket active-origin gate would break that accepted flow.
- No quantitative probability sign-off is claimed. The callable tool inventory contains direct `hoi4.probability_*` routes but no `chaosx_ai_probability_auditor` subagent route, and the GUI MCP transport closed before a second formable-window query could run. Per the project rules, direct MCP output cannot be presented as the required worker-mediated probability audit.

## Localisation and tooltip gaps

- All discovered custom-cost keys have complete normal/blocked/tooltip coverage across the Event 006 English files.
- The staged patron row and its blocked variant are intentionally labeled `Start:` and `Later:` so the player can distinguish the initial reserve from the later balancing charge.
- The selected-formable blocked row lacks the exact family-specific cost breakdown and should be paired with the future four-type payment redesign.
- The six native-PP conferences lack Event 006 `custom_cost_text` rows; if converted, they need exact normal/blocked/tooltip localisation and an inline negative PP payment in the owning decision effect.
- No pre-event crisis or pressure localization key was found in the focused decision/category/localisation scan.

## Cleanup and exploit-risk notes

- The central decisions use `fire_only_once`, cooldowns, active-mission caps, target clearing, route locks, and explicit cancel/timeout effects. The source comments and the specification prohibit world-iteration stores and repeatable recognition or equipment farming.
- Formable and league actions retain generation, family, consent, target, and active-operation locks; stale target and active-operation cleanup is present in the reviewed decision/effect paths.
- The main remaining exploit review is the five/seven-type cost mismatch: any attempt to remove a visible charge without removing its corresponding modifier or payment effect would create a hidden-cost or free-action exploit.
- The GUI status window's animated fallback warnings are visual-state risks, not a reason to add a fallback pressure or pre-event surface.

## Required follow-up recommendations

- Gameplay owner: redesign `iw095_organize_civic_guard` and `iw095_authorize_emergency_directorate` in `common/decisions/006_independence_wave_decisions.txt` and their payment helper so the displayed and consumed security-standard-factory charge contains no more than four spendable types.
- Formable owner: redesign `independence_wave_proclaim_military_union` and `independence_wave_formable_pay_selected_commit_cost` with at most four spendable types, then update `localisation/english/006_independence_wave_formable_registry_l_english.yml` and the dynamic blocked selector together.
- Decision owner: decide whether the six IW-093/IW-098 conference decisions should remain native PP costs or become explicit compact custom-cost rows with matching effect payment; do not silently remove the native cost.
- UI owner: route `independence_wave_status_window` and `chaosx_independence_wave_formable_state_puzzle_window` to the event UI worker for the required state/resolution/click-region repair. This audit did not edit `interface/006_independence_wave.gui` or any shared GUI.
- Probability owner: rerun the named `chaosx_ai_probability_auditor` workflow when that callable route is available, using the same founding, resource-starved, former-host-threat, network-ready, league-ready, route-lock, and formable-impossible scenarios.

## MCP and static evidence

- Focused validator: `python .tools/audit_event6_allocator.py` completed successfully and reported `pre-event crisis surface: retired; no category, mission, cost, or queue`.
- Current status-window inspect: `hoi4.gui_inspect`, window `independence_wave_status_window`, scenario `independence_wave_status_decision_visibility_cost_audit_2026_08_31`, status `ok`, 48 inspected elements, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4be01b08e61325a72850fd7c070446455a3b6768f5c15633dd2df50c61d6002c/32994c370b07337a1379f4b579c6e1b7917fc5427ca627cc6b2f2fc5b3a6ebff/gui-inspect.66b9f968c76e0163.json`.
- Current status-window render: `hoi4.gui_render` covered normal, active, warning, long-text, and missing-localisation states at 1920x1080 and 1280x720, status `ok`, 27 artifacts, full render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1c44bf62df862216410bd68f15e23278866a65534e7fdc5f3ceff56e1f9fc57b/7ba60e923c5bb9a4f540888ba4b8c0be05f81b9f58a69c62549f67eb458a4d19/independence_wave_status_window-full.svg`, validation `passed = false` because of `GUI_TAB_STATE_CONFLICT` and incomplete state coverage.
- The required formable-window inspect/render attempt for `chaosx_independence_wave_formable_state_puzzle_window` used scenario `independence_wave_formable_state_puzzle_visibility_cost_audit_2026_08_31` and returned the exact MCP error `Transport closed`; no current artifact is claimed. Historical artifacts in prior Event 006 handoffs are not treated as current evidence.
- Direct decision/mission inspection is not exposed by the installed MCP inventory. Source counts and lifecycle tracing are therefore not engine decision projection evidence.

## Changes, validation, and blockers

- Changed files in this tranche: only this handoff document.
- Changed decision, mission, scripted-GUI, or localisation IDs: none.
- Before behavior and after behavior: unchanged, because no safe gameplay/localisation patch was applied.
- Meaningful validation run: focused allocator validator, custom-cost triplet scan across all 37 Event 006 English files, direct-cost scan, category/mission source census, and mandatory read-only GUI inspect/render attempts.
- Skipped meaningful validation: worker-mediated AI probability analysis was skipped because `chaosx_ai_probability_auditor` is absent from the callable tool inventory; the formable GUI pass was blocked by the exact `Transport closed` MCP failure; no live-game test was run per instruction.
- Simplifications, omissions, and blockers: no fallback or hidden-cost simplification was introduced. The five- and seven-type cost designs, six native political-power costs, over-six source category declarations, GUI state conflict, and missing probability-worker route remain explicitly queued for their owning agents.
