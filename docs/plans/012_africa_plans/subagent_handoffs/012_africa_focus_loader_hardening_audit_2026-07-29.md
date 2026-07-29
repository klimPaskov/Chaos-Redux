# Event 12 Africa Focus Loader Hardening Audit

## Scope and evidence

This audit covers every Event 012 `load_focus_tree` call, the canonical continental loader and its callers, priority-member installation, RSA host succession, dormant external-continent packages, one-shot guards, meaningful-tree protection, and completed-focus preservation.

The audited source is HEAD `41c0f4bbe` (`Preserve Event 12 focus progress`). The worktree also contains an unrelated modified Event 006 handoff and a vendor submodule marker; neither was changed. No gameplay file was patched by this audit and no commit was created.

Engine semantics were checked against `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md:500-517`, `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:497`, and `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md:4771-4787`. `keep_completed = yes` retains only completed IDs shared by the old and new trees. `copy_completed_from` copies completed IDs from another valid country; it does not copy current focus progress, variables, flags, ideas, or rewards.

Read-only MCP focus inspections were run for `africa_continental_focus_tree` (276 focuses, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5ab14e44d7601e199935ff9c497701267655608931c1596d525a39a15edb0a3f/f7279576d120319eae2a49276a763decb6ef13d2994a00f2d2dabd6b107e2dbb/focus-inspect.674538b92e22843ae447490ffdc014caa7bbb3319905b76f26bf0d3d5a33559c.json`), `africa_priority_member_focus_tree` (8 focuses, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ed55b27fd069f34ada538773b9344dd9e09e00ab20f906f2daba6e0f94d24b1b/e5e226c741631db3a74b4ab953a7c43dfc7dd9077cf2a35c1cfa8d8e7b1ace20/focus-inspect.674538b92e22843ae447490ffdc014caa7bbb3319905b76f26bf0d3d5a33559c.json`), and `africa_asia_world_focus_tree` (20 focuses, artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/b40676690b16bfbb2feaf79c726bd9c5340fd10d53350ea4efa8b2b572db16c1/5e4c6017726b8e9ee42c668ab8bab831110d1739352e0eb4fe8cf1cdcf0ed8af/focus-inspect.674538b92e22843ae447490ffdc014caa7bbb3319905b76f26bf0d3d5a33559c.json`).

## Route and loader coverage

| Route or package | Loader and source | Guard and one-shot behavior | Meaningful-tree protection | Completion handling | Assessment |
|---|---|---|---|---|---|
| Initial continental host | `africa_load_continental_focus_tree` in `common/scripted_effects/012_africa_effects.txt:1365-1385`, called by `africa_initialize_selected_host` at `:513` | Requires `africa_is_current_host` and `NOT has_focus_tree = africa_continental_focus_tree`; the loaded flag is set only after the target tree is active | `africa_is_eligible_host` requires `has_focus_tree = generic_focus` at `common/scripted_triggers/012_africa_triggers.txt:331-364` | `keep_completed = yes` at `012_africa_effects.txt:1371-1374` preserves only same-ID completions | Safe for initial generic-tree replacement; `yes` is harmless for unrelated IDs but does not preserve a generic tree's unrelated checklist |
| Continental compatibility route | `africa_focus_route_ensure_continental_tree_loaded` at `common/scripted_effects/012_africa_focus_route_effects.txt:11-14` | Delegates to the canonical helper; no second replacement body remains | Inherits the canonical host guard | Inherits `keep_completed = yes` | Duplicate loader drift was removed in HEAD `41c0f4bbe` |
| RSA successor host | `africa_rsa_transfer_host_to_exile_patron` at `common/scripted_effects/012_africa_rsa_effects.txt:817-974`, calling the canonical helper at `:959` | Patron is selected before transfer; the canonical helper still requires the new host identity and target tree absence | `africa_rsa_is_valid_exile_patron` requires `has_focus_tree = generic_focus` at `common/scripted_triggers/012_africa_rsa_triggers.txt:45-59` | No `copy_completed_from` exists anywhere in Event 012; `keep_completed = yes` intersects the patron's generic tree, not the old host's continental tree | **High-priority defect:** completed Event 012 focus IDs are lost on RSA host succession even though the ledger variables and flags are copied |
| Priority member package | `africa_priority_member_ensure_focus_tree_loaded` at `common/scripted_effects/012_africa_priority_member_effects.txt:258-287`, called at `:575` | Registration requires `NOT has_country_flag = africa_priority_member_package_active` at `common/scripted_triggers/012_africa_priority_member_triggers.txt:412-423`; loader resets display flags each call | Keeps the package tree if already active; otherwise loads only for an approved Event 006 carrier or `generic_focus`; all other trees receive `africa_priority_member_focus_tree_overlay_skipped` | `keep_completed = yes` at `:276-279` | Good local safeguard; the Event 006 carrier branch is intentionally explicit but assumes those carrier tags are approved replacement owners |
| Middle East package | `africa_world_install_current_package` at `common/scripted_effects/012_africa_world_order_effects.txt:465-545`, tree load at `:516` | Requires candidate, implementation readiness, status in candidate-to-rival range, and `NOT africa_world_package_installed`; candidate is cleared and installed flag set before the tree load | Candidate base requires generic tree or explicit `africa_world_package_focus_replacement_approved` at `common/scripted_triggers/012_africa_world_order_triggers.txt:9-28` | `keep_completed = yes` at `:516` | One-shot and replacement guards are present; package is dormant while readiness has no setter |
| Europe package | Same installer, tree load at `012_africa_world_order_effects.txt:521` | Same candidate/readiness/install receipt guards | Same generic-or-explicit-approval gate | `keep_completed = yes` at `:521` | Safe while dormant; no live activation evidence |
| Asia package | Same installer, tree load at `:526` | Same candidate/readiness/install receipt guards | Same generic-or-explicit-approval gate | `keep_completed = yes` at `:526` | MCP inspection is structurally valid with 20 focuses; authored package focuses have missing-icon warnings |
| North America package | Same installer, tree load at `:531` | Same candidate/readiness/install receipt guards | Same generic-or-explicit-approval gate | `keep_completed = yes` at `:531` | Safe while dormant; no live activation evidence |
| South America package | Same installer, tree load at `:536` | Same candidate/readiness/install receipt guards | Same generic-or-explicit-approval gate | `keep_completed = yes` at `:536` | Safe while dormant; no live activation evidence |
| Oceania package | Same installer, tree load at `:541` | Same candidate/readiness/install receipt guards | Same generic-or-explicit-approval gate | `keep_completed = yes` at `:541` | Safe while dormant; no live activation evidence |

The exact direct `load_focus_tree` blocks are the six world branches, the priority branch, and the canonical continental branch. RSA and the compatibility route call the canonical helper rather than adding direct tree loaders.

## Missing or simplified content

- RSA successor focus continuity is missing. The architecture handoff requires preserving `event_target:africa_previous_host` before old-host cleanup and loading the successor with `copy_completed_from = event_target:africa_previous_host` (`docs/plans/012_africa_plans/012_africa_focus_architecture_handoff.md:611-642`), but `africa_rsa_transfer_host_to_exile_patron` has no previous-host target and no copy effect.
- `keep_completed = yes` is not full progress preservation. It retains only same-ID completions; it cannot retain an active focus's progress, and all normal generic-tree IDs are unrelated to the Event 012 continental IDs.
- External-continent package activation remains intentionally dormant because `africa_world_package_implementation_ready` is read by the installer but has no setter in the current source. This is a deferred package, not a runtime fallback.
- No broad tree redesign or new route family was attempted. The existing overlay-coordinate warnings are outside this loader hardening scope.

## Icon coverage and layout findings

| Tree | MCP/source result | Loader relevance |
|---|---|---|
| `africa_continental_focus_tree` | 276 focuses; structural inspect succeeded. The artifact reports 448 connector crossings, 1,028 node intersections, and 55 same-row spacing conflicts caused by authored mutually exclusive overlay coordinates. | Existing layout risk remains; loader calls `mark_focus_tree_layout_dirty` after activation, but this does not resolve authored coordinate reuse. |
| `africa_priority_member_focus_tree` | 8 focuses; no Event 012 icon diagnostics. Three long-connector warnings remain. | No loader-specific icon blocker. |
| `africa_asia_world_focus_tree` | 20 focuses; authored Event 012 focuses have missing-icon warnings. | Package is dormant behind readiness, so this remains a release gate before enabling it. |
| Other five world trees | Source files exist with the same dormant package pattern; no separate MCP render was needed for this loader audit. | Their icon and localisation surfaces remain unaccepted until package readiness review. |

The continental layout warnings are not a loader defect and should not be flattened by moving route coordinates without a separate focus-layout plan.

## Localisation and reward mismatch list

No loader-specific localisation or reward mismatch was found in the inspected callsites. Loader effects set trees, flags, and layout invalidation only; they do not grant focus rewards. The MCP Asia and priority inspections surfaced generic vanilla continuous-focus icon/localisation diagnostics alongside the tree, but those are not introduced by the loader calls. A full focus-title, description, icon, and reward audit remains a separate route audit.

## AI behavior gaps

No loader-specific AI gap was proven by source inspection. Initial host selection, priority packages, and world package actions have separate AI gates and route weights. The outstanding succession defect is state continuity rather than AI selection. Live AI behavior and focus selection remain unvalidated because in-game execution is outside this audit and prohibited for agents by repository instructions.

## High-priority fixes

1. Add the missing RSA successor focus-copy contract. Save the old host as a temporary or global `africa_previous_host` target before `africa_rsa_cleanup_old_host_runtime` or any annexation-invalidating effect, load the successor with `copy_completed_from = event_target:africa_previous_host`, and clear the temporary target after the load. Keep the explicit ledger transfer because focus copying does not copy variables, flags, ideas, arrays, or rewards. This is the smallest safe fix and should be implemented in `common/scripted_effects/012_africa_rsa_effects.txt:817-974` with a parser-valid dynamic source form checked against the installed effects documentation.
2. Qualify player-facing and completion documentation that says “preserves completed-focus history” as same-ID preservation unless the RSA copy contract is implemented. `keep_completed = yes` is correct for duplicate-safe replacement but does not preserve arbitrary prior-tree completion.
3. Before enabling world package readiness, inspect and wire all six world trees' authored icons and localisation, then run a separate focus render/layout review. Do not treat the dormant gate as a gameplay fallback.

## Validation and remaining risks

Validation consisted of an exact source scan of all `012_africa*.txt` focus-loader callsites, trigger and transfer-order inspection, offline wiki and installed vanilla documentation review, and three read-only MCP focus inspections. No in-game save was launched or claimed as tested. The main unresolved risk is RSA host succession: the old host remains available at `on_civil_war_end_before_annexation`, but the current transfer does not preserve a source target for `copy_completed_from`. Secondary risks are dormant world-package assets and the existing intentional continental overlay layout diagnostics.

## Handoff

Parent review should treat `common/scripted_effects/012_africa_rsa_effects.txt:817-974` and `docs/plans/012_africa_plans/012_africa_focus_architecture_handoff.md:611-642` as the direct contract mismatch. This handoff is an audit only; no implementation patch or commit was made here.
