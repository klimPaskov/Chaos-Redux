# Fuel Crisis

## The moment the reserves disappear

Every country that exists when Fuel Crisis fires loses its entire national fuel stockpile in the same event resolution. Stored fuel becomes exactly zero. The loss happens before any player acknowledges the news.

The oil economy continues to function. Oil deposits, ownership of oil-producing states, refineries, fuel silos, trade agreements, imports, ordinary fuel generation, and existing fuel-use rules retain their pre-event state. The event removes the accumulated reserve once. Subsequent production and deliveries can immediately begin restoring it.

The strategic shock comes from the sudden loss of operational endurance. An offensive that was affordable yesterday may now compete with interception, convoy protection, training, and the rebuilding of reserves. Different countries face different choices because their usable supply, current commitments, and access to imports differ.

The disappearance remains unexplained. The presentation can show empty gauges and personnel checking intact depots. It must not establish a culprit or a physical disaster that the gameplay does not implement.

## Event identity

| Field | Specification |
| --- | --- |
| Event ID | 109 |
| Original catalog ID | 114 |
| Event name | Fuel Crisis |
| Type | Minor Fire-Once |
| Status | To Be Reworked |
| Chaos level | 1 |
| Cluster | Unassigned |
| Ordinary occurrence | Once per campaign through the shared Fire-Once system |
| Direct connection | Event 101 Tasks |
| Evolution policy | No evolutions |

These values preserve the current user brief. The supplied catalog snapshots use older identifiers and availability labels. The migration record in the implementation handoff resolves their treatment without changing this design identity.

## The exact world change

Let the affected set contain every country that exists at the instant the admitted occurrence resolves. For every member, replace the national stored-fuel amount with zero. This set includes human and AI countries, majors and minors, subjects, eligible existing exile governments, civil-war countries, and unusual Chaos Redux countries. Country status, ideology, fuel demand, oil wealth, and diplomatic alignment do not provide exemptions.

An already empty country remains empty. It still belongs to the affected set, although it contributes no positive reserve loss to the event's Chaos calculation. A country created after the completed occurrence receives its ordinary creation and stockpile behavior. The event does not return to wipe later countries.

The same national stockpile must not be processed repeatedly through subjects, faction membership, ownership of oil fields, or notification recipients. The country that happens to coordinate the event is an execution context. It is not the source of the crisis and must not be represented as its perpetrator.

| Surface at the moment of impact | Required result |
| --- | --- |
| Current national stored fuel | Exactly zero for every affected country |
| Maximum fuel storage | Its existing value |
| Oil resources and extraction | Existing resources, control, access, and rules |
| Refineries and other buildings | Existing levels, damage, construction, and output rules |
| Imports and trade | Existing agreements and delivery conditions |
| Ordinary fuel generation | Continues under the existing game rules |
| Units and military orders | Continue under ordinary fuel, supply, and activity rules |
| Fuel already represented inside deployed units or other local buffers | Remains governed by the native engine representation |
| Future fuel gains | Accumulate and are consumed normally |

The national reserve is the measurable event target. The specification does not promise that every ship, aircraft, or motorized formation becomes immobile on the same frame. Engine allocation, local buffers, and supply distribution can delay or soften operational consequences. Presentation must describe lost reserves and threatened operations accurately.

## Resolution and acknowledgment

The world change belongs to the event's immediate resolution. A player cannot postpone the loss by leaving a popup open, reverse it by closing a window, or choose an exemption through an option.

The ordinary sequence is:

1. The shared dispatcher admits one valid occurrence.
2. The event claims that occurrence before any fuel change and records the small amount of onset context needed for its one-time Chaos calculation and any enabled Tasks integration.
3. The same immediate world pass sets each affected national stockpile to zero.
4. The claimed occurrence is marked complete and its one-time world Chaos contribution is applied.
5. The shared history and a single native news announcement communicate the result through the verified framework order.

The announcement has one acknowledgment. Its purpose is to register the shock and direct attention to ordinary fuel management. It contains no policy selection. The option must never apply the wipe, award fuel, create a task, or perform cleanup that changes the outcome.

Each human observer should receive at most one announcement for the occurrence. The shared event log retains one historical record. Its report image is a log asset and does not imply another modal event.

## Why recovery differs

Recovery depends on the relationship between usable inflow and actual consumption. Domestic oil ownership alone does not determine the result. A country can have substantial oil resources and still consume its output faster than it replenishes a reserve. A country relying on imports can recover quickly if delivery remains dependable and operating demand is restrained.

For explanation and balance review, use this accounting relationship:

**Next reserve = current reserve + fuel actually received or produced − fuel actually consumed**, bounded by the native storage floor and capacity.

This is a design explanation, not replacement engine code. The game remains responsible for the actual hourly or daily calculation, conversions, delivery losses, modifiers, and rounding.

A country with a positive balance can rebuild a buffer while continuing selected operations. A country at balance may operate with little reserve and remain exposed to disruption. A country with a deficit must reduce consumption, secure more usable supply, or accept deteriorating operational freedom.

There is no fixed crisis duration and no global recovery day. The event is a completed historical occurrence while individual countries continue recovering through their ordinary economies. Recovery itself does not require an Event 109 completion button.

## The first decisions the player faces

The player should be able to answer three questions from existing fuel information and the announcement:

1. Which operations are consuming the scarce fuel now arriving?
2. Which of those operations protect something the country cannot afford to lose?
3. What combination of lower demand and more dependable supply can restore a useful reserve?

The resulting play belongs to existing military, trade, construction, and diplomacy interfaces. A naval power might preserve escorts while suspending exercises and distant sorties. A land power might concentrate fuel on a narrow armored effort while restricting less urgent movement. A country under air attack might preserve interception and postpone training. Another country may accept a quieter period to rebuild a reserve.

These are adjustable operational choices. The event does not lock a country into a permanent land, air, naval, or reserve stance.

## Chaos impact map

The disappearance is a concrete abnormal world event and should contribute Chaos when fuel is actually lost. The following numbers are proposed starting balance values for this rework. They are not observations from an implemented Event 109.

Define two temporary counts during the onset pass:

- **N** is the number of affected countries with positive national stored fuel immediately before their wipe.
- **W** is the number of those countries that are majors and are currently at war.

Each country contributes at most once to each count. Count countries rather than war pairs or opponents.

| Milestone | Why it matters | Direction and proposed starting value | Scaling and repeat rule | Overlap and reversal |
| --- | --- | --- | --- | --- |
| Accepted occurrence with N = 0 | No additional stored fuel was destroyed | 0 | Record the occurrence normally, without inventing a loss | No later compensation |
| Actual wipe with N from 1 to 2 | A material national reserve disappears | +10 | One world contribution for the occurrence | Does not include subsequent war or casualty effects |
| Actual wipe with N from 3 to 9 | Several countries lose operational endurance together | +15 | Replaces the preceding band | Does not stack with another Event 109 manifestation award |
| Actual wipe with N of at least 10 | Reserve loss reaches a broad international scale | +20 | Replaces the preceding bands | Lowest proposed broad-world band for this small event |
| W of at least 2 during a positive-loss occurrence | Multiple major belligerents lose reserves together | Additional +5, with total capped at +25 | Added once to the selected onset band | Measures the simultaneous reserve shock, not the act of declaring war |
| Ordinary shortages and later oil competition | Consequences develop through existing campaign systems | No further Event 109 contribution | No recurring fuel-loss or shortage check | Generic war, annexation, and other shared sources retain their own accounting |
| Country refills fuel through ordinary play | One country regains a buffer | No automatic Event 109 reduction | No refill farming or repeated refund | Existing natural Chaos decline continues |
| Fuel-related Tasks success or failure | A selected player completes or misses an Event 101 challenge | Event 101 owns any existing outcome contribution | One terminal Tasks outcome | Event 109 adds no second reward, penalty, or Chaos adjustment |

The final onset value is one world write. Applying this value separately to every country would multiply a modest world shock into a much larger event and is incorrect.

A deliberate force replay can create a new actual wipe through the shared force feature. It receives its own occurrence accounting under that feature. Duplicate delivery of an already consumed occurrence contributes nothing.

The first committed occurrence consumes the ordinary once-per-campaign slot even if it arrived through an explicit force request or a raw direct-debug call. Later deliberate force replays never reopen that slot. Part 4's achievement requires an eligible ordinary occurrence and excludes forced and raw direct-debug origins.

## Durable consequences

Fuel Crisis creates a temporary change in strategic opportunity whose length is set by the campaign. A country that preserved essential operations may regain freedom quickly. A country that fought at its old tempo may need a longer period of rationed activity. A producer that restores exports can become diplomatically valuable. A secure trade corridor can become more important than additional nominal storage.

These outcomes are ordinary responses to the original loss. Oil diplomacy, hoarding, expensive unofficial trade where supported by an existing system, competition over oil fields, and substitute-fuel investment remain part of that response. They are not stages or mutations of Fuel Crisis.

The recovery patterns, costs, and illustrative examples are developed in Part 2. Part 3 defines the bounded connection to Tasks. Part 4 describes the announcement, shared log presentation, and achievement. Part 5 defines design acceptance and balance review. The separate implementation handoff contains the technical ownership and verification contract.
