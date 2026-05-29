# Angelic Directorate Clone World-End Path Specification

## Purpose

This feature turns the existing Mengele / Angelic Directorate and triggerable Army of Clones systems into a late world-end path rather than a single scenario country. The path is built around hidden cloning infrastructure, foreign scientific aid fronts, deniable military assistance, and a final coordinated activation of clone-controlled cells abroad.

The path is deliberately late. It requires the Directorate to be a major power, to have completed the deep clone-state focus branch, to build a hidden foreign network through decisions and acceptance events, and to reach world-end chaos conditions before the final focus can activate the network.

## Tone

The early foreign contacts should look useful, suspicious, and deniable:

- emergency medical-industrial aid
- free biological-defense specialists
- anti-collapse military modernization
- replacement manpower and laboratory infrastructure
- sealed scientific advisers

Foreign governments do not fully understand the cost. The Directorate presents the project as modernization, medical logistics, and emergency defense support. Later symptoms appear as missing personnel, sealed laboratories, duplicated soldiers, unknown convoys, and staff who answer to foreign research directors.

The final event is not a normal invasion. It is a synchronized activation of a larger-than-expected network.

## Existing Integration Points

The implementation extends existing files instead of creating a parallel subsystem:

- `common/national_focus/germany_mengele_clone_army.txt`
- `common/decisions/germany_mengele_decisions.txt`
- `common/decisions/categories/germany_mengele_categories.txt`
- `common/script_constants/germany_mengele_constants.txt`
- `common/scripted_effects/germany_mengele_effects.txt`
- `common/scripted_triggers/germany_mengele_triggers.txt`
- `common/ideas/germany_mengele_ideas.txt`
- `events/germany_mengele.txt`
- `localisation/english/germany_mengele_l_english.yml`
- `interface/germany_mengele_world_order.gfx`
- `interface/chaosx_super_events.gfx`
- `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `music/chaosx_super_event_music.asset`
- `sound/chaosx_sound.asset`
- `docs/systems/world_threat_mechanic.md`

The existing `mengele_clone_army_focus_tree` becomes the late Directorate tree as well as the triggerable Army of Clones tree. When the Angelic Directorate wins the Germany civil war, it loads this tree. The scenario country already loads it on creation.

## Flag and Cosmetic Identity

Create a fictional in-universe fascist research-state flag for:

- `germany_mengele_angelic_directorate`
- `mengele_clone_client_regime`

Palette:

- red field
- white disc or central panel
- black authoritarian research symbol
- historical swastika element as requested
- fictional biomedical / cloning / laboratory / military experimentation emblem centered over the field

Required HOI4 flag outputs:

- `gfx/flags/germany_mengele_angelic_directorate.tga`
- `gfx/flags/medium/germany_mengele_angelic_directorate.tga`
- `gfx/flags/small/germany_mengele_angelic_directorate.tga`
- `gfx/flags/mengele_clone_client_regime.tga`
- `gfx/flags/medium/mengele_clone_client_regime.tga`
- `gfx/flags/small/mengele_clone_client_regime.tga`

The implementation also includes ideology-suffixed copies for both cosmetic tags in all three flag folders so HOI4 cosmetic-tag flag lookup cannot fall through to missing ideology assets.

Because HOI4 country flags use the flag folder directly rather than a `.gfx` sprite definition, the flag wiring is done by cosmetic tag name and localisation.

## Hidden Cloning Network

### Directorate Decisions

The Directorate gets a decision category once it is either:

- the triggerable Army of Clones country, or
- the victorious Angelic Directorate.

New late decisions are unlocked by focus:

- `Dispatch Biomedical Aid Mission`: sends a hidden offer to one eligible foreign government.
- `Deepen Foreign Tank Network`: targets an existing host and adds more depth, more facility value, and another hidden marker if possible.
- `Compile Activation Ledger`: recalculates network strength, facility count, and industrial/military ranking flags.

These are not random-event pool events and do not create news popups.

### Host Eligibility

A country can receive an offer if it:

- exists
- uses normal civilian systems
- is not the Directorate
- is not a subject of the Directorate
- is not already a clone client
- is not a zombie country or other non-normal crisis country
- has at least one owned controlled state
- has not recently rejected the mission
- is not already at war with the Directorate unless desperate enough for the deeper branch

Acceptance is more likely if the country is desperate:

- losing a war
- high surrender progress
- unstable
- authoritarian or extremist
- high chaos exposure
- isolated or not in a faction
- threatened by a major power

Acceptance is less likely if the country is:

- democratic and stable
- a strong major power
- internally secure
- already hostile to the Directorate
- not under enough pressure

### Hidden Markers

Acceptance marks:

- a country flag: `mengele_hidden_clone_network_host`
- a state flag on a selected owned controlled state: `mengele_hidden_clone_facility`
- country variables:
  - `mengele_hidden_clone_depth`
  - `mengele_hidden_clone_facility_count`
  - `mengele_hidden_clone_strength`
- Directorate variables:
  - `mengele_clone_network_hosts`
  - `mengele_clone_network_facilities`
  - `mengele_clone_network_strength`

The country-level marker represents foreign staff, indoctrination cells, sealed laboratories, recruitment and replacement files, and Directorate-controlled biomedical staff.

## Directorate Preparation

The new late focus branch appears only after `MCL_the_numbered_future` is complete and the tree layout is refreshed. This prevents the world-end focus from being visible before the state has already committed to the numbered future.

New focus branch:

1. `MCL_foreign_aid_fronts`
2. `MCL_embassy_science_cells`
3. `MCL_hidden_tank_consortia`
4. `MCL_directorate_project_registry`
5. `MCL_global_replacement_maps`
6. `MCL_the_numbered_world`

The branch unlocks the foreign network decisions, raises network capacity, makes the reusable Directorate special-project registry available for research, and arms the final activation focus.

## Final Focus Requirements

`MCL_the_numbered_world` requires:

- the branch prerequisites completed
- Directorate is a major country
- `global.chaos_meter_value > 1000`
- no `world_end`
- no `world_end_disabled`
- at least the configured hidden host count
- at least the configured hidden facility count
- at least the configured network strength
- either top-three industrial status or top-three military status
- not capitulated

The top-three check is calculated by `mengele_clone_world_order_refresh_rank_status`, which counts countries with more factories than the Directorate and countries with higher army strength ratio. The final trigger accepts the Directorate if fewer than three countries exceed it in either category.

## World-End Scenario

When the final focus completes, `mengele_clone_world_order_launch`:

- sets `world_end`
- sets `world_threat_source_mengele`
- sets `world_end_angelic_world_order` or `world_end_aryan_supremacy`
- shows super-event slot `13`
- sets `global.current_super_event_audio_id = 13`
- grants `mengele_clone_world_order_state`
- records the chaos history reason `mengele_world_order`
- refreshes world threat state
- activates all hidden host facilities
- creates clone client regimes from hidden hosts
- transfers hidden facility states into those regimes
- puppets the clone clients to the Directorate
- spawns clone infantry formations scaled by host depth, facility count, and network strength
- has the Directorate declare on eligible major opponents and neighboring targets through guarded `can_declare_war_on` checks

Scenario names:

- normal path: `Angelic World Order`
- Aryan variant: `Aryan Supremacy`

The Aryan variant is used if the country is the Aryan scenario type or has completed the Aryan/Perfect Aryan clone branch.

## Clone Client Regimes

Each host generates a dynamic country from its original host tag and copy tag, then receives the `mengele_clone_client_regime` cosmetic tag. The client is fascist, non-electoral, and puppeted to the Directorate. It receives:

- `mengele_clone_client_state`
- clone infantry equipment
- support equipment
- manpower
- clone divisions spawned in its transferred facility state

If a host accepted deeply, the client transfers more of the host's facility-marked territory and spawns more formations.

## Final National Idea

`mengele_clone_world_order_state` represents:

- mass clone production
- centralized biomedical command
- forced loyalty
- accelerated military replacement
- hidden foreign infrastructure
- ideological control

The idea gives strong but specific bonuses:

- weekly manpower
- recruitable population
- organization and recovery
- army attack/defense
- production and special-project speed
- resistance suppression in occupied states
- stability/political pressure costs

`mengele_clone_client_state` is smaller and represents activated foreign cells under Directorate command.

## Special Project Registry

The branch uses two reusable effects:

- `make_random_directorate_special_project_researchable`
- `make_all_directorate_special_projects_researchable`

These are the extension points for future Chaos Redux biological or clone-related special projects that the Directorate should be able to research from its capstone or late-tree branch. The current registry covers `weaponize_the_zombies` and `sp_mengele_cloning`. When a future project is added, its project-specific availability flag should be added to these effects and to the matching project `visible` or `available` gates instead of duplicating direct completion logic in focus rewards.

## Super-Event Package

Super-event slot `13` is reserved for this world end.

Image sprite:

- `GFX_super_event_angelic_world_order`
- `gfx/super_events/super_event_angelic_world_order.dds`

Quote:

- Revelation 13:4, KJV, verified from Bible Gateway.

Audio:

- `chaosx_super_event_13_*` music variants use `music/super_event_angelic_world_order.ogg`.
- `chaosx_super_event_13_sound_*` sound variants use `chaosx_super_event_angelic_world_order_track`.
- The sound-channel derivative is `sound/chaosx_super_event_angelic_world_order.wav`.
- Source, license, duration, and conversion notes are recorded in `docs/super_events/super_event_audio_packages.md`.

## Asset Package

Required generated assets:

- Directorate flag source, processed PNG preview, and HOI4 TGA sizes
- clone client flag copies
- `gfx/interface/ideas/idea_mengele_clone_world_order.dds`
- `gfx/interface/ideas/idea_mengele_clone_client_state.dds`
- `gfx/interface/decisions/decision_mengele_hidden_clone_network.dds`
- `gfx/interface/goals/focus_mengele_numbered_world.dds`
- `gfx/super_events/super_event_angelic_world_order.dds`

All generated assets must be recorded in `docs/assets/chaos_redux_asset_manifest.md`.

## Validation Checklist

- Angelic Directorate loads the clone focus tree after victory.
- The late branch is hidden until the numbered future is complete.
- Hidden network decisions unlock through the late branch.
- Foreign offer acceptance uses AI weights based on desperation, ideology, stability, war pressure, isolation, and hostility.
- Accepted countries receive country and state markers without news popups.
- Network strength/facility/host variables increment and can be recalculated.
- Final focus cannot complete without chaos over `1000`, major status, network thresholds, and top-three industry or army status.
- Launch sets `world_end` and scenario-specific flags.
- Launch grants the final idea.
- Hidden hosts activate into clone client regimes.
- Clone client regimes are puppets and receive divisions scaled to network depth.
- Directorate and clients use guarded war declarations.
- Aryan variant uses `Aryan Supremacy`.
- Normal variant uses `Angelic World Order`.
- Super-event slot `13` has image, title, quote, button, description, and audio definitions.
- World-threat state refreshes.
- Localisation covers focuses, decisions, ideas, events, cosmetic tags, and tooltips.
- Docs and asset manifest are updated.
