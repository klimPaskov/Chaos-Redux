# Event 016 remaining Directorate report flavour handoff

## Scope

This tranche extends the existing host-archetype presentation to the loyalty dossier `chaosx.nr16.10` and primary-laboratory convoy dossier `chaosx.nr16.11`. It adds no event ID, root fire, cluster, evolution, meter, project reward, decision, event-log row, asset, or model.

## Changed surfaces

- `localisation/english/016_brilliant_scientist_directorate_outcomes_l_english.yml` appends `[This.GetBrilliantScientistHostFlavorClause]` to all five `.10` finding descriptions and all five `.11` convoy descriptions.
- `docs/events/016_brilliant_scientist/systems/directorate.md` and `docs/events/016_brilliant_scientist/overview.md` record that `.10` and `.11` use the same host-archetype clause while retaining their existing report semantics.

## Runtime contract

The existing scripted localisation helper still resolves exactly one clause from the host's mutually exclusive archetype flags and retains its default branch. Event scripts, triggers, effects, event-log mappings, event details, and catalog-facing fields are unchanged. The reports remain ordinary incidents and cannot create an additional reward or evolution through this presentation change.

## Validation evidence

The ten updated descriptions reference the existing helper. The seven helper localisation keys remain present and unique. The localisation file remains UTF-8 with BOM and has no duplicate keys or `:0` entries. Focused static checks cover the helper reference count, localisation key resolution, and the Event 016-only diff. No game launch or live consumer test was performed.

## Remaining risks

Broader country-specific report writing, bespoke project, news, and remnant art, quantitative balance evidence, live acceptance, and the seven documented generic 3D unit packages remain deferred. No model is produced or referenced by this tranche.
