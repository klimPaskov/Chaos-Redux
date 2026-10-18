# Implement the Fuel Crisis connection to Event 101 Tasks

Read all five Fuel Crisis spec parts, the implementation handoff, and the final review record under `docs/specs/109_fuel_crisis_specs/`. Part 3 is the canonical contract. Read current `AGENTS.md`, the Tasks specification and implementation discovered in the checkout, and the current decisions-missions, events, dynamic helper, subagents, and relevant UI and save-inspection guidance before editing. The prior Tasks brief was fully read during planning and establishes player-only assignments, dynamic objectives, and Tasks-owned outcomes. It is not an implementation API.

The parent assigns exact Event 101 adapter, mission, trigger, effect, and localisation paths after discovery. Remain within that scope. Place the audit handoff under `docs/plans/109_fuel_crisis_plans/`. Do not create another recovery service, event-owned reward table, task currency, or parallel mission interface.

## Verify the owner and measurements

Locate the real player selector, objective pool, active-task limit, assignment record, progress evaluator, deadline synchronization, success callback, timeout path, cancellation, and cleanup. Inspect installed native documentation and exact precedents for demand, national stock, capacity, actual delivered oil, conversion units, and attributable ordinary actions. Record source identity, units, precision, and limitations.

D0 must represent meaningful pre-wipe active-commitment demand. Automatic fuel starvation is not an action and cannot establish conservation. Nominal import allocation is not proof of usable delivery. Do not invent accessors or silently substitute an estimate for an unavailable required measurement. Report the conservation route, recurring supply route, and oil-access template separately if support differs.

The core world pass stays unconditional. A verified enabled adapter can capture its onset facts during that already required pass. Invoke Tasks afterward through its real owner. Preserve the committed receipt, onset date, frozen origin, country membership, D0, C0, and F0 as defined by the specification.

## Preserve selection and admission

Event 101 selects its recipient under its own player-only rules. In multiplayer, Fuel Crisis must not reroll that player merely because another country has a better crisis objective. Consider this connection during the first 90 days after impact, only for a country that existed then, lost positive fuel, still has a meaningful gap, and has a real measurable action available. Retain existing enabled states, active-task limits, diversity, and no-valid-task behavior.

Issue at most one Fuel Crisis task per country per occurrence, with no more than one active at once. Already solved, automatic, impossible, unaffordable under the actual ordinary rules, or technically unobservable candidates must be excluded. An excluded candidate does not alter the world wipe.

## Implement the two alternatives exactly

For reserve recovery, use `R = min(14 × D0, 0.5 × C0)`, positive meaningful D0, C0 of at least `14 × D0`, current capacity able to hold R, and assignment stock below R. Freeze the selected conservation or supply-improvement action. Da is demand implied by actual assignment-time commitments, independent of starvation-limited consumption. Conservation requires a real observable activity change and sustainable demand at most `min(0.8 × D0, 0.8 × Da)`. Supply improvement requires at least `0.25 × D0` of additional recurring usable inflow. Hold the action and reserve requirement for seven complete daily observed intervals. The reserve remains owned by the country.

Exclude unchanged recovery expected to reach R within 60 days and an intervention already made before assignment that leaves only waiting. Ca is actual assignment capacity. Forecast stock after the action lead as `min(Ca, max(0, S + A × (J0 − Da)))`. Use `G = max(0, R − projected stock)`, positive `N = J1 − D1`, and `B = ceil(G / N)`. The reserve duration is the next multiple of five at or above `max(90, 1.30 × (A + B) + 7)`. The 30% margin covers the full action lead and refill period.

For oil access, choose a real feasible source action and freeze its identity and baseline. The source target is `max(Q0 + 0.25 × D0, 1.1 × D0 − Jother)`. Require a genuine post-assignment source improvement and actual usable delivery for fourteen complete daily observed intervals. Initial total dependable inflow must be below `1.1 × D0`. The duration is the next multiple of five at or above `max(90, 1.30 × A + 14 + 7)`.

Reject either forecast when its rounded duration exceeds 180 days. Do not clamp an impossible project into the range. Recheck feasibility after the existing Tasks difficulty or stakes scaling, then freeze all terms once. Part 3's worked examples and Part 5's boundaries are required review cases.

## Synchronize progress and resolution

The first qualifying observation records zero elapsed days. Seven complete intervals require eight qualifying daily observations, and fourteen intervals require fifteen. Failed conditions reset the hold. Do not infer missed observations or fabricate continuity on load. Daily sampling does not prove every intraday value.

Use the verified native timer synchronization route after activation and any accepted owner deadline change. A stored date alone does not update a native mission timer. Document the exact cutoff convention, compare the last permitted and first expired observations, and preserve Part 3's success-before-timeout behavior within the valid cutoff.

Consume the active task record before dispatching a reward or consequence. All terminal callbacks share one guard. Normal success, normal timeout, foreseeable wartime disruption, neutral technical cancellation, country disappearance, loss of player control, and feature disablement must follow Part 3. A fresh deliberate forced occurrence neutrally cancels a replaced old-context task through Event 101. Duplicate delivery changes nothing. Preserve minimal terminal and achievement provenance before cleanup.

The assigned task uses at most three primary numeric groups for target/progress, observed hold, and time remaining. Explain the selected action and retained fuel clearly through existing Tasks text. Ordinary trade and construction costs remain on those actions. Write final localisation from the direction rather than copying working labels.

## Achievement callback

Read the achievement prompt and Part 4 fully. The extra qualification belongs inside a genuine active reserve task. Eligible ordinary origin, same player country, wartime onset and assignment, material pre-wipe reserve, sufficient capacity, no assignment surplus, additional actual imported flow, full reserve, observed hold, and both cutoffs must all be proven. Forced and raw debug origins are excluded. A successful ordinary task can grant its reward without the achievement. Do not delay its success or add post-completion monitoring to chase a badge.

## Audit and return evidence

Use the installed decision, event, and linked consumer inspection routes and the required matched UI render evidence. Route changes to recipient or objective weights through the read-only probability auditor with baseline inspection, named scenarios, evaluation, boundary sweeps, and post-change comparison. Keep unsupported capability findings explicit.

Return exact files and identifiers, owner and accessor evidence, unit mapping, candidate and action coverage, formula checks, timer and hold behavior, outcome and cleanup results, exploit checks, localisation coverage, achievement callback state, and unresolved limitations. The parent owns final integration and completion. Do not call the entire connection complete when any accepted template or required action path remains unsupported or unverified.
