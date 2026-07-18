# Event 019 triggerable scenario runtime handoff

> Visual supersession notice (2026-07-16): the original generic-government
> image statement in this dated handoff predates the formation-first visual
> override. SCN-013 now resolves `GetInfantrySpawnScenarioActorArmyScene` and
> uses Event 19 army/muster or massed-host scenes; it no longer uses
> `GFX_portrait_communist_rebels`. Gameplay and transaction findings below
> remain historical implementation evidence.

## Outcome

The Event 019 scenario runtime is implemented and registered as `SCN-013`, **The Unbidden Muster**, for all four types and all four intensities. It creates real connected dynamic breakaways where territory permits, uses a same-tag government takeover for one-state and all-island hosts, materializes fresh Event 019 formations, begins immediate former-parent wars, limits additional High/Maximum wars to valid adjacent targets, isolates anomalous providers from their parent event chains, records exact achievement actors, and clears all setup bypass state.

The shared data-driven launcher owns the stable ID, aligned registry arrays, four sort views, type cycling, eligibility bridge, scripted-localisation selectors, confirmation dispatch, and English row text. The existing generic scripted GUI and interface require no scenario-specific edit. No existing ID was overwritten and no substitute fallback was added.

## Files and identifiers

### Scenario-owned gameplay files

- `common/script_constants/019_infantry_spawn_scenario_constants.txt`
  - four exact type values and four exact intensity values;
  - country share, revolt pressure, state coverage, generation/lot/family/front/war counts, actor manpower, bounded safety tuning, and scenario AI weights.
- `common/ai_strategy/019_infantry_spawn_scenario_ai_strategy.txt`
  - self-removing common actor strategy;
  - distinct conventional, mobile-arsenal, claimant-command, and anomalous-host production/force postures keyed to each actor's frozen scenario type.
- `common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt`
  - `infantry_spawn_scenario_launch_inputs_are_valid`
  - `infantry_spawn_scenario_country_is_valid_host`
  - `infantry_spawn_scenario_can_launch_unregistered`
  - `infantry_spawn_scenario_can_launch_from_triggerable_scenarios`
  - `infantry_spawn_scenario_launch_has_no_surviving_hostile_actors`
  - `infantry_spawn_scenario_country_can_split`
  - `infantry_spawn_scenario_revolt_state_is_candidate`
  - `infantry_spawn_scenario_regional_war_target_is_valid`
  - `infantry_spawn_scenario_current_registry_row_can_form_derivative`
- `common/scripted_effects/019_infantry_spawn_scenario_effects.txt`
  - public entry: `infantry_spawn_scenario_launch_unregistered`
  - intensity: `infantry_spawn_scenario_load_intensity_runtime`
  - bypass/profile: `infantry_spawn_scenario_clear_actor_bypass`, `infantry_spawn_scenario_apply_actor_bypass_for_type`
  - actor identity: `infantry_spawn_scenario_mark_actor`, `infantry_spawn_scenario_install_actor_government`, `infantry_spawn_scenario_set_actor_ai_profile`, `infantry_spawn_scenario_apply_actor_pressure`
  - region/family selection: `infantry_spawn_scenario_build_coherent_revolt_region`, `infantry_spawn_scenario_select_derivative_family`
  - packages: `infantry_spawn_scenario_begin_ordinary_generation`, `infantry_spawn_scenario_run_conventional_flood_package`, `infantry_spawn_scenario_run_arsenal_lottery_package`, `infantry_spawn_scenario_materialize_random_lots`, `infantry_spawn_scenario_run_general_mutiny_package`, `infantry_spawn_scenario_find_takeover_family_row`, `infantry_spawn_scenario_materialize_one_takeover_family_formation`, `infantry_spawn_scenario_run_anomalous_rising_package`, `infantry_spawn_scenario_run_actor_package`
  - territory/diplomacy: `infantry_spawn_scenario_transfer_selected_region_to_actor`, `infantry_spawn_scenario_rollback_dynamic_actor_creation`, `infantry_spawn_scenario_declare_regional_wars`, `infantry_spawn_scenario_create_dynamic_actor_from_selected_region`, `infantry_spawn_scenario_execute_same_tag_takeover`, `infantry_spawn_scenario_process_host`
  - actor-root dispatch: `infantry_spawn_scenario_finalize_actor_setup`
- `events/019_infantry_spawn_scenario.txt`
  - hidden actor-root event `chaosx.nr19.950`;
  - direct-caller confirmation `chaosx.nr19.951`;
  - setup-complete report `chaosx.nr19.952`;
  - setup-failed report `chaosx.nr19.953`.
- `common/scripted_localisation/019_infantry_spawn_scenario_scripted_localisation.txt`
  - exact pending and active type/intensity selectors for confirmation and setup reports.
- `localisation/english/019_infrantry_spawn_l_english.yml`
  - `infantry_spawn_scenario_muster_council`
  - `infantry_spawn_scenario_unbidden_assembly`
- `docs/systems/019_infantry_spawn_triggerable_scenario.md`
  - shared and direct callers, type/intensity behavior, revolt safety, isolation, roster, cleanup, assets, and SCN-013 registration contract.

### Shared scenario integration

- `common/script_constants/chaosx_triggerable_scenarios_constants.txt`
  - `triggerable_scenario_id.infantry_spawn = 13`;
  - `triggerable_scenario_sort_value.infantry_spawn_name = 5.75`.
- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`
  - initializes the Event 019 type selector;
  - keeps the ID/name arrays aligned in the registry and all four view orders;
  - cycles all four type values with exact wraparound;
  - maps the confirmed shared selectors to the raw Event 019 launch effect.
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
  - delegates SCN-013 button and confirmation eligibility to the pure Event 019 bridge trigger, which validates persistent type/intensity selectors without writing temporary variables.
- `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt`
  - resolves the SCN-013 row ID/name, four descriptions, four type names, four intensity impacts, and launch status before the Zombie fallbacks.
- `localisation/english/chaosx_gui_l_english.yml`
  - The Unbidden Muster shared row and confirmation text.

## Exact direct caller

```txt
set_temp_variable = {
	infantry_spawn_scenario_launch_type_input = constant:infantry_spawn_scenario.type_general_mutiny
}
set_temp_variable = {
	infantry_spawn_scenario_launch_intensity_input = constant:infantry_spawn_scenario.intensity_maximum
}
infantry_spawn_scenario_request_unregistered = yes
```

Both inputs use exact enum equality; fractional values between two enum members are rejected. `infantry_spawn_scenario_request_unregistered` is the player-facing confirmation route. `infantry_spawn_scenario_launch_unregistered` remains the raw no-confirmation route for trusted scripted callers.

## Scenario behavior proof

- Conventional Flood always runs baseline, Evolution I, and Evolution II generations even at Low. Higher intensities add further Evolution II generations. Registered anomalous providers are explicitly skipped.
- Arsenal Lottery locks its actor to Evolution II and uses the ordinary serious/strange generation package.
- General Mutiny draws fully random `scripted_scenario` lots, creates an exact claimant, assigns available lots, executes takeover, and gives dynamic actors the claimant-breakaway wrapper after freezing claimant UID, archetype, origin generation, and former parent.
- Anomalous Rising selects only aligned rows that allow Event 019 spawning and publish derivative plus parent-isolation profiles. Dynamic actors run the exact provider setup and family materializer without firing a parent event.
- Splittable hosts lose only a connected controlled noncapital mainland region; the parent retains its capital. Every completed dynamic actor starts an annexation war against the former parent.
- Existing civil wars use the same independent dynamic-country route. No nested `start_civil_war` call exists.
- One-state and all-island hosts are never partitioned. They receive the complete package in place and attempt only a reachable adjacent war.
- High and Maximum extra wars require adjacency, ordinary-country validity, absence from the scenario actor roster, no existing war, and `can_declare_war_on`.
- Maximum never sets `world_end`.
- A second launch is rejected by durable `_launched` history. Actor setup is idempotent, provisional failures are not rostered, and final cleanup clears every scenario bypass/profile/force flag.
- Successful actors freeze their launch type and intensity. Self-removing AI strategies give every AI actor a viable army/supply posture and type-specific conventional, mobile, claimant-offense, or anomalous-host priorities.
- No existing division is transferred. Every new formation is represented by Event 019's generation, lot, template, unit, obligation, claimant, or derivative ledgers.

## Achievement contract supplied

The launch freezes `global.infantry_spawn_scenario_launch_serial`, copies it to the initiating country and each successful actor, fills `global.infantry_spawn_scenario_actor_countries`, freezes a nonzero hostile total when hostile actors exist, sets `infantry_spawn_scenario_origin_pulse_active`, and calls `infantry_spawn_achievement_register_scenario_launch` after type/intensity freeze.

`infantry_spawn_scenario_launch_has_no_surviving_hostile_actors` scans that exact roster and launch serial. It excludes only the initiating same-tag takeover actor and counts an exact hostile actor as defeated only after capitulation or removal.

## Parent integration completed

The parent patched the four main evolution triggers in `common/scripted_triggers/019_infantry_spawn_triggers.txt`. For each stage, the natural global flag branch is disabled while the scenario profile lock exists, but the explicit country force flag remains valid:

```txt
infantry_spawn_has_evolution_i = {
	OR = {
		AND = {
			NOT = { has_country_flag = infantry_spawn_scenario_profile_locked }
			has_global_flag = infantry_spawn_evolution_i_active
		}
		has_country_flag = infantry_spawn_scenario_force_evolution_i
	}
}
```

The same structure is present on `_ii`, `_iii`, and `_iv` with their matching global and country flags. Natural world evolution therefore cannot contaminate the scenario's forced package profile.

## Natural claimant-revolt boundary

The connected-region selector and dynamic actor creator are scenario-owned
precedents, not a substitute for natural claimant revolt. They transfer selected
states and create fresh scenario formations; they never recreate or delete the
selected claimant's exact preexisting division ledger. Natural revolt
eligibility is explicitly fail-closed and awaits the user's separate approval
for that exact recreate/delete transaction.

## Assets and localisation

No new visual asset or `.gfx` registration is required. The two generated leader names use the existing `GFX_portrait_communist_rebels`, while the direct confirmation and result reports reuse `GFX_report_event_infantry_spawn`. The shared localisation now owns the `#013` row, The Unbidden Muster name, four type descriptions and labels, four intensity impacts, and blocked-launch explanations.

## Validation evidence

- All scenario scripts have balanced braces and no duplicate top-level scenario identifier.
- The source contains no `start_civil_war`, transfer of a parent's existing divisions into a new actor, call to the currently undefined natural claimant revolt helper, or `world_end` setter. Transaction rollback uses `annex_country` with `transfer_troops = yes` only to return a failed provisional actor and its newly created forces to the former parent.
- The exact actor-root dispatch uses a no-delay hidden country event, matching the documented immediate `country_event` form and preventing parent `ROOT` from leaking into Event 019 ledger helpers.
- Scenario type and intensity dispatch cover all 16 exact combinations through shared package and tuning tables.
- Registry and view arrays contain SCN-013 exactly once. Name ascending places it after Cannibalism/The Hunger Lines and before The World in Fury; name descending reverses that neighborhood; ID descending places 13 first; ID ascending places 13 last.
- Shared confirmation maps the live type and intensity selectors directly into `infantry_spawn_scenario_launch_unregistered`, avoiding the direct-caller confirmation event and preserving the one-confirmation flow.
- Localisation remains UTF-8 with BOM.
- The optional `hoi4.event_inspect` lint could not retain its read-only artifact because the shared artifact store returned `ARTIFACT_STORAGE_LIMIT`; no source conclusion relies on that failed optional tool.

## Simplifications, omissions, and blockers

- The natural claimant revolt's exact division-ledger transaction remains separately approval-gated and was not replaced by the scenario's state-only actor creation.
- The event catalog workbook was deliberately not edited in this bounded registration tranche.
- No gameplay simplification or fallback was used inside the implemented runtime or SCN-013 launcher integration.

## Skills and references

The implementation used `chaos-redux-events`, `hoi4-decisions-missions`, and `chaos-redux-subagents`, plus the required offline wiki, official vanilla documentation, vanilla dynamic-country precedents, and current Chaos Redux Event 019/provider patterns. No skill file required an update because this tranche introduced no reusable workflow absent from the existing skills.

## Git handoff

No subagent commit was created. The worktree contains concurrent parent and sibling changes; the parent owns the final Event 019 commit.
