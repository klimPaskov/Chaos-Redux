# Event 006 RHI/BAY Gameplay Handoff — 2026-07-15

> Superseded for route publication, government identifiers, AI route coupling, and readiness mapping by `006_nwe_route_matrix_remediation_2026_07_15.md`. The original implementation record below is retained for provenance and must not be used as the current route matrix.

## Status

Bounded package-owned gameplay for `IW-008` Rhineland (`RHI`) and `IW-009` Bavaria (`BAY`) is implemented in new files and ready for parent review and integration.

**This handoff does not claim allocator readiness.** The parent-owned runtime dispatcher and preflight registry do not yet call or admit these packages, and the shared selected-family formable registry still lacks the family-specific `FORM04` commit consumer. No readiness, content-readiness, or dormant-history package flag was set.

No Git commit was created.

## Files created

- `common/script_constants/006_independence_wave_rhineland_bavaria_constants.txt`
- `common/ideas/006_independence_wave_rhineland_bavaria_ideas.txt`
- `common/scripted_triggers/006_independence_wave_rhineland_bavaria_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_rhineland_bavaria_package_effects.txt`
- `common/decisions/categories/006_independence_wave_rhineland_bavaria_categories.txt`
- `common/decisions/006_independence_wave_rhineland_bavaria_decisions.txt`
- `common/ai_strategy/006_independence_wave_rhineland_bavaria.txt`
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`
- `docs/events/006_independence_wave/northern_western_europe_packages.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_rhi_bay_gameplay_handoff_2026_07_15.md`

No shared allocator, reservation, registry, dispatcher, tag history, vanilla character, formable, event, or interface file was edited by this subtask.

## Runtime identifiers and parent hooks

### Exact package identity

- `is_independence_wave_rhi_package`
  - original tag `RHI`
  - package `constant:independence_wave_package_id.iw_008`
  - anchor and capital state 51
  - regional depth
  - industrial-breakaway archetype
- `is_independence_wave_bay_package`
  - original tag `BAY`
  - package `constant:independence_wave_package_id.iw_009`
  - anchor and capital state 52
  - regional depth
  - agrarian-regional archetype

### Setup and proof effects/triggers

- `can_initialize_independence_wave_iw_008_package`
- `can_initialize_independence_wave_iw_009_package`
- `independence_wave_setup_iw_008_rhineland`
- `independence_wave_setup_iw_009_bavaria`
- `has_prepared_independence_wave_iw_008_package_setup`
- `has_prepared_independence_wave_iw_009_package_setup`
- `has_complete_independence_wave_iw_008_package_setup`
- `has_complete_independence_wave_iw_009_package_setup`

### Bounded dispatcher adapters

- `independence_wave_dispatch_rhineland_bavaria_package_setup`
- `independence_wave_dispatch_rhineland_bavaria_package_final_validation`
- `independence_wave_dispatch_rhineland_bavaria_package_cleanup`

The parent must add these calls to the three corresponding functions in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`.

The parent must also extend `has_independence_wave_runtime_package_adapter_for_execution_id` and the package-specific preflight proof in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` for IDs 8 and 9. The current preflight requires a dormant-history `independence_wave_package_content_ready` flag and a pre-release command roster. That contract cannot prove these existing vanilla tags because this task was explicitly forbidden from adding readiness/content flags or duplicate tag history, and the institutional rosters are generated only after release. Parent integration must resolve this contract without weakening the living-country and frozen-plan protections.

## Character and portrait ownership

### Generated institutional characters

- `RHI_independence_wave_provisional_directorate`
  - country-leader roles: centrism, socialism, oligarchism, despotism
- `RHI_independence_wave_river_commandant`
  - distinct corps commander
  - despotism country-leader role for emergency and sovereignty routes
- `BAY_independence_wave_state_council`
  - country-leader roles: centrism, socialism, oligarchism, despotism
- `BAY_independence_wave_mountain_commandant`
  - distinct corps commander
  - despotism country-leader role for emergency and sovereignty routes

All four are created with guarded `generate_character` calls using stable `token_base` identifiers. No `recruit_character` call, common character duplicate, or history override is present.

### Vanilla historical-character gates

- `RHI_josef_friedrich_matthes`
  - availability flag: `independence_wave_rhi_matthes_available`
  - accepted only if the RHI country still has the vanilla character
  - portrait hook at package setup: `set_portraits` -> `GFX_portrait_RHI_josef_friedrich_matthes`
  - used only by the labor government
  - institutional fallback: `RHI_independence_wave_provisional_directorate`
- `BAY_rupprecht_of_bavaria`
  - availability flag: `independence_wave_bay_rupprecht_available`
  - accepted only if BAY still has him and GER does not
  - portrait hook at package setup: `set_portraits` -> `GFX_portrait_independence_wave_BAY_rupprecht_of_bavaria`
  - used only by the traditional restoration government
  - institutional fallback: `BAY_independence_wave_state_council`

The provisional openings always use the institutional authorities, so the real-person portraits remain route-owned. Cleanup restores the vanilla RHI and BAY portrait sprites. No global sprite override is used.

The two Event 006 portrait sprites and DDS files were already present and registered in `interface/006_independence_wave.gfx`; this subtask did not edit that concurrent asset surface.

## Focus framework and route publication

Both packages assign `constant:independence_wave_focus_assignment.full_framework`, so the shared Event 006 tree supplies the survival, government, economy, military, diplomacy, former-host, regional ambition, league, and high-chaos lanes. Package decisions provide the national overlays and visible ledgers.

### RHI route matrix

- constitutional: enabled
- popular council / labor: enabled
- traditional: disabled
- emergency military: enabled
- patron client: enabled
- radical sovereignty / independence: enabled
- former-host negotiation: enabled
- guarded frontier: enabled
- association: enabled
- reclamation: enabled
- internal power struggle: `civilians_vs_army`
- league route: enabled
- ambition family: enabled
- selected formable family: `rhine_federation` (`FORM04`)

Package government flags:

- `independence_wave_rhi_constitutional_government`
- `independence_wave_rhi_labor_government`
- `independence_wave_rhi_emergency_government`
- `independence_wave_rhi_patron_government`
- `independence_wave_rhi_sovereignty_government`

### BAY route matrix

- constitutional: enabled
- popular council / labor: enabled
- traditional / restoration: enabled
- emergency military: enabled
- patron client: enabled
- radical sovereignty / independence: enabled
- all four former-host routes: enabled
- internal power struggle: `restoration_court_vs_military_guardians`
- league route: enabled
- ambition family: enabled
- selected formable family: intentionally absent

Package government flags:

- `independence_wave_bay_constitutional_government`
- `independence_wave_bay_labor_government`
- `independence_wave_bay_traditional_government`
- `independence_wave_bay_emergency_government`
- `independence_wave_bay_patron_government`
- `independence_wave_bay_sovereignty_government`

The ordinary sovereignty government and the later high-chaos action are separate. The government can be formalized only after the shared radical-sovereignty route; the seizure action additionally requires `can_independence_wave_use_high_chaos_actions`.

## Visible values, missions, and balance paths

### RHI Corridor Authority

- variable: `independence_wave_rhi_corridor_authority`
- start: 25
- stable threshold: 65
- mission: `independence_wave_rhi_keep_rhine_arteries_open`
- deadline: 420 days

Baseline viable settlement:

1. `independence_wave_rhi_restore_bridge_dispatch`: +18, 75 days, light administration
2. `independence_wave_rhi_integrate_factory_rail_guards`: +18, 120 days, light security
3. `independence_wave_rhi_secure_river_crossings`: +12, 120 days, light administration

This reaches 73 in 315 serialized decision days. The 105-day margin permits resource recovery or one cancellation without making the baseline mathematically impossible. The optional host-ledger project gives +8 and diplomatic progress.

### BAY Civic Settlement and Mountain Security

- variables:
  - `independence_wave_bay_civic_settlement`
  - `independence_wave_bay_mountain_security`
- starts: 25 civic / 30 security
- stable thresholds: 60 / 60
- mission: `independence_wave_bay_hold_the_state_together`
- deadline: 480 days

Baseline viable settlement:

1. `independence_wave_bay_reconcile_district_treasuries`: +18 civic, 75 days, light administration
2. `independence_wave_bay_organize_mountain_passes`: +18 security, 120 days, light security
3. `independence_wave_bay_integrate_mountain_companies`: +18 civic / +18 security, 120 days, light administration

This reaches 61 civic / 66 security in 315 serialized decision days. The design intentionally consumes only one light security package during the baseline line because the shared regular-defector opening stockpile cannot safely fund two such commitments in succession. Labor, traditional, emergency, patron, and sovereignty government decisions subsequently trade civic consent against mountain security in different proportions.

Both missions apply package-variable losses plus the shared legitimacy, recognition, capacity, security, and instability failure bundle on timeout or loss of the capital. Timed projects are serialized by package-specific active-project triggers, pay real shared costs, and have cancellation effects.

## Decision identifiers

The file contains 32 package entries: 15 for RHI and 17 for BAY, including one timed crisis mission per country.

### RHI

- `independence_wave_rhi_keep_rhine_arteries_open`
- `independence_wave_rhi_restore_bridge_dispatch`
- `independence_wave_rhi_integrate_factory_rail_guards`
- `independence_wave_rhi_settle_host_customs_ledgers`
- `independence_wave_rhi_secure_river_crossings`
- `independence_wave_rhi_ratify_constitutional_charter`
- `independence_wave_rhi_entrust_workers_councils`
- `independence_wave_rhi_establish_corridor_command`
- `independence_wave_rhi_accept_patron_transit_mandate`
- `independence_wave_rhi_proclaim_sovereign_corridor`
- `independence_wave_rhi_codify_durable_independence`
- `independence_wave_rhi_survey_rhine_federation_corridor`
- `independence_wave_rhi_convene_rhine_congress`
- `independence_wave_rhi_charter_network_transit`
- `independence_wave_rhi_seize_corridor_authorities`

### BAY

- `independence_wave_bay_hold_the_state_together`
- `independence_wave_bay_reconcile_district_treasuries`
- `independence_wave_bay_organize_mountain_passes`
- `independence_wave_bay_settle_wittelsbach_host_ledgers`
- `independence_wave_bay_integrate_mountain_companies`
- `independence_wave_bay_ratify_constitutional_compact`
- `independence_wave_bay_entrust_workers_districts`
- `independence_wave_bay_restore_the_crown`
- `independence_wave_bay_establish_mountain_guardians`
- `independence_wave_bay_accept_patron_estates_mandate`
- `independence_wave_bay_proclaim_sovereign_directorate`
- `independence_wave_bay_codify_durable_independence`
- `independence_wave_bay_choose_south_german_restoration`
- `independence_wave_bay_keep_german_reunification_claim`
- `independence_wave_bay_convene_south_german_estates`
- `independence_wave_bay_negotiate_alpine_supply_accord`
- `independence_wave_bay_seize_south_german_protectorates`

## Idea lifecycles and maximum spirits

### RHI lifecycle pair

- founding: `rhi_divided_river_authority`
- mature: `rhi_rhine_civic_industrial_compact`

RHI route ideas:

- `rhi_constitutional_river_compact`
- `rhi_workers_rhine_charter`
- `rhi_emergency_corridor_command`
- `rhi_patron_transit_mandate`
- `rhi_sovereign_corridor_directorate`

### BAY lifecycle pair

- founding: `bay_disputed_state_inheritance`
- mature: `bay_estates_and_districts_settlement`

BAY route ideas:

- `bay_constitutional_state_compact`
- `bay_workers_district_charter`
- `bay_restoration_court_settlement`
- `bay_emergency_mountain_guardians`
- `bay_patron_estates_mandate`
- `bay_sovereign_mountain_directorate`

Each package owns exactly one lifecycle idea and at most one route idea at a time. The maximum simultaneous package-spirit count is **2**, below the requested maximum of 3. No decision adds a third persistent package idea.

## Starting forces

Force application is wrapped behind both `independence_wave_command_roster_ready` and the exact package command-roster proof.

### RHI (`p8`)

- shared profile: `regular_defectors` (3)
- military tradition: 71
- reinforcement mask: 1612
- inheritance mask: 2, enabling the shared air-inheritance lane
- resulting shared features: secure depots, converted defectors, factory/rail guards, professional officers, capital defense, and border defense

### BAY (`p9`)

- shared profile: `regular_defectors` (3)
- military tradition: 75
- reinforcement mask: 1676
- inheritance mask: 2, enabling the shared air-inheritance lane
- resulting shared features: secure depots, converted defectors, terrain units, professional officers, capital defense, and border defense

The setup calls only:

- `independence_wave_load_force_package_mapping`
- `independence_wave_apply_dynamic_starting_force`

No bespoke OOB, direct unit spawn, equipment archetype, or history army file was added.

## Formable coexistence

### RHI and FORM04

RHI selects `constant:independence_wave_formable_family.rhine_federation`, registers the family, sets `independence_wave_rhi_form04_candidate`, and opens survey plus congress decisions. The congress sets the shared formation-congress proof and calls `independence_wave_decision_request_selected_formable_commit`.

The package closes `declare_germany_reunified_decision` only after the prepared setup proof succeeds, so Event 006 RHI is committed to the Rhine Federation identity rather than competing with the vanilla Germany path. Cleanup calls `activate_decision = declare_germany_reunified_decision`, making rollback reversible.

The RHI setup and prepared proof both reject simultaneous active `IW-010` Ajax, preserving the shared `RG-RHINE-SAAR` exclusion.

### BAY and Germany

BAY intentionally clears and does not register an Event 006 formable family. It sets `independence_wave_bay_german_reunification_preserved` at setup and never creates a duplicate Germany formable.

After the shared regional ambition opens, mutually exclusive decisions choose between:

- `independence_wave_bay_choose_south_german_restoration`
  - removes `declare_germany_reunified_decision`
  - opens `independence_wave_bay_convene_south_german_estates`
  - produces a diplomatic South German settlement, not a new Germany tag
- `independence_wave_bay_keep_german_reunification_claim`
  - leaves the vanilla decision intact
  - applies broader-claim recognition and instability tradeoffs

Cleanup reactivates the vanilla decision if the South German choice had removed it.

## AI behavior

Decision AI prioritizes the solvable founding line, favors emergency government under severe former-host threat, prefers Matthes labor or Rupprecht restoration when those historical figures are genuinely available, weighs South German restoration against the wider German claim, advances the network projects, and uses high-chaos actions only after the shared gate opens.

Macro profiles include:

- `independence_wave_rhi_corridor_survival`
- `independence_wave_rhi_founding_restraint`
- `independence_wave_rhi_host_threat`
- `independence_wave_rhi_civic_corridor_policy`
- `independence_wave_rhi_corridor_command`
- `independence_wave_rhi_high_chaos_command`
- `independence_wave_bay_mountain_survival`
- `independence_wave_bay_founding_restraint`
- `independence_wave_bay_host_threat`
- `independence_wave_bay_civic_state_policy`
- `independence_wave_bay_restoration_court`
- `independence_wave_bay_mountain_guardians`
- `independence_wave_bay_high_chaos_command`

They use only AI strategy types already proven by the Wallonia/Frisia packages: army construction, equipment production, building priorities, and early-war restraint. Dynamic former-host behavior stays in shared triggers and package decision weights; no fixed host tag is assumed.

## Validation evidence

- All 103 referenced script-constant namespace/key pairs resolve to existing definitions.
- All 73 package scripted-effect or scripted-trigger `= yes` calls resolve to a definition in `common/scripted_effects` or `common/scripted_triggers`.
- All 32 declared mission/decision entries have matching cleanup references and English name/description localisation.
- All 23 timed decisions are included in the relevant serialized active-project trigger.
- All package effect/trigger/decision/idea/AI files have balanced script braces.
- The seven reused decision sprites resolve exactly once in `interface/006_independence_wave.gfx`.
- Both route-owned portrait sprites resolve exactly once, and both referenced DDS files exist.
- Institutional character tokens have no vanilla collision; their only repository references are the new effects, triggers, and localisation.
- RHI's baseline crisis line reaches 73/65 in 315/420 serialized days.
- BAY's baseline crisis line reaches 61/66 against 60/60 in 315/480 serialized days.
- The BAY availability proof rejects Rupprecht if Germany has recruited or received him; the RHI proof uses Matthes only while RHI still has him.
- The RHI complete proof requires the Germany decision-closure flag; the cleanup restores that decision.
- The localisation file is UTF-8 with BOM and contains no legacy `:0` keys.

## Skipped work, simplifications, omissions, and blockers

### Parent-owned integration blockers

1. **Runtime dispatcher not wired.** The three bounded adapters exist but are not yet called by `006_independence_wave_package_dispatch_effects.txt`.
2. **Preflight registry cannot currently admit these packages.** IDs 8 and 9 are absent, and the current contract requires a forbidden dormant-history content flag and pre-release generated roster.
3. **FORM04 final commit consumer is absent.** RHI can discover, survey, convene, and submit the selected family, but `independence_wave_decision_request_selected_formable_commit` currently only publishes `independence_wave_formable_commit_pending`. No family-specific shared transaction consumes it.
4. **Audited readiness remains parent-owned.** No package content/readiness flag was created or set, as required.

### Intentional non-omissions

- No new RHI or BAY history file was added; the guarded runtime roster is the required non-duplicating approach for living vanilla tags.
- No separate RHI/BAY focus tree was added; both packages use the accepted shared full framework plus package overlays.
- No South German or duplicate Germany formable was added; the South German line is an ambition and diplomatic settlement, while the vanilla Germany formable remains the deliberate alternative.
- No bespoke OOB was added; the accepted shared force mappings supply the complete starting-force package.
- No new visual fallback was created; the approved portraits and shared Event 006 decision icons already exist and are wired by stable sprite names.
- Soviet Collapse content and origins were not touched; every trigger is locked to Event 006 package IDs 8 or 9.

Within the bounded package files, no route, government, visible value, mission, host settlement, network project, high-chaos action, AI profile, localisation surface, portrait hook, force call, lifecycle, or cleanup path requested for RHI/BAY was simplified or omitted.

## Skills and references used

- `chaos-redux-events`
- `hoi4-focus-trees`
- `hoi4-decisions-missions`
- required offline Paradox wiki pages, including national focuses, country creation, divisions, portraits, events, decisions, ideas, AI, scopes, triggers, effects, modifiers, localisation, and on-actions
- official vanilla documentation for script concepts, script constants, effects, triggers, and generated characters
- vanilla RHI/BAY histories and characters, Germany's Rupprecht transfer, and the vanilla German reunification decision
- existing Event 006 Wallonia/Frisia package and shared focus, decision, force, formable, and dispatcher layers
