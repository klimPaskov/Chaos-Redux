# 11. Consequences that the campaign records

## Chaos impact map

The Directorate contributes Chaos through material events, not through timer ticks or abstract stage labels. Record each premium through the shared Chaos history owner with the actual actor, target and cause. Existing generic gains for wars, annexation, capital capture, deaths, contamination, nuclear use and military buildup continue to operate once.

The following premiums represent additional abnormal significance. They are not second copies of those generic facts.

| Outcome | Proposed event-owned change | Dynamic factors | Receipt and overlap rule |
| --- | --- | --- | --- |
| Natural Directorate arrival | +20 to +35 | Opening force relative to world strength, industrial maturity and actual fielded diversity | One per committed episode. Represents the appearance of the final-boss institution, separate from its ordinary wars |
| The Final Boss setup | +20, +30, +40 or +50 by intensity | Actual committed opening may tune within the selected band | Replaces the natural arrival premium, never stacks with it |
| First durable expansion beyond the initial state | +5 | Real additional governed capacity and connected military reach | One per episode after actual control and useful capacity are established, no recapture repeats |
| First decisive absorption of a major's industrial or research base | +10 to +15 | Share of that major's usable productive system actually secured | One per distinct pre-arrival major identity, with at most the first three such premiums. Generic capitulation and annexation remain separate |
| Live control first crosses 25, 50 and 75 percent of the origin set | +5, +10 and +15 | Increase only for a genuinely larger geographic footprint, no extra scaling by current Chaos | Each band once per episode. No repeat on losing and regaining a threshold |
| First complete origin-continent control | +20 to +35 | Origin continent's share of surviving world industry and population | Once on real completion. The ending still needs its independent live gates |
| First sustained external-continent beachhead | +10 to +20 | Real force supplied and territorial depth outside the origin continent | Once per newly reached continent. A raid or transient province touch does not qualify |
| First operational demonstration of a newly absorbed major capability class | +5 to +10 | Strategic effect beyond simple possession, such as a new delivery network affecting a real battle | Once per neutral capability class, with an episode premium budget of +30. Do not count ordinary casualties or contamination again |
| Chaos Always Wins flag alone | 0 | None | The flag and cinematic are not a new physical source. Its global wars and later material outcomes use their own shared or mapped paths |
| Focus, technology, registration or baseline stage alone | 0 | None | Unlocking future action does not count as having used it |
| First durable restoration of a captured major base | -5 to -10 | Actual operational capacity removed from the Directorate and restored to resistance | Once per matching positive major-base receipt. Retaking an empty capital icon is insufficient |
| Break of first continental completion | -10 | A real required territory is retaken and held through its recovery review | Once per episode, distinct from repeatable generic war outcomes |
| Directorate destroyed before its ending | -25 to -50 | Its peak demonstrated territorial and operational scale | One per confirmed destroyed episode, no full refund of accumulated historical Chaos |
| Directorate destroyed after its ending | -10 to -25 | Removal of surviving military threat | One per confirmed defeat. Does not clear the world-end latch or restart ordinary events |

### Durable outcomes

Use a normal 30-day review anchor for establishing a new governed foothold or sustained beachhead. Longer review applies when a territory remains disputed or unsupplied. A rapid collapse cancels the pending milestone without a reward. The date belongs to the state or recorded theater, so controller cycling cannot compress the review.

Continental live-control bands and full completion are recorded on actual control, because they describe immediate strategic geography. Their reversal reduction requires a durable resistance hold to prevent repeated single-day trading. Both gain and reversal receipts are one-shot. The territorial terminal check itself has no artificial 30-day waiting period.

The total event-owned premium from military-capability demonstrations is bounded because a future mod update may add hundreds of weapons. Universal access must not imply hundreds of duplicate Chaos rewards. New units join the arsenal dynamically while existing broad capability classes provide stable achievement and Chaos accounting. A genuinely new class can extend that shared taxonomy in its owner change.

### Shared consequences remain intact

Civilian deaths use measured physical population loss and a single Deaths registration. Contamination uses the existing atmosphere or local contamination system. Native raids and attacks report their real results. Nuclear or biological outcomes can contribute to another world-end branch through that branch's own rules. Event 103 must not hide those consequences to ensure its preferred ending wins.

Defeat removes current Directorate instability. It does not refund dead populations, reconstruct destroyed infrastructure, clean the atmosphere, recall displaced civilians or erase another country's political fragmentation. Negative Chaos gains therefore remove only a bounded part of the specific threat.

The initial scenario addition is not a minimum meter setting. If the Chaos Meter is disabled, preserve the existing shared policy and the episode's recorded cause without secretly bypassing the setting. A later setting change follows the shared system's own historical treatment, not a private Event 103 backfill.

## World Threat contribution

Register one Directorate source with the existing aggregate. Its contribution grows with actual military strength, direct territorial and industrial share, number of active hostile theaters, viable intercontinental reach and terminal state. Its presence is significant immediately, then increases through real expansion.

The aggregate consumes cached owner data updated by arrival, control changes, committed operations, losses and bounded owner reviews. It does not scan every country's complete military every day. Remove the active contribution only after confirmed destruction, while retaining historical peak and defeat receipts for achievements.

World Threat does not replace Chaos, continental control or sustainment. It informs shared resistance behavior and existing UI. Adding the boss to that aggregate must not trigger the unrelated actual-nonhuman or special-country cleanup classifiers.

## Achievement architecture and common tracking rules

### Scope and qualification

The following eight achievements are required design concepts. Their working keys are unreserved. Implementation must check collisions and register final IDs in the single `common/achievements/chaos_redux_achievements.txt` registry under Event 103. They need final localisation, all three icon states, tracking, actor attribution, tests, and documentation. Completing this specification does not mean any achievement is implemented.

Five concepts serve resistance countries and three serve optional human control of the Directorate. No concept awards for arrival, a setup click, a focus click alone, technology unlocks alone, or a few days of passive survival.

Use the established general achievement-validity rules after inspecting their current implementation. The additional Event 103 challenge policy proposed here is explicit design intent, not a claimed existing engine rule:

- A resistance actor is a qualifying human-controlled non-Directorate country enrolled at the committed arrival, with its starting identity, sovereignty, owned core states, and capital state frozen for this episode. A later country switch cannot inherit the original actor's receipts.
- A boss actor must explicitly obtain ordinary supported control of the Directorate before any scored post-arrival conquest or operation receipt. Verify the actual engine and mod country-selection route first. Do not use CXT console setup, an achievement-only takeover decision, a debug country switch, or an automatic switch by The Final Boss. If ordinary control is unsupported, the three boss concepts remain fully specified but unavailable for release until that control route is verified.
- Resistance achievements qualify after natural automatic arrival or a manual The Final Boss launch at High or Maximum intensity. Freeze launch provenance, chosen intensity and the initial scaling snapshot at committed arrival. Lower-intensity manual launches do not qualify resistance achievements.
- Boss-player achievements may qualify at any intensity through verified ordinary supported control, subject to their own conditions and the common validity rules. Lower intensity makes their conquest harder and does not disqualify them. This exception does not grant control, add a country-selection interface, or change any terminal gate.
- Debug grants, fake attack records, forced completion receipts, test-country setup, artificial project success, and episode refreshes never count. No score is imported from the dormant carrier. Event-owned debug use that materially assists the actor or boss invalidates the affected challenge. Do not claim detection of arbitrary console commands beyond verified mod and engine eligibility mechanisms.
- Pre-terminal containment challenges require global world ends and this branch enabled throughout their scored interval. Another world-end before their completion disqualifies those specific pre-terminal routes. The terminal-reversal concept instead requires the actual irreversible Event 103 ending receipt.
- Country-level eligibility and receipts must remain distinct in multiplayer. One participant's capture or global victory does not award everyone the actor-specific achievement. Verify native player/control identity behavior, hotjoin, and tag changes before claiming multiplayer attribution support. Do not silently invent account-level persistence.

These rules are achievement qualifications. They do not alter normal event gates, global Chaos behavior, arsenal availability, baseline combat strength, peace policy, or the requester's scenario control.

The user-approved manual relaunch in Part 09 creates a new challenge episode after confirmed destruction and cleanup. Freeze new actor enrollment, provenance, intensity, geography, dates and thresholds for that episode without resetting completed achievements or finalized earlier history. Never combine state recoveries, family-use receipts, operation results, continuous holds or victory milestones across attempts. A valid fresh launch may qualify under the same natural/manual intensity rules, while a duplicate request or refill of an active episode remains excluded.

Pending post-defeat checks, including R2 and R5, retain their original frozen episode, actor identity, destruction receipt, state set and due date. They may evaluate only their own accepted outcome and the required surviving resistance actor. They cannot read a replacement CXT as their destroyed boss or consume the new episode's captures, shipments, defeat or terminal receipts. Tag equality alone does not establish incarnation identity. Actor-mutating old work must be retired before carrier reuse, while independent frozen historical score checks remain separately bound.

### Evidence vocabulary

Implementation must expose semantic hooks rather than guessed engine syntax:

| Receipt or snapshot | Required meaning | Exclusions |
| --- | --- | --- |
| Committed arrival | One active immutable episode, provenance, intensity, origin state and continent, initial world/force snapshot, eligible actors | Provisional setup, rollback, duplicate launch or refill of the same active episode, dormant CXT history. A valid new post-defeat manual episode has its own identity |
| Qualifying hostile control acquisition | This actor gained control of this state from the Directorate in a real hostile campaign, with previous controller, date, episode and provenance retained | Diplomatic gifts, scripted giveaways, debug transfer, claimant-only ownership, allied capture credited to the wrong country |
| Qualifying loss | The Directorate actually took an actor's state under the same provenance standard | Voluntary transfers or a prearranged test fixture |
| Live hold | The same actor continuously controls the named state set across a persisted due date | Callback count, historical peak, recapture resets disguised as continuous control |
| Actual family use | Owner-certified role-appropriate field use by this Directorate actor of one dynamically registered deployable family | Mere unlock, availability, stockpile grant, template creation, a fake combat record, or test-unit spawn |
| Actual special-operation success | Exact owner-authorized successful gameplay callback and any required delivered-result proof | AI intent, target selection, queued project, canceled mission, failed action, debug success |
| Terminal commit | The actual Chaos Always Wins transaction succeeded under all normal gates | Historical continent completion, disabled settings, low Chaos, or presentation-only visibility |
| Confirmed destruction | No controlled territory and actual country destruction under verified engine semantics | Capitulation alone, a stale country reference, missing GUI rows, or provisional rollback |
| Actual world conquest | The complete world-control and no-remaining-sovereign predicate specified in Part 09 | All wars declared, all opponents capitulated, a puppet shortcut, or an asserted news description |

These are required integrations and tests. They are not assertions that existing callbacks already provide every distinction. If native evidence cannot distinguish a required real outcome from a scripted transfer, add a bounded owner-side receipt at the responsible action or mark that achievement's proof route blocked. Do not silently weaken the condition.

State and action receipts are idempotent per episode, actor, source owner, target, and semantic outcome. Unique sets count a state or family once. An annexation receipt records real acquired resources once and must not be repurposed as fabricated combat contribution. Save/load and late duplicate delivery preserve the same due date and consumed receipt. Delayed checks after boss cleanup use one bounded actor-owned callback with a persistent due date and a pending receipt consumed before verification, not a periodic world scan.

### Achievement concepts

#### R1. Rapid restoration from the opening loss

**Working key:** `proposal_103_r1_opening_restoration`. **Audience:** the enrolled former controller of the arrival state, provided it remains a valid sovereign actor with another state after the initial seizure. **Visibility:** visible in achievement UI after arrival. **Difficulty:** extreme.

**Win conditions:** personally recover the arrival state through a qualifying hostile-control receipt within 60 calendar days of arrival, keep it continuously for 30 calendar days, and achieve confirmed Directorate destruction within 180 calendar days of arrival, before Chaos Always Wins or another world-end begins. The actor must not capitulate during this scored interval.

**Disqualifiers:** common invalidation, a scripted or allied transfer substituted for the personal recovery, loss of the recovered arrival state during the hold, missed deadline, actor capitulation, or a terminal receipt before destruction. A lost hold restarts from a genuine recapture if the overall 180-day deadline still permits it.

**Tracking:** frozen former-controller identity and arrival date, first qualifying recovery date, one hold due date, actor capitulation latch, and final destruction date. Consume the completion receipt once.

**Icon direction:** an original compact defensive emblem breaking through the Directorate's damaged industrial seal, with one recovered standard. **Writing direction:** difficult immediate counteroffensive and recovery of the place where the crisis began. Do not present it as clicking the first obvious response. **Related systems:** counterattack, front defence and the real destruction transaction.

#### R2. National recovery after deep occupation

**Working key:** `proposal_103_r2_national_recovery`. **Audience:** an enrolled sovereign resistance country with at least six initially owned core states. **Visibility:** hidden until its qualifying occupation crisis occurs. **Difficulty:** extreme.

**Crisis qualification:** the Directorate must simultaneously control the actor's arrival-era capital state and at least half of its initially owned core states, rounded up, through qualifying losses. Freeze the exact crisis-state set at that first qualifying moment.

**Win conditions:** the actor personally recovers its arrival-era capital, regains control of every state in that frozen crisis set, then holds the entire set continuously for 90 calendar days and survives to confirmed Directorate destruction before any world-end begins. At least half of the crisis set, rounded up and including the capital, must have personal qualifying hostile recovery receipts. The actor must still exist under its enrolled identity at completion.

**Disqualifiers:** voluntary staged occupation, identity replacement, gifts counted as personal recovery, actor destruction, or a world-end before completion. Losing a required state resets the hold clock. It does not create another crisis receipt or lower the frozen target.

**Tracking:** initial core-state set, initial capital state, unique loss receipts, frozen crisis set, personal recovery subset, and a persisted 90-day hold due date. If the boss dies during the hold, retain a one-time actor-owned delayed check after event cleanup.

**Icon direction:** a ruined civic structure being reclaimed beneath a torn institutional standard, with a readable repaired center. **Writing direction:** recovery of a country that was close to being consumed. **Related systems:** counterattack, reconstruction, evacuation consequences, and persistent post-defeat receipts.

#### R3. Final continental holdout

**Working key:** `proposal_103_r3_continental_holdout`. **Audience:** an enrolled resistance country controlling at least one of its initially owned core states on the origin continent. **Visibility:** hidden until the Directorate first reaches at least 90 percent live control of that continent. **Difficulty:** exceptional.

**Win conditions:** while at war with the Directorate, preserve continuous control of a named enrolled core-state anchor on that continent for 90 calendar days after the first 90-percent crisis qualification. Chaos must remain strictly above 1000 and both ending settings must remain enabled throughout that 90-day hold. Afterwards, personally recover the arrival state and achieve confirmed Directorate destruction before any world-end begins.

Freeze the anchor and due date at the first actor-specific qualifying crisis check. At that instant the actor must be at war, the boss must directly control at least 90 percent of the required continent, Chaos must be above 1000, both ending settings must be enabled, and the actor must directly control at least one of its initially owned core states on that continent. Select the frozen arrival-era capital if it is still eligible. Otherwise select the eligible state with the smallest stable native state ID. Record and disclose that deterministic result immediately. Delayed UI opening, later state choice, changed control, save/load or a more convenient island cannot restart the clock or replace the anchor.

The 90-percent qualification is a one-time historical crisis entry condition. Directorate control may fall during a successful resistance campaign without resetting the hold. A currently defended island counts if it belongs to the exact origin-continent set. The boss's baseline ability to pursue such disconnected territory remains mandatory.

**Disqualifiers:** loss of the named anchor during the hold, Chaos falling to or below 1000 during the hold, ending settings disabled, a world-end, actor destruction, or an artificial state transfer. After a lost anchor the original attempt fails. It is not replaced with a more convenient state.

**Tracking:** unique crisis date, selected eligible anchor, persistent 90-day due date, continuous control and Chaos/setting invalidation latches, personal arrival-state recovery, and destruction receipt.

**Icon direction:** a small fortified remnant with a surviving light set against the encircling Directorate emblem, without an invented geographic border. **Writing direction:** sustained resistance after almost an entire continent has fallen. **Related systems:** defence objectives, sea corridors where appropriate, exact-state navigation, and counterattack.

#### R4. Intervention from outside the origin continent

**Working key:** `proposal_103_r4_external_intervention`. **Audience:** an enrolled sovereign whose initial capital and all initially owned states lie outside the origin continent. **Visibility:** visible after arrival for an eligible country. **Difficulty:** extreme.

**Win conditions:** personally recover at least `max(5, ceiling(origin_required_state_count / 4))` distinct states on the origin continent from the Directorate, including the arrival state, hold those qualifying recovered states for at least seven calendar days each, and survive to confirmed Directorate destruction before any world-end. The actor remains sovereign and is never a Directorate subject or faction partner.

This is outside intervention. It does not claim that a naval landing occurred when the actual route crossed an intercontinental land border. Existing naval, airborne, transport, supply, and diplomatic-access systems determine the real expedition.

**Disqualifiers:** fewer than five required states in an unusual map's origin set, common invalidation, subject or faction shortcut, allied restoration counted as the actor's personal capture, or terminal activation. A recapture does not count the same state twice. A lost seven-day hold can restart on a later qualifying recovery.

**Tracking:** arrival geography and sovereign status, frozen denominator, distinct actor-state recovery set, per-state due dates for the bounded scored set, and destruction receipt.

**Icon direction:** an expeditionary supply vessel or transport column carrying a resistance standard into an occupied shore or frontier. **Writing direction:** costly intervention in a crisis that began elsewhere. **Related systems:** sea corridors, material aid, reconnaissance, overseas logistics and counterattack.

#### R5. Military reversal after the terminal event

**Working key:** `proposal_103_r5_terminal_reversal`. **Audience:** an enrolled resistance actor still existing when Chaos Always Wins commits. **Visibility:** hidden until the actual terminal receipt. **Difficulty:** exceptional.

**Win conditions:** Chaos Always Wins must have genuinely begun, the Directorate must then have controlled qualifying territory on at least two continents, and the actor must personally recover at least five distinct states across at least two of those continents, including the arrival state. The actor must achieve confirmed Directorate destruction before actual Directorate world conquest and remain sovereign with its arrival-era capital under its control for 60 calendar days after destruction.

**Disqualifiers:** presentation without a terminal transaction, fabricated foreign bridgeheads, gifts counted as personal recoveries, actor destruction or identity replacement, boss world conquest first, or common debug invalidation. Ordinary loss of the capital during the final 60-day interval resets that hold if the actor survives. The ending history is never cleared as a reward.

**Tracking:** immutable terminal receipt, real cross-continent boss-control history, actor's distinct personal recovery set, destruction receipt, and one actor-owned post-defeat due date that survives boss cleanup. Final verification checks current sovereignty and the frozen capital state.

**Icon direction:** a broken Directorate standard falling across a battered but still illuminated resistance emblem. **Writing direction:** defeating the army after an irreversible global threshold without pretending that the world returned to its former state. **Related systems:** terminal wars, continuing event maintenance, counterattack and post-terminal destruction.

#### B1. Rapid complete continental campaign

**Working key:** `proposal_103_b1_continental_campaign`. **Audience:** valid explicitly enrolled Directorate player only. **Visibility:** visible only in that eligible country context. **Difficulty:** very hard to extreme, requiring tuning across origin continents.

**Win conditions:** achieve the real Chaos Always Wins terminal receipt no later than the geography-scaled deadline frozen at the committed arrival, with every required origin-continent state under live control, without ever losing control of the arrival state or capitulating. Every disconnected required state is included. Low-Chaos manual arrival must raise Chaos through real allowed play and satisfy the normal ending gates within the same deadline.

**Accepted deadline:** `deadline_days = 5 * ceil(min(300, max(150, 120 + 5 * sqrt(S) + 10 * L)) / 5)`. Here `S` is the number of required origin-continent states, including disconnected states, and `L` is the number of disconnected ownable landmasses in that required geography, excluding the mainland. Count each disconnected landmass once. Freeze the geography inputs, calculated calendar-day allowance and absolute due date at committed arrival. Changes in control, intensity or player enrollment and save/load never recalculate or restart this allowance. The result is clamped to 150 through 300 days and rounded upward to the next multiple of five.

**Disqualifiers:** late enrollment after scored AI progress, unsupported or debug control transfer, missing geography, missed deadline, another world-end, loss of the arrival state, capitulation, or common invalidation. Any intensity may qualify through valid ordinary player control. Intensity never waives geography, continuity or terminal conditions.

**Tracking:** arrival and enrollment receipts, immutable arrival state, frozen required-geography snapshot and its `S` and `L` counts, computed deadline and absolute due date, loss/capitulation latches, normal terminal commit, and elapsed calendar time. Do not unlock from the focus tree's display state or an assertion that a continent was once complete.

**Icon direction:** the Directorate institutional standard carried past a broken coastal defence into a functioning embarkation route. **Writing direction:** an uninterrupted, fast complete continental campaign, including difficult access. **Related systems:** continental campaign, logistics and ocean reach, and normal terminal gates. The accepted geography-scaled target requires matched-continent balance validation without changing a live episode's frozen deadline.

#### B2. Real employment of the dynamic arsenal

**Working key:** `proposal_103_b2_dynamic_arsenal_use`. **Audience:** valid explicitly enrolled Directorate player only. **Visibility:** visible in eligible boss context, with progress kept in achievement UI. **Difficulty:** exceptional breadth and execution.

**Win conditions:** obtain a qualifying actual-use receipt for every currently registered deployable unit family, under its owner-declared role, and obtain successful real-operation receipts from at least three distinct eligible operational-system owners, including a real biological-warfare operation. Also control the complete origin continent and hold at least one real off-continent state for 30 consecutive calendar days. Missing biological integration or proof blocks this condition rather than removing it.

The family set is generated from package-owned registry dispositions. It is not a list of named zombies, robots, or other current examples. Combat families require real hostile combat use. Support, transport, or other noncombat families require the owner's verified substantive role-use receipt. Pure registry carriers and nondeployable utility entries are excluded only by explicit owner type evidence. Geography-limited families remain pending until their legitimate production and deployment context exists.

Registry additions before unlock join the required set, retaining previous receipts under stable owner IDs. Renames use an explicit owner migration map. Deleted or superseded entries need a documented disposition rather than disappearing through an unreviewed filter. An available but uninstrumented family is a proof blocker, not silently omitted. The achievement interface may expose qualitative progress in achievement UI but must not add an arsenal meter to the Directorate objective display.

**Disqualifiers:** unlocks, grants, fake combat history, canceled projects, debug operation success, unsupported family-use inference, missing current family disposition, a lost off-continent hold, or common invalidation. A lost hold restarts from the next genuine controlled bridgehead. An operation repeated many times does not satisfy three different owners.

**Tracking:** registry revision, current required family set, stable owner receipt set, three distinct successful operational owners, the required biological-operation receipt, and one off-continent hold due date. The owner adapter must attest actual gameplay outcomes without firing the original event country's evolution, ending, or exclusive-character path.

**Icon direction:** a compact original assembly of clearly different military materials bound by the Directorate emblem, with a readable three-part silhouette. **Writing direction:** mastery of the entire living arsenal through actual employment. **Related systems:** universal non-debug consumption, owner operational adapters, native production, ocean reach and receipt-backed use.

#### B3. Complete conquest with a functioning war machine

**Working key:** `proposal_103_b3_world_conquest`. **Audience:** valid explicitly enrolled Directorate player only. **Visibility:** hidden until Chaos Always Wins commits. **Difficulty:** exceptional completion.

**Win conditions:** after the real terminal receipt, satisfy the Part 09 world-conquest predicate with no remaining sovereign outside Directorate control, never capitulate, never lose the arrival state, and retain at least 75 percent current operational capacity relative to the Part 03 planned force requirement at the victory check. Every current arsenal registry entry must have a valid owner-authorized disposition and no unresolved missing required consumer.

**Disqualifiers:** wars declared without conquest, capitulations without actual control, a subject shortcut that fails the Part 09 sovereignty predicate, debug annexation or refill, loss of the initial state, capitulation, unresolved universal-access integration, or common invalidation. Ordinary conquest and legitimate owner-authorized absorption remain valid. Do not forbid the event's intended one-time absorption to manufacture difficulty.

**Tracking:** enrollment, initial-state continuity, capitulation latch, irreversible terminal receipt, actual global completion receipt, one atomic operational-capacity snapshot, and registry convergence status. If capacity is below the threshold when all territory is controlled, the actor may rebuild through legitimate native production while the same real world-conquest state remains true. No special debug refresh is granted.

Freeze the victory-check force requirement immediately before the last sovereign's final defeat. It must include the real planned force and essential equipment from that final theater and cannot shrink merely because no war remains. Retain at least 75 percent of the committed serviceable force equivalents used for that snapshot as well as the 75 percent sustainment threshold. Disbanding the army, emptying the plan or changing a priority cannot manufacture a perfect capacity score. Legitimate losses can be repaired through production before the achievement completes.

**Icon direction:** the Directorate seal enclosing a dense but readable industrial and military composition, with the outer edge complete and the central mechanism visibly intact. **Writing direction:** actual world conquest without destroying the force that must hold it. **Related systems:** global conquest, final sweep, native production and operational-capacity accounting.

### Required achievement verification

Check every concept against both qualifying and near-miss scenarios. Shared cases include provisional rollback, repeated manual launch, low manual intensity, dormant CXT data, duplicate receipts, allied capture, diplomatic transfer, recapture farming, save/load across due dates, a changed actor, a canceled operation, missing owner proof, a newly registered family, disabled ending settings, Chaos at exactly 1000, capitulation with surviving controlled territory, another ending, and post-terminal boss destruction.

Qualification checks must distinguish resistance eligibility after natural arrival or High or Maximum manual launch from boss-player eligibility at any intensity under valid ordinary control. Specific tests must exercise B1's 150-day and 300-day clamps, upward rounding to five days, disconnected-landmass counting with the mainland excluded, frozen arrival inputs and exact due-date boundary, each other deadline's exact boundary, each rounded state threshold, continuous holds with loss and recovery, all required disconnected origin states, terminal state that later loses territory, and delayed callbacks after event workspace and boss-maintenance cleanup. Preserve achievement-relevant durable receipts in their owner scopes. No test fixture or forced grant may become a release qualification path.

Achievement conditions and progress belong in the achievement interface and technical documentation. Ordinary focus, decision, report and news descriptions must not advertise that they open or complete these routes.

