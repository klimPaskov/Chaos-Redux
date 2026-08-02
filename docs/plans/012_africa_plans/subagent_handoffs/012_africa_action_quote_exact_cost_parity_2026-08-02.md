# Event 012 action quote exact-cost parity

Date: 2026-08-02.

Status: Implemented as a narrow shared affordability correction. Live campaign acceptance remains open.

## Scope

The quoted-action launch gate and the Event 013 natural-disaster weapon reservation both rejected an actor holding exactly the required scalar resource. The strict checks also rejected actions whose unused scalar components were zero.

## Changes

`common/scripted_triggers/012_africa_triggers.txt` now treats political power, command power, manpower, fuel, stability, and war support as affordable when the stored amount is exactly the quoted amount. The checks use supported inverse less-than triggers and `greater_than_or_equals` for war support. Civilian and intelligence capacity and equipment checks remain unchanged.

The host-side and priority-member natural-disaster caller gates now accept exactly the configured political-power and command-power reserve. The existing reservation effect still debits once, keeps the actor-specific caller scope, and refunds on a failed shared-action start.

The compact promotion tooltip now names damaged access as a visible blocker. The active access receipt remains `africa_project_access_damaged`; an older clear for `africa_compact_access_failure` is retained for save compatibility and is not used by the gate.

## Acceptance cases

- A zero-cost scalar component passes at exactly zero.
- A nonzero scalar component passes at exact cost and fails one unit below.
- `open_aid_corridor` can launch when unused political power, command power, fuel, stability, and war-support costs are zero.
- Host and member nature actions accept exactly the configured 35 political-power and 10 command-power reserve, debit once, and leave the caller at zero.
- Player, AI, focus, and diaspora callers still fail final revalidation when any actual quoted component is below cost.

## Validation

The parent will run the focused brace and quote hygiene checks, localisation BOM/key checks, and the Event 012 decision/action source audit before committing. No tags, country carriers, models, portraits, world-order readiness flags, or disaster-strength tuning were changed.

## Remaining risk

The repository does not run a live Hearts of Iron IV campaign in this environment. Exact-cost behavior still needs user-owned in-game verification across one zero-cost action, one resource-bearing action, and both natural-disaster caller paths.
