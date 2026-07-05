# Event 014 Cannibalism, world-end route, super-events, assets, and triggerable scenario

This file continues the Event 014 source design. All names are working labels and not final localisation.

## Super-event roles

Event 014 can remain low severity in ordinary campaigns. Super-events are reserved for moments that change world understanding.

### Super-event role 1, cannibal islands reveal

Use only if Evolution II creates multiple silent islands, an independent cannibal country, or a remote commune that foreign governments can no longer dismiss.

Trigger direction:

- Evolution II active
- one cannibal country exists or multiple island silence states reached severe status
- at least one normal country receives public evidence
- not already hidden by a world-end branch

Tone direction:

- uncertain naval and military reports
- ships missing or returning wrong
- foreign ministries refusing to name the island until verification
- strong horror without explaining Hannibal

Image direction:

- generated period-documentary super-event image
- island shore, ruined dock, signs of violent consumption, military debris, no readable text
- gore is required and should be fictional

Quote direction:

- research required
- look for public-domain literature, siege writing, famine testimony, or religious material about hunger, taboo, and the collapse of restraint

Button remark direction:

- research required
- grim, maritime, or bureaucratic understatement

Audio direction:

- research required
- real licensed music, tense and cold, preferably low strings, chant, or funeral march mood

### Super-event role 2, Hannibal network reveal

Use only if the Hannibal event exists and the cult connection becomes public.

Trigger direction:

- Hannibal exists
- Evolution III active
- Hannibal resonance or cult network reaches a high threshold
- one cannibal country, multiple infected countries, or a major exploited cult network exists

Tone direction:

- organized will behind scattered horrors
- reports that separate outbreaks share the same discipline, symbols, or orders
- public revelation that the hunger ideology has a commander, patron, or prophet

Image direction:

- generated super-event image
- central Hannibal-linked figure or obscured commander if portrait not finalized
- ritual table, military maps, cult officers, explicit fictional gore
- no final likeness unless Hannibal asset exists

Quote direction:

- research required
- use public-domain or historical material about appetite, command, empire, or moral corruption

Button remark direction:

- research required
- short and cold, avoid comedy

Audio direction:

- research required
- unique licensed track, controlled and imperial rather than chaotic

### Super-event role 3, world-end scenario

Use only when the route becomes terminal.

Trigger direction:

- chaos exceeds world-end threshold
- world_end flag is not set
- Hannibal exists and has enough power, or a later accepted spec allows a non-Hannibal terminal cannibal network
- cannibal countries or cult networks control enough territory, population pressure, or death-system impact
- the normal event system should freeze according to world-end rules

Tone direction:

- campaign terminal state
- governments understand that the cult no longer hides inside armies
- the world is being reorganized as hunting ground and larder
- avoid generic apocalypse wording

Image direction:

- generated fictional super-event image with global scale
- burning capitals, ritual command center, columns moving through ruined streets, explicit gore
- strong central composition for HOI4 super-event UI

Quote direction:

- research required
- scripture, public-domain tragedy, philosophical writing, or ancient literature about devouring, judgment, hunger, and human collapse

Audio direction:

- research required
- final track must be unique and licensed, no drones or generated tones

### Super-event role 4, defeat aftermath

Use only if the threat reached global or near-global scale and was later defeated.

Trigger direction:

- cannibal world threat source active for a meaningful time
- at least one cannibal country controlled significant territory or Hannibal network was public
- the last cannibal country is defeated and cult pressure falls below global threshold
- no terminal world-end route has already locked the campaign

Tone direction:

- grim recovery and record keeping
- trials, missing-person lists, burned islands, rebuilt field hospitals
- no easy triumph

Image direction:

- generated report or super-event image depending on scale
- field tribunal, empty island dock, sealed archive room, memorial ledgers, signs of gore as aftermath

Quote direction:

- research required
- memory, responsibility, survival, and fear of recurrence

## World-end route

Working label, not final localisation: `The World as Larder`.

This is a terminal scenario. It should not be the default path.

### Required build-up

The route requires all of these concepts:

- Event 014 has evolved to global network scale
- cannibalism is no longer one country's army problem
- Hannibal exists
- deaths, territory, cult nodes, or infected states show the network can survive normal containment
- chaos exceeds the world-end threshold

### Terminal behavior

Once triggered:

- set global world-end flag
- set scenario-specific world-end flag
- set matching super-event visibility
- set current super-event audio id through the settings-aware helper
- freeze incompatible future random events according to world-end rules
- mark cannibalism as a world-threat source until terminal transition overrides ordinary threat handling
- cannibal countries become the main terminal threat
- ordinary countries receive emergency anti-cannibal cooperation options if the world-end framework allows final resistance play

### World-end mechanics

The world-end route should use the deaths system heavily.

- cannibal-controlled states suffer periodic civilian deaths and population reduction
- starving or captured military units add military death logs
- resistance collapses in some areas and rises violently in others
- state industry can be damaged or abandoned
- food, supply, trains, convoys, and ports become strategic objectives
- global panic and refugee pressure can feed other systems if they remain active

### Player interaction during world-end

If the player is a normal country:

- emergency coalition decisions
- evacuate capitals and ports
- guard rail corridors
- burn captured ledgers
- destroy cult courier routes
- choose whether to cooperate with former enemies
- hunt Hannibal if the Hannibal event provides a target

If the player is a cannibal country:

- coordinate or conquer other cannibal actors
- capture capitals and ports
- convert hunting grounds into recruitment and supply
- complete Hannibal network objectives if available
- reach terminal victory conditions

The route should remain playable, not become a single popup and game over.

## Triggerable scenario

Add a manual scenario after implementation facts exist.

Working scenario label, not final localisation: `Cannibalism`.

Scenario types:

- War Horror Opening. One country at war receives the baseline report.
- Cult Seeds. One or more countries begin at Evolution I with cult pressure visible.
- Silent Islands. A remote island or cut-off garrison starts near Evolution II.
- Cannibal Commune. A cannibal country appears immediately with scaled state and unit package.
- Hannibal Network. Locked until the Hannibal event exists or a test bypass is explicitly allowed.

Intensity stops:

- Low. One target country, low pressure, easy containment.
- Medium. One severe target country or two exposure countries, stronger spread pressure.
- High. Multiple countries or one island commune near formation.
- Maximum. Immediate cannibal country with high chaos opening and global reaction, but no world-end unless the Hannibal type is selected and allowed.

Manual scenarios should not require normal chaos tier, date, evolution history, or prior event state. They should only block impossible launches, dead scopes, missing countries, or active terminal conflicts.

## Asset direction

Gore is a required visual component for this event. Use generated fictional gore, symbolic gore, or stylized gore for event images, super-event images, icons, animated UI, and portraits. Do not use real photographs of identifiable victims or real atrocities as gore references. Sourced historical material can support research and non-gore documentary framing, while gore should be generated or fictionalized.

### Required asset families

Report images:

- first field report, 210 by 176
- field hospital audit, 210 by 176
- prison kitchen seizure, 210 by 176
- island inspection, 210 by 176
- empty village aftermath, 210 by 176
- contained aftermath, 210 by 176

News images:

- minor news for public leak, 397 by 153, black and white
- cannibal country declaration, 397 by 153, black and white
- global network public reveal, 397 by 153, black and white

Super-event images:

- cannibal islands reveal, 457 by 328
- Hannibal network reveal, 457 by 328
- world-end terminal scenario, 457 by 328
- defeat aftermath if needed, 457 by 328

Idea and national spirit icons:

- cannibalism in the ranks
- sealed kitchens
- military tribunal pressure
- ritual hunger
- no common rations
- hunted by the living
- eating ledger
- Hannibal discipline
- contained aftermath
- exploitation stain

Decision icons:

- secure field kitchens
- rotate compromised units
- ration convoy
- hospital audit
- prison transfer freeze
- island inspection
- evacuation
- break ritual cell
- exploit terror
- dismantle terror units

Decision category icon:

- frontline hunger office

Focus icons:

- full coordinated focus icon family for the cannibal shared tree
- opening survival
- command hierarchy
- supply and economy
- military formations
- expansion
- cannibal pact
- Hannibal branch
- world threat branch

Country identity assets:

- `CBL` base flag, normal, medium, small
- ideology variants if the implementation uses ideology flags
- Last Table cosmetic flag if formable is implemented
- Hannibal dominion flag only after Hannibal spec confirms it
- generated fictional leader or council portrait, 156 by 210
- animated council or leader portrait for high-chaos route, with static fallback
- faction emblem for cannibal pact

Achievement icons:

- one completed 64 by 64 icon for each achievement
- grey and not-eligible variants if the achievement system needs them

### Animated assets

Animation is useful because the mechanic is about hidden pressure becoming visible.

Planned animations:

- decision category seal, 64 by 64 or existing category size, 8 frames, slow pulse, gore required, static fallback
- cult pressure warning frame, 64 by 64 or UI meter size, 8 frames, active only after Evolution I, static fallback
- island silence signal, target GUI card size, 8 to 12 frames, radio flicker and bloodied paper, static fallback
- Hannibal resonance seal, hidden until Hannibal exists, 8 to 12 frames, stronger ritual motion, static fallback
- cannibal council portrait overlay, 156 by 210 or overlay size, 8 frames, subtle breathing candlelight and gore details, static fallback
- world-end progress border, UI panel size, 12 frames, severe warning state, static fallback

Every animated asset must follow the frame-animation workflow. It needs separate source frames, processed frames, sheet PNG, sheet DDS, preview GIF for review only, static fallback DDS, manifest entry, and gfx handoff.

## Localisation handoff

Final player-facing localisation must be written during implementation.

Text surfaces:

- event name and short event detail
- opening country event
- follow-up report events
- minor news event
- evolution log names and descriptions
- decision category header
- decision names and descriptions
- mission objective text
- state modifier names and descriptions
- national spirit names and descriptions
- cannibal country names, party names, leader names, cosmetic names
- focus names and descriptions for shared cannibal tree
- formable decision text
- triggerable scenario text
- super-event title, description, quote, and button remark after research
- achievement titles and descriptions

Text rules:

- early baseline does not reveal the global cult path
- Event Details and spreadsheet details describe the situation, not mechanical effects
- options can use grim irony only when it condemns the speaker or fits bureaucratic denial
- exploitation text should be self-damning and severe, not comedic
- cult and Hannibal text must not use unresearched final cultural references

## Acceptance criteria

Implementation is complete only when these surfaces align:

- event registration and Minor Fire-Once classification
- target validity and fire-once behavior
- baseline country event and follow-up events
- staged idea and state modifiers
- decisions, missions, costs, AI behavior, tooltips, and cleanup
- evolution logging for Evolution I, II, and III
- spread model with per-country containment
- cannibal country package if Evolution II country creation is implemented
- shared cannibal focus tree if any cannibal country can persist
- starting forces and reinforcement pathways
- world threat integration for global stage
- Hannibal hooks that do not require Hannibal to exist yet
- world-end branch gated by chaos and Hannibal requirements
- super-event research and audio for any super-event implemented
- all required assets, animated assets, static fallbacks, and manifests
- docs and spreadsheet alignment
- achievement surface
- completion audit with no undisclosed simplifications
