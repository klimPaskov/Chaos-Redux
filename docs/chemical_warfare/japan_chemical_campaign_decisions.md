# Japan Chemical Campaign Decisions

## Overview

This mechanic adds a Japan-only decision category for targeted cylinder use during the China war.

- Category: `japan_chemical_campaign_category`
- Decisions:
	- `japan_chemical_campaign_cycle_agent`
	- `japan_chemical_campaign_attack`
- Scripted effects:
	- `japan_cycle_targeted_chemical_campaign_agent`
	- `japan_apply_targeted_chemical_campaign_attack` (migration-safe retired identifier)

The decisions are state-targeted and only appear for Japan while it is at war with Chinese tags (`CHI`, `PRC`, `SHX`, `GXC`, `YUN`, `XSM`, `SIK`).

## How It Works

1. Japan selects an eligible state in Asia that is a Chinese core and currently controlled by an enemy at war with Japan.
2. Japan can rotate the prepared chemical agent for free inside the category.
3. The attack decision spends command power and consumes the selected cylinder type.
4. The attack remains unavailable until a current-version adapter can provide the selected state, exact payload debit, military and civilian protection, and verified weather and terrain inputs to the shared chemical exposure dispatcher.
5. The historical decision does not retain a direct contamination or Condemnation path while that adapter is unavailable.
6. The targeted state will receive the short anti-spam cooldown flag (`japan_chemical_campaign_recently_targeted`) only after an accepted shared dispatch exists.

## Integration With Existing Systems

- **Condemnation:** The accepted adapter will use the same source-aware chemical Condemnation dispatcher as raids and occupation suppression; no decision-local Condemnation formula remains active.
- **Air Cleanliness / Contamination:** The accepted adapter will contaminate only the exact selected state through the shared state consequence dispatcher.
- **Deaths / Chaos:** The accepted adapter will record deaths, medical saturation, evidence, attribution, and cleanup through the shared exposure pipeline.
- **AI:** Japan gets extra AI weighting for Livens and chemical support usage during the China war.

## AI Changes

- Major-country cylinder production requires enemy chemical weapon use, except Japan.
- Japan starts with `livens_projector_tech` in 1936 setup.
- Japan gets increased Livens and chemical support template/production pressure while fighting China.

## Icons and UI Wiring

The exact category `japan_chemical_campaign_category` uses a dedicated generated category icon:

- Sprite: `GFX_decision_category_japan_chemical_campaign`
- Final DDS: `gfx/interface/decisions/japan_chemical_campaign/decision_category_japan_chemical_campaign.dds`
- Category wiring: `common/decisions/categories/japan_chemical_campaign_categories.txt`
- Sprite definition: `interface/chaosx_gfx_cleanup.gfx`
- Source package: `docs/assets/shared_gfx_cleanup/`

The two individual decisions continue to use `GFX_decision_generic_operation`; the category header provides the campaign's persistent visual identity.

- Localisation keys are in: `localisation/english/chaosx_decisions_l_english.yml`

## Adapter status

The decision is visible for historical continuity and retains its selector, but its attack trigger is fail-closed because the current decision surface does not provide a verified weather and terrain receipt. Implementing a neutral-condition or neighboring-state estimator would violate the package contract and is not retained.

## Future Plans

- Add decision outcome events/news flavor for major operations.
- Add front-distance scaling so decisions prioritize active Japanese offensives.
