# Event 26 Black Friday — current decision, mission, and cost audit

Status: BLOCKED and incomplete. This is a read-only source audit handoff and does not approve Event 26 or claim universal cost coverage.

Audit date: 2026-08-30, against the physical shared worktree at audit time.
Documentation refresh: 2026-09-02 against the current worktree; this refresh changes documentation only.

## Scope and changed file

The complete package under `docs/specs/026_black_friday_specs/`, `AGENTS.md`, the decisions, events, subagent, focus-tree, and event skills, the universal-cost framework documentation, the exact custom and native inventories, the current Chaos Redux source tree, the offline Paradox wiki core pages, and the installed Vanilla documentation and precedents were reviewed.

HOI4 was not launched for this audit, and no save or game log was used; the current worktree includes the parent implementation and its source, documentation, catalog, export, and asset changes.

Changed file from this audit:

- `docs/plans/026_black_friday_plans/subagent_handoffs/decision_mission_cost_audit_current.md`

## Executive result

The earlier requested `2,160` custom trigger and `2,160` custom text target is superseded by the current exact source inventory.

The current anchored exhaustive scan finds `2,224` `custom_cost_trigger` declarations and `2,225` `custom_cost_text` declarations in 81 decision files. The only count difference is the text-only requirement disclosure at `common/decisions/020_black_plague_rat_decisions.txt:923`; the current nuclear-bomb declarations are paired at 63 trigger and 63 text declarations, and the Brilliant Scientist technology-action declarations add eight paired rows.

The current anchored native scan finds `1,328` top-level decision `cost =` declarations in 62 files, consisting of `1,033` declarations not written as the literal `cost = 0` and `295` literal zero/free sentinels.

The native total is confirmed by the current native inventory contract, but that source inventory is evidence of declarations rather than proof of engine display and payment behavior.

The shared universal-cost framework is now exercised by bounded owner adapters in the Event 26 adapter file and in the biological, Japan chemical, Japan biological, Germany Mengele, D'Rhondan alien-infantry, Random Faction, and Africa Elephant owner files, with component receipts, settlement, and owner-specific refund acknowledgements where the source owns a custom payload. This is ten bounded owner tranches covering 104 logical components, not universal owner coverage.

The bounded tranches are five Communist-spread logical actions, seventeen reachable Fury decisions, the Japan chemical campaign attack, biological medical-capacity expansion, CBRN civilian-shelter movement, two Japan biological campaign agents, four Germany Mengele command-power actions, and the D'Rhondan alien-infantry landing reservation. Their source adapters preserve ordinary requirements and effects while quoting, preflighting, paying, recording actual amounts, settling, and acknowledging owner-controlled refunds where applicable, and remain pending live proof. The CBRN diplomacy, CBRN doctrine, CBRN occupation, and genocide-crisis owner audits rejected unsafe partial adapters and remain explicit blockers.

Event 26 registers and clears its source through `common/scripted_effects/026_black_friday_effects.txt`; the exact lifecycle remains source-present and live-unverified.

Event 26 therefore remains blocked by the many unadapted owner surfaces, missing engine proof for native surfaces, missing static variants for inaccessible surfaces, missing refund acknowledgements, and missing current decision-MCP evidence.

## Recomputed inventory

| Surface | Current count | Exact evidence | Disposition |
| --- | ---: | --- | --- |
| Chaos Redux `custom_cost_trigger` | 2,224 in 81 files | Anchored scan of `common/decisions/*.txt` | Current count; 104 logical component rows are source-adapted across ten bounded tranches, while all other owner payment paths remain unproven |
| Chaos Redux `custom_cost_text` | 2,225 in 81 files | Anchored scan of `common/decisions/*.txt` | Current count; the text-only requirement disclosure remains explicitly classified |
| Chaos Redux native `cost =` | 1,328 in 62 files | `docs/plans/026_black_friday_plans/event26_cost_surface_native_inventory.md:6-12` and current scan | Current count; 1,033 are not literal `cost = 0` and 295 are zero/free sentinels |
| Inventory header target | 2,224 / 2,225 | `docs/plans/026_black_friday_plans/event26_cost_surface_custom_inventory.md:11` | Aggregate corrected; bounded owner tranches recorded and owner line inventories match the current scan |

The custom inventory rows identify the exact drift.

- `common/decisions/035_great_depression_decisions.txt` is currently 89 trigger and 89 text declarations, matching the exact inventory row.
- `common/decisions/016_brilliant_scientist_technology_actions.txt` contributes eight paired trigger and text declarations at `:25/:26`, `:47/:48`, `:69/:70`, `:88/:89`, `:112/:113`, `:137/:138`, `:157/:158`, and `:176/:177`; these were absent from the previous documentation snapshot and remain blocked pending an owner adapter.
- `common/decisions/023_sov_nuclear_bombs_decisions.txt` is currently 63 trigger and 63 text declarations, matching the inventory row at `docs/plans/026_black_friday_plans/event26_cost_surface_custom_inventory.md:71`.
- `common/decisions/020_black_plague_rat_decisions.txt:923` remains a text-only `custom_cost_text` declaration for `black_plague_rat_king_execute_terminal_takeover`; the owning block has no matching custom trigger and proceeds to `complete_effect` at `:925`.

The native inventory's current summary is internally consistent: `common/decisions/003_holy_realm_decisions.txt:51` is a zero-cost sentinel, `:103` is a non-zero native cost, `common/decisions/005_soviet_collapse_decisions.txt:14150` is a dynamic native cost, and `common/decisions/006_independence_wave_decisions.txt:1020` is another zero-cost sentinel.

## Universal helper callsite audit

The public contract is documented at `docs/systems/universal_cost_modifier.md:11-21`, with owner requirements at `:67-75`, `:83-89`, and `:116-120`.

The earlier zero-callsite table is superseded by the current registry and owner handoffs. They record 104 bounded logical component rows invoking shared quote, affordability, payment, receipt, settlement, and owner-specific refund paths across ten bounded tranches. Direct callsite totals are implementation snapshots rather than logical-row counts because several owner selectors and effects are reused. This documentation refresh does not claim a universal helper-callsite count, and unadapted owners remain unconnected.

The helper definitions exist at `common/scripted_effects/chaosx_universal_cost_effects.txt:389`, `:561`, `:582`, `:939`, `:1177`, `:1205`, and `:1260`, but definitions are not interception or owner coverage.

The only current Event 26 framework callsites are `universal_cost_source_clear_black_friday` at `common/scripted_effects/026_black_friday_effects.txt:556` and `universal_cost_source_register_black_friday` at `:667`.

The native payment helper has explicit branches only for political power, command power, manpower, fuel, infantry equipment, support equipment, motorized equipment, train equipment, and convoy at `common/scripted_effects/chaosx_universal_cost_effects.txt:605-745`.

It has no automatic owner path for factory commitments, laws, advisors, ideas, technology, operations, equipment designs, special projects, custom currencies, stability, war support, or arbitrary equipment types. MIO assignment and policy costs remain engine-inaccessible in the Event 26 registry, and no Event 26 MIO fields or generic confirmation adapter are installed.

## Named cost-family coverage

Part 4 requires the families at `docs/specs/026_black_friday_specs/026_black_friday_spec_part_4_cost_surface_coverage.md:55-94`, and requires the actual consumer rather than a display string at `:133-154`.

| Family | Current source evidence | Current status and blocker |
| --- | --- | --- |
| Political power | `common/ideas/026_black_friday_ideas.txt:18` and `:127`; bounded adapters in `common/scripted_effects/026_black_friday_effects.txt`, `common/scripted_effects/biological_countermeasure_effects.txt`, and `common/scripted_effects/JAP_chemical_campaign_effects.txt` | Native source factor exists; Communist-spread, Fury, Japan chemical, biological medical-capacity, CBRN shelter, and Japan biological adapters quote and pay bounded PP components, while remaining custom PP owners have no adapter |
| Laws | Economy, mobilization, and trade factors at `common/ideas/026_black_friday_ideas.txt:25-27` and `:134-136` | Native route is source-only; no distinct additional political-law factor was found; custom law actions remain blocked |
| Advisors and personnel | Advisor and staff factors at `common/ideas/026_black_friday_ideas.txt:19-24` and `:28-30` | Native source exists; owner-level display/payment proof is unavailable |
| Command power | Command-ability factor in `common/ideas/026_black_friday_ideas.txt`, leader factors in `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt`, and bounded adapters in the Event 26, Japan biological, and Germany Mengele owner files | Native source covers documented factors; bounded Communist-spread, Fury, Japan chemical, Japan biological, and Germany Mengele owners quote and pay CP components, while other custom CP actions and inaccessible flat costs remain blocked |
| Army, navy, and air experience | Doctrine factors at `common/ideas/026_black_friday_ideas.txt:32-35` and equipment-design factors at `:94-97` | Native source exists for the documented design factors; equipment-upgrade XP fields remain engine-inaccessible and custom experience actions have no adapter |
| Officer corps | Staff, spirit, leader, promotion, and assignable-trait surfaces | Assignable traits are engine-inaccessible; all custom owner paths remain blocked |
| Doctrine unlocks | Doctrine factors at `common/ideas/026_black_friday_ideas.txt:32-35` | Native source-only evidence; no decision inspection or payment proof |
| Equipment stockpile | Native helper branches at `common/scripted_effects/chaosx_universal_cost_effects.txt:669-735` and bounded owner adapters in the Event 26, biological, CBRN, Japan chemical, Japan biological, Germany Mengele, and D'Rhondan files | Native helper branches cover registered aggregate/exact kinds; bounded owners also handle custom payload acknowledgements, while custom and other equipment types have no owner adapter |
| Convoys and trains | Native helper branches at `common/scripted_effects/chaosx_universal_cost_effects.txt:726-745` and bounded CBRN/train owner adapter at `common/scripted_effects/026_black_friday_effects.txt` | CBRN shelter movement quotes and pays exact train equipment through the shared transaction, while other convoy/train owners remain undiscounted or unproven |
| Fuel | Native helper branch at `:653` and `:803` | Helper exists but no owner invokes it |
| Manpower | Native helper branch at `:637` and `:796`, bounded owner adapters in `common/scripted_effects/026_black_friday_effects.txt` | Communist-spread and Fury components invoke bounded native manpower payment where applicable; remaining manpower owners remain unadapted |
| Stability and war support | Current custom direct-payment examples include `common/scripted_effects/035_great_depression_effects.txt:299-324` | No universal branch or owner adapter; floor, precision, receipt, and refund are unproven |
| Civilian, military, and dockyard commitments | Current decisions contain 602 factory-commitment signals, including `civilian_factory_use` such as `common/decisions/006_independence_wave_balkan_decisions.txt:73`; no `military_factory_use` or `dockyard_use` declaration was found in the current decision scan | No generic reservation/payment/refund helper; factory components require explicit owner treatment and D-CF evidence |
| Intelligence agency upgrades | No `agency_upgrade` match exists in the Event 26 idea or dynamic-modifier files | No current native route and no owner adapter; this family is not covered |
| Intelligence operations | Installed operation documentation for `operation_cost`, infiltration, coup, and target-sabotage fields; the corresponding Event 26 relative-factor route is absent from `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt` | Operation costs remain engine-inaccessible because the fields are flat absolute values; custom operation preparation and factory components remain blocked |
| Military-industrial organizations | Installed Vanilla docs expose MIO cost fields at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md:3360-3388`; Vanilla country dynamic-modifier precedent is `common/dynamic_modifiers/wuw_dynamic_modifiers.txt:462-492` | The four MIO fields remain engine-inaccessible in the Event 26 registry; Event 26 installs no MIO flat fields or generic confirmation adapter, and live MIO-panel evidence is unavailable |
| International market and agreements | Licensed-equipment and trade factors at `common/ideas/026_black_friday_ideas.txt:107-119` and `:216-228` | Licensed-equipment factor source is present, but flat license-purchase fields and custom market/agreement fees remain engine-inaccessible or owner-bound and blocked |
| Special projects | Current Chaos Redux has 34 anchored `resource_cost` blocks and installed Vanilla has 47; examples are `common/special_projects/projects/020_black_plague_weaponization_projects.txt:29-30` and `common/special_projects/projects/016_dhrondan_envoy_project.txt:24-25` | Project resource blocks have no universal owner adapter or refund path |
| Diplomatic transactions | Embargo, guarantee, annex, puppet, and trade factors at `common/ideas/026_black_friday_ideas.txt:101-119` | Native fields are source-only; custom diplomatic payments remain blocked |
| State-targeted projects | Current custom/factory owners and project effects | No owner quote/payment/refund path for target-scoped commitments |
| Custom mechanic currencies | No generic resource-kind branch or owner callsite | Blocked pending per-system adapters and quantum definitions |
| Scripted GUI actions | Event 26 specifies existing event and status surfaces and no dedicated scripted GUI at `docs/specs/026_black_friday_specs/026_black_friday_spec_part_9_implementation_crosswalk.md:162` | No Event 26-owned scripted GUI is in scope; shared GUI is not evidence of cost coverage |
| Event options with payment | `events/026_black_friday.txt:18-27` is an informational popup with `ai_chance = 100`, not a paid option | No Event 26 paid option; other paid event options remain owner surfaces |
| Research and design | The Event 26 dynamic modifier contains 672 country fields in both ratios, 5 leader fields in both ratios, and concrete design fields at `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt:15-25`, `:701-710`, and the corresponding design inventory ranges | Source inventory shows 195 equipment-design, 312 module-design, and 157 unit-design fields, but no live designer display/debit/save proof |
| Subject and autonomy actions | Annex and puppet factors at `common/ideas/026_black_friday_ideas.txt:104-106` and `:210-212` | Native source-only; custom subject/autonomy payments remain blocked |
| Trade and resource agreements | Trade and license factors above plus custom agreement owners | No universal adapter for custom fees or commitments |
| Shared stockpile helpers | Native helper kinds at `common/scripted_effects/chaosx_universal_cost_effects.txt:605-745` and owner adapters in the Event 26, biological, CBRN, and Japan chemical files | Bounded owner callsites now use the helper for registered native kinds, but helper existence and bounded use do not provide universal coverage |

## Engine-inaccessible and static-variant surfaces

The following surfaces remain explicit compatibility blockers rather than silently supported rows.

- Flat army/navy leader assignment and preferred tactics use `assign_army_leader_cp_cost`, `assign_navy_leader_cp_cost`, and `choose_preferred_tactics_cost`, documented in installed Vanilla at `documentation/modifiers_documentation.md:1982`, `:1987`, and `:2172`; no relative Event 26 factor route is present.
- MIO assignment and policy costs are documented at `documentation/modifiers_documentation.md:3360-3388`, but the Event 26 source and registry install no corresponding flat fields or generic confirmation adapter; the Vanilla country dynamic-modifier precedent at `common/dynamic_modifiers/wuw_dynamic_modifiers.txt:462-492` is reference evidence only.
- Special-project resource blocks are defined by project owners rather than a shared percentage cost modifier; current examples are `common/special_projects/projects/020_black_plague_weaponization_projects.txt:29-30` and `common/special_projects/projects/016_dhrondan_envoy_project.txt:24-25`.
- The Chaos Redux assignable trait has a static `cost` at `common/unit_leader/chaosx_traits.txt:29-34`.
- The current installed Vanilla scan has 229 anchored `cost =` fields in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/unit_leader/*.txt`; the earlier registry value of 234 is stale.
- Factory commitments require exact reservation, cancellation, timeout, save/load, and restoration evidence because the universal helper has no factory component branch.

No normal, 50 percent, and 75 percent static variant set is installed for any of these surfaces.

The specification only permits a static route when the finite variants share one logical action, one lifecycle, one display/payment source, one AI candidate, and one cooldown state.

## Quote, display, payment, receipt, and refund requirements

The specification requires `discounted_unrounded = ordinary_current_cost * payment_ratio / 10000`, upward quantization, a positive minimum quantum, and unchanged zero and negative classifications at `docs/specs/026_black_friday_specs/026_black_friday_spec_part_3_reusable_cost_modifier_architecture.md:36-77`.

The owner must quote for display, re-quote at payment, check every component, pay once, record actual paid amounts, and settle or refund the actual paid amounts at `docs/systems/universal_cost_modifier.md:67-75` and `common/scripted_effects/chaosx_universal_cost_effects.md:245`.

The ten bounded source tranches use the shared quote, affordability, payment, receipt, and settlement paths for their registered components, with external refund acknowledgements for owner-controlled biological, chemical, and Africa Elephant payloads. They do not provide universal owner coverage, and the remaining owner surfaces do not call the contract.

Event 26's achievement recorder requires a positive transaction id, family id, ordinary cost, and actual paid cost at `common/scripted_effects/026_black_friday_effects.txt:207-214`.

It can confirm or retract pending achievement transactions at `:286-338`; each bounded adapter supplies its registry-defined primary family, while the remaining owners supply no universal receipt.

Expiry clears current achievement progress at `common/scripted_effects/026_black_friday_effects.txt:56-64` while the source itself is cleared at `:553-561`; this does not repair missing owner receipts or refunds.

The current custom display surface is mixed rather than icon-complete.

- Correct icon-first examples include `localisation/english/001_communism_spread_l_english.yml:115` and `localisation/english/007_random_expansion_l_english.yml:111`.
- Literal resource names and prose remain at `localisation/english/035_great_depression_l_english.yml:78-79` and `localisation/english/cbrn_occupation_l_english.yml:19`.
- `localisation/english/020_black_plague_rat_decisions_l_english.yml:154` is a requirement sentence exposed as custom-cost text rather than a spendable cost.
- Event 26 defines source strings at `localisation/english/026_black_friday_l_english.yml:28-34`; the bounded owner adapters consume the shared quote paths, while universal consumption by every custom owner remains unproven.

There is no current complete per-reference texticon proof for all 2,224 purchase-bearing custom text references.

## Mission quality and lifecycle notes

Event 26 owns a global fire-once sale, not a mission category or mission list.

The spec explicitly says it does not create a separate store, decision category, or sale-only purchase list at `docs/specs/026_black_friday_specs/026_black_friday_spec_part_1_event_identity_and_player_experience.md:51-53`, and the implementation crosswalk confirms that a dedicated scripted GUI is not used at `docs/specs/026_black_friday_specs/026_black_friday_spec_part_9_implementation_crosswalk.md:162`.

The current repository scan finds 46 `selectable_mission = yes` declarations, 268 `selectable_mission = no` declarations, and 536 `days_mission_timeout` declarations under `common/decisions`.

These are existing owner surfaces that Event 26 would need to preserve, not Event 26-owned missions.

The current Event 35 mission tranche is an important concrete blocker because it adds 15 paired custom-cost mission rows at `common/decisions/035_great_depression_decisions.txt:2785-3295`.

For example, `great_depression_halt_the_panic` is owned by `common/decisions/035_great_depression_decisions.txt:2775-2808` in the Event 35 crisis surface, with national objective context and no explicit map-region cue in the block.

Its activation requirement is `great_depression_should_activate_halt_the_panic` at `:2778-2779`, its click-time requirement is the objective plus `great_depression_can_pay_emergency_relief` at `:2781-2787`, and its display is `great_depression_cost_emergency_relief` at `:2788`.

Its cancellation path is `:2789-2797`, completion path is `:2798-2800`, timeout/failure path is `:2801-2803`, duration is `constant:great_depression_event.opening_mission_days` at `:2804`, and it is non-selectable at `:2805`.

Its duplicate and active-cap policy is delegated to the parent activation and receipt helpers, while `fire_only_once = no` remains at `:2807`.

The corresponding custom payment trigger checks political power, manpower, fuel, convoys, and civilian-factory availability in `common/scripted_triggers/035_great_depression_decision_surface_triggers.txt:407-603`.

The corresponding direct payment path debits political power, manpower, fuel, trains, convoys, support equipment, stability, and war support and adds a civilian commitment modifier at `common/scripted_effects/035_great_depression_effects.txt:203-350`.

The mission completion helper calls that direct cost path at `common/scripted_effects/035_great_depression_decision_effects.txt:962-973` rather than any universal quote, payment, receipt, settlement, or refund helper.

This illustrates the general mission blocker: owner/context, activation, requirement, duration, complete, timeout/failure, cancel, duplicate guard, cooldown, display, and payment all exist locally, but Event 26 is not integrated at the payment boundary.

## Cognitive-load findings

- Event 26's own lifecycle is compact and its visible state is meaningful: reserved, active, expired, disabled, and the 50 or 75 percent snapshot are defined by `common/scripted_triggers/026_black_friday_triggers.txt:9-60` and the Event 26 localisation at `localisation/english/026_black_friday_l_english.yml:11-41`.
- The global sale does not add visible primary actions or active missions, so it does not itself exceed the six-action or three-active-mission guidance.
- The broad repository surface still exposes many custom actions, including 46 selectable mission declarations, and the owner categories can exceed the intended cognitive budget independently of Event 26.
- Mixed cost prose, hidden custom helper values, and factory commitments are not reliably distinguishable from non-consumed requirements.
- `great_depression_cost_emergency_relief` at `localisation/english/035_great_depression_l_english.yml:78` contains four spendable types but spells out resource names instead of using texticons, while the plague requirement at `:154` is not a spendable cost at all.
- A player cannot currently know that a custom action has the Black Friday price because the owner does not invoke the quote/display contract.

## AI, route-lock, and probability notes

Event 26's informational popup has `ai_chance = 100` at `events/026_black_friday.txt:18-27`; no Event 26 decision or mission `ai_will_do` weight is added by the current source.

The lifecycle route preserves the key global locks: reservation requires the running system, enabled and unfired state, no existing reservation or active sale, and the chaos threshold at `common/scripted_triggers/026_black_friday_triggers.txt:38-49`; natural activation requires reservation, Friday, and the same threshold at `:51-63`.

The activation path snapshots the ratio, marks the event fired, registers the source, refreshes native modifiers, and updates the global state at `common/scripted_effects/026_black_friday_effects.txt:1046-1091`.

Those lifecycle locks do not make custom AI affordability valid.

Custom owners still need discounted affordability, ordinary reserve floors, target validity, route locks, cooldowns, one logical AI candidate, and revalidation at payment.

The callable HOI4 MCP registry has no decision-specific inspect, render, or compare route.

The event route is available but partial: the 2026-09-02 `hoi4_event_inspect` run with selector `chaosx.nr26.1` returned `EVENT_INSPECTED_PARTIAL`, validation false with deferred helper/lifecycle analysis, revision `27c77545e9241b4398d074f7bae0aaedf8ebba6790c26141f6e3508bf4238175`, and graph hash `9231a40d3395079e08c9610848afcd4d0fc93e97e2dd33dcff81f5d140de7291`.

The 2026-09-02 overview render returned `EVENT_RENDERED_PARTIAL` with no selector-specific blockers and layout hash `3ea884981b1b4ab3fcaf97c911a7503b65b619f8757e3164f29a88b151b0d96a`; workspace-wide validation remains false because helper/lifecycle analysis is deferred.

The available probability route freshly inspected `events/026_black_friday.txt` with the `event_option_ai_chance` adapter and returned `PROBABILITY_SOURCE_INSPECTED`, source revision `a477c32d9183b75725e09db4c376b6207faf6cfb97047b2b577b89c455cf75d5`, source hash `135da139b2368e30cf374cdcb389692bc649162f9bf7409dab57350a090b0995`, `poolComplete = true`, `candidates = 1`, `availableCandidates = 0`, `requiredInputs = 0`, and `unresolved = 0`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eab86ce19d442fff7e62eb716544540fad3d998f002fa2a3e2277514a31d133/155fd9cbd71664a2568e3ccef139b912d4a1ae58c6466b419a6c2a883932a2e4/probability-inspect-135da139b236.json`.

No probability comparison is claimed because no stable before/after owner-weight surface exists. The current narrow option evaluation covers only `chaosx.nr26.2.a` at 100 percent across the eight named empty scenarios; the custom-pool inspect returned an incomplete zero-candidate pool and the event-option/custom-pool inspect settings returned `INTERNAL_ERROR`.

No GUI inspect/render evidence is claimed because Event 26 has no Event 26-owned scripted GUI; the shared event log, event details, popup, and status surfaces are explicitly outside the dedicated-GUI route.

## Cleanup and exploit risk

The Event 26 native lifecycle cleanup is present: active ideas, dynamic country modifiers, and leader modifiers are removed at `common/scripted_effects/026_black_friday_effects.txt:408-418` and `:471-505`, source registration is cleared at `:980`, and the active sale is created with its snapshot at `:1046-1091`.

The unresolved risks are at the owner boundary.

- A mixed native/custom action can charge the native cost and its custom debit unless the owner reconciles the logical transaction.
- The bounded Communist-spread adapters preflight their components and record receipts, but a race after preflight can still produce partial payment because no engine-level atomic commit is available.
- A delayed or canceled unadapted custom action can return no money or return the ordinary rather than actual paid amount because no owner refund path is wired; the bounded biological and chemical payload paths acknowledge their external credits explicitly.
- Factory reservations can be treated as absent by the universal resource helper even when the custom tooltip names them.
- AI can evaluate a custom action using ordinary affordability while the player sees no verified discounted price.
- The bounded adapters supply primary-family achievement receipts, but the achievement cannot progress universally because the remaining owners supply no transaction receipt.
- No static normal/50/75 variants exist, so duplicate-variant suppression and one-candidate AI behavior are not demonstrated.

## Severity-sorted blockers

### Critical

1. Only the bounded Communist-spread, Fury, Japan chemical, biological medical-capacity, CBRN shelter, Japan biological, and Germany Mengele tranches call the universal quote/payment/receipt contract; the remaining custom cost owners leave payment, display, settlement, and refund behavior unintegrated.
2. The current custom inventory aggregate is corrected to 2,224/2,225, with the text-only 020 row and the eight paired Brilliant Scientist technology-action rows explicitly recorded and owner line inventories reconciled.
3. Native/custom actions are not reconciled at the transaction boundary, creating double-payment or undiscounted-payment risk.
4. Factory commitments and other unsupported components have no generic quote/payment/refund provider.

### High

1. No decision-specific HOI4 MCP inspection/render/compare route is callable, so native decision display and payment cannot be promoted from source evidence to engine evidence; the available event and probability routes remain partial or narrow.
2. No static normal/50/75 variants exist for engine-inaccessible surfaces.
3. Engine-inaccessible flat leader/tactic, native one-time decision, equipment-upgrade, guarantee, operation, license-purchase, MIO assignment and policy, special-project, assignable-trait, and factory/dockyard commitment surfaces remain unresolved; Event 26 installs no generic route for these surfaces.
4. Intelligence agency upgrades have no Event 26 modifier match and no owner adapter.
5. Custom cost display is not universally icon-first or semantically limited to spendable costs.

### Medium

1. The Event 35 mission tranche contains 15 additional custom owner rows whose activation, timeout, cancellation, direct payment, and custom text paths are not on the universal contract.
2. Event 26 source and lifecycle status are present, but the cost-source localisation is not proven to be consumed by every owner UI.
3. The current event timing render returned a partial artifact with no MCP blockers, while the partial event inspection still defers helper/lifecycle validation.

## Concrete next fixes for the parent

1. Rebuild and freeze the custom registry after the current Event 35 and nuclear-file drift, preserving exact file and line evidence.
2. For each custom owner, decompose one logical action into no more than four spendable component types and keep requirements, targets, cooldowns, reserve floors, and route locks separate.
3. Wire display and payment to the same quote, re-quote at click time, preflight all components, debit once, record actual paid amounts, and settle or refund actual paid amounts.
4. Add explicit external providers and `universal_cost_mark_component_refunded` handling for factories, custom currencies, special projects, and other unsupported components, or record accepted engine-inaccessible evidence and static variants.
5. Reconcile every native/custom overlap before enabling the Event 26 source.
6. Replace literal resource names in spendable cost strings with the correct texticons and move non-consumed requirements out of `custom_cost_text`.
7. Add the same discounted affordability and reserve logic to AI owners; run baseline and comparison probability audits for every changed weighted surface.
8. Do not mark Event 26 complete until the decision-MCP blocker is resolved or explicitly carried as an accepted limitation and the owner registry, receipts, refunds, localisation, and live acceptance evidence are complete.

## Current disposition

Event 26 has a source registration, native modifier source, global reservation/activation/expiry lifecycle, and cleanup path, but it does not currently have universal decision/mission cost coverage. Eight bounded owner tranches are source-adapted through shared quote/payment/receipt paths, pending probability/live proof and universal owner completion.

The current worktree confirms `2,224` custom triggers, `2,225` custom text references, and `1,328` native top-level decision cost declarations across 62 files, including 1,033 nonzero/non-literal-zero declarations and 295 literal zero/free sentinels.

The bounded owners invoke universal quote, affordability, payment, receipt, settlement, and owner-specific refund paths through their adapters; unadapted owners still lack those paths.

The audit is therefore incomplete and blocked; the source implementation is present, but no universal coverage claim is made and Event 26 remains disabled.
