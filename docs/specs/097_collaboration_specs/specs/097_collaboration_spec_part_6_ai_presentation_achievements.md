# Event 097 Collaboration: Part 6, AI, Presentation, Achievements, and Compatibility

## AI design principle

Event 097 changes every war in the world, so AI behavior matters more than any single popup. The AI must use the event's tools in ways that make sense for its situation, and the event must never start wars on its own. Event 097 adds no AI strategy that makes a country declare war, seek new enemies, or change its target selection outside an existing war. It only changes how existing wars end and how occupations are held.

All weights in this part are intended orderings. Exact values must come from the scenarios in `matrices/097_collaboration_ai_probability_scenarios.md` and must be audited through `chaosx_ai_probability_auditor`.

## AI actor groups

| Actor group | Recognized by | Opening stance preference | Wartime behavior |
| --- | --- | --- | --- |
| Expanding power | Major or regional power at war, or with an active war goal or war-preparation focus | Cultivate | Takes the prepared-government offer when it needs garrisons elsewhere. Uses B1 and B2 actively. Rarely takes A1 unless its own Fifth Column appears. |
| Threatened neighbor | Borders an expanding power with a claim on it, or is already losing a war | Screen | Takes A1 early, A3 and A4 at Collapsing, and A5 when it has allies who will fight on. |
| Neutral or isolated state | No war, no threatening neighbor | Accept | Rarely visible to the decision layer. |
| Democracy at peace | Democratic ruling party, no war | Accept, with Screen rising if a fascist or communist neighbor is expanding | Uses A5 readily, because it expects a government in exile to fight on. Takes the prepared-government offer at reduced weight. |
| Ideological revolutionary | Communist or fascist government with an active expansion route | Cultivate | As expanding power. |
| Installed government | Government installed through Event 097 | Accept, or Screen when Contested | Uses A1 and A3 in its own wars. Never seeks a new overlord except through Turned Regime. |
| Country in civil war | Active civil war | Accept, because Screen is blocked | Uses A1 only if stability allows it. |

### Opening stance weights

The stance choice is the decision most AI countries will make, so its ordering must be checked across the whole world.

- An expanding power at war prefers Cultivate strongly, but the weight falls when its own surrender progress passes 20 percent, because a cultivator becomes easier to defeat.
- A threatened neighbor prefers Screen, but the weight falls when its stability is near the minimum, because the vetting spirit could destabilize it.
- Every other country prefers Accept.
- No group should end with a near-zero chance for Accept. The world must not polarize into cultivators and screeners in every firing.

### Prepared-government offer weights

- Install when the installer controls most of the host's cores and is fighting on another front.
- Keep direct occupation when the installer plans to annex the territory through a peace conference it expects to win soon, or when the installer is itself losing.
- A democratic installer installs at lower weight.
- An installer that already holds three governments through this route installs only on its own continent.

### Evolution and variant timing

The MTTH anchors in Part 2 and the Open Gates and Turned Regime anchors in Part 3 are timing claims. They must be checked against named scenarios so that evolutions arrive in the intended windows and rare variants stay rare.

## Presentation surfaces

Final text belongs to the implementation agent. This section gives direction only. Working labels in this package are not final localisation.

### General voice

The event is about people quietly changing sides. The voice should be dry, observant, and uncomfortable, with irony aimed at cynics and opportunists and never at the people who suffer under occupation. Show behavior and objects: lists, keys, uniforms kept in wardrobes, a second flag folded in a desk drawer, the official who learns another language in a hurry. Do not make paperwork, archives, or diplomatic phrasing the emotional center. Do not label anything as a warning, a threat, or a danger signal. Do not use real collaborator names. Do not use em dashes or semicolons in sentences, staccato chains, or contrast formulas between rumor and official denial.

### Opening report

Viewpoint: the receiving government.

Visible: sympathizers inside many institutions, the same pattern in every foreign country, no single organizer.

Uncertain: origin, depth, which foreign power gains the most.

Variants:

- ordinary opening
- Deep Networks pre-fire opening, in which the networks already sit inside ministries and police headquarters
- an Administrations in Waiting line, when that evolution is active before the first firing
- a Collaboration Governments line, when that evolution is active before the first firing
- a repeat line from the second firing onward, in which the government recognizes the pattern and notices the same faces again

Option direction is in Part 1. Ideology should change the register of the Cultivate and Screen options.

### Deep Networks report

Viewpoint: a government noticing that recruitment has reached higher offices. Direction: the people who now talk to foreign services are department heads, police directors, plant managers, and staff officers, and the report gives no numbers.

### Seat report

Viewpoint: the capturing country. Direction: officials waiting with keys and lists, a police chief who already knows the patrol routes the new army wants, a district council that asks for its new instructions. Tone: unsettling efficiency.

### Open Ministries report

Viewpoint: the owner whose capital has been taken. Direction: the ministries reopened the day after the city fell, with most of the same staff. Tone: grim, not melodramatic.

### Fifth Column spirit

Name direction: a short name that uses the common phrase or a period equivalent. Description direction: each band describes behavior in the state. Wavering shows delay and hedging. Defecting shows offices that stop answering and local officials meeting the enemy. Collapsing shows a state that has started serving the victor before the war is over. The tooltip names the strongest foreign network by country.

### Open Gates reports

Host viewpoint: a district opened its doors to the enemy without a fight, and nobody in the capital ordered it.

Enemy viewpoint: a column entered a district that was waiting for it.

Tone: plain and disturbing. The host option direction can be bitter. The enemy option direction can be smug, which condemns the speaker.

### Collaborators Unmasked

Direction in Part 4.

### Prepared Government event

Viewpoint: the installer. Direction: a group of the defeated country's own politicians, officials, and officers has been ready for months and asks to be allowed to govern under the installer's protection. Option direction: Install should sound like a practical arrangement that the speaker knows is cynical. Keep direct occupation should sound like distrust of people who already betrayed one government. Democratic installers use provisional-administration wording, which should read as self-serving euphemism.

### Installed Administration spirit

Each stage describes the government's real position: imposed and resented, entrenched and comfortable, contested and frightened, abandoned and alone.

### Turned Regime reports

Viewpoint of the former installer: a government it created now answers to its enemy. Viewpoint of the new master: a government arrived already prepared, for the second time. The irony is that the same officials are now changing sides again. It should land on them, not on their population.

### Decision texts

Divided Loyalties texts describe protective measures in concrete terms: commissions, arrests, evacuated ministries, military commissars in civilian offices, ministers sent abroad with reserves and archives. Prepared Governments texts describe the installation and arming of a government as an administrative act that everyone involved understands.

Decision descriptions explain visible effects. They must not reveal hidden thresholds, band formulas, or variant chances.

### Event Log and Event Details

- One history row per firing, with no actor.
- One evolution row per evolution activation, with no actor.
- Event Details premise in Part 1, with one qualitative current-state line.
- The Event Details evolution catalog describes each evolution's premise in one or two sentences, without effects or numbers.

### Spreadsheet direction

The catalog row's Details field must match the Event Details premise. The four evolution columns must match the evolution catalog text. The implementation agent updates only the workbook and then runs the export tool. The catalog alignment handoff in `handoffs/097_collaboration_catalog_alignment.md` lists the fields.

## Super-event: Competing Orders

### Why this moment

The competing-orders milestone is the point where Event 097 changes how the world is governed. At least two powers each rule several defeated countries through prepared governments. The campaign map no longer shows only conquests and alliances. It shows rival systems of client regimes built from the same networks that exist in every country. This changes how the player reads the rest of the campaign, which is the test for a super-event.

### Trigger

The first time two or more different powers each hold at least two living governments installed through Event 097 at the same time, as defined in Part 3. It fires once per campaign. Evolution activation never fires it.

### Slot

Super-event slots are global numbers independent of event ids. Slot 97 already belongs to an Event 015 super-event. Event 097 takes the next free slot when it is implemented, confirmed against the super-event selectors at that time. Source currently shows slot 116 as the highest used slot, with several free gaps below it. The sprite name keeps the Event 097 prefix, as other event-owned super-event sprites do.

### Role and tone

Role: irreversible political shift. Tone: cold, wide, and quiet. The world has not ended. It has been reorganized by people who were ready to serve whoever arrived first. Avoid generic apocalypse wording and avoid triumph.

### What the world believes

That defeated countries are now governed by their own people on behalf of foreign powers, that several such systems compete, and that no government can be sure which of its officials already serve the next one.

### What stays uncertain

Who organized the first networks, whether any country is free of them, and which current government will be the next to be replaced.

### Image direction

A generated, period-documentary scene. A formal ceremony in a provincial government building where a newly installed local cabinet stands beneath a flag of their own country, while officers of an unnamed foreign army stand at the edge of the frame. No real flags of real foreign armies, no readable text, no real persons. Strong central composition and enough contrast for the super-event frame.

### Text research gates

- Super-event title: research required. Direction: short, about governments or loyalties changing hands, avoiding generic apocalypse phrasing.
- Button remark: research required. Direction: a short, grim, or ironic period remark about serving whoever is in charge, verified through the super-event text workflow.
- Main quote: research required. Direction: a traceable public-domain quote about loyalty, betrayal, or serving foreign masters, from political writing, scripture, classical literature, or historical speeches. Attribution must be verified.
- Audio: research required. Direction: a structured, restrained musical recording such as a slow march, a choral piece, or a chamber work with a formal, ceremonial character, between one and two minutes, public domain or clearly licensed.

Unresearched titles, remarks, quotes, and audio choices are blockers. The implementation agent must not turn these directions or any working label into final localisation.

## Achievements

All achievements are visible unless marked otherwise. Titles in this table are working labels, not final titles. The keys follow the repository convention for event-owned achievement ids, `<id>_<slug>_<name>`, and are the proposed final ids. Every achievement must be tracked without whole-world periodic scans.

The repository has no single shared forced-setup trigger. Achievement triggers in other events combine the same checks, and Event 097 uses that set: the player is human, debug mode is off, force-trigger mode is off, the Chaos Redux test country is not initialized, no Event 097 manual-trigger disqualifier flag is set, and no triggerable scenario has been launched. The manual-trigger disqualifier is written when Event 097 is fired from Event Details or through the forced trigger path in settings.

| Key | Working label | Who can earn it | Requirement | Disqualifiers | Difficulty |
| --- | --- | --- | --- | --- | --- |
| `097_collaboration_open_doors` | Every Door Already Open | Any participant | Make three different countries capitulate to you in one campaign, each while its Fifth Column was at Collapsing with you as its strongest network | Choosing Screen in any Event 097 firing | Hard |
| `097_collaboration_clean_ministries` | Nobody Left to Open the Gates | Any participant | Choose Screen in at least three firings, then reach the Defecting band in a war against a major power and end that war without capitulating and without losing control of your capital | Losing control of the capital at any point in that war | Hard |
| `097_collaboration_three_continents` | Administrations Everywhere | Any participant | Hold living governments installed through Event 097 whose capitals lie on three different continents at the same time | none beyond forced setup | Very hard |
| `097_collaboration_turned_regime` | Two Masters | Any participant | Receive a government through Turned Regime, then make its former installer capitulate while that government is still your subject | none beyond forced setup | Very hard, rare |
| `097_collaboration_return_from_exile` | The Cabinet Comes Home | The original country of a government installed through Event 097 | Charter a government in exile before capitulating, have a government installed over your cores, then own your capital again within three years of that installation while the installed government no longer exists | Accepting a separate peace with the installer before your return | Hard |
| `097_collaboration_quiet_capitulation` | Taken by Telephone | Any participant | Make a major power capitulate to you while you control fewer than half of its core states, its Fifth Column is active, and your network inside it is Total | none beyond forced setup | Very hard |

### Why these are not trivial

- Open Doors needs three separate wars to reach the deepest internal collapse with the player as the strongest network, which requires Cultivate choices, Fifth Column evolution, and real military pressure.
- Clean Ministries rewards the opposite route: a defender who paid for vetting in peace and then survived the worst internal pressure against a major power.
- Administrations Everywhere needs Evolution IV, several capitulations on different continents, and the political power to keep installing as the cost rises.
- Two Masters needs a rare variant and then a full victory over the former installer.
- The Cabinet Comes Home is a comeback route that connects to Event 095 and to allied liberation.
- Taken by Telephone makes a major power surrender to internal collapse more than to military defeat.

### Tracking notes

- Stance choices are recorded per country per firing.
- The highest Fifth Column band and the strongest network per host per war are recorded when the band changes and read at capitulation.
- Capitulation credit is checked once in the capitulation hook.
- The Event 097 government registry records installer, original tag, route, installation date, and capital continent.
- The exile route records the chartered flag on the original country and the installation date in the registry history.
- Core-state control for Taken by Telephone is counted once at capitulation over the loser's core states.

### Icon direction

| Key | Motif |
| --- | --- |
| `097_collaboration_open_doors` | A row of three open doors, each with light spilling out, on a dark ground |
| `097_collaboration_clean_ministries` | A closed ministry door with a heavy bar across it |
| `097_collaboration_three_continents` | Three small flagpoles on a globe without readable flags |
| `097_collaboration_turned_regime` | A ceremonial sash or armband split between two colours |
| `097_collaboration_return_from_exile` | A suitcase with travel labels set on a desk in front of a window |
| `097_collaboration_quiet_capitulation` | A telephone receiver off its cradle on a field desk |

Each achievement needs the completed 64x64 icon generated first, then the grey and not-eligible states derived through the repository achievement workflow. Final files and sprites follow the repository pattern: three DDS files per id under `gfx/achievements/` and the sprites `GFX_achievement_<id>`, `GFX_achievement_<id>_grey`, and `GFX_achievement_<id>_not_eligible` in the achievement interface file.

## DLC and feature compatibility

| Surface | Without DLC | With La Résistance | Note |
| --- | --- | --- | --- |
| Native collaboration value and its surrender and compliance effects | Required | Same | The implementation must confirm that `add_collaboration` and the capitulation defines work without La Résistance. If they do not, the event cannot work without that DLC and the implementation must report this as a blocker instead of building a substitute. |
| Collaboration display | The qualitative readings from Part 1 are the player's view | Vanilla intelligence screens may also show collaboration | The readings exist so the event stays understandable without any DLC screen. |
| Vanilla collaboration operations | Not present | Add collaboration independently | Event 097 never overwrites or removes collaboration from operations. |
| Collaboration-government creation | Must be confirmed | Must be confirmed | Evolution IV relies on the vanilla creation route. Its DLC boundary must be verified. |
| Compliance and resistance | Base game since the 1.9 update | Same | Seats, prepared cadres, and the Fifth Column rely on base-game compliance and resistance. |

The event has no DLC-only surface of its own. If verification shows that a required engine surface is DLC-only, the implementation must report the exact limitation and not invent a parallel system.

## Balance review requirements

The implementation must check these scenarios and record the results.

1. A 1936 start with one firing in 1937: how much earlier do typical wars end, and does compliance at capitulation change garrison needs in a visible way.
2. Four firings with Deep Networks active in a 1940s world war: how often does a major power reach the vanilla 80 percent collaboration-government threshold without Evolution IV.
3. Fifth Column at Collapsing on a minor and on a major: does it hasten capitulation without making a major collapse from a single bad month.
4. Open Gates frequency over a long war: does it stay at most three per host per war and prefer provincial districts.
5. Evolution IV in a world war: how many governments are installed per year, and does the political power growth stop one power from installing everywhere.
6. Turned Regime frequency: does it stay rare and happen only when the installer is losing.
7. AI stance distribution per firing: does the world avoid polarizing into all cultivators or all screeners.
8. Multiplayer: two human players with different stances, checking that every choice made inside the response window counts and that a player who has not answered when the window closes receives Accept.
