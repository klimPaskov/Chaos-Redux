# 10. AI policy and budget behavior

## Objective

AI sponsors pursue a useful subject at a reasonable cost while protecting their own war effort. They use the same Influence formula, saturation, project duration, physical delivery, interference budget, and takeover condition as players. They receive no free monthly Influence and no target choice weighted toward an intended historical victor.

Use public and legitimately available world information. The AI can read its own receipts and the published ranking. It cannot read a future random result or an uncommitted player's next action.

## Target priority

Reevaluate when a race opens, a participant joins, a meaningful action completes, political alignment changes, a major war condition changes, or the target's 30-day attention check occurs. The check iterates the active race registry, not every country daily.

The following values are willingness inputs, not probabilities. Combine them into the existing MTTH-backed or scripted AI score adapter only after inspection of its verified semantics.

| Factor | Proposed contribution |
| --- | --- |
| Base interest in a valid target | 20 |
| Shared border or clear strategic access relationship | +20 |
| Target shares ruling ideology | +15 |
| Target's government is friendly and stable enough for support | +10 |
| Sponsor already has at least 40 Influence | +20 |
| Sponsor is within 20 Influence of the leader | +15 |
| Target controls an objectively useful existing supply, resource, or regional position | +15, supported by a concrete provider |
| Main rival leads by at least 25 | -15 unless a feasible catch-up route exists |
| Sponsor has a serious current equipment deficit | -20 for equipment-intensive routes |
| Sponsor's war situation makes material spending dangerous | -25 for new long material contracts |
| Sponsor is already funding two other targets | -20 |
| No valid positive action can be afforded without breaking reserves | Willingness 0 for paid action, registration retained |

Do not give a bonus simply because the rival is human. Do not assign a permanent factor to a named major. Concrete country strategy can affect the value of a border, alliance, or industry if supplied by normal game state.

## Resource reserves

Initial reserve targets are 75 political power and 15 command power for AI majors. AI-controlled former player participants and AI minor participants use a 50 political-power target. These are budget preferences, not player restrictions.

Equipment assistance must leave at least 25% of the donor's current stockpile of the selected family and must not worsen a verified urgent frontline deficit. If current stockpile demand cannot be measured reliably, use the conservative reserve and select advisory work. Do not invent a division-demand formula from unrelated equipment totals.

Industrial commitments may consume up to 25% of the donor's usable civilian factories under normal conditions, with a minimum of one if a valid public-works contract is affordable. When that minimum would consume all usable civilian construction during a major defensive war, the AI avoids that commitment. The player can choose to take the risk.

A sponsor within 15 Influence of a reachable victory can temporarily lower its political-power reserve by 25 if the final action remains affordable and does not violate an actual game requirement. It cannot spend negative resources or exceed the action cap.

## Campaign styles

An aligned government route favors government support first, then alternates propaganda or material help to avoid repeated-family losses. A weak opposition route raises pledged popularity before attempting expensive leadership operations. A materially strong but politically incompatible sponsor favors a useful investment or advisory relationship while funding opposition work.

A war-strained sponsor prefers short political actions and advisory work over weapons it needs at the front. An established investor can defend its economic institution, but should compare the opportunity cost of interference with simply finishing a project. A sponsor leading at 85 or more normally prefers the fastest valid positive completion.

The AI must plan against remaining time, not only nominal Influence per political power. A 90-day industrial program that will finish well after a rival's visible 15-day finishing campaign is a poor catch-up choice. A material project already close to delivery may still be worth completing.

## Interference policy

Attack when the rival has meaningful Influence, sufficient remaining loss budget, and a credible near-term lead. A target at 0 is never useful. A nearly exhausted loss budget sharply reduces willingness. A sponsor should not repeatedly spend its only political slot on interference while never building its own position.

A blocking coalition is attractive when another sponsor is at least 75 and has a short valid finishing route. Join only if the combined action will have a real remaining effect under the common loss cap. The coalition's support contributions are not separate attacks or score multipliers.

## Several targets

The Great Game allocates three campaign slots across target priorities. The AI can concentrate all practical effort on one target, keep one slow investment in another, or temporarily abandon a low-priority race. It cannot receive an extra campaign slot merely for being a major.

An AI normally selects at most two funded targets at once. A third is allowed only for a near-complete action or a specifically higher-value opportunity. Unfunded registration in the other races remains visible and follows inactivity rules.

## Required AI evidence

Inspect every real decision weight and MTTH provider through `hoi4.probability_inspect`. Evaluate named states for a compatible major, incompatible major, player-sized minor under AI control, poor sponsor, frontline shortage, 85-point leader, exhausted rival-loss budget, and five concurrent targets. Sweep popularity thresholds 25 and 50, finish proximity, available resources, and saturation counts.

Treat the table above as an authored policy specification. It is not a probability distribution and does not establish a win rate. Use `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_simulate`, and `hoi4.probability_compare` as appropriate after implementation. The read-only auditor supplies evidence and does not choose a preferred winner.
