# Event 014 Cannibalism Source Specification

This directory is the source-of-truth design and closure record for Event 014, Cannibalism. The event begins as a containable wartime military-predation crisis. Failed containment, exploitation, cross-border spread, and high chaos can produce ritual cells, remote communes, eight reusable warlord countries, the public Hannibal Lecter unification, and ordinary or Wendigo terminal routes.

## Current implemented scale

- Classification: Minor Fire-Once, no cluster.
- Focus trees: 68 local warlord, 108 unified, 28 Wendigo overlay.
- Warlord countries: eight origin-agnostic reusable slots from CBA through CBH, three origin archetypes, and 56 regional HOI4-style portraits with no prison settings.
- AI closure: two country scorers, two decision-weight MTTH entries, six unified targeted-decision consumers, and separate pre-lock/post-lock Wendigo profiles.
- Objective closure: eight maintained mission families and seven added paid action families.
- Wendigo closure: paid-only Pack recruitment, bounded casualty receipts, complete-batch capacity checks, active-enemy epoch reset, inherited winter cells, structural Pack/origin/commander stages, and four terminal-hunt surfaces.
- Achievements: 18 real achievement definitions plus an 18-entry staged read-only tracker.
- Scenario: `SCN-010` with Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence.
- Event Details: two independent post-reveal terminal rows and toggles.
- Presentation: four action super-events, eight 44.1 kHz runtime audio files (four WAV), 21 closure assets, two real-frame leader portrait animations rooted in the exact canonical `hannibal.dds` and `hannibal_wendigo.dds` files, a full 56-portrait regional refresh, and 195 flat image-generated flag files.
- Runtime consolidation: 93 dedicated Event 014 script, GUI, and localisation loader files were reduced to 23 merge-safe files. Those 23 are the practical minimum of one dedicated file per incompatible HOI4 loader schema, including separate `.gfx` and `.gui` schemas. Per-tag country/history files, engine-required flag ladders, binary assets, and shared global registries are structurally separate and are not counted as merged loader fragments.
- Unified decision art: 38 live unified decisions have 38 distinct icons under `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/`, documented by three row-range manifests and three row-range handoffs.
- Unit and equipment art: Event 014 adds no custom subunit or equipment identifiers. It retains the existing battalion and equipment surfaces, so no bespoke unit-counter or equipment art is required. This is a verified scope disposition, not a fallback.
- Current audits: the 2026-07-15 consolidation re-audits for country packages, decisions/missions, focus trees, localisation/assets, spreadsheets, the improvement loop, and documentation report P0/P1/P2/P3 all zero. The pre-lock first-band AI package is an intentional fixed-assignment design followed by a separate one-time post-lock profile, not an open finding.
- Catalog status: `Events!M15` and `Scenarios!F10` are `Fully Functional`.

## Package map

- `specs/` contains the twelve source specification parts.
- `matrices/` contains current focus, decision, AI, country, idea, asset, super-event, world-reaction, state-machine, and secrecy maps.
- `focus_graphs/` contains Mermaid architecture diagrams retained as design history and route orientation.
- `research/` contains historical, cultural, and source-reading records.
- `prompts/` contains the original bounded implementation and audit prompts. They are historical orchestration inputs, not current implementation status.
- `quality/` contains current package status, validation boundaries, and anti-spoiler review.
- `PACKAGE_MANIFEST.md` records current byte, line, and SHA-256 data for the package.

## Source-of-truth and supersession map

Current implementation facts are read in this order:

1. Live gameplay, localisation, GFX, audio, and asset files.
2. The twelve spec parts and current matrices in this directory.
3. `docs/events/014_cannibalism/overview.md` for the canonical mechanic overview.
4. Current asset manifests under `docs/assets/014_cannibalism/`.
5. The current 2026-07-15 consolidation audits under `docs/plans/014_cannibalism_plans/audits/`: `event014_country_package_consolidation_reaudit_2026-07-15.md`, `event014_decision_mission_consolidation_reaudit_2026-07-15.md`, `event014_focus_tree_consolidation_reaudit_2026-07-15.md`, `event014_localisation_asset_consolidation_reaudit_2026-07-15.md`, `event014_spreadsheet_consolidation_reaudit_2026-07-15.md`, `event014_improvement_loop_consolidation_reaudit_2026-07-15.md`, and `event014_documentation_consolidation_reaudit_2026-07-15.md`. The integration/catalog and super-event visual audits remain current companion evidence.

The two accepted improvement addenda remain in `docs/plans/014_cannibalism_plans/improvement_loop/` as implementation history. H-01, H-02, H-03, M-01, the constituent technology union, and the 38 unified decision icons are accepted, implemented, audited, promoted, and closed. Optional ideas A through C in the post-implementation closure addendum remain queued, unaccepted, and nonblocking.

The 2026-07-11 `014_live_asset_gap_map.md` and `014_remaining_static_asset_ledger.md` are superseded production snapshots. They are retained for provenance but no longer describe missing live files. `014_flag_asset_frozen_ledger.md` and `014_gui_dimension_ledger.md` remain frozen contract records whose outputs are accounted for by the current asset manifests.

Historical subagent handoff bodies retain their checkpoint evidence. Explicit supersession banners or current-disposition notes identify the checkpoint audits whose stale counts could otherwise be mistaken for current authority. Current disposition is recorded here, in package status, and in the 2026-07-15 documentation consolidation re-audit.

`event014_final_completion_audit_2026-07-13.md` is a historical pre-origin-removal checkpoint. Its preserved four-origin counts and accepted-P3 wording are not current completion evidence.

## Reveal and cultural boundary

Hannibal Lecter is public only after `cannibalism_reveal_complete`. Before that flag, no player-facing event, evolution row, decision, focus, GUI, Event Details row, achievement tracker row, scenario, portrait, country identity, super-event, or audio presentation may expose his name, face, silhouette, command title, or a claim that one individual directs the network.

No Event 014 surface uses an actor likeness or borrows living Indigenous ceremonial, sacred, tribal, or authenticity framing. The transformed route uses wholly invented Chaos Redux imagery.

## Validation boundary

The current package records definition-level and filesystem validation plus the completed focus, decision, country, localisation, asset, spreadsheet, and final completion audits. It does not equate those checks with an in-game runtime session. Any runtime evidence must be reported separately and must not be inferred from this documentation.
