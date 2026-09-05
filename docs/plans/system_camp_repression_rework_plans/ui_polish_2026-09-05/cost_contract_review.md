# Selected-location cost contract review

Disposition: `unresolved` architecture proposal for parent selection of formulas and balance coefficients.
Acceptance basis: the parent authorized a read-only review responding to the user's expensive fixed-cost and misleading-stat complaints, restricted to repression-owned consumers.
This review changes no gameplay, AI weights, GUI source, or shared accounting.
The parent explicitly retains countrywide policy pricing and owns final implementation, balance targets, and realistic GUI fixtures.

## Findings and bounded migration surface

`common/script_constants/camp_repression_rework_constants.txt` owns action IDs in `camp_rework_action` and the four independent payment/requirement families beginning at lines 638, 672, 691, and 705.
These constants centralize numbers but do not make the costs responsive to a selected location.

| Selected action | GUI wrapper in `camp_repression_rework_effects.txt` | Direct targeted decision in `camp_repression_generic_decisions.txt` | Current payment |
| --- | --- | --- | --- |
| Labor project | `camp_rework_gui_start_labor_project`, line 3898 | `generic_redirect_labor_to_construction`, line 301; extraction counterpart at 424 | 30 PP, 120 trucks, 18 trains, 180 support equipment |
| Inspection | `camp_rework_gui_inspect_selected_site`, line 3977 | `generic_inspect_active_site`, line 818 | 45 PP |
| Dismantlement | `camp_rework_gui_begin_selected_dismantlement`, line 4015 | `generic_dismantle_detention_network`, line 856 | 60 PP, 6,000 manpower, 180 support equipment |
| Evidence order | `camp_rework_gui_destroy_selected_evidence`, line 4072 | `generic_destroy_evidence_before_retreat`, line 776 | 25 PP, 5,000 manpower, 20 CP, 180 support equipment |
| Existing restricted order A | `camp_rework_gui_apply_selected_chemical_method`, line 4095 | `generic_restricted_contaminated_site_escalation`, line 684, first eligible branch | 60 PP plus the existing abstract stock item |
| Existing restricted order B | `camp_rework_gui_apply_selected_biological_method`, line 4113 | Same decision, second eligible branch | 60 PP plus the existing abstract stock item |

The two restricted identities and their existing stock selection, outcomes, and maintenance remain unchanged by this architecture.
The combined decision chooses its first eligible branch, so its displayed quote must resolve the same branch priority before affordability and payment.
This report does not propose stock-item or casualty tuning for those orders.

GUI IDs come from `camp_rework_action.start_labor_project`, `.inspect_selected_site`, `.dismantle_selected_site`, `.destroy_evidence`, `.chemical_method`, and `.biological_method`.
Decision IDs are distinct `camp_rework_action.generic_*` entries; normalize them to the same quote family without replacing dispatch IDs.

The exact consumer files are:

- `common/scripted_guis/camp_repression_ledger_scripted_gui.txt`: the six matching `camp_gui_*_click_enabled` gates and click handlers.
- `common/scripted_effects/camp_repression_rework_effects.txt`: wrappers above, display refresh, labor start/completion, and selected dismantlement completion/cancellation.
- `common/scripted_effects/camp_repression_action_dispatcher_effects.txt`: targeted labor branches around 132/157, inspection around 176, combined restricted branch around 192, evidence payment at 217, and dismantlement payment at 226.
- `common/scripted_triggers/camp_repression_rework_triggers.txt`: owner quote/affordability predicates and `camp_rework_generic_labor_project_requirements_met` at 2119.
- `common/script_constants/camp_repression_rework_constants.txt`: new owner-specific quote coefficients; retain existing fixed families for non-migrated callers.
- `common/decisions/camp_repression_generic_decisions.txt`: named targeted decisions, `generic_labor_project_cycle`, and `camp_gui_selected_dismantlement_mission`.
- `common/scripted_localisation/camp_repression_ui_scripted_localisation.txt`, `common/scripted_localisation/camp_repression_ledger_scripted_localisation.txt`, `localisation/english/camp_repression_ui_l_english.yml`, and the matching custom-cost strings in `localisation/english/camp_repression_rework_l_english.yml`: dynamic values, resource colours, paid/reserve explanation, and truthful statistics.

## Proposed single quote contract

Use one deterministic owner-local quote calculator, exposed as a scripted trigger that only manipulates temporary variables and returns true after producing the quote.
Suggested name: `camp_rework_prepare_selected_cost_quote`.
Enter the actual state before calling it: GUI uses `var:camp_selected_state_id`, targeted decisions use `FROM`, and execution uses the already validated `var:camp_rework_action_state_id`.
The actor remains the initiating country; do not silently bill the state owner or controller.

Inputs are an explicit action family and live state measurements: `building_level@concentration_camp + building_level@extermination_camp`, `state_population_k`, and `camp_state_reach`.
Population is the territory's population in thousands, not the number of detainees or an inferred custody cohort.
Read `camp_state_reach` as the existing profile value, which may be cached until the owning profile refresh; do not invoke its mutating effect inside a trigger.
Do not use `camp_network_reach` for a single location's quote.

Proposed neutral formula shape, with coefficients left to the parent and auditor:

```text
L = live building levels
P = territory population in thousands
R = existing selected-state reach
Q[action, resource] = round(max(0, B[action, resource]
                                  + KL[action, resource] * L
                                  + KP[action, resource] * P
                                  + KR[action, resource] * R))
```

This is an arithmetic proposal, not an accepted balance target.
Use coefficients only for inputs relevant to the action: physical dismantlement can emphasize levels, labor logistics can respond to levels/population/reach, and administrative inspection can emphasize levels/reach.
Keep zero entries zero rather than inventing additional spendable resource types.
Do not scale costs from observed deaths or change deaths to justify prices.
Keep existing restricted stock-item quotes unchanged unless separately approved; their administrative PP can use the same state quote contract.
Where the parent requires bounds, define them beside the coefficient table and apply them before rounding rather than hiding clamp values inside consumers.

Outputs are positive unscoped temporaries `camp_quote_pp`, `camp_quote_manpower`, `camp_quote_command`, `camp_quote_support`, `camp_quote_motorized`, `camp_quote_trains`, plus any existing abstract order stock token/value and explicit reserve fields.
Initialize every output in the caller before entering a scripted helper, because the offline wiki warns about temporary-variable lifetime across helper boundaries.
Each caller recomputes the same function within its own evaluation; no caller relies on a previous GUI trigger or tooltip evaluation.
Use separate field names for per-row persistent display caches if caching is useful.
A country cache keyed only by selected state is insufficient for targeted decision rows evaluating different `FROM` states.

Suggested helper map:

| Helper | Scope / inputs | Output / side effects | Call sites |
| --- | --- | --- | --- |
| `camp_rework_prepare_selected_cost_quote` | State; action family; initialized temporaries | Quote vector only; no persistent writes | Scripted localisation, affordability, payment preparation |
| `camp_rework_can_pay_selected_quote` | Actor country; prepared quote | Inclusive resource predicate only | GUI enabled trigger, decision `available`, decision `custom_cost_trigger`, execution guard |
| `camp_rework_pay_selected_quote` | Actor country; prepared immutable quote | One debit per nonzero resource; negate separate temporary scratch amounts | Six selected wrappers and targeted dispatcher branches |
| `camp_rework_snapshot_labor_reserve` | Actor country; prepared labor quote | Persistent mission reserve and target identity | Successful labor start before mission activation |
| `camp_rework_clear_labor_reserve` | Actor country | Clears only owner-local reserve snapshot fields | Existing labor success, failure, cancellation cleanup |

The final execution wrapper must validate target, route, and resources before any debit, recompute its quote once, and use those exact rounded outputs for payment.
Execution must not charge PP before a later nested target rejection produces no action.
For targeted decisions, use one custom-cost transaction for all resources with explicit PP handling; do not retain a native PP debit and also add manual PP payment.
The same inclusive predicate belongs in both `available` and `custom_cost_trigger`, with the duplicated raw affordability block hidden when the compact cost row already explains it.
The existing numeric `ai_hint_pp_cost` requirement is a fixed AI hint rather than a dynamic cost source; parent/auditor owns any hint change and associated probability evidence.

## Labor reserve contract

Current payment is 120/18/180 trucks/trains/support; start requirement is separately stored as 160/24/240, and maintained reserve is 40/6/60.
`camp_rework_generic_labor_project_requirements_met` uses strict `>` reserve checks.
An actor holding exactly the documented payment plus reserve therefore fails the current start gate, and an exact retained reserve also fails the ongoing check.
The reserve is not debited a second time, but the displayed payment alone does not explain the full starting requirement.

Compute `start_need[resource] = quote_payment[resource] + quote_reserve[resource]` from the same prepared quote.
Show the compact paid-now vector and a separate concise retained-reserve requirement.
Use inclusive comparisons for both start need and maintained reserve.
Snapshot the chosen reserve into country variables when `generic_labor_project_state_id` and `generic_labor_project_type` are recorded; later selection changes and changed state levels must not rewrite the active mission's requirement.
The mission timeout/cancel paths must clear the reserve snapshot with their existing target/type cleanup and must not debit it again.
Do not replace `camp_rework_equipment_start_requirement` globally, since country-specific mission families also use it.

## Shared payment helpers to preserve

Do not rewrite these functions globally to consume the selected quote:

| Existing helper | Other identified callers |
| --- | --- |
| `camp_rework_consume_labor_project_resources` | Germany rail allocation, war construction, eastern fortifications; Soviet famine relief; Japan dispatch branches; colonial project resources and UK Raj military works |
| `camp_rework_consume_evidence_resources` | Germany evidence destruction; Japan and Soviet dispatch branches |
| `camp_rework_consume_dismantlement_resources` | Germany Auschwitz dismantlement; Soviet Gulag dismantlement; Japan closure dispatch; dormant legacy closure |

Evidence: payment declarations are at `camp_repression_rework_effects.txt:5037`, `:5061`, and `:5073`; other calls are in `camp_repression_major_country_effects.txt:935,946,1039,1199,1239,2409,2486`, `camp_repression_colonial_country_effects.txt:746,1968`, and `camp_repression_action_dispatcher_effects.txt:280,285,290,295,302,333`.
Selected evidence/dismantlement wrappers and their generic dispatcher branches can switch to a new selected payment helper directly.
Labor currently pays inside `camp_rework_start_generic_labor_project_in_action_state` at 5299; split a payload-only start helper beneath the existing paying wrapper or provide a clearly scoped selected-cost entry point so the old wrapper retains its existing contract.
A temporary payment-mode flag that accidentally persists into a country action is unsafe; prefer explicit entry points and no global quote mode.

The four country GUI slots are prepared in `camp_rework_rebuild_country_gui_actions`, lines 2964–3469, and executed by `camp_rework_gui_execute_prepared_country_action` and slot wrappers at 3697–3742.
Their PP field is already displayed and debited through `display_camp_country_action_N_cost`; additional resources still select fixed cost packages.
Germany uses labor/guard/evidence/dismantlement packages; Japan and Soviet slots mix review, labor, and dismantlement; UK/USA/French/Italian/Belgian slots have distinct policy and colonial packages.
Keep this country model separate: some actions affect a fixed site, some an actual network, some country policy, and the dispatcher may select or iterate states.
Changing a selected location in the ledger must not make a countrywide policy arbitrarily cheap.

## Truthful selected-location figures

`camp_rework_apply_monthly_state_effects` resets `camp_site_last_month_deaths` at line 1940.
`camp_rework_record_latest_state_deaths` assigns, rather than adds, `chaos_deaths_change` to it at 1965, and both monthly effects and decision bursts call that function.
It is therefore the latest recorded receipt since the latest reset, not a monthly aggregate, forecast, or cumulative site total.
Even a label such as “latest report” should account for the reset-to-zero behavior; prefer cumulative information for the prominent figure.

`chaos_state_civilian_deaths_total` is accumulated in `chaos_meter_record_state_civilian_deaths_from_deaths_change` in `common/scripted_effects/chaos_meter_effects.txt:2954`.
It includes all recorded civilian causes in the territory and can span different administrations.
Use “Recorded civilian deaths in this state”; do not label it “Camp deaths” or attribute it all to the current actor.
`genocide_deaths` is accumulated on the responsible country in `genocide_credit_state_deaths_to_responsible`, `common/scripted_effects/genocide_crisis_effects.txt:140`.
That country figure is cumulative attributed repression deaths and is not a monthly total or the selected state's total.
All these accounting files remain read-only; no artificial multiplier, new death counter, or receipt rewrite is required for truthful presentation.

## Native support and limits

- Installed `documentation/triggers_documentation.md:2110` explicitly supports `check_variable` against another variable and `compare = greater_than_or_equals`.
- Installed `documentation/dynamic_variables_documentation.md:194,557,743,1168` documents `command_power`, `num_equipment@type`, `political_power`, and `state_population_k`.
  Use those for native inclusive affordability checks, with the same concrete equipment token used by payment.
  Its `manpower` entry at 466 is deprecated and may overflow; prefer `manpower_k` and compare against a quote expressed in thousands for the manpower gate.
- Installed `documentation/effects_documentation.md:1252` explicitly permits a variable `amount` in `add_equipment_to_stockpile` and negative values for removal.
  The existing `camp_rework_gui_pay_political_cost` and owner debit effects already use variable amounts for PP, manpower, and CP.
- Installed `documentation/script_concept_documentation.md:216` and `common/script_constants/documentation.md` support fixed-point `constant:` values in scoped-variable inputs, but only explicitly supported static fields accept constants directly.
- Installed `common/scripted_guis/_documentation.md` documents player-context ownership, enabled/visible trigger blocks, click effects, and dynamic properties.
- Offline `Data structures` covers unscoped temporaries, trigger-side arithmetic, helper-lifetime caveats, and variable localisation; `Scripted GUI modding` covers temporary trigger values; `Decision modding` covers variable PP cost and manual custom-cost debit.
- Vanilla `common/decisions/AST.txt:2481` uses `cost = var:AST_call_on_fascists_cost`; `AUS.txt:1176` uses custom PP/CP affordability.
  A native country-variable cost example does not establish correct target-dependent `FROM` evaluation or eliminate double-payment risk; use the explicit custom transaction contract for migrated multi-resource rows.
- Existing `common/scripted_effects/chaosx_dynamic_effects.txt` and `.md` were consulted for arithmetic and stockpile helpers.
  Their shared registry and the universal cost framework remain untouched; document selected quote helpers in the repression-owned matching markdown.

An example inclusive equipment gate is `check_variable = { var = num_equipment@support_equipment_1 value = camp_quote_support compare = greater_than_or_equals }`.
Quote temporaries are unscoped: `ROOT.camp_quote_support` and `PREV.camp_quote_support` would be wrong.
Normal selected-state pointers and mission fields are scoped and require deliberate actor/state transitions.
Regular event targets can be used transiently inside a payment chain if needed; existing numeric state pointers are sufficient, and no global event target or global daily hook is required.

## Evidence and validation handoff

Read-only GUI inspection succeeded for `repression_ledger_window`, scenario `repression_cost_contract_baseline`, 1920×1080, country object `{tag: GER}`.
Source revision: `dbcf01f39d0345caf198aa63268bf26587767c77f039be1fbaf1281399052481`.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/cb6722f31bf1902de0fde8d203a58a462898761e352960a32ab4c5e13bfe3ccd/c4465a33e89ab1a2ec774f80b64d39d7f1e138612818f88b29d21b4a57031200/gui-inspect.dbcf01f39d0345ca.json`.
Its sparse fixture reports unresolved values and overlapping click regions; this is source-link evidence, not realistic route or visual acceptance.
The parent owns exact before/after fixtures and renders; no further sparse GUI calls were made after that direction.

Read-only event trace used selector `{kind: file, sourcePath: common/decisions/camp_repression_generic_decisions.txt}`, depth 1, 12 nodes, 20 edges, helpers disabled.
It returned `EVENT_INSPECTED_PARTIAL`, revision `f9436dee3f5cb09c3bdc4a12354936955b1f81519dcc79453867ce4504c92978`; workspace helper/lifecycle analysis was deferred, so this does not prove the payment call graph.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b4d90433d37a989af1f97393e16e8c33642ab6976fc736f831677bd92ad11cbc/3d92a2c20088156b24fb248551d9d94e99d8dba360a61ad07a79b268bca75bd0/event-trace-f9436dee3f5c.json`.
Earlier rejected argument shapes were corrected; no MCP write route was used.

Parent validation cases after implementation: equal funds succeeds; one unit below fails; actual debits match displayed rounded amounts; GUI and decision quote the same state identically; changing selection does not alter an active mission reserve; exact reserve survives the first mission check; a disappeared or invalid target causes no debit; country policy payment is unchanged; combined restricted decision quotes its actual selected branch; no duplicate PP or equipment debit occurs through nested helpers.
Compare one-level, multilevel, small-population, large-population, and changed-reach states without assigning casualty-based prices.
No probabilistic helper or balance target was designed here; the separate parent-owned auditor retains AI/weighted evidence responsibility.
No gameplay tests or visual acceptance were claimed for this read-only plan.

Completed: bounded source trace, native support evidence, formula and helper proposal, shared-consumer exclusions, truthful counter semantics, and MCP inspection references.
Unresolved: parent-selected coefficients, final implementation choices, actual runtime arithmetic/payment behavior, and final matched visual/balance evidence.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-scripted-gui`, `chaos-redux-subagents`.
No skill was created or updated.
