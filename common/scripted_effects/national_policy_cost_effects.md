# National policy native law costs

The five native law slots are `refugee_reception`, `civilian_departure`, `chemical_use_policy`, `biological_use_policy`, and `nuclear_use_policy`.
Native law selection owns the displayed Political Power price, affordability, and debit.
These helpers neither spend Command Power nor add a second Political Power charge.
The law owner supplies the base costs of 100 Political Power for the civilian slots and 150 for the warfare slots.

## Helper contract

All helpers run in the country whose law price is being changed.
There is no scope pointer or event target input.

| Helper | Inputs and defaults | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `national_policy_initialize_cost_modifiers` | No explicit input. Reads the live sale flag and `constant:national_policy_cost.chaos_warfare_factor`. | Stores the doctrine factor and idempotently installs its permanent binding. During a sale, calls `black_friday_native_sale_apply` to install the civilian carrier, receipt flag, and both warfare sale variants. Forces refresh. | `national_policy_initialize_country` in the policy law owner. |
| `national_policy_detach_cost_modifiers` | None. | Removes all three owned warfare bindings if present. Preserves variables. Internal only. | `national_policy_refresh_sale_cost_modifiers`. |
| `national_policy_store_warfare_sale_cost` | Required caller-set temporary `national_policy_external_cost`, containing the slot's external cost factor. Reads the stored doctrine factor and existing global sale ratio. No default input. Caller initializes temporary outputs `national_policy_sale_cost` and `national_policy_sale_doctrine_cost` to zero before the first call. | Writes those two caller-owned numeric temporary outputs and leaves the input unchanged. Uses local temporary arithmetic. Its caller stores the outputs in six explicit persistent slot fields. | Three explicit `= yes` calls in `national_policy_refresh_sale_cost_modifiers`. |
| `national_policy_refresh_sale_cost_modifiers` | Existing Black Friday ratio and active sale lifecycle. | Detaches owned bindings, forces refresh, calculates both sale variants per warfare slot, restores all three bindings, forces refresh. | `black_friday_native_sale_apply`, including its active-sale policy initialization caller. |
| `national_policy_remove_sale_cost_modifiers` | None. | Removes both sale bindings, clears all six sale factor variables, preserves the permanent doctrine binding and factor, and forces refresh. Idempotent. | `black_friday_native_sale_remove`. |

Example:

```text
# Country setup, after native policy laws have been assigned.
national_policy_initialize_cost_modifiers = yes

# Numeric helper usage after all owned modifiers have been detached and refreshed.
set_temp_variable = { national_policy_external_cost = modifier@chemical_use_policy_cost_factor }
set_temp_variable = { national_policy_sale_cost = constant:black_friday_event.zero }
set_temp_variable = { national_policy_sale_doctrine_cost = constant:black_friday_event.zero }
national_policy_store_warfare_sale_cost = yes
set_variable = { national_policy_sale_chemical_use_policy_factor = national_policy_sale_cost }
set_variable = { national_policy_sale_doctrine_chemical_use_policy_factor = national_policy_sale_doctrine_cost }
```

No helper charges a resource, grants a law, changes policy authority, or starts recurring work.
There are no new on-actions or world iterators.

## Cost composition and tuning

`national_policy_cost.chaos_warfare_factor` is -0.25.
Eligibility is the live country predicate `has_doctrine = chaos_warfare`.
A historical adoption flag never supplies eligibility.
The three warfare fields are absent from `black_friday_native_sale` so a second sale contribution cannot stack with the policy totals.
The two civilian fields use that ordinary sale carrier and its existing read, subtract, store, and clear contract.

Let `b` be a warfare slot's external native cost factor, `d` the doctrine factor, and `r` the snapshotted Black Friday payment ratio.
All owned warfare modifiers are detached and refreshed before reading `b`.

| Enabled variant | Owned contribution |
| --- | --- |
| Doctrine active, sale inactive | `d` |
| Sale active, doctrine absent | `(r - 1) * max(0, 1 + b)` |
| Sale active, doctrine active | `d + (r - 1) * max(0, 1 + b + d)` |

Both sale variants remain bound during the sale and their `enable` predicates are mutually exclusive.
The engine's daily modifier refresh therefore handles doctrine acquisition or removal without recomputing a stale sale offset.
The adoption owner can force the same refresh immediately after changing doctrine.
An immediate mid-day removal refresh is not established by the available engine callbacks.
Changes to external factor `b` still require an existing explicit sale refresh, as on other Black Friday native factors.

For `b = 0`, the unrounded native prices are:

| State | Civilian PP | Warfare PP |
| --- | ---: | ---: |
| No doctrine, no sale | 100 | 150 |
| Chaos Warfare, no sale | 100 | 112.5 |
| 50% sale, no doctrine | 50 | 75 |
| 50% sale, Chaos Warfare | 50 | 56.25 |
| 75% sale, no doctrine | 25 | 37.5 |
| 75% sale, Chaos Warfare | 25 | 28.125 |

These are modifier arithmetic, before the native law consumer's display and debit quantization.
The native consumer remains the single owner of affordability and charging.

## Lifecycle and achievement accounting

Policy initialization installs the permanent doctrine binding for each eligible initialized country.
Black Friday's existing activation and country-refresh paths install both sale bindings.
Expiry clears the active global flag before the existing recipient cleanup removes sale bindings and variables, restoring the doctrine-only factor where eligible.
No global target, country registry, flag polling loop, or additional daily country scan is introduced.

`black_friday_engine_purchase_read_laws`, its activation snapshot, expiry comparison, and cleanup include all five law slots.
Policy options use their owner enums and exact `has_idea` ids.
They contribute the existing Laws achievement family only when the original natural-sale gates and net Political Power spending inference pass.
This inherits the existing limitation that unrelated PP loss may coincide with a change and same-day PP gains can conceal a real purchase.
It does not produce an individual payment receipt.

## Engine references and validation limits

Installed `documentation/modifiers_documentation.md:1296-1303` defines `<IdeaGroup>_cost_factor` in country scope, revision `00a0eca6d2b3a70ce4b8a0d38997dd609aa0c9349ddcd04c8cac92849425be7e`.
The installed modified-type list enumerates base-game slots and cannot enumerate this mod's five new slots.
Their actual slot and law definitions are owned by the policy law package.
Installed `common/dynamic_modifiers/0_dynamic_modifiers.txt:3-27` supplies the `enable` and daily-refresh precedent.
Installed `documentation/effects_documentation.md:4372-4382`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents forced refresh.
Offline `paradox_wiki/Modifiers - Hearts of Iron 4 Wiki.md:108-122`, revision `fe41a26f2b8d3b8e78a9b0dea9ce1a55f001d1e27886807a0a3fb2d2f535f14f`, documents daily dynamic-value evaluation.
Installed `documentation/triggers_documentation.md:3748-3765`, revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`, confirms that `has_doctrine` tests the currently active doctrine.
Installed `documentation/effects_documentation.md:7820-7827`, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, documents copying another variable into temporary storage.
The numeric helper is invoked with `= yes` and the three slot reads and persistent stores are explicit.
It requires no named argument substitution or literal field injection.

Source-semantic scenario tests cover initialization, both sale ratios, repeat refresh, adoption and removal inside and outside sale, sale expiry, new-country binding, external discounts and surcharges, exact enabled-variant count, and all five law accounting paths.
They do not establish the running game's native price rounding, tooltip output, affordability boundary, or observed debit.
The helper does not replace native pricing with a scripted approximation.

## Assets and future work

These hidden cost bindings require no icon, GFX entry, sprite, or GUI change.
Their player-facing law names, prices and policy explanation belong to the policy law package.
If another owner changes one of these external slot factors during a sale, that owner should use the existing explicit sale refresh contract.
Any future doctrine-removal callback could force refresh at that exact boundary while retaining the same formulas.
