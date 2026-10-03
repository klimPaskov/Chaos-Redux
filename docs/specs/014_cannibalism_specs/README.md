# Event 014 Cannibalism Source Specification

This directory holds the source design and scoped implementation evidence for Event 014, Cannibalism. The event begins as a containable wartime military-predation crisis. Failed containment, exploitation, cross-border spread, and high chaos can produce ritual cells, remote communes, eight reusable warlord countries, the public Hannibal Lecter unification, and ordinary or Wendigo terminal routes.

The current parent instruction for this reconciliation explicitly preserves 56 distinct regional HOI4-style finals as accepted and unfinished, seven bespoke models across nine gameplay families, approved cavalry/infantry visual reuse, and no animation toggle. The [2026-10-03 continuation report](../../plans/014_cannibalism_plans/2026-10-03_continuation_report.md) and [resume packet](../../plans/014_cannibalism_plans/resume_packet.md) are the current implementation checkpoint, not full completion proof. Archive recovery is committed as `f440c5329` and accepted only at the source-archive boundary.

## Recorded implementation scale and open requirements

- Classification: Minor Fire-Once, no cluster.
- Focus trees: 68 local warlord, 108 unified, 28 Wendigo overlay.
- Warlord countries: eight origin-agnostic reusable slots from CBA through CBH and three origin archetypes. The accepted portrait design requires 56 distinct regional HOI4-style finals with no prison settings; current final coverage remains unfinished.
- AI source surfaces: two country scorers, two decision-weight MTTH entries, six unified targeted-decision consumers, and separate pre-lock/post-lock Wendigo profiles. Current scenario-specific engine evidence remains incomplete.
- Objective closure: eight maintained mission families and seven added paid action families.
- Wendigo closure: paid-only Pack recruitment, bounded casualty receipts, complete-batch capacity checks, active-enemy epoch reset, inherited winter cells, structural Pack/origin/commander stages, and four terminal-hunt surfaces.
- Achievements: 18 real achievement definitions plus an 18-entry staged read-only tracker.
- Scenario: `SCN-010` with Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence.
- Event Details: two independent post-reveal terminal rows and toggles.
- Presentation: four action super-events, eight unique 44.1 kHz super-event source/runtime audio files (four runtime WAVs), 21 closure assets, two protected leader portrait sheets rooted in the exact canonical `hannibal.dds` and `hannibal_wendigo.dds` files, and 195 flat image-generated flag files. The current 64 warlord sprite aliases reference 56 distinct existing regional DDS textures. Recovered archive coverage is the 16 HATE source packages H01-H16; archive status for the remaining 40 is unknown pending the portrait audit. These are not accepted HOI4-style finals.
- Runtime consolidation: 93 dedicated Event 014 script, GUI, and localisation loader files were reduced to 23 merge-safe files. Those 23 are the practical minimum of one dedicated file per incompatible HOI4 loader schema, including separate `.gfx` and `.gui` schemas. Per-tag country/history files, engine-required flag ladders, binary assets, and shared global registries are structurally separate and are not counted as merged loader fragments.
- Unified decision art: 38 live unified decisions have 38 distinct icons under `docs/assets/014_cannibalism/static_icons_imagegen/unified_decisions/`, documented by three row-range manifests and three row-range handoffs.
- Unit gameplay and model consumers: Event 014 defines nine inactive custom irregular-infantry/cavalry sub-units with stable gameplay identities, locked-template consumers, and an additive CXT registration bus. It adds no equipment archetype and reuses ordinary infantry, support, artillery, and motorized equipment. The locked Scavenged Elephant Column uses installed vanilla `elephantry` and its real infantry- and artillery-equipment need without adding a custom elephant token. The 27 counter DDS files and registry consumers are present. Seven families have parent-installed bespoke model/entity/action/material/audio packages. Bone Riders intentionally reuses vanilla `sprite = cavalry`, and Network Cadre intentionally reuses vanilla `sprite = infantry`; neither requires an Event 014 custom model, action, entity, or provider package.
- Current audits: the 2026-07-15 consolidation re-audits for country packages, decisions/missions, focus trees, localisation/assets, spreadsheets, the improvement loop, and documentation report P0/P1/P2/P3 all zero for their frozen scope. The current downstream model, GUI, portrait-handoff, weighted-logic, and parent live-consumer reaudits remain partial or blocked. The pre-lock first-band AI package is an intentional fixed-assignment design followed by a separate one-time post-lock profile, not an open finding in that frozen scope.
- Catalog status: `Events!N15` and `Scenarios!F10` are `Needs Testing` while parent live-consumer validation and the other documented evidence gates remain open.
- Portrait status: the [current portrait-worker receipt](../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_event014_portrait_receipt_repair.md) and protected static Hannibal file/binding receipt exist. The [archive recovery handoff](../../plans/014_cannibalism_plans/subagent_handoffs/2026-10-03_portrait_source_archive_recovery.md) and [parent review](../../plans/014_cannibalism_plans/evidence/2026-10-03_portrait_archive_parent_review.json) verify all 16 originals, lossless crops and 156x210 candidates against historical hashes, with exact crop/source and candidate/installed-DDS pixel equality, 121 archive file hashes and 62 protected runtime/definition hashes. Reproducible co-located source commands are restored for these 16 packages. Rights, 56 distinct HOI4-style finals, visual/live acceptance and external static Hannibal provenance remain open; H06 retains its opaque white field. The retained user-authorized direct-source branch is not rejected solely for lacking the default fictional ImageGen route.

The 2026-08-22 unit/model amendment supersedes any earlier “no unit-counter” or “no downstream blocker” wording for this tranche. Current model inputs must begin from actual Internet-sourced or user-supplied modern artwork and may receive only faithful ImageGen enhancement; generated-from-scratch or redesigned descendants are rejected. Feast Guard’s current source record is `docs/assets/014_cannibalism/models_3d/cannibal_feast_guard/refs/source/untouched.png` with faithful input SHA-256 `C67AF852A27E1379590BD84C5175C378D449AE226F895A2D326B45099040D8C9`.

Feast Cohort's selected `11014` mesh and eight actions match installed bytes in the current checkpoint receipt. Changing Feast Guard export recovery and five missing model-manifest links remain parent-owned; follow the continuation report and its subsequent parent-reviewed handoffs rather than infer restored source fields or new manifests here.

## Package map

- `specs/` contains the twelve source specification parts.
- `matrices/` contains current focus, decision, AI, country, idea, asset, super-event, world-reaction, state-machine, and secrecy maps.
- `focus_graphs/` contains Mermaid architecture diagrams retained as design history and route orientation.
- `research/` contains historical, cultural, and source-reading records.
- `prompts/` contains the original bounded implementation and audit prompts. They are historical orchestration inputs, not current implementation status.
- `quality/` contains current package status, validation boundaries, and anti-spoiler review.
- `PACKAGE_MANIFEST.md` is a recorded package byte/line/hash checkpoint; the parent must refresh it after integrating this documentation patch before calling its hashes current.

## Source-of-truth and supersession map

Accepted design comes from explicit user decisions or parent acceptance within the authorized scope, with the twelve spec parts recording the intended design. File location, date, a status label or implementation does not establish approval. Current implementation facts are read in this order:

1. Live gameplay, localisation, GFX, audio, and asset files.
2. The current continuation report, resume packet and narrowly accepted receipts, including the portrait archive parent review.
3. `docs/events/014_cannibalism/overview.md` for the canonical mechanic overview.
4. Current asset manifests under `docs/assets/014_cannibalism/`.
5. The 2026-07-15 consolidation audits under `docs/plans/014_cannibalism_plans/audits/`: `event014_country_package_consolidation_reaudit_2026-07-15.md`, `event014_decision_mission_consolidation_reaudit_2026-07-15.md`, `event014_focus_tree_consolidation_reaudit_2026-07-15.md`, `event014_localisation_asset_consolidation_reaudit_2026-07-15.md`, `event014_spreadsheet_consolidation_reaudit_2026-07-15.md`, `event014_improvement_loop_consolidation_reaudit_2026-07-15.md`, and `event014_documentation_consolidation_reaudit_2026-07-15.md`. All July zero-finding audits are historical evidence for frozen tranches, not current full-package proof. Later integration/catalog and super-event audits retain their own dated scopes and limits.

The two improvement addenda remain in `docs/plans/014_cannibalism_plans/improvement_loop/` as recorded implementation history. Their historical dispositions report H-01, H-02, H-03, M-01, the constituent technology union and the 38 unified decision icons as implemented/promoted within that frozen scope; this receipt reconciliation does not establish fresh design acceptance or current full validation. Optional ideas A through C remain unresolved, unaccepted proposals rather than an accepted implementation queue.

The 2026-07-11 `014_live_asset_gap_map.md` and `014_remaining_static_asset_ledger.md` are superseded production snapshots. They are retained for provenance but no longer describe missing live files. `014_flag_asset_frozen_ledger.md` and `014_gui_dimension_ledger.md` remain frozen contract records whose outputs are accounted for by the current asset manifests.

Historical subagent handoff bodies retain their checkpoint evidence. Explicit supersession banners or current-disposition notes identify the checkpoint audits whose stale counts could otherwise be mistaken for current authority. Current disposition is recorded here, in package status and in the current continuation checkpoint; the 2026-07-15 documentation consolidation re-audit retains its historical scope.

`event014_final_completion_audit_2026-07-13.md` is a historical pre-origin-removal checkpoint. Its preserved four-origin counts and accepted-P3 wording are not current completion evidence.

## Reveal and cultural boundary

Hannibal Lecter is public only after `cannibalism_reveal_complete`. Before that flag, no player-facing event, evolution row, decision, focus, GUI, Event Details row, achievement tracker row, scenario, portrait, country identity, super-event, or audio presentation may expose his name, face, silhouette, command title, or a claim that one individual directs the network.

The accepted design forbids actor likenesses and living Indigenous ceremonial, sacred, tribal or authenticity framing; current full visual acceptance remains open. The transformed route uses wholly invented Chaos Redux imagery.

## Validation boundary

The package records definition-level and filesystem evidence and scoped historical audits. Current event/helper comparison, attributable GUI state/resolution/hierarchy/click-region comparison, probability scenarios, rights/final portrait coverage and user-owned live consumer acceptance remain incomplete. The curator's current read-only event, focus, GUI and technology calls returned `MCP tool hoi4_agent_tools/hoi4.<route> is not available to the model` despite metadata exposure; no service health or standalone viewer availability is established by that exposure. The probability specialist's scenario-specific handoff remains the owning evidence. No current full-package or in-game completion is inferred.

The current `interface/014_cannibalism.gfx` mapping has 64 warlord aliases referencing 56 distinct existing texture paths, confirmed by the curator and the parent's independent regex scan. Exact archive recovery covers the 16 HATE packages H01-H16 only; archive status for the remaining 40 regional textures is unknown pending the parent-owned portrait audit. Actual subject gender/human identity/framing, source approval and final-art acceptance remain unresolved. Neither path coverage nor the August source-gate `PASS` claim approves all 56 sources, finals or a new generation route.
