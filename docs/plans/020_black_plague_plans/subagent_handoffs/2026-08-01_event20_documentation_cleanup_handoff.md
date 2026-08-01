# Event 020 documentation cleanup handoff

Date: 2026-08-01

## Scope and result

This cleanup reconciles the consequence/aftermath addendum and core-readiness report with the current Event 020 worktree evidence for the RTA hierarchy, RTX route crises, Crown Strike, Rat King defeat aftermath, two-tag boundary, no-model boundary, and super-event 87 blocker.

Only documentation surfaces were changed.
No gameplay, localisation, GFX, audio, image, model, spreadsheet, or export-only CSV file was edited.
No Git commit was created because the parent did not request one.

## Files changed

- `docs/plans/020_black_plague_plans/2026-08-01_event20_consequence_and_aftermath_addendum.md`
- `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md`
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
- `docs/super_events/020_black_plague/research.md`

The three asset manifests are ignored by the current Git status but are updated in the shared workspace and remain part of this documentation handoff.

## Source-of-truth map

| Surface | Current source | Disposition |
| --- | --- | --- |
| Country identity and scenario rule | `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md` and `docs/specs/020_black_plague_specs/README.md` | Accepted source: `RTA` is the sole reusable Rat Nation carrier, `RTX` is the separate Rat King, and internal broods are state markers. |
| RTA hierarchy route | `common/national_focus/020_black_plague_rat_focus_tree.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_triggers/020_black_plague_rat_triggers.txt`, `common/ai_strategy/020_black_plague_rat_ai_strategy.txt` | Static implementation evidence: roots, follow-ups, `.45` acknowledgement, hierarchy consumers, and route-aware AI are present; dedicated icons, emergent-exposure consumption, and live validation remain open. |
| RTX crises and Crown Strike | `events/020_black_death.txt`, `common/scripted_effects/020_black_plague_rat_effects.txt`, `common/scripted_effects/020_black_plague_shared_response_effects.txt`, `common/decisions/020_black_plague_shared_response_decisions.txt` | Static implementation evidence: `.57-.59`, `.64-.65`, route consumers, costs, and reports are present. Crown Strike and Seal Royal Burrows use shared timed state actions rather than native mission fields. |
| Rat King defeat aftermath | `common/scripted_effects/020_black_plague_rat_effects.txt`, `events/020_black_death.txt`, `common/decisions/020_black_plague_shared_response_decisions.txt` | Partial static implementation: idempotent resolver, `.71`, `.73-.75`, and sealing action exist. Scoped actor hooks, contribution registry, reconstruction coupling, and ID 87 gate remain open. |
| Event-chain and decision coverage | `docs/specs/020_black_plague_specs/matrices/event_chain_map.md`, `docs/specs/020_black_plague_specs/matrices/decision_mission_matrix.md`, `docs/specs/020_black_plague_specs/specs/020_black_plague_spec_part_7_world_end_and_aftermath.md` | Current matrix/spec evidence records `.45`, `.57-.59`, `.64-.65`, and `.73-.75`; native mission fields and live proof remain open. |
| Current narrative overview | `docs/events/020_black_plague/overview.md`, `docs/events/020_black_plague/shared_response.md`, `docs/systems/black_plague_rat_route_modules.md` | Current implementation-facing docs; shared-response future-work wording was corrected. |
| Addendum and readiness baseline | `docs/plans/020_black_plague_plans/2026-08-01_event20_consequence_and_aftermath_addendum.md`, `docs/plans/020_black_plague_plans/2026-07-29_event20_core_readiness_report.md` | Reconciled working records with explicit implemented, partial, queued, and blocked dispositions. |
| Super-events and audio | `docs/super_events/020_black_plague/research.md`, `docs/assets/020_black_plague/audio_manifest.md` | Audio IDs 101 and 102 are wired evidence; ID 87 remains reserved and production-blocked. |
| Asset provenance | `docs/assets/020_black_plague/event_art/manifest.md`, `docs/assets/020_black_plague/rat_identity_asset_manifest.md` | Three report/news assets are wired evidence; RTB-RTM flags are archival unused production; dedicated crisis/Crown/aftermath/Doctor Wu/87 assets remain queued. |

## Plan and handoff dispositions

| Document or package | Disposition |
| --- | --- |
| 2026-08-01 consequence and aftermath addendum | Partially implemented and retained as the working disposition record. RTA hierarchy, `.45`, RTX crises, Crown Strike, and static aftermath are represented; actor attribution, reconstruction coupling, native-mission API decision, dedicated assets, ID 87, and live validation remain queued or blocked. |
| 2026-07-29 core readiness report | Historical baseline reconciled with the later tranche. It no longer implies 3D models are a current blocker or that all crisis/aftermath surfaces are absent. |
| 2026-08-01 completion audit handoff | Historical audit snapshot retained. Its old “missing” wording is superseded only for static `.57-.59`, `.64-.65`, and `.71-.75`; whole-spec and validation findings remain usable. |
| 2026-08-01 live-wiring completion audit handoff | Historical audit snapshot retained with a superseded notice. Its lifecycle, actor, asset, and validation gaps remain open. |
| 2026-08-01 decision/mission incremental audit | Historical audit snapshot retained. Native mission fields remain absent; current Crown Strike and Seal Royal Burrows shared actions are now named explicitly. |
| 2026-08-01 RTA hierarchy runtime handoff | Current Package A evidence: hierarchy graph, consumers, and AI are present. Its emergent-exposure ownership boundary and lack of live validation remain open. |
| 2026-08-01 report/news art handoff | Current provenance handoff for the three promoted origin, emergence, and overseas assets. It does not supply the dedicated crisis, Crown, aftermath, Doctor Wu, or ID 87 packages. |
| 2026-08-01 content-tranche handoff | Current implementation evidence and integration boundary; it remains partial and is not a replacement for this disposition record. |
| `rat_absorption_follow_up.md` | Already resolved/superseded by state-marker absorption; unchanged. |
| Super-event 87 design | Queued behind the explicit global-crisis gate and unique final art, quote, cultural remark, audio, localisation, and registry package. |
| Workbook and CSV export | Left unchanged and parent-owned. No workbook update or export was authorized in this cleanup. |

## Contradictions resolved

- Historical claims that route crises, Crown Strike, and defeat aftermath were wholly absent now distinguish static wiring from missing live proof and deeper design work.
- Historical claims that the current aftermath is actor-owned now state that the resolver dispatches to the first eligible human host and still lacks scoped defeating-actor capture.
- Historical claims that the Crown Strike is a native mission now identify the current shared timed state-action implementation and leave the API choice to the parent.
- Historical multi-tag and independent-Rat-Nation language is superseded by the accepted `RTA`/`RTX` two-tag rule.
- Historical 3D model blockers are classified as outside the current goal rather than hidden completion work.
- Audio manifests and super-event research now record IDs 101 and 102 as wired evidence instead of future parent-owned registry work.

## Contradictions still open

- `chaosx.nr20.45` is now defined and called from the three RTA hierarchy root rewards; the remaining open issue is dedicated hierarchy art.
- The defeat resolver lacks the accepted scoped `on_capitulation` and Royal Basin/Node `on_state_control_changed` calls and does not preserve a deterministic defeating actor or contribution registry.
- Reconstruction `.72` is still fired by global eradication logic rather than being coupled to successful aftermath sealing.
- ID 87 is reserved only; no trigger, qualification tracking, image, localisation, quote, cultural remark, audio, GFX, GUI, or music package exists.
- Crisis, aftermath, and Doctor Wu consumers still need dedicated art or icons where the accepted asset inventory requires them; Crown Strike and Royal Burrow sealing now use dedicated decision icons while event reports still reuse generic art.
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
- Confirmed the current Rat King resolver fires `.71` and dispatches `.73`, while `.74` and `.75` are defined and reconstruction `.72` remains on the eradication path.
- Searched `common/on_actions/` for Event 020 defeat resolver hooks and found no targeted `on_capitulation` or Royal Basin/Node `on_state_control_changed` integration.
- Searched for `super_event_087` and found no runtime package beyond the reserved constant/addendum references.
- Confirmed sound/music registry evidence for audio IDs 101 and 102 and preserved the explicit ID 87 exclusion.
- Reviewed the targeted documentation diffs and did not launch Hearts of Iron IV, run an in-game session, or edit the workbook/export files.

## Remaining parent decisions and risks

1. Decide whether the shared timed state-action API is accepted for Crown Strike and Seal Royal Burrows or whether native mission fields are required.
2. Implement or explicitly queue `.45` and the six hierarchy icons.
3. Add scoped defeating-actor capture, contributor fallback, aftermath audience routing, and reconstruction coupling before claiming actor-owned aftermath.
4. Keep ID 87 blocked until its global gate and unique presentation package are complete.
5. Do not revive RTB-RTM flags, independent Rat Nation wording, or 3D model production as hidden runtime requirements.
6. Run focused route, crisis, Crown Strike, defeat, aftermath, asset, and balance validations before promoting this addendum into the full source matrices.

No resume packet was created because this handoff is the current documentation state and the parent did not request a separate resume document.
