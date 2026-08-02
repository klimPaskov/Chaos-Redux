# Event 016 static balance matrix handoff

Date: 2026-08-02

## Scope

This is a parent-owned static balance pass for Event 016. It reads the live Event 016 script constants and stage loaders, derives transparent timing, capacity, cost, force, foreign-operation, formation, and world-threat bounds, and records what still requires campaign observation. It does not launch Hearts of Iron IV, change gameplay, produce a model, or claim whole-event balance completion.

## Source contract

- `common/script_constants/016_brilliant_scientist_constants.txt` supplies visible and hidden measure bands, project capacity, stage baselines, family profiles, family durations, evolution factors, and formation or force limits.
- `common/script_constants/016_brilliant_scientist_foreign_constants.txt` supplies operation gates, costs, clocks, scoring, detection, network bands, and AI option weights.
- `common/script_constants/016_brilliant_scientist_super_event_constants.txt` supplies formation, world-threat, defeat, and singularity threshold inputs.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` and `016_brilliant_scientist_evolution_effects.txt` supply the active-stage capacity refresh and sovereignty-deadline formulas.
- `docs/specs/016_brilliant_scientist_specs/acceptance/016_balance_and_exploit_review.md` remains the acceptance authority for campaign observations that this static pass cannot provide.

## Fixed state bands

All four visible Directorate meters and both hidden causal meters are clamped to `0..100`. Public appointment starts at Mandate `65`, Dependence `25`, Exposure `20`, Capacity `30`, Independent Capacity `15`, and Grievance `5`. Secret appointment starts at Mandate `45`, Dependence `45`, Exposure `10`, Capacity `35`, Independent Capacity `5`, and Grievance `15`. The public route therefore begins with stronger authority and lower dependence, while the secret route begins with five additional capacity points but materially worse hidden governance posture.

The visible active-stage burdens are Theory `10`, Prototype `20`, Deployment `35`, and Weaponization `50`. A suspended project retains half of its burden. With only the public or secret opening capacity, the host can hold one Prototype plus one Theory (`30`) or (`35`), but cannot hold two Prototypes (`40`) or one Weaponization plus a Prototype (`70`) without capacity decisions, facilities, or route rewards. Two Weaponization projects require `100`, which is the global capacity ceiling before suspension or dismantling.

## Stage-time envelope

The following sums are the constant stage durations for a family from Theory through Weaponization. They are arithmetic envelopes, not AI completion forecasts, and they exclude pauses, incidents, foreign actions, facility construction, and capacity decisions.

| Family | Theory | Prototype | Deployment | Weaponization | Full stage sum |
| --- | ---: | ---: | ---: | ---: | ---: |
| Computation | 120 | 180 | 270 | 360 | 930 days |
| Electronics | 120 | 210 | 300 | 390 | 1,020 days |
| Materials | 150 | 240 | 330 | 420 | 1,140 days |
| Rocketry | 180 | 270 | 390 | 540 | 1,380 days |
| High Energy | 240 | 360 | 540 | 720 | 1,860 days |
| Biomedical | 150 | 240 | 330 | 450 | 1,170 days |
| Teleportation | 240 | 360 | 540 | 720 | 1,860 days |
| Cloning | 210 | 330 | 480 | 660 | 1,680 days |
| Robotics | 180 | 300 | 450 | 600 | 1,530 days |
| Paleogenetics | 210 | 330 | 480 | 660 | 1,680 days |
| Xenobiological Synthesis | 240 | 390 | 570 | 750 | 1,950 days |
| Biological Weapons | 180 | 300 | 450 | 600 | 1,530 days |
| Alien Arms | 270 | 420 | 600 | 780 | 2,070 days |
| Temporal | 360 | 540 | 720 | 900 | 2,520 days |
| Strategic Singularity | 720 | 900 | 1,080 | 900 | 3,600 days |

The fastest ordinary full route is Computation at `930` stage days, while the slowest is Strategic Singularity at `3,600` stage days. The evolution MTTH base is `90` days for each prefire and active interval; the live factors range from stabilization `1.35` to active crisis `0.65`, before public or secret posture, meter, project, context, and chaos modifiers are combined by the existing MTTH helper.

## Project-capacity and production pressure

Stage capacity is intentionally more restrictive than the global ceiling. Deployment plus Theory consumes `45`, Deployment plus Prototype consumes `55`, and Weaponization plus Theory consumes `60`. These combinations force the player to suspend, dismantle, or expand the Directorate rather than keeping every route active. The stage cost baselines rise from one civilian factory and `50` political power at Theory to six civilian and five military factories and `150` political power at Weaponization, with support equipment, trucks, trains, fuel, manpower, XP, and resource units increasing at each stage. Family profiles make High Energy, Teleportation, Alien Arms, Temporal, and Singularity the most factory- or resource-intensive paths; Computation and Biomedical remain cheaper on factories but still charge real manpower or equipment.

## Foreign-operation envelope

Foreign operations are gated at interest values `20/30/35/40/45/55/65/75` for observation, invitation, joint laboratory, protection, theft, sabotage, extraction, and assassination. The defined political-power costs range from `15` for observation to `100` for an assassination attempt. Operation clocks run from `30` to `90` days, incoming operations are capped at two per host, and each actor can run one live operation. Success chance is bounded to `5..90`, detection to `5..95`, and network bands are `25/50/75`. Security, exposure, intelligence, diplomacy, and prior operation history alter score and detection through the central constants rather than an unbounded random bonus.

## Formation and world-threat bounds

Formation routes require at least two origin states for charter or enclave, three for rebellion, and four for multi-site or takeover routes. The route score floors are Enclave `45`, Charter `55`, Rebellion `70`, and Takeover or multi-site `90`; takeover additionally requires Dependence `90`, Control below `30`, at least three warning incidents, four captured domains, one statewide domain, and one sovereign science authority. This keeps a one-state weak enclave from inheriting the full country package.

The shared world-threat threshold requires score `12`, six controlled states, fifteen factories, three deployed project families, four weaponized families, three distinct opponents, and one major opponent. High-threat presentation uses fifteen states, thirty-five factories, five deployed families, and the same major-opponent gate. The late Singularity branch requires four components before it can satisfy the late-construction check. The Singularity constants separately define six components, `720`-day component research, `1,080`-day core construction, `720`-day delivery construction, and `365`-day arming, so the terminal weapon has an explicit multi-year race even after its project-stage ledger is advanced.

## Project-derived force envelope

The conventional cap is `12` formations. Route-specific caps are Clone `8`, Robot `8`, Paleogenetic `6`, Xenobiological `6`, Portal `4`, Temporal `3`, Exotic `4`, and Biological `4`. Theory produces no force, Prototype scales at `0.25`, Deployment at `0.60`, and Weaponization at `1.00`; equipment delivery is bounded to `50..100%` and the maximum spawn ratio is `0.50`. These constants preserve causal distinction between project families and prevent a theory-only project from creating an unsupported army.

## Scenario projections

| Scenario | Static projection from current constants | Remaining campaign observation |
| --- | --- | --- |
| Small peaceful public host | Starts with capacity `30`, enough for Theory plus Prototype; the public mandate and low dependence make a safe settlement plausible if the player avoids early high-burden branches. | Research-speed timeline, AI project selection, incident frequency, and settlement probability. |
| Wartime major secret host | Starts with capacity `35` and lower exposure, but higher dependence and grievance; military or energy families fit the intended tradeoff but their factory and fuel profiles are heavier. | Secret-route research lead, foreign-action frequency, and whether +100% research speed becomes automatic victory. |
| Project-rich rebellion | Formation score and force caps scale with controlled territory, independent capacity, grievance, and project stage; no unit is granted by the formation transaction itself. | Former-host counterplay, supply, force-production rate, and rebellion outcome distribution. |
| Weak enclave | Enclave has the lowest route score floor and still needs two origin states; force caps remain project-derived rather than country-size free units. | Survival time, corridor or patron decisions, and whether a one-state start has viable counterplay. |
| Evolution IV global threat | The threat requires multiple deployed or weaponized families, opponents, territory, and factories; Singularity detonation remains behind the shared world-end threshold and Fallout pipeline. | Weak/normal/dominant Singularity timing, coalition intervention, and disarmament success. |

## Disposition

This handoff supplies reproducible static bounds and exposes the main pressure points for future tuning. It does not satisfy the acceptance review's required campaign observations, AI completion rates, force-production samples, rebellion distributions, or live terminal scenarios. No gameplay change is proposed from this pass; all seven 3D entity packages remain deferred.

