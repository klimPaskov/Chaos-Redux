# Event 019 achievement tracking handoff

## Status

The bounded achievement tracking package is ready for integration. It provides centralized thresholds, eleven completion triggers, persistent history/disqualifier effects, exact generation/lot/unit audits, rail continuity, claimant and derivative tracking, scenario continuity, and one-shot capitulation/annex hooks.

The package is not a complete wired achievement set on its own. Shared Event 019 files, the achievement registry, localisation, and icons remain parent-owned. Four battle achievements also remain deliberately unwired because the documented public combat callback does not expose an exact participating division or the three required significance measurements. No country-level proxy was substituted.

## Files added

- `common/script_constants/019_infantry_spawn_achievement_constants.txt`
- `common/scripted_triggers/019_infantry_spawn_achievement_triggers.txt`
- `common/scripted_effects/019_infantry_spawn_achievement_effects.txt`
- `common/on_actions/019_infantry_spawn_achievement_on_actions.txt`
- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_achievement_tracking_handoff.md`

No shared gameplay, registry, localisation, interface, or asset file was edited by this subagent.

## Achievement contracts

| Achievement | Positive proof | Persistent exclusions or continuity checks | Wiring status |
| --- | --- | --- | --- |
| Every Rifle Accounted For | Close a generation of at least 30 units with no unresolved lot or obligation, at least 70 Muster Control, and congestion below 25 | No claimant takeover, revolt history, forced setup, or debug completion | Tracking implemented; closeout hook required |
| One Battalion Wonder | Win a significant battle with the exact tracked generated division whose immutable original signature contains one combat component and is still present | Exact live unit row, active status, original unit/lot/generation/template identity, no sanctioned composition edit | Exact recorder implemented; combat bridge unavailable |
| The Army Has Voted | Exact promoted claimant remains country leader for 365 days or leads the country to capitulate/annex a major | Player, unforced, exact stored character identity | Tracking implemented; promotion hook required |
| Order from Noise | Integrate at least 8 distinct Evolution III random lots, reach Evolution III, at least 85 Muster Control, and congestion below 25 | Player, unforced | Tracking implemented; integration hook required |
| Combined Arms Accident | Win a significant battle with an exact Evolution III random division containing at least 8 distinct generated combat-component types still present | Exact unit proof and no sanctioned composition edit | Exact recorder implemented; combat bridge unavailable |
| No Room on the Train | Close a generation of at least 20 units with at least 15 integrated units after maintaining and completing the exact lot-origin rail corridor | Live capital-to-origin railway at start, during pulse checks, mission completion, and closeout; no emergency integration | Tracking implemented; rail, pulse, and closeout hooks required |
| Borrowed Future | Win a significant battle with the exact generated division registered before a required technology/project was unlocked, while at least one registered gate remains locked | Exact unit proof and no sanctioned composition edit | Exact recorder implemented; combat bridge unavailable |
| Three False Apocalypses | As the non-derivative player parent, defeat exact isolated zombie, ghost, and golem derivative countries, each with a distinct country ID | No parent-event forced merge | Tracking implemented; derivative metadata and defeat ordering required |
| Barracks of Babel | Win a significant battle with an exact Evolution III random division whose generated signature still contains camelry, bicycle, amphibious tank, flame element, artillery, and engineers | Exact unit proof and no sanctioned composition edit | Exact recorder implemented; combat bridge unavailable |
| Quiet Demobilisation | Close a generation of at least 30 units after every lot and unit is fully demobilized through supervised teardown, with no unresolved obligation and at least 70 Muster Control | No revolt, claimant takeover, emergency integration, teardown invariant failure, forced setup, or debug completion | Tracking implemented; teardown and closeout hooks required |
| Every Barracks a Front | Launch General Mutiny or Anomalous Rising at maximum intensity and survive 365 days or defeat an exact scenario actor | Starting player country remains the player country; no tag switch, AI takeover, world end, or intensity change | Tracking implemented; scenario setup and pulse hooks required |

Central values are in `constant:infantry_spawn_achievement_threshold.*`, `constant:infantry_spawn_achievement_battle.*`, and `constant:infantry_spawn_achievement_technology_gate.*`. The exact profile-to-technology dispatcher mirrors all 43 equipment profiles in the Event 019 unit registry.

## Parent integration hooks

All snippets below are country scope unless stated otherwise.

### 1. Capture every generated division and its pre-technology gates

In `common/scripted_effects/019_infantry_spawn_generation_effects.txt`, inside `infantry_spawn_spawn_current_template_unit`, call this after the exact live division has been captured and the unit row and obligations have been registered successfully:

```hoi4
infantry_spawn_achievement_register_current_generated_division = yes
```

In `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`, call the same idempotent effect immediately after:

```hoi4
infantry_spawn_unit_registry_mark_current_live_division_manifest = yes
```

The second call is necessary for Evolution III because its complete manifest equipment-profile list exists only after registry scoring.

### 2. Record exact random-lot integration

In `common/scripted_effects/019_infantry_spawn_management_effects.txt`, inside `infantry_spawn_record_integrated_lot`, call this while `infantry_spawn_lot_row_index` still points to the successful exact lot:

```hoi4
infantry_spawn_achievement_record_current_lot_integration = yes
```

The effect deduplicates by lot UID and records only `evolution_iii_random` lots.

### 3. Disqualify sanctioned composition edits before mutation

Inside `infantry_spawn_complete_selected_lot_standardization`, immediately before the meta effect that unlocks or changes the selected lot template, insert:

```hoi4
set_temp_variable = {
	infantry_spawn_achievement_target_lot_uid = infantry_spawn_lot_uid_entries^infantry_spawn_lot_row_index
}
infantry_spawn_achievement_disqualify_units_in_current_lot = yes
```

Use the same two-step contract before every future standardization, recombination, replacement, or sanctioned template-unlock path. It records exact unit UIDs from the lot, so later battle proof cannot be credited after an authorized composition mutation.

### 4. Mark emergency instant-integration paths

Inside `infantry_spawn_emergency_integrate_selected_lot`, call this on the successful path after the lot status is committed and before `infantry_spawn_record_integrated_lot`:

```hoi4
infantry_spawn_achievement_mark_emergency_integration = yes
```

The parent must also decide whether `infantry_spawn_recognize_selected_emergency_reserve` is an emergency instant-integration path under the achievement design. If it bypasses the ordinary audited/integrated lifecycle, call the same effect there. This is a design classification, not a safe assumption for this bounded package.

### 5. Record supervised demobilisation before closeout

Inside `infantry_spawn_execute_exact_lot_teardown`, on the successful full-teardown branch, call this immediately after `infantry_spawn_record_demobilized_lot` and before `infantry_spawn_close_resolved_generations`:

```hoi4
infantry_spawn_achievement_record_supervised_demobilized_lot = yes
```

The effect rejects a failed teardown, specialist-only preservation, and an invalid lot UID. Do not move this call after closeout; the generation audit must see the proof.

On the teardown failure branch, call:

```hoi4
infantry_spawn_achievement_mark_teardown_invariant_failure = yes
```

### 6. Audit the exact generation at closeout

Inside `infantry_spawn_close_resolved_generations`, after the exact generation row becomes resolved and after `infantry_spawn_last_closed_generation_uid` is assigned, but while `infantry_spawn_closeout_generation_uid` still identifies that row, call:

```hoi4
infantry_spawn_achievement_evaluate_closed_generation = yes
```

This single audit can set Every Rifle Accounted For, No Room on the Train, and Quiet Demobilisation ready flags.

### 7. Wire the rail proof lifecycle

Inside `infantry_spawn_start_rail_corridor_mission`, after the selected lot and target state have been captured and before mission activation, call:

```hoi4
infantry_spawn_achievement_start_rail_proof = yes
```

Inside the success branch of `infantry_spawn_complete_rail_corridor_mission`, before clearing its target-state variable, call:

```hoi4
infantry_spawn_achievement_complete_rail_proof = yes
```

Inside the failure branch, call:

```hoi4
infantry_spawn_achievement_mark_rail_proof_failure = yes
```

The helper verifies an actual `has_railway_connection` from the current capital to the controlled exact origin state. Control alone is not accepted.

### 8. Register the exact claimant after promotion

In `common/scripted_effects/019_infantry_spawn_claimant_crisis_effects.txt`, inside `infantry_spawn_resolve_selected_claimant_takeover`, immediately after:

```hoi4
infantry_spawn_promote_selected_claimant_character = yes
```

insert:

```hoi4
infantry_spawn_achievement_register_claimant_takeover = yes
```

The effect verifies that `event_target:infantry_spawn_selected_claimant_character` is actually the leader, persists that exact character scope, and begins the 365-day pending flag. `on_capitulation` and `on_annex` already recognize an exact major defeat while that character remains leader.

Every claimant revolt and derivative revolt path must also call:

```hoi4
infantry_spawn_achievement_mark_claimant_or_derivative_revolt = yes
```

### 9. Preserve derivative identity before defeat cleanup

The derivative package must persist, on every derivative country:

- `infantry_spawn_derivative_family_id`
- `infantry_spawn_derivative_former_parent`
- exactly one family flag: `infantry_spawn_zombie_derivative`, `infantry_spawn_ghost_derivative`, or `infantry_spawn_golem_derivative`

Before lifecycle cleanup mutates or clears those fields, its defeat effect must save the exact winner as `event_target:infantry_spawn_achievement_derivative_winner` and call, in losing-derivative scope:

```hoi4
infantry_spawn_achievement_record_current_derivative_defeat = yes
```

The sibling derivative-package agent confirmed these fields and ordering are part of its handoff. The supplied capitulation/annex on-actions also call this effect. It is idempotent and requires the exact winner target, exact family ID, family flag, parent isolation, and a non-derivative human winner. The three recorded derivative country IDs must be distinct.

Any parent-side forced merge of one of these derivative events must call:

```hoi4
infantry_spawn_achievement_mark_parent_event_merge = yes
```

### 10. Wire triggerable-scenario history without a global scan

After the scenario type and intensity have been frozen in globals, call in the starting player-country scope:

```hoi4
infantry_spawn_achievement_register_scenario_launch = yes
infantry_spawn_schedule_country_pulse = yes
```

For every exact scenario actor created or selected, set:

```hoi4
set_country_flag = infantry_spawn_scenario_actor
set_variable = {
	infantry_spawn_scenario_origin_country_id = <starting player country ID>
}
```

The starting country ID must be copied from the player scope during setup; it cannot be inferred later after scopes change.

On any post-launch intensity edit, call:

```hoi4
infantry_spawn_achievement_mark_scenario_intensity_changed = yes
```

On any explicit player-country/tag switch, call:

```hoi4
infantry_spawn_achievement_mark_scenario_tag_switch = yes
```

In `common/scripted_effects/019_infantry_spawn_pulse_effects.txt`, inside `infantry_spawn_run_country_pulse`, call before rescheduling:

```hoi4
infantry_spawn_achievement_country_pulse = yes
infantry_spawn_schedule_country_pulse = yes
```

In `common/scripted_triggers/019_infantry_spawn_triggers.txt`, extend `infantry_spawn_country_can_continue_pulse` with this additional `OR` branch:

```hoi4
AND = {
	has_country_flag = infantry_spawn_achievement_scenario_launched
	NOT = { has_country_flag = infantry_spawn_achievement_scenario_tracking_complete }
}
```

This keeps the already country-scoped Event 019 pulse alive until scenario survival succeeds or continuity fails. It does not add a daily, weekly, monthly, country, or world scan.

### 11. Mark forced setup and debug completion at their sources

Every forced non-scenario setup entry must call:

```hoi4
infantry_spawn_achievement_mark_forced_setup = yes
```

Every debug or test path that completes, closes, integrates, demobilizes, wins, or otherwise satisfies Event 019 conditions must call:

```hoi4
infantry_spawn_achievement_mark_debug_completion = yes
```

Scenario launch intentionally sets the forced-setup history itself. Every Barracks a Front uses its separate scenario continuity contract and therefore checks player identity rather than the ordinary unforced-history trigger.

## Achievement registry insertion

Append the following blocks to `common/achievements/chaos_redux_achievements.txt` under an Event 019 heading. The four battle-dependent achievements are hidden as specified.

```hoi4
019_infantry_spawn_every_rifle_accounted_for = {
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_every_rifle_accounted_for_tooltip
			infantry_spawn_achievement_every_rifle_accounted_for_is_complete = yes
		}
	}
}

019_infantry_spawn_one_battalion_wonder = {
	hidden = yes
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_one_battalion_wonder_tooltip
			infantry_spawn_achievement_one_battalion_wonder_is_complete = yes
		}
	}
}

019_infantry_spawn_the_army_has_voted = {
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_the_army_has_voted_tooltip
			infantry_spawn_achievement_the_army_has_voted_is_complete = yes
		}
	}
}

019_infantry_spawn_order_from_noise = {
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_order_from_noise_tooltip
			infantry_spawn_achievement_order_from_noise_is_complete = yes
		}
	}
}

019_infantry_spawn_combined_arms_accident = {
	hidden = yes
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_combined_arms_accident_tooltip
			infantry_spawn_achievement_combined_arms_accident_is_complete = yes
		}
	}
}

019_infantry_spawn_no_room_on_the_train = {
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_no_room_on_the_train_tooltip
			infantry_spawn_achievement_no_room_on_the_train_is_complete = yes
		}
	}
}

019_infantry_spawn_borrowed_future = {
	hidden = yes
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_borrowed_future_tooltip
			infantry_spawn_achievement_borrowed_future_is_complete = yes
		}
	}
}

019_infantry_spawn_three_false_apocalypses = {
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_three_false_apocalypses_tooltip
			infantry_spawn_achievement_three_false_apocalypses_is_complete = yes
		}
	}
}

019_infantry_spawn_barracks_of_babel = {
	hidden = yes
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_barracks_of_babel_tooltip
			infantry_spawn_achievement_barracks_of_babel_is_complete = yes
		}
	}
}

019_infantry_spawn_quiet_demobilisation = {
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_quiet_demobilisation_tooltip
			infantry_spawn_achievement_quiet_demobilisation_is_complete = yes
		}
	}
}

019_infantry_spawn_every_barracks_a_front = {
	possible = { custom_override_tooltip = { tooltip = infantry_spawn_achievement_eligible_tooltip always = yes } }
	happened = {
		custom_override_tooltip = {
			tooltip = infantry_spawn_achievement_every_barracks_a_front_tooltip
			infantry_spawn_achievement_every_barracks_a_front_is_complete = yes
		}
	}
}
```

## Localisation and icon handoff

The parent/localisation owner must add UTF-8-BOM entries for:

- `infantry_spawn_achievement_eligible_tooltip`
- one `<achievement_id>_NAME` and `<achievement_id>_DESC` pair for each of the eleven registry IDs
- `infantry_spawn_achievement_every_rifle_accounted_for_tooltip`
- `infantry_spawn_achievement_one_battalion_wonder_tooltip`
- `infantry_spawn_achievement_the_army_has_voted_tooltip`
- `infantry_spawn_achievement_order_from_noise_tooltip`
- `infantry_spawn_achievement_combined_arms_accident_tooltip`
- `infantry_spawn_achievement_no_room_on_the_train_tooltip`
- `infantry_spawn_achievement_borrowed_future_tooltip`
- `infantry_spawn_achievement_three_false_apocalypses_tooltip`
- `infantry_spawn_achievement_barracks_of_babel_tooltip`
- `infantry_spawn_achievement_quiet_demobilisation_tooltip`
- `infantry_spawn_achievement_every_barracks_a_front_tooltip`

Achievement art should use the stable registry IDs as filenames under `gfx/achievements/`, following the existing custom-achievement loader convention. The asset manifest must record all eleven IDs; hidden entries still require final icon art.

## Exact battle bridge blocker

`infantry_spawn_achievement_record_exact_division_significant_victory` is intentionally dormant. A future exact combat bridge must call it in the owning country scope with all of these inputs from the same won battle:

```hoi4
event_target:infantry_spawn_achievement_battle_division
infantry_spawn_achievement_battle_enemy_strength_ratio
infantry_spawn_achievement_battle_duration_hours
infantry_spawn_achievement_battle_enemy_casualties
```

The values must meet the centralized minimums of 0.50 enemy strength ratio, 24 hours, and 500 enemy casualties. The division target must be the exact participating generated division, not any division owned by the winner.

Vanilla `on_army_leader_won_combat` documents `ROOT` as the unit leader and `FROM` as the owning country. It does not expose combat scope, a participating division, enemy strength ratio, duration, or casualties. The installed effects/triggers also expose no supported leader-to-exact-participating-division iterator. Consequently:

- One Battalion Wonder cannot currently become ready.
- Combined Arms Accident cannot currently become ready.
- Borrowed Future cannot currently become ready.
- Barracks of Babel cannot currently become ready.

This is a hard engine/input blocker, not an omitted country proxy. Registering the hidden achievements before an exact bridge exists is safe but leaves them unobtainable.

There is a second, narrower engine limitation even after a bridge exists: the scanner proves exact ledger identity, live unit scope, active status, the continued presence of every generated component token, and the absence of every sanctioned composition-edit hook. HOI4 exposes no exact unit-level trigger proving that the division has not been manually switched to a different superset clone/template. Locked Event 019 templates and complete edit-path disqualification substantially constrain this, but they do not prove it absolutely. Do not describe that proof as stronger than the engine permits.

## Validation evidence

- All technology and special-project identifiers used by the gate dispatcher were matched against vanilla source.
- The equipment-profile gate dispatcher covers the same 43 equipment profiles as the Event 019 registry technology-lock trigger.
- The package uses only one-shot capitulation/annex hooks and the existing country-scoped Event 019 pulse; it adds no daily, weekly, monthly, all-country, or world iteration.
- Derivative defeat recording requires exact family ID, exact family flag, parent-isolation state, a non-derivative human winner, and three distinct defeated country IDs.
- Rail proof checks a live railway connection rather than accepting controlled-state ownership as a substitute.

## Simplifications, omissions, and blockers

- No fallback or country-level battle proxy was implemented.
- Four battle achievements remain unwired and unobtainable until an exact combat bridge can provide all required inputs.
- Shared integration hooks, registry entries, localisation, icons, and the Event 019 asset manifest remain parent-owned and are listed above.
- The classification of `infantry_spawn_recognize_selected_emergency_reserve` as an emergency integration exploit requires the parent’s design decision.
- Exact proof against a manual switch to a different superset clone/template is not exposed by the engine; the implemented proof is limited as described above.

