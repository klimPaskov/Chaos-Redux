# Secret Alliance decision map

This map gives the implementation agent an action-level design. Names are working labels, not final localisation.

| Decision or mission | Phase | Target | Main cost palette | Success | Failure or risk | AI use |
| --- | --- | --- | --- | --- | --- | --- |
| Trace courier routes | Dossier opens | suspected route or region | convoys, trains, fuel, political attention | Evidence gain, possible liaison reveal | exposure risk, relations loss | AI player equivalent can run if target is AI and system supports AI |
| Intercept field radios | Dossier opens | domestic state or suspect | support equipment, infantry equipment, army XP | high Evidence, sabotage delay | false lead, stability strain | Pact AI counters with burn-evidence action |
| Turn a courier | Counter-network | named suspect | civilian burden, political attention, agency strength | reveal ring, lower cohesion | courier lost, readiness rises | AI should use only with sufficient evidence |
| Convene neutral inquiry | Counter-network | neutral observer | convoys, diplomatic credibility, civilian burden | lower player isolation, raise pact isolation | humiliation if evidence weak | Neutral AI evaluates credibility and relations |
| Guard industrial centers | Dossier opens onward | player industrial states | infantry equipment, support equipment, manpower | Preparedness gain, sabotage mitigation | production strain, security strain | AI player can use if threatened |
| Secure rail and depot lines | Dossier opens onward | rail or supply states | trains, fuel, support equipment, divisions | supply protection, evidence chance | rail sabotage if failed | High AI priority during war risk |
| Harden ports and cipher rooms | Dossier opens onward | coastal and naval routes | convoys, fuel, navy XP, support equipment | overseas route protection | convoy loss or naval intel leak | Use for island and colonial players |
| Emergency counterintelligence sweep | Severe incidents | domestic states | support equipment, command power, stability risk | strong Evidence and Preparedness | stability loss and isolation | AI uses only at high threat |
| Quiet demarche | Suspect named | suspected country | diplomatic cost, relations, evidence | lower confidence, pause incidents | cohesion gain if weak evidence | Pact AI may deny or escalate |
| Offer face-saving exit | Counter-network | liaison or armed associate | concessions, trade burden, guarantees | member leaves outer ring | pact readiness rises from panic | AI members accept based on motive |
| Public accusation with dossier | High evidence or Evolution III | suspect or network | diplomatic credibility, evidence | pact isolation, partial reveal | player isolation and War Clock gain | AI rarely uses against player unless high evidence |
| Secret bargaining with Convener | Counter-network | Convener | concessions, high evidence, relation channel | delay reveal, split pact | talks leaked, isolation rises | Convener AI accepts if cohesion low |
| Border watch mission | Dossier or public pressure | neighboring suspect | supplied divisions, equipment, command attention | Preparedness, reduced border tension | border incident severity rises | AI uses if border threat exists |
| Controlled border incident | Confirmed neighbor | pact member neighbor | army XP, support equipment, divisions | lower member confidence, capture proof | reveal or war | AI should be cautious |
| Preemptive war authorization | Public pact | pact faction or member | evidence, war support, preparedness | player chooses timing | neutral sympathy loss | Human-facing, AI only with strong advantage |
| Publish captured pact plans | Revealed war | public audience | evidence, stability, diplomatic effort | lower pact cohesion, reduce outer-ring joins | propaganda backlash if weak evidence | AI player equivalent can use |
| Strike coordination offices | Revealed war | pact member | command power, intel, air or army resources | lower pact war coordination | failed raid increases enemy readiness | AI if war active and target valid |
| Separate exit pressure | Revealed war | weak minor member | evidence, military pressure, diplomacy | member exits faction or war | patron retaliation | AI uses when member low confidence |

## Active mission cap

The player should normally have at most two active timed missions from this event, plus one emergency mission. This cap keeps the category from becoming a task wall.

## Target display rule

Human-facing target decisions should show only currently selected, named, or confirmed suspects. AI should still evaluate valid hidden targets through script logic without needing the player selector.
