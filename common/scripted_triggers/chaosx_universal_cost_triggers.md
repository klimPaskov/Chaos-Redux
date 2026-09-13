# chaosx_universal_cost_triggers

This file documents the neutral scripted triggers declared in `chaosx_universal_cost_triggers.txt`.

## universal_cost_source_is_active

Scope: any scope that can read the global source registry.

Input: temporary `universal_cost_source_query_id`.

Result: true only while the source id is present in `global.universal_cost_source_ids`.

Expiry: owners call `universal_cost_source_clear` when their active window ends, so the trigger never fabricates a dynamic global-flag name.

Example:

```txt
set_temp_variable = { universal_cost_source_query_id = constant:universal_cost_framework.black_friday_source_id }
universal_cost_source_is_active = yes
```

## universal_cost_resource_kind_is_native

Scope: payer country.

Input: temporary `universal_cost_affordability_resource_kind`.

Result: true for the sixteen resource kinds implemented by the shared native payment and credit branches: `political_power`, `command_power`, `army_experience`, `navy_experience`, `air_experience`, `manpower`, `fuel`, `infantry_equipment`, `support_equipment`, `support_equipment_1`, `motorized_equipment`, `train_equipment`, `train_equipment_1`, `convoy`, `stability`, and `war_support`.

`custom_adapter` is deliberately false so owner adapters remain responsible for their own payment, refund, and external-resource semantics.

Side effects: none.

Native trigger evidence: `political_power`, `command_power`, `has_manpower`, and `has_fuel` use their documented country resource triggers; `army_experience` uses `has_army_experience`; and all equipment kinds use the documented `has_equipment` trigger with the exact archetype or concrete equipment token recorded by the resource kind.

The native branches for Army Experience, Navy Experience, Air Experience, Stability, War Support, `support_equipment_1`, and `train_equipment_1` are grounded in the installed vanilla documentation at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` and the installed equipment definitions at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/units/equipment/support.txt` and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/units/equipment/trains.txt`.

## universal_cost_component_is_affordable

Scope: payer country.

Inputs: temporary `universal_cost_affordability_resource_kind` and `universal_cost_affordability_amount`.

Result: true for zero or negative amounts, or when the payer has an inclusive amount of one of the sixteen supported native resources.

Unsupported commitment/resource kinds return false and must be checked by the owner adapter.

Side effects: none.

## universal_cost_transaction_is_recorded

Scope: payer country.

Input: temporary `universal_cost_transaction_query_id`.

Result: true when the payer's transaction receipt array contains that logical id, regardless of whether the row is currently refundable, partially refunded, refunded, or settled.

Side effects: none.
