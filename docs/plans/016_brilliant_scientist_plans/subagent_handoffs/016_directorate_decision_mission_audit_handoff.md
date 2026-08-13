# Event 016 Directorate decision and mission audit handoff

## Audit identity

- Date: 2026-07-16
- Mode: patch-capable decision and mission audit
- Scope: Event 016 host Directorate institutions, facilities, foreign liaison, category, modifiers, constants, localisation, and system documentation
- Explicit exclusions: the project-board decision file, opening and Kruger identity, shared Event 016 gameplay files, focus trees, specs, and all other Event 016 surfaces
- Skills used: `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`

The owned slice is structurally sound after the local corrections recorded below. Two outcome consumers and one UI status remain parent-owned integration work; those gaps prevent this handoff from claiming the complete Host Management acceptance section.

## Files reviewed

- `common/decisions/016_brilliant_scientist_directorate_institutions.txt`
- `common/decisions/016_brilliant_scientist_directorate_facilities.txt`
- `common/decisions/016_brilliant_scientist_directorate_foreign.txt`
- `common/decisions/categories/016_brilliant_scientist_directorate_categories.txt`
- `common/dynamic_modifiers/016_brilliant_scientist_directorate_modifiers.txt`
- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
- `localisation/english/016_brilliant_scientist_directorate_l_english.yml`
- `docs/events/016_brilliant_scientist/systems/directorate.md`

## Identifiers reviewed

### Institutions, staff, priorities, security, and authority

- `brilliant_scientist_convene_public_science_council`
- `brilliant_scientist_establish_compartmentalized_military_office`
- `brilliant_scientist_grant_private_industrial_concession`
- `brilliant_scientist_assemble_exile_scholar_network`
- `brilliant_scientist_recruit_research_cohort`
- `brilliant_scientist_charter_university_research_network`
- `brilliant_scientist_prioritize_fundamental_inquiry`
- `brilliant_scientist_prioritize_prototype_delivery`
- `brilliant_scientist_prioritize_distributed_replication`
- `brilliant_scientist_establish_internal_security_section`
- `brilliant_scientist_rotate_security_clearances`
- `brilliant_scientist_conduct_loyalty_review`
- `brilliant_scientist_loyalty_review_mission`
- `brilliant_scientist_lay_false_procurement_trails`
- `brilliant_scientist_establish_cabinet_safety_board`
- `brilliant_scientist_delegate_technical_authority`
- `brilliant_scientist_grant_final_technical_authority`

### Facilities

- `brilliant_scientist_formalize_primary_research_campus`
- `brilliant_scientist_expand_primary_prototype_works`
- `brilliant_scientist_establish_secondary_laboratory`
- `brilliant_scientist_relocate_primary_laboratory`
- `brilliant_scientist_harden_primary_laboratory`
- `brilliant_scientist_mobilize_primary_laboratory_repairs`

### Foreign liaison

- `brilliant_scientist_review_foreign_approaches`
- `brilliant_scientist_offer_controlled_research_access`
- `brilliant_scientist_open_joint_laboratory`
- `brilliant_scientist_accept_foreign_protection_framework`
- `brilliant_scientist_restrict_foreign_research_access`
- `brilliant_scientist_terminate_foreign_research_frameworks`

## Corrections made

### Timed country-flag cooldowns

Before the audit, three priority switches and the primary-relocation producer copied a script constant into a temporary variable and passed that variable to `set_country_flag = { days = ... }`. This field is a known sensitive duration field and may reject both script-constant and variable tokens.

After the audit:

- the three priority switches use `@brilliant_scientist_priority_cooldown_days = 180`;
- relocation uses `@brilliant_scientist_relocation_cooldown_days = 365`;
- the file-scoped values are explicitly cross-referenced beside their matching `brilliant_scientist_directorate_timing` entries;
- the system documentation records why both copies must be tuned together.

The complete owned-file scan found no other timed country flags. No stale `brilliant_scientist_directorate_cooldown_days` temporary-variable use remains.

### State-target requirement localisation

The two state-target descriptions previously summarized valid destinations as having “existing industry” and “adequate infrastructure.” They now name the actual eligibility gates:

- the secondary laboratory requires a fully controlled core state, at least two Infrastructure levels, a Civilian Factory or Military Factory, and either a home-area connection or a Supply Hub;
- relocation requires another fully controlled core state, at least two Infrastructure levels, a Civilian Factory or Military Factory, and either a home-area connection or a convoy-supported Naval Base.

The construction tooltips already matched the effects: primary campus and secondary laboratory add one Infrastructure, prototype works adds one Military Factory, hardening adds one Anti-Air installation and one Land Fort, and relocation adds no buildings.

## Acceptance evidence

### Causal state

The owned decisions call the shared measure helpers at the following frequencies:

| Measure | Decision-side helper calls |
| --- | ---: |
| Mandate | 14 |
| Dependence | 18 |
| Exposure | 23 |
| Project Capacity | 22 |
| Independent Capacity | 9 |
| Grievance | 14 |

These calls span institutional form, staffing, priorities, facilities, security, authority, and foreign liaison. The four visible values are therefore not decorative counters, and the two hidden values have multiple independent causes.

### Costs, burdens, and map state

- Facility construction and hardening consume equipment, fuel, or logistics, occupy time, and impose active consumer-goods or production-efficiency burdens.
- The secondary laboratory and relocation use bounded `any_owned_state` targeting with daily root and target prechecks; they do not scan the entire world.
- Relocation consumes trucks and fuel, consumes convoys on the sea route, records origin and destination, and grants no building, slot, prototype, or project-stage reward.
- Staffing and internal security consume manpower, support equipment, logistics, time, or active industrial burden where appropriate.
- Governance and liaison actions use time and continuing political or industrial trade-offs rather than acting as a repeatable Project Capacity purchase.
- The explicit foreign-approach refresh is player/AI initiated. There is no daily, weekly, or monthly global on-action in the owned slice.

### Lifecycle and repeatability

- Campus, prototype works, secondary laboratory, hardening, institution, staffing, security-section, and authority construction is one-use or protected by persistent completion flags.
- Controlled access, joint laboratory, and foreign protection each have a lifetime establishment flag. Termination clears the active framework but does not clear its lifetime flag, preventing reopen/reward loops.
- Priority modifiers are mutually exclusive. Each priority's meter change occurs only on first adoption, while the active selection may change again after the 180-day cooldown.
- Clearance rotation, false procurement trails, repairs, foreign review, and loyalty-review initiation have re-enable timing and/or resource/industrial burdens.
- All fourteen persistent Directorate dynamic modifiers require `brilliant_scientist_is_current_host` and remove themselves when that condition is lost.

### AI

All 28 selectable decisions have `ai_will_do`. Their modifiers read relevant government, route flags, war state, Exposure, Project Capacity, Independent Capacity, Government Control, intelligence capability, or resource/target availability. `brilliant_scientist_loyalty_review_mission` is the twenty-ninth decision entry and is intentionally non-selectable, activated only by `brilliant_scientist_conduct_loyalty_review`.

The two map decisions rely on the same target eligibility as the player. Relocation has low base interest, increases at war, and is discouraged under stable control. Loyalty review has low base interest, increases under compromised control or high Exposure, and values an existing intelligence agency.

### Loyalty-review guard regression

Verified exactly:

- `brilliant_scientist_rotate_security_clearances` is blocked only by `brilliant_scientist_security_action_in_progress`; it does not test `brilliant_scientist_directorate_loyalty_review_requested`.
- `brilliant_scientist_conduct_loyalty_review` tests both the shared in-progress flag and `NOT = { has_country_flag = brilliant_scientist_directorate_loyalty_review_requested }`.

Pending findings therefore block another loyalty review without incorrectly blocking clearance rotation.

## Required parent integration

### Loyalty-review outcome consumer

The mission currently produces a coherent request packet but no owned or shared consumer exists. Implement country-scope scripted effect `brilliant_scientist_resolve_directorate_loyalty_review_request`, then call it as the final gameplay instruction in `brilliant_scientist_loyalty_review_mission.timeout_effect`, immediately after the request context and tooltip are written:

```txt
brilliant_scientist_resolve_directorate_loyalty_review_request = yes
```

The resolver must require `brilliant_scientist_directorate_loyalty_review_requested`, use the saved visible/hidden meter snapshots, project-stage counts, intelligence score, intelligence evidence flags, and project-history flags, select a weighted narrative result, and then clear every request flag, evidence flag, and snapshot variable. It must not guarantee an Exposure reduction or capturable operative on every review.

Until this consumer is wired, the request flag intentionally blocks another loyalty review and remains pending; clearance rotation remains available.

### Relocation outcome consumer

The relocation timer currently produces a coherent request packet but no owned or shared consumer exists. Implement country-scope scripted effect `brilliant_scientist_resolve_directorate_relocation_request`, then call it as the final gameplay instruction in `brilliant_scientist_relocate_primary_laboratory.remove_effect`, immediately after both request targets and the tooltip are written:

```txt
brilliant_scientist_resolve_directorate_relocation_request = yes
```

The resolver must revalidate `event_target:brilliant_scientist_relocation_requested_origin` and `_destination`, use the route/under-fire flags and saved meter/project snapshots, and choose among weighted transfer, interception, prototype loss, staff refusal, or escape outcomes. Success moves only the primary-facility state flag, facility-type variable, and global target. Every terminal result must clear the request flag, route and under-fire flags, both request targets, and all relocation snapshot variables. It must grant no buildings, slots, facilities, prototypes, project stages, or equipment.

Until this consumer is wired, `brilliant_scientist_directorate_relocation_requested` intentionally blocks a second relocation and leaves the recorded request pending.

### Broad Government Control display and cause breakdowns

The category description currently exposes the four raw visible values but does not show the required broad Government Control label. The shared Event 016 effect/trigger layer already computes and exposes `brilliant_scientist_control_stable`, `_strained`, `_compromised`, and `_lost`; the missing surface is a scripted-localisation selector plus category-description call, which is outside this audit's owned files. Add a selector that returns only the broad label and never the hidden arithmetic.

The full Host Management acceptance file also asks for cause breakdowns for Mandate, Dependence, and Exposure. The owned category text explains what each value means but does not dynamically enumerate its current causes. That UI/shared-state work was not expanded inside this bounded decision audit.

## Validation performed

- Compared all state-target building and route triggers against player-facing descriptions and effect tooltips.
- Confirmed the four sensitive timed flags use file-scoped literals and that the mirrored values remain 180 and 365 in the script-constant table.
- Confirmed 28 `ai_will_do` blocks for 28 selectable decisions; the only decision entry without one is the activated, non-selectable loyalty mission.
- Confirmed all 29 decision/mission identifiers and all 14 dynamic-modifier identifiers have English names, and every decision/mission has a description.
- Confirmed all six measure helpers have multiple decision-side callers.
- Confirmed all fourteen persistent Directorate modifiers self-remove when the country stops being the current host.
- Confirmed the loyalty-review pending flag appears in the review guard and not in the clearance-rotation guard.
- Confirmed neither required request-resolver symbol exists in gameplay script, while both producer packets and their documented contracts are present.
- Verified the edited English localisation remains UTF-8 with BOM.

Live engine execution was not performed by this subagent. The remaining resolver work requires parent-owned narrative/effect implementation before relocation and loyalty-review outcomes can be considered end-to-end complete.

## Simplifications, omissions, and risks

- No fallback or substitute mechanic was introduced.
- No project-board, focus-tree, identity, shared gameplay, or spec file was edited.
- Loyalty review and relocation remain producer-only adapters until the parent implements and wires their consumers exactly as above.
- Broad Government Control status and dynamic cause breakdowns remain missing from the player-facing category.
- Host transfer and terminal cleanup of Directorate route/framework flags remain shared lifecycle responsibilities and were not edited or end-to-end audited here.
- No unrelated working-tree change was staged or adopted.
