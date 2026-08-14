# IW-050 Komi focus hooks handoff

Date: 2026-08-14

Scope: Add the five guarded Komi package dispatches to the established Independence Wave shared anchors.

## Changed source

This subagent changed only `common/national_focus/006_independence_wave_focus.txt`.

The Komi scripted effect and trigger files were already present in the concurrent worktree and were not edited here:

- `common/scripted_effects/006_independence_wave_komi_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt`

## Route coverage

| Shared anchor | Focus id | Exact guard | Komi helper | Result |
| --- | --- | --- | --- | --- |
| Capital administration | `independence_wave_prepare_capital_administration` | `original_tag = KOM` + `is_independence_wave_komi_package = yes` | `independence_wave_komi_focus_convene_northern_congress` | Added |
| State inventory | `independence_wave_inventory_the_state` | `original_tag = KOM` + `is_independence_wave_komi_package = yes` | `independence_wave_komi_focus_secure_railhead_communities` | Added |
| First oath | `independence_wave_bind_the_first_oath` | `original_tag = KOM` + `is_independence_wave_komi_package = yes` | `independence_wave_komi_focus_integrate_forest_guards` | Added |
| Former-host policy | `independence_wave_define_former_host_policy` | `original_tag = KOM` + `is_independence_wave_komi_package = yes` | `independence_wave_komi_focus_settle_former_host_ledgers` | Added |
| Fellow new states | `independence_wave_recognize_fellow_new_states` | `original_tag = KOM` + `is_independence_wave_komi_package = yes` | `independence_wave_komi_focus_open_pechora_corridor` | Added |

Before this patch, the shared anchors had no Komi dispatch. After this patch, each anchor calls its Komi helper only when both the original tag and package trigger match.

Non-Komi countries and Komi states that fail either guard remain on the existing shared-anchor behavior.

## Scope exclusions and mismatch audit

No focus nodes, prerequisites, central admission, Join logic, assets, localisation, icons, AI weights, or route rewards outside the five requested helper calls were added or changed by this subagent.

The existing Komi helper definitions provide their own package checks and idempotency flags.

There are no new localisation or reward-text mismatches because no player-facing focus text or reward was changed.

There are no new icon requirements because all five calls reuse existing shared focus anchors.

No AI behavior gap was introduced because this patch does not alter focus weights or selection logic.

## MCP evidence

Pre-patch `hoi4.focus_inspect` artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/caf22dd28bcd5c40573ec3e600fdf2a70982ab10530335f5853bdf2576eaff00/806fc9d1fd6073732eafe9aaa9cc48e5f61185c879365a2305c02e0db96b571e/focus-inspect.4f8f5facc6e6e974.json`

Pre-patch render artifacts:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6c95b6d7fe0b98c27b9c2f47455dbf4ccc4a13568ac2c53c537dc1c0dd7098c1/4d3282c725c92efc60723ce6acac3b9bfcbf087c6be542f176f934b54ed25877/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/f67479776973af5150a72b8014229976e5ccc1ef44d198e71b1eeccd53cc69f7/independence_wave_focus_tree.focus.svg`

Post-patch `hoi4.focus_inspect` artifact:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0317baf413810ed07d1fd6881e7a85241b7104a7d56e2c9882016b999b2efa74/f28a06a89e98f155fa846b28332f53144a6f6fa11cb308dc61ad397ae23ce3c6/focus-inspect.ed3b63e678193f52.json`

Post-patch render artifacts:

- HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed22a75e7acdb9dc9790c48c79fbf2b870e98b0f323078cc277439bb6d6cfd5a/cc191cdce4a6664f2e8b666a95abbdb0e444aebc815000295b9caf0f6b17c314/independence_wave_focus_tree.focus.html`
- SVG: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/02a33b6e26cd319131d46e708aa7260478638f337d0a28a6efe1f823d448af30/d468ca8f3de13afb29484a6c9fc90496a76b7a6a084b249a3105d21263810fe5/independence_wave_focus_tree.focus.svg`

The post-patch inspect and render returned `status = ok`.

The tree remains at 184 focuses with layout hash `014c594a446087d67b6623767e34af4b83a026e7446235e5a3bd3cbc4eceef2a`, zero connector crossings, zero node intersections, and two long connectors.

MCP validation remains false because of the same pre-existing generic continuous-focus sprite diagnostics and six existing layout warnings, including the long connector from `independence_wave_define_former_host_policy` to `independence_wave_inherit_successor_ledger`.

## Targeted validation

The exact guarded Komi helper-call pattern occurs five times in the focus file, once for each requested helper.

The focus inspect and render completed after the patch without adding a node or changing layout metrics.

The probability auditor was skipped because no AI weight or other probability-bearing logic changed.

`hoi4.focus_rewrite` was skipped because the patch is a completion-reward dispatch addition and does not require layout rewriting.

Live HOI4 execution was skipped because runtime validation belongs to the parent and user workflow.

## Remaining risks

The existing focus-tree MCP diagnostics remain unresolved outside this narrow hook scope.

The Komi package remains fail-closed on its existing symbol, admission, and package-trigger prerequisites; this handoff does not widen those gates.

No simplifications were made within the requested five-hook scope.
