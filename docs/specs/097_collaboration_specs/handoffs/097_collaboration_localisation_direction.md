# Event 097 Collaboration: Localisation Direction

This handoff lists every text surface Event 097 needs and the direction for each. It is direction only. Every name in this file is a working label, not final localisation. The implementation agent writes the final English text in the Chaos Redux voice and keeps it in the event's own localisation file, saved as UTF-8 with BOM, with keys written without `:0`.

## Shared voice

- Subject: ordinary people changing sides. Officials, clerks, policemen, prefects, factory directors, party secretaries, junior officers, and émigrés.
- Register: dry, observant, and uncomfortable. Irony lands on cynics, opportunists, and the officials who change flags. It never lands on people living under occupation or on victims of reprisals.
- Show behavior and objects: a second armband kept in a desk drawer, keys handed over on the town hall steps, a police inspector who already knows the new patrol routes, a ministry that reopens the morning after the city falls with the same staff.
- Do not make paperwork, archives, maps, or staff tables the main source of mystery.
- Do not label anything a warning, a threat, or a danger signal.
- Do not write staged contrasts between unofficial fear and official denial, thesis and antithesis framing, staccato chains, em dashes, or semicolons.
- Do not name real collaborators or real collaboration regimes.
- Event text never explains surrender limits, compliance values, thresholds, or formulas. Tooltips state visible consequences plainly.
- Text describes the world as it is. It never mentions updates, reworks, tuning, or caps.

## Dynamic placeholders

Final text should use these instead of fixed names:

- the receiving country's name and adjective
- the country with the strongest network inside the host, in the Fifth Column spirit tooltip, the Divided Loyalties header, and Open Gates reports
- the installer and the installed government, in Prepared Government, Turned Regime, and Installed Administration texts
- the captured state's name, in seat and Open Gates reports
- the qualitative band words for Foreign networks among us and Our networks abroad, through one scripted localisation selector each
- the Fifth Column band word, through one selector
- the restoration mood word, through one selector
- the active protective measure and its remaining days, in the Divided Loyalties header

Selectors must not write formatting characters directly. Colour for band words comes from the shared colour identity named in Part 1.

## Opening report

- Title direction: short and plain, about strangers and familiar officials who now answer to more than one government.
- Description direction: the receiving government's own services describe what they are noticing. Sympathizers have appeared in ministries, police, factories, party offices, and the officer corps. The same pattern appears abroad among people who favor this country. Nobody can find one organizer. The text shows a few concrete people rather than describing a system.
- Variant lines: a Deep Networks opening in which the contacts already sit in ministries and police headquarters, an Administrations in Waiting line about offices that seem to know which flag they will serve under, a Collaboration Governments line about exiles abroad discussing who would run their country under foreign protection, and a repeat line from the second firing onward in which the government recognizes the same faces.
- Option Accept: a resigned shrug, or the observation that a country cannot arrest its whole civil service. Slightly too comfortable.
- Option Cultivate: cold opportunism that treats foreign officials as future employees. Register changes by ruling ideology: friends of the new order for fascist governments, fraternal parties and class allies for communist governments, consular contacts and commercial goodwill for democracies, which should read as self-serving euphemism, and keeping every door open for non-aligned governments.
- Option Screen: suspicion that may turn on the speaker. The text should let the player suspect that the vetting committee contains the people it is looking for, without saying so.
- Option tooltips: the visible change to our networks abroad and to foreign networks among us, as percentages, then the current band words for both readings. Screen also shows the Vetting Campaign spirit and its duration.

## Evolution reports and log

- Deep Networks deepening report: recruitment has reached department heads, police directors, plant managers, and staff officers, and the report gives no numbers.
- Evolution log entries: one title and one short body per evolution. Titles follow Part 2: recruitment reaching the offices that matter, offices ready before the soldiers arrived, the column inside the walls, governments formed before their countries fell.
- Evolution type label: a short name for the collaboration track.
- Event Details evolution catalog: one or two sentences per evolution describing its premise without effects or numbers.

## Occupation and capitulation texts

- Seat report, capturing country: officials waiting with keys and lists, a police chief who already knows the patrol routes, a district council asking for instructions. Tone: unsettling efficiency.
- Open Ministries report, owner whose capital fell: ministries reopened the next day with most of the same staff. Grim, not melodramatic.
- Prepared cadres report, government in exile: the people who kept the provinces running under the enemy were the same people who ran them before.
- Prepared cadres state modifier name and description: local cadres who prepared the handover.
- Fifth Column spirit name: a short name using the common phrase or a period equivalent. Band descriptions: Wavering shows delay and hedging. Defecting shows offices that stop answering and local officials meeting the enemy. Collapsing shows a state already serving the victor. The tooltip names the strongest foreign network by country.
- Fifth Column acquisition report: the government learns that its own state has started to hedge.
- Open Gates, host: a district opened its doors and nobody in the capital ordered it. Option direction can be bitter.
- Open Gates, enemy: a column entered a district that was waiting for it. Option direction can be smug in a way that condemns the speaker.

## Governments

- Prepared Government event, installer: politicians, officials, and officers of the defeated country have been ready for months and ask to govern under the installer's protection. Install option: a practical arrangement the speaker knows is cynical. Keep direct occupation option: distrust of people who already betrayed one government. Democratic installers use provisional-administration wording, which should read as self-serving euphemism.
- Installed Administration spirit stages: imposed and resented, entrenched and comfortable, contested and frightened, abandoned and alone.
- Turned Regime, former installer: a government it created now answers to its enemy. New master: a government arrived prepared for the second time. The installed government: the same officials change sides again. The irony lands on the officials, not on the population.
- Auxiliary template name: police and gendarmerie raised by the network. The working label is Auxiliary Police.
- Restoration mood line in exile reports: the mood in the occupied homeland, using the selector words for the three restoration bands.

## Decisions

- Divided Loyalties category name and description: a government trying to keep its own state loyal during a war. The header lines are written as game text, with no pipes, dividers, or raw variable names.
- Prepared Governments category name and description: installing and sustaining governments made from prepared networks, described as an administrative act everyone involved understands.
- Decision names and descriptions describe concrete measures: commissions, arrests, evacuated ministries, military commissars in civilian offices, ministers sent abroad with reserves, a sash and a chair for the prepared government, rifles for the auxiliaries. Descriptions explain visible effects and never reveal hidden thresholds, band formulas, or variant chances.
- Blocked tooltips name the exact requirement, such as the stability minimum or the missing seated state.
- Vetting Campaign and Loyalty Commissions spirit names and descriptions: a state that checks its own servants and pays for it in stability and supply.
- Collaborators Unmasked: Purge is the voice of a returning government that wants visible punishment, and its irony can point at how fast the same officials denounce each other. Amnesty is cold pragmatism: the trains must run and nobody else knows how. Neither option makes light of reprisals.

## Event list, history, and Chaos history

- Event name: the existing name Collaboration stays.
- Event Details premise: sympathizers ready to serve foreign governments have appeared in every country at once, each government has the same abroad, and the networks grow deeper as the world grows more unstable. No effects, numbers, stances, or evolution rules.
- Event Details current-state line: one qualitative word or short phrase, such as first contacts, spreading, or entrenched.
- Unavailability reasons: one short reason for too few participants and one for a pass still in progress, in both the event list and the cluster member list.
- Chaos history reasons: one short line for each row of the Chaos impact map, describing the outcome in the past tense.

## Achievements

Achievement titles and descriptions follow the directions in `prompts/097_collaboration_achievement_prompt.md`. Descriptions state the requirement clearly. Event, decision, and report text never mention achievements.

## Super-event

The super-event title, description, quote, button remark, and audio are research-gated and follow `prompts/097_collaboration_super_event_prompt.md`. No working label may become final super-event text.

## Spreadsheet wording

The catalog Details field matches the Event Details premise, and the four evolution fields match the Event Details evolution catalog text. See `handoffs/097_collaboration_catalog_alignment.md`.
