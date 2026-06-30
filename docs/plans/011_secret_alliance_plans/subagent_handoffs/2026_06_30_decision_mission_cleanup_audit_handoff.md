# Event 011 Secret Alliance Decision/Mission Cleanup Audit

Date: 2026-06-30
Owner: Chaos Redux decision and mission subagent

## Scope Read Directly

- `docs/specs/011_secret_alliance_specs/` specs, matrices, prompts, routing, and manifest files.
- Event 011 implementation files requested by the parent, including decision categories, decisions, scripted effects/triggers/constants, scripted GUI, GUI layout, event file, localisation, and event docs.
- Relevant offline Paradox wiki pages for decisions, scripted GUI, effects, triggers, localisation, scopes, and data structures.
- Existing mod/vanilla decision precedents for custom costs, missions, AI weights, and category GUI usage.

Repo note: no Chaos Redux `AGENTS.md` was found in the repository or immediate parents by direct file search. The only `AGENTS.md` found was `C:\Users\klimp\Documents\Paradox Wiki\AGENTS.md`, which was read but is wiki-specific.

## Changed Files

- `common/scripted_effects/011_secret_alliance_effects.txt`

## Changed Identifiers

- Added/used `secret_alliance_close_compact_state`
- Updated `secret_alliance_cleanup_invalid_members`
- Updated `secret_alliance_select_public_leader`
- Updated `secret_alliance_expose_random_hidden_member`
- Updated `secret_alliance_reveal_public_pact`

## Before/After Behavior

- Before: if invalidation left the compact with zero valid members, cleanup cleared only some global reveal flags and mission flags. The target could keep stale `secret_alliance_target`, dossier/counterplay flags, ideas, arrays, and event targets, keeping decision surfaces alive after the compact was gone.
- After: zero-member cleanup closes the compact fully: target/category flags, active/reveal globals, target ideas, member flags, arrays, and selected/patron/public-leader/war event targets are cleared.

- Before: public reveal preferred a patron, then only a founder fallback. If founders had been removed but invited members still existed, public faction creation could fail despite valid public members.
- After: public reveal still prefers a valid patron, then a valid founder, then any valid public member.

- Before: random exposure incremented `pact_known_member_count` even if no hidden member remained, and public reveal exposed all remaining members without syncing the known count to total membership.
- After: random exposure increments only when an eligible hidden member exists, and public reveal sets `pact_known_member_count = pact_member_count`.

## Validation Performed

- Brace count on `common/scripted_effects/011_secret_alliance_effects.txt`: `opens=1058 closes=1058 balanced=True`.
- Custom cost localisation coverage scan: 23 unique `custom_cost_text` keys in `common/decisions/011_secret_alliance_decisions.txt`. No base or `_blocked` keys are missing in `localisation/english/011_anti_player_pact_l_english.yml`.
- Direct scans confirmed:
  - founder count gating via `secret_alliance_has_three_founder_candidates`
  - founders, minor invites, and patrons block war with target through `NOT = { has_war_with = ROOT }`
  - war relation on-action calls `secret_alliance_on_war_relation_added`
  - reveal path calls `secret_alliance_call_public_members_to_target_war`
  - mission timers use the varied constants 90, 120, 105, 150, and 120 days
  - dossier category attaches `scripted_gui = secret_alliance_dossier_board_scripted_gui`
  - decision costs use custom cost triggers and AI weights across the decision surface.

Skipped: in-game HOI4 load validation. This session did not launch the game parser/runtime.

## Audit Findings

### Fixed High

- Stale compact cleanup after all members become invalid. This could leave dossier/counterplay category visibility, target ideas, arrays, and event targets active after the compact had effectively collapsed.

### Fixed Medium

- Public reveal could fail to create a public pact if only non-founder invited members remained valid.
- Dossier Board known-member count could overcount after repeated random exposure attempts with no eligible hidden member, or undercount after public reveal.

### Remaining Medium

- Missions are functional and have success/failure, varied durations, and active-mission gating, but their map requirements are abstract. They use total division/equipment/fuel and preparatory flags rather than checking actual assigned divisions in named capital, industrial, route, or border states.
- If the public pact leader later capitulates or becomes invalid while other public members remain, the system records public-member validity but does not reselect or transfer public leadership.

### Remaining Low

- Dossier Board meters show dynamic text values, but the GUI sprites are hardwired to `GFX_secret_alliance_*_meter_fill_75`, so visual fill state does not match current evidence/pressure/preparedness.
- Both Event 011 categories use `visible_when_empty = no`. This is mostly fine because decisions/missions usually populate the categories, but it means the Dossier Board may disappear if all decision entries are hidden by stage/cooldown conditions.
- Several AI weights are valid but coarse. They use constants and condition modifiers, but not every choice scales deeply by target/member score state.

## Mission Quality Notes

- `guard_capital_network_mission`: owner target, dossier category, capital network region, and 90 day duration. Success uses `secret_alliance_guard_capital_network_success`, failure uses `secret_alliance_guard_capital_network_failure`, and duplicate risk is low because active mission flags gate repeats. The requirement is total divisions plus a prior hardening or vetting flag.
- `secure_industrial_belt_mission`: owner target, dossier category, industrial belt region, and 120 day duration. The success and failure effect pair is present, duplicate risk is low, and the requirement is military factories, total divisions, and hardening or sabotage flags.
- `keep_foreign_route_watched_mission`: owner target, dossier category, foreign route region, and 105 day duration. The success and failure effect pair is present, duplicate risk is low, and the requirement is trains plus courier, sabotage, or infiltration state.
- `expose_patron_hand_mission`: owner target, counterplay category, patron network region, and 150 day duration. The success and failure effect pair is present, duplicate risk is low, and the requirement needs high evidence, a patron, and a supporting counterplay, route, or leak flag.
- `hold_border_public_crisis_mission`: owner target, counterplay category, public border crisis region, and 120 day duration. The success and failure effect pair is present, duplicate risk is low, and the requirement is total divisions plus fuel, preparation, or border flags.

## Cost And Requirement Clarity

- Event 011 no longer reads as a passive political-power store. Costs vary across CP, PP, stability, army/air XP, support equipment, infantry equipment, trains, trucks, fuel, and manpower.
- Custom cost text exists for all scanned cost keys, including blocked variants.
- Costs are constant-driven and varied, but mostly not dynamically scaled by country size. That is acceptable for the current local pass but remains a balance-depth limitation.

## AI Validity And Route-Lock Notes

- Founder, minor invite, patron, member-validity, and public-faction triggers block dead targets, capitulated actors, subjects where appropriate, special/nonhuman countries, same-faction-with-target cases, and war-with-target candidates.
- Human-only Dossier Board scripted GUI is acceptable because gameplay actions are represented as decisions with AI weights. GUI card buttons only set selection event targets.
- AI action weights exist for the decision surface and use route/state modifiers, but some remain broad `low/medium/high` constants.

## Localisation And Tooltip Gaps

- Cost localisation coverage passed for the decision custom-cost keys.
- Dynamic public pact target naming and Event Details text are present in the inspected localisation/docs.
- Remaining GUI gap: meter fill sprites are not dynamically selected by current values.

## Cleanup And Exploit-Risk Notes

- Fixed the main stale-state cleanup risk for a compact with no valid members.
- Active mission flags and mission start helpers limit mission spam.
- No free-unit, equipment-farming, core-spam, or repeated war-goal reward loop was found in this decision/mission pass.
- Remaining exploit/edge risk: public leader invalidation after faction creation may leave faction behavior less deterministic until a broader public-pact lifecycle pass handles leadership transfer.
