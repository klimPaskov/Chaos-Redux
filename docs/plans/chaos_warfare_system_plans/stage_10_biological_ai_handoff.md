# Stage 10 biological program AI handoff

Handoff date: 2026-07-26.

This is a partial Stage 10 handoff for ordinary biological project selection and payload production.

Stage 10 remains incomplete until regimental templates, the final operation audit, country profiles, designers, and the full scenario matrix are finished.

## Implemented files

- `common/scripted_triggers/cbrn_ai_posture_triggers.txt`
  - Adds exact route, first-project, escalation-risk, agent-selection, and safe-versus-desperate production gates.
- `common/scripted_triggers/cbrn_scripted_triggers.md`
  - Documents the subsystem-private CBRN AI interfaces and their fail-closed scope contracts without adding them to the shared dynamic-trigger registry.
- `common/special_projects/projects/biowarfare_main_projects.txt`
  - Replaces generic tag, government, factory, war, and strength-ratio weights for Anthrax, Plague, Tularemia, and Smallpox with route-aware gates.
- `common/ai_strategy/biological_warfare_production.txt`
  - Adds exact-model normal, Japan-China, and desperate biological payload surplus strategies.
- `docs/systems/cbrn_biological_ai.md`
  - Records the implemented selector, potency and delivery-odds boundary, engine behavior, asset boundary, and remaining Stage 10 integration.
- `docs/plans/chaos_warfare_system_plans/stage_10_biological_ai_handoff.md`
  - This handoff.

## Project route matrix

| Project | Normal first-project route | Escalation prerequisite | Additional hard gate |
| --- | --- | --- | --- |
| Tularemia | Non-Japanese battlefield program | None | No retaliatory, strategic, or desperate posture |
| Anthrax | Non-Japanese retaliatory or strategic program; exact Japan-China campaign; exact desperate route | None | Normal routes require the stable protection and containment foundation |
| Plague | Non-Japanese strategic program; exact Japan-China campaign; exact desperate route | Tularemia or Anthrax, with Japan's China campaign specifically requiring Anthrax | Complete current arsenal-risk context |
| Smallpox | Unrestricted major strategic program or exact desperate route | Plague | Normal route requires Fail-Safe Containment, safe risk, and at least twenty Military Factories |

The first project does not require an arsenal-risk snapshot because no completed ordinary project has created a designated arsenal.

Every later project requires exact current risk proof.

Controlled or Strained risk permits normal expansion.

Dangerous or Critical risk permits escalation only through the explicit desperate-release route.

Missing or stale arsenal state fails closed.

## Production route matrix

| Route | Exact model selection | Stop conditions |
| --- | --- | --- |
| Battlefield | Tularemia until a stronger route-appropriate completed family exists | Target stock reached, route lost, conventional deficit, protection failure, containment failure, or unsafe risk |
| Retaliatory | Anthrax until Plague or Smallpox supersedes it | Same normal gates |
| Strategic | Plague, then Smallpox only after unrestricted and fail-safe acceptance | Same normal gates |
| Japan-China | Anthrax and Plague only, because separate historical campaign actions consume both | Exact campaign route lost or any normal safety gate fails |
| Desperate | Strongest completed ordinary family | Exact desperate route lost, risk context missing, handling technology missing, or target stock reached |

No branch grants stock.

The engine must create production lines and manufacture the exact completed-project model.

## Potency and raid-probability lock

The implemented consequence order is Tularemia less than Anthrax less than Plague less than Smallpox.

The lifecycle profiles use severity ranks one, two, three, and four respectively.

Only Smallpox is severe.

A focused balanced-block comparison proved:

- all four strategic raids use the same `@BIO_RAID_AI_MIN_SUCCESS_CHANCE`;
- all four strategic `success_factors` blocks are identical, including success, critical-success, and disaster inputs;
- all four battlefield raids use the same `@BIO_BATTLEFIELD_AI_MIN_SUCCESS_CHANCE`;
- all four battlefield `success_factors` blocks are identical.

Agent identity changes preparation, reservation, lifecycle, deaths, contamination, medical saturation, evidence, attribution, countermeasures, and Condemnation, but not ordinary raid delivery odds.

## Source and engine evidence

Installed current-version `common/ai_strategy/_documentation.md` states that `equipment_production_surplus_management` controls production only after normal equipment needs are met and accepts exact equipment models rather than only archetypes.

Current vanilla `common/ai_strategy/default.txt` provides the consumed-file precedent.

Current special-project definitions grant the four delivery technologies on project completion, and those technologies enable the exact four payload models.

The production strategies therefore select exact models without researching project-output technologies directly and without changing the shared infantry-equipment category.

The native surplus value is a relative weight, not a guaranteed percentage of Military Factories.

The specification's biological production shares are consequently represented by conservative relative weights and bounded stock targets.

This engine-native limitation is disclosed and is not used to infer payload, risk, authorization, or target state.

The HOI4 inspection transport returned `Transport closed` during this tranche.

No MCP result is claimed for the project selectors, and no fallback implementation was added.

## Scenario expectations

- A battlefield program with protection and no ordinary project selects Tularemia, not all four projects.
- A retaliatory program with protection and no ordinary project selects Anthrax.
- A strategic program advances from an early project to Plague only with exact safe risk, then reaches Smallpox only under the stricter route and containment gates.
- Japan in China selects Anthrax before Plague only while its exact theater route remains open.
- A country entering the exact desperate route without an ordinary project follows Anthrax, then Plague, then Smallpox rather than jumping directly to the severe agent.
- Dangerous or Critical risk stops normal biological payload production.
- A desperate country with a valid arsenal snapshot may continue the strongest completed payload family.
- A country with conventional equipment deficits or unstable protection does not expand a normal offensive biological program.

These are source-derived expectations for the completed selector.

The full seven-major and three-minor Stage 10 scenario matrix remains pending until the other AI consumers and country profiles are complete.

## Assets

No asset was created for this AI-only tranche.

Existing biological project, equipment, and raid icons remain in use.

The existing `gfx/interface/military_raids` package was preserved, and no runtime Chaos Redux icon was overwritten.

## Remaining Stage 10 work

- event-driven regimental template adoption and removal;
- final exact operation target-country and relationship audit;
- country profile assignment and differentiated research, production, and use behavior;
- historically sourced national designer and MIO identities;
- full major and minor scenario matrix.

Headquarters role arbitration, outbreak countermeasure and cleanup weights, condemned-target response profiles, automatic participant sanctions, faction shielding, continued-use pressure near victory, collapse shutoff, and stockpile-destruction preference are implemented and recorded in `stage_10_command_and_sanction_ai_handoff.md`.

## Simplifications, omissions, and blockers

No estimator, proxy target, inferred safe risk, free stock, hidden arsenal, tag-only authorization, broad periodic pulse, or decision substitute for ordinary biological raids was introduced.

Exact Military Factory percentage allocation is unsupported by the native surplus strategy; only its documented relative-weight behavior is claimed.

The HOI4 MCP transport was unavailable for this tranche.

Stage 10 and the overall package remain incomplete.
