# Camps, Genocide Crisis, and Discovery-Based Condemnation

## Overview

The genocide crisis system models hidden state repression, forced labor, extermination sites, gulag networks, experiment-linked atrocity sites, restricted chemical site escalation, discovery, foreign response, and tribunal pressure. It is built around two separate layers:

1. Internal damage while the responsible regime controls or operates the site.
2. External condemnation only after enemy discovery or survivor evidence reaches foreign countries.

This keeps the system tied to visible evidence instead of automatic passive condemnation. Camps can kill civilians and reduce state population long before the outside world can prove who is responsible.

## Script Files

Core tuning lives in `common/script_constants/genocide_crisis_constants.txt`.

Main gameplay wiring lives in:

- `common/buildings/chaosx_buildings.txt`
- `common/decisions/categories/genocide_crisis_categories.txt`
- `common/decisions/genocide_crisis_decisions.txt`
- `common/scripted_effects/genocide_crisis_effects.txt`
- `common/scripted_triggers/genocide_crisis_triggers.txt`
- `common/on_actions/genocide_crisis_on_actions.txt`
- `common/on_actions/chaosx_on_actions_chaos_meter.txt`
- `events/genocide_crisis_events.txt`
- `common/ai_strategy/genocide_crisis_ai_strategy.txt`

Supporting surfaces live in:

- `common/dynamic_modifiers/genocide_crisis_dynamic_modifiers.txt`
- `common/ideas/genocide_crisis_ideas.txt`
- `common/opinion_modifiers/genocide_crisis_opinion_modifiers.txt`
- `interface/chaosx_buildings.gfx`
- `gfx/entities/chaosx_buildings.asset`
- `localisation/english/chaosx_buildings_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_ideas_l_english.yml`
- `localisation/english/chaosx_modifiers_l_english.yml`
- `localisation/english/_chaosx_events_l_english.yml`
- `localisation/english/chaosx_chaos_meter_l_english.yml`

## Buildings

The system uses three state buildings:

- `concentration_camp`
- `extermination_camp`
- `gulag_labor_camp_network`

Concentration camps are available in the normal construction interface. Extermination camps and gulag networks are created by decisions and scripted effects. Whenever script creates or registers a site, the affected state stores `genocide_responsible_country`; that variable is the authority used later for discovery, condemnation, events, and tribunals.

### Concentration Camps

Concentration camps represent detention, forced labor, deportation processing, and general repression infrastructure. They reduce manpower and compliance growth, slightly suppress resistance in the short term, and add modest state output. Their monthly deaths use `chaos_meter_deaths_reason.camp_atrocity`.

### Extermination Camps

Extermination camps represent systematic mass killing. They cause much higher monthly deaths, damage compliance, increase resistance pressure, and create the largest condemnation spike if discovered. They use `chaos_meter_deaths_reason.extermination_camp`.

### Gulag Networks

Gulag labor camp networks represent Soviet forced labor and mass repression. They provide resource and construction pressure while causing population loss, resistance pressure, and later condemnation if discovered. They use `chaos_meter_deaths_reason.gulag_repression`.

## Step-by-Step Flow

1. Startup initializes country variables and quiet historical concentration camp buildings for fascist Germany, fascist Japan, and communist Soviet Union without registering active death-producing sites on day one.
2. Construction, decisions, or country-specific AI build camp, extermination, forced labor, or gulag sites after escalation. AI countries build concentration camps through the construction system, not through generic construction decisions.
3. Each created state stores `genocide_responsible_country = ROOT`.
4. Each active camp, experiment, or restricted chemical site is registered into `global.genocide_active_camp_states`.
5. The existing Chaos Meter monthly pulse runs `genocide_monthly_global_pulse`.
6. Only registered states that still have active camp buildings, experiment-site flags, or an active restricted chemical site flag are processed.
7. Monthly camp and experiment-site deaths reduce real state population through the Chaos Meter deaths pipeline. When deaths happen in occupied territory, the state owner receives the registered death total while the occupier remains the responsible country for evidence and condemnation.
8. Responsible countries accumulate hidden crisis variables such as `genocide_escalation`, `genocide_deaths`, `genocide_visibility`, `genocide_resistance_pressure`, `genocide_refugee_pressure`, and `hidden_atrocity_score`.
9. Active camp processing does not roll recurring internal report, leak, refugee, or sabotage popups. Internal pressure is represented through variables, state modifiers, decisions, and later discovery.
10. If enemy forces take a state with undiscovered atrocity evidence, `on_state_control_changed` attempts discovery.
11. Discovery marks the state, calculates condemnation based on site type and repeat discoveries, and applies condemnation to the stored responsible country.
12. The first discovery fires the discoverer event and responsible-country event. Extermination discoveries fire the global news event once.
13. Condemnation thresholds at 25, 50, 75, and 100 trigger newspaper, refugee, sanctions, and tribunal-pressure events.
14. If the responsible country capitulates after reaching tribunal-level condemnation, tribunal preparation activates.

## Decision Visibility

The `Camps and Genocide` category has the lowest priority and appears only when the country has an actual player action available beyond the show/hide controls. The generic category no longer offers concentration camp construction decisions; concentration camps are built through the normal construction interface. The generic category highlights only controlled states with an existing concentration camp that can be upgraded into an extermination camp.

When a valid existing concentration camp can be upgraded, `genocide_show_hidden_decisions` reveals the extermination-camp upgrade decision and `genocide_hide_hidden_decisions` hides it again. The reveal decision remains available while valid upgrade targets exist, but the category disappears when the country has no existing concentration camps, no eligible upgrade targets, or no special decision to take.

Soviet gulag and mass-repression decisions use their own player toggle. `sov_show_gulag_decisions` reveals eligible gulag actions through `genocide_gulag_decisions_visible`, while `sov_hide_gulag_decisions` hides them again. AI-controlled Soviet Union bypasses this player-facing toggle and evaluates the gulag decisions as always expanded.

## Evidence And Foreign Observers

Foreign-observer pressure is context-based. Domestic repression inside closed or authoritarian states does not automatically create a foreign evidence problem. Foreign pressure requires conditions such as occupied foreign camp systems, non-core target populations, diplomatic visibility, enemy or democratic exposure, or discovered sites.

This means Soviet internal repression does not normally ask the player to hide evidence from foreign observers. If the Soviet Union operates camp infrastructure in occupied foreign territory, the foreign-observer chain can still apply. Japanese actions in occupied China are treated as occupation atrocities and local evidence unless visibility, diplomacy, or foreign-population context raises the pressure enough.

## Evidence Destruction

The evidence-destruction decisions are state-targeted and require:

- controlled or owned atrocity evidence,
- no previous discovery in that state,
- nearby enemy forces.

Success removes camp buildings and marks the state as a destroyed atrocity site, reducing later condemnation. Failure marks the state with failed cover-up evidence, increasing later condemnation. Both paths create additional deaths and leave discoverable state evidence.

Historical quiet camps are not registered into monthly deaths, discovery pressure, or player popups until escalated into active camp infrastructure.

## Country-Specific Branches

Fascist Germany has direct wartime decisions after 1939 for occupied Poland camp administration, camp expansion, extermination-site escalation after 1940 when the Auschwitz area is controlled, extermination-policy intensification after 1941, and prisoner transfers into Mengele-linked experiment sites. These decisions use the existing camp, Deaths, discovery, and Mengele autonomy systems rather than a separate event pool.

Japan's forced-labor, reprisal, and prisoner-experimentation decisions require an active war with the configured Chinese target bloc and a controlled Chinese or Manchurian target state. Japan's biowarfare-linked experiment sites register into monthly processing and use the existing biowarfare Deaths reason and contamination helpers.

The Soviet Union uses gulag expansion, deportations, food confiscation, camp-administrator purges, forced-labor quotas, and evidence destruction. Gulag, deportation, famine, purge, and labor-quota actions call a Soviet Collapse bridge when the Union Crisis is active: early repression can strengthen Moscow Authority and Military Obedience, but it also adds Old Movement and foreign grievance pressure. The bridge stops giving suppression relief at the high-threat band so it cannot block Union Unmade or mandatory terminal collapse.

## Restricted Chemical Site Escalation

Restricted chemical escalation is a state-targeted camp decision for countries with sarin or soman capability through existing technologies or special projects and enough matching cylinder stockpile. The target must already be an active extermination, gulag, or experiment site with stored responsibility.

The action consumes sarin or soman cylinders, applies existing state contamination through `chem_apply_state_contamination`, creates immediate hidden deaths, registers the site for monthly processing, and leaves `genocide_restricted_chemical_site` evidence. It does not fire the public chemical-attack condemnation path immediately; condemnation is added later if enemy forces discover the site.

## Country AI

AI behavior is split between decision weights and broad AI strategy:

- Germany is weighted toward occupied Poland camp administration, extermination escalation, experiment-site transfers, deportation logistics, and retreat cover-ups when fascist and at war.
- Japan is weighted toward forced labor camps, occupation reprisals, and prisoner experimentation only during a war with the configured Chinese target bloc while it controls Chinese or Manchurian target regions. Biowarfare experimentation connects to the existing biological contamination effects.
- The Soviet Union is weighted toward gulag expansion, deportations, famine pressure, camp-administrator purges, forced-labor quotas, and evidence destruction in remote or borderland gulag target states.

`common/ai_strategy/genocide_crisis_ai_strategy.txt` adjusts broad behavior for active and exposed crisis regimes, including army-building, cautious concentration camp construction, and reduced appetite for additional wars after high condemnation. Germany has a small pre-1939 construction weight capped at a few early camps, then stronger wartime and occupied-territory weights only after 1939 or meaningful escalation.

## Existing-System Integration

### Chaos Meter Deaths

Camp deaths use the shared deaths system, reduce real state population, and appear in the Deaths tab as:

- From camps and forced labor
- Biowarfare outbreak, for Japan's biowarfare-linked experiment sites

The country summary folds concentration-camp, extermination-camp, and gulag repression deaths into the same camps-and-forced-labor total.

### Condemnation

Discovery adds to the existing `chem_warfare_condemnation` variable so the Chaos Meter Condemnation tab and diplomatic consequence effects continue to work. Camps do not add passive condemnation before discovery.

### Biological Warfare

Japan's prisoner experimentation decision uses the existing anthrax, tularemia, and plague contamination effects. The action also creates Chaos Meter deaths and tribunal severity.

### Germany Mengele Chain

The German historical setup includes early concentration camp infrastructure and supports occupied Poland and Auschwitz-area escalation. Auschwitz uses state `88` with province `9412` for the shared node already used by the biowarfare event chain.

When Germany authorizes or restricts the Auschwitz Experiments, state `88` is marked as `genocide_auschwitz_experiment_site` and `genocide_ss_laboratory_site`, stores Germany as the responsible country, and becomes discoverable evidence even before a normal extermination camp building exists there. Discovery of this site adds the ordinary camp/evidence condemnation plus an experiment-site bonus that scales with `mengele_autonomy` and `mengele_permission_level`. If the Auschwitz Directorate exists, it receives a separate condemnation spike as well.

Extermination camps feed the Mengele system when Germany has active or restricted Auschwitz authority:

- restricted authority gives small one-time and monthly autonomy growth;
- full authority gives larger one-time and monthly autonomy growth;
- bypass authority gives the largest autonomy growth and pushes coup pressure fastest.

If enemy forces capture an Auschwitz-linked or biological-facility state while Germany has high Mengele autonomy, the genocide state-control hook can trigger the emergency laboratory revolt. The Directorate then fights the invader first and later attempts war against loyalist Germany once it is no longer at war.

### On Actions

The system adds startup, state-control, and capitulation hooks. Monthly deaths run through the existing host-only Chaos Meter monthly on-action block and iterate the registered camp-state array rather than adding a separate monthly world-country loop.

## Icons and Assets

Building icons are registered in `interface/chaosx_buildings.gfx`.

Required sprites:

| Code icon | GFX entry | Sprite path |
| --- | --- | --- |
| `concentration_camp` | `GFX_building_concentration_camp` | vanilla `gfx/interface/buildings/building_fort_icon.dds` |
| `extermination_camp` | `GFX_building_extermination_camp` | vanilla `gfx/interface/buildings/building_intel_icon.dds` |
| `gulag_labor_camp_network` | `GFX_building_gulag_labor_camp_network` | `gfx/interface/buildings/building_gulag_labor_camp_network.dds` |

The concentration camp building entry uses a vanilla fort-style building icon and the vanilla bunker map mesh. The extermination camp building entry uses a distinct vanilla intelligence-building icon and the vanilla stronghold-network map mesh. Both building types have valid UI sprites and map entities until dedicated final camp art exists.

Camp and Gulag decision categories use the existing Chaos Redux doom category icon `GFX_decision_category_chaos_doom`; no separate camp category DDS is required.

The dynamic modifiers and ideas use existing `GFX_idea_jews_massacre` / `generic_oppression` style icons. The decisions use existing vanilla/Chaos decision icons and do not require additional sprites.

## Future Plans and Suggestions

- Add a dedicated event-log view for discovered camp evidence, separate from ordinary news popups.
- Add deeper German follow-up decisions for occupied Europe and the existing Auschwitz/Mengele chain.
- Add Japanese prisoner-transfer variants that depend on the exact biological agent researched.
- Add Soviet paranoia or purge variables if a later Soviet internal-politics system exists.
- Add postwar tribunal outcomes that can remove leaders, force ideology changes, or create reparations decisions after defeat.
- Add resistance rescue-network decisions for democratic or exile governments after discovery.
