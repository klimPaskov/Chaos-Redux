# 107 Lootboxes: rewards, probabilities, and evolutions

## Reward economy

Every box delivers an authentic benefit. Its value depends on its rarity and the recipient's useful reward opportunities at purchase time. A small country must receive something it can use, and a large country must receive more than a token quantity. Country scaling should grow more slowly than national power so that the same 50 PP does not buy an unlimited proportion of a major country's economy.

The reward pool combines immediate material relief with improvements that support a plan over the following weeks. Equipment helps fill shortages or build a reserve. Fuel can support current operations. Manpower and experience can improve readiness. Research, construction, and production support create useful opportunities for countries that are not fighting. A country should not need to enter a war, found a fleet, or activate an unrelated event simply to receive meaningful prizes.

The primary selection process has four design steps: select the shell form, select rarity, select a useful recipe from that rarity, and seal the complete scaled contents. The one-time first-fire welcome grant and each genuinely new paid purchase use fresh randomness and perform this selection once. These steps create one sealed box; only later paid purchases are purchase transactions. Reward generation does not run again on every GUI click, tooltip refresh, load, resumption, retry, or result replay. The exact RNG syntax must come from the current installed reference and the auditor's cited finding.

Names for recipe families in this part are working labels. Their purpose is to explain composition, relative strength, recipient fit, and delivery requirements. They are not final item names or localisation lines.

## Five rarities from the beginning

| Rarity | Relative frequency | Reward role | Ordinary pre-evolution composition |
| --- | --- | --- | --- |
| Common | Most frequent | Small but useful relief that justifies the transaction as a real benefit | One modest primary reward |
| Rare | Second most frequent | A useful reserve, a research opportunity, or a meaningful production improvement | One medium primary reward |
| Epic | Third most frequent | A major operational or economic improvement | One large primary reward |
| Mythic | Second rarest | An exceptional package with a strong primary benefit and a related supporting benefit | Two coherent components |
| Legendary | Rarest | The strongest jackpot budget with several complementary benefits | Two or three substantial components |

Common, Rare, Epic, Mythic, and Legendary are eligible in an ordinary box before any evolution. Mythic and Legendary have no Chaos threshold, minimum opening count, technology age, or evolution prerequisite as rarity tiers. The country may receive an early Legendary or a long series of Common results.

Within a comparable country snapshot and reward family, each tier must have a larger total benefit budget than the tier below. The Legendary budget must exceed Mythic. This comparison includes quantity, duration, charges, permanent building value, and supporting components. A visually impressive Mythic package must not quietly outvalue the strongest tier because its secondary benefits were left out of the balance calculation.

Rarity is evaluated before country-specific recipes. Removing an ineligible recipe must not remove the entire rarity or transfer that rarity's probability to Common. Each tier needs useful certified recipes for every supported recipient class. A landlocked country can still roll Legendary. A country without any compatible Chaos equipment can still receive a Mythic or Legendary package with conventional value.

## Soft adaptation after poor results

Repeated Common outcomes gradually reduce the probability of another Common result and raise the probability of every other rarity. This is a soft probability adjustment. There is no guaranteed promotion, predetermined reward sequence, forced non-Common result, or pity box.

Use a bounded country-owned poor-result history state. A completed Common opening raises it. A completed non-Common opening eases it by a modest amount. One better result need not erase a very long poor run, but successful results should gradually return the distribution toward its ordinary starting profile. Buying without completing an opening does not advance this history. Closing or reloading cannot reset it.

The history state is distinct from hidden influence. Peaceful recovery does not worsen a player's rarity odds by clearing poor-result history. An unfortunate Common run can improve the next reward odds while independently deepening influence. Lifetime openings can support audit and achievements, but lifetime count alone must not drive Common probability toward zero.

### Probability invariants

The rarity invariants are part of the accepted design in [README.md](README.md); exact weights remain tuning proposals. The probability auditor owns read-only numeric checks. The current design-math review reports that the illustrative rarity formulas normalize and preserve their stated order, but actual eligible recipe pools, omen outcome pools, engine precision, and Chaos/cadence functions remain unverified; see the [probability-review handoff](../../plans/108_wrestling_tournament_plans/subagent_handoffs/107_108_probability_review_2026-10-10.md). Do not independently repeat the audit or change weights without parent coordination.

The final balance model must satisfy these requirements in every ordinary and Premium state and in every mixture of them:

1. The five probabilities sum to one.
2. Each probability is strictly positive after conversion to the engine's supported weight precision.
3. Common is more likely than Rare, Rare more likely than Epic, Epic more likely than Mythic, and Mythic more likely than Legendary.
4. Raising poor-result pressure lowers Common and raises all four other tiers.
5. Premium improves the chance of higher tiers while preserving the full ordering and a real Common chance.
6. All finite histories still permit another Common result.
7. No hidden influence value or omen result is used to punish or improve the sealed reward roll.
8. Candidate filtering within a rarity cannot starve that tier or turn an unavailable custom reward into an empty result.

### Illustrative tuning model

These figures are **planning anchors for balance review**, not final production probabilities. The user-confirmed price, interaction count, availability of all five tiers, rarity invariants, and evolution thresholds are mandatory. Final numeric values remain candidate tuning and must satisfy the accepted invariants.

A simple model changes the total probability of Common and keeps a stable conditional split among the other four rarities. An illustrative non-Common split is 65% Rare, 25% Epic, 8% Mythic, and 2% Legendary. When Common falls, every non-Common tier receives part of the released probability.

Let poor-result pressure range from zero to one. An ordinary example starts at 70% Common and reaches 55% Common at maximum pressure. Premium shifts those endpoints to 60% and 45%. Linear interpolation between the endpoints is sufficient for a first implementation. A smooth bounded curve is also acceptable if it preserves the same ordering and is easier to express accurately in the actual engine.

| Illustrative state | Common | Rare | Epic | Mythic | Legendary |
| --- | ---: | ---: | ---: | ---: | ---: |
| Ordinary, fresh history | 70.00% | 19.50% | 7.50% | 2.40% | 0.60% |
| Ordinary, maximum poor-result pressure | 55.00% | 29.25% | 11.25% | 3.60% | 0.90% |
| Premium, fresh history | 60.00% | 26.00% | 10.00% | 3.20% | 0.80% |
| Premium, maximum poor-result pressure | 45.00% | 35.75% | 13.75% | 4.40% | 1.10% |

For the illustrative split, Common must remain above roughly 39.4% to stay more frequent than Rare. The 45% lower anchor leaves a margin. This is a mathematical ordering constraint, not a public threshold or an exact probability requirement for the final mod.

A corresponding internal pressure example uses a range of 0 to 100, adds 2 after a completed Common result, and removes 3 after another rarity. Clamping prevents runaway growth or negative pressure. This reaches maximum assistance only after a sustained poor run. Changing these rates affects responsiveness without introducing a guarantee. Production tuning should inspect shorter mixed histories as well as the extreme all-Common sequence.

The pressure used for a purchase is the value already earned from completed openings. The new purchase does not update it. On completion, the sealed rarity updates it once for future purchases. One pending box per country prevents several simultaneous purchases from drawing against a stale history value.

## Scaling that remains useful

Scale recipe quantity from a stable purchase-time country snapshot. Useful inputs include legal industrial capacity, actual force composition, supported technology, current equipment demand, operational fuel use, controlled construction opportunities, and remaining research opportunities. Treat unmet need as a bounded preference signal. It must not be possible to multiply a prize by deliberately deleting factories, disbanding the army, or emptying a stockpile immediately before opening.

Use three broad recipient bands as planning references: small economy, established regional power, and major industrial power. The final formula may be continuous. Give each reward a useful minimum for a small economy and a saturating upper bound for a large one. Equivalent countries should receive comparable value even when their currently eligible recipe lists differ.

Equipment value should be compared through the current cost and practical use of the concrete equipment model. Ten advanced vehicles are not equivalent to ten rifles. At purchase, select models the country can genuinely use or support, then seal those exact models and quantities. Do not silently update an unopened box to a newer model after research completes.

For initial tuning, an ordinary Common material reward can represent several days of a modest useful production line. Rare should represent roughly two to three times that relief, Epic roughly four to six times, Mythic roughly seven to ten times, and Legendary roughly twelve to sixteen times. These ratios compare total package budgets rather than prescribing identical quantities in every family. Permanent industrial awards need a separate long-run value check so repeated jackpots cannot grow a country's economy without a sensible saturation boundary.

Avoid direct Political Power prizes in this design. A prize that regularly refunds the purchase price would undermine the political tradeoff and create self-financing purchase loops. Experience, research, equipment, and timed advantages already provide sufficient variation.

## Reward family matrix

| Working family | Common and Rare direction | Epic direction | Mythic direction | Legendary direction | Recipient and delivery rule |
| --- | --- | --- | --- | --- | --- |
| Infantry and support stock | A useful replacement reserve, with Rare substantially larger | A broad reinforcement reserve | Large infantry reserve with a distinct useful support component | A major reserve across compatible infantry, support, and transport needs | Concrete supported models, no forced divisions or equipment debt |
| Motor transport and logistics stock | Trucks, support equipment, or other ordinary logistics stock in useful amounts | A major logistics reserve | Large transport stock plus a bounded logistics advantage | Transport, support, and operational fuel support within the top budget | Select only stock the country can use, with real fuel headroom where included |
| Armor reserve | Small appropriate-model replacement stock at the upper ordinary budget | A substantial armored reinforcement opportunity | Major armor stock with related support | Exceptional compatible armor and sustainment bundle | Requires a usable current model and actual recipient capability, no unusable prototype dump |
| Air and naval support stock | Useful aircraft or convoys where the country has a valid consumer | Major air reserve or maritime logistics relief | Strong service-specific stock and related support | Exceptional compatible air or naval logistics bundle | Service fit checked at sealing, a landlocked or airless country keeps other eligible recipes |
| Fuel | Useful emergency operating reserve | Sustained operating reserve | Large fuel reserve with useful operational support | Major fuel and logistics jackpot | Actual reserve increases by the full sealed amount, capacity support certified |
| Manpower | A meaningful addition to the country's usable manpower | A substantial reinforcement reserve | Major manpower plus related readiness support | Exceptional manpower and equipment support | Genuine manpower grant using the ordinary system, no population theft or hidden later debit |
| Army, navy, or air experience | A small or medium amount appropriate to the service | A major training or doctrine opportunity | Large experience plus related research or production assistance | Exceptional multi-part service improvement | Full usable amount, supported cap handling, no wasted overflow |
| Research assistance | Rare introduces a focused useful research charge | Stronger eligible research assistance | Several coherent research opportunities or a longer useful program | Strongest supported research package plus material follow-through | Genuine research benefits, preserved charges, no illegal graph unlock or overwrite |
| Civilian construction | Rare can offer a useful bounded construction program | Major progress or a completed useful civilian improvement | Major civilian construction plus supporting infrastructure or production | Exceptional civilian development package | Certified state selection, complete retained value, exact placement shown at reveal |
| Military construction | Rare can offer a focused production or construction program | Major military factory improvement | Strong military construction plus equipment support | Exceptional armaments development package | Existing building types and legal receiving capacity |
| Infrastructure and useful buildings | Small relevant infrastructure or production support where viable | Significant useful state improvement | Several related infrastructure benefits within one plan | Major coherent logistical or industrial development | Never place a useless building simply to satisfy a random table |
| Timed military or economic advantage | Common uses modest support, Rare a clearly useful program | Strong temporary support that changes a near-term plan | Exceptional support with a related material benefit | Longest or strongest bounded support plus a substantial reserve | Full duration starts at reveal, repeated prizes preserve earned value |
| Established Chaos equipment or resources | Added after Chaos Loot only when a small eligible packet fits the tier | A substantial compatible packet or program | Exceptional established unusual supply plus support | Strongest useful unusual package with ordinary sustainment | Existing owner registry, usable consumer, verified pure reward path |

The baseline pool must offer meaningful material, manpower, experience, research, construction, and timed-support opportunities. The broad matrix is not permission to activate unverified effect types. Each production recipe needs a certified provider and at least one acceptance case. Missing certification for a requested reward family remains visible in the implementation coverage report until resolved.

### Coherent combinations

Bundle components should help the same plan. A mobile reserve can combine compatible vehicles, transport, fuel, and a short logistics program. An industrial award can combine a civilian improvement, useful infrastructure, and a temporary construction or production advantage. A research award can combine eligible assistance with equipment or production support that makes the resulting technology useful.

Avoid bundles that simply collect unrelated rewards until a component count is reached. Do not pair naval experience with a country that has no supported naval use, award incompatible models to make a bundle appear exotic, or conceal a small primary benefit behind several negligible extras.

Every result lists each actual component. A phrase suggesting broad prosperity cannot replace exact quantities, state placements, research charges, or modifier durations. The UI may group related equipment lines for readability, but it must retain access to a complete native-text receipt.

## Capacity-safe sealed rewards

A player's state can change while a box remains unopened. A fuel reserve can fill, experience can approach its cap, another construction project can use the last slot, or a research opportunity can complete. Purchase-time eligibility alone is therefore insufficient.

The sealed record must contain the logical reward, exact quantity, provider version, and a deterministic delivery policy. Where receiving capacity is needed, the package includes the right to the real support required for the entire reward. The amount of that support may be calculated from opening-time holdings, but the sealed prize does not change. Support is a genuine benefit with its own controlled lifecycle, not an invisible excuse for lost value.

| Provider | Required full-delivery behavior | Invalid shortcut |
| --- | --- | --- |
| Fuel | Establish enough supported receiving capacity, then add the complete sealed amount to the country's actual fuel reserve | Clamping excess away, crediting only the empty portion, a fuel voucher, or reclaiming awarded fuel later |
| Experience | Preserve and make usable the entire sealed service experience through verified native cap or genuine storage support | Truncating at the cap, silently switching service, or exchanging it for unrelated points |
| State building | Use the sealed legal placement policy, adding supported real slot or capacity support when required | Placing beyond a verified cap, replacing the award with a weaker timed modifier, or declaring an invalid state complete |
| Construction progress | Apply a supported amount to a valid intended improvement with full retained value | Losing progress because the old target completed or changed owner |
| Research assistance | Preserve exact charges and strength, start duration at reveal, and select only a compatible destination under the sealed research-family policy | Overwriting an older bonus, expiring while the chest is closed, or granting a mutually exclusive technology |
| Timed support | Preserve the full new duration or earned contribution through a bounded queue or extension policy inside the existing modifier system | Replacing a stronger active bonus with a weaker one or shortening its expiry |

A queued duration for an already awarded timed benefit is acceptable because the full benefit is delivered as a retained program. It is different from postponing the material contents of the box. The player should see the real timing of that program in the receipt, and cannot be required to make another purchase or click a separate claim action.

Capacity support must not remove or invalidate still-unused prize value when it ends. Fuel support can retire only when the supported reserve fits the remaining ordinary capacity without deleting fuel. Experience support must not destroy unspent awarded experience. Additional legal state capacity or a completed building remains a real country benefit. These policies need engine proof and a long-run balance review.

If a native provider cannot meet its full-delivery contract, it remains disabled before purchase while that particular technical gap is resolved. This does not authorize deleting fuel, experience, research, or construction from the agreed design. The implementation remains incomplete for that family. Existing pending boxes from a supported earlier provider version must retain a compatible delivery path during migration.

A country can become temporarily invalid through annexation or loss of its government while a paid or welcome box waits. Preserve the pending ownership and restoration contract from Part 1. Do not invent a new recipient or give the conqueror its prize. Supported-country eligibility at the fifth activation must still yield a real delivery path for every certified recipe.

## Evolution framework

The three evolutions improve the visible reward system and enable different hidden consequence families. They use the shared evolution mechanism and its enablement, timing, and history rules. Reaching a Chaos threshold creates eligibility, while the actual unlock follows the shared event evolution pacing. Do not turn the threshold into an instant independent daily poll or grant an evolution whose shared setting is disabled.

The two entry paths both matter. A country may already have Lootboxes access when an evolution unlocks, or it may receive Lootboxes after one or more evolutions are already active. Both cases must produce the same capabilities for newly purchased boxes. A pre-fire evolved welcome opening uses the then-active evolution rules once. It does not replay several introductory reports, reset the country's private state, or issue more than the single first-fire welcome box.

| Evolution | Shared Chaos eligibility | Visible change | Hidden family enabled | Existing paid boxes |
| --- | ---: | --- | --- | --- |
| Premium Boxes | 200+ | Some purchases become a recognizable Premium form with better rarity odds at the same price | Whispered Fortune | Keep sealed form and reward |
| Bonus Drops | 400+ | Rare can gain an extra, Epic and higher receive stronger coherent bundles | The Need for Another | Keep sealed component list |
| Chaos Loot | 600+ | Eligible established unusual supplies and experimental advantages enter the recipe pool | Borrowed Prosperity | Keep sealed contents and provider version |

The evolved reward states are cumulative in the order defined by the shared evolution owner. The country does not lose a sealed box or have its contents downgraded if global Chaos later falls. If the shared system retains an unlocked evolution permanently, Lootboxes follows that state. Any supported shared setting change must preserve paid obligations and active effect expiry.

The reward snapshot and concealed consequence context have different timing. The reward uses purchase-time evolution state. The hidden episode uses actual completion-time evolution, Chaos, post-opening burden, and cadence under Part 3. Waiting through an unlock cannot improve the sealed prize or erase already earned exposure.

### Evolution I: Premium Boxes

Premium is an automatic random upgrade within the single purchase action. Ordinary boxes remain possible. The player does not choose between two differently priced rows and cannot pay more for a guaranteed improved shell. A Premium chest can still contain Common, and an ordinary chest can still contain Legendary.

For a first balance pass, a Premium incidence in the broad range of 20% to 35% provides a visible occasional upgrade without making ordinary boxes disappear. The final incidence may respond moderately to the shared Chaos environment after unlock. It must retain a strict upper bound below one and must not read the country's hidden influence or sealed rarity.

The shell is chosen before rarity and then uses its declared probability profile. Its recognizable appearance may communicate that this is an upgraded box. Its light, cracks, motion, and impact sound remain rarity-neutral until the fifth activation.

The hidden political risk becomes genuinely possible after this evolution is active and the country has exposure. Better reward odds do not pay off or cancel the hidden burden. The exact gain and omen policy remains in Part 3.

### Evolution II: Bonus Drops

Bonus Drops increases the value and composition of the same reward system. Common retains its useful single primary reward. Rare has a real chance of one small related extra. Epic gains one related supporting component. Mythic gains a third component or an equivalent increase in the useful supporting package. Legendary can reach four meaningful components, with the strongest total budget.

An illustrative Rare bonus chance of 20% to 40% is sufficient for an occasional pleasant extra. Exact bonus probabilities and component budgets belong to balance tuning. Epic-and-higher supporting components should be reliably present once this evolution is applied to the purchase, so that the evolution has a noticeable effect beyond Rare's occasional extra.

The primary reward is not reduced to pay for the extra. The evolution increases total value. Repeated identical components may be consolidated in the result display only when their full combined amount remains clear. Four component groups are the ordinary receipt ceiling. Longer equipment manifests use a readable expanded receipt within the same result, without introducing another claim step.

One box with several rewards is still one completed opening, one update to poor-result history, and one influence increase. Bonus count cannot multiply the private charge or create several omen rolls.

### Evolution III: Chaos Loot

Chaos Loot expands eligible recipe families with strange but useful supplies already established in Chaos Redux. It can provide unusual equipment, compatible resources, or experimental support whose owner has a valid grant contract. It does not require each country to qualify for every exotic reward.

Select unusual contents according to actual recipient capability. A country that already fields a registered custom equipment family is a plausible recipient of a replenishment packet. A country with a relevant supported experimental program may receive research or production support. If no unusual family is usable, its conventional recipes continue with evolved value and the same full rarity distribution.

Reuse Event 019's established equipment and provider knowledge only through a narrow reward contract. A token resolver is not permission to invoke its formation materialization, recruitment, obligation, or country lifecycle chain. Equipment should enter the intended stockpile without creating another event's divisions, debts, claims, country setup, or unrelated progression. Other owner integrations follow the same rule.

The Chaos appearance identifies the evolved supply form. It does not reveal hidden influence, an upcoming omen, or whether the sealed reward uses an unusual family. The ordinary/Premium distinction remains separate, producing the four shell combinations described in Part 4.

Borrowed Prosperity can affect the country's normal performance after exposure at this stage. Its existence never changes the validity of Chaos equipment or makes the reward secretly cursed cargo. The country receives the exceptional supplies exactly as promised.

## Fuel Crisis connection

Fuel Crisis uses accepted design ID 109; former catalog identity 114 is historical only under the user-authorized migration. No runtime implementation is claimed. Event 107's fuel-prize connection remains a proposed integration, not an existing implementation. Under this proposal, a completed fuel award increases the recipient's actual reserve, and a Lootboxes omen cannot spill it, recall it, destroy it, or disguise a missing amount as national inefficiency.

If the Event 109 integration is implemented, preserve that event's ordinary rules and add no special Event 107 fuel clawback. Verify the current source owners and fuel delivery when the link is wired; do not claim runtime behavior while the event remains unimplemented.

## Balance questions with concrete acceptance criteria

| Question | Required answer from the balance pass |
| --- | --- |
| Does Common feel empty for a major? | Its minimum and scaled quantity provide a visible useful reserve or program in the representative country fixtures |
| Does a tiny country receive a useless service reward? | Service and consumer eligibility exclude unusable recipes while retaining all five rarities |
| Does adaptation become a guarantee? | Every finite poor history retains a positive Common weight and no forced promotion path |
| Can Premium reverse the rarity order? | Every form-pressure state and mixture preserves the strict five-tier ordering |
| Can a rare jackpot finance endless political purchases? | No direct PP refund recipe, and no runaway PP-generating timed reward loop |
| Can bundles grow without limit? | Per-tier total value and component ceilings remain bounded across repeated openings |
| Can the player reroll by waiting? | Sealed contents, quantities, provider version, and reward evolution state remain stable |
| Can the player lose part of a valid prize to a cap? | Each capped provider demonstrates complete retained delivery or remains an explicit incomplete family |
| Is recovery punished by worse loot? | Peace credit changes influence only, leaving independently earned poor-result history intact |
| Does a Common-only run escape the hidden system? | Influence depends on completed openings, with genuine evolved risk at repeated exposure |

The final probability audit must evaluate complete declared pools and state transitions using the actual implementation. Mathematical planning checks establish that an example distribution is coherent. They do not establish the engine's random behavior, native weight precision, scheduling cadence, or AI purchase probability.
