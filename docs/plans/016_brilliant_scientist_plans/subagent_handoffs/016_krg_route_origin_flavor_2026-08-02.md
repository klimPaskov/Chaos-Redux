# Event 016 Kruger State route-origin presentation handoff

## Scope

This bounded continuation keeps the existing Kruger State route and foreign-integration reports tied to the sovereignty transaction that created the country. It adds the already-registered `GetBrilliantScientistKrgOriginClause` beside the existing carried-portfolio clause on route reports `.10`, `.11`, `.20` through `.22`, `.30`, `.40` through `.42`, `.50`, and foreign-integration reports `.60` through `.64`.

## Changed files

- `localisation/english/016_brilliant_scientist_kruger_state_decisions_l_english.yml`
- `docs/events/016_brilliant_scientist/overview.md`
- `docs/events/016_brilliant_scientist/systems/kruger_state_decisions.md`
- `docs/plans/016_brilliant_scientist_plans/016_core_runtime_handoff_map.md`
- `docs/specs/016_brilliant_scientist_specs/handoffs/016_completion_status.md`

## Runtime contract

- The report event IDs, options, triggers, effects, receipts, event-log rows, pictures, decisions, focus routes, and AI plans are unchanged.
- `GetBrilliantScientistKrgOriginClause` reads only the formation flags already retained by the KRG country package: charter, rebellion, enclave, or takeover.
- The helper has an existing neutral branch, so reports remain safe if a historical or cleanup path has no origin flag.
- No project stage, equipment, unit, technology, meter, reward, diplomatic transaction, evolution, new fire path, or model dependency is introduced.

## Validation

- Confirmed all fifteen route and foreign-integration descriptions already used `GetBrilliantScientistKrgPortfolioClause` and now pair it with the existing origin helper.
- Confirmed every referenced helper and localisation key already exists; no new scripted-localisation block or key was required.
- The edited localisation remains UTF-8 with BOM and contains no `:0` keys.
- No unsupported `<=` or `>=` operator was introduced.
- No model, entity, sprite, or asset file was created or referenced.

## Simplifications and remaining blockers

This is presentation-only content, not a new country-specific event chain. Broader country flavour, quantitative balance evidence, user-owned live acceptance, and the seven deferred generic 3D packages remain outside this tranche. The copied stage-0 source's external redistribution rights remain unresolved.
