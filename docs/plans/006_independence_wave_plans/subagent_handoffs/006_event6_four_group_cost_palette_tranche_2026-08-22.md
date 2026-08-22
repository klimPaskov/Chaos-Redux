# Event 006 four-group decision cost palette tranche

Date: 2026-08-22.

Owner: `/root`.

Disposition: **SOURCE-IMPLEMENTED / PARTIAL**.

This tranche narrows the active shared Event 006 actions that previously combined strategic, security, administration, transport, equipment, manpower, army experience, stability, war support, and civilian-factory charges into one visible action. Every changed action now exposes and pays at most four spendable resource groups, with the affordability trigger, payment effect, normal text, blocked text, and factory reservation kept in the same contract.

## Changed actions

| Surface | Affordability trigger | Payment effect | Visible groups |
| --- | --- | --- | --- |
| DM-51 `independence_wave_prepare_border_ultimatum` | `can_pay_independence_wave_border_ultimatum_cost` | `independence_wave_decision_pay_border_ultimatum` | stability, command power, infantry equipment, support equipment |
| DM-52 `independence_wave_integrate_settled_district` | `can_pay_independence_wave_integration_cost` | `independence_wave_decision_pay_integration` | command power, manpower, infantry equipment, support equipment |
| DM-56 `independence_wave_integrate_member_region` | `can_pay_independence_wave_integration_cost` | `independence_wave_decision_pay_integration` | command power, manpower, infantry equipment, support equipment |
| DM-57 `independence_wave_sponsor_another_breakaway` | `can_pay_independence_wave_coordinated_operation_cost` | `independence_wave_decision_pay_coordinated_operation` | command power, convoy or trains, infantry equipment, support equipment |
| DM-58 `independence_wave_coordinate_reclamation_fronts` | `can_pay_independence_wave_coordinated_operation_cost` | `independence_wave_decision_pay_coordinated_operation` | command power, convoy or trains, infantry equipment, support equipment |

The dedicated payment effects remove the old composite double-charge path, so DM-51 no longer pays strategic plus major security, DM-52/DM-56 no longer pay administration plus standard security, and DM-57/DM-58 no longer pay diplomatic plus major security. DM-51, DM-52, DM-56, and DM-57 no longer reserve an additional civilian factory through a decision modifier.

## Shared palettes

`independence_wave_decision_pay_strategic` and `can_pay_independence_wave_strategic_cost` now omit war support while retaining stability, command power, transport (convoy or trains), and the civilian-factory reservation. The Pacific island strategic payment and trigger likewise omit war support, and its custom cost text is defined once in `006_independence_wave_pacific_l_english.yml` with matching tooltip and blocked keys.

The same contract is now applied to the six package strategic palettes for Komi, Kosovo, Kuban, Ruthenia, Tatarstan, and Udmurtia. Their package triggers and payment paths retain stability, command power, transport, and the package factory reservation without a separate war-support charge.

The Transcaucasus IW-070 garrison, IW-071 command, and IW-072 oil projects now use the material-security helper: command power, manpower, infantry equipment, and support equipment. Their previous duplicate Army Experience charge was removed from the trigger, payment effect, and all three cost strings. IW-070 depots, IW-071 rail, and IW-072 rail retain their administration, transport, and factory contracts.

FORM-03 Reopen Charter Talks now discloses stability, command power, transport, and its three-factory reservation; the shared strategic payment already uses the same four groups. IW-058 Fortify the Mountain–River Corridor now commits infantry equipment, support equipment, trains, and civilian capacity. Its transaction remains synchronized, with the command-power field explicitly zeroed rather than charged or hidden from the cost text.

The remaining package and formable outliers are now synchronized as well. FORM-05 proclamation uses the strategic payment plus its one-factory assignment; it no longer adds a second light-administration manpower charge. FORM-05 reopening and first-board reconvening retain the strategic/factory palette. FORM-05 defense and coastal-warning projects use material security (manpower, infantry equipment, support equipment) plus their factory assignment, without Army Experience. FORM-39 shipping uses stability, command power, transport, and manpower, with its civilian-factory condition disclosed as a gate rather than a payment. FORM-39 plebiscites use command power, manpower, infantry equipment, and support equipment. MNT durable sovereignty retains stability, command power, transport, and its one-factory assignment.

A source-linked localisation scan covers 187 active `custom_cost_text` keys and reports zero keys above four normalized spendable groups. This is a bounded cost-surface result, not a whole-event balance or runtime acceptance claim.

## Files changed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_triggers/006_independence_wave_pacific_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_pacific_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_transcaucasus_package_triggers.txt`
- `common/scripted_effects/006_independence_wave_transcaucasus_package_effects.txt`
- `common/decisions/006_independence_wave_iw043_iw058_decisions.txt`
- `common/decisions/006_independence_wave_form05_decisions.txt`
- `common/scripted_triggers/006_independence_wave_form05_triggers.txt`
- `common/scripted_triggers/006_independence_wave_form39_triggers.txt`
- `common/scripted_effects/006_independence_wave_form39_effects.txt`
- `common/scripted_triggers/006_independence_wave_montenegro_package_triggers.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `localisation/english/006_independence_wave_pacific_l_english.yml`
- `localisation/english/006_independence_wave_transcaucasus_l_english.yml`
- `localisation/english/006_independence_wave_form03_l_english.yml`
- `localisation/english/006_independence_wave_iw043_iw058_decisions_l_english.yml`
- `localisation/english/006_independence_wave_komi_l_english.yml`
- `localisation/english/006_independence_wave_kosovo_l_english.yml`
- `localisation/english/006_independence_wave_kuban_l_english.yml`
- `localisation/english/006_independence_wave_ruthenia_l_english.yml`
- `localisation/english/006_independence_wave_tatarstan_l_english.yml`
- `localisation/english/006_independence_wave_udm_l_english.yml`
- `localisation/english/006_independence_wave_form05_l_english.yml`
- `localisation/english/006_independence_wave_formable_registry_l_english.yml`
- `localisation/english/006_independence_wave_montenegro_l_english.yml`

## Evidence

The four Event 006 static audits passed after the source edits: allocator, country API, strict flag-family, and SCN-008 scenario-matrix audits. The current `hoi4.event_inspect` lint returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics; its artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ca737876d7cf8f0fc52a5849bab98f77f7a57bc39280d5bce920c37ae0e207f3/8d4bac0dd460c49bf4011db0c4c598af03044c6fdc2fef2253cd3f657e030bed/event-lint-a6101ec18545.json`. The matching bounded state render produced JSON, SVG, and PNG artifacts under `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8d2226092038940c2d16738a0be4538f2bddbf1946874efe144a64e10086532b/8e4f9e5d088c4d9e000c8383dcfd5b419fe314eddde17b37330cf775c54f9dd5/event-state-a6101ec18545-manifest.json`. Workspace-wide helper projections remain deferred by the MCP analysis boundary. The required probability discovery pass on `common/decisions/006_independence_wave_decisions.txt` used `decision_ai_will_do` and returned `PROBABILITY_SOURCE_INSPECTED` with ten candidates, zero statically available candidates, 87 required inputs, and zero unresolved inspect diagnostics; its current artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5d67cf18cc72580da3709d2516f4a135c6f28977a9d56f0229705a48a07a865c/efb0a67992db9c2c67817508a63b832cd909cbaea9c14bcfac7b59c5e098b0b5/probability-inspect-ca15c59248ac.json`. Both are structural evidence only because the runtime candidate pool is incomplete.

## Remaining limits

This tranche does not claim whole-event completion. The active custom-cost localisation scan is within the four-group ceiling, but package cost prose, dynamic or automatic DM-01 pre-activation disclosure, decision category density, and same-scenario probability evaluation/compare remain queued. Event 006 also remains HOLD/PARTIAL at the current 32 content-attested packages of 193 selectable non-overlay rows, with formable, GUI, super-event, and runtime receipt gates still unresolved.

## Final reconciliation evidence — 2026-08-22

The follow-up reconciliation removed the remaining stale wording in the Transcaucasus IW-070 garrison, IW-071 command, and IW-072 oil strings, and removed the obsolete war-support wording from the FORM-05 reopening description. The Pacific strategic tooltip/blocked keys are now defined once beside the base key, and the shared strategic blocked string uses the `independence_wave_decision_cost` constant namespace.

The four static Event 006 audits were rerun successfully after this reconciliation. The current read-only `hoi4.event_inspect` state-flow pass returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics and linked artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/765682d137f5aaa106e4c4d91c297780e1dc3383158872247cecc22aa1724897/606af29a7afb63a2bb052db95e57b823bcd9fda0775f5402a59952a49ff74f9a/event-state_flow-43f28961e452.json`. The MCP validation remains partial because workspace-wide helper projections are deferred; this is not a gameplay completion claim.
