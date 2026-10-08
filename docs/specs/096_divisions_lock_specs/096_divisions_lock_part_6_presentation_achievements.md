# Event 096: presentation, narrative, assets, and achievements

Proposed design: [README](README.md#authority-and-current-workflow) records current authority, owner workflows and historical receipt limits.

## 1. The information hierarchy

Use the normal decision category as the main control surface. The event needs a small current-state summary and two explicit actions, so a dedicated mechanic window would add complexity without improving the decision.

| Public slot | Value | Where it appears |
| --- | --- | --- |
| 1 | Current weighted fielded force | Country report, category, relevant tooltip |
| 2 | Current live allowance | The same surfaces, using the exact decision precision |
| 3 | One contextual time value | Minimum-week time while held before the floor, next-review time during a watch, or a qualitative condition after the floor |
| 4 | Authorized up-to formation count | Action and confirmation context only |

The time slot changes meaning with the state and must be labelled accordingly. It never presents a fixed release date while force is above allowance. During a held state after the floor, there is no numeric release countdown. During a watch, the countdown describes the next inspection, not guaranteed relock or guaranteed freedom afterward.

Use textual severity and cause direction derived from F and A. The player can be told that growth in population or industry improved the allowance, or that lost territory reduced it. Do not add simultaneous public counters for population, factories, territorial access, excess percentage, review credits, pressure, projected recovery, or cooldown debt. The design and debugging documents may expose the full internal breakdown.

Numeric values in reports and tooltips must use the same quarter-point representation as the actual predicate. Show current values when a surface is refreshed and identify historical snapshots as historical when necessary. Do not keep a stale opening number beside a current action eligibility state without a clear distinction.

## 2. Notification coverage

| Surface | Trigger and purpose | Writing direction |
| --- | --- | --- |
| Opening country report | Human-controlled affected country receives the initial or renewed hold | State the establishment lock, current force versus allowance, and minimum week. Explain optional reduction and national growth |
| Current category state | While held or in an evolved watch | Make the present decision legible with the smallest useful explanation |
| Confirmation | Human requests one or a batch | Make randomness, the up-to bound, current authority, possible military consequence, actual refund treatment, and possible removal of the final owned fielded formation explicit |
| First local release | This event's hold ends | Explain that the country met its own allowance. Distinguish other owners and any remaining evolved watch |
| Renewed restriction report | A failed evolved review actually reacquires the hold | Explain which kind of reassessment failed and that a fresh minimum week applies |
| Routine passed review | A review credit is consumed without a hold | Update state through existing category or log feedback without a repeated full popup |
| Final local finish | Hold ended and review budget is exhausted | Communicate that this firing's local inspection work has ended |
| Event Details | Catalog or framework detail surface | Describe the premise and strategic identity. Keep the full formula and transaction manual in the specs and gameplay tooltips |
| Global event log | Canonical firing and real registered evolutions | Record the actual global occurrence once, preserving existing framework order |

Coalesce same-day overlapping notices for the same country while retaining the actual latest state. Do not suppress the initial explanation of a new rule or make the player acknowledge a popup before compliance can release the hold. AI countries do not need player-facing report chains to perform their calculations.

An unavailable action explains the actual failed condition, such as a pending request, no compatible eligible formations, no current excess, or an invalidated inspection context. Do not conceal why a growth-only route currently remains.

## 3. Narrative identity and historical anchor

The tone is administrative intrusion into military planning. Staff officers can still command the formations already in the field, while inspectors treat their establishment documents as frozen records. The pressure comes from having an army the current country cannot justify under the inspection rules.

A useful historical design anchor is the June 18, 1932 diplomatic draft held by the United States Office of the Historian. Its land-armament proposal considered a population-related component, relative national military burdens, and differences between troop types. This supports the idea of differentiated national capacity and weighted formations as creative inspiration. It does not establish the game's formula or suggest that a global template lock was a historical institution. See R07 for the primary document.

Do not copy the draft's population ratio or disarmament percentage into game balance. Avoid presenting a real treaty, nation, leader, or international organization as the literal source of this fictional universal effect unless a later researched narrative decision expressly chooses that framing. No historical quotation or final event prose is supplied here.

The four evolutions progressively harden inspection standards, add provisional release, introduce repeated checking, and make the regime relentless. Keep that recognizable progression instead of replacing the event with unrelated mutiny, forced peace, economic sanctions, or supernatural unit destruction.

## 4. Visual manifest

These are design directions and intended consumers. No art was generated or visually approved in this task. Native image and sprite dimensions must be checked at the installed consumer before production.

| Asset ID | Consumer and target | Original visual direction |
| --- | --- | --- |
| `096_report_lock` | Country report, 210 by 176 runtime card | Period military office with formation files held under a physical seal or locking bar, readable silhouettes and restrained staff activity |
| `096_report_release` | Country release report, 210 by 176 runtime card | A corresponding office scene with approved establishment files reopened, composition distinct enough to read as release without text baked into the image |
| `096_category_inspection` | Ordinary category icon, 32 by 32 | A formation record and inspection seal, strong small silhouette |
| `096_action_single` | One-formation decision icon, 32 by 32 | One military formation record being administratively retired |
| `096_action_batch` | Severe-excess decision icon, 32 by 32 | Several formation records retired together, visually distinct from the single action |
| `chaosx_096_grow_into_army` | Achievement, three 64 by 64 states | Factory structure supporting a formation standard, industrial capacity is the readable idea |
| `chaosx_096_orderly_stand_down` | Achievement, three 64 by 64 states | An ordered stack of retired formation records beside a still-standing military standard |
| `chaosx_096_inspection_proof` | Achievement, three 64 by 64 states | Repeated inspection marks around a growing but orderly establishment record |

Report production generates the underlying period image first, then applies the project card treatment locally. Use the required black-and-white image with restrained sepia treatment, tilted card geometry, shadow, and transparent corners. Do not ask a generator to render final UI borders, exact lettering, or the complete card layout.

Icons are separate original subjects for their actual family. A decision icon is not a resized focus icon. Respect the canonical small-icon references and verify native-size readability after processing. The category uses its ordinary icon and text layout. Final production can add a category picture only if it passes the skill's picture eligibility gate and improves this specific compact surface, with parent review and corresponding manifest changes.

Achievements each begin with one original transparent color subject. Produce its grey version deterministically and apply the supplied unchanged red-cross overlay for the not-eligible subject. Use the supplied completed and grey background templates through the canonical processor. The resulting nine runtime DDS files all live directly under `gfx/achievements/`, with exact achievement IDs and `_grey` and `_not_eligible` suffixes.

The separate asset prompt contains the required source, reference, processing, sprite, licensing, and validation evidence. Do not treat these descriptions as already produced assets.

## 5. Achievement contracts

The IDs below are proposed stable identifiers, subject to a collision check before implementation. Names are working concept labels and writing directions, not final localisation. Use the shared project achievement eligibility and registry conventions. Do not add gameplay rewards merely for completing them.

Every unfinished attempt binds to one exact qualifying firing grant and valid actor episode. A genuine repeat retires the old unfinished attempt as nonqualifying, then may begin a separate new attempt if its new entry independently qualifies. Capture fresh entry values and reset that attempt's observation days, transaction contributions, and review evidence. Duplicate delivery of the same dispatch does not retire or reset an attempt. Already awarded shared achievements remain awarded.

An active evolution within the same grant does not reset an attempt by itself. Apply each objective's own regime and disqualification rules. Inspection succession into a different actor does not transfer unfinished achievement qualification. A cosmetic change that preserves the same valid actor can preserve progress. Control changes follow the shared human-eligibility rules and never transfer destructive consent.

### A096.1: `chaosx_096_grow_into_army`

Concept direction: a country supports its existing oversized force through domestic industrial growth.

| Field | Requirement |
| --- | --- |
| Initial eligibility | A genuine firing at Evolution I or higher, entry F at least 1.5 times entry A, and a valid human-controlled country under the project's achievement rules |
| Challenge | Spend at least thirty recorded days under the hold, use no Event 096 removal action, and legitimately release with F at least its entry value |
| Industrial proof | Recalculate a counterfactual allowance using entry P and T, current C and M, and the release regime. That industrial-only allowance must support the retained entry force |
| Territorial condition | No gain of control of a new state during the qualifying episode, so the industrial route is not a disguised territorial acquisition |
| Continuity | At every completed authoritative daily observation during the qualifying episode, F remains at least its entry value |
| Disqualifiers | Manual clear, disabled-regime escape, debug firing outside accepted test eligibility, annexation, invalid successor transfer, or unproven observation continuity |
| Tracking | Entry F/A/P/T/C/M, qualifying regime, episode identity, locked-day observations, minimum observed F, controlled-state gain receipt, Event 096 removal count, counterfactual release result |
| Visibility | Show the goal when this event has occurred, with qualitative condition progress through the existing achievement system |
| Difficulty | Long planning horizon and substantial economic expansion while retaining a large army |

The observation condition is defined at the authoritative daily snapshots. Do not falsely claim continuous native tracking of every intra-day structural change. Event-owned removals are additionally recorded at the exact transaction. If an engine setup cannot maintain the declared observations, keep the achievement ineligible rather than filling gaps with assumed success.

### A096.2: `chaosx_096_orderly_stand_down`

Concept direction: substantial voluntary demobilization that leaves a useful force inside a live national budget.

| Field | Requirement |
| --- | --- |
| Initial eligibility | Genuine firing with entry F at least twice entry A |
| Challenge | Complete at least one severe-excess batch and legitimately release with current F between 0.75A and A inclusive |
| Meaningful contribution | The verified structural reduction caused by Event 096 transactions totals at least half of the initial force excess |
| Country continuity | No capitulation or loss of control of an entry-controlled state during the qualifying episode |
| Disqualifiers | Manual clear, settings escape, invalid source-owner removal, replacement or refund failure, or absence of exact transaction evidence |
| Tracking | Entry force and excess, episode identity, actual transaction F before and after, successful batch receipt, territorial-loss and capitulation receipts, final live F/A |
| Visibility | Available after a qualifying severe-excess opening, with the ordinary achievement eligibility state |
| Difficulty | Large deliberate force reduction and management of random removal risk without hollowing the country below the final band |

This is not a precision lottery requiring an exact random unit or exact equality. The broad final band permits meaningful planning and capacity growth. A batch stops at compliance and may leave the force below the achievement band, so the player must account for the risk rather than receiving an automatic award for pressing the largest action.

### A096.3: `chaosx_096_inspection_proof`

Concept direction: a country expands its army while consistently supporting it through rolling inspections.

| Field | Requirement |
| --- | --- |
| Initial eligibility | A genuine Evolution III or IV episode with entry F at least 1.25 times entry A |
| Challenge | Reach the first legitimate release, then pass at least three actual scheduled reviews and finish the firing's entire local review budget without another Event 096 hold |
| Growth requirement | At the final review, F is at least 1.25 times the first-release force |
| Strict compliance | At every qualifying review, F is at most A, even though the relock hysteresis would tolerate a small higher value |
| Disqualifiers | Repeat firing replaces the qualifying grant, renewed hold, skipped or cancelled reviews, regime-disable credit removal, manual clear, annexation, or invalid succession |
| Tracking | Firing grant, first-release force, actual spent-review receipts, each review's F/A, renewed-hold flag, final local closure |
| Visibility | Revealed with rolling-inspection capability, conditions shown without another dedicated public review counter |
| Difficulty | Sustained expansion under repeated capacity checks rather than a single threshold crossing |

## 6. Achievement and asset integration

Keep the three achievement definitions in the existing shared root registry if its `unique_id` contract requires one. Update the shared English achievement localisation, `interface/chaosx_achievements.gfx`, all exact three-state DDS paths, and the event documentation together.

Every objective needs an eligible unfinished state, a completed state, and a not-eligible state. Its art must communicate its own objective. None may reuse the category or action icon as a resized substitute.

Achievement tracking is durable country history with explicit episode and grant boundaries. A new game, observer fixture, or source-only model does not grant a real achievement. Repeats cannot merge unrelated progress into an easy completion, and a vanished country cannot be treated as a successful demobilization.

The normal achievement interface may describe objective thresholds, but this event adds no new live achievement meters to the decision category. The core four-slot information budget remains intact.
