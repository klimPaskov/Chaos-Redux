# Inflation planning package

This is the accepted design and implementation handoff for Event 100, Inflation.
A major or player country enters a price crisis managed through one signed price index, a lagged credit stance and a few paid programmes; it must hold prices stable for a continuous period, can overshoot into harmful deflation, and can lose its government to its actual opposition if prices stay extreme.
Every cost it charges is a native lever: consumer goods, construction, factory and military output, stability, political power, war support, trade and transport.

The event is not implemented; the legacy script is `events/100_unknown.txt`, with the existing `chaosx.nr100.1` root.
Working implementation plans and actual specialist handoffs belong under `docs/plans/100_inflation_plans/`.

## Read the design in order

| Part | File | Main purpose |
| --- | --- | --- |
| 1 | [Core](100_inflation_spec_part_1_core.md) | Identity, opening, central loop and complete design orientation |
| 2 | [Economic balance](100_inflation_spec_part_2_economic_balance.md) | Current causes, policy lag, penalties, emergency access and both recovery directions |
| 3 | [Decisions and missions](100_inflation_spec_part_3_decisions_missions.md) | All fourteen native action consumers, two support slots, costs, milestones and cancellation |
| 4 | [Recovery and recurrence](100_inflation_spec_part_4_recovery_repeat_lifecycle.md) | Stable attempts, exposure, warning, closure, cooldown and memory |
| 5 | [Political consequences](100_inflation_spec_part_5_political_consequences.md) | Actual opposition, concession/refusal, native civil war and country continuity |
| 6 | [Evolutions, connections and Chaos](100_inflation_spec_part_6_evolutions_connections_chaos.md) | Four cumulative tiers, real owner integrations and bounded outcome accounting |
| 7 | [Presentation and assets](100_inflation_spec_part_7_presentation_assets.md) | The public read model, native category, complete art families and writing direction |
| 8 | [AI and balance scenarios](100_inflation_spec_part_8_ai_and_balance_scenarios.md) | Economic intent, targeting, politics and probability questions |
| 9 | [Achievements](100_inflation_spec_part_9_achievements.md) | Six difficult objective contracts and anti-farming continuity |

## Production handoffs

- [Coding prompt](100_inflation_coding_prompt.md)
- [Decision and mission prompt](100_inflation_decision_mission_prompt.md)
- [Asset prompt](100_inflation_asset_prompt.md)
- [Achievement prompt](100_inflation_achievement_prompt.md)
- [Goal prompt](100_inflation_goal_prompt.md)
- [MCP and subagent map](100_inflation_mcp_subagent_handoff.md)

## Evidence and design basis

- [Research and bibliography](100_inflation_research_and_bibliography.md)
- [Supplied-source manifest](100_inflation_supplied_source_manifest.json), a historical receipt of the original planning session's attachments rather than a current-checkout inventory
- [Authored-model examples and future acceptance scenarios](100_inflation_balance_examples.md)

All named actions and content concepts are working labels, not final localisation.
Numbers are proposed gameplay tuning anchors.
The package does not claim runtime implementation, finished art, calibrated AI, native rendering or live-game testing.

## Acceptance basis

The original user brief is summarized by the planning author and not bundled here.
The package attributes these requirements to it, and they stay fixed:

- Event 100 Inflation is Minor Repeatable at Chaos level 1, a High member of the Negative Economy cluster (10), with status To Be Reworked.
- One signed balance problem in which deflation is harmful too, and sustained stabilization as the victory condition.
- Prolonged failure brings political upheaval through the country's actual opposition, by transfer or civil war, and the successor inherits the damaged economy.
- The event repeats, and its four cumulative evolutions keep their names and gates: Wage-Price Spiral at 200, Currency Crisis at 400, Economic Radicalization at 600 and Hyperinflation at 800.

The [research record](100_inflation_research_and_bibliography.md#independent-review-and-accepted-refinements) attributes the rest of the design to the original planning parent after architecture, decision and improvement-loop reviews.
The 7 October import review and the 10 October audit preserve that acceptance without treating it as authorization to implement.

## Public read model

The 10 October audit checked the package for the defect of a money-like meter that becomes a second economy, and the read model holds.
The player sees one signed price index with its band and trend, the credit stance in effect and the one that will take effect at the next review, and at most one timer per active programme plus one recovery-or-political objective; [Part 7](100_inflation_spec_part_7_presentation_assets.md#what-the-player-sees) is the canonical home of that budget.
Each value drives a choice: the index and stances decide whether to tighten or ease, the programme timers decide when to wind a commitment down, and the objective timer is the deadline the player plays against.
Exposure clocks, reprieve progress, wage liability, failure memory, re-entry cooldowns and cause point values stay hidden, and causes are named with the native lever that removes them.
There is no treasury, currency stock, confidence gauge or event-specific resource; every cost is paid in existing economic levers.

## Open questions

### Famine coupling (resolved)

Disposition: accepted and queued; the orchestrator accepted the audit proposal on 10 October 2026, and it is now specified in [Part 6](100_inflation_spec_part_6_evolutions_connections_chaos.md#systems-this-event-leaves-to-their-owners).
Implementation waits for Event 100 itself, and the famine owner adds the read when both exist.

### Review cadence if the credit loop proves busy

Disposition: `unresolved`; the orchestrator's 10 October 2026 decision is to keep the ten-day review and switch to thirty days only if playtests show clicking.
The ten-day review with a one-step tighten or ease decision and a shared ten-day cooldown is the event's core loop, and a typical episode needs only a handful of stance changes.
If live play shows the loop turning into a click every review, the proposal is to move to a thirty-day review with all per-review index values tripled.
That keeps the per-day rates of Part 2 and the balance examples, at the price of a coarser forecast and a policy lag of thirty to sixty days.

## Revision log

### 2026-10-10 spec audit

- Recorded the public read-model verdict and the attributed user decisions in this entry; Part 7 stays the canonical home of the value budget.
- Retired D12 Targeted Credit, which duplicated the +5 Moderate support stance at a similar cost; the package now has fourteen action consumers, 43 art subjects and 55 runtime textures.
- Part 2: the crisis spirit expresses inflation through consumer goods and deflation through idle factory output and construction, so the crisis is felt on the production screen.
- Part 7: causes are shown by name with their native lever, never as point contributions.
- Part 6: added a section stating which shared systems the event deliberately leaves to their owners, and the famine coupling (severe inflation raises Import Food cost and slows Food Reserve refill through a read-only band trigger), accepted by the orchestrator the same day.
- Replaced the remaining Codex-specific image-generation wording with the `gptimage` MCP route and trimmed asset-prompt passages that restated `chaos-redux-event-assets` (portrait lifecycle, DDS byte checks).
