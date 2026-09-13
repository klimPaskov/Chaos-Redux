# Event 016 native prototype exclusivity audit

Date: 2026-09-08

Status: read-only source audit complete; no gameplay, GUI, localisation, or balance files were changed.

Scope: inventory the fifteen Kruger Prototype family fallback rows in `common/decisions/016_brilliant_scientist_directorate_project_board.txt`, compare them with their native special-project presentation gates, and trace the private Computation presentation and receipt lifecycle without inferring an undocumented universal DLC restriction.

## Executive findings

- The board contains fifteen native integration rows, not fourteen: ten custom family rows, four conventional electronics/rocketry/high-energy/biological rows, and one Singularity family row at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:928`.
- The Singularity row has no single native root project ID; it is a family-level integration row gated by theory stage `^14 = theory` and `brilliant_scientist_singularity_component_count > zero`, after the six component projects have been completed.
- Every native board row explicitly requires `has_dlc = "Gotterdammerung"` in its visible block, while every one of the fifteen family fallback rows explicitly requires `NOT = { has_dlc = "Gotterdammerung" }`.
- The fifteen fallback rows are source-connected and are not dead placeholders: each has a research-entry path, an exact active-receipt continuation path, a paid begin effect, a cancellation path, and a finish/refund-or-output path.
- The native project definitions themselves do not establish a universal Gotterdammerung restriction. The four conventional project definitions and all ten custom family definitions either omit `allowed` or use `allowed = { }`; the explicit DLC split is in the Event 016 board wrappers, with an additional explicit DLC predicate in the private Computation presentation helper.
- Source review cannot prove whether the game engine will render a native project panel without Gotterdammerung when the board wrapper is bypassed. That is an engine-presentation question, not evidence that the board fallback rows are dead.

## Fifteen-row source inventory

The shorthand `NATIVE` below means the board row requires current-host ownership, Gotterdammerung, the matching theory stage, and the exact native completion predicate, then starts `brilliant_scientist_begin_native_prototype_integration` and finishes through the native integration callbacks.

The shorthand `FALLBACK` means the no-DLC row requires current-host ownership, `NOT = { has_dlc = "Gotterdammerung" }`, terminal-lock exclusions, and either the family research helper or an exact active receipt continuation; its available block requires board readiness, the family research helper, and the family can-pay helper.

| Family | Native project ID(s) and specialization | Native source predicates | Event 016 native board row | No-DLC fallback row and receipt consumer |
|---|---|---|---|---|
| Computation | `sp_brilliant_scientist_computational_engine`, `specialization_land` (`common/special_projects/projects/016_brilliant_scientist_projects.txt:76-80`) | `allowed = { }`; visible/available are `brilliant_scientist_can_research_computation_prototype` | `brilliant_scientist_integrate_computation_prototype` at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:488-506`; theory index `^0`; native completion exact ID | `brilliant_scientist_research_computation_prototype_no_dlc` at `:5028-5075`; begin/cancel/finish canonical project-stage effects; active receipt continuation is in the root visible OR block |
| Electronics | `sp_air_radar`, `specialization_air` (`C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/special_projects/projects/radar_projects.txt:1-18`) | No `allowed` or `visible` gate; available requires `has_tech = electronic_mechanical_engineering` | `brilliant_scientist_integrate_electronics_prototype` at `:3508-3526`; theory index `^1`; `is_special_project_completed = sp:sp_air_radar` | `brilliant_scientist_research_electronics_prototype_no_dlc` at `:5077-5124`; canonical receipt begin/cancel/finish |
| Materials | `sp_brilliant_scientist_advanced_materials`, `specialization_land` (`016_brilliant_scientist_projects.txt:153-157`) | `allowed = { }`; visible/available are the host or private Mengele materials research helper | `brilliant_scientist_integrate_materials_prototype` at `:532-550`; theory index `^2`; exact custom native completion | `brilliant_scientist_research_materials_prototype_no_dlc` at `:5126-5173`; canonical receipt begin/cancel/finish |
| Rocketry | `sp_rockets_flying_bomb` (`rocket_projects.txt:10-56`) or `sp_air_jet_engine` (`air_projects.txt:793-819`), both `specialization_air` | Flying Bomb available requires `experimental_rockets`; Air Jet Engine has the vanilla `By Blood Alone` branch and airframe/engine requirements; neither definition has an Event 016 Gotter gate | `brilliant_scientist_integrate_rocketry_prototype` at `:3552-3570`; theory index `^3`; OR exact native completion IDs | `brilliant_scientist_research_rocketry_prototype_no_dlc` at `:5175-5222`; canonical receipt begin/cancel/finish |
| High Energy | `sp_nuclear_reactor`, `specialization_nuclear` (`nuclear_projects.txt:1-13`) | `allowed = { }`; available requires `has_tech = atomic_research` | `brilliant_scientist_integrate_high_energy_prototype` at `:3596-3614`; theory index `^4`; exact native completion | `brilliant_scientist_research_high_energy_prototype_no_dlc` at `:5224-5271`; canonical receipt begin/cancel/finish |
| Biomedical | `sp_brilliant_scientist_biomedical_acceleration`, `specialization_biowarfare` (`016_brilliant_scientist_projects.txt:223-227`) | `allowed = { }`; visible/available are the host or private Mengele biomedical research helper | `brilliant_scientist_integrate_biomedical_prototype` at `:576-594`; theory index `^5`; exact custom native completion | `brilliant_scientist_research_biomedical_prototype_no_dlc` at `:5273-5320`; canonical receipt begin/cancel/finish |
| Teleportation | `sp_brilliant_scientist_quantum_transit`, `specialization_nuclear` (`016_brilliant_scientist_projects.txt:293-297`) | `allowed = { }`; visible/available are the host or private Mengele teleportation research helper | `brilliant_scientist_integrate_teleportation_prototype` at `:620-638`; theory index `^6`; exact custom native completion | `brilliant_scientist_research_teleportation_prototype_no_dlc` at `:5322-5369`; canonical receipt begin/cancel/finish |
| Cloning | `sp_brilliant_scientist_cloning`, `specialization_biowarfare` (`016_brilliant_scientist_projects.txt:363-367`) | `allowed = { }`; visible/available are the host cloning helper | `brilliant_scientist_integrate_cloning_prototype` at `:664-682`; theory index `^7`; exact custom native completion | `brilliant_scientist_research_cloning_prototype_no_dlc` at `:5371-5418`; canonical receipt begin/cancel/finish |
| Robotics | `sp_brilliant_scientist_autonomous_cognition`, `specialization_land` (`016_brilliant_scientist_projects.txt:432-436`) | `allowed = { }`; visible/available are the host or private Mengele robotics research helper | `brilliant_scientist_integrate_robotics_prototype` at `:708-726`; theory index `^8`; exact custom native completion | `brilliant_scientist_research_robotics_prototype_no_dlc` at `:5420-5467`; canonical receipt begin/cancel/finish |
| Paleogenetics | `sp_brilliant_scientist_paleogenetics`, `specialization_biowarfare` (`016_brilliant_scientist_projects.txt:502-506`) | `allowed = { }`; visible/available are the host or private Mengele paleogenetics research helper | `brilliant_scientist_integrate_paleogenetics_prototype` at `:752-770`; theory index `^9`; exact custom native completion | `brilliant_scientist_research_paleogenetics_prototype_no_dlc` at `:5469-5516`; canonical receipt begin/cancel/finish |
| Xenobiological Synthesis | `sp_brilliant_scientist_xenobiological_synthesis`, `specialization_biowarfare` (`016_brilliant_scientist_projects.txt:572-576`) | `allowed = { }`; visible/available are the host or private Mengele xenobiological helper, including the xeno-control lock | `brilliant_scientist_integrate_xenobiological_synthesis_prototype` at `:796-814`; theory index `^10`; exact custom native completion | `brilliant_scientist_research_xenobiological_synthesis_prototype_no_dlc` at `:5518-5565`; canonical receipt begin/cancel/finish |
| Biological Weapons | `anthrax_bomb`, `tularemia_bomb`, or `plague_bomb`, all `specialization_biowarfare` (`common/special_projects/projects/biowarfare_main_projects.txt:432-437`, `671-676`, `909-914`) | Each definition has empty allowed/visible blocks; the research helper supplies the required biological technologies | `brilliant_scientist_integrate_biological_weapons_prototype` at `:3640-3658`; theory index `^11`; OR exact native completion IDs | `brilliant_scientist_research_biological_weapons_prototype_no_dlc` at `:5567-5614`; canonical receipt begin/cancel/finish |
| Alien Arms | `sp_brilliant_scientist_alien_arms`, `specialization_nuclear` (`016_brilliant_scientist_projects.txt:642-646`) | `allowed = { }`; visible/available are the host or private Mengele alien-arms research helper | `brilliant_scientist_integrate_alien_arms_prototype` at `:840-858`; theory index `^12`; exact custom native completion | `brilliant_scientist_research_alien_arms_prototype_no_dlc` at `:5616-5663`; canonical receipt begin/cancel/finish |
| Temporal Mechanics | `sp_brilliant_scientist_temporal_mechanics`, `specialization_nuclear` (`016_brilliant_scientist_projects.txt:712-716`) | `allowed = { }`; visible/available are the host or private Mengele temporal research helper | `brilliant_scientist_integrate_temporal_prototype` at `:884-902`; theory index `^13`; exact custom native completion | `brilliant_scientist_research_temporal_prototype_no_dlc` at `:5665-5712`; canonical receipt begin/cancel/finish |
| Singularity | Six component projects: `sp_brilliant_scientist_singularity_command_core` (`specialization_air`), `...power_link` (`specialization_nuclear`), `...containment_lattice` (`specialization_land`), `...temporal_authenticator` (`specialization_nuclear`), `...delivery_architecture` (`specialization_air`), and `...fail_deadly_governor` (`specialization_nuclear`) at `016_brilliant_scientist_projects.txt:782-1136` | Each component has `allowed = { }` and visible/available `brilliant_scientist_can_research_singularity_component`; there is no single `sp_*singularity` root | `brilliant_scientist_integrate_singularity_prototype` at `:928-946`; current host + Gotter + theory index `^14` + `brilliant_scientist_singularity_component_count > zero`; available remains board-ready + prototype capacity | `brilliant_scientist_research_singularity_prototype_no_dlc` at `:5714-5761`; canonical family receipt begin/cancel/finish. Six separate component fallback rows at `:5765-6016` use the component receipt adapter and must remain available for component progress |

## Native facility and specialization gates

The custom project definitions map to the vanilla or mod facility specializations rather than to a universal DLC predicate.

- `specialization_land` maps to `land_facility` in vanilla `common/buildings/00_buildings.txt:556-576`.
- `specialization_air` maps to `air_facility` in vanilla `common/buildings/00_buildings.txt:533-553`.
- `specialization_nuclear` maps to `nuclear_facility` in vanilla `common/buildings/00_buildings.txt:500-530`.
- `specialization_biowarfare` maps to the mod `biowarfare_facility` in `common/buildings/chaosx_buildings.txt:37-71`.
- The Event 016 research helpers require a valid `brilliant_scientist_primary_facility` target owned by the current host through `brilliant_scientist_primary_facility_is_valid` in `common/scripted_triggers/016_brilliant_scientist_triggers.txt:342-350`.
- The Singularity helper additionally requires `brilliant_scientist_has_required_singularity_facilities` in `common/scripted_triggers/016_brilliant_scientist_project_triggers.txt:212-226`, the enabled-scenario trigger, and all six completed component flags before the family prototype route becomes eligible.
- The ordinary family research helpers and the native board rows add family-specific theory, technology, incident, capacity, host, and route-lock predicates; these are not equivalent to a source-level DLC requirement.

## Fallback entry, continuation, cancellation, and settlement

All fifteen family roots use the same lifecycle shape, with family-specific IDs and resource helpers.

- Entry rows are the fifteen roots at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:5028-5761`; their visible OR block accepts the family research helper or a matching active receipt identified by `brilliant_scientist_project_stage_in_progress`, `brilliant_scientist_active_project_family`, and `brilliant_scientist_active_project_stage`.
- Each available block requires `brilliant_scientist_project_board_is_ready = yes`, the family research helper, and the family can-pay trigger, then reserves the family-specific PP/support-equipment/fuel/civilian-factory commitment and duration.
- Each completion sets `brilliant_scientist_project_family` and `brilliant_scientist_requested_project_stage = prototype`, then calls `brilliant_scientist_begin_project_stage = yes`.
- Each family root has `cancel_if_not_visible = yes`, an invalid-context cancel trigger, `brilliant_scientist_cancel_project_stage = yes`, and a remove callback to `brilliant_scientist_finish_project_stage = yes`.
- The canonical host receipt begins in `common/scripted_effects/016_brilliant_scientist_project_effects.txt:10-66`, stores active family/stage/capacity state, and subtracts the committed costs.
- Host cancellation is finalized in `:79-88`; the source does not advertise a separate direct-cost refund there, so the active paid receipt must not be retired as a redundant future entry while it is still visible through the continuation branch.
- Host settlement is completed in `:112-143`; it advances the stage ledger, applies output/incident handling, finalizes the active receipt, and clears the active capacity delta.
- The six Singularity component fallback rows use the separate component receipt adapter at `common/decisions/016_brilliant_scientist_directorate_project_board.txt:5765-6016` and `brilliant_scientist_begin_singularity_component_fallback`, `...cancel_singularity_component_fallback`, and `...finish_singularity_component_fallback`; these are component progress entries, not duplicate family Prototype rows.

## Private Computation presentation and receipt route

The private Computation path is source-connected but has an explicit presentation DLC predicate that should be reviewed against the intended product behavior.

- `brilliant_scientist_mengele_computation_native_prototype_presentation_available` in `common/scripted_triggers/016_mengele_computation_decision_triggers.txt:32-40` requires `has_dlc = "Gotterdammerung"`, the private research helper, and `NOT = { is_special_project_completed = sp:sp_brilliant_scientist_computational_engine }`.
- The same file comments at `:9-13` identify this as the native-presentation test; completed native projects are deliberately excluded so the parent bridge can synchronize the callback.
- `brilliant_scientist_mengele_computation_prototype_decision_visible` at `:52-59` requires the strict private provider, an empty private receipt, Theory completion, no Prototype completion, no native computational completion, and the negation of the native-presentation helper.
- The private decision `mengele_event016_computation_prototype` is at `common/decisions/016_mengele_computation_stage_decisions.txt:107-180`; it has the family can-pay gate, completion call, explicit `cancel_if_not_visible = no`, cancellation callback, and settlement callback.
- Private begin/cancel/finish effects are in `common/scripted_effects/016_mengele_project_stage_effects.txt:694-764`; begin writes active array entries and debits PP/support equipment/fuel, while the decision `modifier = { civilian_factory_use = ... }` owns the civilian-factory commitment, cancel snapshots and refunds direct costs, and finish applies output or refunds the snapshot if output cannot be authorized.
- Native private synchronization is in `:1303-1430`; it authenticates exact native completion, adopts a completed native result after Theory when appropriate, and records the six Singularity component completions through the component adapter instead of replaying an output.
- The underlying custom native project definition at `common/special_projects/projects/016_brilliant_scientist_projects.txt:76-80` has `allowed = { }` and visible/available helper predicates without a direct DLC line. Therefore the source proves an explicit private presentation lock, but does not prove the engine would or would not display the custom project panel without Gotterdammerung.

## Issues and recommendations

### Severity: medium review point

Review whether the explicit `has_dlc = "Gotterdammerung"` in `brilliant_scientist_mengele_computation_native_prototype_presentation_available` is intended to mirror the board’s native presentation policy or is an accidental overrestriction. The underlying custom project definition does not independently carry that DLC condition, so this should be decided from the accepted design and, if needed, a live engine presentation check rather than inferred from source.

### Severity: low documentation point

Keep the distinction between “native project source definition has no DLC gate” and “Event 016 board chooses native presentation only with Gotterdammerung” explicit in future changes. The four conventional native IDs are `sp_air_radar`, `sp_rockets_flying_bomb`/`sp_air_jet_engine`, `sp_nuclear_reactor`, and the three biowarfare bomb alternatives; none has a universal Event 016 DLC predicate in its installed definition.

### No missing fallback route found

No family row was found that lacks an entry route, exact active-receipt continuation, cancellation consumer, or settlement consumer. The six Singularity component fallback rows are separate and must be preserved because they feed the component count used by the family-level Singularity integration row.

## Required GUI evidence and limits

The mandatory read-only GUI inspection was run for `interface/016_brilliant_scientist_directorate.gui`, window `kruger_directorate_container`, scenario `default`; it is evidence for the shared directorate container, not proof of special-project engine presentation.

- `hoi4.gui_inspect` returned `GUI_INSPECTED` with parsed graph artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/30aa955f6f0f066325f17205485493b5f12c7af0c80599fa7915ddedbb3c1721/8e57f0b2021b120a150dfb4f7ced5a40c66ae836ba721528964186aa886e1f0e/gui-inspect.7ab09de0a80b7a7e.json`.
- The inspect diagnostics report a 100% conflicting click-region overlap between `kruger_directorate_open_button` and `kruger_directorate_close_button` at source lines 36 and 65 in the offline default scenario, plus nonblocking compact/full-panel overlap and z-order risks.
- `hoi4.gui_render` returned `GUI_RENDERED` with five variants, three requested states, one 1920x1080 resolution, `offlineRepresentation = true`, and zero changed pixels for the requested comparison. Full and cropped artifact URIs are in the MCP result; no GUI rewrite or GUI source edit was authorized for this audit.
- The offline render includes renderer limitations for stateful button code and does not establish how a native special-project panel behaves under DLC ownership. A future UI task should own any container overlap repair and run the required matching before/after GUI evidence.

## Validation and disposition

- Read-only source checks covered the exact board rows, custom project definitions, installed vanilla project definitions, building specializations, family research triggers, fallback decision blocks, and host/private receipt effects listed above.
- Offline Paradox wiki pages and installed vanilla special-project, project, and specialization documentation were consulted for `allowed`, `visible`, `available`, specialization, and facility semantics.
- This bounded source inventory did not obtain weighted evidence; the parent-owned `/root/mengele_conventional_probability` audit remains pending.
- No gameplay patch, GUI patch, localisation change, or commit was made.
- Disposition: retain all paid fallback paths pending an accepted design choice; this source inventory proves the Event 016 wrapper DLC split, not native special-project panel visibility without Gotterdammerung. The private Computation DLC predicate remains an unresolved review point, and no source-only engine-presentation claim is made.
