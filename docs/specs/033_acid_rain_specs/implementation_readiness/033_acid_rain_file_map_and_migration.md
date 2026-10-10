# Event 033 Acid Rain file map and remaining work

Status: the runtime that replaced the continent prototype is `implemented`, including prototype save migration (Part 11).
This file maps the implemented source and the remaining work; the original work-package plan is complete and is preserved in Git history.

## Event-owned files

| Path | Responsibility |
| --- | --- |
| `events/033_acid_rain.txt` | Root dispatcher, hidden worker and operation events, reports, world notices and news |
| `common/script_constants/033_acid_rain_constants.txt` | Every timing, chance, mortality, damage, cost, cap, Chaos, AI and GUI anchor value |
| `common/scripted_effects/033_acid_rain_effects.txt` | Registry, fronts, coverage, pulses, mortality gateway, Air requests, evolutions, dissipation, cleanup and migration |
| `common/scripted_effects/033_acid_rain_aftermath_effects.txt` | Consequence classifier, episode caps, damage receipts, aftermath bands and Humanitarian requests |
| `common/scripted_effects/033_acid_rain_preparedness_effects.txt` | Preparedness, quotes, payments, operations, completions and returns |
| `common/scripted_effects/033_acid_rain_gui_effects.txt` | Read-only GUI projection |
| `common/scripted_effects/033_acid_rain_achievement_effects.txt` | Achievement tracking and settlement |
| `common/scripted_effects/033_acid_rain_cxt_effects.txt` and `common/ideas/033_acid_rain_cxt_extension_ideas.txt` | CXT test-country package |
| `common/scripted_triggers/033_acid_rain_triggers.txt` and `033_acid_rain_achievement_triggers.txt` | Eligibility, affordability, usefulness, achievement and tooltip loaders |
| `common/dynamic_modifiers/033_acid_rain_dynamic_modifiers.txt` | Acute bands, aftermath tiers, evacuation disruption, demobilized recovery and operation commitments |
| `common/decisions/033_acid_rain_decisions.txt` and `categories/033_acid_rain_categories.txt` | Acid Rain Response category, decisions and AI |
| `common/on_actions/033_acid_rain_on_actions.txt` | Host scheduling and lifecycle hooks |
| `common/scripted_guis/033_acid_rain_scripted_guis.txt`, `common/scripted_localisation/033_acid_rain_scripted_localisation.txt`, `interface/033_acid_rain.gui`, `interface/033_acid_rain.gfx` | World map, category inlay and sprites |
| `localisation/english/033_acid_rain_l_english.yml` and `033_acid_rain_requirement_flags_l_english.yml` | Player text |
| `sound/033_acid_rain/`, `sound/033_acid_rain_sound.asset` | Super-event audio and severe forecast cue |
| `docs/events/033_acid_rain/overview.md` | Runtime description |

## Shared-system touchpoints

| Surface | Touchpoint |
| --- | --- |
| Event registry and cluster | `chaosx_event_cluster_effects.txt` and `chaosx_settings_effects.txt` (launch markers, mixed pacing) |
| Deaths | `apply_exact_state_civilian_population_loss` in `chaosx_dynamic_effects.txt`, reason 34 |
| Air | Shared source ledger, source id 5 |
| Famine | `famine_adapt_acid_rain_state` in `famine_adapter_effects.txt` |
| CBRN | `cbrn_civilian_mask_effective_coverage` and the strong-protection triggers |
| World end | `acid_rain_interrupt_for_world_end` called by each base `world_end` setter |
| Event Details | Shared Event Log entry points only |
| Achievements | `common/achievements/chaos_redux_achievements.txt` |

## Remaining work

The ordered list is in [the goal prompt](../prompts/033_acid_rain_goal_prompt.md); it covers the README open questions, the D37 regional strips, the F7 legacy report-receipt policy, the pending probability comparison and the Part 12 agent evidence.

## Handoff evidence for later changes

Each later change records its changed files, identifiers, the constants it touches, the before source of any weighted change for the probability auditor, and the user live checks it leaves pending, in the existing plans-folder resume rather than a new report.
