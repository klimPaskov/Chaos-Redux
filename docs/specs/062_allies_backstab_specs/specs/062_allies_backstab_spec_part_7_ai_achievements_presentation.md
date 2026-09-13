# Event 062 AI, balance, achievements, and presentation

## AI purpose

AI should make betrayal dangerous while preserving basic strategic competence. The event changes alliance behavior, but it does not instruct countries to enter impossible wars, abandon every useful partner, or refuse every viable settlement.

Every weighted selection and AI choice requires a dedicated probability audit before and after implementation.

## Faction-selection AI

The faction selector favors high internal pressure while preserving diversity among valid candidates.

It should respond to:

- faction size
- capability disparity
- political divergence
- recent military strain
- weak institutional ties
- prior betrayal or defection memories
- loss of a common threat
- fresh-faction and Event 62 cooldowns

A large stable faction should not always outrank a smaller alliance already near collapse. Evolution III adds a stronger large-faction preference only after full-fracture conditions are proven.

## Victim-selection AI

The target model should normally prefer weak, exhausted, isolated, low-contribution members.

It should protect:

- the faction leader during baseline selection
- core military and industrial contributors
- strategically essential ports, fronts, and corridors
- recent joiners during grace
- recent Event 62 victims during protection
- subject bundles that cannot be separated safely

A high-casualty country with major war contribution should usually rank below a low-contribution isolated country. The probability scenarios define this ordering as a required audit case.

## Faction leader AI

The leader chooses conflict intent from visible strategic facts.

Forced compliance becomes more likely when:

- the victim remains strategically useful
- the leader expects a quick victory
- the leader wants the country back inside the bloc
- no major territorial claim exists

Territorial settlement becomes more likely when:

- loyalists hold registered cores or claims
- the target territory is reachable
- the claim does not conflict with another loyal member

Regime replacement becomes more likely when:

- ideology hostility is severe
- a viable political replacement exists
- outside sponsors will tolerate the outcome

Liquidation remains rare. AI considers it only when the target is very small, relations are irreparable, Chaos is high, and the diplomatic and military cost is affordable.

Leader AI should secure cohesion before launching a difficult offensive. It accepts settlement when victory is no longer credible.

## Retained-member AI

A retained member evaluates:

- relations with the original leader and victims
- ideology compatibility
- fear of becoming the next target
- military and industrial strength of each side
- shared wars and contradictory enemies
- territorial connection and supply
- war contribution and perceived fairness
- outside sponsors
- prior security promises
- current cohesion

Close partners remain loyal. Politically isolated members with strong victim ties can defect. Distant or exhausted members can withdraw neutrally.

A member does not join a side merely because it is stronger. Survival matters, but relations, war legality, and political identity must remain material.

## Victim AI

Victims prioritize:

1. preventing immediate capitulation
2. protecting the capital and supply route
3. coordinating with co-victims
4. obtaining equipment or guarantees when outmatched
5. seeking recognized separation after survival proof
6. accepting readmission only when the terms preserve government viability

Victim AI does not spend its last equipment on a minor cohesion action while the capital lacks a defense. It does not donate reserves when its own divisions cannot reinforce.

## Outside sponsor AI

An outside power considers:

- relations and ideology
- guarantees and existing treaty obligations
- rivalry with the original faction leader
- strategic interest in the region
- distance, access, convoys, fuel, and equipment
- current war load
- stability and war support
- expected escalation
- whether another sponsor backs the opposite side

Mediation is favored by overextended powers and governments with balanced relations. Material support is favored when one side is strategically valuable and reachable. Direct intervention remains high-Evolution or treaty-bound.

## The Offensive integration

When The Offensive is active, AI receives stronger preference for viable aggressive actions. It should:

- favor punitive operations when supply and force ratio support them
- lower the threshold for a legal defection war
- resist settlement while a plausible offensive path remains

It should not:

- target invalid countries
- ignore shared-war conflicts
- enter a side without access
- choose liquidation by default
- continue a hopeless war after capital, supply, and reserves are lost

## Military balance anchors

The event compares effective side strength rather than raw division count. The calculation should include:

- fielded divisions adjusted by strength and organization
- available manpower
- equipment readiness
- military factories and current output
- air and naval support where the theater requires them
- fuel and supply
- number of active fronts
- capital and route security

Suggested response bands:

| Loyalist to victim strength | Design response |
| --- | --- |
| below `1.25:1` | leader AI prefers limited aims or settlement, victims receive no catch-up package |
| `1.25:1` to `2.5:1` | ordinary crisis balance |
| `2.5:1` to `4:1` | victim support interest rises and emergency costs reduce moderately |
| above `4:1` | strongest emergency tools and outside-sponsor interest, no free victory |

These are starting anchors. Final values require MCP probability and implementation balance evidence.

## Repeatability balance

The event already uses the shared Minor Repeatable weight system. The event also needs local anti-repetition:

- active faction transactions are invalid
- faction cooldown after resolution
- victim country protection after resolution
- fresh faction protection
- successor-faction protection
- no country selected twice in one generation
- no faction selected twice in one generation
- no direct repeat reward from a failed transaction

A later firing can affect former victims after protection expires. Their betrayal memory changes trust and side-choice behavior.

## Achievements

Achievement names below are working labels. Final localisation requires a separate writing pass.

### The Weak Link Holds

**Role:** expelled player country.

**Requirement:** the player was in the highest-vulnerability candidate tier at selection, remained uncapitulated, kept the original capital, and obtained recognized separation or a defensive victory.

**Disqualifiers:** console or debug disqualification under normal achievement policy, loss of original capital for the full failure period, voluntary readmission before survival proof.

**Difficulty:** hard.

**Tracking:** store the selection-tier receipt, starting capital, generation ID, capitulation state, and final outcome.

**Icon direction:** a cracked alliance chain held together around a small national shield. Completed icon shows the shield intact. Grey and not-eligible variants follow the normal achievement triplet.

### Council of the Cast Out

**Role:** expelled player country in a multi-victim purge.

**Requirement:** at least three original victims survive, establish the liaison, reach unified cohesion, form a successor compact, and secure peace with every surviving compact member independent.

**Disqualifiers:** player leaves the victim coalition before settlement, compact forms with fewer than three original victims, any counted member remains a subject of the original leader.

**Difficulty:** very hard.

**Tracking:** original victim array, liaison receipt, cohesion threshold, successor-faction origin, member independence, final peace.

**Icon direction:** several broken table placards arranged into a new circular council.

### No Second Betrayal

**Role:** player faction leader during Evolution II.

**Requirement:** after the first internal split, complete `Prevent a Second Defection`, keep at least five original political units loyal, and resolve the war without another loyal unit leaving.

**Disqualifiers:** a second defection, faction dissolution, player changes country, or the conflict ends through the leader's capitulation.

**Difficulty:** hard.

**Tracking:** original membership snapshot, first split proof, mission receipt, post-split exit counter, final loyal membership.

**Icon direction:** a war council seal with one broken segment and the remaining ring locked together.

### A Seat of Our Own

**Role:** player participant in the Evolution III world-order fracture.

**Requirement:** survive an Evolution III generation, become leader of a valid faction containing members from at least two different shattered original factions, and keep the new faction intact for one year.

**Disqualifiers:** faction created only from one original faction, fewer than three independent political units, loss of faction leadership during the holding period.

**Difficulty:** extreme.

**Tracking:** original faction identities, Evolution III generation receipt, new faction leader, membership origins, one-year timer.

**Icon direction:** two shattered alliance emblems joined beneath a new central chair.

## Achievement implementation rules

Achievements belong in the single Chaos Redux achievement registry. Each needs:

- a stable ID
- trigger and disqualifier logic
- persistent progress receipts
- English localisation
- completed, grey, and not-eligible icons
- event documentation
- catalog or achievement documentation alignment

The event cannot award an achievement from a hidden approximate score without storing the proof used at selection.

## Event and report art

### Main report image

Use a generated World War II era documentary scene. The subject should be the moment of betrayal in physical form, such as allied liaison officers removing a former partner's insignia at a guarded checkpoint, military representatives leaving a joint headquarters under armed watch, or a former ally's flag and documents being taken down while troops seal the gate.

The image should show period uniforms, architecture, vehicles, equipment, and photographic technology. It should avoid readable generated text, modern tactical gear, cinematic color grading, abstract maps, and generic conference-table compositions.

Planned event-picture canvas: `210x176`, subject to exact local consumer inspection.

### Decision category picture

Use a static full-canvas picture that establishes the broken-alliance theme. It can show severed liaison lines, empty chairs in a war council, removed insignia, or a guarded alliance headquarters. It must not contain fake buttons, fake meters, or painted interface controls.

The canonical decision-category picture references should be inspected before production. The current skill reference family uses `114x101`, but implementation must inspect the active consumer before locking size.

### Conditional super-event image

Evolution III's global fracture super-event needs a distinct generated image. It should show several alliance symbols and military delegations separating under armed pressure across one coherent period scene. It should communicate a world order breaking into rival camps without turning into a map graphic.

Planned super-event canvas: `457x328`, subject to exact local consumer inspection.

## Icon package

Each icon family needs its own generated source art and target-specific composition.

### Decision icons

- broken alliance emblem
- war council commitment
- emergency mobilization
- expelled-governments liaison
- foreign guarantee
- conditional readmission
- recognized separation
- faction defection
- neutral withdrawal
- successor compact

### Mission icons

- capital and supply-spine defense
- punitive offensive
- co-victim connection
- prevent a second defection
- armistice conference

### Idea icons

- betrayed by the bloc
- war council purge
- expelled-governments liaison
- coordinated defense
- isolated government

### Achievement icons

Four completed icons and their normal grey and not-eligible variants.

All alpha-backed icons request native transparency and preserve it through PNG and DDS processing. Each icon type uses its own source output. Focus icons, decision icons, idea icons, and achievement icons are never satisfied by resizing one another.

## Asset exclusions

The accepted event design does not introduce new countries, leaders, flags, portraits, units, equipment, technologies, buildings, 3D models, counters, unit audio, focus trees, or animated sprites.

The implementation and asset workers must not add these surfaces as decoration. A later accepted expansion can change the boundary through a new spec addendum.

## Super-event direction

The Evolution III super-event role is global alliance-order fracture.

It needs:

- one intentionally selected slot
- final title, description, reaction text, and verified quote
- unique licensed or public-domain musical audio
- generated image
- settings-aware sound playback
- one-time trigger proof
- documentation and catalog alignment

No quote, cultural reference, or audio selection is fixed by this planning pack. Those require the super-event text and audio research workflows.

## Writing direction

### Main global report

The report should describe concrete signs of alliance rupture. Suitable details include sealed headquarters, removed insignia, border posts closing, liaison officers escorted out, depot access revoked, and former partners receiving conflicting orders.

The text names the largest affected faction and states that other alliances suffered similar purges. It should not list formulas or every affected country.

### Faction leader event

The viewpoint is the government ordering the purge. The tone can use official security language, fear of weakness, and political self-justification. It should reveal the targets and visible war intent without treating the leader's claims as objective truth.

### Victim event

The viewpoint is the expelled government. It should focus on blocked communications, units stranded outside home territory, revoked access, urgent capital defense, and the identity of co-victims.

### Retained-member event

The viewpoint is uncertainty inside the alliance. The member sees which government was removed, which commitments are demanded, and why remaining neutral or defecting carries risk.

### Evolution III report

The public evidence is simultaneous alliance fracture. The text should use several concrete collapses and changing military alignments. It should avoid generic claims that history changed forever.

### Option tone

- faction leader options use security doctrine, ambition, or calculated restraint
- victim options use emergency resolve, bitter restraint, or practical coordination
- retained-member options use loyalty, fear, self-preservation, or open dissent
- mediator options use controlled diplomatic language
- a cutting or ironic option is acceptable for minor role events, but mass casualty outcomes should remain serious

Final wording must mention dynamic faction names, countries, capitals, co-victims, or settlement terms where useful. It must not expose hidden future defections or achievement conditions.
