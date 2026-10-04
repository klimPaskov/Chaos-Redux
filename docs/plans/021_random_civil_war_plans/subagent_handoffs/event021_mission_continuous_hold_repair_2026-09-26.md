# Event 021 continuous mission-hold repair

Disposition: implemented in source; decision-score comparison and live mission validation remain unresolved.

## Acceptance basis and parent decision

The Event 021 decision and mission spec requires map objectives with meaningful success, failure, timing, and cleanup. The independent decision/mission audit at `docs/plans/021_random_civil_war_plans/subagent_handoffs/decision_mission_audit_2026-09-26.md` identified that the capital and rail objectives were resolved from deadline snapshots and that a failed rail mission could restart and repeat its failure effect.

Within the user's authorized Event 021 scope, the parent accepted event-driven continuity checks for capital and rail state control. The parent chose the audit's explicit terminal-rail-failure option for a single crisis: `event021_rail_spine_lost` now ends this rail mission for that crisis, while the separate reconstruction decision remains available to restore infrastructure. No AI weight or coefficient was changed.

## Changed files and behavior

- `common/scripted_triggers/021_random_civil_war_parent_triggers.txt`: added `event021_secure_rail_mission_target_valid`, a shared current-target check for ownership, control, opening-front membership, and supply node or usable infrastructure. Rail activation, selection, and deadline resolution now use this predicate.
- `common/decisions/021_random_civil_war_decisions.txt`: the capital mission stores its exact capital state when selected and clears that receipt on cancellation. The rail mission requires a valid target before it appears or can be selected, and `event021_rail_spine_lost` prevents a same-crisis retry after failure.
- `common/scripted_effects/021_random_civil_war_decision_effects.txt`: capital success rechecks the saved target, current-capital status, control, infrastructure, supply, and the same defense receipt required at mission selection. The timeout and completion paths are idempotent and clear the saved state. Rail resolution uses the shared live-target predicate, and terminal failure is applied once while the mission is active.
- `common/on_actions/021_random_civil_war_cxt_on_actions.txt`: the existing `on_state_control_changed` callback records the changed state as a short-lived event target, compares it with each active mission's exact target pointer, and fails a hold immediately when control changes. This is event-driven and adds no periodic country or world scan. The existing capital-continuity callback remains in place.
- `localisation/english/021_random_civil_war_l_english.yml`: capital and rail descriptions now distinguish continuous control from conditions checked at the deadline.
- `common/scripted_triggers/021_random_civil_war_parent_triggers.md`: documents the target-valid predicate.

## Source identities and validation

Pre-edit hashes recorded by the decision/mission auditor include decision source `8937CAC0802745EAD68D6F1EC1B2BFA97DCCAA451EFFCC925D45A715DEDD3123`, decision effects `A1ED64466537E6E2F0235B7D268BE68AB525AEC119FC08E3240CEB6FE35DDF23`, and parent triggers `97E43B7BEB01FEBE49D13E26F169FDE1EB2B751EB451250C7E35C748D24AC622`. Post-edit hashes are decision source `C928B1B802B4B2CCCFA49913AF9E288571099398A0000DA1814B6E35CDE81BC1`, decision effects `653D04B02509FD090E5FAF395BE489539B912E4BE0B929C1B694A7F4B6C63065`, parent triggers `3E518F2088239F4D739AE97FA23A6BF4793034ED389B215A6EE85A53476E4465`, and CXT on_actions `5D7BD7B5A47CEBE555818715D7B6307A6594E86927C849D6D6A1591C33602571`.

The post-change focused `hoi4.event_inspect(mode=trace, selector={kind:event,eventId:chaosx.nr21.1}, refresh=true)` returned `EVENT_INSPECTED_PARTIAL`, revision `b38458235c44df993369ce3967f3e0891e3028c570069e8ac728961428509bab`, graph hash `9f5b70b9c419274482a8159f87edf0d3b1437a39f5d27c3eb1217cada636c3a2`, zero blocking diagnostics, and zero expanded helpers. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/22a5ac72064a9c6e41575296e6038dc8a8cb13d0a71849ce345cb01bf164f483/2fead33de2d72306da982c50aef900410d804ab6f75e5b9c8ffc1b12a8a71a13/event-trace-b38458235c44.json`. This route scans events and on_actions but does not parse the decision/effect helper lifecycle.

The source update leaves all `ai_will_do` coefficients unchanged. The immutable pre-edit decision snapshot is `docs/plans/021_random_civil_war_plans/probability_snapshots/event021_decisions_before_2026-09-26/021_random_civil_war_decisions.txt`. The pre-edit mission-AI inspect was incomplete with three candidates and three required inputs. A post-change probability compare is still pending for the identical source-flag scenario set in `docs/plans/021_random_civil_war_plans/subagent_handoffs/event021_mission_ai_source_flag_scenarios_2026-09-26.json`; no score, ranking, or balance result is claimed.

## Remaining validation and blockers

Both mission outcomes and the state-control callback need live validation for control loss, recapture, capital change, infrastructure/supply failure, crisis cleanup, successor adoption, cancellation, and timeout ordering. The ordinary `countrydecisionview` inspect and render route previously timed out after 180 seconds, so UI wrapping, mission state visibility, and native failure feedback remain unverified. No game was launched.

The full Event 021 dynamic front/actor migration remains incomplete. Fixed ordinary secondary and Event 006 secondary planner, activation, succession, review, scenario, and cleanup readers are still present. This mission repair does not certify the full decision system, its three-mission simultaneous visibility, the four-value settlement cost row, AI balance, Event 006 package reuse, or overall Event 021 completion.
