# Equipment Choice
## Part 2. Useful manifests and substantial quantities

## The value allowance

Build one baseline value allowance for each recipient and firing.
The allowance is an internal balance measure expressed in equipment production value.
The player receives equipment and sees equipment quantities.
The allowance is never spendable, transferable, or shown as a national resource.

Use the following initial tuning model.
All coefficients, thresholds, rounding sizes, and caps belong in one documented tuning source.
The equations are design requirements and calibration anchors, not unverified HOI4 syntax.

- M is the recipient's controlled military-factory capacity, capped at 100 for this calculation.
- C is controlled civilian-factory capacity, capped at 100.
- K is controlled dockyard capacity, capped at 40.
- W is one when the recipient is at war and zero otherwise.
- D is one when a verified fielded-equipment assessment finds a deficit of at least 25% in a compatible major army equipment family, and zero otherwise.

The industrial subtotal is `1,500 + 160 M + 40 C + 80 K`, bounded between 2,000 and 25,000.
The baseline allowance B is that subtotal multiplied by `1 + 0.20 W + 0.15 D`.
The largest possible B under these input caps is 33,345.
The 25,000 subtotal ceiling leaves tuning headroom above the current 24,700 capped-input subtotal.
A zero-demand or unverified-demand denominator cannot create D.

Factory capacity is a defined snapshot of controlled economic capacity.
Do not substitute available factories after trade, consumer goods, or decision reservations without documenting that change and its balance effect.
Do not count an overlord's capacity twice for its subject.
The shortage assessment reads actual equipment demand or fielded shortfall through a verified source contract.
Division count alone cannot create an emergency multiplier.

| Illustrative recipient | M, C, K | War and severe deficit | B | Concentrated evolved allowance | Combined immediate total |
| --- | --- | --- | ---: | ---: | ---: |
| Very small state | 0, 2, 0 | Neither | 2,000 | 6,000 | 7,200 |
| Established minor | 10, 20, 0 | Neither | 3,900 | 11,700 | 14,040 |
| Minor under severe wartime pressure | 10, 20, 0 | Both | 5,265 | 15,795 | 18,954 |
| Industrial power | 60, 60, 15 | War only | 17,640 | 52,920 | 63,504 |
| Capped industrial inputs | 100, 100, 40 | Both | 33,345 | 100,035 | 120,042 |

These examples test the design arithmetic.
They do not claim that these are measured countries or engine balance results.
The allowance, equipment profiles, per-format quantities, and unusual family are frozen from the firing snapshot.
Handling and setback risk receive a final immutable quote at the commitment confirmation, using the schedule rule in Part 3.
Dismissing divisions, trading equipment away, or changing a production line after the offer opens cannot enlarge it.

## Converting value into equipment

Each manifest row resolves a concrete equipment token, a finished variant and creator where applicable, a value per unit, a positive whole-unit quantity, and the recipient's consumer or reserve-use reason.
Use the actual definition and complete module cost when resolving value.
If the engine has no supported runtime accessor for that value, build a reviewed provider table from the current definitions and module combination.
Regenerate that table when the content changes.
A generic chassis cost is insufficient for a finished modular vehicle.

Divide each category's allocated value among its component rows, then round down to sensible lots.
Use initial lot sizes of 50 for infantry equipment, 10 for support and towed guns, 5 for vehicles, and 1 for aircraft, trains, convoys, and unusual complete sets.
An unusually small legal row can use a smaller lot to preserve a positive useful allocation.
Spend the rounding residual on the category's primary compatible row, within its value allowance.
Do not exceed the allowance through independent rounding of every row.
A completed conventional manifest should realize at least 90% of its allocation and normally over 95%.
If a category cannot use that much value coherently, increase useful existing rows or remove the category before publication.

For an illustrative infantry profile, assume a rifle costs 0.5 value and support equipment costs 4 value.
An 80/20 division of B = 3,900 yields 6,240 rifles and 195 support units before lot rounding.
The proposed lot rules produce 6,250 rifles and 190 support units after allocating the residual, for 3,885 value.
That example uses declared illustrative costs.
Implementation replaces them with the exact selected definitions and keeps the quoted quantities identical to the grant.

A country does not receive research merely because a higher-quality model exists elsewhere.
Prefer its highest currently usable ordinary model and a completed design already available to it.
A captured or externally created design is legal only when its creator, concrete type, complete modules, stockpile creation, and recipient use are all supported by the verified grant path.
The baseline does not roll ahead-of-time equipment generations.
The principal improvements at Evolution I are quantity and composition.
Evolution II introduces the explicitly listed unusual families.

## Conventional package profiles

Each group has one frozen manifest in a given offer.
Where a group has several sensible profiles, use the following priority rules to choose the profile from the recipient snapshot.
The player chooses between visible complete manifests and can inspect the chosen profile's contents.
Profile selection is deterministic and cannot reroll when the category is reopened.

| Group | Default value shares | Profile selection and useful prerequisites |
| --- | --- | --- |
| Infantry and support | 80% infantry, 20% support | Prefer the largest compatible infantry shortfall. For a support-heavy existing army, allow 60/40 when support demand is the greater verified deficit. Preserve a real infantry or reserve-use path. |
| Fire support | 65% artillery, 25% anti-air, 10% anti-tank | Add anti-tank only with a valid consumer and actual armoured threat or existing anti-tank demand. Reassign an omitted share to artillery and anti-air in their existing ratio. An air-threat profile can use 50/50 artillery and anti-air. |
| Mobility and armour, armoured profile | 70% complete tanks, 20% trucks, 10% support | Require a valid finished design, a compatible fielding route, plausible manpower, and usable fuel access. Select the role with a real equipment shortage or established army use. |
| Mobility and armour, transport profile | 75% trucks, 15% trains, 10% support | Use when armour is not practical or logistics shortages dominate. Omit trains where the country has no relevant rail-supply use, then place their share in trucks. |
| Aircraft | 70% primary air role, 30% complementary role | Prefer fighters under enemy air pressure, close air support for an established land-support air force, or a bomber role already in national use. Require a compatible airbase or carrier deployment route and a genuine completed aircraft design. Consolidate into the primary role when no complementary role is useful. |
| Maritime logistics | 75% convoys, 20% trucks, 5% trains | Require a coast, controlled usable port or valid existing overseas supply responsibility. A documented government-in-exile maritime route can qualify. Omit irrelevant trains and move their share into convoys. |

The transport profile and maritime profile serve different bottlenecks.
The maritime choice is about shipping and the land connection to ports.
A completed warship is a fleet object with a different creation and basing contract.
This category's promised material is genuine stockpile logistics equipment.
Its picture and text must depict the actual contents.

Airbase access and naval access are checked for the receiving country.
A base that exists only in another country's scope does not establish access without a valid engine permission.
Low fuel reduces the usefulness of vehicles and aircraft and can select a transport profile or remove an impractical air profile.
The player can still choose a clearly labelled reserve aircraft package when it has a verified future deployment path.
The AI should avoid such a reserve while an urgent immediately usable category exists.

## Complete designs and DLC

For No Step Back, a tank row resolves an actual complete tank variant with compatible modules.
For By Blood Alone, an aircraft row resolves an actual complete airframe variant.
Without the relevant designer DLC, use the corresponding genuine legacy equipment type and the same military purpose.
A locked module or unresearched chassis cannot be treated as a complete usable vehicle based solely on a variant name.
If a neutral grant design is created, give it an idempotent stable identity and verify the selected module combination for the current DLC route.

The receiving player sees the delivered role and model.
The design's creator remains the real creator used by the engine.
A recipient's own production permissions change only through the separate systems that normally grant them.
The exact validity of an unresearched creator or captured design is an implementation acceptance question.
A failed designer grant cannot be masked by a successful-looking receipt.

The five conventional purposes must remain playable in the no-DLC configuration.
The implementation supplies supported equipment equivalents for each eligible purpose.
It must test the relevant designer combinations, including both land and air designers active together.
A single successful infantry grant does not establish tank or aircraft compatibility.

## Delivery contract

Publication creates fixed per-format manifests with all rows, quantities, selected roles, and entitlement identity.
The category gives a current risk preview.
The final native confirmation captures the binding handling and setback quote.
It also captures the current human controller, control mode, and selection authority through the verified native controller contract.
If another completed transaction changes that quote materially before confirmation, close it without granting and present a fresh confirmation for the same frozen cargo.
Keep the old popup receipt immutable until its after-block closes.
The AI captures and validates the equivalent quote synchronously through the same transaction.
Commitment checks that the country identity and current authorized controller still match, the entitlement is unconsumed, the selected groups are distinct where required, and every row remains constructible and usable under its quoted contract.
A controller change, switch between human and AI control, or loss of selection authority makes the old popup's confirmation consequence-free and supplies no consent.
After it closes, preserve the same country entitlement and original deadline for the current valid human's fresh confirmation or the normal AI resolver.
Already committed country-owned cargo keeps its original delivery contract through a controller change.
A changed capability can invalidate a category before any delivery begins.
The selection reopens with a concrete explanation and the remaining valid options, preserving the original allowance and deadline with a short corrective grace period of two days when necessary.
A technical revalidation never creates a larger budget or another unusual-family draw.

Use a synchronous before-and-after measurement of each concrete stock row where the engine supports it.
Mark each actually delivered row before processing a later row.
Only missing quantities may be retried after a partial delivery.
A row that succeeded must never be granted twice to compensate for a failed sibling.
If a quoted design becomes impossible, preserve a visible incomplete entitlement and require an explicit replacement within the same group and remaining value.
Never silently transform an aircraft selection into rifles.

A fully delivered package consumes its entitlement once and publishes one national receipt.
An incomplete package cannot award completion achievements or completed-delivery Chaos.
It also cannot erase already received equipment through a broad stockpile debit.
Late callbacks are tied to the exact firing, recipient generation, consignment, and row receipt.

The country keeps delivered stock through ordinary war, capture, trade, and equipment-consumption rules.
The event does not claw stock back when its category closes or an evolution is disabled.
Recipient death cancels its undelivered entitlement and prevents inheritance by a new country that later reuses the tag.
Already existing stock follows ordinary engine treatment.
A continuing government in exile retains its identity and pending delivery when the verified engine country scope supports it.
