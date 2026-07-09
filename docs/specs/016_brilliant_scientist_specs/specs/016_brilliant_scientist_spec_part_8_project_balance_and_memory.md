# Event 16 Brilliant Scientist, project balance and memory

All project names in this file are working labels, not final localisation. This section deepens the project system from the core spec and should be folded into the project and decision specs if accepted.

## Balance model purpose

Kruger projects should feel profitable before they feel safe. Every approval should give visible research value, unlock a field, or solve an immediate problem. The price is not a simple penalty. The price is a trail of facilities, staff, authority, material, and secrecy that the host may later lose control over.

Each project writes three kinds of memory:

- a visible facility summary for the player, such as public institute, sealed reactor, prototype range, specimen wing, or automated foundry
- a hidden project memory used for evolution pacing, rebellion strength, focus branch unlocks, foreign reactions, and achievements
- a project intensity value that records whether the host approved the cautious, military, or reckless version of that project

The project system should avoid a wall of buttons. The host sees only the current field, the next safe project, and the next dangerous project revealed by the current route. AI can evaluate hidden candidates through scripted weights.

## Shared balance values

Use these planning values as the balance vocabulary. Implementation can translate them into variables, constants, scripted effects, and dynamic localisation.

| Value | Range direction | Raised by | Lowered by | Use |
| --- | --- | --- | --- | --- |
| Country Scale Band | 1 to 5 | factories, research slots, manpower, major status | subject status, low industry | converts absolute costs into fair burdens |
| Project Tier | 1 to 5 | later phases and higher danger | safe public variants | drives duration, material cost, and risk |
| Field Danger | 1 to 5 | biology, nuclear, xenotech, time, final device | public mathematics, civil medicine | drives accident and rebellion value |
| Project Load | 0 upward | active projects and repeated approvals | completed audits and cooldowns | prevents project spam |
| Containment Gap | 0 upward | Autonomy, Strangeness, risky memories | Security Integrity and Government Leverage | drives accident, defection, and revolt risk |
| Foreign Heat | 0 upward | Public Fame, military successes, rival incidents | observers, treaties, counterintelligence | drives theft, invitation, sabotage, and pressure |
| Arsenal Weight | 0 upward | dangerous project memories | prototype destruction, evacuation, containment | drives Kruger starting army if he secedes |

## Shared formula families

These formulas are design formulas. They should be implemented with constants, helper effects, and readable scripted localisation rather than scattered numbers.

### Facility cost formula

Use for public institute, computation rooms, medicine wards, and other early projects.

- Civilian factory burden equals base 1 plus Country Scale Band, plus Project Tier, plus half of Project Load, minus Government Leverage Band. Bound the result between 1 and 8.
- Duration equals base 90 days, plus 15 days per Project Tier, plus 8 days per Project Load, minus 6 days per Industry Band. Bound the result between 60 and 210 days.
- Stability pressure equals Field Danger plus Public Fame Band, minus Government Leverage Band. Apply it as a temporary political strain when the result is positive.

### Military prototype formula

Use for weapons ranges, rockets, nuclear work, robots, and guarded field tests.

- Military factory burden equals base 1 plus Project Tier, plus War Pressure Band, plus half of Country Scale Band, minus Security Integrity Band. Bound the result between 1 and 10.
- Equipment burden equals base equipment package multiplied by 1 plus 0.20 per Country Scale Band, plus 0.15 per Chaos Band, plus 0.10 per Laboratory Autonomy Band.
- Army XP or Air XP burden equals base 15 plus 5 per Project Tier, minus 3 per existing related project memory. Bound the result between 10 and 60.
- Duration equals base 120 days, plus 20 days per Project Tier, plus 10 days per Field Danger, minus 5 days per Security Integrity Band.

### Sealed project formula

Use for cloning, creatures, xenotechnology, teleportation, temporal work, and any project where ordinary ministries cannot inspect the site.

- Civilian factory burden equals base 2 plus Project Tier, plus Country Scale Band.
- Military factory burden equals base 1 plus half of Project Tier, plus one if the country is at war.
- Support equipment burden equals base package multiplied by 1 plus 0.25 per Field Danger, plus 0.20 per Containment Gap Band.
- Security staff burden equals base manpower package multiplied by 1 plus 0.15 per Public Fame Band, plus 0.20 per Foreign Heat Band.
- Duration equals base 150 days, plus 25 days per Project Tier, plus 15 days per Field Danger, minus 8 days per Industrial Automation Memory.

### Emergency containment formula

Use for destroying prototypes, quarantining labs, evacuating staff, and delaying final device work.

- Security requirement equals Field Danger plus Autonomy Band, plus Project Tier, minus Government Leverage Band.
- Required loyal divisions equals 1 plus half of Project Tier, plus one if the lab state is isolated, plus one if clone or robot memories exist.
- Equipment burden equals base security package multiplied by 1 plus 0.30 per Containment Gap Band.
- Failure risk equals base 20, plus 8 per Autonomy Band, plus 8 per Strangeness Band, plus 6 per Field Danger, minus 7 per Government Leverage Band, minus 7 per Security Integrity Band.

### Final device formula

Use only after Kruger sovereignty or host surrender to laboratory rule.

- Progress gain each cycle equals base progress, plus nuclear memory, plus temporal memory, plus xenotech memory, plus automation memory, plus controlled reactor count, plus captured major research center count.
- Progress loss from sabotage equals sabotage success value, plus intelligence superiority, plus air access, plus local resistance, minus Kruger Security Band.
- Arming urgency rises when Kruger is close to capitulation, when his capital is threatened, or when he has lost a final-device component state.
- Completion should raise chaos above the world-end threshold when needed, then route into the fallout terminal branch.

## Risk score model

Every project should update a project risk score when started and when completed.

Risk score equals base project risk, plus 10 per Field Danger, plus 8 per Laboratory Autonomy Band, plus 6 per Strangeness Band, plus 5 per Chaos Band, plus 4 per previous dangerous project, minus 8 per Security Integrity Band, minus 8 per Government Leverage Band, minus 5 if a peer review route is active.

Risk outcomes use bands:

| Risk band | Outcome direction |
| --- | --- |
| 0 to 24 | Normal success, modest memory |
| 25 to 49 | Success with visible strain, foreign attention, or staff concern |
| 50 to 74 | Success with incident roll and stronger project memory |
| 75 to 99 | Success with severe incident, possible foreign theft, panic, or hidden revolt preparation |
| 100 upward | Immediate crisis candidate, especially during Evolution III or IV |

## AI project willingness model

AI willingness should use a base score per project, then route and situation modifiers. AI should not use human-only GUI clicks. It should call the same decision effects through AI decisions or scripted pulses.

General AI modifiers:

| Condition | Modifier direction |
| --- | --- |
| at major war | raises military, rockets, nuclear, medicine, automation, and final device work |
| democratic and stable | raises public science, medicine, peer review, and computation |
| authoritarian and at war | raises military lab, sealed projects, robotics, and biological weapons |
| low industry | lowers sealed projects, final device, robots, and nuclear projects |
| high chaos | raises risky projects and reduces restraint preference |
| low stability | lowers public fame projects and severe autonomy projects |
| high Autonomy with low Leverage | lowers arrest, raises bargains, raises late concessions |
| Kruger sovereign | ignores host ethics and weights conquest usefulness |

## Project-by-project table

| Working project label | Unlock | Cost formula | Risk factors | AI base and major modifiers | Memory outputs | Kruger rebel output |
| --- | --- | --- | --- | --- | --- | --- |
| University synthesis network | Baseline or Evolution I public route | Facility cost formula with low Field Danger and added stability requirement | public fame, foreign heat | base 70, plus stable democracy, plus high research slots, minus authoritarian secrecy | `kruger_mem_public_institute`, public facility intensity | safer start, lower rebel army value unless later converted |
| Applied mathematics bureau | Baseline public or secret route | Facility cost formula with low material cost and longer duration | weak foreign theft, academic rivalry | base 65, plus electronics route, plus public route | `kruger_mem_mathematics`, theory intensity | unlocks computation and temporal prerequisites |
| Radio computation annex | Evolution I | Facility cost formula with electronics equipment burden | theft, code leaks, AI planning | base 70, plus war, plus intelligence agency, plus electronics route | `kruger_mem_computation`, codebreaker intensity | automated targeting and cybernetic command staff |
| Industrial catalysis line | Evolution I | Facility cost formula with extra civilian factory burden and resource access requirement | industrial accidents, labor unrest | base 75, plus low production efficiency, plus major status | `kruger_mem_industrial_catalysis`, factory intensity | faster rebel industry and prototype production |
| Metallurgical miracle foundry | Evolution I or II | Military prototype formula with steel or rare-material requirement | factory fires, hidden stockpiles | base 60, plus tank or artillery production, plus war | `kruger_mem_miracle_foundry`, material intensity | elite armor, shielded weapons, stronger fortifications |
| Rocket test range | Evolution I or II | Military prototype formula with Air XP and fuel burden | crashes, foreign observation, delivery system escalation | base 60, plus air focus, plus war with large enemy | `kruger_mem_rocketry`, delivery intensity | long-range strikes and final device delivery progress |
| Medical acceleration ward | Evolution II | Facility cost formula with hospitals or support equipment burden | suspicious recoveries, missing patients | base 75, plus high casualties, plus outbreak pressure | `kruger_mem_medicine`, humane biology intensity | medical clone support if later corrupted |
| Cryptographic engine room | Evolution II | Facility cost formula with intelligence agency preference | theft, spy purges, false positives | base 65, plus intelligence agency, plus rival nearby | `kruger_mem_cryptography`, secrecy intensity | resistance to sabotage and stronger foreign manipulation |
| Sealed reactor program | Evolution II or III | Military prototype formula with civilian factory burden and reactor-state preference | nuclear accident, final device prerequisite | base 45, plus nuclear focus, plus at war, minus low industry | `kruger_mem_reactor`, nuclear intensity | final device prerequisite, reactor guard units |
| Autonomous foundry brain | Evolution III | Sealed project formula with industrial automation memory discount | control loss, machine loyalty drift | base 45, plus automation memory, plus authoritarian war state | `kruger_mem_ai_foundry`, machine intensity | robot foundries and automated production |
| Synthetic labor cells | Evolution III | Sealed project formula with support equipment and manpower burden | labor scandal, identity confusion | base 35, plus manpower shortage, plus high casualties | `kruger_mem_synthetic_labor`, biology intensity | cheap labor, clone logistics, obedience networks |
| Clone compliance program | Evolution III | Sealed project formula with medicine memory discount and heavy security staff | rebellion manpower, atrocity exposure, staff disappearance | base 30, plus desperate manpower shortage, plus authoritarian route | `kruger_mem_clone_program`, clone intensity | clone divisions and manpower regeneration |
| Prototype organism wing | Evolution III | Sealed project formula with biology, supply, and quarantine burden | escaped creatures, panic, nonhuman classification | base 25, plus high chaos, plus biological route | `kruger_mem_specimen_wing`, organism intensity | monster units, fear tools, occupation terror |
| Dinosaur recovery chamber | Evolution III rare project | Sealed project formula with extra duration and specimen prerequisite | containment breach, supply burden, public panic | base 10, plus high chaos, plus specimen memory, player higher than AI | `kruger_mem_dinosaur_chamber`, prehistoric intensity | dinosaur shock formations, huge supply strain |
| Xenotech ballistics range | Evolution III | Military prototype formula with alien material requirement or alien event memory | alien confirmation, foreign panic, diplomatic rupture | base 25, plus alien-event memory, plus high chaos | `kruger_mem_xenotech_range`, alien weapon intensity | alien guns, shields, and specialist infantry |
| Teleportation gate | Evolution III or IV | Sealed project formula with computation and rocketry memory discounts | missing units, supply distortion, impossible raids | base 20, plus war, plus large front distance, plus high chaos | `kruger_mem_teleportation`, logistics anomaly intensity | teleport raids and impossible encirclement decisions |
| Temporal observatory | Evolution IV | Sealed project formula with mathematics and computation prerequisites | time accidents, duplicate staff, failed predictions | base 15, plus high chaos, plus time-event memory | `kruger_mem_temporal_observatory`, temporal intensity | prediction focuses, time-displaced units, event resets |
| Final equation device | Evolution IV sovereign or surrendered route | Final device formula with reactor, temporal or xenotech, rocketry or teleportation, and major industry inputs | fallout world-end, sabotage race, capitulation trigger | base 5 for host, base 80 for sovereign Kruger with prerequisites, plus desperation | `kruger_mem_final_device`, terminal device progress | world-end branch if completed and fired |

## Project memory outputs by family

| Memory family | Visible player summary | Hidden use |
| --- | --- | --- |
| Public institute | open laboratories and university patrons | safer research route, foreign attention, public achievements |
| Computation | calculation rooms and encrypted machines | electronics bonuses, AI path prerequisites, sabotage defense |
| Automation | automated foundries and factory mathematics | robot route, rebel production, final device progress |
| Medicine | accelerated recovery and impossible trials | civilian medicine, clone prerequisite, outbreak interaction |
| Rocketry | test ranges and delivery systems | missile path, final device delivery, air defense |
| Nuclear | sealed reactor and theoretical physics | final device prerequisite, nuclear route, reactor defense |
| Clone | replicated labor and controlled populations | clone armies, manpower, ethical scandal |
| Robot | machine overseers and autonomous production | robot armies, low manpower route, security drift |
| Specimen | contained organisms and field pens | monsters, dinosaurs, panic, nonhuman hooks |
| Xenotech | alien material and impossible weapons | alien infantry, shields, Tomorrow's Girls connections |
| Teleportation | gate rooms and missing-distance logistics | strategic raids, supply bypass, reality accidents |
| Temporal | observatories and repeated experiments | time route, prediction focuses, final device acceleration |
| Final device | terminal equations and component sites | world-end race, final super-event, achievement hooks |

## Balance guardrails

- Safe projects should be strong enough to tempt public and democratic hosts.
- Risky projects should be stronger than safe projects in immediate output, but should add more Arsenal Weight and Containment Gap.
- No project should be a flat political power purchase.
- Repeating the same project family should increase Project Load and make accidents more likely.
- Project memories should never be cleared casually. They are campaign history.
- Destroying prototypes should remove or reduce rebel output from that family, but should not erase the fact that the host approved the work.
