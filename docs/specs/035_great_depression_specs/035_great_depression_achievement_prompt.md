# Event 35 Great Depression 2.0 achievement audit brief

Status: the six Event 35 contracts are implemented in `common/achievements/chaos_redux_achievements.txt` with their textures, and Event 34 keeps `chaos_redux_034_the_long_fall` for the inherited crash-and-recovery chain.
The contracts, required conditions, disqualifiers and tracking rules are owned by part 11.

Use this brief to prove the contracts, not to redesign them.

## For each contract

Check the source evaluator that writes its proof receipt during `great_depression_try_complete_recovery` or the global recovery transaction, and record:

1. One positive scenario that unlocks it.
2. One near miss that does not.
3. One exploit attempt (state transfer, tag switch, debug or force paths, late tracking, refunded or duplicated contributions) that does not.
4. One save and reload case in which the receipt survives and is not replayed.
5. One disqualifier case.

## Rules

- Receipts are per episode and are evaluated before active episode data is cleared.
- Containment Line counts only containment actions whose episode receipt matches the current episode.
- Lean but Standing needs a real Event 35 liquidation loss, never war, bombing, disaster or another event's loss.
- Recovery of Nations reads contribution receipts, not current modifiers.
- Player-facing names and descriptions follow the `chaos-redux-events` writing style and never praise unemployment or suffering.

Return the scenario results, any receipt defect with file and line, and remaining risks.
