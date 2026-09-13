# Event 065 Random Trait Coding Prompt

## Task

Implement the complete Event 65 rework in the Chaos Redux repository.

Read `AGENTS.md`, every file under `docs/specs/065_random_trait_specs/`, the relevant event, asset, debug, cluster, documentation, and improvement-loop skills, and the current repository source before editing.

Use Windows-native repository paths in implementation handoffs.

Do not simplify the complete trait-pool promise.

## Required prework

Run the repo explorer prompt and scripted-system architect prompt with `fork_context=false`.

Resolve the exact country-leader trait source roots, load-order behavior, recipient ledger scope, weighted selection method, report storage, global actor pattern, and cluster ID before coding around them.

Use the offline Paradox documentation and current vanilla source.

Begin event inspection with narrow `hoi4.event_inspect` queries.

Render the current event structure when useful.

Record the pre-change artifacts.

## Preserve identity

Keep:

- file `events/065_random_trait.txt`
- namespace `chaosx.nr65`
- root event `chaosx.nr65.1`
- Event ID `65`
- accepted name `Random Trait`
- Minor Repeatable registration
- sprite name `GFX_report_event_leader_trait`
- runtime image path `gfx/event_pictures/065_random_trait/report_event_leader_trait.dds`

Change shared IDs only when current source inspection proves a collision.

## Core behavior

Make `chaosx.nr65.1` the single authoritative gameplay executor.

It must resolve the active Event 65 form, process every eligible existing country-leader role, add traits, update ledgers and counters, record history and direct Chaos, then dispatch reports to human-controlled countries.

Visible reports must not grant or reroll traits.

AI countries must receive the same gameplay distribution without visible report queues.

Use one synchronized random execution path for multiplayer.

## Trait counts

Implement:

- Baseline: one distinct accepted trait per eligible leader
- Evolution I at raw Chaos `200+`: two
- Evolution II at raw Chaos `400+`: three
- Evolution III at raw Chaos `600+`: five

Use the highest enabled manifested or currently available form according to the specification.

Persist manifested Evolutions.

Do not de-evolve after a Chaos decline.

Do not invent a stronger form above raw Chaos `600`.

## Complete generated pool

Implement the registry-generator prompt.

The runtime source of truth must be generated from every final loaded vanilla and Chaos Redux country-leader trait accepted by `add_country_leader_trait`.

Resolve overrides once.

Keep stable indexes.

Emit the manifest, name selector, counts, checksums, and check mode.

Do not retain the current hand-maintained list as the authoritative pool.

Do not use a small fallback pool after a registry failure.

## Roll rules

Baseline and Evolution I use weight `100` for every eligible source trait.

Evolution II uses ordinary `100` and featured `125`.

Evolution III uses ordinary `100` and featured `150`.

Several featured reasons do not stack.

Chaos Redux origin is one featured reason.

Every slot samples from the remaining eligible pool.

Reject a source ID when the recipient currently owns it, the Event 65 ledger records it, or an earlier slot accepted it.

A rejection does not consume a slot.

Stop only when the target count succeeds, the recipient is saturated, or the target becomes invalid.

Preserve strange, harmful, useless, contradictory, country-specific, ideology-specific, and route-specific outcomes.

Use the real source trait.

Fix hard technical failures without adding hidden theme filters.

## Recipient ledger

Store Event 65 source-grant history on the exact recipient identity proven by architecture inspection.

The ledger must survive save and load, leave and return, and normal leader lifecycle changes that preserve the same recipient.

A country-only ledger is unacceptable when it loses the recipient identity.

Preserve retired registry identities during migration.

## Report

After the world pass, send one report to every human-controlled country.

Show the active form, global leaders changed, global traits added, active pool count, local leader, local accepted trait names, and saturation state.

Use generated registry indexes only as hidden storage.

Render source trait names or bounded fallbacks.

Handle zero, one, two, three, and five local grants.

Keep the acknowledgment option non-mechanical.

Validate five-name layout at supported UI scales.

## History, Evolutions, and Chaos

Record one global Event 65 history row per firing.

Use the existing global or no-actor pattern.

Record an Evolution only when its evolved form successfully adds at least one trait.

Implement one-time successful manifestation Chaos:

- Baseline `+2`
- Evolution I `+3`
- Evolution II `+5`
- Evolution III `+8`

Do not multiply Chaos by leaders or traits.

When the first successful firing occurs at a higher form, grant only that form's milestone and mark lower missed milestones bypassed.

A zero-result firing grants no Event 65 direct Chaos.

## Randomizations cluster

Inspect the authoritative workbook and current source for the final cluster ID.

Prefer `event_cluster_id.randomizations = 9` only when it remains unused.

Register Randomizations as a Minor Repeatable Chaos level 1 cluster.

Register Event 65 as an optional Medium-danger member with named participation value `60`.

Use the same Event 65 executor for direct and cluster paths.

Wire settings, member availability, result status, Event Log, Event Details, and documentation.

Do not add state or country reservations.

## Debug and validation hooks

Add bounded debug tools for all stages, direct and cluster paths, small declared pools, collisions, no leader, invalidation, near saturation, saturation, registry print, counters, and cleanup.

Restrict them to the existing debug pattern.

Debug forcing must not count as ordinary achievement history where the shared system disqualifies it.

## Asset

Run the Event 65 asset prompt.

Inspect the existing DDS before reuse.

Install one valid opaque `210x176` report image.

The asset worker owns production and manifest evidence.

The main agent owns final `.gfx` wiring and in-game consumer proof.

## Localisation and documentation

Write final player-facing text from the specification's direction.

Do not copy prompt language into localisation.

Run the localisation auditor.

Update permanent Event 65 and shared system docs with implemented facts.

Run the spreadsheet alignment prompt against the authoritative XLSX.

Regenerate CSV exports through the official workflow.

## Mandatory probability workflow

Start weighted-logic work with `hoi4.probability_inspect`.

Run every scenario in `quality/065_random_trait_probability_scenario_matrix.md`.

Use exact evaluate, sweep, sequence, compare, and render routes as required by that file.

Use simulation only for declared uncertainty.

After any probability patch, run `hoi4.probability_compare`.

If the probability route is unavailable, record the blocker and do not claim completion.

## Event tools

Use `hoi4.event_inspect` before and after edits.

Use `hoi4.event_render` for the direct path, cluster path, form transitions, and report flow.

Use `hoi4.event_compare` against the pre-change baseline and after final changes.

Keep artifact references in the implementation report.

## Required route coverage table

The final implementation report must compare required and implemented coverage for:

- direct production firing
- Randomizations cluster firing
- Baseline
- Evolution I
- Evolution II
- Evolution III
- human report
- AI mutation
- no-leader result
- saturation result
- debug direct path
- debug cluster path
- save and load
- multiplayer

Report any renamed, merged, blocked, simplified, fallback, or replaced route.

## Near-completion sequence

Run:

1. probability auditor
2. localisation auditor
3. documentation curator
4. spreadsheet alignment worker
5. mandatory improvement-loop planner with `fork_context=false`
6. read-only completion auditor

Integrate every accepted improvement addendum.

Resolve every source blocker.

Provide user test steps and leave status at `Needs Testing`.

Do not set `Available` before user acceptance.

## Final report

Include:

- changed files
- generated files
- generator commands and tests
- registry totals and hashes
- exclusions
- exact weights
- probability artifacts
- event artifacts
- direct and cluster comparison
- Evolution evidence
- Chaos evidence
- report renders
- multiplayer and save evidence
- asset evidence
- docs and workbook changes
- route coverage table
- subagent handoffs
- skipped validation
- unresolved items
- focused user test steps

Keep iterating until every implementation-owned acceptance row passes.

Do not claim completion while the generated registry, weighted logic, shared integrations, or required audits are incomplete.
