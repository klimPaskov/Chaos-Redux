# Event 006 FORM-16 current-closure audit

Date: 2026-08-06.

Scope: current ARM/IW-070, GEO/IW-071, and AZR/IW-072 carriers, FORM-16 Transcaucasian Federation sources, their shared formable transaction registry, current carrier-refresh repair, and the two Transcaucasus decision categories.

This audit is source/static evidence only where the required MCP routes did not return bounded scenario results before parent-requested closure.

## Changed files

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw006_form16_current_closure_2026_08_06.md`

No gameplay, localisation, GUI, GFX, AI, event, trigger, effect, category, registry, country, or asset file was changed.

No FORM-16 readiness condition was weakened and no package was newly attested.

## Sources reviewed

- `common/scripted_effects/006_independence_wave_form16_effects.txt`
- `common/scripted_triggers/006_independence_wave_form16_triggers.txt`
- `events/006_independence_wave_form16_events.txt`
- `common/decisions/006_independence_wave_transcaucasus_decisions.txt`
- `common/decisions/categories/006_independence_wave_transcaucasus_categories.txt`
- `common/script_constants/006_independence_wave_transcaucasus_constants.txt`
- `common/ai_strategy/006_independence_wave_transcaucasus.txt`
- `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_formable_registry_effects.txt`
- `common/scripted_triggers/006_independence_wave_formable_registry_triggers.txt`
- `common/decisions/006_independence_wave_formable_registry_decisions.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt`
- `docs/events/006_independence_wave/systems/country_registry.md`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw006_form16_carrier_refresh_repair_2026_08_06.md`

Required offline wiki references and installed vanilla documentation were consulted for decision, event, scope, trigger, effect, localisation, AI, modifiers, on-action, data-structure, and idea semantics.

The vanilla precedent inspected was `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/decisions/AUS.txt`, particularly the Danubian invitation flow, target safety, in-flight flag, cooldown, and delayed reply pattern.

## Issue list, sorted by severity

### Critical and high

No deterministic critical or high source defect was found in the requested FORM-16 surface.

### Medium: required MCP scenario evidence remains incomplete

The typed probability audit was routed to `chaosx_ai_probability_auditor` as required, but no result was returned before the parent required source/static closure.

The prior carrier-refresh handoff contains only a decision source inventory, not an evaluation of the eight current scenarios.

The parent should obtain or rerun the auditor's `hoi4.probability_inspect` and `hoi4.probability_evaluate` results for the current revision before claiming probability-complete FORM-16 closure.

### Low: FORM-16 generation metadata is retained after cleanup but is non-authorizing

`independence_wave_form16_cleanup_runtime` clears the readiness flag and active charter state, while `independence_wave_formable_cleanup_runtime` clears the generic profile, proposal, readiness-family, and transaction values.

`independence_wave_form16_readiness_generation` and `independence_wave_form16_readiness_family` are not explicitly cleared in the FORM-16 cleanup helper.

This is not patched because no current trigger grants readiness from those variables alone: the receipt flag is cleared before a new generation is prepared, family/profile equality is re-established by the focus registration flow, and current invitations separately compare carrier, member, family, generation, and proposal sequence.

This is a hygiene observation, not an admission or stale-generation bypass.

## Current lifecycle and writer trace

1. Each accepted carrier setup assigns the same FORM-16 family and selected-family flag through `independence_wave_transcaucasus_prepare_full_focus` in `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt`.
2. The focus registration effect loads the profile and calls `independence_wave_formable_register_selected_family_readiness`.
3. The three 210-day founding missions gate each carrier's success flag behind its own named capital and two ledgers at the stable threshold of 65.
4. ARM, GEO, and AZR each complete a distinct arbitration decision and write `iw070_arbitration_receipt`, `iw071_arbitration_receipt`, or `iw072_arbitration_receipt`.
5. The 2026-08-06 repair makes every arbitration completion call `independence_wave_form16_register_readiness` for ARM, GEO, and AZR, so the selected carrier can publish readiness when the last receipt arrives elsewhere.
6. Readiness still requires the selected exact carrier, all three living package members, their state 230/231/229 ownership and control, peace, clear Transcaucasian identity, a constitutional or league route, and the completed arbitration set.
7. FORM-16 discovery permits only negotiated federation or league transformation with voluntary membership, and its invitation loop stores a carrier, carrier generation, candidate generation, family, and proposal sequence for every candidate.
8. AI candidates use `independence_wave_form16_resolve_ai_invitation_from_root`: only a connection to ROOT, recognition, and no severe instability produces consent. Human candidates use event `chaosx.nr006.6816` and retain the generic exact invitation validation.
9. The shared registry rebuilds current member, anchor, consent, observer, and opposition ledgers, freezes consent snapshots before mutation, and rejects a voluntary compact when any opposed member remains.
10. The identity adapter uses `transcaucasia_unified` only after runtime prevalidation, writes its generation receipt, and the integration adapter transfers and cores only 230, 231, and 229 before ending only frozen consenting origins.
11. Rollback removes the FORM-16 cosmetic identity when applicable, clears identity and integration receipts, clears the identity globals only after both receipts exist, and records a rollback flag.
12. Origin reset calls package cleanup and `independence_wave_cleanup_decision_layer`, which calls shared formable cleanup. FORM-16 cleanup removes its seven post-formation decisions, charter ideas, readiness, connection, capital, progression, and ledger values.

## Typed scenario trace

| Scenario | Current source result | Evidence and remaining limit |
| --- | --- | --- |
| `stable_recognized_connected_members` | Can reach readiness and invite/commit flow if one exact selected carrier has all living anchors, all three arbitration receipts, peace, identity clearance, a constitutional or league route, and the generic transaction receipts. | `independence_wave_form16_register_readiness`, `has_independence_wave_form16_commit_readiness`, and generic member ledger/congress predicates provide static proof. Exact AI score remains pending probability MCP evidence. |
| `missing_connection` | AI candidate consent resolves to refusal because `has_independence_wave_form16_connection_to_root` fails. The pre-formation AI gate remains false because the all-member connection proof cannot be recorded. | Connection is deliberately an AI-consent and AI-action condition, not an extra human territorial readiness condition. Human consent remains subject to the exact invitation snapshot and later congress ledger. |
| `severe_instability` | AI candidate consent resolves to refusal and generic AI formable pursuit is blocked. | Severe instability is not a hard human formation ban in the current source. This is a design boundary, not a hidden automatic bypass. |
| `active_war` | Readiness, runtime commit prevalidation, and each member candidate/arbiter path fail when a member is at war. | `has_independence_wave_form16_member_peace` requires all three tags to have no war, while the arbitration decisions cancel on bilateral member war. |
| `lost_anchor` | Formation cannot newly pass because `has_independence_wave_form16_all_members_live` requires the exact member to own and control 230, 231, or 229. Post-formation capital and charter actions become unavailable through the same three-anchor checks. | Source-only confirmation. The relevant post-formation helper is `has_independence_wave_form16_anchor_control`. |
| `identity_collision` | Readiness and runtime prevalidation fail while the vanilla/global Transcaucasian identity flags or any existing `transcaucasia_unified` cosmetic identity exists. | `has_independence_wave_form16_identity_clearance` checks `form_transcaucasia_flag`, `independence_wave_form16_transcaucasia_identity_in_use`, and every country cosmetic tag. |
| `refusal` | A withholding candidate enters the opposed ledger, and voluntary membership requires opposed count zero. | `independence_wave_formable_withhold_consent_for_selected_family`, `independence_wave_formable_evaluate_candidate_consent`, and `can_independence_wave_formable_pass_congress_vote`. |
| `stale_generation` | Invitation, reply, frozen-consent, and active-member rows compare the current carrier, carrier generation, member generation, family, and proposal sequence. Reset clears the authorizing receipt before the next origin receives a new generation ID. | FORM-16's retained metadata noted above is not independently authorizing. MCP state-flow evidence is still pending. |

## Decision category lifecycle notes

`independence_wave_transcaucasus_reconstruction_category` is visible only for one of the three exact package carriers.

It contains one active founding mission, three paid local projects, and one arbitration project per carrier.

Each project is one-shot, fails or cancels on capital loss or carrier invalidation, and clears its in-progress marker in its cancellation path.

`independence_wave_form16_integration_category` is visible only for the active post-formation FORM-16 runtime family after post-formation initialization.

It contains one mutually exclusive capital decision plus four one-shot charter actions.

All seven decisions are removed by `independence_wave_form16_cleanup_runtime`, and all charter ideas/ledger variables are cleared there as well.

No category uses a `scripted_gui` entry.

The existing presentation audit at `docs/decision_category_presentation_audit.md` classifies both as ordinary icon/text categories, with no dedicated picture or GUI selected.

## Mission quality notes

| Owner | Mission | Category | Region and requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ARM/IW-070 | `independence_wave_arm_secure_yerevan_approaches` | Reconstruction | Hold Yerevan and reach the two Armenian settlement ledgers | 210 days | Marks founding success and advances shared/local progress | Applies ledger and shared-system failure | Low. It is tied to Yerevan and Armenian supply/legitimacy. |
| GEO/IW-071 | `independence_wave_geo_keep_tbilisi_black_sea_corridor_open` | Reconstruction | Hold Tbilisi and reach corridor access plus federal mediation | 210 days | Marks founding success and advances shared/local progress | Applies ledger and shared-system failure | Low. It is tied to the Black Sea corridor and Georgian ledgers. |
| AZR/IW-072 | `independence_wave_azr_secure_baku_oil_belt` | Reconstruction | Hold Baku and reach oil security plus export legitimacy | 210 days | Marks founding success and advances shared/local progress | Applies ledger and shared-system failure | Low. It is tied to Baku oil and Azerbaijani ledgers. |

The common 210-day duration is justified as one parallel founding window, not a repeated passive check.

All three missions auto-resolve through cancellation when their goal is achieved, so they do not require an unnecessary second player click.

## Cost and requirement clarity

The three carrier project families use differentiated trains, infantry equipment, support equipment, manpower, army experience, civilian-factory capacity, political power, command power, and fuel costs.

The FORM-16 capital actions use command power plus political power and all three anchors, while language, rail, revenue, and army actions use distinct command-power costs, anchor control, one-shot flags, and materially advance separate charter ledgers.

The category descriptions name Yerevan, Tbilisi, Baku, the charter tiers, and the formation baseline.

The runtime requirements are condensed into named scripted triggers instead of exposing raw state arrays.

No political-power-only exchange or repeatable reward loop was found in this surface.

## AI validity and route-lock notes

The FORM-16 integration actions have a base willingness of 180 and multiply to zero when `has_independence_wave_form16_ai_gate` fails.

The three capital options further select the carrier's original tag and multiply non-preferred capitals to zero.

The AI gate requires connection proof, peace, route compatibility, and arbitration before formation, then retains the same-generation connection receipt after formation.

The AI invitation resolver requires connection, recognition, and no severe instability and otherwise records explicit refusal.

The hard formation path separately protects living members, peace, identity, territory, route compatibility, consent, frozen snapshots, transaction state, and readied adapters.

No invalid dead-target, closed-route, or free-AI-action source path was found by static trace.

## Localisation and tooltip notes

The category names, descriptions, all founding missions, project actions, FORM-16 actions, cost summaries, success/failure tooltips, and human consent event keys are present in `localisation/english/006_independence_wave_transcaucasus_l_english.yml` and the FORM-16 event localisation surface.

The player-facing category description accurately communicates members, peace, route, and anchor continuation without exposing receipt generations, frozen arrays, or rollback internals.

No missing key was identified in the audited decision/event identifiers.

## Cleanup and exploit-risk notes

The current carrier-refresh repair is correctly narrow.

It publishes readiness to every exact ARM/GEO/AZR candidate after arbitration without relaxing the carrier, live-member, peace, identity, route, or receipt limits.

The formation adapter is bounded to States 230, 231, and 229 and ends only frozen consenting origins.

One-shot decisions, in-progress flags, cancellation effects, removal on FORM-16 cleanup, identity collision flags, and transaction rollback prevent obvious equipment farming, free-unit, core, or repeat-formation loops in the reviewed source.

No direct `on_daily`, `on_weekly`, or whole-world polling hook was introduced by FORM-16.

## MCP evidence and fidelity

`hoi4.event_inspect` was run for `events/006_independence_wave_form16_events.txt` and returned `EVENT_INSPECTED_PARTIAL` for workspace `mod_chaos_redux_ea3b2d67c2c0`.

Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ad550e2fc25744f695f7ca7bec9b3ab8c4388be85cd80b256863755b2c100b90/05d7a0e465b05b2b0e66e01a0db16d12d89de7c8e760fc1e61a9e12b4ece6cee/event-scan-be8a459e7129.json`.

`hoi4.event_inspect` trace and `hoi4.event_render` scope requests also returned partial workspace projections with no selected event nodes, so they do not replace the static helper trace.

Scope-render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c4cb47aa5320932aa827e2f51eea321dda1a815b92b73ce04c1c1d92956d0a1/ab70087a534de31d7dd365ad48f0d85f7e65969cb82daf41d77475c7676a01f4/event-scope-be8a459e7129.json`.

GUI inspection and render were requested for `independence_wave_form16_integration_category` with a stable scenario and two resolutions.

There is no `scripted_gui` category field or named FORM-16 window in source, and both MCP GUI calls produced no result before termination.

This is a fidelity limitation, not evidence that the ordinary decision category was rendered correctly.

The required probability route was delegated but did not return before closure.

## Meaningful validation run

- Static writer/reader trace covered founding, arbitration, fan-out readiness, invitation, consent, frozen snapshot, identity, territory, integration, rollback, stale generation, and cleanup writers.
- The source confirms exactly three territorial anchors and exact ARM/GEO/AZR carrier tags.
- MCP event scan and scope render artifacts are recorded above, with their partial-projection limitation.
- No source patch was made, so a probability compare is not applicable.

## Skipped meaningful validation

- Current-revision `hoi4.probability_evaluate` results for the eight named scenarios are not available from the required auditor before parent-requested closure.
- `hoi4.gui_inspect` and `hoi4.gui_render` did not complete for an ordinary decision category that has no linked scripted-GUI window.
- No live game, save/load, or in-game GUI validation was run.

## Recommended parent follow-up

1. Obtain the pending `chaosx_ai_probability_auditor` result or rerun it against the exact eight scenario ids before treating AI/probability evidence as complete.
2. If ordinary category rendering is needed for completion evidence, use a GUI route that can inspect the vanilla decision category shell rather than treating the FORM-16 category id as a scripted-GUI window.
3. Retain the current fan-out repair and do not broaden its gates.

No broader implementation plan was written because the static review found no required new decision system, formable suite, event chain, or GUI mechanic.
