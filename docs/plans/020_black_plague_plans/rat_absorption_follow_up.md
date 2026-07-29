# Event 020 rat-brood absorption follow-up

## Status

Deferred for parent review because a correct resolution changes the Rat Nation mechanic rather than merely cleaning its implementation.

## Finding

`black_plague_rat_absorb_a_weaker_brood` spends Brood Mass and calls `black_plague_rat_try_absorb_adjacent_brood`.

The helper is intentionally empty and explains that the current one-carrier model has no country-to-country annex transaction.

The decision description nevertheless promises adjacent territorial absorption and inherited strength.

## Required design decision

Do not alter this during cleanup because a correct change needs a defined state-level payoff, valid target selection, AI conditions, cap interaction, and retirement cleanup.

Either implement an explicit state-level absorption result with a one-time target and cooldown, or remove the decision and its localisation as obsolete.

## Evidence

The absorption helper and call site are in `common/scripted_effects/020_black_plague_rat_effects.txt` and `common/decisions/020_black_plague_rat_decisions.txt`.
