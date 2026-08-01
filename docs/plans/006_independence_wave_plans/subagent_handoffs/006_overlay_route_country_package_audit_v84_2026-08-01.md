# Event 006 Overlay Route Country Package Audit v84

Date: 2026-08-01

Scope: IW-005 Flanders, IW-022 Dalmatia, IW-025 Vojvodina, IW-035 Livonia, IW-059 Mesopotamia, and IW-085 Cyrenaica.

Disposition: all six are overlay-only adapters for living vanilla tags or vanilla dynamic/cosmetic identities. None is an independently admitted Event 006 release package. The six planner triggers are explicitly fail-closed with `always = no`, and no standalone tag, history, focus-tree replacement, country registration, leader, portrait, flag, advisor, or package-dispatch admission was added.

## Executive finding

The six packages preserve their vanilla host identity and run only from narrow identity-specific daily hooks. This is coherent for an additive route-overlay feature, but it is not sufficient evidence for selectable Event 006 release admission. Keep all six out of automatic planner allocation until the remaining host-survival, focus/network, formable/patron, source, and runtime checks are closed.

The source-of-truth rows already classify IW-005 as a living-BEL overlay and IW-022, IW-025, IW-035, IW-059, and IW-085 as partial or research-gated overlays. This audit agrees with those dispositions.

## Country package coverage checklist

| Package | Vanilla identity and exact activation | Planner status | Coverage result |
|---|---|---|---|
| IW-005 Flanders | `original_tag = BEL`, `has_cosmetic_tag = BEL_flanders`; host hook `on_daily_BEL` | `can_plan_independence_wave_package_iw_005 = { always = no }` | PASS for bounded living-BEL overlay; not a standalone release candidate |
| IW-022 Dalmatia | dynamic country with `original_tag = CRO`, `has_cosmetic_tag = dalmatia`; host carriers D01-D50 | `can_plan_independence_wave_package_iw_022 = { always = no }` | PARTIAL; vanilla YUG dynamic-country route is preserved, but no Event 006 admission |
| IW-025 Vojvodina | dynamic country with `original_tag = HUN`, `has_cosmetic_tag = vojvodina`; host carriers D01-D50 | `can_plan_independence_wave_package_iw_025 = { always = no }` | PARTIAL; vanilla HUN dynamic-country route is preserved, but no Event 006 admission |
| IW-035 Livonia | `tag = LIT`, `has_cosmetic_tag = LIVONIA`; host hook `on_daily_LIT` | `can_plan_independence_wave_package_iw_035 = { always = no }` | PARTIAL; living-LIT cosmetic route is preserved, but no Event 006 admission |
| IW-059 Mesopotamia | `has_cosmetic_tag = neo_mesopotamia`, `has_global_flag = neo_mesopotamia_formed_flag`, and original-tag allowlist KUR/IRQ/SYR/PAL/EGY/KUW/LEB/ASY; host hooks KUR/IRQ/SYR/PAL/EGY/KUW/LEB/ASY | `can_plan_independence_wave_package_iw_059 = { always = no }` | PARTIAL; vanilla formable overlay is preserved, but no Event 006 admission |
| IW-085 Cyrenaica | `original_tag = LBA`, subject of ITA, fascist government, satellite/dominion autonomy; host hook `on_daily_LBA` | `can_plan_independence_wave_package_iw_085 = { always = no }` | PARTIAL / RESEARCH-GATED; independent Cyrenaica is intentionally suppressed, but actual start-state and historical source checks remain open |

## File surface checklist

The following surfaces were inspected for each package:

- Identity and eligibility triggers in `common/scripted_triggers/006_independence_wave_iw005_flanders_triggers.txt`, `006_independence_wave_iw022_dalmatia_triggers.txt`, `006_independence_wave_iw025_vojvodina_triggers.txt`, `006_independence_wave_iw035_livonia_triggers.txt`, `006_independence_wave_iw059_mesopotamia_triggers.txt`, and `006_independence_wave_iw085_cyrenaica_triggers.txt`.
- Lifecycle and value effects in the matching `common/scripted_effects/006_independence_wave_iw005_flanders_effects.txt`, `006_independence_wave_iw022_dalmatia_effects.txt`, `006_independence_wave_iw025_vojvodina_effects.txt`, `006_independence_wave_iw035_livonia_effects.txt`, `006_independence_wave_iw059_mesopotamia_effects.txt`, and `006_independence_wave_iw085_cyrenaica_effects.txt`.
- Five-action decision surfaces and categories in `common/decisions/006_independence_wave_iw005_flanders_decisions.txt`, `006_independence_wave_iw022_dalmatia_decisions.txt`, `006_independence_wave_iw025_vojvodina_decisions.txt`, `006_independence_wave_iw035_livonia_decisions.txt`, `006_independence_wave_iw059_mesopotamia_decisions.txt`, `006_independence_wave_iw085_cyrenaica_decisions.txt`, and the six matching files under `common/decisions/categories/`.
- Localisation in `localisation/english/006_independence_wave_iw005_flanders_l_english.yml`, `006_independence_wave_iw022_dalmatia_l_english.yml`, `006_independence_wave_iw025_vojvodina_l_english.yml`, `006_independence_wave_iw035_livonia_l_english.yml`, `006_independence_wave_iw059_mesopotamia_l_english.yml`, and `006_independence_wave_iw085_cyrenaica_l_english.yml`.
- Identity-specific hooks in `common/on_actions/006_independence_wave_iw005_flanders_on_actions.txt`, `006_independence_wave_iw022_dalmatia_on_actions.txt`, `006_independence_wave_iw035_livonia_on_actions.txt`, `006_independence_wave_iw059_mesopotamia_on_actions.txt`, and `006_independence_wave_iw085_cyrenaica_on_actions.txt`.
- Planner and reservation metadata in `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt`, `...region_02_triggers.txt`, `...region_03_triggers.txt`, `...region_04_triggers.txt`, `...region_06_triggers.txt`, and `...region_08_triggers.txt`, plus matching `common/scripted_effects/006_independence_wave_packages_region_*_effects.txt` files.
- Central package dispatch and admission surfaces in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt` and `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`.
- Existing package documentation in `docs/events/006_independence_wave/systems/iw005_flanders_overlay.md`, `docs/events/006_independence_wave/overview.md`, `docs/specs/006_independence_wave_specs/specs/006_independence_wave_spec_part_1_core.md`, `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md`, and the six prior adapter handoffs under `docs/plans/006_independence_wave_plans/subagent_handoffs/`.

No package-specific `.gfx`, flag, portrait, advisor, focus-icon, or country-definition surface is required by the current additive-overlay design.

## Missing or stale country-package surfaces

- There is no dispatch setup/final-validation/cleanup wrapper for IW-005, IW-022, IW-025, IW-035, IW-059, or IW-085 in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt`. This is consistent with the six packages being route overlays, but it blocks any claim that they are independently runnable Event 006 packages.
- None of the six appears in the runtime package adapter, content-attestation, or preflight admission OR-lists in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`. Do not add them until the open evidence listed below is complete.
- The region-08 reservation metadata remains stale relative to the adapter anchor: `common/scripted_effects/006_independence_wave_packages_region_08_effects.txt:20` loads IW-085, and `:81` reserves state `450` as the candidate anchor while trying `451` and `663` as compact states; the live adapter writes `independence_wave_anchor_state = 663` in `common/scripted_effects/006_independence_wave_iw085_cyrenaica_effects.txt:193` and checks state `663` in `common/scripted_triggers/006_independence_wave_iw085_cyrenaica_triggers.txt:28-31`. Because `can_plan_independence_wave_package_iw_085` is permanently false, this is an unadmitted metadata blocker rather than a current runtime regression. Resolve the intended anchor before any future admission.
- IW-059 and IW-085 lifecycle ideas use `allowed = { always = yes }` in their idea files, unlike the route-gated idea files for IW-005/IW-022/IW-025/IW-035. They are currently added and removed only by overlay lifecycle effects, but identity-gated `allowed` checks should be required before any broader admission or if manual/console injection is in scope.

## Map and state setup issues

Read-only map inspection passed file/definition checks, bitmap geometry, state-region membership, networks/adjacencies, and positions/ports for the requested states.

The inspected state records were coherent for the live vanilla hosts: IW-005 uses Belgian states 6 and 977; IW-022 uses YUG state 103 with optional Zara state 163; IW-025 uses YUG/HUN-origin state 45; IW-035 accepts Latvian state 12 or Estonian state 191; IW-059 uses Iraqi state 291; and IW-085 currently checks Cyrenaican state 663.

The important map issue is the IW-085 anchor mismatch. State 450 is Benghasi with a victory point and naval base, state 451 is Derna with a victory point and naval base, and state 663 is an interior Cyrenaica state with no capital and no victory point. The adapter's state-663 hold/garrison requirement therefore does not match the planner's state-450 anchor metadata. This must be reviewed before admission; no map rewrite was made.

Map artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/805ea17b34ad3a1e1a64636c1cb4c600a37068e3e102ac2121c454cd3d45a3ef/1ccf010ac97c1d78f23b1837bf4364a46e2fa43a4f60dca192dd6a4570544446/map-inspect.37f06fe42271cc01.json`.

## Politics, leaders, portraits, flags, advisors, and parties

- All six preserve the living vanilla host tag, government, parties, leaders, characters, portraits, flags, and country history. No fictional leader or opposite-gender portrait/name pairing was introduced.
- IW-005 remains Belgium with the vanilla `BEL_flanders` cosmetic identity; IW-022 and IW-025 remain vanilla dynamic-country identities created by the Yugoslavia focus tree; IW-035 remains LIT with vanilla LIVONIA cosmetic naming; IW-059 remains the vanilla `neo_mesopotamia` cosmetic formable; and IW-085 remains LBA under the specified Italian subject relationship.
- No package-specific advisor, high-command, commander, party, flag, or portrait asset is present or required. Any future identity redesign would require a separate source-reviewed plan and must not be folded into this overlay audit.
- IW-085 remains research-gated because the intended start-state autonomy and historical Cyrenaican symbol/leader evidence are not yet closed.

## Focus, decision, idea, and asset issues

- The meaningful vanilla focus trees remain untouched. Vanilla precedents inspected were the Dalmatia and Vojvodina dynamic-country branches in `common/national_focus/yugoslavia.txt`, the Livonia route in `common/national_focus/lithuania.txt`, and the Mesopotamia formable decision in `common/decisions/formable_nation_decisions.txt`.
- Each overlay has five decisions with visible cost, blocked-cost, effect-tooltip, `fire_only_once`, and AI-weight surfaces. Cost triggers use the exact `NOT = { resource < constant:cost }` boundary pattern in the six package trigger files.
- The timed guard action uses an intentionally inactive decision activation gate and is started by the preceding route actions. The existing IW-005 handoff records a one-day mission-timeout versus `on_daily` ordering caveat; retain that caveat until a runtime trace exists.
- Shared focus insertion, route-network/league/decision integration, patron/formable integration, and route-specific AI behavior remain open for IW-022, IW-025, IW-035, IW-059, and IW-085. These are design/admission blockers, not reasons to replace a vanilla tree.
- Existing shared decision icons and idea sprites are registered and referenced. No missing package-specific asset reference was found.

## Starting military, technology, industry, supply, and production

- The adapters do not create units, add free equipment, alter technologies, add research slots, change production lines, or rewrite industry, ports, railways, or supply. They set route metadata and charge real command power, manpower, equipment, trains, and army experience through the costed decisions.
- IW-022 uses `port_or_island` / `coastal_maritime`; IW-025 uses `agrarian` or `river_or_corridor` / `mounted_mobile`; IW-035 uses `river_or_corridor` / `coastal_maritime`; IW-059 uses `river_or_corridor` / `river_jungle`; IW-085 uses `port_or_island` / `desert_nomadic`; and IW-005 retains its existing industrial profile.
- Starting forces, technology, industry, production, and supply therefore remain those of the vanilla host/carrier. This is appropriate for an additive overlay but cannot support an independently balanced release package without a separate design and balance pass.

## AI and playability

- AI behavior remains host-country behavior with narrow decision `ai_will_do` entries and opportunistic garrison completion. IW-005's existing handoff explicitly notes that garrison completion is opportunistic.
- There is no package-specific front, diplomacy, focus-selection, research, production, or survival AI. This is acceptable only while the packages remain non-selectable overlays.
- Host survival, save/load persistence, suspension and resumption, and live AI traces remain unverified for all six packages. No HOI4 process was launched, per repository instructions.

## Localisation patch in this audit

Changed files:

- `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml` lines 6, 12, 18, and 28 now use the corresponding `independence_wave_iw059_mesopotamia_cost.*` script constants in all `_cost`, `_cost_blocked`, and `_cost_tooltip` triplets. Numeric values are unchanged.
- `localisation/english/006_independence_wave_iw085_cyrenaica_l_english.yml` lines 6, 12, 18, and 28 now use the corresponding `independence_wave_iw085_cyrenaica_cost.*` script constants in all `_cost`, `_cost_blocked`, and `_cost_tooltip` triplets. Numeric values are unchanged.

The patch also normalizes the train and equipment icon tokens to the existing `£GFX_train_texticon`, `£support_equipment_text_icon`, `£infantry_equipment_text_icon`, and `£motorized_equipment_text_icon` forms. Both files retain UTF-8 BOM encoding. A six-file cost-triplet scan found no remaining hardcoded numeric cost values.

Before: IW-059 and IW-085 player-facing cost strings duplicated literal numbers and, for IW-085, literal prose in blocked/tooltips.

After: the same values are read from the package script constants, so tuning remains synchronized with decision affordability triggers while preserving wording and costs.

## Validation performed

- Read-only HOI4 map inspection covered states 6, 977, 103, 163, 45, 764, 12, 191, 291, 663, 450, and 451 and returned `MAP_INSPECTED` with all five map validations passing.
- Verified all six `can_plan_independence_wave_package_iw_*` triggers are explicit `always = no` and that no central dispatch wrapper, runtime adapter, content-attestation, or preflight admission entry exists for these six ids.
- Verified each of the six on-action files is narrow and identity-specific rather than a global `on_daily` loop.
- Verified all six decision cost trigger families use the intended strict-less-than affordability checks and that all six localisation surfaces contain cost, blocked-cost, tooltip, effect-tooltip, and mission/localisation entries.
- Verified all six localisation cost triplets contain no hardcoded numeric costs after the IW-059/IW-085 patch and verified BOM bytes for the two changed files.
- No HOI4 launch, live save/load trace, live AI trace, or runtime event execution was performed.

## Fail-closed blockers before any standalone admission

1. Keep all six planner triggers at `always = no` until an explicit design decision makes a route overlay selectable.
2. Do not add dispatch/admission OR-list entries until each package has a complete adapter, content attestation, preflight, final validation, cleanup, host-survival, save/load, and AI evidence path.
3. Resolve IW-085 state-450 planner reservation versus state-663 adapter anchor, including capital/port/VP and garrison semantics, before any admission.
4. Close shared focus-tree insertion and route-network/league/patron/formable integration for IW-022, IW-025, IW-035, IW-059, and IW-085 without replacing their meaningful vanilla trees.
5. Gate IW-059/IW-085 idea availability by exact route identity if broader admission or manual injection is ever supported.
6. Complete source-reviewed leader/symbol and actual-start-state research for IW-085; retain its `PARTIAL / RESEARCH-GATED` status.
7. Produce host-survival, suspension/resumption, save/load, and AI runtime evidence for every route; the current source audit alone does not prove live playability.

## Simplifications and omissions

No broad identity redesign, new country package, new tag, leader, portrait, flag, advisor, focus tree, formable suite, or map rewrite was added. The only gameplay-adjacent change was the narrow IW-059/IW-085 localisation constant synchronization described above. The six packages remain intentionally non-selectable overlays, so their vanilla host military, technology, industry, supply, production, AI, and focus behavior are preserved rather than duplicated.

## Parent handoff

Review this handoff together with `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` and the six prior package handoffs. The recommended disposition is to preserve fail-closed non-admission for IW-005, IW-022, IW-025, IW-035, IW-059, and IW-085 and to queue the blockers above for a separately scoped design and runtime-evidence pass.
