# Event 065 Random Trait Completion Audit Prompt

## Role

Run `chaosx_event_completion_auditor` with `fork_context=false` after implementation, asset work, probability audit, localisation audit, documentation, spreadsheet export, and the improvement loop are complete.

Read `AGENTS.md`, every Event 65 specification and prompt file, every implementation handoff, the generated trait manifest, the probability audit, the asset manifest, and:

`quality/065_random_trait_acceptance_matrix.md`

Remain read-only.

## Audit scope

Compare the accepted specification with:

- event source
- constants
- scripted effects
- scripted triggers
- generated trait pool
- registry index history
- featured overrides
- generated scripted localisation
- report localisation
- picture GFX
- report DDS
- repeatable registration
- event dispatch
- Event Log
- Event Details
- Evolution settings and history
- direct Chaos milestones
- Randomizations cluster
- debug hooks
- permanent docs
- authoritative workbook
- exported CSVs
- validation reports
- user-test handoff

## Required methods

Use narrow `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` evidence.

Read the probability auditor's exact artifacts.

Inspect report renders and asset metadata.

Inspect workbook export evidence.

Do not pass runtime, multiplayer, save, or user-owned rows from source inspection alone.

## Acceptance matrix

Evaluate every row `A01` through `A87`.

For each row record:

- pass
- fail
- blocked
- needs user review
- evidence path or artifact
- concise reason

Check the implementation route coverage table for:

- direct production path
- Randomizations cluster path
- baseline
- Evolution I
- Evolution II
- Evolution III
- human report
- AI mutation
- debug direct path
- debug cluster path
- save and load
- multiplayer

## Specific blocking checks

Block completion for:

- incomplete or stale registry
- hidden trait filtering
- duplicate source weights
- mutation in report options
- incorrect trait counts
- biased saturation fallback
- missing probability comparison
- unsynchronized multiplayer rolls
- farmable direct Chaos
- cluster ID conflict
- invalid event art
- raw report keys
- stale docs or workbook
- skipped improvement-loop handoff
- status set to Available without user acceptance

## Output

Write:

`docs/plans/065_random_trait_plans/subagent_handoffs/065_random_trait_completion_audit.md`

Include:

- final status
- acceptance table
- source and artifact map
- blocking defects
- non-blocking defects
- needs-user-review items
- skipped validation
- route coverage result
- shared-file regression result
- exact next owner for every unresolved item

Do not edit files.
