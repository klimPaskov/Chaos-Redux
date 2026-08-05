# Event 018 Decision and GUI Compliance Audit Handoff

## Result

No Event 018 gameplay or GUI source file was changed.

The parent’s uncommitted `FROM` wrappers in state-target `target_trigger` blocks were preserved.

No narrow confirmed defect was safe to patch inside the requested surface.

The only material finding is an action-density design warning that requires a broader category-phase decision, not a local syntax, cost, tooltip, AI, or GUI repair.

## Audit scope

- `common/decisions/018_resources_found_decisions.txt`
- `common/decisions/categories/018_resources_found_categories.txt`
- `common/scripted_guis/018_resources_found_scripted_gui.txt`
- `interface/018_resources_found.gui`
- Event 018 localisation and scripted localisation
- Event 018 decision, UI, and static-acceptance handoffs

The source inspection also read the directly consumed Event 018 project-validity and cleanup helpers without editing them.

## Issues, ordered by severity

### Medium design warning: the field-management category can exceed the readable action budget

`resources_found_field_management_category` contains 28 clickable decisions plus its project mission.

The individual `visible` gates are meaningful, but a developing, non-suspended field can expose several posture, survey, development, labour, safety, and output actions at once.

For example, the two posture alternatives, two suspension actions, appraisal, depth test, basin mapping, settlement expansion, safety work, hospital, regulated output, and maximum shifts are not all mutually exclusive in their visibility logic.

This exceeds the decision-skill’s normal three-to-six primary-action budget and leaves the player to sort routine development from urgent response actions.

Do not patch this locally because hiding one decision or adding an arbitrary cooldown would alter route pacing and AI incentives.

Recommended parent-owned plan: define phase or priority gates for the existing field actions, retain emergency containment actions during crisis, and prove the maximum concurrent action count for baseline, industrial, incident, and suspension states before changing `common/decisions/018_resources_found_decisions.txt`.

### Low documentation discrepancy: the older decision audit understates visible mission count

The earlier `decision_mission_audit_handoff.md` says that ten missions remain player-facing.

Current source defines 12 visible non-clock missions: five category project runners, contract term, frontier corridor, commission observation, dispute settlement, border-war limit, burrow objective, and anchor-recapture objective.

This does not change behaviour, but later completion reports should use the current count and distinguish those 12 visible missions from the nine hidden evolution-clock missions.

### Low tool-fidelity limitation: offline GUI font glyphs are incomplete

The GUI inspector reports one missing glyph set for the title text in its deterministic font substitute.

It reports no missing Event 018 sprite, texture, localisation, button effect, button trigger, cost mismatch, click-bounds mismatch, or resolution drift.

This is a renderer-fidelity limitation rather than a source localisation or asset failure.

## Decision-category lifecycle notes

| Category | Lifecycle result |
| --- | --- |
| `resources_found_field_management_category` | Appears for an owned active field or exact closed-history record, remains visible when empty, and hosts the selected-field panel. The closed record is read-only and cannot re-enter the active selection list. |
| `resources_found_trade_and_security_category` | Appears only for a foreign actor or an owned field with live contract, foreign interest, or high pressure. It hides when empty. Trade missions cancel when their locked field or partner becomes invalid. |
| `resources_found_containment_category` | Appears only after disturbance, breach, or full-seal state is present. It remains available for mission status even when no ordinary containment action is currently valid. |
| `resources_found_cave_brood_network_category` | Is restricted to the living flagged Oth-Kesh country and remains available across its route phases. Targeted cave project missions cancel when their exact state loses legal validity. |
| `resources_found_anti_cave_response_category` | Is restricted to ordinary countries during the live cave threat or defined post-defeat reconstruction. Targeted state and aid projects cancel when the threat, state, or partner becomes invalid. |
| `resources_found_hidden_clock_category` | Is permanently non-rendered at category level. Its nine activated evolution clocks therefore cannot leak into the player decision list even though mission-level `visible` is not a reliable render gate. |

## Mission-quality notes

| Mission family | Owner/category | Region or requirement | Duration | Success | Failure or cleanup | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- |
| Field, trade, containment, cave, and anti-cave project runners | Their matching decision category | A dynamically locked field, targeted state, or partner with exact cached costs | `resources_found_active_project_days` | Route-specific completion helper | Invalid field, state, country, threat, or partner cancels and clears runtime | Low, because each runner owns a different project family. |
| Contract term | Trade | Locked field, owner, and partner must retain a valid contract context | `resources_found_contract_term_days` | Contract completion helper | Contract failure helper | Low. |
| Frontier corridor | Trade | Both named border states, supplied forces, and usable owner infrastructure | `resources_found_frontier_mission_days` | Corridor completion helper | Pair invalidation or timeout failure helper | Low, distinct map objective. |
| Commission observation | Trade | Live commission observation context | `resources_found_commission_observation_days` | Observation completion helper | Observation failure helper | Low. |
| Dispute settlement | Trade | Locked field and claimant settlement context | `resources_found_dispute_settlement_days` | Settlement qualification helper | Qualification failure helper | Low. |
| Border-war limit | Trade | Active owner, claimant, and state-pair context | `resources_found_border_war_limit_days` | Moves the dispute into settlement if the war ends | Timeout cancels the limited war and cleanup clears runtime | Low. |
| Burrow objective | Cave | Exact defended capital, supply hub, or fortification target | `resources_found_burrow_objective_window_days` | The separate captured-objective chain consumes it | Timeout or invalidation clears its objective runtime | Low, exact state pointer. |
| Anchor recapture | Anti-cave | Exact activating anchor held by the defender | `resources_found_anchor_recapture_days` | Disrupts the anchor and marks success | Sets failure evidence then clears pointer and days | Low, exact state pointer. |
| Evolution clocks and rescheduler | Hidden clock category | Per-evolution field validity, ownership, closure, disable, and later-stage conditions | Event-owned dynamic clock variables | Fires the matching progression helper | Cancels the matching clock helper | Low, one clock per progression state. |

## Cost and requirement clarity

All 100 priced actions use a custom-cost key tied to the shared exact-preview ledger.

The calculator stores rounded values for political power, command power, army experience, manpower, civilian and military capacity, equipment, trains, convoys, fuel, and duration before availability and payment use them.

`resources_found_decision_has_dynamic_project_inputs` verifies cache parity and each displayed input before a timed or immediate action can pay it.

All 109 `custom_effect_tooltip` keys and all 31 GUI text or tooltip keys resolve in the scoped Event 018 localisation files.

Free actions are navigation, state selection, a policy choice, a cancellation or withdrawal, or an activated mission callback, not repeatable reward loops.

## Target semantics, AI, cleanup, and exploit risk

The seven state-target decisions are `resources_found_cave_activate_resource_anchor`, `resources_found_cave_accelerate_critical_anchor`, `resources_found_cave_guard_feeding_chamber`, `resources_found_deny_resource_state`, `resources_found_liberate_activating_anchor`, `resources_found_clear_mature_anchor`, and `resources_found_restore_liberated_resource_state`.

Each state-target `target_trigger` is explicitly scoped through `FROM` and each matching completion effect locks the exact state in `resources_found_active_response_state`.

Country-target decisions retain direct target-scope predicates as expected by vanilla targeted decisions, then store `FROM` only where a project needs a partner pointer.

The shared runtime cleaner clears `resources_found_active_response_state`, `resources_found_pending_project_partner`, project variables, project flags, and cached costs.

The cave and anti-cave mission cancel triggers independently revalidate each locked state or partner before allowing completion.

Every clickable non-mission decision has an `ai_will_do` block.

The scripted GUI is intentionally human-only with `ai_enabled = { always = no }`, while AI uses the same normal decision and project-effect paths.

No free unit, equipment, core, claim, war-goal, or cooldown loop was found in the audited source.

## Scripted-GUI integrity and coverage

`resources_found_field_scripted_gui` uses `decision_category` context and binds `resources_found_field_window`.

Its five visible controls are real actions: previous field, next field, map focus, animation toggle, and closed-history toggle.

Each has a matching click effect, `_click_enabled` trigger, label, and tooltip.

The standard `buttonType` handles hover and disabled presentation.

History selection is conveyed by switching to the mutually exclusive closed-state title and container rather than by a separate selected button sprite.

The selection and closed-history containers are mutually exclusive, and each artwork state has mutually exclusive animated or static visibility gates.

The root panel is 470 by 304 pixels and maps its background regions as follows.

| Background region | GUI content | Status |
| --- | --- | --- |
| Header field | Record title and active or closed state label | Used. |
| Main left record panel | Resource ledger, four operating values, then conditional disturbance and breach lines | Used. |
| Main right inset | One 128-pixel operating, warning, sealing, suspended, or closed illustration | Used. |
| Right lower status field | Posture, stage, lifecycle, contract, and commission summary | Used. |
| Bottom control strip | Five evenly spaced interactive buttons | Used. |

The field record has four baseline operating values and reveals two additional hazard values later in the lifecycle.

They have separate labels, colour plus label cues, bands, tooltips, thresholds, and associated actions, so no narrow presentation change is recommended.

This is nevertheless above the normal one-primary-plus-three-supporting-value guideline and should be reconsidered together with the wider action-density plan.

Source bounds are internally safe: body containers are 438 by 180 pixels, the final breach row ends exactly at the clipped lower edge, and the five scaled button bounds end inside the 470 by 304 root panel with distinct gaps.

## MCP evidence

`hoi4.gui_inspect` artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7eb2626947a6fc38275b501960ca575f092b593b5a4e4b31a721acb1ff27e704/36ad17288fb40fe12dc1a9536d00d204480e63d1fe905ce05b7c62683e582c11/gui-inspect.5f78fee194cf0e50.json`.

`hoi4.gui_render` covered normal, hover, disabled, selected, active, warning, long-text, and missing-localisation states at 1366 by 768, 1920 by 1080, and 2560 by 1440.

The render returned full-window, cropped, annotated, click-region, hierarchy, state-matrix, resolution-scale, and comparison artifacts for source revision `18d639a849b32143d551b185cbe3fa5ab01646206e56482261573be02ec7bd8f`.

The comparison artifact reports zero changed pixels for the supplied normal scenario.

MCP reports global GUI-source failures from unrelated scripted GUI context types and unrelated reference collisions, so its repository-wide blocking count is not an Event 018 finding.

For this window, the task-relevant checks report no text overflow, inconsistent alignment, inconsistent spacing, invalid size, click-bounds mismatch, invisible click blocker, conflicting click region, missing sprite, missing texture, missing localisation, button effect gap, button trigger gap, cost mismatch, AI-equivalent gap, or resolution drift.

The generic animation-static-fallback diagnostic cannot infer Event 018’s paired static visibility gates, but source confirms a static DDS and matching `_static_visible` trigger for every one of its five animated conditions.

## Changed files and identifiers

Changed file: this handoff only.

No decision, mission, scripted GUI, interface, localisation, or scripted-localisation identifier changed.

## Meaningful validation

- Audited all 21 mission definitions, including 12 visible non-clock missions and nine hidden evolution clocks.
- Confirmed the seven state-target blocks retain explicit `FROM` target triggers after the parent’s uncommitted edit.
- Confirmed all state-target project kinds have exact validity checks and cleanup coverage.
- Confirmed every clickable GUI control has a matching source effect, enable trigger, label, and tooltip.
- Confirmed GUI source bounds, sprite dimensions, and button effective bounds from the shipped DDS metadata and the interface scale values.
- Confirmed complete Event 018 tooltip and GUI localisation key coverage.

## Skipped meaningful validation

No Hearts of Iron IV live run was performed because this audit is source and MCP based and live validation belongs to the user.

The offline renderer could not use the final title-font glyph set and its PNG artifact retrieval was unavailable for manual pixel inspection, so visual fidelity conclusions are limited to the returned source-map, state, resolution, and validation evidence plus source geometry.

## Follow-up for the parent

Treat field-management action density and the nominal visible-value budget as one parent-owned design pass.

If that pass is deferred, record the intentional exception rather than presenting the category as within the normal compact-action guideline.

No gameplay patch is pending from this audit.
