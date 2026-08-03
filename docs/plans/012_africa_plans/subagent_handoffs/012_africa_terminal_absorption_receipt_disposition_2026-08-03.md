# Event 012 legacy terminal absorption receipt disposition

## Gap

`africa_world_package_is_resolved` read `africa_world_package_terminal_absorbed`, and successor cleanup cleared it, but no Event 012 source effect ever wrote that flag. The live package lifecycle instead records consent-based union, submission settlement, successor transfer, exile, breakup, or explicit terminal resolution.

## Change

The unwritten `africa_world_package_terminal_absorbed` branch was removed from `common/scripted_triggers/012_africa_world_order_triggers.txt`, and its dead cleanup line was removed from `common/scripted_effects/012_africa_world_order_effects.txt`.

This keeps the resolver fail-closed and preserves the Event 012 rule that integration cannot be inferred from an unwired absorption receipt or an instant annexation path. The broader specification's absorbed-union disposition remains a future, explicitly authored outcome rather than a phantom flag.

## Evidence

- A repository-wide Event 012 source census found the flag only in the resolver and successor cleanup before this patch; there was no writer.
- Submission, union, successor, exile, breakup, and terminal-resolution writers remain intact and are the documented lifecycle receipts.
- No country tag, focus tree, decision, localisation key, asset, or model surface changed.

## Remaining acceptance

The source cleanup is static evidence only. Live package-loss, successor, exile, breakup, and union scenarios still require campaign validation, and the broader world-order W5 package certification remains gated by the missing authoritative pre-install receipts.
