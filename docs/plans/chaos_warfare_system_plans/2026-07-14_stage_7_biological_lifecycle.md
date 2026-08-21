# Stage 7: Biological Lifecycle, Delivery, Safety, and Countermeasures

## Later surface correction

The generic twelve-decision supply-chain tranche described below is retired from player and AI access because native state-target decisions create one card per eligible state. Its identifiers and exact ledger remain migration-only. Active covert ordinary-agent deployment uses the four native operative operations; strategic and battlefield delivery remain raids; Japan's historically bounded actions and doomsday release remain decisions.

Status: in progress. The overall Chaos Warfare goal remains incomplete.

Disposition: partially implemented and still active. The completed tranche below is implemented. All remaining acceptance work stays queued in this plan.

## Accepted design and boundaries

This stage implements numbered specification 06, the biological-agent countermeasure matrix, the shared-consequence requirements in specifications 01 and 09, and the biological portions of the coding, decision, AI, asset, and completion prompts. Conflicts resolve in that order.

Biological warfare is not chemical exposure with a longer modifier. Anthrax, plague, tularemia, and smallpox each retain distinct incubation, detection, spread, lethality, persistence, treatment, evidence, and friendly-blowback behavior. Weaponized zombies remain on their own projects, operations, outbreak state, AI policy, and world-threat path. Ordinary pathogens may share only generic death, evidence, Condemnation, and cleanup adapters with zombies.

Chaos Warfare doctrine is an escalation path. Theater Contamination and Terminal Hazard may increase biological seed potency, intensity growth, spread pressure, deaths, duration, medical saturation, preparation speed, and aggressive AI willingness. They may ease deployment through bounded preparation savings or a bounded Command Power refund after a resolved operation. Terminal Hazard may reduce Condemnation after attribution, subject to public-harm floors. Condemnation is the only consequence record doctrine may reduce. Doctrine may not reduce physical payload debit, evidence, attribution, deaths or death history, contamination or contamination history, medical saturation or medical history, confirmed-use history, domestic war-support penalties, biological-use counters, accident risk already incurred, accident records, resistance trauma, or public-harm floors.

Doctrine cannot create, reveal, authorize, or unlock camps, extermination sites, experiment sites, restricted chemical sites, or generic concentration laws. Any separately authorized interaction with an existing camp system is limited to raising its already resolved killing efficiency. It cannot alter that system's evidence, discovery, responsibility, resistance, trauma, Condemnation, or historical records.

No broad `on_daily`, `on_weekly`, or `on_monthly` biological pass is permitted. A seeded state owns its delayed incubation and outbreak events. Spread schedules only the exact newly exposed state. A stale delayed event checks its agent flag and exits without rescheduling. No estimator, proxy release, neutral condition substitute, or silent fallback is allowed.

## Current tranche ledger

Implemented in the completed strategic-raid, operative-release, battlefield-dissemination, and covert-sabotage tranches:

- `common/on_actions/chaosx_on_actions_biowarfare.txt` is absent. Legacy startup and weekly calls to `initialize_smallpox_vaccination_protection`, `progress_smallpox_vaccination`, and `check_all_states_for_contamination_cleanup` are absent.
- `smallpox_vaccination_program_idea` has no legacy `on_add` or `on_remove` state-scan hooks. The ordinary lifecycle reads the country idea directly when applying agent-specific growth, spread, and death multipliers.
- `bio_lifecycle_cleanup_state_response_if_no_ordinary_episode` owns exact-state response cleanup after recovery. It clears field hospitals, quarantine, stale legacy protection state, and the quarantine modifier only when no ordinary biological episode remains in that state.
- Strategic biological raids use the exact native selected state, exact payload reservation and debit, six biological outcomes, state-owned incubation and lifecycle ticks, and no continuous-air contamination.
- `GFX_decision_bio_designate_strategic_raid_staging_state` is registered in `interface/biological_warfare.gfx` and resolves to the final staging decision DDS.
- The existing raid icons under `gfx/interface/military_raids/` remain byte-preserved and are reused by the four strategic biological raids.
- Four native operative-release operations cover Anthrax, Plague, Tularemia, and Smallpox with exact selected-state profiles, distinct preparation time, operatives, network requirements, native non-refundable payload and support-equipment costs, and abort, partial, or full resolution.
- Partial and full operative releases enter `bio_lifecycle_dispatch_seed` through the private `operative_release` route. The operation engine exposes no runtime debit amount, so this route does not fabricate numeric payload proof or payload history.
- Exact operative captures use the current operation token, assigned country, and positive assigned state. A matching live episode confirms attribution; otherwise each actual capture records a confirmed no-release attempt without weapon-use history. No timer, periodic search, inferred state, or operation-instance proxy is used.
- Operative AI applies policy and route gates, defensive-profile suppression, domestic-safety preference, and agent-specific target-country profiles. Native AI cannot rank the eventual selected state, and no estimator is retained.
- Theater Contamination and Terminal Hazard increase success and refund 2 or 4 Command Power once after resolution while leaving equipment, evidence, history, deaths, and physical consequences intact.
- `docs/plans/chaos_warfare_system_plans/2026-07-16_stage_7_operative_release_validation.md` records the bounded source and scenario audit for this tranche.
- Four native exact-state land raids cover Anthrax, Plague, Tularemia, and Smallpox battlefield dissemination. Deployment is never a decision click. Each raid uses a supply-node origin, one assigned infantry, motorized, or mechanized formation, native essential-equipment reservation, and all four current raid result callbacks.
- A valid active Combined CBRN Overmatch command proves theater authorization and preparation. The native selected state and assigned formation prove release context. Current-version scripting exposes no exact HQ-to-selected-state link or raid launch callback, so no inferred state, estimator, proxy, or fallback is retained.
- Failure loses the complete reservation and records attempt evidence without completed-use history. Releasing outcomes enter the same ordinary lifecycle through the private `battlefield_dissemination` route. A successful primary dispatch may create one bounded adjacent friendly connected-spread seed without a second payload debit or deliberate-use record.
- Battlefield doctrine raises biological harm and friendly-blowback risk while refunding only bounded Command Power after valid resolution. Payload, evidence, attribution, deaths, contamination, saturation, history, and public-harm floors remain intact; only Condemnation may be reduced.
- Battlefield raids reuse the existing Anthrax, Plague, Tularemia, Smallpox, and biological-category military-raid DDS assets byte-for-byte. Generated decision-icon drafts are not wired to this route.
- `docs/plans/chaos_warfare_system_plans/2026-07-18_stage_7_battlefield_dissemination_validation.md` records the bounded source and scenario audit for this tranche.
- Twelve exact-state timed covert decisions cover Anthrax, Plague, Tularemia, and Smallpox sabotage of the selected state's combined public food, water, and medical network. Twelve internal variants preserve the agent-and-doctrine preparation matrix while using the committed decision ledger; strategic and battlefield biological delivery remain on their dedicated raid surfaces.
- Decision preparation and Command Power cost consume the exact agent model and `support_equipment_1` through the committed ledger. Partial and full callbacks enter the ordinary lifecycle through the private `food_water_medical_sabotage` route; failure, abort, and invalid context never create release or completed-use history. The two Japan-China historical exceptions remain exact decisions.
- A complete actor, victim, state, agent, equipment, Command Power, doctrine, and cooldown ledger is required before failed-attempt evidence, hidden Condemnation, or cancellation history can be written. Invalid records receive no refund and create no substituted state or fabricated attempt record.
- Doctrine keeps preparation inside 120–300 days, raises release success and downstream harm, shortens cooldown, and refunds bounded Command Power only after a valid resolution. Physical equipment debit, evidence, attribution, deaths, contamination, saturation, historical records, and public-harm floors remain intact.
- Route-aware sabotage AI evaluates policy route, retaliation, desperation, domestic program safety, agent-specific state evidence, Japan-China context, and sanctions vulnerability. Defensive profiles and existing outbreak risk suppress use.
- The four final type-specific sabotage decision icons remain registered in `interface/biological_warfare.gfx` for the timed covert family and Japan-China exceptions. Strategic and battlefield biological raids retain the existing Anthrax, Plague, Tularemia, and Smallpox raid icons byte-for-byte; no existing raid icon or Chaos Redux runtime asset was overwritten.
- `docs/plans/chaos_warfare_system_plans/2026-07-19_stage_7_biological_sabotage_validation.md` records the bounded source and scenario audit for this tranche.
- The ordinary countermeasure tranche provides national Medical Capacity, Biological Security, surveillance, exact-state field hospitals, quarantine, agent-specific antibiotics, Smallpox vaccination, exact bilateral border closures, international medical missions, and four exact-state containment durations with full, partial, and failed outcomes.
- Weapon potency is strictly `Tularemia < Anthrax < Plague < Smallpox`; only Smallpox is classified as severe. The four strategic biological raids continue to use the same success, critical, and disaster factors, so delivery reliability remains independent from post-release harm.
- Medical teams and treatment services reserve exact capacity at dispatch, store their provider on the selected state, prevent parallel overcommit, and return capacity exactly once after failed arrival, agent recovery, program stand-down, mission resolution, or final state cleanup. Consumed equipment is not refunded.
- Public agent-threat gates read exact local detection or per-agent global confirmed-use history written at the real confirmed-attribution transition. Secret foreign projects do not leak through response decisions.
- International assistance uses existing inspection or observer access and bounded allied or outward-guaranteed country scopes. It does not scan the world, infer an inverse guarantee, fabricate a donor, or maintain a relationship proxy.
- Ten unique final decision icons and two unique final idea icons are registered in `interface/biological_countermeasures.gfx`; existing field-hospital and Smallpox decision sprites are reused without overwriting any military-raid asset.
- The current decision source exposes 25 timed mission AI surfaces and three immediate decision AI surfaces to the installed probability adapter, with zero unresolved inputs.
- `docs/plans/chaos_warfare_system_plans/2026-07-24_stage_7_biological_countermeasure_validation.md` records the bounded source, asset, AI, cleanup, and migration evidence for this tranche.
- Project field tests now remain at the exact active special-project facility. Every ordinary agent uses the same containment-accident probability, while the shared lifecycle applies the agent-specific potency and consequence profile after a real containment failure.
- Unsupported legacy biological callers have been removed instead of translated into permissive adapters: UWR focus completion no longer selects and contaminates a random neighboring state, the Chaos Assault Battalion has no passive outbreak roll, and abstract camp killing methods no longer seed an ordinary outbreak episode.

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
- route-specific payload authority: numeric required/consumed/proof for script-debited routes, or the private native operation cost for `operative_release`
- seed intensity and exposed share
- evidence, concealment, weaponization quality, safety, and friendly-spread risk
- route outcome: failed, partial, successful, catastrophic, accident, spread, or doomsday.

Deliberate release is rejected unless the exact state, actor, agent, and route-specific payload authority are proven. The operative-release route is accepted only through its private native operation path; its exact `equipment` block and `return_on_complete = no` own the debit because the engine exposes no runtime amount to script. No temporary amount or proof is fabricated. Natural spread, laboratory accident, captured-facility release, and doomsday use have separate explicit source contracts and may not pass through a fabricated deliberate actor. Failed delivery can record attempt evidence and capture consequences but cannot seed an outbreak unless a defined accident outcome releases material.

The seed dispatcher performs this order:

1. Validate the route-specific record and debit authority.
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
- Battlefield dissemination is four native exact-state land raids, not a decision family. It requires readiness, policy, the matching agent project and payload, a valid active Combined CBRN Overmatch command, a supply-node origin, and an assigned infantry, motorized, or mechanized formation. Native failure records the lost attempt; all releasing outcomes enter the shared lifecycle and may create bounded adjacent friendly spread.
- Ordinary food, water, and medical-chain sabotage uses twelve exact-state timed covert decisions. Each reserves and consumes the real agent payload and support equipment through the committed decision ledger and applies Command Power once; partial and full releases use the private low-dose route with uncertain initial attribution and severe later discovery consequences. Invalid or aborted decisions cannot receive doctrine refunds or fabricate release history. The two Japan-China historical actions remain decisions.
- Doomsday release requires the explicit route, extreme policy, near-capitulation or world-end conditions, a real arsenal, and a domestic-risk warning. It consumes the arsenal, seeds own and nearby fronts, records maximum evidence, and harms allies and the user.

Every valid caller of a legacy `apply_*_contamination` identifier is migrated to an exact route adapter, while invalid random, passive, or abstract callers are removed. The legacy identifiers are then removed and no permissive compatibility wrapper remains. A route adapter is valid only when it can supply every required actor, victim, agent, route, result, target-state, and route-specific debit authority directly from the current engine scope.

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
- Every deliberate route proves its exact payload authority before seeding and reaches the same dispatcher; native operations use their non-refundable operation cost without a fabricated runtime amount.
- No global biological daily, weekly, or monthly pass remains, and the Chaos Meter daily state scan no longer calculates ordinary biological outbreak deaths.
- Deaths, Air Cleanliness, evidence, attribution, Condemnation, sanctions, confirmed-use history, and medical saturation each register once at the correct lifecycle transition.
- Doctrine raises biological operational harm and reduces only Condemnation after attribution, with public-harm floors intact.
- Countermeasures have agent-specific effects and tradeoffs from the accepted matrix.
- Stockpile accidents are event-triggered, facilities can be captured, and human experimentation has atrocity consequences.
- Weaponized zombies share no ordinary payload, spread, project, AI, or world-threat path.
- Route-aware AI uses the same payload, safety, policy, readiness, targeting, retaliation, and consequence gates as the player.
- Decision, localisation, asset, scripted-system, improvement-loop, package-scenario, and completion audits have no unresolved findings.

Stage 7 cannot close while any route, facility choice, countermeasure, asset, localisation surface, AI profile, migration caller, audit finding, or package scenario remains unresolved.
