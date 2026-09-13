# Event 54 Technology Registry Prompt

Use `chaosx_scripted_system_architect` to design and implement the reusable owner-registration contract for Event 54, Gift from Scientists.

## Context

Event 54 grants random completed technologies to every valid research participant. Ordinary technologies enter through Event 54's active-graph inventory. Custom Chaos Redux technologies remain excluded until their owner explicitly registers an eligible candidate. Evolution II and Evolution III may draw those registered candidates.

Read the full Event 54 specification pack, especially Part 2 and the technology eligibility matrix. Read `AGENTS.md`, the events skill, the dynamic effects and triggers registries, Event 16's custom technology grant API and documentation, every currently proposed owner technology definition, the active vanilla technology documentation, and the mandatory offline wiki pages.

Use `hoi4.tech_inspect` before design decisions. Render affected folders and branches. Use `hoi4.tech_compare` after source changes.

## Ownership model

Event 54 owns:

- recipient validation
- ordinary candidate inventory
- candidate draw and without-replacement state
- final compatibility validation
- grant receipts
- human report aggregation
- Event 54 history and achievement tracking

Each technology owner owns:

- stable provider identity
- stable candidate identity
- candidate registration
- owner-side recipient eligibility
- owner lifecycle gate
- compatibility family and conflicting technologies
- safety profile
- declared dependency package when needed
- grant callback when direct `set_technology` is insufficient
- optional public use milestone for achievement tracking
- cleanup and migration when the owner removes or replaces the technology

## Required safety profiles

Support the five specification profiles:

1. Direct jump
2. Prerequisites required
3. Grant package
4. Owner callback required
5. Excluded

A candidate without a valid profile fails closed. A grant package counts as one Event 54 draw and may grant only the explicitly declared target and setup dependencies. Every granted node is removed from later draws in the same country transaction.

## Contract rules

- Registration cannot mark an owner event fired or complete an owner project.
- Owner callbacks may grant the selected technology and declared setup only.
- Owner callbacks cannot create countries, launch event chains, add unrelated equipment, reveal hidden routes, or award the owner's normal primary reward.
- Final Event 54 validation can reject an owner-approved candidate when the recipient graph would become incompatible.
- A rejected candidate is removed from the current attempt so it cannot loop forever.
- Candidate and provider identifiers must be stable across save and reload.
- Removed or renamed providers need explicit migration or clean invalidation.
- Doctrine candidates remain outside the contract.
- DLC-sensitive candidates exist only when their current graph node and owner conditions exist.
- One provider with many technologies receives no hidden weighting bonus. Each eligible technology remains one candidate unless the final approved design declares a different rule and completes the audit-patch-compare cycle.

## Extension pattern

Prefer owner-side registration from bounded startup or owner initialization paths. Event 54 should consume registered provider data and avoid a large central switch for every future event.

Keep the public gateway event-owned unless a genuinely neutral helper has callers across several unrelated systems. When a shared registry index is useful, add only a discoverability row and keep the authoritative contract in Event 54 documentation.

Use script constants for stable profile, provider, and compatibility identifiers when supported. Use flags for boolean lifecycle state. Use event targets only when a scope pointer must survive the immediate call. Avoid persistent global targets for short-lived selection work.

## Required outputs

- event-owned scripted triggers and effects for registration and validation
- documented input, output, default, failure, side-effect, and lifecycle contracts
- owner integration examples for Event 16 and at least one different provider shape
- an inventory of all current custom technologies with explicit included, excluded, pending-owner, or blocked status
- technology graph evidence for every included candidate
- CXT coverage for any new technology or equipment definition created by the owner work
- a handoff listing changed helpers, providers, call sites, evidence, and unresolved candidates

## Validation

Test direct grants, missing-prerequisite jumps, package grants, callbacks, branch conflicts, rejected callbacks, provider removal, DLC changes, save and reload, repeated Event 54 firings, and a recipient with zero safe candidates.

Run the Event 54 probability scenarios after the registry exists. Any candidate-weight or provider-share change requires a baseline audit and `hoi4.probability_compare` after the patch.
