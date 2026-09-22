# 04. Economic Investment and Military Assistance

## Material campaign slot

Economic and military assistance share one material campaign slot per target. The sponsor has to choose between creating economic dependence and building military relationships. The global three-campaign limit also applies. A funded material project maintains the sponsor's activity in that target.

Every material action distinguishes a pledged amount, an actual paid amount, a delivery record, and an Influence award. The sponsor does not gain Influence for selecting an unaffordable contract. A decision tooltip must identify its real recipient and output.

## Economic Investment

Investment commits civilian industrial capacity for a specified period and delivers a real project inside the target. Political power is the administrative cost, not a complete substitute for industrial work. The donor's reserved factories cannot simultaneously be used for its normal construction. Available factory capacity must be checked at confirmation and on later work installments.

| Contract | Minimum stage | Political power | Civilian factories committed | Required funded work | Delivered output | Influence anchor |
| --- | --- | --- | --- | --- | --- | --- |
| Public works | Baseline | 25 | 1 | 45 funded days | One infrastructure level in a valid target state, or an explicitly selected damaged-infrastructure repair of equivalent contracted scope | 10 |
| Industrial investment | Baseline | 75 | 3 | 90 funded days | One civilian factory in a valid owned and controlled target state | 25 |
| National development program | Influence Campaigns | 150 | 5 | 90 funded days | One civilian factory and one infrastructure level, both with valid placement | 40 |
| Strategic industrial program | The Great Game | 200 | 5 | 120 funded days | One civilian factory and one military factory in valid target-owned states | 50 |

These are Event 79 grant contracts with deliberately specified output ratios. They are not a claim that their factory-days equal vanilla construction costs. Their balancing cost is the donor's real unavailable industrial capacity, duration, political expenditure, and campaign-slot use. Initial tuning must be tested against ordinary construction opportunities and takeover rewards.

Building counts are discrete quantities. Do not replace the one-factory output with five factories to satisfy the general five-point tuning convention. The country's economy affects the value and placement of an investment, not whether a valid small state can receive a single useful project.

### Placement and delivery

Show the selected state and planned building before payment. Use owned and controlled states with real space for the output. Prefer the capital's economic region, damaged core infrastructure, or an existing industrial center according to the target's needs. Avoid occupied foreign states that the minor merely controls.

Reserve logical project space across Event 79 contracts to prevent two sponsors from promising the same final free slot. Native construction can still change the state. Revalidate at each milestone and delivery. If the selected state becomes invalid, present a valid alternative before more work is charged. Do not silently move the project to a different country or grant a factory beyond its building limits.

Funded work is displayed in five-day installments. Count actual funded days using a bounded update of active industrial commitments only. A day counts when the stated factories were genuinely reserved and usable for that work interval. Preserve a partial installment of one through four funded days instead of deleting it at closure. An end-of-interval capacity check alone cannot prove that all preceding days were funded. A country that loses sufficient usable factories pauses the work clock. After 30 consecutive paused days, the sponsor must renegotiate a smaller compatible project or end the contract. No progress is awarded while the industrial commitment is unavailable.

Influence is awarded only when the contracted physical output is delivered. The project board shows its funded progress before then. If the race ends early, completed work is retained as target-owned construction credit for that exact project. The new overlord or the target can fund the remaining work through the aftermath contract. The old donor's future factory reservation is released. Past factory-days are not refunded as political power or newly created factories.

This construction-credit handoff is a required implementation surface. The installed engine must prove the factory reservation, placement, partial-work record, and post-race completion path. It must not be replaced by a temporary spirit that claims a factory was built.

### Economic dependence without another public meter

Keep bilateral records of delivered projects and their current ownership. One delivered project can support the economic-connection seed of a later, genuinely new race. The detailed target panel lists the sponsor of completed projects and how large their outputs are relative to the target's current industry. It does not turn those projects into ownership rights over the country.

A program that adds at least 10% of the target's pre-program industrial capacity, measured using a minimum denominator of 5 factories, can sponsor an economic institution for 60 days. This is a categorical relationship and has no automatic Influence income. In a larger economy, the same small project still delivers its stated Influence anchor but does not falsely become national economic control.

## Military Assistance

Military aid has two baseline forms. Equipment delivery gives real material to the target. Advisory work consumes command resources and creates a bounded training benefit. The player chooses an available form within the same action family.

| Contract | Minimum stage | Payment | Duration | Influence anchor | Delivered result |
| --- | --- | --- | --- | --- | --- |
| Advisory mission | Baseline | 25 political power, 10 command power, 10 army experience | 30 days | 10 | Target receives 10 army experience and an advisory relationship lasting 60 days. |
| Infantry assistance | Baseline | 25 political power and 500 units of usable infantry equipment | 30 days | 20 | Transfer the actual 500 weapons to the target stockpile. |
| Expanded advisory mission | Influence Campaigns | 50 political power, 25 command power, 25 army experience | 35 days | 25 | Target receives 25 army experience and an officer relationship lasting 60 days. |
| Senior advisory mission | The Great Game | 75 political power, 40 command power, 40 army experience | 30 days | 35 | Target receives 40 army experience and an officer relationship lasting 90 days. |
| Expanded military mission | Influence Campaigns | 50 political power, 1,000 infantry equipment, 50 support equipment, 15 command power | 30 days | 35 | Transfer both equipment components and establish a 60-day officer relationship. |
| Defense assistance program | The Great Game | 100 political power, 1,500 infantry equipment, 100 support equipment, 25 command power | 25 days | 45 | Transfer both equipment components and establish a 90-day officer relationship. |

The largest action has four payment types. Do not add fuel, manpower, convoys, money, army experience, and a fifth hidden payment to the same contract. The card shows at most three inline quantities and puts the full component list in the payment breakdown.

### Equipment conservation

Select actual eligible equipment variants, debit the donor's stockpile, and deliver those same usable variants or a proven equivalent representation to the target. Aggregate affordability must not be checked against all weapons and then debit a different unavailable concrete variant. Recipient gains cannot exceed donor-paid material after accounting for any explicitly priced logistical conversion.

Equipment is debited at dispatch and held in a race-owned delivery receipt until arrival. It is not available to either army during that interval. A cancellation before arrival returns the undelivered actual material once. A completed delivery is never reclaimed merely because the donor loses the race. If the engine cannot safely preserve the concrete stockpile receipt, block that implementation path until it is solved.

Material delivery uses a valid existing transport relationship or a verified project delivery adapter. Do not force volunteers into an ineligible war, create instant divisions, or fabricate naval access. Where the chosen military shipment cannot be delivered legally, advisory work remains a baseline option. Both are fully usable without an intelligence DLC. Expanded and senior advisory variants provide later-stage military routes when a valid material shipment is unavailable. They create training and institutional benefits, never fictional delivered weapons.

### Advisory and officer relationships

Advisers are a political and training commitment. They do not generate a free general, division template, or combat unit. A target can have one sponsor-aligned officer institution. Another sponsor can replace that relationship through a stronger valid institution action, while both countries retain separate Influence records.

A current verified advisory relationship raises the minimum compatibility of later military aid to 0.75. The first advisory action uses the relationship state before that new relationship is granted, so it does not improve its own Influence by creating its prerequisite in the same completion. The target's training gain and the sponsor's paid experience are separately recorded.

Volunteers and attachés already present in the normal game can contribute to seed and military-cooperation evidence. They are optional valid-world relationships, not a requirement to unlock the entire military family.

## Payment and refund interpretation

The common cost framework handles eligible quoted political, command, experience, and equipment costs. Factory reservation amount and duration are a separate owner adapter. Until that adapter has proven discount behavior, do not apply Black Friday to factory-days by guessing. Display exactly which components receive a supported discount.

The full contracted output is delivered when the final discounted payable receipt and the required industrial commitment are satisfied. Discounts cannot reduce the target's promised weapons while still displaying the undiscounted shipment. The adapter must distinguish a purchase payment discount from a physical transfer quantity. For direct donor-to-target equipment aid, the transfer quantity is the actual physical debit and is not discounted into newly created weapons. Discount eligibility for that transfer component is therefore off by default.
