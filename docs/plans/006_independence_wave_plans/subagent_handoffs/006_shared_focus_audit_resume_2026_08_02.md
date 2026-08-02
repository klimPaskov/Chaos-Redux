# Event 006 shared focus audit resume — 2026-08-02

## Outcome

The current Event 006 shared tree is source-complete for the accepted shared-tree architecture, but its rendered layout remains validation-blocked. No safe bounded coordinate patch was identified. The focus source, imported package modules, icons, localisation, rewards, prerequisites, and source-level AI blocks are present; the remaining geometry and additive-carrier limits require a broader reviewed reflow or architecture decision outside this narrow audit.

## Evidence and limits

The current `hoi4.focus_inspect` run targeted `common/national_focus/006_independence_wave_focus.txt`, tree `independence_wave_focus_tree`, national mode.

- Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/722df48404377cbb72b68a967223d9655e569d5d4cb196a83842555a7e98200a/016e735c8a5600723d1d20160ae1a60da44da71c1a7d3b1904086ce72bec9439/focus-inspect.ddca0dfa3050caa9.json`
- Render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/12160e902184c36255109203ac80a9392f349dfb03c93c194e5e6fc98c516ab5/2e97885a859c72ad5f5952455c353908373bfc6666d526a3483d5228bfea645f/independence_wave_focus_tree.focus.html`
- Render SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56b47295032754eacb221bca80e282cf17bd002465d6d4d72696920d1eb5a6b0/71087ae842c7cd8ab01a8fddc1faf7e2389409be4eae4b3ef79636726ef68f7d/independence_wave_focus_tree.focus.svg`
- Source-map JSON: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/34caa01abdeb8caa03e051b25e8edd069edd662bd1331b5dfc95efa788b45b0b/4f290bcafa7ead1dd1abf8abff87df40f422aeba9bd8ff3dc2dc2b25fab706b6/independence_wave_focus_tree.focus.source-map.json`

MCP reports 184 regular focuses, 223 connectors, 43 connector crossings, 7 node intersections, 28 long connectors, 5 same-row pairs closer than the 2-cell spacing rule, x=1..101/y=0..19 bounds, and `validation=false` with 14 blocking diagnostics. `movableFocusIds=[]` in the returned layout; therefore there is no isolated focus coordinate the audit can safely move without a coupled layout rewrite. Do not call `hoi4.focus_rewrite` as a local cleanup: the existing audit trail records that a compact rewrite is quality-blocked and a full reflow would need parent review.

## Route coverage

| Architecture lane | Current source coverage | Main identifiers / source |
|---|---|---|
| Survival and state construction | Present: opening administration/state inventory, founding settlement, sovereignty capstone | `independence_wave_prepare_capital_administration` through `independence_wave_secure_durable_sovereignty` in `common/national_focus/006_independence_wave_focus.txt:100-3178`; trigger gates in `common/scripted_triggers/006_independence_wave_focus_triggers.txt` |
| Government and internal power | Present: constitutional, popular council, traditional, emergency military, patron-client, radical sovereignty, plus AJX neutral commission package branch | Core routes begin at `...focus.txt:856`; AJX branch at `...focus.txt:1252`; architecture contract in `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md:149-339` |
| Economy, infrastructure, administration | Present: revenue, food/fuel, transport, customs, package economic program, treasury, regional service overlays | `...focus.txt:318-438`, with package modules imported at `...focus.txt:50-92` |
| Army, security, military identity | Present: militia integration, depots, officer vetting, border guard, archetype, professional defense, civilian/autonomy/reserve/arsenal/league branches | `...focus.txt:439-700`; the professional-defense capstone uses five separate prerequisite blocks (intentional AND-of-five-OR semantics) at `...focus.txt:540-561` |
| Diplomacy, recognition, patrons | Present: foreign office, missions, recognition, neutrality, patrons, treaty-backed state, permanent service | `...focus.txt:709-847`; route triggers in `006_independence_wave_focus_triggers.txt` |
| Former-host, borders, expansion | Present: former-host policy through frontier, coexistence, association/union, claims, reclamation, and regional ambition | `...focus.txt:1312-1549` |
| Network, league, formables, high chaos | Present: network arbitration/league charter and congress, defensive/development/equality branches, formable preparation, open sovereignty/high-chaos, plus imported package modules | `...focus.txt:1567-2008`; imports and package shared focuses at `...focus.txt:50-92` and `...focus.txt:3183+` |
| Reviewed meaningful-tree overlays | Narrowly present only for Iceland; other package additive assignments fail closed unless a reviewed carrier exists | Static Iceland carrier at `...focus.txt:3318-3465`, `common/national_focus/iceland.txt`, and `common/scripted_effects/006_independence_wave_ice_package_effects.txt:365-367`; carrier trigger is `can_attach_independence_wave_additive_focus_carrier` in `006_independence_wave_focus_triggers.txt` |

No required route family from the accepted Part 4 architecture is missing in the shared tree. The design intentionally uses one shared tree plus package-gated modules; it does not provide bespoke Event 006 trees for every admitted country.

## Missing or simplified content

1. The accepted simplification remains one generic shared tree rather than bespoke country trees. This is documented architecture, not a new omission: `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_4_focus_tree_architecture.md:24-48`.
2. Additive overlays are fail-closed for meaningful trees without a reviewed static carrier. Only Iceland currently passes the carrier predicate; IW-022/IW-025/IW-035/IW-059/IW-085/IW-101/IW-102/IW-105/IW-156/IW-196/IW-197/IW-204 remain decision/idea/mission surfaces rather than visible overlay focuses. This is the accepted dynamic-link boundary, not a safe local focus-file patch.
3. The rendered layout is not release-ready because of the 14 blocking geometry diagnostics below. Fixing this requires a coordinated reflow and rerender, not a one-node edit.
4. No seeded AI scenario sweep or focus-selection simulation was run in this audit. Source-level `ai_will_do` coverage is present, but runtime probability evidence remains queued.

## Geometry diagnostics (high priority)

The current MCP diagnostic set includes the following coupled issues:

- Long connector `independence_wave_complete_founding_settlement -> independence_wave_map_internal_power_centers` (span 17).
- Crossing `independence_wave_bind_the_first_oath -> independence_wave_integrate_provinces_and_councils` with `independence_wave_inventory_the_state -> independence_wave_establish_emergency_revenue` (latter span 12).
- Founding-settlement fan crossings into AJX neutral commission, former-host, and fellow-new-state branches over the food/fuel to regional-transport route.
- Through-node intersection: `independence_wave_complete_founding_settlement -> independence_wave_survey_regional_ambition` through unrelated `independence_wave_establish_customs_service`.
- Long connector `independence_wave_bind_the_first_oath -> independence_wave_integrate_militia_commands` (span 14).
- Founding-settlement fan crossing depot -> recall/vet-officers.
- Founding-settlement -> survey-regional-ambition crossing form-border-guard -> adopt-military-archetype.
- Foreign-service -> durable-sovereignty crossing preserve-independent-command -> found-professional-defense and standardize-with-league -> found-professional-defense.
- Long connectors from civilian-control/preserve-independent-command into the professional-defense capstone (span 9), and adopt-military-archetype into reclamation (span 9) and league-standardize (span 11).
- Remaining close-row and crossing diagnostics are the same connected root/fan family; they should be solved as one layout pass rather than by moving an individual node.

## Icon coverage

Static scan of the four Event 006 focus source files found 318 focus/shared-focus blocks using 121 distinct icon IDs. All 121 icon IDs resolve to interface definitions; package icon families are registered in `interface/006_independence_wave.gfx`, `interface/006_independence_wave_pacific_focus_icons.gfx`, `interface/006_independence_wave_iw043_iw058_focus_icons.gfx`, and `interface/006_independence_wave_iw093_iw098_focus.gfx`. The corresponding DDS files are present under `gfx/interface/goals/006_independence_wave/`. No missing icon reference was found.

| Icon family | Definition surface | Result |
|---|---|---|
| Core shared lanes | `interface/006_independence_wave.gfx` | 12 core families plus AJX neutral commission resolve |
| Pacific package | `interface/006_independence_wave_pacific_focus_icons.gfx` | HBX/HAW package icons resolve |
| IW-043/IW-058 | `interface/006_independence_wave_iw043_iw058_focus_icons.gfx` | Volga/Assyria families resolve |
| IW-093/IW-098 | `interface/006_independence_wave_iw093_iw098_focus.gfx` | Asante/Emirate families resolve |

## Localisation and reward mismatch list

No static mismatch found. Every one of the 318 focus/shared-focus IDs has both `<focus_id>` and `<focus_id>_desc` in the localisation corpus, and all focus blocks contain `icon`, `completion_reward`, `ai_will_do`, `x`, and `y`. No duplicate focus IDs were found across the four Event 006 source files. Package shared-focus localisation lives alongside its package files (for example `localisation/english/006_independence_wave_focus_l_english.yml` and package-specific files).

The audit did not reword player-facing text or alter rewards because the requested issue is geometry/route audit and no mismatch was evidenced.

## AI behavior gaps

- Every regular focus has a source-level `ai_will_do`; core values and route modifiers are centralized in `common/script_constants/006_independence_wave_focus_constants.txt` and use route/state triggers in `common/national_focus/006_independence_wave_focus.txt`.
- Generic profile strategy blocks exist in `common/ai_strategy/006_independence_wave_generic.txt` for survival/recovery/consolidation, with package strategy files layered separately.
- Missing evidence is runtime scenario coverage: no seeded focus-selection/probability sweep was run for urgent survival, each government route, former-host hostility, recognition/patron pressure, network/league, formable, or World Collapse states. This is a validation task, not a safe source patch.

## Recommended next action

Parent should retain the current source and schedule a reviewed layout pass that treats the founding-settlement root fan and professional-defense fan as coupled subgraphs, then rerun `hoi4.focus_inspect` and `hoi4.focus_render`. Keep the additive carrier boundary fail-closed unless a meaningful-tree owner is explicitly reviewed and statically imports the overlay. No focus source files were changed by this audit.

