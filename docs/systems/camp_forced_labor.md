# Camp forced labor

Status: implemented in source.
Acceptance basis: the user's 10 October 2026 brief asked for a labor system that works end to end and weighs output against deaths, famine and condemnation.
No game was launched; live behavior, AI timing and save persistence remain user-validated.

## What the system does

Forced labor is the national economy of the Camp Administration window.
A site produces output only while it holds living detainees, is a labor or penal institution, is not suspended, and its administering country holds a coercive or radical mandate.
Output is derived each month by `camp_admin_refresh_state_economy` and applied through two dynamic modifiers.

| Country priority | Output | Where it applies |
| --- | --- | --- |
| Industrial Production | Share of the site's undamaged arms factories, capped at 25 percent of national factory output | `camp_admin_country_economy` (`industrial_capacity_factory`) |
| Construction and Logistics | Infrastructure construction speed, only while a funded works project runs at that site | `camp_admin_state_economy` (`state_production_speed_infrastructure_factor`) |
| Resource Extraction | Local resource output at sites with iron, steel-chain or oil resources | `camp_admin_state_economy` (`local_resources_factor`) |

Construction output needs a spending ceiling above maintenance, because the funded project is what grants the bonus and, on completion, adds one infrastructure level.

## Where the workers come from

Workers are the people already counted in a site's living custody rows.
`camp_admin_workforce_k` is 65 percent of living custody (bounded by physical capacity), scaled by the funded support fraction, then reduced by hunger in the host state.
Admission, release, rows and responsibility are unchanged and documented in `common/scripted_effects/camp_administration_effects.md`.

## The trade-off

| Pressure | Effect on output | Effect on deaths |
| --- | --- | --- |
| Coercive mandate | Base output | Base labor mortality |
| Radical mandate on a labor or penal site | Output multiplied by `camp_admin_labor.radical_output` | Labor deaths multiplied by `camp_admin_labor.radical_mortality` |
| Maintenance below the quote | Workforce and output fall with the funded fraction | Custody deaths rise with the unfunded share |
| Host state in acute shortage, famine or catastrophic famine | Workforce multiplied by the matching `camp_admin_labor` factor | None added here |

Deaths already feed the other systems through the single measured receipt in `camp_admin_record_deaths`.
The shared Deaths record, the responsible country's hidden atrocity score and Condemnation scale with the people actually lost, so a harsher labor policy raises condemnation exposure in proportion to its losses.
`famine_adapt_camp_state` submits the same receipt to Famine, and Famine's camp surfaces already add extraction and vulnerability pressure for every state holding an active camp.
Hunger therefore closes the loop: crowded camps push their host state toward shortage, and a state in shortage cannot field its workforce.

The legacy labor burden index `camp_labor_output` on the site profile follows the labor actually assigned at an administered site, through `camp_admin_scale_profile_labor_output`.
An idle, suspended or custody-only site adds no labor burden to the stability and supply ideas.

## Tuning

All values live in `common/script_constants/camp_administration_constants.txt`.
`camp_admin_labor` holds the radical output and mortality multipliers and the three famine workforce factors.
The base monthly rates (`labor_monthly_rate`, `custody_monthly_rate`, `shortage_mortality_factor`, `workforce_share`) stay in `camp_admin_value`.

## Player-facing text

The mandate and priority tooltips state the trade-off in the window.
No value was added to the window: the output, held and deaths cards already show the result.

## Future plans

- A visible hunger indicator per site beside the maintenance bar once the Famine presentation exposes one stable value per state.
- Country-specific labor rates, for example harsher Soviet penal mortality, when a country package owns the justification.
- A condemnation line that names forced labor as its own source instead of the shared camp operation context.
