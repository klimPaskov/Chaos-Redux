# Event 006 military archetype choice-cohort reflow handoff

Date: 2026-08-24

Status: **SOURCE-APPLIED / MCP POST-CHECK PASS / WHOLE EVENT HOLD-PARTIAL**

## Scope

This bounded tranche changes only the authored coordinates of the shared Event 006 military-archetype choice cohort in `common/national_focus/006_independence_wave_focus.txt`. It preserves every focus ID, prerequisite, mutual exclusion, availability predicate, completion reward, helper effect, AI block, icon, localisation key, cost, and route gate. No gameplay, package admission, or probability surface was changed.

## Coordinate change

The archetype hub moves from `x = 36, y = 7` to `x = 40, y = 7`, aligning it with the professional-defense convergence at `x = 40, y = 9`. The ten existing choice focuses remain on row 8 and shift one column right, in their existing order: `32, 34, 36, 38, 40, 42, 44, 46, 48, 50`. This shortens the hub-to-choice span without moving the convergence node or changing the choice semantics.

The border-guard parent remains at `x = 38, y = 5`. A trial that moved the hub to `y = 6` produced four connector/node intersections in the inspect receipt, so the accepted patch retains `y = 7` and records the remaining parent detour as an explicit safe warning rather than introducing crossings or intersections.

## Static preservation proof

The source comparison covers all 184 focus IDs. For the 11 changed IDs, the complete focus blocks are byte-equivalent after removing only their coordinate lines. Prerequisites, mutual exclusions, availability, completion rewards, helper effects, AI blocks, icons, and localisation references are unchanged. The changed IDs are `independence_wave_adopt_military_archetype_program`, `independence_wave_confirm_civilian_control`, `independence_wave_grant_military_autonomy`, `independence_wave_raise_mass_reserve`, `independence_wave_build_professional_core`, `independence_wave_fund_domestic_arsenals`, `independence_wave_accept_foreign_arms`, `independence_wave_adopt_border_defense`, `independence_wave_adopt_reclamation_doctrine`, `independence_wave_standardize_with_league`, and `independence_wave_preserve_independent_command`.

## MCP evidence

The pre-change national-tree inspection used `hoi4.focus_inspect` with `nodeSpacing = 80`, `laneSpacing = 80`, tree `independence_wave_focus_tree`, and returned 184 focuses, 195 connectors, zero crossings, zero node intersections, `longConnectorCount = 3`, and six authored Event 006 layout warnings. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e42cefc5f620d065a7ff35983dc55bbf1d38ee60f0eeaf0f092b1f2694240a81/064563f225b62308820845fcaa45e5742747edb020e2b429b4f904ae326af589/focus-inspect.b50ec7c2f6807aff.json`.

The pre-change render used the same tree and spacing family and returned the following source-linked artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e6ba2c85186c97080db15c19092f8ef5616325cef7f7eafabef1f12ec49ccab2/55b65dca002f8d9650ef660da536f58db0f63288fa76906bc2816ff2aca6507b/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d78b2305df0497d81ffd61502fb1897ca8fd35222b772b4eaa10a77cd333d540/982c5c699942702659a808324f01a28e590b2caf0c927eb53794d95fccf0821c/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e0209c1e7a4d26032c09da1503f5bb6369f2169b37022913063a6f9f25566fcd/8fa0b5e8056daaf068e23c5b1c6a0cafe6a73a3dc8b861caa6488d77713c82c4/independence_wave_focus_tree.focus.json`.

The post-change inspection returned 184 focuses, 195 connectors, zero crossings, zero node intersections, `longConnectorCount = 2`, maximum horizontal span 10, and no military long-edge diagnostic under the inspect spacing contract. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2b6649a84d9faa27b7e405210bb6c8074f4f10aa82bc5f0c4581850355a0ed10/778b50cd4f22ea533108ec9ba7f18e8674416cefbdfe15d2b765b224f1d73e7f/focus-inspect.05232ce42dc79a7d.json`.

The post-change render returned 184-focus HTML/SVG/JSON artifacts with no blocking diagnostics. It reduces authored Event 006 layout warnings from six to five: the military standardization long edge is removed, while the parent detour and the independent-command long edge remain documented alongside the treasury, former-host, and formable detours. The unrelated vanilla continuous-focus localisation warning remains outside Event 006 ownership. Artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5deb2e5143e9711d00288cf857f3bc82368f56259a2e8b48282cda065b8ce1aa/5ca5970b08c0b2c188be0c784d7299758702992734849f170bb1b7f9631b5689/independence_wave_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/aaba9f4b8e2a182487fa12b59d900188d7d2c39f27ef71dae4e70f5c4d1dd879/7cee49c93f24a6a9daf99c1444284b65763b75d6c3996e67e55aba114600c763/independence_wave_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fbcd5faa465ff3ebfc485c96a0186fb244cb79c5bafff72a3dbc9b1169653f72/abea811c24afe5c2a1b0c459e2a5fbb5a42966e21a35c5005a5ac780cd14e5dc/independence_wave_focus_tree.focus.json`.

The MCP focus validation status was `ok` with the source/reference/layout check passed. No live game or save/load claim is made. No probability comparison was required because this is coordinate-only.

## Boundary and remaining warnings

This tranche does not change the 32 content-attested packages, 29 compatible reservation groups, 40 adapters, 161 unattested rows, eight adapter-only fail-closed IDs, focus route coverage, or AI weights. Focus acceptance remains **HOLD** because five authored layout warnings and unrelated vanilla diagnostics remain, and the whole Event 006 implementation remains **HOLD / PARTIAL**.
