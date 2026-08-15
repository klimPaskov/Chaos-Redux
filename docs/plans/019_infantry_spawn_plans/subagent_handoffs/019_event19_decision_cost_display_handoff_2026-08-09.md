# Event 19 provider cost-display contract handoff

Date: 2026-08-09
Owner: `/root/event19_decision_audit_current`
Parent: `/root`

## Changed files

- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` — added `get_management_cost_display` owner callbacks for 504-510 and 522.
- `common/scripted_effects/002_zombie_outbreak_effects.txt` — added provider 511 callback.
- `common/scripted_effects/012_africa_effects.txt` — added providers 512 and 513 callbacks.
- `common/scripted_effects/010_death_effects.txt` — added provider 514 callback.
- `common/scripted_effects/018_resources_found_cave_effects.txt` — added provider 518 callback.
- `common/scripted_effects/020_black_plague_effects.txt` — added provider 520 callback.
- `common/scripted_effects/cbrn_doctrine_effects.txt` — added provider 521 callback.
- `common/scripted_localisation/019_infantry_spawn_scripted_localisation.txt` — added selected-row request and sustainment profile selectors with neutral ledger-backed fallback.
- `localisation/english/019_infrantry_spawn_l_english.yml` — replaced static request/sustainment cost text and blocked/tooltip variants; added 19 request and 19 sustainment profile strings.
- `common/scripted_effects/019_infantry_spawn_ledger_effects.txt` — retained committed provider-manifest row/accounting totals while publishing obligation rows.
- `common/scripted_effects/019_infantry_spawn_generation_effects.txt` — captured manifest totals and the actual obligation-array tail delta after provider reconciliation.
- `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt` — added the manifest-aware appended-row/UID/accounting verifier and removed fixed two-row assumptions.
- `common/scripted_effects/019_infantry_spawn_management_effects.txt` — allowed equality materialization only for registered zero-row family manifests; ordinary and nonzero family requests still require a strict obligation-row increase.
- `.tmp/event19_decision_audit_current.md` — audit evidence and remaining issue list.

The root-owned shared enum/cache changes in `common/script_constants/019_infantry_spawn_constants.txt` and `common/scripted_effects/019_infantry_spawn_muster_board_effects.txt` were preserved and not duplicated.

## Before / after

Before, Event 19 selected-family sustainment text listed only base zombie, weak ghost, and coal golem. Providers 504-522 either had no provider-specific text or appeared to require the 501-503 costs. After, the selected row reads its owner-selected profile from `infantry_spawn_muster_gui_family_cost_profile_entries`; debit-backed providers show their own constants, while providers whose Event 19 payment callbacks only settle the ledger explicitly state that no separate stockpile debit occurs. The payment, refund, category, AI, and registry paths were not changed.

The selected-family spawn verifier previously assumed exactly two appended obligation rows. It now receives the committed manifest row count and aggregate manpower/equipment-debt totals, checks the actual tail size and sequential UIDs from the request snapshot boundary, validates row ownership/payment/status fields, and compares observed accounting to manifest-derived totals. Providers 518 and 520 publish zero rows because both manifest per-battalion costs are zero; the shared materialization proof explicitly accepts equality only for this registered zero-row family case. Existing rollback truncation still removes every tail row back to `infantry_spawn_obligation_row_count_before_create` and restores country/lot aggregates exactly as before.

## Validation and evidence

- Targeted `rg` census confirms one callback for each requested ID 501-514, 518, 520, 521, 522.
- 19 profile keys exist for both request and sustainment selectors; all selector branches use `infantry_spawn_muster_board_selected_family_index_is_valid` and the shared cache array.
- The four ordinary decision cost keys now resolve through `GetInfantrySpawnSelectedFamilyRequestCost` / `GetInfantrySpawnSelectedFamilySustainmentCost`.
- Targeted diff/brace scans were run. Repository-wide `git diff --check` reports pre-existing blank trailing-space lines in unrelated in-flight Event 19 owner edits; the added callback and localisation lines are clean. No game launch was performed. No GUI MCP call was made because Event 19 currently has no scripted GUI surface.
- Manifest census covered all 18 requested providers: compatibility wrapper 501/502/503/511/514/518/520 (518/520 zero rows), three rows 504/505/506/507/509/522, four rows 508/510, two rows 512, sixteen rows 513, and seven rows 521. Targeted brace scans passed for the edited ledger, generation, muster-board, and management files.
- The installed MCP inventory has probability inspection but no decision-specific inspect/render endpoint; prior probability artifacts are cited in the audit report.

## Remaining risk

No known verifier blocker remains in the bounded scope. Medium residual risk: provider callbacks 512/513/521 keep bespoke manifest profiles, and derivative sustainment remains intentionally limited to providers 501-503; neither design boundary was broadened by this patch.
