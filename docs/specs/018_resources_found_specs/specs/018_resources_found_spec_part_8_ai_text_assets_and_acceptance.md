# Event 018 Resources Found Specification, Part 8

## AI, writing direction, presentation, achievements, and acceptance

All names in this file are working labels for design structure. They are not final localisation.

## AI design principles

Event 018 affects ordinary owners, foreign buyers, claimants, neighbors of the cave country, and the cave country itself. Each group needs behavior tied to its actual situation.

AI must understand the event’s public values and strategic consequences. It should not use a flat chance to exploit, close, nationalize, invade, or spawn units.

The full behavior matrix is in `matrices/ai_strategy_matrix.md`. This section defines the intent that implementation must preserve.

## Field-owner AI

### Discovery posture

The owner evaluates:

- domestic deficit in the discovered resource
- current trade dependence
- civilian industry available for development
- current war pressure
- state defensibility
- government ideology and economic policy
- relations with likely investors
- border claims
- stability and public trust
- number of existing active fields

Likely tendencies:

- strong majors prefer national control or strategic reserve
- small weak states prefer foreign concession or balanced buyers
- market-oriented governments accept commercial charters and contracts
- communist or strongly statist governments prefer national authority and state-to-state agreements
- fascist or militarized governments favor wartime requisition, guards, and reserved output
- neutral governments near rivals value commission or guarantee routes

These are weighted tendencies. A desperate communist state can accept foreign machinery, and a democratic major can nationalize a strategic field.

### Development intensity

AI should invest more when:

- the resource deficit is severe
- the field is safe and defensible
- transport is practical
- the country has construction capacity
- the field has several resources
- a valuable contract exists

AI should slow or suspend when:

- the state is about to fall
- safety is catastrophic
- Disturbance or Breach Pressure is high
- the country cannot fund a closure or evacuation later
- the resource is not needed
- another field already provides enough supply

### Safety behavior

AI safety preference should react to ideology, stability, labor policy, casualties, and war need.

Careful AI:

- funds ventilation and medical inspection early
- rotates crews
- suspends after repeated unexplained deaths
- begins closure before Breach Pressure becomes critical

Risk-taking AI:

- accepts more deaths during war or severe shortage
- conceals incidents
- uses military labor
- keeps extracting during Evolution III

Even risk-taking AI should not always choose maximum extraction. It should understand the possibility of losing the state and creating a powerful enemy.

### Closure behavior

AI should attempt full closure when:

- the field’s net economic value has become negative
- public attacks threaten cities
- Breach Pressure is critical
- the owner has the engineering capacity to finish
- the field is not essential to immediate national survival
- the cave-country opening would be severe

AI can refuse closure when:

- defeat in a major war is imminent without the resource
- the government follows an extreme exploitation route
- evacuation and sealing are impossible
- a foreign concession or military faction forces continued operation

## Foreign AI

Foreign AI should target a limited number of fields based on interest score.

### Commercial actors

Prefer normal contracts, development assistance, and long-term access. Avoid coercion when relations and trade routes are good.

### Strategic majors

Seek exclusive rights, guarantees, national allocations, or commission influence when wartime need is high.

### Revisionist claimants

Use survey pressure, local sponsorship, smuggling, and border escalation when they have a real claim and military opportunity.

### Neutral mediators

Support commissions, compensation, demilitarization, and multi-buyer access when a field threatens regional war.

### Cave-crisis response

Foreign countries should change priorities when Evolution III or IV becomes public.

They can:

- provide hard-attack equipment
- send engineers or evacuation transport
- guarantee threatened states
- open access for anti-cave forces
- reduce ordinary rivalries through the world-threat framework
- refuse aid if weak, isolated, or ideologically committed to exploiting the crisis

## Neighbor AI against the cave country

Neighbors need a shared response package.

AI should:

- prioritize anti-tank and high hard-attack divisions
- hold resource-rich states and deny anchors
- recapture newly occupied resource states before activation completes
- demolish or evacuate resource infrastructure when retreat is unavoidable and the chosen policy permits it
- guard supply hubs and tunnel-prone approaches
- concentrate air power against slow cave formations
- avoid repeated soft-infantry attacks into high armor
- seek alliances, access, and aid when the threat exceeds national capacity

A threatened neighbor with no effective hard attack should prefer delay, fortification, evacuation, and foreign aid instead of suicidal attacks.

## Cave-country AI

The cave AI should:

- defend the origin
- rank reachable states by resource capacity, supply value, and strategic access
- attack toward rich states
- activate anchors before overextending
- guard mature anchors
- avoid wasting formations in barren land when a rich route exists
- concentrate against enemies with hard attack
- replace destroyed divisions through the queue
- select hierarchy and doctrine routes based on geography
- complete continent objectives
- use world-end footholds as independent strategic fronts without abandoning the origin continent

The AI must understand excess-capacity penalties. If it loses anchors, it should retreat excess formations toward active anchors, prioritize recapture, or accept controlled brood loss rather than dispersing them across weak fronts.

## Player-facing writing direction

The planning package provides direction only. Implementation writes final localisation.

All player-facing prose should follow the Chaos Redux event style rules:

- no em dash
- no semicolon in sentences
- no staccato fragments for artificial drama
- no thesis versus antithesis versus synthesis framing
- no generic crisis templates
- no process notes or rework history
- no direct warning labels when observed details can show fear and uncertainty
- no hidden mechanics, achievement paths, world-end thresholds, or formulas in ordinary event text

## Baseline event text direction

### Viewpoint

Surveyors, engineers, local workers, transport officials, business organizers, or state authorities.

### Visible information

- the state
- the resource
- the unexpected scale
- development needs
- immediate interest from buyers or government

### Tone

Practical optimism, industrial excitement, commercial urgency, or guarded administrative interest.

### Avoid

- ominous cave references
- unexplained supernatural language
- statements that the resource is a trap
- generic lines about the world changing forever
- map-only summaries

### Option tone

Options should feel like administrative and economic positions. Depending on the country, they can use confident state direction, commercial enthusiasm, cautious understatement, nationalist ownership language, or pragmatic foreign partnership.

## Repeat discovery text direction

Repeat events should mention revised surveys, connected seams, new samples, deeper structures, or a second resource body. They should recognize the field’s current posture and foreign partners.

Do not replay the first-discovery text. A mature national field, concession zone, and suspended reserve should each react differently.

## Trade and diplomacy text direction

### Buyer events

Use commercial and strategic language appropriate to the country. Buyers should mention the actual resource and route.

### Concession disputes

Focus on ownership, compensation, workers, machinery, and delivery obligations. Avoid generic diplomatic outrage.

### Commission events

Describe practical terms such as inspections, quotas, troop limits, roads, and border access. Do not make paperwork the emotional center.

### Border crisis

Use patrols, survey markers, roads, checkpoints, field camps, and local troop movement. Avoid a generic claim that tension has suddenly risen.

## Evolution II text direction

### Early incidents

Use concrete symptoms and objects:

- corroded supports
- failed lamps
- coughing workers
- damaged tools
- missing crews
- knocks that follow shifts
- animals refusing passages

The player should infer that normal explanations are failing through repeated details.

### Worker voice

Workers can use local mine-spirit language, religious interpretation, scientific explanation, or plain fear depending on the region. No one tradition is canonically correct.

### Official voice

Officials can be practical, evasive, exploitative, compassionate, or militarized. Avoid contrast formulas that pair worker fear with official denial.

### Humor

Cheap humor is forbidden because the stage involves sickness and deaths. Grim company euphemism or self-damning propaganda can appear when it condemns the speaker.

## Evolution III text direction

### Public attacks

Describe what people see in settlements and streets. Use movement, wounds, damaged transport, evacuation, and visible creatures.

### Decision tone

- hunt decisions should sound military and practical
- evacuation decisions should emphasize routes, capacity, and priority
- continued extraction can use cold industrial or desperate wartime language
- closure should emphasize sacrifice of the entire field

### Hidden information

Do not expose the exact exploitation-to-starting-army formula.

## Evolution IV and cave-country text direction

### Emergence

The first reveal should communicate organized nonhuman formations, the loss of the field state, and immediate border attacks.

### Cave-country voice

The cave country’s focus and decision text should use original nonhuman vocabulary while remaining mechanically clear. Sensory themes can include pressure, vibration, mineral taste, heat, depth, and collective command.

Avoid:

- comedy growling
- simplistic broken grammar
- human parliamentary language
- borrowed folklore names
- unexplained magic when physical subterranean behavior can carry the concept

## Event Details direction

The Event Details description should explain that a state can reveal a huge random strategic-resource deposit, become a center of investment and trade, and attract foreign attention. It should mention that repeated discoveries can make one field unusually important.

It must not list resource amounts as effects, explain evolution formulas, mention cave monsters, reveal closure as a secret prevention method, or spoil the world-end branch.

Evolution Details can reveal each evolution after it is enabled or logged according to the shared UI pattern.

## Asset coverage

The full asset brief is in `prompts/resources_found_asset_prompt.md`. The event needs the following visible families.

### Report event images

Generated period-documentary report images at 210 by 176 with report-card treatment:

- baseline discovery survey or drilling scene
- compound-field development
- sick lower workings
- missing crew or damaged equipment
- perimeter breach
- evacuation or urban hunt
- full sealing project
- liberated cave anchor cleanup

Each image should be a real scene, not a map or abstract icon.

### News event images

Generated black-and-white period-news images at 397 by 153:

- internationally important compound field
- border crisis around the field
- first public creature attacks
- cave country emergence
- regional containment or major defeat

### Super-event images

Generated fictional images at 457 by 328:

- cave-country emergence
- world-end cross-continent rupture
- global defeat aftermath when justified

### Field UI assets

- baseline resource-field seal
- active development animation
- unsafe field warning state
- Disturbance reveal state
- Breach Pressure critical state
- suspended state
- sealing state
- closed state

Every animated state needs real source frames, sheet DDS, static fallback, preview, manifest, and GFX handoff.

### Cave-country assets

- leader portrait
- animated leader portrait and fallback
- base flag at all three sizes
- world-end cosmetic flag if identity changes
- country emblem
- commander portraits if commanders are implemented
- cave division or unit identity art where the UI requires it

### Icons

Separate generated asset families are required for:

- focus icons
- idea and national spirit icons
- decision icons
- decision category icons
- achievement icons
- warning and mechanic icons

Do not satisfy one icon type by resizing another.

## Achievement set

Achievements are planned in full in `prompts/resources_found_achievement_prompt.md`. The set should cover ordinary economic mastery, dangerous greed, successful closure, cave-country play, anti-cave victory, and world-end completion.

Working achievement concepts:

### One Vein to Rule the Market

Build one Event 018 resource type in one state to an extreme total through repeated discoveries. The exact threshold should be difficult and above one ordinary firing.

### The Whole Periodic Table, Figuratively

Create a field containing all six standard strategic resources before the cave country emerges.

### Seal It While We Still Can

Complete full Evolution III closure after public attacks begin, remove every Event 018 addition, and prevent Evolution IV.

### Thirty From Below

Cause a cave-country emergence with the maximum 30 starting divisions, then survive or defeat the resulting crisis as the former owner.

### Contract of the Century

Build a stable high-yield field with a long-term contract, strong safety, and no active border crisis.

### No Claims Left Unsettled

Resolve a severe resource dispute through commission, demilitarization, or compensation without losing the field to war.

### Ten From One State

As the cave country, activate the full 10-division capacity from one captured state.

### The Last Shaft Closed

Defeat a regional cave country and clear every active resource anchor without triggering world end.

### Continental Appetite

As the cave country, consume the origin continent and trigger the Event 018 world-end scenario.

### Every Worker Came Home

Develop and permanently close a meaningful field with no Event 018 deaths. This requires strong safety and should disqualify concealment or coercive labor.

The final set should include difficult tracking and disqualifiers. No achievement should unlock merely because the event fires.

## Balance and anti-exploit direction

Implementation must test:

- repeated discovery stacking
- exact closure subtraction
- state transfer and ownership changes
- contract duplication
- multiple active fields
- same-resource duplicate rolls
- all-resource Evolution III opening
- starting army cap
- origin-state exclusion
- capacity activation delay
- capacity loss and excess-unit penalties
- automatic spawn pacing
- neighbor war refresh
- continent eligibility
- cross-continent foothold validity
- world-end single-fire protection
- AI closure and exploitation choices

Key exploits to prevent:

- closing a field to delete preexisting resources
- reopening a permanently closed state for repeated free deposits
- firing several contracts for the same exclusive output
- repeatedly transferring a state to duplicate field initialization
- counting the origin state in captured capacity
- gaining more than 10 capacity from one state
- instant spawning from a state held for only a day
- keeping full-strength armies after all anchors are lost
- farming cave divisions through occupation flicker
- using the cave country’s zero equipment cost to train normal units
- route switching to collect every hierarchy and doctrine capstone
- triggering the world end from excluded islands or temporary control

## Meaningful validation scenarios

The implementation completion report should record results from scenario-based checks.

### Baseline safe field

A normal country discovers one resource, develops carefully, signs a contract, stabilizes, and closes. Confirm economic usefulness, exact ledger, AI decisions, and clean removal.

### Repeat enrichment

The same field receives several random rolls, including a duplicate resource. Confirm stacking, display, discovery count, and closure subtraction.

### Concession transfer

A field with a foreign partner changes owner. Confirm the physical field transfers, contracts review, and no duplicate first-discovery reward occurs.

### Border dispute

A valid claimant escalates through survey, patrol, mission, and border war. Confirm off-ramps, state transfer, settlement, and field persistence.

### Evolution II careful owner

High safety and restricted workings reduce casualties and slow Disturbance. Confirm competent safety matters.

### Evolution III full seal

Public attacks begin. The owner evacuates, hunts, seals, removes Event 018 resources, and permanently blocks Evolution IV.

### Maximum breach

An extreme field creates exactly 30 starting cave divisions, excludes the origin from future capacity, and declares war on all land neighbors.

### Captured capacity

Test states with 0, 9, 10, 48, 100, and more than 100 total resources. Confirm capacities of 0, 0, 1, 4, 10, and 10.

### Capacity loss

Lose several anchors while over capacity. Confirm divisions weaken instead of vanishing and replacement queues adjust.

### Cave AI campaign

Observe target choice, anchor defense, hard-attack response, and continent progress across several fronts.

### World-end threshold

Confirm the terminal branch requires chaos above 1000, verified continent consumption, no existing world end, valid footholds, unique super-event, and event-system freeze.

### Global defeat

Liberate every cave state and foothold. Confirm threat-source cleanup, resource restoration, aftermath gating, and no secret unavoidable restart.

## Specification acceptance

The design pack is accepted only if implementation preserves all of the following:

- random standard resource selection
- large baseline deposit around 100
- exact event-owned ledger
- repeatable stacking in persistent fields
- complete baseline economy and closure with evolutions disabled
- dynamic field values and compact management UI
- meaningful contracts and foreign interest
- valid border escalation and demilitarization
- separate pre-fire and active evolution paths
- gradual horror progression
- real population loss through shared Deaths
- guaranteed successful pre-breach closure
- full nonhuman country package
- dynamic 6 to 30 starting army
- one division per 10 captured resources, capped at 10 per state
- origin-state exclusion
- automatic paced spawning without manpower or equipment
- slow armored units with hard-attack counterplay
- neighbor war refresh
- real focus tree, AI, assets, and decisions
- continent plus chaos world-end gate
- stronger cross-continent emergence
- distinct regional and global aftermath
- aligned logs, docs, spreadsheet, assets, super-events, and achievements

No smaller fallback version counts as full implementation without explicit user approval.
