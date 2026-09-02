# Event 016 technology-action cost postreview — 2026-09-02

Status: bounded read-only postreview against baseline commit `ef48d393f7211a1d3ed0a85cfaab006e565fb6c1`.

Only this handoff was written by this subagent; no gameplay, localisation, documentation, weight, asset, or commit change was made by this subagent.

The review covers the eight technology-action decisions, their payment/refund effects, affordability triggers, tuning constants, the new scripted-localisation cost presentation, and the English localisation file.

The promoted cross-project contract was checked at `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md:52-54,72`.

The Event 016 project-system cost table was checked at `docs/events/016_brilliant_scientist/systems/projects.md:193-215`.

Required repository guidance was read, including `AGENTS.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md`.

The required offline decision, trigger, effect, localisation, data-structure, scope, modifier, on-action, event, and AI references were consulted together with the installed vanilla documentation and vanilla decision precedents.

## Issue list sorted by severity

### P1 documentation blocker — the technology-action system spec is stale

`docs/specs/016_brilliant_scientist_specs/systems/016_wonder_technology_actions.md:5` still names `brilliant_scientist_directorate_category`, while the reviewed decision file now attaches all eight IDs to `conventional_technology_operations` at `common/decisions/016_brilliant_scientist_technology_actions.txt:17` and the category is registered at `common/decisions/categories/016_conventional_technology_categories.txt:10-14`.

`docs/specs/016_brilliant_scientist_specs/systems/016_wonder_technology_actions.md:15-17` still says selection spends trucks and manpower and that cancellation refunds manpower, while the current payment helpers contain only Command Power, support equipment, and fuel at `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt:10-44`.

`docs/specs/016_brilliant_scientist_specs/systems/016_wonder_technology_actions.md:64` still claims that fuel uses an exclusive gate and that manpower is an inclusive cost, while the current trigger uses inclusive `NOT = { has_fuel < ...refund }` checks at `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt:81-105` and no manpower gate exists.

The promoted completion contract and the current project-system documentation already describe the four-axis profile correctly, so this is a documentation source-of-truth mismatch rather than a demonstrated runtime defect.

Minimal remediation: synchronize that stale system spec with the promoted contract and current project-system table, preserving the current category name, four cost axes, inclusive fuel boundary, and native factory commitment.

### P2 visual and engine evidence limitation — the native decision surface is not dynamically cost-certified

The mandatory read-only `hoi4.gui_inspect` call covered `countrydecisionview` with scenario `{ id: "event016_directorate_compact_current" }` in workspace `mod_chaos_redux_ea3b2d67c2c0`.

It returned `GUI_INSPECTED`, status `ok`, source revision `1d8d9b635245875164c7ad96ab2890b14c548b5706b3edc72be301eb1a2616d3`, validation passed, and no blocking tool blocker.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4228e7462a20d56f510883c62eae670a723defd0150d2119194a63dd52162704/55ed134e69c8b8bf05710ba713ddff5ca4d5703140a1267a2049feccbf24c695/gui-inspect.1d8d9b6352458751.json`.

The inspect diagnostics report `GUI_ACCIDENTAL_CLIPPING` because `countrydecisionview` is clipped from `550x1080` to `0x0`, several `GUI_INVALID_SIZE` warnings for zero-sized native elements, and `GUI_SPRITE_RENDER_PARTIAL` because the button-state Lua effect is not executed by the offline renderer.

The mandatory `hoi4.gui_render` call returned `GUI_RENDERED`, status `ok`, four requested states (`normal`, `locked`, `warning`, and `long-text`), two requested resolutions (`1366x768` and `1920x1080`), and the same source revision.

Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cf551d536d5f323e23809df0f5530c6e66fe7983b7cd75e14d4bec5fd0e44e19/5960b3f917d647c2d2eb5391b35d4f8c39fdd35830bf34bbf3e29b87682ee8c4/countrydecisionview-full.svg`.

The render scenario did not execute or expand the Event 016 technology-action rows and its metadata lists the visible full variant at `1920x1080`, so it does not prove the four dynamic cost entries fit the native decision row at either resolution or that the hover `_tooltip` expansion is readable.

The production-render warnings are recorded as evidence limits and are not dismissed as renderer differences.

No GUI rewrite is recommended in this cost postreview because the patch changes decision data and localisation, not the shared native layout, and no in-scope GUI file was authorized for editing.

### P2 cognitive-load boundary — eight IDs can be visible in one ordinary category

The source preserves all eight accepted decision IDs and the ordinary category intentionally groups them by mature project family.

The family completion flags are not mutually exclusive, so a country with all six relevant families weaponized can expose eight rows at once because Rocketry and Biomedical each contribute two actions.

This exceeds the generic six-primary-action guidance even though each row has a distinct project identity and the cost display is compact.

This is not introduced by the cost patch and no cardinality or outcome change is proposed in this bounded review; it remains an explicit UX acceptance dependency for the category owner before claiming full presentation acceptance.

## Cost and requirement audit

The current source has exactly four spendable or committed axes per action: Command Power, support equipment, fuel, and native temporary civilian-factory occupation.

The factory occupation is implemented by the native `modifier = { civilian_factory_use = ... }` field and is not duplicated as a scripted debit or refund.

| Decision ID | Payment helper | Command Power | Support equipment | Fuel | Occupied civilian factories | Other requirement |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `brilliant_scientist_saturate_sensor_region` | `brilliant_scientist_pay_light_technology_action` | 20 | 75 | 250 | 2 | Valid controlled core with radar, air base, or anti-air infrastructure. |
| `brilliant_scientist_launch_predictive_campaign` | `brilliant_scientist_pay_standard_technology_action` | 25 | 100 | 500 | 2 | Computation family availability. |
| `brilliant_scientist_order_epidemic_control` | `brilliant_scientist_pay_standard_technology_action` | 25 | 100 | 500 | 2 | Biomedical family availability. |
| `brilliant_scientist_construct_state_synthesis_works` | `brilliant_scientist_pay_standard_technology_action` | 25 | 100 | 500 | 3 | Valid owned core with industrial capacity; three factories are required and occupied. |
| `brilliant_scientist_activate_high_speed_strike_network` | `brilliant_scientist_pay_heavy_technology_action` | 40 | 200 | 1,500 | 3 | At least two military factories. |
| `brilliant_scientist_launch_long_range_delivery_strike` | `brilliant_scientist_pay_heavy_technology_action` | 40 | 200 | 1,500 | 3 | At least two military factories and a valid enemy industrial target. |
| `brilliant_scientist_raise_field_projectors` | `brilliant_scientist_pay_heavy_technology_action` | 40 | 200 | 1,500 | 3 | At least two military factories. |
| `brilliant_scientist_order_emergency_regeneration` | `brilliant_scientist_pay_heavy_technology_action` | 40 | 200 | 1,500 | 3 | At least two military factories. |

The light, standard, synthesis, and heavy custom-cost rows are wired at `common/decisions/016_brilliant_scientist_technology_actions.txt:21-26,43-48,65-70,83-89,107-113,132-138,152-158,172-177`.

The heavy military-factory condition is a non-consumed requirement shown through `brilliant_scientist_technology_action_military_industry_tt` in the four heavy decision `available` blocks at `common/decisions/016_brilliant_scientist_technology_actions.txt:83-86,107-110,132-135,152-155`.

The synthesis helper composes standard affordability with the heavy three-factory floor at `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt:95-98`, matching its native three-factory modifier at `common/decisions/016_brilliant_scientist_technology_actions.txt:71-74`.

The shared affordability boundaries are:

- Command Power is inclusive through `NOT = { command_power < ... }` at `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt:81-105`.
- Civilian-factory availability is inclusive through `NOT = { num_of_civilian_factories_available_for_projects < ... }` at the same trigger block.
- Support equipment uses the native strict `>` form against gate constants exactly one below the displayed payment, so 75, 100, and 200 are accepted at `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt:84,91,103`.
- Fuel is inclusive through `NOT = { has_fuel < ...refund }` at `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt:85,92,104`.

The constants retain paired positive refund/display and negative debit values at `common/script_constants/016_brilliant_scientist_technology_action_constants.txt:14-37`.

The current values are magnitude-conserving: light is 20 Command Power, 75 support equipment, and 250 fuel; standard is 25, 100, and 500; heavy is 40, 200, and 1,500.

The three payment effects debit exactly once from each of the eight `complete_effect` blocks at `common/decisions/016_brilliant_scientist_technology_actions.txt:30,52,73,93,117,142,162,181`.

The matching refund effects occur exactly once in each of the eight `cancel_effect` blocks at `common/decisions/016_brilliant_scientist_technology_actions.txt:33,55,76,96,120,145,165,184`.

The payment and refund implementations are `brilliant_scientist_pay_light_technology_action`, `brilliant_scientist_pay_standard_technology_action`, `brilliant_scientist_pay_heavy_technology_action`, and their three matching refund helpers at `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt:10-44`.

No truck, motorized-equipment, or manpower debit, refund, gate, or cost text remains in the six reviewed surfaces.

The native timed factory modifier is released by the decision engine on cancellation, while the scripted cancel effects refund only the resources actually debited by `complete_effect`.

This matches the offline decision-modelling rule that custom costs are not debited automatically and must be paid in `complete_effect`, and the installed vanilla `EST.txt:353-363` precedent that pairs `civilian_factory_use = 2` with a `num_of_civilian_factories_available_for_projects > 1` custom-cost gate.

No duplicate charge or refund path was found in the eight native decision lifecycles.

## Decision category and lifecycle notes

The category rename is structurally registered by `common/decisions/categories/016_conventional_technology_categories.txt:10-14`, and no duplicate copy of these eight IDs remains under the old Directorate category in the reviewed decision file.

All eight actions retain their original outcome helpers, target semantics, durations, cooldowns, and AI blocks; the decision diff contains only the category/custom-cost wiring and the separate requirement tooltip additions.

The native timer fields remain file-local `@` constants in `common/decisions/016_brilliant_scientist_technology_actions.txt:1-8` and their values were not changed by this patch.

The targeted actions retain state-target and target-trigger validation, and invalid targets remain cancellation conditions rather than hidden payments.

These are timed decisions, not missions; no mission owner, mission category, activation, timeout, or mission duplicate risk is in scope for this postreview.

## Localisation, texticons, and tooltip audit

The new scripted-localisation file defines exactly eleven country-scoped helpers at `common/scripted_localisation/016_brilliant_scientist_technology_action_cost_scripted_localisation.txt:8-62`: three Command Power helpers, three support-equipment helpers, three fuel helpers, and two civilian-factory helpers.

Each helper selects a normal or blocked fragment independently, yielding 22 normal/blocked fragment bindings with no resource-side effect.

The four rows at `localisation/english/016_brilliant_scientist_technology_actions_l_english.yml:30-41` compose the helpers as light, standard, synthesis, and heavy profiles.

The light row shows Command Power, support equipment, fuel, and two civilian factories; the standard row uses the same first three with two civilian factories; synthesis swaps in three civilian factories; heavy uses the heavy values and three civilian factories.

Every spendable entry is amount-first and uses a registered texticon: `£command_power`, `£support_equipment_text_icon`, `£fuel_texticon`, or `£civ_factory` at `localisation/english/016_brilliant_scientist_technology_actions_l_english.yml:43-64`.

The blocked aliases at lines 31, 34, 37, and 40 preserve the normal row key while the nested helper branches colour only the unaffordable entries red.

The `_tooltip` aliases at lines 32, 35, 38, and 41 are live under the vanilla `custom_cost_text` convention, which automatically resolves `<key>_tooltip` on hover; they are not dead localisation.

The cancellation text at `localisation/english/016_brilliant_scientist_technology_actions_l_english.yml:28` explicitly says that support equipment, fuel, and Command Power are returned and factories released.

The payment explanation at line 42 distinguishes immediate resource payment from the timed factory commitment without dumping internal trigger text.

The scripted-localisation file contains no raw `£` or `§` formatting characters; all formatting remains in normal localisation, consistent with the scripted-localisation contract.

The English localisation file retains the required UTF-8 BOM bytes `239,187,191`.

No raw nested affordability helper or obsolete cost prose is exposed by the changed decision rows.

## Dead constants and obsolete localisation

The removed truck, manpower, and old exclusive fuel constants have no references in the six reviewed files or in the current gameplay source search.

The removed legacy cost keys (`brilliant_scientist_*_cost_tt`) have no remaining gameplay or localisation references in the current reviewed surface.

The pre-existing `kruger_aggression_factor` at `common/script_constants/016_brilliant_scientist_technology_action_constants.txt:75` has no current gameplay consumer found by the bounded source search, but it was already present in the baseline and was not introduced by this cost patch.

That pre-existing AI constant is a non-blocking cleanup note and should not be removed in this tranche because the parent requested unchanged AI formulas and a separate probability owner retains the weighted audit.

## Cognitive load and player-facing significance

The four-row cost surface is substantially more scannable than the former prose rows because each resource is isolated, icon-led, and independently coloured.

The visible Command Power, support-equipment, fuel, and factory values each correspond directly to a concrete start condition or native timed commitment.

Heavy military factories and target validity remain requirements rather than hidden fifth or sixth costs, and the heavy requirement has a dedicated concise tooltip.

The category can still reach eight visible primary actions in an all-families weaponized state, as noted under the P2 category-density boundary.

No active missions are created by these actions, and no unexplained meter dump or raw scripted-trigger row was introduced.

## AI validity and route-lock notes

All eight `ai_will_do` blocks and the AI constants remain unchanged from the baseline commit.

The hidden affordability helper in each `available` block prevents selection when any of the four payment or capacity axes is unavailable.

The four heavy actions retain the separate military-factory gate in `available`, and the three targeted actions retain their existing valid-target checks.

No `ai_hint_pp_cost` is needed because these decisions do not spend Political Power; Command Power is a different resource.

No probability audit or before/after probability comparison is claimed here because no AI weight or probability-bearing source changed and that pass remains assigned to the separate probability owner.

The decision helpers still use the current-host/project-family eligibility path; the ordinary category does not by itself certify neutral-provider API eligibility.

The broader neutral API patch is explicitly outside this postreview and remains pending separately.

## Validation and acceptance boundary

Task-specific static checks found eight decision IDs, eight `custom_cost_trigger` calls, eight `custom_cost_text` calls, eight payment calls, and eight matching refund calls.

The scripted-localisation audit found eleven `defined_text` helpers, 22 resolved normal/blocked fragment keys, four composed rows, no missing localisation references, no raw scripted-localisation format characters, and complete expected texticon coverage.

The current six source hashes are:

| File | SHA-256 |
| --- | --- |
| `common/decisions/016_brilliant_scientist_technology_actions.txt` | `57986EE9ED6B7C585C03E7FF39270881B637AC86218C0572A2E4EC6ABCDD1531` |
| `common/scripted_effects/016_brilliant_scientist_technology_action_effects.txt` | `3792A52E52700908DC1C9EF4F0A7907B7A56360405996E3E479836114FAA9C01` |
| `common/scripted_triggers/016_brilliant_scientist_technology_action_triggers.txt` | `DC0BF5D7D8CED72995D47CDBA93A043253D47886D11B26903D910F5B616B3A5C` |
| `common/script_constants/016_brilliant_scientist_technology_action_constants.txt` | `B10C4BB772F3DF3E706FF352E4DB07C772FAE0614B4958779D404CDCD9CC0029` |
| `common/scripted_localisation/016_brilliant_scientist_technology_action_cost_scripted_localisation.txt` | `273A5BBFD13B8F4E55A640E31A0D2E45CE77A581DD595574D41734FB8869F479` |
| `localisation/english/016_brilliant_scientist_technology_actions_l_english.yml` | `C2E470E130307B33337B1DF298F2CD7306CB9AF3B29199200E608142C61D2B0C` |

The promoted contract hash during this review was `262431D0BB79F38E1121FC71A5C7CCA44CB31910E3AF2D1FC6E0C4B486898E70`.

The stale technology-action system-spec hash was `E95FD8EBD3C259F2FEA9B7A5BB24DE7540BD43430DC8708DC54989B753F2A3C6`.

Source acceptance: no P0 or P1 gameplay defect was found in the six reviewed technology-action cost surfaces, and the four-axis payment/refund design is internally conserved at the current hashes.

Full completion acceptance remains open for the P1 stale spec, the P2 category-density decision, and current dynamic Event 016 decision-row visual evidence.

No Hearts of Iron IV process was launched, no logs were requested, and no live save-state or engine-ordering proof is claimed.

No gameplay patch, balance change, or commit was made by this subagent.

Plan handoff path: this file.
