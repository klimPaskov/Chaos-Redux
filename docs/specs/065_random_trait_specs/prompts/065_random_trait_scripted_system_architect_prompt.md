# Event 065 Random Trait Scripted-System Architect Prompt

## Role

Run `chaosx_scripted_system_architect` with `fork_context=false`.

Read `AGENTS.md`, the complete Event 65 specification package, the repo explorer handoff, the event skill, the dynamic trigger and effect references, the cluster contract, and the offline country-leader trait documentation.

Remain read-only.

## Goal

Resolve a buildable and exact architecture for the Event 65 trait registry, roll engine, recipient ledger, world executor, reporting, persistence, and cluster entry path.

## Questions to answer

### Trait discovery

- Which final loaded files define traits accepted by `add_country_leader_trait`?
- How should vanilla and Chaos Redux load-order overrides be resolved?
- How are DLC-dependent definitions detected?
- Which entries, if any, fail native application?
- What structured parser should the generator use?
- How should stable indexes and retired indexes work?

### Runtime pool

- Which generated Clausewitz structure provides exact `100`, `125`, and `150` entry weights?
- Can entries be conditionally excluded inside the random primitive?
- Is hierarchical dispatch needed for performance?
- How will the hierarchy preserve exact flat probabilities?
- How will high saturation avoid source-order bias?
- How will a failed trait effect avoid consuming a slot?

### Recipient identity

- Are traits stored on character scope, country-leader role scope, ideology role, or country?
- Where should the Event 65 source grant ledger live?
- How should leave, return, exile, country transfer, copied characters, and shared roles behave?
- Which identity can be saved and compared safely during the world pass?

### Execution and reporting

- How does `chaosx.nr65.1` apply all changes before reports?
- How are human countries identified without sending reports to AI?
- How are up to five registry indexes stored for each human report?
- How is a registry index mapped to a localized source name?
- How are global counters stored safely across multiplayer report timing?

### Persistence and migration

- How are registry versions recorded in saves?
- How are removed source traits and retired indexes represented?
- How does the event behave when the mod updates between saves?
- Which values are persistent and which are temporary?

### Shared integration

- How does the direct random-event path converge with the Randomizations cluster path?
- What is the exact availability trigger?
- How are Event Log, Event Details, Evolution history, and direct Chaos milestones called?
- What global or no-actor log pattern should be reused?

### Failure behavior

- What blocks the entire firing?
- What skips only one leader?
- What evidence distinguishes saturation from failure?
- How does a stale registry fail safely without a hidden small fallback pool?

## Required output

Write:

`docs/plans/065_random_trait_plans/subagent_handoffs/065_random_trait_scripted_system_architecture.md`

Include:

- recommended architecture
- at least one rejected alternative with concrete reason when alternatives exist
- event and effect call graph
- source generator pipeline
- runtime data model
- ledger scope proof
- weighted selection proof
- persistence contract
- report data contract
- error states
- performance plan
- exact source files to add or change
- constants and ownership
- MCP and offline documentation evidence
- unresolved blockers
- implementation acceptance checks
- status of ready, blocked, or needs user review

Do not implement gameplay source.
