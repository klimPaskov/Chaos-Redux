# Event 016 static-field constant compatibility handoff

Date: 2026-08-02

## Scope

This bounded runtime-safety tranche makes Event 016 database declarations consume engine-compatible file-scoped `@` values where static fields cannot parse `constant:` script-constant tokens. The mirrored values remain sourced from the authoritative Event 016 script-constant definitions; no tuning value, project gate, reward, route, or model contract was changed.

## Changed surfaces

- `common/country_leader/016_brilliant_scientist_traits.txt` mirrors the fixed Kruger research and country-leader trait values.
- Event 016 idea files mirror static modifier values in the aftermath, country, focus, host, and project-force idea declarations.
- `common/special_projects/projects/016_brilliant_scientist_projects.txt` mirrors static resource, threshold, and icon-adjacent project fields while preserving every trigger and reward bridge.
- Event 016 project technology and project-force technology files mirror static research, production, and equipment values.
- `common/units/016_brilliant_scientist_project_forces.txt` mirrors static sub-unit priorities, combat values, terrain modifiers, equipment needs, and training values.
- `common/opinion_modifiers/016_brilliant_scientist_foreign_opinion_modifiers.txt` mirrors static opinion values; `common/opinion_modifiers/016_brilliant_scientist_country_opinion_modifiers.txt` now uses the required `opinion_modifiers` root wrapper.
- `common/mtth/016_brilliant_scientist_foreign_mtth.txt` scopes ideology comparisons through `event_target:brilliant_scientist_current_host = { has_same_ideology = yes }`, preserving the intended foreign-operation weighting.

The Event 016 equipment declaration is intentionally not changed in this tranche. Its six `can_be_produced` gates remain tied to the corresponding deployment triggers, stage history, and facility ownership.

## Review and validation

- Compared every mirrored `@` value against the corresponding Event 016 script constant; the read-only compatibility audit found zero value mismatches across traits, five idea files, technologies, units, foreign opinions, and ninety-four special-project replacements.
- Confirmed that no `allow`, `visible`, `available`, `enable`, specialization, or equipment-production gate was changed by the macro rewrite.
- Confirmed the equipment file still has causal deployment gates rather than `always = yes`.
- Reviewed the two semantic fixes separately: scoped ideology checks follow the event-target trigger form, and the country opinion file follows the vanilla `opinion_modifiers = { ... }` database root.

## Remaining boundary

This tranche does not produce 3D models, add unit entities, alter project costs, or claim live Hearts of Iron IV validation. The seven reusable Event 016 project-force model packages remain deferred under `016_event19_generic_unit_family_3d_model_backlog.md`.
