# Event 021 history selection

The country viewing history owns the selected detail variables.
`event021_parent_record_system_log` appends an immutable detail row, records the shared history entry, and then appends the resulting shared history sequence to `global.random_civil_war_log_snapshot_history_sequence_entries`.
The owner sequence array is aligned with the owner detail arrays, independent of the shared view's sorting and filtering.

`event021_resolve_history_selection` first clears the selection.
For an Event 021 history entry with a positive sequence, it scans only the owner sequence array and finds the matching row.
The published `_snapshot_row` is zero-based for array access.
The `_snapshot_index` is one-based only as a presence indicator, so row zero is visible.
Missing matches leave both values zero and display no unrelated detail.

The shared history click calls the resolver after selecting its sequence and before opening the details view.
Closing history details and opening ordinary event details call `event021_clear_history_selection`.
These are the only shared source edits, preserving the framework's other staged and unstaged hunks.

Example: after opening and settlement entries have been written for Germany, choosing the earlier opening uses its own capital, cause, severity and sponsor values, even if the live crisis has ended.
Switching to a different event or the ordinary Event 021 catalog view clears that historical context.
