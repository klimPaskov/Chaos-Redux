# 004 Random War Event Specification

## Design goal

Random War creates an unexpected war between eligible countries. The base event creates one declaration. Evolutions increase the number of linked declarations and later allow compatible Chaos Redux special countries to enter the pool.

The event should stay simple: a border incident, false order, ultimatum, disputed claim, panicked commander, or government exploiting confusion.

## Cluster placement

This event belongs in the **Wars** cluster.

The event is available from campaign start. The **Wars** cluster becomes visible or active around chaos tier 2.

## Selection rule

Selection is random within the eligible country pool, using weights and cooldowns. Player-controlled countries are included in the same pool as other eligible countries.

## Core flow

1. Select an eligible aggressor and legal target using the existing pairing model.
2. Retain the invocation's stage, requested declaration count and selected actors.
3. Create each declaration only while the pair remains legal at that step.
4. Build the remaining linked dispute from the realized participants, excluding already-hostile pairs from additional declaration credit.
5. Finish the chain before sending its participant responses and observer summary.
6. Record the declarations actually created and the distinct countries actually involved.

The evolution ladder specifies the requested size of a dispute, while the realized chain records what happened.
After each declaration, faction calls, subject relations, capitulation or another crisis can make a later pair unavailable.
Use the existing legal-pair exclusions and permitted safe-pair fallback rather than forcing that stale pair.
If the remaining eligible pairs cannot complete the requested linked dispute, retain the wars already created and identify the unfilled slots as blocked.
Do not report the requested count as an accomplished count, reopen an existing war for another receipt, or add a disconnected filler conflict solely to reach the number.
An invocation that creates no declaration uses the existing unsuccessful-launch feedback and grants no participant reward.
An invocation that creates some declarations is reported as that partial incident, not as a second complete firing.

Every involved country receives at most one participant response for this invocation.
A country that both attacked and was attacked receives the defender response, following the accepted response priority.
One observer summary covers the completed chain and uses its actual distinct participant count.
Observer relevance includes major or faction-leader involvement, a neighboring participant, a compatible special country, or the late evolution stage.
Participant resources and temporary effects are applied once through that response, while shared war systems own the underlying war and its normal consequences.

Future acceptance cases should interrupt a three-country chain after its first declaration, make the next pair already hostile through a faction call, and remove one actor before the final step.
Each case must show truthful realized counts, one response per live participant, no repeated war reward and no forced stale declaration.
Existing option weights, special-country draw thresholds and stage-size tuning remain unchanged by this contract.

## Baseline: Border Incident Becomes War

Available from campaign start when Event ID 4 is enabled and selected by the random event system.

Result:

- 1 eligible aggressor declares war on 1 eligible target.
- Calm World baseline pair selection blocks major-versus-non-major pairings so the first-stage event stays regional or scale-matched instead of opening with a major power overrunning a minor.
- Aggressor and target are saved for localisation and event log text.
- Aggressor and target receive short cooldowns so the same countries are not selected repeatedly.

Report direction:

A border incident becomes a war before either government can control the story. Each side issues its own explanation as troops cross the line and diplomats argue over who moved first.

Aggressor options:

- **The order stands**
  - war continues
  - small temporary war support gain
  - small political power or command power cost

- **Blame the general staff**
  - war continues
  - small stability loss
  - temporary reduction to future aggressor selection weight

Target options:

- **Hold the line**
  - small temporary defensive bonus on owned core states or national territory
  - small war support gain

- **Mobilize the reserves**
  - temporary mobilization or recruitable population bonus
  - small stability cost

## Country eligibility

### Aggressor pool

Aggressor candidates should be:

- existing countries
- active on the map
- independent enough for normal war
- able to declare war cleanly
- outside incompatible scripted crisis states
- outside recent aggressor cooldown
- not already at war with the selected target

Increase aggressor weight for:

- high war support
- militarist or aggressive ideology
- claims, cores, bad relations, or border friction
- local strength advantage
- current instability, especially at higher chaos

Decrease aggressor weight for:

- very low stability at baseline
- severe active war losses
- too many active wars
- very small countries at baseline
- faction leaders at baseline
- countries recently selected by this event

### Target pool

Target candidates should be:

- existing countries
- valid war targets
- active on the map
- outside recent target cooldown
- not already at war with the aggressor
- not allied with the aggressor through same-faction or subject relationships
- legally declarable by the aggressor under current game rules
- outside protected scripted states

Hard exclusions cover same-country, same-faction, master or subject, already-at-war, and other pairs that fail the engine declaration check.

Increase target weight for:

- neighboring or nearby regional rivals
- low relations with the aggressor
- contested cores or claims
- military weakness at baseline
- symbolic or irrational value at higher chaos

Decrease target weight for:

- countries already overwhelmed by wars
- distant countries at baseline

## Pairing model

Use staged target selection:

1. Try a bordering target.
2. Try a nearby regional target.
3. Try a rival, claim, core, or low-relation target.
4. Use wider global selection if no cleaner pairing exists.
5. Loosen distance and rationality checks at higher evolution stages.
6. Add compatible special chaos countries from Evolution II onward.

## Evolution track: War Contagion

War Contagion increases declaration count and widens the country pool.

| Stage | Chaos tier | Name | Declarations | Special chaos country chance | Behavior |
| --- | --- | --- | --- | --- | --- |
| Baseline | campaign start | Border Incident Becomes War | 1 | 0% | one aggressor declares on one target |
| I | Gathering Storm, 200+ | Triangular Incident | 3 | 0% | three countries form a linked dispute |
| II | Rising Chaos, 400+ | Four Fronts | 4 | 15% to 25% | four declarations form a conflict web |
| III | Chaos Tier, 600+ | Contagious Ultimatums | 5 | 30% to 40% | majors and faction members become more likely |
| IV | Totalen Chaos, 800+ | The War Week | 6 | 50% to 60% | several wars fire in one chain |
| V | World Collapse, 1000+ | Open Season | 7 to 8 | 70% | late-game war wave while normal random events still run |

Use constants for thresholds, declaration counts, special-country chances, and cooldowns.

### Evolution I: Triangular Incident

Select three countries.

Preferred pattern:

- A declares on B
- B declares on C
- C declares on A

Fallback pattern:

- create three safe pairwise declarations among the selected countries

### Evolution II: Four Fronts

Create four declarations.

Possible patterns:

- A declares on B, B declares on C, C declares on D, D declares on A
- A declares on C, B declares on D, C declares on B, D declares on A
- two linked disputes joined by one extra declaration

### Evolution III: Contagious Ultimatums

Create five declarations.

Changes:

- one major country can enter the pool more often
- faction members can appear with reduced weight
- compatible special chaos countries become a normal rare outcome
- the conflict web should stay readable

### Evolution IV: The War Week

Create six declarations.

Changes:

- one declaration may ignore normal rationality weighting
- faction entanglement is allowed with restraint
- compatible special chaos country involvement becomes common
- observer reports become more common when majors or special countries are involved

### Evolution V: Open Season

Create seven to eight declarations.

Changes:

- compatible special chaos country involvement is strongly favored if one exists
- one major power or faction leader can be included if it is not already overwhelmed
- irrational pairings are acceptable
- event log text marks this as the highest War Contagion stage

## Compatible special chaos countries

Later evolutions can include special Chaos Redux countries that are safe for normal diplomacy and war.

Use a compatibility marker or scripted trigger, for example:

- `chaosx_can_join_random_war`
- `is_special_chaos_country = yes`

Use three simple roles:

1. **Special aggressor**
   - special country declares on a normal country

2. **Special target**
   - normal country declares on the special country

3. **Special catalyst**
   - special country becomes one node in the larger conflict web

The event uses existing compatible tags. It does not create new special countries.

## Pacing and safeguards

Add temporary cooldowns after a country is selected as aggressor or target.

Recommended behavior:

- baseline cooldowns keep repeated targeting rare
- higher evolutions loosen cooldown limits
- countries already losing major wars receive reduced weight
- baseline pairings should usually be close enough to matter
- higher stages can use less rational pairings while keeping hard exclusions

## Event log and settings

Record:

- Event ID 4
- event name
- aggressor
- target
- realized declaration count and any blocked requested slots
- special chaos country involvement
- active War Contagion stage
- fired count

Event details text should say that Random War creates unexpected wars, and higher chaos allows larger linked war webs and compatible special-country participation.

The event enable setting controls all Random War firings. Evolution settings should select the highest enabled War Contagion stage available under the current chaos tier.

## Presentation and assets

### Report event image

Use a suitable vanilla HOI4 report event image if possible. Existing Chaos Redux imagery is the second choice.

Good subjects:

- military mobilization
- border troops
- troop movement
- diplomatic crisis
- government war announcement

If a new copied or processed asset is needed:

- target size: 210x176
- suggested file: `report_event_random_war.dds`
- suggested sprite: `GFX_report_event_random_war`

### Optional news event image

Use only for wider observer popups tied to majors, faction leaders, special chaos countries, or late evolutions.

Prefer a suitable vanilla HOI4 news event image. Existing Chaos Redux news imagery is the second choice.

Good subjects:

- black-and-white mobilization
- troop columns
- foreign ministry scenes
- crowds reading notices
- troop trains

If a new copied or processed asset is needed:

- target size: 397x153
- suggested file: `news_event_random_war.dds`
- suggested sprite: `GFX_news_event_random_war`

## Localisation direction

### Evolution names

- Triangular Incident
- Four Fronts
- Contagious Ultimatums
- The War Week
- Open Season

### Event details text

Explain:

- Random War creates unexpected wars
- repeatable weighting makes repeated firings less common over time
- chaos unlocks larger war webs
- later stages can include compatible Chaos Redux special countries

## Catalog update text

### Details

Random War catches two countries in a sudden declaration. Later stages can link several wars and draw compatible Chaos Redux powers into the same conflict web.

### Evo I

Gathering Storm: Triangular Incident links three countries in one sudden conflict.

### Evo II

Rising Chaos: Four Fronts links four declarations in one conflict web and may draw in a compatible Chaos Redux power.

### Evo III

Chaos Tier: Contagious Ultimatums links five declarations and can draw major powers, faction members, or a compatible Chaos Redux power into the conflict.

### Evo IV

Totalen Chaos: The War Week links six declarations in a short chain, with a compatible Chaos Redux power likely to participate.

### Evo V

World Collapse: Open Season spreads seven or eight declarations as ordinary events continue, and compatible Chaos Redux powers are likely to join.

### Cluster

Wars. Secondary connection: Minor events.

## Implementation checklist

- Keep event root as `chaosx.nr4.1`.
- Register ID 4 as a repeatable event.
- Keep availability from campaign start.
- Make Wars cluster visibility or active status begin around chaos tier 2.
- Use event targets for selected countries.
- Use scripted effects for country selection, declaration logic, and shared logging.
- Use script constants for thresholds, declaration counts, special-country chances, and cooldown lengths.
- Add aggressor and target cooldowns.
- Add explicit special chaos country compatibility checks.
- Update event registration, event type lookup, event log names, debug names, detail text, localisation, docs, and spreadsheet row together.
- Reuse suitable vanilla or Chaos Redux event images where possible.
- Keep evolved variants readable in the event log and evolution view.
