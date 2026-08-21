# Biological Supply-Chain Sabotage

## Purpose

This subsystem preserves the ledger and cleanup contract for the retired generic supply-chain decision family. New covert ordinary-agent deployment uses the four native operative operations, which select one exact state without filling the decision view with one card per eligible state.

It is not battlefield dissemination. Battlefield delivery remains in `common/raids/biological_battlefield_raids.txt` and reuses the established military-raid icons. It is also separate from weaponized-zombie projects, operations, state records, AI, and outcomes. Japan's two accepted China-theater historical actions remain exact decisions in `common/decisions/japan_biological_campaign_decisions.txt`; the doomsday release remains a decision.

## Active player routes

- Strategic and battlefield deployment use native raid surfaces.
- Covert ordinary-agent deployment uses the native operative operations.
- Japan's bounded China-theater actions remain exact-state decisions.
- Doomsday release remains a decision.

The twelve legacy supply-chain decisions cannot list new targets. Their identifiers, exact-state ledger, resolver, and cleanup helpers remain only so an already committed record can end safely.

## Agent hierarchy and raid odds

Overall weapon potency is strictly `Tularemia < Anthrax < Plague < Smallpox`. Tularemia is low, Anthrax moderate, Plague serious, and only Smallpox is the severe ordinary weapon tier. The potency profile changes incubation, spread, contamination, medical pressure, deaths, and other lifecycle consequences after the native delivery result.

All ordinary-agent strategic and battlefield raids use agent-neutral native delivery factors. Agent identity does not make Plague or Smallpox intrinsically easier or harder to deliver. Agent-specific AI preferences and target-fit weights may represent doctrine, history, and route selection, but they do not alter the route result.

The route's critical outcome is an operational delivery band, not a weapon-severity label. It does not make Anthrax or Plague severe. Only the separate Smallpox doomsday decision may submit the severe biological lifecycle result.

## Migration tuning

Lifecycle, route, doctrine, and AI tuning remains centralized in `common/script_constants/biological_lifecycle_constants.txt` and the route-specific raid and operation constants. `common/script_constants/biological_sabotage_constants.txt` remains migration-only tuning for committed legacy records.

| Agent | Payload | Support equipment | Command Power | Base / Theater / Terminal preparation |
|---|---:|---:|---:|---:|
| Anthrax | 10 | 40 | 12 | 160 / 136 / 120 days |
| Plague | 12 | 50 | 15 | 240 / 204 / 180 days |
| Tularemia | 10 | 40 | 12 | 180 / 153 / 135 days |
| Smallpox | 8 | 60 | 20 | 300 / 255 / 225 days |

These values apply only if an already committed legacy record is loaded. They do not create a new player-facing route.

## Legacy doctrine interaction

Theater Contamination and Terminal Hazard make sabotage easier and more aggressive by shortening preparation and cooldown, increasing downstream biological potency through the shared lifecycle, increasing AI willingness, and returning a bounded Command Power amount after a valid resolution.

Doctrine never reduces or refunds physical payload, support equipment, evidence, attribution, deaths, contamination, medical saturation, confirmed-use history, public-harm floors, or cancellation losses. Doctrine may reduce only the Condemnation impact. A rejected or cancelled legacy operation receives no Command Power refund.

## Legacy exact-state and accounting contract

An already committed timed decision preserves its selected payload and support equipment in the ledger and rechecks relationship, controller, policy, readiness, program, agent profile, and target validity before dispatch. No replacement payload or alternate state is selected.

A failed outcome records failed-attempt evidence and attempted-use consequences without creating an outbreak. A limited or full outcome records the exact route and payload through the shared biological lifecycle. If the dispatch proof fails, the resolver records a rejected release and never fabricates a biological episode or equipment proof.

Cleanup preserves permanent attempt, resolution, equipment-consumption, evidence, attribution, history, and consequence records while avoiding a broad periodic scan.

## Legacy failure, cancellation, and history

- A proven failure records low-confidence attempt evidence and hidden attempted-use Condemnation but no deliberate-use history.
- A limited, successful, or critical release records the exact route and payload through the shared lifecycle, which owns later detection, attribution, deaths, contamination, medical saturation, evidence escalation, Condemnation, and sanctions interaction.
- Decision preparation and resolution consume the committed payload and support equipment according to the decision ledger.
- A dispatcher rejection records failed-attempt evidence and hidden attempted-use Condemnation, applies cooldown, and grants no doctrine refund.
- The actor history stores the committed outcome, biological result, agent, selected state, and victim country for audit and AI use.

## AI behavior

AI cannot select the retired generic decision family. Active raids, operative operations, Japan's historical decisions, and doomsday release retain their own route-aware gates and weights. No target estimator or alternate-state search is retained.

## Files and identifiers

- Migration-only decision identifiers and resolvers: `common/decisions/biological_sabotage_decisions.txt`, `common/scripted_effects/biological_sabotage_effects.txt`, `common/script_constants/biological_sabotage_constants.txt`, and `common/scripted_triggers/biological_sabotage_triggers.txt`
- Shared lifecycle effects: `common/scripted_effects/biological_lifecycle_effects.txt`
- Retained historical decisions: `common/decisions/japan_biological_campaign_decisions.txt` and `common/decisions/chemical_warfare_decisions.txt`
- Retained migration localisation and Japan icon strings: `localisation/english/biological_sabotage_l_english.yml`
- Strategic and battlefield raid map icons remain the existing `GFX_raid_type_icon_anthrax_strike`, `GFX_raid_type_icon_plague_strike`, `GFX_raid_type_icon_tularemia_strike`, and `GFX_raid_type_icon_smallpox_strike` definitions
- Existing decision icons retained for the Japan exceptions and stable migration references: `GFX_decision_bio_sabotage_anthrax`, `GFX_decision_bio_sabotage_plague`, `GFX_decision_bio_sabotage_tularemia`, and `GFX_decision_bio_sabotage_smallpox`
- Asset manifests: `docs/assets/chaos_warfare_system/stage_7_biological_warfare/food_water_medical_sabotage/manifest.md` and the existing biological raid icon manifests

The raid map icons are owned by the existing strategic and battlefield biological raid interface definitions. The retained decision icons remain in `gfx/interface/decisions/biowarfare/` for the Japan historical decisions and stable migration references and are not overwritten or deleted.

## Engine boundaries

HOI4 exposes a selected state and its controller, not native target objects for food depots, municipal water systems, or medical distribution chains. The selected state's combined public network is therefore the sabotage object. No unrelated building is damaged or used as a release proxy.

The migration resolver stores exact actor, victim, state, preparation, equipment reservation, and outcome proof in its committed ledger. New records cannot be created. All biological sabotage helpers remain in biological-sabotage-specific files because their remaining callers are the legacy resolver and narrow historical adapters.

## Status

The generic state-card surface is closed. The shared lifecycle continues to expose active incidents and discovered outbreaks to biological response decisions, while current covert use is handled by native operative operations.
