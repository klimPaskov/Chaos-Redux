# Event 014 Wendigo Preservation Map

## Purpose

Event 014 must merge with the existing live Wendigo outbreak country rather than recreate a generic `ZZZ` country. The merge must preserve the active country's territory, player control, units, templates, technologies, ideas, profile variables, recruitment rules, AI identity, and zombie-system links before adding Event 014 state.

This map records the current repository contracts that the Event 014 unification effects must preserve.

## Live-country identity

A valid existing Wendigo is a dynamic country with all of the following:

- `original_tag = ZZZ`
- `weaponized_zombie_type_wendigo`
- `weaponized_zombie_archetype_wendigo`
- a live country scope, not the dormant base `ZZZ` shell

The canonical creation path is `spawn_wendigo_incident_from_completion` in `common/scripted_effects/zombie_special_project_effects.txt`. It creates a dynamic `ZZZ` country and runs `initialize_wendigo_incident_outbreak_country`.

Identity state that must survive the Event 014 merge includes:

- `zombie_outbreak_dynamic_country`
- `weaponized_zombie_outbreak_country`
- `weaponized_zombie_created_by_@ROOT`
- `weaponized_zombie_type_wendigo`
- `weaponized_zombie_archetype_wendigo`
- `weaponized_zombie_attack_other_zombies`
- `weaponized_zombie_independent_outbreak`
- cosmetic tag `ZZZ_weaponized_wendigo`
- the original `ZZZ` identity used by zombie decisions, ideas, AI, unit names, and on-actions

Event 014 must add `cannibalism_wendigo_hannibal_country` only after the public reveal and merge. It must not replace `original_tag = ZZZ`, clear the Wendigo flags, or substitute `CBL` for the live Wendigo country.

## Units and battalions

The true Wendigo battalion is `wendigo_zombies` in `common/units/zombies.txt`. Its current tuning is deliberately distinct from the other zombie battalions and must remain the basis of the merged army.

The live division template is `Wendigo Pack` in both:

- `history/units/ZZZ_weaponized_1936.txt`
- `history/units/ZZZ_weaponized_hardened_1936.txt`

The canonical spawn path is `weaponized_zombie_create_profiled_units`. Wendigo incidents begin from `weaponized_zombies.stage_wendigo_divisions`, gain `weaponized_zombies.wendigo_incident_spawn_per_chaos_tier`, and use `weaponized_zombies.wendigo_incident_spawn_experience`.

Event 014 must therefore:

1. keep every existing division owned by the Wendigo country;
2. keep the live `Wendigo Pack` template and its existing battalion mix;
3. never call a prune/delete effect that removes `Wendigo Pack`;
4. add further training through the existing template rather than a generic cannibal template;
5. preserve existing unit experience and equipment state;
6. keep the Wendigo counter and text-icon assets already wired to `wendigo_zombies`.

## Recruitment and training AI

`weaponized_zombie_unlock_profiled_template` is the canonical recruitment contract. It:

- locks all division templates;
- prunes profiles that do not match the live zombie type;
- force-allows recruitment only for `Wendigo Pack` when the Wendigo flag is present;
- locks the `Wendigo Pack` design;
- runs `weaponized_zombie_apply_training_ai`.

The merged country must continue to use that contract. Event 014 may increase the rate or size of costed Wendigo training, but it must not unlock ordinary infantry recruitment, replace the template, or remove the zombie AI template priorities.

## Ideas and profile state

The current Wendigo package includes:

- `never_ending_hunger`, added by the incident initializer;
- `weaponized_zombie_wendigo`, applied by `weaponized_zombie_apply_type_idea`;
- any live stage/profile ideas and project consequences already held by the country;
- the existing profile variables for strength, infectiousness, speed, durability, cure resistance, friendliness, stage, and cure interactions.

The initializer sets the five combat/profile attributes to `weaponized_zombies.profile_score_extreme` and friendliness to `weaponized_zombies.profile_friendliness_feral`. These variables and any later changes must remain untouched by Event 014 reset effects.

Event 014 may add cannibal route bonuses, global Larder, anchor-state, countdown, and lock-state modifiers. It must not call `clear_weaponized_zombie_resolution_flags`, `clear_weaponized_zombie_type_flags`, `remove_weaponized_zombie_type_ideas`, or any generic country reset that strips the live zombie package.

## Technology and country state

The live dynamic country carries whatever technologies, templates, equipment, convoys, research state, political state, and country variables its creation path and subsequent campaign produced. The safe preservation rule is structural: transform the existing Wendigo country in place.

The merge must not:

- create a replacement dynamic country;
- copy only a fixed technology list;
- call `set_technology` as a reset;
- reset research slots, stability, war support, convoys, equipment, or politics to base `ZZZ` history values;
- reload an OOB over the live army.

Any Event 014 additions must be additive and must occur after the live country scope has been saved as the merge host.

## Leader and public identity

The current Wendigo leader is produced by `weaponized_zombie_refresh_country_leader`, which sets:

- portrait `GFX_portrait_ZZZ_weaponized_wendigo`;
- name `weaponized_zombie_leader_name_wendigo_pack`.

Event 014 may replace the visible leader with the publicly revealed Hannibal Lecter only after `cannibalism_reveal_complete`. The transformed portrait must be a real frame animation package with separate source frames, static fallback, sheet DDS, preview GIF, manifest, and GFX handoff. Before reveal, no Event 014 portrait, name, tooltip, GUI, event, focus, decision, achievement, scenario, or audio metadata may identify him.

## Existing cross-system surfaces

The following existing systems identify or depend on the live Wendigo and must remain compatible:

- `common/scripted_triggers/chaosx_dynamic_triggers.txt`
- `common/scripted_triggers/chaosx_triggerable_scenarios_triggers.txt`
- `common/scripted_localisation/zombie_weaponized_scripted_localisation.txt`
- `common/scripted_effects/zombie_special_project_effects.txt`
- `common/decisions/002_zombie_outbreak_decisions.txt`
- `common/on_actions/002_zombie_outbreak_on_actions.txt`
- `common/ai_templates/templates_ZZZ.txt`
- `common/ai_strategy/ZZZ.txt`
- `common/units/names_divisions/ZZZ_names_divisions.txt`
- the zombie cure/global-context event targets created by `weaponized_zombie_save_global_context_targets`
- the existing Wendigo world-end readiness and super-event system

Event 014's own terminal branch must use distinct flags and super-event/audio ids while leaving these generic zombie checks valid.

## Cultural-content boundary

The Event 014 Wendigo branch will treat the repository's existing creature as fictional body-horror content. It will make no claims about living Indigenous traditions, will not name or imitate ceremonies, and will not introduce borrowed sacred motifs. Visual direction must remain invented military/body-horror imagery tied to the fictional campaign state.

## Implementation proof required later

Before the Wendigo merge can be considered complete, a country-package audit must prove all of the following in current gameplay files:

- the existing country, not a replacement, is the merge host;
- human control is preserved whichever eligible host the player controls;
- existing units, `Wendigo Pack`, technologies, ideas, zombie flags, profile variables, recruitment, and AI survive;
- Event 014 adds more Wendigo training without free ordinary recruitment;
- anchor states and countdown have pre-lock counterplay;
- the locked form is gated and effectively undefeatable;
- both generic zombie and Event 014 cleanup/world-end paths remain coherent;
- no pre-reveal surface exposes Hannibal.
