# Event 016 containment temporary cleanup analysis

Disposition: implemented after parent source and consumer review.
Acceptance basis: the user authorized isolated safe startup fixes; the parent accepted the exact one-line deletion after reviewing all four references and the repeated-call initialization contract.
The research subtask did not edit gameplay; the parent subsequently removed only the terminal unsupported command and archived the immediate original under pre_patch_containment_temp_cleanup/.

## Recommendation

Delete only `clear_temp_variable = brilliant_scientist_containment_exile_recipient_preserved` at `common/scripted_effects/016_brilliant_scientist_containment_effects.txt:63`.
Retain the unconditional entry initialization, conditional assignment, branch test, recipient selection, candidate weighting, and all event-target cleanup exactly as written.
No replacement cleanup effect or exit sentinel assignment is needed for the current consumer contract.

This is semantically equivalent for all current consumers, rather than an assertion that leaving a temporary value alive is equivalent to explicit memory deletion in every possible script.
No current consumer observes the variable after its local branch test, and every subsequent invocation overwrites it before testing it.
Its automatic temporary lifetime is sufficient for this local scratch value.

## Confirmed error and supported behavior

The supplied `logs/launch_07/logs/error.log:1685–1686` identifies invalid `clear_temp_variable` and unknown effect type at containment effects line 63.
Installed `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:2773` documents `clear_variable` as an effect that clears a variable, but does not explicitly establish temporary-variable support.
The required offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, `clear_variable` table row, explicitly says it can only be used on regular variables.
Neither installed effects nor triggers documentation contains a `clear_temp_variable` entry.
Therefore a mechanical replacement with `clear_variable` is unsupported by the consulted references and is not recommended.

Installed effects documentation at line 7820 and triggers documentation at line 7482 document `set_temp_variable` assignment from a value, variable, or math expression.
The offline Data structures Variable types section at lines 410–419 documents temporary values as unscoped and limited to the containing effect/trigger lifetime, without carrying over into events.
It also cautions that values created inside scripted helpers may not survive into the caller; this does not affect the proposal because the value has no downstream consumer.
Do not claim automatic deletion precisely at the closing brace of this helper; the documented lifetime may extend through the containing effect block.

## Exhaustive runtime references for this identifier

Repository searches across `common`, `events`, `localisation`, and `interface` find exactly four occurrences of `brilliant_scientist_containment_exile_recipient_preserved`, all in the same helper.
There are no regular-variable writes, scoped references, event-target uses, localisation reads, `has_variable` checks, arithmetic reads, or external comparisons of this identifier.

| Location in containment effects | Operation | Meaning |
| --- | --- | --- |
| Line 19 | Unconditional `set_temp_variable` to `constant:brilliant_scientist_value.zero` | This invocation has not proved that the existing exile recipient may be preserved |
| Line 29 | Conditional `set_temp_variable` to `constant:brilliant_scientist_value.one` | Existing recipient exists, passes the transfer-recipient predicate, and is not at war with the host |
| Line 34 | `check_variable` equals the zero constant | Execute recipient replacement only when preservation was not established |
| Line 63 | Unsupported `clear_temp_variable` | Terminal scratch cleanup attempt; no later read depends on absence or a value |

The zero/one values are local branch sentinels, not an external return value or a persistent flag.
The parent restricted this task to a syntax cleanup, so converting this branch to a country flag or restructuring the selector is outside scope.

## Caller and continuation trace

`brilliant_scientist_select_containment_exile_recipient` has exactly one runtime call site: `brilliant_scientist_prepare_sovereignty_board` in the same effects file at line 176.
The caller next executes `brilliant_scientist_prepare_formation_territory_plan`, then `brilliant_scientist_calculate_containment_scores`, sets the board-prepared country flag, and records the prepared date.
None reads the preservation scratch identifier.

The board preparation helper is called by the following current entry paths:

- `brilliant_scientist_start_sovereignty_deadline`, in `common/scripted_effects/016_brilliant_scientist_evolution_effects.txt:973`, then mission activation.
- `brilliant_scientist_reopen_invalidated_sovereignty_board`, containment effects line 301, then delayed `chaosx.nr16.32` report.
- `brilliant_scientist_resolve_unanswered_sovereignty_deadline`, containment effects line 605, then explicit action-temp initialization and resolution.

The exile recipient itself remains stored in the existing global event target and is independent of the preservation scratch variable.
Removing the terminal unsupported command does not clear, change, or recreate that target.
No event-target lifetime change is proposed.

## Branch and repeated-call reasoning

| Scenario | Scratch sequence before terminal cleanup | Behavior after deleting only terminal cleanup |
| --- | --- | --- |
| Existing valid peaceful recipient | Entry zero, then one; zero-test fails | Same target is preserved; no candidate redraw |
| No existing target | Entry zero; zero-test passes | Existing selection logic runs unchanged |
| Existing target invalid or at war | Entry zero; zero-test passes | Existing target clearing and replacement logic run unchanged |
| Repeated call after preserving a recipient | Prior scratch may remain one until enclosing block ends; next entry overwrites zero before validation | The second invocation independently revalidates the recipient |
| Repeated call after recipient becomes invalid | Entry zero precedes every read | No stale one can incorrectly preserve the invalid recipient |
| Helper returns to its caller | Scratch may remain until its temporary lifetime ends | No downstream consumer observes it |

An exit `set_temp_variable = { ... = constant:brilliant_scientist_value.zero }` is supported syntax, but would introduce an unnecessary terminal state that is neither absence nor a required caller contract.
Deleting the unsupported terminal command is the smaller repair and avoids claiming that zero equals nonexistence.
No new default or sentinel value is introduced.

## Validation and boundaries

Completed checks: exact runtime read/write inventory, sole direct caller inventory, all board-preparation callers, continuation inspection, documentation comparison, and branch/reentry reasoning above.
No gameplay file was edited; no game, desktop, process, staging, or commit operation was performed.
The earlier containment MCP inspections remain the event-surface evidence for this same consumer chain: full state-flow revision `95690b83dbc974ecf7dc8386de220deefae81d2c8f862910662071ef27f03cb9` with diagnostics, and refreshed focused trace revision `4520c3ceb2ac2ff2148d4a7228cd8878f66ba12464a692526456f94fa064899f` with helper coverage deferred.
Their artifact links and limits are recorded in `containment_parameter_repair_plan.md`.
Neither proves temporary-memory behavior in a running game; this proposal relies on the required installed documentation, offline wiki, and exact consumer inventory.

No weighted condition, candidate pool, random-selection branch, weight, or recipient predicate is modified or redesigned by this proposal.
A probability evaluation would not establish support for an unknown cleanup command, and no balance conclusion is claimed.
Unsupported `clear_temp_variable` calls outside this containment helper were not analyzed and must not receive a global replacement based on this finding.

The parent implemented the one-line repair; launch 08 no longer reports this exact unsupported cleanup command.
No gameplay simplification or fallback is proposed.
