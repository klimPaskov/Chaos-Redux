# Event 26 agent decisions, 2026-10-04

These decisions were taken by the implementing agent under the user's standing grant of design authority, following the lead's recommended options for the Round 1 remaining-work list.
Each entry records the decision, its basis, and its disposition.

## D1. Friday anchor

Decision: the in-game Friday is the seven-day cycle where `global.num_days % 7 = 6`, so 3 January 1936 is the first Friday.
`friday_remainder` changes from 2 to 6 in `common/script_constants/026_black_friday_constants.txt`.

Basis: the offline wiki Data structures page (line 1470) gives `num_days` as days since the start of year 0, with 706640 on 1 January 1936.
The save `qa_cxt_base.hoi4` dated 1936.1.3 stores `great_depression_recent_major_industrial_state_loss_day=706642`, which `common/scripted_effects/035_great_depression_external_adapters.txt:160` sets from `global.num_days`.
706642 % 7 = 6, and 3 January 1936 was a Friday.
The former remainder 2 opened the sale on 6 January 1936 and every seven days after, which are Mondays.

The engine calendar has 365 days in every year, so the seven-day cycle drifts one real weekday after each skipped 29 February.
That drift is accepted as the in-game week and documented rather than corrected, because a leap-day correction would need a real calendar the engine does not keep.

Disposition: implemented.
Live date progression remains a `needs_live_game` acceptance item.
