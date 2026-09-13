# 11. Balance, Probability, and Acceptance

## Balance objective

Event 53 should force a real comparison between a known immediate sacrifice and an unknown serious consequence.

The event fails when either choice becomes automatic across most campaigns.

Payment becomes automatic when demands stay too small, arrive too rarely, or scale only from current reserves. Refusal becomes automatic when most packages are weak, easily reversible, or invalid for common countries. Refusal also becomes automatic when payment demands are so large that payment is almost never possible.

## Demand affordability targets

The implementation should measure payment availability across country sizes and tiers.

Recommended broad targets for ordinary campaign states:

| Behavior tier | Visits where payment is realistically possible | Design purpose |
| --- | --- | --- |
| Baseline | roughly 65 to 85 percent | establish the choice without making refusal constant |
| Evolution I | roughly 55 to 75 percent | broaden resource pressure |
| Evolution II | roughly 40 to 65 percent | make inability and strategic refusal common |
| Evolution III | roughly 25 to 55 percent | permit absurd demands while preserving occasional payment |

These are scenario targets, not guaranteed per-campaign probabilities. Resource type, country build, prior compliance, and current war pressure can move them.

The probability auditor should classify these results as sampled or bounded unless the complete campaign-state distribution is declared.

## Demand growth

The first payment should noticeably affect later demand strength. Growth should remain bounded.

A useful curve has:

- clear increase over the first three successful payments
- slower growth after several payments
- stronger tier multipliers at 800 and 1000 Chaos
- demand-family caps that prevent invalid engine values
- structural floors that stop stockpile dumping from making future demands trivial

Refusal history can increase demands modestly. Its stronger effect is shorter pacing and immediate consequence risk.

## Consequence severity bands

### Baseline

A baseline consequence should disrupt national planning for several months, remove a meaningful reserve, create a real political crisis, damage a strategic network, or start a bounded conflict.

It should not usually end a healthy major-power campaign by itself.

### Evolution I

Evolution I can create serious regional crises, viable breakaways, disease outbreaks, major industrial disruption, and coordinated military or border problems.

### Evolution II

Evolution II can create national-scale crisis packages, several simultaneous incidents, multi-front conflicts, and curated compound consequences.

### Evolution III

Evolution III can destroy the selected country's campaign position through catastrophe-class packages. Earlier packages remain dangerous through maximum safe severity profiles.

## Equal-probability acceptance

For every tested active pool:

- each valid package appears exactly once
- each invalid package appears zero times
- normalized probability for every active package is identical
- sum of active probabilities equals one
- severity variants do not create extra entries
- internal target candidates do not create extra Event 53 entries
- previous selection history does not change weights

This must be proven with the HOI4 MCP probability workflow after implementation.

## Target-selection acceptance

For every multiplayer test scenario:

- each valid human country appears once in the target pool
- invalid countries do not appear
- normalized probability is equal for all valid countries
- country size, major status, and host status have no effect

## Demand-selection acceptance

At Evolution I and higher:

- each valid demand type appears once
- each invalid type is absent
- normalized probability is equal among valid types
- affordability does not determine type validity unless the resource system itself is inapplicable
- amount calculation occurs after type selection

A zero-stockpile but otherwise meaningful equipment system can produce an unaffordable demand and forced refusal.

## Registry composition review

Equal package weight does not remove the need to review aggregate family exposure.

The implementation team should calculate how many valid ballots belong to broad families in representative scenarios:

- political and government
- military fracture
- war and borders
- stockpile and logistics
- industry and infrastructure
- humanitarian
- disease
- disaster
- intelligence and diplomacy
- independence and civil fracture
- catastrophe compounds

A family with many substantively distinct packages will have a larger aggregate chance. That is acceptable only when every package has a real distinct identity. Cosmetic splitting is forbidden.

## Representative probability scenarios

The mandatory scenario set appears in `quality/probability_scenarios.md`. It includes:

- one-player baseline target
- four-player uniform target selection
- Evolution I demand selection for a continental power
- Evolution I demand selection for a landlocked minor
- baseline compact peaceful country consequence pool
- occupation-heavy empire consequence pool
- maritime empire consequence pool
- Evolution II major at war
- Evolution III large empire with maximum valid registry
- pool change after loss of occupied territory
- repeated refusal with previous package still valid

## Exploit review

### Stockpile dumping

A player can spend or discard resources before a visit, but this does not guarantee a smaller demand. Structural floors and capacity anchors should preserve meaningful amounts. If the player cannot pay, refusal follows.

### Political and experience spending

Spending Political Power or experience before a visit can make payment impossible. This is a strategic risk, not a method for avoiding the event.

### Country-control pause

Giving up human control pauses visits because the selected player must make the decision. The chain stays on the country and does not retarget. Normal campaigns do not treat abandoning the country as a free gameplay action.

### Tag and cosmetic changes

Changing ideology, cosmetic identity, subject status, or capital does not clear the target. Only actual country extinction, incompatible nonhuman transformation, or proven legal-successor transfer changes lifecycle state.

### Reload and duplicate outcomes

All payments, refusals, package selections, state reservations, and adapter jobs need transaction IDs and idempotent receipts. Reload cannot apply an outcome twice.

The design does not add an achievement tied to a lucky punishment roll. This avoids rewarding repeated reloads for one random package.

### Consequence fishing

The package locks immediately after refusal. The player cannot inspect the result and switch back to payment within the same transaction.

### Adapter no-op

A package that cannot complete is absent. A selected adapter that rejects triggers one bounded redraw, followed by the guaranteed government-paralysis package after a second failure. Refusal never becomes free.

## Performance acceptance

The event must use:

- one selected target
- country-scoped delayed visits
- one bounded pause recheck
- sparse owner adapters
- temporary candidate data cleared after each transaction
- no daily, weekly, or monthly whole-world Event 53 scan
- no repeated scan of every state unless a selected catastrophe package requires a bounded one-time national transaction

The nationwide nuclear package can process many states, but only after that rare package is selected. It should use the owner-approved batch pattern when needed.

## Player-facing clarity acceptance

Every demand popup must make these points clear without a long explanation:

- what he demands
- the exact amount
- whether payment is possible
- what payment does for this visit
- that refusal is dangerous

It must not reveal hidden package lists or formulas.

The event uses normal popup presentation. No custom interface is needed to understand the choice.

## Event-system acceptance

Implementation passes only when:

- Event 53 is registered as Minor Fire-Once at Chaos level 1
- its default enabled state matches the reworked-event allowlist policy after completion
- the parent firing creates one History row
- recurring visits do not create extra firing records
- evolutions log correctly with actor and zero Chaos
- source events remain available after borrowed consequences
- borrowed consequences create no source History, pacing, cluster, evolution, super-event, or world-end bookkeeping
- target loss and successor transfer preserve invariants
- an unrelated `world_end` flag does not cancel a valid target's recurring follow-up chain

## Asset acceptance

The five report-event scenes must:

- use the verified report-event canvas and processing path
- depict the same fictional man consistently
- preserve period detail
- keep the secure location readable
- avoid supernatural visual explanation
- have source PNG, processed preview, final DDS, contact sheet, manifest, and GFX handoff
- be wired to the correct appearance variants

A single repeated image is an unapproved simplification of the accepted location family.

## Completion audit

Before completion, `chaosx_event_completion_auditor` should compare the final implementation with every file in this package.

Any missing adapter must be reported. A reserved package that cannot yet be safely activated can remain inactive only when the final completion status clearly identifies the blocker. The event cannot be called fully complete while accepted live registry entries remain silently absent.

The implementation can stage adapter activation by owner readiness, but the status and catalog must reflect the actual completed surface.
