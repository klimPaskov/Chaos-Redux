# Japan Chemical Campaign Decisions

## Overview

This mechanic adds a Japan-only decision category for targeted cylinder use during the China war.

- Category: `japan_chemical_campaign_category`
- Decisions:
	- `japan_chemical_campaign_cycle_agent`
	- `japan_chemical_campaign_attack`
- Scripted effects:
	- `japan_cycle_targeted_chemical_campaign_agent`
	- `japan_apply_targeted_chemical_campaign_attack`

The decisions are state-targeted and only appear for Japan while it is at war with Chinese tags (`CHI`, `PRC`, `SHX`, `GXC`, `YUN`, `XSM`, `SIK`).

## How It Works

1. Japan selects an eligible state in Asia that is a Chinese core and currently controlled by an enemy at war with Japan.
2. Japan can rotate the prepared chemical agent for free inside the category.
3. The attack decision spends command power and consumes the selected cylinder type.
4. The selected state receives contamination through `chem_apply_state_contamination`.
5. The operation calls the shared chemical-use helper with reduced Japan-campaign tuning, the target owner, and measured contamination, then notifies the Air Cleanliness Treaty use hook.
6. The targeted state gets a short anti-spam cooldown flag (`japan_chemical_campaign_recently_targeted`).

## Integration With Existing Systems

- **Condemnation:** The state-targeted China campaign decision applies reduced source-aware chemical condemnation and treaty-use reactions. Japan's separate general-led cylinder use against Chinese targets also uses reduced chemical condemnation.
- **Air Cleanliness / Contamination:** Adds to state contamination using existing chemical state modifier logic.
- **Deaths / Chaos:** Uses existing contamination/death systems through shared effects.
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
- Sprite definition: `interface/chaosx_decisions.gfx`
- Source package: `docs/assets/shared_gfx_cleanup/`

The two individual decisions continue to use `GFX_decision_generic_operation`; the category header provides the campaign's persistent visual identity.

- Localisation keys are in: `localisation/english/chaosx_decisions_l_english.yml`

## Future Plans

- Add decision outcome events/news flavor for major operations.
- Add front-distance scaling so decisions prioritize active Japanese offensives.
