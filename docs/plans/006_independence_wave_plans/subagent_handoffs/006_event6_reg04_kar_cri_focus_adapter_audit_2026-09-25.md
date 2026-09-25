# Event 006 REG-04 Karelia and Crimea Focus Adapter Audit

## Scope and acceptance basis

This read-only audit covers the IW-033 Karelia and IW-041 Crimea package gates and callbacks on `independence_wave_inventory_the_state`, their visible reward text and lifecycle effects, and their contribution to REG-04. The user explicitly approved the accepted Event 006 scope on 2026-09-25. This is not a full Event 006, focus-tree, country-package, decision, or AI audit.

The reviewed source set was `common/national_focus/006_independence_wave_focus.txt`, `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt`, `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`, `common/script_constants/006_independence_wave_constants_registry.txt`, `localisation/english/006_independence_wave_focus_l_english.yml`, `docs/events/006_independence_wave/karelia_crimea_packages.md`, the REG-04 matrix row, Part 4 and Part 5 focus and regional requirements, and the 2026-09-25 baseline regional coverage audit.

## Findings

The exact package gates and callback pairing are correct within the reviewed source boundary. No wrong-package mutation, territory effect, admission change, focus graph change, or paid-project completion hook was found.

The new callbacks add one-time regional ledger progress to a shared focus. They do not supply a country-specific focus group, so the accepted regional focus-group requirement remains unmet. REG-04 also remains partial because the Don package IW-039 has no focus completion adapter.

The working localization changed during this audit from fixed-gain wording to `can raise ... by up to`. I made no source edits. The final MCP refresh below uses the later wording. The same localization file has an out-of-scope Transylvania tooltip addition in its worktree diff; it was left untouched.

## Route coverage

| REG-04 package | Current focus coverage | Result |
| --- | --- | --- |
| IW-033 Karelia (`KAR`) | `independence_wave_inventory_the_state` shows the Karelia tooltip and calls `independence_wave_kar_focus_reconcile_forest_supply_records` under `is_independence_wave_kar_package` (`common/national_focus/006_independence_wave_focus.txt:168,190`). | Adapter present on the shared focus. No country-specific group. |
| IW-041 Crimea (`CRI`) | The same focus shows the Crimea tooltip and calls `independence_wave_cri_focus_register_land_and_return_rolls` under `is_independence_wave_cri_package` (`common/national_focus/006_independence_wave_focus.txt:169,191`). | Adapter present on the shared focus. No country-specific group. |
| IW-039 Don (`DON`) | No Don package predicate, callback, or focus-family reference is present in the reviewed focus source. The baseline audit also recorded no IW-039 focus adapter (`006_event6_regional_overlay_coverage_audit_2026-09-25.md:32`). | Missing adapter. REG-04 remains partial. |
| IW-040 Kuban (`KUB`) | Existing package callbacks remain on shared focuses, including the inventory and oath effects (`common/national_focus/006_independence_wave_focus.txt:122,179,217`). The baseline audit records these shared-node adapters and no separate regional family (`006_event6_regional_overlay_coverage_audit_2026-09-25.md:32,89`). | Existing shared-focus coverage. Not re-audited beyond these bounded references. |

Before these adapters, the baseline row reported no focus adapters for IW-033, IW-041, or IW-039. Current source adds the two Karelia and Crimea inventory rewards while leaving the Don gap and shared-tree geometry unchanged. This audit itself makes no gameplay change.

Part 4 requires one or more country-specific focus groups for highlighted packages (`006_independence_wave_spec_part_4_focus_tree_architecture.md:651-660`). Part 5 specifies one country-specific focus group for a Level 2 featured regional country (`006_independence_wave_spec_part_5_country_packages_and_regional_overlays.md:52-56`). The two new callbacks are reward adapters on one generic focus and do not meet either group requirement. The package document records a prior parent-waived Level 2 expectation (`docs/events/006_independence_wave/karelia_crimea_packages.md:13,56`), but the adapter does not satisfy the accepted group scope. The parent should reconcile that recorded waiver against the 2026-09-25 accepted scope before treating the group requirement as waived.

The REG-04 row identifies Karelia, Crimea, Don, and Kuban as featured packages and requires Event 5 origin and state-reservation checks (`matrices/006_regional_overlay_matrix.csv:5`). Those release checks are outside this focus adapter audit.

## Gate, callback, clamp, and lifecycle review

`is_independence_wave_kar_package` requires `original_tag = KAR`, active Event 006 package content, and package id `iw_033` (`006_independence_wave_karelia_crimea_package_triggers.txt:8-12`). The Crimea predicate applies the equivalent `CRI` and `iw_041` checks (`:14-18`). The constants resolve those package ids to 33 and 41 (`006_independence_wave_constants_registry.txt:7494-7540`). The three conditions in each predicate form an AND gate. The two package identities cannot both satisfy their distinct original-tag and package-id checks.

The focus displays each package tooltip under that exact predicate, then repeats the same gate around its callback inside the hidden completion effect (`006_independence_wave_focus.txt:167-191`). Each callback checks its own package predicate again before setting its two deltas (`006_independence_wave_karelia_crimea_package_effects.txt:113-130`). The shared ledger helper checks the package again before changing only that package's two variables (`:92-105`). This layered gating is consistent and fails closed when package content is inactive or the package identity differs.

Karelia applies `standard_gain = 12` to Forest Supply and `minor_gain = 6` to Civic Mandate. Crimea applies 6 to Return Capacity and 12 to Land Settlement. The constants define initial values of 36/42 for Karelia and 34/40 for Crimea, a shared minimum of 0, maximum of 100, and stable threshold of 65 (`006_independence_wave_constants_registry.txt:5958-5975`). From those initial values the focus produces 48/48 for Karelia and 40/52 for Crimea, below the stable threshold.

The helper clamps each changed ledger to 0 through 100, then runs `independence_wave_refresh_kar_lifecycle` and `independence_wave_refresh_country_state` (`006_independence_wave_karelia_crimea_package_effects.txt:92-109`). The lifecycle predicates require both package ledgers to be at least 65 (`006_independence_wave_karelia_crimea_package_triggers.txt:125-135`). The refresh replaces the contested idea with the compact idea and sets the stabilized flag when both conditions pass, and restores the contested idea and clears the flag otherwise (`006_independence_wave_karelia_crimea_package_effects.txt:63-90`). Each lifecycle branch has the matching package gate. This is coherent with the existing ledger lifecycle and does not grant or finish a paid project.

If earlier package actions leave both ledgers near 65, the focus callback can trigger the conditional idea transition. The package-specific focus tooltip names the ledger gains but does not describe that threshold transition. The shared focus tooltip says it strengthens administrative capacity, which is broad context rather than a clear description of the conditional idea swap. This is a tooltip completeness caveat, not a gate or mutation defect. The body of `independence_wave_refresh_country_state` is outside the specified source boundary, so its separate side effects were not audited.

Each matching package receives one additional concise tooltip line. The two mutually exclusive package gates prevent repeated adapter hover text for one country.

## Icon coverage

| Focus | Icon id | Coverage |
| --- | --- | --- |
| `independence_wave_inventory_the_state` | `GFX_goal_independence_wave_infrastructure_authority` | Both adapters use the same focus node and therefore the same icon. The package doc identifies the existing sprite and texture (`karelia_crimea_packages.md:40`), and focus inspection emitted no missing-icon diagnostic. No new icon is required for these callbacks. |

## Localisation and reward mismatch

| Key | Visible text versus callback | Finding |
| --- | --- | --- |
| `independence_wave_kar_inventory_focus_tt` (`localisation/english/006_independence_wave_focus_l_english.yml:79`) | Says forest and railway records can raise Forest Supply by up to the standard gain and Civic Mandate by up to the minor gain. | Matches the callback and clamp, with current constants of up to 12 and 6. |
| `independence_wave_cri_inventory_focus_tt` (`...focus_l_english.yml:80`) | Says land and return rolls can raise Return Capacity by up to the minor gain and Land Settlement by up to the standard gain. | Matches the callback and clamp, with current constants of up to 6 and 12. |
| Shared focus title and description (`...focus_l_english.yml:76-78`) | Inventorying records and depots fits both callback themes. | No title or description mismatch found. |

The package document says the focus “gains” the full 12/6 or 6/12 values (`docs/events/006_independence_wave/karelia_crimea_packages.md:40`). Those are the nominal gains from the documented starting values, but actual increments can be smaller near the 100 cap. Consider aligning that documentation with the current `up to` tooltip wording. The current player-facing text itself does not overstate the capped result.

## AI behavior gaps

No package-specific AI selection behavior is added by these effect adapters. The shared focus retains its existing urgent AI weight (`common/national_focus/006_independence_wave_focus.txt:194`). AI weighting was explicitly outside this bounded adapter review, was not changed, and was not sent through `chaosx_ai_probability_auditor`. No adapter-specific AI defect is identified.

## High-priority follow-up

1. **REG-04 coverage remains partial.** The Don package IW-039 has no focus adapter, and the country-specific focus-group requirement remains unmet by the Karelia and Crimea shared-node rewards. The parent should keep this gap open and reconcile the older Level 2 waiver with the accepted scope. This requires broader design or implementation and was not attempted here.
2. **Documentation wording.** Align the package document's fixed-gain sentence with the capped `up to` behavior if it is intended to describe all reachable ledger states.
3. **Conditional tooltip detail.** Decide whether the package tooltips should mention the possible contested-to-stable idea transition when both ledgers reach 65. No definite gameplay source defect was found in the reviewed callback chain.

## MCP evidence and validation limits

Fresh `hoi4.focus_inspect` returned `FOCUS_INSPECTED`, revision `2481cdbe9f03f38152699849acca481609a81bf4f5bc53e684bd6605512c6ecf`, 184 focuses, and 196 connectors. The layout hash is `a4d2d61f7c8f879a7e98ea8e6befc1b6c561138f0373355b91508b4056ad03e7`, with zero crossings and zero node intersections. The render returned `FOCUS_RENDERED` with the same layout hash. The parent-provided revision `ae4069ebd12391ee20c151df1659b2e064ab93c404d97fe03d12257803f58558` differs from this fresh revision, while the tree count and layout hash agree.

The inspect and render reported one unrelated ten-column connector warning from `independence_wave_adopt_military_archetype_program` to `independence_wave_adopt_reclamation_doctrine`. They also reported the unrelated vanilla localization warning for `continuous_restrict_freedom_desc` and an informational inline file inventory truncation. No diagnostic points to the shared inventory focus, its icon, or the new localization keys. Focus diagnostic validation passed with no blockers.

- Inspect artifact: [focus-inspect JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dffdeca346570ec3553819ea9e73a20a776ee6997a01029cc899d2da21e2dd8a/b539e3e0fc6eedd872722b45534a19444c30a2a549a6520188e8c1ab5e08ed86/focus-inspect.2481cdbe9f03f381.json).
- Render artifacts: [HTML](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ce7d6ab4862487592b507f96885fc8948b6e22f58cc376a4a3ecced94a00d85a/62e0e5480842260639cf22b1ccf6f8bb35f69e9b7b32ba4bc5fa5c62415266ad/independence_wave_focus_tree.focus.html), [SVG](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5086d880824847a69a40978a74727d27f869e94a735828bcfccb315258f70109/df6e96ef882d15bd4d4bbe89af66050415ed93e67d2b68f15838bb5463374ab9/independence_wave_focus_tree.focus.svg), and [JSON](hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/07ebcec39da9808d4953634bd4f91505b3ce09d59fa01bb1844dfd500062c4fb/05e64c609ea085557c27bffecbe902975c3bab14ed76c954ca016f7b306d7bee/independence_wave_focus_tree.focus.json).

No tests or live game were run, as requested. No source files were changed. A probability audit was skipped because no in-scope AI weight or probability surface changed. No separate improvement plan was written because the user limited this task to the single audit handoff and prohibited broad design. Skills consulted and applied: `chaos-redux-focus-trees`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-subagents`, and `chaos-redux-improvement-loop`. No skill was created or updated.
