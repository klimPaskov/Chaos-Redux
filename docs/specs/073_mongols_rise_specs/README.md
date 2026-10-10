# Event 073: Mongols Rise

Start with [the main specification](073_mongols_rise_spec.md). This folder contains the expanded campaign design. Working labels identify design functions and are not final localisation or a fixed set of runtime identifiers.

The package preserves the user’s normal cavalry army, rapid opening, offensive strength, permanent defensive weakness, three Great Khan routes, flexible regional campaigns, khanates, tribute, Karakorum, connected routes, three Evolutions, succession and meaningful successors.

[Planning, execution, source records, prompts and honest limits](../../plans/073_mongols_rise_plans/README.md) are kept separately. The detailed path-level design is not an implemented focus graph. Its Mermaid route guide is conceptual and is not native layout proof.

Use current [event](../../../.claude/skills/chaos-redux-events/SKILL.md), [planning](../../../.claude/skills/chaos-redux-event-planning/SKILL.md) and [subagent](../../../.claude/skills/chaos-redux-subagents/SKILL.md) guidance when implementing from those prompts.
Retain the recorded user requirements; separately record acceptance of author-added design before treating it as approved.

## Campaign

- [Opening and sovereignty](campaign/01_opening_and_sovereignty.md)
- [Momentum and Authority](campaign/02_momentum_and_authority.md)
- [Evolutions](campaign/03_evolutions.md)

## Military

- [Cavalry and the tumen system](military/01_cavalry_and_tumens.md)
- [Muster, conquest rewards, and logistics](military/02_muster_rewards_and_logistics.md)

## Focus tree

- [The imperial focus tree](focus_tree/01_tree_structure.md)
- [Political route: Heir of Genghis](focus_tree/02_heir_of_genghis.md)
- [Political route: The New Great Khan](focus_tree/03_new_great_khan.md)
- [Political route: Council of Khans](focus_tree/04_council_of_khans.md)
- [Shared army, economy, and crisis routes](focus_tree/05_army_economy_and_crisis_routes.md)
- [Conceptual route map in Mermaid format](focus_tree/06_route_map.mmd)

## Expansion

- [Campaign and settlement rules](expansion/01_campaign_rules.md)
- [Mongol union and the Siberian approaches](expansion/02_mongol_union_and_siberia.md)
- [Northern China](expansion/03_northern_china.md)
- [Central Asian khanates](expansion/04_central_asia.md)
- [The Rus and the Golden Horde](expansion/05_rus_and_golden_horde.md)
- [Persia and the Middle East](expansion/06_persia_and_middle_east.md)
- [The Great Western Campaign](expansion/07_great_western_campaign.md)
- [Southern campaigns](expansion/08_southern_campaigns.md)

## Empire

- [Revived khanates and country packages](empire/01_khanates_and_country_packages.md)
- [Tribute and imperial diplomacy](empire/02_tribute_and_diplomacy.md)
- [Karakorum and the Silk Roads](empire/03_karakorum_and_silk_roads.md)
- [Succession, collapse, and recovery](empire/04_succession_collapse_and_recovery.md)

## Interaction

- [Decisions and missions](interaction/01_decisions_and_missions.md)
- [Interface and state puzzles](interaction/02_interface_and_state_puzzles.md)

## AI and multiplayer

- [AI and multiplayer behavior](ai/01_ai_and_multiplayer.md)

## Presentation and achievements

- [Events, news, and super-events](presentation/01_events_and_super_events.md)
- [Visual and audio asset design](presentation/02_asset_design.md)
- [Achievement design registry](presentation/03_achievements.md)

## Changelog

### 2026-10-10 spec audit

- The settlement rules now state how the existing Famine and Migration owners weigh on the direct rule, khanate, and tributary choice: conquest causes ordinary war flight, harsh extraction occupation feeds Famine, and a directly ruled hungry region counts toward the empire's own Food Crisis penalty while a khanate carries its own. No new Event 073 mechanic is added; the existing systems give the settlement choice a cost the player can see.
- The rest of the package was already proportionate: two meters with distinct roles, conditions shown as states rather than more meters, and bounded rewards. It is otherwise unchanged apart from Claude-first subagent wording and skill links.
