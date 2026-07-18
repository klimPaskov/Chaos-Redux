# Fallout Ash-Week Orientation Contract Proposal

## Status

This proposal is unaccepted. It requires explicit user approval before implementation.

The proposed package defines dormant event content only. It does not set `fallout_event_scheduler_activation_approved`, `fallout_event_scheduler_active`, any manual-scenario activation flag, or any transition request flag. It does not change the current Fallout living-world count of 0 out of 660 manually reviewed blocks.

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
- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_effects/fallout_world_end_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_event_triggers.txt`
- Fallout event localisation and scripted localisation files
- `interface/fallout_world_end.gfx` for dedicated report sprites
- dedicated files under `gfx/event_pictures/fallout_world_end/`
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

## Proposed identifier allocation

The dedicated Fallout event file was scanned before this proposal. Suffixes `62` through `84` are free. Suffixes `100` through `126` remain reserved for the living-world pilot and are not reused.

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
| 74 | government-archetype root | human visible | 76 |
| 75 | government-archetype root | hidden AI | 77 |
| 76 | government-archetype result | human visible | 78 |
| 77 | government-archetype result | hidden AI | 79 |
| 78 | character or institution root | human visible | 80 |
| 79 | character or institution root | hidden AI | 81 |
| 80 | character or institution result | human visible | 82 |
| 81 | character or institution result | hidden AI | 83 |
| 82 | orientation closure | human visible | 84 |
| 83 | orientation closure | hidden AI | 84 |
| 84 | orientation cleanup | hidden | none |

These 23 identities are proposed reservations only. They become countable only after their callers, localisation, effects, AI, delayed results, memory, cleanup, assets, log entries, event details, and manual review are complete.

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

The proposed common score bands are:

| Score | Outcome |
| ---: | --- |
| 70 or more | success |
| 45 through 69 | partial success |
| below 45 | failure |

Each component receives a base score of 50. The approved implementation must put all additions and deductions in typed script constants. The shared allowed inputs are:

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

Exact ties use the lowest stable branch identity. AI evaluates the same score and effects as the human path. It chooses the highest projected score after survival-need weighting. Exact ties use the lowest stable branch identity. Hidden AI events may not receive reduced costs or guaranteed success.

## Component contract

### National orientation

The root describes the surviving territory, population loss, government reach, and the strongest and weakest numerical survival values. Text must use the country's region, archetype, and cause memory.

The three required branch families are:

- complete a household and workplace register
- recognize district and settlement compacts
- impose an emergency command register

Every branch spends a meaningful combination of Food, Clean water, Filters, Fuel, Scrap, or Shelter capacity. No branch spends political power. The delayed result must change Recognition and Cohesion by at least 4 points in opposite risk patterns. A failure must also create a concrete shortage, unrest, building-damage, or Deaths consequence. Success records the chosen national-authority memory. Partial success records both the authority memory and its contested form. Failure records the failed authority memory and closes the transaction without a retry reward.

### Capital or main-state condition

The target is the preserved capital when it is owned and valid. Otherwise it is the deterministic highest-priority owned state from the accepted main-state registry. This is an eligibility rule, not a fallback to an arbitrary state.

The three required branch families are:

- seal and heat the civic core
- disperse stores and offices across surviving districts
- evacuate the poisoned core into a prepared receiving state

The root must show the target state's grade, phase, exposure, shelter, surviving infrastructure, and population receipt. Regional variants must distinguish snow, frost, cold rain, ash, dead vegetation, frozen water, dim light, and thaw where they apply.

The evacuation branch is available only with an exact prepared receiving state and a balanced migration transaction. The result must reconcile population movement, building damage or repair, shelter pressure, supply access, and Deaths. A failed evacuation may not delete population from the source without the matching Deaths and destination receipts.

### Immediate resource crisis

The crisis identity is the lowest normalized current value among Food, Clean water, Medicine, and Filters. Exact ties use that fixed order. Fuel, Power, Scrap, Shelter capacity, and Recognition remain scoring and payment inputs.

The three required response families are:

- strict public rationing with a published ledger
- emergency requisition from protected stores
- a locally tailored production or distribution measure

The third response must be manually selected for each region and archetype pair. Examples include thaw-water capture, cistern control, insulated rail distribution, fishing access, seed protection, and filter workshops. These are design directions, not final localisation.

Success must improve the selected crisis value by at least 8 points and consume at least 4 points from one supporting resource. Partial success improves it by 4 to 7 points and creates a durable dispute or fatigue memory. Failure may not grant the selected resource. It must apply a concrete supply, disease, Deaths, recognition, or building consequence.

### Government archetype

The package must support exactly twelve manually reviewed archetypes. Each archetype receives one concrete root-text block, three tailored branch descriptions, branch-specific AI weights, and at least one distinct effect. Scripted localisation may select those blocks. A single generic paragraph with substituted archetype names does not satisfy the contract.

Each root must present:

- consolidation of the current emergency authority
- a negotiated division of authority with a region-appropriate institution
- an archetype-specific rival claim to legitimacy

The result may set government memory, unlock later focus or decision layers, alter Recognition and Cohesion, and add a substantial timed or persistent country modifier. It must not perform a broad ideology or tag rewrite. Any later government change needs its own accepted country-package contract.

### First character or institution

Every successor needs a curated candidate registry before this component can run. Real people, flags, and attested institutions require sourced manifests. Fictional successors use generated fictional characters and institutions through the approved asset workflow. Mutant content is treated as fictional high-chaos society content.

The root presents two or three valid candidates with distinct survival roles, costs, risks, and later memories. At least one branch must prioritize administration or relief. At least one must prioritize security or extraction. A third branch may represent a regional institution, technical body, faith network, labor organization, military remnant, or civic council when historically or fictionally appropriate.

Success installs the exact character or institution and records its relationship memory. Partial success installs a contested or limited form with a delayed liability. Failure consumes the committed cost and records injury, refusal, factional rupture, institutional collapse, or Deaths as appropriate. A failed branch cannot be selected repeatedly for free.

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

Working labels in this proposal are not final localisation.

Final text must name concrete conditions, districts, institutions, resources, weather, and authority disputes. It must react to region, archetype, country memory, state grade, resource crisis, and outcome. It must not use generic apocalypse wording, implementation language, staged contrast formulas, em dashes, or semicolons.

Visible roots and results require event titles, descriptions, option text, effect tooltips, log entries, event-detail entries, and evolution-detail text where durable identity changes. Hidden AI and cleanup events require keys only where the engine or audit surface needs them.

## Dedicated asset brief

The package requires five dedicated Fallout report images:

- national register under ash-darkened light
- damaged capital administration and shelter routing
- region-specific resource distribution under winter conditions
- government authority meeting in a damaged civic interior
- first character or institution presented in its actual setting

Each image needs a source or generation manifest, working PNG, final DDS, stable sprite name, dimensions, crop notes, provenance, and event binding. Real people and attested symbols require sourced assets. Fictional content uses the approved generated-art workflow. No zombie asset, audio, sprite, filename, or path may be reused.

The five roots may share their component image with the matching result only when the result shows the same place and subject. The closure requires either a sixth dedicated image or an explicitly approved text-only disposition. No placeholder is permitted.

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

## Implementation order after approval

1. reserve suffixes `62` through `84` in the event ID ledger
2. approve the nine-region and twelve-archetype coverage matrices
3. approve successor memory and character or institution registries for the pilot countries
4. add typed constants and the idempotent component transaction
5. define all 23 events with effects, AI, delayed results, memory, and cleanup
6. write final regional and government-aware localisation
7. produce and wire dedicated assets and manifests
8. wire log and event-detail surfaces
9. wire one future host-authority caller only after successor allocation and player continuation are accepted
10. run event, localisation, asset, country-package, and completion audits
11. update the workbook from implementation facts and export its CSV views
12. count only the blocks that pass manual review

## Approval checklist

Approval should confirm all of the following:

- suffixes `62` through `84` may be reserved for this package
- the five components and their exact order are accepted
- the deterministic score bands and listed inputs are accepted
- the 2, 3, 4, 3, and 2 day delayed-result cadence is accepted
- the package remains dormant until a separate caller and activation review
- missing regional, archetype, memory, state, or character rows fail closed with no fallback
- all 23 blocks remain outside the 660 count until fully wired and manually reviewed
- dedicated Fallout assets are required before completion

Until that approval is recorded, no gameplay file should implement this proposal.
