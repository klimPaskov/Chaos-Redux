# Event 014 focus-tree audit

> **Superseded snapshot (2026-07-15).** This 2026-07-11 audit predates the
> focus, asset, localisation, and gameplay closure passes. Do not use its
> incomplete counts or missing-asset findings for current status; use the
> consolidated Event 014 focus audit and package status instead.

Date: 2026-07-11  
Mode: read-only audit; no gameplay, localisation, interface, or asset files were edited  
Status: **incomplete — no completion claim**

## Verdict

The three files contain the accepted raw node counts—72 warlord, 108 unified CBL, and 28 Wendigo—and their focus graphs are structurally coherent. That does not make the package complete.

Completion is blocked by four systemic failures:

1. The dormant CBL tag is never explicitly given the unified tree. Its tree selector requires flags that are false when the country is evaluated, while the unification transaction sets those flags without calling load_focus_tree.
2. The unified tree is mostly a contract façade. Its reward effects set 215 unique country flags, but only seven have a consumer outside the reward-effect file. There is no unified decision category or decision file, 61 focus reward helpers are wholly inert apart from setting unused flags, and the ordinary terminal gate accepts focus-completion flags even though the promised branch mechanics do not exist.
3. Every one of the 208 custom focus icons is absent from the live runtime folder. All 72 warlord focus sprites are also unregistered. Twenty-nine focus-created idea icons are missing or unregistered.
4. Event 014's 18 specified achievements and their focus-route hooks do not exist in gameplay/localisation wiring.

The Wendigo route is the strongest of the three mechanically: its decision gates, countdown, anchor, and terminal effects have live consumers. Its focus rewards are nevertheless shallow, its three stage ideas have neither localisation nor sprites, all 28 focus textures are absent, and 17 focuses use an undefined search filter.

## Authorities and inspected scope

Required repository guidance:

- AGENTS.md
- .agents/skills/chaos-redux-focus-trees/SKILL.md
- .agents/skills/chaos-redux-subagents/SKILL.md

Offline wiki pages consulted:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding
- National focus modding

Vanilla documentation and precedent:

- Hearts of Iron IV/documentation/script_concept_documentation.md
- Hearts of Iron IV/documentation/effects_documentation.md
- Hearts of Iron IV/documentation/triggers_documentation.md
- Hearts of Iron IV/common/script_constants/documentation.md
- Hearts of Iron IV/events/BFTB_Greece.txt:3196-3252, which explicitly calls load_focus_tree for a dynamically prepared country
- Representative current vanilla national-focus files for prerequisites, mutual exclusions, availability, search filters, AI weights, and dynamic loading

Event 014 design sources:

- docs/specs/014_cannibalism_specs/README.md
- spec parts 4, 5, 7, 8, 9, 10, 11, and 12
- focus-route, country-package, idea-lifecycle, AI-strategy, asset-inventory, and hidden-identity matrices
- all three focus graph files and the acceptance/quality documents

Implementation surfaces:

- all three national-focus files
- all three focus reward-effect files
- country creation, unification, Wendigo, terminal, and super-event effects/triggers
- Event 014 constants, ideas, dynamic modifiers, decisions, categories, AI folders, achievements, localisation, interface sprites, live assets, manifests, country history, and characters

## Summary matrix

| Surface | Result | Evidence |
|---|---:|---|
| Raw node scale | Pass | 72 warlord, 108 unified, 28 Wendigo; all are inside the accepted ranges |
| Graph integrity | Pass | No missing prerequisite IDs, prerequisite cycles, duplicate IDs, duplicate coordinates, or asymmetric mutual exclusions |
| Cost hygiene | Pass | Only 5/10/15-week file-local costs; 35/70/105-day equivalents |
| Focus AI blocks | Pass | 72/72, 108/108, and 28/28 |
| Existing decision AI | Pass | 16/16 warlord decisions and 11/11 Wendigo decisions have ai_will_do |
| Unified tree assignment | **Critical fail** | No load_focus_tree for cannibalism_unified_focus_tree |
| Warlord mechanical depth | Partial | Core recruitment, state use, dynamic route modifier, and one operation per origin exist; 53 advertised downstream contracts do not |
| Unified mechanical depth | **Critical fail** | No unified decision system; 204 unresolved external contracts after excluding four internal terminal bookkeeping gates |
| Wendigo mechanical depth | Partial | Live decisions/countdown/anchors/terminal; generic micro-rewards and missing presentation |
| Ordinary >1000 gate | Pass in isolation | Both focus availability and scripted trigger use strict greater-than 1000 |
| Wendigo >1000 gate | Pass in isolation | Countdown start and terminal lock require strict greater-than 1000 |
| Terminal integrity | **Critical fail** | Ordinary gate measures focus flags, not implementation of the promised four packages |
| Focus localisation | Pass | All 208 titles, descriptions, and custom tooltips exist exactly once |
| Other localisation | Fail | Three tree names and six Wendigo idea keys are missing; three pre-reveal strings violate prose rules |
| Pre-reveal spoiler control | Pass | Warlord focus titles/descriptions/tooltips do not expose Hannibal or Wendigo |
| Focus icons | **Critical fail** | 208/208 live DDS files absent; 72/72 warlord base and shine sprites unregistered |
| Focus-created idea icons | Fail | 26 registered textures absent and three Wendigo sprites/textures absent |
| Idea ceiling/lifecycle | Pass structurally | Warlord and unified routes stay at or below three focus-created static spirits; Wendigo stage ideas replace one another |
| Achievement hooks | Fail | None of the 18 Event 014 achievements are implemented |

## Findings

### F-01 — Critical: the unified CBL tree is not loaded

Evidence:

- common/national_focus/014_cannibalism_unified_focus.txt:15-25 gives the tree a score only when CBL already has cannibalism_unified_country and the global reveal flag.
- history/countries/CBL - Cannibal Unified Host.txt defines CBL as a dormant tag with neither those flags nor a focus-tree load.
- common/scripted_effects/014_cannibalism_unification_effects.txt:388-405 transfers the first state, then sets cannibalism_unified_country and cannibalism_unified_focus_tree_available, but never calls load_focus_tree.
- The only Event 014 load_focus_tree calls are for warlords at common/scripted_effects/014_cannibalism_country_effects.txt:793 and Wendigo at common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt:26.
- The offline National Focus Modding reference warns that country selection is normally evaluated before play and is not automatically refreshed. The vanilla dynamic-country precedent explicitly loads the tree.

Impact:

- CBL can retain no focus tree or an unrelated previously selected tree. The 108 authored focuses are therefore not a dependable playable surface.

Required correction:

- Explicitly load cannibalism_unified_focus_tree on CBL, after its public identity/eligibility flags are set and before control is handed to the player/AI. Preserve no old completions. Re-audit ordering against player tag transfer and the Wendigo alternative.

### F-02 — Critical: the unified tree's advertised systems stop at unused flags

Evidence:

- common/scripted_effects/014_cannibalism_unified_focus_effects.txt sets 215 unique country flags.
- A full token scan of common/, events/, history/, and interface/ finds external consumers for only seven:
  - cannibalism_terminal_route_complete
  - cannibalism_terminal_route_ready
  - cannibalism_unified_disposition_break
  - cannibalism_unified_disposition_chain
  - cannibalism_unified_disposition_keep
  - cannibalism_unified_universal_enemy_decisions_open
  - cannibalism_unified_world_end_focus_complete
- The three disposition flags only influence later focus AI. The universal-enemy flag is also set by the super-event effect and does not reveal a unified decision set.
- common/decisions/categories/014_cannibalism_categories.txt defines containment, warlord, and network-alert categories only.
- There is no unified Event 014 decision file and no decision references any cannibalism_unified_* contract.
- Sixty-one unified completion helpers have no live output beyond setting flags with no consumer. They are listed in Appendix C.
- Representative tooltips promise systems that do not exist:
  - localisation/english/014_cannibalism_l_english.yml:708 promises warlord submission decisions.
  - line 934 promises an active terminal army package and Hannibal trait upgrade.
  - line 962 promises global naval corridors and an ocean-crossing package.
  - line 983 promises an air front-collapse package.
  - line 1007 promises prewar cell operations.
  - line 1019 promises global campaigns and postwar integration.
  - line 1031 promises costed counterwar conversion.

Terminal exploit:

- The four terminal preparation flags are set by completing the larder, army, expansion, and counterwar capstone focuses.
- cannibalism_unified_focus_refresh_terminal_route at lines 166-193 treats those flags as sufficient and sets terminal readiness.
- It does not verify that any promised decision category, mission, army package, campaign system, or counterwar conversion exists or has been used.
- A player can therefore reach the ordinary world-end route through focus completion while the supposed preparation mechanics remain absent.

Required correction:

- Implement the named categories, decisions/missions, costs, failure states, target selection, AI use, cleanup, and route consequences; or redesign the focus tooltips/spec contracts with explicit user approval. Then make terminal readiness depend on real package state rather than placeholder focus flags.

### F-03 — Critical: the live focus art package is empty

Evidence:

- gfx/interface/goals/014_cannibalism/ contains zero files.
- All 108 unified and 28 Wendigo base/shine sprite pairs are registered in interface/014_cannibalism.gfx:82-353, but their 136 unique texture files are absent.
- All 72 warlord focuses reference unique GFX_goal_cannibalism_warlord_* sprites, but neither the base nor _shine variants are registered anywhere.
- The exact 208 missing focus IDs are listed in Appendix A. The required texture for each is gfx/interface/goals/014_cannibalism/goal_{focus-id}.dds.
- Source prompts, generated-source packages, or manifests under docs/assets/ do not satisfy the live DDS/sprite requirement.

Focus-created idea art is also incomplete:

- Twenty-six registered idea sprites point to absent DDS files; exact names appear in the missing-asset inventory below.
- The three Wendigo stage ideas have no GFX_idea_* sprite definitions and no DDS files.

Impact:

- Every custom focus icon is transparent/missing in game. Most route-defining national spirits are also missing their intended presentation.

### F-04 — High: the warlord tree has real foundations but incomplete route payoffs

Working parts:

- Explicit dynamic loading after origin setup.
- Three mutually exclusive hierarchy routes and three mutually exclusive Larder routes.
- A single dynamic operating-order modifier prevents spirit spam.
- Costed, capped recruitment and population/Larder spending.
- State consumption/intensification/relocation.
- One live decision operation for each of Island, Siege, March, and Prison origins.
- Evolution II alignment decisions and synchronized attacks.

Missing parts:

- Five focuses are entirely inert apart from unused flags:
  - cannibalism_warlord_captains_as_officers
  - cannibalism_warlord_siege_open_the_tunnels
  - cannibalism_warlord_march_sabotage_the_rails
  - cannibalism_warlord_mark_the_supply_hubs
  - cannibalism_warlord_read_the_common_signs
- Fifty-three advertised external contracts have no consumer; Appendix B lists them exactly.
- The four origin overlays are only four focuses each. They establish identity and one operation, but do not deliver the several origin-specific focus groups demanded by the spec. Hidden anchorages/landings, tunnels, rail sabotage/corridors, prison/depot follow-through, and the four regional endgames are absent or represented only by unused flags.
- Alignment is the only Evolution II route with two implemented player actions. Manipulation and defiance mostly reduce to passive dynamic-modifier values and generic existing operations; their promised endgames are not implemented.

### F-05 — High: the Wendigo tree is wired but too shallow for the specified absurd/terminal route

Working parts:

- Correct explicit tree load.
- Live frozen-corridor, pack-training, acceleration, stabilization, anchor, countdown, hunt, and terminal consumers.
- Countdown/lock logic preserves the existing Wendigo country and requires real tracked state.
- One transformation-stage idea is active at a time.

Defects:

- Many of the 28 focuses grant only authority +1/+2/+3, frenzy +4, 2-4% stability/war support, command/political power, or repeated one-use 50% research bonuses.
- This does not provide the requested escalating absurd military and world-end mechanics across the route, even though the final lock effect is materially powerful.
- cannibalism_wendigo_conjoined_hunger, cannibalism_wendigo_winter_feeding_network, and cannibalism_wendigo_locked_terminal_form have no name/description localisation.
- Those same three ideas have no registered sprite or live DDS.
- All 28 focus textures are absent.

### F-06 — High: player reward values violate the focus-tree tuning standard

The focus skill requires clean, legible multiples of five unless a specific engine/formula exception is documented.

Warlord examples from common/script_constants/014_cannibalism_warlord_focus_constants.txt:25-99:

- 12% burden attack and organization
- 12% council planning
- 12% speed, 18% organization regain, and 8% defence on the confederacy route
- 18% regain and 12% attack on rapid consumption
- 12% mobile speed
- 12% discipline regain
- 12% organization, 4% reinforce, and -12% supply on alignment
- 12% political power/efficiency and 6% speed on manipulation
- 18% attack, 12% organization, and -8% political power on defiance

Wendigo examples from common/script_constants/014_cannibalism_wendigo_focus_constants.txt:15-31:

- authority +1/+2/+3
- frenzy +4
- stability +2%/+4%
- war support +3%
- pack capacity +2/+4

No engine or design exception is documented for these authored reward values. Unified route-idea values are consistently rounded to 5% increments and do not have this defect.

### F-07 — High: all 18 specified achievement routes are absent

docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_11_achievements_scenarios_and_aftermath.md specifies cannibalism_01 through cannibalism_18, including warlord, unified, ordinary-terminal, and Wendigo-terminal mastery routes.

No matching achievement definition, scripted trigger/effect, focus completion hook, localisation, or runtime sprite registration exists in common/, events/, localisation/, or interface/. Source achievement images under docs/assets/ are not gameplay implementation.

Required missing focus-route hooks include, at minimum:

- warlord defiance survival/independence
- selected unification host plus retained warlords and a major unified branch
- unified absorption/global Larder mastery
- ordinary world-end completion above threshold
- Wendigo world-end completion above threshold
- defeat/break routes for unified and Wendigo terminal progress

### F-08 — Medium: 17 Wendigo focuses use an undefined search filter

FOCUS_FILTER_ARMY does not exist in the mod or current vanilla. Vanilla uses FOCUS_FILTER_ARMY_XP.

Affected focuses:

- ZZZ_wendigo_preserve_the_pack
- ZZZ_wendigo_bind_the_warlord_commands
- ZZZ_wendigo_open_the_winter_hunt
- ZZZ_wendigo_march_through_the_blizzard
- ZZZ_wendigo_count_the_winter_victories
- ZZZ_wendigo_raise_the_winter_network
- ZZZ_wendigo_drill_the_original_pack
- ZZZ_wendigo_open_the_pack_musters
- ZZZ_wendigo_feed_the_anchor_guardians
- ZZZ_wendigo_expand_the_hunting_packs
- ZZZ_wendigo_army_of_the_frozen_larder
- ZZZ_wendigo_keep_the_cannibal_legions
- ZZZ_wendigo_retain_the_warlord_captains
- ZZZ_wendigo_accelerate_the_transformation
- ZZZ_wendigo_designate_the_last_hunt
- ZZZ_wendigo_hunt_every_remaining_capital
- ZZZ_wendigo_the_world_beneath_winter

### F-09 — Medium: non-focus localisation coverage and prose are incomplete

Missing keys:

- cannibalism_warlord_focus_tree
- cannibalism_unified_focus_tree
- cannibalism_wendigo_focus_tree
- cannibalism_wendigo_conjoined_hunger
- cannibalism_wendigo_conjoined_hunger_desc
- cannibalism_wendigo_winter_feeding_network
- cannibalism_wendigo_winter_feeding_network_desc
- cannibalism_wendigo_locked_terminal_form
- cannibalism_wendigo_locked_terminal_form_desc

Pre-reveal prose violations:

- localisation/english/014_cannibalism_l_english.yml:447, cannibalism_warlord_secure_the_first_larder_tt, contains a semicolon.
- line 591, cannibalism_warlord_prison_unite_cells_and_guards_desc, contains a semicolon.
- line 610, cannibalism_warlord_seize_prisons_and_depots_desc, contains a semicolon.

There are no missing or duplicated title/description/tooltip keys for the 208 focus nodes themselves.

### F-10 — Medium: the unified air route lacks capability-aware availability and AI

The navy route gates CBL_captured_shipyards and CBL_oceanic_hulk_routes on controlled coastal/naval infrastructure. The seven-focus air route has no comparable aircraft, airbase, technology, or stockpile validity gate, and its AI weights do not avoid the route when the country cannot use it.

Affected path:

- CBL_repair_the_captured_airframes
- CBL_terror_reconnaissance
- CBL_interdiction_markers
- CBL_airborne_cell_insertion
- CBL_battlefield_recovery_signals
- CBL_fear_bombing_tables
- CBL_skies_over_the_larder

This is separate from the larger defect that all promised air projects/missions are absent.

## Route coverage against the accepted design

### Warlord tree

| Required lane | Structural coverage | Playable coverage | Audit result |
|---|---:|---:|---|
| Survival opening | 6 focuses | Real variables, capital/state effects, and category opening | Pass |
| Personal tyranny / council / confederacy | Three symmetric four-focus routes | Dynamic modifier tradeoffs and AI personality weights | Pass structurally; numeric tuning needs cleanup |
| Rapid / managed / mobile Larder | Three routes after shared trunk | Dynamic modifier tradeoffs and some state actions | Partial; several named decisions/missions absent |
| Military doctrine | Nine focuses | Costed recruitment and caps exist | Partial; officers, supply targeting, protection follow-through absent |
| Island origin | Four focuses | Port work, one convoy operation, specialist, idea upgrade | Partial |
| Siege origin | Four focuses | Fort/workshop work, one relief operation, specialist, idea upgrade | Partial |
| March origin | Four focuses | Mobile setup, one depot operation, relocation, idea upgrade | Partial |
| Prison origin | Four focuses | One transfer operation, foreign cells/cadres, idea upgrade | Partial |
| Expansion/cells | Eight focuses | Basic raids, seeding, cadres, synchronized attack | Partial; supply hubs, corridors, corruption follow-through absent |
| Evolution II alignment/manipulation/defiance | Shared root plus three three-focus routes | Alignment has actions; manipulation/defiance mostly passive | Partial |
| Regional endgames | One capstone per Evolution II route | Alignment only has meaningful action support | Fail for manipulation/defiance depth |

### Unified CBL tree

| Required lane | Structural coverage | Playable coverage | Audit result |
|---|---:|---:|---|
| Reveal/opening | Eight focuses | Variables, burden removal, small capital works | Partial; submission/settlement systems absent |
| Warlord disposition | Three five-focus routes | Root/capstone idea swaps | Partial; governance, hostage, purge, and rivalry systems absent |
| Supreme hierarchy | Three five-focus routes | Root/capstone idea swaps | Partial; command/council/ritual decisions absent |
| Continental Larder | Shared trunk plus four methods | Route ideas and a few buildings | Fail for promised projects, missions, consumption-state play, and terminal package |
| Army | Fourteen focuses | One factory/fort-style map layer at most | Fail; recruitment, template, legion, Bone Guard, capital assault, collapse, and terminal army package absent |
| Navy | Eight focuses | Coastal availability on two nodes | Fail; flotillas, hulks, convoy missions, landings, anchorages, and corridors absent |
| Air | Seven focuses | One airbase-style map effect at most | Fail; projects/missions/stockpile costs/collapse package absent |
| Intelligence/cells | Eight focuses | Flags only on most nodes | Fail; target pools, corruption, surrender, uprising, and cured-network missions absent |
| Expansion/global campaigns | Four focuses | Hostility changes and terminal flag | Fail; campaigns, target scoring, incidents, integration absent |
| Counterwar | Four focuses | Hostility/authority changes and terminal flag | Fail; coalition targets, corridors, conversion, failure responses absent |
| Ordinary terminal | Two focuses | Strict >1000 check and live world-end effect | Gate passes; route integrity fails because four prerequisites are focus flags rather than implemented packages |

### Wendigo tree

| Required lane | Structural coverage | Playable coverage | Audit result |
|---|---:|---:|---|
| Merge/setup | Five focuses | Preserves pack/Larder/warlord state and establishes anchors | Pass with missing art/localisation |
| Winter route | Five focuses | Frozen-corridor decision and winter network | Pass |
| Recruitment | Five focuses | Pack training/capacity and paid decisions | Pass, but rewards are numerically shallow |
| Cannibal inheritance | Five focuses | Preserved legions/captains/cells/routes feed readiness | Pass |
| Anchors/countdown | Four focuses | Live anchor strength, acceleration, stabilization | Pass |
| Terminal hunt | Four focuses | Live countdown, target prioritisation, terminal lock | Pass in logic; presentation and escalating route depth incomplete |

## Structural and terminal evidence that passed

- Node counts: 72/108/28.
- No missing prerequisite reference and no prerequisite cycle in any tree.
- No duplicate focus ID or coordinate in the three files.
- All explicit mutual exclusions are reciprocal.
- Every completion reward helper referenced by a focus is defined.
- All 208 focuses have ai_will_do.
- Costs are centralized within each focus file:
  - warlord: 47 short and 25 normal
  - unified: 74 short, 25 normal, and 9 terminal
  - Wendigo: 7 short, 18 normal, and 3 terminal
- The unified hostility gate is not impossible: initial world hostility is 75 while the relevant gate is 50.
- common/scripted_triggers/014_cannibalism_triggers.txt:811-837 requires unified state, terminal readiness, network/state/population/Larder conditions, and chaos greater than the 1000 world-end threshold.
- common/scripted_triggers/014_cannibalism_wendigo_triggers.txt:101-155 requires the real Wendigo country, winter route, anchors, network/states/population/winter victories/authority/Larder, and chaos greater than 1000 before countdown/lock.
- common/scripted_effects/014_cannibalism_wendigo_effects.txt:567-589 performs the actual terminal lock, spirit replacement, leader trait, and super-event.
- Warlord pre-reveal focus text contains no Hannibal/Wendigo/master/unifier disclosure.
- Static focus-created spirit ceiling is respected:
  - warlord starts with Closed Muster Rolls, Survival Burdens, and one origin; hierarchy replaces the burden through a dynamic modifier and origin capstones swap the origin idea.
  - unified holds at most one disposition, one hierarchy, and one Larder idea.
  - Wendigo stage ideas replace one another.

## Explicit missing inventory

### Missing localisation

Exactly nine keys are missing:

1. cannibalism_warlord_focus_tree
2. cannibalism_unified_focus_tree
3. cannibalism_wendigo_focus_tree
4. cannibalism_wendigo_conjoined_hunger
5. cannibalism_wendigo_conjoined_hunger_desc
6. cannibalism_wendigo_winter_feeding_network
7. cannibalism_wendigo_winter_feeding_network_desc
8. cannibalism_wendigo_locked_terminal_form
9. cannibalism_wendigo_locked_terminal_form_desc

No focus-node title, description, or custom-tooltip key is missing.

### Missing idea assets

Registered sprite, missing DDS:

- cannibalism_authority_without_rivals
- cannibalism_battlefield_continental_larder
- cannibalism_confederation_under_one_name
- cannibalism_council_of_retained_hosts
- cannibalism_dominion_of_chains
- cannibalism_harvest_follows_victory
- cannibalism_island_host_origin
- cannibalism_larder_that_moves
- cannibalism_managed_continental_larder
- cannibalism_managed_continental_reserve
- cannibalism_many_jaws
- cannibalism_march_host_origin
- cannibalism_mobile_continental_larder
- cannibalism_one_command
- cannibalism_prison_host_origin
- cannibalism_rapid_continental_larder
- cannibalism_retained_lieutenants
- cannibalism_ritual_administration
- cannibalism_rivals_in_chains
- cannibalism_short_horizon_continent
- cannibalism_siege_commune_origin
- cannibalism_single_operational_will
- cannibalism_state_of_the_last_table
- cannibalism_unified_command_burden
- cannibalism_warlord_survival_burdens
- cannibalism_warlords_broken

Missing sprite and missing DDS:

- cannibalism_wendigo_conjoined_hunger
- cannibalism_wendigo_winter_feeding_network
- cannibalism_wendigo_locked_terminal_form

The expected idea path is gfx/interface/ideas/014_cannibalism/idea_{idea-id}.dds and the expected sprite is GFX_idea_{idea-id}.

### Missing AI paths

There are no missing ai_will_do blocks on existing focuses or existing warlord/Wendigo decisions.

The missing AI surfaces are:

1. Every unresolved unified contract in Appendix B: the corresponding decisions/missions/projects do not exist, so no AI can select targets, budget costs, react to failure, or use route mechanics.
2. Every unresolved warlord contract in Appendix B for the same reason.
3. Capability-aware route selection for the seven unified air focuses listed in F-10.
4. Achievement tracking for AI/opponent-dependent focus outcomes, because the achievement system itself is absent.

The lone externally unconsumed Wendigo flag, cannibalism_wendigo_focus_overlay_loaded, is loader bookkeeping and is not a missing player or AI path.

## Completion blockers and required re-audit

Before any focus-tree completion claim:

1. Add and verify explicit CBL tree loading.
2. Implement the unified decision/mission/project systems and make terminal readiness depend on live mechanics.
3. Implement or explicitly redesign every unresolved warlord contract.
4. Deepen origin and Evolution II route payoffs.
5. Deepen Wendigo escalation and normalize reward values.
6. Install/register all focus and idea assets.
7. Add the missing tree/idea localisation and repair pre-reveal prose.
8. Replace/define the 17 invalid Wendigo search filters.
9. Implement the 18 achievements and route hooks.
10. Re-run a focus-tree audit after the above surfaces are live.

No fallback or simplification was accepted in this audit. The current package remains incomplete.

## Appendix A — exact missing focus asset IDs

For every ID below, the live file gfx/interface/goals/014_cannibalism/goal_{ID}.dds is missing.

All warlord IDs additionally lack both GFX_goal_{ID} and GFX_goal_{ID}_shine sprite definitions. Unified and Wendigo base/shine definitions exist but point at the missing files.

### Warlord: 72

cannibalism_warlord_survive_the_first_encirclement, cannibalism_warlord_hold_the_origin_ground, cannibalism_warlord_repair_the_broken_routes, cannibalism_warlord_secure_the_first_larder, cannibalism_warlord_name_the_first_lieutenants, cannibalism_warlord_the_host_endures

cannibalism_warlord_seize_the_knives, cannibalism_warlord_break_the_captains, cannibalism_warlord_bind_the_guard_to_one_mouth, cannibalism_warlord_personal_dominion, cannibalism_warlord_divide_the_first_table, cannibalism_warlord_recognize_the_captains

cannibalism_warlord_assign_feeding_districts, cannibalism_warlord_council_of_hosts, cannibalism_warlord_free_the_captains, cannibalism_warlord_mark_the_hunting_grounds, cannibalism_warlord_share_the_captured_roads, cannibalism_warlord_no_single_mouth

cannibalism_warlord_inventory_the_captured_stores, cannibalism_warlord_secure_the_prisoner_ledger, cannibalism_warlord_restore_the_taken_workshops, cannibalism_warlord_organize_battlefield_recovery, cannibalism_warlord_establish_larder_accounting, cannibalism_warlord_rapid_consumption

cannibalism_warlord_short_horizon_larder, cannibalism_warlord_managed_herds, cannibalism_warlord_long_larder, cannibalism_warlord_mobile_larder, cannibalism_warlord_moving_larder, cannibalism_warlord_discipline_the_warbands

cannibalism_warlord_captains_as_officers, cannibalism_warlord_form_the_feast_cohorts, cannibalism_warlord_train_the_origin_specialists, cannibalism_warlord_raise_the_bone_guard, cannibalism_warlord_battlefield_harvest, cannibalism_warlord_protect_the_command_body

cannibalism_warlord_disciplined_feeding_army, cannibalism_warlord_war_doctrine_of_the_host, cannibalism_warlord_island_repair_the_ports, cannibalism_warlord_island_ambush_the_convoys, cannibalism_warlord_island_train_landing_cadres, cannibalism_warlord_island_archipelago_hunt

cannibalism_warlord_siege_fortify_feeding_districts, cannibalism_warlord_siege_open_the_tunnels, cannibalism_warlord_siege_take_the_workshops, cannibalism_warlord_siege_city_that_eats, cannibalism_warlord_march_seize_wheels_and_mounts, cannibalism_warlord_march_raid_the_depots

cannibalism_warlord_march_sabotage_the_rails, cannibalism_warlord_march_moving_front, cannibalism_warlord_prison_unite_cells_and_guards, cannibalism_warlord_prison_infiltrate_the_transfers, cannibalism_warlord_prison_arm_the_penal_columns, cannibalism_warlord_prison_lockhouse_network

cannibalism_warlord_raid_the_neighboring_states, cannibalism_warlord_mark_the_supply_hubs, cannibalism_warlord_seize_prisons_and_depots, cannibalism_warlord_open_the_predatory_corridors, cannibalism_warlord_shelter_foreign_cells, cannibalism_warlord_train_network_cadres

cannibalism_warlord_corrupt_the_enemy_officers, cannibalism_warlord_synchronized_sabotage, cannibalism_warlord_read_the_common_signs, cannibalism_warlord_accept_the_common_symbols, cannibalism_warlord_open_the_courier_routes, cannibalism_warlord_regional_common_table

cannibalism_warlord_copy_the_shared_doctrine, cannibalism_warlord_divert_the_courier_routes, cannibalism_warlord_regional_stolen_routes, cannibalism_warlord_execute_the_couriers, cannibalism_warlord_fortify_independent_ground, cannibalism_warlord_independent_regional_host

### Unified CBL: 108

CBL_reveal_the_command, CBL_summon_the_warlords, CBL_choose_the_first_command_capital, CBL_audit_the_submitted_hosts, CBL_bind_the_network_territories, CBL_settle_the_host_question

CBL_open_the_continental_ledger, CBL_establish_the_first_continental_command, CBL_keep_the_lieutenants, CBL_seat_the_regional_governors, CBL_preserve_the_origin_commands, CBL_arbitrate_the_captains

CBL_council_of_retained_hosts, CBL_break_the_warlords, CBL_seize_the_hidden_hoards, CBL_dissolve_the_regional_commands, CBL_appoint_the_bone_officers, CBL_authority_without_rivals

CBL_chain_the_rivals, CBL_take_their_heirs, CBL_levy_hostage_tribute, CBL_rotate_the_hostage_governors, CBL_dominion_of_chains, CBL_one_command

CBL_standardize_host_ranks, CBL_centralize_the_larder_quota, CBL_command_without_distance, CBL_the_single_operational_will, CBL_many_jaws, CBL_charter_the_regional_hosts

CBL_divide_the_campaign_theaters, CBL_covenant_of_mutual_predation, CBL_confederation_under_one_name, CBL_ritual_administration, CBL_codify_the_feeding_law, CBL_ordain_the_punishment_tables

CBL_census_of_mouths_and_chains, CBL_the_state_of_the_last_table, CBL_central_accounting, CBL_classify_the_consumption_states, CBL_build_the_storage_network, CBL_boards_of_captured_industry

CBL_continental_larder_doctrine, CBL_burn_through_the_near_states, CBL_feed_the_legion_surge, CBL_exhaust_the_frontier, CBL_short_horizon_continent, CBL_preserve_the_working_herds

CBL_rotate_the_feeding_districts, CBL_police_the_long_harvest, CBL_managed_continental_reserve, CBL_prisoner_trains, CBL_escort_the_larder_columns, CBL_oceanic_hulk_routes

CBL_the_larder_that_moves, CBL_mark_the_battlefield_yields, CBL_recovery_battalions, CBL_convert_the_captured_hospitals, CBL_harvest_follows_victory, CBL_continents_as_supply_regions

CBL_abolish_the_old_supply_ceiling, CBL_integrate_the_warbands, CBL_map_the_origin_templates, CBL_standardize_captured_calibers, CBL_raise_the_cannibal_legions, CBL_legion_reinforcement_tables

CBL_legions_of_the_continents, CBL_bone_guard_command, CBL_shield_the_supreme_body, CBL_breach_the_enemy_capitals, CBL_enemy_collapse_doctrine, CBL_harvest_the_rout

CBL_break_the_retreating_fronts, CBL_coordinate_the_three_armies, CBL_the_army_that_does_not_end, CBL_captured_shipyards, CBL_raider_flotillas, CBL_prison_hulks

CBL_convoy_hunt_tables, CBL_amphibious_feeding_columns, CBL_silent_anchorages, CBL_island_command_network, CBL_every_ocean_a_corridor, CBL_repair_the_captured_airframes

CBL_terror_reconnaissance, CBL_interdiction_markers, CBL_airborne_cell_insertion, CBL_battlefield_recovery_signals, CBL_fear_bombing_tables, CBL_skies_over_the_larder

CBL_global_courier_network, CBL_prison_and_port_cells, CBL_corrupt_the_enemy_officers, CBL_perfect_the_false_surrender, CBL_sleep_beneath_retreat, CBL_synchronize_the_uprisings

CBL_reactivate_the_cured_networks, CBL_the_war_begins_inside, CBL_read_the_continental_weakness, CBL_terror_ultimata, CBL_cell_backed_border_incidents, CBL_host_theaters_without_borders

CBL_measure_world_hostility, CBL_break_the_relief_corridors, CBL_sever_the_coalition_command, CBL_consume_the_counterwar, CBL_final_global_mobilization, CBL_dismantle_the_ordinary_world

### Wendigo: 28

ZZZ_wendigo_bind_the_two_hungers, ZZZ_wendigo_preserve_the_pack, ZZZ_wendigo_keep_the_larder_ledger, ZZZ_wendigo_bind_the_warlord_commands, ZZZ_wendigo_raise_the_first_anchors, ZZZ_wendigo_open_the_winter_hunt

ZZZ_wendigo_freeze_the_supply_corridors, ZZZ_wendigo_march_through_the_blizzard, ZZZ_wendigo_count_the_winter_victories, ZZZ_wendigo_raise_the_winter_network, ZZZ_wendigo_drill_the_original_pack, ZZZ_wendigo_open_the_pack_musters

ZZZ_wendigo_feed_the_anchor_guardians, ZZZ_wendigo_expand_the_hunting_packs, ZZZ_wendigo_army_of_the_frozen_larder, ZZZ_wendigo_keep_the_cannibal_legions, ZZZ_wendigo_retain_the_warlord_captains, ZZZ_wendigo_keep_the_foreign_cells

ZZZ_wendigo_join_the_larder_routes, ZZZ_wendigo_all_inheritances_intact, ZZZ_wendigo_link_the_transformation_anchors, ZZZ_wendigo_mark_the_irreversible_road, ZZZ_wendigo_accelerate_the_transformation, ZZZ_wendigo_stabilize_the_anchor_chain

ZZZ_wendigo_begin_the_countdown, ZZZ_wendigo_designate_the_last_hunt, ZZZ_wendigo_hunt_every_remaining_capital, ZZZ_wendigo_the_world_beneath_winter

## Appendix B — exact externally unconsumed reward contracts

An externally unconsumed contract is a country flag set by a focus reward but never read anywhere else in common/, events/, history/, or interface/. This is stricter than merely checking that the scripted reward helper exists.

### Warlord: 53 missing external contracts

- cannibalism_warlord_anti_decapitation_open
- cannibalism_warlord_battlefield_harvest_open
- cannibalism_warlord_capital_repairs_open
- cannibalism_warlord_commune_absorption_open
- cannibalism_warlord_confederacy_doctrine_open
- cannibalism_warlord_convergence_leverage_open
- cannibalism_warlord_council_doctrine_open
- cannibalism_warlord_council_votes_open
- cannibalism_warlord_courier_routes_open
- cannibalism_warlord_defiance_endgame_open
- cannibalism_warlord_depot_raids_open
- cannibalism_warlord_distributed_recruitment_open
- cannibalism_warlord_diverted_couriers_open
- cannibalism_warlord_feeding_districts_open
- cannibalism_warlord_hidden_anchorages_open
- cannibalism_warlord_hierarchy_routes_open
- cannibalism_warlord_independent_fortification_open
- cannibalism_warlord_island_endgame_open
- cannibalism_warlord_landing_operations_open
- cannibalism_warlord_larder_accounting_open
- cannibalism_warlord_larder_inventory_open
- cannibalism_warlord_leader_protection_open
- cannibalism_warlord_lieutenant_assignments_open
- cannibalism_warlord_managed_herd_actions_open
- cannibalism_warlord_manipulation_endgame_open
- cannibalism_warlord_march_endgame_open
- cannibalism_warlord_mobile_larder_escort_open
- cannibalism_warlord_network_manipulation_open
- cannibalism_warlord_network_routes_open
- cannibalism_warlord_officer_corruption_open
- cannibalism_warlord_officer_training_open
- cannibalism_warlord_origin_defense_open
- cannibalism_warlord_penal_column_actions_open
- cannibalism_warlord_personal_guard_doctrine_open
- cannibalism_warlord_predatory_corridors_open
- cannibalism_warlord_prison_depot_raids_open
- cannibalism_warlord_prison_endgame_open
- cannibalism_warlord_prisoner_ledger_open
- cannibalism_warlord_provincial_servants_open
- cannibalism_warlord_purge_decisions_open
- cannibalism_warlord_rail_sabotage_open
- cannibalism_warlord_rapid_consumption_open
- cannibalism_warlord_relief_ambush_open
- cannibalism_warlord_shared_roads_open
- cannibalism_warlord_siege_endgame_open
- cannibalism_warlord_state_exhaustion_risk
- cannibalism_warlord_submission_preparation_open
- cannibalism_warlord_supply_targeting_open
- cannibalism_warlord_survival_order_open
- cannibalism_warlord_transfer_infiltration_open
- cannibalism_warlord_tunnel_operations_open
- cannibalism_warlord_tyrant_doctrine_open
- cannibalism_warlord_workshop_conversion_open

The four other externally unconsumed warlord flags—cannibalism_warlord_larder_order_complete, cannibalism_warlord_military_order_complete, cannibalism_warlord_network_order_complete, and cannibalism_warlord_operating_order_open—are consumed inside the same reward-effect file to maintain the dynamic operating-order package, so they are not counted as missing rewards.

### Unified CBL: 208 externally unconsumed contracts

The complete externally unconsumed set follows. The four entries explicitly marked internal bookkeeping are consumed by cannibalism_unified_focus_refresh_terminal_route inside the same file; the remaining 204 have no live downstream consumer.

- cannibalism_hannibal_terminal_trait_upgrade_pending
- cannibalism_unified_air_front_collapse_package_pending
- cannibalism_unified_air_interdiction_targets_open
- cannibalism_unified_air_network_capstone
- cannibalism_unified_air_recovery_signals_open
- cannibalism_unified_air_target_marking_open
- cannibalism_unified_airborne_cell_insertion_open
- cannibalism_unified_airframe_repair_projects_open
- cannibalism_unified_airframe_stockpile_costs_required
- cannibalism_unified_amphibious_column_decisions_open
- cannibalism_unified_anchorage_discovery_risk
- cannibalism_unified_archipelago_command_missions_open
- cannibalism_unified_battlefield_harvest_caps_required
- cannibalism_unified_battlefield_larder_capstone
- cannibalism_unified_battlefield_processing_projects_open
- cannibalism_unified_battlefield_yield_decisions_open
- cannibalism_unified_bone_guard_breach_package_pending
- cannibalism_unified_bone_guard_cap_active
- cannibalism_unified_bone_guard_cap_upgraded
- cannibalism_unified_bone_guard_recruitment_open
- cannibalism_unified_bone_officer_assignments_open
- cannibalism_unified_border_incident_decisions_open
- cannibalism_unified_caliber_standardization_projects_open
- cannibalism_unified_campaign_category_open
- cannibalism_unified_cannibal_legion_recruitment_open
- cannibalism_unified_capital_assault_missions_open
- cannibalism_unified_capital_projects_open
- cannibalism_unified_captain_arbitration_open
- cannibalism_unified_captured_equipment_conversion_open
- cannibalism_unified_captured_hospital_conversion_open
- cannibalism_unified_captured_hull_conversion_open
- cannibalism_unified_captured_industry_projects_open
- cannibalism_unified_cell_category_open
- cannibalism_unified_central_accounting_open
- cannibalism_unified_central_command_decisions_open
- cannibalism_unified_central_quota_decisions_open
- cannibalism_unified_chained_dominion_open
- cannibalism_unified_coalition_command_operations_open
- cannibalism_unified_coalition_officer_targets_open
- cannibalism_unified_command_category_open
- cannibalism_unified_command_dissolution_open
- cannibalism_unified_confederation_capstone
- cannibalism_unified_consumption_stage_decisions_open
- cannibalism_unified_continental_supply_regions_open
- cannibalism_unified_convoy_harvest_caps_required
- cannibalism_unified_convoy_hunt_missions_open
- cannibalism_unified_corridor_target_pool_open
- cannibalism_unified_corruption_exposure_missions_open
- cannibalism_unified_counterwar_capstone
- cannibalism_unified_counterwar_category_open
- cannibalism_unified_counterwar_conversion_open
- cannibalism_unified_cured_country_reactivation_missions_open
- cannibalism_unified_direct_authority_open
- cannibalism_unified_disconnected_region_management_open
- cannibalism_unified_disposition_routes_open
- cannibalism_unified_distant_governor_management_open
- cannibalism_unified_distant_theater_priority_open
- cannibalism_unified_district_recovery_missions_open
- cannibalism_unified_dormant_cell_missions_open
- cannibalism_unified_dynamic_campaign_scoring_open
- cannibalism_unified_enemy_collapse_decisions_open
- cannibalism_unified_exhausted_state_abandonment_open
- cannibalism_unified_external_reinfection_open
- cannibalism_unified_false_surrender_decisions_open
- cannibalism_unified_false_surrender_failure_risk
- cannibalism_unified_fear_bombing_escalation_risk
- cannibalism_unified_fear_bombing_missions_open
- cannibalism_unified_fear_pressure_tracking_open
- cannibalism_unified_feeding_law_decisions_open
- cannibalism_unified_feeding_rotation_decisions_open
- cannibalism_unified_final_global_mobilization_active
- cannibalism_unified_foreign_cell_target_pool_open
- cannibalism_unified_front_cascade_missions_open
- cannibalism_unified_frontier_exhaustion_missions_open
- cannibalism_unified_global_campaigns_open
- cannibalism_unified_global_courier_decisions_open
- cannibalism_unified_global_mechanic_open
- cannibalism_unified_global_naval_corridors_open
- cannibalism_unified_governor_loyalty_missions_open
- cannibalism_unified_herd_revolt_missions_open
- cannibalism_unified_hidden_hoard_investigations_open
- cannibalism_unified_hierarchy_many_jaws
- cannibalism_unified_hierarchy_one_command
- cannibalism_unified_hierarchy_ritual
- cannibalism_unified_hoard_seizure_missions_open
- cannibalism_unified_host_charters_open
- cannibalism_unified_host_conflict_missions_open
- cannibalism_unified_hostage_defection_risk
- cannibalism_unified_hostage_governance_open
- cannibalism_unified_hostage_heir_missions_open
- cannibalism_unified_hostage_rotation_open
- cannibalism_unified_hostage_tribute_open
- cannibalism_unified_hulk_escort_missions_open
- cannibalism_unified_incident_escalation_missions_open
- cannibalism_unified_internal_front_capstone
- cannibalism_unified_island_integration_open
- cannibalism_unified_joint_army_operations_open
- cannibalism_unified_landing_corridor_missions_open
- cannibalism_unified_larder_audit_missions_open
- cannibalism_unified_larder_category_open
- cannibalism_unified_larder_column_escort_open
- cannibalism_unified_larder_method_battlefield
- cannibalism_unified_larder_method_managed
- cannibalism_unified_larder_method_mobile
- cannibalism_unified_larder_method_rapid
- cannibalism_unified_larder_method_routes_open
- cannibalism_unified_larder_route_projects_open
- cannibalism_unified_larder_tradeoff_missions_open
- cannibalism_unified_law_enforcement_missions_open
- cannibalism_unified_leader_protection_missions_open
- cannibalism_unified_legion_cap_active
- cannibalism_unified_legion_cap_upgraded
- cannibalism_unified_legion_deaths_accounting_required
- cannibalism_unified_legion_reinforcement_open
- cannibalism_unified_legion_surge_decisions_open
- cannibalism_unified_legion_theaters_open
- cannibalism_unified_lieutenant_governance_open
- cannibalism_unified_lieutenant_registry_open
- cannibalism_unified_lieutenant_rivalry_missions_open
- cannibalism_unified_long_campaign_horizon
- cannibalism_unified_long_harvest_policing_open
- cannibalism_unified_loyal_officer_training_open
- cannibalism_unified_major_victory_receipts_open
- cannibalism_unified_managed_herd_decisions_open
- cannibalism_unified_managed_larder_capstone
- cannibalism_unified_marked_battlefield_missions_open
- cannibalism_unified_mobile_global_routes_open
- cannibalism_unified_mobile_larder_capstone
- cannibalism_unified_mutual_predation_votes_open
- cannibalism_unified_network_anchor_capitals_open
- cannibalism_unified_ocean_crossing_package_pending
- cannibalism_unified_oceanic_hulk_routes_open
- cannibalism_unified_officer_corruption_decisions_open
- cannibalism_unified_organized_resistance_risk
- cannibalism_unified_origin_specialist_recruitment_open
- cannibalism_unified_origin_specialists_preserved
- cannibalism_unified_origin_template_mapping_open
- cannibalism_unified_postwar_integration_open
- cannibalism_unified_prewar_cell_operations_open
- cannibalism_unified_prison_administration_projects_open
- cannibalism_unified_prison_hulk_decisions_open
- cannibalism_unified_prison_hulk_transport_open
- cannibalism_unified_prison_port_cell_missions_open
- cannibalism_unified_prisoner_train_decisions_open
- cannibalism_unified_public_command_established
- cannibalism_unified_punishment_table_decisions_open
- cannibalism_unified_purge_resistance_risk
- cannibalism_unified_raider_construction_costs_required
- cannibalism_unified_raider_flotilla_decisions_open
- cannibalism_unified_rank_standardization_open
- cannibalism_unified_rapid_consumption_decisions_open
- cannibalism_unified_rapid_larder_capstone
- cannibalism_unified_rapid_recruitment_cost_scaling_open
- cannibalism_unified_recovery_battalion_missions_open
- cannibalism_unified_regional_army_compacts_open
- cannibalism_unified_regional_governor_assignments_open
- cannibalism_unified_regional_host_votes_open
- cannibalism_unified_regional_recruitment_open
- cannibalism_unified_regional_theater_missions_open
- cannibalism_unified_relief_corridor_attack_missions_open
- cannibalism_unified_remote_command_missions_open
- cannibalism_unified_retained_host_council_open
- cannibalism_unified_retreat_cell_preservation_open
- cannibalism_unified_retreat_disruption_open
- cannibalism_unified_ritual_administration_open
- cannibalism_unified_ritual_census_open
- cannibalism_unified_ritual_state_capstone
- cannibalism_unified_rival_purges_open
- cannibalism_unified_rout_harvest_caps_required
- cannibalism_unified_rout_harvest_missions_open
- cannibalism_unified_route_interdiction_missions_open
- cannibalism_unified_shipyard_projects_open
- cannibalism_unified_short_campaign_horizon
- cannibalism_unified_silent_anchorage_projects_open
- cannibalism_unified_single_will_capstone
- cannibalism_unified_standard_training_missions_open
- cannibalism_unified_state_classification_open
- cannibalism_unified_state_exhaustion_risk
- cannibalism_unified_state_ledger_open
- cannibalism_unified_storage_projects_open
- cannibalism_unified_submission_decisions_open
- cannibalism_unified_supply_ceiling_package_pending
- cannibalism_unified_supply_interdiction_missions_open
- cannibalism_unified_synchronized_uprising_missions_open
- cannibalism_unified_template_conversion_missions_open
- cannibalism_unified_terminal_army_gate — internal terminal bookkeeping; not counted among the 204 missing downstream contracts
- cannibalism_unified_terminal_army_package_active
- cannibalism_unified_terminal_consumption_preparation_open
- cannibalism_unified_terminal_counterwar_gate — internal terminal bookkeeping; not counted among the 204 missing downstream contracts
- cannibalism_unified_terminal_expansion_gate — internal terminal bookkeeping; not counted among the 204 missing downstream contracts
- cannibalism_unified_terminal_larder_gate — internal terminal bookkeeping; not counted among the 204 missing downstream contracts
- cannibalism_unified_territorial_integration_open
- cannibalism_unified_terror_reconnaissance_missions_open
- cannibalism_unified_terror_ultimata_open
- cannibalism_unified_theater_command_assignments_open
- cannibalism_unified_three_army_coordination_open
- cannibalism_unified_transport_aircraft_costs_required
- cannibalism_unified_transport_escort_burden
- cannibalism_unified_tribute_failure_missions_open
- cannibalism_unified_ultimatum_refusal_missions_open
- cannibalism_unified_uprising_target_cap_active
- cannibalism_unified_victory_harvest_scaling_open
- cannibalism_unified_warband_integration_open
- cannibalism_unified_warlord_audit_open
- cannibalism_unified_warlord_response_resolution_open
- cannibalism_unified_warlord_settlement_category_open
- cannibalism_unified_workshop_conversion_open
- cannibalism_unified_world_hostility_breakdown_open

### Wendigo

No missing downstream player contract was found. cannibalism_wendigo_focus_overlay_loaded has no external consumer, but is explicit loader bookkeeping. The Wendigo defects are reward depth, presentation, localisation, and search-filter validity rather than absent consumers.

## Appendix C — focus rewards with no live output

These completion helpers do not add or remove an idea/dynamic modifier, alter a variable, create a map/state/country effect, call a live downstream system, or set a flag that another gameplay surface consumes.

### Warlord: 5

- cannibalism_warlord_captains_as_officers
- cannibalism_warlord_siege_open_the_tunnels
- cannibalism_warlord_march_sabotage_the_rails
- cannibalism_warlord_mark_the_supply_hubs
- cannibalism_warlord_read_the_common_signs

### Unified CBL: 61

- CBL_reveal_the_command
- CBL_summon_the_warlords
- CBL_audit_the_submitted_hosts
- CBL_settle_the_host_question
- CBL_seat_the_regional_governors
- CBL_preserve_the_origin_commands
- CBL_arbitrate_the_captains
- CBL_seize_the_hidden_hoards
- CBL_appoint_the_bone_officers
- CBL_take_their_heirs
- CBL_levy_hostage_tribute
- CBL_rotate_the_hostage_governors
- CBL_standardize_host_ranks
- CBL_command_without_distance
- CBL_charter_the_regional_hosts
- CBL_divide_the_campaign_theaters
- CBL_covenant_of_mutual_predation
- CBL_codify_the_feeding_law
- CBL_census_of_mouths_and_chains
- CBL_central_accounting
- CBL_classify_the_consumption_states
- CBL_continental_larder_doctrine
- CBL_rotate_the_feeding_districts
- CBL_escort_the_larder_columns
- CBL_recovery_battalions
- CBL_convert_the_captured_hospitals
- CBL_integrate_the_warbands
- CBL_map_the_origin_templates
- CBL_raise_the_cannibal_legions
- CBL_legion_reinforcement_tables
- CBL_legions_of_the_continents
- CBL_bone_guard_command
- CBL_breach_the_enemy_capitals
- CBL_enemy_collapse_doctrine
- CBL_harvest_the_rout
- CBL_break_the_retreating_fronts
- CBL_coordinate_the_three_armies
- CBL_raider_flotillas
- CBL_prison_hulks
- CBL_convoy_hunt_tables
- CBL_amphibious_feeding_columns
- CBL_silent_anchorages
- CBL_island_command_network
- CBL_every_ocean_a_corridor
- CBL_terror_reconnaissance
- CBL_interdiction_markers
- CBL_airborne_cell_insertion
- CBL_battlefield_recovery_signals
- CBL_skies_over_the_larder
- CBL_global_courier_network
- CBL_prison_and_port_cells
- CBL_corrupt_the_enemy_officers
- CBL_perfect_the_false_surrender
- CBL_sleep_beneath_retreat
- CBL_synchronize_the_uprisings
- CBL_reactivate_the_cured_networks
- CBL_the_war_begins_inside
- CBL_read_the_continental_weakness
- CBL_measure_world_hostility
- CBL_break_the_relief_corridors
- CBL_sever_the_coalition_command

Four additional unified capstones—CBL_abolish_the_old_supply_ceiling, CBL_the_army_that_does_not_end, CBL_host_theaters_without_borders, and CBL_consume_the_counterwar—also set otherwise unused package flags, but they call cannibalism_unified_focus_refresh_terminal_route and therefore have the narrow live effect of satisfying an ordinary-terminal focus gate. They are not counted among the 61 wholly inert rewards.

No Wendigo focus reward is wholly inert.
