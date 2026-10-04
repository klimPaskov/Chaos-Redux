# Event 033 Acid Rain AI acceptance matrix

| Case | Starting conditions | Expected permanent behavior | Expected urgent behavior | Expected recovery behavior | Failure condition |
| --- | --- | --- | --- | --- | --- |
| A1 | Fragile peaceful minor, distant front | Start one payable Shelter or Water tier, keep two free civilian factories when possible | None until threat rises | None | Spends all trains or cannot start any project |
| A2 | Fragile minor, destination warning | Prefer Shelter, then one payable protocol | Shelter protocol if affordable, no impossible long action | Preserve recovery resources | Ignores warning despite payable action |
| A3 | Fragile minor under invasion | Respect manpower floor and war stockpile shortage | Use one high-value emergency action, avoid broad overspend | Delay low-priority repair until threat falls | Reserves manpower below shared safety floor |
| A4 | Island country with convoy stock | Use island Water route | Use convoy water route and island evacuation variant | Use convoy decontamination | Charges trains and convoys together |
| A5 | Island country with convoy shortage | Prefer Shelter or Medical | Avoid unaffordable convoy route, choose payable alternative | Repair local industry if payable | Repeatedly selects blocked convoy decision |
| A6 | Landlocked country | Use land project variants | Use train route, never convoy route | Use land decontamination | Pays convoys |
| A7 | Established country, 180 days before arrival | Run two projects, balance lowest component tiers | Prepare no emergency action too early | None | Stacks one component to tier 4 while another stays 0 without reason |
| A8 | Great power, two simultaneous region warnings | Run up to three projects with reserves | Protect highest-population and capital states first | Keep one reserve for later recovery | Evacuates low-value state before dense capital without affordability reason |
| A9 | Major at war, low support equipment | Shift toward Transport if payable | Use reroute with trains and trucks, preserve support reserve | Repair transport first | Buys support-heavy action below emergency floor |
| A10 | Country with strong CBRN civilian protection | Still build broad civil infrastructure | Lower priority for overlapping Medical tier, never disable it | Use decontamination efficiently | Treats CBRN score as automatic 100 Preparedness |
| A11 | Active ordinary exposure, no warning | Continue useful near-complete project | Shelter, water, medical, or reroute according to current harm | Queue recovery only after state exits | Starts severe evacuation without forecast |
| A12 | Severe forecast in three states | Permanent slots unchanged | Evacuate highest weighted payable targets, shelter remaining states | Prepare medical recovery | Starts evacuation after first severe pulse when no benefit remains |
| A13 | Multiple fronts, country exposed in two regions | Raise project urgency | Keep per-country action caps and separate forecast receipts | Sort aftermath globally by tier and importance | Confuses front IDs or clears one warning with another |
| A14 | Global layer, Preparedness below 50 | Use extra slot only with factory proof | Maintain shelter and medical actions, prioritize superstorms | Repair only when urgent reserves remain | Consumes every factory or support item |
| A15 | Global layer, Preparedness above 80 | Finish weakest component if affordable | Target superstorms and transport continuity | Begin high-tier decontamination as states permit | Repeats expired emergency action with no added effect |
| A16 | Capital severe forecast | Transport and Shelter score rise | Protect capital unless unaffordable or already protected | Restore capital route first | Chooses low-population rear target first |
| A17 | Occupied forecast state changes controller | Old AI releases target | New controller receives valid action and reevaluates cost | New controller owns aftermath work | Both countries pay for one action |
| A18 | Acute event dissipates with project in progress | Let valid project finish or convert through accepted rule | Stop new urgent actions | Use completion as recovery benefit | Deletes paid project or returns consumed equipment |
| A19 | Aftermath tier 3 water burden | New permanent project only if future threat remains | No obsolete urgent action | Decontaminate before low-tier industry repair | Repairs factory while tier-3 water pressure remains without reason |
| A20 | No active, warning, aftermath, or commitment | Start no new Event 33 work | None | Demobilize and close category | Keeps empty category open forever |

## Probability checks

For cases A1 through A20, inspect the final decision weights and confirm:

- at least one reachable payable choice when a useful action exists
- no blocked option retains dominant effective weight
- reserve rules can reduce a choice to zero intentionally
- tie-breaks are deterministic or use documented weighted draws
- threat-state changes produce the intended priority shift
- no AI-only effect bypasses the player cost or target trigger
