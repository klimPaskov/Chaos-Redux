# Event 016 Observer-Lecture Reachability Handoff

## Scope

This tranche keeps the impossible lecture's interrupted-observer branch tied to an actual detected observation operation. Hosts without a foreign observer no longer receive a choice whose text claims that one is present.

## Gameplay changes

- `common/scripted_effects/016_brilliant_scientist_foreign_effects.txt` writes `brilliant_scientist_foreign_observer_contact` on the active host when a detected observation operation dispatches the host response.
- `events/016_brilliant_scientist_context_events.txt` uses that receipt for the interrupted description and for the `chaosx.nr16.12.d` option trigger; public, military, industrial, and default branches remain available according to the existing context policy.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` and `common/scripted_effects/016_brilliant_scientist_country_effects.txt` carry the observer receipt through ordinary transfer and KRG formation when a pending lecture follows the identity.

## Runtime contract

The observation receipt is written only for the active current host and only from a detected observation operation. It is a history guard, not a project reward or a second foreign-operation resolution. The existing foreign host response and after-action reports remain unchanged.

## Validation evidence

- Exact event option and description triggers were checked after the edit.
- Gameplay braces are balanced and no unsupported comparison operators were added.
- The receipt appears in both transfer and formation inheritance blocks.

## Remaining risks

Live operation timing and the user-owned foreign-decision scenario still require in-game validation. This tranche adds no new art, event-log row, evolution, project stage, or 3D model.
