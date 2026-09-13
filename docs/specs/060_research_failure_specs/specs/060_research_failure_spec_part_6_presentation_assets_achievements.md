# Presentation, idea lifecycle, assets, achievements, and documentation

## Presentation choice

Research Failure uses the normal event popup, Event Details, one evolving decision category, national spirits or dynamic modifiers, missions, targeted foreign events, and the shared Event Logs.

The decision category uses a static category picture and a concise attached status summary.
The two values, operational slot count, and current project can be read clearly without a separate event-owned window.
The picture establishes identity and atmosphere but contains no painted buttons, meters, numbers, or fake controls.

The category changes by phase so the player sees the actions that matter now.
The normal budget is three to five primary decisions and one active mission.
A second mission appears only when a foreign or wartime objective genuinely needs a separate deadline.

## Player-facing information hierarchy

The player should understand five things within a few seconds of opening the category:

1. How much Scientific Capacity remains.
2. How much of the archive has been recovered.
3. How many research slots are currently operational compared with the recorded ceiling.
4. Which major project is active and when it ends.
5. Which action most directly improves the current bottleneck.

Internal values such as branch depth, false-record seed, specialist-cohort identity, external slot receipts, target weight, and owner callbacks remain hidden.
A tooltip can explain material contributors in plain language when they change an immediate choice.

The category description should not become a ledger of every lost technology.
A compact lost-domain list or selected-domain tooltip is enough for ordinary play.
A detailed debug or documentation view can carry the full technical ledger outside normal player text.

## Event text direction

### Opening event

The viewpoint should be the affected government receiving verified evidence from laboratories, factories, universities, and armed-service design offices.
The force driving the event is institutional failure.
The text should show that existing machines and weapons still exist while the processes needed to reproduce them no longer produce consistent results.

Useful concrete details include:

- Two laboratories producing different measurements from the same standard.
- A prototype shop unable to recreate a component already fitted to deployed equipment.
- Empty university departments and sealed offices.
- Notebooks with missing pages or conflicting revisions.
- Production drawings that omit the adjustments known only to a vanished specialist.
- Research projects abandoned because no one can verify the earlier work.

The text should preserve uncertainty about the complete cause when several profiles are active.
It should avoid generic claims that science itself has disappeared.
The country has lost institutions and reproducible knowledge, not human curiosity.

### First inventory

The follow-up should summarize the broad domains affected, the operational slots, and the two public values.
It should mention the strongest visible collapse profile without listing hidden weights.

The tone is diagnostic and urgent.
It should not sound like a developer report or present raw technology IDs.

### Opening options

- The open-emergency option should sound publicly accountable and willing to admit weakness in exchange for rapid cooperation.
- The sealed option should sound controlled and security-minded, with a visible warning that verification and specialist retention will suffer.
- The Kruger option should sound contractual and coercive, with the political transfer of authority clear before the player accepts.

Final button wording remains an implementation localisation task.
This pack supplies direction and leaves final wording to implementation.

### Secondary incidents

Secondary incident text should use the actor that caused the problem.
A false archive focuses on incorrect methods and wasted work.
A foreign appointment focuses on specialists and institutions.
A prototype failure focuses on production and maintenance.
A concealment exposure focuses on evidence reaching outsiders.

The incidents should avoid repeated scenes of ministers reading sealed reports.
They should show the people, laboratories, factory floors, instruments, archives, and training systems involved.

### Reconstruction completion

The completion event should describe a functioning scientific network and the settlement that now governs it.
It must also make clear that some lost technologies may still need to be researched again.
The country has restored the ability to progress.
It has not received a magical return to its old technology position.

## Event Details direction

The Event Details premise should explain that the target loses the ability to reproduce part of its own established knowledge and must rebuild scientific institutions.
It should name the valid target class in broad terms and identify the event as repeatable.

Evolution details should focus on their public premises:

- Lost Archives expands the range and depth of missing knowledge.
- Scientific Dark Age damages core industrial, electronics, military, and advanced-engineering capacity.
- Knowledge Collapse reduces the country to one functioning research slot and leaves recovery as a multi-year national project.

The details view should not list exact node counts, internal severity formulas, hidden target weighting, or special-technology registry fields.

## Decision and mission text direction

Each decision needs:

- A concrete action.
- A compact icon-first cost string.
- A concise requirement summary.
- A visible effect on Scientific Capacity, Archive Recovery, a slot project, a lost domain, or a named risk.
- A tooltip that explains the public tradeoff.

The text should name dynamic places, partners, and domains where relevant.
A decision to secure laboratories should identify the selected states or research centers in its tooltip.
A foreign archive channel should name the partner.
A lost-domain priority should name the current field.

Missions should state the objective, deadline, success effect, and failure consequence.
They should not expose hidden project-roll values.

## Idea lifecycle

The event should use a small number of evolving ideas or dynamic modifiers.
It should not leave every stage as a separate permanent national spirit.

| Working identity | Start or unlock | Role | Changes through | Final disposition |
| --- | --- | --- | --- | --- |
| Scientific Establishment in Ruins | Opening | Main Capacity-linked research penalty and slot crisis | Capacity thresholds, slot projects, evolution escalation | Removed at institutional reconstruction |
| Fragmented Archives | Opening | Archive state, false-record risk, and rediscovery access | Archive projects, foreign duplicates, specialists, evolutions | Replaced by settlement archive state or removed when ledger closes |
| Legacy Production Crisis | Conditional | Represents active production families whose knowledge was regressed | Standards projects and technology rediscovery | Recalculated and removed family by family |
| International Recovery Network | Consortium settlement | Foreign duplicate records, research links, and dependence | Partner actions and completion | Matures into a bounded long-term institution |
| Central Scientific Authority | Central settlement | Fast Capacity recovery and directed priorities with political risk | State projects and false-result incidents | Matures into a bounded long-term institution |
| Independent Academy Compact | Academy settlement | Slow protected reconstruction and strong resilience | Education and archive projects | Matures into a bounded long-term institution |
| Directorate Emergency Mandate | Kruger option | Slot preservation and Event 16 entrenchment | Event 16 authority and later settlement struggle | Replaced only through Event 16-approved outcomes |

The final implementation can use dynamic modifiers or staged ideas according to the verified engine pattern.
The player should normally see one main crisis idea, one archive or settlement idea, and a conditional legacy-production state.

## Visual direction

The visual package should present institutional collapse. Generic explosion imagery does not fit the event.
The central image is a period scientific workplace whose knowledge chain has broken.

### Report event picture

**Purpose:** Opening Research Failure event.

**Source mode:** Generated period-authentic documentary scene because the incident is fictional and country-dynamic.

**Subject direction:** A 1936-1945 laboratory or prototype workshop after abrupt abandonment, with damaged notebooks, calibration instruments, dismantled apparatus, empty work stations, and engineers trying to compare incompatible drawings or measurements.

**Composition direction:** One clear human-scale scene with recognizable scientific and industrial activity.
The emotional center should be failed reproduction and missing expertise.
A map, staff table, or generic burning city should not dominate.

**Avoid:** Modern computers, contemporary safety equipment, readable generated text, science-fiction devices, exaggerated fire, cinematic color grading, generic chemical glassware without an industrial context, and real identifiable scientists.

### Static decision category picture

**Purpose:** Persistent identity for the reconstruction category.

**Source mode:** Generated full-canvas period institutional scene.

**Subject direction:** A damaged archive and laboratory being rebuilt, with recovered boxes, measuring instruments, technical drawings, shelves, and a small working team.

**State direction:** One static picture is enough because the category state is communicated through values, decisions, and idea icons.
The picture should remain readable behind category text and must not contain fake interface elements.

The asset worker must inspect the canonical vanilla decision-category picture reference folder and its contact sheet before production.
The current reference family uses a 114 by 101 canvas, but the active consumer must be verified before final sizing.

### Decision category icon

**Purpose:** Small category button icon.

**Source mode:** Generated with genuine transparent background.

**Symbol direction:** A broken scientific instrument, cracked lens, damaged technical drawing, or interrupted measurement standard combined into one strong silhouette.
The icon should remain readable at its actual decision-category size.

### Decision icons

Each icon needs separate source art designed for the decision surface.
Do not resize the category icon to satisfy these roles.

Planned decision icon families:

- Secure surviving laboratories.
- Recover records and instruments.
- Protect and recall specialists.
- Establish emergency standards.
- Open a foreign archive channel.
- Reopen a research institute.
- Rebuild universities and technical schools.
- Restore the national standards network.
- Reconstruct the central archive.
- Train replacement cohorts.
- Prioritize a lost domain.
- Commission foreign reconstruction.
- Choose each institutional settlement.
- Challenge or confirm the Directorate mandate where Event 16 permits it.

Icons should use strong silhouettes and real transparent unused canvas.
They should avoid tiny writing, fake blueprints with readable text, and repeated recolors of one source.

### Mission icons

Planned mission roles:

- Stabilize the scientific network.
- Reopen the current institute.
- Complete a major archive or standards project.
- Protect a foreign or exile research route when that mission is active.

Mission icons should follow the exact vanilla mission reference family and must not use decision-icon treatment.

### Idea and national spirit icons

Planned idea icon families:

- Scientific Establishment in Ruins.
- Fragmented Archives.
- Legacy Production Crisis.
- International Recovery Network.
- Central Scientific Authority.
- Independent Academy Compact.
- Directorate Emergency Mandate.

The settlement icons should share a visual theme but remain separate source artworks designed for 64 by 64 idea presentation.
The Directorate icon may use an established Event 16 symbol only after checking ownership and visual consistency.

### Achievement icons

Each achievement requires the full normal, grey, and not-eligible triplet under the root achievement path and must use the final achievement ID as its basename.
The icons need separate generated source art and the normal achievement overlay workflow.

### Event Log and evolution presentation

The event uses the shared Event Log and Event Details assets.
No new shared-framework art should be created merely for Event 60.
The event name, actor, cluster role, evolution names, and details text still need full localisation coverage.

## Asset inventory and status

| Asset family | Quantity direction | Source mode | Animation | Main status note |
| --- | --- | --- | --- | --- |
| Report event picture | 1 | Generated period documentary scene | Static | Opening incident |
| Decision category picture | 1 | Generated period institutional scene | Static | No fake controls |
| Decision category icon | 1 | Generated native transparency | Static | Separate source art |
| Decision icons | About 12 to 16 | Generated native transparency | Static | Final count follows implemented actions |
| Mission icons | About 3 to 4 | Generated native transparency | Static | Separate mission reference family |
| Idea icons | About 7 | Generated native transparency | Static | Includes three settlements and Kruger mandate |
| Achievement triplets | 2 triplets | Generated source plus achievement processing | Static | Root achievement naming rules |

The accepted design does not need character portraits, country flags, 3D models, unit counters, skeletal animation, or frame-sheet animation.
This sentence is an asset authorization boundary inside the handoff, not a request to create placeholders for absent families.

## Achievement set

The event is deep enough to support two difficult achievements.
The titles below are working labels and IDs.
Final player-facing names and descriptions should be written during implementation from the stated direction.

### Achievement 1: From First Principles

- Working ID: `research_failure_from_first_principles`
- Eligible countries: Any human-controlled country targeted by Event 60.
- Visibility: Visible.
- Required severity: Scientific Dark Age or Knowledge Collapse.
- Core objective: Reach institutional reconstruction and recover every technology lost by the qualifying incident through ordinary research.
- Time target: Within six years of the qualifying incident, subject to final balance testing.
- Disqualifiers: Direct technology restoration from Gift from Scientists, Brilliant Scientist auto-grant, donor union grant, console or debug grant, Kruger technology restoration, or foreign archive action that directly grants a lost technology.
- Allowed help: General research bonuses, ordinary research sharing, archive bonuses, licenses, specialist return, and foreign help that does not grant the technology directly.
- Why it is difficult: The player must rebuild slots and research a broad multi-domain deficit under severe speed penalties without using the strongest direct recovery shortcuts.
- Tracking: Store the qualifying incident sequence, complete lost-node set, direct-grant disqualifiers, start date, institutional resolution, and final ledger closure.
- Title direction: Rebuilding advanced knowledge through reconstructed methods without receiving finished answers.
- Description direction: Mention the high-severity collapse, independent relearning, and full recovery without listing internal flags.
- Icon direction: A damaged formula or technical drawing reconstructed from separate pieces beside a working measuring instrument.

### Achievement 2: The Last Laboratory

- Working ID: `research_failure_last_laboratory`
- Eligible countries: Any human-controlled country targeted by Knowledge Collapse.
- Visibility: Visible.
- Core objective: Survive the one-slot phase, restore the full recorded pre-failure slot ceiling, reach Scientific Capacity 100, and complete the institutional settlement.
- Minimum one-slot exposure: At least 365 days, subject to final balance testing, so the achievement cannot be unlocked by an immediate scripted restoration.
- Disqualifiers: Emergency Kruger mandate, capitulation during the unresolved crisis, debug completion, slot duplication, or a direct effect that bypasses institute projects.
- Technology condition: Recover at least a substantial majority of the incident's lost nodes, with a final target around 75 percent after balance testing.
- Why it is difficult: The country must continue functioning with one research slot and rebuild the national system under the most severe event state.
- Tracking: Store the Knowledge Collapse sequence, one-slot dates, pre-failure ceiling, restored-slot receipts, capitulation state, Kruger receipt, recovered-node ratio, and institutional completion.
- Title direction: The survival of one functioning center while a national network is rebuilt around it.
- Description direction: Emphasize the one-slot crisis and full institutional recovery without revealing hidden timing variables.
- Icon direction: One illuminated period laboratory window surrounded by dark damaged buildings, with a precise instrument or archive box in the foreground.

The implementation should inspect the current Chaos Redux achievement registry and existing tracking patterns before final IDs are accepted.
The achievement prompt in this pack defines the production handoff.

## Documentation direction

Implementation should create a complete Event 60 document under the normal `docs/events/` structure.
It should explain:

- Target validity.
- Collapse profiles.
- Technology regression policy.
- Public values.
- Reconstruction phases.
- Institutional settlements.
- Kruger interaction.
- Evolutions.
- Foreign reactions.
- Event connections.
- Chaos impact.
- AI.
- Assets and their runtime consumers.
- Achievements.
- Validation scenarios.
- Known owner-controlled technology exclusions.

The event document should describe implemented behavior, not copy this planning pack word for word.
Exact technology registry and validation evidence can live in a system appendix.

## Catalog alignment direction

The authoritative workbook row should be updated only after implementation facts exist.
The CSV files are export-only snapshots and should not be edited directly.

The final player-facing row needs:

- Event name: Research Failure.
- Type: Minor Repeatable.
- Chaos level: 1.
- Cluster: Scientific Research.
- Member severity or role: High.
- Baseline detail describing the collapse of research capacity, regression of established technology, and national reconstruction.
- Evolution I: Lost Archives.
- Evolution II: Scientific Dark Age.
- Evolution III: Knowledge Collapse.
- Status matching the actual validation state.

The detail fields should match Event Details wording and avoid raw modifiers, exact node counts, implementation history, or the phrase To Be Reworked after completion.

## Localisation coverage

Implementation needs final localisation for:

- Event name and debug name.
- Opening event and first inventory.
- Opening options.
- Collapse-profile summaries.
- Public value names, bands, and tooltips.
- Decision category and phase descriptions.
- Every decision and mission.
- Settlement names and descriptions.
- Foreign offers and reactions.
- Secondary incidents.
- Evolution names and details.
- Event Details.
- Event Log actor and evolution selectors.
- Ideas and dynamic modifiers.
- Achievements.
- Asset tooltips where applicable.
- Catalog-facing text mirrored from the game.

All player-facing text should follow the project rule against developer-facing wording, raw state labels, rework history, and unexplained variables.
Final localisation must use the target's current country name, selected partner, selected domain, selected state, current slot count, and public values where those details matter.
