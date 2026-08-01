# Event 020 rat-brood absorption follow-up

## Status

Resolved and superseded by the live two-tag state-marker implementation.

No further design addendum is required for this gap.

## Finding

`black_plague_rat_absorb_a_weaker_brood` spends Brood Mass and calls `black_plague_rat_try_absorb_adjacent_brood`.

The helper now selects a valid adjacent state-level brood marker inside the single `RTA` carrier, reserves it, records absorption, inherits its bounded surviving-unit value, adds Brood Mass, refreshes the shared division cap, and emits `chaosx.nr20.43` once.

It does not annex another Rat Nation country and does not require another tag.

## Accepted resolution

Keep the paid decision and its state-level payoff.
Treat additional broods as Rat Infestation, brood-strength markers, unit inheritance, and internal consolidation inside `RTA`.
Preserve the two-tag correction with `RTA` as the base carrier and `RTX` as the separate Rat King.

## Evidence

The absorption helper and call site are in `common/scripted_effects/020_black_plague_rat_effects.txt` and `common/decisions/020_black_plague_rat_decisions.txt`.
The state eligibility and absorbed-marker checks are in `common/scripted_triggers/020_black_plague_rat_triggers.txt`.
The two-tag correction is `docs/specs/020_black_plague_specs/corrections/2026-07-29_two_rat_tags.md`.
