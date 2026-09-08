# Event 012 Gods of Africa late-onboarding repair

## Disposition

Implemented. This handoff closes the accepted `REG-05` later-major and `REG-06` later-player-control requirement with the owner-local quarterly route already permitted by the Gods of Africa technical architecture. It does not introduce a generic daily, weekly, or monthly world action.

## Changed surfaces

- `common/scripted_triggers/012_africa_gods_triggers.txt`
  - Participant registry membership checks now use `PREV` while the authoritative `africa_host` event target is nested. This preserves the country currently being tested in the initial array pass, transaction callbacks, decision categories, and the owner-local country sweep.
- `common/scripted_effects/012_africa_gods_effects.txt`
  - `gods_of_africa_review_registry` still archives invalid maintained records, then runs one capped `every_country` onboarding pass from the active host scope.
  - The existing `gods_of_africa_participant_can_register` predicate enforces the valid-major/player rule, excludes the host and special actors, rejects duplicates, and stops at `max_participants`.
- `events/012_africa_gods_of_africa.txt`
  - The hidden registry-review event comment now describes the maintained registry rather than a frozen queue.
- `docs/events/012_africa/gods_of_africa.md`
- `docs/events/012_africa/overview.md`
  - Document the 90-day owner-local onboarding route and its bounded scope.

## Behavior

At each registry review, the active Event 012 host first archives capitulated or otherwise invalid participants. It then checks current countries once through the owner-owned review. A country that became major or player-controlled after activation is registered exactly once, receives the normal introduction and deterministic first-demand delay, and cannot bypass the participant cap. A registered country remains a participant if it later loses major status, as required by the specification.

## Validation

- The source predicates and effects remain brace-balanced and use the existing Event 012 owner clock.
- The review cadence remains `constant:gods_of_africa_timing.registry_review_days`, currently 90 days.
- No `on_daily`, `on_weekly`, or `on_monthly` world action was added.
- MCP event inspection remains partial aggregate evidence for this large workspace and does not replace user-owned live campaign validation.

## Remaining limits

The installed engine exposes no dedicated generic player-tag-switch callback in the available Event 012 hook set. The 90-day owner-local pass is therefore the accepted fallback for newly controlled countries. Live save playback of `REG-05` and `REG-06` remains user-owned evidence.
