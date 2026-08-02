# Event 012 protection-war achievement generation guard

Date: 2026-08-02.

## Scope

The canonical protection-war achievement owner now rejects stale protected-member receipts before opening an unresolved protection-war record.

## Changed files

- `common/scripted_effects/012_africa_achievement_effects.txt`
  - Added `africa_member_host_generation_is_current = yes` to `africa_achievement_record_protection_war_started`.
- `docs/plans/012_africa_plans/012_africa_achievements_handoff.md`
  - Documented the current-generation requirement for the Guardians without Borders ledger.

## Contract

The defender branch of `on_war_relation_added` calls this owner after identifying a protected partner. The owner now proves that the member's recorded generation matches the committed live host before incrementing `global.africa_achievement_protection_wars_started` or setting the unresolved-war flag. This prevents a superseded host receipt from poisoning the settled-versus-started proof used by `africa_guardians_without_borders_is_complete`.

## Validation

- The owner remains idempotent through `africa_achievement_protection_war_counted`.
- Braces and comparator syntax remain valid, and no new helper or store was introduced.
- No tags, models, assets, external packages, or tuning values changed.
- Live acceptance still needs current-generation, stale-generation, and successor-host war scenarios.
