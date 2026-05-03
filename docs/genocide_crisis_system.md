# Camps, Genocide Crisis, and Discovery-Based Condemnation

## Overview

The genocide crisis system models hidden state repression, forced labor, extermination sites, gulag networks, discovery, foreign response, and tribunal pressure. It is built around two separate layers:

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
- `localisation/english/chaosx_buildings_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/chaosx_ideas_l_english.yml`
- `localisation/english/chaosx_modifiers_l_english.yml`
- `localisation/english/_chaosx_events_l_english.yml`
- `localisation/english/chaosx_chaos_meter_l_english.yml`

## Buildings

The system uses three hidden state buildings:

- `concentration_camp`
- `extermination_camp`
- `gulag_labor_camp_network`

They are not normal construction-tab buildings. They are built by decisions and scripted effects so each affected state can store `genocide_responsible_country`. That variable is the authority used later for discovery, condemnation, events, and tribunals.

### Concentration Camps

Concentration camps represent detention, forced labor, deportation processing, and general repression infrastructure. They reduce manpower and compliance growth, slightly suppress resistance in the short term, and add modest state output. Their monthly deaths use `chaos_meter_deaths_reason.camp_atrocity`.

### Extermination Camps

Extermination camps represent systematic mass killing. They cause much higher monthly deaths, damage compliance, increase resistance pressure, and create the largest condemnation spike if discovered. They use `chaos_meter_deaths_reason.extermination_camp`.

### Gulag Networks

Gulag labor camp networks represent Soviet forced labor and mass repression. They provide resource and construction pressure while causing population loss, resistance pressure, and later condemnation if discovered. They use `chaos_meter_deaths_reason.gulag_repression`.

## Step-by-Step Flow

1. Startup initializes historical sites for fascist Germany, fascist Japan, and communist Soviet Union.
2. Decisions or country-specific AI build additional camp, extermination, forced labor, or gulag sites.
3. Each created state stores `genocide_responsible_country = ROOT`.
4. Each active camp state is registered into `global.genocide_active_camp_states`.
5. The existing Chaos Meter monthly pulse runs `genocide_monthly_global_pulse`.
6. Only registered states that still have active camp buildings are processed.
7. Monthly camp deaths reduce real state population through the Chaos Meter deaths pipeline.
8. Responsible countries accumulate hidden crisis variables such as `genocide_escalation`, `genocide_deaths`, `genocide_visibility`, `genocide_resistance_pressure`, `genocide_refugee_pressure`, and `hidden_atrocity_score`.
9. Internal crisis events can fire if stability or party support is weak enough.
10. If enemy forces take a state with undiscovered atrocity evidence, `on_state_control_changed` attempts discovery.
11. Discovery marks the state, calculates condemnation based on site type and repeat discoveries, and applies condemnation to the stored responsible country.
12. The first discovery fires the discoverer event and responsible-country event. Extermination discoveries fire the global news event once.
13. Condemnation thresholds at 25, 50, 75, and 100 trigger newspaper, refugee, sanctions, and tribunal-pressure events.
14. If the responsible country capitulates after reaching tribunal-level condemnation, tribunal preparation activates.

## Evidence Destruction

The evidence-destruction decisions are state-targeted and require:

- controlled or owned atrocity evidence,
- no previous discovery in that state,
- nearby enemy forces.

Success removes camp buildings and marks the state as a destroyed atrocity site, reducing later condemnation. Failure marks the state with failed cover-up evidence, increasing later condemnation. Both paths create additional deaths and leave discoverable state evidence.

## Country AI

AI behavior is split between decision weights and broad AI strategy:

- Germany is weighted toward concentration camps, occupied Poland, extermination camps, deportation logistics, and retreat cover-ups when fascist and at war.
- Japan is weighted toward forced labor camps, occupation reprisals, and prisoner experimentation when it controls Chinese or Manchurian target regions. Biowarfare experimentation connects to the existing biological contamination effects.
- The Soviet Union is weighted toward gulag expansion, deportations, famine pressure, and record destruction in remote or borderland gulag target states.

`common/ai_strategy/genocide_crisis_ai_strategy.txt` adjusts broad behavior for active and exposed crisis regimes, including army-building and reduced appetite for additional wars after high condemnation.

## Existing-System Integration

### Chaos Meter Deaths

Camp deaths use the shared deaths system, reduce real state population, and appear in the Deaths tab as:

- Camp atrocities
- Extermination camp
- Gulag repression

The country summary folds those deaths into the existing occupation-repression total so the current Deaths tab layout remains stable.

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
| `concentration_camp` | `GFX_building_concentration_camp` | `gfx/interface/buildings/building_concentration_camp.dds` |
| `extermination_camp` | `GFX_building_extermination_camp` | `gfx/interface/buildings/building_extermination_camp.dds` |
| `gulag_labor_camp_network` | `GFX_building_gulag_labor_camp_network` | `gfx/interface/buildings/building_gulag_labor_camp_network.dds` |

The current files are placeholder sprites copied from vanilla-style building assets so the game has valid references. Replace those files in place when final art is ready; the GFX names and code references do not need to change.

The dynamic modifiers and ideas use existing `GFX_idea_jews_massacre` / `generic_oppression` style icons. The decisions use existing vanilla/Chaos decision icons and do not require additional sprites.

## Future Plans and Suggestions

- Add a dedicated event-log view for discovered camp evidence, separate from ordinary news popups.
- Add country-specific German escalation decisions tied to SS archives, occupied Europe, and the existing Auschwitz/Mengele chain.
- Add Japanese prisoner-transfer variants that depend on the exact biological agent researched.
- Add Soviet paranoia or purge variables if a later Soviet internal-politics system exists.
- Add postwar tribunal outcomes that can remove leaders, force ideology changes, or create reparations decisions after defeat.
- Add resistance rescue-network decisions for democratic or exile governments after discovery.
