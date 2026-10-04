# Event 021 calendar conversion

`event021_days_to_date_offset` accepts ANY scope.
Its required caller-owned temporary input/output is `event021_date_offset`.
Initialize it with a day duration immediately before calling the helper, then add its returned value to an encoded date variable.
The helper is a thin wrapper over the shared `chaosx_convert_days_to_date_offset` in `chaosx_dynamic_effects.txt`: it copies the days into `chaosx_date_days`, creates `chaosx_date_offset` before the call so the shared output survives the return, and copies the result back into `event021_date_offset`.
The shared helper multiplies days by the centralized 24 hours per day in `chaosx_date_units`, rounds fractional hours upward, and divides by 100,000 hours per date unit.
Whole-day durations are exact.
Nonintegral durations are represented at the engine's one-hour resolution and cannot expire early.
No country, state, registry, flag, or game clock is mutated by the helper.
Event 021 keeps no calendar constants of its own.

Example: set `event021_date_offset = constant:event021_action_tuning.settlement_obligation_days`, call `event021_days_to_date_offset = yes`, and add `event021_date_offset` to `event021_settlement_deadline` after copying `global.date` into it.
Leave native `days =`, mission durations, flag durations, AI scores, and MTTH values in days.
Do not convert the day input in place when another consumer still expects days.
Already encoded stored dates, including the recurrence base date and treaty hold-date copies, are copied without another conversion.

The offline Data structures Game variables section at lines 1467-1470 describes one game hour as 0.00001, revision `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`.
Installed dynamic variables documentation describes `date` at line 977 and `num_days` at lines 996-998, revision `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
`.tools/test_event021_date_units.py` runs the wrapper through the shared helper with the shared constants and checks exact whole days, upward rounding, and every Event 021 deadline addition.
