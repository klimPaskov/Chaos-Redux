# Event 005 Localisation Audit Handoff

**Date:** 2026-07-11
**Role:** Chaos Redux Event 005 localisation auditor
**Bounded tranche:** Command and Corridors, live corridor targeting, selected republic desks, terminal reclamation and aid, release causes, UWR contamination hooks, and KMB treaty and concession hooks
**Commit:** None

## Outcome

The bounded localisation surface is internally aligned with the current scripted mechanics after small localisation-only corrections.

No gameplay, interface, GFX, asset, AI, event, decision, trigger, effect, constant, or scripted-localisation file was edited by this audit. Parent-owned exact-cost gate corrections landed concurrently and were verified in the final shared tree.

## Required references consulted

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- Offline wiki pages for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding
- Vanilla `common/decisions/_documentation.md`
- Vanilla `documentation/loc_objects_documentation.md`
- Vanilla `documentation/script_concept_documentation.md`
- Vanilla `common/script_constants/documentation.md`
- Relevant official effect and trigger documentation entries
- Current Event 005 command, corridor, selected-target, and UWR/KMB audit handoffs

## Files changed by this audit

- `localisation/english/005_soviet_collapse_l_english.yml`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_07_11_soviet_localisation_audit.md`

## Localisation corrections

### Command and Corridors

- `soviet_collapse_corridors_and_depots_compromise_cost_text_tooltip`
  - Added the live corridor file requirement that is part of the actual cost gate.
- The following 21 mission requirement keys now state which live corridor project must remain valid while the mission is active:
  - `soviet_collapse_soviet_mission_005_count_the_missing_trains_req_tt`
  - `soviet_collapse_soviet_mission_006_freeze_unapproved_transfers_req_tt`
  - `soviet_collapse_soviet_mission_017_restore_the_central_supply_seal_req_tt`
  - `soviet_collapse_soviet_mission_034_secure_the_last_loyal_rail_spine_req_tt`
  - `soviet_collapse_soviet_mission_038_publicly_recover_a_lost_depot_req_tt`
  - `soviet_collapse_soviet_mission_043_prove_the_depots_can_be_retaken_req_tt`
  - `soviet_collapse_soviet_mission_046_break_the_defense_committees_supply_req_tt`
  - `soviet_collapse_soviet_mission_047_keep_the_next_declaration_unarmed_req_tt`
  - `soviet_collapse_soviet_mission_053_send_political_officers_to_the_rail_junctions_req_tt`
  - `soviet_collapse_soviet_mission_056_gather_the_armored_train_crews_req_tt`
  - `soviet_collapse_soviet_mission_061_seal_the_smolensk_ledger_req_tt`
  - `soviet_collapse_soviet_mission_062_recount_the_ukrainian_depots_req_tt`
  - `soviet_collapse_soviet_mission_063_guard_the_belarusian_rail_net_req_tt`
  - `soviet_collapse_soviet_mission_068_move_the_fuel_before_the_flags_change_req_tt`
  - `soviet_collapse_soviet_mission_069_guard_the_ammunition_census_req_tt`
  - `soviet_collapse_soviet_mission_091_western_gate_discipline_req_tt`
  - `soviet_collapse_soviet_mission_094_the_tashkent_anchor_req_tt`
  - `soviet_collapse_soviet_mission_098_kazakhstan_must_not_be_first_req_tt`
  - `soviet_collapse_soviet_mission_099_siberian_distance_command_req_tt`
  - `soviet_collapse_soviet_mission_106_prove_the_league_cannot_protect_depots_req_tt`
  - `soviet_collapse_soviet_mission_127_inventory_the_recovered_depots_req_tt`
- The wording follows the exact project gate used by each mission:
  - Seven rail projects require the selected corridor to support rail work.
  - Three logistics projects require the selected corridor to support a supply, rail, port, or border logistics project.
  - Eight depot projects require the selected corridor to contain a supply node.
  - Three border projects require the selected corridor to cover a border state.

### Category and release-cause text

- `soviet_collapse_breakaway_category_desc`
  - Replaced priority-plumbing language with in-world wording about institutions, foreign interest, Moscow's immediate response, and neighboring reactions.
- `soviet_collapse_foreign_patron_category_desc`
  - Corrected terminal aid from maintaining an existing corridor to opening a wartime corridor.

### Terminal aid

- `soviet_collapse_sustain_terminal_republic_front`
- `soviet_collapse_sustain_terminal_republic_front_desc`
- `soviet_collapse_sustain_terminal_republic_front_req_tt`
- `soviet_collapse_sustain_terminal_republic_front_tt`

The user-facing action is now titled **Open a Wartime Republic Corridor**. Its text states that the selected republic must be at war with Moscow, must not be at war with the sponsor, must not already have an open corridor, must have a political or logistics contact, and must have clear basic and major aid cooldowns. This matches `can_target_soviet_collapse_terminal_republic_front` and the reused aid-corridor application effect.

### UWR and KMB hooks

- `UWR_field_release_doctrine_desc`
- `UWR_chaos_warfare_path_desc`
  - Both now state the first-time state hook exactly. Each newly marked neighboring state adds 3 Armed Breakaway Momentum and 2 Foreign Penetration while the Union crisis remains active.
- `kmb_sign_resource_treaty_tt`
  - Now states 4 Depot Control for KMB, then 2 Soviet Depot Vulnerability and 1 Foreign Penetration while the Union crisis remains active.
- `kmb_force_mining_concession_tt`
  - Now states 4 Soviet Depot Vulnerability, 3 Armed Breakaway Momentum, and 2 Foreign Penetration while the Union crisis remains active.

## Mechanical alignment evidence

### Compromise actions

The visible costs and deltas match the final constants and effects:

| Decision | Cost | Visible outcome |
|---|---:|---|
| `soviet_collapse_broker_provisional_command_compact` | 15 Command Power | Moscow Authority +1, Command Obedience +1, Armed Breakaway Momentum +2 |
| `soviet_collapse_accept_emergency_corridor_board` | 35 Political Power | Moscow Authority -2, Depot Vulnerability -2, Foreign Penetration +1, League Cohesion +2 |
| `soviet_collapse_offer_interim_republic_statute` | 50 Political Power | Moscow Authority -2, Armed Breakaway Momentum -2, Foreign Penetration +1, League Cohesion +2 |

All three resolve exactly one active mission in their family, avoid the current mission's failure record, do not register a decisive success, and use the 28-day response re-enable value.

### Release causes

`GetSovietCollapseReleaseCause` has one ordered branch for each mutually exclusive release flag and one fallback. `soviet_collapse_clear_release_cause_flags` clears all four flags before the dominant-cause branch sets one.

The recorded cause consumers match the category summary:

| Cause | Opening package | Sponsor interest | Moscow next priority | Neighbor reaction |
|---|---|---:|---|---|
| Command Fracture | Local Authority Pressure +4, one extra field unit | 0 | Chain of Command | Neighbor Local Authority Pressure +1 |
| Corridor or Depot Loss | Depot Control +5, one extra field unit | 1 | Corridors and Depots | Neighbor Depot Control +1 |
| Negotiated Political Break | Institution Strength +5, Independence Resilience +4 | 1 | Republic Settlement | Neighbor Institution Strength +1 |
| Foreign or League-Backed Rupture | Liaison Reach +5, Patronage Risk +4, League Support +3 | 4 | Republic Settlement | Neighbor Liaison Reach +1 |

The corresponding AI strategy entries are gated by the same four cause triggers.

### Selected-target disabled states

Nineteen newly added requirement-tooltip call sites were checked against their current target and resource triggers:

- Six basic-aid call sites
- Three major-aid call sites
- One volunteer-aid call site
- Two construction-aid call sites
- One aid-corridor call site
- One League-aid call site
- One protection-treaty call site
- One adviser-privileges call site
- One client-cabinet call site
- One terminal republic-front call site
- One terminal reclamation call site

The shared wording covers registration, selected target state, wars, routes or contacts, sponsor and recipient cooldowns, dependency prerequisites, target acceptance, and the separately displayed resource cost as applicable.

### Terminal reclamation and aid

- Reclamation displays and spends 36,000 fuel and 8 trains.
- Parent-owned final gate constants use `35999.99` fuel and `7` trains with strict `>` checks, so the exact displayed reserve is sufficient.
- Reclamation has a 70-day decision re-enable value.
- It damages one valid original Union state controlled by the selected republic. It prioritizes a supply node, then a railway, then infrastructure.
- Its disruption trace flag lasts 90 days.
- Terminal corridor aid uses the existing target-tier package:
  - Base target: 12,000 fuel, 4 trains, 4 convoys
  - Regional target: 18,000 fuel, 6 trains, 6 convoys
  - Major target: 26,000 fuel, 8 trains, 8 convoys
- Parent-owned final gate constants use one fixed-point or integer sentinel below each displayed amount, so the exact displayed reserve is sufficient.
- The decision has a 45-day re-enable value. The applied aid package also sets the existing 45 and 60 day general sponsor and recipient cooldowns, plus the 90 and 120 day major sponsor and recipient cooldowns.
- The effect opens the target's persistent aid-corridor flag. The corrected localisation no longer describes it as sustaining a corridor that must already exist.

## Selector, key, encoding, and asset proof

- All 80 visible keys changed in the current Event 005 working diff resolve exactly once across English localisation.
- `GetSovietCollapseOperationalPriority`, `GetSovietCollapseCorridorTargetStatus`, and `GetSovietCollapseReleaseCause` each have exactly one definition.
- All 164 localisation keys referenced by Event 005 scripted localisation resolve exactly once across English localisation.
- The operational-priority effect clears all three display flags before one `if`, `else_if`, or `else` branch sets a single flag.
- The selected corridor selector has one validated-target branch and one absent-target fallback.
- The English file begins with the UTF-8 BOM bytes `EF BB BF`.
- The five added decisions use five sprites that each have one definition in `interface/005_soviet_collapse.gfx`:
  - `GFX_decision_soviet_collapse_command_goal`
  - `GFX_decision_soviet_collapse_rail_goal`
  - `GFX_decision_soviet_collapse_cleanup_goal`
  - `GFX_decision_cut_rebel_supply_routes`
  - `GFX_decision_soviet_collapse_foreign_intelligence`
- Every referenced DDS exists under `gfx/interface/decisions/005_soviet_collapse/`.
- No new mission icon was introduced. The 21 corridor missions retain their registered Event 005 mission sprites.

## Remaining risks

- This was a static localisation audit. It did not execute the game UI, so final line wrapping and live tooltip refresh behavior were not observed here.
- No unresolved missing key, duplicate key, selector collision, encoding fault, sprite registration gap, DDS gap, or mechanic-to-wording mismatch remains in the bounded audited surface.

## Simplifications, omissions, and blockers

- No fallback or simplification was used.
- No requested localisation surface was omitted.
- No remaining localisation blocker was found.
- Gameplay-side exact-cost gate mismatches found during the audit were corrected by the parent in centralized constants and shared payment triggers before this handoff was finalized.
