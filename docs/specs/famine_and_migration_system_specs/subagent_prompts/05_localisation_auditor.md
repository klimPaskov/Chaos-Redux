# Prompt for `chaosx_localisation_auditor`

Spawn with `fork_context=false`.

Repository root: `<MOD_ROOT>`.

Audit every player-facing famine and migration text surface:

- state modifiers
- incident and report events
- decision category header
- decisions and missions
- costs and blocked requirements
- map target text
- border policy
- Deaths reasons and log entries
- Condemnation source text
- system history
- achievements
- affected event details and docs-facing text

Read the writing direction in Parts 5 and 6.

Apply bounded fixes for missing keys, duplicate keys, BOM encoding, broken dynamic localisation, raw variables, state and country naming, cost text, tooltip clarity, namespace consistency, and cross-surface mismatch.

Writing rules:

- no em dashes
- no semicolons in sentences
- no staccato
- no dialectical contrast templates
- no generic dramatic filler
- serious treatment of famine, camps, genocide, forced movement, and death
- refugees are not inherently diseased
- distinguish evacuation, internal displacement, refugee flight, deportation, integration, return, and forced return
- do not expose hidden evidence, weights, future routes, or implementation history

Write a handoff under:

```text
docs/plans/famine_and_migration_system_plans/subagent_handoffs/localisation_audit.md
```
