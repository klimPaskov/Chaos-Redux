# Focus cleanup baseline handoff: Events 001-020

Date: 2026-08-22

Mode: read-only baseline audit. This pass wrote only this handoff. No gameplay source, focus source, localisation, asset, `interface/*.gui`, focus inlay, `common/scripted_guis`, or other GUI source was modified. `hoi4.focus_rewrite` was not called.

## Scope and governing constraints

This audit covers national-focus definitions, focus-loading effects, shared focus hooks, focus-related scripted triggers, and static focus consumers belonging to Events 001-020. Event-specific Event 021+ focus trees were not audited. Shared infrastructure was inspected only where it is a consumer or loader for the selected Event 001-020 focus surfaces.

Functional selectors, content, toggles, and scripted-GUI bindings remain inspection-only evidence. No `interface/*.gui` coordinate, sizing, hierarchy, visual, or layout recommendation is made. GUI assets, focus inlays, and `common/scripted_guis` are not cleanup targets in this baseline.

The repository rules, cleanup master prompt, and the full required skills were read before source review: `AGENTS.md`, `docs/plans/repo_cleanup/chaos_redux_repo_cleanup_master_prompt.md`, `.agents/skills/chaos-redux-focus-trees/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The required offline wiki pages were read: Data structures, National focus modding, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Installed vanilla documentation read for this surface included `documentation/script_concept_documentation.md`, `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`, and `documentation/modifiers_documentation.md`. Vanilla precedents included `common/national_focus/germany.txt` for tree structure and `common/on_actions/07_nsb_on_actions.txt` for a focus-tree replacement that pairs `load_focus_tree` with `mark_focus_tree_layout_dirty`.

The audit used a brace-aware static parser and repository-wide exact-token searches. Static results are useful for ownership and cleanup triage, but they are not a substitute for engine execution. Weighted focus logic is explicitly handed to `chaosx_ai_probability_auditor`; no probability rewrite or balance claim is made here.

## Overall verdict

The selected source set contains 3,289 ordinary focus definitions and 134 `shared_focus` definitions. The ordinary focus IDs are unique, all selected prerequisite, mutual-exclusion, and relative-position references resolve statically, and no event-prefixed dead tree or focus reference was found in the scanned scripted consumers. Localisation and custom icon source coverage are also complete by static checks.

The highest-confidence maintainability issue is inconsistent focus-tree replacement hygiene. Event 006 and Event 012 use explicit replacement policy plus `mark_focus_tree_layout_dirty`, and the vanilla Polish restoration precedent does the same. Several other Event 001-020 loaders replace a tree without an adjacent layout refresh, while the Event 005 shared loader also relies on the engine default for `keep_completed`. These are bounded follow-up candidates, not patches made by this baseline.

The main behavior debt is weighted-focus coverage and route-aware selection, not missing syntax. Event 003 has 48 of 111 focuses without an `ai_will_do` block, Event 020 Rat has 17 of 52 without one, and Event 020 Rat King has 57 of 71 without one. The Event 003 and Event 020 specifications require route-aware AI behavior; every weighted focus surface must go through the named probability auditor before any owner-applied change.

No source-side dead-ID, missing-localisation, or missing-icon defect was proven. Event 003 has an engine-rendered layout warning profile worth a separate route-layout decision, but its crossings and intersections are not a reason to perform a broad coordinate migration during cleanup. Event 005's repeated successor families and Event 012's overlay families need semantic route/reward review rather than mechanical deduplication.

## Route coverage table

| Event | Focus source and static coverage | Loading and shared-hook evidence | MCP evidence and disposition |
| --- | --- | --- | --- |
| 001 Communism Spread | No Event 001-specific `common/national_focus` file, non-empty focus tree, or Event 001 tree ID was found in the scoped inventory. This is not proof that no specification ever desired a tree; confirm ownership against `docs/specs/001_communism_spread_specs/`. | No Event 001 focus loader was found in the selected consumer scan. | No layout claim is made. Keep as a spec/ownership confirmation item rather than inventing a tree. |
| 002 Zombie Outbreak | `common/national_focus/002_zombies.txt` contains `ZZZ_focus` with 0 focus definitions. | No non-empty Event 002 focus replacement hook was found. | `hoi4.focus_inspect` returned `ok` for `ZZZ_focus`; render returned `ok`. The empty tree is a source fact, not an icon or parser error. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f4305f1c90d6e38289d4686b3bd215abfefd2813ab916b35add3b7a59c60b9b/5f9d7bdef0304f9efcb93802c3192e6a312a7e95e0e2ff0e9bdbcce6572de7fe/focus-inspect.25707cddff7c7170.json`; render artifacts are linked below. |
| 003 Holy Realm | `common/national_focus/003_holy_realm.txt` defines `THR_focus` with 111 focuses. The Event 003 brief targets a focused 75-95 node tree with trunk, teaching/meditation, governance, diplomacy, industry, anti-chaos, Final Silence, and schism routes. | `common/scripted_effects/003_holy_realm_effects.txt:1868` loads `THR_focus` with `keep_completed = no` but has no adjacent `mark_focus_tree_layout_dirty`. | Inspect succeeded. Metrics were 129 connectors, 25 crossings, 21 node intersections, and 7 long connectors. Tree-specific render succeeded at review scale 0.25; file-level render hit `ARTIFACT_STORAGE_LIMIT`. The layout metrics are a follow-up candidate, not a baseline patch. |
| 004 Random War | No Event 004-specific focus source or tree ID was found in the scoped inventory. Confirm against `docs/specs/004_random_war_specs/` if a future focus package is expected. | No Event 004 focus loader was found. | No layout or route conclusion is made. |
| 005 Soviet Collapse | `common/national_focus/005_soviet_collapse_ancient_restorations.txt` has 76 focuses, `005_soviet_collapse_custom_splinters.txt` has 1,035, `005_soviet_collapse_factory_successors.txt` has 134, and `005_soviet_collapse_republics.txt` has 515, for 1,760 ordinary focuses across the ancient, custom, factory, and republic families. | `common/scripted_effects/005_soviet_collapse_effects.txt:10537-10611` has nine shared release branches without explicit `keep_completed` or adjacent layout refresh. The repeated successor setup blocks at `:21601-22822` use explicit `keep_completed = no` but duplicate route-specific load sites. | The representative `INX_soviet_collapse_ancient_focus_tree` inspect/render was clean: 20 focuses, 24 connectors, 0 crossings, 0 intersections, and 0 long connectors. Do not generalize that clean result to every 005 family. Broad loader migration and route redesign are deferred. |
| 006 Independence Wave | `006_independence_wave_focus.txt` has 184 ordinary focuses and 23 shared focuses. Three auxiliary files add 111 shared focuses: `006_independence_wave_iw043_iw058_focus.txt` has 48, `006_independence_wave_iw093_iw098_focus.txt` has 43, and `006_independence_wave_pacific_focus.txt` has 20, for 134 shared focuses total. This matches the shared, package-gated architecture rather than bespoke country trees. | `common/scripted_effects/006_independence_wave_focus_effects.txt:58` loads the full framework with `keep_completed = no`, and `:83` marks the layout dirty. Additive mode deliberately does not replace an existing meaningful tree. Preserve this pattern. | Inspect succeeded for `independence_wave_focus_tree`: 184 focuses, 195 connectors, 0 crossings, 0 intersections, and 3 long connectors. Render succeeded. Artifact links are listed below. |
| 007 Fury | `common/national_focus/007_fury_focus_tree.txt` defines 52 focuses in the shared Fury tree. | `common/scripted_effects/007_fury_effects.txt:217` uses shorthand `load_focus_tree = fury_focus_tree` without explicit `keep_completed` or an adjacent layout refresh. The player exclusion is present in `common/scripted_triggers/007_fury_triggers.txt:22-38`: `is_ai = yes`, non-major, non-subject, non-capitulated, and player-linked-country rejection. Do not report a missing player guard. | Inspect succeeded: 52 focuses, 64 connectors, 1 crossing, 0 intersections, and 3 long connectors. Both render attempts timed out after 180 seconds. Treat layout render as unresolved engine evidence. |
| 008 Tensions Rising | No Event 008-specific focus source or tree ID was found in the scoped inventory. Confirm against `docs/specs/008_tensions_rising_specs/` if a future tree is expected. | No Event 008 focus loader was found. | No layout or route conclusion is made. |
| 009 White Peace | No Event 009-specific focus source or tree ID was found in the scoped inventory. Confirm against `docs/specs/009_white_peace_specs/` if a future tree is expected. | No Event 009 focus loader was found. | No layout or route conclusion is made. |
| 010 Death | `common/national_focus/010_death_focus_tree.txt` defines 26 focuses. | `common/scripted_effects/010_death_effects.txt:456` loads `death_focus_tree` with `keep_completed = no`; `:509` loads `generic_focus` with `keep_completed = no`. Neither load has an adjacent layout refresh. The generic fallback is a valid fallback and is not a deletion candidate. | Inspect and render calls both timed out after 180 seconds. No layout claim is made from source alone. |
| 011 Secret Alliance | No Event 011-specific focus source or tree ID was found in the scoped inventory. Confirm against `docs/specs/011_secret_alliance_specs/` if a future tree is expected. | No Event 011 focus loader was found. | No layout or route conclusion is made. |
| 012 Africa | `012_africa_continental_focus_tree.txt` has 276 focuses, `012_africa_priority_member_focus.txt` has 8, and the six world overlay files have 121 combined focuses. Total selected ordinary focus count is 405. | Continental, priority, host-transfer, and world-order loaders at `common/scripted_effects/012_africa_effects.txt:1634-1669`, `012_africa_priority_member_effects.txt:264-275`, `012_africa_host_transfer_effects.txt:1284-1296`, and `012_africa_world_order_effects.txt:2337-2669` pair tree loads with layout refreshes. The host-transfer helper has both a direct continental load and a helper load; do not deduplicate without dynamic call-chain proof. | No successful 012 tree-specific MCP artifact was obtained in this pass. Source evidence shows the strongest loading hygiene in the selected mod; no layout conclusion is made. |
| 013 Natural Disasters | No Event 013-specific focus source or tree ID was found. The Event 013 specification explicitly says not to add a broad disaster-recovery focus tree unless separately requested. | No Event 013 focus loader was found. | This absence is consistent with the current scope note; no tree redesign is proposed. |
| 014 Cannibalism | `common/national_focus/014_cannibalism_focus.txt` defines 108 unified, 68 warlord, and 28 Wendigo focuses, for 204 total. | `common/scripted_effects/014_cannibalism_effects.txt:5193`, `:12399`, and `:18988` load the three trees with `keep_completed = no` but no adjacent layout refresh. The Wendigo loader has narrow gates for original ZZZ, Wendigo eligibility, reveal, overlay availability, character, no world-end, and not already loaded. | The unified-tree inspect timed out after 180 seconds; no layout claim is made. A bounded refresh candidate exists after dynamic gate review. |
| 015 Utopia Manifesto | `common/national_focus/015_utopia_manifesto_focus_tree.txt` defines 124 focuses. | `common/scripted_effects/015_utopia_manifesto_effects.txt:316` loads with `keep_completed = no`; a later refresh helper marks the layout at `:1019`. Whether every load path reaches that helper is unresolved. | No successful 015 tree-specific MCP artifact was obtained. Treat refresh timing as uncertain dynamic ownership, not a proven duplicate or missing hook. |
| 016 Brilliant Scientist | `common/national_focus/016_brilliant_scientist_kruger_state_focus.txt` has 100 focuses and `016_dhrondan_focus_tree.txt` has 88, for 188 total. | Kruger loads with `keep_completed = no` at `common/scripted_effects/016_brilliant_scientist_country_effects.txt:676,1095`, and the active-Kruger refresh helper marks the layout at `common/scripted_effects/016_brilliant_scientist_focus_effects.txt:310`. Dhrondan intentionally uses `keep_completed = yes` at `common/scripted_effects/016_dhrondan_country_effects.txt:262` but has no adjacent mark; preserve `yes` until identity/continuation policy is confirmed. | No successful 016 tree-specific MCP artifact was obtained. No layout or AI conclusion is made from source alone. |
| 017 Random Faction | No Event 017-specific focus source or tree ID was found in the scoped inventory. Confirm against `docs/specs/017_random_faction_specs/` if a future tree is expected. | No Event 017 focus loader was found. | No layout or route conclusion is made. |
| 018 Resources Found | `common/national_focus/018_resources_found_cave_focus_tree.txt` defines 67 focuses against the 45-65 target in the Event 018 brief. The count variance is not itself a cleanup defect. | `common/scripted_effects/018_resources_found_cave_effects.txt:63` loads with `keep_completed = no` without an adjacent layout refresh. | Inspect timed out after 180 seconds, so render/engine layout evidence is blocked. Do not simplify or remove nodes from source count alone. |
| 019 Infantry Spawn | `common/national_focus/019_infantry_spawn_derivative_focus.txt` defines 45 focuses, matching the shared 30 plus five-family structure in the brief. | `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:576` loads with `keep_completed = no` without an adjacent layout refresh. | Inspect succeeded: 45 focuses, 54 connectors, 0 crossings, 0 intersections, and 0 long connectors. Cohort diagnostics report 5 siblings with 1 asymmetry and 4 off-anchor placements, max deviation 16; this is low-priority readability evidence. Render timed out after 180 seconds. |
| 020 Black Plague | `common/national_focus/020_black_plague_rat_focus_tree.txt` defines 52 Rat focuses and `020_black_plague_rat_king_focus_tree.txt` defines 71 Rat King focuses, for 123 total. This is within the 40-50 Rat and 70-100 Rat King role-tree targets except for the one-node Rat overage. | `common/scripted_effects/020_black_plague_rat_effects.txt:1399` and `:2564` load the two trees with `keep_completed = no` and no adjacent layout refresh. | Rat inspect/render succeeded: 52 focuses, 50 connectors, 0 crossings, 0 intersections, and 0 long connectors. Rat King was not separately rendered in the successful sample. AI gaps are listed below. |

## Static ownership, dead-reference, and helper results

The selected ordinary focus definitions numbered 3,289 and were unique. The selected `shared_focus` IDs numbered 134, giving 3,423 defined focus identifiers across the selected source set. No duplicate definition group was found.

All prerequisite, mutual-exclusion, and relative-position references found in the selected focus files resolved to the selected ordinary or shared focus IDs. The scan found zero unresolved references. This does not cover dynamic `meta_effect`, scripted localisation, or runtime-generated identifiers that never appear as literal tokens.

The consumer scan covered the selected focus IDs and shared IDs across `common/scripted_effects`, `common/decisions`, `common/events`, `common/on_actions`, `common/ai_strategy`, and `common/ai_strategy_plans`. It found zero unresolved event-prefixed dynamic focus references and zero unknown event-prefixed `load_focus_tree` IDs. The 27 apparent Event 006 consumer hits are valid references to the 134 shared focus IDs, not dead IDs.

No stale ordinary focus ID was proven by literal-token search. Dynamic helper ownership remains uncertain for `meta_effect` and event-target paths, so a deletion candidate must receive an additional dynamic call-graph review before removal.

The Event 012 host-transfer path at `common/scripted_effects/012_africa_host_transfer_effects.txt:1284-1296` is the clearest duplicate-looking loader candidate: it contains a direct continental load followed by a helper that may load the same tree. The two calls can be gated differently, so this is an uncertain dynamic reference and must not be removed by text deduplication.

## Icon coverage table

| Surface | Static result | Disposition |
| --- | --- | --- |
| Focus icon tokens | 2,848 unique icon IDs across the selected focus files | Complete by source scan. |
| Mod plus vanilla sprite definitions | 0 missing icon definitions | No icon-definition cleanup candidate. |
| Mod plus vanilla texture paths | 0 missing focus icon textures | No asset deletion or replacement candidate. |
| Focus shine definitions | 0 missing `_shine` definitions | No interface or GFX change proposed. |
| MCP diagnostics | Several successful MCP calls report missing generic/vanilla base icons because the tool scan included `game:common/continuous_focus/generic.txt` but did not include the corresponding vanilla `interface/goals.gfx` and `goals_shine.gfx` files | Treat as MCP input-scope/base-asset false positives. The static mod-plus-vanilla scan is the stronger source-side result for this cleanup pass. |

The Event 003, Event 006, Event 007, Event 019, and Event 020 MCP diagnostic lists contain these base-palette warnings. No selected custom focus icon was missing in the source-plus-vanilla asset scan. GUI assets and focus inlays remain inspection-only.

## Localisation and reward mismatch list

The localisation parser checked both the conventional focus key forms, `<focus_id>` and `<focus_id>_focus`, plus each description key. All 3,289 selected ordinary focuses have a name and description key in the mod localisation set. No missing focus localisation key was found.

Every selected ordinary focus has a `completion_reward` block and an icon token. No absent reward block or stale icon reference was proven. This is structural coverage only; it does not prove that a title, description, reward, decision, idea, leader, claim, core, war goal, event, or formable hook is semantically aligned.

The following semantic review items remain open rather than being called defects:

- Event 005's custom, factory, and regional families contain repeated source patterns. Compare reward text and route identity before extracting any helper; use the family-specific IDs in `common/national_focus/005_soviet_collapse_custom_splinters.txt`, `005_soviet_collapse_factory_successors.txt`, and `005_soviet_collapse_republics.txt` as the review boundary.
- Event 012's continental and world-overlay rewards need route-level review against the Event 012 specification. Do not remove apparently generic rewards without checking the package flags and world-order helper calls in `common/national_focus/012_africa_*.txt` and `common/scripted_effects/012_africa_*_effects.txt`.
- Event 002's `ZZZ_focus` is empty. If the Event 002 design ever promises a player-facing tree, that is a missing design/package decision, not a safe cleanup patch.
- The Event 003 tree has 111 focuses against the brief's 75-95 target. Decide whether the extra support nodes are intentional before any route or reward simplification.
- Event 018 has 67 focuses against its 45-65 planning target. Treat the one-node overage as a design review item only.

## AI behavior gaps and probability handoff

Static AI-block coverage is high in most selected trees, but route-aware behavior is not equivalent to merely having a base weight. The focus-level no-AI counts are:

| Tree family | Focuses | No `ai_will_do` | Follow-up |
| --- | ---: | ---: | --- |
| Event 003 `THR_focus` | 111 | 48 | Route-aware support and route-choice priorities need probability audit against the Holy Realm AI matrix. Examples include `THR_mountain_refuge`, `THR_shelter_border_villages`, `THR_guard_high_passes`, `THR_bodhisattva_accepts_seal`, `THR_first_doctrine_suffering`, `THR_mandala_bureau`, and `THR_arhat_examinations` in `common/national_focus/003_holy_realm.txt`. |
| Event 020 Rat | 52 | 17 | Audit role-tree sequencing and route selectors, including `black_plague_rat_first_warren`, `black_plague_rat_listen_to_the_drains`, `black_plague_rat_feral_quarantine`, `black_plague_rat_citadel_relays`, and `black_plague_rat_cross_sea_cargo` in `common/national_focus/020_black_plague_rat_focus_tree.txt`. |
| Event 020 Rat King | 71 | 57 | Audit crown/government route selection and side-lane pacing, including `black_plague_rat_king_the_royal_basin`, `black_plague_rat_king_crown_the_broods`, `black_plague_rat_king_first_royal_decree`, `black_plague_rat_absolute_throne`, `black_plague_rat_king_court_of_teeth`, and `black_plague_rat_king_warren_charter` in `common/national_focus/020_black_plague_rat_king_focus_tree.txt`. |
| Other selected trees | 3,055 | 0 by structural scan | Still require route-aware quality review where the source uses flat weights or repeated modifiers. No balance conclusion is made here. |

The Event 003 and Event 020 gaps are not permission to insert arbitrary weights. Route `THR_focus`, Rat, Rat King, and every other weighted focus surface through `chaosx_ai_probability_auditor` using named scenarios, then apply any accepted patch through the owning agent and run `hoi4.probability_compare`. This baseline did not call the probability tools.

## Loading-gate and refresh inconsistencies

The following are bounded follow-up candidates. They were not patched because this task is explicitly a baseline pass and the exact completed-focus policy must be reviewed per route.

- Add an explicit `keep_completed = no` and an adjacent `mark_focus_tree_layout_dirty = yes` to Event 003's `THR_focus` replacement path at `common/scripted_effects/003_holy_realm_effects.txt:1868`, if the transformation is intended to replace rather than preserve completed focuses.
- Normalize the nine Event 005 release branches at `common/scripted_effects/005_soviet_collapse_effects.txt:10537-10611` to explicit replacement policy and a layout refresh. Keep the route-specific gates and flags intact. Do not replace the repeated successor setup blocks at `:21601-22822` with a generic dynamic helper in the same tranche.
- Make Event 007's `load_focus_tree = fury_focus_tree` at `common/scripted_effects/007_fury_effects.txt:217` explicit and refresh the layout after load. Preserve the existing player exclusion in `common/scripted_triggers/007_fury_triggers.txt:22-38`.
- Add refresh evidence after Event 010's death-tree replacement at `common/scripted_effects/010_death_effects.txt:456` if engine behavior confirms that this load is a visible replacement. Keep the generic fallback at `:509` as a valid fallback unless a separate owner proves it dead.
- Add refresh evidence after the Event 014 warlord, unified, and Wendigo loads at `common/scripted_effects/014_cannibalism_effects.txt:5193,12399,18988`, especially the narrow Wendigo overlay path. Do not widen its gates.
- Verify that every Event 015 accept/load path reaches `utopia_manifesto_refresh_focus_visibility` before treating the later mark at `common/scripted_effects/015_utopia_manifesto_effects.txt:1019` as sufficient.
- Verify the Kruger refresh helper call chain and the Dhrondan identity continuation policy before adding a mark or changing `keep_completed = yes` at `common/scripted_effects/016_dhrondan_country_effects.txt:262`.
- Add refresh evidence after Event 018, 019, and 020 replacement loads at `common/scripted_effects/018_resources_found_cave_effects.txt:63`, `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:576`, and `common/scripted_effects/020_black_plague_rat_effects.txt:1399,2564` only after the corresponding load call paths are confirmed.

Event 006 and Event 012 are the local patterns to preserve: explicit replacement policy, package/region gates, and layout refresh. The vanilla Polish restoration precedent in `common/on_actions/07_nsb_on_actions.txt` confirms the engine-facing load-plus-refresh sequence.

## Safe bounded patches, uncertain candidates, and rejected work

### Safe bounded follow-up candidates

The loader normalisation items above are narrow, file-owned changes if the owner confirms completed-focus policy and validates the replacement scenario. A first tranche should be limited to one loader family at a time, retain existing flags and gates, add explicit policy only where the current behavior is known, and record before/after focus inspection evidence.

The Event 003, Event 007, Event 014, Event 018, Event 019, and Event 020 adjacent-refresh candidates are the smallest practical maintenance tranche. They should not be combined with a route redesign or an AI rebalance.

### Uncertain dynamic references

The Event 012 host-transfer double-load, Event 015 later refresh helper, Event 016 Kruger/Dhrondan refresh ownership, and Event 005 successor setup repetition require dynamic call-graph review. Event targets, scripted effects, meta effects, and conditionally constructed tree IDs can be invisible to literal-token scans. Do not delete or merge a helper merely because its direct text call count is low.

Shared files such as `common/national_focus/austro_hungarian_releasable_shared.txt`, `common/national_focus/iceland.txt`, and any shared focus infrastructure were treated as ownership-sensitive references. Their vanilla-localised identifiers were not reported as missing mod localisation.

### Rejected candidates for this baseline

- Do not remove generic continuous-focus palette warnings emitted by MCP when the tool scan omits the corresponding vanilla interface files.
- Do not delete `generic_focus` fallback loading in Event 010.
- Do not delete Event 006 shared focuses or Event 012 overlay focuses because they have no ordinary `focus_tree` block; `shared_focus` is the intended architecture.
- Do not deduplicate the Event 005 successor blocks or the Event 012 host-transfer call without dynamic route proof.
- Do not add arbitrary AI weights to unweighted focuses in this pass. Probability evidence and route ownership are required.
- Do not alter `interface/*.gui`, GUI assets, focus inlays, layout coordinates, scripted-GUI structure, selectors, or toggles.
- Do not inspect or redesign Event 021+ event-specific trees under this handoff.

## Deferred redesign work

The following require plans or owner-led design, not cleanup edits:

- Event 003's 25 crossings, 21 node intersections, and 7 long connectors need route-aware reflow only after the 111-node route structure and target depth are accepted.
- Event 005's broad family repetition, shallow or generic reward patterns, and route-aware AI coverage require a dedicated family-by-family improvement plan. The existing `docs/plans/005_soviet_collapse_plans/` audit material remains the appropriate design surface.
- Event 012's nonlinear continental/world-order route depth and reward identity need a route matrix review.
- Event 020's Rat/Rat King role-tree AI, government route behavior, and weighted route priorities need the mandatory probability audit.
- Events 001, 004, 008, 009, 011, 013, and 017 need spec-owner confirmation if a national-focus package is intended; no tree should be invented from a cleanup request.
- No broad focus-tree migration, new route family, formable chain, country identity change, or GUI redesign belongs in this baseline.

## MCP evidence and unresolved limits

Successful representative focus inspections and renders:

- Event 002 `ZZZ_focus`: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4f4305f1c90d6e38289d4686b3bd215abfefd2813ab916b35add3b7a59c60b9b/5f9d7bdef0304f9efcb93802c3192e6a312a7e95e0e2ff0e9bdbcce6572de7fe/focus-inspect.25707cddff7c7170.json`; HTML render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fad77c3e8034c9fd884d37de25616074b58a84e8662644d415292518dc483943/bdfc4dbf19bcdc81b6bde190b94b72572660a2043628fbb2883907b8ad937a12/ZZZ_focus.focus.html`; SVG render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/9dcc4571fa7af7b5eebbfcb9a7486acae39e0f0e9d8b717b7b784fca441f95dc/af2000757655e980f8bdaba625a8636636c954a2ca7899c62093918325d632d1/ZZZ_focus.focus.svg`.
- Event 003 `THR_focus`: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4355c89fb246f5ee4f6e14b126956ed62616b712020546790cdaf0298e81df76/51500893e85823139079f425c2781a6b1859e77bf5bf257d4cc9bbde68b36a88/focus-inspect.2f9f3986507a3e77.json`; tree render succeeded at review scale 0.25 and produced HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ff7d64dcbdf48d38b368e881b31c16cbb0a0954d5cc3bdffdf737cb5f99ca3b9/57646c3be2f7070430c1a6357969b96c617612a1c763d297e85d8d515266262f/THR_focus.focus.html` and SVG `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e7182a9f4a451cf8d257adb1d9307736cbe5e5e4ab5d747ce2f183472a55334b/882d62c6b64d2d1b24e08b316f9d1587cfb6cd6598d8a10010960c0153c21b90/THR_focus.focus.svg`.
- Event 005 `INX_soviet_collapse_ancient_focus_tree`: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e8fddb769810c685534e73dd02fc410343b4e00758a77915c2b908a7d1b79c85/11090a443d26ac8c6354684da6966cac920ae2827562a536c4dcaae017f6233b/focus-inspect.f521efd97461a0ff.json`; render HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4a62e6115c2c8edd03ef3ff719131dde6862573e1f5f0092cff82d88843ea8e5/935258718bf2514c4d2ca81220db75342d4dcbf550079f553b0cef1bf2297792/INX_soviet_collapse_ancient_focus_tree.focus.html`.
- Event 006 `independence_wave_focus_tree`: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3774063d0f57da18c173f999fb82292c343faea162178c8e0c0df1ed46d1984b/5c4fb83dd1bce92ebe1b6b6409321d8c0501d0c63d0a394556926c4144280c00/focus-inspect.50a2ef0334a0b0e2.json`; render HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/76c58e51d0984860e8504f2a4045e4795843a977ecbd1b63ffdd027c69e23cc2/73c5c3f174c2b837a6861b977a4ce9b708a1f7d36d8b427c2c05e6c8e3c2c83f/independence_wave_focus_tree.focus.html`.
- Event 019 `infantry_spawn_derivative_focus_tree`: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5571fa740c12d6d63e57f0dd7db013b64dc08f152b088377692d1abf2a05dca6/097a5dc82c3c9f7b34be0cf32b8c949e811f53cb4635176ac0fef61ff4f2658f/focus-inspect.fd5fb35922db0737.json`.
- Event 020 Rat `black_plague_rat_focus_tree`: inspect `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8ae2feab50f920a471849eae54898be33e741ec275a69861fece7797dd6844e6/f7fd7546955bc6260c663a259aa87bcaaaebca690e33f280a83a7e4a86b30e86/focus-inspect.33cafa6c042f1e23.json`; render HTML `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d008fb7df79dfbf5e8df99fb3b9c9237c4bcc66b37348d2b4af82cc70380aada/1d5139e7e3a6f9cc18d9c5ba2b16aace1cbda74d83cf25a3c53668e430686f6e/black_plague_rat_focus_tree.focus.html`.

Unresolved MCP limits:

- Event 003 file-level render failed with `ARTIFACT_STORAGE_LIMIT`; tree-specific render succeeded.
- Event 007 and Event 019 renders timed out after 180 seconds.
- Event 010 inspect and render timed out after 180 seconds.
- Event 014 unified-tree inspect timed out after 180 seconds.
- Event 018 inspect timed out after 180 seconds.
- No successful 012, 015, or 016 tree-specific artifact was obtained in this pass.
- `hoi4.focus_compare` was not useful because this was read-only and had no before/after source state to compare.
- No live Hearts of Iron IV process was launched, and no game-log claim is made.

The MCP diagnostic lists for several successful calls contain missing generic/vanilla continuous-focus icons caused by incomplete tool file discovery. Those warnings are separated from the custom-source icon scan above. The MCP layout metrics are retained where returned, but only Event 003's metrics are elevated to a follow-up candidate because it has substantial crossings/intersections.

## Completion evidence and handoff

Files changed by this subagent: only `docs/plans/repo_cleanup/subagent_handoffs/focus_cleanup_baseline_2026-08-22.md`.

Focus IDs changed: none.

Localisation keys changed: none.

Icon IDs or assets changed: none.

Source patches and `hoi4.focus_rewrite`: none.

Meaningful validation: required wiki and vanilla-documentation review, source inventory, brace-aware focus/reference scan, localisation key scan, icon-definition/texture/shine scan, focus inspect/render calls, and MCP artifact review. No probability audit was run because that route belongs to `chaosx_ai_probability_auditor` and this handoff is read-only.

Simplifications, omissions, and blockers: Event-specific 021+ trees were intentionally excluded; several Event 001-020 MCP inspections/renders timed out or hit artifact storage limits; no semantic reward audit, route redesign, dynamic call-graph proof, probability comparison, or live-game validation was performed. No source or GUI patch is claimed.

## Top-priority next actions

1. Route Event 003, Event 020 Rat, Event 020 Rat King, and all other weighted focus logic through `chaosx_ai_probability_auditor` with named scenarios before changing AI weights.
2. Confirm completed-focus policy and add per-loader layout-refresh evidence for the Event 003, 005, 007, 010, 014, 018, 019, and 020 replacement paths, preserving the clean Event 006/Event 012 pattern.
3. Review Event 003's dense layout and 111-node route depth as a separate plan, not as a mechanical coordinate cleanup.
4. Keep Event 005 family deduplication, Event 012 host-transfer load deduplication, and route/reward redesign deferred until dynamic ownership and route matrices are documented.
5. Confirm with spec owners whether Events 001, 004, 008, 009, 011, 013, and 017 are intentionally focus-free; do not add placeholder trees from this audit.
