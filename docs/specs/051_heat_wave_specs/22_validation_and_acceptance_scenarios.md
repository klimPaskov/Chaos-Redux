# Validation and Acceptance Scenarios

## Validation principle

Validation must prove the complete event contract. Parser success is not enough. Event 51 can load while still duplicating deaths, leaving stale state, selecting invalid targets, damaging the wrong buildings, or making every AI choose the same response.

## Source and documentation preflight

Before implementation:

- read the accepted Event 51 specs
- inspect any existing Event 51 source and IDs
- inspect the repeatable-event registry
- inspect Event 013 gateway and wildfire ownership
- inspect Deaths population and military transactions
- inspect Famine and Migration owner APIs
- inspect Natural Disasters cluster registry
- inspect map-mode framework
- inspect current terrain and map tooling
- inspect relevant decision, dynamic modifier, AI, event-log, super-event, achievement, asset, and audio precedents
- read required offline wiki and vanilla documentation

Record exact unavailable sources as blockers.

# Static acceptance scenarios

## HW-VAL-001 Registration

Event 51 resolves as Minor Repeatable, Chaos level 1, and High-severity Natural Disasters member. Event Details and workbook agree.

## HW-VAL-002 Active exclusion

An active episode, recovery, or cleanup state makes Event 51 unavailable to normal selection and cluster firing with the correct reason.

## HW-VAL-003 Fresh generation

A second completed firing increments the generation and contains no stale missions, targets, reports, or temporary state from the first.

## HW-VAL-004 Save and reload

Reload during onset, surge, lull, decline, recovery, and cleanup preserves the phase and does not reroll intensity profile.

# Global intensity scenarios

## HW-VAL-010 Mild profile

Opening intensity is low, one modest surge occurs, duration remains near the mild band, and no permanent damage occurs.

## HW-VAL-011 Long plateau

Intensity rises slowly, remains high for a long plateau, and state consequences continue accumulating without noisy oscillation.

## HW-VAL-012 Lull and resurgence

A visible lull cools some states, a later valid resurgence occurs after the minimum gap, and no text guarantees the resurgence beforehand.

## HW-VAL-013 Terminal decline

After terminal decline locks, no new surge occurs and intensity reaches zero without underflow.

## HW-VAL-014 Global mitigation cap

Several countries complete strong measures. Global momentum improves within the cap, but one country cannot end the event alone.

# State Heat Stress scenarios

## HW-VAL-020 Prepared desert state

A desert state with strong infrastructure, low population, functioning water, and active mitigation stays below a damaged temperate capital under the same global intensity.

## HW-VAL-021 Bombed temperate capital

High population, damaged infrastructure, weak water, and hot nights drive the state into Extreme heat despite moderate climate exposure.

## HW-VAL-022 Northern mountain state

The state remains safer during baseline and becomes meaningfully affected only at high global intensity or Evolution III.

## HW-VAL-023 Humid jungle front

Human and military stress is high from humidity, supply, and army load without using desert terrain logic.

## HW-VAL-024 Empty remote state

Environmental stress can rise, but civilian reports, water decisions, and national cost stay limited because population and system load are low.

## HW-VAL-025 Controller change

Physical stress and permanent damage remain. Old controller missions retire and the new controller receives valid actions without duplicate rewards.

## HW-VAL-026 Hysteresis

A state does not bounce between Dangerous and Extreme from small point changes.

# Decision and mission scenarios

## HW-VAL-030 Priority tradeoff

Protect Population Centres reduces urban mortality risk while agricultural or industrial pressure rises according to the accepted sacrifice.

## HW-VAL-031 Priority switch

Switching respects cooldown, pays the visible cost once, and replaces prior priority effects cleanly.

## HW-VAL-032 Water rationing

Early rationing prevents System Failure with a real economic cost. Late rationing reduces harm but does not instantly restore service.

## HW-VAL-033 Cooling centres

Cooling centres reduce mortality in the target state and lose effectiveness under power or water failure.

## HW-VAL-034 Army protocols

Protocols reduce exposure gain and casualty risk but do not overcome complete undersupply.

## HW-VAL-035 Rail mission success

A critical corridor remains open at reduced throughput and avoids direct damage.

## HW-VAL-036 Rail mission failure

The corridor takes real supported damage or a strong route penalty. Failure does not apply only a minor political cost.

## HW-VAL-037 Harvest partial success

Some target states remain protected. Famine request strength reflects partial outcome.

## HW-VAL-038 Controlled shutdown

Output is sacrificed and damage risk falls. Cleanup ends the temporary closure but does not restore destroyed buildings.

## HW-VAL-039 Invalid target cleanup

Annexed, transferred, destroyed, or cooled targets leave the decision and mission lists without stale event targets.

# Military scenarios

## HW-VAL-040 Acclimatization

A division gains protection over the accepted exposure window. Moving between climates prevents instant full acclimatization.

## HW-VAL-041 Offensive exposure

An attacking division in Extreme heat gains exposure faster than a resting supplied division.

## HW-VAL-042 Rotation

A Heat-Exhausted unit moved to a cooler state recovers after confirmation. Disbanding it does not count as rotation.

## HW-VAL-043 Critical casualty

Evolution I applies a bounded military casualty to a Critical unit under valid conditions and records it once.

## HW-VAL-044 Front safety

AI does not abandon an existential capital front merely because another state is cooler.

# Mortality and owner-system scenarios

## HW-VAL-050 Baseline mortality boundary

Baseline produces no recurring mass mortality loop. Isolated report deaths remain bounded and recorded once.

## HW-VAL-051 Civilian heat death

Evolution I removes exact state population, reconciles manpower credit, respects the floor, and creates one Deaths entry.

## HW-VAL-052 No retroactive death

Evolution I activates during an episode and does not charge deaths for earlier baseline days.

## HW-VAL-053 Famine accepted

A prolonged harvest failure produces a validated request. Famine owns stage, relief, and mortality.

## HW-VAL-054 Famine rejected

Incomplete or weak proof is rejected without partial ledger writes or daily retry spam.

## HW-VAL-055 Migration accepted

A Scorched origin and safe destination create an owner-managed movement cohort. Event 51 does not debit population separately.

## HW-VAL-056 Unsafe destination

A cooler destination with failed reception or food safety is rejected or deprioritized.

## HW-VAL-057 Trapped population feedback

Migration returns a demand receipt that raises local water and reception pressure once.

## HW-VAL-058 Wildfire request

A qualified state submits one Event 013 request. Event 013 owns damage and Air Cleanliness source.

## HW-VAL-059 No duplicate contamination

Wildfire smoke contributes once. Event 51 adds zero direct contamination.

# Evolution scenarios

## HW-VAL-060 Evolution disabled

Disabled evolution does not record, unlock content, or set a recorded flag.

## HW-VAL-061 Evolution I before onset

A new episode starts with lethal rules active but still respects exposure confirmation.

## HW-VAL-062 Evolution II mid-episode

Previously recorded exposure becomes eligible for evaluation without inventing days or applying instant terrain conversion.

## HW-VAL-063 Evolution III surge

Activation can expand the current ceiling and allow a new surge only when terminal decline has not completed.

## HW-VAL-064 Evolution log

Each stage appears in main and related evolution history with correct date, event, name, tier, and stage. Event Details preview shows no fake history data.

# Environmental scenarios

## HW-VAL-070 Warning before degradation

A state enters a visible warning stage and receives a mitigation opportunity before permanent change.

## HW-VAL-071 Fertile state restraint

A healthy fertile state cannot jump directly to desert in one ordinary episode.

## HW-VAL-072 Forest path

A forest loses resilience and vegetation before any valid dryland or desert transition.

## HW-VAL-073 Desert to wasteland

A desert state requires Evolution III, long Scorched exposure, failed mitigation, severe collapse, and cap availability.

## HW-VAL-074 Map-tool proof

Actual terrain change is implemented only after inspect, rewrite, compare, and rollback evidence. Missing route leaves the feature blocked and reported.

## HW-VAL-075 Permanent persistence

Degradation survives cleanup, save and reload, occupation, annexation, and liberation.

# Cluster and repeatability scenarios

## HW-VAL-080 Automatic cluster firing

Natural Disasters cluster starts Event 51 once, records one pacing transaction, and applies repeatable cap behavior.

## HW-VAL-081 Active cluster skip

Cluster skips Event 51 while active and records the reason while other members remain valid.

## HW-VAL-082 Later episode

After cleanup and sufficient weight recovery, Event 51 can fire again with new temporary state and inherited permanent damage.

# AI probability scenarios

Run all named scenarios from the AI spec through the required probability workflow.

Acceptance requires:

- no universal priority dominance
- valid action ordering
- zero score for invalid actions
- reserve protection
- state-target diversity
- same-scenario compare after patches

# Presentation and asset scenarios

## HW-VAL-090 Category clarity

At a glance, the player can identify intensity, national priority, hotspots, current mission, and useful actions.

## HW-VAL-091 Map clarity

Stress bands remain distinguishable without relying only on color. State selection shows cause and response.

## HW-VAL-092 Category animation

Every frame has real source art, stable composition, correct sheet dimensions, static fallback, and no transform-only motion.

## HW-VAL-093 Icon separation

Decision, state, idea, achievement, and category assets are separately designed for their surfaces.

## HW-VAL-094 Super-event

The Evolution III super-event fires once after the real milestone, uses matching image, text, quote, and unique audio, and does not apply duplicate damage.

# Achievement scenarios

Test each achievement for:

- genuine success
- one near miss
- voluntary state transfer exploit
- save and reload
- repeat episode behavior
- owner-system result use
- debug bypass where tracked

# Performance scenarios

## HW-VAL-100 Ordinary world

Run a full episode with normal country and state count. Record pulse cost and log volume.

## HW-VAL-101 Fragmented world

Run after major independence and civil-war events create many countries. Registered processing remains bounded.

## HW-VAL-102 Evolution III load

Several regions are Scorched, Migration and Famine are active, and report rate remains controlled.

## HW-VAL-103 Cleanup load

Cleanup removes all temporary records without one-frame whole-world mutation or stale arrays.

# Required audit routing

Before completion:

- event-chain MCP inspect, render, and compare
- decision and mission audit
- probability baseline and post-patch compare
- localisation audit
- completion audit
- map audit for terrain changes
- asset review and manifest reconciliation
- workbook update through spreadsheet worker
- user-run live validation for in-game behavior

# Completion evidence

The completion report should list:

- files changed
- final identifiers
- public values and thresholds
- decision and mission coverage
- evolution coverage
- adapter results
- Chaos non-duplication
- asset and audio status
- terrain proof or blocker
- AI scenario results
- meaningful validation findings
- simplifications or blockers

Passing generic syntax checks should not replace this evidence.
