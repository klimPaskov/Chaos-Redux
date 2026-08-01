# Event 016 Scientist-Gift Bridge Handoff

## Scope

Event 054 retains its generic random-technology outcome for every country. When the recipient is the active Kruger host, the option also records one independent assistant breakthrough and moves the existing Directorate causal meters. This is a bounded cross-event reaction: it adds no new project stage, evolution, Event Log row, foreign operation, asset, or 3D model.

## Gameplay files

- `common/script_constants/016_brilliant_scientist_directorate_constants.txt`
  - adds the centralized `brilliant_scientist_assistant_breakthrough` meter deltas.
- `common/scripted_effects/016_brilliant_scientist_context_effects.txt`
  - adds `brilliant_scientist_record_assistant_breakthrough`.
- `events/054_random_tech.txt`
  - adds a current-host-only tooltip and calls the guarded helper after the existing random-technology event option.
- `common/scripted_effects/016_brilliant_scientist_effects.txt` and `common/scripted_effects/016_brilliant_scientist_country_effects.txt`
  - carry the country receipt through ordinary transfer and fixed-tag sovereignty formation.
- `localisation/english/016_brilliant_scientist_l_english.yml`
  - adds `brilliant_scientist_assistant_breakthrough_effect_tt`.

## Runtime contract

The helper requires the current host, no country receipt, and no fixed-character receipt. It writes `brilliant_scientist_assistant_breakthrough_recorded` on the host and `brilliant_scientist_personal_assistant_breakthrough_recorded` on `KRG_warren_kruger`, then applies Mandate +10, Dependence -5, Exposure +5, Project Capacity +5, Independent Capacity +10, and Grievance -5 through the existing bounded meter effects. The character receipt prevents a duplicate if the host changes or the Kruger State is formed.

## Validation evidence

- Static source review checked the helper guard, exact flag IDs, centralized constants, and existing Event 054 option order.
- The ordinary transfer and fixed-tag formation inheritance helpers now copy the country receipt; the fixed character receipt remains the duplicate guard.
- No new event ID, project family, event-log reference, evolution, asset, or model reference was introduced.
- Localisation remains in the existing Event 016 BOM file.

## Remaining risks

The generic Event 054 source has a broad existing `every_country` random-technology loop; this tranche does not redesign that unrelated behavior. Foreign scientist aid, counter-Kruger coalitions, and bespoke report/news art remain queued design hooks.
