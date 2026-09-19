# 068 ZIN specification package

This package expands the supplied ZIN brief into a persistent colony campaign for Chaos Redux. Place this folder at `docs/specs/068_zin_specs/`. The preserved original brief and thirteen maps remain the source for the user's world. Added institutions, histories, numerical tuning, route details and implementation contracts are proposed design.

Start with the campaign rules, then read the country and military sections before implementing shared systems. The JSON registries support coverage and consistency. They are not native HOI4 scripts and do not prove that any gameplay or asset has been implemented.

## Reading order

| File | Content |
| --- | --- |
| [01 Colonies and crossings](068_zin_01_colonies_and_crossings.md) | Opening, placement, existing residents, neutrality, provocation peace and ongoing growth. |
| [02 Atlas and history](068_zin_02_atlas_and_history.md) | Thirteen source maps, filename aliases, geography, proposed histories and uncertainty. |
| [03 Rush and the Golden Court](068_zin_03_rush_and_the_golden_court.md) | Royal institutions, Unity, Afrit's Influence, five dominions and Lost Cause formation. |
| [04 Succession and Rush endings](068_zin_04_succession_and_rush_endings.md) | Mandatory death, actual civil-war camps, Einendil, Afrit, Regency and Free Dominions. |
| [05 Baseline core routes](068_zin_05_baseline_core_routes.md) | Magical Forest elves, Noris and Dondor. |
| [06 Baseline country packages](068_zin_06_baseline_country_packages.md) | Twelve additional common societies with individual histories, routes and missions. |
| [07 Greater powers](068_zin_07_greater_powers.md) | Afrit, Shachihata, Sunhot, Children, Volgan, Horos and controller-based Glo. |
| [08 Dangerous country packages](068_zin_08_dangerous_country_packages.md) | Thirteen additional Evolution I societies. |
| [09 Greater country packages](068_zin_09_greater_country_packages.md) | Nine additional Evolution II societies. |
| [10 Military and reinforcement](068_zin_10_military_and_reinforcement.md) | Typed beings, ordinary troops, dragon hosts, ships, supply and strength benchmarks. |
| [11 Decisions and missions](068_zin_11_decisions_and_missions.md) | Exact action inventory, costs, targets, lifecycle, missions and compact UI. |
| [12 Diplomacy and Reckoning](068_zin_12_diplomacy_and_the_reckoning.md) | Pledges, regional unions, three factions, global victory and endings. |
| [13 Evolutions and scenarios](068_zin_13_evolutions_scenarios_and_connections.md) | Four stages, four manual setups, Chaos effects and shared-system boundaries. |
| [14 Narrative and super-events](068_zin_14_narrative_and_super_events.md) | Society-specific report directions, knowledge rules and five researched music candidates. |
| [15 Assets and visual handoff](068_zin_15_assets_and_visual_handoff.md) | Maps, flags, portraits, icons, 3D, counters, sounds, animations and castle production. |
| [16 AI and acceptance](068_zin_16_ai_balance_and_acceptance.md) | Probability audit worlds, combat comparisons and 69 planned acceptance cases. |
| [17 Achievements](068_zin_17_achievements.md) | Thirty proposed achievements with historical proof, scenario exclusions and icon direction. |
| [18 Focus blueprint](068_zin_18_focus_blueprint.md) | Shared and country-specific logical graph rules and native-tree completion requirements. |
| [Subagent briefs](068_zin_subagent_briefs.md) | Bounded future role prompts. No claim that those workers ran during planning. |

## Registries

The `registries/` directory contains 44 arrival countries, 89 unit families, 103 actions, 34 secondary signature missions, 534 logical focus work items, 89 narrative records, five super-events, 416 asset requirement rows, 30 achievements and 69 acceptance cases. Counts describe planned design records, not produced runtime files.

The four additional land-based Rush dominions and four political succession packages are documented in the atlas and Rush files. The Rush Island Confederacy is already counted among the 44 arrivals. Dragons and Volgan's regional military hosts are not additional sovereign countries.

## Implementation prompts

| Prompt | Purpose |
| --- | --- |
| [Coding prompt](prompts/068_zin_coding_prompt.md) | Phased full implementation and parent ownership. |
| [Goal prompt](prompts/068_zin_goal_prompt.md) | A compact goal under 4,000 characters. |
| [Asset prompt](prompts/068_zin_asset_prompt.md) | Complete visual and creature-asset production. |
| [Super-event prompt](prompts/068_zin_super_event_prompt.md) | Five separate image, quote, remark and recorded-music packages. |
| [Decision and mission prompt](prompts/068_zin_decision_mission_prompt.md) | Action, mission and event-owned UI implementation. |
| [Achievement prompt](prompts/068_zin_achievement_prompt.md) | Actual achievement conditions, tracking and icon variants. |

## Source rules that cannot be changed quietly

The Golden King dies through Afrit and a real succession war follows. Einendil offers service, can be dismissed and becomes a non-royal chosen leader through his good victory. Volgan already rules the Dead Lands and starts far stronger than Afrit. Afrit remains an independent third power and can surpass him through the Rush crown. Rush does not normally recruit independent orcs, goblins, trolls or ogres. Dragons never receive a country. Glo belongs to the controller of the state containing the one real Castle of Yeldenne. Edvoid remains Event 010's actor.

## Decisions and implementation gates still visible

The preferred below-1000 Reckoning terminal-eligibility receipt is a proposed exception to the current shared world-end rule. It requires approval. The strict existing-rule alternative is political victory with nonterminal aftermath below 1000, which does not fully match the brief's unconditional terminal promise. Neither behavior may be selected secretly.

The source brief does not locate the Worshipdom or Yeldenne on a particular supplied map. Those two homeland image assignments need confirmation or an approved non-map exception. Smaller map spellings remain marked as uncertain. The cause and location of Einendil's freezing remain intentionally unresolved canon.

The mandatory Rush civil war requires real territorial camps. The design provides later outpost crossings, but a campaign where no legal second center can exist remains a structural blocker. It is not permission for a peaceful succession or an invented province-splitting engine feature.

Country-carrier collisions, actual native creature restrictions, ship capture, mixed-species selection voices, castle placement, final focus layouts, DDS outputs, model animations, sound and in-game balance need the actual installed sources and runtime tests. The units' numeric indexes are design benchmarks, not ready native statistics.

The accompanying reading and validation report is supplied separately from this source design. It records repository inspection, unread dependencies, unavailable subagents and the distinction between package consistency checks and game validation.
