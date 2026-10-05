# Legacy cost localisation review, 2026-10-03

> **Current-status disposition (2026-10-06): superseded by** [takeover_status_2026-10-06.md](../takeover_status_2026-10-06.md) for current famine and migration status.
> This dated document remains historical evidence, with its original acceptance basis, source snapshot, audit outcome, and validation limits scoped to the work described below.
> This reconciliation grants no new design acceptance and upgrades no historical evidence to current or native validation.

Disposition: stable localisation source review implemented, final receipt and guard-tooltip review pending parent readiness.
The parent assigned read-only review of the accepted legacy affordability integration.
Only this new handoff is owned by the auditor.
No source, existing handoff, workbook, asset, Git index, or runtime state was changed.

## Acceptance and scope

The parent acceptance source is `docs/plans/famine_and_migration_system_plans/legacy_cost_affordability_parent_acceptance_20261003.md`.
It preserves all 25 nominal fee tuples, exact resource types, and the three four-resource rows.
The binding decision prompt permits four spendable types.
This review therefore neither removes a fourth resource nor treats the preserved rows as a design deviation.
No compact-row or native layout-fit result is claimed.

The decision owner is still integrating start, paid-work, continuation and cleanup guards.
That unfinished source was not judged as a completed implementation in this stable-text pass.
Open Reception remains separate, with its own three getters, six resource labels and two native parent aliases.

## Complete selector and quote mapping

Each row uses `humanitarian_cost_<tier>_is_affordable` as the getter's ready condition and `humanitarian_cost_quote_<tier>` as the ready/blocked amount.
Both amount strings retain their resource icon and integer formatting.
The positive central constant is `humanitarian_legacy_cost.<tier>`.

| Stable getter | Tier | Nominal fee |
|---|---|---:|
| `GetHumanitarianCostPp10Cost` | `pp_light` | 10 |
| `GetHumanitarianCostPp20Cost` | `pp_standard` | 20 |
| `GetHumanitarianCostPp35Cost` | `pp_heavy` | 35 |
| `GetHumanitarianCostTrain5Cost` | `train_light` | 5 |
| `GetHumanitarianCostTrain10Cost` | `train_heavy` | 10 |
| `GetHumanitarianCostConvoy5Cost` | `convoy_light` | 5 |
| `GetHumanitarianCostConvoy10Cost` | `convoy_heavy` | 10 |
| `GetHumanitarianCostSupport50Cost` | `support_light` | 50 |
| `GetHumanitarianCostSupport100Cost` | `support_heavy` | 100 |
| `GetHumanitarianCostInfantry100Cost` | `infantry_light` | 100 |
| `GetHumanitarianCostInfantry250Cost` | `infantry_heavy` | 250 |
| `GetHumanitarianCostFuel500Cost` | `fuel_light` | 500 |
| `GetHumanitarianCostFuel1000Cost` | `fuel_heavy` | 1000 |
| `GetHumanitarianCostAirXp10Cost` | `air_xp` | 10 |
| `GetHumanitarianCostTransportPlanes5Cost` | `transport_planes` | 5 |

Counts: 15 unchanged getter identifiers, 15 component-ready branches, 30 ready/blocked localisation output keys, 15 normal country quote variables, and 18 complete affordability bundles.
Stable-source SHA-256 snapshot recorded during the 2026-10-03 starting-path follow-up, before final guard review:

- `humanitarian_cost_scripted_localisation.txt`: `77EC340FB89385DCC09ECA4E2316CBEFD93FC6A7D53EEE10036DDD147EEF01B4`.
- `humanitarian_cost_l_english.yml`: `BFF77078C1EC76CDB2730C490E2C609E9FCD9034D7DDE25F023DF36D51E21663`.
- `humanitarian_legacy_cost_triggers.txt`: `F8AEF44112E5CCE33A0213A3877B555A3678DEB3343C0291C8E56BBBE6A72EAF`.
- `humanitarian_legacy_cost_effects.txt`: `61DC8C2A4251C197BCFAE5072799F837E43DE537248D29AA48100E740276E38E`.
- `humanitarian_legacy_cost_constants.txt`: `44EBD402A9B1868E26863666F8AEFF5DA70D2B5B862F6E0721507229F19D0496`.

Core line references below retain their inspected working-copy provenance and may move during final owner cleanup.
The resource predicates and bundles total 33 pure production predicates.
No quote appears as affordability or payment authority in these predicates.
The display projection assigns each quote from the matching positive central constant and does not charge, refund, set a category flag, create a receipt, or reveal actor identity.

## All legacy consumer lineages

Each listed base is consumed by the correspondingly named decision with `_cost` removed.
Its blocked and tooltip keys alias that same base.
The displayed getters resolve to the component tiers below, with no omitted fee.

| Base key | Preserved displayed tuple |
|---|---|
| `famine_cost_release_reserves` | pp_standard=20, support_light=50, fuel_light=500 |
| `famine_cost_emergency_imports` | pp_standard=20, convoy_heavy=10, fuel_light=500 |
| `famine_cost_repair_relief_route` | pp_light=10, train_light=5, fuel_heavy=1000 |
| `famine_cost_escorted_relief_convoy` | pp_standard=20, convoy_heavy=10, support_light=50, fuel_heavy=1000 |
| `famine_cost_emergency_airlift` | pp_standard=20, transport_planes=5, fuel_heavy=1000, air_xp=10 |
| `famine_cost_invite_relief` | pp_standard=20, convoy_light=5, fuel_light=500 |
| `famine_cost_evacuation` | pp_standard=20, train_heavy=10, fuel_heavy=1000 |
| `famine_cost_requisition_safer_state` | pp_standard=20, train_light=5, fuel_light=500 |
| `famine_cost_conceal_crisis` | pp_light=10, infantry_light=100, fuel_light=500 |
| `famine_cost_maintain_extraction` | pp_light=10, train_light=5, fuel_light=500 |
| `migration_cost_prepare_evacuation` | pp_light=10, train_light=5, fuel_light=500 |
| `migration_cost_open_departure_routes` | pp_light=10, train_light=5, fuel_light=500 |
| `migration_cost_restrict_departure` | pp_light=10, infantry_light=100, fuel_light=500 |
| `migration_cost_close_border` | pp_standard=20, infantry_heavy=250, fuel_heavy=1000 |
| `migration_cost_evacuate_vulnerable` | pp_standard=20, train_light=5, fuel_light=500 |
| `migration_cost_evacuate_workers` | pp_standard=20, train_heavy=10, fuel_light=500 |
| `migration_cost_negotiate_corridor` | pp_heavy=35, infantry_light=100, fuel_light=500 |
| `migration_cost_controlled_medical_reception` | pp_standard=20, support_heavy=100, infantry_light=100 |
| `migration_cost_distribute_arrivals` | pp_light=10, train_light=5, fuel_light=500 |
| `migration_cost_transit_only` | pp_light=10, convoy_light=5, fuel_light=500 |
| `migration_cost_enforce_closure` | pp_standard=20, infantry_heavy=250, fuel_heavy=1000 |
| `migration_cost_local_integration` | pp_standard=20, support_heavy=100, fuel_light=500 |
| `migration_cost_third_country_resettlement` | pp_heavy=35, train_light=5, convoy_light=5, fuel_light=500 |
| `migration_cost_voluntary_return` | pp_standard=20, train_light=5, fuel_light=500 |
| `migration_cost_forced_repatriation` | pp_heavy=35, train_heavy=10, fuel_heavy=1000 |

The base/blocked/tooltip lineage covers all 25 legacy consumers.
The 26th current consumer is the separate parent-owned Open Reception family.
No missing base, suffix, getter, quote or ready/blocked key was found in the stable reviewed lineage.
No new price, public metric, information panel, category or fourth canonical value was introduced.

## Inclusive readiness source cases

The audit parsed the actual `humanitarian_legacy_cost_triggers.txt` definitions, not an unrelated adapter or a repeated expected-result fixture.
All 15 component bodies use `NOT(native holding < fresh constant)`.
All 18 bundle bodies compose the exact component predicates as conjunctive Boolean calls under `hidden_trigger`.
The small evaluation substitutes numeric holdings for native reader leaves and evaluates those production comparisons and profile calls.

120 parsed-source cases were evaluated:

- 45 component cases, testing one below, exactly at, and one above each fee.
- 18 complete bundles at exactly their full nominal holdings.
- 57 bundle cases with one constituent resource independently one below its fee.

Every component and bundle accepts its exact nominal reserve case and rejects the relevant one-short case.
Every stable resource getter selects its ready branch through the matching production component.
The getter's ready and blocked values reference the matching quote, so an exactly affordable resource has the normal yellow amount and a one-short resource has red in source.
These cases do not prove native resource aggregation, equipment-archetype interpretation, parser support, current-country reader binding, click-time payment, receipt execution, or actual pixel colour.

The distinct non-spend worker support requirement and airlift's separate 50-XP AI condition were not interpreted as additional fees.
The airlift's displayed and central paid air XP amount remains 10.

## First-visible quote and privacy paths

`famine_refresh_decision_phase_from_country` calls the quote projector in the existing country provider.
`migration_refresh_decision_phase_from_country` calls it before the separate reception preparation quote projector.
`famine_register_active_state` projects quotes only after successful active registration, entering the valid OWNER and a distinct valid CONTROLLER at `famine_core_effects.txt:482` and 485.
`migration_register_active_country` projects quotes inside its valid-current-country branch at `migration_core_effects.txt:564`.
Thus a newly registered valid actor obtains its display amounts through existing bounded registration, before relying only on a later phase refresh.

The values are normal COUNTRY variables.
Unscoped getter calls in the existing decision cost base keys remain in the acting-country localisation context and do not read a targeted state's or a foreign country's holdings.
No ROOT/FROM replacement was introduced by the stable changes.
The cost labels show only nominal public fees and per-resource affordability.
They contain no payer receipt names, generation IDs, private actor identity, registry rows, hidden route status or live cohort details.
The quote projector itself neither sets phase flags nor changes the three-value category descriptions.

## Existing texticons

The unchanged icon families resolve in source:

- Political power: vanilla `interface/texticons.gfx:262`, `GFX_pol_power`.
- Convoys: vanilla `interface/texticons.gfx:34`, `GFX_convoy_texticon`.
- Fuel: vanilla `interface/texticons.gfx:123`, `GFX_fuel_texticon`.
- Air XP: vanilla `interface/texticons.gfx:244`, `GFX_air_experience`.
- Transport planes: vanilla `interface/texticons.gfx:1346`, `GFX_unit_transport_plane_icon_small`.
- Infantry equipment: vanilla `interface/texticons.gfx:2015`, `GFX_infantry_equipment_text_icon`.
- Trains: vanilla `interface/texticons.gfx:2563`, `GFX_train_texticon`.
- Support equipment: mod `interface/chaosx_texticons.gfx:90`, `GFX_support_equipment_text_icon`.

No icon was added, changed or substituted.
No texticon fit or rendering result is inferred from these definitions.

## Prose and localisation audit lists

Missing keys: none found on the stable assigned cost lineage.
Duplicate keys: none found on the stable assigned cost lineage.
Scripted-localisation issues: no incorrect component, quote or output-key mapping found.
Dynamic opportunities: the 15 normal quotes now replace static fee numerals without changing their amounts.
Cross-surface mismatch: none found between stable getter readiness, central nominal fees, quote projection and the preserved base strings.
Encoding: checked internally, no assigned YML encoding concern identified.
Vagueness, bloat, obvious explanation, repetition, overcomplication and prose style: the changed labels are icon/amount strings and introduce no prose.
No quotation-bearing surface was changed.
No spreadsheet row is required for this shared system, and no workbook/export was read or edited.

## Final review pending

### Genuine starting-problem source trace

The parent additionally asked whether the current starting history/profile path could publish a visible food problem before first quote projection.
No current source-proven bypass was found, and no startup quote autorun is recommended from this review.
The category's direct owned-state fallback accepts genuine food-stage evidence, but history and event sources contain no direct famine stage or decision-phase writes in the inspected current tree.
All `famine_food_security_active` writers in the core pair with `famine_register_active_state`, including surface context at lines 909–910, historical profile context at 1689–1690, acute-or-worse stage at 1794–1795, trapped demand at 2763–2764, and nuclear reassessment at 3005–3006.
Successful active-state registration projects owner and distinct controller quotes before returning.
The sole nonstable stage publisher is `famine_transition_food_stage`, reached only through `famine_evaluate_food_security` at lines 2080 and 2096.
The evaluator's sole current production caller is `famine_process_registered_state:2683`, dispatched over `global.famine_active_states`.
Pending food-observation processing explicitly calls active-state registration at line 2681 before evaluation.
Supply-strain transition does not itself re-register, but the actual evaluator caller has already entered the registered active/observation path.
Historical bootstrap registers anchor and durable memory flags rather than food-stage reveal flags.
Its live profile application registers the active state before later active-state evaluation.
This establishes the current source-call ordering only and does not establish arbitrary externally supplied history, malformed save state, or native UI scheduling.

The parent must signal that the decision owner's completion and continuation surfaces are ready.
Then this auditor will inspect every newly introduced private paid-work flag and guard tooltip in the final source.
Private receipt checks must remain hidden rather than rely on raw-name flag localisation.
Meaningful public blocked text should explain the actor, target or paid-work requirement without exposing the internal flag name or promising movement, a safe route or successful delivery.
No claim is made yet about those unfinished guard consumers.

## Reference and native evidence limits

Skills applied: chaos-redux-events, chaos-redux-decisions-missions and chaos-redux-subagents.
AGENTS.md and the parent's accepted boundary were read.
The same-agent earlier review read offline `Decision modding - Hearts of Iron 4 Wiki.md:311`–329, installed decision `_documentation.md:1`–45, and the direct vanilla custom-cost base/blocked precedent at `toa_decisions_l_english.yml:340`–341 with its `AFG.txt:490`–496 consumer.
The pure predicate documentation cites installed country-resource reader sections and the offline scripted-trigger rules, with native scope and constant parsing still separate validation obligations.

The parent's current MCP inspections recovered partial metadata, while linked resource-body access and numeric scenario coverage remain unresolved.
No repeated heavy MCP call was made for this source-only review.
No production GUI render, inline layout-fit, stockpile aggregation, native equipment-token equivalence, callback exclusivity, AI probability result, game launch or log evidence is claimed.
No new artifact URI was returned.
No gameplay simplification was made by this auditor.
