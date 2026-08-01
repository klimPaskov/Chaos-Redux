# IW-093 DOX / IW-098 SOK country-package closure audit v92

Date: 2026-08-01.

Scope: bounded non-asset country-package audit for Event 006 IW-093 Asante (`DOX`) and IW-098 Sokoto (`SOK`) after the v51 portrait/source closure handoff.

Result: the gameplay package is structurally wired and remains fail-closed, but neither package is runtime-admitted because the external runtime-content attestation receipts remain unset and the v51 visual/source gates remain blocked.

No portraits, flags, advisors, new tags, focus routes, formable adapters, central admission gates, or balance values were added or weakened.

## Country package coverage checklist

- [x] Tag registration is consistent for `DOX` in `common/country_tags/006_independence_wave_countries.txt:55`, while `SOK` remains the vanilla carrier in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/country_tags/00_countries.txt:270`.
- [x] DOX graphical shell is present in `common/countries/006_independence_wave_DOX.txt:1-13`, and the dormant DOX history shell is present in `history/countries/DOX - Asante.txt:1-10`.
- [x] SOK vanilla history keeps capital state `902`, `infantry_weapons = 1`, and vanilla `SOK_siddiq_abubakar` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/countries/SOK - Sokoto.txt:1-10`.
- [x] Country names, adjectives, government names, and party names are covered by `localisation/english/006_independence_wave_countries_l_english.yml:616-630` and `localisation/english/006_independence_wave_iw093_iw098_country_core_l_english.yml:8-23`.
- [x] DOX and SOK package IDs, regions, archetypes, reservation groups, and fixed anchors are registered in `common/scripted_effects/006_independence_wave_packages_region_09_effects.txt:11-70`, `common/scripted_triggers/006_independence_wave_packages_region_09_triggers.txt:9-43`, and `common/script_constants/006_independence_wave_package_constants.txt:144-149,361-366,561-579`.
- [x] Central dispatch calls setup, final validation, and cleanup for both package IDs in `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:24,42,58`.
- [x] Package setup and final validation require exact tags, origin/package metadata, fixed anchors, host survival, leaders, command roster, focus surface, values, staged ideas, force mapping, current-generation force proof, and external content attestation in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:594-779`.
- [blocked] `independence_wave_iw093_runtime_content_attested` and `independence_wave_iw098_runtime_content_attested` have no setter in the gameplay tree and are intentionally external admission receipts in `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:394-399`.

## File-surface checklist

The reviewed non-asset surface includes `common/characters/006_independence_wave_iw093_iw098_characters.txt`, `common/countries/006_independence_wave_DOX.txt`, `common/ai_strategy/006_independence_wave_iw093_iw098_ai_strategy.txt`, `common/ideas/006_independence_wave_iw093_iw098_ideas.txt`, `common/decisions/006_independence_wave_iw093_iw098_decisions.txt`, `common/decisions/categories/006_independence_wave_iw093_iw098_categories.txt`, `common/national_focus/006_independence_wave_iw093_iw098_focus.txt`, the paired scripted effects/triggers, package constants, region-09 loaders, central dispatch, package events, and the matching English localisation files.

The package has 43 focus IDs with complete focus localisation and 35 distinct focus icon IDs with registered sprites.

The package has 18 decision IDs with complete decision localisation, 83 distinct tooltip/cost keys with localisation, 16 decision icon IDs with registered sprites, and two decision categories with category localisation.

The package has four staged ideas with complete idea localisation and registered idea icons.

There is no separate mission surface; the timed projects are decisions with explicit active, success, failure, cancellation, transaction, and cleanup receipts.

## Map, state, and ownership findings

- [x] IW-093 reserves state `274` and IW-098 reserves state `902`, and the shared executor assigns the frozen anchor state as capital before package setup in `common/scripted_effects/006_independence_wave_execution_effects.txt:331-337`.
- [x] The fixed-anchor proofs require `state = 274` for DOX and `state = 902` for SOK, owned and controlled by the released country, and marked as its capital in `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:56-70,402-442`.
- [x] Vanilla state `274` has the Kumasi victory point `12787` and Accra victory point `10862` in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/274-British Africa.txt:1-31`.
- [x] Vanilla state `902` has Sokoto victory point `1891` and infrastructure level one in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/history/states/902-Sokoto.txt:1-27`.
- [warning] `independence_wave_iw093_kumasi_victory_point` is set to constant `12787` during setup and cleared during cleanup in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:607,814`, but no trigger or capital effect consumes that province ID; the runtime proof validates state `274` rather than a specific Kumasi province. This is a map-semantics risk to resolve with the shared map/capital owner before admission, not a safe local patch.
- [x] Host capital survival is checked through the saved former-host target in `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:411-431`, and host negotiation requires a living independent former host with a capital in the same trigger file and `events/006_independence_wave_iw093_iw098.txt:1-240`.
- [unresolved] Read-only `hoi4.map_inspect` for states `274` and `902` returned `SCAN_BYTE_LIMIT`; the static vanilla state files above are the available map evidence.

## Politics, leaders, portraits, flags, advisors, and parties

- [x] DOX politics initializes neutrality with 20/5/70/5 popularity, four package party names, no elections, and baseline civilian economy/export focus/volunteer-only laws in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:166-184` and `common/script_constants/006_independence_wave_iw093_iw098_constants.txt:121-144`.
- [x] SOK politics initializes neutrality with 10/5/80/5 popularity and four package party names in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:186-204` and `common/script_constants/006_independence_wave_iw093_iw098_constants.txt:146-159`.
- [x] Route politics distributions total 100 for all six DOX/SOK routes in `common/script_constants/006_independence_wave_iw093_iw098_constants.txt:162-202`.
- [x] DOX Prempeh II is a male civilian leader with despotism and centrism roles, and DOX Kwame Frimpong and Kwaku Ntim are male corps commanders in `common/characters/006_independence_wave_iw093_iw098_characters.txt:34-101`.
- [x] SOK Dikko and Bello are male corps commanders in `common/characters/006_independence_wave_iw093_iw098_characters.txt:103-154`; post-cutover leadership reuses vanilla male `SOK_siddiq_abubakar` only when that character is actually ruling in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:116-145` and `common/scripted_triggers/006_independence_wave_iw093_iw098_package_triggers.txt:453-499`.
- [blocked] The v51 source handoff records Prempeh visual likeness as failed, DOX commander identities as invented/generated, Dikko rights/treatment as unresolved, Hasan pre-cutover source as missing, Siddiq post-cutover source as rights-blocked, and Bello source as missing in `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_closure_audit_v51_2026_08_01.md`.
- [blocked] Existing DOX portrait DDS/sprite registrations are non-admitted artifacts, and no SOK flag triplet exists; the v51 handoff records unresolved DOX flag provenance and absent SOK flags.
- [x] No Event 006 advisor, high-command, dossier, or advisor portrait surface is defined by `common/characters/006_independence_wave_iw093_iw098_characters.txt` and `interface/006_independence_wave_iw093_iw098_portraits.gfx`.
- [x] All defined fictional-person surfaces are explicitly male in character metadata and use male names; no opposite-gender portrait/name pairing was found.

## Focus, decisions, ideas, assets, and formable contracts

- [x] DOX configures the full shared framework with constitutional, popular, traditional, emergency, patron, host, power-struggle, ambition, league, signature, and FORM-24 hooks while excluding radical sovereignty in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:480-535`.
- [x] SOK configures the full shared framework with constitutional, traditional, emergency, patron, host, power-struggle, ambition, league, signature, and FORM-25 hooks while excluding popular and radical routes and guarding Event 012 in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:536-590`.
- [x] Focus prerequisites, mutual exclusions, route receipts, bypasses, and AI weights are package-specific in `common/national_focus/006_independence_wave_iw093_iw098_focus.txt:20-792`.
- [x] Paid decisions use strict `>` affordability, transaction flags, timed completion, cancellation/failure paths, receipt flags, project-to-idea swaps, and cleanup in `common/decisions/006_independence_wave_iw093_iw098_decisions.txt:1-940` and `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt:1-765`.
- [x] Staged idea lifecycle is complete for both packages in `common/ideas/006_independence_wave_iw093_iw098_ideas.txt:1-70` and `common/scripted_effects/006_independence_wave_iw093_iw098_decision_effects.txt:203-337,713-764`.
- [blocked] DOX selects the `west_african_federation` registry family and SOK selects `sahel_confederation`, but `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:74-111` registers readiness only for existing FORM-01/02/03/04/05/07/39/48 adapters. No West African or Sahel family adapter, X-tag reservation, flag package, identity adapter, or integration adapter is admitted; this remains a central formable dependency and must not be bypassed by the country package.
- [warning] Older docs still contain route naming drift, including “federal route” in `docs/events/006_independence_wave/systems/iw093_iw098_signature_packages.md:187` and `docs/plans/006_independence_wave_plans/006_iw093_iw098_signature_packages_improvement_addendum_2026_07_18.md:86`, plus the stale SOK “host settlement” AI wording in the addendum around line `146`; implementation correctly uses `constitutional_cabinet`, `iw098_court_civic_balance`, and `iw098_frontier_security`.

## Starting military, technology, industry, supply, and production

- [x] DOX loads force-registry row `p93`, which resolves to profile `river_jungle` and military tradition `64`, and SOK loads row `p98`, which resolves to profile `mounted_mobile` and military tradition `70`, in `common/script_constants/006_independence_wave_force_package_constants.txt:384-389` and `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:620-637,681-698`.
- [x] Dynamic starting force materialization inherits host technology and research slots, defines the profile-specific division template, creates opening divisions and stockpiles, and records a generation-bound application receipt in `common/scripted_effects/006_independence_wave_force_effects.txt:790-803,871-887`.
- [x] `can_apply_independence_wave_force_package` requires active origin, valid profile/tradition, at least three reinforcement pathways, command roster readiness, generation metadata, anchor ownership, and a distinct living former host in `common/scripted_triggers/006_independence_wave_force_triggers.txt:70-107`.
- [x] No package-specific free divisions, free equipment, or major balance injection is present in the DOX/SOK decision or focus effects; paid project costs remain centralized in `common/script_constants/006_independence_wave_iw093_iw098_constants.txt:43-111`.
- [x] AI strategy surfaces exist for foundation, host crisis, and all six government routes in `common/ai_strategy/006_independence_wave_iw093_iw098_ai_strategy.txt:1-136`, using documented vanilla strategy types and package constants.
- [warning] There are no DOX-specific history production lines and SOK vanilla history begins with only `infantry_weapons = 1`; this is intentional because runtime force setup inherits host technology and derives stockpiles/production support, but live playability still depends on the shared release transaction supplying a valid host and three reinforcement pathways.

## Patch applied

Changed `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:812` to clear `independence_wave_iw093_runtime_content_attested` during exact DOX/package-93 cleanup.

Changed `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.txt:874` to clear `independence_wave_iw098_runtime_content_attested` during exact SOK/package-98 cleanup.

Changed the helper contract row in `common/scripted_effects/006_independence_wave_iw093_iw098_package_effects.md:31` to document the receipt reset.

Before the patch, a future external admission receipt could survive a package teardown and be inherited by a later generation on the same carrier.

After the patch, exact package cleanup clears the receipt together with setup, focus, route, idea, value, and leader state, while leaving the central admission gate fail-closed and leaving Event 012 lifecycle flags untouched.

This is a narrow cleanup-only safety correction and does not set, weaken, or infer either attestation.

## Validation

- `python .tools/audit_event6_allocator.py` passed with 149 publishers, 126 automatic/high-chaos selectable packages, 14 attested packages, and 13 compatible reservation groups.
- Static focus audit found 43 focus IDs with zero missing localisation keys, 35 distinct focus icons with zero missing sprite registrations, and 43 hidden focus effects with zero missing scripted effects.
- Static decision audit found 18 decision IDs with zero missing localisation keys, 83 tooltip/cost keys with zero missing localisation keys, and 16 decision icons with zero missing sprite registrations.
- Static idea audit found four idea IDs, four idea icons, and zero missing localisation or sprite registrations.
- Static package constant audit found 184 referenced constant groups/keys with no unresolved package constant reference, and all six route politics rows sum to 100.
- Brace/quote syntax checks passed for the eight touched package script surfaces, and `git diff --check` passed for the two edited package-effect files.
- `audit_chaosx_country_tags.py --surface-scan` was attempted but exceeded the 64-second command timeout while scanning the installed workspace; no report was written.
- Read-only `hoi4.map_inspect` and `hoi4.focus_inspect` were attempted but returned `SCAN_BYTE_LIMIT`; no MCP write tool was called.
- Hearts of Iron IV was not launched, and no in-game or live-save validation is claimed.

## Remaining setup or identity risks

The package remains incomplete for runtime admission until a future owner clears the v51 visual/source blockers, supplies exact DOX/SOK flag evidence, and writes the external attestation only after the complete country-package audit.

The pre-cutover SOK branch remains intentionally unavailable until Hasan receives a sourced, rights-clear, face-visible treatment, and the post-cutover Siddiq branch remains blocked on an admitted portrait/source package.

The FORM-24 and FORM-25 family adapters, X-ending tags, flags, identity adapters, integration adapters, and member-policy receipts remain outside this country-package patch and must stay behind central readiness gates.

The Kumasi-specific province/capital semantic proof remains an unresolved map review item because setup records province `12787` but only validates state `274` as the capital.

No simplification was introduced by this audit; the existing fail-closed admission and content blockers remain in force.

Plan handoff path: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw093_iw098_country_package_closure_v92_2026_08_01.md`.
