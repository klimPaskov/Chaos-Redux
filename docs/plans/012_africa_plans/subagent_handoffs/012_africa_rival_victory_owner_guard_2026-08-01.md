# Event 012 rival-victory owner guard handoff

Date: 2026-08-01

Scope: narrow achievement owner-integrity correction.

## Changed files

- `common/scripted_effects/012_africa_priority_member_effects.txt`
- `docs/events/012_africa/overview.md`

## Runtime correction

`africa_priority_member_record_rival_bloc_victory` now requires the helper's own `africa_priority_member_rival_bloc_victory` receipt before refreshing the host's achievement windows and calling `africa_achievement_record_recognised_rival_confederation`. The existing `on_capitulation` caller still requires a current Event 12 host, an existing package, the Rival Bloc relationship, the explicit rival-departure choice, and direct capitulation of the host.

This closes a reusable-helper false-positive path without adding a new achievement proxy, changing the rival war, or widening any carrier/tag gate.

## Validation and remaining risk

The helper has one literal caller in `common/on_actions/012_africa_world_order_on_actions.txt`, and the positive writer remains inside the package/rival condition. Static brace and unsupported-operator checks remain required before commit. Live positive and disqualifier acceptance remains open.
