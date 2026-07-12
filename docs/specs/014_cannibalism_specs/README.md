# Event 014 Cannibalism Source Specification

This directory is the source-of-truth design and closure record for Event 014, Cannibalism. The event begins as a containable wartime military-predation crisis. Failed containment, exploitation, cross-border spread, and high chaos can produce ritual cells, remote communes, eight reusable warlord countries, the public Hannibal Lecter unification, and ordinary or Wendigo terminal routes.

## Current implemented scale

- Classification: Minor Fire-Once, no cluster.
- Focus trees: 72 local warlord, 108 unified, 28 Wendigo overlay.
- Warlord countries: CBA through CBH, four origin archetypes, 56 regional portraits.
- AI closure: two country scorers, two decision-weight MTTH entries, six unified targeted-decision consumers, and separate pre-lock/post-lock Wendigo profiles.
- Objective closure: eight maintained mission families and seven added paid action families.
- Wendigo closure: paid-only Pack recruitment, bounded casualty receipts, complete-batch capacity checks, active-enemy epoch reset, inherited winter cells, structural Pack/origin/commander stages, and four terminal-hunt surfaces.
- Achievements: 18 real achievement definitions plus an 18-entry staged read-only tracker.
- Scenario: `SCN-010` with Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence.
- Event Details: two independent post-reveal terminal rows and toggles.
- Presentation: four action super-events, four unique audio IDs, 21 closure assets, two real-frame leader portraits, and zero missing Event 014 GFX texture paths in the final scan.
- Final supporting audits: country package, localisation/secrecy, and assets/audio are completion-ready at P0/P1/P2/P3 all zero. The focus re-audit has no P0 or P1, with its documentation P2 closed by this reconciliation and its bounded P3 recorded in the AI source docs.
- Final completion: `event014_final_completion_audit_2026-07-13.md` reports completion-ready status with P0, P1, and P2 at zero and one accepted non-blocking P3 for the documented first-assignment pre-lock AI band. `Events!M15` and `Scenarios!F10` are promoted to `Implemented`.

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
3. `docs/events/014_cannibalism.md` for the canonical mechanic overview.
4. Current asset manifests under `docs/assets/014_cannibalism/`.
5. Final audit and remediation handoffs under `docs/plans/014_cannibalism_plans/subagent_handoffs/`.

The two accepted improvement addenda remain in `docs/plans/014_cannibalism_plans/improvement_loop/` as implementation history. Their accepted behavior is promoted into the source specs and matrices. Optional ideas in the first closure addendum remain queued and unaccepted.

The 2026-07-11 `014_live_asset_gap_map.md` and `014_remaining_static_asset_ledger.md` are superseded production snapshots. They are retained for provenance but no longer describe missing live files. `014_flag_asset_frozen_ledger.md` and `014_gui_dimension_ledger.md` remain frozen contract records whose outputs are accounted for by the current asset manifests.

Historical subagent handoffs are not rewritten. Their pending and missing statements describe the checkpoint when each handoff was created. Current disposition is recorded here, in package status, and in the final documentation reconciliation handoff.

## Reveal and cultural boundary

Hannibal Lecter is public only after `cannibalism_reveal_complete`. Before that flag, no player-facing event, evolution row, decision, focus, GUI, Event Details row, achievement tracker row, scenario, portrait, country identity, super-event, or audio presentation may expose his name, face, silhouette, command title, or a claim that one individual directs the network.

No Event 014 surface uses ancient-general, Carthaginian, Punic, actor-likeness, living Indigenous ceremonial, sacred, tribal, or authenticity framing. The transformed route is fictional Chaos Redux content.

## Validation boundary

The current package records definition-level and filesystem validation plus the completed focus, decision, country, localisation, asset, spreadsheet, and final completion audits. It does not equate those checks with an in-game runtime session. Any runtime evidence must be reported separately and must not be inferred from this documentation.
