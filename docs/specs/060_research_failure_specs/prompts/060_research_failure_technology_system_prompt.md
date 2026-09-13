# Event 60 technology and slot system implementation prompt

Design and implement the owner-owned technology regression, lost-knowledge ledger, research-slot suppression, and rediscovery APIs for Event 60.
Read `AGENTS.md`, `chaos-redux-events`, the dynamic effect registry, Event 16 custom technology documentation, the complete Event 60 pack, the offline technology and effect references, installed vanilla documentation, vanilla technology files, and every current Chaos Redux technology owner before editing.
Use `chaosx_scripted_system_architect` for bounded reusable helpers after the graph and engine behavior are inspected.

## First evidence gate

Before writing removal logic, use `hoi4.tech_inspect` and source inspection to answer:

- whether researched technologies can be removed in the current engine
- what occurs to researched descendants
- how mutual exclusions behave
- whether active research and partial progress can be cancelled or read
- how equipment, modules, variants, production lines, licences, ships under construction, buildings, special projects, and accumulated bonuses respond
- how research slots from unrelated sources can be suppressed and restored without duplication

Record exact evidence.
Unknown behavior must fail closed.
Do not replace all technology regression with a national modifier.

## Event-owned registry

Create an Event 60 registry using the fields and policy classes in `matrices/060_research_failure_technology_registry.md`.
Every eligible node or branch record must identify domain, predecessor, root protection, branch exclusivity, bundle relationships, equipment or module consumers, DLC gates, owner, regression policy, rediscovery category, and evidence status.

Default policies:

- safe linear normal technologies may regress after validation
- protected roots remain researched
- doctrine technologies remain outside Event 60
- research-slot and research-system technologies remain protected
- strategic weapon and terminal-system technologies remain protected unless their owner explicitly opts in
- event-owned and custom technologies require an owner callback or registered policy
- unknown technologies remain protected

## Regression transaction

The opening transaction must:

1. Allocate one unique incident sequence.
2. Record the target's operational slot ceiling and Event 60 owed-slot count.
3. Snapshot valid researched frontier nodes by domain.
4. Resolve predecessor closure, bundle rules, owner policies, and exclusions.
5. Select a severity-scaled set with broad domain coverage and no duplicate node.
6. Record every selected node before applying removal.
7. Apply slot suppression and active-project failure once.
8. Apply technology regression once.
9. Verify the final graph and record rejected or protected candidates.
10. Publish receipts for UI, AI, Gift from Scientists, Brilliant Scientist, achievements, reconstruction, and cleanup.

An active incident that evolves receives only the difference between its current severity and the new severity.
A pre-fire high-severity incident uses one highest-valid transaction.

## Material continuity

Do not delete existing deployed units, stockpiles, captured equipment, completed ships, buildings, or facilities.
Define a verified policy for existing production lines and unfinished ships.
The intended outcome preserves existing material while limiting future reproduction, replacement, upgrades, modules, or new lines according to the safe engine behavior.

## Slot ledger

Record the pre-failure operational ceiling.
The baseline floor is two and Knowledge Collapse uses one.
A valid Kruger mandate preserves the current operational count through Event 16 authority transfer.
Later unrelated slot gains must remain separate.
Each institute project restores one exact Event 60 owed slot once.
Scientific Capacity 100 requires every valid owed slot to be restored or formally preserved.

## Lost-knowledge API

Publish bounded owner APIs for:

- testing whether a technology is in the current lost ledger
- marking ordinary research recovery
- reconciling a direct technology grant
- selecting a compatible lost node for Gift from Scientists
- applying a Brilliant Scientist recovery opportunity
- applying owner-approved special technology degradation or recovery
- reading domain counts for AI and localisation
- closing a sequence and archiving its history
- transferring or clearing continuity during civil war, exile, liberation, and annexation

Every call must be idempotent and carry sequence proof.

## Evidence and handoff

Render every affected technology folder, compare source before and after, run every TECH scenario, and test save and reload.
Report the final registry coverage, protected families, engine findings, helper names, constants, event targets, ledger layout, slot sources, callbacks, test evidence, and unresolved owners.
