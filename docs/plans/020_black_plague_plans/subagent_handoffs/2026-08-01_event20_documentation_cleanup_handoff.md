# Event 020 documentation cleanup handoff

Date: 2026-08-01

## Scope and result

This cleanup reconciles the consequence/aftermath addendum and core-readiness report with the current Event 020 worktree evidence for the RTA hierarchy, RTX route crises, Crown Strike, Rat King defeat aftermath, two-tag boundary, no-model boundary, and super-event 87 runtime gate.

Only documentation surfaces were changed.
No gameplay, localisation, GFX, audio, image, model, spreadsheet, or export-only CSV file was edited.
No Git commit was created because the parent did not request one.

## Second reconciliation (2026-08-01)

The parent-owned completion tranche is now documented as implemented static evidence for the scoped defeat hooks, participant registry, duration/peak/deaths/major-participant gate, resolver-owned reconstruction `.72`, and slot-087 art/text/audio/sprite/sound wiring.

| Surface | Promoted evidence | Current disposition |
| --- | --- | --- |
| Scoped defeat actor hooks | `common/on_actions/020_black_plague_on_actions.txt` plus `black_plague_rat_record_defeat_participant` and `black_plague_rat_king_resolve_defeat` in `common/scripted_effects/020_black_plague_rat_effects.txt` | Implemented narrow capitulation/state-control participant capture; `.73` still selects the first eligible human response host rather than the saved actor. |
| Duration and peak gate | `common/scripted_triggers/020_black_plague_rat_triggers.txt`, `common/script_constants/020_black_plague_constants.txt`, `common/script_constants/020_black_plague_evolution_constants.txt`, and runtime metric updates in the Rat/evolution effects | Implemented statically with current values 180 days, 250,000,000 deaths, 24 peak controlled states, 12 peak continent states at ratio 0.50, and 3 major participants. |
| Reconstruction coupling | Resolver in `common/scripted_effects/020_black_plague_rat_effects.txt` dispatches `.72` once after `.71` when the same eligibility gate passes | Implemented as an eligible-defeat dispatch; later `.74` sealing remains separate and no live proof exists. |
| Slot 087 presentation | `interface/020_black_plague_super_events.gfx`, `localisation/english/020_black_plague_super_events_l_english.yml`, `sound/chaosx_sound.asset`, `music/chaosx_music_track_list.html`, and the final art/audio/text handoffs | Implemented static wiring for sprite `GFX_super_event_087_rat_king_defeat_aftermath`, localisation `.87`, and audio ID 103; release rights record and live validation remain. |

## Files changed

- `docs/plans/020_black_plague_plans/2026-08-01_event20_consequence_and_aftermath_addendum.md`
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`
- `docs/plans/020_black_plague_plans/2026-08-01_event20_content_tranche_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_documentation_cleanup_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_completion_audit.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_live_wiring_completion_audit_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_decision_mission_incremental_audit.md`
- `docs/events/020_black_plague/overview.md`
- `docs/events/020_black_plague/shared_response.md`
- `docs/specs/020_black_plague_specs/README.md`
- `docs/specs/020_black_plague_specs/review/source_of_truth_and_plan_disposition.md`
- `docs/specs/020_black_plague_specs/matrices/event_chain_map.md`
- `docs/specs/020_black_plague_specs/matrices/decision_mission_matrix.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_coding_prompt.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_goal_prompt.md`
- `docs/specs/020_black_plague_specs/prompts/black_plague_decision_mission_prompt.md`
- `docs/assets/020_black_plague/event_art/manifest.md`
- `docs/assets/020_black_plague/rat_identity_asset_manifest.md`
- `docs/assets/020_black_plague/audio_manifest.md`
- `docs/assets/020_black_plague/super_event_087_manifest.md`
- `docs/assets/020_black_plague/super_event_087_gfx_handoff.md`
- `docs/specs/020_black_plague_specs/review/limitations_and_blockers.md`
- `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_7_world_end_and_aftermath.md`
- `docs/super_events/020_black_plague/research.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_super_event_087_art_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_super_event_087_text_research_handoff.md`
- `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_rat_king_defeat_aftermath_audio_handoff.md`

The asset manifests are ignored by the current Git status but are updated in the shared workspace and remain part of this documentation handoff.

## Source-of-truth map

| Surface | Current source | Disposition |
| --- | --- | --- |
| Country identity and scenario rule | `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md` and `docs/specs/020_black_plague_specs/README.md` | Accepted source: `RTA` is the sole reusable Rat Nation carrier, `RTX` is the separate Rat King, and internal broods are state markers. |
| RTA hierarchy route | `common/national_focus/020_black_plague_rat_focus_tree.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_triggers/020_black_plague_rat_triggers.txt`, `common/ai_strategy/020_black_plague_rat_ai_strategy.txt`, `common/decisions/020_black_plague_rat_decisions.txt` | Static implementation evidence: roots, follow-ups, `.45` acknowledgement, hierarchy consumers, route-aware AI, and three continuing route actions are present; dedicated icons and live validation remain open. |
| RTX crises and Crown Strike | `events/020_black_death.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_effects/020_black_plague_shared_response_effects.txt`, `common/decisions/020_black_plague_shared_response_decisions.txt` | Static implementation evidence: `.57-.59`, `.64-.65`, route consumers, costs, and reports are present. Crown Strike and Seal Royal Burrows use shared timed state actions rather than native mission fields. |
| Rat King defeat aftermath | `common/on_actions/020_black_plague_on_actions.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_triggers/020_black_plague_rat_triggers.txt`, `common/script_constants/020_black_plague_constants.txt`, `events/020_black_death.txt`, `common/decisions/020_black_plague_shared_response_decisions.txt` | Implemented static scoped hooks, participant registry, duration/peak/deaths/major-participant gate, idempotent `.71`, eligible `.72`, gated 087, `.73-.75`, and sealing action. `.73` audience fallback, broader aftermath depth, and live proof remain open. |
| Event-chain and decision coverage | `docs/specs/020_black_plague_specs/matrices/event_chain_map.md`, `docs/specs/020_black_plague_specs/matrices/decision_mission_matrix.md`, `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_7_world_end_and_aftermath.md` | Current matrix/spec evidence records `.45`, `.57-.59`, `.64-.65`, resolver-owned `.72`, and `.71/.73-.75`; native mission fields, broader chain depth, and live proof remain open. |
| Current narrative overview | `docs/events/020_black_plague/overview.md`, `docs/events/020_black_plague/shared_response.md`, `docs/events/020_black_plague/rat_route_modules.md` | Current implementation-facing docs; shared-response future-work wording was corrected. |
| Addendum and readiness baseline | `docs/plans/020_black_plague_plans/2026-08-01_event20_consequence_and_aftermath_addendum.md`, `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md` | Reconciled working records with explicit implemented, partial, queued, and blocked dispositions. |
| Super-events and audio | `docs/super_events/020_black_plague/research.md`, `docs/assets/020_black_plague/audio_manifest.md`, `interface/020_black_plague_super_events.gfx`, `sound/chaosx_sound.asset`, `music/chaosx_music_track_list.html` | Audio IDs 101, 102, and 103 are wired evidence; slot 087 is runtime-gated and has final art/text/audio registration. Release attribution, broader presentation depth, and live proof remain open. |
| Asset provenance | `docs/assets/020_black_plague/event_art/manifest.md`, `docs/assets/020_black_plague/rat_identity_asset_manifest.md`, `docs/plans/020_black_plague_plans/subagent_handoffs/2026-08-01_event20_super_event_087_art_handoff.md` | Three report/news assets and slot-087 final art are wired evidence; RTB-RTM flags are archival unused production; dedicated crisis/Crown/ordinary-aftermath/Doctor Wu/route assets remain queued where still required. |

## Plan and handoff dispositions

| Document or package | Disposition |
| --- | --- |
| 2026-08-01 consequence and aftermath addendum | Core tranche implemented statically and retained as the working disposition record. RTA hierarchy, `.45`, RTX crises, Crown Strike, scoped actor hooks/metrics/gate, resolver-owned `.72`, and slot-087 presentation wiring are represented; broader depth, native-mission API decision, dedicated crisis/route assets, rights, workbook alignment, and live validation remain queued. |
| 2026-07-29 core readiness report | Historical baseline reconciled with the later tranche. It no longer implies 3D models are a current blocker or that all crisis/aftermath surfaces are absent. |
| Completion-audit clarification | The historical handoff's older absence wording is superseded for `.45`, `.57-.59`, `.64-.65`, `.71-.75`, resolver-owned `.72`, and slot-087 presentation; its whole-spec and validation findings remain usable. |
| 2026-08-01 completion audit handoff | Historical audit snapshot retained. Its old “missing” wording is superseded only for static `.57-.59`, `.64-.65`, and `.71-.75`; whole-spec and validation findings remain usable. |
| 2026-08-01 live-wiring completion audit handoff | Historical audit snapshot retained with a superseded notice. Its actor/slot-087 absence claims are superseded by the second reconciliation; evolution/scenario/audience, broader assets, and live-validation findings remain open. |
| 2026-08-01 decision/mission incremental audit | Historical audit snapshot retained. Native mission fields remain absent; current Crown Strike and Seal Royal Burrows shared actions are now named explicitly. |
| 2026-08-01 RTA hierarchy runtime handoff | Current Package A evidence: hierarchy graph, consumers, AI, and the parent follow-on's three continuing actions are present. Dedicated icons and lack of live validation remain open. |
| 2026-08-01 report/news art handoff | Current provenance handoff for the three promoted origin, emergence, and overseas assets. It does not supply the dedicated crisis, Crown, ordinary-aftermath, Doctor Wu, or ID 87 packages; slot 087 is covered by its separate final art handoff. |
| 2026-08-01 content-tranche handoff | Current implementation evidence and integration boundary; it remains partial and is not a replacement for this disposition record. |
| `rat_absorption_follow_up.md` | Already resolved/superseded by state-marker absorption; unchanged. |
| Super-event 87 design | Final art, selected text, audio ID 103, sprite, and sound-wrapper package promoted behind the explicit runtime gate; release attribution, docs/workbook alignment, and live validation remain open. |
| Workbook and CSV export | Left unchanged and parent-owned. No workbook update or export was authorized in this cleanup. |

## Contradictions resolved

- Historical claims that route crises, Crown Strike, and defeat aftermath were wholly absent now distinguish static wiring from missing live proof and deeper design work.
- Historical claims that the current aftermath lacked actor evidence now distinguish the implemented scoped participant registry from the remaining `.73` first-eligible-human audience fallback.
- Historical claims that the Crown Strike is a native mission now identify the current shared timed state-action implementation and leave the API choice to the parent.
- Historical multi-tag and independent-Rat-Nation language is superseded by the accepted `RTA`/`RTX` two-tag rule.
- Historical 3D model blockers are classified as outside the current goal rather than hidden completion work.
- Audio manifests and super-event research now record IDs 101, 102, and 103 as wired evidence; slot 087 art/text/sprite and settings wrappers are promoted while rights/live proof remain open.

## Contradictions still open

- `chaosx.nr20.45` is now defined and called from the three RTA hierarchy root rewards; the remaining open issue is dedicated hierarchy art.
- The defeat resolver now has the accepted narrow `on_capitulation` and state-control participant hooks plus a contributor registry; the remaining mismatch is `.73` audience fallback to the first eligible human response host rather than the saved actor.
- Reconstruction `.72` is now coupled to the same once-only eligibility gate in the defeat resolver; it remains separate from later `.74` sealing and lacks live proof.
- ID 87 is no longer an unwired reservation: qualification tracking, final image, localisation, selected quote/cultural remark, audio ID 103, GFX registration, and sound/music records are present; release rights documentation and live validation remain.
- Crisis, aftermath, Doctor Wu, and hierarchy consumers still need dedicated art or icons where the accepted asset inventory requires them; Crown Strike and Royal Burrow sealing use dedicated decision icons while several event reports still reuse generic art.
- No live scenario or in-game validation proves the new route, crisis, Crown Strike, actor, or aftermath behavior.
- The current shared timed state-action API may or may not satisfy the accepted “mission” design; parent decision required before any conversion.

## Duplicate, superseded, and stale-document list

- Superseded notices were added to the coding, goal, and decision/mission prompts without rewriting their historical bodies.
- Superseded notices were added to the completion, live-wiring, and decision/mission audit handoffs without deleting their still-valid findings.
- `docs/assets/020_black_plague/rat_identity_asset_manifest.md` no longer presents RTB-RTM as runtime requirements.
- `docs/assets/020_black_plague/event_art/manifest.md` no longer claims that all parent GFX/gameplay wiring is still pending; it now limits that statement to the producer package and records queued art gaps.
- The source README and source-of-truth disposition now point later implementers to the reconciled two-tag/no-model and partial-tranche state.
- No document was deleted because archival scope deletion was not requested.

## Validation performed

- Searched Event 020 event definitions and callers for `.45`, `.57-.59`, `.64-.65`, `.71-.75`, and `.90`.
- Confirmed the current RTA focus and runtime files contain the hierarchy roots, follow-ups, state variable, route consumers, and AI references.
- Confirmed the current shared response decision/effect files contain Crown Strike and Seal Royal Burrows state actions and no native `activate_mission` or `days_mission_timeout` fields.
- Confirmed the current Rat King resolver records scoped participants, tracks duration/peak metrics, fires `.71`, dispatches eligible `.72` and slot 087, and retains the `.73-.75` path.
- Searched `common/on_actions/020_black_plague_on_actions.txt` and confirmed the narrow `on_capitulation` and `on_state_control_changed` participant hooks.
- Searched the defeat constants/triggers/effects for the current 180-day, 250M-deaths, 24-state, 12-state/0.50-ratio, and 3-participant gate.
- Searched for `super_event_087` and confirmed the final sprite registration, localisation `.87`, audio ID 103 wrappers, music catalogue row, and resolver call.
- Confirmed sound/music registry evidence for audio IDs 101, 102, and 103; retained the explicit runtime gate and release-attribution limitation.
- Reviewed the targeted documentation diffs and did not launch Hearts of Iron IV, run an in-game session, or edit the workbook/export files.

## Remaining parent decisions and risks

1. Decide whether the shared timed state-action API is accepted for Crown Strike and Seal Royal Burrows or whether native mission fields are required.
2. Implement or explicitly queue the six hierarchy icons and broader route/narrative depth.
3. Decide whether `.73` should dispatch to the saved defeating actor rather than the current first eligible response host, and whether the shared timed state-action API is sufficient for native mission requirements.
4. Retain the ID 87 gate, release the CC BY-SA attribution record, and run focused live playback/consumer validation.
5. Do not revive RTB-RTM flags, independent Rat Nation wording, or 3D model production as hidden runtime requirements.
6. Align the workbook/export and run focused route, crisis, Crown Strike, defeat, aftermath, asset, and balance validations before any whole-spec completion claim.

No resume packet was created because this handoff is the current documentation state and the parent did not request a separate resume document.
