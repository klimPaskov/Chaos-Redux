# Fallout The Bad Batch event improvement addendum

Status: core implementation folded into the dormant Bad Batch tranche. The
regional and government-archetype expansion remains queued and grants no
activation or release-floor credit.

The core tranche has concrete player-facing localisation in the implementation
and proof record. The direction below remains the source for the queued
regional and government-archetype expansion.

## Improvement-loop decision

The chain should be expanded now. Seed Vault Custody proves who controls a
genetic reserve, but the current design has no event that tests whether those
seeds can safely become a living crop. The Bad Batch adds that missing
agricultural consequence without creating another ownership dispute.

No prior Bad Batch addendum exists under this plan folder. Seed Vault Custody
has an implemented dormant proof, so the improvement-loop cadence requirement
is satisfied. The fixed identity, receipt, branch, delayed-result, callback,
Deaths, Event Log, and cleanup surfaces in this addendum are implemented in the
dormant tranche. Regional and government-archetype variants remain queued.

## Feature promise

During the first post-Fallout year, workers open a multiplication lot or
greenhouse tray and find uneven germination, lesions, mold, and off-type growth.
They do not know whether the cause is a seed-borne pest, contaminated water,
damaged storage, cold stress, toxic residue, or a fictional altered-ecology
effect. The government must destroy the lot, plant it under risk, isolate it in
experimental plots, or share samples through its surviving exchange network.

The player should understand four facts before choosing:

- the lot comes from a proven pre-Fallout seed or greenhouse program
- every choice spends a different scarce survival resource
- the result is delayed and can succeed, partly succeed, or fail
- a failed containment or harvest can kill civilians through hunger, exposure,
  disease, or unsafe field work

The chain must never present mutation as an ordinary real-world consequence of
radiation. Strange traits can create later fictional altered-ecology
eligibility, but the first diagnosis remains uncertain.

## Fixed identity contract

| Surface | Fixed identity |
| --- | --- |
| Human discovery and choice | `chaosx.fallout.204` |
| Hidden AI discovery and choice | `chaosx.fallout.205` |
| Human destroy result | `chaosx.fallout.206` |
| Human plant result | `chaosx.fallout.207` |
| Human isolate result | `chaosx.fallout.208` |
| Human share result | `chaosx.fallout.209` |
| Hidden AI destroy result | `chaosx.fallout.210` |
| Hidden AI plant result | `chaosx.fallout.211` |
| Hidden AI isolate result | `chaosx.fallout.212` |
| Hidden AI share result | `chaosx.fallout.213` |
| Human callback | `chaosx.fallout.214` |
| Hidden AI callback | `chaosx.fallout.215` |
| Authenticated cleanup | `chaosx.fallout.216` |
| Candidate id | `204` |
| Transaction key | `710008` |
| Candidate route | `7108` |
| Event Log history id | `9113` |
| Phase | `constant:fallout_event_phase.first_winter_year` |
| Cooldown family | food security |
| Target type | state |
| Visible budget cost | `1` |

The chain remains dormant. It must not set either scheduler activation flag and
must not call itself outside the accepted scheduler transaction.

## Discovery and eligibility contract

### Deterministic state target

The candidate producer selects the lowest stable database id among valid owned
states. The target must have all of the following:

- a current Fallout state identity row
- a durable current-generation survival-resource row
- a produced Air Winter snapshot from the current transition generation
- frozen Air Winter Adaptation above `24`
- frozen Air Winter Reclamation above `20`
- no committed Bad Batch registry
- one positive seed or greenhouse provenance receipt from the same state

The candidate also requires country Food of at least `24` and at least one
payable branch. It must not require Medicine merely to discover the event.
Medicine is the cost and competency input for the destroy branch. The current
scaffold's unconditional Medicine gate would suppress valid plant, isolate, and
share stories and should be replaced by an affordability OR across the four
branches.

### Accepted seed provenance

The following state memories qualify because they prove an active or surviving
seed program:

- `air_winter_memory_seed_vaults`
- `air_winter_memory_seed_vaults_flourished`
- `fallout_event_188_memory_national_archive`
- `fallout_event_188_memory_farmers_covenant`
- `fallout_event_188_memory_alliance_compact`
- `fallout_event_188_memory_market_access`

`air_winter_memory_seed_vaults_failed` and the four Seed Vault Custody failure
memories do not qualify. Contested custody memories may alter writing later,
but they do not prove that a working multiplication lot survived.

### Required greenhouse provenance repair

The live Air Winter greenhouse project sets
`air_winter_greenhouse_refuge`, but Air Winter teardown clears that flag. The
Fallout snapshot does not currently copy it into a durable provenance field.
The Bad Batch therefore cannot satisfy its accepted greenhouse route without a
narrow snapshot repair.

During pretransition state capture, before pending Air Winter chains are
cancelled, copy a live greenhouse receipt into both of these state fields:

- `fallout_pretransition_air_winter_greenhouse_provenance_recorded`
- `fallout_pretransition_air_winter_greenhouse_generation`

The generation value must equal `global.fallout_snapshot_epoch_generation` at
capture and `global.fallout_transition_generation` when the candidate is
tested. Snapshot rebuild must clear both fields before recapture. A generic
Food, Shelter, Reclamation, urban, or building value must never stand in for a
missing greenhouse receipt.

This is a provenance handoff, not a permanent outcome memory. The Bad Batch
result writes its own durable state memories later.

### Branch affordability

The opening may be committed only when at least one branch can be paid. Every
visible option remains present, with an unavailable trigger and a clear
resource tooltip when its cost cannot be paid.

| Branch | Admission cost |
| --- | ---: |
| Destroy the lot | Medicine `5` and Scrap `4` |
| Plant the lot | Food `6` |
| Isolate experimental plots | Filters `5` |
| Share samples | Recognition `3` |

Payment occurs only after the delayed-result transaction is accepted. A
rejected or stale transaction pays nothing. Each cost has one idempotent paid
receipt.

## Frozen chain registry

The opening transaction must freeze the following before any branch cost is
paid:

- transition generation
- scheduler country registry index
- human-visible or hidden-AI control mode
- selected state id and state owner
- region id and government archetype id
- `global.fallout_pretransition_request_source`
- issue date and due day
- selected branch
- result event token
- frozen country Food, Medicine, Scrap, Filters, Shelter, and Recognition
- frozen state Exposure, Adaptation, Reclamation, Food reserve, Shelter
  capacity, and Water security
- qualifying seed or greenhouse provenance kind
- batch viability
- frozen success, partial, or failure result

Batch viability is calculated once at transaction commit and never rerolled:

```text
viability =
  Adaptation * 35 / 100
  + Reclamation * 30 / 100
  + Air Winter Food reserve * 20 / 100
  + Air Winter Shelter capacity * 15 / 100
  - Exposure * 20 / 100
```

Clamp the result to `0` through `100`. Every weight, divisor, and bound belongs
in the Bad Batch script-constant groups. Do not hardcode the coefficients in
effects. The formula represents the condition of the surviving growing system,
not a biological mutation probability.

## Four choice directions

### Destroy the lot

Gameplay identity: cautious containment with a certain short food loss.

- consume Medicine and Scrap for testing, sealed handling, and disposal
- reward strong medical capacity and high Air Winter Adaptation
- on success, preserve clean lines and improve containment practice
- on partial success, remove most material after some workers or beds were
  exposed
- on failure, discover the problem after contaminated material entered stores
  or fields
- write a durable state memory that distinguishes clean destruction, late
  destruction, and failed containment

The writing should make destruction costly. It must not read as a free safe
button.

### Plant the lot

Gameplay identity: the highest food upside and the clearest crop-failure risk.

- consume Food as seed and opportunity cost
- reward high Adaptation and a viable growing system
- on success, establish a locally adapted cultivar
- on partial success, produce a mixed harvest that needs selection and further
  testing
- on failure, lose a planting cycle and create a contaminated or blighted farm
  zone
- write a durable state memory for cultivar, mixed harvest, or ruined plots

This branch should be attractive to food-poor governments with technical
confidence, not automatically correct for every food-poor country.

### Isolate experimental plots

Gameplay identity: controlled research with infrastructure and filter demand.

- consume Filters and reserve protected Shelter capacity
- reward strong Filters, Shelter capacity, and technical Adaptation
- on success, establish a controlled line and a repeatable testing protocol
- on partial success, retain only a small usable sample
- on failure, breach containment and lose both material and protected space
- write a durable state memory for controlled plots, restricted samples, or a
  containment breach

This branch is the main research and altered-ecology observation route. It does
not confirm that the observed traits are supernatural.

### Share samples

Gameplay identity: distributed trials with the widest institutional upside and
the widest failure footprint.

- consume Recognition as courier access, certification trust, and political
  credit
- reward adequate Food, high Recognition, and a viable lot
- on success, create a distributed trial network and return useful reports
- on partial success, receive contradictory reports and retain a disputed line
- on failure, spread blight or unsafe seed and lose public trust
- write a durable state memory for shared trials, disputed circulation, or
  distributed contamination

This is a network exchange, not a bilateral diplomatic event. Do not invent a
foreign partner when the transaction has no authenticated secondary actor. A
future seed treaty or bilateral aid chain can consume the shared-trial memory.

## Deterministic outcome bands

The outcome is computed at the accepted opening transaction from frozen inputs.
The ten-day result reports that stored outcome. Later resource changes cannot
improve or worsen it.

| Branch | Success | Partial success | Failure |
| --- | --- | --- | --- |
| Destroy | Medicine at least `22` and Adaptation at least `30` | Medicine at least `12` and Adaptation at least `24` | Either partial threshold is missed |
| Plant | Food at least `30`, Adaptation at least `36`, viability at least `25` | Food at least `24`, Adaptation at least `24`, viability at least `16` | Any partial threshold is missed |
| Isolate | Filters at least `28`, Shelter capacity at least `35`, viability at least `25` | Filters at least `16`, Shelter capacity at least `20`, viability at least `16` | Any partial threshold is missed |
| Share | Food at least `26`, Recognition at least `30`, viability at least `25` | Food at least `24`, Recognition at least `18`, viability at least `16` | Any partial threshold is missed |

The current constants already carry most of these values. Add named partial
Shelter and branch viability thresholds rather than burying them in event
effects.

## Result timing and effects

- result delay: `10` days
- callback delay: `90` days after the result transaction
- destroy modifier duration: `180` days
- plant modifier duration: `300` days
- isolate modifier duration: `240` days
- share modifier duration: `210` days
- blight pressure duration: `270` days

The following numerical package matches the concurrent constant scaffold. The
parent should retain it unless scenario testing shows a concrete outlier.

| Branch and outcome | Food | Medicine | Filters | Adaptation | Reclamation | Recognition | Cohesion | Stability |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Destroy success | -2 | -2 | 0 | +4 | +3 | 0 | +2 | +0.02 |
| Destroy partial | -3 | -1 | 0 | +1 | +1 | 0 | -1 | -0.01 |
| Destroy failure | -4 | -3 | 0 | -3 | -4 | 0 | -5 | -0.06 |
| Plant success | +10 | 0 | 0 | +8 | +6 | 0 | +3 | +0.03 |
| Plant partial | +3 | 0 | 0 | +2 | +1 | 0 | 0 | -0.01 |
| Plant failure | -6 | 0 | 0 | -6 | -8 | 0 | -4 | -0.07 |
| Isolate success | -1 | 0 | -3 | +7 | +4 | 0 | +2 | +0.02 |
| Isolate partial | -2 | 0 | -2 | +3 | +1 | 0 | -1 | -0.01 |
| Isolate failure | -4 | 0 | -4 | -5 | -5 | 0 | -4 | -0.06 |
| Share success | +7 | 0 | 0 | 0 | +3 | +7 | +3 | +0.02 |
| Share partial | +2 | 0 | 0 | 0 | +1 | +2 | 0 | -0.01 |
| Share failure | -3 | 0 | 0 | 0 | -4 | -7 | -4 | -0.06 |

Clamp every survival resource and Air Winter-derived state ledger through its
existing owner helper. Cohesion changes must use the sole Cohesion helper.

### Temporary national modifiers

| Modifier | Gameplay role |
| --- | --- |
| `bad_batch_destroyed` | small stability, supply, and production benefit from disciplined containment |
| `bad_batch_planted` | larger production and food-logistics upside during the new crop cycle |
| `bad_batch_isolated` | research infrastructure and controlled-consumption burden |
| `bad_batch_shared` | network and market benefit with a distribution burden |
| `bad_batch_blight_pressure` | stability, supply, and consumer burden after any failed lane |

The dynamic modifiers must have localisation and must not replace the durable
state memories.

## Deaths-backed failure

Every first result in the failure band applies one exact target-state civilian
population loss through the shared Deaths pipeline:

- requested proportion: `0.0035` of the frozen current state population
- minimum population remaining in a nonempty state: `100`
- actor: the chain country
- target: the authenticated state
- reason: the existing Fallout aftermath population-loss reason
- population application: performed by the exact state helper before the Deaths
  registration, matching the established Seed Vault contract

The loss represents hunger, exposure during failed field work, contaminated
food handling, or disease following containment failure. It is not evidence
that radiation directly created monsters or instant lethal mutations.

Failure deaths apply once in events `206` through `213`. The callback must not
repeat them. An invalid owner, state, generation, or transaction cancels the
result without resource mutation, population mutation, or Deaths registration.
There is no fallback state.

## Ninety-day callback

Events `214` and `215` report the institutional consequence of the already
frozen outcome. They do not roll a second success check.

| Stored outcome | Callback direction | Food | Adaptation | Reclamation | Cohesion | Stability |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Success | clean reserve, local cultivar, controlled line, or distributed trial reports become usable | +6 | +4 | +4 | +3 | +0.02 |
| Partial | selection continues with a small usable line and contested reports | +2 | +1 | +1 | +1 | -0.01 |
| Failure | ruined plots, lost trust, and continuing blight consume another season | -2 | -3 | -3 | -3 | -0.05 |

The callback text must remember the selected branch. A destroy success should
not describe a cultivar, and a share failure should not describe a local-only
breach.

## Persistent memory contract

The result must leave enough durable memory for later food, treaty, public
health, and altered-ecology chains without keeping transaction debris.

On the target state, persist:

- one branch and outcome memory
- the frozen cause-memory identity
- the provenance kind, seed program or greenhouse program
- one institutional result, such as clean reserve, local cultivar, controlled
  plots, shared trial network, mixed harvest, or contaminated farm zone

Suggested compact storage is one state variable for branch, one for outcome,
one for cause memory, one for provenance, and a small set of descriptive state
flags consumed by later triggers. Do not create twelve unrelated numeric
booleans.

Mutation-fiction eligibility may be set only when all of these are true:

- branch is plant, isolate, or share
- result is success or partial success
- the accepted high-chaos or altered-ecology gate is met
- cause memory is Final Silence, biological follow-through, mixed terminal, or
  strategic singularity

The eligibility flag means a later explicitly fictional event may occur. It
does not state that this crop has mutated, that radiation caused it, or that a
new species exists.

## Cause-memory writing and AI direction

Freeze `global.fallout_pretransition_request_source` in the chain registry and
use it in the discovery, result, callback, Event Log detail, and AI score. Cause
memory changes suspicion and institutional preference. It does not rewrite the
observed symptoms into a proven diagnosis.

| Cause identity | Writing direction | AI emphasis |
| --- | --- | --- |
| Gradual air collapse | old filter failures, repeated ash exposure, delayed cleanup, and pre-collapse agricultural promises | modest support for isolate and share when Recognition is healthy |
| Final Silence | unexplained off-type growth, broken instruments, rumor, and competing scientific or religious interpretations | isolate gains weight, destroy gains weight for low-cohesion governments |
| Chemical saturation | storage-seal damage, poisoned water, residue, and protective handling | destroy and isolate gain weight |
| Biological follow-through | seed-borne pest fear, quarantine records, testing, and carrier accusation risk | isolate gains the largest weight, destroy gains a smaller weight |
| Mixed terminal | several plausible hazards and incompatible protective practices | isolate and cautious share gain weight |
| Manual thermonuclear | ash, damaged irrigation, firestorm residue, and missing laboratory capacity | destroy gains weight when Medicine is strong, plant loses weight at high Exposure |
| Legacy Fallout | incomplete cause records and inherited nuclear-fallout assumptions | use neutral safety weighting and never borrow another cause's final text |
| Strategic singularity | engineered terminal contamination, corrupted technical records, and surviving laboratory claims | isolate gains weight, technate and machine-protocol governments react strongly |

Every source value needs a dedicated localisation direction. `legacy_fallout`
is a compatibility identity, not permission to use a generic fallback line.

## Regional writing matrix

Regional text supplies place, material, and agricultural practice. Government
archetype supplies authority, conflict, and the reason a branch is preferred.
Country memory supplies named institutions when a reviewed memory exists.

| Region | Discovery objects and actors | Branch emphasis |
| --- | --- | --- |
| North America | prairie grain stores, greenhouse trays, Great Lakes or rail exchange, surviving extension workers | plant and share can invoke broad distribution, destroy can invoke recall across long transport routes |
| Europe | glasshouses, allotments, seed-testing stations, dense river and port exchange, border varieties | isolate competes with urgent urban planting, share raises border certification and local autonomy |
| Eurasian Interior | steppe experimental stations, mine-town greenhouses, rail depots, well routes, evacuated collections | isolate fits station science, share depends on long rail corridors, plant risks a full steppe season |
| East Asia | rice nurseries, floodgates, river paddies, fisheries, factory schools, dense shelter gardens | water control and nursery separation matter more than generic grain language |
| South Asia | canal nurseries, rice, wheat, or legume lots, monsoon-disrupted storage, refugee food demand | plant carries large hunger pressure, isolate consumes protected space and reliable water |
| Middle East and North Africa | irrigated basins, reservoirs, oasis wells, dryland grain, date or staple nurseries | water source and lot certification shape every branch, share follows corridor law |
| Sub-Saharan Africa | reviewed river-basin, highland, lake, pastoral, or mining-settlement crop systems | choose a locally researched crop and institution, never use one generic continental farming voice |
| Latin America and Caribbean | Andean seed stores, southern grain ports, tropical highland plots, river routes, island quarantine | isolate and share differ sharply between continental basins and island ports |
| Oceania and remote islands | port quarantine, limited land, wheat belts, fisheries, radio-linked islands, convoy seed stores | destroy and isolate receive strong biosecurity framing, share risks every connected island |

Final localisation must research the actual country-memory row before naming a
crop, institution, river, ethnicity, religion, or legal tradition. When exact
local facts are unavailable, use the reviewed regional material system rather
than inventing a local custom.

## Government-archetype writing and AI matrix

| Archetype | Governing conflict | Choice tendency when affordable |
| --- | --- | --- |
| Continuity government | statutory recall, regional authority, public trust, and emergency necessity | destroy or share, depending Recognition |
| Bunker authority | life-support allocation, technician control, and surface labor | isolate, then destroy |
| Warlord command | granary control, coercion, loyalty, and visible short-term yield | plant, with destroy favored when the command fears loss of stores |
| Food compact | grower councils, seed custody, ration legitimacy, and land title | plant or share |
| Maritime remnant | port quarantine, convoy certification, rescue obligations, and scarce land | share only with high Recognition, otherwise isolate |
| Quarantine state | cordon law, false positives, medical power, and inspection | isolate or destroy |
| Scavenger syndicate | counterfeit tags, salvage rights, broker profit, and contamination liability | share for profit when Recognition is high, otherwise plant |
| Nomad convoy | portable seed caches, route knowledge, wells, and seasonal movement | plant or share, with low Shelter reducing isolate interest |
| Machine protocol | classification confidence, data gaps, maintenance, and exception handling | isolate unless protocol confidence is very low |
| Technate | sampling protocol, technical franchise, intellectual property, worker safety, and accountability | isolate, then share |
| Mutant polity | consent, medical authority, stigma, citizenship, and the difference between identity and diagnosis | isolate or plant, never write biological essentialism as fact |
| Religious refuge | stewardship, charity, ritual interpretation, clerical authority, and lay hunger | destroy or share according to relief ethics, never use a cheap miracle |

The regional and archetype layers must combine. A maritime quarantine state in
Oceania should not sound like a technate in Eurasian Interior even when both
choose isolation.

## Deterministic hidden AI

Event `205` uses the same option admission, costs, outcome formula, effects,
history, callback, and cleanup as event `204`. It scores only payable branches.
No `random_list` or default unpaid branch is allowed.

Start every payable branch at `10`, then apply named constant adjustments:

| Condition | Destroy | Plant | Isolate | Share |
| --- | ---: | ---: | ---: | ---: |
| Branch meets its success thresholds | +8 | +8 | +8 | +8 |
| Branch meets only its partial thresholds | +3 | +3 | +3 | +3 |
| Continuity government | +5 | 0 | 0 | +5 |
| Bunker authority | +5 | -3 | +6 | -3 |
| Warlord command | 0 | +6 | -3 | -2 |
| Food compact | -2 | +7 | +2 | +7 |
| Maritime remnant | +2 | 0 | +4 | +6 |
| Quarantine state | +7 | -6 | +8 | -4 |
| Scavenger syndicate | -2 | +3 | 0 | +5 |
| Nomad convoy | 0 | +6 | -5 | +4 |
| Machine protocol | +2 | -2 | +8 | 0 |
| Technate | 0 | -2 | +9 | +4 |
| Mutant polity | -4 | +4 | +5 | +2 |
| Religious refuge | +2 | +1 | 0 | +5 |
| Chemical or biological cause | +5 | -5 | +7 | -3 |
| Final Silence or strategic singularity | +1 | 0 | +6 | 0 |
| Active war | +3 | +2 | -3 | -6 |
| Food below `28` | -3 | +5 | -3 | -2 |
| Recognition at least `30` | 0 | 0 | 0 | +5 |

Select the highest score. Exact ties use the lowest stable branch identity,
which is destroy, then plant, then isolate, then share. Freeze the chosen branch
and result before paying. If every branch becomes invalid, reject the candidate
and release its scheduler reservation. Do not silently choose share, plant, or
any other fallback.

## Event Log contract

History `9113` owns fifteen payloads:

| Stage | Payloads |
| --- | --- |
| Destroy result | `11` success, `12` partial, `13` failure |
| Plant result | `21` success, `22` partial, `23` failure |
| Isolate result | `31` success, `32` partial, `33` failure |
| Share result | `41` success, `42` partial, `43` failure |
| Callback | `51` success, `52` partial, `53` failure |

Each result writes once for the current transition generation and includes the
country as actor. The detail selector must also read frozen branch, cause,
region, and state memory so a callback detail remains specific. Do not claim a
secondary actor for the share branch.

## Authentication and cleanup

Mirror the proven Seed Vault transaction order:

1. authenticate the ordinary opening receipt
2. freeze state, generation, control mode, branch, inputs, and outcome
3. commit the result transaction
4. pay the branch cost once
5. issue the human or AI result once after ten days
6. authenticate the result before any mutation
7. write result effects, memory, and Event Log row once
8. commit and issue the human or AI callback transaction
9. authenticate the callback after ninety days
10. write callback effects and Event Log row once
11. release callback receipt first
12. release result receipt second
13. run event `216` to clear the Bad Batch registry and scheduler reservation

Cleanup removes temporary country flags, temporary variables, transaction
keys, scheduled tokens, paid receipts, history receipts, state registry flag,
and state registry variables. It preserves durable branch, outcome, cause,
provenance, and institutional memories.

Save recovery may issue a committed but unissued result, callback, or cleanup
once. It must not recompute viability, branch, outcome, target, cost, or control
mode. A country changing between human and AI control after commit stays on the
frozen event route.

## Visual direction and presentation

The chain merits one dedicated static Fallout report image because a sealed
seed vault does not visually communicate diseased greenhouse seedlings.

- proposed sprite: `GFX_fallout_bad_batch_report`
- source mode: generated fictional documentary scene through the approved
  event-art route
- temporary workspace: `docs/assets/204_the_bad_batch/`
- final DDS path:
  `gfx/event_pictures/204_the_bad_batch/report_event_bad_batch.dds`
- final dimensions: 210 by 176 pixels
- subject: gloved agronomists around divided seedling trays, with healthy and
  damaged growth visible but no monsters
- visual language: documentary postwar agriculture, cold light, ash residue,
  improvised labels, controlled tension
- exclusions: zombies, glowing fantasy crops, body horror, modern laboratory
  branding, readable generated text, and copied Seed Vault art
- animation: not required

The source scene should be produced as period-authentic documentary material,
then processed into black and white with sepia, grain, tilted report-card edge,
transparent corners, and a soft shadow through the repository report-event
processor. The active workspace must retain the prompt, generated source PNG,
processed PNG, manifest, requirement-to-runtime crosswalk, and
`gfx_handoff.md`. The main agent owns the sprite registration in
`interface/fallout_world_end.gfx`. Asset production belongs in a later
event-asset handoff. This addendum creates no image, DDS, sprite registration,
or manifest.

## Research basis

The historical basis supports a testing and quarantine story rather than a
generic mutation story:

- FAO genebank standards organize acquisition, drying, storage, viability
  monitoring, regeneration, distribution, and safety duplication. This supports
  the chain's distinction between preserving seed and proving a living lot.
  Source: https://www.fao.org/agriculture/crops/thematic-sitemap/theme/seeds-pgr/gbs/en/
- FAO standards also treat seed health, regulated pests, quarantine, and safe
  distribution as genebank responsibilities. This supports destroy, isolate,
  and share as materially different policies.
  Source: https://www.fao.org/4/i3704e/i3704e.pdf
- The International Plant Protection Convention identifies pest risk in the
  international movement of seeds and uses inspection, sampling, testing, and
  certification as safeguards. This grounds the shared-sample failure lane.
  Source: https://www.ippc.int/static/media/files/publication/en/2017/05/ISPM_38_2017_En_2017-05-15.pdf
- The International Seed Testing Association formed in 1924 and issued early
  international seed-testing rules and certificates before the Second World
  War. Formal seed testing therefore fits the mod's institutional vocabulary.
  Source: https://www.seedtest.org/en/informations-footer/about-us/history-of-ista.html
- The Vavilov Institute records that parts of its collection were evacuated and
  other holdings were preserved through the siege of Leningrad while staff and
  experimental stations continued their work. This provides inspiration for
  the political gravity of destroying, guarding, or distributing scarce seed.
  Source: https://www.vir.nw.ru/blog/2023/01/18/proryv-blokady-leningrada-80-let-nazad-my-pomnim/

These sources provide institutional inspiration. They do not justify exact
country-specific crop or cultural claims without a separate local research
check.

## Implementation surfaces for the parent

If accepted, the implementation should touch or create only the appropriate
parts of these surfaces:

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_triggers/fallout_world_end_bad_batch_event_triggers.txt`
- `common/scripted_effects/fallout_world_end_bad_batch_event_effects.txt`
- `common/dynamic_modifiers/fallout_world_end_bad_batch_dynamic_modifiers.txt`
- `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`
- `common/scripted_effects/fallout_world_end_effects.txt` for the narrow
  greenhouse provenance capture and reset
- `events/fallout_world_end_events.txt`
- a dedicated Bad Batch Event Log detail selector under
  `common/scripted_localisation/`
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
- the existing event-detail history routing effect
- English localisation for events, options, tooltips, modifiers, Event Log, and
  event details
- `interface/fallout_world_end.gfx` and the dedicated asset package after asset
  production
- the event id ledger, scheduler proof, implementation status, source-of-truth
  map, and a new Bad Batch implementation proof after the code exists
- the event catalogue workbook only after implementation facts and final
  in-game wording exist

The current untracked trigger and modifier files already occupy two of these
paths. Preserve other agents' work and reconcile it rather than replacing it
wholesale.

## Acceptance scenarios

1. A produced current-generation state with a positive seed memory can become
   the deterministic target.
2. A produced current-generation state with greenhouse provenance and no seed
   memory can become the deterministic target.
3. High Food or Reclamation without seed or greenhouse provenance cannot
   qualify.
4. A failed seed memory alone cannot qualify.
5. A greenhouse live flag that was not copied into the current snapshot cannot
   qualify.
6. The lowest valid owned state id is selected when several states qualify.
7. Every human branch can produce success, partial success, and failure under
   the frozen threshold table.
8. Hidden AI uses identical gates, costs, results, Deaths, history, callback,
   and cleanup.
9. AI branch selection is deterministic across repeated identical scenarios.
10. A control-mode change after commit does not change the scheduled route.
11. Resource changes after commit do not change the frozen outcome.
12. A stale generation, changed owner, missing state, or invalid registry
    cancels without effects or fallback targeting.
13. Every failure lane changes the exact target-state civilian population once
    and registers the observed loss through Deaths once.
14. Callback failure does not apply a second population loss.
15. Result history writes one of payloads `11` through `43` and callback writes
    one of `51` through `53` exactly once.
16. Cleanup removes all transient receipts while durable state memories remain.
17. All eight request-source identities have a dedicated text direction.
18. Regional and archetype overlays combine without unsupported local claims.
19. Altered-ecology eligibility never appears as a real-world radiation claim.
20. No zombie path, asset, audio, sprite, event, or localisation key is used.
21. The candidate remains dormant and contributes zero release-floor credit.

## Scope limits

Do not add a decision category, scripted GUI, focus route, country package,
formable, achievement, super-event, or bilateral diplomacy system for this
chain. Those surfaces would add bloat before the ordinary event proves its own
agricultural loop. Do not create a technology or doctrine unlock. The installed
package has no Technology Tree Viewer, but this is not an evidence gap because
the accepted design touches no technology tree.

## Promotion and closure handoff

This addendum should remain in `docs/plans/air_cleanliness_fallout_plans/` until
the parent accepts, queues with a reason, or rejects it. If accepted, promote
the design facts into these source-of-truth specs before claiming the design is
resolved:

- add the share branch and exact continuation to
  `matrices/fallout_global_event_family_matrix.md`
- add the chain contract to
  `specs/04_global_survival_and_society_event_bible.md`
- add the regional and archetype overlay rules to the appropriate sections of
  `specs/05_regional_event_bible.md` and
  `specs/06_government_archetype_event_bible.md`
- add the explicit fictional eligibility boundary to
  `specs/10_cause_memory_mutant_fiction_and_altered_ecology.md`

After implementation, replace proposal status with a proof that lists the
actual files, identifiers, asset manifest, Event Log mapping, event-detail
routing, meaningful scenario results, and every remaining blocker. The chain
cannot be called complete while the asset, localisation, AI parity, history,
event details, dormant candidate proof, or cleanup proof is missing.
