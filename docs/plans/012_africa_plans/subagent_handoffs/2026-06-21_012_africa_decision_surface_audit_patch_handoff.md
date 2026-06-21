# Event 012 Africa Decision Surface Audit Patch Handoff

Date: 2026-06-21

## Scope

Audited Event 012 Africa decision, mission, and scripted GUI decision surfaces against the current Africa objective. This pass inspected:

- `docs/specs/012_africa_specs/`
- accepted 012 Africa plans and handoffs under `docs/plans/012_africa_plans/`
- `common/decisions/012_africa_decisions.txt`
- `common/decisions/categories/012_africa_categories.txt`
- `common/scripted_effects/012_africa_effects.txt`
- `common/scripted_triggers/012_africa_triggers.txt`
- `common/scripted_guis/012_africa_scripted_gui.txt`
- directly referenced localisation in `localisation/english/012_african_union_l_english.yml`

Offline Paradox wiki and vanilla decision/scripted GUI documentation/examples were consulted before judging syntax and behavior.

## Files Changed

- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-21_012_africa_decision_surface_audit_patch_handoff.md`

## Changed Identifiers

- `africa_member_petition_to_leave_charter`
- `africa_member_prepare_resistance_war`
- `africa_member_petition_to_leave_charter_req_tt`
- `africa_member_prepare_resistance_war_req_tt`

## Before Behavior

- `africa_member_petition_to_leave_charter` only required a Charter leader, no active integration docket, and no war with the leader. Because `africa_charter_member_category` is visible to former and resistant members, a former member could repeatedly complete the leave decision and push the leader's sovereignty/alarm values again.
- `africa_member_prepare_resistance_war` could be repeated after peace by any still-qualified former, resistant, or integration-docketed country, granting the resistance manpower and rifles again.

## After Behavior

- `africa_member_petition_to_leave_charter` now requires a current Charter binding: `africa_charter_member`, `africa_charter_protected_member`, `africa_regional_authority_subject`, or `africa_bestiary_actor_bound_to_charter`. It also blocks former and resistant members.
- `africa_member_prepare_resistance_war` now sets `africa_charter_resistance_war_prepared` and blocks countries that already prepared a resistance war, preventing repeated manpower/equipment farming.
- Requirement tooltips now describe the added current-membership and one-time preparation gates.

## Remaining Audit Findings

1. Medium: the Continental Congress scripted GUI is still not a full target-selection surface. The accepted spec notes this directly at `docs/specs/012_africa_specs/specs/012_africa_decisions_missions_ui.md:70`; the implementation in `common/scripted_guis/012_africa_scripted_gui.txt:20` through `common/scripted_guis/012_africa_scripted_gui.txt:89` is limited to buttons/status hooks, while card/list work remains queued in `docs/plans/012_africa_plans/2026-06-21_continental_congress_gui_animation_gap_handoff.md:43`.
2. Medium: `africa_influence_charter_member` at `common/decisions/012_africa_decisions.txt:510` is still a mostly flat political power influence exchange. It has AI weights and target checks, but it does not consume support equipment, logistics, local backing, legitimacy, or an active influence deadline.
3. Medium-low: `africa_docket_authority_integration` at `common/decisions/012_africa_decisions.txt:698` is still political power only, despite being part of the integration surface. It does have authority target gates, but the next main-agent patch should tie docketing to local trust, support equipment, manpower, a regional mandate, or a short integration hearing mission.
4. Low: the RSA emergency category uses `africa_rsa_civil_war_active` as its category visibility gate at `common/decisions/categories/012_africa_categories.txt:79`, and the continental victory path in `common/scripted_effects/012_africa_effects.txt:5127` keeps that global flag alive for post-victory settlement decisions. That appears intentional for visibility, but the flag name can mislead downstream checks. Consider splitting a post-victory emergency flag from the active-civil-war flag if other systems start consuming it.

## Lifecycle Notes

- Charter League defense, aid, influence, integration, resist, leave, and fight-back surfaces exist. Aid and corridor missions have target storage, success/failure, cleanup, and non-PP costs. The leave/fight-back exploit risk was patched in this handoff.
- Liberation, regional integration, diaspora, high-chaos, sponsor, World Is One, and RSA emergency categories have active missions or timed decisions with requirements and cleanup. The remaining weak spots are the two PP-heavy Charter influence/integration decisions listed above.
- Continent sponsor and World Is One gates are strict in `common/scripted_triggers/012_africa_triggers.txt:2146` through `common/scripted_triggers/012_africa_triggers.txt:2488`; sponsor charters, external proofs, dynamic union, certification, and final gate all revalidate state before completion.

## Mission Quality Notes

- Charter aid/confidence missions include owner/target storage, duration, success on stabilized target, failure on timeout, and cleanup. Duplicate risk is controlled with active mission and target flags.
- Regional integration and liberation missions use state control, support/equipment/manpower, deadlines, and stored targets. They are not simple passive stores.
- Sponsor and proof timed decisions use regional flags, continent readiness gates, and repeated revalidation. They appear structurally sound, but still need live scenario proof per the current source of truth.
- RSA emergency mission covers owner `africa_rsa_continental_side`, category `africa_rsa_emergency_category`, Pretoria/Transvaal/Cape/Natal requirements, mine-port/negotiator/settlement prerequisites, and failure on deadline. Duplicate risk is controlled by global emergency flags.

## Validation

- Reviewed the decision diff after an accidental formatting drift and restored the decision file before reapplying only the intended lines.
- Focused diff review confirms the gameplay edit is limited to the two Charter member decisions and their two tooltip strings.

## Recommended Next Main-Agent Patch

Upgrade `africa_influence_charter_member` and `africa_docket_authority_integration` from flat PP actions into active Charter operations. The least disruptive patch is to add small support equipment/manpower/logistics or local-trust costs through existing constants and require a short timed outcome mission or existing regional mandate signal, while keeping their current AI target checks and localisation structure.
