# CBRN biological program AI

## Purpose

The biological program AI selects ordinary-agent projects and production from the country's actual CBRN posture, protection, conventional supply, completed projects, containment technology, designated-arsenal risk, and explicit use route.

It also applies differentiated country profiles from `common/ai_strategy/cbrn_country_profiles.txt`. Britain prioritizes meteorology, filtration, wash columns, sampling, and medical response; France and the Soviet Union weight chemical-artillery and field-response support; Germany weights armored delivery and sealed containment; the United States weights sampling, medical response, and fail-safe containment; Italy weights artillery and field response; Japan weights the exact China biological route and its containment, epidemiology, and hospital prerequisites; and secondary profiles favor protection and outbreak response according to their industrial and geographic exposure.

It never grants free payload, treats a country tag as authorization, researches locked project-output technology directly, infers a safe arsenal from missing data, or substitutes a decision for ordinary strategic or battlefield raid delivery.

Weaponized zombies remain outside this selector.

## Project selection

The four ordinary-agent special projects use the country-scope gates in `common/scripted_triggers/cbrn_ai_posture_triggers.txt`.

1. Every normal first project requires Pathogen Handling Protocols, Rapid Outbreak Response, at least eight Military Factories, no conventional infantry, support, artillery, or motorized reserve deficit, a stable mask and countermeasure base, and an accepted biological posture.
2. A battlefield program chooses Tularemia as its first project.
3. A retaliatory, strategic, or exact desperate program chooses Anthrax as its first project.
4. A strategic or exact desperate program may advance from Tularemia or Anthrax to Plague.
5. Smallpox requires a completed Plague project and either an explicit desperate-release route or an unrestricted major-power strategic program with at least twenty Military Factories, Fail-Safe Containment Facilities, and a Controlled or Strained arsenal.
6. Every project after the first requires a complete current designated-arsenal risk context.
7. Dangerous or Critical risk stops normal project escalation and permits it only through the exact desperate-release route.

Japan's China campaign delegates to `japan_bio_campaign_route_is_open`, which requires the accepted Pingfang, Ishii-authority, China-war, policy, readiness, security, and attribution conditions.

That campaign selects Anthrax first and Plague second.

Japan receives no tag-only preference for Tularemia, Smallpox, or any ordinary raid.

## Production selection

`common/ai_strategy/biological_warfare_production.txt` uses the native `equipment_production_surplus_management` strategy with exact equipment models.

Vanilla evaluates this strategy only after ordinary equipment needs are met and weighs its value against other surplus equipment types.

The normal generic selector maintains one strongest route-appropriate family:

| Program state | Payload family |
| --- | --- |
| Battlefield route with only Tularemia completed | Tularemia |
| Retaliatory or early strategic route with Anthrax completed | Anthrax |
| Strategic route with Plague but no Smallpox | Plague |
| Unrestricted fail-safe strategic route with Smallpox | Smallpox |

The Japan-China selector can maintain both Anthrax and Plague because its separate historically mapped campaign actions consume those exact families.

The desperate selector maintains only the strongest completed family and is the sole production branch permitted during Dangerous or Critical arsenal risk.

Every production strategy stops at its file-local stock target and aborts immediately when its route, containment, protection, supply, industry, project-output technology, or exact risk gate no longer passes.

No generic infantry-equipment production factor is used because the biological models currently share the infantry equipment type and a category-wide factor would also affect unrelated infantry equipment.

The profile strategy also gives CBRN regimental roles different preferences after the existing exact template gates pass. Defensive profiles favor protected infantry and containment, artillery profiles favor chemical artillery, assault profiles favor chemical assault and armored delivery, the United States favors containment, and Japan's China profile favors chemical assault, armored delivery, and containment. These are AI composition preferences only; the unsupported current-version Army-HQ target receipt remains fail-closed.

## Potency and delivery odds

The accepted ordinary-agent potency order is Tularemia, Anthrax, Plague, then Smallpox.

`common/script_constants/biological_lifecycle_constants.txt` records severity ranks one through four plus strictly increasing weapon-strength, weekly-death, death-cap, and medical-pressure values.

Growth, detection, environmental persistence, and transmissibility remain distinct epidemiological profiles rather than being forced into one monotonic ladder.

Only Smallpox is the severe ordinary agent.

Agent identity does not alter native ordinary-raid delivery probability.

All four strategic raids use the same `@BIO_RAID_AI_MIN_SUCCESS_CHANCE` and byte-identical `success_factors` block, including the success, critical-success, and disaster factors.

All four battlefield raids use the same `@BIO_BATTLEFIELD_AI_MIN_SUCCESS_CHANCE` and byte-identical `success_factors` block.

Their different payload reservations, preparation costs, lifecycle profiles, countermeasures, deaths, contamination, evidence, and Condemnation remain consequences or logistics, not delivery-odds modifiers.

## Interactions and safety boundaries

- `bio_stockpile_safety_risk_context_is_valid` owns exact arsenal-state validity.
- Controlled or Strained risk permits normal project and payload expansion.
- Dangerous or Critical risk stops normal production and escalation.
- `cbrn_ai_has_desperate_release_posture` is the only risk override and still requires an exact risk context after the first completed project.
- `cbrn_ai_has_stable_protective_base` requires real masks, decontamination equipment, CBRN instruments, and a refreshed non-shortage protection ledger.
- `cbrn_ai_has_conventional_army_deficit` pauses offensive expansion before ordinary army supply is sacrificed.
- Special-project completion grants the exact delivery technology that enables the exact payload model.
- Ordinary strategic and battlefield deployment remains on the raid surfaces.
- Ordinary covert food, water, and medical supply-chain sabotage uses both the native exact-state land-raid category and the separate exact-state timed covert-decision family with agent-and-doctrine variants; it does not replace either ordinary strategic or battlefield raid surface. The two historically scoped Japan-China actions and biological doomsday release remain decisions.
- Historically precise Japan-China campaign releases remain targeted decisions.
- Biological doomsday release remains a decision.
- An unrestricted actor under formal censure receives a continuation preference only when a current enemy has reached the exact near-victory surrender threshold.
- An actor at its own near-capitulation threshold stops choosing ordinary strategic raids, battlefield raids, covert sabotage, operative release, and Japan-China campaign actions.
- An explicitly authorized doomsday route leaves the doomsday decision as the sole biological release choice during collapse.
- A collapsing actor without that route strongly prefers exact stockpile destruction instead of continued release.

No daily, weekly, monthly, all-country, or all-state pulse is introduced by this AI layer.

## Engine limits

The native surplus-management strategy is a relative weight used after normal equipment needs are met.

It does not expose a guaranteed military-IC percentage contract, so the specification's biological production shares are implemented as bounded relative surplus weights and stock targets rather than presented as exact percentage allocations.

This is an engine-native tuning limit, not an estimator or fallback.

The currently connected HOI4 inspection transport was unavailable during the project-selector audit, so source validation used installed current-version documentation, vanilla AI strategies, current project-output technology definitions, and exact mod references.

No unsupported project or production behavior was added to compensate for the unavailable inspection transport.

## Assets and wiring

This AI layer adds no player-facing asset.

It reuses the existing ordinary biological project, equipment, and raid icons, including the existing runtime raid assets under `gfx/interface/military_raids`.

No icon was overwritten, replaced with a placeholder, or resized across asset types.

## Future integration and suggestions

Required Stage 10 follow-up:

- finish event-driven regimental template adoption and removal while preserving exact stock and unlock gates;
- connect the offensive chemical template gates to an exact target receipt once the Stage 6 chemical delivery adapter exposes one;
- finish the exact operation target-country and relationship audit within the native operation interface;
- complete the historically sourced designer-identity audit and confirm the differentiated profile weights against the package scenarios;
- run the seven-major and three-minor scenario matrix after those consumers are complete;
- carry completed headquarters, countermeasure, sanction-response, and collapse behavior through the final Stage 10 audit.
