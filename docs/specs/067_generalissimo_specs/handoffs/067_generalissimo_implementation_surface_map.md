# Event 067 Implementation Surface Map

## Purpose

This handoff maps the likely implementation surfaces without replacing repository inspection. Exact paths and identifiers must follow current repository ownership and MCP findings.

## Event and lifecycle

Likely owner files:

- `events/067_generalissimo.txt`
- `common/script_constants/067_generalissimo_constants.txt`
- `common/scripted_triggers/067_generalissimo_triggers.txt`
- `common/scripted_effects/067_generalissimo_effects.txt`
- `common/on_actions/067_generalissimo_on_actions.txt`

Responsibilities:

- target validation and weighting
- canonical character creation
- command package
- service record
- Influence
- evolution pacing and logging
- demands
- removal
- civil-war setup
- resolution
- world-end readiness and actor processing

## Character and traits

Likely surfaces:

- `common/characters/067_generalissimo_characters.txt`
- `common/country_leader/067_generalissimo_traits.txt` or current repository trait location
- commander trait references after installed-file inspection
- portrait-specific GFX

Responsibilities:

- one canonical character token
- male metadata
- commander and field marshal package
- country-leader role
- four ruler traits
- Event 065 family marker
- transfer and cleanup

## Decisions and missions

Likely surfaces:

- `common/decisions/categories/067_generalissimo_categories.txt`
- `common/decisions/067_generalissimo_decisions.txt`
- Event 067 scripted effects and triggers
- Event 067 localisation

Responsibilities:

- crisis category
- command authority
- concessions
- counterweights
- missions
- removal actions
- postwar integration
- junta force growth
- world-end military and civilian actions

## Country package

Likely surfaces:

- Event 067 scripted effects and triggers
- `common/ideas/067_generalissimo_ideas.txt`
- `common/opinion_modifiers/067_generalissimo_opinion_modifiers.txt`
- optional event-owned dynamic modifiers
- optional AI strategy files

Responsibilities:

- dynamic civil-war country markers
- army, navy, air, stockpile, commander, and territory split
- capitals
- ideology and ruling party
- starting ideas
- Command Cohesion
- subjects and faction settlement
- victory and defeat cleanup

## Focus tree

Likely surfaces:

- `common/national_focus/067_generalissimo_focus.txt`
- current focus-tree selection and loading path
- `common/focus_inlay_windows/067_generalissimo_inlay.txt`
- Event 067 decisions and effects
- Event 067 localisation

Responsibilities:

- host-adaptive full tree
- route locks
- conditional navy and air branches
- postwar integration
- world-end extension
- search filters
- Focus Navigation
- route AI
- inlay attachment

Mandatory MCP:

- `hoi4.focus_inspect`
- `hoi4.focus_render`
- `hoi4.focus_rewrite` when layout changes are needed
- post-change comparison

## Event-owned GUI and GFX

Likely surfaces:

- `interface/067_generalissimo.gui`
- `interface/067_generalissimo.gfx`
- `common/scripted_guis/067_generalissimo_scripted_guis.txt`
- Event 067 scripted localisation

Responsibilities:

- compact crisis attached display
- Influence meter
- focus inlay layout
- Command Cohesion meter
- regime emblems
- visibility and click transparency

Mandatory event UI worker evidence:

- `hoi4.gui_inspect`
- pre-change `hoi4.gui_render`
- bounded `hoi4.gui_rewrite`
- post-change inspect and render comparison
- relevant states and resolutions

## Event Logs and Event Details

Shared surfaces to inspect and patch narrowly:

- `common/scripted_effects/chaosx_events_log_effects.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`
- `interface/chaosx_events_log_popup.gui` only if row layout needs a verified change
- event name and detail localisation files

Responsibilities:

- Event 067 history actor
- three evolution records
- event catalog row
- public world-end row and toggle
- unavailable `N/A` state
- cluster member status

The shared UI is not owned by `chaosx_event_ui_worker`.

## Event system registration

Likely shared surfaces:

- current event-category initialization
- event type lookup
- default-enabled event allowlist
- event name mappings
- automatic fire routing

Responsibilities:

- Minor Fire-Once registration
- Chaos level 1
- target validity before selection
- one-time weight behavior
- disabled-by-default state until rework completion

## Triggerable scenario

Shared surfaces to inspect:

- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
- `common/scripted_guis/chaosx_scripted_gui_settings.txt`
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
- scenario and GUI localisation
- triggerable scenario documentation

Responsibilities:

- `SCN-015`
- four types
- four intensities
- target resolution
- confirmation
- one-time launch
- bypass cleanup

The shared scenario window is not owned by `chaosx_event_ui_worker`.

## Cluster

Shared surfaces to inspect:

- current cluster registry
- cluster constants
- cluster member weighting and logging
- authoritative workbook

Responsibilities:

- Military Preparation identity
- Event 067 High member registration
- valid-target skip reason
- one pacing transaction

## World-end

Shared surfaces to inspect:

- public world-end registry
- Event Details world-end rows
- world-end enable state
- super-event visibility
- event-system freeze

Responsibilities:

- public `generalissimos_world` branch
- Chaos 1000 gate
- active Generalissimo readiness
- independent toggle
- world-end flag
- bounded actor roster
- International Command
- rival military blocs
- Civil Authority Compact

## Assets

Temporary workspace:

- `docs/assets/067_generalissimo/`

Runtime categories:

- portrait
- event pictures
- news pictures
- decision category pictures
- decisions and missions
- ideas
- leader traits
- focus icons
- flags
- faction emblems
- focus inlay assets
- achievement triplets
- super-event images
- super-event WAV files

No 3D, unit counter, or unit sound surface is required.

## Super-events

Likely shared surfaces:

- super-event image GFX
- scripted localisation getters
- super-event visibility logic
- `sound/chaosx_sound.asset`
- `music/chaosx_music_track_list.html`
- event-owned sound folder
- super-event documentation

Responsibilities:

- ruler super-event
- world-end super-event
- unique images
- unique audio
- sourced quotes and remarks
- settings-aware playback

## AI and probability

Likely surfaces:

- event `ai_chance`
- decision `ai_will_do`
- focus AI weights
- random lists
- target selection
- world-end country outcomes
- faction and bloc membership

Mandatory audit:

- every scenario in `067_generalissimo_probability_scenario_matrix.md`
- baseline inspect
- owner patch
- mandatory compare

## Localisation

Likely event-owned files:

- event text
- decisions and missions
- focus tree
- GUI
- traits and ideas
- achievements
- scenario text
- news text

Shared mapping files may need narrow additions.

All final text must follow the direction in the spec and match workbook wording.

## Documentation and workbook

Permanent docs should cover:

- event overview
- Influence and removal
- junta country package
- focus tree
- manual scenario
- world-end branch
- assets and super-events
- probability and acceptance evidence

Workbook update belongs to `chaosx_spreadsheet_doc_worker`. CSV exports are regenerated only after the workbook saves successfully.
