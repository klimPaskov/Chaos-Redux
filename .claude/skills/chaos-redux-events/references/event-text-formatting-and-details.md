# Event text formatting and Event Details rules

### Detail text, immediate effects, and value formatting

Report and event descriptions drawn on light parchment must use plain text for names and values, without § colour formatting, including strings returned by scripted localisation.
Keep colours only in supported dark option, tooltip, decision, or GUI consumers; use separate plain and coloured localisation variants when a shared helper feeds both.
Audit the whole owned description family and its dynamic substitutions for contrast in the actual consumer, including at 1080p.

Native PowerShell stdin can replace non-ASCII program text before Python receives it, even when Python writes a UTF-8 BOM correctly.
For localisation writes through that route, use ASCII program text with Unicode escapes or `chr()` for the `U+00A3` texticon and `U+00A7` formatting glyphs, or read the intended text from an explicitly UTF-8 file.
Re-read the affected values as UTF-8 and verify their actual glyphs after writing.
If an existing OneDrive-backed source file repeatedly rejects write-open with `OSError: [Errno 22] Invalid argument`, write the reviewed bytes to a uniquely named sibling file and replace the exact owned target atomically.
Preserve BOM and line endings, verify both resolved paths stay in the intended directory, and re-read the target immediately before replacement to confirm its bytes still match the edit baseline.
If another writer changed it, rebuild the narrow edit from that fresh content instead of replacing their work; retain or remove only the task-owned temporary file on failure.
When normalizing physical line endings, preserve authored `\n` escapes inside localisation values rather than rewriting them as literal `\r\n` escapes.

Event Details text must never display mechanical effects. The Event Details window, spreadsheet `Details` field, and player-facing detail summaries should describe the situation and premise, not list rewards, penalties, modifiers, variable changes, or script effects. If an event is meant to apply gameplay effects immediately regardless of which option the player chooses, place the real effects in the event `immediate` block inside a `hidden_effect`. The option should not reapply those effects. The option may show the immediate result only through a custom tooltip for cosmetic clarity, so the player sees the consequence without turning Event Details into an effects list.

Player-facing event, decision, focus, and Event Details text must describe in-world consequences rather than meta reward routes. Do not advertise that a choice opens, grants, counts toward, or completes an achievement path. Keep achievement conditions in achievement UI and docs, and use ordinary in-world consequence text elsewhere. For ambiguous report-stage incidents, describe what people see, fear, suffer, or fail to explain. Do not directly label the incident as a warning, a non-warning, a danger signal, or the absence of one.

Visible dynamic values often display decimal places unless their localisation formatter says otherwise. If a value is conceptually an integer, show it as an integer with `|0` formatting or an equivalent scripted-localisation helper. Only show decimal places when the value genuinely needs fractional precision, such as ratios, percentages, fractional costs, or progress values where the fraction changes player decisions.

For numeric `defined_text` output, put the formatted variable in a real `.yml` localisation value, such as `numeric_value_display: "[?temp_value|0]"`, and use the key's literal name in the corresponding `text` block: `localization_key = numeric_value_display`.
An inline formatted variable string such as `localization_key = "[?temp_value|0]"` is tokenized as a dynamic key and may fail with dynamic-token errors.
Temporary variables assigned in the same `text.trigger` remain visible to the selected localisation key, so calculate the display value there.
Retain constant-backed temporary getters where the installed documentation supports the assignment, and do not introduce persistent globals solely for formatting.
