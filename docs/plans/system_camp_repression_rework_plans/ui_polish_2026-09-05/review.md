# Repression GUI presentation review

Disposition: superseded by `completion_review.md` after the user authorized direct source application and selected-site cost repairs.
The blocked writer results and preservation claims below are historical evidence for the first scalar-only attempt, not the current implementation status.
The shared scripted GUI skill package was committed as `86b6ff4045abce6027b50b9c6bf5d46dc280a839`.

## Authorization and ownership

The user requested a dedicated `chaos-redux-scripted-gui` skill, mandatory reference images before native GUI implementation, and thorough visual/usability repairs using the HOI4 MCP.
The user narrowed runtime work to small changes, explicitly prohibited touching core Chaos Redux systems, and offered the repression GUI as an example.
The parent selected presentation-only repairs to `interface/camp_repression_ledger.gui` within that authorization.
Events 14–39 were offered as optional review scope and were not expanded into this repair.
No shared event log, event details, settings, super-event framework, gameplay effects, AI, costs, or localisation was edited for this work.

## Accepted reference and native mapping

The parent accepts [reference.png](reference.png) as the intended direction for this narrow repair based on the user's express instruction to create reference images and fix uneven presentation.
The [reference note](reference_note.md) records the ImageGen prompt, original screenshot, generated image, hashes, and processing.
The reference precedes the proposed native source changes and is review art, not a runtime texture.

| Reference region | Native consumer | Proposed implementation and adaptation |
| --- | --- | --- |
| Title and navigation column | `camp_ui_title`, `camp_ui_institution`, five `camp_ui_nav_*` labels and existing tab controls | Align heading left edges; center rendered navigation labels on both axes inside the existing 160×44 controls. |
| Middle operating-sites browser | `repression_ledger_locations_panel`, `camp_ui_site_list`, native row selection and scrolling | Preserve real dynamic rows, selected-state overlays, two-line name allowance, and existing input behavior. |
| Selected-location card | `camp_ui_selected_location` | Align its top/bottom with the main 460-pixel content region while preserving the selected name and contextual status. |
| Two-column action grid | Existing `camp_gui_*` action buttons and `camp_ui_cost_*` labels | Equal 20-pixel side insets, 148-pixel columns, clear action/cost grouping, and taller two-line cost bounds. |
| Other native pages using the same visual family | Situation paired cards and four policy directive cards | Equal paired card widths; center each policy button and its cost text in its own card. |

Generated lettering, resource glyphs, proportions, and button styling are guidance only.
The native proposal retains installed HOI4 sprites, fonts, live localisation, tooltips, controls, lists, visibility, selection, and effect bindings.
No generated fake control, flattened dynamic value, new asset, or unsupported styling property is introduced.

## Measured findings and reviewed proposal

The [baseline](baseline.png) and [MCP proposed render](proposed.png) show the same `sites_all_orders` fixture at 1920×1080 and UI scale 1.
The exact 59 scalar edits are preserved in [reviewed_layout.patch](reviewed_layout.patch) and the original MCP [rewrite request](reviewed_rewrite_request.json).

| Finding | Baseline | Reviewed correction |
| --- | --- | --- |
| Navigation label centering | Horizontal glyph-center offsets approximately −39, −35, −52, −48, and −22.5 pixels; vertical offset −1 pixel | Center text horizontally and move its baseline down one pixel; MCP proposed centering assertions report no mismatch. |
| Two-line action costs | Measured 38.4-pixel text in 34-pixel bounds | Use 40-pixel bounds; proposed `GUI_TEXT_OVERFLOW` check reports none. |
| Right action-column padding | Cost labels extend to x392 inside a 396-pixel card, leaving 4 pixels on the right | Give both columns 148-pixel bounds and 20-pixel outer insets. |
| Action-row separation | Compact rows leave insufficient vertical room for longer costs | Increase row pitch to 84 pixels while keeping each cost below its own native button. |
| Main-content symmetry | Selected card starts below adjacent content; paired Situation cards differ by 4 pixels | Align the selected card to the 460-pixel content region and use equal 348-pixel Situation cards. |
| Policy-card alignment | 238-pixel buttons at x16 inside 348-pixel cards | Center buttons at x55 and center cost text within the existing padded card bounds. |

Source identity before the attempted write: SHA-256 `2fe2666127b854ca07343ec2b466fdbb7e72ff2cead6f45810cbd761ba76d13c`.
Proposed source identity: SHA-256 `8975874f8cd9c2d0d50b4036742c16f4ece96b69ad9e33ce6e9ebc607c58b601`.
The runtime file was restored to the former hash after MCP rollback.

## MCP evidence and blocker

Production service: installed `hoi4-agent-tools` 3.0.7, workspace `mod_chaos_redux_ea3b2d67c2c0`, actual mod root and installed vanilla game root.
The parent read the required offline wiki material, installed scripted GUI documentation, relevant vanilla documentation, and a native campaign GUI precedent.
The production baseline inspection and render are preserved under [before](before/), with exact source/scenario identities rather than choosing a concurrent task's newest image.
The baseline render covers five pages, empty sites, a long-name/locked case, and bottom-of-list scrolling at 1920×1080 scale 1, 1280×720 scale 1, and 1920×1080 scale 1.25.
The generic selected-state variant activates mutually exclusive tabs and is an invalid fixture; it is not accepted as a runtime state or a GUI defect.
Final-state requests must use explicit per-control states and retain the matching normal/hover/disabled cases.
The reviewed fixtures are recorded in [scenarios.json](scenarios.json).

The app's 180-second rewrite timeout was retried through the same installed MCP service with its supported progress heartbeat handling, without changing project configuration or replacing the production renderer.
The first completed exact-patch attempt returned `REWRITE_SOURCE_STALE` because three event 16 dependency files changed during preparation; the repression GUI source itself retained its expected hash.
The refreshed attempt produced the intended image and applied the proposed bytes, then returned `REWRITE_POST_VALIDATION_FAILED` and restored the original file.
Its failed checks are `post-write-shared-index` and `post-write-gui-graph`.
Post-write indexing reports unresolved native sprite references including `GFX_button_148x34`, `GFX_button_238x38`, and `GFX_closebutton`, plus a truncated global GUI diagnostic set.
These exact sprites appear in the production proposed render; that observation does not waive the writer's failed verification or establish a completed runtime repair.

The complete responses are [first result](rewrite_result.json) and [retry result](rewrite_retry_result.json).
The retry's images, visual difference, fidelity, proposal validation, execution validation, and post-write diagnostics are preserved under [rewrite_retry_artifacts](rewrite_retry_artifacts/).
No MCP validation was bypassed, no renderer defect was dismissed, and no source-only check is presented as equivalent completion evidence.
The runtime repair remains unapplied while the user decides whether to authorize direct application of the reviewed patch followed by production MCP inspection and full state/resolution renders.
The independent [interaction audit](interaction_audit.md) confirms that the scalar proposal preserves control identities, click-through layers, list reachability, action/cost bindings, and gameplay scope; it records the outstanding final-state checks.

## Skill package and remaining work

Created `chaos-redux-scripted-gui` and its detailed visual-review checklist; redirected the decisions/missions, events, event-planning, event-assets, and subagent workflows; updated repository/MCP routing and both relevant canonical agent prompts.
Generated Qoder and Cursor counterparts were synchronized using the repository's official sync functions/scripts.
The parent reviewed the skill and its native mapping, centering, bounds, state, background, interaction, scenario, and completion rules; the official skill validator and TOML parsing accepted the package.
The task-only commit preserves unrelated staged work, including pre-existing staged hunks inside shared skill files.
See [shared skill handoff](../../shared_scripted_gui_skill_handoff.md) for the exact ownership and authored routing changes.

Skills used: `skill-creator`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `imagegen`, and the created `chaos-redux-scripted-gui`; the skill maintainer also consulted event and planning routing guidance.

## Simplifications, omissions, and blockers

No requested skill rule was omitted.
The repression GUI repair is incomplete because the mandatory writer rolled it back; the proposed image is not an installed result.
Final post-change page/state/resolution renders, click-region review, and runtime-source completion cannot be claimed while application remains blocked.
No fallback has been applied.
Live game execution was not performed.
