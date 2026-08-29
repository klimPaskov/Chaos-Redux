# Event 027: Doctrine-domain registry matrix

## Purpose

Event 027 needs one stable doctrine-domain registry. The registry lets the event support current vanilla domains, DLC domains, Chaos Warfare, and future custom doctrine families without hardcoding every choice into the global fanout.

This document defines the design contract. The coding agent must map it to current repository patterns after doctrine graph inspection.

## Registry principles

A doctrine domain enters Event 027 only when its adapter can answer every question needed for a safe country choice.

The adapter must fail closed. A valid Army domain can remain available when a broken custom domain is hidden.

The registry preserves the doctrine interface's order and identity. It does not rename tracks, merge branches, or flatten several doctrine domains into one generic pool.

The event queries the registry at country scope. It does not run a recurring whole-world doctrine scan.

## Required adapter contract

| Contract field | Required answer |
| --- | --- |
| Stable domain identity | One stable ID that remains distinct from display text. |
| Display identity | Dynamic domain name and verified domain icon. |
| Country eligibility | Whether the current country can use the domain under its DLC, origin, route, and owner-system rules. |
| Grand Doctrine state | Whether one Grand Doctrine is active and which doctrine it is. |
| Grand Doctrine adoption pool | Every Grand Doctrine the country can currently adopt when the domain is empty. |
| Grand Doctrine adoption action | A safe native or owner-system action that selects exactly one eligible Grand Doctrine. |
| Track order | Every track identity in the order used by the doctrine interface. |
| Track display | Track name and icon when available. |
| Selected subdoctrine | Current selected branch for each track, or an empty state. |
| Empty-track pool | Every subdoctrine the country can currently select in an empty track. |
| Subdoctrine selection action | A safe action that selects one eligible branch without replacing an existing branch. |
| Current mastery level | Whole-number level after native banked mastery and other effects are resolved. |
| Maximum mastery level | Exact branch maximum, with no assumption that every branch has five levels. |
| One-step advancement | A safe action that grants exactly one event-attributed mastery step. |
| Completion state | Whether the branch is complete and whether the track's native Grand Doctrine Milestone is active. |
| Native banked mastery behavior | How banked mastery resolves when the branch is selected or completed. |
| AI domain factors | Country state that makes this domain relevant or irrelevant. |
| AI doctrine factors | Strategy factors for eligible Grand Doctrines. |
| AI branch factors | Force, production, theater, route, and completion factors for tracks and subdoctrines. |
| DLC and feature gate | Exact content ownership and ruleset conditions. |
| Icon ownership | Verified sprites for domain, Grand Doctrine, track, and subdoctrine display. |
| Cleanup contract | How stale owner-system state is removed and how the adapter reports invalid state. |
| Documentation owner | Source document that explains the doctrine family and its public behavior. |

## Domain matrix

| Domain | Baseline status | Grand Doctrine model | Track model | Event 027 treatment | Main validation risk |
| --- | --- | --- | --- | --- | --- |
| Army | Required | Current vanilla Army Grand Doctrines | Arbitrary registered tracks, commonly infantry, armor, combat support, and operations | Adopt one eligible Army Grand Doctrine or advance one valid Army subdoctrine track. | Exact one-level effect and banked mastery order. |
| Navy | Required when available in current ruleset | Current vanilla Navy Grand Doctrines | Current naval tracks and subdoctrines | Adopt one eligible Navy Grand Doctrine or advance one valid naval track. | DLC topology, domain icon consumer, and naval AI strategy. |
| Air | Required when available in current ruleset | Current vanilla Air Grand Doctrines | Current air tracks and subdoctrines | Adopt one eligible Air Grand Doctrine or advance one valid air track. | DLC topology and air AI strategy. |
| Supported Special Forces content | Conditional | Include only when the installed graph exposes a compatible doctrine hierarchy | Use the installed track structure | Participate through its own adapter. | Current version and DLC model must be proven. |
| Chaos Warfare | Required custom domain | Conditional `chaos_warfare` Grand Doctrine | Four project tracks with five mastery levels each | Respect establishment gates, then advance only through the owning mastery route. | Bypassing equipment, formation, policy, readiness, technology, or operation state. |
| Future custom domain | Registry extension | Owner-defined | Owner-defined arbitrary track structure | Participate only after full adapter, AI, asset, and documentation coverage. | Incomplete callback surface or unsupported mastery semantics. |

## Army domain expectations

The Army adapter should expose the current installed Grand Doctrine and track graph without assuming the September 2025 work-in-progress examples are final.

The adapter should preserve:

- the installed doctrine names
- the installed track order
- one selected subdoctrine per track
- branch-specific mastery thresholds
- native Grand Doctrine Milestone behavior
- native doctrine and branch AI preferences
- all current DLC and country restrictions

The Event 027 Army page should show only tracks that can receive one event mastery step.

## Navy domain expectations

The Navy adapter should treat maritime relevance as AI strategy, not human availability.

A landlocked human country may select Navy doctrine when the native system permits it. A landlocked AI country normally scores the domain very low unless its focus route, future expansion, subject network, or scripted strategy gives it a credible maritime plan.

The adapter must use current naval doctrine topology. It should not assume that every naval branch, track, or mastery source exists without the required DLC.

## Air domain expectations

The Air adapter should preserve the current domain's separation between broad doctrine choice and track-specific mastery.

AI should consider actual aircraft production, wings, mission plans, airbase capacity, enemies, and strategic route. The adapter should not use a fixed major-country bonus as a substitute for air relevance.

## Supported Special Forces expectations

Special Forces content remains conditional because its exact current doctrine structure must be inspected in the installed game and DLC setup.

The adapter can be enabled when all of these are proven:

- one stable doctrine-domain identity
- eligible doctrine or track selection
- selected branch identity
- mastery levels
- exact one-step advancement
- icons
- AI strategy
- DLC gate

If current Special Forces content uses a different model, Event 027 should omit it until an owner-specific adapter is designed. The event should not translate it into Army mastery or generic experience.

## Chaos Warfare adapter expectations

The Chaos Warfare adapter must use the owning system's established compatibility IDs:

| Public track | Compatibility identity |
| --- | --- |
| Hazard Assault Formations | `extermination_columns` |
| Toxic Armored Warfare | `chemical_suppression` |
| Contaminant Fire Support | `contaminant_firebases` |
| Integrated CBRN Command | `integrated_chemical_operations` |

The adapter must expose the public name while using the correct internal identity.

### Grand Doctrine establishment

Chaos Warfare adoption through Event 027 is available only when the country satisfies the owning system's establishment rules. The supplied mechanics guide identifies equipment and fielded-formation requirements. The implementation must read the current doctrine documentation and source for the complete active gate.

The event waives the doctrine purchase cost. It does not waive the establishment package.

### Track advancement

Each track's event mastery step must enter through the same state transition used by normal Chaos Warfare mastery.

Directly setting a visible level while skipping the owner-system transition is invalid because later systems may read:

- compatibility IDs
- mastery-level flags or variables
- operation eligibility
- equipment or formation qualification
- doctrine capstones
- officer-corps effects
- Condemnation multipliers
- AI state
- documentation and event detail state

### Downstream requirements

A mastery level can be earned while a separate downstream technology, equipment, formation, policy, or readiness gate remains unmet. The downstream content stays locked until that gate is satisfied.

Event 027 should not convert a mastery grant into the direct unlock of a custom unit, chemical operation, policy, or equipment type.

## Future custom doctrine registration

A future event or system that adds a doctrine family can register it for Event 027 after completing this sequence:

1. Identify the owner system and stable domain ID.
2. Document the doctrine hierarchy and player-facing purpose.
3. Provide every adapter contract field.
4. Prove the one-step mastery action with doctrine graph inspection and comparison.
5. Provide AI domain, doctrine, and branch factors.
6. Verify icons and event-page consumers.
7. Add DLC, route, and special-country gates.
8. Add save, cleanup, and invalidation behavior.
9. Add Event 027 scenario coverage.
10. Update the doctrine-domain matrix and Event 027 documentation.

An owner should extend an existing domain adapter when it adds branches to that domain. It should create a new domain only when the doctrine family has a distinct high-level selection, track registry, mastery state, AI identity, and player-facing role.

## Option-pool contract

The registry returns only actions that can succeed now.

### Valid Grand Doctrine adoption

A Grand Doctrine is valid when:

- the domain is eligible
- the domain has no active Grand Doctrine
- the doctrine exists in the current graph
- required DLC is active
- country and route restrictions pass
- selection does not replace progress
- the owner-system adoption action is available

### Valid active-track mastery

A selected branch is valid when:

- its domain and Grand Doctrine are valid
- the track exists
- the selected subdoctrine exists
- the current level is below maximum
- the one-step advancement action is available

### Valid empty-track mastery

An empty track is valid when:

- its domain and Grand Doctrine are valid
- the track exists and has no selected branch
- at least one eligible subdoctrine exists
- branch selection is safe
- banked mastery behavior is understood
- one event mastery step can be applied without corrupting native progress

## Registry output needed by human pages

For each visible domain or branch, the adapter should make these public values available:

- localized name
- icon
- selected or unselected state
- current mastery level
- next mastery level
- maximum level
- track completion state
- native Milestone state when relevant
- concise blocked reason when a visible action can become invalid during confirmation

The event page should not reconstruct these values from hardcoded English names or branch-number assumptions.

## Registry output needed by AI

The adapter should return scores or score factors for:

- domain relevance
- eligible Grand Doctrine fit
- track relevance
- subdoctrine fit in an empty track
- completion value
- continuity value
- route-specific preference
- hard invalidation

AI factors can call owner-system triggers. They should not duplicate large custom-system state tables inside Event 027.

## Registry output needed by achievements

Every successful mastery receipt needs stable identities for:

- batch
- domain
- Grand Doctrine
- track
- subdoctrine
- event-attributed mastery step number
- branch completion at batch close

Achievement tracking should use stable IDs. Localized names and icons can change without breaking records.

## Graph validation expectations

Before and after implementation, the coding agent must use the current HOI4 MCP doctrine and technology routes to inspect:

- folders and domains
- Grand Doctrine placements
- track identities and order
- subdoctrine identities
- prerequisites and exclusivity
- mastery levels and thresholds
- unlocks and native Milestones
- effects used by mastery grants
- icons and texture references
- DLC-dependent graph differences
- Chaos Warfare graph and references

The implementation comparison must prove that Event 027 adds grant and query behavior without altering the doctrine graph itself unless an accepted graph repair is separately required.

## Registry acceptance criteria

The registry is ready when:

- every required domain has a complete adapter
- every conditional domain is either complete or explicitly absent from the current ruleset
- no invalid branch can reach a doctrine effect
- one event mastery step is proven for every supported branch family
- banked mastery sequence behavior is documented
- human option order matches the doctrine interface
- AI can score every supported domain
- achievements receive stable domain and track identities
- custom-system cleanup removes stale options
- local graph, assets, and DLC combinations pass the named acceptance scenarios
