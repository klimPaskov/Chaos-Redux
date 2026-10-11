# Event 030: Time Traveler

Major event, Chaos level 1 (Calm World), no cluster, fires once per campaign. Specification: `docs/specs/030_time_traveler_specs/`. Accepted scope and deferrals are recorded in the status table of its README.

## What it is

A man who remembers a later time appears in one country and proves it. The host chooses how he works with the state, and the strongest rewards come from consultations whose objectives the government carries out. Foreign countries compete for him and for the copied knowledge. Three public values describe the situation: Credibility (current custodian), Exposure (the traveler) and Timeline Divergence (global), each with three bands.

## Event map

Namespace `chaosx.nr30`, file `events/030_time_traveler.txt`, evolutions in `events/030_time_traveler_evolutions.txt`.

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

## Assets

Wired in `interface/030_time_traveler.gfx`: the main category icon and the foreign intelligence category icon, the consultation category picture, 14 decision icons, five idea icons, the baseline arrival report image and the achievement triplets of the two baseline achievements. The generated DDS files live under `gfx/interface/decisions/030_time_traveler/`, `gfx/interface/ideas/030_time_traveler/`, `gfx/event_pictures/030_time_traveler/` and `gfx/achievements/`.

### Assets still needed

- Portrait for Jonas Calder (fictional): advisor portrait and later the country-leader portrait, through the portrait worker. The character has no portrait wired and shows the engine silhouette.
- Baseline super-event: the image `gfx/super_events/030_time_traveler/super_event_030_time_traveler_baseline_arrival.dds` exists, the sourced quote and the licensed audio do not, so the super-event is not wired.
- High divergence category picture variant `decision_category_030_time_traveler_high_divergence.dds` exists and is not wired yet.
- The GUI value icons (`gfx/interface/scripted_guis/030_time_traveler/`) are unused because the header is text.
- Icons of later phases (incident, node, stance, alignment emblems, state modifier, Closed Future flag) are on disk and wired by their phases.

## Limitations of the baseline

- Proofs one and two read the host's own state and always hold. Verification decides Credibility and Exposure, not authenticity. The forecast proof compares the world's Chaos with the value recorded at the forecast.
- A consultation's doctrine result through Event 027 and the custom technology grant of Event 016 are not connected. Rewards use experience, timed spirits, infrastructure, research bonuses, pacts and Exposure.
- A mission that is running when custody changes is closed without penalty. Knowledge that already spread does not continue under the old government.
- A registry member that is annexed stays in the array until the next rebuild. Decisions check that the target exists.
- Event 016's Kruger prototype and deployment do not call a Divergence adapter yet. The constants `time_traveler_divergence.kruger_prototype` and `kruger_deployment` are reserved for it.
- The catalog workbook rows for Event 30 are not updated.
- Nothing was run in the game.
