# Event 006 IW-022 Dalmatia overlay audit

Date: 2026-08-03.

Scope: current IW-022 Dalmatia vanilla-route overlay source after the parent repair that added `independence_wave_iw022_mobilize_adriatic_watch` and closed the watch-success legitimacy reachability gap. This is a source audit and handoff only; no gameplay source patch was authored by this audit.

Disposition: **PARTIAL / non-selectable overlay**. The bounded adapter is coherent for an additive CRO-origin dynamic-country route and the activation/settlement arithmetic repairs are source-complete, but it is not an independently admitted Event 006 country package. Focus ownership, planner admission, host-survival runtime evidence, save/load evidence, AI scenario evidence, and route-loss mission cleanup remain outside the closed source contract.

## Authority and references

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw022_dalmatia_overlay_adapter_2026_07_28.md` defines the original overlay-only contract.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_overlay_route_country_package_audit_v84_2026-08-01.md` keeps IW-022 non-selectable and records the D01-D50 carrier scope.
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_overlay_focus_contract_audit_2026_08_02.md` forbids an unreviewed focus import or focus-tree replacement for this overlay.
- `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv` records IW-022 as `reuse_vanilla_route_overlay`, `vanilla_route_overlay_only`, baseline states `103|163`, and reservation group `RG-ADRIATIC-TRIESTE-DALMATIA`.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` binds state 103 Dalmatia and optional state 163 Zadar while preserving `103=YUG|163=ITA` baseline ownership.
- Vanilla `common/national_focus/yugoslavia.txt` around the Dalmatia branch creates a dynamic country with `original_tag = CRO`, cosmetic tag `dalmatia`, and `transfer_state = 103`; no adapter-side creation or transfer was added.
- Vanilla `history/states/103-Croatia.txt` and `history/states/163-Dalmatia.txt` were consulted for the anchor, owner, controller, victory-point, port, and host-survival baseline.
- Required offline Paradox wiki pages were read from `paradox_wiki/`: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, and National focus.
- Vanilla documentation consulted: `documentation/script_concept_documentation.md`, `documentation/effects_documentation.md`, and `documentation/triggers_documentation.md`. The installed package exposes no Technology Tree Viewer, so technology inspection remains unresolved by tool limitation.

## Country package coverage checklist

| Surface | Result | Evidence and identifiers |
| --- | --- | --- |
| Exact identity and tag safety | PASS, source | `is_independence_wave_iw022_dalmatia_route_active` requires `exists = yes`, `is_dynamic_country = yes`, `original_tag = CRO`, and `has_cosmetic_tag = dalmatia` in `common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt:12-17`. No standalone tag is registered. |
| Dynamic carrier scope | PASS, source | `common/on_actions/006_independence_wave_iw022_dalmatia_on_actions.txt:10-59` defines only `on_daily_D01` through `on_daily_D50`; there is no global `on_daily` loop. |
| Map and states | PASS, static baseline | State 103 is the Dalmatian anchor and state 163 is optional Zara access. The adapter owns/controls only state 103 for coastwatch, mobilisation, and the watch objective. Read-only map inspection passed all five validations. |
| Host survival | PASS, preservation source; runtime unverified | The adapter never calls country creation, state transfer, autonomy, annexation, or host-state removal. Baseline host ownership remains YUG state 103 and ITA state 163 until vanilla dynamic-country logic acts. |
| Politics, parties, leaders, portraits, flags, advisors | PASS, preservation source | The carrier keeps its vanilla dynamic-country political and character surfaces. No country file, history file, party, leader, portrait, flag, advisor, or commander was added. |
| Decisions and mission | PASS after activation repair | Five visible action surfaces are present. The new `independence_wave_iw022_mobilize_adriatic_watch` calls the existing paid `independence_wave_iw022_dalmatia_start_watch_mission`, which activates `independence_wave_iw022_hold_adriatic_watch` despite `activation = { always = no }`. |
| Settlement reachability | PASS after legitimacy repair | `watch_legitimacy_gain = 27` is centralized in `common/script_constants/006_independence_wave_iw022_dalmatia_constants.txt:25`, applied by `complete_watch_mission`, and shown by the success tooltip. The normal municipal chain reaches `32 + 10 - 4 + 27 = 65`. |
| Ideas and lifecycle | PASS, source | Four route-gated ideas in `common/ideas/006_independence_wave_iw022_dalmatia_ideas.txt:27-66` are added/refreshed by lifecycle effects and removed on suspension. Their modifiers mirror the central constants through file-scoped fallbacks where static idea fields reject script constants. |
| Focus tree | Intentionally fail-closed | No `load_focus_tree`, `shared_focus`, generic carrier receipt, or static owner-tree replacement is present. The current focus contract requires a reviewed owner tree before any additive focus attachment. |
| Planner and dispatch admission | Intentionally fail-closed | IW-022 remains outside central package admission; the prior audit records `can_plan_independence_wave_package_iw_022 = { always = no }`. No dispatch OR-list entry was added. |
| AI | PASS, source only | Decision and mission `ai_will_do` blocks use centralized IW-022 constants. Read-only probability inspection found five decision candidates and one mission candidate with zero unresolved source diagnostics; the candidate pools are not complete without runtime scenario inputs. |
| Technology | Not applicable to adapter; inspection unresolved | The overlay changes no technology, doctrine, research slot, production, or equipment archetype. No Technology Tree Viewer is installed, so no technology-tree artifact is claimed. |
| Assets and localisation | PASS for current overlay surface | Shared decision icons and idea pictures are referenced; no package-specific asset is required. IW-022 localisation has 45 keys, no duplicate keys, and UTF-8 BOM. |

## File surface checklist

| File | Reviewed surface | Result |
| --- | --- | --- |
| `common/script_constants/006_independence_wave_iw022_dalmatia_constants.txt` | Values, costs, duration, outcome, modifiers, AI | PASS. `watch_legitimacy_gain = 27` now centralizes the settlement-threshold repair. |
| `common/scripted_triggers/006_independence_wave_iw022_dalmatia_triggers.txt` | Identity, state ownership/control, garrison, costs, settlement thresholds | PASS. State 103 is the hard anchor; `has_independence_wave_iw022_dalmatia_zara_access` for state 163 is defined but not consumed by the current decisions. |
| `common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt` | Initialization, payment, values, mission lifecycle, suspension/resumption | PASS for the active route. `start_watch_mission` is now called by a visible decision and `complete_watch_mission` uses the new legitimacy constant. Route-loss cleanup remains a design HOLD described below. |
| `common/ideas/006_independence_wave_iw022_dalmatia_ideas.txt` | Four lifecycle ideas and route-gated availability | PASS. No leader or country identity surface is overwritten. |
| `common/on_actions/006_independence_wave_iw022_dalmatia_on_actions.txt` | Carrier hook table | PASS. Exactly 50 Dxx keys invoke IW-022 and the shared IW-025 refresh; duplicate Dxx registration was not found in the mod. |
| `common/decisions/categories/006_independence_wave_iw022_dalmatia_categories.txt` | Category visibility and icon | PASS. Category visibility requires the active overlay flag and uses the existing shared decision icon. |
| `common/decisions/006_independence_wave_iw022_dalmatia_decisions.txt` | Five action/mission surfaces, costs, tooltips, cancellation, AI | PASS after parent repair. The mobilisation decision is at lines 57-90 and the inactive mission is activated by its complete effect. |
| `localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml` | Decision names/descriptions, costs, blocked text, effect tooltips, ideas | PASS after parent repair. The mobilisation keys and the corrected success tooltip are present. |
| `common/country_tags/`, `common/countries/`, `history/countries/`, `history/states/`, `common/national_focus/`, `common/characters/`, `common/ai_strategy/`, `interface/`, and `gfx/` | Potential standalone package surfaces | Intentionally untouched. The adapter reuses the vanilla carrier and shared UI assets. |

## Missing or stale country-package surfaces

- No Event 006 planner or dispatch admission exists for IW-022, by design. Promoting the adapter would require content attestation, package preflight, cleanup, focus ownership, host-survival, save/load, and runtime evidence.
- No safe focus attachment exists for the dynamic carrier. Adding `load_focus_tree` would replace the vanilla owner tree and adding carrier flags without a static import would expose no focus nodes.
- No package-specific flag, portrait, leader, advisor, or country-definition surface exists. This is correct for the current vanilla-route overlay contract, not an asset omission.
- `has_independence_wave_iw022_dalmatia_zara_access` is a valid optional state-163 ownership/control trigger but is currently unused by decisions or missions. Treat this as a future design hook, not a defect.
- The original adapter handoff states that route loss clears mission flags and values, but the current source only removes ideas, clears the active route flags, and marks the overlay suspended. The current source behavior is authoritative for this audit.

## Map and state setup issues

Read-only `hoi4.map_inspect` for states 103 and 163 returned `MAP_INSPECTED`, status `ok`, and passed file/definition checks, bitmap geometry, state-region membership, networks/adjacencies, and positions/ports. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5bc6c36b81bc4bc311fbd40720218a5dc9a46695edab78b8119e01a31c7a2def/a7c9a5b6e883eda1cf5402c63bbc1b3fad6e73d40a7b95ec4ba02e91d1a78c9c/map-inspect.a95e99f4e9c82ab9.json`.

State 103 is the only hard ownership/control anchor used by the adapter. State 163 remains an optional Zara access state and is not transferred or required for watch completion. No map rewrite was necessary or safe inside this overlay audit.

## Politics, leaders, portraits, flags, advisors, and parties

The exact dynamic carrier identity preserves vanilla CRO-origin Dalmatia politics, parties, leaders, portraits, flags, and history. The adapter does not invent a person, institutional portrait, gender metadata, party, or symbol. Any future identity redesign would need a separate source-reviewed country plan and must not be folded into this overlay.

## Focus, decision, idea, and asset issues

The parent repair adds the missing visible mobilisation action while preserving the inactive mission pattern used by the adjacent IW-025 and IW-035 overlays. Before the repair, `independence_wave_iw022_dalmatia_start_watch_mission` had no caller, so the mission could not be activated and both settlement decisions were unreachable. After the repair, mobilisation checks the existing guard cost and state-103 ownership/control, pays through the existing scripted effect exactly once, clears stale interruption state, sets `watch_running`, resets the hold ledger, and calls `activate_mission`.

The settlement arithmetic is now reachable through both branches. The municipal branch requires port coordination and municipal legitimacy at 65; the documented chain is `28 + 24 + 10 + 10 = 72` port coordination and `32 + 10 - 4 + 27 = 65` legitimacy. The security compact branch remains reachable through port coordination and coastal security at 65. No focus icon, idea icon, flag, portrait, or country asset was added.

## Starting military, technology, industry, supply, and production issues

The adapter does not create units, add free equipment, alter technologies, add research slots, change production lines, rewrite industry, or change supply capacity. It consumes command power, manpower, trains, infantry equipment, support equipment, and army experience through the existing cost effects. The carrier retains the vanilla dynamic-country army, equipment, technology, industry, production, railway, port, and supply setup. This is suitable only for an additive overlay and is not evidence of a separately balanced country package.

## AI and playability issues

The mobilisation AI weight is high in peacetime and war, but is multiplied by the disabled constant when no qualifying division is in state 103. A human can still click the decision when the cost and anchor gates pass without a garrison, then pay the guard cost and allow the mission to fail; this is an intentional risk surface documented by the localisation, not a source defect found in this audit.

Read-only `hoi4.probability_inspect` on the current decision source returned `PROBABILITY_SOURCE_INSPECTED` with validation passed, five decision candidates, nine required inputs, and zero unresolved diagnostics. The mission source returned the same result with one candidate, five required inputs, and zero unresolved diagnostics. Both artifacts report `poolComplete = false`, so no runtime AI or survival claim is made. Decision artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b2fac27973556ff607718e09b0bc4a2413963f1b23c981060188ee58de0ec281/adc935f4c93d46af687a945c7a07b045336245cb73d552f32988ca2bcb8216c1/probability-inspect-47bcb9351b23.json`. Mission artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e820904df23859bcd57113c994fe33ac16c97174a6d58f366040e4e3b24ece76/e69c276258068fa531c85a366728a308b8fb253f4aa52a0fe0ce1954f840ba27/probability-inspect-47bcb9351b23.json`.

## Route-loss cleanup HOLD

The current source has a design-sensitive stale-mission path when a carrier permanently loses the exact CRO-origin Dalmatia identity while the watch is running. `independence_wave_iw022_dalmatia_suspend_overlay` sets `watch_interrupted`, removes ideas, and clears the active route flags. The inactive branch of `independence_wave_iw022_dalmatia_refresh_overlay` then calls `independence_wave_iw022_dalmatia_pause_watch_mission`, which adds one day to the active mission timeout on every Dxx hook while the mission remains active. `independence_wave_iw022_dalmatia_fail_watch_mission` is gated by `is_independence_wave_iw022_dalmatia_overlay_active = yes`, so timeout cannot clear the running/interrupted flags while the carrier remains inactive. If the carrier remains in D01-D50, the mission may therefore remain indefinitely paused with stale flags.

This is not patched because the intended policy is not specified. The owner must choose one of a permanent pause, a bounded suspension grace period, or explicit mission cancellation and flag cleanup on permanent identity loss. A fix must also preserve temporary identity interruptions and route resumption semantics.

## Validation performed

- Offline wiki and vanilla documentation requirements were satisfied for the decision, mission, effect, trigger, idea, on-action, localisation, focus, country, and AI surfaces.
- Read-only map inspection for states 103 and 163 passed all five map validations; no map write was attempted.
- Read-only probability inspection after the parent repair found five decision candidates and one mission candidate with zero unresolved source diagnostics; neither pool was complete for runtime evaluation.
- Static scans over the seven IW-022 script files found balanced braces, even quote parity, and no unsupported literal `<=` or `>=` operators.
- Localisation scan found 24 player-facing decision/mission field references with no missing keys, no duplicate keys, and UTF-8 BOM bytes.
- The carrier hook scan found exactly `on_daily_D01` through `on_daily_D50` and no duplicate Dxx key in the IW-022 hook file.
- No Hearts of Iron IV process, live event execution, save/load trace, host-survival trace, or runtime AI scenario was run, per repository instructions.

## Changed files and before/after behavior

No gameplay source file was authored by this audit. The current review snapshot includes the parent repair in:

- `common/decisions/006_independence_wave_iw022_dalmatia_decisions.txt` (`independence_wave_iw022_mobilize_adriatic_watch`).
- `localisation/english/006_independence_wave_iw022_dalmatia_l_english.yml` (mobilisation strings and success tooltip).
- `common/script_constants/006_independence_wave_iw022_dalmatia_constants.txt` (`watch_legitimacy_gain = 27`).
- `common/scripted_effects/006_independence_wave_iw022_dalmatia_effects.txt` (success effect consumes `watch_legitimacy_gain`).

Before: the paid watch-start effect had no decision caller, and the inactive mission could not be activated; the municipal settlement threshold was also unreachable through the normal ledger/coastwatch/watch sequence. After: mobilisation explicitly starts the mission and the success effect closes the legitimacy threshold with a centralized 27-point gain. Route-loss cleanup remains unresolved by design choice.

## Simplifications, omissions, and blockers

- IW-022 remains intentionally non-selectable and is not a standalone country package.
- No new tag, country history, state transfer, autonomy change, focus-tree route, leader, portrait, flag, advisor, formable, map rewrite, or technology package was added.
- Shared focus ownership and route-network/league/formable integration remain unproved and fail-closed.
- Host survival, suspension/resumption, save/load persistence, and live AI behavior remain unverified.
- The indefinite pause/stale mission path on permanent route identity loss is a design-sensitive HOLD requiring an explicit cleanup policy.
- The installed Technology Tree Viewer is unavailable, so no technology-tree artifact is claimed.
- No fallback implementation was used and no simplification was silently promoted.
