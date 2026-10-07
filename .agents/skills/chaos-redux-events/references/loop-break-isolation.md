# Isolate foreach break state

Use this rule when a helper iterates records or scopes, especially nested receipt settlement and recovery.
Both `for_each_loop` and `for_each_scope_loop` default to the unscoped temporary variable `break`, so an inherited nonzero value can truncate traversal.
Give every loop a private helper-owned break temporary, reset it to `0` immediately before every invocation, and explicitly bind `break = <that_temp>`.
Use distinct names for inner and outer loops and any nested helpers that can execute together, because changing scope does not isolate temporary variables.
Repairing an inner loop does not protect its enclosing loop, and one reset at helper entry does not protect repeated inner invocations.

Tiny generic example, with valid country scopes in `participants` and each participant's records in `receipt_ids`:

```text
set_temp_variable = { settlement_participants_break = 0 }
for_each_scope_loop = {
	array = participants
	break = settlement_participants_break
	set_temp_variable = { settlement_receipts_break = 0 }
	for_each_loop = {
		array = receipt_ids
		value = settlement_receipt_id
		index = settlement_receipt_index
		break = settlement_receipts_break
		# Validate and settle this exact receipt here.
	}
}
```

Keep pending, unvisited, and unacknowledged receipts until their exact settlement is complete.
Clear only acknowledged receipts and retain unfinished work across an interrupted or deliberately bounded pass.
Do not remove array elements during `for_each_loop` traversal.

Test the actual source with inherited `break = 1` and two objects for each iterable kind, then two outer participants with two receipts each, asserting complete visitation and exactly one settlement per eligible receipt.
Also seed each private break temporary with `1` before calling the helper, repeat the call, and exercise an intentional early exit or unresolved receipt to verify reset and retention.
Keep a conservative test with more than 1,000 objects and repeated invocations, but do not impose an undocumented foreach ceiling in the fixture or claim that test proves an engine limit.
The documented 1,000-iteration bound explicitly applies to `while_loop_effect` and `for_loop_effect`, while the cited foreach sections state no such ceiling.

Sources:

- Installed `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md`, lines 4279-4295 (`for_each_loop`) and 4296-4311 (`for_each_scope_loop`), explicitly define the default temporary break variable and nonzero termination.
- Offline `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md`, lines 440-442 (temporary lifetime and unscoped storage), 1216-1217 (foreach rules), and 1222-1256 (foreach examples).
- The same offline file, lines 1219-1220 and footnote at 1828, explicitly documents the default 1,000 bound for `while_loop_effect` and `for_loop_effect` through `NDefines.NGame.MAX_EFFECT_ITERATION`.
