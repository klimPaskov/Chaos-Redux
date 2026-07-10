# Achievement Implementation and Asset Prompt for Event 018 Resources Found

Implement a difficult, route-diverse achievement set for Event 018. All titles below are working labels, not final localisation. Final titles and descriptions must be written from the direction in this prompt and must not expose hidden variables outside the achievement UI.

Use the existing single Chaos Redux achievement registry, localisation pattern, GFX pattern, and root-only `gfx/achievements/` file convention. Every achievement needs tracking, disqualifiers, final localisation, a completed icon, a grey icon, a not-eligible icon, documentation, and validation.

Do not unlock an achievement merely because Event 018 fired.

## General implementation rules

- Use stable IDs beginning with `018_resources_found_` or the established event-achievement naming pattern.
- Add achievements to the existing root registry rather than creating a new registry with a new unique ID.
- Keep Event 018 achievements together in one documented section.
- Use explicit tracking flags or variables when final-state checks cannot prove the route.
- Prevent tag switching, console-like force paths, or scenario bypasses from granting achievements when the existing achievement framework tracks those disqualifiers.
- Record whether the player started as an ordinary country, the field owner, the former owner, or the cave country.
- Track permanent closure, concealment, field deaths, maximum extraction, border-war history, cave starting army, anchor capacity, world-end state, and global defeat where required.
- Use integer-safe comparisons and centralized thresholds.
- Never advertise achievement progress in normal event options, focus descriptions, or Event Details.

## Achievement 1: One Vein to Rule the Market, working label

Proposed ID:

```text
018_resources_found_one_vein_market
```

### Story requirement

Create an extraordinary single-resource concentration in one active Event 018 field through repeated discoveries.

### Eligibility

- player owns the field state
- field originated from Event 018
- Evolution IV has not taken the state

### Unlock direction

- one Event 018 resource type in the selected state reaches at least a difficult threshold, recommended 400 or more
- the amount comes from Event 018 additions, not preexisting state resources
- the field remains active or mature when checked

### Disqualifiers

- field amount produced through a manual debug or scenario bypass when those are tracked
- field has been permanently closed
- player no longer owns the state

### Difficulty

Hard. Requires several repeat discoveries or evolved enrichment in one state.

### Icon direction

One immense ore seam, oil column, or resource stream dominating rail and factory machinery. No text or currency symbols.

## Achievement 2: The Whole Periodic Table, Figuratively, working label

Proposed ID:

```text
018_resources_found_all_resources_one_state
```

### Story requirement

Own one Event 018 field containing every six standard strategic resources at the same time.

### Unlock conditions

- Event 018 oil addition above zero
- Event 018 aluminium addition above zero
- Event 018 rubber addition above zero
- Event 018 tungsten addition above zero
- Event 018 steel addition above zero
- Event 018 chromium addition above zero
- player owns and controls the state
- cave country has not emerged from that field

### Difficulty

Very hard in normal repeat play, more accessible through Evolution III.

### Icon direction

Six distinct strategic-resource motifs converging on one mine or drill complex. No readable labels.

## Achievement 3: Every Worker Came Home, working label

Proposed ID:

```text
018_resources_found_every_worker_home
```

### Story requirement

Develop a meaningful field safely, then close it permanently without Event 018 causing a single death.

### Unlock conditions

- field reached at least Operating or a meaningful Developed Yield threshold
- field completed at least one major development project
- field was permanently closed by the player
- Event 018 death count for the field is zero
- no casualty concealment action was used
- no coercive labor route was used
- closure removed all Event 018 resources correctly

### Disqualifiers

- any Event 018 worker, military, or civilian death at the field
- concealment flag
- state lost before closure

### Difficulty

Hard. Requires deliberate safety and restraint.

### Icon direction

A safely sealed shaft with an orderly row of returned helmets and lamps, no memorial imagery that implies deaths.

## Achievement 4: Seal It While We Still Can, working label

Proposed ID:

```text
018_resources_found_full_seal_evolution_three
```

### Story requirement

Complete the full Evolution III sealing project after the creatures have become public and prevent Evolution IV.

### Unlock conditions

- Evolution III active for the player’s field
- at least one public settlement or transport attack occurred
- full sealing project completed
- all Event 018 resource additions removed
- Evolution IV prevention flag set
- cave country never emerged from that field

### Disqualifiers

- only partial closure completed
- cave country emerged first
- field lost and another country completed closure

### Difficulty

Very hard. Requires evacuation, hard-attack capable containment, engineering, and sacrificing the full deposit.

### Icon direction

A massive reinforced shaft seal under visible pressure, guarded by engineers and heavy braces.

## Achievement 5: Contract of the Century, working label

Proposed ID:

```text
018_resources_found_contract_of_century
```

### Story requirement

Turn a major field into a stable international economic success without allowing the diplomacy to become a crisis.

### Unlock conditions

- field reaches Industrial Developed Yield
- at least one long-term export contract completes a full review cycle without breach
- Workforce Safety remains Managed or Protected
- Foreign Pressure remains below Crisis during the qualifying period
- field owner remains sovereign
- no border war over the field
- field has no active public breach

### Optional stronger condition

Use balanced access with at least two buyers and no single foreign partner above the dependence threshold.

### Difficulty

Medium to hard. Rewards safe ordinary event mastery.

### Icon direction

A period contract seal, rail line, and resource field in one compact composition. No readable signatures or text.

## Achievement 6: No Claims Left Unsettled, working label

Proposed ID:

```text
018_resources_found_resolve_field_dispute
```

### Story requirement

Resolve a severe border-resource dispute through commission, demilitarization, compensation, or arbitration without losing the field to war.

### Unlock conditions

- a valid border crisis reached at least armed patrol or timed frontier mission stage
- Foreign Pressure reached Crisis band
- player retained ownership of the field state
- no border war transferred the state
- functioning settlement lasted for a defined period
- claimant’s active field claim or dispute was resolved or suspended by agreement

### Disqualifiers

- player wins a border war and then signs a settlement
- claimant is annexed merely to remove the dispute
- commission immediately collapses before the stability period

### Difficulty

Hard diplomatic route.

### Icon direction

Two border markers joined by a neutral resource seal and lowered weapons.

## Achievement 7: Thirty From Below, working label

Proposed ID:

```text
018_resources_found_thirty_from_below
```

### Story requirement

As the country that owned the field at breach, survive a cave-country emergence with the maximum 30 starting divisions and ultimately destroy the regional cave country before world end.

### Unlock conditions

- player owned or controlled the field at Evolution IV emergence
- recorded cave starting army equals 30
- player country survives the emergence
- cave country is fully defeated before the Event 018 world-end scenario
- no other country owns the player’s original capital at unlock, or use another strong survival condition suited to the campaign

### Disqualifiers

- player switches to the cave country after emergence
- cave world end triggers
- cave country is removed through a debug or forced cleanup path

### Difficulty

Extreme. It rewards deliberate greed followed by successful survival.

### Icon direction

A huge organized formation of cave silhouettes leaving one breach, opposed by a small hard-attack defense. Do not place a readable number 30.

## Achievement 8: The Last Shaft Closed, working label

Proposed ID:

```text
018_resources_found_last_shaft_closed
```

### Story requirement

Lead or materially contribute to the defeat of the regional cave country and clean every active resource anchor.

### Unlock conditions

- cave country existed
- cave country held at least several non-origin anchors
- cave country fully defeated before world end
- every mature anchor state completed cleanup
- player contributed a defined share of occupied cave states, casualties inflicted, or cleanup projects
- cave threat source cleared

### Difficulty

Hard military and reconstruction route.

### Icon direction

The final cave entrance sealed after battle, with damaged anti-armor weapons and engineering equipment.

## Achievement 9: Ten From One State, working label

Proposed ID:

```text
018_resources_found_ten_from_one_state
```

### Story requirement

As the cave country, activate the full 10-division capacity from one captured non-origin state.

### Unlock conditions

- player controls the Event 018 cave country
- one non-origin state has at least 100 total strategic resources
- that state completes continuous-control activation
- recorded contribution from that state equals 10
- at least one division from its capacity enters the active queue or army

### Disqualifiers

- origin state used
- state capacity exceeds 10 due to a bug or bypass
- player receives the condition only through world-end scripted freebies that ignore normal anchor rules

### Difficulty

Medium to hard cave-country objective.

### Icon direction

One richly veined resource anchor feeding a ring of brood marks. No readable number.

## Achievement 10: No Men, No Guns, working label

Proposed ID:

```text
018_resources_found_no_men_no_guns
```

### Story requirement

As the cave country, build a large functioning army entirely through the resource-capacity system.

### Unlock conditions

- player controls cave country
- at least 25 active cave divisions
- at least four mature non-origin resource anchors
- no normal division training completed
- no normal manpower or equipment requirement paid for core broods
- no world-end foothold bypass used for the qualifying divisions

### Difficulty

Hard system-mastery achievement.

### Icon direction

Empty human rifle racks and barracks beside active mineral veins forming organized broods.

## Achievement 11: The Moving Mountain, working label

Proposed ID:

```text
018_resources_found_moving_mountain
```

### Story requirement

Complete the Stone Phalanx doctrine and defeat a major prepared hard-attack opponent without losing the origin state.

### Unlock conditions

- player is cave country
- Stone Phalanx capstone completed
- opponent qualifies as a major or has a defined high hard-attack army threshold
- opponent capitulates or loses the relevant continental war objective
- origin state remained controlled throughout the qualifying war

### Disqualifiers

- doctrine route switched or bypassed
- victory occurs only after world-end transformation overwhelms the opponent

### Difficulty

Very hard route-specific cave achievement.

### Icon direction

A colossal layered carapace formation advancing under anti-tank fire.

## Achievement 12: The Front Has a Floor, working label

Proposed ID:

```text
018_resources_found_front_has_a_floor
```

### Story requirement

Use the Burrow War route to take a fortified capital or key supply hub through a prepared underground approach.

### Unlock conditions

- player is cave country
- Burrow War capstone or required focus completed
- prepared burrow approach decision used
- target is a capital, supply hub state, or heavily fortified state
- state captured during the action window

### Disqualifiers

- target was undefended or already controlled when the decision began
- unrestricted world-end foothold effect supplied the capture

### Difficulty

Hard route-specific operational achievement.

### Icon direction

A fortified surface line with a dark armored force breaking through beneath it.

## Achievement 13: The Hills Begin to Move, working label

Proposed ID:

```text
018_resources_found_hills_begin_to_move
```

### Story requirement

Use the Scree Tide route to break several enemies in rapid succession through lighter broods.

### Unlock conditions

- player is cave country
- Scree Tide capstone completed
- at least a defined number of raiding brood formations active
- capture several states or capitulate two countries within a difficult short window after a breakthrough
- capacity remains valid rather than relying on excess-division bug behavior

### Difficulty

Very hard route-specific tempo achievement.

### Icon direction

A broad slope or ridgeline resolving into many moving armored silhouettes.

## Achievement 14: Continental Appetite, working label

Proposed ID:

```text
018_resources_found_continental_appetite
```

### Story requirement

As the cave country, consume the eligible origin continent and trigger the Event 018 world-end scenario.

### Unlock conditions

- player controls cave country
- every eligible origin-continent state owned and controlled
- verification period completed
- chaos above 1000
- Event 018 world-end flag set
- cross-continent footholds created
- super-event triggered through normal route

### Disqualifiers

- world end forced by debug or manual bypass
- continent state group incomplete due to excluded valid states
- another world-end scenario fired first

### Difficulty

Extreme terminal-route achievement.

### Icon direction

A continent silhouette crossed by a connected underground vein network and several breach points. The continent must remain generic rather than Europe-specific.

## Achievement 15: The Ground Is Quiet Again, working label

Proposed ID:

```text
018_resources_found_ground_quiet_again
```

### Story requirement

After the Event 018 cave world-end scenario begins, eliminate every cave foothold, clear every active anchor, and complete the global defeat aftermath.

### Unlock conditions

- Event 018 world end previously triggered
- player remained an ordinary country
- no cave-owned state remains anywhere
- no active cave anchor remains
- cave threat source cleared
- global defeat aftermath event or super-event completed
- player made a major contribution under the shared contribution measure

### Difficulty

Maximum. Intended as one of the hardest achievements in the event set.

### Icon direction

A silent sealed chasm under a repaired industrial skyline, with a subdued global or multi-continent motif.

## Icon production rules

For every final achievement ID create:

```text
gfx/achievements/<achievement_id>.dds
gfx/achievements/<achievement_id>_grey.dds
gfx/achievements/<achievement_id>_not_eligible.dds
```

Workflow:

1. Generate the completed 64 by 64 icon through the approved icon workflow.
2. Create the grey variant in black and white.
3. Create the not-eligible variant by applying the required achievement overlay to the grey icon.
4. Do not red-tint or invent another locked treatment.
5. Keep final files in the achievement root.
6. Match exact registry IDs and GFX sprite names.
7. Record source PNG, processed PNG, DDS paths, prompt, status, and related achievement in the Event 018 asset manifest.

## Tracking and validation table

Implementation should fill this after coding.

| Achievement ID | Start eligibility tracked | Route history tracked | Disqualifiers tracked | Final-state check | Icon triplet wired | Validation scenario |
| --- | --- | --- | --- | --- | --- | --- |
| 018_resources_found_one_vein_market |  |  |  |  |  |  |
| 018_resources_found_all_resources_one_state |  |  |  |  |  |  |
| 018_resources_found_every_worker_home |  |  |  |  |  |  |
| 018_resources_found_full_seal_evolution_three |  |  |  |  |  |  |
| 018_resources_found_contract_of_century |  |  |  |  |  |  |
| 018_resources_found_resolve_field_dispute |  |  |  |  |  |  |
| 018_resources_found_thirty_from_below |  |  |  |  |  |  |
| 018_resources_found_last_shaft_closed |  |  |  |  |  |  |
| 018_resources_found_ten_from_one_state |  |  |  |  |  |  |
| 018_resources_found_no_men_no_guns |  |  |  |  |  |  |
| 018_resources_found_moving_mountain |  |  |  |  |  |  |
| 018_resources_found_front_has_a_floor |  |  |  |  |  |  |
| 018_resources_found_hills_begin_to_move |  |  |  |  |  |  |
| 018_resources_found_continental_appetite |  |  |  |  |  |  |
| 018_resources_found_ground_quiet_again |  |  |  |  |  |  |

## Completion standard

The achievement set is complete only when every implemented achievement has a difficult nontrivial route, reliable tracking, disqualifiers, final localisation, icon triplet, registry and GFX wiring, documentation, and a recorded validation scenario. Any removed or merged concept must be reported with a reason. No automatic firing achievement, missing icon, vague contribution check, or untracked route history counts as complete.
