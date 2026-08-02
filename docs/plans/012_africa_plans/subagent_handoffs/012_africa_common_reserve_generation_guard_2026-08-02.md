# Event 012 common-reserve host-generation guard

Date: 2026-08-02.

## Scope

The defender-only common-reserve war trigger now rejects protected relationship receipts from a superseded Event 012 host generation.

## Changed files

- `common/scripted_triggers/012_africa_common_reserve_triggers.txt`
  - Added `africa_member_host_generation_is_current = yes` to `africa_common_reserve_can_cover_defensive_war` immediately after the protected-relationship gate.
- `docs/events/012_africa/common_reserve_deployment.md`
  - Documented the generation guard in the defensive deployment contract.

## Contract

`on_war_relation_added` calls `africa_common_reserve_can_cover_defensive_war` on the protected defender before `africa_common_reserve_deploy_on_defensive_war` debits the current host's stockpile. The canonical host-generation trigger now proves that the protected member's recorded generation matches the live committed host. Current-generation members retain the existing deployment path. Stale members fail closed without changing the offensive-war branch.

## Validation

- The canonical trigger is already defined in `common/scripted_triggers/012_africa_triggers.txt` and is reused without duplication.
- The changed trigger has balanced braces and no unsupported comparator syntax.
- No tags, models, unit entities, extra stockpiles, world-order packages, or recurring scans were added.
- Live acceptance still needs current-generation, stale-generation, and RSA succession scenarios.
