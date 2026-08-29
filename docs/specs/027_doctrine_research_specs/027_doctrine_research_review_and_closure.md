# Event 027: Manual subagent-role review and improvement-loop closure

## Review status

The supplied project defines custom Codex subagents for repository exploration, scripted-system architecture, probability auditing, localization auditing, event completion auditing, asset production, documentation curation, spreadsheet work, and improvement-loop planning.

This runtime did not expose a Codex subagent launcher or the configured HOI4 MCP server. No custom subagent was actually spawned, and no MCP artifact was produced.

The roles below were applied manually to the specification. Their required implementation-time evidence remains pending and is carried into the coding prompt and acceptance criteria.

## Repository explorer lens

### Finding

The supplied source set gives the project-wide event, doctrine-adjacent, cluster, asset, decision, focus, improvement, and subagent contracts. It does not contain the live Chaos Redux repository files, offline wiki snapshot, installed vanilla game, or authoritative catalog workbook.

### Design consequence

The package defines behavior and required surfaces without pretending that exact current file paths, doctrine IDs, effect names, sprite names, or free registry IDs have been verified.

### Required later work

A repository explorer should map:

- any current Event 027 implementation
- event registration and default enable allowlist
- event-log name, actor, detail, and evolution selectors
- current doctrine and technology files
- current Chaos Warfare source and helpers
- current AI doctrine preferences
- current achievement IDs
- current cluster registry and free ID
- current report-event sprite convention
- authoritative workbook row and cluster sheet
- required vanilla and project precedents

## Scripted-system architect lens

### Finding

The event needs two reusable structures:

- a doctrine-domain adapter registry
- a country-owned batch transaction and queue

The domain adapter prevents vanilla-only hardcoding and supports Chaos Warfare safely. The batch transaction prevents duplicate effects, lost choices, cross-country leaks, and stage overwrite.

### Required architecture properties

- one bounded country fanout per Event 027 firing
- no recurring whole-world on-action
- country-owned active batch and ordered queue
- batch size and stage snapshot
- dynamic option rebuild before every choice
- one-time success receipt
- exact one-level doctrine action
- banked mastery preservation
- fail-closed custom adapter behavior
- stable IDs for achievement tracking
- cleanup on completion and annexation

### Pending evidence

The actual architect must inspect existing dynamic effects and triggers before creating helpers. It must document any new generally reusable helper in the owning registry and keep event-private orchestration beside Event 027.

## AI probability auditor lens

### Finding

Global symmetry creates a balance problem when human choices are strong and AI choices are weak. Event 027 therefore needs scenario-based AI evidence.

### Manual output

`027_doctrine_research_probability_scenarios.md` defines domain, Grand Doctrine, track, custom doctrine, batch sequence, repeatable-event, cluster, DLC, and validity scenarios.

### Pending evidence

The actual auditor must use the HOI4 MCP probability workflow. Exact probabilities cannot be claimed from this specification because the complete candidate pools and live modifiers are unavailable.

Any patch to weights requires baseline inspection and final `hoi4.probability_compare` using the same scenario IDs.

## Localization auditor lens

### Finding

The main clarity risk is terminology. The official doctrine system uses Milestone for a completed-track Grand Doctrine reward, while the rough brief uses mastery milestone for a one-level grant.

### Accepted wording rule

Use mastery level or event mastery step for Event 027. Reserve Milestone for the native completed-track reward.

### Other text risks

- unclear choice consumption
- raw doctrine IDs
- hidden invalid options
- stale mastery values
- long effect lists
- identical wording for adoption and mastery
- generic laboratory framing
- service pages with no dynamic country or doctrine identity

### Pending audit

The actual localization auditor should review every event page, Event Details surface, evolution row, achievement description, scripted localization selector, and catalog-facing field after final implementation wording exists.

## Event completion auditor lens

### Finding

The most likely false completion states are:

- Army-only support
- five choices implemented as one large mastery-point grant
- no banked-mastery handling
- no queue
- AI using a smaller pool
- Chaos Warfare bypassing owner state
- cluster double fanout
- missing achievement tracking
- reused or missing assets
- stale catalog row
- no MCP evidence

### Manual output

`027_doctrine_research_acceptance_criteria.md` converts these risks into feature-level completion checks.

### Pending audit

The actual completion auditor should compare every specification file, any later accepted addendum, implementation source, assets, documentation, workbook, and validation evidence before a completion claim.

## Spreadsheet worker lens

### Finding

The supplied CSV row is stale and the National Breakthroughs cluster is absent. The CSVs are export-only snapshots.

### Manual output

`027_doctrine_research_catalog_cluster_handoff.md` gives the proposed event row, provisional cluster row, member treatment, status transitions, and workbook update sequence.

### Pending work

The spreadsheet worker must edit only the authoritative XLSX after final implementation wording exists, then run the repository CSV exporter.

## Generated event art lens

### Finding

The event needs one report image. A generated period documentary scene is appropriate because the event describes a worldwide institutional pattern and does not require a real person or specific archive event.

### Accepted scope

- one report-event image
- period-authentic joint-service exercise or staff-school demonstration
- source PNG, processed PNG, final DDS, manifest, and handoff

### Pending work

The generated event art subagent must inspect the canonical report-event references and use the official image-generation route. It must not create a portrait, national flag, modern scene, readable text, or generic command-table image.

## Icon artist lens

### Finding

The event needs three distinct achievement icon triplets. Doctrine option pages should reuse verified doctrine-owned icons.

### Pending work

The icon artist must inspect the canonical achievement references, generate original source art for each working achievement ID, create completed, grey, and not-eligible states, convert to DDS, and provide a manifest and GFX handoff.

## 3D and frame-animation lens

### Finding

The event does not introduce a visible unit, vehicle, aircraft, ship, building, creature, map entity, animated icon, animated panel, or animated portrait.

### Closure decision

3D production and frame animation would add no gameplay clarity. The accepted asset package remains static.

This decision follows the source skills after review. It is not a missing fallback.

## Decision and focus lens

### Finding

The complete interaction already occurs through a short chain of doctrine choices. A decision category would duplicate the event flow. A focus tree connection would give selected countries extra permanent access that conflicts with the event's global symmetric role.

### Closure decision

The event remains an event-and-doctrine system. The implementation should not add a decision category or focus content merely to increase size.

## Super-event lens

### Finding

Doctrine Research is a minor positive event. Its evolutions increase the number of choices without creating a campaign threshold that deserves major presentation.

### Closure decision

The accepted presentation remains a report-event image and normal country events.

## Improvement-loop review

### Playable promise

The player expects a direct doctrine choice whose value depends on current military development. Evolutions should make the same choice more flexible and more powerful.

### Depth achieved

The specification provides:

- global country participation
- domain-aware Grand Doctrine adoption
- exact one-level mastery advancement
- stacking and distribution
- four evolution stages
- custom doctrine adapters
- Chaos Warfare integration
- AI strategy
- batch queues
- multiplayer and tag-switch behavior
- native banked-mastery handling
- cluster integration
- presentation and assets
- three achievements
- probability scenarios
- catalog alignment
- completion criteria

### Closure finding

Broad expansion should stop here. A new currency, pressure meter, scripted GUI, decision board, faction, country package, focus tree, super-event, or crisis chain would add maintenance and distract from the event's small positive role.

The next work is implementation, graph verification, AI evidence, asset production, localization, documentation, workbook alignment, and final audit.

## Tooling blockers carried forward

The following evidence could not be produced in this runtime:

- live Chaos Redux repository inspection
- offline Paradox wiki consultation
- installed vanilla documentation inspection
- installed vanilla doctrine precedent inspection
- `hoi4.event_inspect`
- `hoi4.event_render`
- `hoi4.event_compare`
- `hoi4.tech_inspect`
- `hoi4.tech_render`
- `hoi4.tech_compare`
- HOI4 MCP probability inspection and comparison
- actual custom subagent handoffs
- authoritative XLSX update
- generated or processed assets
- live game validation

The package does not treat source-only reasoning as equivalent to these checks.

## Simplification statement

The event design was not shortened or converted to a smaller fallback. Every behavior needed by the user's baseline and Evolutions I through IV is specified.

Unresolved items are engine and repository facts that cannot be responsibly invented. They are explicit implementation blockers, not silent omissions.
