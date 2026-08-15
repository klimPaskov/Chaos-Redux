# IW-053 ALT focus-hook handoff

Date: 2026-08-15.

Scope: five package-local callbacks in `common/national_focus/006_independence_wave_focus.txt` for the ALT package.

## Result

The shared worktree contains the five requested callbacks, each guarded by both `original_tag = ALT` and `is_independence_wave_altai_package = yes`.

No focus node, central admission list, Join effect, localisation file, icon definition, or effects-file change was made for this handoff.

The existing concurrent target diff is limited to the five ALT additions at the requested anchors; the former-host and network callbacks extend existing one-line reward blocks without changing their other package routes.

## Route coverage

| Shared anchor | Focus ID | Exact package helper | Source line | Guard |
| --- | --- | --- | ---: | --- |
| Prepare capital | `independence_wave_prepare_capital_administration` | `independence_wave_altai_focus_convene_mountain_council` | 120 | `original_tag = ALT` and `is_independence_wave_altai_package = yes` |
| Inventory state | `independence_wave_inventory_the_state` | `independence_wave_altai_focus_secure_oyrot_communities` | 171 | `original_tag = ALT` and `is_independence_wave_altai_package = yes` |
| Bind first oath | `independence_wave_bind_the_first_oath` | `independence_wave_altai_focus_integrate_mountain_guards` | 203 | `original_tag = ALT` and `is_independence_wave_altai_package = yes` |
| Former host policy | `independence_wave_define_former_host_policy` | `independence_wave_altai_focus_settle_former_host_ledgers` | 1439 | `original_tag = ALT` and `is_independence_wave_altai_package = yes` |
| Recognize fellow states | `independence_wave_recognize_fellow_new_states` | `independence_wave_altai_focus_open_frontier_network` | 1710 | `original_tag = ALT` and `is_independence_wave_altai_package = yes` |

The exact helper definitions are present in `common/scripted_effects/006_independence_wave_altai_package_effects.txt` at lines 238, 251, 263, 276, and 312 respectively.

## Before and after behavior

Before these additions, ALT completed the shared anchors without invoking its package-local compact, ledger, or frontier-network callbacks.

After these additions, only the ALT-origin Altai package invokes the five matching helpers, while other packages continue through their existing branches.

The helper effects retain their own idempotence and package checks, so duplicate completion callbacks do not double-count the Altai compact ledgers.

## Localisation and icon audit

No new focus IDs were introduced, so no new focus localisation or icon IDs are required.

The five anchor focus IDs already use the shared focus localisation and existing icons in `006_independence_wave_focus.txt`.

The ALT package-local helper names are script identifiers, not player-facing focus IDs, and therefore do not require additions to the ALT localisation file.

There are no localisation/reward mismatches in this hook-only scope; helper rewards remain defined in the effects file.

## AI and route audit

No AI weights, prerequisites, mutual exclusions, focus positions, or route availability checks changed.

No probability audit was required because this patch adds no weighted logic.

The five callbacks are hidden completion effects and do not create a new visible branch or a new focus route.

## Validation

`hoi4.focus_inspect` ran against `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree` with status `ok` and code `FOCUS_INSPECTED`.

Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/79e04b9d945dcbefd97938be519d09af5f9b196cb3b687b74f549236e213e12d/3b8bed0c4bfa5d66ef18ed641392a90fad62bc3e931aef4f5a710e5709ede86c/focus-inspect.bebf7f8fbd95165b.json`.

`hoi4.focus_render` ran against the same tree with status `ok` and code `FOCUS_RENDERED`.

Render artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0fea223a189955642fb67f60f9037afe95abc93e814bb78043d0c425f9f394e7/ba7cc15e578df685d32375166ef438be2f723c1ec3a8df35c35593194129b79d/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/55af361eab605e63379b4ebfde0e12f469d94d08bdacc8e1aacb9ccf76f22e85/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fe64c6bab42dc8a3d78eb357c06ca8423d35ef844e39cb078a28566e3deb33c2/0a5ed9d8ef6051cfa49e19a431ec035971c84b2a2de1daa50a4f0ae5d3de408a/independence_wave_focus_tree.focus.json`.

The MCP tree parse completed successfully with 184 focuses, zero connector crossings, zero node intersections, and no ALT-specific focus or icon diagnostics.

The MCP validation remains false because it reports 14 blocking diagnostics from unrelated generic continuous-focus icon references; it also reports existing whole-tree layout warnings. These are outside this hook-only scope and were not changed.

## Remaining risks and skipped checks

The live game callback execution and save-state behavior were not run because in-game testing belongs to the parent/user workflow.

The effects helper runtime behavior was source-checked but not reimplemented or altered here; the parent should review the helper/effect package handoff together with this focus handoff.

No central admission or `Join` wiring was added by design.

Parent review should preserve the five existing target-file additions when reconciling concurrent edits.
