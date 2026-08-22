# Japan–China Biological Campaign

## Overview

The Japan–China biological campaign provides two exact-state decisions for Japan's explicitly authorized Ishii program while preserving native raids as the normal strategic and battlefield delivery systems.

These decisions represent historically specific theater actions whose fixed selected state and narrow AI route make the historical campaign easier to reproduce without inventing a raid target, launch state, proxy state, or continuous-air estimate.

Both actions consume real resources and dispatch the exact selected state through the shared ordinary-pathogen lifecycle.

Weaponized zombies remain separate.

## Route and Target Gate

The category is limited to the original Japanese country while it is fighting a Chinese country and operating the explicit Pingfang, Ishii program, and Ishii authority route.

Containment, reform, and prisoner-experiment shutdown routes close the campaign.

The acting country also needs an active CBRN program, Operational Chemical Readiness, strategic biological-use policy, biological security, and attribution-control records.

An eligible target is an enemy-controlled Chinese core state in Asia that:

- remains controlled by an actual Chinese belligerent rather than Japan, a Japanese subject, or a faction partner;
- is adjacent to a state controlled by Japan or a Japanese subject, which proves the occupation-linked theater route;
- is inhabited, passable, eligible for the ordinary-pathogen lifecycle, and outside its exact 180-day campaign cooldown;
- has no active episode of the selected agent; and
- meets the selected action's target profile.

The Anthrax action requires a supply node, port, sufficient infrastructure or industry, or an actual division in the selected state.

The Plague action requires a capital, city, port, or sufficiently populous selected state.

No helper searches for an alternate state when the selected state is invalid.

## Actions and Costs

| Decision | Agent | Political Power | Payload | Support Equipment | Command Power | Base national cooldown |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| Contaminate Supply Networks | Anthrax | 35 | 8 Anthrax Bombs | 35 | 10 | 90 days |
| Disperse Plague Vectors | Plague | 40 | 10 Plague Bombs | 45 | 14 | 90 days |

The custom decision cost validates all four resources and the complete effect revalidates them before making any debit.

Political Power, the exact agent model, Support Equipment, and Command Power are then consumed inside the same committed effect chain.

Theater Contamination doctrine shortens the national cooldown to 60 days and refunds 2 Command Power after a valid lifecycle dispatch.

Terminal Hazard doctrine shortens the national cooldown to 45 days and refunds 4 Command Power after a valid lifecycle dispatch.

Doctrine never refunds Political Power, payload, or Support Equipment.

## Shared Lifecycle

Both decisions use the private `japan_china_campaign` route and call `bio_lifecycle_dispatch_seed` for the exact selected state.

The decision layer has equal deterministic release acceptance for Anthrax and Plague after every route, target, and cost gate passes.

It does not give Plague a better delivery-success roll than Anthrax.

Uncertainty begins inside the shared lifecycle through incubation, detection, spread, response, attribution, and recovery.

The canonical agent profile preserves the accepted weapon hierarchy `Tularemia < Anthrax < Plague < Smallpox`.

Anthrax remains moderate, Plague remains serious, and only Smallpox is severe.

Chaos Warfare doctrine can increase seed potency, growth, spread, deaths, contamination pressure, duration, medical saturation, preparation ease, and aggressive AI willingness through the shared lifecycle.

Condemnation is the only consequence component doctrine may reduce.

Doctrine does not reduce evidence, attribution, physical costs, deaths, contamination, medical saturation, use history, domestic penalties, accident records, or public-harm floors.

## History and Failure Contract

A valid dispatch records the exact actor, victim controller, selected state, agent, date, resource totals, national cooldown, state cooldown, and agent-specific use history.

The ordinary lifecycle separately records incubation, outbreak, death, contamination, evidence, attribution, and Condemnation history.

If the exact committed context fails revalidation, no equipment is consumed and no release is created.

If the shared lifecycle rejects a record after the committed debit, the material remains consumed and the actor receives a diagnostic dispatch-failure history flag.

That failure creates no alternate state, proxy contamination, evidence substitute, payload refund, or inferred use record.

## AI Behavior

AI Japan uses the same route, project, target, stockpile, Command Power, Political Power, and cooldown gates as the player.

Anthrax receives additional target weight for supply nodes and ports.

Plague receives additional target weight for capitals, major cities, ports, and high population.

Theater Contamination and Terminal Hazard doctrine increase willingness because they represent a more aggressive Chaos Warfare route.

An exact state already used by the campaign receives lower weight after its cooldown expires.

High Condemnation combined with high import vulnerability sharply suppresses use without disabling an otherwise authorized human action.

Japan stops selecting either historical campaign action when its own surrender progress reaches the exact near-capitulation threshold. An explicitly authorized doomsday route leaves only the separate doomsday decision as a biological release choice during collapse; without that route, stockpile destruction is preferred.

The AI never receives a fabricated target, inferred frontline, or fallback action.

## Historical Confidence

The Japanese biological warfare program, Unit 731, weaponized plague-vector work, and deliberate plague releases in China are well attested.

The 1940 Ningbo plague release is a particularly well-documented basis for the Plague action.

Japanese work with *Bacillus anthracis* and the program's Anthrax capability are also well attested.

The specific supply-network Anthrax action is a medium-confidence gameplay abstraction of that documented capability rather than a claim that one named historical operation used this exact method.

The route gates, occupation linkage, and differentiated target profiles are gameplay tuning, not quantitative historical estimates.

Sources:

- [Plague as a Biological Weapon and Bioterrorism Threat](https://pmc.ncbi.nlm.nih.gov/articles/PMC7270574/)
- [Biological Warfare and Bioterrorism: A Historical Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC1200679/)
- [Shiro Ishii biography, American Experience](https://www.pbs.org/wgbh/americanexperience/features/weapon-biography-shiro-ishii/?flavour=full)
- [History of Biological Warfare, NOVA](https://www.pbs.org/wgbh/nova/bioterror/hist_nf.html)
- [Anthrax: A Disease of Biowarfare and Public Health Importance](https://pmc.ncbi.nlm.nih.gov/articles/PMC7106442/)

## Files and Stable Identifiers

Gameplay:

- `common/decisions/categories/japan_biological_campaign_categories.txt`
- `common/decisions/japan_biological_campaign_decisions.txt`
- `common/script_constants/japan_biological_campaign_constants.txt`
- `common/scripted_triggers/japan_biological_campaign_triggers.txt`
- `common/scripted_effects/japan_biological_campaign_effects.txt`
- `common/script_constants/biological_lifecycle_constants.txt`
- `common/scripted_triggers/biological_lifecycle_triggers.txt`
- `common/scripted_effects/biological_lifecycle_effects.txt`

Player-facing wiring:

- `localisation/english/japan_biological_campaign_l_english.yml`
- `interface/biological_warfare.gfx`

Stable category and decision identifiers:

- `japan_biological_campaign_category`
- `japan_bio_campaign_contaminate_supply_network`
- `japan_bio_campaign_disperse_plague_vectors`

## Assets

The category icon is `gfx/interface/decisions/biowarfare/japan_china/decision_category_japan_biological_campaign.dds`.

It is registered as `GFX_decision_category_japan_biological_campaign` in `interface/biological_warfare.gfx`.

Its generated source, transparent processing evidence, exact 52x40 preview, contact sheet, manifest, and handoff live under `docs/assets/chaos_warfare_cbrn/japan_biological_campaign/`.

The Anthrax and Plague actions reuse their existing exact-agent decision sprites, `GFX_decision_bio_sabotage_anthrax` and `GFX_decision_bio_sabotage_plague`.

No focus icon, idea icon, placeholder, resized cross-type substitute, or raid icon is used for the category.

Every existing asset under `gfx/interface/military_raids/` remains untouched and available to the native biological raids.

## Engine Limits

The state-targeted decision contract exposes the exact selected state as `FROM`, so the implementation can preserve the player or AI target without an estimator.

The shared lifecycle requires a real current victim controller, so these actions target enemy-controlled Chinese states adjacent to a real Japanese or Japanese-subject occupation zone rather than Japanese-occupied states.

The campaign does not infer an active combat province, an alternate target, or a historical operation state when the exact selected state is unavailable.

No daily, weekly, or monthly all-country pulse is added.

## Future Extensions

- Add another historically specific campaign action only when research supports a distinct route, target profile, and agent payload rather than a renamed duplicate.
- Add player-facing forensic summaries only when they can expose real lifecycle evidence without revealing hidden information.
- Preserve native raids for ordinary strategic and battlefield deployment while keeping campaign decisions narrow, historical, and exact-state.
