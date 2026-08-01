# Event 016 Kruger State origin flavour handoff

## Scope

This tranche adds formation-origin presentation to the first four Kruger State foundation reports. It reuses the existing charter, rebellion, enclave, and takeover flags that the sovereignty transaction already carries into `KRG`. It adds no event ID, decision, focus, idea, meter, project reward, asset, model, or new fire path.

## Changed surfaces

- `common/scripted_localisation/016_brilliant_scientist_kruger_state_scripted_localisation.txt` defines `GetBrilliantScientistKrgOriginClause` with a safe default branch.
- `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml` appends the clause to `chaosx.brilliant_scientist_krg.1` through `.4` descriptions and supplies five origin strings.
- `docs/events/016_brilliant_scientist/overview.md` records the origin-aware foundation presentation.

## Runtime contract

The helper reads only the formation flags already set by the KRG country transaction. Because those flags are mutually exclusive in the existing formation path, one clause is selected for each foundation report. The default branch preserves readable text for unusual or legacy scopes. Event IDs, option effects, decision gates, focus routes, event-log mappings, and catalog-facing fields remain unchanged.

## Validation evidence

The four foundation descriptions reference the existing KRG report events and the new helper. All five helper output keys are present and unique in the Event 016 KRG localization file. Static checks cover Clausewitz block balance, helper-reference count, formation-flag coverage, UTF-8 BOM, duplicate keys, `:0` absence, and the Event 016-only diff. No game launch or live formation scenario was performed.

## Remaining risks

Broader country-specific chains, bespoke project, news, defeat, and remnant art, quantitative balance evidence, live acceptance, and the seven documented generic 3D unit packages remain deferred. No model is produced or referenced by this tranche.
