# Event 26 universal-cost architect follow-up

Audit date: 2026-08-30.

Agent: `chaosx_scripted_system_architect`, invoked with `fork_context=false`.

## Disposition

The installed engine exposes no generic owner-independent interception point for `custom_cost_trigger`, `custom_cost_text`, or an arbitrary decision `complete_effect`. The offline Decision Modding reference states that custom-cost declarations describe availability and text while payment remains in the owner completion effect, and Vanilla precedents confirm owner-local resource and custom-currency debits. `meta_effect`, event targets, and dynamic modifiers are caller-invoked mechanisms rather than interception hooks.

Consequently, the 2,175 Chaos Redux custom-cost declarations cannot be covered by one universal wrapper. Each qualifying owner must either call the shared quote/payment/receipt/settlement contract from its own completion path, use a complete normal/50/75 static variant set, or remain an explicitly documented compatibility blocker.

## MIO native route

The four MIO cost fields are valid native modifiers: `military_industrial_organization_design_team_assign_cost`, `military_industrial_organization_design_team_change_cost`, `military_industrial_organization_industrial_manufacturer_assign_cost`, and `military_industrial_organization_policy_cost`. Vanilla carries MIO modifier keys in a country dynamic modifier at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/dynamic_modifiers/wuw_dynamic_modifiers.txt:462-492`, and the installed modifier documentation enumerates the fields at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/modifiers_documentation.md:3360-3388`.

Event 026 now supplies those fields at `common/dynamic_modifiers/026_black_friday_dynamic_modifiers.txt:21-25` and `:706-710`, using the snapshotted baseline or Evolution I sale rate. This is native MIO confirmation coverage and does not intercept custom costs.

## Parent action and remaining risk

The parent updated the MIO rows in `event26_cost_surface_registry.md` to `covered_native` and retained the Event 26 disabled gate. The custom-owner gap, static/engine-inaccessible non-MIO rows, live consumer evidence, MCP comparison gap, and Part 8 live scenarios remain unresolved.

No gameplay files were edited by this handoff and Hearts of Iron IV was not launched.
