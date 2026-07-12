# Event 014 Wendigo Preservation and Merge Audit

## Audit status

- Mode: read-only preservation audit.
- Gameplay, map, localisation, asset, and preservation-map files were not edited.
- This handoff is the only file produced by the audit.
- No commit was created.
- Live repository state was inspected alongside Event 014 Part 8 and `014_wendigo_preservation_map.md`.

## Executive finding

The only safe Event 014 Wendigo merge is an in-place transformation of the already-live dynamic Wendigo country. The Wendigo country must be the structural survivor even when the player began in a cannibal host. Player control can be moved into that survivor with `change_tag_from` before the cannibal countries are annexed with `transfer_troops = yes`.

This invariant is necessary because annexation transfers territory and, when requested, troops; it does not transfer the annexed country's country flags, variables, ideas, technologies, cosmetic identity, template locks, AI strategies, global/event-target relationships, or other country-scoped state. Annexing the Wendigo into `CBL` would therefore discard exactly the state that Part 8 requires Event 014 to retain.

Four blockers must be addressed in the implementation tranche:

1. The generic Event 2 Wendigo world-end event, `chaosx.nr2.11`, remains eligible after the Event 014 merge and can set `world_end` through its old 85-percent-continent rule. It must exclude the Event 014 pending and merged routes.
2. Existing zombie cure/global-context event targets are not a persistent Wendigo identity. Event 014 needs its own saved Wendigo-host event target.
3. The live Wendigo country has a country-wide division-template lock. `Wendigo Pack` is recruitable only because it is force-allowed. Event 014 must preserve that state and must not assume ordinary templates become trainable after annexation.
4. Generic zombie on-actions continue to treat the transformed country as a zombie. They currently run autonomous expansion, state population decay, core creation, world-threat logic, and destructive capitulation cleanup. Event 014 must explicitly decide which of those contracts remain active and exclude the merged route from incompatible cleanup.

## Reference basis

The audit used the required offline wiki snapshot, including Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Country creation, National focus modding, Unit modding, Division modding, Technology modding, and Portrait modding.

The relevant official vanilla documentation was also checked, especially:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/script_concept_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_strategy/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/ai_templates/_documentation.md`
- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/script_constants/documentation.md`

The authoritative player-preservation precedent is:

- `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/events/LaR_France.txt`, lines 3995-4003.

That event checks that the annexed `FROM` country is human and the surviving current country is AI, calls `change_tag_from = FROM`, and only then calls `annex_country = { target = FROM transfer_troops = yes }`. Official effects documentation describes `change_tag_from` as changing the player to the current country. The offline Effects page is more explicit: `ABC = { change_tag_from = XYZ }` moves the player controlling `XYZ` into `ABC`, and the effect does nothing when `XYZ` is AI.

## Reachable live Wendigo creation routes

The preservation map describes the special-project completion incident as the canonical path, but it is not the only reachable live path.

### Route A: catastrophic special-project completion

Relevant chain:

1. `complete_weaponized_zombie_project`
2. `weaponized_zombie_check_completion_wendigo_failure`
3. `chaosx.weaponized_zombies.8`
4. `spawn_wendigo_incident_from_completion`
5. `initialize_wendigo_incident_outbreak_country`

Files:

- `common/scripted_effects/zombie_special_project_effects.txt`
- `events/zombie_weaponized_special_projects.txt`, event 8 at lines 334-355

The failure requires no latched global Wendigo flag, demonic or necrotic nature, dead or transformed life state, and at least four mutation extremes. Completion saves a target state, latches `weaponized_zombie_wendigo_exists`, and fires event 8. Event 8 immediately creates the dynamic country.

This route uses:

```text
create_dynamic_country = {
    original_tag = ZZZ
    copy_tag = ZZZ
    ...
}
```

The new country receives a transferred/core capital state, the normal weaponized OOB, the locked profile template contract, additional spawned packs, the original Wendigo super-event, and the latest global cure-context pointers.

### Route B: triggerable-scenario Wendigo profile

Relevant chain:

1. a selected or maximum-intensity triggerable zombie profile sets `triggerable_zombie_profile_type` to `constant:triggerable_scenario_zombie_type.single_wendigo` (`10`);
2. `triggerable_scenario_spawn_profiled_zombie_outbreak` creates a dynamic `ZZZ` country;
3. `triggerable_scenario_apply_zombie_profile_to_current_country` applies the Wendigo profile.

File:

- `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt`, especially lines 952-1177, 1315-1355, and 1758-1792.

This route is reachable through the random profile selector at low weight and is forced by the maximum-intensity connected/random setup when no latched Wendigo flag exists. It produces a valid live Wendigo with a materially different flag and variable package from Route A.

Unlike Route A, the triggerable spawn function does not call `trigger_wendigo_super_event` or save the weaponized cure-context targets. A Route B host can therefore be fully valid without the old Wendigo achievement/audio having fired and without any cure-target pointer to itself.

### Latent but not currently reachable creator-deployment support

`weaponized_zombie_copy_profile_to_outbreak`, the major deployment effect, and the unit creation effect contain branches that can copy or spawn a creator-side Wendigo profile. However, `weaponized_zombie_roll_wendigo_override` is defined but has no call site. The normal profile resolver does not currently call it. The currently reachable creator route to a Wendigo is therefore the catastrophic completion route, not a successful deployed-Wendigo profile.

This latent support still matters for future-proofing: structural in-place preservation automatically handles any later route that creates a country with the canonical live flags.

## Exact live-country identity ledger

### State common to both reachable routes

The following is the dependable live identity and must remain on the structural survivor:

| Identifier/state | Meaning | Preservation rule |
|---|---|---|
| `original_tag = ZZZ` | Dynamic-country ancestry used by ideas, focus selection, AI, unit names, zombie classification, and on-actions | Must remain `ZZZ`; do not replace the country with `CBL` |
| `zombie_outbreak_dynamic_country` | Dynamic zombie classification | Keep |
| `weaponized_zombie_outbreak_country` | Live weaponized-profile classification and cure target eligibility | Keep |
| `weaponized_zombie_independent_outbreak` | Prevents canonical standard-zombie absorption logic and marks independent behavior | Keep |
| `weaponized_zombie_type_wendigo` | Type identity, template pruning, unit creation, decisions, scripted localisation, Event 2 | Keep |
| `weaponized_zombie_archetype_wendigo` | Archetype identity and Event 014 host test | Keep |
| `ZZZ_weaponized_wendigo` cosmetic | Current pre-transformation presentation | Keep through the reveal; see the cosmetic correction below |
| neutrality at 100 and no elections | Current political state at creation | Preserve actual live state; Event 014 changes must be additive and reveal-gated |
| `never_ending_hunger` | Base zombie country package | Keep |
| `weaponized_zombie_wendigo` | Wendigo type spirit | Keep |

`cannibalism_wendigo_hannibal_country` must be additive. It must never replace the two weaponized type/archetype flags or the `original_tag` contract.

### Route A-only or Route A-default state

Route A adds:

- targeted creator flag `weaponized_zombie_created_by_@ROOT` (the concrete flag is creator-tag-specific);
- `weaponized_zombie_attack_other_zombies`;
- numeric country flag `zombie_current_tier` with value `3`;
- numeric country flag `zombie_target_tier` with value `3`;
- 3,000 `infantry_equipment` in the initial stockpile;
- fixed profile variables listed below.

Route A does **not** set a nature flag, a life-state flag, `weaponized_zombie_creator_cure_days`, `weaponized_zombie_outbreak_stage`, `weaponized_zombie_profile_hardened`, `weaponized_zombie_profile_public`, `weaponized_zombie_triggerable_scenario`, or hidden profile-strength ideas.

Consequently, `weaponized_zombie_created_by_@ROOT`, `weaponized_zombie_attack_other_zombies`, and the numeric tier flags must not be made mandatory in Event 014's generic valid-Wendigo trigger.

### Route B-only or Route B-default state

Route B adds:

- `weaponized_zombie_triggerable_scenario`;
- `weaponized_zombie_nature_demonic`;
- `weaponized_zombie_life_transformed`;
- `triggerable_zombie_profile_type = 10`;
- the route's `triggerable_zombie_profile_score`;
- `weaponized_zombie_creator_cure_days = 90`;
- 4,000 `infantry_equipment` in the initial stockpile;
- hidden profile ideas derived from the randomized attribute values.

It clears `events_activated`. It does not add `weaponized_zombie_created_by_@ROOT`, `weaponized_zombie_attack_other_zombies`, or the numeric zombie tier flags.

The OOB selector checks `weaponized_zombie_profile_hardened`, but a newly created triggerable country does not receive that flag and the triggerable initializer never evaluates the hardened thresholds. In the current reachable Route B creation chain the hardened branch therefore does not activate. The check should still be preserved for future compatibility, but the preservation map should not describe a hardened Wendigo as the normal triggerable result.

### Optional live country state that structural preservation must not strip

An in-place merge also safely retains any later or externally applied state, including:

- `weaponized_zombie_profile_hardened`;
- `weaponized_zombie_profile_public`;
- `weaponized_zombie_special_dynamic_outbreak`;
- `weaponized_zombie_friendly_to_creator`;
- `weaponized_zombie_friendly_to_humans`;
- `weaponized_zombie_attack_other_zombies`;
- `weaponized_zombie_targets_zombies_only`;
- any `weaponized_zombie_raid_success_*` flag;
- `weaponized_zombie_counterstrain_exposed` while its timer is live;
- arrays such as `weaponized_zombie_friendly_countries` if future content gives them to the country;
- all country/state campaign variables not enumerated in this handoff.

Do not call `clear_weaponized_zombie_resolution_flags`, `clear_weaponized_zombie_type_flags`, `remove_weaponized_zombie_type_ideas`, or `remove_weaponized_zombie_profile_ideas` on the merge host. `clear_weaponized_zombie_resolution_flags` explicitly clears the Wendigo archetype, the hardened flag, targeting/friendship behavior, and all type flags.

### Generic Event 2 readiness state is not merge identity

The following are temporary readiness flags owned by the old world-end evaluator, not permanent identity:

- `wendigo_world_end_ready`
- `wendigo_world_end_continent_europe`
- `wendigo_world_end_continent_north_america`
- `wendigo_world_end_continent_south_america`
- `wendigo_world_end_continent_australia`
- `wendigo_world_end_continent_africa`
- `wendigo_world_end_continent_asia`
- `wendigo_world_end_continent_middle_east`

An Event 014 merge is incompatible with an already-active `world_end`, `world_end_wendigo`, or `weaponized_zombie_wendigo_world_end` package. Those conditions must block the merge rather than be copied into the alternate route.

## Exact variable ledger

### Route A fixed values

`initialize_wendigo_incident_outbreak_country` creates:

| Variable | Value |
|---|---:|
| `weaponized_zombie_strength` | `4` (`profile_score_extreme`) |
| `weaponized_zombie_infectiousness` | `4` |
| `weaponized_zombie_speed` | `4` |
| `weaponized_zombie_durability` | `4` |
| `weaponized_zombie_cure_resistance` | `4` |
| `weaponized_zombie_friendliness` | `0` (`profile_friendliness_feral`) |

### Route B values

Route B starts each of the five combat/profile values from `triggerable_zombie_profile_score`, independently changes it by -1/0/+1 with 2/6/2 weight, and clamps it to 0-5. It then sets:

- `weaponized_zombie_friendliness = 0`;
- `weaponized_zombie_creator_cure_days = 90`;
- `triggerable_zombie_profile_type = 10`;
- `triggerable_zombie_profile_score` to the selected scenario score.

### Correction to the preservation map's stage wording

Neither reachable initializer sets `weaponized_zombie_outbreak_stage` on the live Wendigo. Route A uses numeric tier flags; Route B has neither those tier flags nor an outbreak-stage variable. Event 014 should preserve an outbreak-stage variable if one exists in a future or modified live country, but must not assume it is part of the current Wendigo baseline and must not synthesize it as a preservation repair.

The safest rule remains structural: copy Event 014 values into the live country; never reset or reconstruct its zombie variables from a fixed list.

## Units, OOBs, and recruitment contract

### Battalion identifier and current tuning

The true subunit is `wendigo_zombies` in `common/units/zombies.txt`, lines 497-547.

Current material properties are:

- abbreviation `WND`;
- infantry sprite, armored map icon category;
- priority `6008`, AI priority `100000`, `active = no`;
- infantry type/group;
- front-line, light-infantry, all-infantry, and army categories;
- combat width `1`;
- maximum strength `10`;
- organization `28`, morale `0.2`;
- speed `0.90`, reliability `1.00`;
- manpower `2,500` per battalion;
- soft attack `1.90`, hard attack `2.40`, breakthrough `3.20`, defence `1.85`;
- armor `18`, hardness `0.65`;
- air attack `-1`, entrenchment `0`, casualty trickleback `-0.5`, initiative `1.25`;
- training time `1`, suppression `0`, weight `0.55`, supply consumption `0.016`;
- equipment need `infantry_equipment = 1`.

### Division template

The live template is exactly `Wendigo Pack` in both:

- `history/units/ZZZ_weaponized_1936.txt`, lines 180-203;
- `history/units/ZZZ_weaponized_hardened_1936.txt`, lines 180-203.

It has:

- division-name group `ZZZ_INF_01`;
- role `zombies`;
- priority `2`;
- sixteen `wendigo_zombies` battalions in a 4-by-4 layout.

At current tuning this is 16 combat width and 40,000 manpower before equipment and modifiers. The Wendigo template is identical in the normal and hardened OOB files; only other zombie profiles differ between those files. Both OOB files contain templates, not starting divisions.

### Spawn counts and experience

Route A starts from `stage_wendigo_divisions = 8` and adds five packs for each current chaos tier. The resulting intended counts are 8/13/18/23/28/33 at tiers 0/1/2/3/4/5+.

The preservation map says the pack creation uses `wendigo_incident_spawn_experience`. The calculator does set `weaponized_zombie_spawn_experience = 0.75`, but the Wendigo branch of `weaponized_zombie_create_profiled_units` does not consume that temporary variable. It hardcodes `start_experience_factor = 0.75` in the generated division string at lines 2806-2813. This is currently equivalent in value but not equivalent in implementation; changing the constant would not change spawned Wendigo experience.

Route B uses its triggerable scenario spawn-count value, then enters the same hardcoded 0.75 Wendigo unit branch.

### Lock and force-recruit rules

`weaponized_zombie_unlock_profiled_template` is the live contract:

1. `country_lock_all_division_template = yes` prevents training, disbanding, and editing at country level;
2. `weaponized_zombie_prune_profiled_templates` deletes every nonmatching weaponized profile template **and every unit using it**;
3. `weaponized_zombie_apply_training_ai` adds generic zombie-role strategies;
4. the Wendigo branch force-allows `Wendigo Pack` recruitment;
5. the Wendigo template itself is locked against editing/deletion.

Consequences for Event 014:

- Never clear `weaponized_zombie_type_wendigo` before any call to the prune helper. If the flag is absent, `delete_unit_template_and_units = { division_template = "Wendigo Pack" }` destroys the template and every live pack.
- Do not reload either OOB during the merge. `load_oob` acts immediately and the live country already owns its evolved template and army state.
- Do not call `country_lock_all_division_template = no`; that would enable ordinary training/disbanding/editing and break the monster-country contract.
- Do not re-run the entire unlock helper merely to "preserve" recruitment. Structural survival already preserves the country lock, force-allow, and template lock. Re-running it can add duplicate AI strategies and will prune other weaponized profile templates.
- If Event 014 needs a repair step, verify `has_template = "Wendigo Pack"`, then apply only the narrow force-allow and template-lock effects while the Wendigo type flag is intact.
- Existing Event 014 special templates are deliberately locked and force-disallowed, and their units are created through scripted effects. That approach is compatible with the country-wide Wendigo lock. It does not require unlocking generic infantry.
- `annex_country` with `transfer_troops = yes` is necessary to retain cannibal divisions and avoid their equipment being lost, but Event 014 should explicitly create/retain its named special templates on the surviving Wendigo scope rather than assume country-scoped recruitment settings transfer from an annexed actor.

### No existing Wendigo recruitment decision

There is no Wendigo-specific unit recruitment decision in the live repository. Wendigo recruitment is the force-allowed `Wendigo Pack` template plus scripted `create_unit` at outbreak creation. The two Wendigo-named decisions are profile review and counterstrain research, not recruitment.

Part 8's wording about retaining every existing recruitment decision should therefore be implemented as preserving the template/recruitment lock contract; there is no hidden Wendigo decision family to copy.

## Ideas and modifiers

### Always-live baseline ideas

`never_ending_hunger` is added by both reachable initializers. Its current package includes surrender limit 1, very high desired-division/aggression/mobilization values, isolation from normal diplomacy and trade, equipment capture, disabled ideas, and severe civilian/industry/experience penalties. Event 014 must preserve it unless a separately approved design explicitly replaces each behavior. Removing it would change diplomacy, surrender, AI, economy, and nonhuman country identity at once.

`weaponized_zombie_wendigo` is the type idea applied by both initializers. Its current values include:

- supply consumption factor `-0.90`;
- conscription `0.10`;
- defence `0.30`;
- army attack `0.45`;
- breakthrough `0.25`;
- attack speed `1.00`;
- no-supply grace `400`;
- out-of-supply factor `0.90`;
- land night attack `2.00`;
- attrition `-1.00`;
- army speed `0.35`.

### Conditional profile ideas

Route A sets all five profile variables to 4 but does not call `weaponized_zombie_apply_profile_ideas`. It therefore does not normally hold the hidden profile-strength ideas despite those extreme variables.

Route B does call the profile-idea effect and can hold one idea from each applicable pair:

- `weaponized_zombie_profile_strength_medium` / `weaponized_zombie_profile_strength_strong`
- `weaponized_zombie_profile_infectiousness_medium` / `weaponized_zombie_profile_infectiousness_strong`
- `weaponized_zombie_profile_speed_medium` / `weaponized_zombie_profile_speed_strong`
- `weaponized_zombie_profile_durability_medium` / `weaponized_zombie_profile_durability_strong`
- `weaponized_zombie_profile_cure_resistance_medium` / `weaponized_zombie_profile_cure_resistance_strong`

Do not normalize the two variants by applying or removing those ideas during the merge. Preserve the live idea set exactly.

### Counterstrain and old terminal idea

`weaponized_zombie_counterstrain_exposed` is a 240-day live debuff applied by outside researchers. It reduces attack, defence, organization, strength, speed, and night combat. Preserve an active timer through the merge. Before lock it is valid counterplay; after Event 014 terminal lock it conflicts with Part 8's impossible-to-defeat requirement and must be explicitly gated or neutralized by the approved terminal package.

`weaponized_zombie_wendigo_world_end` belongs only to generic Event 2. If it is present, the old world-end has already fired and Event 014's alternate merge must not proceed.

## Technologies, equipment, and country state

The dynamic country is created with `original_tag = ZZZ` and `copy_tag = ZZZ`. The base `ZZZ` history grants:

- zero research slots;
- stability and war support at 1.0;
- 1,000 convoys;
- `infantry_weapons`;
- `infantry_weapons1`;
- recruited character `ZZZ_leader`;
- neutrality politics.

The live country may subsequently own additional technologies, equipment, convoys, research state, political state, templates, stockpile, units, generals, wars, cores, and variables. Those must be preserved structurally, not reconstructed.

There is no Wendigo-specific technology. `zombie_disease_bomb_delivery_systems` is the special-project equipment-enabling technology, but the catastrophic Wendigo failure branch skips the successful completion bonuses that grant it to the creator. It is not a baseline Wendigo technology. Event 014 must not add it under the label of preservation.

There is also no Wendigo-specific focus tree. The country selects the blank `ZZZ_focus` by `original_tag = ZZZ`. Event 014's alternate focus/overlay must be loaded explicitly after reveal. The current 108-focus unified tree is restricted to `tag = CBL` and explicitly excludes `cannibalism_wendigo_hannibal_country`; it is not the alternate tree.

Forbidden merge operations remain:

- creating a replacement dynamic country;
- annexing the Wendigo into `CBL` or a warlord;
- a fixed `set_technology` copy/reset;
- `load_oob`;
- resetting research slots, convoys, stability, war support, politics, stockpile, or equipment;
- deleting or converting existing divisions;
- invoking generic Event 014 country cleanup on the Wendigo host.

## AI contract and conflicts

### Static country AI strategy

`common/ai_strategy/ZZZ.txt` defines `ZZZ_unit_production`. It is enabled only while `has_zombie_outbreak` is set, the zombie system is not disabled, and the country is original/dynamic `ZZZ`.

It applies:

- immediate equipment use;
- ignored army incompetence;
- minimal garrison and maximum spare-unit use;
- global area priorities and force concentration;
- high desired-division and force-build-armies factors;
- zombie role/template preference;
- heavy penalties to infantry, cavalry, motorized, mechanized, armor, garrison, and special-force roles.

The file contains both `template_prio id = zombies value = 2500` and a later `template_prio id = zombies value = -1000`. The current static net is therefore not a clean single +2500 contract.

### Dynamic training strategies

`weaponized_zombie_apply_training_ai` adds another `template_prio id = zombies value = 2500`, `role_ratio id = zombies value = 1`, and -1000 values for ordinary land roles/templates. These strategies are applied at outbreak creation and are not gated by the global zombie-system enable block in the same way as the static plan.

### AI template definition

`common/ai_templates/templates_ZZZ.txt` does not target `wendigo_zombies`. Its target template is sixteen base `zombies` battalions under role `zombies`. It also has neither `available_for` nor `blocked_for`. Official AI-template documentation states that using neither or both has undefined behavior.

Therefore the preservation map's phrase "type-specific AI template priorities" is inaccurate. The current live contract is generic zombie-role priority plus a locked/force-allowed Wendigo template. Event 014 should preserve those strategies but must not rely on them as a complete Wendigo-Hannibal AI package.

The existing zombie AI also penalizes the infantry, cavalry, motorized, marine, and other roles used by Event 014's ordinary special units. If the alternate route expects AI use of those units, it needs explicit alternate-route AI strategies or effect-driven reinforcement decisions that outweigh/avoid the generic penalties. This is an additive compatibility layer, not a reason to erase the zombie AI.

### Division names

The template's group is `ZZZ_INF_01` in `common/units/names_divisions/ZZZ_names_divisions.txt`. Its `can_use` accepts `tag = ZZZ`, `original_tag = ZZZ`, or the dynamic-country flag. It remains valid after an in-place Event 014 transformation.

## Decisions and cure interactions

### Profile review

`review_weaponized_zombie_wendigo_outbreak_profile` requires a live weaponized W, the creator-targeted flag, and profile visibility. `is_reviewable_weaponized_zombie_profile_country` excludes triggerable-scenario and special-dynamic outbreaks.

Thus:

- Route A remains reviewable by its creator if its targeted flag is preserved;
- Route B is intentionally not reviewable through this decision;
- Event 014 must not add a fake creator flag to Route B.

### Counterstrain

`develop_weaponized_zombie_wendigo_counterstrain` is globally visible while any live weaponized W exists. It costs 45, lasts 55 days, contributes 34 progress, and at more than 99 progress applies `weaponized_zombie_counterstrain_exposed` to **every** live Wendigo for 240 days. It can repeat.

This remains valid pre-lock counterplay. At terminal lock, its visibility/application loops need an Event 014 terminal exclusion if the final country is truly meant to be undefeatable. Merely keeping the type flag without gating the loop allows ordinary countries to continue applying the large debuff after the Event 014 world-end.

## Event targets and globals

### Spawn-chain regular event targets

Route A uses regular chain targets:

- `weaponized_zombie_creator`
- `weaponized_zombie_new_country`
- `weaponized_zombie_target_state`

Regular event targets persist through events fired in the same effect chain, then clear automatically. They cannot be used to find the Wendigo at a much later Hannibal unification.

Route B also uses short-lived `triggerable_zombie_new_country`, `weaponized_zombie_new_country`, and relation targets during creation/expansion.

### Existing global targets are not a Wendigo host pointer

`weaponized_zombie_save_global_context_targets` saves:

- `weaponized_zombie_cure_target_creator`
- `weaponized_zombie_cure_target_outbreak`

These are singleton latest-context pointers. Every later weaponized deployment can overwrite them. Route B does not call this helper. They can therefore be stale, point to another profile, or be absent for a valid triggerable Wendigo.

`wendigo_super_event_creator` points to the creator/origin used by super-event localisation, not the live Wendigo country. It must not be used as the merge host.

### Other global state

- `weaponized_zombie_wendigo_exists` is latched by both reachable creation routes and is never cleared in current code. It can remain set after the country is dead. It is a spawn uniqueness latch, not proof of a live host.
- `achievement_the_wendigo_rises` is a historical global achievement flag.
- `global.weaponized_zombie_wendigo_counterstrain` and `weaponized_zombie_wendigo_counterstrain_ready` are global/shared research state, not country identity.
- `outbreak_state` in triggerable scenarios is a state target, not the Wendigo country.

Other Wendigo-named state belongs outside the live host and must not be copied onto it as a repair:

- `weaponized_zombie_completion_wendigo_failure` is a creator-side completion flag;
- `achievement_containment_was_temporary` is set on the creator by the catastrophic-completion event option;
- the non-shared `weaponized_zombie_wendigo_counterstrain` variable and `weaponized_zombie_wendigo_counterstrain_ready` country flag belong to the researching country, not the outbreak;
- `world_end_wendigo` is the old Event 2 terminal global and is incompatible with an Event 014 merge.

### Required Event 014 target

Event 014 should save the selected live host under its own identifier, for example:

```text
cannibalism_wendigo_merge_host
```

If the entire merge is one immediate effect chain, a regular target is sufficient. If the target must survive delayed reveal, countdown, decisions, missions, or later cleanup, use `save_global_event_target_as` and explicitly clear it in abort, defeat, ordinary-route selection, and terminal cleanup. Never overwrite or repurpose the zombie cure targets.

## Exact generic Event 2 race

The old Wendigo world-end is `chaosx.nr2.11` in `events/002_zombie_outbreak.txt`, lines 872-905.

Its trigger at lines 878-885 requires:

- chaos tier numeric global flag 5;
- no `world_end`, `world_end_disabled`, or `zombie_system_disabled`;
- `weaponized_zombie_outbreak_country`;
- `weaponized_zombie_type_wendigo`.

After a five-day MTTH, it calls `evaluate_wendigo_world_end_readiness`. If the country controls at least one state, no more than three states are missing, and at least 85 percent of any supported continent is controlled, it immediately:

- sets `world_end`;
- runs faction cleanup;
- sets `world_end_wendigo`;
- adds `weaponized_zombie_wendigo_world_end`;
- calls `trigger_wendigo_super_event`.

`trigger_wendigo_super_event` uses super-event/audio ID 6, the old `GFX_super_event_wendigo`, old localisation, old origin target, and the generic Wendigo achievement flag. Event 014 reserves ID 53 for its distinct terminal branch.

Preserving the live weaponized/type flags makes the merged country continue to satisfy the old trigger. This bypasses Event 014's chaos-above-1000 rule, anchor system, dynamic countdown, lock gates, terminal flags, image, quote, and audio.

Required exclusions belong directly in the Event 2 trigger at lines 878-885:

```text
NOT = { has_global_flag = cannibalism_wendigo_transformation_pending }
NOT = { has_country_flag = cannibalism_wendigo_hannibal_country }
```

Set the pending global as the first atomic step of alternate unification, before any delayed event or merge work. The merged-country exclusion must remain after pending is cleared. If the final implementation uses a differently named route-active flag, use that exact active flag in addition to the pending guard.

The preservation map's instruction to leave the old Wendigo world-end system generally valid is too broad. Generic zombie classification should remain valid; the old terminal event must not remain valid for the Event 014 merged route.

## On-action and lifecycle conflicts

### State capture and population decay

`on_state_control_changed` identifies the in-place transformed country as a zombie and schedules zombie state decay. The daily zombie branch processes population/degradation while `has_zombie_outbreak` is active and the zombie system is enabled.

Event 014 also has an exact finite population-consumption/Larder ledger. If both systems remain active, the same state can suffer generic zombie deaths and Event 014 consumption as separate transactions. This may be intended supernatural pressure, but Event 014 must not credit generic zombie decay as Larder consumption and must avoid double-counting deaths. If the design wants only Event 014's ledger after convergence, gate generic state decay for `cannibalism_wendigo_hannibal_country`; do not silently leave two ledgers claiming the same losses.

### Weaponized daily behavior

The weaponized daily branch at `common/on_actions/002_zombie_outbreak_on_actions.txt`, lines 133-143, is not gated by `has_zombie_outbreak` or `zombie_system_disabled`. It continues to:

- turn a formerly friendly profile hostile when fighting normal countries;
- resolve canonical-standard neighbor merges;
- call `weaponized_zombie_expand_against_neighbors`.

The original-`ZZZ` daily branch at lines 145-211 calls expansion again while the generic outbreak is active. A live weaponized Wendigo can therefore execute the neighbor-expansion helper twice per day while the generic system is active, and once per day after it is disabled.

The helper can declare annexation wars on adjacent normal countries and, for triggerable scenario zombies, merge same-type neighbors based on division count. Route A's `weaponized_zombie_attack_other_zombies` also allows aggression against zombie neighbors. Event 014 must decide whether this autonomous daily expansion remains part of the route or whether Event 014's own conquest/anchor AI owns expansion. Leaving both active without review can race scripted unification, anchor counterplay, diplomacy, and player war choices.

### Original-`ZZZ` daily behavior

While the generic outbreak system is active, the same branch also:

- refreshes zombie world-threat state;
- participates in continent-rejoin pressure;
- tries to annex neighboring standard dynamic zombie outbreaks into the main outbreak;
- cores every controlled non-core state every day;
- relocates isolated capitals;
- can declare war on the United States to avoid Monroe white-peace behavior.

The independent-outbreak flag prevents the canonical weaponized/standard merge helper from absorbing this Wendigo, but it does not disable the rest of the original-`ZZZ` behavior.

### Weekly and anti-zombie systems

The merged country continues to count as a zombie for strength totals, anti-zombie league formation/pressure, world-threat classification, special-country checks, and nonhuman/civilian-system checks. This is generally desirable and follows Part 8. Event 014 defeat/aftermath must nonetheless prevent the generic zombie-defeat super-event and Event 014 defeat super-event from both claiming the same terminal outcome.

### Capitulation

The generic zombie `on_capitulation` block begins with `original_tag = ZZZ` and immediately removes every core of the capitulated country. A dynamic Wendigo-Hannibal remains original `ZZZ`, so this destructive cleanup will run before Event 014 can choose its specified pre-lock outcomes.

The generic block also participates in main-outbreak shutdown/successor logic, winner state transfers, and `on_zombie_threat_defeated`. Event 014 must exclude `cannibalism_wendigo_hannibal_country` from the generic core-removal/defeat ownership block and route pre-lock defeat through Event 014's anchor/network aftermath. The final locked form is separately world-end-gated.

### Leader refresh

`weaponized_zombie_refresh_country_leader` first runs `refresh_dynamic_zombie_country_leader`, then applies:

- portrait `GFX_portrait_ZZZ_weaponized_wendigo`;
- name `weaponized_zombie_leader_name_wendigo_pack`.

Any later call after Hannibal's revealed transformation will overwrite the transformed leader name and portrait. The current generic daily branches normally avoid refreshing a weaponized dynamic country, but creation/promotion/future helpers can call it. Add an Event 014 transformed-country guard or a final Event 014 override branch so any legitimate refresh leaves revealed Hannibal intact. Do not expose that override before `cannibalism_reveal_complete`.

## Player-safe structural merge contract

### Host selection

The current Event 014 triggers require original `ZZZ`, type Wendigo, archetype Wendigo, a non-capitulated country, and at least one controlled state. They do not require the dynamic/weaponized/independent flags and implement territory only, while Part 8 says meaningful territory **or units**.

The valid-host trigger should be based on the live weaponized identity:

- `exists = yes`;
- `original_tag = ZZZ`;
- `zombie_outbreak_dynamic_country`;
- `weaponized_zombie_outbreak_country`;
- `weaponized_zombie_independent_outbreak`;
- `weaponized_zombie_type_wendigo`;
- `weaponized_zombie_archetype_wendigo`;
- not capitulated;
- the approved meaningful-presence test.

Do not require creator, attack-other-zombies, triggerable-scenario, nature, life, profile-public, tier, or cosmetic flags because those differ by creation route.

The global uniqueness latch is stale-able and is not a host selector. Search live countries and save the exact country scope.

If more than one valid Wendigo somehow exists, do not use an unbounded `random_country`. A deterministic policy is required. Recommended ordering is: human-controlled Wendigo first; otherwise strongest live country by divisions, then controlled states, with a stable tie-break. More than one human Wendigo is an explicit multiplayer conflict, not an AI fallback.

### Required ordering

1. Verify reveal/Evolution III/no-world-end gates.
2. Set `cannibalism_wendigo_transformation_pending` immediately so Event 2 is excluded.
3. Select and save the exact Wendigo structural host.
4. Save the player-controlled cannibal donor, convergence actors, and all Event 014 values/arrays that must be copied before annexation.
5. Resolve player control before annexing any human country.
6. Add Event 014 country flags, variables, ideas, arrays, focus state, anchor state, and AI to the existing Wendigo scope. Do not clear zombie state.
7. Annex each cannibal actor **from the Wendigo scope** with `transfer_troops = yes`.
8. Re-register the Wendigo country as the Event 014 actor and update all Event 014 global arrays/targets that formerly pointed to retired warlords or `CBL`.
9. Ensure the existing `Wendigo Pack` template, lock, and force-allow remain; create Event 014 named templates additively and keep their intended lock/decision behavior.
10. Apply revealed Hannibal name/portrait/cosmetic only after the reveal gate.
11. Start anchors/countdown and clear the pending flag only after the merged-country exclusion and persistent host target are in place.
12. Preserve the Event 014 host target for route decisions/defeat if needed, then explicitly clear it in the matching lifecycle cleanup.

### Player-control cases

#### Wendigo already human

Leave player control on the Wendigo. Annex AI cannibal actors from the Wendigo scope with troop transfer. Do not call `change_tag_from` from an AI donor.

#### Cannibal host human, Wendigo AI

In the saved Wendigo scope, call:

```text
change_tag_from = event_target:cannibalism_player_merge_donor
```

Then annex that donor and the other actors with `transfer_troops = yes`. This mirrors the verified vanilla France/Vichy ordering.

#### Another warlord human

Resolve Event 014's unification choice first, save the selected human donor, then move that player into the Wendigo survivor before the warlord is annexed. Do not run a warlord release/cleanup effect that deletes its units before troop transfer.

#### Multiple human countries in multiplayer

One surviving country cannot preserve separate control seats for two human countries through normal annexation. If both the Wendigo and a cannibal actor are human, or multiple cannibal actors are human, silently annexing any of them violates Part 8. The design needs an explicit multiplayer choice/observer/co-op policy before implementation. This is not safely solvable with a single `change_tag_from` call and must not be hidden as a fallback.

### Data that annexation does not replace

Before annexing cannibal actors, copy/aggregate into the Wendigo host every Event 014 value the alternate route needs, including Larder, authority, route/stage state, terminal progress, victories, actor arrays, warlord-origin state, completed route/focus facts, decision unlocks, leader identity, and any country-scoped progression. Annexation is not a country-variable merge.

Conversely, do not copy Wendigo state into `CBL`; preserving a fixed list cannot capture future technologies, timed ideas, template locks, generals, unit history, state variables, arrays, or event-target relationships.

## Special/nonhuman classification

`is_special_chaos_country` and `is_actual_nonhuman_country` already accept original `ZZZ` and weaponized zombie identities. The latter also checks the Wendigo flags/cosmetic. An in-place transformed country therefore remains special and nonhuman without a new generic-classification branch.

`cannibalism_wendigo_hannibal_country` should still be added for Event 014 route logic. It is an Event 014 subtype marker, not a replacement for shared zombie identity.

## Leader, localisation, and asset inventory

### Existing leader and country presentation

- Character: `ZZZ_leader` in `common/characters/ZZZ.txt`.
- Live Wendigo name key: `weaponized_zombie_leader_name_wendigo_pack` -> "Wendigo Pack".
- Portrait sprite: `GFX_portrait_ZZZ_weaponized_wendigo`.
- Portrait file: `gfx/leaders/002_zombie_outbreak/portrait_ZZZ_weaponized_wendigo.dds`, present, 156x210.
- Cosmetic localisation: `ZZZ_weaponized_wendigo`, `_DEF`, `_ADJ`.
- Full/neutrality flags are present at 82x52, medium at 41x26, and small at 10x7.

`ZZZ_weaponized_wendigo` is a presentation state, not the indispensable structural identity. The preservation map should require it until the public transformation. Part 8 separately requires a bespoke transformed flag. After reveal, a dedicated Event 014 cosmetic is permissible if its flags/localisation are fully wired, while `original_tag = ZZZ` and the Wendigo flags remain intact. Systems that use `original_tag` continue to work; no pre-reveal cosmetic may expose Hannibal.

### Unit assets

- `GFX_unit_wendigo_zombies_icon_medium` -> `gfx/interface/counters/divisions_large/unit_wendigo_zombies_icon.dds`, present, 152x42, two frames.
- `GFX_unit_wendigo_zombies_icon_medium_white` -> `gfx/interface/counters/divisions_small/onmap_unit_wendigo_zombies_icon.dds`, present, 60x12, two frames.
- `GFX_unit_wendigo_zombies_icon_small` -> `gfx/texticons/unit_wendigo_zombies_icon_small.dds`, present, 60x12, two frames.
- Localisation keys `wendigo_zombies` and `wendigo_zombies_desc` are present.

These assets remain tied to `wendigo_zombies` and survive an in-place merge automatically.

### Ideas and old super-event assets

- `never_ending_hunger` uses `GFX_idea_never_ending_hunger`; the 64x64 source is present.
- `weaponized_zombie_wendigo` uses `GFX_idea_zombies_3`; the source is present.
- `weaponized_zombie_wendigo_world_end` uses `GFX_idea_wendigo_ascendancy`; the 64x64 source is present.
- Old super-event sprite `GFX_super_event_wendigo` points to a present 457x328 DDS.
- Old Wendigo audio/music files are present and both last approximately 91.54 seconds.
- Achievement sprites for `002_zombie_outbreak_27_the_wendigo_rises` are present.

Event 014 must not reuse the old world-end image/audio as its ID 53 presentation. Existing files remain historical Event 2 assets.

### Existing Event 014 anchor asset

`GFX_report_event_cannibalism_wendigo_anchor_broken` is registered and its 210x176 DDS exists. That confirms one alternate-route report surface, but it does not substitute for the transformed portrait/frame package, flag set, route icons, or ID 53 super-event package required by Part 8.

## Corrections required in `014_wendigo_preservation_map.md`

The map should be corrected in a later parent-owned documentation edit as follows. This audit intentionally does not edit it.

1. **Lines 11-18, creation/identity:** add the triggerable-scenario route. The special-project incident is canonical lore, not the only reachable country initializer.
2. **Lines 20-30, universal flags:** mark `weaponized_zombie_created_by_@ROOT`, `weaponized_zombie_attack_other_zombies`, and tier flags as Route A-specific. Add the common `weaponized_zombie_outbreak_country`/dynamic/independent/type/archetype contract and the Route B flags/variables separately.
3. **Line 29, cosmetic:** preserve `ZZZ_weaponized_wendigo` through pre-reveal state, but do not make it a permanent structural invariant. Part 8's bespoke transformed flag can replace the visible cosmetic after reveal while original/type/archetype identity remains.
4. **Lines 38-43, OOB/spawn:** record that both OOBs contain the same 16-battalion `Wendigo Pack`; Route A loads normal, and the current Route B hardened check is not reached because the initializer does not set `weaponized_zombie_profile_hardened`.
5. **Line 43, experience:** change "uses `wendigo_incident_spawn_experience`" to "currently hardcodes 0.75 in `weaponized_zombie_create_profiled_units`; the calculator's 0.75 temp is unused by the Wendigo branch."
6. **Lines 54-64, recruitment:** state that the country-wide lock prevents training/disbanding/editing; `Wendigo Pack` is narrowly force-allowed. Re-running the full unlock helper is not required for preservation and can duplicate AI strategies/prune profiles. There is no existing Wendigo recruitment decision.
7. **Lines 66-75, ideas/profile:** distinguish Route A (fixed 4/0 variables, no hidden profile ideas) from Route B (randomized values, nature/life/cure variables, hidden profile ideas). Remove the implication that outbreak stage is always present.
8. **Lines 79-91, technology:** explicitly state that there is no Wendigo-specific technology or focus tree. Baseline copied `ZZZ` tech is `infantry_weapons` and `infantry_weapons1`; disease-bomb delivery technology is not granted to the failed Wendigo.
9. **Lines 93-100, leader:** add the risk that `weaponized_zombie_refresh_country_leader` can overwrite the revealed Hannibal portrait/name unless the transformed country is guarded or overridden.
10. **Lines 102-118, event targets:** replace the implication that cure/global targets identify the Wendigo. They are latest-context singleton pointers, can be overwritten, and are absent from Route B. Require an Event 014-specific saved host target.
11. **Lines 102-118, AI:** replace "type-specific" wording with the exact current contract: generic `zombies` role priorities, a base-zombie AI template, and locked/force-allowed W template. Add the undefined `templates_ZZZ` availability configuration and ordinary-unit role conflicts.
12. **Lines 102-118, Event 2:** explicitly require pending/merged exclusions in `chaosx.nr2.11`. Generic Event 2 terminal logic cannot remain valid for the merged route.
13. **Lines 102-118, on-actions:** add state decay/Larder double-ledger risk, twice-daily expansion while the generic system is active, daily core creation/USA war behavior, and original-`ZZZ` capitulation core deletion.
14. **Lines 124-135, proof:** add triggerable-route merge, Route A merge, player-switch-before-annex, multiple-human handling, counterstrain before/after lock, Event 2 race prevention, generic capitulation exclusion, and technology/template/AI snapshot comparisons.
15. **Global uniqueness:** add that `weaponized_zombie_wendigo_exists` is never cleared and cannot be used as proof of a live host.

## Implementation acceptance checklist

### Structural preservation

- The exact live Wendigo dynamic country survives; no replacement is created.
- `original_tag = ZZZ` remains true.
- Dynamic, weaponized, independent, type, and archetype flags remain.
- Route A's creator/attack/tier state survives when present.
- Route B's triggerable/nature/life/profile/cure state survives when present.
- All pre-existing technologies, ideas, timed ideas, variables, stockpile, convoys, generals, units, templates, template locks, force-allow state, cores, states, wars, and campaign state remain unless Part 8 explicitly transforms them.
- `Wendigo Pack` still has sixteen `wendigo_zombies` battalions.
- Every existing pack retains owner, experience, equipment, organization, name/history, and location to the extent supported by the engine's transfer operation.

### Player control

- Human Route A/Route B Wendigo remains controlled.
- Human `CBL`/selected cannibal host moves to the Wendigo before annexation when W is AI.
- Human non-host warlord receives the same explicit preservation route.
- No human country is silently annexed.
- Multiple-human multiplayer behavior is explicitly designed and tested rather than inferred.

### Cross-system safety

- `chaosx.nr2.11` cannot fire while Event 014 alternate transformation is pending or active.
- Old Event 2 super-event/audio ID 6 and `world_end_wendigo` are not used by Event 014 ID 53.
- Generic zombie capitulation does not delete the merged country's cores before Event 014 defeat logic.
- Counterstrain remains valid before lock and cannot undermine the approved locked terminal form.
- The revealed leader cannot be reverted by the weaponized leader refresh helper.
- Generic state decay and Event 014 consumption have a deliberate non-duplicative accounting policy.
- Generic neighbor expansion and Event 014 conquest/anchor logic do not issue conflicting wars or annexations.
- Zombie world threat/anti-zombie league and Event 014 defeat/aftermath cannot fire duplicate victory packages.

### AI and recruitment

- `Wendigo Pack` remains the only conventionally force-allowed monster template unless an approved design says otherwise.
- Ordinary Event 014 units remain available through their costed scripted systems under the country-wide lock.
- No generic infantry recruitment is opened accidentally.
- AI can use Event 014 reinforcement decisions and the alternate route despite the generic ZZZ role penalties.
- Any dedicated Wendigo AI template uses explicit `available_for` or `blocked_for` and targets `wendigo_zombies`, not base `zombies`.

### Presentation

- No Hannibal name, portrait, flag, focus, decision, event, achievement, audio metadata, or scenario description appears before reveal.
- Existing Wendigo unit icons, idea art, country flag, portrait, localisation, and historical super-event remain valid.
- The post-reveal transformed cosmetic/portrait/frame package is separately wired and does not erase structural W identity.

## Required scenario matrix for the later country-package audit

1. Route A Wendigo, AI W, human cannibal host.
2. Route A Wendigo, human W, AI cannibal actors.
3. Route B triggerable Wendigo, AI W, human cannibal host.
4. Route B triggerable Wendigo, human W.
5. Human non-host warlord chosen for preservation.
6. W and cannibal actors both human in multiplayer.
7. W with active `weaponized_zombie_counterstrain_exposed`.
8. W at chaos tier 5 controlling an Event 2-ready continent when unification begins.
9. W alive after `zombie_system_disabled` to confirm alternate AI/daily behavior.
10. W capitulates before transformation lock.
11. W reaches Event 014 terminal lock and outside counterstrain research completes.
12. No live W exists but the stale global `weaponized_zombie_wendigo_exists` remains set; ordinary Hannibal route must still work.
13. More than one valid W exists through an edge-case setup; deterministic selection and human priority must hold.
14. Before/after snapshots of country flags, variables, ideas/timers, technologies, unit count, template definition, template lock/recruitment, stockpile, convoys, player controller, and relevant global targets.

## Current implementation state at audit time

At the time of this trace, Event 014 has identity/valid-host/world-end triggers and tuning constants for the alternate route, but no completed Wendigo merge effect in `common/scripted_effects/014_cannibalism_country_effects.txt`. The current valid-host triggers are under-specified, the alternate focus overlay is not present, and the generic Event 2/on-action/counterstrain exclusions are not wired.

This is an implementation handoff, not a completion claim. No gameplay simplification or fallback was introduced by this audit.
