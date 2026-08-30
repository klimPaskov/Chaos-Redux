# Event 006 decision surface completion — 2026-08-30

## Scope and disposition

This bounded tranche audits and repairs only the Event 006 decision-category lifecycle surface. It covers category visibility, package admission receipts, action and mission exposure, active-project locking, costs, AI scoring, localization, cleanup, and stale pre-event surfaces. No completed cost-gate work was repeated. The patch is source-backed and limited to six package category registrations.

The overall Event 006 objective remains **HOLD/PARTIAL**. This tranche does not admit any fail-closed package, add fallback content, redesign a category, or change cost, mission timing, AI weights, event flow, or scripted GUI layout.

Required repository guidance was consulted before source review: `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`. The offline Paradox wiki decision, effect, trigger, localization, data-structure, scope, modifier, on-action, event, idea, AI, interface, and scripted-GUI pages were read alongside the relevant vanilla documentation and vanilla decision/mission precedents. No live game launch or save/load claim is made.

## Issue list sorted by severity

### P2 — resolved: six admitted-looking package category shells lacked setup receipts

The FSM, FIJ, NAV, GLC, Sakha/YAK, and UDM category shells previously required only their exact package identity helpers. Those helpers require an active Event 006 country and package ID, but they did not prove that the package setup effect had completed. Their action and mission rows already used the stronger package-local `*_project_ready` predicates, so the category header could be visible while every action was unavailable and before the package’s setup receipt existed.

The category registrations now require both the exact package helper and the matching authoritative setup-complete flag. Setup effects clear and later set these flags, and the package-local action/mission gates already consume the same receipts. This closes the empty-shell window without widening admission or changing any gameplay outcome.

### P2 — unresolved validation boundary: weighted AI audit route is unavailable

No AI or probability value was changed in this tranche. The inherited source-qualified MCP traces cover the shared decisions and frontier missions, but the required custom `chaosx_ai_probability_auditor` route is not callable in this runtime. The exact blocker recorded by the parent audit is `TypeError: tools.mcp__hoi4_agent_tools__hoi4_probability_inspect is not a function`. No quantitative AI balance, normalized selection, or campaign-frequency claim is made.

### P2 — unresolved validation boundary: state-puzzle inspect timed out

The required read-only inspect for `chaosx_independence_wave_formable_state_puzzle_window` with scenario `event006_formable_activated_normal` timed out after the MCP 180-second limit. Its bounded render completed successfully with no blocking diagnostics. The timeout is recorded rather than treated as equivalent engine inspection.

### P3 — retained fail-closed adapter packages

IW-013, IW-015, IW-043, IW-058, IW-048, IW-050, IW-051, IW-177, and IW-179 remain adapter-only or otherwise fail-closed where their identity, source, rights, or package admission contracts require more evidence. This tranche only repairs category lifecycle exposure for the six packages whose setup receipts and action gates are already authoritative. It does not turn the other adapters into selectable content.

### P3 — no stale active pre-event surface found

The focused Event 006 category and decision scan found no active `wave_pressure`, crisis category, crisis cost, crisis queue, or retired release-barrier surface. Compatibility helpers remain hard-disabled or cleanup-only by contract, and SCN-008 queue handling remains the accepted scenario ledger path. No deletion was safe or necessary.

## Changed source and identifiers

Changed file: `common/decisions/categories/006_independence_wave_categories.txt`.

The following six category IDs changed from package-identity-only visibility to package identity plus setup receipt visibility:

* `independence_wave_fsm_micronesia_category` now requires `is_independence_wave_fsm_package = yes` and `has_country_flag = independence_wave_iw_179_setup_complete`.
* `independence_wave_fij_founding_congress_category` now requires `is_independence_wave_fij_package = yes` and `has_country_flag = independence_wave_iw_177_setup_complete`.
* `independence_wave_nav_iberian_category` now requires `is_independence_wave_nav_package = yes` and `has_country_flag = independence_wave_iw_013_setup_complete`.
* `independence_wave_glc_iberian_category` now requires `is_independence_wave_glc_package = yes` and `has_country_flag = independence_wave_iw_015_setup_complete`.
* `independence_wave_sakha_arctic_compact_category` now requires `is_independence_wave_yak_package = yes` and `has_country_flag = independence_wave_iw_051_setup_complete`.
* `independence_wave_udm_industrial_forest_category` now requires `is_independence_wave_udm_package = yes` and `has_country_flag = independence_wave_iw_048_setup_complete`.

Before the patch, an active exact-package country could expose these category shells as soon as package identity was assigned. After the patch, the shell remains hidden until the package setup receipt is present, and package-local action/mission availability remains unchanged. Because each setup flag is paired with the exact package helper, this cannot reintroduce a pre-event category for a normal country or a different package.

## Decision-category lifecycle notes

The shared categories continue to use the accepted lifecycle gates: active-origin admission for founding and status, provisional or recognized state for recognition and patron/network surfaces, explicit unlock flags for League, borders, formables, and high-chaos surfaces, and active-country or former-host checks for host administration. The scenario ledger remains committed-only and rejects failed/finalized state. Evolution and incident categories remain behind their existing active-origin gates.

Package categories continue to use package-specific country identity, setup, route, generation, compact, and failure predicates. The six repaired registrations now match the package-local `is_independence_wave_*_project_ready` contracts. IW-043 and IW-058 retain their broader adapter identity categories because their admitted source/rights/role contracts are intentionally separate and currently fail closed. IW-093 and IW-098, overlay categories, formable categories, and the shared status/state-puzzle windows were not altered.

## Cognitive-load notes

The shared surface remains phase-gated and does not expose the retired pressure meter, crisis queue, or pre-event category. Founding, government, recognition, security, host, patron, network, League, border, formable, high-chaos, and evolution actions are distributed across lifecycle categories rather than placed in one global wall of buttons. Existing package categories may contain longer sequential rows, but their visibility and project-ready gates phase them by route and completed receipts.

The earlier Event 006 audits cover the form03, form05, and form48 density decisions and accepted their phase/action contracts. This tranche adds no new raw values, tabs, panels, or explanatory prose. The shared status GUI communicates ledger state through its existing structured frames, and the state-puzzle GUI remains the accepted grouped formable surface. No visible value was changed without a corresponding meaning or threshold change.

## Mission quality notes

The core founding mission family remains owner-scoped to the active Event 006 country and founding category. Its requirements use the current-capital, activation, setup, aligned-array, resource, and route predicates already present in source. Duration and timeout fields use the centralized Event 006 duration constants. Success branches commit the intended setup or route result, while cancellation, timeout, failed-package, lost-capital, and ended-origin paths perform the existing cleanup. The shared active-founding-mission helper serializes overlapping founding missions.

The DM-01 starter/founding mission, DM-02 revenue or service mission, DM-03 registration mission, and DM-04/DM-05 route-opening missions retain their existing owner, category, region, requirement, duration, success, failure, and duplicate-risk contracts. Package founding missions for NAV, GLC, FSM, FIJ, Sakha/YAK, and UDM retain their package-local capital and setup gates, and their active-project helpers prevent duplicate timed projects. FORM auto first-session missions intentionally omit `cancel_effect` because their first-session completion/deadline lifecycle is owned by the formable contract; the setup and ratification cleanup paths remain unchanged.

No mission identifier, timeout, success effect, failure effect, or active-mission helper was changed by this tranche. The only mission-surface change is that six category shells no longer appear before the setup receipt that their missions already require.

## Cost and requirement clarity notes

No cost rows were changed because the completed Event 006 cost tranche already repaired the instant strategic-cost rows and the administration, diplomatic, security, and strategic custom-cost localization. The inherited audit reports 153 generic administration cost rows reserving factories, 191 custom cost keys resolving, and icon-first texticon coverage for spendable values. No visible gameplay-changing decision in this patch adds a fifth spendable type, spells out a resource name, or hides a cost in secondary prose.

The new category gates add no spendable requirement. They only require the package’s existing setup receipt, so the category header and its actions now disclose the same lifecycle boundary. Existing capital-control, route-lock, target-validity, and generation checks remain in their decision and mission triggers.

## AI validity and route-lock notes

No `ai_will_do`, target weight, MTTH, random-list, or strategy factor changed. The source-level validity audit still finds package-specific country identity, active-origin, living-target, capital-control, route, generation, formable, and active-project locks in their existing decision and mission predicates. The six setup receipt gates are non-weighted visibility checks and do not alter AI scoring.

The AJX Rhenish corridor survey remains a fire-only-once immediate survey. It is listed by the active-package helper, but it has no timed overlap window; adding a new lock without an accepted design requirement would be speculative, so it was not changed. Its adjacent paid and timed projects retain their existing active-project serialization.

## Localization and tooltip gaps

No localization key changed. The prior Event 006 localization audits found UTF-8 BOM files, icon-first custom cost text, concise package-neutral player wording, and no active player-facing `package` terminology in the audited route families. Category visibility changes use existing flags and do not introduce player-facing text. No tooltip or dynamic-localization gap was found that could be safely fixed within this category-only tranche.

## Cleanup and exploit-risk notes

The repaired gates are tied to setup flags that the package setup effects clear during reinitialization and set only after setup completion. This prevents a stale category shell from surviving a package-generation or setup rollover while leaving existing decision and mission cleanup authoritative. The allocator audit continues to report the pre-event crisis surface as retired with no category, mission, cost, or queue.

No free unit loop, equipment farming path, war-goal spam path, core-spam path, or cooldown bypass was introduced. Existing active-project, fire-only-once, timeout, route, and failed-origin cleanup remains unchanged.

## Mandatory GUI evidence

The shared status window was inspected read-only as `independence_wave_status_window` with scenario `independence_wave_status_default`. Inspect returned `GUI_INSPECTED`, revision `50c12bc58498786f`, validation passed, no blocking diagnostics, 48 selected elements, and zero unresolved resources. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63753b25dde5c394b606dfd3650ab6759d2088e1ed81779ea9548ed8270d149f/f2bccdeb8ad7493125202e8abf62f8f1a457546c4e031e404f8f08f76dd75ddb/gui-inspect.50c12bc58498786f.json`.

The same status window rendered successfully at 1920×1080 and 1280×720 across normal, warning, long-text, and missing-localisation states. Validation passed with no blocking diagnostics and zero changed pixels in the comparison. Full SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c50499c1ebe6b51447730518aac2be4ec9a45575bb4f5dc793bf95730110931/ad0ed5212d087eaf63a086bc3397ff2eb912af397ddc7848399640f54bbd823f/independence_wave_status_window-full.svg`. Full PNG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cff1425b3902b79554b2abd36c780c2070c50577dd4acee9ef10481ac75fb713/50b5a8bb326cd02693b219c632e3643202add92592736f26c98abf7a70b260c2/independence_wave_status_window-full.png`.

The formable state-puzzle window rendered successfully as `chaosx_independence_wave_formable_state_puzzle_window` with scenario `event006_formable_activated_normal` at both resolutions and eight requested states. Validation passed with no blocking diagnostics, no visible-overlap diagnostics, zero unresolved resources, and zero unsupported resources. Full SVG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0f62af8876d463158e58357ba1ea513b8702e60f9c3286d2bf5faa292449f121/f029c7e7e637ea81daec3e9f3b83c644cb6fd681a596c8f08b0dc81133a94573/chaosx_independence_wave_formable_state_puzzle_w-full.svg`. Full PNG artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/397d44367a8a781890ca2bc55c286a9b4f1f5d87c380f87d08bbe82d9d756820/03878356e5a3797d190066268291352bd87c8d59e2e07ed908aa68ef44aa3862/chaosx_independence_wave_formable_state_puzzle_w-full.png`.

The required state-puzzle inspect used the same window and scenario but timed out awaiting the MCP call after 180 seconds. No GUI rewrite was performed because this patch changes ordinary category visibility only and the completed production renders showed no in-scope layout or click-region defect.

## Validation evidence

The following task-specific validators completed successfully after the source patch:

* `python -B .tools/audit_event6_allocator.py` reported the pre-event crisis surface retired, 32 attested packages, 29 compatible reservation groups, and the existing adapter-only fail-closed set.
* `python -B .tools/audit_event6_scenario_matrix.py` passed all 32 SCN-008 cells and eight edge cases.
* `python -B .tools/audit_event6_gui_matrix.py` passed the Statehood Ledger semantic source matrix and its cleanup/static-animated sibling checks.
* `python -B .tools/audit_event6_flags.py` reported 102 registered Event 006 tags with complete flag families and zero incomplete families.
* `python -B .tools/audit_event6_country_api.py` reported zero missing and zero duplicate carrier mappings, including the IW-031 crosswalk.
* `python -B .tools/audit_event6_form16.py` passed the FORM-16 readiness, consent/refusal, mutation, rollback, and cleanup contract.
* A focused category lifecycle assertion passed for all six category/helper/setup-flag pairs.
* A focused Event 006 category and decision scan found no active pre-event pressure, crisis, cost, queue, or release-barrier references.

## Remaining blockers and simplifications

Live HOI4 execution, save/load, and gameplay completion were not run because repository guidance assigns live validation to the user. The custom probability-auditor route remains unavailable, so no quantitative AI balance claim is made. The state-puzzle inspect remains blocked by the 180-second MCP timeout even though its render completed. The broader Event 006 completion remains HOLD/PARTIAL pending its parent-owned admission, asset, route, event-chain, and probability evidence.

No fallback content, speculative redesign, localization rewrite, cost simplification, mission removal, AI-weight change, GUI rewrite, or unrelated file edit was made. No separate plan handoff was written because the issue was safely repairable within the existing category lifecycle contract.
