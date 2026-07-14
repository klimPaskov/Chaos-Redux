# Event 016 — Vanilla and Engine Precedent Handoff

Date: 2026-07-14

Route: `chaosx_repo_explorer` read-only precedent and feasibility pass

Implementation ownership: parent agent
Gameplay files changed by this pass: none

## Purpose

This handoff tests the Event 016 design against current HOI4 documentation, vanilla script, approved large-mod precedents, and the existing Chaos Redux framework. It distinguishes documented engine support from exact vanilla precedent and from surfaces that still require a live engine test or a user-approved design decision.

Path aliases used below:

- `$HOI4` = `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`
- `$OWB` = `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/2265420196`
- `$CWIC` = `C:/Program Files (x86)/Steam/steamapps/workshop/content/394360/1458561226`
- `$REPO` = Chaos Redux repository root

No online Paradox wiki pages were used. The required offline wiki snapshot and the official documentation under `$HOI4/documentation` were consulted before repository inspection.

## Executive feasibility verdict

| Event 016 surface | Verdict | Main constraint |
|---|---|---|
| One character serving as scientist and advisor | Confirmed | Exact vanilla characters use both roles on one character token. |
| Adding country-leader status to that same character | Documented and structurally supported | `add_country_leader_role` is additive, but no exact vanilla scientist + advisor + country-leader triple was found. Validate the full triple in game before treating it as proven. |
| Scientist field specializations | Confirmed with hard limits | Only nuclear, naval, air, and land specializations exist. Omitted fields default to level 1. Engine maximum is level 5. |
| Extreme scientist traits | Confirmed modifier surface, unverified extreme balance | Scientist traits affect special projects, breakthroughs, and matching basic research; they are not a substitute for a global country research-speed modifier. No documented numeric cap was found. |
| Custom special projects and rewards | Confirmed | Project completion does not automatically create army templates or units. `complete_special_project` skips normal facility/scientist context unless explicitly provided. |
| Decision-led additive system | Confirmed | Use a decision category, bounded variables, and reusable effects. Do not introduce a daily/weekly/monthly world iteration. |
| Persistent primary-laboratory target | Confirmed | A global event target is appropriate, but every exit path must clear or deliberately replace it. |
| Dynamic MTTH values | Documented and already used by Chaos Redux | Vanilla ships only a documentation example; no live vanilla call site was found. |
| Event-created country with viable territory | Confirmed | A stable Event 016 tag should be predeclared and released/assembled. `create_dynamic_country` is a poor fit for stable `KRG` mappings. |
| Project-derived equipment and divisions | Confirmed as explicit scripting | A project can unlock equipment/subunits; variants, templates, and deployed units still need explicit effects. |
| Conditional focus branches and bypasses | Confirmed | After a branch flag changes, call `mark_focus_tree_layout_dirty = yes`; guard child branches explicitly. |
| Animated leader portrait | Confirmed in approved mod | OWB uses `frameAnimatedSpriteType` as a character's large civilian portrait. |
| Animated advisor tile or scientist panel portrait | Unverified | No vanilla or approved-mod precedent was found for an animated advisor `small` portrait or a native scientist-panel animated portrait. |
| Super-event and audio | Confirmed as scripted-GUI convention | Vanilla has no super-event system. Event 016 must extend the existing Chaos Redux framework rather than inventing or importing another one. |
| Custom mod achievements | Confirmed | Append to the existing Chaos Redux `unique_id` file; `possible` is start-of-campaign eligibility and `happened` carries runtime route conditions. |

## Reference baseline

The required offline wiki pages reviewed were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Task-specific pages reviewed were National focus modding, Country creation, Equipment modding, Division modding, Technology modding, Interface Modding, Scripted GUI Modding, Sound modding, Achievement modding, Graphical asset modding, and Music modding.

Official documentation consulted included:

- `$HOI4/documentation/effects_documentation.md`
- `$HOI4/documentation/triggers_documentation.md`
- `$HOI4/documentation/modifiers_documentation.md`
- `$HOI4/documentation/script_concept_documentation.md`
- `$HOI4/common/script_constants/documentation.md`
- `$HOI4/common/characters/_documentation.md`
- `$HOI4/common/scientist_traits/_documentation.md`
- `$HOI4/common/special_projects/specialization/_documentation.md`
- `$HOI4/common/special_projects/projects/_documentation.md`
- `$HOI4/common/special_projects/prototype_rewards/_documentation.md`
- `$HOI4/common/decisions/_documentation.md`
- `$HOI4/common/on_actions/_documentation.md`
- `$HOI4/common/ai_templates/_documentation.md`
- `$HOI4/common/scripted_guis/_documentation.md`

The `hoi4-mtth` skill governed the MTTH conclusions. The `chaos-redux-super-events` skill governed the super-event/audio recommendation.

## 1. One character as scientist, advisor, and leader

### Official additive role effects

The current official effect documentation provides all three additive role effects:

- `$HOI4/documentation/effects_documentation.md:715-733` — `add_advisor_role`; supported in country or character scope and can use `activate = yes`.
- `$HOI4/documentation/effects_documentation.md:985-1003` — `add_country_leader_role`; supported in country or character scope and supports `promote_leader = yes`.
- `$HOI4/documentation/effects_documentation.md:2101-2119` — `add_scientist_role`; supported in country or character scope and accepts the normal scientist-role body.

The scientist effect has one important limitation: a scientist role created through `add_scientist_role` cannot carry the character-database `visible` trigger. Visibility must therefore be controlled before the role is added, or through the Event 016 decision/event logic rather than inside the dynamically added scientist role.

The corresponding character transfer effect is documented at `$HOI4/documentation/effects_documentation.md:7397-7415`:

```hoi4
my_character = {
	set_nationality = POL
}
```

`set_nationality` transfers the character object; it does not create a second character.

### Exact vanilla multi-role precedents

`$HOI4/common/characters/HUN.txt:1524-1566` defines `HUN_gyorgy_jendrassik` once, then gives that character both a `scientist` block and an `advisor` block. The scientist is an air specialist at level 2; the advisor is an air theorist.

`$HOI4/common/characters/JAP.txt:2346-2395` defines `JAP_yoshitoshi_tokugawa` once with:

- `scientist` at `specialization_air = 2`
- `corps_commander`
- `advisor` in the theorist slot

This is strong evidence that HOI4's character model is additive rather than mutually exclusive.

`$HOI4/common/decisions/BUL.txt:4088-4095` is the closest vanilla transfer-and-rule precedent: `BUL_kimon_georgiev` is moved to `BUZ` with `set_nationality = BUZ`, then receives a country-leader role. `$HOI4/common/scripted_effects/DEN_scripted_effects.txt:4112-4124` also transfers a selected character to Denmark and then promotes the character.

### What was not found

No exact vanilla character with the simultaneous static triple `scientist` + `advisor` + `country_leader` was found. This is not a syntax blocker because each role is additive and documented, but the complete Event 016 triple should be treated as an engine-validation item.

Do not use `AST_jack_piddington` as proof of one dual-role instance. Vanilla creates mutually exclusive DLC-dependent instances there; it is evidence of compatibility design, not of one live character holding both roles.

### Event 016 recommendation

Use one stable character token for the scientist. Add roles to that token as route state changes. Do not create separate scientist, advisor, and leader copies, because duplicated characters will break portrait, trait, achievement, event-target, and transfer consistency.

For a transfer to `KRG` or another owner:

1. resolve and store the current host country;
2. transfer the same character with `set_nationality`;
3. reconcile the role state explicitly after transfer;
4. rebind any owner/laboratory global targets;
5. clear the former host's active-advisor or route state when applicable.

The documentation proves character transfer but does not promise that every active advisor-hiring state survives a nationality transfer cleanly. Event 016 should not rely on implicit preservation.

### DLC boundary

Vanilla frequently gates scientist and special-project content behind `has_dlc = "Gotterdammerung"`. Event 016 needs an explicit design decision about ownership of that DLC. A silent non-DLC substitute would be a fallback and cannot be introduced without user approval.

## 2. Scientist fields, levels, and extreme traits

### Four canonical specialization fields

The complete vanilla specialization registry is `$HOI4/common/special_projects/specialization/specializations.txt`:

```hoi4
specialization_nuclear = { ... }
specialization_naval = { ... }
specialization_air = { ... }
specialization_land = { ... }
```

These are the only four canonical scientist fields. Event 016 should express narrower disciplines through project tags and scientist traits, not invent a fifth scientist specialization unless the engine documentation and all dependent UI are deliberately extended.

### Default level behavior and maximum

`$HOI4/common/characters/_documentation.md:36-40` states that every specialization defaults to level 1 and that `skills` only overrides named fields:

```hoi4
skills = {
	# By default all specialization start with level 1
	# Put here the ones to override
	specialization_token = 2
}
```

Consequences:

- omitting `specialization_naval`, for example, does not make the scientist incapable of naval work; it leaves that field at level 1;
- no vanilla character with an explicit specialization value of 0 was found;
- the engine has a level-0 state, but using explicit zeroes as a hard field lock lacks a vanilla character precedent and should be tested before reliance;
- robust field restrictions should normally be enforced through project eligibility, portfolio flags, traits, decisions, or scripted triggers.

The hard current maximum is level 5. `$HOI4/common/defines/00_defines.lua:4488-4501` gives five level-up thresholds and explicitly comments that maximum level equals the array size. The speed-modifier array contains level entries 0 through 5. Vanilla reward code also guards level gain with `level < 5`, for example `$HOI4/common/special_projects/projects/land_projects.txt:1402-1413`.

`add_scientist_level` is documented at `$HOI4/documentation/effects_documentation.md:2083-2098` and accepts a variable for `level`, but it does not expand the engine maximum. Event 016's tuning should clamp planned skill progression at 5.

### Vanilla scientist trait modifier surface

`$HOI4/common/scientist_traits/00_traits.txt:18-39` defines `scientist_trait_genius` with:

```hoi4
special_project_speed_factor = 0.1
scientist_breakthrough_bonus_factor = 0.05
scientist_research_bonus_factor = 0.05
```

The same file provides more specialized examples at lines 41-65 and project-tag experts at lines 92-200, with tag-specific project speed factors up to 0.15. Its opening documentation comment states that scientist traits apply only to special projects.

Therefore a proposed global `+100% research speed` cannot be represented solely as a scientist trait. Use two surfaces:

- a scientist trait for special-project speed, breakthrough gain, and matching-facility basic-research bonus;
- an advisor trait, country idea, or dynamic modifier using the country-level `research_speed_factor = 1.0` when the global research bonus is meant to be active.

The engine documents the modifier names but no hard numeric cap for custom scientist-trait values was found. Very large values are syntactically possible, not behaviorally proven. They need balance review and task-specific live validation, particularly for prototype/reward iteration speed and breakthrough overflow.

### Recommended role separation

Keep these concepts separate in script and localisation:

- scientist level: one of 0-5 in each of four fields;
- scientist traits: project and breakthrough behavior;
- advisor role trait: country-wide policy/research effect while hired;
- country-leader trait: government-wide effect while ruling;
- portfolio/decision variables: which Event 016 research programs have been pursued.

This avoids the misleading situation where a scientist appears to grant a global bonus even while not serving as an advisor or leader.

## 3. Special projects and rewards

### Strong vanilla project precedent

`$HOI4/common/special_projects/projects/air_projects.txt:1568-1720` defines `sp_air_helicopter`. It demonstrates a full project package:

- `specialization = specialization_air`
- project tags and DLC gating
- breakthrough and resource costs
- prototype and complexity configuration
- `project_output` unlocks `helicopter_equipment_1`, `helicopter_brigade`, and `lc_helipad`
- generic and unique rewards with thresholds, weights, options, and iteration output

`$HOI4/common/special_projects/projects/air_projects.txt:9-108` defines `sp_air_bouncing_bomb` and its backspin-mechanism reward. Its scientist-side effects grant experience while country-side effects add project progress. This is a good model for keeping scientist and owner-country consequences in their correct scopes.

`$HOI4/common/special_projects/projects/land_projects.txt:1296+` defines `sp_land_multi_charge_large_caliber_gun`, including scientist experience guarded below level 5 and a failure branch that damages the facility/infrastructure. It is useful precedent for Event 016 projects that should have visible operational risk rather than guaranteed linear progress.

### `complete_special_project` caveat

Official documentation at `$HOI4/documentation/effects_documentation.md:2896-2914` warns that `complete_special_project`:

- ignores the current project tree and can unlock out of sequence;
- is not completed within a facility by default;
- therefore does not apply facility-state or scientist effects by default;
- can accept explicit `project`, `scientist`, `state`, and `iteration_output` context.

Event 016 should use normal project flow when the facility and scientist are meant to matter. Reserve `complete_special_project` for authored event resolutions where bypassing the normal process is intentional and the required context/reward consequences are applied explicitly.

### Reward architecture recommendation

Each Event 016 project should define:

1. canonical specialization and tags;
2. explicit availability/prerequisite triggers;
3. breakthrough, facility, resource, complexity, and prototype behavior;
4. base output;
5. generic reward pool where appropriate;
6. unique route reward with stable completion flags;
7. scientist-scope and country-scope effects separately;
8. AI desirability and reward selection;
9. achievement/portfolio hooks through stable flags rather than display names.

A project reward may unlock equipment, modules, subunits, or buildings, but it should not be expected to generate a complete division package automatically. Section 8 covers the necessary explicit template and unit effects.

## 4. Decision-led additive systems

### Vanilla structural precedent: Soviet paranoia

The Soviet paranoia system is the clearest vanilla precedent for an additive mechanic driven by decisions and a compact UI:

- `$HOI4/common/decisions/categories/SOV_decision_categories.txt:7-30` defines `SOV_paranoia_system`, associates a scripted GUI, and controls visibility with flags.
- `$HOI4/common/decisions/SOV.txt:133+` defines repeatable decisions with availability, visibility, re-enable timing, and AI behavior.
- `$HOI4/common/scripted_effects/SOV_scripted_effects.txt:149-291` centralizes tiered add/subtract effects and then calls `SOV_paranoia_clamp_and_update_ui_effect` to clamp the value to 0-100 and refresh the UI.

This is the right structural pattern for an Event 016 research portfolio, patronage, instability, secrecy, or ethics meter:

```text
decision category
    -> decisions/missions
        -> reusable scripted effects
            -> bounded state variables
            -> dynamic modifiers/ideas
            -> explicit GUI refresh
```

### Event 016 constraints

- Centralize thresholds, costs, cooldowns, and reward values in subsystem script constants where supported.
- Use flags for boolean route state and variables only for genuinely numeric meters.
- Keep repeated mutations in scripted effects and repeated eligibility in scripted triggers.
- Clamp all player-visible meters after every mutation.
- Give every decision meaningful trigger and effect tooltips, plus AI weights tied to the current route and resources.
- Do not copy Soviet whole-world `on_daily`, `on_weekly`, or `on_monthly` processing. Repository rules prohibit such iteration unless the user explicitly requests it.
- Prefer explicit event/decision callbacks, targeted timed events, missions, or existing narrow on-actions.

## 5. Persistent event targets and cleanup

### Lifetime rules

The offline Data structures wiki and official effects documentation distinguish two target lifetimes:

- `save_event_target_as`: a regular event target persists through the current effect chain and events fired from that chain, then clears automatically;
- `save_global_event_target_as`: persists beyond the chain and must be cleaned explicitly with `clear_global_event_target`;
- event-target localisation omits the `event_target:` prefix, while scripted scope usage includes it.

Official effect entries are at:

- `$HOI4/documentation/effects_documentation.md:6496-6503` — `save_event_target_as`
- `$HOI4/documentation/effects_documentation.md:6505-6512` — `save_global_event_target_as`
- `$HOI4/documentation/effects_documentation.md:2733-2749` — global-target cleanup

### Vanilla persistent-target precedent

`$HOI4/common/decisions/RAJ_GOE.txt` uses a global target for a communist coup target:

- lines 4662-4666 save `RAJ_communist_coup_target`;
- lines 5044-5054, 5117-5126, and 5194-5204 guard later uses with `has_event_target`, `country_exists`, and target-validity checks;
- lines 5214-5223 clear it on success;
- lines 5249-5260 clear it on abandonment.

This is the correct lifecycle model for Event 016's primary laboratory or persistent host country.

### Event 016 cleanup contract

Use a global target only for a pointer that truly must survive across independent decisions/events. Before every use:

```hoi4
has_event_target = event_016_primary_lab
```

Then validate that the pointed state/country still exists and remains appropriate. The cleanup/rebind effect must run on at least:

- laboratory destruction;
- laboratory capture if the design invalidates the original relationship;
- scientist transfer to another host;
- `KRG` formation and any route that moves the laboratory;
- project-system shutdown;
- scientist death/retirement/removal;
- terminal Event 016 outcomes;
- aborted or mutually exclusive route exits.

Do not leave a global target pointing at an invalid state or obsolete host. Do not use `clear_global_event_targets`, which would erase unrelated systems' pointers; clear only the Event 016 token.

If the laboratory pointer needs only one event chain, use a regular target and allow automatic cleanup. Global lifetime should not be the default.

## 6. Dynamic MTTH

### Documented syntax and existing project proof

Vanilla's only direct example is `$HOI4/common/mtth/mtth_variables.txt:2-13`:

```hoi4
example_mtth_value = {
	base = 50
	modifier = {
		add = 25
		has_war = yes
	}
}

set_variable = { my_value = mtth:example_mtth_value }
```

The definition uses `base`, then trigger-controlled `factor` or `add` modifiers. The resulting value is injected through `mtth:<entry>` into `set_variable` or `set_temp_variable`.

No live vanilla gameplay call site for `mtth:<entry>` was found. Chaos Redux already proves the pattern locally:

- `$REPO/common/mtth/chaosx_mtth_variables.txt` defines `zombie_outbreak_chance`;
- `$REPO/common/scripted_effects/002_zombie_outbreak_effects.txt:2378-2385` stores `mtth:zombie_outbreak_chance` in `zombie_outbreak_days`.

### Event 016 recommendation

Use subsystem-scoped MTTH entries when many route, country, project, scientist, or world-state modifiers would otherwise duplicate weight logic. Typical safe uses are:

- event delay values stored in a variable;
- AI decision weights injected through a temporary variable;
- project incident or discovery cadence;
- transfer/defection pressure calculated from several conditions.

Keep the MTTH entry's trigger scope documented and stable. Store its output in a variable before passing it into a dynamic duration or weight surface. Do not mix an MTTH value with ad hoc duplicate modifiers elsewhere, because the effective balance will become opaque.

This surface is documented and already used by Chaos Redux, but the absence of a live vanilla call site should be recorded in validation notes rather than presented as exact vanilla precedent.

## 7. Event-created countries and viable territory

### Engine surfaces

Official country/state effects include:

- `$HOI4/documentation/effects_documentation.md:3033-3044` — `create_dynamic_country`
- `$HOI4/documentation/effects_documentation.md:5724-5731` — `release`
- `$HOI4/documentation/effects_documentation.md:5791-5798` — `release_puppet`
- `$HOI4/documentation/effects_documentation.md:6655-6667` — `set_capital`
- `$HOI4/documentation/effects_documentation.md:7734-7741` — `set_state_owner`
- `$HOI4/documentation/effects_documentation.md:8323-8330` — `transfer_state`
- `$HOI4/documentation/effects_documentation.md:8030-8060` — `start_civil_war`, including explicit `states`, armed-forces ratios, `keep_all_characters`, and `keep_scientists_trigger`

`create_dynamic_country` creates an engine-generated dynamic country based on `original_tag`/`copy_tag` and runs child effects in that country. It is valid engine syntax, but it is not the appropriate primary mechanism when later script, focus, localisation, achievements, AI, and event mappings need a stable tag such as `KRG`.

### Vanilla territory precedents

`$HOI4/common/national_focus/congo.txt:3280-3395` starts a Congolese civil war with:

```hoi4
start_civil_war = {
	ideology = neutrality
	size = 0.1
	army_ratio = 0.1
	navy_ratio = 1
	air_ratio = 0.4
	capital = 295
	states = { 295 888 538 }
	keep_all_characters = yes
	# targeted character transfers and country setup follow
}
```

The same block transfers selected characters, applies a cosmetic tag, defines a division template, and creates units. It is the strongest vanilla precedent for an authored breakaway with specified territory and immediately viable forces.

`$HOI4/events/BBA_Ethiopia.txt:6919-6949` demonstrates `create_dynamic_country`, saving the new country to a variable and transferring core states. Lines 6951-6973 demonstrate the fixed-tag alternative: release `SOM`, transfer two states back, then set politics and popularity.

### Event 016 recommendation: predeclared `KRG`

Because Event 016 already expects stable `KRG` references, implement it as a normal predeclared country package:

- country tag and common country definition;
- history/country setup;
- colours and graphical culture;
- localisation and cosmetic names where required;
- character ownership;
- ideas/modifiers;
- focus tree and AI behavior;
- event-log and event-detail actor mapping;
- achievements and super-event mappings.

At formation/takeover time, assemble its territory with fixed release/transfer effects. The formation effect should:

1. build a deterministic candidate-state set from the accepted Event 016 design;
2. require a minimum viable owned/controlled set before offering or firing formation;
3. transfer the selected states to `KRG`;
4. select a capital that is inside the transferred set;
5. set ownership and control consistently;
6. establish politics, popularity, autonomy/war/diplomatic state, and country flags;
7. transfer the single scientist character and reconcile roles;
8. define project-derived forces only after the country owns the required states;
9. rebind the laboratory target to a valid `KRG` state if that route moves it;
10. mark focus layout dirty after setting route/portfolio flags.

Do not form a country with zero states, a capital outside its territory, or only disconnected/nonviable fragments. The exact viable-state rule is a design choice, not something the engine can infer. If the required territory is unavailable, stop the route or present an explicitly designed alternative; do not silently choose arbitrary states.

### Character and scientist retention during takeover

For civil-war formation, `keep_scientists_trigger` can control which scientists remain with the original country, and effects inside `start_civil_war` can transfer named characters to the revolt. For a fixed release/transfer path, use `set_nationality` on the named Event 016 character after `KRG` exists.

In both cases, do not combine implicit civil-war character assignment and a second unconditional nationality transfer. One effect should own the transfer, with a postcondition that the character has exactly one nationality and the intended role set.

## 8. Project-derived equipment, templates, and units

### Project output can unlock content

The helicopter project at `$HOI4/common/special_projects/projects/air_projects.txt:1568-1720` proves that a special project can unlock an equipment type, subunit, and building. It does not create a division template or deploy a unit.

### Vanilla explicit follow-through

`$HOI4/common/national_focus/italy.txt:4335-4415`, `ITA_italian_tankettes`, checks:

```hoi4
is_special_project_completed = sp:sp_land_flamethrower_tank
```

and then invokes `ITA_add_basic_light_flamethrower_template`. The helper in `$HOI4/common/scripted_effects/ITA_scripted_effects.txt:5470-5513` creates the `L3 Lf` equipment variant with `create_equipment_variant`. This is the exact precedent for a project-dependent authored variant and template package.

`$HOI4/common/national_focus/yugoslavia.txt:1192-1234` releases Macedonia, saves it as an event target, defines a division template, and creates units. Similar blocks exist for Kosovo and Montenegro. This demonstrates the correct sequencing: country exists and owns territory first, then receives a template and deployed forces.

### Event 016 implementation contract

Treat “project-derived forces” as an explicit scripted package:

1. require stable project completion or portfolio flags;
2. enable the equipment/module/subunit where the project itself does not already do so;
3. create a named equipment variant if needed;
4. grant a bounded stockpile amount through a variable-driven effect;
5. define a manually authored division template;
6. create a bounded number of divisions in valid owned states;
7. give the AI a production/template plan for continued use;
8. localise the equipment, variant, template, and tooltips;
9. document/register every icon;
10. update `common/script_enums.txt` if a genuinely new equipment archetype/category is introduced.

No vanilla mechanism turns arbitrary project properties into a generated battalion layout. The template must be authored, balanced, and validated like any other division design. “Derived from the project” should mean gated and thematically constructed from its unlocks, not dynamically synthesized by the engine.

Avoid duplicate templates by guarding the helper with a stable country flag or equivalent trigger. If the scientist transfers with a project portfolio, decide explicitly whether the project completion belongs to the original country, the scientist's new country, or both; HOI4 special-project completion is country state, not character-carried inventory.

## 9. Conditional focus branches and bypass behavior

### Branch visibility precedent

`$HOI4/common/national_focus/argentina.txt:1005-1018`, `ARG_hitler_1`, uses both `available` and `allow_branch` tied to a flag. `$HOI4/events/TOA_Argentina.txt:2440-2442` sets the relevant flag and calls:

```hoi4
mark_focus_tree_layout_dirty = yes
```

The offline National focus modding wiki confirms that `allow_branch` is evaluated when the tree layout is built. When Event 016 sets a portfolio, takeover, or route flag that changes branch layout, it must mark the layout dirty.

### Bypass precedent

`$HOI4/common/national_focus/belgium.txt:1791-1843`, `BEL_poudreries_reunies_de_belgique`, bypasses when a relevant state is lost and uses `bypass_effect` to preserve an effect that should still be applied.

`$HOI4/common/national_focus/indonesia.txt:1494-1505`, `INS_just_a_fisherman`, uses `bypass_if_unavailable = yes`.

### Event 016 recommendation

- Use `allow_branch` for genuine route-level layout gating.
- Set route/portfolio flags before calling `mark_focus_tree_layout_dirty = yes`.
- Guard child branches explicitly; do not assume a hidden parent alone prevents every child from appearing or being selected under all layout states.
- Use `available` for live completion eligibility.
- Use `bypass` when the focus objective is already satisfied or has become impossible in a designed way.
- Use `bypass_effect` only for effects that should still occur when bypassed; it is not a general reward duplication mechanism.
- Give AI focus weights the same route/portfolio gates as the player path.
- Include takeover/transfer branches in the same exclusivity system as ordinary scientist routes so they cannot coexist accidentally after a layout refresh.

## 10. `frameAnimatedSpriteType` on character surfaces

### Vanilla engine syntax

Vanilla uses `frameAnimatedSpriteType` extensively for GUI elements. `$HOI4/interface/alerts.gfx:3-12` provides the canonical structure:

```hoi4
frameAnimatedSpriteType = {
	name = "GFX_green_alert_glow"
	texturefile = "gfx/interface/green_alert_glow.dds"
	noOfFrames = 2
	animation_rate_fps = 0.5
	looping = yes
	play_on_show = yes
}
```

A scan found 162 vanilla `frameAnimatedSpriteType` definitions, but none named or used as a character leader, advisor, or scientist portrait. Vanilla character portrait registrations remain ordinary `spriteType`, including:

- `$HOI4/interface/_scientists_portraits.gfx:245-247` — Jendrassik scientist portrait
- `$HOI4/interface/_scientists_portraits.gfx:343-345` — Tokugawa scientist portrait
- `$HOI4/interface/_leader_portraits.gfx:8955-8957` — Tokugawa leader portrait
- `$HOI4/interface/ideas.gfx:10766-10768` — Tokugawa advisor-small portrait

### Approved-mod proof for large leader portraits

OWB provides a direct working precedent:

- `$OWB/interface/z_fallout_leaders_animated.gfx:299-306` defines `GFX_Portrait_Bad_V_Animated` as 48 frames at 24 fps.
- `$OWB/common/characters/CHC.txt:2-60` assigns that animated sprite to `CHC_v` as `civilian.large`.
- The same character has two country-leader roles, an advisor role, and a field-marshal role.
- Its `civilian.small` advisor portrait remains the static `GFX_idea_CHC_v_bad`.

Additional exact leader-surface examples are:

- `$OWB/interface/z_fallout_leaders_animated.gfx:2-9` and `$OWB/common/characters/VEG.txt:2-14` — `GFX_Portrait_House_animated`, 60 frames at 12 fps, used as `civilian.large` for a country leader;
- `$OWB/interface/z_fallout_leaders_animated.gfx:147-153` and `$OWB/common/characters/TTM.txt:2-21` — animated Diana portrait used for civilian/army large surfaces and a country leader.

### Unsupported surfaces

No approved-mod character was found with an animated `small` portrait while serving as an advisor. No native scientist-panel use of a `frameAnimatedSpriteType` portrait was found. Therefore:

- animated country-leader/civilian-large portrait: verified in an approved mod;
- animated army-large portrait: verified in an approved mod;
- animated custom scripted-GUI image: supported by normal frame-animation syntax;
- animated advisor tile: unverified;
- animated scientist panel: unverified.

Event 016 may safely plan animation for the large leader portrait and any custom scripted GUI. It must not promise native animation in the advisor tile or scientist panel without an engine test. If the intended design requires static art on those two surfaces, that is a simplification/fallback and must be discussed with the user rather than silently accepted.

Animated final assets also fall under `chaos-redux-event-assets` and `chaos-redux-frame-animation`: they need real planned source frames, static surface art, manifest, contact sheet, preview, and `.gfx`/`.gui` handoff. A transform-only still-image loop is not acceptable.

## 11. Super-event and audio precedent

### Vanilla status

Vanilla has no native “super-event” framework. A super-event is a scripted GUI convention combining visibility state, an image/text mapping, a close/cleanup path, and music or sound playback. It is therefore incorrect to claim a vanilla super-event implementation precedent.

### Approved-mod structural precedent

CWIC demonstrates the common architecture:

- `$CWIC/common/scripted_guis/CWIC_super_events.txt:1-13` defines a player-context scripted GUI window whose visibility is controlled by a country flag.
- `$CWIC/common/scripted_effects/CWIC_Super_Event_Scripted_Effects.txt:1-12` iterates human countries, plays a named song, and sets event-specific/general visibility flags.
- `$CWIC/music/super_event_ogg.asset:3-11` registers named OGG tracks and volume.
- `$CWIC/events/Afghanistan_War.txt:323-332` calls a dedicated super-event scripted effect from an event option.

This proves the convention, not the correct Chaos Redux implementation. In particular, Event 016 should not copy CWIC's whole-world iteration because repository rules prohibit adding daily/weekly/monthly world iteration and the local framework already has its own audience/audio logic.

### Chaos Redux framework is authoritative

Event 016 should extend these existing surfaces:

- `$REPO/interface/chaosx_super_events.gui`
- `$REPO/interface/chaosx_super_events.gfx`
- `$REPO/common/scripted_guis/chaosx_scripted_gui_super_events.txt`
- `$REPO/common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`
- `$REPO/music/chaosx_super_event_music.asset`
- `$REPO/music/chaosx_super_event_music.txt`
- `$REPO/sound/chaosx_sound.asset`

`$REPO/events/002_zombie_outbreak.txt:202-207` shows an older local pattern: a timed `super_event_visible` slot, `global.current_super_event_audio_id`, and `play_current_super_event_audio = yes`.

`$REPO/common/scripted_effects/011_secret_alliance_effects.txt:5860-5872` is the stronger current pattern: constants drive visibility duration, the effect sets the audio identity, presents the event, and schedules cleanup. Its lines 5887-5896 contain the paired cleanup behavior.

### Event 016 super-event package

For each Event 016 super-event, reserve and wire:

- unique display slot / visibility identity;
- image sprite and final DDS;
- title, description, quote, attribution, and close-button localisation;
- scripted-localisation image/text mapping;
- unique audio ID;
- final 44.1 kHz OGG asset with all required volume variants;
- music asset registration;
- zero-random-chance music-station registration;
- sound wrapper where used by the framework;
- settings-aware playback helper;
- timed or explicit close cleanup;
- docs and music attribution/source HTML required by the super-event skill;
- world-end/terminal flags only where the outcome is truly terminal.

Do not allocate an audio slot before checking the current registry, and do not reuse an existing numeric ID just because a music entry appears visually vacant.

## 12. Custom achievements

### Vanilla and custom-mod formats

Vanilla achievements in `$HOI4/common/achievements.txt` use Steam achievement IDs. Two useful thematic triggers are:

- `wunderwaffen`, lines 113-129, checks special-project completion;
- `american_prometheus`, lines 6562-6579, checks an Oppenheimer character flag.

These are trigger precedents, not the correct custom-mod file header.

The offline Achievement modding wiki documents custom achievements with:

```hoi4
unique_id = chaos_redux

achievement_token = {
	possible = { ... }
	happened = { ... }
}
```

`possible` is evaluated for campaign eligibility at game start. Runtime Event 016 route, scientist, project, formation, and terminal conditions belong in `happened`.

Official trigger documentation at `$HOI4/documentation/triggers_documentation.md:3471-3483` defines `has_completed_custom_achievement`, including both `mod = <unique_id>` and `achievement = <token>`.

### Existing Chaos Redux registry

`$REPO/common/achievements/chaos_redux_achievements.txt:1-35` already declares the mod's `unique_id`. Event 016 achievements should be appended to this file. Do not create a second `unique_id` registry.

Custom achievement art is filename-driven rather than registered through a `.gfx` sprite. Each achievement needs exactly three DDS files in `gfx/achievements/`:

```text
<achievement>.dds
<achievement>_grey.dds
<achievement>_not_eligible.dds
```

Vanilla's `american_prometheus` triplet is a direct filename precedent.

If the Event 016 specification retains 16 achievements, completion requires:

- 16 achievement blocks in the existing registry;
- 32 English localisation keys (`<ID>_NAME` and `<ID>_DESC`);
- 48 final DDS files;
- stable route/project/formation/terminal flags or variables for `happened`;
- triggers that remain valid if the scientist changes nationality;
- an achievement audit confirming every trigger is attainable and mutually exclusive routes are represented intentionally.

Do not key achievements to transient event targets, temporary variables, GUI state, or player-facing localisation. Use persistent gameplay facts.

## 13. Terminal and takeover sequencing

The highest-risk Event 016 failure mode is a terminal outcome that presents correctly but leaves live decisions, targets, roles, projects, audio, or focus routes behind. Use one reusable terminal-resolution effect per terminal branch and keep its order explicit.

Recommended sequence:

1. guard against a second resolution with a terminal flag;
2. snapshot any actors/values needed for final event, log, or achievement text;
3. set the route-specific terminal flag and the general Event 016 terminal flag;
4. lock or remove Event 016 decisions and missions;
5. cancel/resolve active project timers and incident chains in the designed manner;
6. complete, preserve, or invalidate country project state explicitly;
7. transfer/retire the character and reconcile scientist/advisor/leader roles exactly once;
8. form or transform `KRG` only after its territory viability trigger passes;
9. create project-derived forces after the receiving country exists and owns deployment states;
10. refresh focus layout after all route/takeover flags are final;
11. write event-log/evolution state and fire the terminal event/news event;
12. present the super-event and settings-aware audio;
13. schedule/perform super-event visibility and audio cleanup;
14. clear or deliberately rebind the primary-laboratory and host global event targets;
15. remove transient variables/flags while preserving achievement facts;
16. expose the final stable flags to achievements and post-terminal content.

The final text/event should not be fired before the state it describes exists. Likewise, global targets should not be cleared before any localisation snapshot or log effect that still needs them. Snapshot needed names first, then clean pointers.

For nonterminal takeover, use the same ownership/territory/role/target steps but do not set the general terminal flag or remove future content. The spec must say whether takeover ends the scientist arc or opens a new country-play route.

## 14. Unsupported or uncertain claims that must not enter completion reporting

The following claims are not supported by the evidence found:

1. “Vanilla has a scientist/advisor/country-leader triple.” It does not; only the additive engine effects and partial multi-role examples were found.
2. “Omitting a specialization makes the scientist unable to work in it.” Omitted fields default to level 1.
3. “A scientist trait grants global research speed.” Scientist traits are scoped to the special-project system; global research speed belongs on a country-applied surface.
4. “A project completed by effect behaves exactly like normal facility completion.” The documentation explicitly says it does not unless the missing context/consequences are supplied.
5. “A project unlock automatically creates its derived division.” It does not.
6. “`create_dynamic_country` is suitable for stable `KRG` focus/event mappings.” It creates a dynamic tag; use a predeclared fixed tag for this design.
7. “Vanilla gameplay proves `mtth:<entry>`.” Vanilla provides documentation, while Chaos Redux provides the live local precedent.
8. “Vanilla proves animated character portraits.” It does not. Approved OWB proves animated large leader portraits.
9. “Animated advisor and scientist portrait surfaces are verified.” They are not.
10. “Vanilla has a super-event system.” It does not; Chaos Redux has a custom framework.
11. “Achievement `possible` can be used for a route chosen mid-campaign.” It is start-of-campaign eligibility; use `happened` for runtime state.
12. “A transferred character's active advisor status is guaranteed to migrate.” The transfer effect is documented, but that active-role state guarantee was not found.

## 15. Parent implementation checklist

Before claiming Event 016 complete, the parent implementation should prove:

- one stable character token exists and every route refers to it;
- all four scientist fields are deliberately initialized, with no planned value above 5;
- field restrictions do not rely on omission;
- scientist, advisor, and country-leader modifier responsibilities are separated;
- transfer paths reconcile roles and active-hiring state;
- every real project has valid prerequisites, facility/scientist behavior, rewards, AI, and stable completion facts;
- any forced project completion deliberately reproduces or omits facility/scientist consequences;
- decision variables are centralized, bounded, and refreshed through reusable effects;
- no new daily/weekly/monthly world iteration was introduced;
- every global target use is guarded and every exit path clears/rebinds it;
- MTTH scope and output variables are documented;
- `KRG` is a complete fixed-tag country package with a viable territory rule;
- project-derived equipment, variants, templates, stockpiles, units, and AI production are all explicit;
- conditional focus branches refresh their layout and all children share route gates;
- large portrait/custom-GUI animation is wired from real frames;
- any static advisor/scientist portrait compromise has explicit user approval;
- every super-event slot, text mapping, image, audio variant, station entry, wrapper, and cleanup path exists;
- all 16 specified achievements have attainable triggers, 32 localisation keys, and 48 DDS files;
- terminal effects clean decisions, projects, targets, audio, GUI state, and transient flags without erasing achievement facts;
- event log, evolutions, event-details UI, docs, and spreadsheet wording match the final in-game localisation.

## Conclusion

The core Event 016 design is technically feasible, including one transferable character, multi-role progression, genuine special projects, a decision-led portfolio, a fixed-tag takeover country, project-gated forces, conditional focus routes, super-events, and custom achievements.

The design has four material engine boundaries: only four scientist specializations with a level-5 maximum; omitted specializations default to level 1; project completion and project-derived forces require explicit context/follow-through; and native animation is proven only for large leader portraits, not advisor or scientist portrait surfaces. The parent should carry these boundaries into implementation, live validation, and any user discussion about unsupported animation or non-DLC behavior.

No fallback or simplification was implemented by this research pass. No gameplay file was changed.
