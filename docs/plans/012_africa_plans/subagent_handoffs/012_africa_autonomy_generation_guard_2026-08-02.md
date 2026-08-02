# Event 012 autonomy host-generation guard

Date: 2026-08-02.

## Scope

The two Event 012 autonomous states now verify the member's recorded host generation before the engine can retain or qualify the state.

## Changed files

- `common/autonomous_states/012_africa_autonomy.txt`
  - Added `africa_member_host_generation_is_current = yes` to `autonomy_africa_federal_member.allowed`.
  - Added the same guard to `autonomy_africa_integrated_region.allowed`.
- `docs/events/012_africa/charter_autonomy_and_focus_ai.md`
  - Documented the current-generation retention rule and validation requirement.

## Contract

`africa_member_host_generation_is_current` requires a live `africa_host` target with a committed host generation and compares the member's recorded generation to that host value. Relationship transitions already write the member generation before applying autonomy. Current-generation members therefore retain the normal path, while stale receipts fail closed after host succession or partial lifecycle cleanup.

## Validation

- The trigger is defined in `common/scripted_triggers/012_africa_triggers.txt` and is reused rather than duplicated.
- Both autonomous-state blocks remain closed with `can_take_level = { always = no }` and `can_lose_level = { always = no }`.
- No tags, models, country definitions, assets, or world-order readiness flags were added.
- Live successor/autonomy retention still requires in-game acceptance by the parent.
