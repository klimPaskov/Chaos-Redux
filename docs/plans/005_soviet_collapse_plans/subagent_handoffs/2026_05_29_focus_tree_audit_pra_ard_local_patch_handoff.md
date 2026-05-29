# Soviet Collapse Focus Tree Audit - PRA/ARD Local Patch Handoff

Date: 2026-05-29
Subagent scope: focus-tree audit and small local patch for the four Soviet Collapse focus files.

## Files Changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_05_29_focus_tree_audit_pra_ard_local_patch_handoff.md`

## Route Coverage Table

| Required route | Implemented route or focus branch | Status | Notes |
| --- | --- | --- | --- |
| Construction Directorate should heavily build civilian industry | `CFR_soviet_collapse_focus_tree` in `005_soviet_collapse_factory_successors.txt`, 47 focuses | Mostly covered | Tree has civilian factory/offsite construction, reconstruction decisions, mandate variables, and construction AI. Broader route identity still needs parent review per existing follow-up plan. |
| Dead Soldiers Congress should get aggressive war goals, cores, units, recruitment identity | `DSC_soviet_collapse_focus_tree` in `005_soviet_collapse_custom_splinters.txt`, 18 focuses | Partly covered | Current tree has manpower, claims/controlled cores, SOV and neighbor war goals, AI conquest strategies, assault column spawn, and dead army decisions. It is still shallow compared with full custom splinter trees. |
| Railway country should build rail/supply | `PRA_soviet_collapse_focus_tree`, especially `PRA_armored_train_directorate` | Patched | Replaced tiny train/truck stockpiles with `pra_rolling_stock` progress and existing `soviet_collapse_apply_focus_rail_authority_reward`; keeps rail/supply map construction. |
| Factory states should match factory lore | `CFR`, `MFR`, `OGB` factory successor trees | Partly covered | CFR/MFR are deep enough to audit as real trees; OGB remains 23 focuses and needs expansion or explicit narrow classification. |
| Naval directorate should support ships/naval warfare | `ARD_soviet_collapse_focus_tree` naval/dockyard branch | Patched locally | `ARD_naval_infantry_yards` now has navy filtering and a dockyard payoff; `ARD_fuel_and_convoy_escorts` and `ARD_murmansk_dockyard_contracts` now advertise naval filters; dockyard contract AI is more war/depot-aware. |
| No focus pathline through mutually exclusive focuses / no focus on lines | All four scoped focus files | Covered by static audit | Coordinate audit found 0 duplicate coordinates, 0 adjacent same-row collisions, and 0 straight prerequisite-line focus hits after patch. In-game screenshot validation still not run. |

## Changed Focus IDs

- `PRA_armored_train_directorate`
- `ARD_naval_infantry_yards`
- `ARD_fuel_and_convoy_escorts`
- `ARD_murmansk_dockyard_contracts`

## Behavior Before And After

| Focus id | Before | After |
| --- | --- | --- |
| `PRA_armored_train_directorate` | Paid tiny train and motorized stockpiles plus rail/supply construction. | Adds `pra_rolling_stock`, calls existing `soviet_collapse_apply_focus_rail_authority_reward`, and keeps rail/supply construction and military consolidation. |
| `ARD_naval_infantry_yards` | Filtered as army/manpower despite navy XP and naval identity; paid a small convoy stockpile. | Adds `FOCUS_FILTER_NAVY_XP`, replaces the small convoy stockpile with a coastal dockyard build when a slot exists, and keeps manpower, navy XP, command power, coastal bunker, and signature-force unlock. |
| `ARD_fuel_and_convoy_escorts` | Filtered as industry/army while granting convoy/naval logistics rewards. | Adds `FOCUS_FILTER_NAVY_XP`; reward otherwise unchanged. |
| `ARD_murmansk_dockyard_contracts` | Filtered only as industry and had flat AI. | Adds `FOCUS_FILTER_NAVY_XP`, normalizes indentation of the focus header/building limit, and adds war/depot AI modifiers. |

## Localisation And Icon IDs

- Localisation keys changed: none.
- Icon ids changed: none.
- Existing icon ids verified for changed focuses:
  - `GFX_focus_PRA_armored_train_directorate`
  - `GFX_focus_ARD_naval_infantry_yards`
  - `GFX_focus_ARD_murmansk_dockyard_contracts`

## Missing Or Simplified Content

- `OGB_soviet_collapse_focus_tree` remains a 23-focus successor and is not deep enough for a full overpowered restoration/state route.
- Ancient restorations `KZR`, `SOG`, `KHW`, and `ALN` remain 16-focus packages; they need route identity and existing-mechanic hooks before completion can be claimed.
- Crisis custom trees `PRA`, `DSC`, `TSC`, `RMC`, `NRF`, and `ICD` are shallower than the 47-focus custom-splinter standard; decide whether they are intentionally compact crisis actors or deepen them.
- Direct tiny convoy/support equipment rewards remain in many custom-splinter focuses. This patch only touched the high-confidence PRA/ARD cases.
- Ukraine and Belarus have broad depth, but route readability and route-specific AI remain uneven and need a focused pass.

## Localisation And Reward Mismatch List

- No missing focus names/descriptions were found in the four scoped files.
- `PRA_armored_train_directorate` reward now better matches the rail authority/armored train title.
- `ARD_naval_infantry_yards` reward now better matches a naval-yard title by adding a dockyard instead of only a small convoy stockpile.
- Remaining likely mismatch class: naval, river, convoy, and support-equipment focuses that still pay small stockpiles instead of decisions, state construction, units, or route variables.

## AI Behavior Gaps

- `ARD_murmansk_dockyard_contracts` received simple war/depot-aware AI modifiers.
- Many shallow or crisis trees still use simple `base` AI weights; broader route-aware AI should prioritize DSC aggression, PRA rail buildout, NRF/KRS/ARD naval pressure, and Ukraine/Belarus political route decisions.
- Focus AI was audited statically only; decision AI for war goals, cores, and unit decisions remains a parent-level validation surface.

## High-Priority Follow-Up

1. Finish the existing full redesign follow-up plan at `docs/plans/005_soviet_collapse_plans/2026_05_29_soviet_collapse_focus_tree_redesign_followup_plan.md`.
2. Deepen or explicitly classify compact crisis trees: `PRA`, `DSC`, `TSC`, `RMC`, `NRF`, `ICD`.
3. Replace remaining tiny stockpile rewards with existing helpers, decision unlocks, state construction, spawned units, claims/cores, or war goals.
4. Give Ukraine and Belarus visible route semantics and stronger route-aware AI.
5. Run in-game focus-tree screenshots for wide trees after the next layout pass.

## Validation Run

- Brace depth over all four scoped focus files: final depth `0`, minimum depth `0`.
- Duplicate focus id audit over all four scoped focus files: `0` duplicates across `1698` focus blocks.
- Missing focus prerequisite/mutual-exclusion references: `0`.
- `rg -n "<=|>="` over the four scoped focus files: no matches.
- `rg -n "add_ideas\s*="` over the four scoped focus files: no matches.
- Coordinate/pathline script over the four scoped focus files: `duplicate_coords 0`, `near_same_row 0`, `straight_prereq_hits 0`.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed.

## Skipped Validation

- No in-game load or screenshot validation was run from this subagent pass.
- No scripted AI route simulation was run; the audit is static.

## Remaining Route Risks

- Broad route depth and identity are still incomplete for several compact trees; this was not safe to patch as a local focus-audit change.
- The shared working tree already contains extensive uncommitted Soviet Collapse changes from other agents; this handoff records only the local PRA/ARD focus patch.
