# Event 021 calendar conversion

`event021_days_to_date_offset` accepts ANY scope.
Its required caller-owned temporary input/output is `event021_date_offset`.
Initialize it with a day duration immediately before calling the helper, then add its returned value to an encoded date variable.
The helper multiplies days by the centralized 24 hours per day, rounds fractional hours upward, and divides by the centralized 100,000 hours per date unit.
Whole-day durations are exact.
Nonintegral durations are represented at the engine's one-hour resolution and cannot expire early.
The private `event021_date_unrounded_hours` is not an output and need not survive the helper return.
No country, state, registry, flag, or game clock is mutated by the helper.

Example: set `event021_date_offset = constant:event021_action_tuning.settlement_obligation_days`, call `event021_days_to_date_offset = yes`, and add `event021_date_offset` to `event021_settlement_deadline` after copying `global.date` into it.
Leave native `days =`, mission durations, flag durations, AI scores, and MTTH values in days.
Do not convert the day input in place when another consumer still expects days.
Already encoded stored dates, including the recurrence base date and treaty hold-date copies, are copied without another conversion.

The offline Data structures Game variables section at lines 1467-1470 describes one game hour as 0.00001, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed dynamic variables documentation describes `date` at line 977 and `num_days` at lines 996-998, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
The installed Script Constants documentation requires schema-first groups and permits `constant:` access in variable operations.
The existing Event 013 calendar converter supplies the repository precedent for the 24/100,000 unit conversion.
This Event 021 helper additionally prevents sub-hour deadlines from resolving early.
It requires no new image, GUI, asset, or periodic hook.
