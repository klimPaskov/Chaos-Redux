# Event 017 Decision and Mission Audit Handoff

- Date: 2026-07-10
- Subagent: `chaosx_decision_mission_auditor`
- Mode: audit plus bounded patch
- Commit: none

## Outcome

The Event 17 decision map now covers all eleven specified decision or mission families with holder-specific visibility, exact resource gates, effect-time target revalidation, active mission objectives, outcome-matched localisation, and AI behavior informed by ideology, relations, war and threat state, geography, and neutrality resilience.

The parent agent's live selection, pressure-source, option-preservation, join-order, and evolution scheduling refactors were preserved. The only intentional insertion into the refactored join path is `random_faction_prepare_stabilize_alignment_cost = yes` immediately after `random_faction_apply_alignment_shock = yes`.

## Files Changed

- `common/decisions/017_random_faction_decisions.txt`
- `common/script_constants/chaosx_random_faction_constants.txt`
- `common/scripted_effects/017_random_faction_effects.txt`
- `common/scripted_triggers/017_random_faction_triggers.txt`
- `common/scripted_localisation/017_random_faction_scripted_localisation.txt`
- `localisation/english/017_join_faction_l_english.yml`
- `docs/events/017_random_faction.md`
- this handoff

`common/decisions/categories/017_random_faction_categories.txt` was audited and did not require a patch. Its category visibility delegates to the holder-aware scripted trigger, and the category has no unrelated permanent visibility condition.

## Decision and Mission Changes

### Newly aligned minors

- `random_faction_stabilize_alignment`
  - Snapshots Political Power and support-equipment costs at accession from `num_of_controlled_states`.
  - Political Power scales from 25 to 70 and support equipment from 60 to 180.
  - Wartime accession snapshots an additional 15 Command Power and 2% War Support cost.
  - Removes both accession spirits, reduces pressure, improves Stability and mutual leader relations, and lowers faction cohesion strain.
- `random_faction_request_liaison`
  - Implements the paired cost: the minor pays 15 Command Power and the current faction leader provides 60 support equipment.
  - Revalidates the leader before either side pays.
  - Adds liaison coordination, leader-specific pull and dependency, mutual relations, and distinct supported-minor tracking.
- `random_faction_quiet_opposition`
  - Uses exact Political Power, infantry-equipment, Stability, and conditional War Support gates.
  - Reduces shock and pressure.
  - Adds a dynamic 10% to 50% Bloc Polarization backlash roll based on Stability and Evolution II/III state.

### Pressured neutrals

- `random_faction_convene_neutrality_council`
  - Raises resilience, lowers immediate pressure, and snapshots the border objective before mission activation.
- `random_faction_reinforce_border_posts`
  - Names a controlled frontier state, or the capital when the country has no controlled land frontier.
  - Records the launch-time garrison and requires at least one additional division in that exact state, 450 infantry equipment in reserve, and continued capital/state control.
  - Existing divisions cannot complete the mission passively.
  - Success and timeout now change both pressure and resilience in the documented directions.
- `random_faction_invite_observers`
  - Requires a valid reachable faction leader.
  - Records that leader as the pressure source, adds leader-specific pull, lowers resilience through dependency, improves mutual relations, and applies rival-opinion backlash when another valid leader exists.
- `random_faction_publish_neutrality`
  - Raises resilience and reduces immediate pressure with exact Political Power and Stability gates.

### Faction leaders

- `random_faction_offer_staff_mission`
  - Requires a valid reachable target and applies a 180-day target cooldown.
  - Stabilizes aligned faction members or adds leader-specific pull and dependency to pressured neutrals.
  - Improves relations and records distinct supported-minor progress.
- `random_faction_radio_networks`
  - Replaces the decision's `every_country` scan with `for_each_scope_loop` over `global.random_faction_pressure_targets`.
  - Revalidates regional reach per target before applying pressure, polarization, or supported-minor tracking.
- `random_faction_guarantee_corridor`
  - Requires a valid reachable target and stores the target before activating the mission.
  - Snapshots the current train stockpile at launch.
- `random_faction_guarantee_corridor_mission`
  - Is a 120-day active objective requiring a still-valid route and target, at least 15 convoys, and five trains added after launch.
  - A pre-existing route or stockpile cannot complete it passively.
  - Invalid target/route state cancels immediately without a reward.
  - Success and failure now apply distinct relation, pressure, dependency, and rival-pull outcomes.
- `random_faction_demand_commitment`
  - Requires a valid reachable pressured target and revalidates before payment.
  - At the collapse threshold it dispatches the shared faction-choice path.
  - Refusal raises resilience, damages relations with the demanding leader, and can shift the pressure source toward another valid faction leader.

## AI Audit

The decision AI now uses centralized weights and factors from `chaosx_random_faction_constants.txt`.

- Stable democratic and neutral countries favor the council and public neutrality.
- Fascist and communist countries favor coercive opposition, radio, and commitment routes.
- Targeted actions evaluate ideology match, mutual opinion, neighbor or coastal reach, war/threat state, and low or high neutrality resilience.
- Staff and corridor AI prefer nearby or threatened low-resilience targets and discount high-resilience targets.
- Commitment demands remain low-base aggressive actions, with democratic use strongly discouraged.
- Radio multi-target evaluation uses the Event 17 target array and does not introduce a periodic country-wide scan.

## Cleanup and Exploit Controls

- New Stabilize cost variables and wartime flags are cleared by full pressure cleanup and pre-join retirement.
- Border state, garrison floor, and displayed requirement variables clear on success, timeout, cancellation, retirement, and full cleanup.
- Corridor train floor and target variables clear on success, failure, cancellation, leader cleanup, retirement, and full cleanup.
- Staff missions use a target-local 180-day cooldown matching the liaison duration, closing the previous 90-day repeat-farming window.
- Targeted effects perform target and cost revalidation before payment.
- Rival selection uses short-lived regular event targets and a transient country flag that is removed in the same effect.

## Validation Evidence

- All six touched Clausewitz script files have balanced brace counts.
- The decision file contains the complete eleven-family map: three aligned-minor actions, four neutral actions including the border mission, and four leader families including the corridor action/mission pair.
- Every decision tooltip and custom-cost localisation reference resolves. The Event 17 localisation file has 169 unique keys and no duplicates.
- `017_join_faction_l_english.yml` retains its UTF-8 BOM.
- Stabilize snapshots after faction entry; both mission snapshots are prepared before mission activation.
- The radio decision effect iterates `global.random_faction_pressure_targets`; it contains no `every_country` scan.
- Neither mission relies on the ineffective mission `visible` field.
- No unsupported `<=` or `>=` operators were introduced.

## Remaining Risks

- Final whole-event integration validation remains with the parent agent because the parent was concurrently changing Event 17 core routing and lifecycle code.
- The active objectives use variable-valued numeric comparisons for `divisions_in_state` and `has_equipment`, consistent with the engine's dynamic-value system. These fields should receive extra attention in the parent's final integration pass because vanilla provides fixed-value examples more often than variable-valued examples.

## Simplifications, Omissions, and Blockers

- Simplifications: none.
- Omitted decision or mission families: none.
- Missing costs, AI behavior, localisation, target revalidation, or cleanup in the bounded decision surface: none known.
- Blockers: none.
