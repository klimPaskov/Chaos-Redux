# Event 012 Africa Decision and Mission Audit Handoff

Date: 2026-06-16
Agent role: Chaos Redux decision and mission subagent

## Scope

Audited the current Event 012 Africa decision and mission surfaces, with emphasis on the true timed missions in `common/decisions/012_africa_decisions.txt`, supporting script constants, effects, triggers, focus unlocks, localisation, and docs.

Required references consulted:

- `AGENTS.md`
- offline Paradox wiki core pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- vanilla decision docs/examples: `~/projects/Hearts of Iron IV/common/decisions/_documentation.md`, mission examples from vanilla decisions, `effects_documentation.md`, `triggers_documentation.md`, `script_concept_documentation.md`, `common/script_constants/documentation.md`
- skills: `hoi4-decisions-missions`, `chaos-redux-events`, `chaos-redux-subagents`, `hoi4-focus-trees`

## Files Changed

- `common/decisions/012_africa_decisions.txt`
- `localisation/english/012_african_union_l_english.yml`

## Changed IDs

Mission `available` tooltips added:

- `africa_liberation_front_deadline_mission`
- `africa_regional_integration_deadline_mission`
- `africa_archive_guard_deadline_mission`
- `africa_bestiary_containment_deadline_mission`
- `africa_rsa_pretoria_deadline_mission`

Localisation keys added:

- `africa_liberation_front_deadline_available_tt`
- `africa_regional_integration_deadline_available_tt`
- `africa_archive_guard_deadline_available_tt`
- `africa_bestiary_containment_deadline_available_tt`
- `africa_rsa_pretoria_deadline_available_tt`

## Patch Behavior

Before:

- The five true timed missions used raw `available` triggers for their success conditions.
- The player could see internal country flags, global flags, and variable checks as mission success requirements.

After:

- The same success triggers are wrapped in mission-specific `custom_trigger_tooltip` blocks.
- The mission lifecycle, objectives, durations, success effects, failure effects, activation flags, and cleanup flags are unchanged.
- Player-facing success requirements now summarize the objective in plain language.

## Findings By Severity

High: Regional/state target clutter remains broader than the spec.

- `africa_survey_paper_claim_state`, `africa_complete_living_core_state`, `africa_secure_integration_rail_belt`, and `africa_build_return_settlement` use `state_target = africa`.
- This is active gameplay and not a PP store, but it can still expose a large wall of state-target decisions once many African states are claimed or owned.
- The spec asks for selected-region or active-target presentation. A proper fix needs a selected-region/target-cap pattern, not a local patch.

Medium: Several missions are real timed missions but still abstracted around flags and counters instead of named map objectives.

- `africa_liberation_front_deadline_mission` checks columns, rail readiness, and war state, but does not require named front states, ports, rail hubs, or supplied divisions.
- `africa_regional_integration_deadline_mission` checks living-core and regional-authority counts, not a named regional capital or corridor.
- `africa_archive_guard_deadline_mission` checks dossier office, guard, and settlement counts, not a named old seat or map site.
- `africa_bestiary_containment_deadline_mission` checks high-chaos binding state, not a named habitat/river/forest objective.
- `africa_rsa_pretoria_deadline_mission` is the strongest route-specific mission, but still succeeds through branch flags rather than explicit Pretoria, mine-port, or rail-state control.

Medium: AI weights are present but mostly flat.

- Most decisions have `ai_will_do`, and invalid targets are usually gated by `target_array`, `target_trigger`, route flags, or resource costs.
- The weights mostly use `normal`, `preferred`, `strong`, or simple route modifiers. They do not deeply score equipment surplus, war pressure, colonial-holder strength, local state importance, or route ideology.
- This is acceptable for a foundation pass but weaker than the spec's route-aware AI goals.

Medium: Covenant Pressure is defined but not meaningfully surfaced or moved by the decision layer.

- `africa_covenant_pressure` is initialized and clamped in scripted effects and appears in the decision/UI spec.
- Current decisions mostly move `africa_mythic_pressure`, `africa_bestiary_alarm`, `africa_habitat_trust`, and `africa_mythic_volatility`.
- The visible category descriptions do not expose Covenant Pressure, and the audited decision layer does not appear to change it directly.

Low: Mission durations are varied and centralized as file constants, but not in `common/script_constants/012_africa_constants.txt`.

- `days_mission_timeout` uses file-scoped `@africa_*_mission_days` constants.
- This is valid and avoids scattered literals in the decision file, but the supporting constants file does not list the mission timers.
- If later tuning needs cross-file references or docs-generated tables, mirror them into script constants and keep the file constants only where the duration field requires `@`.

## Decision Category Lifecycle Notes

- `africa_continental_congress_category` appears from `africa_decision_layer_visible` after `africa_establish_union_start`.
- `africa_charter_league_diplomacy_category` is also tied to `africa_decision_layer_visible`; target pools are refreshed by `africa_publish_charter_register` and startup helpers.
- `africa_charter_member_category` appears for member/protected/regional/high-chaos actors and hides from the active unifier.
- `africa_liberation_war_office_category`, `africa_regional_integration_category`, `africa_diaspora_return_category`, `africa_authority_atlas_category`, `africa_high_chaos_category`, `africa_continent_sponsor_category`, and `africa_rsa_civil_war_emergency_category` are route/focus/branch gated.
- Cleanup exists in `africa_clear_runtime_context` for mission flags, arrays, selected dossier variables, and selected high-chaos package variables.
- Category lifecycle risk is mostly clutter and stale target pools, not missing visibility gates.

## Mission Quality Notes

| Mission | Owner | Category | Region | Requirement | Duration | Success | Failure | Duplicate risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `africa_liberation_front_deadline_mission` | Africa unifier | Liberation War Office | Continental war front, abstracted | Border columns, rail belt, active war | 180 days | Momentum and Cohesion rise | Colonial Alarm rises, Cohesion falls | Low duplicate risk, medium abstraction risk |
| `africa_regional_integration_deadline_mission` | Africa unifier | Regional Integration | Pan-African paper-core system | 3 living cores and 2 regional authorities | 300 days | Trust, Authority, burden relief | Trust falls, Paper-Core Burden and alarm rise | Low duplicate risk, medium passive-count risk |
| `africa_archive_guard_deadline_mission` | Africa unifier | Authority Atlas | Active dossier, abstracted | Local office, guard, settlement | 180 days | Archive Mandate and Old-Seat Legitimacy rise | Restoration Debt and Local Sovereignty pressure rise | Low duplicate risk, medium selected-dossier clarity risk |
| `africa_bestiary_containment_deadline_mission` | Africa unifier | High-Chaos Reports | Bestiary actor network | Habitat terms, omen review, bound actor | 210 days | Habitat Trust and Nonhuman Sovereignty rise, volatility falls | Bestiary Alarm, volatility, Cohesion damage | Low duplicate risk, medium high-chaos target clarity risk |
| `africa_rsa_pretoria_deadline_mission` | RSA continental side | RSA Civil-War Emergency | South Africa branch | Mine-port belt, negotiators, settlement, victory, Allied peace | 120 days | Momentum and Legitimacy rise | Momentum falls, Colonial Alarm rises, war support falls | Low duplicate risk, strongest branch specificity |

## Cost And Requirement Clarity

- The decision layer is not a passive PP store. It uses equipment, manpower, command power gates, convoys, support equipment, state control, target arrays, route flags, living-core state checks, and timed objectives.
- Custom cost text exists for equipment/manpower/convoy costs and matches the visible non-PP costs inspected.
- Political power remains present through the standard `cost = constant:africa_decision.*` fields, but it is usually paired with non-PP requirements or concrete objectives on higher-impact decisions.
- Requirement clarity is improved by this patch for the five timed mission success conditions.

## AI Validity And Route Locks

- Most target decisions use `target_array` with candidate/member arrays and `target_trigger` checks, which avoids dead target spam when arrays are current.
- Focus/route flags gate major families: Charter mandate, general staff, courts, integrated regions, liberation office, diaspora offices, old-seat mission calendar, Bestiary route, sponsor office, and RSA branch.
- AI has nonzero weights for almost every clickable decision. The main weakness is strategic shallowness, not missing AI blocks.
- No direct disabled-evolution route lock issue was found in the audited decision file, but the broader event evolution gates were not exhaustively revalidated.

## Localisation And Tooltip Gaps

- Patched: mission success requirements now use custom tooltip keys instead of raw triggers.
- Existing category descriptions expose many core values with dynamic variables.
- Remaining gap: `africa_covenant_pressure` is documented as a core visible value but is not visible in the audited category descriptions and does not appear to be directly changed by decisions.
- Existing cost localisation is icon-first and readable.

## Cleanup And Exploit Risk

- Mission completion, timeout, cancellation, and runtime cleanup clear active mission flags.
- One-time or capped content generally has flags: raised border columns, selected dossier flags, living-core state flags, Bestiary package arrays/counts, and RSA branch flags.
- Remaining risk: repeated aid/influence decisions are cooldown-limited but not strongly diminishing. This is not an immediate exploit loop because equipment/manpower costs and cooldowns exist, but influence farming may need tapering if balance tests show it.
- Remaining risk: state-target integration can still become too broad and too cheap in late game if the player has manpower and enough selected states. The staged paper-core flow prevents instant continent-wide cores, but the presentation and per-region cap need a broader pass.

## Validation

- Verified the five new tooltip keys are referenced from `common/decisions/012_africa_decisions.txt` and defined in `localisation/english/012_african_union_l_english.yml`.
- Verified the localisation file still starts with UTF-8 BOM after the patch.
- Ran `git diff --check` on the touched decision and localisation files; no whitespace errors were reported.
- Skipped game-load validation because this subagent pass is limited to static audit and local patching.

## Remaining Recommended Fixes

1. Add a selected-region or active-target cap for broad `state_target = africa` integration and settlement decisions.
2. Upgrade at least the liberation and RSA missions to named map objectives where possible: named ports, rail hubs, mine-port belt states, Pretoria/capital control, or supplied divisions.
3. Add route/resource-aware AI modifiers for major decision families, especially high-chaos, integration, and war-office decisions.
4. Decide whether Covenant Pressure is still a live Event 012 value. If yes, expose it and make specific high-chaos decisions move it. If no, remove it from docs/spec acceptance language.
5. Consider mirroring mission duration tuning into `common/script_constants/012_africa_constants.txt` for auditability, while retaining file-scoped `@` constants if `days_mission_timeout` is kept in the decision file.

## Parent Follow-Up

After this audit, the parent pass addressed the Covenant Pressure visibility/movement finding by adding it to the High-Chaos Reports header and moving it through Bestiary unlocks, habitat terms, omen review, actor binding, and containment mission outcomes. The broad state-target presentation, map-objective depth, and route/resource-aware AI findings remain open.

## Plan Handoff

No separate broad mechanic plan was written. The remaining issues are actionable follow-up items for the parent implementation pass.
