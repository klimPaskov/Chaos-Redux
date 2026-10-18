# Physical transport decision costs

This package is the physical logistics payment seam for migration and famine decision consumers.
The C11 restore plan requests fuel and sea transport in place of political power, and the parent accepted the three profiles below within that scope.
It changes no population, food, reception, pressure, policy, route permission, cooldown, AI weight, art, or periodic hook.
Existing genuine equipment payments remain with the decision owner, which composes their inclusive predicates and limits the complete tuple to four cost types.

## Tuning and geography

All raw amounts live in `common/script_constants/migration_transport_cost_constants.txt`.

| Profile | Connected fuel | Disconnected fuel | Disconnected convoys |
| --- | ---: | ---: | ---: |
| `light` | 5k | 10k | 5 |
| `standard` | 10k | 20k | 10 |
| `heavy` | 20k | 40k | 20 |

`migration_transport_state_has_mainland_connection` runs in COUNTRY payer scope and supplies one shared geography predicate to quotes, affordability and display.
For a state owned by the payer, it uses native `is_in_home_area = yes`, which checks the first province's connection to that owner's capital.
The exact owned-state check is `is_owned_by = PREV` inside `var:migration_transport_target`, where PREV remains the paying country.
For a foreign-owned target, it tests a native existing railway connection or buildable railway path from `THIS.capital` to `var:migration_transport_target` in the paying country's scope.
`build_only_on_allied = no` keeps diplomatic ownership from becoming a geographical fee condition, and the action retains its separate control, route-permission and safety gates.
The predicate evaluates its geography only inside an `if` whose limit requires `var:migration_transport_target` to resolve to a populated state, and it returns false for an unset or zero target.
`humanitarian_cost_display_resolve_target` applies the same populated-state check to its resolved output, so a native decision shown without a selected state resolves no target and the cost selectors fall through to the unavailable text.
The existing-connection branch also handles a maximum-level railway for which further construction may be unavailable.
The foreign state's owner-relative home area cannot waive the occupying payer's sea-transport fee.
These are native land-path semantics, not proof of an operational supply route or permission to move people, and native pathing over special terrain or straits remains engine behavior rather than a local simulation claim.
Disconnected state fees include interior states on disconnected landmasses, since supplies can reach those inland destinations through the same sea transport.
Country policy actions use the connected fuel amount and consume no convoys.
Airlifts also consume no convoys, but use state-keyed receipts so concurrent destinations retain independent paid work.
Their refund and completion consume the same state receipt helpers used by other targeted work.
Neither a missing target nor a zero-population state authorizes state payment.

`migration_transport_project_cost_quotes` projects six COUNTRY display-only fuel values from the raw constants divided by `units_per_k`.
Localisation writes those values with one decimal and a literal lowercase `k`.
Affordability and debit never read this display cache.
The migration reception projector calls it at the existing registration and phase boundaries, and famine consumers must call it at their existing equivalent boundaries.
No additional scheduler is needed.
The actual connected/disconnected choice always uses the shared payer-relative predicate, never the display cache.

## Helper map

All public payment, affordability, receipt, refund and forgetting helpers run in COUNTRY scope on the actual payer.
Scripted helpers are called with `= yes`, and triggers also support `= no` for negation.
Dollar macro arguments are not an HOI4 scripted-helper API.
The caller initializes temporary inputs in the current effect or trigger chain before the call.
Temporary `migration_transport_fuel_land`, `migration_transport_fuel_sea` and `migration_transport_convoys_sea` carry the chosen light, standard or heavy profile's three exact constants.
Temporary `migration_transport_target` is the exact STATE pointer assigned from `FROM` or the saved regular event target, and is entered as `var:migration_transport_target`.
Temporary `migration_transport_receipt` is a token of the actual native decision, assigned with `token:<decision_id>`.
Receipt-name fields use `meta_effect` or `meta_trigger` with `[RECEIPT]` bound to `[?migration_transport_receipt.GetTokenKey]`.
Reception preparation passes `token:migration_open_reception`, and an explicit branch preserves its existing `migration_reception_preparation` field prefix.
There are no implicit input defaults.
The table's PROFILE, TARGET and RECEIPT labels describe these temporary inputs rather than call arguments.

| Helper | Inputs | Outputs and side effects |
| --- | --- | --- |
| `migration_transport_state_has_mainland_connection` | TARGET | Read-only owned home-area fast path or foreign-target railway path from the payer capital, shared by quote, gate and display. |
| `migration_transport_state_fuel_is_affordable` | PROFILE, TARGET | Read-only inclusive current fuel check using the selected state's geography. |
| `migration_transport_state_convoys_are_affordable` | PROFILE, TARGET | Read-only inclusive current convoy check, waived only for connected states. |
| `migration_transport_state_cost_is_affordable` | PROFILE, TARGET | Positive state population and both spendable components, shared by availability and custom cost. |
| `migration_transport_policy_cost_is_affordable` | PROFILE | Read-only inclusive connected fuel fee. |
| `migration_transport_quote_state_cost` | PROFILE, TARGET | Temporary raw `migration_transport_fuel_quote` and `migration_transport_convoys_quote`, no payment. |
| `migration_transport_pay_state_cost` | PROFILE, TARGET, RECEIPT | Fresh full quote, saved payer/action/state quantities before one fuel/convoy debit, temporary payment result. |
| `migration_transport_air_cost_is_affordable` | PROFILE, TARGET | Inclusive fuel-only quote for an exact aerial destination. |
| `migration_transport_pay_air_cost` | PROFILE, TARGET, RECEIPT | Saves the payer/action/state fuel quote and zero convoy quantity, then debits fuel once. |
| `migration_transport_pay_policy_cost` | PROFILE, RECEIPT | Saved payer/action fuel quantity and country flag before one debit, temporary payment result. |
| `migration_transport_state_receipt_is_paid` | TARGET, RECEIPT | Read-only proof of a positive paid fuel quantity and retained convoy quantity on this payer/action/state. |
| `migration_transport_policy_receipt_is_paid` | RECEIPT | Read-only positive paid fuel quantity and matching action flag. |
| `migration_transport_refund_state_cost` | TARGET, RECEIPT | Consumes this receipt, then returns its saved fuel and convoy quantities once. No fresh quote. |
| `migration_transport_refund_policy_cost` | RECEIPT | Consumes this receipt, then returns saved fuel once. |
| `migration_transport_forget_state_cost` | TARGET, RECEIPT | Clears only this payer/action/state paid quantities after success. No refund. |
| `migration_transport_forget_policy_cost` | RECEIPT | Clears only this payer/action paid flag and quantity after success. No refund. |
| `migration_transport_project_cost_quotes` | None | Six normal country text quantities in k, no debit or gameplay authority. |
| `migration_transport_state_receipt_is_clear` | RECEIPT, internally resolved target ID | Both exact state receipt fields absent, including rejection of partial stale receipts. |
| `migration_transport_policy_receipt_is_clear` | RECEIPT | Both action flag and saved policy fuel field absent. |
| `migration_transport_publish_state_receipt` | RECEIPT, resolved target ID, fuel/convoy quote temps | Internal helper writes both actual paid fields before debit, preserving the preparation alias. |
| `migration_transport_read_state_receipt` | RECEIPT, resolved target ID | Internal helper fills caller-predeclared `migration_transport_fuel_refund` and `migration_transport_convoys_refund`. |
| `migration_transport_clear_state_receipt` | RECEIPT, resolved target ID | Internal helper clears only this payer/action/state's two paid fields. |

State quantities retain `<decision_id>_fuel_paid_@var:migration_transport_target_id` and `<decision_id>_convoys_paid_@var:migration_transport_target_id` on the payer, with the exact selected state ID as the targeted-variable suffix.
Policy receipts retain `<decision_id>_transport_paid` and `<decision_id>_fuel_paid` on the payer.
The reception-preparation prefix remains `migration_reception_preparation`.
Positive fuel is an actual paid quantity, not a Boolean numeric variable.
Separate states can hold the same action concurrently, separate actions can hold the same state, and another payer cannot refund this country's receipt.
Starts fail closed when either prior state quantity or either policy receipt field remains, including partial stale receipts.
Decision owners retain their existing actor/state/generation-bound work receipt and must prove it at completion or cancellation.
The transport receipt does not replace that gameplay proof.
Successful work forgets payment before retiring native action proof, and failed work refunds from the original payer before retiring it.
Never refund from the state's later owner or recompute a fee after geography has changed.
Native fuel storage capacity can constrain a later refund grant, which is an engine primitive limit rather than a reason to recompute the paid amount.

## Usage and migration

```text
# COUNTRY payer, FROM is the exact selected STATE.
# Use the same predicate in available and custom_cost_trigger.
set_temp_variable = { migration_transport_fuel_land = constant:migration_transport_cost.standard_fuel_land }
set_temp_variable = { migration_transport_fuel_sea = constant:migration_transport_cost.standard_fuel_sea }
set_temp_variable = { migration_transport_convoys_sea = constant:migration_transport_cost.standard_convoys_sea }
set_temp_variable = { migration_transport_target = FROM }
migration_transport_state_cost_is_affordable = yes

# In the existing guarded complete_effect, before publishing work changes.
# Reinitialize the three profile inputs and exact target in this effect chain.
set_temp_variable = { migration_transport_receipt = token:migration_evacuate_vulnerable }
set_temp_variable = { migration_transport_payment_result = constant:migration_transport_cost.zero }
migration_transport_pay_state_cost = yes
# Continue only when migration_transport_payment_result equals one.

# Failed unmoved work, still in the original payer's scope.
# Initialize target and receipt again in each separate cancellation chain.
set_temp_variable = { migration_transport_target = FROM }
set_temp_variable = { migration_transport_receipt = token:migration_evacuate_vulnerable }
migration_transport_refund_state_cost = yes
# Successful work, with the same target/receipt inputs and payer.
migration_transport_forget_state_cost = yes
```

Payment result is temporary zero on rejection and one only on the actual first debit.
Callers consuming that result must predeclare it before the helper call.
Callers consuming the quote helper's temporary outputs must likewise predeclare both quantities before calling it.
The payment helper already does so internally.
The existing `migration_prepare_reception_services` call site uses `standard`, its exact saved preparation state, and `migration_reception_preparation` as the receipt token.
It retains support equipment 100, refunds that same click's support quantity on rollback, and refunds or forgets transport only after its established result proof.
All earlier reception PP payment, refund and affordability code is removed.

The parent migrates legacy decision profiles by replacing each PP/fuel/unconditional-convoy tuple with the accepted transport profile and retaining real equipment costs separately.
Use `migration_transport_light_state_cost`, `migration_transport_standard_state_cost`, or `migration_transport_heavy_state_cost` as a complete transport-only native cost base.
Their `_blocked` and `_tooltip` aliases use the same quote.
Country-only analogues end in `_policy_cost`.
For composed equipment fees, reuse the profile fuel and convoy getters inside the action's existing cost key, with no repeated cost amounts in its ordinary tooltip.
The getters are `GetMigrationTransportLightFuelCost`, `GetMigrationTransportLightConvoysCost`, and `GetMigrationTransportLightPolicyCost`, with matching Standard and Heavy variants.
Each component color uses the same authoritative inclusive affordability component as the payment gate.
Connected state rows omit convoys entirely.

## References and validation

Installed `documentation/triggers_documentation.md` lines 5704-5712 defines state `is_in_home_area`, with source revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` returned by MCP reference search.
Offline `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` line 1850 gives its Boolean overland semantics, with revision `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`.
Vanilla `common/decisions/ENG.txt` lines 7161-7188 uses the native state trigger inside owned controlled state selection.
Installed `documentation/triggers_documentation.md` lines 1884-1918 documents `can_build_railway` state endpoints, optional path/controller priorities and default unrestricted territory pathing, and lines 4603-4624 documents `has_railway_connection` with the same endpoints.
Offline Triggers line 1868 documents state scope/variable endpoints, and lines 1979-1996 supplies the corresponding examples.
Installed `documentation/dynamic_variables_documentation.md` lines 179-181 defines the country capital-state reader.
Vanilla `common/national_focus/soviet.txt` lines 8520-8528 uses capital-state variables for railway endpoints, while `common/scripted_triggers/012_africa_triggers.txt` lines 875-894 uses `THIS.capital` and a scoped target in controller-country scope.
Installed `documentation/effects_documentation.md` lines 1252-1267 documents variable equipment amounts, with negative amounts removing stock, and lines 1388-1395 documents country fuel addition.
Installed `documentation/triggers_documentation.md` lines 3835-3843 and 3957-3966 documents country equipment/fuel readers, with offline Triggers lines 1516-1539 documenting their comparison syntax.
Installed `documentation/script_concept_documentation.md` lines 216-248 and `common/script_constants/documentation.md` defines shared constant fixed-point access.
Offline Data structures lines 440-442 gives temporary output lifetime, and line 551 documents targeted `@var:` variable keys.
Offline Decision modding lines 304-329 defines the three native custom-cost localisation keys and the need for a manual debit.
The existing dynamic stockpile helper uses concrete `convoy_1` for actual additions/removals, which this API mirrors while affordability reads the convoy archetype.

Historical C11 source results used `.tmp/c11/migration_costs/test_contract.py`, whose dollar-argument substitution model did not establish native parser support.
Its 45 cases cover all three profiles on connected/disconnected states just below, exactly at and above fuel fees, insufficient sea convoys, duplicate starts, wrong-payer refunds, changed geography, repeated refunds, parallel target receipts, successful forgetting, fuel-only country policies the 20.0k display projection and actual getter color/debit agreement across both land modes for all profiles, foreign-owned occupied islands and mainland, existing maximum rail, and replay after actor-relative geography changes, parallel fuel-only airlift destinations and duplicate aerial starts.
These results are source contract evidence and do not prove native callbacks, rendering, fuel-cap behavior or engine execution.
Reception rollback was reviewed against its existing setter/result proof and all transport operations use the saved exact preparation state.
No AI weights changed.
The broad MCP reference-context request did not return within the bounded work period and was terminated, and the one narrower reference-search request succeeded.
The parameterized effects-file validator returned `SCRIPT_CHECK_PARTIAL`, with `valid = null`, four unresolved `$TARGET$` scopes, `parametersChecked = false` and 39 unchecked argument blocks.
Its documented checks covered syntax, command kind, declared scope, event popups and known mistakes, and did not establish parameter semantics or native execution.
The one corrected standard-profile payment body with explicit FROM STATE binding did not return within the bounded work period and was terminated.
The two targeted reference-read requests likewise did not return within that period, so their exact relevant text was read from the local cited files.
The following source lookup in that request script was never reached, and the vanilla precedent was read locally.
Retrying these unchanged requests has no additional evidence value until the service returns or a parameter-aware check becomes available.
No unrelated helper, asset, population ledger or world periodic hook is added.

Future extensions should use the existing receipt contract for further exact-state physical relief actions, retaining native land-path semantics and the complete action's four-cost budget.

## Cold-load parser repair evidence

The supplied 13 October main-menu log reports invalid PROFILE, TARGET and RECEIPT blocks, unresolved dollar-profile constants, and cascading parse errors in the former helper implementation.
The current API uses caller-owned temporary numeric/scope/token inputs and documented native meta text instead.
The three profile constants, payer-relative geography, every existing receipt name, inclusive fee gates, publication before debit, saved-quantity refunds and duplicate-start guards are retained.
No constant, weight, native decision timer, art or player-facing wording changes.
The preparation alias preserves the exact pre-repair saved field names without trying to tokenize an internal helper name.

The current 50-case transport fixture runs the production helper bodies with conservative child temporary cleanup and mocks only native facts, resource operations and meta interpolation.
It covers fuel boundaries for all profiles and land modes, sea convoy shortage, display/debit agreement, duplicate and partial stale receipts, different payers, concurrent states and actions, geography changes before saved refund, replay, aerial concurrency, preparation alias and caller-owned quote output lifetime.
The maintained famine tests pass all 11 regressions through a temporary meta-text adapter, including actual decision publication, equipment debit, zero-consumption refund and replay on connected and disconnected targets.
The unadapted maintained runner lacks meta-trigger support and therefore cannot execute that transport regression.
These are source-contract results, with no claim of native engine execution, UI rendering or fuel storage-cap behavior.
Exact snapshots, local source citations, changed calls and patch evidence are in `.tmp/live_verification_2026-10-13/migration_load_repair.md`.
