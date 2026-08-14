# IW-038 Ruthenia shared-focus hook handoff

## Scope and ownership

This bounded patch wires the five IW-038 Ruthenia package helpers into the existing full `independence_wave_focus_tree` framework.

The patch owns only `common/national_focus/006_independence_wave_focus.txt` call sites and does not create a RUT tree, additive overlay, helper definition, decision, localisation key, icon, or package-core file.

## Changed file and identifiers

- `common/national_focus/006_independence_wave_focus.txt`
- `independence_wave_prepare_capital_administration` calls `independence_wave_rut_focus_convene_provisional_assembly` at line 115.
- `independence_wave_inventory_the_state` calls `independence_wave_rut_focus_guarantee_mountain_communities` at line 157.
- `independence_wave_bind_the_first_oath` calls `independence_wave_rut_focus_integrate_border_guards` at line 180.
- `independence_wave_define_former_host_policy` calls `independence_wave_rut_focus_settle_former_host_ledgers` at line 1410.
- `independence_wave_recognize_fellow_new_states` calls `independence_wave_rut_focus_open_carpathian_corridor` at line 1680.

Every call uses the exact guard `original_tag = RUT` together with `is_independence_wave_rut_package = yes`.

## Route behavior before and after

| Full-framework focus | Before | After |
| --- | --- | --- |
| `independence_wave_prepare_capital_administration` | No IW-038 helper call. | The active IW-038 RUT package invokes `independence_wave_rut_focus_convene_provisional_assembly`. |
| `independence_wave_inventory_the_state` | No IW-038 helper call. | The active IW-038 RUT package invokes `independence_wave_rut_focus_guarantee_mountain_communities`. |
| `independence_wave_bind_the_first_oath` | No IW-038 helper call. | The active IW-038 RUT package invokes `independence_wave_rut_focus_integrate_border_guards`. |
| `independence_wave_define_former_host_policy` | No IW-038 helper call. | The active IW-038 RUT package invokes `independence_wave_rut_focus_settle_former_host_ledgers`. |
| `independence_wave_recognize_fellow_new_states` | No IW-038 helper call. | The active IW-038 RUT package invokes `independence_wave_rut_focus_open_carpathian_corridor`. |

RUT continues to receive the full shared tree, and no layout node, prerequisite, mutual exclusion, AI weight, icon, or focus localisation was changed by this handoff.

## Validation and MCP evidence

The offline National focus modding page and required core wiki pages were consulted, together with vanilla `effects_documentation.md`, `triggers_documentation.md`, and `script_concept_documentation.md`.

The pre-change `hoi4.focus_inspect` resolved `independence_wave_focus_tree` with 184 nodes and 193 connectors and recorded the existing generic continuous-focus icon errors and five known layout warnings at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/f03ff2e31e865e009b138fff64790a6efdadaa3007bc7310bc00121c375efa0b/906f795f9e9d7c9e7b3b97b00c47eb5e9262929dfd4894e8ec199c7c5fe21d2c/focus-inspect.7bcf6baeea496cc7.json`.

The post-change `hoi4.focus_inspect` resolved the same 184 nodes and 193 connectors with the same layout hash and reported the five new helper references as `FOCUS_GAMEPLAY_REFERENCE_PARTIAL` because the current MCP shared inventory does not yet include the country-core helper definitions, at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c08eaf3936a1ee4188bece4cf94213e012c483cc5e0bc546a637fd54c4d74bcd/a0d97f7c07f7c23a59f714647861feccb086cd132cc68af72ce7232bc175d994/focus-inspect.f15049544f64a86b.json`.

The post-change `hoi4.focus_render` completed successfully without a layout delta and produced HTML, SVG, JSON, source-map, and plan artifacts, including `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6febb01e879e99a85279c901d3f354e819ded1df6e66095d92c45284c5fc23ae/536b8c842f17a612d1649f50833b65ac44147c65932d15cb5ee0729e43f7bda1/independence_wave_focus_tree.focus.html` and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/14c03b812bd3c319ba1af492eae0ad576b49e8960e47431696e3af87df34c37c/80ebfdb03c7642285cffccbf85a7a3df0137bffa4167ecbe61e89856078af52b/independence_wave_focus_tree.focus.json`.

No `hoi4.focus_rewrite` was needed because the patch does not change focus layout or route geometry.

## Skipped meaningful validation

The helper definitions and `is_independence_wave_rut_package` trigger are country-core owned and are not present in the current shared source inventory, so helper-body behavior and typed package-trigger resolution remain for the parent and country-core validation pass.

No live game launch or in-game focus completion was performed because repository instructions reserve that validation for the user.

## Remaining risks and follow-up

The parent must ensure that country-core helper definitions and the exact `is_independence_wave_rut_package` trigger are loaded before relying on the five calls.

The current MCP report retains nine pre-existing generic continuous-focus icon errors and five known layout warnings that are outside this narrow RUT hook scope.

The current workspace already contained concurrent KOS hook lines in the same file, and they were preserved without modification.

