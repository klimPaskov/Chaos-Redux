# Repository Explorer Handoff

## Scope read

- Parent task: convert the accepted Air Cleanliness and Fallout design into an implementation-ready repository plan
- Repository inspected: `klimPaskov/Chaos-Redux`
- Commit inspected: `8044d232376fef3a1a3ca1ea3e0d487523924cc6`
- Access mode: read only
- Gameplay edits: none
- Source package: `air_cleanliness_fallout_planning_package_expanded.zip`
- Required project sources read in this environment: all uploaded Markdown, TOML, and CSV files, plus every Markdown file in the expanded planning package
- Local source unavailable in this environment: writable Windows checkout, local Hearts of Iron IV installation, and local official documentation folder

## Primary findings

1. Air Contamination already has a host-owned monthly update and a shared daily state-death pass.
2. Chaos Redux already has a reusable scripted state mapmode framework.
3. The current winter mechanic is a random-state pulse and does not meet the accepted state-phase design.
4. A stale Fallout event block is defined in `events/chemical_warfare_events.txt` and still uses normal super-event wiring.
5. The stale block must be deleted. No compatibility event remains in that namespace.
6. Raw id 8 is already assigned in the inspected snapshot, so Fallout must receive the next free registry id after a live scan.
7. The mapmode sprite strip metadata and its documentation disagree about the current frame count.
8. The repository contains no observed `every_province` iteration pattern.
9. The existing custom tag pool is substantial but already owned by other feature packages.
10. Runtime focus assignment and shared-focus composition have usable precedents.

## Relevant files

| Path | Why it matters | Observed evidence |
| --- | --- | --- |
| `common/on_actions/chaosx_on_actions_chaos_meter.txt` | host authority for monthly Air update and daily Chaos Meter work | monthly host calls `air_contamination_monthly_update` once |
| `common/scripted_effects/chaos_meter_effects.txt` | current Air, winter, fallout, deaths, category degradation, treaty helpers | contains monthly state scan, random winter pulse, irreversible effects, treaty helpers, nuclear hooks |
| `common/script_constants/chaos_meter_constants.txt` | current Air thresholds, winter values, nuclear and death tuning | threshold table includes 25, 50, 75, 100, and 1000 percent entries |
| `common/dynamic_modifiers/nuclear_state_modifiers.txt` | nuclear fallout marker and visible state effects | `nuclear_fallout_state` is a marker while scripted logic applies population loss |
| `events/chemical_warfare_events.txt` | contamination milestones plus a stale Fallout block | delete the Fallout block and keep the file limited to Air and chemical events |
| `common/map_modes/chaosx_state_map_modes.txt` | closest mapmode precedent | defines deaths and contamination state mapmodes with daily updates |
| `common/script_constants/state_map_modes_constants.txt` | mapmode palette and threshold tuning | separates deaths and contamination constants |
| `common/scripted_triggers/cbw_triggers.txt` | reusable state hazard detection | contains mapmode contamination trigger family |
| `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt` | mapmode tooltip and selected-state text | branches by active state hazards |
| `localisation/english/chaosx_map_modes_l_english.yml` | visible names and tooltips | contains current two mapmode key families |
| `interface/mapmodes_interface.gfx` | frame count and strip registration | says `noOfFrames = 19` while comments claim two appended slots |
| `docs/systems/state_map_modes.md` | mapmode behavior and slot claims | says strips have 20 frames and assigns slots 19 and 20 |
| `common/script_constants/chaosx_triggerable_scenarios_constants.txt` | scenario ids, sort values, types, intensities | the inspected snapshot ends at raw id 8, which is assigned to Africa Is One |
| `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt` | registry, sort, launch, and scenario dispatch | explicit arrays contain every current scenario |
| `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt` | launch eligibility | every current scenario has an explicit branch |
| `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt` | scenario name, id, details, type, intensity text | every scenario is mapped by explicit id checks |
| `common/scripted_guis/chaosx_scripted_gui_settings.txt` | scenario button and confirmation behavior | must route the new scenario using current selected state |
| `events/chaosx_triggerable_scenarios.txt` | generic scenario framework events | preserve generic entries and call a Fallout-owned event from the next-free scenario registry entry |
| `events/fallout_world_end_events.txt` | dedicated Fallout event chain | create with `add_namespace = chaosx.fallout` and place every Fallout event here |
| `interface/chaosx_super_events.gui` | existing presentation lifecycle reference | centered window with dynamic text, image, and close button |
| `common/scripted_guis/chaosx_scripted_gui_super_events.txt` | existing scripted GUI visibility and cleanup | uses a global visibility flag and clears audio on close |
| `common/country_tags/chaosx_countries.txt` | custom base tag pool | registers general Chaos tags and 34 Soviet Collapse successors |
| `common/scripted_effects/007_fury_effects.txt` | runtime country-package and focus precedent | applies flags, ideas, focus tree, template, units, and follow-up events |
| `common/national_focus/*.txt` | focus composition and current event tree ownership | must be audited before shared Fallout branches are added |
| `docs/systems/air_contamination_mechanic.md` | current Air documentation | contains stale recovery, treaty, event id, and super-event claims |
| `CHAOS_REDUX_MECHANICS.md` | root mechanics description | world-end section assumes chaos-above-1000 normal super-events |

## Existing patterns to reuse

### Host-owned periodic work

The Air system already updates from the host. Keep this authority model. The state phase scan belongs inside the existing monthly Air update or in a helper called by it. Do not add another independent monthly world-state loop.

### Shared population-loss pipeline

The Deaths system already calculates state population losses, records totals, feeds the death mapmode, and synchronizes Chaos. Winter and Fallout population losses should call that shared pipeline with new reason and scaling inputs.

### Scripted mapmodes

The two existing mapmodes establish the file family, dynamic color variables, state trigger pattern, background layer, daily update behavior, scripted localisation, and shared strip assets. Add the winter mapmode to this system.

### Runtime country package

The Fury package shows a bounded order for a transformed country:

1. set country and global flags
2. initialize variables
3. add starting ideas
4. load a focus tree
5. unlock equipment and templates
6. spawn dynamic starting units
7. schedule follow-up events

Fallout successor packages should use a generic version of that sequence.

### Cosmetic identity

The repository uses `set_cosmetic_tag` in many event systems. Cosmetic tags are the default identity mechanism for successors that do not need a unique base tag.

## Local references still required

Before implementation, open the local official documentation for:

- effects
- triggers
- modifiers
- script constants
- scripted GUI
- map modes
- state scope
- country creation
- focus trees
- dynamic and cosmetic tags
- nuclear strike effects
- province selection
- game rules around pausing and GUI input

Also inspect vanilla examples for:

- scripted state mapmodes
- full-screen independent GUI windows
- runtime focus-tree changes
- country release and state transfer cleanup
- nuclear and thermonuclear strike effects
- large scripted world rewrites

If vanilla and the offline wiki disagree, use vanilla behavior and record the difference.

## Likely edit order

1. Correct mapmode metadata and establish a verified third slot.
2. Add winter constants, variables, triggers, modifiers, and state-phase refresh helpers.
3. Extend the existing monthly Air scan to update states and aggregate global counts.
4. Add winter mapmode, tooltips, and selected-state response decisions.
5. Replace random winter pulses and wire real phase effects.
6. Restore and modernize treaty behavior.
7. Add the generic Fallout request coordinator.
8. Build the blackout GUI and scripted state machine.
9. Implement state grading and world cleanup helpers.
10. Scan and record the live scenario registry, allocate the next id after the current maximum, and prove exact province strike support.
11. Add the manual Fallout scenario only after that proof.
12. Implement the first successor batch and focus composition proof.
13. Expand by regional batches and run audits after each batch.

## Confirmed blockers

### Writable repository unavailable

This pass cannot patch or validate files in place.

### Local official documentation unavailable

The repository contains its offline wiki snapshot, but this environment does not expose the local Hearts of Iron IV documentation directory required by `AGENTS.md`.

### Exact province strike unproven

The offline reference confirms `every_state` and province selectors for some effects. It does not prove a direct global iteration that applies a nuclear strike to every valid province. The exact effect must be validated locally.

### Scenario id allocation

Raw id 8 is already assigned to Africa Is One in the inspected snapshot. Fallout must append to the live registry using the next integer after the highest assigned id. Existing scenario ids must not be moved.

### Mapmode strip conflict

The `.gfx` frame count and documentation disagree. The actual DDS dimensions and frame contents must be inspected.

## Ordinary risks

- duplicate focus ids from shared overlay composition
- stale old-world wars and guarantees after the rewrite
- tag reuse colliding with active feature packages
- country deletion or release while player scope is invalid
- multiplayer desynchronization during the world rewrite
- performance spikes from repeated world loops
- population loss being applied twice through country modifiers and state deaths
- category degradation becoming irreversible without stored original-state memory
- mapmode tooltip work evaluating too often
- save-load during the seven-day countdown or blackout

## Recommended next action

Open a writable local checkout at the inspected commit or a recorded successor commit. Complete Tranche 0 from `IMPLEMENTATION_TRANCHE_PLAN.md`. Do not begin the winter code until mapmode strip metadata is verified. Do not begin the manual Fallout scenario until exact province-strike behavior is proven and the next free live registry id is recorded.
