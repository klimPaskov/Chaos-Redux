# Reusable cost modifier architecture

## Purpose

Event 26 requires a shared cost framework because no single Vanilla modifier reaches every purchase surface. The framework must calculate, display, charge, and refund the same final amount across script-defined actions. It must also provide a clear adapter contract for static database costs and engine-native costs.

The architecture should support later temporary universal cost sources without forcing future events to copy Black Friday checks into every action.

## Shared source model

A registered universal cost source has these fields:

| Field | Meaning |
| --- | --- |
| Source ID | Stable identity for the modifier source |
| Active trigger | Condition that makes the source apply |
| Payment ratio | Portion of the ordinary current cost that remains payable |
| Start state | Activation date and source context |
| End state | Timed expiry or explicit removal condition |
| Display key | Player-facing source name for tooltips |
| Priority | Deterministic composition order when several sources exist |
| Eligibility mask | Cost families or explicit exclusions |

Event 26 registers one source named for Black Friday. Its payment ratio is `5000` basis points at baseline and `2500` basis points during Evolution I. The full basis is `10000`.

The source registry must be source-identified. Expiry removes the Black Friday source only. It must not restore saved old costs or clear other discounts.

## Current payable cost

Every adapter begins from the ordinary payable cost that would apply at the moment of purchase without Black Friday. This ordinary cost already includes the owning system's current route modifiers, laws, ideas, discounts, surcharges, escalation, country size scaling, target scaling, and other valid campaign factors.

Black Friday applies to that result.

For one active source:

`discounted_unrounded = ordinary_current_cost × payment_ratio ÷ 10000`

The registered quantizer then rounds upward to the cost family's smallest payable unit.

This order preserves composition. A normal 20 percent discount on a base cost of 100 produces an ordinary current cost of 80. Baseline Black Friday produces 40. A normal 25 percent surcharge produces an ordinary current cost of 125. Baseline Black Friday produces 63 after integer upward rounding.

## Rounding contract

A positive ordinary cost can never become free through rounding.

### Integer resources

Use this semantic result:

`final_cost = max(1, ceil(ordinary_current_cost × payment_ratio ÷ 10000))`

Examples:

| Ordinary cost | 50 percent off | 75 percent off |
| --- | --- | --- |
| 1 | 1 | 1 |
| 2 | 1 | 1 |
| 3 | 2 | 1 |
| 5 | 3 | 2 |
| 10 | 5 | 3 |
| 101 | 51 | 26 |

### Fixed-point resources

Round upward to the smallest unit the owning system can display and pay reliably. The coverage registry records that quantum. A positive result is clamped to one quantum.

### Percentage-point costs

Round upward to the owning system's documented percentage quantum. If stability or war support is displayed to one decimal place, the transaction must use the same supported precision.

### Factory and dockyard commitments

A positive commitment keeps at least one committed factory or dockyard. A five-factory commitment becomes three at baseline and two during Evolution I.

### Zero and negative values

An ordinary zero cost remains zero. A reward, rebate, refund, or negative cost does not receive a second discount. The adapter must classify the direction of the transaction before applying a sale source.

## Transaction contract

Every script-defined qualifying action should use a shared four-stage contract.

### Quote

The quote stage calculates:

- ordinary current cost
- active universal cost sources
- final payable cost
- amount saved
- rounding quantum
- cost family
- active source display data

The quote is display data until the transaction commits.

### Affordability

The affordability check uses the final payable cost from the same calculation. It preserves ordinary reserve floors and requirements.

### Payment and commit

Payment recalculates or validates the quote at the moment of the click. The payment and action commitment occur in one effect chain when the engine surface permits it.

A transaction record stores the amount actually paid when later failure or cancellation can produce a refund.

For an action with several spendable components, quote and quantize each component separately. Each component keeps its own resource type, ordinary amount, final amount, and refund amount. Non-cost requirements remain outside the payment calculation. The complete action still commits atomically when the owning surface supports atomic payment.

Quote scratch values must stay in the payer or transaction scope, or in temporary effect-chain state. Country-specific quotations must never share mutable global scratch values that another player, AI country, tooltip, or simultaneous transaction can overwrite.

### Refund

A refund returns the amount actually paid. It must not return the undiscounted ordinary cost. A multi-component refund returns each recorded component once. The refund clears the transaction record after use and cannot be claimed twice.

## Atomicity rules

- Opening a window does not lock a price.
- Hovering a decision does not lock a price.
- Selecting a target without payment does not lock a price.
- A confirmation window must recalculate at confirmation time.
- A committed upfront payment keeps its paid amount after the sale expires.
- A delayed payment due after expiry uses the price active at payment time.
- An installment plan discounts only installments committed during the active day unless the owning system defines one atomic upfront commitment.
- Existing projects, operations, construction queues, market contracts, and missions receive no retroactive rebate.

## Display contract

The displayed amount and paid amount must share the same helper or static variant.

When the owning UI has enough room, show:

- ordinary current cost
- active sale percentage
- final payable cost
- minimum-unit rounding when it changes the mathematical result

A concise tooltip may show the ordinary cost followed by the sale cost. Do not expose internal basis points, temporary variables, helper names, or formula fragments.

When the owning UI cannot show both prices, display the final payable amount and add a short Black Friday source line in the tooltip.

## Generic helper family

Working helper responsibilities include:

| Responsibility | Required behavior |
| --- | --- |
| Resolve active sources | Build the deterministic current universal payment ratio |
| Quote integer cost | Apply source composition and upward integer rounding |
| Quote fixed cost | Apply source composition and registered quantum rounding |
| Test affordability | Compare the payer's resource to the final amount and preserve reserve floors |
| Pay registered resource | Debit the exact quoted amount once |
| Record transaction | Store paid amount, family, source, payer, and refund state when needed |
| Refund transaction | Return the recorded paid amount once |
| Format display | Expose ordinary and final cost without stale values |
| Record achievement family | Credit a completed paid transaction to the active human country |
| Clear source state | Remove only the expired universal modifier source |

Final helper names, scopes, inputs, outputs, defaults, and side effects must be documented in the owning scripted-effect or scripted-trigger documentation.

## Static and native surfaces

The shared quotation API cannot replace every static engine field. Each discovered surface receives one implementation class.

### Native composition

Use a verified engine modifier that changes the real cost and displayed cost. Confirm its stacking and rounding behavior in the installed build.

### Shared scripted transaction

Use the quote, affordability, payment, and refund helpers.

### Event-aware static variant

Create normal, 50 percent, and 75 percent records or equivalent conditional forms. Only one logical version is visible and AI-valid at a time. All variants share the same completion flags, cooldowns, targets, effects, and cleanup.

### Engine-inaccessible surface

Record exact evidence that the cost cannot be changed through current script, database, GUI, or modifier support. Do not show a fake discounted price and do not replace the action with a weaker imitation. The completion report must list every such surface.

A static strategy is valid only when the ordinary cost is static or has a finite conditional set that is fully represented. A dynamically scaled ordinary cost cannot be approximated with a few fixed variants.

## Variant integrity

When static variants are required:

- all variants represent one logical action
- only one variant can appear at a time
- completion and cooldown state is shared
- target selection is shared
- AI evaluates one variant
- effects are called through one shared helper where possible
- localisation shows the current real cost
- the normal variant returns immediately after expiry
- save and reload cannot reveal duplicate variants
- overlap with every other currently registered universal source is either fully represented, routed through a scripted transaction, or explicitly excluded with evidence

## Source composition

When several universal cost sources are active, apply them in a documented deterministic order. Each source multiplies the remaining payable cost. The final quantizer runs once after all applicable sources.

The system must not sum percentage reductions into an unbounded negative price. It must not overwrite a more specific cost rule. Static records that can overlap another universal source need the complete combined state, a scripted payment route, or a documented exclusion. The coverage registry may exclude a source from a family when a system has an explicit design reason, but that exclusion must be visible in the ledger and player tooltip where relevant.

## Public adapter contract

Chaos Redux systems added after Event 26 should register new purchase transactions with:

- one stable logical action ID
- one cost family
- payer scope
- resource or commitment type
- ordinary cost provider
- rounding quantum
- affordability provider
- payment provider
- refund policy
- display provider
- AI consumer
- DLC and route gates

Third-party mods receive automatic coverage only when they use a verified native modifier affected by the sale or call the public adapter. Arbitrary external scripted costs are outside the guaranteed coverage boundary.
