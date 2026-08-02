# Fallout Ash-Week Orientation Contract

## Status

The user approved this contract on 2026-07-18. It is accepted Fallout source design and authorizes implementation within the scope boundaries below.

Approval does not claim that any event, localisation, caller, asset, log entry, event-detail entry, or audit already exists. The accepted package remains dormant. It does not set `fallout_event_scheduler_activation_approved`, `fallout_event_scheduler_active`, any manual-scenario activation flag, or any transition request flag. The Fallout living-world count remains 0 of 660 manually reviewed blocks until the full orientation tranche passes its implementation and audit gates.

## Purpose

The Ash-week orientation package gives every materialized playable Fallout successor five distinct opening components:

1. national orientation
2. capital or main-state condition
3. immediate resource crisis
4. government-archetype introduction
5. first character or institution

The package explains the successor's actual survival ledger, establishes durable opening memory, and completes the existing five-part orientation receipt. It does not start the ordinary scheduler. A separate reviewed activation contract remains required after orientation, successor allocation, player continuation, and runtime ownership are proven.

## Scope boundary

Implementation may touch only the following Fallout-owned surfaces:

- `events/fallout_world_end_events.txt`
- `common/script_constants/fallout_consolidated_constants.txt`
- `common/scripted_effects/fallout_consolidated_effects.txt`
- `common/scripted_triggers/fallout_consolidated_triggers.txt`
- Fallout event localisation and scripted localisation files
- `interface/fallout_consolidated.gfx` for dedicated report sprites
- dedicated files under `gfx/event_pictures/fallout/`
- the Fallout event log, event details, manifests, proof documents, and workbook after implementation facts exist

The package must not implement or alter:

- scheduler activation
- the manual scenario or province sweep
- successor allocation, tag materialization, or the NZL pilot
- the blackout GUI
- treaty, intelligence, trade-route, active-combat winter, or strategic-bombing systems
- strategic-singularity request ownership
- final focus trees or decisions

No fallback successor, fallback character, generic country-memory row, or substitute asset is authorized.

## Reserved identifier allocation

The accepted contract reserves suffixes `62` through `84` for this orientation package. Suffixes `100` through `126` remain reserved for the living-world pilot and are not reused.

| Suffix | Event role | Visibility | Follow-up |
| ---: | --- | --- | --- |
| 62 | national orientation root | human visible | 64 |
| 63 | national orientation root | hidden AI | 65 |
| 64 | national orientation result | human visible | 66 |
| 65 | national orientation result | hidden AI | 67 |
| 66 | capital condition root | human visible | 68 |
| 67 | capital condition root | hidden AI | 69 |
| 68 | capital condition result | human visible | 70 |
| 69 | capital condition result | hidden AI | 71 |
| 70 | immediate resource crisis root | human visible | 72 |
| 71 | immediate resource crisis root | hidden AI | 73 |
| 72 | immediate resource crisis result | human visible | 74 |
| 73 | immediate resource crisis result | hidden AI | 75 |
| 74 | government archetype root | human visible | 76 |
| 75 | government archetype root | hidden AI | 77 |
| 76 | government archetype result | human visible | 78 |
| 77 | government archetype result | hidden AI | 79 |
| 78 | character or institution root | human visible | 80 |
| 79 | character or institution root | hidden AI | 81 |
| 80 | character or institution result | human visible | 82 |
| 81 | character or institution result | hidden AI | 83 |
| 82 | orientation closure | human visible | 84 |
| 83 | orientation closure | hidden AI | 84 |
| 84 | orientation cleanup | hidden | none |

These 23 identities are reserved for the Ash-week orientation package. They become countable only after their callers, localisation, effects, AI, delayed results, memory, cleanup, six dedicated assets, log entries, event details, and manual review are complete.

## Eligibility barrier

No root may be issued unless all of the following are current for the same transition generation:

- Fallout map return is complete
- the successor allocation receipt is complete
- the survival numerical ledger is committed
- the country belongs to the frozen Fallout successor registry
- the country has a living materialized tag
- the player-continuation owner is already preserved
- the country has one manually reviewed nine-region row
- the country has one manually reviewed twelve-archetype row
- the country has one country-memory row
- the required capital or main-state target is bound and owned
- the required character or institution registry has at least two valid curated candidates

A missing row blocks orientation for that country and records a typed diagnostic. It does not select a generic row.

## Five-component order

The components run in the exact order listed below. A component result records its existing orientation receipt only after its delayed transaction reaches success, partial success, or failure. The next root is issued only after that current-generation receipt exists.

| Component | Root | Result delay | Receipt value |
| --- | ---: | ---: | --- |
| national orientation | 62 or 63 | 2 days | `national_orientation` |
| capital condition | 66 or 67 | 3 days | `capital_condition` |
| immediate resource crisis | 70 or 71 | 4 days | `immediate_resource_crisis` |
| government archetype | 74 or 75 | 3 days | `government_archetype` |
| character or institution | 78 or 79 | 2 days | `character_or_institution` |

The closure is eligible only after `fallout_event_orientation_is_complete` proves all five receipts for the current generation. The closure does not set either scheduler activation flag.

## Shared deterministic result model

Each root records one immutable component transaction with:

- transition generation
- country registry index
- component identity
- visible or hidden mode
- selected branch
- exact state target when applicable
- exact character or institution target when applicable
- frozen region and archetype identities
- frozen relevant survival inputs
- issue date and day
- exact due day
- event token
- result-issued marker written last

Each result calculates a score from the frozen transaction. No random list, random country, random state, or variable timing is allowed.

The accepted common score bands are:

| Score | Outcome |
| ---: | --- |
| 70 or more | success |
| 45 through 69 | partial success |
| below 45 | failure |

Each component receives a base score of 50. Implementation must put all additions and deductions in typed script constants. The shared allowed inputs are:

- plus 15 when the branch's primary resource is at least 60
- plus 8 when it is at least 40 but below 60
- minus 12 when it is below 20
- plus 10 for a manually declared archetype match
- plus 6 for a manually declared regional match
- plus 5 when Recognition is at least 50
- minus 8 when Recognition is below 25
- minus the state's exposure pressure mapped to a 0 through 15 deduction
- plus the state's recovery and adaptation support mapped to a combined 0 through 12 addition
- minus 10 when a relevant unresolved opening crisis exists

The exposure mapping is exact:

| Frozen exposure | Score deduction |
| ---: | ---: |
| 0 through 19 | 0 |
| 20 through 39 | 4 |
| 40 through 59 | 8 |
| 60 through 79 | 12 |
| 80 through 100 | 15 |

Recovery and adaptation are each clamped to 0 through 100. Their sum is multiplied by `0.06` and rounded once to produce the 0 through 12 support addition. Resource, Recognition, Cohesion, recovery, adaptation, shelter, reclamation, and exposure mutations are clamped to their accepted bounds after each transaction. All values in this section become typed script constants. None may remain as an inline tuning number in gameplay effects.

Exact ties use the lowest stable branch identity. AI evaluates the same score and effects as the human path. It chooses the highest projected score after survival-need weighting. Exact ties use the lowest stable branch identity. Hidden AI events may not receive reduced costs or guaranteed success.

## Component contract

### National orientation

The root describes the surviving territory, population loss, government reach, and the strongest and weakest numerical survival values. Text must use the country's region, archetype, and cause memory.

The three required branch families are:

- complete a household and workplace register
- recognize district and settlement compacts
- impose an emergency command register

Every branch spends a meaningful combination of Food, Clean water, Filters, Fuel, Scrap, or Shelter capacity. No branch spends political power. The delayed result must change Recognition and Cohesion by at least 4 points in opposite risk patterns. A failure must also create a concrete shortage, unrest, building-damage, or Deaths consequence. Success records the chosen national-authority memory. Partial success records both the authority memory and its contested form. Failure records the failed authority memory and closes the transaction without a retry reward.

The accepted branch transaction uses these exact values:

| Branch | Cost at root | Success result | Partial result | Failure result |
| --- | --- | --- | --- | --- |
| household and workplace register | Food 4, Clean water 3, Filters 2 | Recognition plus 10, Cohesion plus 6 | Recognition plus 5, Cohesion plus 2 | Recognition minus 6, Cohesion minus 5, Food minus 4 |
| district and settlement compacts | Food 3, Shelter capacity 5, Scrap 2 | Recognition plus 7, Cohesion plus 10 | Recognition plus 3, Cohesion plus 5 | Recognition minus 5, Cohesion minus 7, Shelter capacity minus 4 |
| emergency command register | Fuel 4, Filters 4, Scrap 3 | Recognition plus 5, Cohesion plus 8, one 90-day command modifier | Recognition plus 2, Cohesion plus 3, one 45-day contested-command modifier | Recognition minus 9, Cohesion minus 6, one 90-day command-resistance modifier |

The failure branch also records a Deaths transaction equal to `0.001` of the country's post-rewrite population when Recognition began below 20. The request is rounded, clamped to the available living population, and recorded through Deaths.

### Capital or main-state condition

The target is the preserved capital when it is owned and valid. Otherwise it is the deterministic highest-priority owned state from the accepted main-state registry. This is an eligibility rule, not a fallback to an arbitrary state.

The three required branch families are:

- seal and heat the civic core
- disperse stores and offices across surviving districts
- evacuate the poisoned core into a prepared receiving state

The root must show the target state's grade, phase, exposure, shelter, surviving infrastructure, and population receipt. Regional variants must distinguish snow, frost, cold rain, ash, dead vegetation, frozen water, dim light, and thaw where they apply.

The evacuation branch is available only with an exact prepared receiving state and a balanced migration transaction. The result must reconcile population movement, building damage or repair, shelter pressure, supply access, and Deaths. A failed evacuation may not delete population from the source without the matching Deaths and destination receipts.

The accepted branch transaction uses these exact values:

| Branch | Cost at root | Success result | Partial result | Failure result |
| --- | --- | --- | --- | --- |
| seal and heat the civic core | Filters 6, Fuel 6, Scrap 4 | target exposure minus 10, shelter plus 8, recovery plus 6, repair one eligible infrastructure level | target exposure minus 5, shelter plus 4, recovery plus 2 | target exposure plus 7, shelter minus 5, damage one eligible infrastructure level, Deaths equal to 0.002 of target population |
| disperse stores and offices | Food 4, Scrap 6, Power 4 | target shelter plus 10, adaptation plus 7, supply value plus 6 | target shelter plus 5, adaptation plus 3, supply value plus 2 | target shelter minus 6, supply value minus 5, Deaths equal to 0.0015 of target population |
| evacuate the poisoned core | Fuel 8, Food 6, Shelter capacity 5 | move 20 percent of the frozen source population request, destination shelter plus 6, source exposure minus 8 | move 12 percent, destination shelter plus 2, source exposure minus 4 | move 6 percent, record Deaths equal to 0.04 of the intended 20-percent migrant request, source exposure plus 5 |

Migration uses the frozen source request. The source decrement equals destination increment plus exact Deaths. The one-person floor applies to the source. A capacity clamp reduces the whole request before any mutation and is recorded in the result text.

### Immediate resource crisis

The crisis identity is the lowest normalized current value among Food, Clean water, Medicine, and Filters. Exact ties use that fixed order. Fuel, Power, Scrap, Shelter capacity, and Recognition remain scoring and payment inputs.

The three required response families are:

- strict public rationing with a published ledger
- emergency requisition from protected stores
- a locally tailored production or distribution measure

The third response must be manually selected for each region and archetype pair. Examples include thaw-water capture, cistern control, insulated rail distribution, fishing access, seed protection, and filter workshops. These are design directions, not final localisation.

Success must improve the selected crisis value by at least 8 points and consume at least 4 points from one supporting resource. Partial success improves it by 4 to 7 points and creates a durable dispute or fatigue memory. Failure may not grant the selected resource. It must apply a concrete supply, disease, Deaths, recognition, or building consequence.

The accepted branch transaction uses these exact values:

| Branch | Cost at root | Success result | Partial result | Failure result |
| --- | --- | --- | --- | --- |
| strict public rationing | Cohesion 5 | crisis resource plus 10, Recognition plus 6 | crisis resource plus 5, Recognition plus 2, Cohesion minus 2 more | no crisis resource gain, Recognition minus 5, a 60-day ration unrest modifier |
| emergency requisition | Recognition 7, Cohesion 4 | crisis resource plus 16 | crisis resource plus 7, Recognition minus 3 more | no crisis resource gain, Recognition minus 8 more, Deaths equal to 0.0015 of country population |
| tailored production or distribution | Scrap 6 and either Power 4 or Fuel 4 from the reviewed regional row | crisis resource plus 13, Reclamation plus 5 | crisis resource plus 6, Reclamation plus 2 | no crisis resource gain, Scrap minus 4 more, one relevant building level damaged when available |

When the selected crisis value is Food, Clean water, Medicine, or Filters, a cost may not subtract that same resource. The reviewed regional row chooses Power or Fuel before the root transaction. A result cannot raise the crisis value above 100.

### Government archetype

The package must support exactly twelve manually reviewed archetypes. Each archetype receives one concrete root-text block, three tailored branch descriptions, branch-specific AI weights, and at least one distinct effect. Scripted localisation may select those blocks. A single generic paragraph with substituted archetype names does not satisfy the contract.

Each root must present:

- consolidation of the current emergency authority
- a negotiated division of authority with a region-appropriate institution
- an archetype-specific rival claim to legitimacy

The result may set government memory, unlock later focus or decision layers, alter Recognition and Cohesion, and add a substantial timed or persistent country modifier. It must not perform a broad ideology or tag rewrite. Any later government change needs its own accepted country-package contract.

The accepted branch transaction uses these exact values before archetype-specific additions:

| Branch | Cost at root | Success result | Partial result | Failure result |
| --- | --- | --- | --- | --- |
| consolidate current authority | Food 3, Fuel 3 | Recognition plus 7, Cohesion plus 8, 180-day authority modifier | Recognition plus 3, Cohesion plus 4, 90-day contested-authority modifier | Recognition minus 8, Cohesion minus 6, 120-day legitimacy crisis |
| negotiated division of authority | Food 4, Shelter capacity 4 | Recognition plus 11, Cohesion plus 7, institution compact memory | Recognition plus 5, Cohesion plus 2, disputed compact memory | Recognition minus 6, Cohesion minus 5, one later institution dispute ticket |
| archetype-specific rival claim | Scrap 5, Fuel 4 | Recognition plus 5, Cohesion plus 10, rival integrated memory | Recognition plus 1, Cohesion plus 4, rival autonomous memory | Recognition minus 10, Cohesion minus 7, rival rupture memory |

Each archetype adds one exact non-cosmetic effect worth at least 5 ledger points or a 90-day modifier with at least a 5-percent operational consequence. The coverage matrix must state that effect before implementation. It may not use a one-percent modifier or a political-power award.

### First character or institution

Every successor needs a curated candidate registry before this component can run. Real people, flags, and attested institutions require sourced manifests. Fictional successors use generated fictional characters and institutions through the approved asset workflow. Mutant content is treated as fictional high-chaos society content.

The root presents two or three valid candidates with distinct survival roles, costs, risks, and later memories. At least one branch must prioritize administration or relief. At least one must prioritize security or extraction. A third branch may represent a regional institution, technical body, faith network, labor organization, military remnant, or civic council when historically or fictionally appropriate.

Success installs the exact character or institution and records its relationship memory. Partial success installs a contested or limited form with a delayed liability. Failure consumes the committed cost and records injury, refusal, factional rupture, institutional collapse, or Deaths as appropriate. A failed branch cannot be selected repeatedly for free.

The accepted branch transaction uses these exact values:

| Branch | Cost at root | Success result | Partial result | Failure result |
| --- | --- | --- | --- | --- |
| relief or administration candidate | Medicine 5, Food 5 | install exact candidate, Recognition plus 8, recovery plus 5 in the main state | install limited candidate, Recognition plus 4, recovery plus 2, 120-day capacity liability | no installation, Medicine minus 3 more, Recognition minus 5, refusal or injury memory |
| security or extraction candidate | Fuel 5, Scrap 5 | install exact candidate, Cohesion plus 7, supply value plus 5 in the main state | install contested candidate, Cohesion plus 3, Recognition minus 3, 120-day coercion liability | no installation, Cohesion minus 6, Deaths equal to 0.001 of country population, rupture memory |
| regional institution | Power 4, Shelter capacity 4, Scrap 4 | install exact institution, Recognition plus 7, Reclamation plus 6 | install limited institution, Recognition plus 3, Reclamation plus 3, dispute memory | no installation, Recognition minus 7, Shelter capacity minus 4, collapse memory |

The root exposes only candidates whose exact cost can be paid. If fewer than two candidate branches remain affordable and valid, the component stays blocked with a typed diagnostic. It does not create a free option.

## Regional and archetype coverage

The accepted implementation must provide a manual coverage matrix for nine regions and twelve archetypes. Each cell records:

- applicable national-authority language
- capital-condition emphasis
- local resource response
- government institution or rival
- candidate character or institution class
- one meaningful AI preference
- one prohibited or unavailable branch where the world state requires it

Country-memory overlays then replace or extend these cells for selected successors. An overlay must cite the exact existing pre-Fallout memory, terminal cause, leader survival receipt, territorial history, or institution registry that makes it applicable. No overlay may depend only on a country tag name.

## Human and AI ownership

Human roots use visible events. AI roots and results are hidden and apply the same branch costs, score bands, result effects, memory, and cleanup.

The future caller must preserve host authority and issue only one mode per country. A country that changes human control while a component is pending keeps its original transaction mode until that component closes. The next component may use the current control mode. This prevents duplicate visible and hidden resolutions.

## Save recovery and cleanup

The component transaction writes payload fields before its pending marker. The result-issued marker is written only after the event command is committed. A load before issue may issue the same result once. A load after issue preserves the exact token and may not issue a second result.

Event `84` performs authenticated cleanup. It clears only temporary component payloads, issue tokens, due-day fields, and transient targets. It preserves:

- the five current-generation orientation receipts
- branch and outcome memories
- installed character or institution identity
- regional, archetype, and country-memory identity
- survival-ledger current and initial values
- Deaths receipts
- later focus and decision unlock memory

A stale generation cancels the pending component with a typed reason and clears its temporary payload. It does not promote the stale receipt into the current generation.

## Scheduler handoff

After event `84`, the country must prove:

- all five orientation receipts are current
- no orientation transaction remains pending
- no orientation event token remains issued
- all component targets are cleared
- all durable branch and outcome memories are internally consistent

The package may set an orientation-closure receipt. It must not set `fallout_event_scheduler_activation_approved` or `fallout_event_scheduler_active`. Family fatigue remains at its initialized value. Cooldown mutation begins only after a separately approved ordinary-event activation contract.

## Localisation direction

Working labels in this contract are not final localisation.

Final text must name concrete conditions, districts, institutions, resources, weather, and authority disputes. It must react to region, archetype, country memory, state grade, resource crisis, and outcome. It must not use generic apocalypse wording, implementation language, staged contrast formulas, em dashes, or semicolons.

Visible roots and results require event titles, descriptions, option text, effect tooltips, log entries, event-detail entries, and evolution-detail text where durable identity changes. Hidden AI and cleanup events require keys only where the engine or audit surface needs them.

## Dedicated asset brief

The package requires six dedicated Fallout report images:

- national register under ash-darkened light
- damaged capital administration and shelter routing
- region-specific resource distribution under winter conditions
- government authority meeting in a damaged civic interior
- first character or institution presented in its actual setting
- orientation closure showing the successor's first coordinated public response

Each image needs a source or generation manifest, working PNG, final DDS, stable sprite name, dimensions, crop notes, provenance, and event binding. Real people and attested symbols require sourced assets. Fictional content uses the approved generated-art workflow. No zombie asset, audio, sprite, filename, or path may be reused.

The five roots may share their component image with the matching result only when the result shows the same place and subject. The closure uses the sixth dedicated image. No text-only disposition or placeholder is permitted.

## Validation scenarios

Implementation review must prove at least these deterministic cases without claiming runtime observation:

1. a high-resource human successor completes all five components with success outcomes
2. a low-resource human successor receives at least one failure without a retry reward
3. an AI successor pays the same costs and receives the same score outcome as the matching human case
4. a capital evacuation balances source loss, destination gain, and Deaths
5. a missing curated character registry blocks the fifth component and records the exact diagnostic
6. a save before a delayed result issues that result once
7. a save after issue cannot issue the result again
8. a stale transition generation cancels pending orientation without recording a current receipt
9. all nine regions select their declared environmental language and resource response
10. all twelve archetypes select distinct reviewed government content
11. a country-memory overlay changes content only when its exact receipt is current
12. orientation closure leaves both scheduler activation flags unset

The audit must also check for free-resource loops, branch cycling, repeated failure rewards, invalid state or character targets, missing AI weights, stale decisions, tiny modifiers, and political-power storage.

## Implementation order

The event ID ledger reserves suffixes `62` through `84`. Implementation proceeds in this order:

1. approve the nine-region and twelve-archetype coverage matrices
2. approve successor memory and character or institution registries for the pilot countries
3. add typed constants and the idempotent component transaction
4. define all 23 events with effects, AI, delayed results, memory, and cleanup
5. write final regional and government-aware localisation
6. produce and wire all six dedicated assets and manifests
7. wire log and event-detail surfaces
8. wire one future host-authority caller only after successor allocation and player continuation are proven
9. run event, localisation, asset, country-package, and completion audits
10. update the workbook from implementation facts and export its CSV views
11. count only the blocks that pass manual review

## Approval record

The user approved all of the following on 2026-07-18:

- suffixes `62` through `84` are reserved for this package
- the five components and their exact order are accepted
- the deterministic score bands and listed inputs are accepted
- the 2, 3, 4, 3, and 2 day delayed-result cadence is accepted
- the package remains dormant until a separate caller and activation review
- missing regional, archetype, memory, state, or character rows fail closed with no fallback
- all 23 blocks remain outside the 660 count until fully wired and manually reviewed
- six dedicated Fallout assets are required before completion

Approval authorizes scoped implementation. No caller may be wired until successor allocation, player continuation, the nine-region rows, twelve-archetype rows, country-memory rows, main-state targets, and curated character or institution registries are proven. The package must not activate the ordinary scheduler.
