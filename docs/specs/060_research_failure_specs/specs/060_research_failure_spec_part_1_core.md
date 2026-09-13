# Research Failure

## Catalog entry

- Event ID: `60`
- Event name: Research Failure
- Type: Minor Repeatable
- Status before implementation: To Be Reworked
- Chaos level: 1
- Cluster: Scientific Research
- Cluster role: High member

## Event promise

A country does not remain technologically advanced because a list of discoveries once existed.
Its equipment, factories, laboratories, armed forces, and public institutions rely on people who understand the work, records that can be found and trusted, instruments that can be calibrated, suppliers that can reproduce tolerances, and organizations that can teach the next generation.
Research Failure breaks enough of that structure at once that the country is pushed backward.

The affected country immediately loses current research work, suffers a severe research-speed penalty, and regresses a broad safe selection of normal researched technologies.
Its research-slot capacity falls to two unless the active severity is Evolution III, which reduces it to one, or a valid Kruger Directorate accepts the special emergency mandate.

The event creates a long national recovery problem. A short negative modifier cannot carry the concept.
The player must decide which institutions to save, whether to reveal the scale of the collapse, which foreign help to accept, which fields to rebuild first, and what kind of scientific system will replace the one that failed.
The AI receives the same recovery logic through ordinary decisions, missions, and scripted priorities.

## What has failed

Every firing selects one primary collapse profile and may add a secondary profile at higher evolution levels.
The profiles change the opening losses, the most efficient recovery actions, the secondary incidents, and the foreign reaction pool.
They never replace the core effects of slot loss, research-speed damage, active-project failure, and technology regression.

### Physical destruction

Laboratories, testing halls, university buildings, prototype shops, archives, and specialized instruments have been destroyed or rendered unusable.
This profile produces the highest initial loss of Scientific Capacity and makes facility reconstruction, replacement equipment, transport, and guarded work sites especially important.
War, occupation, bombing, disaster damage, sabotage, and severe domestic disorder increase its weight.

### Archive catastrophe

Design notebooks, test records, production drawings, tables, specimen collections, calibration histories, and unpublished corrections have been burned, stolen, scattered, or deliberately destroyed.
This profile produces the lowest initial Archive Recovery and increases the chance that advanced branches regress by more than one generation when the active evolution permits it.
Archive retrieval, foreign duplicate records, surviving libraries, and retired specialists become especially valuable.

### Specialist dispersal

Scientists, engineers, technicians, toolmakers, laboratory assistants, professors, and production specialists have disappeared into exile, military service, prisons, competing institutions, or foreign employment.
This profile lowers Scientific Capacity, creates a larger scientific diaspora, and opens recall, protection, credential recognition, and foreign-poaching incidents.
A country at war, under occupation, suffering repression, or experiencing poor stability receives greater weight for this profile.

### Institutional purge

Political authorities, security services, factional leaders, military offices, or ideological organizations have removed entire schools of thought and the people associated with them.
The immediate physical damage may be limited, but the country loses trust, mentorship chains, criticism, and the ability to admit error.
This profile raises the cost of an open reconstruction, makes concealment more attractive to authoritarian AI, and gives the Independent Academy Compact its strongest long-term value.

### Verification collapse

Published results, factory tolerances, laboratory standards, and prototype claims can no longer be reproduced consistently.
Some surviving records are false, incomplete, badly indexed, or dependent on instruments that no longer agree with one another.
This profile creates strong research-speed and production-reliability pressure and makes standards, metrology, proficiency testing, peer review, and controlled replication central to recovery.
It also carries the highest risk of false archives when the player rushes reconstruction.

### Educational rupture

Universities, technical schools, apprenticeships, professional societies, and military design schools have stopped producing qualified replacements.
Senior specialists remain, but their knowledge cannot pass reliably to a new cohort.
This profile makes the crisis slower to solve through emergency spending alone and gives training, mentorship, reopened institutes, and protected early-career specialists greater value.

## Target selection

Each firing selects one valid major country or one valid player-controlled country.
A country that is both a major and player-controlled appears once in the candidate pool.
The event does not gain an extra hidden preference for a human player merely because that country satisfies both categories.

All valid candidates receive a base chance, then target suitability adjusts the ordering.
The intended result is broad campaign variety without repeatedly striking the same damaged state or selecting a country whose research system cannot support the event.

### Valid target requirements

A normal country is valid when all of the following are true:

- It exists and controls at least one state.
- It has a functioning ordinary technology and research system.
- It is a major or is currently controlled by a human player.
- It has enough safe researched technology for the active severity to produce a meaningful rollback.
- It is not already in the unresolved institutional phase of Research Failure.
- It is not inside its post-reconstruction target immunity period.
- It is not a country whose owner system marks ordinary technology regression as invalid.

The shared civilian classifiers may support the target check, but Event 60 owns the final validity predicate.
A special Chaos country is excluded when it does not use ordinary human research institutions or when its owner has no safe regression contract.
A human Kruger host or Directorate remains eligible only when Event 16 explicitly confirms that the country uses the standard research system and provides the required preservation and cleanup adapter.

### Low-capacity player countries

A player-controlled country with only two current research slots can still be targeted at baseline because the technology loss, active-project failure, and research-speed collapse remain meaningful.
Its selection weight should be lower when stronger valid candidates exist because one of the event's main effects would otherwise have no practical impact.
Evolution III remains fully meaningful because it reduces the country to one slot.

A country with too few safe regression candidates is unavailable. It receives no fake losses or unsafe technology removal.
The event picker should show Event 60 as unavailable when no valid target exists.

### Repeat-target protection

A country in active reconstruction is always excluded.
After institutional reconstruction is complete, the country receives a substantial target immunity period.
The baseline design target is about three years, with carefully bounded shortening at higher Chaos tiers.
The immunity begins when the institutional crisis resolves, not when the opening event fires.

A country can still retain unrecovered technologies after the institutional crisis is resolved.
A later firing may add new losses to the existing national lost-knowledge ledger, but its target weight is reduced when a large earlier deficit remains.
This allows the repeatable event to matter again without creating an automatic permanent scientific death spiral.

## Incident identity and persistence

Every firing creates a unique incident sequence.
The sequence owns the target, opening severity, evolution level, collapse profiles, pre-failure slot count, active-project records, lost-technology ledger entries, response stance, foreign actors, reconstruction progress, Chaos transactions, and cleanup state.

The incident must be idempotent.
Reloading a save, rebuilding a decision category, reopening Event Details, changing player control, or receiving the same delayed event twice may not apply the opening damage again.
Every major transaction needs a one-time receipt tied to the incident sequence.

The country can have only one unresolved institutional incident at a time.
Residual lost-technology entries from older resolved incidents remain distinguishable by sequence for audit and achievement tracking, but the player sees one combined list of knowledge still missing.

## Opening sequence

The opening should use a short sequence so one popup does not hide every calculation and choice.

### The collapse

The entry event establishes that the affected country can no longer trust or reproduce part of its own scientific and industrial knowledge.
The visible evidence should include closed laboratories, missing specialists, unusable records, failed prototype repetition, conflicting measurement standards, and production teams unable to recreate equipment that already exists in service.
The final text should avoid declaring a single universal cause when the selected profile is broader or uncertain.

Before any mutation, the event records the target's scientific state and verifies that the transaction can be completed safely.
If the technology and slot preflight cannot build a valid transaction, the event must fail closed and return to the picker without applying partial damage.

### The first inventory

A short delayed follow-up presents the first verified damage summary.
It identifies the broad affected domains, the current research-slot count, the scale of active-project loss, the two reconstruction values, and the strongest immediate threat.
It does not expose internal technology IDs, random weights, hidden profiles, or technical implementation state.

### The national response

The target chooses one opening response stance.
Every stance accepts the core collapse.
The choice changes starting recovery conditions, foreign awareness, institutional politics, and later route availability.

#### Open scientific emergency

The government admits the scale of the failure and allows universities, armed services, industry, foreign partners, and professional societies to exchange records quickly.
This begins with higher Archive Recovery and gives the broadest access to foreign duplicate records, diaspora support, and international reconstruction.
It also makes the country's weakness easier for rivals and intelligence services to exploit.

The option suits governments with trusted allies, research-sharing partners, high institutional legitimacy, or a strong need for rapid recovery.
Its tone should be grave, practical, and publicly accountable.

#### Seal the institutions

The government restricts information, classifies the missing knowledge, isolates laboratories, and tries to conceal how far the country has fallen.
This reduces immediate foreign exploitation and limits the first public political shock.
It begins with lower Archive Recovery, greater specialist flight, and a rising chance that concealment will later be exposed.

The option suits governments at war, isolated states, authoritarian administrations, and countries facing strong enemy intelligence.
Its tone should be controlled, euphemistic, and aware that secrecy is being purchased with slower verification.

#### Emergency Kruger mandate

A valid Kruger Directorate may offer to preserve the country's existing research-slot capacity by placing the remaining scientific system under emergency Directorate control.
Accepting the mandate prevents the slot reduction for this incident.
It does not prevent the research-speed penalty, cancellation of active work, loss of research advantages, or technology regression.

The cost must be severe and owned jointly with Event 16.
The Directorate gains durable political and institutional leverage, civilian oversight weakens, and later reconstruction is constrained by the bargain.
The option must never grant immunity without moving the country closer to the consequences of Directorate power.
Its tone should present a precise coercive contract with no heroic framing.

A Kruger country that rejects the mandate uses either the open or sealed response.
A Directorate that already governs directly still pays an institutional cost because preservation concentrates the surviving system further and makes independent recovery harder.

## Immediate national state

After the opening transaction, the country enters the unresolved institutional phase.
It receives one evolving crisis idea that represents the scientific establishment in ruins and one archive state that changes as records are recovered.
The design should use staged replacements or dynamic modifiers instead of leaving a pile of permanent crisis ideas.

The opening state includes:

- The operational research-slot floor for the active severity.
- A major research-speed penalty derived from Scientific Capacity.
- Cancelled or failed active research projects.
- A recorded set of regressed researched technologies.
- A national lost-knowledge ledger that allows safe rediscovery support.
- Legacy-production pressure for affected equipment and industrial families where the technology graph proves that pressure is valid.
- A temporary reconstruction decision category.
- A first stabilization objective.
- Foreign aid and exploitation hooks appropriate to the response stance and collapse profile.

## Public mechanic values

The event exposes two persistent custom values.
Internal calculations may use more variables, but they remain hidden unless a concise explanation is needed for a current action.

### Scientific Capacity

Scientific Capacity runs from 0 to 100.
It represents functioning laboratories, technical schools, trained personnel, institutional coordination, verified instruments, protected facilities, professional trust, and the ability to sustain several research programs at once.

Low Capacity imposes the main research-speed penalty and blocks restoration of missing research slots.
Higher Capacity opens institute projects, reduces the penalty, supports reliable research, and eventually restores the country's pre-failure institutional ceiling.

The value should use clear qualitative bands and keep the long formula internal:

| Capacity | Public state | Main consequence |
| --- | --- | --- |
| `0-19` | Ruptured system | Research is barely coordinated and only the emergency core functions. |
| `20-39` | Emergency network | The country can preserve a small research program but cannot reopen normal institutions. |
| `40-59` | Reopened institutes | The first missing slot can be restored through a real project and the speed penalty begins to ease materially. |
| `60-79` | Coordinated system | Several institutions function again and repeated slot restoration becomes possible. |
| `80-99` | Productive system | The pre-failure network is nearly restored and only residual institutional damage remains. |
| `100` | Reconstructed establishment | The country has restored its institutional capacity and can resolve the active crisis when all required slot and settlement conditions are met. |

The exact starting value scales with severity and collapse profile.
A normal baseline opening should usually begin in the emergency-network band.
Evolution III should begin at or near the bottom of the scale.

### Archive Recovery

Archive Recovery runs from 0 to 100.
It represents surviving notebooks, blueprints, raw data, specimen collections, standards, calibration histories, test failures, tacit procedures captured from specialists, foreign duplicate records, and verified indexes that allow the country to distinguish useful knowledge from false or obsolete material.

Archive Recovery never restores a researched technology automatically by reaching a threshold.
It makes rediscovery easier, reveals reliable branch information, unlocks targeted research support, and reduces the chance that rushed reconstruction follows false records.

| Archive Recovery | Public state | Main consequence |
| --- | --- | --- |
| `0-24` | Scattered fragments | The country knows that knowledge is missing but cannot reconstruct a trustworthy sequence. |
| `25-49` | Indexed remnants | Lost domains are identified and the first targeted rediscovery support becomes available. |
| `50-74` | Reconstructed series | Verified predecessor chains and design families provide substantial bonuses when relearning lost work. |
| `75-99` | Verified national archive | Most lost work has a usable documentary trail and advanced branch recovery becomes much faster. |
| `100` | Complete recovery ledger | Every surviving record has been assessed and the country retains the strongest allowed rediscovery support until the outstanding lost technologies are relearned. |

Archive Recovery can remain below 100 when the institutional crisis resolves.
The decision category then enters a smaller residual mode focused on lost knowledge. Emergency governance ends.

## Institutional resolution and residual recovery

Research Failure has two related end points.

### Institutional reconstruction

The active unresolved crisis ends when all of the following are true:

- Scientific Capacity has reached 100.
- Every research slot suppressed by this incident has been restored up to the recorded pre-failure ceiling, with any valid external capacity additions reconciled correctly.
- The country has completed one institutional settlement route or the Event 16 Directorate settlement that replaces it.
- No mandatory emergency project is still failed or unresolved.

At this point the main research-speed penalty ends, the country leaves the unresolved-target exclusion, the one-time reconstruction Chaos reversal is applied, and the target immunity period begins.

### Lost-knowledge legacy

Technologies that remain unresearched stay in the lost-knowledge ledger.
The same category changes to a compact post-crisis mode with no more than three relevant actions at one time, such as selecting a priority domain, using a verified archive package, or recalling a specialist linked to an outstanding branch.

This phase ends when every recoverable lost technology has either been researched again, explicitly abandoned by a valid permanent branch decision, or removed from the ledger because its owner system made it obsolete.
The category then closes completely and any residual temporary rediscovery support is removed.

Restoring research slots never restores lost technologies.
Completing the archive never grants an automatic full technology refund.

## Repeat firing

A later firing creates a new incident and repeats the opening transaction only after the earlier institutional crisis is resolved and target immunity has ended.
The new incident records the country's current slot ceiling and current technology state.

Older missing technologies remain missing.
The new rollback process skips already lost nodes, expands the combined ledger safely, and avoids selecting branches that cannot support further regression.
A country with a large residual deficit receives lower target weight and a less aggressive safe-selection cap unless the active evolution explicitly permits a deeper collapse.

Repeated Kruger exemptions require a fresh cost.
Earlier Directorate entrenchment makes the political consequence stronger and may make independent settlement routes harder to recover.
The exemption can never become a permanent toggle that removes the event's slot effect without further sacrifice.

## Player-control changes

The incident belongs to the country, not to the person currently controlling it.

- A player who takes control of an affected AI country gains the reconstruction category and the current state without reapplying the opening damage.
- A country returned to AI control continues through the same decisions and missions using the AI strategy matrix.
- A player tag switch does not clear the original country's crisis.
- Multiplayer players receive country-scoped decisions and targeted diplomatic events only for the countries they control.
- The target-selection pool deduplicates countries so multiplayer does not create extra weight for a player major.

## Event log and Event Details

The opening event creates one normal Event 60 history entry with the affected country as actor.
Follow-up reports, project events, setbacks, and foreign offers do not create extra random-event pacing entries.
Actual evolution milestones use the shared evolution log with the target as actor.

Event Details should present:

- The premise that a national scientific system can no longer reproduce part of its own knowledge.
- The valid target class in player-facing terms.
- The repeatable nature of the event.
- The Scientific Research cluster and High member role.
- The three evolution premises.
- The most recent actor and normal fired-count information supplied by the shared framework.

The details text should not list exact penalties, hidden candidate weights, internal technology registries, or future surprise incidents.
The event history row should use the target country's flag and name.

## Scientific Research cluster contract

Event 60 remains individually eligible at Chaos level 1 when a valid target exists.
Its cluster membership does not raise the event's own minimum level.
The Scientific Research cluster may unlock at a different tier according to the authoritative cluster registry.

As a High member, Research Failure represents one of the cluster's strongest negative outcomes.
When a cluster firing includes a positive scientific event in the same episode, ordering must preserve the crisis and prevent accidental cancellation.
Technology regression occurs first.
A later technology gift or research benefit may then interact with the newly created lost-knowledge ledger as a partial recovery opportunity.

Two destructive scientific members should not independently target the same country in contradictory order unless their accepted designs define a combined incident.
Cluster firing still counts as one global pacing event while Event 60 retains its own history, repeatable cap change, actor, and evolution state under the shared cluster rules.

## Player-facing writing direction

The writing should focus on material and institutional evidence.
Useful details include silent laboratories, prototype teams unable to repeat a test, contradictory measurement standards, missing notebooks, empty university departments, rejected production batches, specialists whose locations are unknown, and archives whose surviving pages no longer form a complete process.

The tone should be severe and concrete.
The event should avoid mystical explanations unless another event has genuinely caused the collapse.
It should also avoid modern digital language that does not fit the normal 1936-1945 presentation.

The final localisation should treat working labels in this pack as structural names only.
Options should communicate the public stance and visible consequence without exposing hidden weights or later incidents.
Decision text should describe the action being taken, its real costs, the value it changes, and the immediate risk.
The Kruger option should sound like a bargain that transfers power, not a free scientific rescue.
