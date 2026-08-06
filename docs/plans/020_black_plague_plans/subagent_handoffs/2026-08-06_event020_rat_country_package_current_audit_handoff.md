# Event 020 rat country-package audit handoff — 2026-08-06

Scope: current country-package coverage for `RTA` (Rat Nation) and `RTX` (Rat King), including registration, dormant history, runtime state transfer, leaders, portraits, flags, parties, ideas, focus loading, decisions, military setup, technology and industry surfaces, AI references, cleanup, and asset evidence.

Status: the bounded local defect found in this pass is fixed. No country identity redesign, new tag, new focus route, broad balance change, map write, or live-game run was performed.

## Coverage checklist

| Surface | Current result | Evidence and risk |
| --- | --- | --- |
| Tags and definition | Covered | `common/country_tags/020_black_plague_rat_countries.txt:8-11` registers exactly `RTA` and `RTX`, both using the shared shell in `common/countries/020_black_plague_rat_country.txt`. No current implementation reference to retired rat tags was found. |
| Dormant history | Covered after narrow fix | `history/countries/RTA - Rat Nation.txt:2-9` and `history/countries/RTX - Rat King.txt:2-9` use safe `capital = 1`, the shared OOB, zero research slots, neutrality-only politics, and disabled elections. RTA now starts with only Brood Instinct and No Civilian Economy; RTX starts with No Civilian Economy and King Dominion. Runtime rebinds the capital and adds the staged RTA spirit after state creation. |
| Spawn, transfer, cores, capital, cleanup | Covered dynamically | `common/scripted_effects/020_black_plague_rat_effects.txt:1329-1575` initializes and creates RTA from a selected state, adds the transferred-state core, and rebinds the capital. `:2546-2723` initializes and transfers RTX to the Royal Basin. `:2283-2391` clears retired RTA flags, ideas, templates, variables, and controlled-state bookkeeping. The King defeat path retires its own state and templates. No formable or extra rat tag is present. |
| Map and state setup | No rat-specific defect found | Read-only MCP state-1 inspection passed map-file, geometry, membership, network, and adjacency checks and a full owner-layer render completed. Global diagnostics still contain 1,323 building-position and 1,331 port-adjacency errors from `mod:map/buildings.txt`; these are not tied to RTA or RTX. No map rewrite was attempted. |
| Politics, classification, parties | Covered | History and runtime set neutrality with elections disabled. `common/scripted_triggers/chaosx_dynamic_triggers.txt:22-71` classifies both runtime flags as special and actual nonhuman countries, and the civilian-system helper excludes them from ordinary human economy behavior. Party and ideology localisation is present in `localisation/english/020_black_plague_rat_countries_l_english.yml:4-43`. |
| Leaders and portraits | Runtime coverage present, identity gap remains | RTA creates institutional `The Brood Voice` with four archetype portraits at `common/scripted_effects/020_black_plague_rat_effects.txt:1424-1451`; RTX creates `The Rat King` with the King portrait at `:2611-2617`. The static portrait and the ten-frame animated sheet are registered in `interface/020_black_plague_rat_identity.gfx:42-53`, and all portrait DDS files exist. The broader identity specification still asks for an actual-like nonhuman sovereign name/epithet pool; the current title-only `The Rat King` does not satisfy that design requirement. |
| Flags and visual wiring | Covered at runtime | Normal, medium, and small `RTA.tga` and `RTX.tga` files exist under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`. Static reference checks found zero missing GFX texture paths and zero missing Event 020 focus icon registrations. Current docs claim promoted source-frame manifests under `docs/assets/020_black_plague/...`, but those durable manifest paths were not present in the local `docs/assets` listing; provenance/archive reconciliation remains open. |
| Focus loading and routes | Covered; parent focus handoff owns route details | Runtime loads `black_plague_rat_focus_tree` at `common/scripted_effects/020_black_plague_rat_effects.txt:1454` and `black_plague_rat_king_focus_tree` at `:2617`. MCP inspection/render completed for both trees: 52 RTA roles and 71 RTX roles, with no Event 020 icon diagnostics, no connector crossings, and no node intersections. The remaining diagnostics are shared vanilla continuous-focus sprite references and local layout-spacing warnings, not country loading failures. |
| Decisions and ideas | Present, cross-surface audit remains parent-owned | `common/decisions/020_black_plague_rat_decisions.txt` and its category file expose RTA and RTX actions. `common/ideas/020_black_plague_rat_ideas.txt:12-78` defines Brood Instinct, No Civilian Economy, Fractured Instinct, Dominion, and King Dominion, and interface idea sprites resolve. Decision weighting and shared GUI evidence are outside this narrow country handoff. |
| Starting military and equipment | Intentionally scripted | `common/units/020_black_plague_rat_units.txt:24-228` defines six inactive rat-only subunits with no ordinary equipment requirement and explicit supply consumption. `history/units/020_black_plague_rat_1936.txt:13-77` provides five locked templates using `override_model = black_plague_rat_entity`; runtime pulse effects create divisions rather than normal human recruitment. |
| Technology, industry, supply, production | Intentional nonhuman simplification | Both histories set `set_research_slots = 0`; Brood Instinct and No Civilian Economy suppress conventional manpower/production behavior. Captured knowledge and nest-industry progression are represented by scripted variables, spirits, templates, and decisions rather than a conventional technology tree. The installed HOI4 MCP exposes no Technology Tree Viewer, so no technology-tree evidence can be claimed. |
| AI and playability | Source references resolve; quantitative balance remains open | `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` is flag- and route-gated for both tags, and the rat-only roles in `common/ai_templates/020_black_plague_rat_templates.txt` resolve to the five custom subunit roles (`rat_swarm`, `rat_brutes`, `rat_burrowers`, `rat_carrion_guard`, and `rat_dock_stowaways`). The mandatory `hoi4.probability_inspect` route for the AI strategy file returned `PROBABILITY_SURFACE_EMPTY`; therefore this handoff makes no normalized AI survival or route-dominance claim. |

## File-surface checklist

- `common/country_tags/020_black_plague_rat_countries.txt` — the only current rat tag registration, `RTA` and `RTX`.
- `common/countries/020_black_plague_rat_country.txt` — shared graphical culture and color shell.
- `history/countries/RTA - Rat Nation.txt` and `history/countries/RTX - Rat King.txt` — dormant country setup.
- `history/units/020_black_plague_rat_1936.txt` and `common/units/020_black_plague_rat_units.txt` — locked scripted templates and inactive rat subunits.
- `common/scripted_effects/020_black_plague_rat_effects.txt` and `common/scripted_triggers/020_black_plague_rat_triggers.txt` — initialization, state transfer, pulse, evolution, Royal Basin, and cleanup logic.
- `common/ideas/020_black_plague_rat_ideas.txt`, `common/decisions/020_black_plague_rat_decisions.txt`, and `common/decisions/categories/020_black_plague_rat_categories.txt` — current spirit and decision surfaces.
- `common/national_focus/020_black_plague_rat_focus_tree.txt` and `common/national_focus/020_black_plague_rat_king_focus_tree.txt` — trees loaded by the matching runtime initializer.
- `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` and `common/ai_templates/020_black_plague_rat_templates.txt` — route strategy and rat-only template roles.
- `localisation/english/020_black_plague_rat_countries_l_english.yml`, `localisation/english/020_black_plague_rat_focus_l_english.yml`, and `localisation/english/020_black_plague_rat_decisions_l_english.yml` — current country, leader, idea, focus, and decision text.
- `interface/020_black_plague_rat_identity.gfx`, `gfx/flags/`, `gfx/leaders/020_black_plague/`, and Event 020 focus/idea DDS folders — runtime visual wiring.

## Applied patch

Changed file: `history/countries/RTA - Rat Nation.txt:9`.

Before: dormant RTA history added `black_plague_rat_brood_instinct`, `black_plague_rat_no_civilian_economy`, and `black_plague_rat_dominion`.

After: dormant RTA history adds only `black_plague_rat_brood_instinct` and `black_plague_rat_no_civilian_economy`.

Reason: `black_plague_rat_initialize_country` already adds Brood Instinct, No Civilian Economy, and Fractured Instinct at runtime (`common/scripted_effects/020_black_plague_rat_effects.txt:1453`), while Dominion is earned later by the `black_plague_rat_harden_the_immune_blood` decision (`common/decisions/020_black_plague_rat_decisions.txt:354-368`). The before state granted a later progression spirit in dormant history; the after state leaves the RTA staged lifecycle to the runtime initializer and decision. No other gameplay or asset file changed in this pass.

## MCP evidence and limitations

### Focus trees

`hoi4.focus_inspect` and `hoi4.focus_render` both completed for `black_plague_rat_focus_tree` and `black_plague_rat_king_focus_tree`. The latest route handoff artifacts are:

- RTA inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/817d677799a5a990d6082baa01d3676768c73f332c96fd55f4d3625697b5c831/912df526abc60e2307d00720c044ea76f3146f2515d1a6c1672bb24567f19f2d/focus-inspect.d84c539a9abe5622.json`.
- RTA render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3c7778b72c41a32df5f19d19af9fa374c241c78fa82a5dcf7ff236f2a45d1b06/9f3228ffaf5f641e9e2e53e2f875dc5284ed5da38ca7bad11bb7af61b2666ca8/black_plague_rat_focus_tree.focus.html` and the corresponding SVG under artifact `80e08999ba7371a4acaee5f157dec05610ddb5a00a14317ec231931f03153d48/a8d12d1add1efc033e3425d5a900e5b04d3831b194e41f5b67a12c03ec72d7ed`.
- RTX inspect: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16ebc5e6a9e2e4165a4a186e9cae6555664b9162edeca326d65f637a12baebb5/79632d2e9136881b61f66bcd1def68924eeffbb7ae4f1c427c142370e5292b56/focus-inspect.a89d4a7b76388f17.json`.
- RTX render: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/61a187d2394aa2a2fe2924c82d8d722da75a354b57c5eb985ca2c659b97a9fc3/27b34ba3dd279517bac30bb5795a8fe014b243a6b32a33559ec5ab68cb9e56d0/black_plague_rat_king_focus_tree.focus.html` and the corresponding SVG under artifact `fa44d96a794c112f7a704d534ed498056f4e6dd70d0cda90e02b189202e8ebc2/df850fb42c11d10ecfb4d5b33598e9f24955a2b321f9db7bb452986bc924df73`.

### Event 020

`hoi4.event_inspect` for namespace `chaosx.nr20`, file scans, and event trace `chaosx.nr20.1` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics, but helper/lifecycle validation was deferred because the inline workspace projection was truncated (`MCP_INLINE_FILES_TRUNCATED`). The latest namespace scan artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b48aa864d9ad155519f93214d47ba9017aed5dfed1d27531b4a3504236918df1/79c2745b98abcb84e48926a46e6316a570a9cd6e3e039dc162b1b094ec8cdb66/event-scan-e95cc5f8ce60.json`. Earlier narrow file and root-trace artifacts remain `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d9f7927bff2b16331bbfa08ffc2ee57e7efe9ff0fc6c46387303d2bf734cf53c/9928bc76903190458ed6e655caeda6904b06c1c6c8a1d6aac1bfafbc45d9568c/event-scan-c5c2ec44234b.json` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce49ce4053c6a27200d430773131514dcddf67ab5221fc1fbe9c64e7f98190d1/9d51e79d1ced9e27f2287adc5877ce84ab5423790b92539af8ae288a2d1363a0/event-trace-c5c2ec44234b.json`. This is not equivalent to a complete event graph validation.

### Map

`hoi4.map_inspect` for state 1 returned `MAP_INSPECTED` and `hoi4.map_render` returned `MAP_RENDERED` with owner, coastline, port, victory-point, building, supply, and railway overlays. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/86d2f13cbde650494bf7a697b4952f31191ad2f00210015f357cf3d14b773114/092a5d20f7c108cd71618fa70afa51861f70704e1c7eb11c1a319781227d5447/map-inspect.f1c123073e1222ac.json`. Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/48523ff3b868652410cf501163e7da6631266dc80a98838b57853ad3f2d7a34a/400705f10fa13ba23e02aa97120a84a7c350eeab51e9399b45bef847ccc88437/map-owner.png`. The selected state showed no RTA/RTX-specific map failure; the omitted global building/port diagnostics remain unrelated map debt.

### Weighted AI surface

The required `hoi4.probability_inspect` call for adapter `ai_strategy_factor` against `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` returned `PROBABILITY_SURFACE_EMPTY` with no artifact because no weighted block matched the adapter request. This is an MCP route limitation, not evidence that AI strategy code is absent. No quantitative AI balance claim or probability patch was made.

## Missing, stale, or unresolved package surfaces

- RTX still uses title-only `The Rat King` instead of the broader spec's actual-like fictional nonhuman sovereign name and epithet pool. A future identity pass must also preserve male-coded metadata for the current portrait or explicitly review gender metadata if the portrait changes.
- No RTA or RTX advisor, high-command, or commander characters are defined in the current package. This is an identity-depth gap, not a narrow tag or wiring defect.
- Public names remain fixed `Rat Nation` and `Rat King`; the broader matrix asks for archetype-aware public naming. Changing that requires design authority rather than a local audit patch.
- Runtime portrait coverage is present, including the King animated sheet, but the durable source-frame/rights manifests referenced by current Event 020 docs were not found in the local `docs/assets` listing. Parent/docs ownership should reconcile the archive path and provenance without changing runtime DDS references.
- Some older handoffs report 51 RTA focuses or missing animated King frames. Current source/MCP evidence is 52 RTA roles, 71 RTX roles, and a registered ten-frame King sheet; those older claims are superseded.
- The installed MCP exposes no Technology Tree Viewer, so conventional technology completeness remains an unresolved tooling limitation. No custom technology surface is currently loaded by either country.

## Validation performed

- Static cross-checks confirmed exactly two current rat tags, matching country definition/history files, all current RTA/RTX localisation identifiers, all six rat subunits, and all five rat-only AI template roles.
- Static GFX checks found zero missing texture paths, zero missing Event 020 focus icon registrations, and resolved idea/portrait sprite references.
- Read-only focus, event, probability, and map MCP routes were executed as described above. No map write, GUI rewrite, technology viewer, or game executable was used.
- No live save, AI survival, event-click, or focus-click test was run because live consumer validation belongs to the parent/user boundary.

## Remaining setup and identity risks

The package is wired for the current two-tag runtime design, but the sovereign naming requirement, optional advisor/command package, durable portrait provenance manifests, and quantitative AI route evidence remain open. These are broader design, asset-provenance, or parent-owned audit items; no new simplification was introduced by this pass beyond the existing design gaps listed above.

Plan handoff path: `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-06_event020_rat_country_package_current_audit_handoff.md`.
