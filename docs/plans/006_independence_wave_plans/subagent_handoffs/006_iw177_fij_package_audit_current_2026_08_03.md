# Event 006 IW-177 FIJ country-package audit handoff (2026-08-03)

## Outcome

The existing FIJ/IW-177 country package is internally coherent in the current source, and this audit found no small, source-correct country-package defect to patch.

FIJ remains deliberately outside canonical Event 006 admission because the central content-attestation contract excludes `iw_177`, the Sukuna portrait has a circa-1940s source against the 1936 admission baseline, and FORM-39 member, X-tag, flag, identity, and route-adapter evidence remains closed.

No readiness flag, attestation flag, admission state, route-adapter flag, or fallback asset was created or changed by this audit.

## Authority and scope

The audit used `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, current completion evidence `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_current_completion_evidence_v102_2026_08_02.md`, the current FIJ package scripts, the offline Paradox wiki pages named by `AGENTS.md`, relevant vanilla HOI4 documentation, and vanilla FIJ history files.

The audit covered tag and package registration, state 636 anchoring and host survival, politics and leader setup, the generic focus contract, six FIJ decisions and the founding mission, lifecycle ideas and ledgers, dynamic starting forces, AI strategy, FORM-39 gates, cleanup, localisation, and visual consumers.

## Country-package coverage checklist

- Tag identity is coherent: `original_tag = FIJ`, package id `independence_wave_package_id.iw_177`, reservation group `rg_pacific_islands`, and anchor state 636 agree across the loader and package triggers.
- The package uses the vanilla FIJ carrier and does not replace vanilla `history/countries/FIJ - Fiji.txt` or `history/states/636-Fiji.txt`.
- `is_independence_wave_fij_package` and `has_prepared_independence_wave_iw_177_package_setup` are present and use the expected FIJ, IW-177, region, depth, archetype, anchor, host, law, route, focus, force, AI, and lifecycle contracts.
- FIJ origin leadership is registered through `FIJ_independence_wave_founding_congress_chair` and the hidden roster event, with ruling-only promotion handled by the setup effect.
- FIJ politics, elections, popularity, party names, provisional-authority state, ledgers, lifecycle ideas, and command structure are initialized by `independence_wave_setup_iw_177_fiji`.
- The package assigns the full shared `independence_wave_focus_tree` framework because vanilla FIJ exposes `generic_focus`; no bespoke FIJ tree is required by the current design.
- The six FIJ shared focuses are imported into the generic tree and have prerequisites, availability, reward adapters, bypass flags, and player-facing localisation.
- The founding-congress mission and six FIJ decisions have activation, costs, timers, cancel conditions, effects, and localisation.
- Dynamic starting-force mapping identifies FIJ profile `coastal_maritime`, military tradition `p177`, five reinforcement pathways, navy inheritance, and no research-sensitive dependency.
- FIJ AI strategy covers coastal congress survival, founding restraint, and severe-host-threat response with valid vanilla building and equipment category identifiers.
- FIJ cleanup removes package-specific mission, decisions, ideas, ledgers, lifecycle flags, formable selection, route flags, and leader retirement, while shared reset clears generic focus, AI, command-roster, and force-mapping runtime.
- Visual consumers resolve the FIJ country-leader portrait path, and no advisor or small-portrait asset is required by the current package.
- FORM-39 uses exact FIJ anchor 636 and explicit research, route, X-tag, flag, identity, invitation, and consent gates; the package is correctly fail-closed while those inputs are absent.

## File surface checklist

- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt` contains `is_independence_wave_fij_package`, FIJ leadership and stability triggers, active-project checks, and `has_prepared_independence_wave_iw_177_package_setup` at the current source lines around 32, 71, 104, and 435.
- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` contains FIJ origin preparation, politics, focus adapters, `independence_wave_setup_iw_177_fiji` around line 804, and `independence_wave_cleanup_iw_177_fiji` around line 1012.
- `common/scripted_effects/006_independence_wave_packages_region_13_effects.txt` contains `independence_wave_load_package_iw_177` around line 294 and preserves state 636 as the FIJ anchor.
- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` includes IW-177 in package dispatch and runtime preflight, while the central content-attestation list intentionally excludes IW-177.
- `common/scripted_effects/006_independence_wave_focus_effects.txt` and `common/scripted_triggers/006_independence_wave_focus_triggers.txt` implement the full shared-focus assignment and its contract.
- `common/national_focus/006_independence_wave_pacific_focus.txt` defines the six FIJ shared focuses, and `common/national_focus/006_independence_wave_focus.txt` imports FIJ roots into the shared tree.
- `common/decisions/categories/006_independence_wave_pacific_categories.txt` defines `independence_wave_fij_founding_congress_category`, and `common/decisions/006_independence_wave_pacific_decisions.txt` defines the founding mission and six FIJ decisions.
- `common/ideas/006_independence_wave_pacific_ideas.txt` defines `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`.
- `common/characters/006_independence_wave_pacific_characters.txt` defines the FIJ leader character, and `events/006_independence_wave.txt` event `chaosx.nr6.350` replenishes the hidden origin roster when needed.
- `interface/006_independence_wave_pacific_portraits.gfx` consumes `gfx/leaders/006_independence_wave/portrait_FIJ_independence_wave_founding_congress_chair.dds`.
- `common/ai_strategy/006_independence_wave_pacific.txt` contains the three FIJ AI strategy blocks.
- `common/script_constants/006_independence_wave_pacific_constants.txt` and `common/script_constants/006_independence_wave_force_package_constants.txt` provide FIJ tuning and the p177 force mapping.
- `common/scripted_triggers/006_independence_wave_form39_triggers.txt` and `common/scripted_effects/006_independence_wave_form39_effects.txt` own the exact FIJ member and FORM-39 readiness/cleanup contracts.
- `common/localisation/english/006_independence_wave_pacific_l_english.yml` contains the FIJ names, parties, leader, mission, decisions, focuses, ideas, category, and tooltips.

## Missing or stale country-package surfaces

No current gameplay surface is missing or stale enough to justify a local FIJ patch.

Older FIJ handoffs stated that `has_prepared_iw_177` required the FIJ FORM-39 route-adapter flag; the current trigger authority around `has_prepared_independence_wave_iw_177_package_setup` no longer requires that flag, and the current source-of-truth map is authoritative. This is a documentation-drift finding, not a code defect.

The installed HOI4 agent package exposes no Technology Tree Viewer, so technology-tree inspection remains an unresolved tooling limitation rather than a FIJ source defect.

## Map and state setup

Vanilla FIJ remains `history/countries/FIJ - Fiji.txt` with capital 636, and vanilla `history/states/636-Fiji.txt` remains owner ENG with FIJ core, province 4286 naval base 1, victory point 4286, and the original island-state data.

`independence_wave_load_package_iw_177` and `has_prepared_independence_wave_iw_177_package_setup` agree on state 636, and preparation requires FIJ to own and control the anchor while the former host remains alive and owns its protected state.

The static contract is safe, but live allocator output, host-survival behavior, state transfer, supply, and save/load persistence were not run because this agent must not launch HOI4 and no live allocator evidence was supplied.

## Politics, leader, portrait, flag, advisor, and party issues

FIJ setup initializes democratic elections and the constant-backed starting popularity split of democratic 44, communist 12, neutrality 34, and fascism 10, then registers four FIJ party-name localisation pairs.

`FIJ_independence_wave_founding_congress_chair` is a male centrism country leader with a full-size portrait consumer and no opposite-gender name or metadata pairing.

The FIJ leader texture and GFX basename resolve, but the accepted source is circa the 1940s while the Event 006 baseline is 1936. This remains a deliberate visual admission blocker and must not be solved with an unreviewed fallback or an invented portrait.

The package has no FIJ-specific flag override, advisor, operative, high-command, or small-portrait consumer requiring a missing asset.

## Focus, decision, idea, and asset issues

The six FIJ focus ids are `independence_wave_fij_convene_constituent_congress_focus`, `independence_wave_fij_register_communal_veto_focus`, `independence_wave_fij_open_labor_shipping_board_focus`, `independence_wave_fij_settle_colonial_accounts_focus`, `independence_wave_fij_charter_coastal_guard_focus`, and `independence_wave_fij_ratify_island_compact_focus`.

The six decision ids are `independence_wave_fij_convene_constituent_congress`, `independence_wave_fij_register_communal_veto`, `independence_wave_fij_open_labor_shipping_board`, `independence_wave_fij_settle_colonial_accounts`, `independence_wave_fij_charter_coastal_guard`, and `independence_wave_fij_ratify_island_compact`.

The mission id is `independence_wave_fij_hold_constituent_congress_together`, and its failure path calls the shared project-failure effect rather than leaving an orphaned project.

The three FIJ idea ids are `fij_unsettled_congress`, `fij_communal_charter`, and `fij_coastal_guard_compact`; lifecycle transitions remove superseded ideas before adding the next state, and cleanup removes all three.

Static extraction found no missing FIJ focus, decision, mission, idea, category, leader, or tooltip localisation, and all referenced FIJ texture paths exist.

Live focus rendering, route availability, decision timing, and tooltip display remain unperformed validation items.

## Starting military, technology, industry, supply, and production issues

The p177 force package is `coastal_maritime` with military tradition value 53, reinforcement mask 659, inheritance mask 1 for navy inheritance, and research-sensitive value 0.

Mask 659 resolves to five reinforcement pathways, matching the package trigger requirement and dynamic starting-force application contract.

FIJ setup preserves the vanilla carrier rather than replacing vanilla country history, and the package only adds the dynamic force profile after command-roster and current-generation checks pass.

No FIJ-specific technology tree, production-line, equipment, train, fuel, supply-capacity, railway, or industry override is present in the package; no static contradiction was found, but live materialisation, resource flow, production, and technology behavior remain unvalidated.

## AI and playability issues

`independence_wave_fij_coastal_congress_survival` enables army 78, infantry 55, support 45, convoy 80, fuel-silo 65, infrastructure 65, and dockyard 75 priorities.

`independence_wave_fij_founding_restraint` applies avoid-starting-wars -260 when no severe host threat or regional power condition is present, and `independence_wave_fij_host_threat` raises army and coastal-bunker priorities when severe host threat is detected.

The building and equipment identifiers match vanilla AI documentation and script-enum categories, so no source-correct syntax patch is indicated.

AI focus order, survival timing, threat response, naval inheritance, and scenario balance remain live-validation items.

## Deliberate admission and integration blockers

The central trigger `has_independence_wave_runtime_package_content_attestation_for_execution_id` intentionally omits `iw_177`; therefore runtime and scenario preflight correctly remain false even though an IW-177 dispatch branch exists.

The Sukuna portrait source-date review remains open because the circa-1940s image does not satisfy the 1936 baseline.

FORM-39 remains fail-closed until the explicit FIJ/PNG/WPG research and identity inputs are reviewed: `independence_wave_fij_melanesian_route_adapter_complete`, `independence_wave_fij_melanesian_member_research_complete`, `independence_wave_png_melanesian_member_research_complete`, `independence_wave_wpg_melanesian_member_research_complete`, `independence_wave_form39_x_tag_reserved`, `independence_wave_form39_flag_package_ready`, and `independence_wave_form39_identity_review_complete`.

The FORM-39 trigger also requires exact anchors FIJ 636, PNG 523, and WPG 669, frozen member and invitation arrays, consent, and no MFX collision; these are admission inputs and not patchable FIJ setup defects.

The current FIJ setup intentionally does not set `independence_wave_fij_melanesian_route_adapter_complete`, and the FIJ cleanup does not manufacture or clear the dedicated research receipts; changing either would alter the admission design without source approval.

## Changed files and behavior

Changed files: none.

Before and after behavior: identical; this was a read-and-audit handoff with no gameplay, localisation, asset, readiness, attestation, admission, map, or fallback changes.

## Validation performed

Static identifier and path checks covered FIJ tag and anchor consistency, focus and decision ids, localisation key coverage, GFX texture existence, character gender and portrait consumer, p177 force masks, AI building and equipment identifiers, FORM-39 anchor and gate names, and cleanup ownership.

Vanilla references checked `history/countries/FIJ - Fiji.txt`, `history/states/636-Fiji.txt`, vanilla AI documentation, vanilla building definitions, and vanilla script-enum categories.

Offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, countries, focuses, divisions, equipment, and technology were consulted as required by `AGENTS.md`.

## Skipped meaningful validation

Live HOI4 launch and in-game save/load validation were skipped because repository instructions reserve live consumer validation for the user.

Allocator execution, state transfer, former-host survival, dynamic force materialisation, focus rendering, decision timing, AI timing and balance, FORM-39 consent, and final MFX identity/flag review were skipped because no approved live evidence or admission inputs were available.

Technology-tree rendering and comparison were skipped because the installed package exposes no Technology Tree Viewer; this remains an unresolved tooling limitation.

## Remaining risks and handoff

FIJ cannot be admitted until the central attestation decision, Sukuna date/source review, FORM-39 research and identity receipts, and live execution evidence are resolved by the parent scope.

No simplifications were made by this audit, and no broad identity redesign, bespoke focus tree, advisor icon, fallback asset, or readiness shortcut was introduced.

No plan handoff is required because no broad redesign or unresolved local implementation defect was found; the admission blockers remain in the parent event plan and source-of-truth map.
