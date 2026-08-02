# Biological Supply-Chain Sabotage

## Purpose

This subsystem covers covert biological sabotage of a selected state's combined public food, water, and medical distribution network. It provides one approved ordinary delivery surface for four distinct agents: exact-state timed covert decisions for espionage-style supply-chain penetration.

It is not battlefield dissemination. Battlefield delivery remains in `common/raids/biological_battlefield_raids.txt` and reuses the established military-raid icons. It is also separate from weaponized-zombie projects, operations, state records, AI, and outcomes. Japan's two accepted China-theater historical actions remain exact decisions in `common/decisions/japan_biological_campaign_decisions.txt`; the doomsday release remains a decision.

## Player flow

1. Complete the matching biological-agent project and establish an authenticated CBRN program.
2. Reach Operational Chemical Readiness and adopt a use policy that authorizes the selected foreign controller.
3. Choose the exact-state covert sabotage decision family. It selects the combined public network in one state and remains the lower-profile espionage route. Strategic and battlefield biological delivery continue to use their own raid surfaces.
4. Select one mutually exclusive timed preparation posture for the current doctrine posture. The decision reserves the exact agent payload model and required support equipment before preparation and allocates Command Power.
5. Maintain the exact actor, victim controller, selected state, policy, readiness, route, and agent context until the chosen surface resolves.
6. Resolve failure, limited success, success, or critical success. Limited and full releases enter `bio_lifecycle_dispatch_seed` through `bio_lifecycle_route.food_water_medical_sabotage`.

There are three timed covert decision variants per agent. Base, Theater Contamination, and Terminal Hazard preparation timing is exposed separately, while route-specific costs, evidence, and initial-dose handling remain distinct.

## Agent hierarchy and raid odds

Overall weapon potency is strictly `Tularemia < Anthrax < Plague < Smallpox`. Tularemia is low, Anthrax moderate, Plague serious, and only Smallpox is the severe ordinary weapon tier. The potency profile changes incubation, spread, contamination, medical pressure, deaths, and other lifecycle consequences after the native delivery result.

All twelve supply-chain decision variants use the same shared route result bands and the same agent-neutral delivery factors. Agent identity does not make Plague or Smallpox intrinsically easier or harder to deliver. Agent-specific AI preferences and target-fit weights are allowed to represent doctrine, history, and route selection, but they do not alter the route result.

The route's critical outcome is an operational delivery band, not a weapon-severity label. It does not make Anthrax or Plague severe. Only the separate Smallpox doomsday decision may submit the severe biological lifecycle result.

## Central tuning

Lifecycle, route, doctrine, and AI tuning remains centralized in `common/script_constants/biological_sabotage_constants.txt`, `common/script_constants/biological_lifecycle_constants.txt`, and `common/script_constants/biological_battlefield_constants.txt`.

| Agent | Payload | Support equipment | Command Power | Base / Theater / Terminal preparation |
|---|---:|---:|---:|---:|
| Anthrax | 10 | 40 | 12 | 160 / 136 / 120 days |
| Plague | 12 | 50 | 15 | 240 / 204 / 180 days |
| Tularemia | 10 | 40 | 12 | 180 / 153 / 135 days |
| Smallpox | 8 | 60 | 20 | 300 / 255 / 225 days |

The accepted matrix gives this route a 120-300-day preparation range, low initial attribution risk, and medium friendly-spread risk. The lifecycle route profile supplies the low initial dose, evidence, concealment, spread pressure, Condemnation base, incubation, deaths, contamination, and medical saturation after a proven release.

## Doctrine interaction

Theater Contamination and Terminal Hazard make sabotage easier and more aggressive by shortening preparation and cooldown, increasing downstream biological potency through the shared lifecycle, increasing AI willingness, and returning a bounded Command Power amount after a valid resolution.

Doctrine never reduces or refunds physical payload, support equipment, evidence, attribution, deaths, contamination, medical saturation, confirmed-use history, public-harm floors, or cancellation losses. Doctrine may reduce only the Condemnation impact. A rejected or cancelled raid receives no Command Power refund.

## Exact-state and accounting contract

The timed covert decision reserves the selected payload and support equipment in its committed ledger and rechecks relationship, controller, policy, readiness, program, agent profile, and target validity before dispatch. No replacement payload or alternate state is selected.

A failed outcome records failed-attempt evidence and attempted-use consequences without creating an outbreak. A limited or full outcome records the exact route and payload through the shared biological lifecycle. If the dispatch proof fails, the resolver records a rejected release and never fabricates a biological episode or equipment proof.

Cleanup preserves permanent attempt, resolution, equipment-consumption, evidence, attribution, history, and consequence records while avoiding a broad periodic scan.

## Failure, cancellation, and history

- A proven failure records low-confidence attempt evidence and hidden attempted-use Condemnation but no deliberate-use history.
- A limited, successful, or critical release records the exact route and payload through the shared lifecycle, which owns later detection, attribution, deaths, contamination, medical saturation, evidence escalation, Condemnation, and sanctions interaction.
- Decision preparation and resolution consume the committed payload and support equipment according to the decision ledger.
- A dispatcher rejection records failed-attempt evidence and hidden attempted-use Condemnation, applies cooldown, and grants no doctrine refund.
- The actor history stores the committed outcome, biological result, agent, selected state, and victim country for audit and AI use.

## AI behavior

AI uses the same readiness, policy, project, equipment, active-operation, cooldown, and state gates as the player. Decision weights distinguish retaliation, first use, unrestricted use, desperation, defensive profiles, domestic pathogen-handling preparation, doctrine, target-agent fit, Japan attacking Chinese states, active outbreak risk, and Condemnation plus import vulnerability. An actor at its own near-capitulation threshold does not choose ordinary sabotage; the separate doomsday decision remains the collapse route. The decision evaluates the exact proposed state; no target estimator or alternate-state search is retained.

## Files and identifiers

- Timed covert decision family: `common/decisions/biological_sabotage_decisions.txt` and `common/scripted_effects/biological_sabotage_effects.txt`
- Decision tuning and route triggers: `common/script_constants/biological_sabotage_constants.txt` and `common/scripted_triggers/biological_sabotage_triggers.txt`
- Shared lifecycle effects: `common/scripted_effects/biological_lifecycle_effects.txt`
- Retained historical decisions: `common/decisions/japan_biological_campaign_decisions.txt` and `common/decisions/chemical_warfare_decisions.txt`
- Retained Japan localisation and legacy icon strings: `localisation/english/biological_sabotage_l_english.yml`
- Strategic and battlefield raid map icons remain the existing `GFX_raid_type_icon_anthrax_strike`, `GFX_raid_type_icon_plague_strike`, `GFX_raid_type_icon_tularemia_strike`, and `GFX_raid_type_icon_smallpox_strike` definitions
- Existing decision icons retained for the Japan exceptions: `GFX_decision_bio_sabotage_anthrax`, `GFX_decision_bio_sabotage_plague`, `GFX_decision_bio_sabotage_tularemia`, and `GFX_decision_bio_sabotage_smallpox`
- Asset manifests: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/manifest.md` and the existing biological raid icon manifests

The raid map icons are owned by the existing strategic and battlefield biological raid interface definitions. The retained decision icons remain in `gfx/interface/decisions/biowarfare/` for the covert and Japan historical decisions and are not overwritten or deleted.

## Engine boundaries

HOI4 exposes a selected state and its controller, not native target objects for food depots, municipal water systems, or medical distribution chains. The selected state's combined public network is therefore the sabotage object. No unrelated building is damaged or used as a release proxy.

The timed covert decision surface stores exact actor, victim, state, preparation, equipment reservation, and outcome proof in its committed ledger. It does not expose a verified continuous-air activity callback, so no estimator or broad periodic fallback is retained. All biological sabotage helpers remain in biological-sabotage-specific files because their callers are the covert decision resolver and the narrow historical adapters.

## Future Stage 7 integration

The shared lifecycle already exposes active sabotage and discovered-outbreak state to the biological response decisions. Final package closure still requires cross-route scenarios, the mapped specialist audits, and final asset and documentation disposition. Those remaining checks do not change the exact-state delivery contract.
