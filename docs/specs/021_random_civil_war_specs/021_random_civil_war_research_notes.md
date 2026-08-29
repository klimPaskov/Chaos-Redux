# Event 021 Research Notes

## Purpose

This note records the research ideas that shaped the Event 021 design. It is a design reference, not player-facing text and not a substitute for the installed Hearts of Iron IV documentation or the repository source.

## Main findings translated into design

### Internal war needs organized opposition and a political claim

The Uppsala Conflict Data Program defines armed conflict around an incompatibility concerning government or territory and the use of armed force between organized parties. Event 021 therefore requires an actor with a public claim, an organization, a territorial or governmental objective, and a military route. A country cannot fracture only because one abstract instability value is low.

Design translation:

- every front has a political or territorial purpose
- every side has leadership or a governing institution
- every side needs viable territory, forces, supply, and an outcome
- generic unrest that cannot produce a viable side should remain a crisis event or same-tag contest
- the opening must name the public dispute and the institution or region behind it

Source:

- Uppsala Conflict Data Program, Definitions, https://www.uu.se/en/department/peace-and-conflict-research/research/ucdp/definitions

### Weak state capacity matters more than diversity by itself

James Fearon and David Laitin argue that conditions favoring insurgency, including weak state capacity, rough terrain, political instability, and low administrative reach, explain civil-war onset better than ethnic or religious diversity by itself.

Design translation:

- low State Authority, broken rail links, divided command, occupation, weak local administration, and inaccessible territory raise hidden Fracture Pressure
- cultural or regional identity is never enough on its own
- an Event 006 package becomes relevant only when its regional institutions, claims, organization, and territory are valid
- stable diverse countries can receive limited crises
- fragile countries with organized actors can receive severe crises

Source:

- James D. Fearon and David D. Laitin, Ethnicity, Insurgency, and Civil War, American Political Science Review 97, 1, 2003, DOI 10.1017/S0003055403000534, https://doi.org/10.1017/S0003055403000534

### Political exclusion and mobilization create organized challengers

Lars-Erik Cederman, Andreas Wimmer, and Brian Min connect civil conflict risk to politically excluded groups, organizational capacity, prior conflict, and the ability to mobilize. Event 021 therefore distinguishes ordinary cultural difference from a movement capable of making an armed claim.

Design translation:

- ideological popularity matters when it is paired with organization and exclusion
- regional movements need a valid package, institutions, claims, local support, or earlier autonomy conflict
- a negotiated settlement can reduce recurrence by opening peaceful access
- a harsh settlement can preserve an underground network and raise future pressure
- prior Event 021 generations matter, but they never force automatic recurrence

Source:

- Lars-Erik Cederman, Andreas Wimmer, and Brian Min, Why Do Ethnic Groups Rebel, New Data and Analysis, World Politics 62, 1, 2010, DOI 10.1017/S0043887109990219, https://doi.org/10.1017/S0043887109990219

### Regional spread comes through networks, arms, sponsors, and state weakness

Idean Salehyan and Kristian Skrede Gleditsch find that civil wars can spread across borders through rebel networks, arms, combatants, and political effects. They also state that the vast majority of refugees do not engage in violence. Event 021 therefore separates humanitarian pressure from armed political contagion.

Design translation:

- displaced civilians create administrative and relief pressure, not automatic rebellion
- cross-border recruitment, weapons routes, returning volunteers, sponsors, and ideological emulation drive armed spread
- relief corridors and military aid corridors are separate actions
- neighbors can contain, mediate, exploit, or support
- Regional Exposure changes future risk and prevention without instantly creating another civil war

Source:

- Idean Salehyan and Kristian Skrede Gleditsch, Refugees and the Spread of Civil War, International Organization 60, 2, 2006, DOI 10.1017/S0020818306060103, https://doi.org/10.1017/S0020818306060103

### Recurrence depends on unresolved hardship and blocked political access

Barbara Walter argues that renewed civil war becomes more likely when citizens face severe hardship and lack credible peaceful means to change conditions. Event 021 therefore treats the settlement as part of the event, not cleanup after the real gameplay.

Design translation:

- military victory does not erase the causes of fracture
- postwar settlement can be negotiated, punitive, revolutionary, federal, independent, or partitioned
- durable obligations and reconstruction lower recurrence
- exclusion, repression, failed reconstruction, unresolved partition, and surviving networks raise recurrence
- the visible Unsettled Settlement idea records postwar risk until recovery is real

Source:

- Barbara F. Walter, Does Conflict Beget Conflict, Explaining Recurring Civil War, Journal of Peace Research 41, 3, 2004, DOI 10.1177/0022343304043775, https://doi.org/10.1177/0022343304043775

### Multiple armed organizations make wars harder to end

David Cunningham finds that conflicts with more actors able to block settlement tend to last longer. Kathleen Gallagher Cunningham, Kristin Bakke, and Lee Seymour also show that fragmentation inside self-determination movements changes bargaining and conflict behavior.

Design translation:

- Evolution I fronts have separate objectives, relationships, momentum, and settlement positions
- defeating one side does not erase the others
- opposition coalitions can cooperate, compete, merge, or fight
- multi-front wars need independent settlement and cleanup
- AI evaluates whether a coalition or separate peace improves its position
- the event avoids several visually different sides with identical goals

Sources:

- David E. Cunningham, Veto Players and Civil War Duration, American Journal of Political Science 50, 4, 2006, DOI 10.1111/j.1540-5907.2006.00221.x, https://doi.org/10.1111/j.1540-5907.2006.00221.x
- Kristin M. Bakke, Kathleen Gallagher Cunningham, and Lee J. M. Seymour, A Plague of Initials, Fragmentation, Cohesion, and Infighting in Civil Wars, Perspectives on Politics 10, 2, 2012, DOI 10.1017/S1537592712000667, https://doi.org/10.1017/S1537592712000667

### External support changes capacity and dependence

The Stockholm International Peace Research Institute has documented the importance of external support to armed groups and the difficulty of reducing conflicts to internal factors alone.

Design translation:

- sponsors provide equipment, access, training, recognition, volunteers, and political backing
- support creates influence, dependency, exposure, retaliation, and rival sponsorship
- AI sponsor limits depend on industry, distance, ideology, relations, current wars, and strategic interest
- foreign aid never appears as free reinforcement
- settlement can preserve or reject sponsor influence

Source:

- Stockholm International Peace Research Institute, External Support in Civil Wars and Armed Conflict research materials, https://www.sipri.org/

## Historical and regional inspiration policy

The event is global and repeatable. Historical cases are used to improve the generic system, not to assign one historical script to every country.

Implementation research should inspect region-specific precedents only after a target or Event 006 package is known. Useful research categories include:

- rival constitutional governments
- army district mutinies
- regional autonomy movements
- anti-colonial or separatist organizations
- provincial congresses and emergency committees
- railway, port, mountain, island, and border defense organizations
- negotiated autonomy, federal settlement, amnesty, exile, and partition
- foreign recognition, arms corridors, and volunteer networks

The implementation must not infer that a modern ethnic, religious, or regional community is violent. A grounded independence package needs its own accepted Event 006 research, map, leaders, identity, forces, and national content.

## Strange-incident research boundary

Evolution II can contain dark rituals, oath circles, repeated symbols, night ceremonies, unusual endurance, or claims of protection from unseen forces. These are fictional high-chaos incidents attached to active sides.

They are not factual claims about a real religion, ethnicity, or historical movement.

Rules:

- no real religion is presented as the source of magical power
- no modern extremist symbol is reproduced
- no real atrocity is converted into casual occult flavor
- early reports remain uncertain
- material effects stay bounded and counterable
- one side cannot stack several strange incidents without an explicit later addendum
- another event's supernatural identity is not copied

## Research limits

The live Chaos Redux repository, current Event 006 package registry, offline Paradox wiki, installed vanilla files, and approved Workshop references were not available in this planning environment.

The implementation agent must verify:

- current civil-war engine behavior
- valid country and character ownership
- Event 006 package coverage
- exact scenario ID
- current Wars cluster registry
- valid State Authority presentation surface
- target and force allocation precedents
- current DLC-sensitive behavior
- current asset consumers and dimensions

No source in this note authorizes a final country tag, leader, flag, portrait, ideology, territory map, or political claim.
