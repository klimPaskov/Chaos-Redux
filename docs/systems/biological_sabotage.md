# Biological Supply-Chain Sabotage

## Purpose

This subsystem covers covert biological sabotage of a selected state's combined public food, water, and medical distribution network. It is a timed state-targeted decision family for the four ordinary agents: Anthrax, Plague, Tularemia, and Smallpox.

It is not battlefield dissemination. Battlefield delivery remains exclusively in `common/raids/biological_battlefield_raids.txt` and reuses the established military-raid icons. It is also separate from weaponized-zombie projects, operations, state records, AI, and outcomes.

## Player flow

1. Complete the matching biological-agent project and establish an authenticated CBRN program.
2. Reach Operational Chemical Readiness and adopt a use policy that authorizes the selected foreign controller.
3. Select one eligible foreign state. The state profile differs by agent: durable industrial or logistics networks for Anthrax, dense urban networks for Plague and Smallpox, and troop or supply concentrations for Tularemia.
4. Commit Political Power, the exact agent payload model, `support_equipment_1`, and Command Power. Equipment and Command Power are debited immediately.
5. Maintain the exact actor, victim controller, selected state, policy, readiness, and agent context until the timer resolves.
6. Resolve failure, partial release, or full release. Partial and full releases enter `bio_lifecycle_dispatch_seed` through `bio_lifecycle_route.food_water_medical_sabotage`.

There is one visible action per agent. Three mutually exclusive internal variants supply base, Theater Contamination, or Terminal Hazard preparation timing without exposing duplicate doctrine buttons.

## Central tuning

All costs, timings, success bands, cooldowns, AI weights, and history increments are in `common/script_constants/biological_sabotage_constants.txt`.

| Agent | Payload | Support equipment | Command Power | Base / Theater / Terminal preparation |
|---|---:|---:|---:|---:|
| Anthrax | 10 | 40 | 12 | 160 / 136 / 120 days |
| Plague | 12 | 50 | 15 | 240 / 204 / 180 days |
| Tularemia | 10 | 40 | 12 | 180 / 153 / 135 days |
| Smallpox | 8 | 60 | 20 | 300 / 255 / 225 days |

The accepted matrix gives this route a 120–300-day preparation range, low initial attribution risk, and medium friendly-spread risk. The lifecycle route profile supplies the low initial dose, evidence, concealment, spread pressure, Condemnation base, incubation, deaths, contamination, and medical saturation after a proven release.

## Doctrine interaction

Theater Contamination and Terminal Hazard make sabotage easier and more aggressive by shortening preparation and cooldown, increasing success, increasing downstream biological potency through the shared lifecycle, increasing AI willingness, and returning a bounded 3 or 6 Command Power after a valid resolution.

Doctrine never reduces or refunds physical payload, support equipment, evidence, attribution, deaths, contamination, medical saturation, confirmed-use history, public-harm floors, or cancellation losses. A rejected or cancelled operation receives no Command Power refund. Condemnation remains the only consequence record doctrine may reduce.

## Exact-state and accounting contract

The selected state stores the actor, victim controller, agent, payload required and consumed, support equipment required and consumed, Command Power cost and possible refund, cooldown, and start date. A country flag and scope-valued active-state record prevent concurrent sabotage operations by one actor.

The full release validator rechecks exact state, controller, actor, relationship, policy, readiness, current agent episode, all material debits, and the doctrine record. A weaker committed-attempt validator may write only failed-attempt evidence, hidden Condemnation, cancellation history, and cooldown when every original debit and scope pointer remains provable. It never authorizes release.

If exact context cannot be proven, the operation cleans up without selecting another state, inferring a victim, creating an outbreak, fabricating equipment proof, or returning Command Power. The initial Political Power click can be lost if context changes between the UI availability check and immediate commitment revalidation; no material ledger is created in that race.

## Failure, cancellation, and history

- A proven ordinary failure records low-confidence attempt evidence and hidden attempted-use Condemnation but no deliberate-use history.
- A partial or full release records the exact route and payload through the shared lifecycle, which owns later detection, attribution, deaths, contamination, medical saturation, evidence escalation, Condemnation, and sanctions interaction.
- Cancellation loses all committed payload, support equipment, and Command Power. It records attempt history only while the committed ledger remains exact.
- A dispatcher rejection after a valid timed resolution records failed-attempt evidence and hidden attempted-use Condemnation, applies cooldown, and grants no doctrine refund; it does not fabricate a release.
- Cleanup removes transient operation fields while preserving permanent attempt, resolution, equipment-consumption, evidence, and consequence history.

## AI behavior

AI uses the same readiness, policy, project, equipment, active-operation, cooldown, and state gates as the player. Weights distinguish retaliation, first use, unrestricted use, desperation, defensive profiles, domestic pathogen-handling preparation, doctrine, target-agent fit, Japan attacking Chinese states, active outbreak risk, and Condemnation plus import vulnerability. The decision engine evaluates the exact proposed state; no target estimator or alternate-state search is retained.

## Files and identifiers

- Decisions: `common/decisions/biological_sabotage_decisions.txt`
- Tuning: `common/script_constants/biological_sabotage_constants.txt`
- Private triggers: `common/scripted_triggers/biological_sabotage_triggers.txt`
- Private effects: `common/scripted_effects/biological_sabotage_effects.txt`
- Localisation: `localisation/english/biological_sabotage_l_english.yml`
- Sprites: `interface/biological_warfare.gfx`
- Final DDS: `gfx/interface/decisions/biowarfare/decision_bio_sabotage_{anthrax,plague,tularemia,smallpox}.dds`
- Asset manifest: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/manifest.md`

The four sprite identifiers are `GFX_decision_bio_sabotage_anthrax`, `GFX_decision_bio_sabotage_plague`, `GFX_decision_bio_sabotage_tularemia`, and `GFX_decision_bio_sabotage_smallpox`. Each icon visually emphasizes one compromised chain, while every decision mechanically represents the selected state's combined food, water, and medical network.

## Engine boundaries

HOI4 exposes a selected state and its controller, not native target objects for food depots, municipal water systems, or medical distribution chains. The accepted state-targeted decision therefore treats the selected state's combined public network as the sabotage object. No unrelated building is damaged or used as a release proxy.

The system needs no periodic on action, dynamic helper registry entry, continuous-air activity hook, scripted GUI, target estimator, or compatibility wrapper. All helpers remain in biological-sabotage-specific files because their only callers are this decision family.

## Future Stage 7 integration

Later accepted Stage 7 work should expose active sabotage and discovered outbreak records in the final CBRN overview, include this route in cross-route package scenarios, and connect completed countermeasure and international-response content to the resulting lifecycle episode. Those surfaces remain Stage 7 requirements; they are not substitutes for this route's current exact-state implementation.
