# Event 027: Doctrine Research

## Part 3: Evolutions, AI, balance, and cluster behavior

## Evolution model

Event 027 has one linear evolution track. Each stage increases the number of separate choices in a country batch.

The evolution changes quantity and strategic flexibility. It does not increase the strength of one choice. Every choice still adopts one Grand Doctrine without mastery or advances one subdoctrine by one event mastery step.

The recommended eligibility follows the global chaos tiers:

| Event state | Recommended chaos eligibility | Choices per country batch |
| --- | --- | --- |
| Baseline | Calm World | 1 |
| Evolution I | Gathering Storm | 2 |
| Evolution II | Rising Chaos | 3 |
| Evolution III | Chaos Tier | 4 |
| Evolution IV | Totalen Chaos | 5 |

Evolution unlocks should use the normal evolution pacing model with a base around 90 days after the relevant campaign state becomes eligible. Dynamic factors may shorten or lengthen the delay. The event should not switch stages instantly on the same day the Chaos Meter crosses a threshold.

The final implementation must follow the current project rule for one evolution stage per chaos tier. Exact tier constants, MTTH factors, and enable-state handling belong in centralized tuning.

## Evolution entry paths

Event 027 can enter an evolved state before its first firing or after earlier firings.

### Pre-fire evolved opening

When an evolution has already unlocked before Event 027 fires for the first time, the first firing uses the highest currently active and enabled evolution stage.

The player does not receive a baseline batch first. The first global doctrine wave arrives with the evolved batch size.

### Post-fire evolution

When Event 027 has fired before, a later evolution changes future batches.

Countries do not receive a free batch at the moment the evolution unlocks. The mutation changes the size of the next normal Event 027 firing.

### Evolution during an active batch

A batch stores its stage and size when Event 027 fires. A later evolution does not enlarge that active batch or any batch already queued from an earlier firing.

The next random-event firing creates a new batch at the current stage.

### Disabled evolution handling

A disabled evolution must not block higher enabled stages.

When Evolution I is disabled and Evolution II is enabled, a country can move from baseline batches to three-choice batches once Evolution II unlocks. The disabled stage creates no evolution record and sets no prerequisite flag needed by higher stages.

Every stage's availability, record, and effect must check its own enabled state.

## Baseline

Every valid country receives one choice.

The baseline is strategically meaningful because one choice can:

- establish one Army, Navy, Air, eligible Special Forces, Chaos Warfare, or custom Grand Doctrine
- begin one empty subdoctrine track at Mastery I
- advance one active branch
- complete one branch and unlock or restore its native Grand Doctrine Milestone

The baseline has no secondary reward. Its replay value comes from country doctrine state at the time it fires.

## Evolution I

Every valid country receives two separate choices in one batch.

Evolution I creates the first complete adoption-to-mastery sequence. A country can establish a Grand Doctrine with its first choice and begin one track with its second.

A country with active doctrine may stack both choices in one branch or split them across two tracks or domains.

The evolution record should communicate a second round of staff review, repeated exercises, or a doctrine conference producing two adopted lessons. Final wording should remain grounded in military institutions and practical study.

The second choice uses the same selection flow as the first. It is not a hidden bonus attached to the first action.

## Evolution II

Every valid country receives three separate choices.

Three choices make service prioritization more visible. A country can establish a doctrine and begin two tracks, push one branch three levels, or spread development across several domains.

The evolution record should communicate several schools of military thought being accepted in one cycle. The tone remains positive and institutional.

## Evolution III

Every valid country receives four separate choices.

Four choices are enough to touch the four common track categories in a typical Army Grand Doctrine or the four tracks of Chaos Warfare. This stage supports deliberate broad-development play and the Joint Curriculum achievement.

The evolution record should communicate a complete inter-service or multi-track curriculum. It should avoid claiming that every doctrine is complete.

## Evolution IV

Every valid country receives five separate choices.

Five choices are the highest planned stage. A country can fully develop a fresh five-level branch when every choice is validly directed into that branch. It can also distribute the batch across a large doctrine portfolio.

This stage is intentionally powerful. It arrives at Totalen Chaos, applies symmetrically across the world, and remains constrained by Event 027's diminishing repeatable weight cap.

The evolution record should communicate a doctrine cycle whose findings are adopted at every level of military education and field command. It should remain a minor-event presentation and should not become a global crisis announcement.

## Why the evolution track stops at five

The rough design reaches five choices at Evolution IV. Most current branches use a compact sequence of mastery levels, and Chaos Warfare has five levels in each of its four tracks.

A fifth evolution that merely grants six choices would add another quantity tier without a distinct design purpose. Event 027 should stop broad expansion here. A future Evolution V would need a separate mutation concept, a clear balance case, and a new player decision. It should not be added as a routine extension.

## Evolution stage memory

The current Event 027 stage is global campaign memory.

It affects:

- batch size at the next firing
- Event Details evolution preview
- the evolution history record
- achievement eligibility that depends on batch size
- AI multi-choice allocation behavior

It does not affect:

- the strength of one mastery step
- doctrine eligibility
- branch prerequisites
- country participation rules
- repeatable-event weight recovery
- repeatable cap reduction
- direct Chaos Meter value

## AI design goals

AI countries need choices that are coherent with their military plans and strong enough to preserve global balance against a human player.

The AI should:

- use the same valid doctrine pool as a human
- prefer doctrine domains relevant to its current and intended forces
- use native or country-specific doctrine preferences where available
- recognize near-complete branches and valuable Grand Doctrine Milestones
- change its preference when wars, production, force composition, geography, and strategic plans change
- recalculate after each choice in a batch
- stack when one branch has a clear strategic advantage
- diversify when several branches offer similar value
- avoid irrelevant domains and invalid custom content
- preserve a bounded amount of variation so countries do not converge on one doctrine pattern in every campaign

The AI should not chase perfect global optimization. It should produce a plausible military curriculum for the country and its current campaign.

## AI domain scoring

A valid domain begins with a neutral domain score. The following factors raise or lower it.

### Army domain

Raise the score for:

- large fielded land forces
- active land wars or expected land wars
- long land borders with threatening countries
- national focus routes centered on land expansion or defense
- large Army equipment production
- existing Army Grand Doctrine progress
- near-complete Army tracks
- severe land-front losses that expose a doctrinal weakness

Lower the score for:

- a country with no meaningful land force or land theater
- an isolated maritime strategy with little land ambition
- every Army track already complete

Army should remain a common AI choice. It must not receive an unconditional preference that prevents maritime or air powers from using their evolved choices well.

### Navy domain

Raise the score for:

- owned coastline and usable naval bases
- island or archipelago geography
- active naval war
- significant dockyards, fleets, convoy exposure, or naval production
- focus routes that require naval control, overseas operations, convoy protection, or naval invasion
- an existing Navy Grand Doctrine with incomplete tracks
- a track close to completion

Lower the score for:

- landlocked geography without a route to acquire a coast
- no fleet, no dockyards, no naval production, and no naval strategic plan
- every Navy track already complete

A future naval plan can justify doctrine adoption before a fleet exists when the plan is explicit through AI strategy, focus route, or country identity.

### Air domain

Raise the score for:

- significant aircraft production
- active air wings and airbase capacity
- contested or important air regions
- strategic bombing, interception, close air support, carrier air, or airborne plans
- a focus route centered on air power
- an existing Air Grand Doctrine with incomplete tracks
- a near-complete air track

Lower the score for:

- no aircraft production, no air bases, no air plan, and no relevant strategic threat
- every Air track already complete

### Supported Special Forces domain

Raise the score for:

- fielded special-forces formations
- a military plan centered on marines, airborne forces, mountaineers, rangers, or another supported family
- relevant terrain and operational targets
- national focus or AI strategy support
- an existing incomplete doctrine

Lower the score for:

- unavailable DLC or incompatible graph
- no fielded or planned special-forces role
- every track complete

The domain remains absent when the local graph does not provide a verified mastery-compatible adapter.

### Chaos Warfare domain

Raise the score for:

- Chaos Warfare already active
- chemical or biological technology and equipment investment
- fielded CBRN headquarters and support formations
- an authorized use policy
- active contamination, unconventional-warfare threats, or planned exact-state operations
- a special Chaos country whose military identity uses this doctrine
- a Chaos Warfare track close to a meaningful operational threshold

Lower the score for:

- missing Grand Doctrine establishment prerequisites
- no CBRN equipment, formations, policy, or strategic plan
- ordinary countries whose current route rejects unconventional warfare
- every Chaos Warfare track complete

The event cannot use AI scoring to bypass Chaos Warfare eligibility.

### Future custom domains

Every custom adapter supplies its own domain factors and hard blockers. The factors must be based on visible force structure, country identity, route strategy, active threats, or owner-system state.

A generic custom-domain bonus based only on the adapter existing is insufficient.

## AI Grand Doctrine selection

When a selected domain lacks a Grand Doctrine, the AI scores every eligible Grand Doctrine in that domain.

The score should reuse the country's current doctrine strategy and native AI preferences where those are available and valid. Event 027 should not maintain a second disconnected Grand Doctrine strategy table when the game or mod already expresses the country's intended doctrine.

Additional Event 027 factors can consider:

- force composition
- production plans
- current enemies
- terrain and theater
- defensive or offensive posture
- manpower and industrial limits
- faction role
- focus route
- historical plan when the AI follows one
- high-chaos or special-country identity

The AI cannot replace an active Grand Doctrine through this event. Doctrine selection scoring applies only to an empty domain.

## AI track and subdoctrine scoring

For an active Grand Doctrine, the AI scores valid tracks and any eligible subdoctrines in empty tracks.

### Force composition fit

The branch gains value when its mastery-generating units and bonuses match formations the country fields or is actively building.

Examples include:

- infantry and irregular branches for infantry-heavy armies
- armor branches for tank production and armored formations
- artillery or combat-support branches for artillery-heavy templates
- operations branches for planning, logistics, command, or theater roles
- carrier, submarine, surface-fleet, escort, or naval-air branches for matching fleets
- fighter, bomber, support-air, or operational-air branches for matching aircraft and mission plans
- CBRN branches for matching equipment, formations, and operations

### Current-war fit

The branch gains value when it addresses a current campaign problem, such as:

- poor supply in a land war
- enemy armor pressure
- convoy losses
- enemy air superiority
- an amphibious campaign
- mountain or jungle operations
- contamination and protection needs

The factor should use measurable campaign state. It should not read flavor text as strategy.

### Completion value

A branch near its next level gains a modest preference because the event can convert the choice into an immediate reward.

A branch one event mastery step from completion gains a stronger preference when its Grand Doctrine Milestone or completed-track unlock fits the country.

Completion value must not overpower a severe strategic mismatch. A landlocked country should not prioritize an irrelevant naval track only because it is close to completion.

### Empty-track value

An empty track can receive a preference when selecting a subdoctrine would fill a missing capability.

The AI should compare the branch's intended unit family and bonuses with production, templates, focus plans, and theater needs.

### Existing investment

An active branch with several levels already earned gains continuity value. This helps the AI finish coherent doctrine plans and limits aimless distribution across unrelated branches.

Continuity remains a factor, not a hard lock.

### Native Milestone value

When a choice completes a track and unlocks or restores a Grand Doctrine Milestone, the AI should consider the Milestone's strategic fit.

The event must not use the presence of any Milestone as an automatic dominant score. Some Milestones are valuable only for a matching doctrine plan.

## Multi-choice allocation

The AI recalculates after every successful choice.

This allows these patterns:

- stack two or more choices in one high-value branch
- complete a branch, then move to another
- establish a Grand Doctrine, then begin its most valuable track
- establish several service doctrines in one evolved batch
- spread choices across several tracks when their scores are close

The allocation should use these principles:

- strong score lead favors stacking
- one step from a valuable completion strongly favors finishing
- several close scores increase diversification
- completing a branch removes it from later choice pools
- adopting a Grand Doctrine changes the next score pass immediately
- the fifth choice at Evolution IV receives a fresh score pass and does not copy the fourth

The implementation should use bounded randomness among the best valid candidates. A low-value branch must not win merely because it remains technically valid.

## AI diversity

Countries should retain recognizable doctrine tendencies without becoming deterministic.

A historical or route-specific preference can be strong. Campaign evidence can override it when the country's situation changes substantially.

Recommended diversity behavior:

- choose from the top two or three candidates when their scores are close
- choose the clear top candidate when its score exceeds the next candidate by a meaningful margin
- use a small continuity preference for the branch selected by the prior choice in the same batch
- reduce continuity after that branch completes or loses strategic relevance
- preserve country-specific and custom-system AI factors

Exact factors require the mandatory probability audit. The spec defines ordering and scenario expectations, not final numeric weights.

## Balance intent

### Global symmetry

Every valid country receives the same number of choices from one firing. This limits direct relative advantage.

Symmetry does not guarantee equal value. Countries have different doctrine states, branch rewards, DLC content, and strategic opportunities. Strong AI selection is therefore part of balance, not optional polish.

### Direct power

One baseline choice should feel valuable. It can complete a track or establish a doctrine, but it cannot create an entire military doctrine portfolio.

Evolution IV is a late-chaos capstone. Five direct mastery choices can complete a fresh five-level branch. This is intentional and should remain visible in the event's balance report.

### Repeatable diminishing returns

Event 027 uses the shared repeatable system:

- initial weight follows the repeatable-event default
- monthly recovery follows the configured recovery rate
- the maximum weight cap is reduced after each firing

The event needs no separate universal cooldown at specification stage. The shared cap reduction already makes repeated global doctrine waves progressively rarer.

A later probability audit may recommend an event-specific cooldown if sequence analysis proves that the event can dominate the positive-event pool. Such a cooldown would be a balance change requiring documented evidence.

### No direct Chaos change

Doctrine Research does not directly raise or lower the Chaos Meter. Its evolution eligibility reads global chaos, and its firing affects normal event pacing through the shared event system.

### No compensation

A country with no valid option receives no substitute resource. Compensation would reward countries that already completed the most doctrine content and would turn the event into a generic economic handout.

### No hidden scaling by country power

Majors and minors receive the same choice count. The native value of a mastery level may differ, but the event does not grant more choices to majors or fewer to minors.

This preserves the rough design and complements the native mastery system's effort to keep smaller countries relevant.

## Exploit controls

### Doctrine replacement exploit

The event never replaces an active Grand Doctrine or selected subdoctrine. Players cannot use it to reset a poor choice for free.

### Cost refund exploit

The event waives the cost of its own valid adoption. It never refunds experience spent before the event.

### Double-consumption exploit

A one-time transaction receipt prevents the same confirmation from applying twice after a double click, duplicate event page, save, reload, or delayed continuation.

### Banked mastery exploit

The event preserves banked mastery and attributes only one explicit event step per successful mastery choice. It cannot zero banked mastery and regrant it for achievement credit.

### Queue overwrite exploit

Every firing creates a distinct batch. A later firing cannot reset remaining choices or turn one unfinished baseline choice into five evolved choices.

### Cluster duplication exploit

One cluster firing calls the Event 027 global fanout once. Member subevents and country choice pages cannot call the fanout again.

### Tag-switch exploit

The batch remains owned by its country. A player cannot tag switch through several countries and redirect all batches into one doctrine state.

### Annexation transfer exploit

Unused choices disappear with the country. Annexation cannot farm doctrine choices for the annexer.

### Re-release exploit

Releasing a country after Event 027 fires does not grant a retroactive batch. Releasing and annexing the same tag repeatedly cannot multiply one firing.

### Achievement exploit

Achievements use the batch ledger and event-attributed receipts. Native mastery, faction sharing, debug grants, and progress from another event cannot be counted as Event 027 choices.

## National Breakthroughs cluster role

National Breakthroughs groups small positive developments that improve research, military knowledge, leadership, institutions, or accumulated experience without creating a crisis.

Event 027 is a Medium-severity member because its effect is global and can produce several direct mastery levels at higher evolutions.

The recommended event member behavior is:

| Attribute | Recommendation |
| --- | --- |
| Member role | Optional when another member is selected. The originally selected member remains guaranteed through the shared cluster system. |
| Minimum tier | Calm World. |
| Display severity | Medium. |
| Optional participation | Use the cluster's moderate participation band after the full member pool is reworked and audited. |
| Runtime setup | One Event 027 fanout using the current evolution stage. |
| Cluster bonus | None. |

The cluster should usually produce a small set of related breakthroughs, not every eligible member at once. Exact participation weights belong to a cluster-wide balance pass after Events 54, 65, 67, 83, 85, and 89 have accepted specs.

Event 027 does not change its batch size when it fires through the cluster. It uses the same baseline or evolution stage as a normal firing.

Cluster firing counts as one global pacing event. Event 027's country fanout, AI resolution, human pages, and batch summaries do not add timer pressure or major-event gain.

## Interaction with selected cluster member

When Event 027 is the random event selected before the cluster roll, it is the guaranteed Event 027 member and its global fanout occurs once.

When another National Breakthroughs member is selected and Event 027 joins as an optional member, Event 027 uses its normal global fanout once.

A country can receive effects from several cluster members. Event 027 does not combine its choice ledger with military experience, leader traits, infrastructure, agency content, or other member rewards.

## Cluster availability and stale members

National Breakthroughs can be registered only when its runtime member definitions are valid.

Unreworked or unavailable member events should remain in the catalog concept without being loaded as active runtime members. Event 027 can be implemented and tested independently before the full cluster becomes playable.

The cluster row should remain unavailable or partially available according to the current runtime registry. The accepted rough member list does not justify marking the cluster playable while most member events remain unreworked.

## Improvement-loop closure

The event's playable promise is fully served by the doctrine batch, its stacking and distribution choices, custom doctrine adapters, AI, evolutions, achievements, and cluster connection.

A separate pressure meter, doctrine currency, decision category, focus branch, country package, faction mechanic, animated interface, or larger crisis chain would duplicate existing doctrine systems or move the event away from a small positive breakthrough.

The improvement loop should close broad expansion after implementation proves the accepted batch flow. Later work should focus on graph coverage, AI evidence, clarity, assets, achievements, save behavior, and catalog alignment.
