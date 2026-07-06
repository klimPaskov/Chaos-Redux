# Event 011 Scripted System Architecture

This matrix is a source-spec consolidation of the architecture handoff. It is not code.

## Planned Files

Likely implementation surfaces:

- `events/011_secret_alliance.txt`
- `common/script_constants/011_secret_alliance_constants.txt`
- `common/mtth/011_secret_alliance_mtth.txt` or the repo-preferred MTTH file
- `common/scripted_effects/011_secret_alliance_effects.txt`
- `common/scripted_triggers/011_secret_alliance_triggers.txt`
- `common/decisions/categories/011_secret_alliance_categories.txt`
- `common/decisions/011_secret_alliance_decisions.txt`
- `common/ideas/011_secret_alliance_ideas.txt`
- `common/on_actions/011_secret_alliance_on_actions.txt`
- `common/factions/templates/011_secret_alliance_faction_templates.txt`
- `common/scripted_localisation/011_secret_alliance_scripted_localisation.txt`
- Event Logs and Event Details integration files required by `chaos-redux-events`
- super-event script, localisation, asset, sound, and docs surfaces

## Persistent State

Global event targets:

- `secret_alliance_target_player`
- `secret_alliance_leader`

Arrays:

- `global.secret_alliance_members`
- `global.secret_alliance_founders`
- `global.secret_alliance_minor_members`
- `global.secret_alliance_major_members`
- `global.secret_alliance_revealed_members`
- `global.secret_alliance_invalid_members`
- `global.secret_alliance_counter_targets`

Member flags:

- `secret_alliance_member`
- `secret_alliance_founder`
- `secret_alliance_minor_member`
- `secret_alliance_major_member`
- `secret_alliance_hidden`
- `secret_alliance_revealed`
- `secret_alliance_leader`
- role flags such as organizer, financier, border arm, intelligence node, agitator, reluctant member, major sponsor

Player flags:

- `secret_alliance_target`
- `secret_alliance_under_sabotage`
- `secret_alliance_countermeasures_unlocked`
- `secret_alliance_exposed_network`
- `secret_alliance_war_reveal_processed`

Variables:

- global: phase, member counts, exposure, cohesion, sabotage pressure, reveal pressure, pulse sequence
- player: counterintelligence, border watch, diplomatic alarm, discovered members, readiness, industrial security, active operations
- member: commitment, risk, sabotage value, recruit weight

## Constants

Use `common/script_constants/011_secret_alliance_constants.txt`.

Recommended categories:

- `secret_alliance_setup`
- `secret_alliance_membership`
- `secret_alliance_pressure`
- `secret_alliance_timing`
- `secret_alliance_ai_weight`
- `secret_alliance_decision_cost`
- `secret_alliance_border_wars`

Prefer explicit fixed-point access such as `constant:secret_alliance_membership.evo2_major_cap`.

If a field rejects script constants, assign the constant to a variable first, use a file-scoped constant in that file, or use a documented meta-effect pattern.

## MTTH Entries

Use the `hoi4-mtth` pattern where it reduces repeated AI or pacing clutter.

Candidate entries:

- `secret_alliance_recruitment_pulse_days`
- `secret_alliance_sabotage_pulse_days`
- `secret_alliance_exposure_gain`
- `secret_alliance_ai_member_action_weight`
- `secret_alliance_ai_counter_action_weight`
- `secret_alliance_reveal_pressure_days`
- `secret_alliance_major_invite_weight`
- `secret_alliance_member_defection_weight`

## Scripted Triggers

| Helper | Scope | Purpose |
| --- | --- | --- |
| `secret_alliance_target_is_valid` | player target | confirms target can own Event 011 |
| `secret_alliance_country_base_valid` | candidate | confirms normal independent country validity |
| `is_secret_alliance_founder_candidate` | candidate | checks setup founder rules |
| `is_secret_alliance_minor_recruit_candidate` | candidate | checks Evolution I and later minor recruitment |
| `is_secret_alliance_major_recruit_candidate` | candidate | checks major sponsor cap and eligibility |
| `is_secret_alliance_valid_member` | member | confirms a member remains in the pact |
| `is_secret_alliance_reveal_war_pair` | on-action participant | detects member-player war relation |
| `secret_alliance_can_reveal` | leader or target | confirms reveal can create faction and war join |
| `secret_alliance_counter_target_valid` | target country | checks selected-target decisions |
| `secret_alliance_can_start_border_operation_against_target` | target country | checks adjacency, state, war, and cooldown |
| `secret_alliance_has_minimum_members` | target or global | checks collapse floor |

## Scripted Effects

| Helper | Scope | Purpose |
| --- | --- | --- |
| `secret_alliance_initialize_context` | target player | reset stale state and save target |
| `secret_alliance_build_founder_pool` | target player | build weighted candidate pool |
| `secret_alliance_select_founders` | target player | select founders, assign organizer and roles |
| `secret_alliance_add_member_from_current_scope` | candidate | flag and array-add a member |
| `secret_alliance_refresh_member_arrays` | target or leader | prune invalid members and recompute counts |
| `secret_alliance_schedule_next_pulse` | target or leader | queue delayed event-owned pulse |
| `secret_alliance_run_hidden_pulse` | leader or target | run bounded recruit, sabotage, or report action |
| `secret_alliance_try_recruit_member` | leader or target | add minor or major based on phase |
| `secret_alliance_apply_sabotage_packet` | target player | apply damage or pressure with cooldowns |
| `secret_alliance_unlock_counter_decisions` | target player | open Evolution II category and seed targets |
| `secret_alliance_select_counter_target` | target player | set selected target |
| `secret_alliance_clear_counter_target` | target player | clear selected target |
| `secret_alliance_reveal_pact` | target or leader | reveal, log, faction, super-event, and war join |
| `secret_alliance_create_revealed_faction` | leader | create faction from template |
| `secret_alliance_join_members_to_war` | leader | add valid members to intended war |
| `secret_alliance_cleanup_all` | target player | full cleanup |

Event-specific helpers should live in Event 011 files. Add to `chaosx_dynamic_effects.md` only if a helper is generic and reused beyond Event 011.

## On-Actions

Approved narrow hook:

- `on_war_relation_added`: reveal when the player and a live pact member become enemies

Potential narrow cleanup hooks, only if needed:

- capitulation
- annexation
- peace conference ended
- faction leave
- subject status changes

Do not add recurring daily, weekly, or monthly world iteration without explicit user approval.

## Faction Reveal

Use `create_faction_from_template`.

Planned template:

- file: `common/factions/templates/011_secret_alliance_faction_templates.txt`
- template id: `faction_template_secret_alliance_pact`
- icon: `GFX_faction_logo_secret_alliance`
- name key direction: dynamic Anti-[target country] Pact if verified

Reveal order:

- refresh members
- resolve leader
- set leader faction rule if necessary
- create faction from template
- add valid members to faction
- add valid members to the intended player war
- run super-event and logs
- close hidden missions and decisions

Dynamic faction name display is a technical gate. If dynamic target-country names cannot display correctly in faction UI, do not approve a generic fallback without user input.

