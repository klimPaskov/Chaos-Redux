# Event 030 Time Traveler Source Specification

This package expands Event 030, Time Traveler, into a complete major-event design. The event begins with one verified traveler and a contest over future knowledge. Later evolutions can produce a political struggle around the traveler, returned figures from the past, visitors from later eras, uncontrolled temporal incidents, a war among possible futures, and the Machine Extinction War.

All names marked as working labels are structural design labels. Implementation must write final localisation after the relevant research and source checks.

## Event identity

- Event ID: `30`
- Entry event: `chaosx.nr30.1`
- Classification: Major
- Chaos level: `1`, Calm World
- Cluster: none
- Baseline public values: Credibility, Exposure, and Timeline Divergence
- Public value count: three
- Evolution I threshold: Gathering Storm, `200+` Chaos
- Evolution II threshold: Rising Chaos, `400+` Chaos
- Evolution III threshold: Chaos Tier, `600+` Chaos
- Evolution IV threshold: Totalen Chaos, `800+` Chaos
- Evolution V threshold: World Collapse, `1000+` Chaos
- Public world-end branch: Machine Extinction War
- Triggerable scenario: proposed `SCN-015`, All Times at Once, pending authoritative workbook collision review

## Central design decisions

The event uses one original traveler. Foreign countries compete for the traveler and copied knowledge. The traveler can change custody, defect, disappear, or die. Copied knowledge remains after loss through a weaker institutional national spirit.

The player actively tracks three values. Hidden sector influence, operation scores, incident severity, visitor reliability, portal pressure, and AI weights remain internal. Evolution V derives Temporal Stability from Timeline Divergence. The interface shows one of those two labels at a time, so it never creates a fourth persistent meter.

The event uses a normal decision category, a strong category picture, and a compact attached display. It does not require a separate full mechanic window. Consultations create timed objectives. Foreign operations use a bounded shortlist and selected-target presentation when needed.

Most returned people remain characters, movements, claimants, commanders, or advisors inside existing countries. A new country package is created only when an actor controls durable territory and can support a real government, army, economy, AI plan, and cleanup path. The Closed Future machine actor meets that standard. Ordinary prehistoric incidents do not create dinosaur countries.

Existing major-country focus trees remain intact. The traveler, returned figures, and future visitors use additive events, decisions, characters, national spirits, and crisis content. The Closed Future receives its own fixed-purpose focus tree because it becomes a durable independent military actor.

## Package map

- `specs/` contains the twelve source specification parts.
- `matrices/` contains the compact implementation maps for values, decisions, figures, incidents, AI, assets, achievements, super-events, integrations, and country packages.
- `focus_graphs/` contains Mermaid architecture diagrams.
- `research/` records historical sources, source-to-design connections, supplied-file reading, and connected-repository inspection.
- `prompts/` contains bounded implementation and audit prompts for the parent agent and project subagents.
- `quality/` records the manual improvement-loop pass, acceptance matrix, anti-bloat review, package status, validation, and tooling limits.
- `030_time_traveler_full_spec.md` concatenates the twelve specification parts for convenient reading.
- `PACKAGE_MANIFEST.md` records byte counts, line counts, and SHA-256 hashes.

## Source and validation boundary

Every supplied Markdown source, catalog CSV, configuration file, and subagent definition was read in full. The connected GitHub repository was searched for Event 30 identifiers and the proposed scenario ID. No indexed implementation was found. The repository was not mounted as a writable local checkout, the offline Paradox wiki and installed vanilla game files were not accessible, and the project-specific HOI4 MCP and custom subagent execution routes were not available in this environment. This package therefore defines design and implementation acceptance criteria. It does not claim source implementation, MCP evidence, asset production, spreadsheet edits, or live-game validation.

No design surface was shortened to save time. Several tempting additions were deliberately rejected because they would create clutter or duplicate existing systems. Those rejections are recorded in `quality/anti_bloat_and_clarity_audit.md`.
