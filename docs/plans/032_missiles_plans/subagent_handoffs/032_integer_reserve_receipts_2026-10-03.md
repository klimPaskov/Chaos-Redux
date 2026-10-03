# Event 032 whole-missile creation receipts

Disposition: implemented in source, with runtime accounting validation still pending.
Acceptance basis: part 2 defines Operational Reserve as a nonnegative integer, and the user requires exact reserve custody and no-duplication accounting.

`missiles_calculate_reserve_package` evaluates factory, controlled-state, wartime, and saturation factors before publishing a rounded whole-missile quantity.
The existing `round_temp_variable` command is applied once to the finished package before any stockpile mutation.
No existing reserve, prepared allocation, payload receipt, cost, weight, or tuning constant is changed.
This avoids fractional unspendable missile tails and keeps creation quantities consistent with integer launch costs and captured/resettled stock.

Files changed are `common/scripted_effects/032_missiles_effects.txt`, `.tools/test_event32_recipient_scope.py`, and the current test ledger.
The immutable pre-edit source is `docs/plans/032_missiles_plans/baselines/2026-10-03_reserve_integer/032_missiles_effects.txt`, SHA-256 `3900869d7b38a6fffa203ec30d0451e65feeb4ddcdb07c65577aa36d9950e1fa`.
The baseline folder's byte-preservation attributes apply to this snapshot.

The installed `documentation/effects_documentation.md` lines 6476–6495 document `round_temp_variable` and `round_variable` in any scope.
The file revision is `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
Existing capture, natural-disaster settlement, civil-war division, and casualty helpers already use the same round command.

The focused offline regression passes eleven tests.
Its package arithmetic case covers sixty small, large, peacetime, wartime, ordinary, mature, and saturation input combinations with the current script constants.
The pre-repair source produces fractional quantities in forty-eight of those combinations.
The model checks positive nearest-integer arithmetic and source receipt placement, but does not establish engine tie behavior or runtime custody outcomes.
No Hearts of Iron IV process was launched by this agent.
