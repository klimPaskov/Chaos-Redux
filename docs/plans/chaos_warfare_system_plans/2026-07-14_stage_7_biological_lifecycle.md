# Stage 7: Biological Lifecycle, Delivery, Safety, and Countermeasures

Status: in progress. The overall Chaos Warfare goal remains incomplete.

Disposition: partially implemented and still active. The completed tranche below is implemented. All remaining acceptance work stays queued in this plan.

## Accepted design and boundaries

This stage implements numbered specification 06, the biological-agent countermeasure matrix, the shared-consequence requirements in specifications 01 and 09, and the biological portions of the coding, decision, AI, asset, and completion prompts. Conflicts resolve in that order.

Biological warfare is not chemical exposure with a longer modifier. Anthrax, plague, tularemia, and smallpox each retain distinct incubation, detection, spread, lethality, persistence, treatment, evidence, and friendly-blowback behavior. Weaponized zombies remain on their own projects, operations, outbreak state, AI policy, and world-threat path. Ordinary pathogens may share only generic death, evidence, Condemnation, and cleanup adapters with zombies.

Chaos Warfare doctrine is an escalation path. Theater Contamination and Terminal Hazard may increase biological seed potency, intensity growth, spread pressure, deaths, duration, medical saturation, preparation speed, and aggressive AI willingness. They may ease deployment through bounded preparation savings or a bounded Command Power refund after a resolved operation. Terminal Hazard may reduce Condemnation after attribution, subject to public-harm floors. Condemnation is the only consequence record doctrine may reduce. Doctrine may not reduce physical payload debit, evidence, attribution, deaths or death history, contamination or contamination history, medical saturation or medical history, confirmed-use history, domestic war-support penalties, biological-use counters, accident risk already incurred, accident records, resistance trauma, or public-harm floors.

Doctrine cannot create, reveal, authorize, or unlock camps, extermination sites, experiment sites, restricted chemical sites, or generic concentration laws. Any separately authorized interaction with an existing camp system is limited to raising its already resolved killing efficiency. It cannot alter that system's evidence, discovery, responsibility, resistance, trauma, Condemnation, or historical records.

No broad `on_daily`, `on_weekly`, or `on_monthly` biological pass is permitted. A seeded state owns its delayed incubation and outbreak events. Spread schedules only the exact newly exposed state. A stale delayed event checks its agent flag and exits without rescheduling. No estimator, proxy release, neutral condition substitute, or silent fallback is allowed.

## Current tranche ledger

Implemented in the current strategic biological tranche:

- `common/on_actions/chaosx_on_actions_biowarfare.txt` is absent. Legacy startup and weekly calls to `initialize_smallpox_vaccination_protection`, `progress_smallpox_vaccination`, and `check_all_states_for_contamination_cleanup` are absent.
- `smallpox_vaccination_program_idea` has no legacy `on_add` or `on_remove` state-scan hooks. The ordinary lifecycle reads the country idea directly when applying agent-specific growth, spread, and death multipliers.
- `bio_lifecycle_cleanup_state_response_if_no_ordinary_episode` owns exact-state response cleanup after recovery. It clears field hospitals, quarantine, stale legacy protection state, and the quarantine modifier only when no ordinary biological episode remains in that state.
- Strategic biological raids use the exact native selected state, exact payload reservation and debit, six biological outcomes, state-owned incubation and lifecycle ticks, and no continuous-air contamination.
- `GFX_decision_bio_designate_strategic_raid_staging_state` is registered in `interface/biological_warfare.gfx` and resolves to the final staging decision DDS.
- The existing raid icons under `gfx/interface/military_raids/` remain byte-preserved and are reused by the four strategic biological raids.

Still queued under this active plan:

- Every Stage 7 route, facility choice, countermeasure, asset, localisation surface, AI profile, migration caller, audit finding, and package scenario that lacks completion evidence in the acceptance sections below.
- Final Stage 7 and full CBRN completion review. Neither is established by this tranche.

## Persistent state model

Each ordinary pathogen owns an independent state record so concurrent agents can coexist:

- lifecycle flags for incubating, active, detected, contained, and tick scheduled
- intensity from 0 to 100, with isolated, local, serious regional, severe multi-state, and catastrophic bands
- exposed share, cumulative deaths, evidence, attribution state, medical saturation, mutation pressure, and episode dates
- route, source type, repeated-seed count, and a scope-valued responsible-country variable when a real actor exists
- one Condemnation-release marker per attribution threshold so delayed discovery cannot double-charge
- one Air Cleanliness contribution marker per material outbreak band so the same transition cannot double-register
- cleanup that removes modifier variables and transient flags but preserves deaths, confirmed-use, evidence history, and episode history.

An agent-state record is one aggregate outbreak episode. Repeated seeding raises intensity, exposed share, evidence, and repeated-seed pressure. If another responsible country supplies stronger current evidence, that country becomes the active attribution lead. Weaker evidence cannot overwrite a stronger lead.

## Shared biological seed contract

Every deliberate delivery route must prepare one normalized temporary action record before calling the state seed dispatcher:

- exact agent
- exact target state
- exact actor and victim when deliberate
- route and source type
- payload required, payload consumed, and positive debit proof
- seed intensity and exposed share
- evidence, concealment, weaponization quality, safety, and friendly-spread risk
- route outcome: failed, partial, successful, catastrophic, accident, spread, or doomsday.

Deliberate release is rejected unless the exact state, actor, agent, and positive payload debit are proven. Natural spread, laboratory accident, captured-facility release, and doomsday use have separate explicit source contracts and may not pass through a fabricated deliberate actor. Failed delivery can record attempt evidence and capture consequences but cannot seed an outbreak unless a defined accident outcome releases material.

The seed dispatcher performs this order:

1. Validate the route-specific record and debit proof.
2. Apply actor doctrine to potency, spread, deaths, duration, and medical pressure, but not evidence.
3. Store or strengthen the independent agent-state record.
4. Schedule that agent's incubation event if no tick is already scheduled.
5. Record attempt/use history without declaring an outbreak before detection.
6. Defer civilian deaths, active modifiers, attribution release, Condemnation, and Air Cleanliness contribution until their lifecycle thresholds occur.

## Event-owned lifecycle

### Incubation and detection

- Incubation delay comes from the agent profile and route outcome.
- Surveillance, medical infrastructure, field epidemiology, density, war damage, chaos, concealment, and agent difficulty determine detection pressure.
- Undetected states may suffer ambiguous medical and military pressure without revealing the agent, actor, exact intensity, or deliberate origin to the player.
- Detection reveals only the supported stage and response choices. Evidence advances attribution from unknown natural through suspicious and probable deliberate to confirmed attack.

### Progression, deaths, and containment

- Every active agent schedules its own weekly state event.
- Growth reads density, state category, infrastructure, war damage, adjacent active outbreaks, route pressure, repeated seeding, global Air Cleanliness thresholds where the accepted design calls for them, and actor doctrine.
- Decline reads quarantine, field hospitals, antibiotics, vaccination, border closure, surveillance, containment capacity, medical response, international aid, and agent decay.
- Weekly deaths use the matrix's agent and intensity bands, the current exposed share, treatment, medical response, and a cumulative per-agent state-population cap. Each interval is registered exactly once through the shared Deaths adapter.
- Active modifiers are recalculated from intensity and countermeasures. Tularemia keeps the strongest military disruption identity, anthrax the strongest persistent local burden, plague the strongest rapid connected spread, and smallpox the longest incubation and highest strategic catastrophe risk.
- Cleanup ends the scheduler only when intensity and exposed share reach the defined recovery threshold. It preserves all historical ledgers.

### Spread

- Spread attempts occur only from an active agent tick.
- The source state may target an exact adjacent state and, where a verified route exists, a connected occupied or foreign state.
- Border closure and quarantine reduce only eligible cross-border or local spread. They do not erase an already seeded state.
- The target receives the same agent with source type `spread`, reduced seed intensity, inherited strain evidence, and no fabricated attacker. If the source has a responsible-country record, that record is copied as the attribution lead without increasing evidence by doctrine.

## Route migration

- Strategic biological raids reserve and consume the exact agent payload, select an exact state, and resolve failed, partial, hidden, detected, successful, and attacker-accident outcomes before seeding.
- Operative planting covers all four ordinary agents and separates acquire, transport, infiltration, release/abort, and capture. Captured operatives provide confirmed attribution and coverup consequences.
- Battlefield dissemination requires readiness, policy, selected agent, prepared headquarters, route equipment, and payload. It applies troop, supply, friendly, occupied-population, and front-spread risk.
- Food, water, and medical-chain sabotage uses a covert low-dose seed with uncertain initial attribution and severe later discovery consequences.
- Doomsday release requires the explicit route, extreme policy, near-capitulation or world-end conditions, a real arsenal, and a domestic-risk warning. It consumes the arsenal, seeds own and nearby fronts, records maximum evidence, and harms allies and the user.

Every caller of a legacy `apply_*_contamination` identifier is migrated to an exact route adapter and the legacy identifiers are then removed. No permissive compatibility wrapper remains. A route adapter is valid only when it can supply every required actor, victim, agent, route, result, target-state, and debit proof directly from the current engine scope.

## Program safety, facilities, and countermeasures

- Biosecurity, surveillance, containment capacity, medical response, weaponization quality, attribution control, and mutation pressure are explicit country values derived from real technologies, projects, facilities, choices, damage, and current measures.
- Cautious, accelerated, dispersed, centralized, and human-experimentation development choices trade time, safety, evidence, deaths, and facility risk. Human experimentation always creates atrocity and coverup exposure. It is never a free research bonus.
- Accident checks are invoked only by project milestones, production/stockpile thresholds, bombing, sabotage, facility capture, and unsafe handling. They are not MTTH background pulses.
- Captured facilities allow secure, destroy, preserve-evidence, and accidental-release outcomes. Biosecurity Assault reduces risk. Experiment-site discovery adds separate atrocity and coverup Condemnation.
- Surveillance, quarantine, field hospitals, antibiotics, vaccination, border closure, and international missions have real costs, duration, AI, cancellation, and cleanup. They act on the exact affected state or connected country path.

## Assets and presentation

Stage 7 requires type-correct final assets for the biological decision category, surveillance, investigation, quarantine, field hospital, antibiotics, vaccination, border closure, international mission, laboratory safety, stockpile-risk bands, captured facility, four agent outbreak states, four delivery routes, accident reports, attribution reports, and biological achievements. Sprite IDs must be registered before art production. Source PNG, processed PNG, DDS, manifest, contact sheet, and GFX handoff are mandatory. No placeholder or resized cross-type substitute is accepted.

Final localisation must describe uncertainty in-world, hide exact incubation and attribution values until discovered, show dynamic costs and response effects, and keep zombies visibly separate from ordinary disease warfare.

## Stage acceptance evidence

- Four independent agent-state lifecycle scenarios prove distinct incubation, detection, spread, deaths, treatment, persistence, and cleanup.
- Multiple ordinary agents can coexist in one state without overwriting each other's modifiers, actor records, evidence, death caps, or schedulers.
- Every deliberate route proves exact payload debit before seeding and reaches the same dispatcher.
- No global biological daily, weekly, or monthly pass remains, and the Chaos Meter daily state scan no longer calculates ordinary biological outbreak deaths.
- Deaths, Air Cleanliness, evidence, attribution, Condemnation, sanctions, confirmed-use history, and medical saturation each register once at the correct lifecycle transition.
- Doctrine raises biological operational harm and reduces only Condemnation after attribution, with public-harm floors intact.
- Countermeasures have agent-specific effects and tradeoffs from the accepted matrix.
- Stockpile accidents are event-triggered, facilities can be captured, and human experimentation has atrocity consequences.
- Weaponized zombies share no ordinary payload, spread, project, AI, or world-threat path.
- Route-aware AI uses the same payload, safety, policy, readiness, targeting, retaliation, and consequence gates as the player.
- Decision, localisation, asset, scripted-system, improvement-loop, package-scenario, and completion audits have no unresolved findings.

Stage 7 cannot close while any route, facility choice, countermeasure, asset, localisation surface, AI profile, migration caller, audit finding, or package scenario remains unresolved.
