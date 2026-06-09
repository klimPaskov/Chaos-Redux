# Event005 Custom Splinter Focus Depth/Layout Follow-up Handoff

Role: `chaosx_focus_tree_auditor`

Scope: bounded audit/patch for `common/national_focus/005_soviet_collapse_custom_splinters.txt` only. No gameplay reward, prerequisite, mutual exclusion, ID, scripted effect, decision, localisation, idea, or flag asset edits were made.

## Required references consulted

- Repo instructions: `AGENTS.md`
- Skills: `hoi4-focus-trees`, `chaos-redux-subagents`
- Offline wiki core pages: Data structures, Triggers, Effect, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding
- Focus-specific wiki page: National focus modding
- Vanilla docs: `documentation/script_concept_documentation.md`, `documentation/triggers_documentation.md`, `documentation/effects_documentation.md`
- Vanilla precedents: `common/national_focus/soviet.txt`, `common/national_focus/baltic_shared.txt`, `common/national_focus/uk.txt`

## Files changed

- `common/national_focus/005_soviet_collapse_custom_splinters.txt`
- `docs/plans/005_soviet_collapse_plans/subagent_handoffs/2026_06_04_custom_splinter_focus_depth_layout_followup_handoff.md`

## Trees inspected

All 25 focus trees in the file were parsed and inspected for pathline/crowding risk, shallow reward surfaces, and visible payoff signals:

`FTH_soviet_collapse_focus_tree`, `PRA_soviet_collapse_focus_tree`, `TSC_soviet_collapse_focus_tree`, `RMC_soviet_collapse_focus_tree`, `DSC_soviet_collapse_focus_tree`, `NRF_soviet_collapse_focus_tree`, `ICD_soviet_collapse_focus_tree`, `BSC_soviet_collapse_focus_tree`, `TNC_soviet_collapse_focus_tree`, `ALA_soviet_collapse_focus_tree`, `BBH_soviet_collapse_focus_tree`, `KRS_soviet_collapse_focus_tree`, `UDC_soviet_collapse_focus_tree`, `SDZ_soviet_collapse_focus_tree`, `GAC_soviet_collapse_focus_tree`, `DHC_soviet_collapse_focus_tree`, `KHC_soviet_collapse_focus_tree`, `FEV_soviet_collapse_focus_tree`, `SZA_soviet_collapse_focus_tree`, `UWD_soviet_collapse_focus_tree`, `MRC_soviet_collapse_focus_tree`, `IUL_soviet_collapse_focus_tree`, `BAC_soviet_collapse_focus_tree`, `ARD_soviet_collapse_focus_tree`, `NLC_soviet_collapse_focus_tree`.

Parser count: 25 trees, 1005 focuses.

## Coordinate changes

Only focus coordinates were changed.

- `PRA_passport_of_the_moving_state` at line 1549: `x = 6` to `x = 2`. Reason: OR-convergence from `PRA_the_board_overrules_ministers` and `PRA_armored_train_directorate` was outside the parent pair.
- `TSC_observatory_guard` at line 2010: `x = 8` to `x = 4`. Reason: OR-convergence from the committee split was outside the parent pair.
- `RMC_reliquary_guard` at line 2463: `x = 8` to `x = 4`. Reason: OR-convergence from the witness/resurrection split was outside the parent pair.
- `DSC_field_hospital_memorials` at line 2974: `x = 8` to `x = 4`. Reason: OR-convergence from the witness/revenant staff split was outside the parent pair.
- `NRF_icebound_marine_guard` at line 3521: `x = 8` to `x = 4`. Reason: OR-convergence from the harbor/revenant admiralty split was outside the parent pair.
- `ICD_funeral_guard` at line 4016: `x = 8` to `x = 4`. Reason: OR-convergence from the last-addresses/dead-commissar split was outside the parent pair.
- `FEV_industry_plan` at line 16770: `x = 8` to `x = 4`. Reason: OR-convergence from the settlement/radical split was outside the parent pair.
- `SZA_industry_plan` at line 17921: `x = 8` to `x = 4`. Reason: OR-convergence from the settlement/radical split was outside the parent pair.
- `MRC_industry_plan` at line 20616: `x = 8` to `x = 4`. Reason: OR-convergence from the settlement/radical split was outside the parent pair.
- `ARD_winter_convoy_columns` at line 23878: `y = 14` to `y = 15`. Reason: its prerequisite `ARD_murmansk_dockyard_contracts` was on the same row.
- `ARD_directorate_staff_map` at line 24045: `y = 15` to `y = 16`. Reason: follow-up after moving `ARD_winter_convoy_columns`, preserving parent-above-child pathing.

References remain valid: no focus IDs, prerequisites, mutual exclusions, allow/available blocks, or rewards were changed.

## Remaining blockers

1. Several template-style branches still depend heavily on generic custom-splinter reward helpers and do not expose enough visible decision/event/war/claim payoff signals in the focus file. Representative examples include FTH opening/route focuses at lines 52, 76, 99, 122, 145, 168, 191, 214, and 238; BSC generic-route blocks at lines 4313-5264; TNC at lines 5432-6394; ALA at lines 6561-7498. This is a design-depth issue and was outside the allowed patch scope.

2. No `country_event`, `news_event`, or `state_event` payoff calls were found in this file. Several trees rely on scripted helpers or variables for payoff visibility instead of direct visible event hooks. This may be intentional, but it leaves route payoff less visible from the focus file alone.

3. Remaining complex OR-convergence candidates need broader branch layout review before patching because moving one node may require moving a whole branch lane: `UDC_loyalist_statute_guarantees` line 10774, `SDZ_chain_of_custody_statutes` line 11990, `DHC_river_and_steppe_compact` line 14680, `KHC_steppe_and_mountain_compact` line 15871, `UWD_workers_canteen_compact` line 19133, `UWD_no_shipments_without_council` line 19323, `IUL_river_port_customs_board` line 21364, `BAC_amur_commune_endurance` line 22898.

4. Same-row mutual-exclusive pairs remain in several template branches: `FTH_settlement`/`FTH_radical_turn` lines 379/410, `BSC_settlement`/`BSC_radical_turn` lines 5232/5264, `TNC_settlement`/`TNC_radical_turn` lines 6362/6394, `ALA_settlement`/`ALA_radical_turn` lines 7466/7498, `BBH_settlement`/`BBH_radical_turn` lines 8412/8445, `KRS_settlement`/`KRS_radical_turn` lines 9215/9246, `IUL_settlement`/`IUL_radical_turn` lines 21100/21133, `BAC_settlement`/`BAC_radical_turn` lines 22239/22270. These are adjacent in a vanilla-tolerated spacing pattern, so I did not move them without visual confirmation.

## Validation run

- Post-patch layout parser: 25 trees, 1005 focuses; patched OR-convergence and ARD parent-row issues no longer reported.
- Remaining parser findings: 16 layout risks left as blockers above.
- Brace balance on `common/national_focus/005_soviet_collapse_custom_splinters.txt`: `brace_balance=0`, no negative-depth events.
- `git diff --check -- common/national_focus/005_soviet_collapse_custom_splinters.txt`: passed with no output.
- No-flag diff/status guard: `git diff --name-only -- gfx/flags ':(glob)**/*.tga' ':(glob)**/*flag*.gfx'` and matching `git status --short` guard both returned no output.

## No-flag confirmation

Confirmed: no edits were made to `gfx/flags`, `.tga` files, flag sprites, flag `.gfx`, or any visual flag asset path. No flag assets were touched.

## Notes for parent

The worktree was already dirty before this audit, including pre-existing changes in the same focus file. This handoff only claims the coordinate edits listed above plus this handoff file.
