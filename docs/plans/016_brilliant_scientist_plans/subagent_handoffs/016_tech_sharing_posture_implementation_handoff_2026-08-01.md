# Event 016 Technology-Sharing Posture Handoff

## Scope

Event 089 retains its ordinary technology-sharing group or refusal outcome for every country. When the country is the active Kruger host, the selected posture is recorded once and updates the existing Directorate meters. This is a cross-event reaction only. It creates no new technology-sharing group, project family, event-log row, evolution, asset, or 3D model.

## Gameplay files

- `common/scripted_effects/016_brilliant_scientist_context_effects.txt`
  - `brilliant_scientist_record_tech_sharing_acceptance`
  - `brilliant_scientist_record_tech_sharing_refusal`
- `events/089_tech_sharing_group.txt`
  - guarded calls in `chaosx.nr89.2.a`, `.2.b`, `.2.c`, `.2.e`, and `.2.g`
- `localisation/english/016_brilliant_scientist_l_english.yml`
  - conditional host tooltips for the two postures

## Runtime contract

Joining any existing Event 089 research group writes `brilliant_scientist_tech_sharing_choice_recorded` and `brilliant_scientist_tech_sharing_network_joined`, then changes Mandate by 5, Dependence by -5, Exposure by 5, Project Capacity by 10, Independent Capacity by 10, and Grievance by -5. Refusal writes the same receipt and `brilliant_scientist_tech_sharing_refused`, then changes Mandate by 10, Dependence by 10, Exposure by -5, Project Capacity by 5, Independent Capacity by -5, and Grievance by 10. The helpers are guarded by `brilliant_scientist_is_current_host`, so non-Kruger countries execute only the original Event 089 behavior.

## Validation evidence

- Event-level inspection targeted at `chaosx.nr89.2` after the edit.
- Gameplay braces, exact helper IDs, and localisation BOM checked on all touched files.
- Conditional `custom_effect_tooltip` blocks are limited to the current host and receipt absence.
- No technology-sharing group definition, project, model, or Event 016 log/evolution reference was added.

## Remaining risks

The future Kruger State submission-based sharing group remains a separate route requirement. This tranche intentionally reuses the four existing generic Event 089 groups and does not infer a new group definition from the unimplemented Event 137 or Event 151 concepts.
