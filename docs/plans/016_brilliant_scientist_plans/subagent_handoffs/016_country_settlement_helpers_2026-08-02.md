# Event 016 country-specific settlement helper handoff

Date: 2026-08-02

Status: implemented as the bounded helper tranche for the accepted country-specific institutional settlement addendum. No commit was created.

## Scope

This tranche adds four guarded settlement resolvers, the shared settlement delta and AI constant tables, and facility and custody receipt selectors. The helpers keep the existing `.5` assistant resolvers and bounded Directorate meter effects. They do not add events, transfer copies, decisions, focus routes, GUI elements, countries, characters, projects, evolution entries, or assets.

## Files changed

- `common/scripted_effects/016_brilliant_scientist_context_effects.txt` adds the four Event 016 settlement resolvers.
- `common/script_constants/016_brilliant_scientist_country_settlement_constants.txt` adds settlement deltas and AI factors.
- `common/scripted_localisation/016_brilliant_scientist_host_flavor_scripted_localisation.txt` adds facility and custody receipt selectors with empty fallbacks.
- `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_country_settlement_helpers_2026-08-02.md` records this handoff.

## Identifiers and behavior

Settlement resolver effects are `brilliant_scientist_context_settle_british_research_associations`, `brilliant_scientist_context_settle_american_federal_contracts`, `brilliant_scientist_context_settle_soviet_academy_plan`, and `brilliant_scientist_context_settle_japanese_riken_council`.

Each resolver checks all four `brilliant_scientist_country_settlement_*` receipt flags inside one mutually exclusive guard. It writes only its own receipt, calls the named existing assistant resolver once, and applies only the additional settlement delta through `brilliant_scientist_change_mandate`, `brilliant_scientist_change_dependence`, `brilliant_scientist_change_exposure`, `brilliant_scientist_change_project_capacity`, `brilliant_scientist_change_independent_capacity`, or `brilliant_scientist_change_grievance`. A repeated call or a call after another settlement is inert.

The receipt flags are `brilliant_scientist_country_settlement_british_research_associations`, `brilliant_scientist_country_settlement_american_federal_contracts`, `brilliant_scientist_country_settlement_soviet_academy_plan`, and `brilliant_scientist_country_settlement_japanese_riken_council`. They remain host-local institutional history and are not added to transfer-copy or Kruger State formation blocks.

The scripted-localisation selectors are `GetBrilliantScientistCountrySettlementFacilityClause` and `GetBrilliantScientistCountrySettlementCustodyClause`. They map the four receipt flags to `brilliant_scientist_country_settlement_facility_british`, `brilliant_scientist_country_settlement_facility_american`, `brilliant_scientist_country_settlement_facility_soviet`, `brilliant_scientist_country_settlement_facility_japanese`, `brilliant_scientist_country_settlement_custody_british`, `brilliant_scientist_country_settlement_custody_american`, `brilliant_scientist_country_settlement_custody_soviet`, and `brilliant_scientist_country_settlement_custody_japanese`. The safe empty branches are `brilliant_scientist_country_settlement_facility_empty` and `brilliant_scientist_country_settlement_custody_empty`.

## Constants

`brilliant_scientist_country_settlement_delta` owns the exact additional values used by the resolvers. British adds Exposure `+5` and Independent Capacity `+5`. American adds Dependence `+5`, Exposure `+5`, and Project Capacity `+10`. Soviet adds Dependence `+5`, Project Capacity `+5`, Independent Capacity `+10`, and Grievance `+5`. Japanese adds Mandate `+5`, Dependence `+5`, Project Capacity `+5`, and Grievance `+10`.

`brilliant_scientist_country_settlement_ai` owns `option_base = 10`, `option_preferred_factor = 2.25`, `option_cautious_factor = 0.50`, `reaction_preferred_factor = 1.50`, and `reaction_cautious_factor = 0.70`.

## Total vectors

The totals below are the current base assistant resolver vectors plus the additional settlement values above. The column order is Mandate, Dependence, Exposure, Project Capacity, Independent Capacity, and Grievance.

| Settlement | Total vector |
| --- | --- |
| British research associations | `+5, -10, +15, +5, +20, -15` |
| American federal contracts | `+10, +5, +10, +15, +5, -5` |
| Soviet Academy plan | `+5, +20, -5, +15, -5, +20` |
| Japanese RIKEN council | `+15, +5, +5, +10, +5, +5` |

## Validation

- Read-only `hoi4.event_inspect` lint was run for `chaosx.nr16.5`, `chaosx.nr16.7`, and `chaosx.nr16.8`. Each returned `status: ok`, `EVENT_INSPECTED_PARTIAL`, no blockers, and zero blocking diagnostics. The linked artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/525b8ce84cc18101e218c974eb66dfb73d1a68497b2a31f7e864a33d40a0d56d/ed01b256c383cb15f46d3474028795dab69586b925da5afadc2f9bf50969768e/event-lint-c956d1f97582.json`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d85af875ac6915670d81274bc2e5ba6855216272c393fbc8621c60021080b6c1/ba06d5bc3944a8b3b6bdc9857c0f3416c6fa511aea03290dbcbb2201e2b089ae/event-lint-c956d1f97582.json`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4561ec541dfb3e14004c5c191ff86f1f25645438ca8f40dd17f8adedf82ed7f2/552a210fea683272745309c503f5bd895964322deb460a965b1f4ef2b9e52ee5/event-lint-c956d1f97582.json`.
- The same three touched script files have balanced braces and contain no unsupported `<=` or `>=` operators.
- The four total vectors were recomputed from the existing assistant resolver values and the new constant deltas. They match the accepted addendum exactly.
- The four event call sites resolve to the four helper identifiers, and each selector maps to the matching parent-owned localisation keys.

## Skipped meaningful validation

No HOI4 process was launched and no live save or popup test was run because runtime validation belongs to the parent and user. The probability inspector was not run by this helper tranche because the parent owns the changed `.5`, `.7`, and `.8` AI option pools. The Event Chain Viewer reports remain partial because workspace-wide helper and lifecycle projections were deferred by the installed adapter.

## Risks and follow-up

- The parent must retain the four `.5` call sites and the eight receipt clause keys in the matching Event 016 localisation file.
- The parent must keep the four receipt flags out of ordinary transfer and Kruger State formation copy blocks as required by the addendum.
- The empty selector branches intentionally resolve to empty strings for countries without a pilot settlement.
- The MCP evidence is structural and partial. It is not a substitute for live presentation or balance acceptance.
