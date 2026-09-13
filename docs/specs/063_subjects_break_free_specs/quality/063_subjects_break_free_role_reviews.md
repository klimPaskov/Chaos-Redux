# Event 063 role reviews

## Review method

Every supplied subagent definition was read in full before this package was drafted. The definitions were then used as separate review lenses over the design. Each review below records the role's applicability, the main question it tested, and the resulting disposition.

The project configuration expects isolated Codex subagents. That execution route was not available in this environment. The outer Codex tool registry and command route were attempted several times and returned MCP tunnel failures with HTTP 404 or 429 responses. The direct sandbox also had no usable Codex executable. No isolated subagent output is claimed.

The role reviews below were performed by the parent process using the complete role definitions as structured checklists. They improve coverage, but they are not a substitute for the independent subagent and HOI4 MCP passes required during implementation.

## Role applicability matrix

| Role definition | Applicability | Review result |
| --- | --- | --- |
| `chaosx_repo_explorer` | High | Mapped all supplied source files, every catalog row, Event 006 ownership, Soviet Collapse provenance, the Liberation Release Coordinator, cluster records, and the closest event overlaps. |
| `chaosx_improvement_loop_planner` | High | Expanded the rough release effect into a bounded settlement and cooperation system, then stopped broad expansion once each promised gameplay question had a complete answer. |
| `chaosx_scripted_system_architect` | High | Reviewed the frozen candidate transaction, reservation ownership, shared liberation-origin contract, settlement state, Pact state, cleanup, and idempotence requirements. |
| `chaosx_decision_mission_auditor` | High | Reviewed action quality, real costs, mission purpose, visibility phases, active mission limits, target cleanup, exploit resistance, and AI equivalents. |
| `chaosx_ai_probability_auditor` | High | Defined named scenarios for release count, candidate selection, settlement postures, cohort selection, intervention, Congress timing, and Pact behavior. Actual MCP probability inspection remains an implementation gate. |
| `chaosx_event_ui_worker` | Medium | Tested whether a dedicated mechanic window was justified. It was not. One normal decision category with a static category picture and compact Cohesion presentation is clearer and cheaper to maintain. |
| `chaosx_localisation_auditor` | High | Reviewed dynamic actor coverage, information boundaries, tone directions, working-label warnings, and the need to keep exact effects in tooltips. Event-detail prose should not carry full effect lists. Final localisation remains implementation-owned. |
| `chaosx_documentation_curator` | High | Split the design into six source specs, added a package index, source inventory, overlap handoff, research notes, diagrams, prompts, and acceptance material. |
| `chaosx_event_completion_auditor` | High | Checked the rough brief against the package and produced the acceptance matrix. The package covers baseline release, all three evolutions, cooperation, Pact rules, AI, decisions, assets, achievements, clusters, connections, and failure handling. |
| `chaosx_spreadsheet_doc_worker` | Medium | Reviewed all exported catalog rows and prepared a workbook handoff. The export-only CSV files were not edited. The authoritative XLSX must be updated after implementation facts and final localisation exist. |
| `chaosx_asset_source_researcher` | Medium | Reviewed which planned images may use historical material and which should use generated documentary-style art. Actual source selection belongs to implementation asset work. |
| `chaosx_generated_event_art` | Medium | Reviewed the report image, three news images, category picture, and faction-emblem directions. No final art was produced during specification work. |
| `chaosx_icon_artist` | Medium | Reviewed separate icon families for decisions, missions, ideas, the Pact, and achievements. The asset prompt forbids satisfying one family by resizing another. |
| `chaosx_country_package_auditor` | Medium | Confirmed that selected subjects are existing countries whose complete campaign state must be preserved. No new generic country package or replacement tag is justified. |
| `chaosx_focus_tree_auditor` | Low | Checked whether Event 063 requires new focus trees. Existing subjects keep their loaded focus trees. Long-term event play belongs in decisions, diplomacy, and the Pact. |
| `chaosx_3d_model_pipeline` | None | The design adds no visible unit, vehicle, creature, building entity, aircraft, or ship that needs a custom 3D package. |
| `chaosx_portrait_creator` | None | The design preserves existing leaders and adds no new portrait-owned character. |
| `chaosx_super_event_text_researcher` | None | The event remains a medium repeatable incident. Its visible milestones use report and news surfaces. |
| `chaosx_super_event_audio_researcher` | None | No super-event audio package is part of the accepted design. |
| `chaosx_skill_maintainer` | Low | The task did not reveal a reusable workflow gap that requires changing a project skill. The resulting design can be implemented under the existing event, decision, asset, subagent, and improvement-loop skills. |

## Repository and ownership review

The event keeps a narrow owner boundary.

- Event 063 owns selection among countries that already exist as subjects, removal of their subject relation, the opening settlement, its own cooldowns, and its Event 063 history.
- Event 006 keeps ownership of Independence Wave country creation, territory allocation, its carrier packages, and its private provenance ledger.
- Event 005 keeps ownership of Soviet Collapse successor creation and its collapse-specific political structures.
- The shared layer records only neutral liberation-origin and cooperation facts that more than one owner needs.
- The Liberation Release Coordinator remains the collision authority when release transactions overlap.
- Event 144, Freedom or Death, remains a distinct future mass declaration and National Liberation Front crisis. Event 063 does not consume that concept.

This boundary prevents a convenient shared helper from becoming a second release engine.

## Scripted-system review

The frozen transaction model passed the design review because it solves the main ordering risks.

- The valid pool is frozen before any release.
- Selection is without replacement.
- Full reservations are attempted before the first status change.
- Frozen fallbacks can replace failed reservations before execution begins.
- A late failure after the first completed release reduces the final batch instead of rebuilding the pool.
- Origin registration is idempotent and stores first and latest origins separately.
- Pending human settlements persist without repeating independence after save and reload.
- Cleanup removes reservations, temporary arrays, stale claims, invalid support offers, and obsolete missions.

The shared origin contract should expose facts and bounded helper calls. It should not inspect or mutate Event 006 and Event 005 private state except through owner-provided public adapters.

## Decision and mission review

The proposed decision layer passed the anti-store and anti-clutter checks.

- One category changes by phase instead of exposing every action at once.
- A normal phase shows three to five primary actions, with six as the hard maximum.
- One to three missions may be active.
- Costs use political, military, industrial, logistical, or diplomatic resources that match the action.
- Equipment aid transfers real stockpiles and cannot create equipment from nothing.
- Recognition, defense, and Congress missions require action over time.
- Targeted actions close when the target, former overlord, war, Pact status, or settlement becomes invalid.
- The AI receives equivalent scripted action paths and does not need to click a human interface.

The design intentionally avoids a permanent button that directly frees any chosen foreign subject. Such an action would bypass event selection, collapse the repeatable event's identity, and invite target farming.

## Probability review

The probability scenarios define expected ordering before exact weights are chosen.

- Higher autonomy, stronger domestic capacity, weaker overlords, active war pressure, hostile relations, liberation support, and recent same-overlord breakaways should increase candidate weight.
- Very loyal or integrated subjects retain a small floor, but should remain rare at low Chaos.
- Negotiated separation should dominate when relations are good and the overlord is pragmatic.
- Armed refusal should rise with strategic value, hostile claims, authoritarian posture, military confidence, and several coordinated losses.
- Evolution I should create one meaningful same-overlord cohort without allowing one empire to consume every release slot.
- Evolution II should cap new direct war theaters and direct interveners while allowing wider indirect support.
- Congress and Pact formation should depend on compatible membership, origin diversity, threat, recognition, and existing network strength.

The implementation prompt requires `hoi4.probability_inspect` first, named scenario evaluation, sweeps for sensitive factors, and a final compare after tuning. The package does not claim exact probabilities from a catalog-only environment.

## AI review

The AI model is separated by role.

- Subject AI evaluates declaration posture through autonomy, survival capacity, foreign support, political identity, public mandate, and expected retaliation.
- Former-overlord AI evaluates recognition, pressure, concession, or war through strength, war load, ideology, claims, strategic dependence, and the size of the coordinated loss.
- Liberated-state AI evaluates recognition, guarantees, aid, intervention, and Pact membership through compatibility, route access, stockpiles, common threats, and escalation risk.
- Pact AI evaluates admission, leadership, collective response, censure, suspension, expulsion, and dissolution through Cohesion and member conduct.

Human choices do not grant immunity from the event. A selected human subject becomes independent and chooses its posture. A selected human overlord chooses its response. Human-human settlement uses a bounded deadline and a safe default so multiplayer cannot stall the world transaction.

## Presentation review

One public persistent value is sufficient.

`Liberation Cohesion` communicates whether the Pact can act together. Candidate weight, relationship compatibility, former-overlord pressure, network trust, and intervention willingness remain hidden calculations. Their material causes are summarized in tooltips and status text.

A dedicated scripted GUI was rejected because the player does not need several interacting public values, state pieces, or repeated board interaction. A static decision-category picture gives the system identity without fake controls. Normal decisions, missions, event reports, country diplomacy, faction information, and concise tooltips carry the playable state.

## Asset review

The asset inventory remains tied to actual consumers.

- one main report image
- three one-time news images
- one decision-category icon
- one static decision-category picture
- distinct decision and mission icon families
- distinct temporary-idea and Pact-state icon families
- one Liberation Pact faction emblem
- four achievement state triplets

No final asset is authorized to be a resized copy of a different asset type. Generated alpha-backed icons and emblems require native transparent backgrounds. Documentary report and news art use their complete painted canvases. Every runtime asset needs a source, manifest row, final DDS path, sprite handoff, and consumer.

## Improvement-loop closure

The improvement pass accepted the following additions because each changes play:

- a frozen multi-country release transaction
- a four-mode settlement matrix
- human posture choices that cannot cancel a selected liberation
- same-overlord coordinated breakaways
- compound independence wars with bounded intervention
- a shared liberation-origin and cooperation contract
- informal recognition, aid, guarantees, and support for later movements
- a formal Pact with membership rules, leadership, collective response, discipline, and dissolution
- one public Cohesion value
- meaningful missions, achievements, AI roles, and persistent diplomatic memory

The pass rejected further broad expansion because it would add maintenance without resolving another core promise:

- several public meters for legitimacy, recognition, threat, and support
- event-created generic country packages for already existing subjects
- replacement focus trees for countries that already have national content
- a dedicated event window
- automatic removal of countries from unrelated factions merely to fill the Pact
- unlimited global intervention in every independence war
- blanket claims on all former imperial territory
- automatic annexation goals for former overlords

The design loop can stop at this point. Further useful work belongs to implementation, tuning, asset production, localisation, catalog alignment, and validation.

## Completion review

The specification package answers every part of the supplied rough brief:

- several valid subjects can be released in one firing
- release count scales with the live subject pool
- selected countries retain their complete normal country state
- separations can be peaceful, hostile, contested, or violent
- Event 063 and Independence Wave countries can recognize and support each other
- same-overlord coordination exists at Evolution I
- compound independence wars and intervention exist at Evolution II
- a formal cross-origin Liberation Pact exists at Evolution III
- compatible Soviet Collapse successors can participate
- event and cluster ownership boundaries are defined
- AI, multiplayer, cleanup, exploit resistance, presentation, assets, achievements, probability scenarios, and acceptance cases are specified

One catalog issue remains for implementation review. The supplied cluster export contains Liberations as Cluster ID 2, but it contains no Domestic Unrest cluster. The requested secondary classification is preserved without inventing an ID. The authoritative workbook must decide whether Domestic Unrest is a future cluster, a descriptive tag, or a catalog correction.

## Implementation evidence still required

The following are implementation gates, not missing planning content:

- inspect the live repository and exact Event 006 public ledger adapters
- consult the required offline wiki and installed vanilla documentation before script changes
- use HOI4 MCP event and probability tools on the implemented source
- run the mandatory audit, patch, and probability-compare cycle for all weighted logic
- produce and review final assets through the assigned asset workers
- write and audit final localisation
- update the authoritative XLSX and regenerate the three CSV exports
- validate event logs, Event Details, cluster behavior, multiplayer settlement, save and reload, and all acceptance scenarios in the finished implementation

## Review verdict

The planning package is complete at specification level. No intentional simplification or truncation was used. Independent subagent execution did not occur because the configured execution route failed, so the implementation goal prompt explicitly retains the requirement to run the actual isolated project subagents when that runtime is available.
