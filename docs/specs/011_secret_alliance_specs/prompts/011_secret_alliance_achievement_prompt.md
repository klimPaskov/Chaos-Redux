# Event 011 Secret Alliance Achievement Prompt

These achievements use working labels and title directions, not final localisation. Final wording belongs to implementation after localisation review.

| Working key | Visibility | Eligible player | Unlock conditions | Disqualifiers | Difficulty | Why it is interesting | Icon direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| secret_alliance_paper_trail | Visible | Target country | Identify all three founders before a major patron joins and before public compact formation | Public reveal by war before identification | Medium | Rewards early evidence play and non-war tools | Dossier thread connecting three hidden seals |
| secret_alliance_no_public_war | Hidden | Target country | Collapse or dissolve a compact that reached at least five members without open war between target and any pact member | Starting a war against any pact member | Hard | Rewards complete peaceful counter-conspiracy play | Broken pact seal without weapons |
| secret_alliance_lonely_crown | Visible | Target country outside any faction at public reveal | Defeat a public pact with at least one major member without joining a faction before victory | Joining a faction before pact defeat | Hard | Creates a lonely-war challenge | Lone shield facing three hostile banners |
| secret_alliance_turn_the_room | Visible | Target country | Turn a founding member into a defector, use its evidence to expose or weaken the pact, then survive the resulting public phase | Defector is annexed or rejoins before use | Medium hard | Rewards targeted diplomacy over brute force | One hand pulling a chair away from a pact table |
| secret_alliance_open_files | Hidden | Target country | Identify every living pact member before Evolution III public compact formation | Public reveal from war before all are identified | Hard | Rewards full dossier mastery | Open cabinet with every file lit |
| secret_alliance_against_the_wall | Hidden | Target country | Win a war against a pact that includes at least two majors and at least six total members | Capitulating or accepting severe ultimatum | Very hard | Rewards surviving the worst nonterminal version of the event | Fortified capital under converging arrows |
| secret_alliance_border_spark | Visible | Target country with border member | Win a controlled border war against an identified pact member, isolate that member, then later dissolve or defeat the compact | Border war escalates into full pact war before isolation completes | Medium hard | Rewards border mechanics and restraint | Border marker with contained sparks and shield |

## Tracking notes

The implementation should track founder identification, major patron entry date, public reveal reason, peaceful collapse, faction membership of the target, defector use, total public member count, major member count, controlled border war outcomes, and severe ultimatum acceptance. Do not unlock achievements from the root event alone.
