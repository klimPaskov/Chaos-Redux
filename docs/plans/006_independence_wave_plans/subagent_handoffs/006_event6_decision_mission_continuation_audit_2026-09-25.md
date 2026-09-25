# Event 006 decision and mission continuation audit

Date: 2026-09-25.

Disposition: PATCHED, with open evidence gates. Event 006 remains HOLD/PARTIAL; this handoff does not promote a package or claim whole-event completion.

## Scope and authority

This tranche audited Event 006 decision categories, decisions, timed missions, cost helpers, category and package gates, relevant event/on-action callers, English cost consumers, and the two decision-owned scripted GUI surfaces. It used the accepted mechanics and decision spec, the decision/mission matrix, the current source-of-truth map and resume packet, the 2026-09-20 decision receipt, the 80-row body crosswalk, the cost audit, the equality repair, and the IW-179 FSM audit. None of those authority documents was edited.

The accepted design remains the only design authority: docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md and docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv. Package attestation remains fail-closed. Soviet Collapse separation and vanilla trees were preserved.

The source inventory covered the 24 common/decisions/006_independence_wave*decisions*.txt files: 006_independence_wave_balkan_decisions.txt, 006_independence_wave_bashkiria_mari_decisions.txt, 006_independence_wave_decisions.txt, 006_independence_wave_far_eastern_decisions.txt, 006_independence_wave_form01_02_04_decisions.txt, 006_independence_wave_form03_decisions.txt, 006_independence_wave_form05_decisions.txt, 006_independence_wave_form48_decisions.txt, 006_independence_wave_formable_decisions.txt, 006_independence_wave_frontier_decisions.txt, 006_independence_wave_iberian_decisions.txt, 006_independence_wave_iw043_iw058_decisions.txt, 006_independence_wave_iw093_iw098_decisions.txt, 006_independence_wave_karelia_crimea_decisions.txt, 006_independence_wave_mediterranean_decisions.txt, 006_independence_wave_minor_overlay_decisions_registry.txt, 006_independence_wave_pacific_decisions.txt, 006_independence_wave_rhineland_bavaria_saar_decisions.txt, 006_independence_wave_scotland_wales_decisions.txt, 006_independence_wave_shared_decisions.txt, 006_independence_wave_siberian_decisions.txt, 006_independence_wave_transcaucasus_decisions.txt, 006_independence_wave_wallonia_frisia_decisions.txt, and 006_independence_wave_western_decisions.txt.

The adjacent category registry, decision/mission scripted effects and triggers, owner helpers, event and on-action callers, 37 Event 006 English localisation files, and the status and formable-puzzle cost consumers were read for the bounded crosswalk. The prior body-level receipt covers 80 accepted rows, including 62 decision/mission rows and 18 FORM03 rows, and 79 custom-cost triplets. Its known open items remain probability evidence, native decision-row rendering, campaign/runtime evidence, and FSM category density.

Required references were read before Chaos Redux source: the offline wiki snapshots for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding; installed HOI4 documentation for triggers, effects, script concepts, decisions, on actions, and scripted GUIs; and vanilla AFG/AUS decision precedents. AUS factory-allocation decisions pair civilian_factory_use with a free-factory availability condition, including the pattern at common/decisions/AUS.txt:2733-2736.

## Severity-sorted findings

### P1 — Fixed: nine displayed civilian-factory commitments lacked matching affordability gates

The accepted cost strings and decision modifiers committed civilian factories, but nine rows did not require the matching free-factory capacity in both available and custom_cost_trigger. This could advertise a payable action whose displayed factory commitment was not affordable. The patch now checks the exact shared constant or calls the existing factory-aware helper, with inclusive equality.

- DM-10 independence_wave_establish_treasury_and_currency in common/decisions/006_independence_wave_decisions.txt now gates independence_wave_decision_cost.civilian_factory_major in both blocks, alongside can_pay_independence_wave_administration_standard_cost.
- DM-16 independence_wave_coordinate_recognition_campaign and DM-42 independence_wave_request_collective_recognition in the same file now use can_pay_independence_wave_diplomatic_standard_factory_cost in both blocks.
- independence_wave_form0124_authorize_full_integration in common/decisions/006_independence_wave_form01_02_04_decisions.txt now gates civilian_factory_standard in both blocks.
- independence_wave_form02_chart_convoy_routes and independence_wave_form04_establish_public_peace_court in that file now use the existing diplomatic-standard factory-aware helper in both blocks.
- independence_wave_cor_secure_mountain_post_road in common/decisions/006_independence_wave_mediterranean_decisions.txt now gates civilian_factory_light in both blocks.
- independence_wave_arx_restore_cagliari_shipping_office in that file now uses the existing diplomatic-standard factory-aware helper in both blocks.
- independence_wave_hbx_settle_federal_asset_ledger in common/decisions/006_independence_wave_pacific_decisions.txt now uses the existing diplomatic-standard factory-aware helper in both blocks.

Before the patch, each affected row could pass its decision/cost trigger without proving the displayed factory allocation. After the patch, the allocation is checked against the same light, standard, or major constant used by the cost display and decision modifier, and equality passes. The underlying payment helper, amount, duration, effect, route gate, package predicate, and AI weight are unchanged. Factories remain an allocation commitment through civilian_factory_use, not a newly consumed stockpile debit.

The DM-16/DM-42 helper already checks command power and the accepted convoy-or-train transport path as well as factory capacity. FORM-02, FORM-04, ARX, and HBX use that same matching helper. DM-10 and COR retain their existing spendable-cost helpers and receive only the missing direct factory-capacity condition. FORM0124 retains its existing diplomatic stockpile gate and receives the accepted two-factory threshold.

### P1 — Open: IW-179 Micronesia can expose more than six primary actions

independence_wave_fsm_micronesia_category in common/decisions/006_independence_wave_pacific_decisions.txt has one founding mission and eight clickable decisions. Source gates allow four government-route flags to coexist before a route is chosen; when the three common actions and the autonomous mandate are also visible, the source permits eight primary actions at once. This is a source-level maximum, not a claim about a rendered campaign state. The existing route visibility gate already requires stable inter-island authority, but it does not reduce the four simultaneous route choices once that state is reached. A phase/hide decision requires parent design review; this tranche did not add or move a surface.

### P1 — Open: state-puzzle GUI inspection reports clipping and zero-size elements

The production inspect for chaosx_independence_wave_formable_state_puzzle_window reported GUI_ACCIDENTAL_CLIPPING and GUI_INVALID_SIZE on state-puzzle elements with 0×0 dimensions, including independence_wave_form01_summary and independence_wave_form01_state_14_piece. Its production PNG render was generated at 1920×1080/UI scale 1 with normal and long-text states. These diagnostics remain open and were not dismissed as renderer differences. GUI layout source was outside the permitted decision/mission patch scope.

The status window independence_wave_status_window also produced layered-overlap warnings and partial animated-asset rendering because the offline animation Lua step did not run. The user-visible rendered images could not be opened in this environment: the Codex browser had no tab for the queued artifact and rejected the hoi4-agent:// URI under its browser URL policy. That route was not retried through a workaround. Parent review should treat the inspect/render findings as unresolved visual evidence.

### P2 — Open: native decision-row inspection/render is absent

The connected HOI4 MCP exposes GUI inspection/render and probability tools but no hoi4.decision_inspect, decision-row render, or native decision-row compare route. Event and focus inspection are not substitutes. The decision lists were source-audited, but rendered row density, native cost placement, clipping, and row click regions remain unverified.

### P2 — Open: probability auditor has not returned scenario evidence

A read-only chaosx_ai_probability_auditor task was dispatched for the Event 006 decision and mission weights as required, agent 01a0d92b-361d-7163-a3ea-f6f1a9ec1bea. It remained pending after bounded waits. No probability inspection/evaluation/compare artifacts or scenario-specific conclusions were available for this handoff. No AI weight, score, target, MTTH, or selection formula was changed.

## Decision category lifecycle

Shared categories continue to use Event 006 local-content and phase gates; package categories retain their package identity, setup receipt, route, and origin gates. Formable actions remain local to their existing categories and do not create a new player-facing surface. Package admission, reservations, adapters, the central allocator, Join/SCN-008, Soviet Collapse, and vanilla focus trees were not changed.

The FSM category lifecycle still depends on the IW-179 setup receipt and package predicate. Its founding mission and ordinary projects remain subject to the existing one-active-project helper and cleanup. The four government-route choices are hidden until stable authority and route flags permit them, and central route selection remains the route-lock authority.

## Cognitive-load notes

The source inventory is broad and contains many package-local actions, but the accepted row-level matrix remains the authority for which actions belong to each owner and phase. The prior body-level crosswalk found no new title/description mismatch in its 80 accepted rows. English names, descriptions, effect tooltips, and custom-cost triplets resolved in the reviewed source set; no localisation change was needed.

FSM is the identified visible-action density risk: up to eight primary actions plus the founding mission can align after setup and stable authority. No native decision-row render route is available to confirm the actual in-game row count or spacing.

Player-facing factory values have clear cost meaning through their cost strings and matching civilian_factory_use modifiers. The status GUI and state puzzle contain dynamic values and state indicators, but inspect diagnostics flag unresolved puzzle sizing/clipping and status-layer overlap; visual significance and legibility were not approved from source alone. There is no source-based proof here that every campaign has at most three concurrent active missions, because native decision-row and campaign runtime evidence are not available.

## Mission quality notes

The accepted matrix supplies owner, phase/category, visible requirements, duration band, success direction, failure direction, and cleanup for its 28 named mission designs. The existing body crosswalk links those designs to implementation rows; no additional owner/requirement/terminal mismatch was proven in this continuation. Regions are the matrix row's owning country/package, capital or economic anchor, state/claim, target host/member, or formable region, as applicable.

- DM-01 through DM-03 are released-country Emergency Founding missions centered on the controlled/supplied capital, economic anchor, and locally peaceful territory. Their accepted duration bands run from 30 to 150 days; success establishes security, administration, legitimacy, capacity, or manpower, while timeout or cancellation can produce relocation, salary/corruption, resistance, or autonomy consequences. The active founding-mission gate and terminal flags limit duplicate starts.
- DM-04, DM-05, and DM-10 are released/suitable-country Provisional State missions gated by legitimacy/capital, local authority support, or the revenue-service/economic anchor. Their matrix bands run from 120 to 270 days; success opens the accepted route or treasury tools, while failure can empower rival factions or produce inflation/debt/patron-control effects. Route flags, one-time completion flags, and active-project checks constrain duplicates.
- DM-15, DM-16, DM-25, DM-26, DM-28, DM-30, DM-35, DM-42, DM-43, and DM-47 cover recognition, bilateral negotiation, host threats, patron balance, and league work for the released country, target host, member, or league owner in their accepted phases. Requirements and durations are row-specific in the matrix (45–300 days); outcomes include recognition, settlement, arbitration, defensive readiness, or leadership/league changes, with failure consequences such as isolation, host pressure, confidence loss, or regional backlash. Target-death, route, one-active-campaign, per-pair, cooldown, or emergency-lockout guards apply where the design requires them.
- DM-17, DM-20, and DM-23 are country-owned militia, border, and army missions tied to available pools, controlled sectors, manpower, training, and equipment. Their accepted bands run from 90 to 360 days; success produces the corresponding integration/readiness/template result, while failure can create warlord, local-abuse, cost-overrun, or militia-resistance consequences. Their pool, sector, and tier gates bound repeatability.
- DM-48, DM-49, DM-50, DM-52, DM-54, DM-56, and DM-58 are region/state/target/formable-scoped survey, plebiscite, transfer, integration, congress, and reclamation operations. Their accepted bands run from 90 to 540 days; success follows the matrix's local-support, control, consent, or transfer result, while failure can cause host detection, fraud, refusal, unrest, secession, or league fracture. Per-state, per-region, per-pair, family-congress, or one-operation locks limit duplicate effects.
- FORM03-D11 is owned by the LCX carrier in the ratification phase, requires both values at least 70 plus resolved status and a real language scope, and runs for 360 days. Its terminal outcomes are the full compact or the accepted compromise/rupture path at timeout; it is activated once from the convergence focus.
- IW-179's package-owned founding mission is independence_wave_fsm_keep_island_federation_connected in common/decisions/006_independence_wave_pacific_decisions.txt. Its category is the FSM Micronesia category and its region is the island federation; activation requires the package/setup receipt and unresolved founding state, success requires stable authority and valid capital control, and package/receipt/capital loss or timeout reaches the failure path. The prior 2026-09-20 FSM receipt records its cancellation and cleanup behavior; the active-project helper prevents a duplicate.
- Eight synthetic charter/first-session/convoy/procurement/basing deadlines use activation = { always = no } and available = { always = no } as automatic mission hooks. Their lack of AI weights is intentional; they are not player-selectable AI alternatives.

The current review found no new free-unit, equipment-farming, repeated-core, repeated-war-goal, uncapped congress, or post-cleanup project loop. The prior FSM receipt's separate shared diplomatic transport equality concern remains an owner follow-up; it is outside these nine factory-gate patches and was not reclassified as fixed here.

## Cost and requirement clarity

All nine affected rows stay within the four-distinct-type cap. DM-10 shows command power, manpower, and factory allocation (three types). DM-16/DM-42/FORM-02/FORM-04/ARX/HBX show command power, the existing convoy-or-train transport path, and factory allocation (three displayed categories). FORM0124 shows command power, its transport path, and standard factory allocation (three). COR shows command power, infantry equipment, support equipment, and factory allocation (four).

The reviewed English cost keys use the matching texticons: £command_power, £manpower_texticon, £civ_factory, £infantry_equipment_text_icon, and £support_equipment_text_icon; the dynamic diplomatic transport helper supplies its accepted icon and text. Base, tooltip, and blocked cost keys remain aligned. Spendable costs are separate from non-consumed requirements such as capital control, setup receipt, route availability, recognition, and active-project locks. No literal resource labels, fifth hidden spendable type, or new cost prose was introduced.

## AI validity and route-lock notes

No AI block, target, formula, or route permission was changed. The source gates continue to bind country/package owners and require the accepted current origin/setup state. Event 006's central attestation boundary remains fail-closed; this work did not admit or promote any package. No dead-country target or disabled-evolution target was proven in the reviewed rows. Weight quality remains open until the dispatched probability auditor returns its MCP scenario evidence.

## Localisation and tooltip gaps

No localisation file was changed. The nine rows retain their existing name, description, cost, blocked-cost, success/failure, and effect-tooltip keys. The reviewed English resource costs use texticons, and the 80-row receipt's 79 base/tooltip/blocked triplets remain aligned. No additional localization or tooltip gap was established.

## Cleanup and exploit risk

The patch adds no effect, payment, flag, timer, target, cooldown, or repeat path. Existing activation, visibility, target validity, cancel/timeout, terminal flags, and package cleanup remain as reviewed in the matrix and current handoffs. No admission, setup-receipt, package, Join, reservation, or central-adapter behavior changed.

## Changed files and behavior

- common/decisions/006_independence_wave_decisions.txt — DM-10, DM-16, and DM-42 affordability/cost-tooltip gates.
- common/decisions/006_independence_wave_form01_02_04_decisions.txt — FORM0124, FORM02, and FORM04 affordability/cost-tooltip gates.
- common/decisions/006_independence_wave_mediterranean_decisions.txt — COR and ARX affordability/cost-tooltip gates.
- common/decisions/006_independence_wave_pacific_decisions.txt — HBX affordability/cost-tooltip gates.
- docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_decision_mission_continuation_audit_2026-09-25.md — this audit and patch receipt.

No decision, mission, GUI, or localization identifiers were added or renamed. No localization key was edited. Before behavior allowed the affected factory costs to be advertised without the matching free-factory gate; after behavior checks the displayed constant in both available and custom_cost_trigger, while keeping the accepted debit, effect, route, duration, and AI behavior unchanged.

## Meaningful validation and evidence

- The source comparison reviewed all nine changed decision blocks against their displayed cost keys, factory-use modifiers, existing helper definitions, accepted matrix row, and vanilla factory-allocation precedent.
- The previous source receipt's 80-row implementation crosswalk, 79 cost triplets, and shared cost helper review were used for cross-reference; no source-of-truth document was edited.
- hoi4.gui_inspect and hoi4.gui_render were run for both decision-owned GUI surfaces before this handoff. Status window: independence_wave_status_window, scenario independence_wave_status_default, source revision 53e18602b8914c9b4b411614eadce3c7626dacaa58497f140e4e9602903e7fc7, inspect artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d215571f2ccb3cccefaee68359d81a35affb6efa69f4719c8b82808c9593fcb3/681e73d3a6ab4d90c4930485585416a3cdf0ab1535da0f02945ebf254bec0718/gui-inspect.53e18602b8914c9b4b411614eadce3c7626dacaa58497f140e4e9602903e7fc7.json.
- Formable puzzle: chaosx_independence_wave_formable_state_puzzle_window, scenario E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09, inspect artifact hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f2d08f9fa5ecdd977f0928588f51302d95ec322e8951c97dd800306fa675eb6b/c502c53e391d872e3aa86e40c783b9b0ce4e13b7a47a9073bd7de472d4a887de/gui-inspect.876aa84a739b6f1b.json, and production PNG hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/f22c90067284d545a23a234ad9678d4c548d2280a0a7d9c7d912db9bffdf680f/chaosx_independence_wave_formable_state_puzzle_w-full.png.
- The vanilla precedent read in common/decisions/AUS.txt:2733-2736 checks available civilian factories when a decision has a factory-use modifier.
- No tests were run, per the explicit task instruction. Hearts of Iron IV was not launched.

## Skipped meaningful validation and blockers

- Native decision-row inspect/render and click-region comparison were skipped because that MCP route is not exposed.
- Scenario-specific decision/mission probability evidence remains pending from agent 01a0d92b-361d-7163-a3ea-f6f1a9ec1bea; no probability claims are made.
- The production GUI PNGs could not be opened due the browser's blocked hoi4-agent:// artifact navigation. Inspect/render diagnostics are preserved above, and no visual issue is dismissed.
- Live campaign, save/load, and runtime execution were not performed; the user owns live-game validation, and the task excluded gameplay launch and logs.

## Simplifications, omissions, and blockers

No mechanic, package, cost, route, AI score, mission, or GUI layout was simplified or redesigned. The nine changes only align affordability and the cost-tooltip gate with accepted factory commitments. The FSM action-density review, puzzle-layout diagnostics, native decision-row evidence, and probability audit remain open and prevent a whole-event completion claim.

Plan handoff path: none created; this continuation report is the required handoff.

## Skills used

Applied chaos-redux-decisions-missions, chaos-redux-events, chaos-redux-subagents, and chaos-redux-scripted-gui. No skill was created or updated.