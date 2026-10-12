# Event 030: Time Traveler

Major event, Chaos level 1 (Calm World), no cluster, fires once per campaign. Specification: `docs/specs/030_time_traveler_specs/`. Accepted scope and deferrals are recorded in the status table of its README.

## What it is

A man who remembers a later time appears in one country and proves it. The host chooses how he works with the state, and the strongest rewards come from consultations whose objectives the government carries out. Foreign countries compete for him and for the copied knowledge. Three public values describe the situation: Credibility (current custodian), Exposure (the traveler) and Timeline Divergence (global), each with three bands.

## Event map

Namespace `chaosx.nr30`. Baseline in `events/030_time_traveler.txt`, Evolution I in `events/030_time_traveler_evolutions.txt`, the three Evolution II figures in `events/030_time_traveler_figures.txt`.

| Id | Role |
| --- | --- |
| `.1` | hidden entry on the host drawn before the history row is accepted |
| `.2` | opening report, five ways to handle the visitor |
| `.3` to `.7` | remembered war variants: Germany and the Soviet Union (`.3` to `.6`), the United States and Japan (`.7`) |
| `.10`, `.11`, `.12` | first proof, second proof (verification), forecast checked |
| `.13`, `.14`, `.55` | access arrangement, revision, leaving by agreement |
| `.15`, `.16` | the visitor is turned away, a shared forecast reaches an ally |
| `.20` to `.24` | family picker, offer, success, partial, failed |
| `.30` to `.39`, `.54` | AI rival turn, compromised staff, forged advice, asylum refused, seizure report, archive copied, caught cell, operation report, captured double, sting, bait |
| `.40` to `.46` | rumor dispatcher and the six rumors |
| `.50` to `.53` | a human country learns it may act, custody lost, traveler killed, traveler vanished |
| `.100` to `.151` | Evolution I: pacing tick, the crisis and its eight routes, resolution report, emergency authority ends, attempted removal, coup or revolt, defeat, changing the remembered war, reappearance |
| `.200` to `.234` | Evolution II: hidden pacing tick (`.200`) and four stage events per figure (Napoleon `.211` to `.214`, Joan `.221` to `.224`, Frederick `.231` to `.234`) |
| `chaosx.news.300` to `.302` | public revelation, the Berlin-Moscow Axis, intelligence on Japan |

## Runtime flow

1. The shared fire dispatcher calls `time_traveler_prepare_random_event_fire`, which draws one host from the major countries and the player countries. The weight is 16 for a player country and 2 for an AI major, multiplied by the individual-crisis ticket curve (a country with three crisis packages is out, one with one or two is less likely). Special Chaos actors, actual nonhuman countries and capitulated countries are excluded. An empty pool leaves the event unconsumed and the event list shows the Not Available reason.
2. `.1` runs `time_traveler_begin` on the host: status, custodian, profile (analyst, engineer or historian, chosen from war, industry and stability), arrival state (capital if controlled and not next to an enemy, otherwise the safest core state), starting values and the opening report. Above the first Chaos threshold the opening is compressed: Exposure is higher and the forecast proof is skipped.
3. `.2` offers five handlings. Dismissing the visitor ends direct access, moves Divergence a little and records the disappearance.
4. `.10` and `.11` are the proofs. They read the host's own state (agency, procurement or research, the head of government). Two proofs verify the traveler. `.12` compares the Chaos meter with the value recorded when the forecast was made, and the result moves Credibility.
5. `.13` sets one of four arrangements (Cabinet Advisor, Secret Program, Confinement, Public Recognition). The first choice installs the character, opens the category, schedules the first offer, builds the interest registry and starts the rumor chain. The spirit moves from Unverified Forecasts to Directed Foreknowledge.
6. Consultations. The `Consult the visitor` decision opens `.20`. Each listed family resolves a real objective for the custodian, `.21` shows recipient, objective, deadline, reward, precision and spread, and committing pays the quote and starts one mission. The mission completes by itself when the objective is observed. At the deadline it resolves as partial (part observed, with a choice to press on once) or failed with a named cause: a recorded forgery, a recorded timeline change (Divergence rose by 8 or more since the offer) or an ignored objective.
7. Three successful consultations raise the spirit to Distributed Future Knowledge and set the durable baseline outcome (trusted advisor, confined asset or public figure). The spirit stage never stacks.
8. The intelligence war runs in the background (see below).

## Public values

Stored as `time_traveler_credibility` and `time_traveler_exposure` on the custodian and `global.time_traveler_divergence`. Bands are in `time_traveler_band` of the constants. Values change only through `time_traveler_raise_*` and `time_traveler_lower_*`, which clamp to 0 to 100 and record the cause. The category header prints the three values, their band names, what the band allows, the arrangement and the last three causes (`global.time_traveler_recent`). Public Recognition or any revelation fixes Exposure at the Public band for the campaign. Divergence never drifts and is not lowered by anything in the baseline.

## Consultation families

| Family | Objective shell | Costs (scaled by factories) | Reward |
| --- | --- | --- | --- |
| Military forecast | place N divisions in a front state or the capital | army experience, command power, support equipment | army experience and a planning window with stronger attack, defence and entrenchment |
| Industrial bottleneck | raise a core state's infrastructure by two levels | fuel, trains | one more infrastructure level and long-lasting factory efficiency |
| Scientific shortcut | complete one of five named technologies | support equipment, political power | research bonus for the next technologies of the field |
| Diplomatic forecast | raise a neighbor's opinion, or the remembered war variants | political power | goodwill and a non-aggression pact, or the legacy faction |
| Counterintelligence map | garrison the arrival site | command power, support equipment | Exposure down, one foreign network set back, cheaper next sting |
| Domestic threat assessment | garrison a state with resistance or the capital | political power, command power | stability and weaker resistance for a time |

Germany with the Soviet Union alive gets the Berlin-Moscow pact as its diplomatic offer, the United States gets a Hawaii garrison objective plus intelligence on Japan. Both reuse the retired legacy chain. Each variant fires once per campaign, and a shared forecast gives an ally its own variant.

## Arrangements and the profile

The profile decides the strongest families (analyst: military, diplomatic, counterintelligence. engineer: industrial, scientific. historian: domestic, diplomatic). Strong families cost 20 percent less, recover sooner and pay 25 percent more. The Secret Program lists only the two strongest families and counterintelligence. Confinement halves Credibility gains. Public Recognition fixes Exposure at Public, shortens the cooldown and pays prestige once.

## Intelligence war

The registry `global.time_traveler_interest` holds at most 2, 4 or 6 countries for the Secret, Suspected and Public bands. It is rebuilt only after a public revelation, a custody transfer or at the first access, scoring majors, players, agencies, enemies, neighbors and allies. A member carries a hidden network level from 0 to 3. AI members act through the self-rescheduling hidden event `.30` (interval from `time_traveler_rival_interval`), human members through four decisions. Operations: infiltrate (three steps: schedules, a recruited staff member and a Future Fragment, the archive and the first theft milestone), plant forged advice, offer asylum, seize the traveler (Public band, mature network). Countermeasures: move the traveler, guard detail, sting (with a possible decoy and a bait escalation), share a forecast with an ally. A captured double never becomes a second traveler. Custody transfer moves the character, category, crisis slot, Exposure and registry, recalculates Credibility from the method and leaves the old custodian a reduced Scattered Forecasts spirit. Annexation of the custodian passes custody to the winner or the traveler vanishes (`on_annex`).

## Event-owned Chaos changes

Two one-shot milestones through the shared history path: the first verified public revelation (reason `time_traveler_revelation`) and the first successful foreign theft of the archive (reason `time_traveler_theft`). Evolution state gives zero Chaos.

## AI

Custodian: arrangement weights in `common/mtth/030_time_traveler_mtth.txt` (war and ideology favor the Secret Program, low stability favors Confinement, a democracy at peace favors the Cabinet), family weights from war, stability, Exposure and profile, decision weights from Exposure and the quote. Rivals: roulette over infiltrate, forge, asylum, seize and restraint from agency, hostility, ideology and alliance, with one seizure attempt per country. AI rivals pay nothing for their operations, human rivals pay the quoted cost.

## Supporting systems touched

Event categories and the Not Available reason (`chaosx_logic_effects.txt`), the shared fire dispatcher (`chaosx_settings_effects.txt`), default enable list (`chaosx_settings_triggers.txt`), event log default actor, Event Details text, Chaos history reasons 300 and 301, individual-crisis provider (custodian flag, `individual_crisis_targeting_triggers.txt`), Event 016 contact bridge and Temporal Theory gate (both now read `time_traveler_has_direct_access`), `on_annex`, achievements.

## Evolution I: The Traveler's Ambition

Gate: Chaos 200 and above (shared tier gate through `is_current_evolution_enabled`), a verified traveler with direct access and about 105 days after the gate, shortened or lengthened by `mtth:time_traveler_ambition_delay` (an Indispensable traveler, Cabinet or Public access, an unsettled government and repeated successes shorten it, Confinement and doubt lengthen it). A hidden tick every 30 days on the custodian runs the check, and a compressed opening makes the crisis due at once. Activation gives zero Chaos and writes one Event Log row with the custodian as actor.

Three hidden blocs of the custodian (Government, Security, Technocrats, 0 to 100) are seeded by the arrangement and moved by carried-out consultations. They are never shown as numbers.

`chaosx.nr30.101` opens the crisis with wording that follows the arrangement. The routes are:

| Route | Resolution |
| --- | --- |
| Charter | the traveler stays an adviser under written terms, Government grows, Security shrinks, Chaos falls once. Two ignored consultations break the charter and reopen the crisis |
| Emergency authority | six months of a strong timed spirit, then a report: stability above half makes his methods a permanent institution, otherwise Credibility falls, Security grows and the crisis escalates |
| Appointment | passes only with Government support and one more bloc, otherwise the cabinet refuses and the supporters move |
| Open contest (democracies) | chance from the Government and Technocrat blocs, a win makes him leader, a loss asks what is to become of him |
| Arrest and investigation (needs an agency) | a clean arrest needs the Security bloc to stay away, success dismantles the blocs and may name a foreign sponsor, failure is a rescue attempt that becomes a coup |
| Exile | the traveler leaves, a reappearance after about 300 days with one of three explanations (a gap in time, a foreign service, a staged disappearance) |
| Transfer to an ally | a negotiated custody transfer |
| Secret removal | success removes him without a report, failure is a public scandal that joins the shared condemnation record and brings the officers out |

Escalation: an attempted removal (`.110`) offers giving way, arrest or a charter. The officers act in `.111`: a civil war needs a very strong Security bloc, a weak Government bloc and at least eight controlled states, a coup needs a strong Security bloc, otherwise the attempt fails, the traveler is arrested and Chaos rises once. The civil war uses `start_civil_war` with the traveler leading the rebels.

When he governs, `time_traveler_trait_leader` and the Traveler Government spirit apply, consultations close, and a category of five decisions opens: watch the predicted threat, restrict future offenders, change the remembered war (a deterrent or a mobilization, with higher world tension and no war goal), build the successful institution and suppress the failed one. Peaceful routes (appointment, contest, giving way) move Chaos once and, when no coup or civil war has brought him to power anywhere, count towards I Have Seen This Office Before.

## Evolution II: The Door to the Past

Accepted tranche: Napoleon Bonaparte and Joan of Arc (France), Frederick the Great (Germany). Gate: Chaos 400 and above, Evolution I resolved, closed or bypassed (disabled, or no custodian can run it), fewer than three active packages. A hidden tick on FRA and GER makes a figure due about 135 days after the gate, slower in a Recognizable timeline and faster in a Broken one, with a public traveler, a lost traveler or several foreign copies.

One scaffold, one event per stage: arrival with an authenticity test (language, archive or the army), custody (protect, present publicly, detain, military consultation), the movement and power decision, and the resolution report. The hidden movement support (0 to 100, `global.time_traveler_fig_support`) starts at 30 and rises or falls with every choice. Routes: adviser or commander (limited modernity: weak logistics and the traits of another century), national symbol (spirit), office (needs support, makes the figure leader in the ruling ideology with a restoration spirit, moves Chaos once), suppression (the movement may answer with arms, the figure may die in custody), exile (a timed claimant movement) and the claim (a civil war with enough support and states, a smaller revolt with a fighting movement, otherwise the claim fizzles). Joan needs more support than the rulers to take up arms.

A resolved figure never arrives again. Resolving the three packages without a death or a full civil war earns Nine Lives of History for the human hosts and custodians.

## Assets

Wired in `interface/030_time_traveler.gfx`: the main category icon and the foreign intelligence category icon, the consultation category picture, 14 decision icons, six idea icons (the sixth is the Traveler Government spirit), the baseline arrival report image, separate Jonas Calder country-leader and advisor portraits, and the achievement triplets of the four implemented achievements (The Future Refused, No One Owns Tomorrow, I Have Seen This Office Before, Nine Lives of History). The generated DDS files live under `gfx/interface/decisions/030_time_traveler/`, `gfx/interface/ideas/030_time_traveler/`, `gfx/event_pictures/030_time_traveler/`, `gfx/achievements/`, and `gfx/leaders/030_time_traveler/`.

### Assets still needed

- Baseline super-event: the image `gfx/super_events/030_time_traveler/super_event_030_time_traveler_baseline_arrival.dds` exists, the sourced quote and the licensed audio do not, so the super-event is not wired.
- High divergence category picture variant `decision_category_030_time_traveler_high_divergence.dds` exists and is not wired yet.
- The GUI value icons (`gfx/interface/scripted_guis/030_time_traveler/`) are unused because the header is text.
- Portraits for Napoleon Bonaparte, Joan of Arc and Frederick the Great: attributed painting, sculpture or coin sources through the portrait worker, one token each. The characters have no portrait wired. Their spirits, the leader traits and the Evolution II events use vanilla idea pictures and generic report images.
- Restoration identities: a cosmetic tag, flag and name for a restored France or a restored Prussian monarchy are not made. The office route changes the leader and adds a spirit only.
- Icons of later phases (incident, node, stance, alignment emblems, state modifier, Closed Future flag) are on disk and are wired by their phases.

## Limitations of the baseline

- Proofs one and two read the host's own state and always hold. Verification decides Credibility and Exposure, not authenticity. The forecast proof compares the world's Chaos with the value recorded at the forecast.
- A consultation's doctrine result through Event 027 and the custom technology grant of Event 016 are not connected. Rewards use experience, timed spirits, infrastructure, research bonuses, pacts and Exposure.
- A mission that is running when custody changes is closed without penalty. Knowledge that already spread does not continue under the old government.
- A registry member that is annexed stays in the array until the next rebuild. Decisions check that the target exists.
- Event 016's Kruger prototype and deployment do not call a Divergence adapter yet. The constants `time_traveler_divergence.kruger_prototype` and `kruger_deployment` are reserved for it.
- The catalog workbook rows for Event 30 are not updated.
- Evolution I does not call the camp owner's custody intake for preventive detention. The program uses ordinary custody, creates no camp and counts no deaths, and a public program joins the shared condemnation record. The intake needs a stable request API from the camp owner.
- The civil war of Evolution I and Evolution II uses `start_civil_war` with a fixed rebel group (neutrality, or democratic for a neutral host) and the figure or traveler leading the rebels. It does not model a restored identity or a new country.
- Evolution II hosts are France (Napoleon, Joan) and Germany (Frederick) only. The six other figures of Part 5, the conflict between two figures of one region and the modern named visitors are deferred. A returned figure in an integrated role does not retire.
- Nothing was run in the game.
