# Soviet Union Collapse Event Specification

## In-world situation

The Soviet center begins losing command over parts of the union before anyone can agree that a collapse has started.

The first signs are administrative. Republican ministries delay replies to Moscow, regional party committees refuse emergency directives, railway offices reroute supplies without approval, and border garrisons report to local councils instead of the central command. Soviet officials describe the situation as an autonomy dispute, a counter-revolutionary provocation, or a temporary breakdown in communications. Foreign journalists call it a constitutional crisis because nobody can prove which authority controls which city by the time their stories are filed.

The breakaway governments do not all describe themselves the same way. Some claim they are restoring legal independence. Some claim the union treaty has been voided by Moscow's violence, incompetence, or defeat. Some insist they remain socialist but no longer accept orders from the Kremlin. At higher chaos, a few declarations become stranger: military committees, ethnic defense councils, anti-Bolshevik provisional governments, exile claimants, or opportunistic regimes backed by foreign armies.

The player should not see the event as the USSR simply releasing countries because the script says so. The crisis should feel like state authority breaking along language, national, military, and supply lines. Moscow still has tanks, officers, secret police, industry, and the Red Army, but that does not mean orders reach the right units or that local commanders obey them.

## What is known, disputed, hidden, and uncertain

Known to the world:

- Several republican governments or regional committees have stopped accepting normal Soviet orders.
- At least two breakaway states declare that Moscow no longer has lawful authority over them.
- Soviet forces and local defense formations are already facing each other across depots, rail junctions, and city administrations.
- Foreign governments are cautious because the legal status of the new states is unclear and the Soviet Union may still survive.

Disputed:

- Whether the breakaways are popular independence movements, opportunistic coups, foreign-backed separatists, or local party elites trying to save themselves.
- Whether Soviet troops are defecting in large numbers or merely refusing to move.
- Whether the crisis is a real dissolution or a temporary rebellion that Moscow can still crush.
- Whether foreign recognition helps stabilize the region or encourages further fragmentation.

Hidden or only partly understood:

- Some republican officials may be negotiating with Moscow while publicly denouncing it.
- Local commanders may be stockpiling Soviet equipment before choosing a side.
- Foreign intelligence services may support one breakaway while officially calling for restraint.
- If Germany or Japan is already at war with the Soviet Union, some breakaways may be encouraged or coerced into becoming buffer clients instead of genuine members of the anti-Moscow coalition.

Scientists are not central to the event, but Soviet technical institutions and arms depots matter as background tension. Observers should worry about who controls laboratories, depots, industrial bureaus, aircraft, and any strategic weapons if the crisis reaches the inner Soviet state.

## First player-facing moment

The Soviet player should first receive a report event, not only a hidden news event. The opening report should describe a political and military ambiguity:

- Moscow receives conflicting telegrams from republican capitals.
- Several local garrisons claim they are "awaiting clarification" rather than obeying movement orders.
- Railway and supply officials cannot confirm whether shipments are being withheld, seized, or redirected.
- The central government is asked to choose a line before the situation becomes irreversible.

Suggested opening title direction:

- **Republics Refuse Orders**
- **The Union Treaty Frays**
- **Moscow's Orders Go Unanswered**

The first global news popup should remain cautious. It should not state that the Soviet Union has fully collapsed unless the later full-collapse stage has fired. The baseline news should say that several republics have declared independence or stopped accepting direct control, while foreign ministries are waiting to see whether Moscow can restore authority.

The current repo already has `GFX_news_soviet_union_collapse` and `gfx/event_pictures/news_soviet_union_collapse.dds`; this is enough for the baseline news presentation.

## Soviet opening options

The opening Soviet report should give a clear story choice. The options should not be pure flavor; they define how the crisis escalates.

### The Union is indivisible

Moscow treats the declarations as illegal secession and prepares force.

Story meaning:

- The center is confident that hesitation will destroy the union.
- Republican governments are called counter-revolutionary organs or illegal committees.
- Loyalist officers receive permission to move without waiting for further civilian negotiation.

Consequences:

- Faster access to reclaim decisions and military solutions.
- Higher spread pressure because other republics expect force.
- Breakaway states are more likely to receive hardline defense spirits, emergency mobilization, and captured-depot support.
- Foreign governments become more cautious about recognition but more likely to send covert help if the fighting drags on.

### Open emergency negotiations

Moscow tries to split moderates from separatists and preserve a looser union.

Story meaning:

- The center admits that the crisis has political roots.
- Republican leaders are treated as negotiators rather than purely criminal actors.
- The public hears language about federal reform, emergency congresses, and legal guarantees.

Consequences:

- Lower spread pressure and better chance to prevent later waves.
- Costs political power, stability, and possibly temporary autonomy concessions.
- Slower reclaim path.
- If successful, some breakaway countries may accept a truce, autonomy settlement, or delayed reintegration path instead of immediate war.

### Isolate the rebel committees

Moscow avoids an immediate general offensive and instead cuts communications, rail access, party funds, and supply channels.

Story meaning:

- The center wants to starve the rebellion of coordination without admitting political weakness.
- Soviet authorities call the crisis a security operation, not a war.
- Civilians experience shortages and censorship before they see front lines.

Consequences:

- Reduces some breakaway equipment or supply bonuses if used early.
- Can delay the next stage.
- Raises local resentment and can increase the chance of radical or extremist breakaway variants if the crisis continues.
- Should be less decisive than force and less stabilizing than negotiation.

### Recognize a new union arrangement

This option should be available only if the Soviet Union is democratic, deeply reformed, or already on a non-authoritarian path.

Story meaning:

- The central government accepts that the old command structure is finished.
- The crisis becomes a political divorce or confederal restructuring instead of a war by default.

Consequences:

- Strongly reduces spread pressure.
- May release or set autonomy for the first wave peacefully.
- Costs legitimacy, stability, political power, or territory.
- Can prevent the coalition from becoming a military bloc, replacing it with a diplomatic independence forum.

## Breakaway player experience

If a breakaway country is player-controlled or becomes relevant to a player, it should receive a report event explaining that independence is not secure. The country has a flag, a provisional government, and local troops, but Moscow still considers it part of the union.

Suggested breakaway report title direction:

- **The Center Falters**
- **The Republic Stands Alone**
- **Independence Under Arms**

Suggested breakaway options:

### Defend the republic

The breakaway accepts that war may come.

Consequences:

- Adds emergency defense spirit.
- Spawns local defense divisions based on owned core states.
- Gives a small equipment/manpower package.
- Increases the chance of joining the anti-Moscow coalition later.

### Ask the world to recognize us

The breakaway seeks diplomatic legitimacy.

Consequences:

- May improve relations with democratic majors and Soviet enemies.
- May reduce Moscow's willingness to negotiate if Moscow chose force.
- Can unlock foreign volunteers or lend-lease flavor.
- Should not guarantee foreign faction membership by default.

### Call the other republics to rise

The breakaway tries to turn its survival into a union-wide revolt.

Consequences:

- Increases spread pressure.
- Raises the chance of coalition formation.
- Gives temporary political momentum or war support.
- Risks a Soviet crackdown decision becoming cheaper or more effective.

## Core gameplay loop

The event should create a crisis state around the Soviet Union rather than ending after the first release.

The loop is:

1. The opening wave creates several breakaway countries.
2. The Soviet Union chooses a crisis line: force, negotiation, isolation, or reform.
3. The breakaways receive temporary survival support so they cannot be instantly erased.
4. Moscow receives decisions to reclaim, negotiate with, or suppress breakaways.
5. Breakaways receive decisions to mobilize, seize supplies, seek recognition, and coordinate.
6. If Moscow does not contain the first wave quickly, spread pressure rises.
7. Later evolutions release more countries, form the coalition, and turn local defiance into a wider collapse.

The important design rule is that force is faster but destabilizing. Negotiation is slower and costly but reduces spread. Isolation buys time but can radicalize the crisis. Reform can defuse the military path only for a USSR that has already moved away from hard authoritarian control.

## Release waves

The release waves should use a curated candidate registry, not one ad hoc hardcoded list inside an event option. The current map and vanilla cores contain many potential non-SOV core tags in Soviet-owned states. The implementation should prefer a maintained registry with stage, region, priority, and variant behavior.

The exact final candidate list is implementation-sensitive, but inspection found relevant candidates such as:

- Initial national republics: `UKR`, `BLR`
- Caucasus: `GEO`, `ARM`, `AZR`, `ABK`
- Central Asia: `KAZ`, `UZB`, `TMS`, `TAJ`, `KYR`, `BUK`, `KHI`, `KKP`
- Western or disputed borderlands if held by the USSR: `MOL`, Baltic tags if Soviet-controlled, `CRI`
- Far east and Siberian/regional breakaways: `FER`, `YAK`, `KAR`, `KOM`, `ALT`, `TAT`, `BSK`, `DAG`, `KAL`, `CHU`, `UDM`, `MEL`, and similar cored tags

Uncertainty: the exact list of "every releasable democratic country inside Soviet territory" should be curated during implementation from the current mod map and country tag set. Some cored regional tags represent small autonomous areas and should probably appear only in late collapse stages, not the first wave.

### Stage 1: Refusal of Orders

Baseline firing.

Default release direction:

- Release `UKR` and `BLR` if valid.
- If either cannot be released because it already exists or has no valid Soviet-held core territory, substitute from a priority list such as `KAZ`, `GEO`, `ARM`, or `AZR`.
- The first wave should usually be two or three breakaways, not the entire union.

Story:

Ukraine and Belarus, or equivalent large republics, become the first proof that Moscow's command is failing. Their declarations should read as legal and administrative first, military second. The situation becomes a war only if Moscow or the breakaways make it one.

### Stage 2: Second Declarations

Triggered if Moscow fails to reclaim, negotiate with, or neutralize the first wave within the early crisis window.

Release direction:

- Add Caucasus and Central Asian republics based on valid cores and map control.
- If the Baltics are Soviet-controlled, they are strong candidates for this stage because foreign journalists and diplomats can frame them as "restored independence" cases.

Story:

Other republican governments conclude that the center cannot punish everyone at once. Some declarations cite constitutional law; others cite self-defense or local emergency authority. Moscow's internal propaganda becomes more severe.

### Stage 3: Free Republics Compact

Triggered when several breakaways survive long enough or remain at war with Moscow.

Gameplay direction:

- The anti-Moscow coalition forms through a faction template.
- The leader should usually be the strongest surviving first-wave breakaway, with `UKR` preferred if it exists, is independent, and is not a foreign puppet.
- Coalition members receive defensive coordination bonuses while at war with the Soviet Union.

Story:

The breakaways stop acting like isolated emergencies and begin coordinating declarations, supply requests, radio messaging, and front-line planning. This is the moment foreign governments begin treating the crisis as a durable post-Soviet bloc rather than a short revolt.

### Stage 4: Loyalty Chain Breaks

Triggered at higher chaos, after failed Soviet containment, low Soviet stability, high surrender progress, or a long war against the coalition.

Release direction:

- Late-stage regional and autonomous tags become valid.
- Far eastern, Siberian, Volga, Caucasus, and northern regional breakaways may appear.
- Some breakaways may be less democratic or less coherent at this stage, especially if chaos is high.

Story:

The crisis stops following only republican borders. Local military districts, ethnic councils, security branches, and transport authorities begin choosing survival over obedience. Moscow may still hold the capital and central Russia, but the union has lost its normal administrative shape.

### Stage 5: Full Civil Collapse

Triggered only at extreme conditions: World Collapse tier, Soviet near-capitulation, prolonged unresolved crisis, or a surviving coalition with several members and growing front coordination.

Release direction:

- Most valid non-SOV cored countries inside Soviet territory can be released if they do not already exist.
- Moscow retains its core heartland and must reconquer most of the former union if it wants restoration.
- The coalition becomes a serious long-term anti-Soviet faction if it survives this stage.

Story:

The world stops asking whether the Soviet Union will restore control quickly. It asks which authorities possess armies, depots, rail lines, archives, and diplomatic recognition. Foreign maps become obsolete within days.

This stage deserves super-event treatment.

## Breakaway support package

Breakaway states must survive long enough for the event to matter. Their support should be strong but temporary, defensive, and tied to the crisis rather than a permanent free empire.

Suggested national spirits:

- **Emergency Defense Committees**: defense, max entrenchment, planning speed, and war support while fighting the Soviet Union.
- **Popular Mobilization**: weekly manpower or recruitable population, lower stability or consumer goods pressure.
- **Captured Soviet Depots**: equipment stockpile, equipment capture, reduced shortage pressure, limited duration.
- **Foreign Volunteers**: small organization regain, training speed, or division recovery bonuses if foreign recognition decisions succeed.
- **Border Garrisons Defect**: one-time unit and equipment package; stronger for border republics or if Soviet stability is low.

The support package should scale by country size, number of owned core states, and crisis stage. Large republics should not get the same package as one-state autonomous regions. Stage 1 should make breakaways hard to crush immediately; Stage 5 can be harsher because the Soviet command structure is already failing.

Defensive coordination bonuses should apply only while fighting the Soviet Union. They should expire after the Soviet war ends, after reintegration, or after the crisis is resolved.

## Soviet decision set

The Soviet decision category should be visible only while the crisis is active and the Soviet Union exists. It should use targeted decisions or a precomputed registry so it does not scan the world every frame.

### Reclaim breakaway republic

Moscow prepares military restoration against a specific breakaway.

Story:

The decision represents a formal order to restore union authority in one republic or region.

Consequences:

- Creates or uses a war goal against the target.
- Can declare war directly if the force path has been chosen and the target is already treated as rebellious.
- Increases force pressure and may increase spread pressure.
- Should have a visible tooltip naming the target and explaining that military action can worsen the wider crisis.

### Restore party control

Moscow sends party cadres, security officials, and reliable administrators into wavering areas.

Consequences:

- Reduces spread pressure.
- Costs political power and possibly stability.
- More effective for communist or authoritarian USSR variants.
- Less effective if Moscow is losing a major war or has very low stability.

### Send loyalist officers

Moscow tries to keep army districts obedient.

Consequences:

- Temporary Soviet command, organization, or planning bonus.
- Reduces defection chance in the next release wave.
- If Soviet stability is very low, it may backfire by pushing local commanders to choose sides.

### Offer autonomy

Moscow negotiates with one breakaway or pending breakaway.

Consequences:

- Can stop a pending release, create a truce, or settle one active breakaway.
- Costs political power, stability, or territory.
- Reduces spread pressure if accepted.
- Should be more attractive to democratic or reformed Soviet variants.

### Cut rebel supply routes

Moscow uses rail control, border troops, and security checkpoints to isolate the breakaways.

Consequences:

- Reduces target supply or equipment bonuses.
- Can delay coalition formation.
- Raises resentment and can increase radicalization if used repeatedly.

### Arrest separatist leadership

Moscow tries to decapitate a pending or early-stage breakaway.

Consequences:

- Chance to prevent one pending declaration.
- Failure should make that target more militant and may immediately release it.
- Should not be a clean universal solution.

### Emergency mobilization

Moscow pulls reserves, internal troops, and emergency logistics into the crisis.

Consequences:

- Adds manpower, command power, or temporary military bonuses.
- Costs stability or consumer goods.
- Can make later negotiation harder.

### Declare the union indivisible

Moscow makes the crisis a constitutional and ideological test.

Consequences:

- Strong force-path bonus.
- Lower negotiation effectiveness.
- Higher spread pressure.
- Breakaways are more likely to coordinate and frame the struggle as survival.

### Proclaim the union restored

Available only if the first wave is contained quickly and no active breakaway war remains.

Consequences:

- Adds a temporary **Union Restored** spirit.
- Reduces future Soviet Collapse evolution chance.
- Should not erase all diplomatic damage; foreign observers remain skeptical.

## Breakaway decision set

Breakaway decisions should be available to countries marked as Soviet collapse breakaways. They should be defensive and independence-focused, not a generic conquest toolkit.

### Join the anti-Moscow coalition

The breakaway joins the Free Republics Compact if the coalition exists and the country is independent enough.

### Request foreign recognition

The breakaway asks foreign governments to treat it as a legitimate state.

Possible outcomes:

- Opinion gains with democratic countries or Soviet enemies.
- Chance for a foreign volunteers spirit.
- Higher legitimacy inside the coalition.
- If Germany or Japan is the main patron, recognition can become a puppet/protectorate variant instead of democratic recognition.

### Mobilize local defense units

Creates or strengthens local defense formations.

The units should be weaker than normal major-power divisions but numerous enough to hold initial lines.

### Seize Soviet depots

Adds equipment and possibly a captured-depot spirit.

This decision should be stronger if the breakaway owns states with military industry, supply hubs, or former Soviet depots.

### Call for other republics to rise

Raises spread pressure and can help trigger the next stage.

This should be risky: if Moscow survives, the caller becomes a priority target.

### Coordinate fronts against Moscow

Available to coalition members while at war with the Soviet Union.

Consequences:

- Temporary defensive coordination bonus.
- Possibly adds planning, entrenchment, or supply grace.
- Should not create offensive expansion bonuses outside the anti-Moscow war.

### Accept an autonomy settlement

Available only if Moscow has offered autonomy and the breakaway is not hardline or foreign-puppet aligned.

Consequences:

- Ends or delays conflict with Moscow.
- Removes some emergency spirits.
- Reduces coalition momentum if the country leaves the coalition.

## Anti-Moscow coalition

The coalition should be a defensive independence bloc, not a normal expansionist alliance.

Suggested name direction:

- **Free Republics Compact**
- **League of Free Republics**
- **Congress of Free Republics**

The coalition's purpose:

- defend breakaway members from Soviet reconquest;
- coordinate supplies, front lines, recognition, and refugee flows;
- support further independence declarations inside Soviet-held territory;
- avoid claims outside the former Soviet space unless another event explicitly changes that.

Implementation direction:

- Use `create_faction_from_template`, following the repo's existing `anti_zombie_league` and `holy_realm_mandala` faction-template pattern.
- The template should be invisible to normal diplomatic creation and created only through this event.
- Rules should prevent unrelated countries from joining by ordinary diplomacy.
- Faction goals can track liberation of valid former Soviet releasable countries, recognition, and defensive coordination.
- If faction goals are too much for the first implementation pass, the spec still expects at least a template-backed faction with rule restrictions and defensive member bonuses. Do not use an obsolete plain `create_faction` fallback without discussing it.

Suggested faction goals:

- **Secure the Republics**: all current members are not at war on their core territory against Moscow.
- **Recognition Mission**: members complete recognition decisions or reach a recognition variable threshold.
- **Free the Remaining Republics**: progress based on valid former Soviet releasable tags existing outside Soviet control.

Coalition member bonuses should be defensive and conditional:

- while at war with the Soviet Union;
- while the member is not an aggressive occupier outside former Soviet territory;
- while the coalition has not become a foreign puppet structure.

## Evolution track: Union Fracture

The event should have one evolution track tied to the same event identity.

| Stage | Name | Eligibility direction | Player-facing meaning |
| --- | --- | --- | --- |
| Baseline | Refusal of Orders | Event fires at the Soviet Union | First wave of republics breaks away |
| I | Second Declarations | First wave unresolved after early window, or Soviet weakness | More republics decide Moscow cannot stop everyone |
| II | Free Republics Compact | Three or more breakaways survive, or several are at war with Moscow | Breakaways coordinate as a bloc |
| III | Loyalty Chain Breaks | Higher chaos, low Soviet stability, prolonged war, or failed containment | Army districts and smaller regions stop obeying |
| IV | Full Civil Collapse | World Collapse tier, near capitulation, or a severe unresolved coalition war | The union breaks into many successor authorities |

Each evolution should have an event-log row with a specific title, not a generic "evolution" label.

The evolution track should not require all stages in every campaign. A strong Soviet Union can contain the first wave. A weak or invaded Soviet Union can jump into later stages faster. A democratic or reformed USSR can convert parts of the track into negotiated dissolution.

## Campaign-state variants

### Germany at war with the Soviet Union

Western breakaways become more likely.

Likely candidates:

- Ukraine
- Belarus
- Baltic countries if Soviet-held
- Moldova or Bessarabian-related tags if valid
- Caucasus tags if the front or occupation reaches them

Story:

Germany claims the declarations prove the Soviet state is rotten. Breakaway leaders may publicly deny German control while privately depending on German arms. Some countries may become German-aligned buffers instead of coalition democracies.

Implementation note:

Do not automatically make every western breakaway a German puppet. Use this as a variant chance tied to occupation, control, ideology, and war state.

### Japan at war with the Soviet Union

Eastern and Siberian breakaways become more likely.

Likely candidates:

- Far Eastern Republic
- Yakutia
- Siberian and northern regional tags where valid
- Pacific or frontier regional tags tied to controlled Soviet territory

Story:

Japanese diplomats describe the breakaways as local self-defense against Moscow, while Soviet propaganda calls them occupation puppets. Some local commanders cooperate with Japan to survive; others join the anti-Moscow coalition without accepting Japanese command.

### Democratic or reformed Soviet Union

The crisis is more political and less violent.

Effects:

- Negotiation options are stronger.
- Breakaways are more likely to become democratic provisional governments.
- Coalition formation can become a diplomatic compact rather than a full military faction.
- Full civil collapse requires much worse external conditions.

### Communist hardline Soviet Union

The crisis is bloodier and more militarized.

Effects:

- Force and security decisions are stronger.
- Failed arrests and isolation decisions create more militant breakaways.
- Breakaways receive stronger emergency defense spirits.
- Foreign observers are less likely to trust Soviet claims of legality.

### High chaos ideological distortion

At Totalen Chaos or World Collapse, some breakaways can emerge with unusual or extremist governments.

Examples:

- military salvation committees;
- radical nationalist provisional governments;
- local Soviet republics claiming Moscow betrayed socialism;
- foreign-backed protectorates;
- security-state remnants holding one region.

The anti-Moscow coalition should prefer democratic or independence-focused members. Extreme variants may cooperate militarily without fully joining the main coalition.

### Soviet first-wave containment

If Moscow defeats, reintegrates, or settles the first wave quickly:

- Add a temporary **Union Restored** spirit.
- Lower or block later Soviet Collapse evolutions for a meaningful period.
- Foreign news should treat the result as a restoration of order with unresolved doubts, not a clean return to the old normal.

## Event cluster placement

This event belongs in a new **Liberations** cluster.

The spreadsheet currently lists the event under **Diseases**, but that appears stale for this rework. The event's gameplay and story belong with countries becoming independent, subjects breaking free, and occupation authorities losing control.

Suggested Liberations cluster membership:

- `006 Independence Wave`: early or medium danger optional member.
- `063 Subject Independence`: early or medium danger optional member.
- `095 Occupation Revolt`: medium danger optional member.
- `005 Soviet Union Collapse`: high danger optional member.

Cluster behavior:

- The Liberations cluster should unlock before Soviet Collapse itself, likely at Gathering Storm or Rising Chaos, so smaller independence events can appear first.
- Soviet Union Collapse should not be eligible as soon as the cluster unlocks. It should normally require Chaos Tier or a special Soviet weakness condition.
- Soviet Union Collapse is optional, not required, inside the cluster.
- It should be occasional rather than common when the cluster fires because it can reshape Eurasia.
- If it fires as part of the cluster, it should be ordered after smaller liberation events unless the selected event was ID 5 itself.

This keeps the event dangerous inside its cluster without making every liberation wave destroy the Soviet Union.

## Assets

Existing usable assets:

- News image: `GFX_news_soviet_union_collapse`
- DDS path: `gfx/event_pictures/news_soviet_union_collapse.dds`
- GFX definition: `interface/chaosx_pictures.gfx`

New assets needed if the full mechanic is implemented:

- Decision category icon: `GFX_decision_category_soviet_collapse`, stored under `gfx/interface/decisions/decision_category_soviet_collapse.dds`, registered in `interface/chaosx_decisions.gfx`.
- Soviet decision icon: `GFX_decision_soviet_reclaim_republic`, stored under `gfx/interface/decisions/decision_soviet_reclaim_republic.dds`.
- Breakaway decision icon: `GFX_decision_breakaway_defense_committee`, stored under `gfx/interface/decisions/decision_breakaway_defense_committee.dds`.
- National spirit icons:
  - `GFX_idea_soviet_union_crisis`
  - `GFX_idea_breakaway_emergency_mobilization`
  - `GFX_idea_breakaway_popular_defense_committees`
  - `GFX_idea_breakaway_captured_soviet_depots`
  - `GFX_idea_breakaway_foreign_volunteers`
  - `GFX_idea_union_restored`
- Faction emblem: `GFX_faction_logo_free_republics_compact` if a custom emblem is wanted. If not, reuse a generic democratic faction logo.
- Super-event image for Stage 5: `GFX_super_event_soviet_collapse`, stored under `gfx/super_events/super_event_soviet_collapse.dds`, size 457x328.

Visual direction:

- News image: documentary black-and-white Soviet administrative crisis, crowds outside a government building, soldiers near a railway station, or a torn Soviet banner in a public square.
- Decision and spirit icons: compact HOI4-style symbols using documents, broken red star imagery, rail lines, defense committees, depots, and militia armbands.
- Super-event image: strong central composition showing the Soviet state as an institution coming apart, not a battlefield panorama. A Kremlin silhouette, map table, broken red banner, or crowded republic parliament would fit.

During implementation, placeholder sprites should be copied from vanilla or existing Chaos Redux assets so the game has valid DDS paths before final art is produced.

## Super-event direction

The baseline crisis does not need a super-event. Stage 5 does.

Trigger moment:

- Full Civil Collapse fires.
- The Soviet Union no longer faces only a few breakaway states; the former union has become a map of successor governments, military committees, and contested front lines.

Role:

- Escalation and reveal.
- It tells the player that the event has stopped being an autonomy crisis and has become a major geopolitical fracture.

Tone:

- Cold, historical, and uncertain.
- Less "the world ends" and more "one of the world's central states has ceased to function normally."

Title direction:

- **The Union Comes Apart**
- **The Red Union Breaks**
- **No Orders from Moscow**

Description direction:

- Mention conflicting recognition statements, contested depots, maps being redrawn, and the fact that Moscow still claims authority while much of the former union no longer obeys.
- Do not claim the Soviet Union is gone if Moscow still exists as a state. The point is collapse of union control, not necessarily immediate deletion of the Soviet tag.

Quote direction:

- Use a verified historical quotation about empire, union, state failure, revolution, or national self-determination.
- Do not choose or attribute a quote until the `chaos-redux-super-events` workflow researches and verifies it.

Audio mood:

- Low military-radio atmosphere, solemn strings, Soviet-era march fragments treated mournfully, or archival-feeling orchestral tension.
- Any final audio must be researched and licensed through the super-event workflow.

## Implementation notes specific to this event

- Keep the entry event root as `chaosx.nr5.1`.
- The current implementation is a hidden stub that releases `UKR` and `BLR` and fires `chaosx.news.5`. The rework should replace that stub with the crisis bootstrap while preserving ID 5.
- ID 5 is already registered as a fire-once event and has default actor mapping to `SOV`. It can remain fire-once while its internal crisis continues through decisions and evolution events.
- Do not queue this event against a missing Soviet Union. If `SOV` does not exist, the event should be unavailable and show no meaningful actor in the event list.
- Use script constants for decision costs, crisis windows, spread thresholds, support package size, truce lengths, temporary spirit durations, stage thresholds, and AI weights.
- Use normal variables for values passed into effect fields that reject `constant:` tokens.
- Use event targets for the currently selected breakaway, coalition leader, and any immediate follow-up event scopes. Use arrays for the full breakaway registry and active-breakaway list.
- Release logic must check that the target country does not already exist. The HOI4 `release` effect does nothing when the tag exists, so existing countries need a separate handling path.
- If a target's cores are only controlled but not owned by the Soviet Union, release behavior needs explicit design. `release_on_controlled` and foreign-puppet variants may be needed for Germany/Japan cases.
- Do not use `on_daily`, `on_weekly`, or `on_monthly` whole-world polling for the crisis. Progression should happen through crisis events, decisions, targeted decision checks, and bounded registries.
- Soviet reclaim decisions should use targeted decision performance patterns: `target_root_trigger` for the Soviet-side precheck and `target_trigger` for actual breakaway targets.
- Breakaway unit spawning should follow vanilla precedent: create a local division template, then spawn units in owned or controlled states with one-line `division = "..."` strings.
- Temporary bonuses should be timed ideas or removable spirits that cancel when the relevant war or crisis state ends.
- Coalition implementation should use a faction template with rules and, if practical, goals. Do not replace that with a plain expansionist faction.
- Event log integration should record the baseline and each evolution stage. The event details view should show the current stage, Soviet crisis line, active breakaway count, and coalition status if available.
- Localisation should avoid saying the Soviet Union has already "collapsed" in the baseline report. Reserve that wording for Stage 5 or for news text that explicitly frames it as outside speculation.
- The event catalog spreadsheet should be updated during implementation: status away from "To Be Reworked", cluster from the stale "Diseases" row to "Liberations", and chaos eligibility aligned with the final tier gate.

## Uncertainties to resolve during implementation

- The exact curated release registry should be finalized from the current mod map, not from memory. The inspected map contains many small cored regional tags inside Soviet-owned territory, and some are better suited to Stage 4 or Stage 5 only.
- The faction goal layer for the Free Republics Compact may require additional collections if the goal tracks "all valid former Soviet releasables." If collections are too heavy for the first pass, define the faction template and rules first, then add goals in a follow-up.
- Germany/Japan puppet variants need careful handling when the invader controls Soviet cores but does not own them. The release path should be tested against the HOI4 release effects before final balancing.
- Stage 5 super-event quote, image source, and audio require the `chaos-redux-super-events` and `chaos-redux-event-assets` workflows before implementation.
