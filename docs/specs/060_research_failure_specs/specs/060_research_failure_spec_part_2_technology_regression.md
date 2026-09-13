# Technology regression

## Design rule

Technology regression is the defining effect of Research Failure.
It must remove real researched technology from safe normal branches. Generic research-speed penalties cannot simulate the whole crisis.
The rollback must also preserve a valid technology graph, existing equipment, event-owned systems, mutually exclusive choices, and the country's ability to recover.

The event therefore uses an explicit Event 60 technology registry and a preflighted transaction.
It never chooses an arbitrary researched technology directly from the whole database.

## Meaning of regression

A regressed branch loses one or more advanced researched nodes while retaining the nearest valid older predecessor where one exists.
The country is pushed back to an earlier reproducible generation.
The removed work enters the lost-knowledge ledger and can normally be researched again through the ordinary technology system.

Regression represents loss of reliable production methods, verification, trained staff, design detail, and institutional continuity.
It does not mean every physical example of the technology disappears.
A country may still own advanced tanks, aircraft, ships, radios, radar stations, factories, rockets, or other equipment that it can no longer reproduce or improve consistently.

## Technology classes

Every technology considered by Event 60 belongs to one of the following policy classes.
The registry records the class explicitly instead of inferring it from a name.

### Safe linear technology

A normal technology with a clear predecessor chain and a normal research path is eligible by default once the current graph proves that removal and rediscovery are safe.
Typical fields include infantry equipment generations, artillery improvements, engineering, radar, electronics, industrial methods, conventional aircraft development, conventional naval development, and armour development.

Eligibility still depends on the exact installed tree.
A familiar vanilla field is not assumed safe merely because its name sounds linear.

### Protected branch root

A technology that establishes a mutually exclusive route, unlocks a permanent branch identity, or acts as the minimum valid node of a family is retained.
Later descendants inside the chosen branch may be regressed.
The event never clears the country's strategic branch choice and never moves it into a competing branch.

Concentrated and dispersed industry remain mutually exclusive.
Flexible and streamlined production remain mutually exclusive.
Equivalent branch choices introduced by DLC or Chaos Redux receive the same protection.

### Bundled family technology

Some nodes unlock a chassis, module family, equipment archetype, facility, or related group of dependent technologies.
They can be eligible only through a family transaction that understands every dependent node and every live consumer.
The family is rolled back as one coherent package or skipped.

A bundled rollback may remove several technology nodes while counting as one selected branch for distribution purposes.
The ledger records each removed node separately.

### Owner-controlled special technology

A technology created or governed by another Chaos Redux event, unusual weapon system, special project, transformation, custom country, or provider package is excluded by default.
It becomes eligible only when its owner registers an explicit Research Failure policy.

The owner policy must state:

- Whether the technology can be removed.
- Which predecessor or degraded state remains valid.
- What happens to existing equipment, units, facilities, decisions, and country identities.
- How rediscovery occurs.
- Whether a technology grant from another event may restore it.
- Which cleanup or reconciliation callback Event 60 must call.

A missing or malformed owner policy means exclusion.
Event 60 may read the policy, but it does not take ownership of the other system.

### Irreversible or non-researchable technology

A technology that represents a completed transformation, a one-time historical identity, a hidden setup marker, a non-researchable event reward, or an irreversible world state is never regressed unless its owner provides a complete reversible design.
A technology that cannot be researched again through a valid route cannot enter the normal lost-knowledge ledger.

### Doctrine technology

Land, naval, air, and special doctrine nodes are excluded from the baseline registry.
Event 27 owns the ordinary doctrine research concept, and doctrine trees have branching and mastery behavior that differs from normal equipment and industry research.
A later implementation may add doctrine regression only after a separate accepted design, a complete reversible doctrine map, and technology graph proof.

### Research-slot and research-system technology

A technology whose direct purpose is to grant research slots, create a research interface, unlock a special research system, or define the research database itself is protected.
Removing it while Event 60 also controls slot capacity risks duplication or permanent loss.
The institutional crisis handles research slots through its own ledger.

### Strategic weapon and terminal-system technology

Nuclear, thermonuclear, chemical, biological, alien, singularity, and other strategically exceptional technologies are excluded by default.
Normal radar, rocketry, engineering, and electronics nodes can remain eligible when safe.
A strategic branch becomes eligible only when its owner or the normal technology graph defines the status of existing stockpiles, facilities, delivery systems, decisions, condemnation, and rediscovery.

## Registry structure

The technology registry is an Event 60-owned design contract.
It should be generated or maintained from the installed technology graph, then reviewed by domain. An unverified list written from memory is unacceptable.

Each branch entry needs the following information:

| Field | Purpose |
| --- | --- |
| Branch identity | Stable internal identity for one rollback sequence. |
| Technology folder | The actual research folder or equivalent graph area. |
| Ordered nodes | The safe predecessor order for the current DLC and mod state. |
| Minimum surviving node | The oldest node that Event 60 may leave researched. |
| Protected roots | Branch choices and setup nodes that cannot be removed. |
| Bundle membership | Nodes that must move together. |
| Domain | Infantry, artillery, armour, air, naval, industry, electronics, engineering, radar, rocketry, or another approved normal field. |
| Owner | Vanilla, Chaos Redux core, or a named owner system. |
| Regression depth allowed | Maximum safe generations that may be removed. |
| Legacy consumer policy | Treatment of equipment, production, units, buildings, and designs already in use. |
| Rediscovery policy | Normal research, owner decision, special project, or owner callback. |
| DLC and tree variant | Conditions under which this entry exists. |
| Validation state | Verified, blocked, or excluded with a reason. |

The detailed matrix file in this pack defines the required registry review and evidence.

## Transaction preflight

The event must build the complete rollback plan before changing the country.
A partial plan is not applied.

The preflight records:

- The target and unique incident sequence.
- Current research-slot count and the intended floor.
- Current active research projects and their progress where the engine exposes it.
- Every researched technology in an eligible branch.
- The current frontier node of each branch.
- Every descendant and bundle dependency that would be affected.
- Existing production lines, designs, equipment, facilities, units, or decisions that depend on a candidate where those consumers can be inspected.
- The planned removed nodes in descendant-first order.
- The predecessor that will remain after each branch rollback.
- The rediscovery route for every removed node.
- The owner callback and legacy policy for every non-vanilla candidate.
- The actual severity that can be delivered safely.

If the transaction cannot meet the minimum meaningful severity for the current event level, the target is rejected before the opening event.
If no other target exists, Event 60 is unavailable.
The implementation may reduce the planned loss within the accepted severity band when the country's graph has few safe branches, but it may not fill the gap with unsafe technologies.

## Frontier selection

The event regresses advanced branch frontiers. Random historical prerequisites remain protected.

For each eligible branch, the system identifies the highest currently researched safe node whose removal leaves a valid older state.
A selected branch then rolls backward by the number of generations permitted by the evolution, registry, and target's actual depth.
The transaction removes descendants before predecessors so that no researched child remains above a missing required parent.

Branches with only the protected minimum node are skipped.
Branches already represented in the lost-knowledge ledger can be selected again only when a still newer safe frontier remains.
The event never records the same lost node twice for one country.

## Domain distribution

The rollback must feel broad, but it should also reflect the target's real scientific and military profile.
A major naval power should not lose only infantry and industry work.
A landlocked minor player should not receive fake naval losses merely to satisfy a global list.

Every transaction uses domain coverage rules:

- Baseline affects several distinct domains and normally includes at least one military equipment domain and one industrial, electronics, or engineering domain.
- Evolution I expands the number of domains and increases the chance of multi-generation losses.
- Evolution II guarantees serious losses in industrial, electronics, military, and advanced-engineering fields when the target has safe eligible nodes there.
- Evolution III approaches a whole-system frontier collapse and reaches most eligible domains.

Selection weight rises for fields the country actively uses.
Relevant evidence includes equipment production, deployed unit types, dockyards and fleet size, air production, radar and rocket infrastructure, industrial specialization, technologies currently being researched, and recent research bonuses.

Industry and electronics retain a minimum share because every advanced state depends on them.
Air and naval losses scale with actual capability and access.
Armour, artillery, and infantry equipment scale with production and fielded force.
Rocketry and radar receive greater weight for countries that have invested in those systems.

The transaction still retains a limited random component so repeated incidents do not always attack the same optimized build.

## Severity bands

The exact count depends on the installed graph and the number of safe branches.
The values below are design targets, not permission to remove invalid nodes.
A bundled family can contain several technology nodes.

| Severity | Intended branch coverage | Intended rollback depth | Typical safe node loss |
| --- | --- | --- | --- |
| Baseline | About one quarter of eligible frontier branches across several domains | Usually one generation, with rare two-generation loss in a deep branch | Roughly 6 to 12 nodes |
| Evolution I | About two fifths of eligible frontier branches | One or two generations, with stronger archive-profile weighting | Roughly 12 to 24 nodes |
| Evolution II | More than half of eligible frontier branches, including core industrial and electronics coverage | One to three generations | Roughly 24 to 45 nodes |
| Evolution III | Most safe frontier branches | Two to four generations where branch depth permits | Roughly 40 to 70 nodes |

A small or early country may lose fewer nodes because fewer safe nodes exist.
The Chaos gain and player-facing severity summary scale to the actual result.
The event must never claim a several-year regression when the applied transaction removed only a few shallow technologies.

A highly advanced country can reach the upper end of a band.
Caps remain necessary so one incident does not require the player to repeat the entire technology tree.

## Active research failure

Every active research project fails at the opening.
The slot is cleared and its current progress is lost.
This effect is separate from regression of already researched technologies.

The incident ledger records each abandoned project and the progress that was lost where the engine exposes reliable progress data.
Archive Recovery may later create a limited project-specific or category-specific rediscovery advantage, especially for a project that had reached an advanced stage before the collapse.
That support does not preserve the original progress directly and cannot exceed the value of a normal research bonus permitted by the technology system.

If the current engine cannot inspect and clear active research safely, implementation must treat the core requirement as blocked.
Silently leaving projects untouched would contradict the accepted event design.

## Research bonuses and accumulated advantages

Baseline and Evolution I primarily damage slots, speed, active projects, and technology state.
They do not indiscriminately erase every national research bonus.

Evolution II can damage accumulated scientific advantages where a safe owner exists.
Eligible targets include unused technology-category bonuses, temporary research accelerators, institution-specific stored bonuses, and similar advantages whose owner can identify and restore them.

Permanent focus rewards, characters, national spirits, MIO traits, special project progress, and event-owned research resources are protected unless their owner supplies a damage and recovery policy.
Event 60 does not delete a scientist character merely because that character contributes research speed.
It may create a specialist-loss incident only through a separate owner-aware route.

Damage to bonuses should be selective and recorded.
The player needs to know which broad advantage was lost, but internal bonus identifiers remain hidden.

## Existing equipment and designs

The country keeps all physical equipment, deployed units, ships, aircraft, stockpiles, and buildings that existed before the rollback.
Research Failure does not delete material to make the technology screen look consistent.

The design uses a legacy-consumer policy for each regressed family:

### Existing stockpiles

Existing equipment remains usable.
It can be deployed, captured, transferred, or consumed normally unless its owner system defines a safety restriction.
The event does not convert equipment into an older type automatically.

### Deployed formations

Units retain their current equipment and organization.
They do not forget combat experience or disappear.
Normal technology effects that the engine removes with the researched node may change their performance, but Event 60 should not add a duplicate blanket combat penalty for the same loss.

### Production lines

A line producing equipment whose enabling knowledge was lost becomes a legacy line only when the engine and family policy support that state safely.
The intended gameplay is reduced output, weaker efficiency recovery, higher reliability pressure, or restricted redesign until the enabling technology is rediscovered.
The line is not deleted automatically.

If the engine allows an existing line to continue at full efficiency after the technology is removed, the family policy may apply a temporary national or equipment-family penalty to represent missing tolerances and replacement expertise.
That penalty ends when the relevant technology is researched again.

If the engine deletes or corrupts the line, the candidate is blocked until an owner-safe preservation method exists.

### Equipment variants and designers

Existing variants remain.
Creating or upgrading a variant that depends on a lost base technology should be blocked by normal engine availability or an owner policy.
Designer, MIO, and variant history remains intact.
The event does not reset MIO progression or erase design organizations unless another explicit effect owns that damage.

### Ships and large projects under construction

Existing hulls and ships remain valid.
A construction line should continue as a legacy project where safe.
A technology whose removal invalidates an in-progress design is excluded until tested.

### Buildings and facilities

Radar stations, reactors, rocket sites, dockyards, air bases, and other structures remain on the map.
Their efficiency or available upgrades may be reduced through the relevant lost technology and safe family modifiers.
A structure is never deleted solely because the knowledge that built it was regressed.

## Industry and production technologies

Industrial regression has national consequences beyond the research screen.
Removing a valid industrial node may lower factory output, production efficiency, construction ability, resource processing, repair, or conversion through the technology's normal effects.
That loss is part of the event and should not be compensated immediately.

Mutually exclusive industry branches retain their chosen root and regress within that branch only.
A country never changes from concentrated to dispersed industry or the reverse.

Production-method branches with mutually exclusive choices follow the same rule.
The minimum surviving node must leave the country with a valid production system.

The standards and verification collapse profile may add a temporary reproduction penalty even when the normal removed technology effects are small.
This penalty is tied to Scientific Capacity and ends through reconstruction. Full recovery of every lost technology is not required for its removal.

## Electronics, radar, and intelligence technologies

Safe electronics and radar branches are eligible because loss of instruments, calibration, components, and trained operators fits the event closely.

Existing radar structures remain.
The country's effective radar, detection, encryption, decryption, or coordination may fall through the removed nodes.
Event 52 Intel Leaked can interact with the resulting vulnerability, but Research Failure does not automatically copy Event 52's entire intelligence effect.

Cryptology agency state, operatives, and completed intelligence upgrades are protected unless their owner provides a reversible policy.

## Armour, aircraft, and naval technologies

These domains use bundled family policies because chassis, hulls, modules, engines, weapons, and designs can have complex dependencies.

A safe rollback should normally remove a later generation while retaining an older usable chassis or hull.
The country keeps existing designs and equipment.
New construction and redesign depend on the remaining technology and the verified legacy policy.

The event should prefer fields the target actually uses, but it must not strip every current combat family at baseline.
The player should face difficult prioritization without immediate military invalidation.
Evolution III can create simultaneous crises across several active military families because its identity is a national knowledge collapse.

## Rocketry and advanced engineering

Normal rocketry, radar, engineering, and related conventional branches are eligible when their graph is linear and their live consumers remain valid.

Missile stockpiles, nuclear weapons, special facilities, custom delivery systems, and event-gated advanced projects require owner policies.
A country may retain physical weapons that it can no longer reproduce.
The owner must define whether maintenance, launch decisions, production, and rediscovery remain valid.

## Custom and modded technologies

Unknown custom technologies are excluded by default.
The registry may admit them only through a reviewed owner entry.

This rule protects compatibility with Chaos Redux event technologies and other installed mods.
It also prevents Event 60 from removing marker technologies, hidden setup nodes, or custom systems whose visible name resembles a normal technology.

A custom technology owner can select one of four policies:

- **Protected**, meaning Event 60 never damages it.
- **Regressible**, meaning it has a normal predecessor and rediscovery route.
- **Degradable**, meaning the technology remains researched but the owner applies a weaker operational state until recovery.
- **Replaceable**, meaning Event 60 removes it and the owner supplies a specific substitute or damaged version.

The policy must be explicit.

## Lost-knowledge ledger

Every removed technology creates one ledger entry containing:

- The country and incident sequence.
- The technology identity.
- Its branch and domain.
- The predecessor left researched.
- The number of generations lost in that branch.
- The owner policy.
- The legacy-consumer state.
- The date of loss.
- Whether the technology was later granted, researched, made obsolete, or restored through an owner route.
- Achievement disqualifiers linked to direct grants or foreign assistance.

The ledger drives decision visibility, AI research priority, Archive Recovery support, Gift from Scientists interaction, Event 16 opportunities, cleanup, and audit.

When the country researches or validly receives a lost technology, the entry is marked recovered once.
The relevant family penalty is recalculated.
The system then checks whether a deeper lost descendant is now reachable.

A technology restored through a direct grant still counts as recovered for gameplay, but achievements that require independent rediscovery can record the grant and disqualify that route.

## Rediscovery

Most lost technologies must be researched again through the normal research interface.
Researching them should feel faster than discovering an unknown technology once the country has rebuilt records and specialists, but it must still consume a research slot and time.

Archive Recovery unlocks bounded support such as:

- A research bonus for one selected lost domain.
- A stronger bonus for a verified predecessor series.
- Reduced ahead-of-time pressure when the technology had been researched before, if the engine supports that safely.
- An abandoned-project bonus for one project that was near completion.
- A specialist-led recovery project tied to a specific owner-approved branch.

The player selects priorities.
The system does not apply full-strength bonuses to every lost node at once.
A country with many losses must decide whether to recover industry, electronics, army equipment, air power, naval power, or another domain first.

Research sharing can increase the support available when a partner still knows the missing technology.
It does not automatically mark the technology researched.
Licensing foreign equipment can bridge a military gap without restoring domestic knowledge.

## Gift from Scientists

When Event 54 or its final accepted replacement grants a technology to a country with lost-knowledge entries, it should first search the safe lost ledger.
A compatible lost technology has priority over an unrelated new discovery unless Event 54's own design explicitly chooses another category.

The grant follows the normal compatibility rules and never changes mutually exclusive branches.
It clears the selected ledger entry, recalculates the affected family, and records that the recovery came from a direct gift.
It does not restore research slots or Scientific Capacity.

If no compatible lost entry exists, Event 54 proceeds with its normal grant logic.
The existing shared union helper can support additive donor grants, but it does not own technology removal or Event 60's selection policy.

## Brilliant Scientist and Kruger technology systems

Event 16 can interact through owner-approved opportunities:

- Verify a damaged archive series.
- Reconstruct one difficult lost branch.
- Recover tacit production knowledge.
- Accelerate an abandoned advanced project.
- Protect an Event 16-owned technology from regression.
- Offer the emergency Directorate mandate.

A Brilliant Scientist opportunity must still respect the lost ledger and owner policy.
It cannot restore an arbitrary incompatible technology or silently undo every loss.

Kruger-owned unusual technologies remain protected unless Event 16 explicitly registers them as regressible or degradable.
The Directorate's slot exemption never changes that owner rule.

## Technical evidence gates

Implementation must inspect the installed technology and doctrine data with the required HOI4 MCP technology tools.
For every included folder or branch, the implementation needs evidence for prerequisites, descendants, mutual exclusions, unlocks, grants, bonuses, references, DLC variants, and assets.

The required pass includes:

- `hoi4.tech_inspect` for the candidate branches and every owner-controlled technology considered.
- `hoi4.tech_render` for the affected folders or branches.
- `hoi4.tech_compare` after the registry and source implementation are changed.
- Direct review of the installed vanilla documentation and offline Paradox Wiki pages required by repository rules.
- Runtime validation of research removal, active-project cancellation, production lines, designs, equipment, facilities, save and reload, and rediscovery.

The exact removal effect, active research access, and slot-cap method are deliberately not specified here because the required local references were unavailable during planning.
The implementation must use the verified engine route.

A field that cannot pass the graph and runtime gates remains excluded.
A complete Event 60 implementation still needs enough verified normal branches to deliver the accepted broad regression at every evolution level.
If the engine cannot safely regress any meaningful technology set, the event remains incomplete. A research-speed-only substitute is not acceptable.
