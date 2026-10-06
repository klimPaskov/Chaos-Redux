# Event 004 release QA decisions

Acceptance basis: the user's 5 October 2026 task authorizes weak-design corrections and requires low popup counts, concrete costs, and complete forced-launch feedback.
Disposition: implemented, with independent audit and MCP coverage tracked in the accompanying handoffs.

## Decisions and evidence

- Aggregate participant reports after each declaration chain and prefer a defensive response for a country that was attacked.
The previous per-declaration delivery could send the same country both response reports during War Contagion.
One observer news and at most one participant report bound each invocation to one or two player popups.
- Count distinct participants instead of treating declaration count as country count.
A closed ring has equal numbers, but an interrupted open chain has one more country than declarations.
- Consume the prepared pair after firing and own temporary helper outputs in the immediate caller.
Repeated Wars-cluster slots must not reuse the previous declaration, and the event log's prepared actor must remain the actual aggressor.
The prepared profile is retained on the dispatching country behind `random_war_prepared_context`, alongside the chain's regular event targets, and consumed after firing.
This preserves the actor and stage even when preparation returns through intermediate helper frames or the dispatcher initializes its temporary outputs.
- Replace seven-modifier defensive and reserve packages with three modest modifiers each for the existing 45-day durations.
Field defenses cost 25 political power.
Reserve mobilization retains its stability cost, draws on the country's recruitable population, and grants no flat or weekly manpower.
The old reserve package added 5,000 manpower immediately, 5,000 each week, and three percentage points of conscription irrespective of national population.
- Keep the existing option weights, stage thresholds, declaration targets, and special-country chance thresholds.
The read-only probability auditor identified half-open integer random ranges in installed documentation.
Use an exclusive upper bound of 101 for the d100 draw and 9 for the final-stage declaration draw, preserving the intended 1–100 and 7–8 results.
Use the documented `set_temp_variable_to_random` for the temporary declaration profile and special rolls.
A normal-variable draw with the declaration profile's temporary name could leave that temporary value at its baseline.
The before/after probability handoffs retain the connected route's unresolved distribution evidence when a call times out.
- Keep static idea modifier tuning in six file-local constants, matching the documented Event 021 and Event 016 idea patterns.
These fields reject global `constant:` tokens, so the syntax route preserves the intended values without duplicating a global table.
- Use an ultimatum as the report's cause instead of assuming every selected pair shares a land border.
The global fallback can select non-neighbors.
- Report an unsuccessful Settings launch from the event's preparation helper and an unsuccessful direct root launch from the root.
The Settings dispatcher rejects an unprepared pair before the root can run, so feedback belongs at preparation as well as entry.
The owner marks `chaosx_manual_event_failure_shown` when it sends its manual-launch report, so the concurrently maintained Settings fallback does not send a second generic report for the same request.

## Integration and evidence limits

The only shared gameplay hunks initialize Random War's temporary outputs immediately before its preparation call in `chaosx_settings_effects.txt` and `chaosx_event_cluster_effects.txt`.
They preserve the existing dispatch and accounting structure.
No shared layout change is required.
Event Details remains a premise rather than a list of response effects.
The catalog note requests the current text without editing the workbook or export-only CSV files.

The supplied `evt004_sheet.jpg` and full `evt004_pop00.png` show one Random War observer report on 1 January 1936, with a readable title, description, image, and button.
Other popups in that sheet are vanilla events.
This evidence establishes the baseline observer presentation only, not evolved chains or participant responses.

The named save `qa_001_fresh_head.hoi4` was inspected read-only with `.agents/skills/chaos-redux-save-inspection/scripts/save_inspect.py info`.
It is a text save, USA democratic, normal difficulty, dated `1936.1.1.12`, version `Operation Postern v1.19.2.0.a729 (2bce)`.
This confirms the supplied QA setup only and establishes no post-change outcome.

Focused MCP event trace revision `3847e34a08e7d75169959ca12d9b601e0b82e964aff636ccd37c531ff000cd41` reports no indexed helpers and explicitly defers helper/lifecycle projections.
It is not evidence that this event lacks scripted helpers.
The user prohibits repository-wide state-flow and helper-expansion queries, so helper lifecycle review uses the source and retains that coverage limit.

The narrow event render for namespace `chaosx.nr4`, options view, 12 nodes, two levels, no helper expansion, timed out at the connected MCP limit of 600 seconds.
The narrow event comparison using the captured pre-edit revision and namespace `chaosx.nr4` also timed out at 600 seconds.
The vanilla `hoi4.source_lookup` request for `bba_switzerland.100` also timed out at 600 seconds, so the underlying vanilla file was read directly.
The report-aggregation snippet's `hoi4.script_validate` result is `SCRIPT_CHECK_PARTIAL`, `valid = null`, with syntax, command-kind, and scope checks performed.
It supports the country iterator and country flags, but leaves the `country_event` argument block unchecked and reports `else` as undocumented.
The argument syntax and the existing native `if`/`else` pattern were read directly rather than treating the partial result as validation success.

## Reference evidence

Both installed documentation and the offline wiki were consulted through `hoi4.reference_context`, `reference_search`, and `reference_read`.
The first event-inspect selector attempts were rejected until the schema was corrected to `{ kind: "event", eventId: "chaosx.nr4.1" }`.

- Installed `documentation/effects_documentation.md`, lines 2943–2967 (`country_event`), 6730–6738 (`set_country_flag`), and 3840–3857 (`every_country`), revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`.
- Installed `documentation/effects_documentation.md`, lines 7842–7858 (`set_temp_variable_to_random`) and 7910–7926 (`set_variable_to_random`), with the matching offline `Effects` row 707 and `Data structures` row 564, for half-open integer draw bounds and temporary storage.
- Offline `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, lines 900, 897, and 99 for the same commands, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
- Offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, lines 436–449, particularly caller-owned temporary output lifetime and unscoped temporaries at lines 440–442.
- Installed `documentation/script_concept_documentation.md`, lines 216–233, and `common/script_constants/documentation.md`, lines 1–85, for global constants, supported fields, and schema-first groups.
- Installed `documentation/modifiers_documentation.md`, lines 1837–1841, 1957–1961, 2403–2407, 3440–3444, and 4552–4556, with the matching offline `Modifiers - Hearts of Iron 4 Wiki.md` rows 942, 956, 962, 1205, and 1209.
- Vanilla `events/BBA_Switzerland.txt`, country-event option and flag pattern, including the Frankfurter response options at lines 219–283.

## Live acceptance checks

1. Load the fresh 1936 USA setup and force Random War once from Settings at Calm World.
Expect one observer news popup naming the actual pair and matching Event Log history.
2. On a fresh test state, set Chaos to 200, 400, 600, 800, and 1000+ and force one invocation at each tier.
Expect the enabled stage's declaration target, one aggregate news, and at most one response for each participant.
Disable the highest evolution and verify selection falls to the next enabled eligible stage.
3. Arrange too few eligible countries to close the chosen chain.
Expect no illegal declaration, a truthful distinct-country total, and one response per involved country.
4. Force the Wars cluster with repeated Random War slots.
Expect every successful slot to select a fresh pair, respect participant cooldowns, and name its actual aggressor in history.
5. Remove all legal pairs through alliances, existing wars, and participant cooldowns, then force from Settings.
Expect one "No Declaration of War" report and no declaration.
6. Play a selected defender and choose each response in separate fresh tests.
Expect the documented cost, only the three documented modifiers, no flat or weekly manpower grant, and expiration after 45 days.

No game was launched by this agent.

## Current parent reconciliation, 2026-10-06

The accepted source repair tranche is committed as c45a0f4988574390182f3683eb1d4b8e249e8bf4.
The updated specialist handoff records current conditional shares of 80/20 and 70/30 across four named scenarios.
Older failed-evaluation paragraphs remain historical; before/after comparisons and direct-random distributions remain unresolved after 600-second timeouts.
Source retains one observer report plus at most one participant response, defender precedence, prepared-profile persistence/reset and calibrated reserves without native manpower gifts.
See `release_qa_completion_20261006.md` for current dispositions, source evidence and review gates.
