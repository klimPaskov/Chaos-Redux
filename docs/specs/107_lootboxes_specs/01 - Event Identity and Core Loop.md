# 107 Lootboxes: event identity and core loop

## The playable promise

Lootboxes gives an affected country a permanent way to exchange Political Power for useful, unpredictable supplies. A purchase costs exactly **50 Political Power**. A large chest immediately appears in a dedicated window, and the player opens it through **five meaningful clicks on the chest itself**. The fifth click resolves the opening, delivers the entire sealed prize, and reveals its rarity. Opening costs nothing.

The reward should be attractive enough that buying another box is a plausible strategic choice. Even an ordinary Common prize has a clear practical use. A Legendary result can substantially change the country's immediate plans. The player is spending a valuable political resource on uncertainty, so the low end must provide credible value and the high end must feel exceptional.

Repeated completed openings also increase a country-specific hidden influence. This influence affects the country separately from the prize. Equipment works, fuel reaches the reserve, research assistance remains valid, and buildings retain their benefit. Later omens concern ordinary political, industrial, logistical, or military performance. Their timing and presentation must never imply that a shipment was counterfeit, damaged, stolen, or replaced with a punishment.

Real peaceful contributions through existing shared systems can reduce this influence. The country must actually contribute to a recorded reduction of the shared global Chaos Meter. Merely waiting for natural global decay, watching other countries make peace, or buying another box does not reduce the underlying influence.

## Identity and distribution

| Field | Required design |
| --- | --- |
| Event number | 107, selected by the user; shared catalog and registry migration remains parent-owned |
| Established event name | Lootboxes |
| Event type | Minor Fire-Once in the imported design; unresolved pending parent acceptance |
| Package disposition | Explicitly confirmed core constraints are accepted; remaining imported design claims are unresolved. See [README.md](README.md). |
| Chaos level | 1 in the imported design; unresolved pending parent acceptance |
| Cluster | Standalone in the imported design; unresolved pending parent acceptance |
| Recipient | The country selected by the normal event recipient route |
| Lasting access | One permanent country-owned Lootboxes category |
| Repeatable activity | Buying and opening boxes after access has been granted |
| Purchase price | Exactly 50 Political Power for every box |
| Opening price | Zero |
| Opening interactions | Five accepted chest activations |
| Pending inventory | One paid, unresolved box per country |

The initial event retains the shared Fire-Once selection contract. Repeat purchases do not re-fire the opening event, count as new initial event occurrences, or turn its catalog entry into a repeatable event. Normal event selection may offer it independently without a cluster-member severity.

Access does not require the recipient to have 50 Political Power at the moment the event arrives. A country with little Political Power can receive the category and purchase later. War, peace, ideology, subject status, and a small industrial base are not additional Lootboxes access gates. The normal shared recipient filter remains responsible for excluding invalid administrative, deleted, or test-only recipients from ordinary selection.

An implementation must preserve this narrow distribution. It must not grant access to every country merely because one country received the initial event. Forced test or existing administrative delivery routes must use the same idempotent access helper. Repeating such a request for the same country must not reset its pending box, reward history, rarity adaptation, or influence.

## First encounter

The opening report presents an unfamiliar supply market whose political cost is clear and whose contents remain uncertain. Its art should fit the mod's period presentation while making the chest recognizable as the object used in the later opening window. The report establishes permanent access and points naturally toward the decisions interface.

The report does not give a free demonstration box. This keeps the first opening inside the same 50 PP transaction that will govern every later purchase. Acknowledging the report grants or confirms access only once. There is no separate irreversible choice about accepting a curse, choosing a rarity track, or joining an organization.

Writing direction should be concise and slightly curious. The humour comes from a national government treating unexplained boxes as an ordinary procurement opportunity. The opening should not explain the concealed influence, identify a demon, diagnose dependence, or advertise a future achievement route. Final report text and the acknowledgement remark are authored during localisation production. Structural names in this package are working labels unless the brief already establishes them.

## The recurring player loop

The category remains easy to understand after the initial report. In its normal state it offers one purchase action with the standard Political Power icon and the exact 50 PP cost. An unresolved paid box replaces that action with a free resumption action. The player should never need to navigate an inventory, choose a box size, select a currency conversion, or find a separate redemption menu.

Purchasing creates a durable country-owned record before the opening window is shown. That record seals the rarity, shell family, reward contents, quantities, delivery policies, and relevant reward evolution state. It also records that the exact 50 PP was paid. These facts are not recreated by opening the GUI.

Arrival starts the chest animation. Each accepted click advances one stage and produces a distinct physical reaction. The first four clicks do not grant anything. The fifth accepted click commits the completed opening through one authoritative resolver. That resolver delivers the full sealed reward, records completion, updates rarity history once, and adds hidden influence once. An omen evaluation is a separate consequence of the completed opening and is never a component in the prize manifest.

After a successful reveal, the result screen shows the exact rarity and every delivered benefit. It remains readable until the player closes it. A short flourish may finish before the result settles, but the player is not forced to wait through a long cinematic. The next purchase becomes available through the same category once this paid opening has resolved. Closing the result is navigation and cannot grant, remove, or recalculate a prize.

## Authoritative state model

The following labels describe internal states. They are not final localisation or a required set of literal script flags.

| State | Player-visible behavior | Authoritative consequence | Permitted next state |
| --- | --- | --- | --- |
| Access unavailable | Category absent | No purchase or GUI entry | Access ready after a valid initial grant |
| Access ready | One purchase action | Recheck affordability and delivery readiness at activation | Paid and sealed |
| Paid and sealed | Chest arrives or free resumption is available | One receipt proves 50 PP paid and fixes the prize | Opening stages 0 to 4 |
| Opening stages 0 to 4 | Current chest condition and physical click response | Each accepted input advances one stage, with no reward or influence charge | Next stage or hidden window |
| Window hidden with a paid box | Free resumption replaces purchase | Pending reward and click stage remain unchanged | Same opening stage when resumed |
| Fifth activation resolving | Final opening begins | One fresh completion receipt authorizes the complete grant and one influence increase | Result available |
| Result available | Rarity and full delivered contents | Durable completion proof makes repeats harmless | Result closed or later result view |
| Result closed | Category returns to purchase state | Completed proof remains, transient visual state can clear | New independent purchase |

GUI animation frames are presentation state. They do not become the payment or reward authority. A completed click stage may be saved even if its impact animation has not yet settled. Reloading that state restores a coherent settled pose for the saved stage, without inventing another accepted click or repeating the associated gameplay effects.

The final resolving transition must have an explicit duplicate-call guard. Merely finding an old record marked consumed does not authorize another grant. The current invocation must receive fresh proof that it alone accepted the unresolved purchase. Repeated input, stale callbacks, co-operative multiplayer clicks, and reload recovery all consult the same country and purchase identity.

## Payment and sealing contract

The purchase uses one authoritative fixed quote of 50 PP. The displayed amount, enabled state, click-time affordability check, debit, and receipt must agree. Exactly 50 PP is sufficient. An amount below 50 is insufficient. The opening stage has no price field that can accidentally debit the player again.

The fixed price is an explicit exception to variable pricing and sale modifiers. Premium status does not change it. Black Friday and other shared discount sources must not silently turn it into 25 PP, 12.5 PP, or another amount. This exception applies only to the Lootboxes purchase and must not alter shared discounts for other actions.

The purchase preflight validates the country, access, absence of an unresolved purchase, payment capacity, and a complete certified reward pool. It must not mutate gameplay or sample a prize merely because the player hovers a tooltip. Once activated, the action establishes one purchase identity, seals its result, records the actual payment, and opens the local presentation. Rejected preflight leaves Political Power, random history, influence, and cooldowns unchanged.

Each genuinely new paid purchase evaluates the reward-selection path once using fresh per-purchase randomness, then seals every selected value. Resumption, saving, reloading, later opening clicks, resolution retries, and result replay read that sealed receipt and never sample again. The read-only auditor verified that a repeated native decision uses `fixed_random_seed = no` in the decision body when its random selection must vary across purchases: see the offline Decision modding reference at lines 383–386 and vanilla `common/decisions/FRA.txt`, line 56, inside `FRA_communist_civil_war_decision`. Apply that setting only if the selected Lootboxes sampling path runs through a repeatable decision; consult the [auditor handoff](../../plans/108_wrestling_tournament_plans/subagent_handoffs/107_108_probability_review_2026-10-10.md) for the source revision and limits. Do not guess another token or alter rarity weights to satisfy this rule.

A normal close or Escape action is not cancellation of the purchase. It does not refund 50 PP, discard the box, or allow another draw. The free resumption action remains available whenever the country can be controlled again. There is no paid reroll, discard-and-rebuy action, or sale of unwanted contents.

Technical repair is distinct from a normal player action. A migrated record must preserve its original identity, paid amount, and prize whenever those facts can be recovered. A verified invalid legacy record that has granted nothing may be repaired or compensated exactly once through a dedicated recovery contract. A compensation cannot refund an already completed box or clear its duplicate-grant proof. Such recovery is recorded as a technical outcome and does not count as a completed opening or an achievement purchase.

## Reward integrity at the fifth activation

Sealing fixes what was bought. Delay, reloading, evolution changes, new technology, and new stockpile levels must not reroll its rarity or quietly replace its prize with a weaker outcome. Country need affects selection and scaling when the purchase is sealed. It does not reward strategic manipulation of the country just before the fifth click.

The reward provider must deliver the full sealed amount even when the player delayed the opening. Capped resources and state-bound rewards therefore need a certified delivery policy, described in Part 2. A provider may include real receiving capacity or a stable placement policy as part of the sealed package. It cannot silently lose overflow, replace promised fuel with a claim token, or tell the player that an undelivered benefit was received.

The normal fifth activation is expected to complete immediately through a fully validated provider. During a detected technical failure, the interface must preserve the original box and prevent repeated grants while recovery runs. It must not mark an incomplete bundle successful or charge influence on an opening that has not completed. This is a defect path to repair, not an intended sixth interaction or a balancing delay.

Each bundle component needs an exact delivery result. All components must be preflighted before irreversible application. Where the engine does not provide atomic multi-effect rollback, the implementation must use supported ordered delivery and durable component receipts. Recovery can then finish only missing components of the same bundle. It must never repeat already applied equipment, fuel, building, research, or modifier effects. Native evidence must establish the normal uninterrupted behavior and the supported save boundaries.

## Closing, saving, and control changes

| Situation | Required behavior |
| --- | --- |
| Close immediately after purchase | The country retains one paid stage-0 box and resumes free |
| Close after any of the first four accepted clicks | Preserve the exact completed stage and sealed reward |
| Escape during an impact animation | Preserve the accepted stage, clear only local transient input, and resume at its settled pose |
| Save while the window is open | Persist payment, sealed result, accepted stage, reward evolution snapshot, and purchase identity |
| Reload after a completed reveal | Show or close the stored result without granting again |
| Evolution unlocks while a box waits | Keep that box's reward and shell snapshot, apply the new reward rules to later purchases |
| Peaceful credit arrives while a box waits | Reduce existing influence normally, with no effect on the sealed prize |
| Human control changes to AI | The AI can resolve the same pending record through the common resolver, once |
| AI control changes to human | The human receives the current unresolved or completed state, without a second purchase |
| Cosmetic country identity changes | Preserve the owning country's continuing transaction and history |
| Civil war or country splitting | Keep one authoritative owner for each purchase, prevent inherited copies from receiving duplicate rights |
| Country is annexed or temporarily unavailable | Never transfer its paid box or private influence to the conqueror, preserve lawful restoration behavior through the supported country lifecycle |
| Two humans control one country | Serialize accepted activations against the same purchase and stage, reject stale duplicate inputs |

The detailed country lifecycle adapter must distinguish a continuing country identity from a newly created country. Broad copying of flags or variables is not proof that access or a paid prize should be duplicated. A restored country should recover its own supported saved state. Any engine limitation on restoration storage must be documented and resolved before that case is advertised as supported.

## Time and multiplayer behavior

The chest is an interaction sequence, so it must work while the player has paused the campaign. Opening cannot require an in-game day to pass between clicks, wait for a monthly pulse, or force a global unpause. Use current native references and source to select supported real-time animation and sound behavior; do not claim runtime timing has been observed when it has not.

The window and its audio belong to the player controlling the recipient country. Other players continue with their own campaign interface. An opening must not seize another player's view, pause the multiplayer session, reveal another country's prize, or play another country's reveal cue locally. Gameplay changes remain authoritative country state, with presentation layered over that state.

Keyboard activation and reduced-motion behavior should use verified native patterns. Both retain five deliberate activations and visible progress. Reduced motion reduces travel, flash, and shake while preserving distinct real stages, a readable chest condition, and the final rarity reveal. It does not become a one-click claim route.

## Public information boundary

The category and opening window display only the information needed to buy, resume, open, and understand an actual prize. There is no added public influence value, pressure value, omen timer, recovery balance, rarity-protection counter, or country-risk score.

| Surface | Information it should communicate | Information kept out |
| --- | --- | --- |
| Initial report | Permanent access and the broad procurement premise | Curse diagnosis, accumulation rules, recovery formula |
| Category | 50 PP purchase, pending status, free resumption | Influence, omen probabilities, hidden thresholds, adaptive odds |
| Unopened chest | Physical progress and recognizable shell family | Rarity, exact contents, influence, omen outcome |
| Final reveal | Rarity, exact delivered components, amounts, duration and real usage conditions | Omen as a reward component or an explanation of later harm |
| Event Details | The event premise and genuine random supplies | Hidden counters, causal instructions, numerical effect lists |
| Evolution presentation | Visible Premium, bundle, and Chaos Loot improvements | The related hidden adverse mechanisms |
| Ordinary national effects | Truthful current effects where the engine normally shows them, with restrained neutral presentation | A diagnostic Lootboxes curse title, hidden burden, or exact trigger formula |

The hidden system is a gameplay information boundary, not a claim of cryptographic secrecy from save inspection or mod files. The implementation must nevertheless audit ordinary player-facing surfaces, stat breakdowns, generated tooltips, and localisation substitutions for accidental disclosure.

## Chaos impact contract

| Lootboxes outcome | Direct global Chaos change | Reason |
| --- | --- | --- |
| Initial access | 0 | Access alone has not produced a separate geopolitical consequence |
| Payment and sealing | 0 | Political Power expenditure is not a new world Chaos event |
| Completed opening | 0 | Private influence is accounted for only inside the recipient country |
| Genuine reward | 0 from Event 107 | Existing shared systems continue to handle any later ordinary consequences |
| Evolution activation | 0 | Shared evolution state is not an additional Chaos source |
| Temporary omen | 0 from Event 107 | Country effects do not create a second accounting path for private influence |
| Qualified peaceful contribution | Existing owner's actual negative change only | Lootboxes observes that contribution and applies private recovery once |

This map prevents private influence from becoming a parallel global meter or from recursively generating its own recovery. If a later action involving awarded equipment produces a normal shared Chaos consequence, its existing owner handles that consequence. Event 107 neither suppresses that owner nor adds a duplicate change.

## What makes the loop complete

A finished Lootboxes implementation must preserve the same purchase and opening promise through an ordinary Common result, an early Legendary result, each evolution, repeated poor luck, recovery, saving, reloading, and multiplayer control changes. The interesting variation comes from useful rewards, changing reward opportunities, hidden country consequences, and genuine peaceful recovery. Additional menus or progression currencies are not needed to create that depth.

Part 2 defines the reward economy and evolution paths. Part 3 defines hidden influence and the peaceful contribution contract. Part 4 defines the full opening presentation. Part 5 defines decisions, AI, and shared integration. Part 6 supplies achievements and the acceptance scenarios that tie these surfaces together.
