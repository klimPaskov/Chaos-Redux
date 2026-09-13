# Decision and Mission Implementation Prompt for Event 052 Intel Leaked

Implement and audit the Event 52 Intelligence Compromise decision and mission system according to the complete specification and `matrices/052_intel_leaked_decision_and_mission_map.md`.

Read `AGENTS.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, the installed offline Decision Modding references, current vanilla documentation, and existing Chaos Redux precedents before editing.

## Player-facing structure

Use one ordinary decision category with a static category picture and concise dynamic header.

Show one persistent value, Exposure, from 0 to 100 with the five specified qualitative stages.

Show active archive domains through compact icons or short labels. Keep Archive Depth, Archive Confidence, Personnel Risk arithmetic, recipient Reliance, and exploitation scores hidden.

Expose three to five primary actions per phase. Six is the hard maximum during a brief transition. Keep active missions between one and three.

Do not print raw variables, pipe-separated telemetry, internal ledgers, or long trigger blocks.

## Required action families

Implement every valid action and its phase replacement behavior:

- Replace Codes and Authentication Tables
- Recall Exposed Personnel
- Rewrite Compromised Plans
- Shut Down Vulnerable Channels
- Rebuild Cover Identities
- Reconstitute Foreign Networks where supported
- Compartmentalize the Archive
- Restore Trusted Liaison Channels
- Seed Contradictory Orders
- Poison the Leak
- Stage a False Deployment
- Trace the Source

Write final localisation from the specification direction. Working labels may be changed while preserving action meaning.

## Cost and sacrifice model

Each action can use at most four spendable cost types.

Use costs that fit the action, including command power, relevant military experience, support equipment, fuel, civilian factory burden, operative time, agency capacity, lost network strength, cancelled operations, tied formations, readiness disruption, or time.

Do not implement the category as Political Power purchases.

Every displayed cost needs the matching texticon. Requirements remain separate from costs. Use concise custom trigger tooltips for dynamic domains, targets, partners, units, fleets, regions, operations, and blocked reasons.

Costs and durations scale from country size, war state, active domains, Exposure, agency strength, affected assets, and evolution profile. Centralize tuning.

## Required missions

Implement:

- Archive Freshness
- Personnel at Risk
- Emergency Replan
- Deception Window

Each mission requires distinct success, partial-success where mapped, failure, cancellation, target-invalid, and cleanup behavior.

Archive Freshness is the target's dynamic incident deadline.

Personnel at Risk must resolve through protective action or one bounded severe failure. It must not roll against every operative in a cascade.

Emergency Replan must ask for a real change in the relevant military posture. Name or highlight the state, port, sea area, air region, or domain. Avoid passive stockpile checklists.

Deception Window must require a coherent selected false posture and a relevant high-Reliance recipient. Tied units, fleets, aircraft, fuel, or transport commitments must remain real until success, failure, or cancellation.

## DLC compatibility

The category must remain complete without agency mechanics.

Agency-only actions hide when unsupported. The base path retains broad intelligence exposure, military replanning, code replacement, generic personnel security, channel shutdown, archive reform, foreign exploitation, Trace the Source, and deception.

Do not show empty agency decisions or generic copies that do nothing.

## AI behavior

Target AI must prioritize current danger, mission deadlines, affordability, agency strength, war state, invasion risk, expected Exposure reduction, and operational sacrifice.

A weak service should recall and close channels. A strong service should preserve selected networks and use deception. A country under invasion should replan before investing in long-term archive reform.

Every weighted decision and mission surface requires the named AI probability scenario workflow. Establish a baseline with `chaosx_ai_probability_auditor`, apply the owner-approved patch, then run `hoi4.probability_compare` against the same scenarios.

## Cleanup and exploit prevention

- One-shot actions cannot be farmed without a new proven tranche.
- Compartmentation resilience has a cap.
- Costs cannot be charged after a target becomes invalid.
- Selected partners and deception targets clear when invalid.
- Cancelling a false-deployment mission cannot produce success.
- Save and reload cannot duplicate completion, cost, Exposure reduction, or failure.
- AI cannot click hidden, unsupported, unaffordable, or target-invalid actions.
- Multi-target Total Compromise maintains separate categories and target state.
- Incident closure removes every event-owned decision, mission, reserved target, and temporary cost commitment.

## Mandatory specialist audit

After implementation, route the final category through `chaosx_decision_mission_auditor` with a self-contained prompt and no inherited context.

The audit must cover:

- action quality
- phase visibility
- cost variety and four-cost limit
- texticons and blocked tooltips
- mission objectives and timing
- success, partial success, and failure separation
- DLC behavior
- AI validity
- cleanup
- target invalidation
- exploit risk
- impact strength
- category clutter

Resolve every finding or record an explicit blocker before Event 52 completion.
