# Event 012 Scramble ultimatum receipt disposition

## Finding

`africa_scramble_ultimatum_requirement_met` read `africa_scramble_ultimata_withdrawn`, but no Event 012 source path wrote that flag. The accepted Scramble actions provide a zero-count path when no ultimatums were issued and an explicit `africa_foreign_ultimatum_answered` receipt after Action 79. A blanket withdrawal outcome was not present in the response matrix or action lifecycle.

## Disposition

The unwritten branch was removed from `common/scripted_triggers/012_africa_world_order_triggers.txt`. The resolver now depends only on the writer-backed zero-count and answered-ultimatum receipts. No new action, decision, event, or shortcut was added, and no ultimatum is silently treated as settled.

## Validation

Source census should now find no runtime reference to `africa_scramble_ultimata_withdrawn`. Focused Event 012 lint and brace/source checks remain required after the patch. The existing recognition, sanctions, intervention, and aftermath gates are unchanged.
