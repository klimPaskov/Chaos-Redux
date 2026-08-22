# Event 020 completion audit

Date: 2026-08-01

> Historical audit snapshot. The later 2026-08-01 content tranche and live wiring handoffs supersede its “missing” wording for the static RTA hierarchy consumers, RTX crisis events `.57-.59`, Crown Strike `.64-.65`, scoped defeat/aftermath `.71-.75`, resolver-owned `.72`, and slot-087 presentation surfaces. Retain this report for still-valid whole-spec, route-depth, `.73` audience, asset, scenario, and validation gaps; use `2026-08-01_event20_documentation_cleanup_handoff.md` for the reconciled disposition.

## Reconciliation update (2026-08-01)

The former absence findings for scoped defeat hooks, defeat metrics, resolver-owned reconstruction `.72`, and slot 087 presentation are superseded by the parent-owned tranche. Evidence is `common/on_actions/020_black_plague_on_actions.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_triggers/020_black_plague_rat_triggers.txt`, `common/script_constants/020_black_plague_constants.txt`, `interface/020_black_plague_super_events.gfx`, `localisation/english/020_black_plague_super_events_l_english.yml`, `sound/chaosx_sound.asset`, and `music/chaosx_music_track_list.html`, with final art/audio/text provenance in the 2026-08-01 slot-087 handoffs.

The audit remains partial: broader narrative and route depth, generic crisis/Doctor Wu/route art, `.73` audience ownership, workbook/catalog alignment, release attribution, and live consumer validation remain open. The later parent tranche resolved the Crown/Seal native mission API gap. No 3D model work is required by the current boundary.

## Audit boundary and verdict

Event 020 is **partial and not whole-spec complete**.

The current working tree contains a substantial playable core: the state disease lifecycle, the shared containment board, the mandatory black mapmode rendering, five evolution log records, exactly two rat country tags, the SCN-012 bootstrap, rat country shells, two focus trees, super-events, and the deterministic terminal takeover.

The current working tree also contains the newly added Diseases cluster and public Black Plague world-end registry row.

Those shared registry patches close the old runtime-registration gaps, but their workbook and historical-document surfaces are still stale.

The remaining completion blockers are not model production.

The user correction is controlling for this audit: `RTA` is the only reusable Rat Nation carrier, `RTX` is the separate Rat King, additional broods are internal RTA state, infestation, mass, and pulse state, and no 3D model production is required.

Older requirements for `RTB` through `RTM`, multiple independently tagged broods, or intensity-scaled rat tag counts are superseded by `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md`.

This auditor made no gameplay or asset changes; the only auditor-owned write is this handoff report.

## Completion status by surface

| Surface | Status | Evidence and disposition |
| --- | --- | --- |
| Accepted design source | Accepted but internally stale | The main specs and detailed matrices remain the accepted design source under `docs/specs/020_black_plague_specs/review/source_of_truth_and_plan_disposition.md`. The later two-tag correction supersedes several still-unedited multi-tag matrix and prompt rows. |
| Natural disease lifecycle | Finished for the declared core | `events/020_black_death.txt:16-24` dispatches the canonical hidden entry to `black_plague_start_natural_outbreak`. `common/scripted_effects/020_black_plague_effects.txt:1518-1548` selects and initializes the natural origin. The state loop, scheduler, spread, mortality, cure, relapse, weaponization, and response providers are present. |
| Shared disease category and crisis board | Finished for the current core | `common/decisions/categories/biowarfare_disease_containment_categories.txt:3-17` owns the single shared category and scripted GUI. Event 020 human actions remain inside that category. The current decision audit counted 31 shared response decisions. |
| Mandatory black mapmode | Finished for the current core | `common/map_modes/chaosx_state_map_modes.txt:116-218` renders tracked Black Plague borders and a pure black base for established states. `common/scripted_localisation/chaosx_scripted_localisation_map_modes.txt:52-272` provides phase, provenance, containment, infestation, and visibility text. |
| State-clipped black fog | Blocked design enhancement with incomplete proof | `docs/events/020_black_plague/overview.md:42` records that no verified safe clipping mechanism is used. The spec requires a reproducible tested-surface blocker artifact if the effect is omitted. No such test artifact was found. This does not invalidate the mandatory black mapmode. |
| Diseases event cluster | Implemented in the current working tree, catalog pending | `common/script_constants/event_cluster_constants.txt:22` assigns append-only ID 8. `common/scripted_effects/chaosx_event_cluster_effects.txt:144-152`, `:401-410`, and `:561-574` register a one-time cluster and Event 20 as its required Severe member. `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:10854-11243` and `localisation/english/chaosx_gui_l_english.yml:753,759` supply the live cluster UI. The workbook has no Diseases row. |
| Event history and event details | Finished for the mechanical core | Event 20 has the ordinary history mapping, a scenario history writer at `common/scripted_effects/020_black_plague_scenario_effects.txt:299-311`, dynamic Event Details text, five prefire previews, and world-end detail projection in the shared log system. |
| Five evolution log entries | Finished mechanically | `black_plague_evolution_record_stage` writes through `record_events_log_evolution_entry` at `common/scripted_effects/020_black_plague_evolution_effects.txt:74-88`. Activations call it for Evolutions I through V at lines 125, 141, 153, 165, and 333. The matching titles and bodies are in `localisation/english/020_black_plague_evolutions_l_english.yml:2-22`. |
| Narrative event chain | Missing beyond one scenario report | The live namespace defines only `chaosx.nr20.1`, `.4`, and hidden callbacks `.900` through `.903` in `events/020_black_death.txt`. The accepted chain in `docs/specs/020_black_plague_specs/matrices/event_chain_map.md:7-39` maps recognition, spread, containment, relapse, cure, deaths, eradication, five evolution resolutions, rat emergence, coronation, terminal, defeat, and aftermath events that do not exist. |
| Exactly two rat tags | Finished | `common/country_tags/020_black_plague_rat_countries.txt:8-11` registers only `RTA` and `RTX`. The current country audit found no mod, vanilla, or approved Workshop tag collision. |
| RTA and RTX coexistence lifecycle | Implemented in the current working tree, validation pending | `black_plague_rat_transfer_to_king` marks the RTA source `black_plague_rat_king_source_pending` at `common/scripted_effects/020_black_plague_rat_effects.txt:895-917` without setting its retired flag. Because `black_plague_rat_country_is_active` rejects only `black_plague_rat_country_retired` at `common/scripted_triggers/020_black_plague_rat_triggers.txt:9-13`, RTA remains active while the grace flag exists. No scenario or natural-path validation artifact proves that coexistence through expiry yet. |
| Post-grace Rat King absorption | Implemented in the current working tree, validation pending | `black_plague_rat_king_absorb_one_adjacent_brood` clears the grace flag, transfers at most one RTA state per pulse, and retires a pending RTA only after it has no controlled states at `common/scripted_effects/020_black_plague_rat_effects.txt:749-845`. The newly added fallback at lines 808-840 directly transfers one pending-source state to RTX when no adjacent internal state was selected, covering one-state and disconnected natural basins. No declared validation artifact proves full transfer and one-time retirement yet. |
| Internal RTA brood consolidation | Implemented in the current working tree, validation pending | The state-marker implementation at `common/scripted_effects/020_black_plague_rat_effects.txt:665-710` compares neighboring state-level brood strength, marks the weaker marker absorbed, inherits its unit budget, and adds brood mass to the sole RTA carrier. `black_plague_rat_state_is_valid_merger_state` at `common/scripted_triggers/020_black_plague_rat_triggers.txt:191-196` no longer performs the impossible same-country mass comparison. No seeded state-marker scenario has been evaluated. |
| Human counterplay against RTX | Implemented as a simplified partial | `black_plague_shared_strike_royal_node` at `common/decisions/020_black_plague_shared_response_decisions.txt:556-575` now supplies a targeted shared-category action with explicit material payment, a 120-day duration, cancellation, cooldown, generic emergency AI weight, and localisation. Its completion branch at `common/scripted_effects/020_black_plague_shared_response_effects.txt:300-306` only reduces state Rat Infestation by 20 and sets a marker flag. It does not lower RTX Dominion, suppress a royal pulse, or provide the accepted failure branch that strengthens world-end pressure. |
| Rat decisions and categories | Partial but recently improved | The current working tree registers each rat category once in `common/decisions/020_black_plague_rat_decisions.txt`. The no-op paid absorption action was removed, and Harden the Immune Blood was changed to a paid one-time strengthening action. Exact rat-meter costs and several operation outcomes remain weakly presented. |
| Native mission family | Not present; shared timed actions exist | No audited Event 020 decision file contains `days_mission_timeout`, `mission_timeout`, or `activate_mission`. Crown Strike and Seal Royal Burrows are now implemented as shared timed state actions with static success/timeout reports; the parent must decide whether native mission fields are still required by the accepted design. |
| SCN-012 registry and base bootstrap | Implemented for the corrected two-tag contract, validation pending | SCN-012 is registered as ID 12, has name and sort mappings, launches one RTA and one RTX, forces Evolutions I through IV, records one history row, refreshes the board and mapmode, and blocks repeat launch. It correctly keeps tag count at exactly one RTA and one RTX at every intensity. The current working tree also accepts an existing RTA carrier through `black_plague_scenario_has_usable_rat_slot` at `common/scripted_triggers/020_black_plague_scenario_triggers.txt:96-122`, consumes Event 20 fire-once state through `black_plague_scenario_suppress_fire_once` at `common/scripted_effects/020_black_plague_scenario_effects.txt:16-35,400`, preserves RTA through royal grace, and now has a non-adjacent post-grace transfer fallback. |
| Public world-end registry and toggle | Implemented in the current working tree | `common/script_constants/world_end_scenario_registry_constants.txt:30,78,101` maps scenario 10, owner event 20, and super-event 86. `common/scripted_effects/chaosx_events_log_effects.txt:1120-1131` registers a public, default-enabled row. `common/scripted_triggers/chaosx_world_end_scenario_triggers.txt:12-14` defines the independent toggle and `common/scripted_triggers/020_black_plague_evolution_triggers.txt:142-145` gates Evolution V on it. UI title, details, owner, and active-state selectors are present. |
| Terminal takeover and super-event | Finished mechanically | `common/scripted_effects/020_black_plague_evolution_effects.txt:288-335` performs the deterministic RTX takeover, marks the world-end flags, and exposes super-event 86. Super-event 85 and 86 sprites exist in `interface/020_black_plague_super_events.gfx`, final DDS files exist under `gfx/super_events/020_black_plague/`, and the sound wrappers are registered. |
| Achievements | Not implemented as a visible system | Fourteen completion triggers exist in `common/scripted_triggers/020_black_plague_achievement_triggers.txt:37-234`, and tracking helpers exist in `common/scripted_effects/020_black_plague_achievement_effects.txt`. There are no Event 20 entries in `common/achievements/chaos_redux_achievements.txt`, no Event 20 sprite triplets in `interface/chaosx_achievements.gfx`, no Event 20 achievement localisation, and no Event 20 files under `gfx/achievements/`. |
| RTA focus tree | Playable compact shell, accepted depth missing | The tree has 23 connected focuses. The current focus audit found no broken prerequisites or Event 20 custom icon reference after its narrow patch. The accepted mutation, territorial plague economy, military-method, hierarchy-choice, rival-absorption, and proto-sentience route families are missing or compressed to one-focus gates. |
| RTX focus tree | Playable compact shell, accepted depth missing | The tree has 38 connected focuses and three mutually exclusive government roots. Administration, plague mastery, captured knowledge, human population policy, continental campaign, and route-specific military tradeoffs are missing or compressed. The accepted target is approximately 70 to 100 focuses. |
| Focus AI | Missing | Neither Event 20 focus tree defines focus-level `ai_will_do`, and no Event 20 focus-factor or AI national-focus plan was found. The current rat AI strategy controls templates and fronts, not route selection or terminal-route preparation. |
| Rat country package | Partial | Country histories, dormant shell capitals, flags, static portraits, leaders, parties, ideas, locked templates, scripted forces, and rat-only AI templates exist. Natural Evolution III transfers one selected state to RTA at `common/scripted_effects/020_black_plague_rat_effects.txt:558-579`, below the accepted minimum connected basin of three states in `docs/specs/020_black_plague_specs/matrices/tuning_and_balance_targets.md:90-94`. Other missing accepted surfaces include the Fractured Instinct lifecycle spirit, advisors and high command, captured-knowledge and nest-industry progression, a stronger fictional Rat King identity, and the planned animated RTX portrait package. |
| Two-dimensional event and UI assets | Partial | Current Event 20 art includes static rat portraits, flags, focus and decision icons, one scenario report image, and three super-event images including final slot 087 art. The accepted outbreak, severe-crisis, overseas-jump, first-emergence, and Rat Nation news images are absent. The unique Doctor Wu report image, dedicated weapon-delivery icon, animated RTX portrait, achievement icon triplets, crisis-seal animation, and readiness animation are absent or explicitly queued. |
| 3D models | Out of scope and not a blocker | The user explicitly removed model production from the completion target. Existing infantry-entity consumers are not treated as an Event 20 completion defect in this audit. |
| Documentation and catalog | Partial and stale | The live overview has been partly updated for the shared registries, but the spec README, core readiness report, several matrices, follow-up notes, system docs, and the workbook still describe earlier states. |

## Highest-priority blockers

### 1. Royal Node counterplay stops at a deterministic infestation hit

The accepted design gives human countries a way to strike royal nodes to lower Dominion and pulse pressure, with failure strengthening the terminal route.

The current working tree now has the player action, payment, duration, target validation, cancellation, cooldown, generic AI weight, and text.

The resolution still only subtracts `constant:black_plague_shared_result.royal_node_damage` from state Rat Infestation and sets `black_plague_shared_royal_node_struck`.

A runtime scan found no behavioral consumer for that marker beyond persistence-owner reconciliation and cleanup.

The action does not change `RTX.black_plague_rat_king_dominion`, suppress or delay the royal pulse, branch on success or failure, or add failure pressure to the terminal route.

Its reach gate accepts ordinary local infrastructure or supply access rather than the accepted intelligence and military reach contract, and its decision uses the generic army-support icon rather than the dedicated Royal Node strike icon listed in the accepted asset inventory.

Recommended owner action: connect the result to Dominion and pulse pressure, implement an explicit success/failure contract and terminal-pressure consequence, tighten reach requirements, give the AI outcome-aware conditions, and replace the generic icon with the accepted dedicated asset.

### 2. The achievement layer is only a tracker scaffold and contains impossible conditions

The absence of registry entries, localisation, sprite definitions, and icon files means none of the fourteen accepted achievements is player-visible or unlockable through the project framework.

Three completion predicates need correction before registration.

- `black_plague_achievement_no_census_required_is_complete` requires `black_plague_achievement_rat_divisions_raised` at `common/scripted_triggers/020_black_plague_achievement_triggers.txt:150-162`, but a repository-wide runtime scan found no writer for that variable.
- `black_plague_achievement_one_crown_many_tails_is_complete` requires five absorbed Rat Nations at lines 165-175 and `constant:black_plague_achievement_threshold.rat_absorbed_nation_count = 5` at `common/script_constants/020_black_plague_achievement_constants.txt:23`. That design is superseded by the two-tag correction, and no writer for `black_plague_achievement_absorbed_rat_nations` exists.
- `black_plague_achievement_crown_one_continent_is_complete` requires Evolution V to be recorded while terminal takeover is not complete at lines 201-211. `black_plague_activate_evolution_v` records Evolution V and immediately calls the terminal takeover in the same effect chain at `common/scripted_effects/020_black_plague_evolution_effects.txt:326-335`, leaving no normal evaluation point that satisfies the trigger.

Recommended owner action: revise the three predicates against the accepted two-tag lifecycle, add explicit tracking writes, audit the other eleven positive and disqualifying paths, then register all approved achievements with final text and unique icon triplets.

### 3. The accepted narrative chain is almost entirely absent

Mechanical history and evolution details are not substitutes for the accepted player-facing event chain.

The live `.4` is the SCN-012 global report, while the accepted event chain reserves `.4` for the first neighboring threat alert and reserves planning ID `.90` for the scenario launch report.

The accepted event map is still broader than the compact runtime chain; however, `.45`, `.57-.59`, `.64-.65`, `.71-.75`, and resolver-owned eligible `.72` are now present as static event evidence. The remaining gaps are narrative depth, audience/picture correctness, and live proof rather than an entirely absent defeat aftermath.

The old `chaosx.news.21` at `events/_chaosx_news.txt:233-243` has no caller, uses `GFX_news_event_indian_famine`, and retains obsolete generic localisation in `localisation/english/020_black_death_l_english.yml:4-6`.

Recommended owner action: either preserve the accepted allocation by moving the scenario report to a collision-free `.90` identifier, or promote a revised allocation into the spec before implementation.

Then implement the recognition, major state transition, evolution resolution, rat emergence, coronation, defeat, eradication, and aftermath events with restrained repetition and matching report or news art.

### 4. Focus and country depth is substantially below the accepted package

The live RTA and RTX trees are connected and playable, but they contain 23 and 38 focuses against accepted ranges of roughly 40 to 50 and 70 to 100.

There is no route-aware focus AI.

The country package also lacks accepted Rat King identity depth, advisor roles, staged Fractured Instinct behavior, and captured-knowledge or nest-industry progression.

These are disclosed in the 2026-08-01 focus and country handoffs, so they are not hidden loader defects.

They remain accepted-plan omissions that prevent whole-spec completion.

## Accepted-plan disposition

| Accepted item | Current disposition |
| --- | --- |
| State disease lifecycle, shared board, black base mapmode, cure, relapse, mortality, weaponization, and Doctor Wu bridge | Implemented for the core tranche. |
| Five evolutions and Event Details evolution rows | Implemented mechanically. Player-facing evolution resolution events remain queued and unimplemented. |
| Exactly one RTA carrier and one RTX Rat King | Implemented at tag and package level. Grace-period coexistence, internal state-marker consolidation, and a non-adjacent post-grace absorption fallback are implemented in the current working tree; task-specific lifecycle validation remains missing. |
| Shared Diseases cluster | Implemented in the current working tree as ID 8 and a one-time required Severe Event 20 member. Workbook and older docs are not promoted. |
| Public Black Plague world-end row | Implemented in the current working tree with independent toggle gating. Workbook and older docs are not promoted. |
| SCN-012 with four intensities and no automatic Evolution V | Implemented in the shared scenario UI and bootstrap. Active-crisis RTA reuse, fire-once suppression, initial RTA/RTX grace coexistence, and post-grace transfer fallback are present in the current working tree. Focused launch and lifecycle validation remains unresolved. |
| Fourteen ordinary achievements | Tracking scaffold only. Visible registry, text, icons, and several attainable predicates are unresolved. |
| Deep RTA and RTX focus architecture | Compact playable subsets only. The 2026-08-01 focus audit records the missing route families and AI. |
| Narrative event map and aftermath | Partially promoted: `.45`, `.57-.59`, `.64-.65`, `.71-.75`, and resolver-owned eligible `.72` are statically present; broader player-facing chain depth and live proof remain deferred. |
| Defeat-aftermath super-event | Final gated package is wired statically: slot 087 art/text/audio ID 103, sprite, and settings wrappers are present; release attribution and live validation remain open. |
| Black fog | Optional engine-dependent enhancement. The omission is disclosed, but the required reproducible engine-surface test artifact is absent. |
| 3D rat models | Superseded for this task by the user's no-model instruction and not treated as a blocker. |

No new broad improvement-loop addendum is justified yet.

The accepted source-of-truth review says broad expansion should stop until the current accepted package is implemented, queued with a reason, superseded, or rejected.

## Stale and contradictory documentation

- `docs/specs/020_black_plague_specs/README.md:3,49` still says the Diseases cluster and public world-end row are missing and still includes 3D among completion gaps.
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md:5,52-72` is historical after the current registry patches, decision removal, two-tag correction, and user no-model instruction.
- `docs/specs/020_black_plague_specs/matrices/catalog_update_draft.md:19-44` still proposes cluster candidate ID 5, scenario candidate SCN-008, several independent Rat Nations, and intensity-scaled Rat Nation count. Live IDs are cluster 8 and SCN-012, and the tag-count rules are superseded.
- `docs/specs/020_black_plague_specs/matrices/triggerable_scenario_matrix.md:22-27,92-94` still contains superseded multi-tag intensity counts. Its active-RTA and active-RTX preservation requirement now matches the current grace-period sequencing.
- `docs/specs/020_black_plague_specs/matrices/event_chain_map.md:10,39` conflicts with the live use of `chaosx.nr20.4` for SCN-012 instead of `.90`.
- `docs/specs/020_black_plague_specs/matrices/achievement_matrix.md` still includes the five-rival One Crown, Many Tails condition that cannot exist under exactly two tags.
- `docs/plans/020_black_plague_plans/rat_absorption_follow_up.md` describes a paid absorption decision that the 2026-08-01 decision audit removed. It should be superseded by the current automatic state-marker consolidation and post-grace transfer implementation.
- `docs/systems/air_cleanliness/air_contamination_mechanic.md` still says SCN-012 has no live public row according to the current localisation handoff.
- `docs/systems/event_system/event_clusters.md:62-63` repeats the Diseases unlock-tier line after the current patch.

The four current 2026-08-01 subagent patches each have a handoff note under `docs/plans/020_black_plague_plans/subagent_handoffs/`.

No unrecorded Event 20 subagent patch was found in the current task surface.

Historical 2026-07-24 fail-closed scenario handoffs are explicitly superseded by the live bootstrap and later readiness report.

## Workbook and export audit

The editable source workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` was opened read-only with formula preservation.

The Event 20 row currently has:

- `Type = Minor Fire-Once`
- `Status = Needs Testing`
- `World-End Scenario = blank`
- `Cluster ID = blank`
- `Member Severity = blank`

The Clusters sheet has IDs 1 through 7 but no Diseases row or ID 8.

The Scenarios sheet contains `SCN-012` with corrected RTA and RTX wording and `Status = Needs Testing`.

The exported Events, Clusters, and Scenarios CSV files are dated 2026-07-29 and do not include the new Diseases registration.

Recommended owner action: update the workbook Events and Clusters rows after final in-game wording is accepted, preserve the SCN-012 row, then run `python .tools/export_event_catalog_csv.py` from the mod root.

The CSVs must not be edited directly.

## Asset and presentation gaps

Current final visual coverage includes:

- one scenario report image, `gfx/event_pictures/020_black_plague/report_event_020_black_plague_unbound.dds`
- three super-event images, including `super_event_085_rat_king_coronation.dds`, `super_event_086_rat_king_takeover.dds`, and `super_event_087_rat_king_defeat_aftermath.dds`
- five static rat portraits
- RTA and RTX flag triplets
- registered rat focus, idea, response-decision, and weaponization sprites

Missing accepted visual surfaces include:

- `report_event_020_black_plague_origin`
- `report_event_020_black_plague_severe`
- `news_event_020_black_plague_overseas`
- `report_event_020_rat_emergence`
- `news_event_020_rat_nations`
- a unique Doctor Wu report image
- a dedicated weapon-delivery icon, because `interface/020_black_plague_weaponization.gfx:6` reuses military-acceleration art
- a dedicated Royal Node Strike decision icon, because `common/decisions/020_black_plague_shared_response_decisions.txt:559` uses `GFX_decision_generic_army_support`
- fourteen achievement icon triplets
- the planned animated RTX portrait with static fallback
- the planned source-frame crisis-seal and world-end-readiness animation packages

The three weaponization report events at `events/020_black_plague_weaponization.txt:16,27,38` all reuse the single SCN-012 report image.

That is a disclosed presentation simplification, not final whole-spec asset coverage.

No model, mesh, skeletal animation, or 3D production gap is included in this audit.

## Meaningful validation performed

- Confirmed the country-tag registry contains exactly RTA and RTX and no legacy rat tag is registered.
- Compared the live event namespace against every planned identifier in `matrices/event_chain_map.md`.
- Confirmed all five evolution activations call the shared evolution-log writer and resolve to Event Details localisation.
- Checked the current Diseases cluster ID, type, member role, severity, name, description, and Event 20 projection across constants, effects, scripted localisation, and English GUI localisation.
- Checked the current world-end scenario ID, owner, super-event, public row, active flag, title, details, and independent disabled-scenario gate across the registry and Evolution V trigger.
- Read the workbook source and all three exported catalogs without writing them.
- Ran a repository-wide identifier-frequency scan for Event 20 achievement state and found no writers for the absorbed-nations or rat-divisions-raised variables.
- Compared the ordering of Evolution V recording and terminal takeover against the Crown One Continent trigger.
- Confirmed the current Royal Node Strike decision has payment, duration, target, cancellation, cooldown, generic AI, and localisation, then traced its outcome and found only a state-infestation reduction with no Dominion, royal-pulse, failure, or terminal-pressure interaction.
- Confirmed the current SCN-012 patch accepts an existing RTA slot and performs shared fire-once bookkeeping before bootstrap.
- Confirmed the current Evolution IV transfer leaves RTA active during the grace period by using a pending-source flag instead of the retired-country flag.
- Traced internal brood and post-grace transfer scope selection, reported the same-country mass comparison and one-state/disconnected-basin dead ends, and confirmed both were subsequently removed in the current working tree.
- Reviewed the 2026-08-01 decision, localisation, focus, and country audit handoffs and their recorded validation artifacts.
- Scanned Event 20 final GFX consumers and asset paths for the present report, super-event, portrait, flag, focus, idea, and decision packages.

## Meaningful validation still missing

- No focused current-tree event inspection artifact covers the new Diseases and world-end registry changes after they were patched.
- No declared scenario validation proves all four SCN-012 intensities, existing-crisis top-up, cleanup, repeat-launch blocking, ordinary fire-once suppression, RTA and RTX coexistence through grace expiry, or complete post-grace absorption after the current patch.
- No terminal validation proves the public toggle prevents Evolution V while disabled and permits it when enabled under otherwise identical conditions.
- No positive and disqualifying validation exists for the fourteen achievement families, and three predicates are statically unattainable as written.
- No Royal Node Strike validation covers valid and invalid reach, successful Dominion and pulse reduction, failure pressure, cancellation, repeat use, or AI prioritisation; several of those accepted outcome surfaces are not implemented.
- No route-aware focus AI validation is possible because focus AI is missing.
- No balance evidence was found for full outbreak pacing, four scenario intensity profiles, RTA to RTX absorption cadence, human anti-RTX counterplay, or terminal-route preparation under representative scenarios.
- The prior HOI4 event inspection in the 2026-07-29 readiness report was workspace-partial and predates the current shared-registry patches.

No Hearts of Iron IV process was launched.

## Recommended implementation order

1. Complete Strike Royal Node by connecting it to Dominion, royal pulse pressure, failure pressure, meaningful reach, and a dedicated icon.
2. Correct the three impossible achievement predicates, then implement the root registry, final text, sprite triplets, and icon files for the approved set.
3. Implement or explicitly re-disposition the accepted narrative event chain and resolve the `.4` versus `.90` allocation.
4. Expand the RTA and RTX route families and add route-aware focus AI before claiming focus-tree completion.
5. Update the authoritative workbook and export the three CSV snapshots.
6. Reconcile the README, overview, readiness report, matrices, system docs, asset manifests, and obsolete follow-up notes with the current two-tag and shared-registry state.
7. Run focused rat-lifecycle, scenario, terminal-toggle, event-chain, defeat-gate, slot-087 playback, achievement, and balance validations after those mechanics exist.

## Completion claim boundary

The core disease runtime can be described as implemented and ready for targeted validation.

Event 20 as defined by the accepted full spec pack cannot be described as complete.

The remaining work is a mix of freshly patched but unvalidated lifecycle behavior, accepted but missing player mechanics, accepted content depth, missing achievement and narrative presentation, stale source documentation, and an unupdated workbook.
