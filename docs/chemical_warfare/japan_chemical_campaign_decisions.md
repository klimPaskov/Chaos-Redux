# Japan Chemical Campaign Decisions

## Overview

The Japan-only China Theater Chemical Campaign provides an exact-state historical cylinder route during a war with `CHI`, `PRC`, `SHX`, `GXC`, `YUN`, `XSM`, or `SIK`.

The category contains the free `japan_chemical_campaign_cycle_agent` selector and the state-targeted `japan_chemical_campaign_attack` operation.

## Operation contract

1. Japan selects an enemy-controlled Chinese core state adjacent to Japanese-controlled territory.
2. Operational Chemical Readiness and battlefield-use authority must be active.
3. The selected Chlorine, Phosgene, Mustard, or Lewisite technology and at least 120 matching legacy agent cylinders are required.
4. The operation saves the exact selected state, maps the selected agent into the shared chemical taxonomy, and debits exactly 120 matching cylinders through the canonical payload helper.
5. The committed release supplies positive release efficiency and resolves military and civilian protection for the selected state. No weather, terrain, launch-state, neighboring-state, or aircraft estimate is created.
6. The shared exposure pipeline calculates disruption, deaths, contamination, medical saturation, evidence, attribution, and Condemnation. Doctrine mastery and designers apply only through that shared pipeline.
7. Accepted use starts an eight-day national cooldown and a twenty-four-day target-state cooldown.

The Controlled Retaliation army spirit reduces the Command Power cost from 20 to 16. It does not alter payload consumption, evidence, attribution, deaths, contamination, or the historical record.

## AI

The AI attacks only after the same readiness, policy, research, stock, target, and Command Power gates pass. If its selected agent lacks a valid researched stockpile but another eligible cylinder stockpile exists, it uses the free selector until it reaches a usable agent. Treaty membership sharply reduces attack weight without bypassing the route.

## Files

- Decisions: `common/decisions/japan_chemical_campaign_decisions.txt`
- Category: `common/decisions/categories/japan_chemical_campaign_categories.txt`
- Effects: `common/scripted_effects/JAP_chemical_campaign_effects.txt`
- Payload accounting: `common/scripted_effects/cbrn_payload_effects.txt`
- Shared exposure and consequences: `common/scripted_effects/cbrn_exposure_effects.txt`, `common/scripted_effects/cbrn_consequence_effects.txt`
- Triggers: `common/scripted_triggers/cbw_triggers.txt`, `common/scripted_triggers/cbrn_payload_triggers.txt`
- Scripted localisation: `common/scripted_localisation/japan_chemical_campaign_scripted_localisation.txt`
- Localisation: `localisation/english/chaosx_decisions_l_english.yml`

## Assets

The category uses `GFX_decision_category_japan_chemical_campaign`, defined in `interface/chaosx_gfx_cleanup.gfx` and stored at `gfx/interface/decisions/japan_chemical_campaign/decision_category_japan_chemical_campaign.dds`.

The selector and attack use dedicated 32×32 decision-type art generated against installed-vanilla decision references:

- `GFX_decision_japan_chemical_campaign_cycle_agent` → `gfx/interface/decisions/japan_chemical_campaign/decision_japan_chemical_campaign_cycle_agent.dds`
- `GFX_decision_japan_chemical_campaign_attack` → `gfx/interface/decisions/japan_chemical_campaign/decision_japan_chemical_campaign_attack.dds`

The generated source, processed PNGs, native-size review enlargements, references, and hashes are retained in `docs/assets/japan_chemical_campaign_decisions/`. The category image was used as subject reference only; it was not resized into either decision icon.
