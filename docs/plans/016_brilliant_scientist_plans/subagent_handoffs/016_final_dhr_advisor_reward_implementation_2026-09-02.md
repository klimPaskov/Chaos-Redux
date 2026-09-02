# DHR paid-advisor reward implementation handoff

Date: 2026-09-02

Status: bounded implementation complete for the accepted Rae Syl and Thel Ior reward tranche; parent review and commit remain pending.

## Scope and ownership

This tranche implements only the two accepted diplomatic focus rewards and their existing political-advisor availability gates.

The owned focus IDs are `DHR_seat_the_human_delegates` and `DHR_open_the_translation_bureaus`.

The owned advisor IDs are `DHR_harmonic_envoy_rae_syl` and `DHR_shadow_listener_thel_ior`.

No focus ID, count, coordinate, prerequisite, mutual exclusion, focus AI weight, advisor cost, advisor AI factor, trait, portrait, character identity, branch, country, spirit, decision, event, GUI, or asset was added or redesigned.

The four other `dhrondan_focus_add_diplomatic_credit` reward calls remain intentionally unchanged on `DHR_ratify_the_two_world_covenant`, `DHR_exchange_maps_for_access`, `DHR_choose_our_terrestrial_partners`, and `DHR_invite_the_enclave_congress`.

The enclave-crisis availability and tooltip are already present in current `HEAD` `957ae81cc6539c2e29beebe92f4c6523eea91532` and are outside this tranche; `git diff HEAD` isolates the two reward replacements in the focus file, so no enclave lines are claimed as this implementation.

No files were staged and no commit was created.

## Exact source changes

In `common/national_focus/016_dhrondan_focus_tree.txt:438`, `DHR_seat_the_human_delegates` now keeps `set_country_flag = dhrondan_human_delegates_seated` and replaces only the repeated `dhrondan_focus_add_diplomatic_credit = yes` call with `custom_effect_tooltip = DHR_human_delegates_effect`.

In `common/national_focus/016_dhrondan_focus_tree.txt:930`, `DHR_open_the_translation_bureaus` now keeps `set_country_flag = dhrondan_translation_bureaus_open` and replaces only the repeated `dhrondan_focus_add_diplomatic_credit = yes` call with `custom_effect_tooltip = DHR_translation_bureaus_effect`.

In `common/characters/016_dhrondan_characters.txt:95-98`, `DHR_harmonic_envoy_rae_syl` remains restricted to `original_tag = DHR` and now requires both `dhrondan_covenant_route` and `dhrondan_human_delegates_seated`.

In `common/characters/016_dhrondan_characters.txt:163-170`, `DHR_shadow_listener_thel_ior` remains restricted to `original_tag = DHR` and now requires `dhrondan_translation_bureaus_open` plus one of `dhrondan_imperial_route`, `dhrondan_synod_route`, or `dhrondan_covenant_route`.

The existing advisor definitions still use `@DHR_ADVISOR_COST` (100 Political Power), `@DHR_ADVISOR_AI` (1), their original traits, and their original large and small portraits.

## Behaviour before and after

Before this tranche, seating Covenant delegates granted the receipt but also consumed the generic diplomatic-credit helper, and Rae was available from the Covenant route without the delegates receipt.

After this tranche, seating delegates records the same receipt, advertises the named paid-advisor unlock, and makes Rae eligible only after the Covenant regime and the receipt exist; appointment still requires the normal 100 Political Power payment.

Before this tranche, opening translation bureaus granted the receipt but also consumed the generic diplomatic-credit helper, and Thel was available on Synod or Covenant route flags without the translation receipt.

After this tranche, opening translation bureaus records the same receipt, advertises the named paid-advisor unlock, and makes Thel eligible in Imperial, Synod, or Covenant regimes only after the receipt exists; appointment still requires the normal 100 Political Power payment.

The completion rewards therefore remain idempotent receipt writes and do not appoint an advisor, grant free Political Power, create a spirit, or add a generic modifier ladder.

## Localisation

`localisation/english/016_dhrondan_focus_l_english.yml:21` adds `DHR_human_delegates_effect`: `Makes Harmonic Envoy Rae Syl available as a paid political advisor for §Y100 Political Power§!.`

`localisation/english/016_dhrondan_focus_l_english.yml:22` adds `DHR_translation_bureaus_effect`: `Makes Shadow Listener Thel Ior available as a paid political advisor for §Y100 Political Power§! in every D’Rhondan regime.`

The focus custom tooltips name the actual existing appointment operation and preserve the current English localisation file format.

## Baseline provenance and source hashes

The earlier probability handoff at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_final_dhr_advisor_reward_probability_2026-09-02.md` used fixture SHA-256 `e9902e866e322e9a13377091fee5079d4ac2c67ba7fe170485079766b1ecc1e5`, scenario hash `2db1f0f978c372b62d7261a12d480cce4302f2830f1a737ec68d1d35d7369f77`, immutable reference commit `4af9495786f600d2487e1ceec7aac7ff4bb9e7fd`, and retained focus blob `48af75cf250f1d2c42b7e686ccb983876bc987c3`.

That first comparison provenance predates the actual current prepatch state at `HEAD` `957ae81cc6539c2e29beebe92f4c6523eea91532` and is superseded for acceptance; its fixture, source hashes, and score results are retained only as historical evidence and must not be presented as the current immutable baseline.

The corrected same-fixture comparison is owned by `tranche4_probability` with `before` bound to current `HEAD` `957ae81cc6539c2e29beebe92f4c6523eea91532`; its final evidence belongs in the [corrected DHR advisor probability handoff](016_final_dhr_advisor_reward_probability_2026-09-02.md). At this handoff revision the corrected comparison is running, so no postpatch probability, score-delta, or acceptance claim is made here.

The superseded probability audit's pre-reward focus raw SHA-256 was `06772a28814d66eb83b10ca1d1ebe13c0791a754681077258f552949b2cf6baa`.

The accepted two-reward source captured immediately before the rewrite transaction had raw focus SHA-256 `356417596E44C1947E4A0EAD6B58AEBA01A28D64D199A486A1CD016680FFC93E`.

After restoring the rewrite drift, the current raw SHA-256 values are focus `13EA41E8AED3A555C77840E00F2D62F4B93845589B7E9BEA7AE8A9DFBF3DD624`, characters `C5652EDC94C8685C0EAF17CAF32B51C02E750D2B8ABA5D1A56CEE125751432C6`, and localisation `C2D5181BF781A47E375D042843E0308CF96B246562587ECE145F591CED375D6C`.

The current Git-normalized focus blob is `d4a4d8d72a86f427bfd23ce56eb62f6177410dc2`.

The raw focus hash differs from the accepted pre-rewrite raw hash because the recovery patch restored the exact authored coordinates and semantic content while the rewrite/recovery path left mixed line-ending representation; `git diff HEAD` confirms the only focus semantics owned here are the two reward-line replacements, while the enclave block is already part of current `HEAD`.

## Mandatory focus evidence

The pre-edit `hoi4.focus_inspect` returned `FOCUS_INSPECTED` for workspace `mod_chaos_redux_ea3b2d67c2c0`, with 88 focuses, 102 connectors, layout hash `cf0c22a43d47e8d04bd383b536b1c1e7bb1a489d22c7d4294eed3b432fa7eb87`, zero connector crossings, zero node intersections, zero long connectors, and bounds x 2-40/y 0-22.

The pre-edit inspect artifact was `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb693d42c369c3af70f43b84f15d1a67a7fc053b86f28e25b372b0cef1e2f6aa/5c45053818d4141a74015e0df11f50c88ea6b7a5accbc7fe5004a5e43dcd265f/focus-inspect.7ce72b409a9bae95.json`.

The post-recovery `hoi4.focus_inspect` returned `FOCUS_INSPECTED` with the same 88-focus count, 102 connectors, layout hash, bounds, and zero layout defects.

The post-recovery inspect artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5631d0d8f37f95a7017e31cf2d3b37e34b232e1b1d218a69ac92ebb9fe89ab74/8b1ba9e3fcb5eb5b9f9a12e8a774043a4f29ccd2006bd63a6308019b3d96e59e/focus-inspect.b77e57553c2c47e3.json`.

The post-recovery `hoi4.focus_render` returned `FOCUS_RENDERED`, preserved the same layout hash and 6992 by 2788 dimensions, and produced SVG hash `58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289`.

The post-recovery render artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/7a83c2ec50369dfba22ad44d9b8c764aad3aed368483b4b355d481c630f0b87b/246163d5dd2bb0abfb71a09f3a3deb5218f08b316a352035203221589003aab0/dhrondan_focus_tree.focus.html`, `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/58b73b820a4727005cbfede8b8ec426e300d884cbfbe48eb54beee1452dd5289/79b22eb9c002da9ec76e33457e8f55bfa213ff9f26673d58215f9e561eee5d5b/dhrondan_focus_tree.focus.svg`, and `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/424d134b212a6a1e72765c9b6ca546ff49aeb8f86971b619bf3e43c6b45537cc/0232a8b906068d1adf85dfb33d82b697d62079374dff00f500749afc697eeba7/dhrondan_focus_tree.focus.json`.

The default-parameter post-recovery `hoi4.focus_raster` returned `FOCUS_RASTERIZED` with the same 6992 by 2788 dimensions and PNG hash `43f131badb3467ae47ed8f116c25a210825d040473908c0749d696908df61dc5` as the pre-edit raster.

The post-recovery raster artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/43f131badb3467ae47ed8f116c25a210825d040473908c0749d696908df61dc5/bd0c76c6f1e2bbcaf7d3a0a0e5520f94b4b54e0269f1179f551ab78fc605869b/dhrondan_focus_tree.focus.png`.

All three post-recovery MCP calls reported no blocking focus diagnostics; the only warning was the unrelated vanilla `continuous_restrict_freedom_desc` localisation reference.

## Rewrite transaction and recovery record

The required authored/no-op `hoi4.focus_rewrite` attempt was blocked with `MCP error -32602 ... plan is required unless layoutMode is compact at plan`, and supplying `plan = {}` was rejected with `Invalid input at plan`.

The fallback `layoutMode = compact` call applied a full-tree coordinate rewrite, changing the layout hash to `353262d940e72744480fc1fb532b294a30b39383769449440002d438a78f20c3` and creating `common/national_focus/016_dhrondan_focus_tree.focus-plan.json`.

That compact rewrite was rejected as outside the two-reward scope.

Only the exact coordinate and y-position drift introduced by that transaction was restored with `apply_patch`, the generated sidecar was deleted with `apply_patch`, and the two accepted reward replacements were retained; the enclave gate was already in current `HEAD` and remained unchanged.

The compact rewrite execution artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fac1fb16722c3996610049f7ca6cb8e065ea5660f829a3cff71d9a06382188b2/ad426aa8392fd6ff8e8b7c7d6696428c1169ad5c97f4a9a87ab7ab3f0d77e8f2/focus-plan-changes.execution-validation.json`.

An initial invalid raster call was also retained as an exact tool error: `MCP error -32602: Input validation error: Invalid arguments for tool hoi4.focus_raster: Too small: expected number to be >=80 at horizontalSpacing; Too small: expected number to be >=60 at verticalSpacing; Too small: expected number to be >=1 at columns; columns is not valid in national mode at columns`.

## Source checks and unresolved limits

The final source scan confirms the two target focuses call only their receipt write and custom tooltip, while the generic diplomatic-credit helper remains on the four queued reward focuses listed above.

The final source scan confirms both advisor blocks retain their existing `allowed`, `cost`, `ai_will_do`, trait, and portrait fields around the new availability predicates.

`git diff --check` returned no whitespace diagnostics for the three owned source files.

No AI weight or other probability-bearing source was changed, so no new probability comparison was run by this subagent; the named fixture and baseline remain owned by the probability auditor and parent review.

Character appointment, Political Power affordability, and occupied-advisor-slot behavior remain unresolved at MCP engine level as documented by the baseline handoff because no character/advisor probability adapter is available.

Live game launch, log search, and runtime acceptance were intentionally skipped and remain user-owned.

No simplification was made within the accepted two-advisor tranche; the four other diplomatic rewards remain queued exactly as directed.
