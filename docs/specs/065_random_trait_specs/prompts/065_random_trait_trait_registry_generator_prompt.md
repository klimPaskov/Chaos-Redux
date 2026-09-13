# Event 065 Random Trait Registry Generator Prompt

## Role

Implement the Event 65 generated trait registry as a bounded event-owned build tool.

Read `AGENTS.md`, the Event 65 specification package, the repo explorer handoff, the scripted-system architecture handoff, the offline country-leader trait documentation, and:

`handoffs/065_random_trait_trait_registry_schema.md`

The main implementation agent owns this work.

## Required source discovery

Inspect and declare every source root whose final loaded entries can be passed to `add_country_leader_trait`.

Include vanilla Hearts of Iron IV and Chaos Redux.

Resolve load order by final source ID.

Do not import unrelated third-party mod roots.

Do not use a regular-expression-only parser as the final source of truth.

Use a structured Clausewitz parser or an existing repository parser that correctly handles nested blocks, comments, repeated keys, and file overrides.

## Required generator behavior

Create a reproducible tool that:

- scans declared roots
- resolves final loaded IDs
- preserves override chains
- assigns stable append-only registry indexes
- preserves retired indexes
- reads reviewed featured overrides
- applies Chaos Redux origin as one featured reason
- assigns weights `100`, `125`, and `150`
- emits the runtime selection pool
- emits the registry-index name selector
- emits generated counts and checksums
- emits the full CSV and Markdown manifest
- emits duplicate, override, localisation, parser, and exclusion reports
- supports declared content profiles
- supports verbose discovery
- supports check-only mode
- returns nonzero on stale or inconsistent output

## Inclusion standard

Include every final loaded country-leader trait by default.

Do not exclude a trait for theme, country, ideology, role, usefulness, harm, contradiction, rarity, route specificity, or strange identity.

A technical exclusion requires evidence and a manifest row.

Do not keep a hidden exclusion list.

## Stable index standard

Existing source IDs keep their indexes when source order changes.

New IDs append.

Removed IDs become retired.

Do not reuse an index for a different source trait.

Provide an explicit migration map for any intentional major-version reindex.

## Generated runtime standard

One included source ID creates one runtime branch.

One runtime branch maps to one registry index.

One registry index maps to one player-facing trait name.

No source ID may appear twice in the active probability pool.

The output ordering must be stable.

Generated headers must identify the tool, source version, content profile, registry version, and checksum.

The generated pool may use a hierarchy when needed for performance.

Its final probabilities must match the equivalent flat weighted pool exactly.

## Name selector

Use the source localized name when available.

Generate a bounded Event 65 fallback mapping when the source name is missing.

Do not expose raw source IDs or registry indexes.

Do not invent effect descriptions.

## Tests

Add unit or fixture tests for:

- nested source parsing
- comments
- duplicate IDs
- load-order override
- stable indexes
- retired indexes
- stale output
- missing override target
- missing localisation
- content gate
- new vanilla trait
- new Chaos Redux trait
- duplicate generated branch
- generated weight total
- name-selector coverage
- deterministic output
- path handling on the repository's Windows workflow

Run check mode against the real current roots.

## Output

Provide:

- changed files
- generator command
- declared source roots
- game and mod versions
- test results
- active registry counts
- class counts
- origin counts
- content-profile counts
- exclusion report
- duplicate and override report
- output hashes
- unresolved engine questions
- integration handoff to the Event 65 coding path

Do not claim complete coverage until check mode passes against the final source roots.
