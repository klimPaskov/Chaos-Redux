# Event 007 catalog wording pending

Disposition: accepted and queued.
Acceptance basis: the user authorised G1-G7 corrections on 5 October 2026; the parent accepted the changes recorded in `agent_decisions_2026-10-05.md`.
The task forbids editing the workbook or exports.
The spreadsheet owner should mirror applicable rows from current in-game wording and then run the required exporter.

## Exact current localisation

Opening news resolves its two getters through the single/multiple branches below.
The frozen batch count selects the branch; do not copy the old single-country description as the only outcome.

| Localisation key | Exact current text |
| --- | --- |
| `chaosx.news.7008.t` | `[GetFuryOpeningNewsTitle]` |
| `chaosx.news.7008.d` | `[GetFuryOpeningNewsDescription]` |
| `chaosx.news.7008.t.single` | `Fury Grips [fury_opening_news_actor.GetName]` |
| `chaosx.news.7008.d.single` | `Reservists crowd the barracks of [fury_opening_news_actor.GetName], and armed columns assemble along its frontier. Officers drive their men through sleepless preparations for an invasion. The name Fury has spread with reports of the mobilisation.` |
| `chaosx.news.7008.t.multiple` | `Fury Grips Several Countries` |
| `chaosx.news.7008.d.multiple` | `Reports of Fury have arrived from [?fury_opening_news_actor.fury_opening_actor_count\|0] countries. Reservists crowd their barracks, and officers assemble armed columns along the frontiers. Neighbouring towns prepare for invasion as the same sleepless mobilisation spreads under different flags.` |
| `chaosx.news.7008.a` | `Watch the border.` |
| `chaosx.news.7007.t` | `Fury Troops Cross the Frontier` |
| `chaosx.news.7007.d` | `The forces of [fury_news_actor.GetName] have taken foreign territory and keep advancing. Soldiers push farther along the roads as civilians flee the occupied towns.` |
| `chaosx.news.7007.a` | `The fighting has crossed the border.` |
| `chaosx.nr7.3.t` | `No Country Can Enter Fury` |
| `chaosx.nr7.3.d` | `Fury can begin only in an independent minor with at least one neighboring country it can attack. Player countries, their allies, and their subjects cannot become Fury's starting country.` |
| `chaosx.nr7.3.a` | `Understood.` |
| `chaosx.nr7.2.d` | `Reservists fill barracks in [ROOT.GetName], and officers assemble armed columns for an invasion. The commanders send their men toward a neighbouring frontier without delivering a demand to its government.` |
| `chaosx.nr7.2.a` | `The border is no longer secure.` |
| `chaosx.nr7.50.d` | `Fury has spread beyond its first country. Other governments are mobilizing and attacking their neighbors. Their columns keep advancing, and countries once beyond Fury's reach now face the same threat.` |
| `chaosx.nr7.51.t` | `Fury Cannot Spread Further` |
| `chaosx.nr7.51.d` | `There are too few independent minor countries for Fury to spread farther. Player countries, their allies, and their subjects cannot become new Fury countries.` |
| `chaosx.nr7.52.t` | `Fury Targets a Player Country` |
| `chaosx.nr7.52.d` | `The World in Fury pact is preparing to attack [fury_terminal_player_target.GetName]. Its forces are gathering near the border.` |
| `chaosx.nr7.53.d` | `The last leading Fury country has fallen. Its forces can no longer carry the war to another country.` |
| `chaosx.nr7.60.t` | `Fury Reaches South America` |
| `chaosx.nr7.60.d` | `The Fury government in [fury_monroe_response_actor.GetNameDef] has taken another South American capital. Its forces are entering government offices as refugees flee by rail.\n\nWashington must decide whether to declare war or leave nearby countries to face Fury alone.` |
| `chaosx.events_log.window.event_details.fury` | `An unnatural rage spreads through a minor country's army. Reservists crowd its barracks and armed columns gather at the frontier, preparing to attack neighbouring countries.` |
| `chaosx.events_log.window.evolution_details.fury.title.stage_1` | `Hardened Fury` |
| `chaosx.events_log.window.evolution_details.fury.title.stage_2` | `Two Fires` |
| `chaosx.events_log.window.evolution_details.fury.title.stage_3` | `All Borders at Once` |
| `chaosx.events_log.window.evolution_details.fury.body.event_detail` | `Reservists gather under commanders who drive their men toward the next frontier. Conquest feeds the rage spreading through the army.` |
| `chaosx.events_log.window.evolution_details.fury.body.stage_1` | `Columns regroup at captured depots, refill their ranks, and march toward the next frontier. Neighbouring governments prepare for a prolonged war.` |
| `chaosx.events_log.window.evolution_details.fury.body.stage_2` | `Reports of Fury arrive from different frontiers. Officers and soldiers repeat the same sleepless preparations under separate flags.` |
| `chaosx.events_log.window.evolution_details.fury.body.stage_3` | `Armies seized by Fury fight for roads and towns across a widening front. Civilians search for a way past the advancing columns.` |
| `chaosx.scenarios.fury.impact.low` | `Up to two independent minor countries enter Fury. Your country, its allies, and its subjects are protected.` |
| `chaosx.scenarios.fury.impact.medium` | `Up to five independent minor countries enter Fury. Your country, its allies, and its subjects are protected.` |
| `chaosx.scenarios.fury.impact.high` | `Up to nine independent minor countries enter Fury. Your country, its allies, and its subjects are protected.` |
| `chaosx.scenarios.fury.impact.maximum` | `Up to sixteen independent minor countries enter Fury. Your country, its allies, and its subjects are protected.` |

The Event Details premise is the applicable Events-sheet detail field.
Report/evolution keys must be mapped to existing workbook rows before updating; this document does not authorise adding speculative rows.
Unused legacy cost adapters do not require catalog rows.
