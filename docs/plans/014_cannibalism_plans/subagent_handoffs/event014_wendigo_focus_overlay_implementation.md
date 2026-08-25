# Event 014 Wendigo Focus Overlay Implementation Handoff

## Scope and ownership

This bounded patch implements the exact post-reveal focus overlay for the live original-ZZZ Wendigo Hannibal country. It changes only:

- `common/national_focus/014_cannibalism_wendigo_focus.txt`
- `common/scripted_effects/014_cannibalism_wendigo_focus_effects.txt`
- `common/script_constants/014_cannibalism_wendigo_focus_constants.txt`
- `localisation/english/014_cannibalism_l_english.yml`
- `interface/014_cannibalism.gfx`
- `docs/plans/014_cannibalism_plans/subagent_handoffs/event014_wendigo_focus_overlay_implementation.md`

Tree id: `cannibalism_wendigo_focus_tree`

Loader effect: `cannibalism_load_wendigo_focus_overlay`

The implementation preserves parent ownership of the merge effect, transformation pulse, decision implementations, ideas, traits, assets, event logs, event details, spreadsheets, and final package audit. No commit was created.

## References consulted

The implementation was checked against the required offline wiki snapshot pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and National focus modding.

The official game documentation consulted in parallel included:

- `documentation/script_concept_documentation.md`
- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- `common/script_constants/documentation.md`

Vanilla national-focus and sprite precedents were checked for focus selection, AND prerequisites, `available_if_capitulated`, research bonuses, map construction, and shine registrations. The Event 014 Wendigo preservation audit and every Event 014 source-spec file were also read before implementation.

## Engine-field correction

The parent corrected the originally requested capitulation field during implementation. Every focus uses the engine-supported field:

```txt
available_if_capitulated = no
```

The unsupported `unavailable_if_capitulated = yes` form does not appear.

## Exact focus count and identifiers

The tree contains exactly 28 manually authored focuses. Every focus has one title key, one `_desc` key, one `_tt` key, one regular sprite, one shine sprite, one isolated reward effect, one `ai_will_do` block, and `available_if_capitulated = no`.

### Merge trunk: five

1. `ZZZ_wendigo_bind_the_two_hungers`
2. `ZZZ_wendigo_preserve_the_pack`
3. `ZZZ_wendigo_keep_the_larder_ledger`
4. `ZZZ_wendigo_bind_the_warlord_commands`
5. `ZZZ_wendigo_raise_the_first_anchors`

### Winter hunger: five

6. `ZZZ_wendigo_open_the_winter_hunt`
7. `ZZZ_wendigo_freeze_the_supply_corridors`
8. `ZZZ_wendigo_march_through_the_blizzard`
9. `ZZZ_wendigo_count_the_winter_victories`
10. `ZZZ_wendigo_raise_the_winter_network`

### Wendigo recruitment: five

11. `ZZZ_wendigo_drill_the_original_pack`
12. `ZZZ_wendigo_open_the_pack_musters`
13. `ZZZ_wendigo_feed_the_anchor_guardians`
14. `ZZZ_wendigo_expand_the_hunting_packs`
15. `ZZZ_wendigo_army_of_the_frozen_larder`

### Cannibal legacy: five

16. `ZZZ_wendigo_keep_the_cannibal_legions`
17. `ZZZ_wendigo_retain_the_warlord_captains`
18. `ZZZ_wendigo_keep_the_foreign_cells`
19. `ZZZ_wendigo_join_the_larder_routes`
20. `ZZZ_wendigo_all_inheritances_intact`

### Transformation countdown: five

21. `ZZZ_wendigo_link_the_transformation_anchors`
22. `ZZZ_wendigo_mark_the_irreversible_road`
23. `ZZZ_wendigo_accelerate_the_transformation`
24. `ZZZ_wendigo_stabilize_the_anchor_chain`
25. `ZZZ_wendigo_begin_the_countdown`

### Alternate terminal: three

26. `ZZZ_wendigo_designate_the_last_hunt`
27. `ZZZ_wendigo_hunt_every_remaining_capital`
28. `ZZZ_wendigo_the_world_beneath_winter`

## Selection and reveal contract

The focus-tree selector, root `allow_branch`, root `available`, and loader effect require the same live identity:

- `original_tag = ZZZ`
- `is_cannibalism_wendigo_hannibal_country = yes`
- `has_global_flag = cannibalism_reveal_complete`
- `has_country_flag = cannibalism_wendigo_focus_overlay_available`
- `has_character = ZZZ_hannibal_wendigo`
- no active `world_end`

Every other focus descends from the reveal-gated root. No transformed title, description, tooltip, or icon can appear through this tree before public reveal.

## Graph and route contract

The five-node merge trunk converges the preserved Pack and Larder-ledger nodes through two explicit AND prerequisites. The trunk then opens four five-node branches:

- winter hunger
- Wendigo recruitment
- cannibal legacy
- transformation countdown

`ZZZ_wendigo_begin_the_countdown` retains the explicit `ZZZ_wendigo_stabilize_the_anchor_chain` prerequisite and its `available` gate requires the other four completed preparations: `ZZZ_wendigo_accelerate_the_transformation`, `ZZZ_wendigo_raise_the_winter_network`, `ZZZ_wendigo_army_of_the_frozen_larder`, and `ZZZ_wendigo_all_inheritances_intact`. This preserves the five-focus AND gate while keeping the visible convergence column compact. The countdown and three terminal focuses occupy consecutive rows so the visible chain has one-row connectors without changing the gameplay gate.

No mutual exclusions were added. Acceleration and stabilization are both deliberate capabilities of the existing decision system, so the countdown convergence requires both preparation focuses.

## Stable reward flags

The requested flags are set at these exact semantic stages:

| Flag | Focus |
| --- | --- |
| `cannibalism_wendigo_frozen_corridor_open` | `ZZZ_wendigo_freeze_the_supply_corridors` |
| `cannibalism_wendigo_pack_training_open` | `ZZZ_wendigo_open_the_pack_musters` |
| `cannibalism_wendigo_countdown_acceleration_open` | `ZZZ_wendigo_accelerate_the_transformation` |
| `cannibalism_wendigo_countdown_stabilization_open` | `ZZZ_wendigo_stabilize_the_anchor_chain` |
| `cannibalism_wendigo_countdown_route_complete` | `ZZZ_wendigo_begin_the_countdown` |
| `cannibalism_wendigo_terminal_hunt_open` | `ZZZ_wendigo_hunt_every_remaining_capital` |
| `cannibalism_wendigo_terminal_route_complete` | `ZZZ_wendigo_the_world_beneath_winter` |

The terminal-route flag is intentionally reserved for the final focus. This prevents the existing weekly pulse from imposing the terminal lock before all three alternate-terminal focuses are complete.

`ZZZ_wendigo_raise_the_winter_network` calls the existing `cannibalism_advance_wendigo_to_winter_network` helper. Focus effects set only opening and route flags. They do not duplicate any decision complete effect.

## Preservation contract

The overlay does not load an OOB, set or clear technology, replace inherited ordinary-route ideas, recreate the country, replace Hannibal, delete divisions, create free units, or unlock the general template roster. The Winter Network capstone deliberately calls the existing stage helper, which replaces only the conjoined Wendigo stage idea with the established winter-stage idea and adds the established winter command trait.

The retained formation contract remains:

- country-wide division-template lock
- `Wendigo Pack` force-allowed for recruiting
- `Wendigo Pack` template locked against editing
- original sixteen `wendigo_zombies` battalions unchanged

Two preservation effects reassert those existing lock states and add zombie-template AI priority. They do not alter the Pack composition or existing units.

The overlay does not alter inherited Event 014 cells, islands, Larder history, population-loss history, warlord commanders, or technology. The legacy focuses supply additional research, infrastructure, authority, and command rewards around those retained systems.

## Terminal and balance proof

All three terminal focuses use `cannibalism_wendigo_can_start_countdown = yes` in their `available` blocks and also require the country countdown flag. The existing trigger requires:

- global Chaos strictly greater than the configured world-end threshold
- no `world_end`
- no `world_end_disabled`
- a live original-ZZZ Wendigo Hannibal country
- active Winter Network stage
- complete countdown route
- minimum live anchors
- minimum controlled territory
- minimum real consumed population
- minimum Network Reach
- minimum real winter victories
- minimum Unified Authority
- minimum real Larder
- no broken or locked transformation state

No focus sets a world-end flag or calls `cannibalism_complete_wendigo_terminal_lock`. The final focus only sets `cannibalism_wendigo_terminal_route_complete`. The existing transformation pulse remains the sole caller that can impose the lock and world-end state.

The focus overlay does not grant Larder, consumed population, Network Reach, territory, anchors, winter victories, divisions, equipment, or manpower. These gates therefore remain dependent on real gameplay transactions.

Authority tuning was checked against the existing starting value and terminal gate. The mandatory pre-terminal focuses can add at most 20 Unified Authority to the configured starting value of 55, reaching 75. The player still needs at least 5 authority from the inherited Event 014 command systems before any terminal focus becomes available.

The paid Pack cap can rise from 12 to 28. Every additional batch remains subject to the existing anchor selection, real population payment, Larder payment, and batch-count checks. No focus spawns a Pack.

## Localisation and sprite contract

Exactly 84 focus localisation keys were appended:

- 28 titles
- 28 descriptions
- 28 reward tooltips

`localisation/english/014_cannibalism_l_english.yml` remains UTF-8 with BOM. The new prose contains no living Indigenous motifs and does not use `sacred`, `regalia`, or `tribal`.

Exactly 56 sprite registrations were appended to `interface/014_cannibalism.gfx`:

- 28 regular `GFX_goal_<focus>` sprites
- 28 `GFX_goal_<focus>_shine` sprites

Every pair uses the exact same path:

```txt
gfx/interface/goals/014_cannibalism/goal_<focus>.dds
```

Every shine sprite uses:

```txt
effectFile = "gfx/FX/buttonstate.lua"
```

No DDS files or fallback sprites were created. The 28 registered DDS paths are an explicit asset dependency for the parent asset route.

## Required parent integration

The existing merge sets `cannibalism_wendigo_focus_overlay_available` but does not currently execute `load_focus_tree`. A focus tree is not automatically reevaluated when the live Event 2 country transforms at runtime.

The parent must call the guarded loader in the existing merge chain. The safest location is immediately after `cannibalism_create_initial_wendigo_anchors = yes` inside `cannibalism_create_wendigo_unification_from_selected_hosts`:

```txt
event_target:cannibalism_wendigo_merge_host = {
	cannibalism_load_wendigo_focus_overlay = yes
}
```

That point is after the optional player-safe `change_tag_from`, after identity preparation, and after initial anchor creation. The loader uses `keep_completed = no`, which is safe because the preserved Event 2 `ZZZ_focus` tree is blank.

This call belongs to `common/scripted_effects/014_cannibalism_wendigo_effects.txt`, which was outside the granted write boundary and was not edited here. Until the parent adds the call, the overlay is defined and selectable but is not loaded onto an already living runtime Wendigo country.

## Validation evidence

The self-audit confirmed:

- 28 unique focus ids and no duplicate ids elsewhere in `common/national_focus`
- five merge, five winter, five recruitment, five legacy, five countdown, and three terminal focuses
- 28 effect calls resolve to 28 focus-specific reward effects
- 28 explicit `available_if_capitulated = no` fields
- 84 unique localisation keys with complete title, description, and tooltip coverage
- 28 regular and 28 shine sprite definitions with exact paired paths
- all seven requested route flags present at the documented stages
- all three terminal `available` blocks use the full existing countdown gate
- no OOB load, technology reset, world-end mutation, free-unit creation, equipment grant, manpower grant, Larder grant, consumption grant, or Network Reach grant
- balanced braces across every touched script and GFX file
- UTF-8 BOM retained on the localisation file

## Simplifications, omissions, and blockers

No gameplay route, focus, localisation key, tooltip, AI block, requested flag, or sprite registration was simplified or omitted.

Two external completion dependencies remain by design:

1. The parent-owned merge effect must call `cannibalism_load_wendigo_focus_overlay` at the handoff point above.
2. The asset route must supply the 28 registered DDS files. No fallback was used.
