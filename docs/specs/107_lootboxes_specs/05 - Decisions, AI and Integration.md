# 107 Lootboxes: decisions, AI, and integration

## A permanent category with one clear next action

The category supports the repeated purchase loop without becoming an inventory system. It has one gameplay action available at a time. A country with access and no unresolved purchase can buy a box. A country with a paid unresolved purchase can resume that box for free. Closing a resolved result returns the player to the same purchase entry point.

The category does not expose a custom meter, progress score, public currency, or influence diagnosis. It can show ordinary purchase availability and the fact that a paid box is waiting. Progress is communicated through the chest's physical state inside the window. The player does not manage the internal receipts or probability history.

All row names below are working action roles. Production localisation must be written from their intended meaning and checked against the native interface. The established category name remains Lootboxes.

## Decision map

| Working action role | Visibility | Availability | Cost | Outcome | Repetition and AI |
| --- | --- | --- | --- | --- | --- |
| Purchase one box | Country has permanent access and no unresolved paid box | Valid owner, complete certified pool, no in-flight purchase, and at least 50 PP | Exactly 50 PP, paid once | Seal one prize and shell, create a payment receipt, then open local presentation or resolve through the AI path | Human can repeat after resolution and affordability, AI uses the strategy policy below |
| Resume paid opening | Country has one valid unresolved paid box | Correct controller and valid pending purchase identity | Free | Reopen at the saved accepted stage with the same sealed result | Never samples, pays, or advances influence by itself, AI may resolve the same pending record |
| Initial report acknowledgement | Valid initial event recipient | Report belongs to the current delivery | Free | Establish access once and allow normal category navigation | AI acknowledges through the ordinary event route, duplicate delivery is harmless |

The initial report acknowledgement is an event option rather than a third decision row. Receipt scrolling and closing are navigation controls within the dedicated window. The active category therefore remains small even after all evolutions are enabled.

The purchase and resumption rows each receive a distinct 32x32 decision-family icon under the accepted asset prompt. The purchase icon emphasizes a sealed crate and procurement. The resumption icon emphasizes an already held crate and continuation without suggesting a second payment. The initial report and three evolution reports receive their own 210x176 report-card compositions. Their art communicates the public reward improvement and never diagnoses the hidden influence.

### Purchase requirements and feedback

Use the correct Political Power texticon beside the displayed 50 PP. The same inclusive check determines the displayed enabled state, the native custom-cost condition where used, and the final debit. Equality at 50 must work. Fractional PP just below 50 must not pass because one surface rounded it upward.

Check pending ownership before allowing a second transaction. A box remains pending after the player closes it, leaves the category, changes the selected map state, saves, or reloads. If a purchase is already being accepted, a second request is rejected without another random draw or debit.

Public disabled feedback should explain the actual immediate reason: insufficient Political Power, an already paid box awaiting completion, a currently resolving request, or loss of the necessary country context. Production needs distinct readable control states where the native interface supports them. It must not use a hidden influence threshold, an omen cooldown, or an addiction flag as a public purchase requirement.

The decision does not ask the player to choose a reward service, spend experience, sacrifice equipment, or negotiate with a supplier. Those additions would alter the simple 50 PP promise. Strategic variety comes from deciding when to spend scarce Political Power and how to use the reward after it arrives.

Each newly accepted paid purchase must evaluate the reward-selection path once with fresh per-purchase randomness before sealing its receipt. A resumed, reloaded, opened, retried, or replayed transaction reads the existing receipt without another sample. If sampling runs through a repeatable native decision, use the verified `fixed_random_seed = no` setting in that decision body; the [probability-review handoff](../../plans/108_wrestling_tournament_plans/subagent_handoffs/107_108_probability_review_2026-10-10.md) records offline Decision modding lines 383–386 and vanilla `common/decisions/FRA.txt`, line 56. If the sampling route differs, verify its current semantics from the installed reference before choosing syntax. Do not change the rarity weights to satisfy this RNG rule.

### Resumption and retained results

The resumption action must clearly communicate that payment has already occurred and that opening is free. It preserves the saved stage and uses the same local opening window. A country with 0 PP can resume its paid box.

After resolution, any retained result view reads the completed receipt only. The implementation must make replay safe even if a stale GUI instance, save recovery, or accessibility flow opens that view again. Reviewing the same receipt does not count as another opening or refresh a temporary reward.

## AI purchase policy

AI countries use the same access rule, 50 PP price, reward sampler, sealed recipe system, completed-opening resolver, influence accumulation, omen rules, and peaceful contribution observer. They do not receive guaranteed useful rarities, exempt Common influence, extra recovery credit, or a reduced price.

The AI does not require a human chest window. A valid AI purchase seals the same prize and resolves it through the common completion path without generating local visual or audio effects for a human. It records one completed opening, regardless of the number of components in the reward. The five-interaction rule remains the human presentation contract.

AI restraint comes from ordinary strategic budgeting and purchase cadence. An AI country should not repeatedly spend every available 50 PP while important laws, diplomatic actions, mobilization, or political recovery need that resource. It should also not know the hidden system well enough to stop exactly one opening before an omen threshold.

### Strategic reserve

Use a country-specific reserve based on verified near-term obligations and the current strategic situation. The reserve is an AI preference boundary, not an extra human price. Before buying, the AI must retain that reserve after paying the same 50 PP.

A starting design is:

`Political Power before purchase >= 50 + strategic reserve`

The reserve is the greater of an ordinary floor and the country's verified urgent PP commitments plus a buffer. An illustrative ordinary floor is 100 PP. A serious political or military emergency can raise that floor toward 200 PP. A verified imminent action with a larger exact cost can set a larger reserve, with an illustrative 25 PP buffer. These values are tuning anchors rather than fixed universal thresholds.

Do not invent a generic cost for every native action. Inspect supported strategic and purchase signals. Where an obligation's exact price cannot be read, use a conservative documented strategic class rather than pretending the quote is exact. Several obligations should be combined only when they genuinely compete in the selected planning horizon. Avoid double-counting the same obligation through two owner signals.

### Cadence and willingness

Use one bounded country-local opportunity policy. An illustrative normal interval is about 30 days between successful discretionary purchases. A severe crisis can defer reconsideration for roughly 60 days. Exact pacing depends on native AI decision semantics and should be tuned using campaign evidence.

Prefer the existing native decision AI evaluation route with a saved success cooldown or an already supported event-owned callback. Do not add a new daily, weekly, or monthly scan across all countries. A delayed opportunity must carry its original due date and country generation so reload or repeated callbacks cannot accelerate it.

At an eligible opportunity, willingness can rise with a healthy PP surplus, a useful conventional shortage, spare administrative capacity, or a sustained period without urgent commitments. It should fall during a coup threat, urgent law change, major political deficit, or competing diplomatic commitment. Wartime shortages can make a box attractive, but only after the reserve rule protects urgent spending.

The AI may react to ordinary observed stability, production, readiness, and resource conditions, as any player can. It must not read hidden burden, omen probability, symptom-relief expiry, the next sealed reward, or private recovery thresholds when deciding to purchase. Shared reward generation still reads its own poor-result history because identical reward odds require that sampler state.

Native willingness factors are scores or priorities unless an inspected engine adapter establishes a complete normalized choice model. A score of 50 is not automatically a 50% purchase chance. Exact purchase frequency requires native cadence, the complete candidate set, affordability changes, and competing decisions.

### AI scenario matrix

| Scenario | Expected behavior | Forbidden behavior |
| --- | --- | --- |
| Small peaceful country with 49 PP | No purchase, access remains | Free box or debt-funded purchase |
| Small country with 50 PP and ordinary commitments | Usually preserve strategic funds under the AI reserve policy | Automatic purchase merely because native affordability passes |
| Stable country with a large surplus | Occasional purchase at a valid opportunity | Several immediate purchases draining the entire reserve |
| Country saving for a verified expensive law | Retain the exact near-term obligation and buffer | Spend the reserved PP because a reward might compensate |
| Major at war with shortages and adequate spare PP | A box can compete as a useful discretionary action | Hidden guarantee of the exact equipment it needs |
| Country in severe political instability | Defer or sharply reduce willingness based on ordinary conditions | Read a hidden omen key as a perfect diagnosis |
| Repeated Common outcomes | Receive the same improving soft rarity distribution | Extra AI pity, a free reroll, or influence exemption |
| High influence with strong public conditions | Follow the same public strategy inputs | Stop at an exact hidden burden threshold |
| Existing paid human box transferred to AI control | Resolve that same box once | Buy again or discard the old result |
| AI makes a genuine peaceful contribution | Receive the same verified private recovery | A private AI cleanse action or full credit for every ally |
| Two AI callbacks arrive together | One purchase or one resolution accepted | Duplicate debit, reward, or history update |

## AI peaceful behavior

Lootboxes does not replace diplomatic AI with a hidden cleansing optimizer. Countries continue to pursue ordinary strategic peace, liberation, release, withdrawal, or supported restorative actions through their existing owners. When such an action meets the contribution contract, the same recovery observer applies its real credit.

An AI country can therefore improve its situation through ordinary peaceful play without receiving information unavailable to the player. It can also remain exposed if it continues buying and never makes eligible contributions. Finite symptoms and the non-recurring withdrawal episode prevent a stalled diplomatic situation from forcing the AI to keep buying simply to function.

## Shared event and evolution integration

The implementation needs one coherent identity across initial selection, the event root, recipient ownership, access state, enablement defaults, Event Log, Event Details, evolution information, and the catalog. The user selected Event 107 for Lootboxes, and the parent reports that the registry and cross-package 107-hold amendments are complete with current identifier checks passing. Use the mapping in [`shared_identifier_registry.md`](../shared_identifier_registry.md). The workbook state last reported by the parent remains row 107 Rule/Unavailable with Type, Chaos, and cluster empty, and row 112 Lootboxes/Unavailable; workbook/runtime catalog migration and status changes remain parent-owned and queued.

The initial event log records the actual recipient. A hover, failed purchase, resumed opening, or repeated result view is not another initial occurrence. Ordinary box transactions retain their country-owned receipts for gameplay and achievements without flooding the shared event history with five click records or hidden omen diagnostics.

Disabling future selection of the initial event after access has been granted does not revoke that permanent category or confiscate a paid box. Evolution and global Chaos settings retain their own supported semantics. Whatever their future-selection effect, they must preserve existing paid obligations, complete ordinary symptom expiry, and avoid erasing burden as a settings side effect.

The three evolution states must be consulted through their shared owner. Unlocking an evolution updates future purchase capabilities and the corresponding visible presentation. It does not overwrite an already paid box. An event arriving after the shared evolutions are active initializes directly into the appropriate visible reward state.

A falling Chaos value can affect current hidden risk as described in Part 3, while retained shared evolution flags follow their normal lifecycle. The interface must not claim that an evolution is active merely because the threshold is met if the shared owner has not enabled or unlocked it.

## System ownership map

| Surface | Event 107 responsibility | Shared or external responsibility |
| --- | --- | --- |
| Initial event and access | Idempotent access and correct country state | Normal selection, recipient filtering, settings, shared occurrence accounting |
| Fixed purchase | Quote, preflight, one payment, one sealed record | Native PP debit support and any neutral receipt framework |
| Rarity and recipes | Soft history model, complete tier pools, exact sealed manifest | Equipment definitions, native research and building rules, compatible owner providers |
| Opening window | Event-owned presentation contract and public state | Verified native GUI, input, animation, local audio behavior |
| Reward commit | One complete grant and durable component proof | Verified native effect semantics and supported provider results |
| Hidden influence | Country burden, finite symptoms, receipt-driven updates | Existing native modifier and timing mechanisms |
| Peace recovery | Consume qualified allocated actual contributions once | Authoritative Chaos commit, source identity, contributor provenance, source anti-farm facts |
| Evolutions | Visible reward changes and private consequence eligibility | Shared evolution enablement, pacing, and history |
| Achievements | Exact country-owned receipt facts and eligibility | Existing achievement registry, standard completion and icon conventions |
| Documentation | Accurate event-specific public premise and technical handoff | Parent-owned shared mirrors and workbook export process |

Neutral helpers may be reused only after their input, output, scope, and mutation contracts are inspected. A helper with an attractive name is not sufficient evidence of safe reuse. Event-specific generation, callbacks, and country state remain in Event 107 ownership unless a genuinely shared contract is required.

## Fixed-price integration with discounts

The universal discounted-cost framework can support receipt and refund concepts, but its ordinary quote composition must not change the user-fixed 50 PP amount. The Lootboxes owner needs an explicit fixed-price adapter classification. It must not pretend that an all-family or zero mask disables discounts if that framework interprets the mask differently.

Verify the native decision cost path under inactive discounts, active Black Friday, overlapping supported sources, source expiry, and reload. Confirm displayed price, affordability, actual debit, and actual-paid receipt are all 50. The adapter must not disable shared discounts globally or modify their behavior for another event.

Any technical compensation uses the stored actual paid amount. A normal box has no refundable cancellation path once validly purchased. Compensation and completion are mutually exclusive transaction outcomes, so a compensated invalid legacy box cannot later grant its original prize.

## Peace integration boundary

The recovery observer operates on the actual committed global Chaos reduction. It does not rescan the display history, read only the current global level, or multiply a displayed nominal negative value by a recovery rate.

Each eligible source needs exact contributor semantics. Liberation can credit a liberator, release can credit a releaser, and restoration can require an explicit contributor separate from the restored beneficiary. A multi-country settlement divides a bounded total contribution among actual participating countries. Membership in a faction or presence in a war is not enough by itself.

The observer must retain causal identity across source aggregation, duplicate callbacks, save/reload, and later durability checks. A presentation row sequence is not necessarily a source-action identity. Part 3 defines the receipt, anti-farming, floor, disabled-system, and nonwar coverage requirements.

## Scope, persistence, and scheduling

Keep persistent purchase identity, sealed reward, accepted stage, completion proof, poor-result history, influence, symptom episodes, contribution receipts, and achievement facts under their correct country owner. Local visibility and transient animation state are separate from that authority.

Nested calls must freeze the country, purchase, component, and source-action identities they depend on. The engine's current `ROOT` or a temporary event target may not mean the same actor after entering another scope. Validate exact actor and phase before payment, grant, recovery, or compensation.

Every helper output consumed by its caller must be initialized in that caller, including forwarding boundaries. Clearing one-shot inputs must not erase returned success or delivery results. A stale temporary success value cannot authorize an irreversible effect.

Use bounded pending work and preserve unvisited entries when the engine's loop limit is reached. An expired symptom should clean up its own effect and stop. A repeated callback must not reset its expiry, create another withdrawal episode, award peaceful credit twice, or revisit every country in the world.

Load recovery checks consistency without replaying purchases. It can resume an already paid opening, finish only the missing components of an interrupted supported transaction, restore current finite modifiers, and retain completed receipts as duplicate protection. It cannot treat the absence of a local window as proof that the country has no pending box.

## Country compatibility

Small countries, majors, subjects, countries at war, countries at peace, and countries with unusual existing equipment should use the same core loop. Recipe eligibility adapts to their real capacities, while the top-level rarity probabilities remain identical for equivalent form and history state.

A missing DLC feature must not empty a rarity or make a paid box unusable. Base-game-compatible recipes carry the core event. A DLC-specific or custom equipment provider is eligible only when its exact consumer and grant behavior exist. Paid boxes preserve the provider version that made their original contents valid.

Government changes and cosmetic identity changes should preserve continuing country state. Country splits require explicit ownership so duplicated inherited flags cannot create free access to the same paid reward. Annexation, restoration, observer mode, and human/AI handover need the lifecycle cases in Part 6.

## Localisation and documentation surfaces

Public text should make the ordinary action easy to understand without explaining the hidden system. Category text explains the purchase and paid resumption. Result text gives exact delivered benefits. Evolution descriptions focus on upgraded shells, larger bundles, and useful unusual supplies. Event Details remains a concise premise description.

The opening report's light parchment uses plain readable text. Final English localisation follows current project encoding and syntax requirements. Other supported languages must not leak raw keys, internal recipe names, private state tokens, or debug explanations when a translation is absent.

The catalog workbook is the editable authority. CSV files are generated exports. After a supported workbook update, run the canonical export process and verify the exact mirrored public detail fields. A planning package does not make an event Playable, resolve a live identity collision, or prove that native behavior is implemented.

## Integration acceptance

The core, GUI, AI, rewards, and recovery must be reviewed as one loop. A visually complete chest is insufficient if it can regrant a prize. A correct transaction is insufficient if the player must wait for campaign time between clicks. Correct rarity arithmetic is insufficient if a country can roll an unusable top-tier reward. A good recovery formula is insufficient if it credits nominal History values or cannot attribute a real peaceful action.

The implementation handoff therefore requires a route coverage table matching every action, reward family, evolution entry path, AI case, country lifecycle case, and native presentation state to its actual source and evidence. Any missing, merged, renamed, simplified, substituted, or blocked route must be reported explicitly before completion is claimed.
