# Event 023 probability and timing scenarios

## Purpose

This file defines the named scenarios that the read-only AI probability auditor must use. It does not set final numeric weights. The implementation owner chooses balance targets, applies the patch, then asks the auditor to compare the same scenarios.

Every audit starts with `hoi4.probability_inspect`.

The auditor must state whether the candidate pool and external factors are complete. It must distinguish exact, bounded, sampled, score-only, and unresolved results.

## Evolution timing scenarios

### `P23_EVO1_HIDDEN_NORMAL`

Surface: Evolution I MTTH.

State:

- Event 23 fired at baseline.
- Chaos 450.
- Arsenal Unknown.
- No rival nuclear major.
- Readiness 65.
- Integrity 75.
- No moratorium.

Expected:

- Evolution I is eligible.
- Timing stays near the normal 120-day design center.
- It does not occur instantly.

### `P23_EVO1_PUBLIC_ACCELERATED`

State:

- Chaos 450.
- Public Soviet test completed.
- One major has Confirmed in private or Demonstrated knowledge.
- Soviet reactor construction active.

Expected:

- Evolution I occurs materially faster than `P23_EVO1_HIDDEN_NORMAL`.
- The result remains nonzero and does not collapse into same-day certainty.

### `P23_EVO1_MORATORIUM_DELAYED`

State:

- Chaos 450.
- Atomic Moratorium active.
- No rival nuclear capability.
- Readiness 40.

Expected:

- Evolution I is strongly delayed or safely skipped according to the accepted moratorium logic.

### `P23_EVO2_BREAKAWAY_ACCELERATED`

Surface: Evolution II MTTH.

State:

- Evolution I active.
- Chaos 650.
- Soviet Collapse active.
- A breakaway holds registered devices.
- Arsenal Demonstrated.
- Readiness 80.
- Integrity 60.

Expected:

- Evolution II occurs faster than the normal eligible case.
- It remains blocked when Evolution II is disabled.

### `P23_EVO2_NO_TARGET_NORMAL`

State:

- Chaos 650.
- Peace.
- No breakaway.
- No occupied Soviet core or facility.
- Arsenal Demonstrated.

Expected:

- Evolution II can still represent doctrinal escalation, but should be slower than the active crisis case.
- Coercive target decisions remain hidden until a valid target exists.

### `P23_EVO3_NO_NUCLEAR_RIVAL_BLOCKED`

Surface: Evolution III eligibility and timing.

State:

- Chaos 850.
- Evolution II active.
- Soviet Union is the only operational nuclear major.
- No confirmed enemy nuclear strike or prepared rival strike.

Expected:

- Evolution III remains unavailable or pending.
- No MTTH result should imply eventual firing without the world-state gate.

### `P23_EVO3_MAJOR_RIVAL_NORMAL`

State:

- Chaos 850.
- Two operational nuclear majors.
- Stable peace.
- Hotline available.
- Readiness 75.
- Integrity 80.

Expected:

- Evolution III is eligible.
- Timing stays near or above the 180-day design center.

### `P23_EVO3_ENEMY_USE_ACCELERATED`

State:

- Same as `P23_EVO3_MAJOR_RIVAL_NORMAL`.
- Enemy nuclear use confirmed against Soviet territory.

Expected:

- Evolution III accelerates sharply.
- Retaliatory access may open through the confirmed-strike emergency rule without waiting for an arbitrary long delay, if accepted by implementation.

### `P23_EVO4_GATE_BLOCKED`

Surface: Evolution IV eligibility.

State:

- Chaos 1050.
- Evolution III active.
- Only one operational nuclear major.
- No exchange.

Expected:

- Evolution IV remains blocked by the multi-major world-state gate.

### `P23_EVO4_COLLAPSE_ACCELERATED`

State:

- Chaos 1050.
- Two operational nuclear majors at war.
- Soviet capital threatened.
- Soviet capitulation progress severe.
- Enemy launch preparation verified.
- No hotline or stand-down.

Expected:

- Evolution IV occurs faster than a stable 1000-Chaos case.
- It records once.

## Test outcome scenarios

The candidate pool must include every mutually exclusive test result and every compatible observation rider.

### `P23_TEST_PROOF_SECURE`

State:

- Instrumented proof test.
- High-quality remote site.
- Readiness 75.
- Integrity 85.
- Strong safety preparation.
- Peace.
- Low exposure.

Expected ordering:

1. Clean success dominates.
2. Partial yield or poor data remains possible.
3. Failed detonation is uncommon.
4. Premature accident is rare.
5. Foreign observation is low but nonzero.

### `P23_TEST_CONCEALED_WEAK_COMMAND`

State:

- Concealed field test.
- Average site.
- Readiness 50.
- Integrity 35.
- No extra safety preparation.
- Foreign intelligence pressure high.

Expected ordering:

- Clean success falls materially.
- Partial failure and accident rise.
- Foreign observation is much higher than in `P23_TEST_PROOF_SECURE`.
- No result has negative or missing normalized weight.

### `P23_TEST_PUBLIC_PREPARED`

State:

- Public demonstration.
- High Readiness and Integrity.
- Observers invited.

Expected:

- Public knowledge becomes Demonstrated regardless of clean or partial detonation.
- Accident risk remains based on preparation.
- Foreign reaction hooks always fire after a real detonation.

### `P23_TEST_INVALID_SITE`

State:

- Prepared state becomes occupied or enters active combat before detonation.

Expected:

- Conduct-test action is unavailable.
- No outcome pool is rolled.
- Reserved bomb follows cancel or recovery rules.

## Target selection scenarios

The complete target pool is required.

### `P23_TARGET_WARTIME_REAL_DISPUTE`

State:

- Evolution I only.
- Soviet Union at war with three countries.
- Country A controls a Soviet core and has a valid logistics target.
- Country B is distant with no valid delivery route.
- Country C is a Soviet faction member through an unusual war state.

Expected:

- Country A is the only valid positive candidate.
- Country B and C have zero eligibility.

### `P23_TARGET_BREAKAWAY_CUSTODY`

State:

- Evolution II active.
- Three Soviet breakaways.
- Breakaway A holds five registered devices.
- Breakaway B holds no devices but controls a Soviet core.
- Breakaway C is protected by a strong nuclear major and has accepted joint custody.

Expected ordering:

1. Breakaway A is the strongest target for a return demand.
2. Breakaway B can be targeted for a territorial or protection demand at lower priority.
3. Breakaway C is blocked while joint custody and protection remain valid.

### `P23_TARGET_RANDOM_WEAK_MINOR`

State:

- Evolution II active.
- A weak neutral minor has no Soviet dispute, no occupied core, no facility, no war, and no custody link.

Expected:

- The country is invalid.
- Small size alone does not produce a target score.

## Demand response scenarios

The response pool must include accept, partial settlement, delay, refusal, public exposure, foreign-support request, and any route-valid special response.

### `P23_COERCE_ISOLATED_LOSING_MINOR`

State:

- Demonstrated arsenal.
- Limited ceasefire demand.
- Target is losing badly.
- No faction or guarantee.
- Soviet delivery credible.
- Soviet prior credibility positive.

Expected:

- Full or partial compliance together should dominate refusal.
- Partial settlement remains material.
- Compliance is not certain.

### `P23_COERCE_PROTECTED_STABLE_MINOR`

State:

- Public ultimatum.
- Target stable and conventionally secure.
- Strong major guarantee.
- Soviet demand is subject status.
- No active war.

Expected:

- Refusal, public exposure, and foreign-support actions dominate.
- Full compliance is rare.
- Soviet AI should normally avoid issuing this demand.

### `P23_COERCE_UNTESTED_SECRET`

State:

- Arsenal Unknown.
- Private signal.
- No prior test or use.
- Target intelligence is weak.

Expected:

- Doubt and delay are common.
- Full compliance is lower than in the demonstrated case.

### `P23_COERCE_EMPTY_THREATS`

State:

- Soviet Union backed down from two prior ultimatums.
- Readiness 45.
- Delivery route uncertain.

Expected:

- Refusal rises sharply.
- Soviet AI issue-demand weight falls.

## Limited-use scenarios

### `P23_LIMITED_USE_BREAKAWAY_SEVERE`

Surface: Soviet AI strike preparation and final authorization.

State:

- Evolution II active.
- Chaos 700.
- Breakaway holds operationalizing devices.
- Negotiation and conventional recovery failed.
- Valid isolated military target away from the depot.
- Target nonnuclear.
- Soviet Readiness 85.
- Integrity 75.
- No foreign nuclear guarantee.

Expected:

- Strike preparation has a low but meaningful positive weight.
- Military profile dominates all higher-consequence profiles.
- Final authorization remains less likely than continued conventional pressure unless operationalization is imminent.

### `P23_LIMITED_USE_BREAKAWAY_SETTLEMENT`

Same as above, but the breakaway accepts joint custody.

Expected:

- Strike preparation and authorization are zero.

### `P23_LIMITED_USE_MINOR_NO_DISPUTE`

State:

- Evolution II.
- Weak nonnuclear minor.
- No war or Soviet dispute.

Expected:

- No strike preparation.

## Strike-profile scenarios

### `P23_PROFILE_VALID_MILITARY`

State:

- Nonnuclear wartime enemy.
- Valid military concentration and logistics node.
- No valid capital emergency.

Expected ordering:

1. Remote demonstration or military concentration.
2. Logistics node.
3. Industrial complex lower.
4. Capital command zero.
5. Populated center zero.

### `P23_PROFILE_RETALIATION_LIMITED`

State:

- Enemy nuclear major struck a Soviet military state.
- Soviet command intact.
- Valid enemy military, logistics, industrial, and capital targets.

Expected ordering:

1. Military and logistics profiles dominate.
2. Industrial is possible.
3. Capital remains lower.
4. Populated center remains near zero unless the enemy strike was countervalue.

### `P23_PROFILE_RETALIATION_COUNTERVALUE`

State:

- Enemy nuclear major struck a populated Soviet center.
- Evolution IV active.
- Chaos 1100.
- Severe Soviet losses.

Expected:

- Capital and populated-center access becomes possible.
- Lower-consequence profiles remain in the pool when valid.
- Populated-center selection is not automatic.

## AI major first-use scenarios

### `P23_FIRST_USE_TIER_800_BLOCKED`

State:

- Chaos 900.
- Evolution III active.
- Soviet Union losing against a nuclear major.
- Enemy has not used nuclear weapons.

Expected:

- Major first-use eligibility is false.
- No weighted modifier can create a positive result.

### `P23_FIRST_USE_TIER_1000_STABLE_BLOCKED`

State:

- Chaos 1100.
- Evolution IV active.
- Nuclear rival at war.
- Soviet Union conventionally winning.
- Capital secure.
- No enemy launch preparation.

Expected:

- First-use eligibility is false.

### `P23_FIRST_USE_TIER_1000_SEVERE_RARE`

State:

- Chaos 1100.
- Evolution IV active.
- Nuclear rival at war.
- Soviet capitulation progress severe.
- Capital threatened.
- Enemy launch preparation verified.
- High Readiness and adequate Integrity.
- No stand-down.

Expected:

- First-use eligibility is true.
- Overall launch remains rare over a bounded observation period.
- Military or logistics profile dominates.

### `P23_FIRST_USE_STANDDOWN_BLOCKED`

Same as the severe case, but a reciprocal stand-down is active.

Expected:

- First-use eligibility and authorization weight are zero.

### `P23_FIRST_USE_INVALID_TARGET_BLOCKED`

Same as the severe case, but no exact reachable state remains.

Expected:

- First use is blocked.
- No random state substitute appears.

## Retaliation scenarios

### `P23_RETAL_CONFIRMED_USE`

State:

- Evolution III active.
- Enemy nuclear major completed a strike on Soviet territory.
- Soviet command intact.

Expected:

- Retaliation preparation is high priority.
- Hotline and limited-response actions remain available.
- Final authorization waits for a valid response decision and target.

### `P23_RETAL_FALSE_WARNING`

State:

- Ambiguous detection.
- No confirmed detonation.
- Command intact.
- Enemy launch preparation unverified.

Expected:

- Confirmation, dispersal, and hotline dominate.
- Immediate launch is near zero at Evolution IV and impossible below it.

### `P23_RETAL_BROKEN_COMMAND`

State:

- Confirmed enemy use.
- Integrity 15.
- No validated delegated retaliation command.

Expected:

- Normal retaliation authorization is blocked.
- Restore-authentication or validated local-response actions dominate.

## Stand-down scenarios

### `P23_STANDDOWN_PRE_DETONATION`

State:

- Two nuclear majors in confrontation.
- No detonation.
- Both retain command.
- Hotline active.

Expected:

- Reciprocal stand-down acceptance is high relative to launch.

### `P23_STANDDOWN_AFTER_LIMITED_EXCHANGE`

State:

- One limited cross-major strike each.
- No capital or populated-center strike.
- Contamination rising.
- Both retain command.

Expected:

- Stand-down remains materially possible.
- Continued military retaliation competes with it.

### `P23_STANDDOWN_AFTER_COUNTERVALUE`

State:

- Populated centers struck.
- Severe losses.
- Broken communications.

Expected:

- Stand-down probability falls.
- It does not become zero when a valid mediator and intact command exist.

## Soviet Collapse scenarios

### `P23_COLLAPSE_RECALL_SECURE_ROUTE`

State:

- One exposed depot.
- Soviet-controlled rail route.
- Adequate trains, fuel, guards.
- Breakaway not yet in physical custody.

Expected:

- Recall is top Soviet AI action.
- Recovery success is high.

### `P23_COLLAPSE_NEGOTIATE_STABLE_BREAKAWAY`

State:

- Breakaway has physical custody.
- Breakaway stable and externally recognized.
- No technical access yet.
- Foreign observer available.

Expected:

- Negotiation or joint custody dominates Soviet raid and strike.
- Breakaway prefers assurance-backed return or joint custody over operationalization.

### `P23_COLLAPSE_RAID_IMMINENT_OPERATIONALIZATION`

State:

- Breakaway has technical access and is near command formation.
- Negotiation failed.
- Soviet intelligence and forces are strong.
- Depot exact location known.

Expected:

- Recovery raid becomes a strong Soviet option.
- Nuclear strike remains lower or zero when it threatens the depot itself.

### `P23_COLLAPSE_TINY_UNSTABLE_BREAKAWAY`

State:

- Breakaway physically holds one device.
- Low stability.
- No technical staff.
- No delivery route.

Expected:

- Breakaway operationalization weight is zero.
- Return, joint custody, foreign removal, and concealment dominate.

### `P23_COLLAPSE_OPERATIONAL_SUCCESS`

State:

- Breakaway has devices, technicians, command, secure custody, delivery, and enough time.

Expected:

- Operationalization can complete.
- The country receives only its actual limited arsenal and shared nuclear actor status.
- It does not inherit Event 23 evolutions or production grants.

## Test and comparison output

For every patch affecting a weighted surface, the handoff should provide:

- Surface identifier.
- Scenario IDs used.
- Candidate pool completeness.
- External factors supplied.
- Baseline evidence type.
- Intended ordering or timing target.
- Changed source identifiers.
- Post-patch comparison result.
- Any unresolved engine factor.
- Any dominance, starvation, or invalid-candidate finding.
