# Event 006 current decision and mission surface audit

Date: 2026-08-25.

Owner: `/root/event6_decision_audit_current2`.

Parent: `/root`.

Status: read-only audit complete; no gameplay, AI, GUI, GFX, asset, or localisation source was changed. This handoff is the only new file from this audit.

## Supersession note (2026-08-25)

The two concrete source findings in this dated audit are closed by later owner patches and should not be re-applied.

Commit `7b9da6c9f` removes the unrelated train icon from the eight FORM-48 convoy-only base and blocked localisation strings, matching the current convoy-only trigger and payment branches.

Commit `9f2ba4de5` adds the standard two-civilian-factory reservation to `independence_wave_form39_open_regional_civil_service`, matching its existing strategic-capacity trigger and cost disclosure.

The remaining GUI, typed probability, visible-action, category-density, and whole-event admission notes below remain evidence gaps or broader HOLD/PARTIAL items; this supersession note does not claim runtime validation.

## Scope and authority

The audit covered the current Event 006 decision categories, decision and mission lifecycle, triggers, costs, dynamic localisation, AI weights, route locks, cleanup, exploit risk, and recent cost-localisation handoffs.

The accepted design references were `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_3_mechanics_and_decisions.md`, `docs/specs/006_independence_wave_specs/prompts/independence_wave_decision_mission_prompt.md`, `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`, and the Event 006 README and current source-of-truth notes.

The required offline Paradox wiki pages and installed vanilla documentation for decisions, missions, triggers, effects, modifiers, localisation, scopes, script constants, and `civilian_factory_use` were consulted before source review.

Recent handoffs reviewed include `006_event6_decision_mission_audit_round2_2026-08-24.md`, `006_event6_decision_transport_cost_patch_handoff_2026-08-24.md`, `006_event6_form48_cost_localisation_2026-08-24.md`, `006_event6_form05_cost_localisation_2026-08-24.md`, `006_event6_form39_cost_localisation_audit_2026-08-25.md`, and the current Event 006 completion/probability audits.

## Exact verdict and highest-impact bounded fix

### P1 — FORM-48 four visible cost rows falsely advertise trains

The current FORM-48 cost localisation displays one convoy amount followed by both `£convoy_texticon` and `£GFX_train_texticon` for four cost families:

- `independence_wave_form48_invitation_acceptance_cost` and `_blocked` at `localisation/english/006_independence_wave_pacific_l_english.yml:173-175`;
- `independence_wave_form48_carrier_convoy_cost` and `_blocked` at `:188-190`;
- `independence_wave_form48_carrier_procurement_cost` and `_blocked` at `:197-199`; and
- `independence_wave_form48_member_convoy_cost` and `_blocked` at `:218-220`.

The invitation and member-convoy decisions use `can_pay_independence_wave_form48_member_convoy_cost` and `independence_wave_form48_pay_member_convoy_cost` at `common/decisions/006_independence_wave_form48_decisions.txt:24-32,224-231`. The carrier convoy and carrier procurement decisions use their corresponding trigger/payment pairs at `:72-80` and `:108-116`.

The relevant availability triggers at `common/scripted_triggers/006_independence_wave_form48_triggers.txt:371-394` check `has_equipment = { convoy > ... }` only. They contain no train branch. The payment helpers at `common/scripted_effects/006_independence_wave_form48_effects.txt:260-285` subtract only convoy for these four families; the procurement helper also subtracts infantry and support equipment. The constants at `common/script_constants/006_independence_wave_constants_registry.txt:3534-3561` define negative convoy spends and no train spend for FORM-48.

This is a direct player-facing cost/requirement mismatch, not a speculative balance finding. A player can reasonably believe trains are required even though the decision is gated and paid with convoys. It also violates the accepted icon-first rule by showing an unrelated spendable icon beside the amount.

Recommended narrow fix for the parent: remove `£GFX_train_texticon` from those eight base and blocked strings, leaving the existing convoy amount and `£convoy_texticon`. Do not add train consumption or a train fallback unless the accepted FORM-48 design is explicitly changed. The shared transport patch already solved this pattern for shared IDs; its own handoff explicitly left package-owned cost strings, including FORM-48, for package-scoped review.

Before: a convoy amount appears to require both convoys and trains.

After the recommended fix: the same amount clearly represents the only transport stockpile checked and paid by the four decisions.

## Severity-sorted issue list

1. **P1 — FORM-48 convoy/train cost mismatch.** Exact identifiers, source evidence, and the safe localisation-only fix are listed above.

2. **P2 — FORM-39 civil-service factory capacity is checked but not reserved.** `independence_wave_form39_open_regional_civil_service` at `common/decisions/006_independence_wave_form39_decisions.txt:121-149` has no `modifier = { civilian_factory_use = ... }`. Its trigger at `common/scripted_triggers/006_independence_wave_form39_triggers.txt:207-221` reaches `can_pay_independence_wave_strategic_cost`, which checks `num_of_civilian_factories_available_for_projects > constant:independence_wave_decision_cost.civilian_factory_standard`, while the effect at `common/scripted_effects/006_independence_wave_form39_effects.txt:167-170` pays strategic and diplomatic resources only. The recent `006_event6_form39_cost_localisation_audit_2026-08-25.md` correctly records this as pre-existing and outside its localisation-only patch. If the accepted 210-day civil-service project is intended to reserve factory capacity, add the standard modifier and align the cost row in a separate scoped change; the payment-versus-capacity intent needs parent confirmation before implementation.

3. **P1/P2 evidence gap — FORM-03 and broad categories lack scenario-backed visible-action proof.** `independence_wave_form03_low_countries_category` has 23 structural child decisions in `common/decisions/006_independence_wave_form03_decisions.txt:14-823`, while its category gate is at `common/decisions/categories/006_independence_wave_categories.txt:165-183`. Structural count is not proof of simultaneous visibility because route, phase, completion, and active-project locks hide many rows. The 2026-08-24 structural scan recorded 87 Event 006 category roots, 785 direct child blocks, 56 categories above six children, 37 above ten, and a maximum of 26. Build phase fixtures before changing layout; do not add a warehouse category or tab solely to hide buttons.

4. **P2 — ordinary category descriptions remain value-dense.** Shared categories still expose raw stability, war support, cohesion, reserve, confidence, host, patron, network, phase, and threshold rows without consistently pairing each value with cause, threshold, consequence, and next player response. The existing Statehood Ledger is intended to carry the five primary values and active-mission summary, but current GUI evidence is aggregate and does not prove family-isolated visual acceptance.

5. **P2 — typed AI/probability evidence remains unresolved.** Current Event 006 source contains AI scores for shared and package decisions/missions, but the required current MCP probability evidence is not available. No AI or balance patch is recommended from source scores alone.

6. **P2 — FORM-03 League Reserve source wiring is closed but live visual proof is not.** The former literal `League Reserve` cost finding is closed in source: `localisation/english/006_independence_wave_form03_l_english.yml:206-207` now uses `£GFX_independence_wave_form03_league_reserve_texticon`, `interface/006_independence_wave_form03.gfx:33` registers it, and the DDS exists. The missing live tooltip/render receipt remains an evidence gap, not a current source defect.

## Decision-category lifecycle notes

The shared category registry at `common/decisions/categories/006_independence_wave_categories.txt:45-150` keeps the core founding, government, recognition, security, former-host, patron, network, league, border, formable, and high-chaos surfaces gated by active-origin and phase flags. The founding category attaches `independence_wave_status_scripted_gui`; the formable categories attach the existing `independence_wave_formable_state_puzzle_scripted_gui`.

FORM-03 uses one `visible_when_empty` category and gates entry through post-charter progression, sovereign-associate state, exact carrier/route anchors, Belgian delegation, or autonomous-member eligibility. Child actions are phased by language, state works, industrial administration, ratification, compromise, and member flags, but the maximum simultaneous set is not engine-proven.

FORM-39 has separate invitation and federal-compact categories at `common/decisions/categories/006_independence_wave_categories.txt:220-228`. Its three post-formation projects are serialized by `has_independence_wave_form39_project_active`, with cancellation on carrier/member loss and runtime cleanup removing decisions and clearing project flags.

FORM-48 has separate invitation and federal-compact categories at `common/decisions/categories/006_independence_wave_categories.txt:230-245`. Its federal carrier sees one stage-gated project at a time: convoy defence, shared procurement, or island basing. Each project locks the other projects, uses a 120-, 180-, or 150-day timer, and activates exactly one deadline mission through `independence_wave_form48_begin_convoy_cycle`, `independence_wave_form48_begin_procurement_cycle`, or `independence_wave_form48_begin_basing_cycle` at `common/scripted_effects/006_independence_wave_form48_effects.txt:361-382`.

FORM-48 member countries see a fulfill/withhold pair for the active convoy, procurement, or basing cycle. The paid response takes 75 days and the withholding response takes 45 days. The carrier missions run for 180, 240, or 210 days and have explicit `complete_effect`, `timeout_effect`, `cancel_trigger`, and `cancel_effect` blocks at `common/decisions/006_independence_wave_form48_decisions.txt:168-210`.

## Cognitive-load notes

- **Visible actions:** FORM-48 is phase-gated to one carrier project and one member response pair at a time, so its normal package surface is bounded. FORM-03 has 23 structural children and many other Event 006 categories exceed six structural children; exact runtime visible counts remain unresolved without fixtures.
- **Active missions:** FORM-48 has one carrier deadline mission per cycle and at most the member responses for the two sovereign members. The source serializes cycle flags and clears old responses before activating the next mission. FORM-03 has language, state-works, industrial, and ratification locks, but no current typed scenario proves the whole Event 006 active-mission cap.
- **Player-facing values:** FORM-48 displays shipping coordination, industrial specialization, defence readiness, member autonomy, compact strain, and completed cycles in its category description. Their thresholds and outcomes are present in source, including the dissolution warning/threshold, but the raw row still requires the player to connect a value to the next response.
- **Text density:** FORM-03 descriptions and ordinary shared category descriptions remain the densest surfaces. Recent FORM-05, shared transport, FORM-39, and FORM-48 localisation tranches reduced prose, but FORM-48 still has the concrete icon mismatch above.
- **Value significance:** every reviewed FORM-48 value has a gameplay consumer; not every ordinary category value states its threshold, consequence, and response in one compact display. No new GUI layout should be invented in this audit.

## Mission quality notes

| Mission | Owner/category/region | Requirement | Duration | Success/failure/cancellation | Duplicate risk |
| --- | --- | --- | --- | --- | --- |
| `independence_wave_form48_convoy_defense_deadline` | HBX carrier, FORM-48 federal-compact category, Pacific compact | Cycle flag plus HAW and FSM convoy responses | 180 days | Completes the shipping/defence cycle or applies failure losses; cancels when the carrier leaves post-formation and clears its active flag | Low: one carrier cycle flag and begin helper gate activation |
| `independence_wave_form48_procurement_deadline` | HBX carrier, same category, Pacific compact | Procurement cycle flag plus HAW and FSM procurement responses | 240 days | Advances industrial/defence/shipping ledgers or applies failure losses; cancellation clears the active flag | Low: mutually exclusive cycle flags and helper activation |
| `independence_wave_form48_basing_deadline` | HBX carrier, same category, Pacific compact | Basing cycle flag plus HAW and FSM consent responses | 210 days | Advances defence/autonomy/shipping ledgers or applies failure losses; cancellation clears the active flag | Low: mutually exclusive cycle flags and helper activation |
| `independence_wave_form03_ratify_confederal_charter` | LCX carrier, FORM-03 category, Low Countries route | Progress thresholds, constitutional statuses, federal language scope, and focus activation | 360 days | Full ratification on completion; explicit partial/rupture resolution on timeout; route-loss cancellation | Low: focus activation and completion/phase flags prevent repeat |
| `independence_wave_form03_request_development_compact_technical_mission` | LCX carrier, FORM-03 category, Development Compact route | Reserve floor, League membership, administration-light bundle, no prior completion/commitment | 180 days | Commits reserve, refunds a smaller amount on cancellation, and applies technical-mission gains on success | Low: active industrial lock, committed flag, completion flag, and cleanup |

## Cost and requirement clarity

The current FORM-48 cost-count audit is within the four-spendable-type ceiling: invitation/member convoy use command power plus convoys; carrier convoy uses command power, convoys, fuel, and civilian-factory capacity; carrier procurement uses convoys, infantry equipment, support equipment, and civilian-factory capacity; carrier basing uses command power, support equipment, and civilian-factory capacity; member procurement uses infantry/support equipment and civilian-factory capacity; and member basing uses command power plus support equipment.

All reviewed ordinary spendables use texticons. The FORM-48 defect is not a missing icon; it is an extra train icon that is not in the trigger or payment branch. The correct narrow correction is to remove that unrelated icon from the four convoy-only cost families.

The FORM-03 technical mission now has four visible groups when the committed factory and League Reserve are counted: command power, manpower, civilian-factory commitment, and League Reserve. Its source and localisation use valid texticons, including the newly registered dedicated League Reserve icon.

FORM-39 civil-service displays a major transport pair and a factory capacity requirement while paying two standard diplomatic transport branches through its helper. The recent localisation handoff made this requirement compact but intentionally did not decide whether the factory should be reserved; parent review is required before changing gameplay.

The recent FORM-05 handoff reports eight compact cost families aligned with their unchanged triggers/effects. The shared transport handoff reports dynamic convoy/train selectors for shared IDs only and explicitly leaves package-owned duplicates for follow-up.

## AI validity and route-lock notes

FORM-48 decision AI uses central low/high/blocked constants with war, instability, and patron modifiers in `common/decisions/006_independence_wave_form48_decisions.txt:38-39,91-95,127-130,162-165,237-240,260-267,301-307,340-347`. Invitation acceptance is intentionally AI-blocked and the package remains fail-closed until the exact HBX/HAW/FSM route is admitted.

FORM-48 triggers require living active members, exact current-generation package bindings, route and anchor checks, controlled capitals, and active-cycle flags. No dead-country target, impossible-border target, stale pointer, or cooldown bypass was proven in this source pass.

FORM-03 AI uses central low/standard/high/urgent constants and route-specific modifiers. The source has no obvious dead-country target in the reviewed BEL/HOL/LUX and state-work paths, but the typed score race is not proven.

The required `chaosx_ai_probability_auditor` route is not callable in the current tool inventory. The installed `hoi4_agent_tools` exposes `hoi4.probability_inspect`, but the current Event 006 probability handoff records source-qualified calls blocked by `Transport closed` or timeout and no current artifact. No source-only score is presented as a probability or balance conclusion.

## Localisation, GUI, and MCP evidence

The current source audit found no remaining literal `League Reserve` in the FORM-03 cost row; the asset wiring is source-present, while live visual proof remains absent.

The two decision-owned GUI surfaces in this scope are `independence_wave_status_window` and `chaosx_independence_wave_formable_state_puzzle_window`. Fresh read-only `hoi4.gui_inspect` and `hoi4.gui_render` attempts were made with object scenarios `{ id: "independence_wave_status_default" }` and `{ id: "E6_FORMABLE_STATE_PUZZLE_GUI_SETTLED_2026_08_09" }` at 1280x720. The calls did not return within the bounded audit window and were terminated; no current artifact is claimed. This matches the prior 2026-08-24 handoff's exact 180-second timeout blocker. No `hoi4.gui_rewrite` was used because no GUI source patch was in scope.

The installed MCP tool inventory exposes no `hoi4.decision_inspect` or `hoi4.mission_inspect` route. Therefore structural source counts and lifecycle tracing above are not engine inspection evidence.

## Cleanup and exploit-risk notes

FORM-48 completion and timeout helpers clear the active cycle flags, apply success or failure ledgers, clear all HAW/FSM responses, and advance the stage at `common/scripted_effects/006_independence_wave_form48_effects.txt:475-576`. Runtime cleanup removes all three missions and all package decisions at `:716-750`. The wiki and vanilla effects documentation note that `remove_mission` skips completion/timeout effects, so the explicit cleanup flags are important and present.

FORM-03 cleanup removes post-charter decisions and ratification, clears variables and flags, and refunds any committed technical reserve exactly once through its existing guard. FORM-39 cancellation and cleanup clear each project flag. No free-unit loop, repeated reserve refund, equipment farming, war-goal spam, or stale target exploit was proven in the bounded source pass.

## Validation, skipped checks, and remaining issues

Validation consisted of targeted `rg` and source crosswalks for every finding, current constants/triggers/effects/localisation re-reads, the recent handoff reconciliation, offline wiki and vanilla documentation review, and bounded attempts of the required GUI MCP routes. No HOI4 launch, save/load, live gameplay, or source patch was performed.

Skipped meaningful validation: current decision/mission engine inspection is unavailable because no decision/mission inspection tool is exposed; GUI inspect/render calls hung and were terminated; current typed probability inspection through `chaosx_ai_probability_auditor` is unavailable and direct probability transport is blocked. These are evidence blockers, not passes.

Remaining issues are the FORM-48 convoy/train localisation mismatch, the FORM-39 factory-capacity-versus-reservation decision, unresolved runtime visible-action proof for FORM-03 and broad categories, aggregate GUI fidelity, incomplete typed AI evidence, and the whole Event 006 HOLD/PARTIAL admission boundary. The former FORM-03 missing-icon issue is not a remaining source defect.

No gameplay files were patched by this audit. The parent should review the P1 FORM-48 localisation fix first because it is a narrow, reversible, source-proven correction with no mechanic redesign.
