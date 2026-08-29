# Event 027: Doctrine Research research notes

## Purpose

This note records the doctrine-system facts and project constraints used to resolve the rough Event 027 idea. It separates supplied-source findings, official Hearts of Iron IV findings, design inferences, and implementation questions.

It is supporting research. The accepted event behavior is defined by the four specification parts.

## Supplied project findings

### Stale catalog row

The supplied event catalog snapshot still defines Event 027 as Doctrine research, a Minor Fire-Once event that grants a complete military doctrine to one major country. Its status is Unavailable, with no cluster or evolution content.

The user's current brief is authoritative and replaces that row. The accepted design is global, Minor Repeatable, choice-based, and evolution-scaled.

### Repeatable-event behavior

The project mechanics define repeatable events with shared weight recovery and a halved maximum weight cap after each firing. Event 027 therefore receives diminishing campaign frequency without needing a separate fallback reward or arbitrary one-time conversion.

### Global event and multiplayer model

Chaos Redux uses a shared global event pool and global Chaos Meter, while events can target one country or act globally. Event 027 is designed as one global firing with country-owned batches.

### Event cluster behavior

The event skill defines clusters as a catalog layer above normal events. A cluster counts as one global pacing event. Member effects, event state, history, and repeatable cap changes still apply, while member subevents do not each advance the timer.

Member severity has four display values: Low, Medium, High, and Severe.

### Chaos Warfare

The supplied mechanics guide defines Chaos Warfare as a conditional CBRN Grand Doctrine with four visible mastery tracks:

- Hazard Assault Formations
- Toxic Armored Warfare
- Contaminant Fire Support
- Integrated CBRN Command

Each track has five mastery levels. Its establishment and later rewards depend on specific equipment, formations, technologies, readiness, policy, and operation gates.

Event 027 therefore needs a custom doctrine adapter. A generic vanilla-only mastery grant would miss one of the project's major doctrine systems and could bypass its downstream state.

### Existing dynamic effects

The supplied dynamic-effect registry includes a broad technology-union helper and custom Kruger technology grant helpers. None fits Event 027.

Event 027 advances selected doctrine state. It should not copy a donor's research, grant a random Kruger technology, or use technology helpers as a doctrine fallback.

### Project implementation requirements

The supplied repository rules require doctrine work to use the HOI4 MCP technology inspection, rendering, and comparison routes. Weighted AI requires the probability auditor and named scenarios. Event work requires event inspection, full event-log wiring, documentation alignment, and authoritative workbook updates.

The actual repository and MCP tools were unavailable in this runtime. These checks remain implementation gates.

## Official Hearts of Iron IV findings

### Grand Doctrines and subdoctrines

The official Developer Diary for Doctrines, published on September 30, 2025, describes a hierarchy of Grand Doctrines and subdoctrines. A country without a Grand Doctrine selects one first. Grand Doctrines expose category tracks, and each track can hold one selected subdoctrine.

Army, Navy, and Air received the reworked doctrine model in the 1.17 release family.

### Tracks and mod support

The official doctrine diary states that the system supports an arbitrary number of tracks. The official 1.17.1 patch notes later added `max_track_columns` and `max_track_rows` properties for Grand Doctrines with multiple rows.

Event 027 should therefore avoid assuming exactly four tracks or one row. The adapter registry must read each domain's verified graph and preserve its native order.

### Mastery

The official doctrine diary defines Mastery as track-specific practical experience. Mastery can come from combat, training, attachés, faction sharing, focuses, and decisions. Each mastery level grants additional rewards.

The system supports arbitrary mastery-point requirements per level. Event 027 should not assume that one fixed mastery-point amount equals one level in every branch.

### Mastery banking

The official doctrine diary states that Mastery can be stored when a track has no selected subdoctrine or when the selected branch is complete.

This creates an important implementation case. Selecting a new subdoctrine through Event 027 may cause native banked progress to resolve. The event must preserve that native progress and separately attribute only its own one-step grant.

### Native Milestones

The official doctrine diary uses Milestone for the Grand Doctrine reward connected to completing a track. Replacing a completed subdoctrine can remove the Milestone.

The user's rough phrase `mastery milestone` describes a one-level event grant. The accepted specification uses `event mastery step` to keep these concepts separate.

### Doctrine purchase cost

The official doctrine diary states that selecting Grand Doctrines and subdoctrines normally costs the relevant military experience.

The accepted Event 027 design waives the cost for the doctrine action selected through the event. This is a design decision, not an official rule. The event does not refund prior spending or grant generic experience.

### Modding safety

The official 1.17.1 patch notes mention a crash fix for the `has_mastery_level` trigger when supplied a bad subdoctrine. This supports a fail-closed adapter design and reinforces the need to validate every branch identity before use.

### Existing official achievement

The official Arts and Achievements publication lists Doctrine of Choice, which requires fully mastering all subdoctrines in a Grand Doctrine.

Event 027's achievements use one-batch adoption, concentration, and distribution patterns. They avoid repeating the same all-subdoctrine completion condition.

## Design inferences

The following points are design resolutions derived from the brief and current doctrine model. They are not direct statements from a supplied or official source.

### One choice begins with a domain

The user describes every country choosing a doctrine or subdoctrine branch. The modern game has several doctrine domains. The specification interprets each Event 027 choice as domain-scoped so a country can adopt Navy doctrine while already having Army doctrine.

This avoids treating the first doctrine selected anywhere as the country's only possible doctrine adoption through the event.

### Empty track selection grants the first event mastery step

The brief states that a country with an active doctrine advances one mastery step in an available subdoctrine branch. An active Grand Doctrine can contain an empty track.

The specification lets the country select an eligible subdoctrine in that track and receive the first event mastery step in the same choice. Grand Doctrine adoption remains the only adoption action explicitly defined to consume a choice without mastery.

This behavior must be verified against the local doctrine effects and banked-mastery sequence. If the engine cannot perform it safely, the implementation must report the blocker. It cannot substitute experience or a two-choice track-adoption rule without approval.

### Event actions waive experience cost

The event represents a breakthrough reward. Charging normal experience after the event grants a choice would make some choices unusable and would convert the event into an availability prompt and weaken the intended doctrine grant.

The specification therefore treats the selected valid adoption as free. All non-cost eligibility remains intact.

### Fully exhausted countries receive no compensation

A country that has completed all valid doctrine content has no coherent mastery target. A substitute reward would make the event increasingly valuable to countries already ahead in doctrine.

The specification closes the batch without compensation.

### Batch queue

The rough idea assumes a simple chain. A repeatable global event in multiplayer can fire while earlier choices remain unresolved. The specification adds country-owned batch queues to prevent overwrite, duplication, and cross-country state leaks.

### Evolution thresholds

The user defines batch sizes but does not assign chaos tiers. The specification recommends one stage per rising tier from Gathering Storm through Totalen Chaos. This follows the project evolution model and leaves World Collapse to its normal automatic-event freeze.

### National Breakthroughs severity

The user names the cluster and provisional members without a numeric cluster ID or Event 027 severity. The specification recommends Medium because the event is global and can grant five direct mastery steps at its highest stage.

## Implementation questions that require local evidence

The coding agent must answer these questions before implementation can be marked complete:

1. What exact effects select a Grand Doctrine, select a subdoctrine, read mastery level, and advance exactly one level in the installed game version?
2. Can the engine grant one level directly, or must the implementation calculate the exact mastery amount needed for the next threshold?
3. In what order does banked mastery resolve when a subdoctrine is selected?
4. Can a branch selection plus one event mastery step be one safe transaction when banked mastery completes the branch?
5. Which doctrine domains exist under every supported DLC combination in the current mod setup?
6. Does current Special Forces content expose a compatible Grand Doctrine, track, subdoctrine, and mastery model?
7. What are the exact Army, Navy, Air, Special Forces, and Chaos Warfare graph identities and sprite identities?
8. Which native AI doctrine preferences can Event 027 reuse?
9. How should a country event display doctrine and track icons under the current event UI consumer?
10. Which save-safe country variables, arrays, flags, or event targets best represent active and queued batches?
11. How does the current multiplayer event pipeline route country-owned events after tag switching or control changes?
12. What current cluster ID is free in the authoritative workbook and runtime registry?
13. Which achievement IDs are free in the root achievement registry?
14. Which report-event sprite naming convention is current in the repository?

## Required local references during implementation

The implementation agent must consult:

- the actual Event 027 source if any baseline implementation exists
- current Chaos Redux event registration and event-log files
- current doctrine and technology definitions
- current Chaos Warfare doctrine files and documentation
- current achievement registry
- current cluster registry
- current report-event GFX and event-picture references
- current AI doctrine and research preferences
- the offline Paradox wiki pages required by `AGENTS.md`
- the installed vanilla documentation and relevant vanilla doctrine definitions
- at least one vanilla or current project precedent for direct mastery grants

## Official source list

- Hearts of Iron IV, Developer Diary | Doctrines, September 30, 2025.
- Hearts of Iron IV, No Compromise, No Surrender release notes for the 1.17 doctrine replacement, November 20, 2025.
- Hearts of Iron IV, NCNS Patch 1.17.1, November 26, 2025.
- Hearts of Iron IV, Arts and Achievements publication containing Doctrine of Choice, November 2025.

## Research conclusion

The rough event is compatible with the modern doctrine system when it is implemented as a domain-aware batch of discrete doctrine actions. The main technical risk is exact one-level advancement around banked mastery and custom doctrine state. A verified adapter layer and transaction receipt solve the design problem without adding a second doctrine interface or generic fallback reward.
