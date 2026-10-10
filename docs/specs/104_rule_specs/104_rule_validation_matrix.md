# Event 104 Rule: validation matrix

## Evidence status

The scenarios preserve behavioural requirements and distinguish source-supported checks from user-owned game observations.
Use current installed references, actual implementation source, and representative available checks without requesting or awaiting live-game evidence.
Apply current `AGENTS.md` retry limits, with an initial read-only request and at most one useful correction across the underlying failure before source review and local calculations.
An unavailable optional check is a limitation, while a requested specific test artifact or an indispensable unsupported native capability remains incomplete.

This file defines implementation acceptance scenarios.
It does not report those scenarios as executed.
The completed planning evidence consists of full supplied-source reading, pinned repository research, mathematical review of the proposed formulas, and the independent design reviews recorded in the closure document.
No HOI4 runtime, MCP event or probability analysis, engine render, save/load test, or multiplayer session ran in this task.

Every implementation result must identify its actual source revision, scenario fixture, tool route, evidence mode, completed coverage, diagnostics, and unresolved limitations.
Retain immutable before-source bytes and hashes for any compare claim.
Use the same named scenario inputs before and after a patch.
An absent pre-edit Event 104 source is an absence baseline, not an excuse to compare the final source against itself.

## Common fixtures

The abstract rule fixtures below validate the specified selection semantics independently of the eventual native rule inventory.
They are declared test models and must not be shipped as substitute game rules.

| Fixture | Definition |
| --- | --- |
| FX-BINARY | One native-like abstract rule with default `D` and one non-default `A`. |
| FX-TRIPLE | One abstract rule with default `D` and non-defaults `A` and `B`, both meaningful in the declared world. |
| FX-OPTIONS | Three equally eligible rules with one, two, and four eligible destinations. |
| FX-MASKED | An apparently permissive destination whose only relationship remains blocked by an independent restriction. |
| FX-PREFIX | A rule destination that would erase the only meaningful consumer of an earlier proposed batch row. |
| FX-IV | Six eligible revisable rules, three fresh rules, compatible transitions, and a frozen requested count of six. |
| FX-NATIVE | An actual admitted base-game rule with exact definition, default, consumer, writer, and readback evidence. Cannot be an invented model. |
| FX-NATIVE-WIDE | Actual no-DLC world demonstrating eight compatible meaningful transitions and at least four revisable altered rules. |
| FX-DUAL | Two legitimate same-day requests with distinct originating context and overlapping candidate pools. |

## Native support and pool admission

| ID | Scenario | Pass condition |
| --- | --- | --- |
| N01 | Discover effective native rule definitions and overrides. | Every admitted native key has one understood effective definition, canonical default, complete option inventory, source revision, and localised names. |
| N02 | Attempt a proved default-to-non-default write on FX-NATIVE during play. | Native readback changes immediately, a current gameplay consumer differs, and no restart or manual save edit is required. |
| N03 | Attempt a non-default-to-different-non-default write. | The distinct destination is native, meaningful, persistent, and accepted only with revision permission if historically touched. |
| N04 | Invoke a country `set_rule` permission effect in the research fixture. | It is correctly classified as a different mechanism and is never accepted as proof of native game-rule mutation. |
| N05 | Select a startup-only map or country setup rule. | It is excluded before the random draw and cannot consume an occurrence. |
| N06 | Place a Chaos Redux configuration control among discovered rule definitions. | Protection excludes it regardless of folder, name, group, or apparent option count. |
| N07 | Use an unavailable DLC option or missing rule object. | No attempt is made, no fallback grants content, and no missing-token error is accepted. |
| N08 | Test a cosmetic option or two currently equivalent options. | No material destination is admitted. |
| N09 | Test `allow_lend_lease` under a bilateral embargo. | The embargo retains precedence, and the masked pair cannot serve as a meaningfulness witness. |
| N10 | Test FREE and LIMITED against the complete installed native consumer. | Their actual distinction is established before either transition is admitted. The script's identical enable branches are not overinterpreted. |
| N11 | Test a country AI rule with a missing, human, annexed, or route-committed country. | The inappropriate destination is excluded without recreating countries or undoing focuses. |
| N12 | Test a startup-random AI option. | It remains excluded unless a supported new mid-campaign consumer is proved. No startup flags are replayed. |
| N13 | Test existing treaties, forces, construction, and ongoing justifications for an admitted transition. | Each affected object follows the documented native behaviour and the report accurately describes any important limit. |
| N14 | Build FX-NATIVE-WIDE without DLC. | All maximum-count and revision-breadth targets have actual consumer evidence, or the exact shortfall is reported as an unresolved design gate. |

## Selection and request correctness

| ID | Scenario | Pass condition |
| --- | --- | --- |
| S01 | Baseline, one fresh eligible rule at default. | Exactly one non-default different setting commits and becomes touched. |
| S02 | Untouched FX-TRIPLE starts at player-selected `A`. | Only `B` is eligible. Default `D` and current `A` are excluded. |
| S03 | Touched FX-BINARY is at `A`, with II and IV enabled. | It has no valid destination and cannot be revised to `D`. |
| S04 | Repeat before revision permission with one untouched candidate remaining. | The untouched rule is selected and touched rules stay excluded. |
| S05 | An external system restores a touched binary rule to default. | Before revision permission it stays excluded, afterward it can change to `A` if meaningful. No automatic reapplication occurs. |
| S06 | FX-OPTIONS ordinary first draw. | Rule probabilities are one-third each, with destination probabilities one-third, one-sixth, and one-twelfth as appropriate. |
| S07 | Previous batch overlaps only part of the eligible pool. | Outside-previous-batch rules are drawn first, then recent rules can fill remaining slots. |
| S08 | Every current candidate is in the previous batch. | The soft respite yields and the event can make a valid revision. |
| S09 | Multi-rule batch requests more successes than candidates. | It commits the supported distinct subset, reports actual count, and never pads with invalid rules. |
| S10 | One attempted identity returns a proven unchanged result. | It is removed for the request, no provenance or Chaos is added for it, and another unattempted candidate may fill the slot. |
| S11 | Every attempted identity is a definite no-op. | No successful handler, cap change, Minor pacing change, successful history, or Chaos award occurs. |
| S12 | FX-PREFIX prospective incompatible destination. | The destination is filtered before selection and writing, preserving every committed row's meaningful effect. |
| S13 | A random compatible prefix leaves fewer possible extensions than another prefix would. | The batch shortens honestly without backtracking or claiming uniform final combinations. |
| S14 | Exhaust the finite attempt inventory. | Execution terminates within one attempt per initial native identity and does not reroll indefinitely. |
| S15 | Direct root call without a valid committed receipt. | It cannot mutate, reroll, or charge a normal occurrence. |
| S16 | Duplicate callback or report acknowledgement. | Native state, touched membership, Chaos, history, and occurrence accounting remain unchanged. |
| S17 | Insufficient safe receipt capacity. | Rejection happens before the first native write and does not erase older provenance. |

## Evolutions and counts

| ID | Scenario | Pass condition |
| --- | --- | --- |
| E01 | First successful occurrence at Chaos 199, 200, 399, 400, 599, 600, 799, 800, and 1000. | Only enabled threshold-eligible pre-fire stages contribute, and each committed new stage is logged once. |
| E02 | First attempted high-Chaos occurrence has zero successes. | Provisional pre-fire stage unlocks and success history are not consumed. |
| E03 | Active-system stage waits at threshold. | The named 90-day MTTH parameter and declared modifiers are used through the verified game-version adapter. |
| E04 | Active-system stage falls below threshold before activation. | Eligibility stops, no hidden guaranteed progress or catch-up activation is invented. |
| E05 | Disable a stage before unlock, then enable it later. | No disabled activation or recorded flag occurs. Correct pre-fire or active-system timing resumes. |
| E06 | Disable an unlocked stage, then reenable it. | Future capability changes immediately, historical native mutations remain, and no duplicate evolution record or Chaos award occurs. |
| E07 | I disabled, II active. | One rule per firing, including valid revisions. |
| E08 | II disabled, III active, IV inactive. | III count applies to fresh rules only. |
| E09 | II disabled, IV active. | IV's own revision and mixed selection remain active without falsely unlocking II. |
| E10 | All four stages active, current Chaos falls below 200. | Unlocked enabled capabilities persist without reapplying the shared activation helper's current threshold, current-value formulas clamp safely, and count precedence remains IV. |
| E11 | I count at Chaos 200, 400, and 600. | Second-slot probability is 0.35, 0.50, and 0.65, with no extra count reroll. |
| E12 | III count at Chaos 600, 800, and 1000. | Requested counts are 2/3, 3/4, and 4/5 respectively before shortening. |
| E13 | IV count at Chaos 800, 900, and 1000 with fewer than four or at least four revisable rules. | Footprint and Chaos steps match Part 3 and never exceed eight successes. |
| E14 | FX-IV with compatible candidates. | One fresh success is sought, three revisions are targeted, and remaining slots use the current union. |
| E15 | IV categories shrink through compatibility or definite no-ops. | Targets yield to actual eligibility and the receipt records truthful fresh/revision totals. |
| E16 | A fresh row becomes touched during the current IV batch. | It does not increase this batch's frozen revision footprint, quota, or revision total. |
| E17 | Batch's Chaos award crosses another threshold. | Current count and provisional capabilities are unchanged. No recursive free firing or same-batch expansion occurs. |
| E18 | Master Rule disabled and later reenabled, with a legitimate forced request during the disabled interval. | Normal firings, background MTTH, and new automatic unlock notifications pause. Native changes and unlocks persist. Force uses applicable enabled capabilities without restarting the background lifecycle. Reenable resumes current-condition checks without catch-up. |

## Accounting, persistence, and concurrency

| ID | Scenario | Pass condition |
| --- | --- | --- |
| L01 | First changes affect two, three, nine, and ten countries. | First-change awards are +1, +2, +2, and +3 using unique demonstrably affected countries. |
| L02 | Novel revision followed by repeated oscillation through previously visited options. | A new destination earns its one-time +1, already visited destinations earn zero, and every real transition remains reported. |
| L03 | Raw batch award exceeds twelve. | Exactly +12 is applied once and all successful destinations remain marked visited. |
| L04 | Later war, annexation, tension, or casualty results from a new permission. | Rule adds no duplicate generic outcome award beyond its own native-transition credit. |
| L05 | Normal, cluster, and manual dispatch around the same state. | Each legitimate request has a distinct ID and at most one successful accounting receipt. Cluster burst pacing is not charged per rule. |
| L06 | Same-day FX-DUAL requests before revision permission. | The second request sees the first touched set and cannot select the same newly touched rule as fresh. |
| L07 | Same-day FX-DUAL requests with revision permission. | A revisit uses the new actual current option and excludes both current and default. |
| L08 | Random Stuff dispatches synchronously after the Rule handler. | Rule history retains its original payload and order, and later cleanup does not erase the nested request. |
| L09 | Two reports for the same human remain open or pending. | Each retains its own immutable transitions and acknowledgement identity. |
| L10 | Save and reload after a commit but before acknowledgement. | Native rules persist, pending presentation is coherent, and no mutation or award repeats. |
| L11 | Save and reload after a rejected request. | The request counter does not reuse the rejected ID. |
| L12 | Executor is annexed, changes tag presentation, or becomes AI controlled. | Native rules and global history survive, future scheduling transfers correctly, and no actor is falsely blamed. |
| L13 | A newly released country uses an affected rule. | It observes the shared native setting without a Rule reapplication loop. |
| L14 | External native change occurs between firings. | Current readback wins, old receipts remain historical, and no external change earns Rule credit. |
| L15 | Content update removes or renames a rule or option. | History preserves identity, future selection excludes unresolved entries, and migration does not reset novelty. |
| L16 | Ambiguous or unintended native result with a verified prefix. | Further writes stop, quarantine persists, the surviving confirmed subset is accounted once, and the unresolved row receives no speculative credit. |
| L17 | Ambiguous result with no confirmed rows. | An incident receipt and quarantine persist without ordinary success accounting or a claim of unchanged world state. |
| L18 | Reload or force attempt while quarantined. | Quarantine remains and no native Rule write occurs. |
| L19 | Multiplayer host and peers process two legitimate requests. | One authoritative order, matching native options, matching provenance, and correct recipient receipts are observed across peers. |

## Campaign integration and achievements

| ID | Scenario | Pass condition |
| --- | --- | --- |
| C01 | Diplomatic task becomes impossible before payment. | Display and action gate change together, with an accepted alternate route or neutral closure. |
| C02 | A pending paid task becomes impossible. | Only recorded refundable outstanding amounts are returned, callbacks retire, and no success or failure reward is manufactured. |
| C03 | A partition proposal changes legality before execution. | It is revalidated or invalidated, no stale transfer occurs, and completed earlier settlements remain. |
| C04 | A warlord focus depends on a now-blocked foreign action. | Its accepted bypass, completion, or cancellation behaviour prevents an endless impossible dependency. |
| C05 | Random Idea or another permission layer masks a candidate. | Native precedence is preserved and only a genuine unmasked witness admits the transition. |
| C06 | A01 success and near misses. | Exact victory, 20 percent contribution, second-family change before victory, day-180 minimum, day-365 deadline, and fixed-core condition are enforced. |
| C07 | A02 success and near misses. | Original independent members remain, two new independent members join, a genuine revision precedes at least one join, three ideology groups coexist, and day-270/day-540 gates are enforced. |
| C08 | A03 success and near misses. | IV has four changes and two revisions, two player-impact rules, 25 percent contribution, timely victory, 90-day continuity, four current non-default touched rules, and fixed-core condition. |
| C09 | Stale achievement deadline or victory callback after failure or new attempt. | Generation mismatch rejects it and cannot grant or restart an achievement. |
| C10 | Player switching, observer, subject, capitulation, or test fixture. | The current attempt follows the documented disqualification contract and no unsupported account continuity is claimed. |
| C11 | A03 qualifying victory occurs exactly on day 365, with valid continuity through day 455. | The victory is captured before expiry can reject it, the attempt remains in its continuity phase, and the final check can award on day 455. |
| C12 | A03 has no qualifying victory by the end of day 365 and wins on day 366. | Expiry occurs only after the inclusive window, the late victory grants no credit, and stale callbacks cannot revive that attempt. |
| C13 | A01 or A03 arms during multiple qualifying wars and a new war begins later. | Only the frozen initial war set qualifies. The first valid result uses its own contribution ratio and cannot be replaced to reset timing. Any merged identity requires verified lineage. |
| C14 | Independent player has no owned core states when a military achievement would arm. | A01 and A03 do not create an attempt, and an empty denominator cannot grant credit. |

## Presentation, assets, and catalog

| ID | Scenario | Pass condition |
| --- | --- | --- |
| V01 | One-rule report and eight-rule report with long names. | Every committed transition remains readable in supported native description/tooltip space. |
| V02 | Earlier receipt viewed after the same rule changes again. | The old report and history retain the old transition, while ordinary campaign UI shows the current setting. |
| V03 | Evolution preview versus actual activation. | Preview has no invented date, actual activation records the correct stage once, and disabled stages remain unrecorded. |
| V04 | Global occurrence actor display. | The executor is not presented as the author of the rule change. Country-specific subjects are labelled accurately. |
| V05 | Report texture and all nine achievement states. | Dimensions, canonical templates, transparency, DDS round-trip appearance, and live consumers match the asset manifest. |
| V06 | Standard and constrained supported resolutions and UI scales. | No clipped rows, broken keys, unusable tooltips, incorrect state art, or hidden acknowledgement occurs. |
| V07 | Catalog reconciliation. | Authoritative workbook uses the accepted identity and exact mirror text, status is evidence-based, and all three CSV exports are regenerated successfully. |
| V08 | Full registration and unsupported state. | ID bounds, type, required Chaos, dispatch, cluster, logs, details, debug, and evolution selectors agree. Unsupported Rule displays the proper unavailable treatment. |

## Probability workflow

The implementation probability auditor prefers a targeted `hoi4.probability_inspect` after verifying the actual exposed schema.
When analysis is unavailable or unsupported after the shared retry limit, calculate the named representative cases from the actual implementation and retain assumptions, score-versus-probability limits, and before/after evidence.
It must identify all count draws, rule strata, destination draws, compatibility predicates, MTTH modifiers, external state inputs, and shared event-pool dependencies.
Evaluate FX-OPTIONS and the named S and E scenarios with complete candidate manifests.
Sweep the threshold boundaries 199/200, 399/400, 599/600, 799/800, 899/900, and 999/1000, plus the IV revisable count boundary three/four.

Use sequence analysis only with the complete declared transition model, including touched removal, revision admission, recency strata, pool masking, eligibility changes, shared cap recovery, and occurrence cadence where relevant.
A result conditional on Rule firing is not the probability that Rule fires in the full campaign.
Use simulation only for declared uncertain inputs and identify it as sampled evidence with its seed and uncertainty.
Do not infer exact campaign timing from a few observed saves.

Every balance patch requires the parent to preserve immutable before bytes and the exact scenario set, then obtain a comparison on those same inputs.
The auditor supplies evidence and does not choose balance or edit source.
Keep exact, bounded, sampled, score-only, and unresolved results visibly distinct.

## Completion record

Record each scenario as passed, failed, blocked, or not run, with a reason and evidence reference.
Label source-supported results separately from rendered or observed game results.
Retain unrun save/load and multiplayer scenarios as unobserved behaviour without treating their absence as an agent delivery gate.
The final implementation claim requires the authorized mechanics, content, assets, consumers, and meaningful balance checks, with no known defect after current reference and source review.
Unsupported native mutation or inadequate required pool breadth is missing capability, and any design reduction needs explicit acceptance.
Unavailable optional MCP or visual checks must have their limitations recorded.
The current planning package does not provide those implementation passes.
