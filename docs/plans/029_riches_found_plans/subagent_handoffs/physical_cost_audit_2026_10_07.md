# Event 029 physical cost contract audit

Date: 2026-10-07

Disposition: unresolved audit handoff. This report covers the ten decision IDs named by the parent and does not claim Event029 completion.

Scope: read-only source audit of physical costs, factory commitments, affordability, localization, debits, refunds, related mission starts, and selected mine lifecycle for the ten current profiles. The three transport profiles remain outside this pass as directed.

This subagent changed no gameplay, localization, AI, index, GUI, or asset files. Parent-owned source edits in the shared tree were preserved. This handoff is the only file written by this subagent.

## Result

All ten current profiles are within the four-cost ceiling when their specified opportunity costs are counted. The exact cost rows, shared affordability predicates, manual debits, and failure refunds line up for the named profiles. The repair reserve path does not duplicate equipment stock in source: it consumes the one-use state reserve and returns exactly the repair's truck and support-equipment debit to the decision owner.

The remaining issues are presentation and lifecycle questions. The category closes when the country loses its last mine even if the accepted spec's surviving contract, compensation claim, or short aftermath should keep the category available. The repair tooltip does not say that reserve funding returns the upfront equipment, and the Seal the Deep Sections tooltip omits the specified reduction to maximum output. Cost magnitudes remain fixed tier constants, while Part 3 describes state-sensitive cost inputs. These items are recorded below for the parent.

## Ten-decision cost and refund crosswalk

Amounts below are current source values. `CIV 2` is two civilian factories committed by the native `civilian_factory_use` modifier for the stated `days_remove` timer. It is a temporary capacity commitment, not a stockpile debit.

| Decision ID | Current cost profile and count | Timer or opportunity cost | Exact manual refund if the delayed result is invalid |
| --- | --- | --- | --- |
| `decision_riches_found_survey` | CIV 2, 100 manpower, 25 motorized equipment. 3 types. | Admin timer, 30 days. | 100 manpower and 25 motorized equipment. No political power refund remains. |
| `decision_riches_found_claim_register` | CIV 2, 10 political power, 300 manpower. 3 types. | Admin timer, 30 days. Starts Secure the First Rush. | 10 political power and 300 manpower. No support-equipment refund remains. |
| `decision_riches_found_reserve_deposit` | CIV 2, 25 political power, 100 manpower, 25 support equipment. 4 types. | Admin timer, 30 days. Starts Secure the First Rush. | 25 political power, 100 manpower, and 25 support equipment. |
| `decision_riches_found_camp_administration` | CIV 2, 300 manpower, 25 support equipment. 3 types. | Project timer, 60 days. | 300 manpower and 25 support equipment. No political power or truck refund remains. |
| `decision_riches_found_drive_deeper` | CIV 2, 300 manpower, 150 support equipment, and 25% temporary mine-output loss. 4 types including the output opportunity cost. | Long-project timer, 90 days. The tooltip says the mine retains 75% of output while the project runs. | 300 manpower and 150 support equipment. No political power or fuel refund remains. |
| `decision_riches_found_seal_depths` | CIV 2, 300 manpower, 150 support equipment. 3 spendable types. Count 4 if the specified lost maximum output is included as an opportunity cost. | Project timer, 60 days. Part 3 says sealing reduces maximum output. | 300 manpower and 150 support equipment. No political power or truck refund remains. |
| `decision_riches_found_nationalize_with_compensation` | CIV 2 and 40 political power. 2 types. | Long-project timer, 90 days. | 40 political power only. Compensation and settled-opinion effects remain on success. |
| `decision_riches_found_buyout` | CIV 2 and 40 political power. 2 types. | Long-project timer, 90 days. | 40 political power only. Compensation and settled-opinion effects remain on success. |
| `decision_riches_found_repair` | CIV 2, 75 motorized equipment, and 75 support equipment. 3 types. If its optional one-use reserve is counted as a separate spent resource, the maximum is 4. | Long-project decision timer, 90 days. Restore the Shaft mission starts concurrently and lasts 120-240 days. If the mine holds a stabilization reserve, that reserve is consumed at repair resolution. | If invalid, 75 motorized equipment and 75 support equipment return to the original decision owner. If the reserve pays on a valid resolution, the same two equipment amounts return and the reserve is consumed. |
| `decision_riches_found_permanent_seal` | CIV 2, 600 manpower, 150 support equipment, and permanent loss of mine output. 4 types including the output opportunity cost. | Long-project timer, 90 days. | 600 manpower and 150 support equipment if invalid. Permanent output loss occurs only on successful sealing. |

The profile amounts resolve through the centralized `riches_found_decision_cost` constants: political power is 10/25/40 for light/standard/heavy, manpower is 100/300/600, support equipment is 25/75/150, motorized equipment is 25/75/150, and standard civilian-factory use is 2. `riches_found_decision_duration` resolves the admin/project/long-project timers to 30/60/90 days.

The five profiles that removed political power from their prior vectors, survey, camp administration, drive deeper, seal depths, and permanent seal, have no remaining political-power debit, refund, or `ai_hint_pp_cost`. The retained political-power hints match their actual debits: claim registration 10, reserve deposit 25, nationalization 40, and buyout 40.

## Availability, native commitment, and localization

Each of the ten shared affordability composites is called from both the decision `available.hidden_trigger` and `custom_cost_trigger`. The resource display selectors use the same per-resource affordability components. The exact composite trigger locations are `029_riches_found_cost_triggers.txt` lines 97, 102, 116, 126, 192, 262, 272, 343, 348, and 364 in the row order shown above.

The civilian-factory component checks `num_of_available_civilian_factories > constant:riches_found_decision_cost.civ_standard_gate`, with the gate set to 1 and the displayed/committed standard value set to 2. The `GetRichesFoundCostCivStandard` selector calls that same component. The decision file's `@RICHES_FOUND_CIVILIAN_FACTORY_STANDARD` mirror is also 2, so the displayed amount, click affordability predicate, and native modifier agree at source level. No engine scenario was run for one-below, exact, or one-above availability.

The ten cost entries have base, blocked, and tooltip localization keys. Inline rows show at most three icon-backed values. Reserve deposit puts its fourth support-equipment value in the full tooltip. The relevant icons are `£civ_factory`, `£pol_power`, `£manpower_texticon`, `£motorized_equipment_text_icon`, and `£support_equipment_text_icon`. The last two are wired by `interface\chaosx_texticons.gfx` at lines 90 and 96. No literal resource-name fallback replaces an icon in these ten rows.

The temporary civilian commitment is not manually debited or refunded. The native modifier is active during the decision timer and expires with it. Vanilla precedent is `AST_union_strike` in `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\AST.txt` lines 2-42, with `days_remove = 25` and `civilian_factory_use = 1`.

The nationalization and buyout decisions still call `riches_found_compensate_contract_partner` before ending the contract. The helper checks that the stored contract partner and current controller exist, grants the partner the compensation political power, and applies `riches_found_concession_settled` opinion. This partner outcome is separate from the controller's 40 political-power debit and is not an extra payer cost.

## Severity-sorted findings

### P2: category lifecycle can close before accepted aftermath actions

The accepted Part 3 spec says the category remains open when the country has a surviving contract, compensation claim, or short aftermath action after losing its last mine. `riches_found_mine_management` currently shows only when `riches_found_country_has_category_mine` is true, and that trigger checks only for a controlled registered mine. The last-mine transfer therefore hides the category even if a valid non-mine claim or aftermath action survives. Review `common\decisions\categories\029_riches_found_categories.txt` and `common\scripted_triggers\029_riches_found_triggers.txt` lines 132-136 against Part 3 lines 5-15.

### P2: repair reserve funding leaves the net equipment cost unclear

`decision_riches_found_repair_tt` says the reserve pays the bill when crews arrive and is then spent. Source then returns the already-debited 75 trucks and 75 support equipment to the country that took the decision. The static cost row continues to show those amounts, which is accurate for the upfront affordability/debit step, but the tooltip does not say that both stocks return when the reserve covers the bill. Clarify the conditional reimbursement in `localisation\english\029_riches_found_decisions_l_english.yml` key `decision_riches_found_repair_tt` or its cost tooltip. If the reserve itself is treated as a spendable cost, it is a fourth cost type and has no dedicated texticon in the cost row.

### P3: the seal-depth output tradeoff is absent from its effect tooltip

Part 3 says sealing the deep sections lowers maximum output. The current `decision_riches_found_seal_depths_tt` lists Extraction Pressure and Mine Development changes but not the output reduction. Add that specific consequence to `localisation\english\029_riches_found_decisions_l_english.yml` key `decision_riches_found_seal_depths_tt`. The physical cost remains at three types, or four if foregone output is counted as an opportunity cost.

### P3: compensated exit tooltips omit parts of their preserved outcome

Nationalization applies `foreign_claim_pressure` +8, and buyout applies `foreign_claim_pressure` -8. Both effects are absent from their current effect tooltips. Both helpers also apply the settled-opinion modifier, while the tooltips mention partner compensation but not the opinion effect. The outcomes exist in source, so this is a player-facing explanation gap rather than a missing effect. Review `decision_riches_found_nationalize_with_compensation_tt` and `decision_riches_found_buyout_tt` in the same localization file.

### P3: tier amounts remain fixed across mine contexts

The current amounts are centralized fixed tier constants. Part 3's general cost rule says costs should respond to population, development, damage, distance, war, supply, local order, concession exposure, and previous failure. The user-provided profile names establish the current vector, but this audit found no per-mine scaling in those amounts. Reconcile whether these fixed profiles are accepted tuning anchors or whether parent balance work must add dynamic scaling. No coefficients were invented in this read-only pass.

## Category, action density, and player-facing values

The category is ordinary, with a static picture and one selected mine for the human player. `riches_found_state_is_active_selected_or_only_mine` lets AI evaluate each registered mine directly. Among these ten IDs only, the claims layer has survey before completion and claim registration plus reserve deposit after completion, the foreign layer has nationalization or buyout depending on relations, and the emergency layer can expose seal depths, repair, and permanent seal. These are scoped counts for this audit, not a complete count of every category action. The source phase reconciler documents a six-primary-action ceiling per layer.

The cost rows themselves are concise and icon-led. The four-value reserve deposit fits the three-value inline limit by placing support equipment in the full tooltip. The drive-deeper output retention and permanent-seal output loss are stated. The seal-depth output cap and repair reimbursement need the clarifications listed above. This pass did not inspect the category header's other four displayed mechanic values or assess their visual significance.

## Mission quality and duplicate risk

`decision_riches_found_claim_register` and `decision_riches_found_reserve_deposit` can start `mission_riches_found_secure_rush`. Its owner is the current country controller, its category is Riches Found, and its region is the selected controlled mine state. Completion requires the mission's progress state, camp administration, resolved claims, and Local Order above the floor. The duration starts from 105 days, varies with state conditions, and is clamped to 90-120 days. Success raises Local Order and Revenue Legitimacy. Timeout is partial when camp administration exists and otherwise fails with Local Order and Extraction Pressure penalties. Duplicate risk is controlled by the three-slot country cap and a guard against the same mission on any other controlled mine.

`decision_riches_found_repair` starts `mission_riches_found_restore_shaft` for that damaged, selected mine. Its owner and category are the same. Completion requires mission progress and `riches_found_restore_shaft_works_ready`. Duration starts from 180 days and is clamped to 120-240 days based on mine conditions. Success restores the shaft, raises Mine Development, and lowers Extraction Pressure. Timeout is partial when repair has started and otherwise fails with development and pressure penalties. The same three-slot cap and one-instance-per-country guard prevent duplicate copies. Both missions cancel and clear their subject/progress flags when the country no longer controls their target.

## AI, route locks, cleanup, and exploit checks

All ten actions target controlled registered mine states and retain their phase, crisis, contract, damage, or terminal-state gates. The AI path bypasses only the human selected-mine filter. Delayed results check the original decision owner through `ROOT` and `riches_found_mine_still_valid_for_payer`, which requires current control, a registered mine, and nonterminal state. Drive Deeper also matches its stored project controller. Repair also requires its Restore the Shaft subject. The controller-change cleanup clears deep-project and works-project markers, selected foreign targets, and mission state. No duplicate stock grant was found in the fund/repair path.

The decision timers resolve through their existing `remove_effect` blocks. The invalid-target refund therefore occurs at the timer's resolution point, not as an immediate refund on transfer. The source guards the original payer correctly. It does not establish what happens in a lose-and-regain cycle before expiry for every simple timed decision, and no runtime cycle scenario was executed.

The separate probability-auditor child owns the required scenario-specific weight analysis. No AI weights or coefficients were edited in this pass. This report contains no numeric AI comparison and should be joined with that child result before any broader balance-completion claim.

## Evidence and validation limits

- Frozen pre-change decision source: `docs\plans\029_riches_found_plans\evidence\2026_10_07_physical_cost_before\common__decisions__029_riches_found_decisions.txt`, SHA-256 `D3E81AF6F864A581F11EE3253C2AF6C2F1987C22298A732E2CD246967D53D590`.
- Current source identities at inspection: decisions `EBC33D0F6516E4B88ECBED35BB213F53381C729002226D6AF77B48D6AD5C166B`; cost triggers `5B93479FCC2E3367847CD5D97B4A0AE4D4275227A2D55F3F9BABA157D465A0D2`; decision localization `AF22486FC2ABD45FC3E347C61D3679FD8A140BB53C561D54128820ED7857B110`; scripted cost localization `8203A3A044699649B9F4A7D4D19C668DF1EAD9AAFEAF80C1070B66706D110B87`.
- `common\scripted_localisation\029_riches_found_scripted_localisation.txt` has a worktree diff relative to HEAD in an unrelated occupied-mine revenue-route selector. Its bytes match the frozen pre-cost snapshot and its `GetRichesFoundCostCivStandard` selector is unchanged. It was preserved.
- Offline Wiki sections read locally: `paradox_wiki\Decision modding - Hearts of Iron 4 Wiki.md` lines 300-356, file SHA-256 `7713B9BCEE5F3818D63AAFBD45D18E812A9173A7C59AB238384B57DB60DB6162`; custom-cost behavior is in lines 311-329 and timer/removal behavior is in lines 339-356. `paradox_wiki\Modifiers - Hearts of Iron 4 Wiki.md` line 686, file SHA-256 `FE41A26F2B8D3B8E78A9B0DEA9CE1A55F001D1E27886807A0A3FB2D2F535F14F`.
- Installed-game source read locally: `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\modifiers_documentation.md` lines 2202-2205, SHA-256 `00A0ECA6D2B3A70CE4B8A0D38997DD609AA0C9349DDCD04C8CAC92849425BE7E`; `common\decisions\_documentation.md` lines 1-33, SHA-256 `5E7E686B5582F32C38D898D805E17171E88F3BFEEE4A030DEB1884F9726DE019`.
- `hoi4.source_lookup` resolved vanilla `game:common/decisions/AST.txt`, decision `AST_union_strike`, lines 2-42, source revision `638a6517b248b8ec8cb385eebd227330b411690434c2827b0e4275209d6ac766`. The underlying installed file hash is `AAD50DA745F5A93C5F7470E06ED990A49A5416C81810849C8A2312600E81F4F2`.
- Parent-supplied script-validator result: `valid = null`, five checks, zero findings, zero unresolved, with 723 unchecked native argument blocks and 96 unknown scope roots. This is not engine proof.
- `hoi4.reference_search` returned Decision Cost, Timer, and `civilian_factory_use` citations but reported four omitted results. Higher-limit search and reference-context/read calls did not return a usable payload before termination, so the cited offline local sections were read directly. `hoi4.source_lookup` returned the vanilla precedent; current mod sources were reviewed locally.
- No tests, gameplay launch, GUI inspection/render, live game validation, or numeric probability evaluation were run. GUI work was explicitly out of scope. The separate AI probability handoff remains required for the weights.

## Changed files and handoff

Changed file: `docs\plans\029_riches_found_plans\subagent_handoffs\physical_cost_audit_2026_10_07.md` only.

Changed gameplay IDs: none. Audited IDs: `decision_riches_found_survey`, `decision_riches_found_claim_register`, `decision_riches_found_reserve_deposit`, `decision_riches_found_camp_administration`, `decision_riches_found_drive_deeper`, `decision_riches_found_nationalize_with_compensation`, `decision_riches_found_buyout`, `decision_riches_found_seal_depths`, `decision_riches_found_repair`, and `decision_riches_found_permanent_seal`.

No plan handoff was written. The parent should resolve the listed lifecycle and tooltip issues, decide whether the fixed tier values satisfy the spec's dynamic-cost rule, and combine this handoff with the separate probability auditor's findings. No commit was made because this is the requested audit-only subagent handoff in a shared tree with parent-owned source edits.
