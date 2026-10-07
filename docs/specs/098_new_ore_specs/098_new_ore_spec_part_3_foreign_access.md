# New Ore, part 3: Foreign access and agreements

## What an agreement grants

Foreign access grants a country the current foreign armor tier through one named deposit controlled by one named supplier. The baseline effective advantage is 20%, Deep Vein raises it to 30%, and the Super-Alloy raises it to 80%. It applies to the same applicable existing and future armor consumers as direct access.

The supplier retains its full direct benefit. Exporting does not weaken its own armor or turn direct access into a percentage allocation. Its sacrifice is strategic: another country gains useful armor, one of its limited export places becomes committed, and its freedom to end a paid agreement is constrained by the terms.

Each deposit supports two foreign recipients at baseline and three after Deep Vein. A supplier can maintain agreements with at most six distinct foreign recipients across all its deposits. A recipient can hold at most two source agreements, allowing one backup. These are access-management limits, independent of the direct armor formula.

One recipient counts once against a particular deposit. A duplicate request cannot consume another place or add another bonus. Agreements at two separate deposits are distinct records. A supplier with several states chooses the physical source assigned to an offer, making the choice of a safe or exposed deposit meaningful.

The recipient uses the strongest currently valid foreign benefit. Multiple agreements do not add together. Direct access overrides foreign access whenever the recipient controls a deposit. An existing foreign agreement may remain as a paid backup, with its cost and expiry visible, even while direct access is stronger. AI normally closes unnecessary backup commitments at expiry.

## Three agreement families

All names below describe working mechanical roles. Final decision and option wording is written during implementation from the tone directions.

| Working agreement family | What the recipient provides | Supplier's reason to accept | Baseline duration | Ongoing requirement |
| --- | --- | --- | ---: | --- |
| Commercial allocation | Equipment barter plus an adaptation cost | Receives useful support equipment and trucks while keeping sovereign armor superiority | 180 days | Countries remain valid and are not at war with each other, supplier controls the named source, applicable trade restrictions permit the agreement |
| Security allocation | Military equipment aid, adaptation effort, and an agreed native diplomatic commitment | Gains material help and a meaningful security or access relationship | 240 days | The specified guarantee, or military-access plus non-aggression relationship, qualifies the deal. Paid-term protection below applies if the supplier causes its later loss |
| Faction allocation | Adaptation effort and an occupied export place | Strengthens a selected ally's armored capability | 270 days | Both countries remain in the same faction and the supplier controls the source |

For a security allocation, the supplier chooses the qualifying commitment when it offers terms. The normal commitment is a native guarantee of the supplier by the recipient. When a useful military corridor is the actual concession, the alternative is military access granted by the recipient to the supplier together with a native non-aggression pact between them. An arbitrary relation score cannot substitute for either commitment.

The parties create those diplomatic relationships through supported ordinary diplomacy or an explicitly accepted agreement action. Existing relationships can qualify. Ending an ore agreement never silently deletes an unrelated guarantee, access right, or pact that already existed.

Faction allocation is selective. Joining the supplier's faction does not grant ore access automatically. The supplier can support a vulnerable member, a major armored ally, or a coalition partner preparing an offensive. The same foreign strength ceiling applies to every agreement family. A more expensive deal buys access and better political terms, not the controller's full armor tier.

## Costs that make sense for the bargain

Commercial allocation begins from 100 support equipment and 50 trucks for a 180-day term. Security allocation begins from 300 infantry equipment and 50 support equipment for a 240-day term. These are ordinary-price tuning anchors before the factors below. All transferred equipment must be real stock removed from the paying country's inventory and credited once to the supplier through a verified transfer contract.

The recipient also pays an adaptation effort once when an agreement starts. The anchor is 15 Army XP, or 15 Navy XP for a naval-oriented recipient choosing that eligible path. Faction allocation uses 10 XP. A recipient cannot pay a nominal air-related cost to create armor in a consumer that lacks an actual armor statistic.

The Navy XP path is available when the recipient has at least one deployed ship with positive actual armor, or an active production/refit project for a verified positive-armor ship. Otherwise the Army XP path applies. This is a choice of meaningful adaptation cost, not a requirement for receiving direct ore or a split between land and naval licences. The five-ship threshold in part 9 scales effort and is not the minimum Navy XP eligibility threshold.

Adaptation cost scales between 0.75 and 1.5 of its anchor according to the recipient's relevant armored force and existing experience with ore. Prior access can reduce repeated adaptation effort, while activating the Super-Alloy for an entirely new recipient can increase it. Existing users receive evolution upgrades without a new adaptation purchase.

Equipment prices respond to four conditions:

1. Recipient capacity. Use the recipient's relevant military and naval industrial capacity, with a square-root scale anchored at 25 relevant production facilities and bounded between 0.5 and 3.0. This makes a large military customer pay more without making tiny countries ineligible.
2. Material grade. Baseline uses 1.0, Deep Vein 1.25, and the Super-Alloy 2.0.
3. Bargaining position. A single global supplier uses 1.5. Competition from another independent controller uses 1.0. A threatened supplier seeking help can accept 0.75 for a security package. Use one bargaining factor rather than stacking several descriptions of the same leverage.
4. Term and offer. Scale equipment by the agreed term relative to the family's anchor. A premium offer adds a 1.5 factor and competes for a scarce export place.

Round ordinary equipment amounts upward to whole units. Apply eligible shared cost discounts afterward through the same quote that drives affordability and payment. The supplier receives the actual equipment paid. Discounting the payer while crediting an undiscounted amount would create equipment and is prohibited.

A commercial contract has three spendable components: two equipment types and one XP type. A security contract has the same maximum. Faction allocation has one XP component and the strategic export commitment. Every confirmation identifies exactly which resources will be spent. No action adds hidden Political Power, Command Power, or an additional cost type.

The agreed term can change from its anchor within 120–360 days. Stable cooperation and an established successfully completed prior agreement favor longer terms. An exposed source, worsening relations, or active military pressure favors shorter terms. Use 30-day increments so players can compare offers. The final term and ordinary compensation are fixed when both parties confirm. A later evolution improves the supplied material for the remaining term without repricing it.

## Negotiating without a separate diplomacy game

The agreement flow uses targeted decisions and short offer events.

1. A recipient selects a known ore state and requests one available agreement family. A supplier can also offer a place directly to a selected country.
2. The supplier sees the proposed recipient, physical source, family, duration, actual compensation, current foreign armor tier, and the place that will be committed.
3. The supplier may accept the proposal, reject it, or make one predefined counteroffer using another eligible family, a premium price, or a shorter term.
4. The recipient confirms the resulting exact terms and fresh costs. The state, supplier, recipient, capacity, diplomacy, and payment are checked again at this moment.
5. Successful payment and agreement activation occur as one logical action. If activation cannot complete, actual paid components are restored once and no place remains reserved.

A proposal is not access and is not payment. Merely opening an offer cannot give armor, equipment, XP, a reserved permanent export place, or an achievement.

An ordinary proposal remains open for 14 days. Use 7 days for a pressing wartime negotiation and up to 21 days for a distant peaceful negotiation. An unanswered proposal expires cleanly. One counteroffer is allowed within the same episode. This prevents an endless chain of new deadlines.

One country pair may have one pending proposal per physical source. A country sees at most three pending negotiations at once, ordered by urgency and expected strategic value. Overflow requests wait as ordinary available targets rather than spawning an unlimited popup queue. The human can inspect all known deposits through the map selection controls.

After rejection, the requester waits 60 days before repeating materially identical terms to the same supplier. Hostility can extend this to 120 days. A materially better offer, a change in controller, a new deposit, or a newly valid security commitment allows a new approach. Repeatedly cancelling and resending the same proposal does not evade the restriction.

## Maintaining and ending access

| Change | Result for the agreement | Payment handling |
| --- | --- | --- |
| Agreed expiry | Access ends, place becomes free, renewal may be negotiated | Completed compensation remains with supplier |
| Capture of its physical source by a different country | Agreement ends immediately, new controller chooses its own partners | Existing compensation is not recreated or automatically refunded |
| Annexation or dissolution of supplier or recipient | Agreement ends under the old country's identity | No successor receives a duplicate payment or inherited licence |
| War between supplier and recipient | Agreement ends immediately | Previously completed compensation remains spent |
| Recipient voluntarily breaks a required security commitment or leaves the required faction | Agreement ends when the relationship change is resolved | No refund for the recipient breaking its qualification |
| Supplier causes a non-hostile qualification loss in a paid commercial or security agreement | Paid access continues until its agreed expiry or a paid buyback | Supplier cannot evade its refund obligation through a native diplomatic action |
| Attribution of a non-hostile qualification loss is unavailable | Existing paid commercial or security access continues to expiry or buyback | Treat uncertain fault conservatively. Renewal still requires current qualification |
| Required faction membership otherwise ends | Faction allocation ends | Adaptation XP remains expended. Faction allocation has no prepaid equipment compensation |
| Recipient discovers or captures another deposit | Agreement remains available as a weaker backup until ended | Existing term remains paid |
| Another supplier offers access | Recipient may accept if it has a free agreement place | Strongest valid access applies, with no stacking |
| Recipient voluntarily abandons access | Access ends immediately | No refund is owed for a unilateral abandonment |
| Supplier buys back the remaining commitment | Access ends after the recorded refund is paid | Refund the unused fraction of actually transferred equipment |
| Supplier voluntarily transfers the source through an event-controlled non-hostile sale or cession | Settle all affected paid buybacks before the transfer commits, then end the source agreements | Use actual unused current/future receipts and real supplier stock. No settlement means that voluntary transfer cannot commit |
| Another native or external non-hostile transfer ends prepaid source delivery without settlement | Actual control changes and agreements end immediately | Apply the 720-day supplier-wide reliability rule below, without creating equipment or retroactive access |
| Technical rejection before activation completes | No agreement starts | Restore every actual paid component once |

Capture is a visible contract risk. The licence concerns continuing access from one controller at one place. It does not oblige a conqueror to arm the former supplier's partners. A restored former controller also needs new agreements. Terminated records do not wake up automatically when old borders return.

A supplier can recover its freedom through a buyback decision. The equipment refund equals the floor of each actually received component multiplied by remaining days divided by the original agreed days. The supplier must possess the refundable equipment before the buyback completes. XP represented already expended adaptation effort and is not refunded after a successful activation.

The buyback is paid from the supplier's current stock. It does not manufacture a refund, debit the recipient, or recalculate an old undiscounted price. If the supplier cannot pay, its paid commitment continues to expiry unless a genuine terminating event occurs. A source capture, war, or invalid country is handled by its own rule and does not wait for a buyback.

Using war solely to seize a payment still carries the normal consequences of war. The former customer records a broken ore relationship for 720 days and AI strongly avoids another prepaid deal with that supplier during the memory. There is no repeated opinion reward for signing and ending contracts.

Voluntary event-controlled non-hostile transfers, including an Event 092 sale by the actual supplying controller, must settle all affected unused paid periods through the real buyback before transferring control. The transferring event receives a verified success/failure result and cannot debit or credit the same compensation again. A title-only sale with unchanged actual control does not terminate access or require that settlement.

The ore lifecycle cannot delay an already effective native control change. If a native or external non-hostile source transfer bypasses an available settlement step and terminates prepaid access, record failed source delivery for 720 days on the former supplier. During that memory, every AI country has an absolute eligibility block on buying a new prepaid commercial/security period from it, including recipient-initiated requests, supplier offers, and renewals at other sources. Already paid valid periods remain honored. State reacquisition, a premium offer, another source, a repeated callback, or switching the source to an ally does not reset or evade that supplier-wide memory. Human customers see the recorded loss and may consciously accept the risk. It applies to a failure of delivery without asserting deliberate intent where the native origin is unknown.

Genuine hostile capture and an imposed transfer within the resulting wartime peace settlement retain the disclosed no-refund risk. They do not trigger the non-hostile supplier-wide block. A voluntary side deal with a peaceful ally is not reclassified as hostile merely because the supplier is fighting an unrelated country. Known transaction provenance and the actual parties to the territorial conflict determine the distinction.

Protection of a paid term covers supplier-caused cancellation of a qualifying pact, withdrawal of a promised relationship, and equivalent non-hostile attempts to end eligibility. It also applies when the native change cannot reliably identify who caused the loss. This rule does not need to undo the diplomatic action. It preserves the already purchased ore entitlement through the original term and any future renewal period already confirmed and paid while qualification was valid. Source capture, war between the parties, or an invalid country still ends both periods immediately. The original contract explains these different risks before payment. A protected term cannot purchase another renewal unless its current requirements are restored.

### Early renewal

Renewal can be confirmed during the final 30 days. The new period starts at the existing expiry, so buying early does not discard already paid days. It occupies the same source place and grants the same single strongest benefit. At most one future period may be confirmed for a contract.

The new period uses its own fresh quote, confirmed duration, and actual payment receipt. It is paid on confirmation, and its equipment price covers only its own future days. The recipient sees both period dates and the capture or war risk of advance payment. An uninterrupted renewal does not charge adaptation XP again. A resumed agreement after a real gap can charge the reduced repeat-user adaptation amount.

A buyback totals the unused fraction of the current period and the entire actually paid equipment amount for a future period that has not started. It must pay both from the supplier's stock before ending the agreement. A source capture, war, or invalid-country termination applies to both periods under the disclosed risk rule and creates no refund. Reassignment carries both periods without charging again. Completed periods are kept only as historical receipts needed for repeat guards and achievements.

## Reassigning an agreement to another deposit

A supplier that controls several deposits may offer to move an existing agreement to another one. The recipient must accept the new physical risk. The destination requires a free export place and a valid controller at confirmation.

The accepted reassignment preserves remaining term, paid compensation, adaptation history, and recipient identity. It consumes the new place and releases the old place together. It is not a new payment or discovery. An agreement cannot be moved after its source was lost in order to retroactively avoid termination.

This gives a multi-deposit supplier a practical advantage before the Super-Alloy. It can protect valuable partners by assigning them to safer sources, while the opponent can plan around the actual deposits supporting its enemies.

## Decisions and visible action families

| Working action | Who sees it and when | Choice and effect | Cost or commitment | AI direction |
| --- | --- | --- | --- | --- |
| Inspect a deposit | Any country after public discovery | Selects a state, shows controller and available access routes | Free information | AI uses the same registered targets |
| Request an allocation | Valid foreign country with a free agreement place | Starts a commercial, security, or faction offer | No upfront payment, bounded proposal episode | Prefer useful affordable access from a defensible supplier |
| Offer an allocation | Current controller with a free export place | Offers one named state to a selected recipient | Commits a place only after confirmation | Value military cooperation, real equipment, and recipient threat |
| Respond to terms | Named counterpart during an active proposal | Accept, reject, or make the one allowed counteroffer | Exact final payment shown before confirmation | Compare material gain with strategic risk |
| Renew an allocation | Parties in the last 30 days of a valid term | Confirms one future period starting at existing expiry | Fresh equipment payment, current qualification, no repeated adaptation XP for continuous access | Avoid paying for redundant access |
| Buy back a commitment | Supplier with an active paid agreement | Ends it after paying recorded unused compensation | Actual remaining equipment refund | Use when an emerging rival becomes more dangerous than the income |
| Abandon an allocation | Recipient of an active agreement | Ends access and releases its place | Forfeits remaining purchased term | Use when the supplier is unreliable or access has become redundant |
| Reassign the source | Supplier and recipient with a valid alternate deposit | Changes the named source with consent | A destination export place | Prefer a safer source without resetting the term |

These are contextual families. The interface presents three to five relevant primary actions for the selected situation, with six as the readability budget. Offers, current agreements, and source selection remain ordinary targeted records. AI never depends on a human selecting a source first.

## Text and feedback direction

Controller text emphasizes military advantage, the requested concession, and the risk of strengthening another country. Customer text emphasizes useful but limited access and the consequences of losing its supplier. A faction allocation can sound cooperative or transactional according to the relationship. A security bargain can carry restrained confidence, uneasy dependence, or the supplier's insistence on a tangible commitment.

Each confirmation explicitly names the source state, supplier, recipient, agreed duration, current foreign armor benefit, exact cost, and termination on any actual controller replacement, including hostile capture, friendly cession, or subject transfer. It also explains voluntary-transfer settlement, the protected paid-term rule, and advance-renewal risk where relevant. Disabled actions name the actual missing condition, such as an occupied export place, missing equipment, insufficient relevant XP, invalid guarantee, expired proposal, or changed controller.

Completed terms appear in a short readable record. The player can identify which source is supporting its armor and what would end that support without reading an internal contract ledger.
