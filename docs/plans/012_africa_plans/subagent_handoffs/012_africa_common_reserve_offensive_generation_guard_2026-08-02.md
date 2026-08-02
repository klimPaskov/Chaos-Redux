# Event 012 common-reserve offensive-abuse generation guard

Date: 2026-08-02.

## Scope

The offensive common-reserve abuse callback now rejects a protected-member receipt from a superseded host generation before setting the lifetime disqualifier.

## Changed files

- `common/on_actions/012_africa_world_order_on_actions.txt`
  - Added `africa_member_host_generation_is_current = yes` inside the attacking `ROOT` validation block.
- `docs/events/012_africa/common_reserve_deployment.md`
  - Documented the generation requirement for offensive-abuse accounting.

## Contract

The `on_war_relation_added` callback records offensive reserve abuse only when the protected attacker is a current-generation Event 012 member and the current host reserve posture is active. The host-scoped owner therefore cannot be poisoned by a former member's stale relationship and lifetime receipt. Current-generation offensive misuse remains a disqualifying outcome. Defensive reserve deployment uses its separate generation-guarded trigger.

## Validation

- The on-action block remains balanced and the existing sole abuse recorder is unchanged.
- No tags, models, assets, tuning values, or reserve stores were added.
- Live acceptance still needs current-generation offensive misuse and successor-host stale-receipt scenarios.
