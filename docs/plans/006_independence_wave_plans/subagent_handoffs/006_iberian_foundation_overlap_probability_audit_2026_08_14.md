# Event 006 Iberian founding-mission overlap probability audit

Audit date: 2026-08-14.

## Superseding implementation note

The initial read-only audit below is retained as historical evidence. The parent subsequently applied the bounded serialization and project-readiness guards described in the recommendation; the current source and post-change MCP receipt are recorded in the final section. No central attestation, Join, DM-01 manual activation, or package admission was widened.

Mode: read-only audit. No gameplay, localisation, or source files were edited by this subagent.

Scope: the shared `has_independence_wave_active_founding_mission` helper and the NAV/GLC founding-mission activation blocks only. Attestation, Join, country identity, package setup, and paid-project design were not widened.

## Audited surfaces

| Surface | Source and identifiers | Current behavior |
| --- | --- | --- |
| Shared active-founding helper | `common/scripted_triggers/006_independence_wave_decision_triggers.txt:41-50`, `has_independence_wave_active_founding_mission` | ORs six generic missions: `independence_wave_secure_provisional_capital`, `independence_wave_ice_hold_the_harbour`, `independence_wave_establish_revenue_service`, `independence_wave_register_population`, `independence_wave_hold_first_assembly`, and `independence_wave_confirm_traditional_authority`. NAV/GLC package missions are absent. |
| Generic activation consumers | `common/decisions/006_independence_wave_decisions.txt:81-87`, `128-135`, `195-202`, and `251-258` | DM-02, DM-03, DM-04, and DM-05 each require `NOT = { has_independence_wave_active_founding_mission = yes }` in `activation`. |
| NAV founding mission | `common/decisions/006_independence_wave_iberian_decisions.txt:14-25`, `independence_wave_nav_hold_fueros_together` | Auto-activates when `is_independence_wave_nav_package`, `independence_wave_iw_013_setup_complete`, and unresolved/failed crisis guards pass. It is non-selectable with `available = { always = no }` and uses `independence_wave_iberian_duration.founding_crisis`. Its activation does not test the shared helper. |
| GLC founding mission | `common/decisions/006_independence_wave_iberian_decisions.txt:206-217`, `independence_wave_glc_hold_council_together` | Same grammar as NAV, using `is_independence_wave_glc_package`, `independence_wave_iw_015_setup_complete`, and GLC compact-crisis flags. Its activation does not test the shared helper. |
| Package project gates | `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:89-118` | `has_independence_wave_nav_active_package_project` and `has_independence_wave_glc_active_package_project` list paid project decisions only; they do not include the founding mission. `is_independence_wave_nav_project_ready` and `is_independence_wave_glc_project_ready` require setup-complete and not-failed, but do not require the founding crisis to be resolved. |
| Mission cleanup | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:537-588` and `590-630` | NAV cleanup removes `independence_wave_nav_hold_fueros_together`; GLC cleanup removes `independence_wave_glc_hold_council_together`. The cleanup is package-scoped and does not replace activation serialization. |

`independence_wave_secure_provisional_capital` is deliberately `activation = { always = no }` and is opened by `activate_mission` from `common/scripted_effects/006_independence_wave_decision_effects.txt:911-916`. Therefore, adding NAV/GLC identifiers to the shared helper will not by itself guard this manual DM-01 activation path; the generic follow-up missions DM-02 through DM-05 are the direct helper consumers in scope.

## Required references consulted

The required offline Paradox wiki pages were opened for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, Decision modding, Event modding, On actions, Idea modding, and AI modding. The decision-specific guidance at `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:449-460` states that mission `activation` is checked daily, `available` controls completion, and `activate_mission` bypasses normal activation. `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` documents `has_active_mission`; `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` documents `activate_mission` and `remove_mission`.

The required vanilla documentation was consulted at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md` (`has_active_mission`), `effects_documentation.md` (`activate_mission` and `remove_mission`), `modifiers_documentation.md`, and `script_concept_documentation.md`. Vanilla precedents inspected included `common/decisions/YUG.txt` and `common/decisions/TUR.txt` for grouping `has_active_mission` guards and `common/decisions/SWI.txt` for explicit `activate_mission` use.

## MCP probability evidence

The mandatory first weighted-logic call was `hoi4.probability_inspect` with adapter `mission_ai_will_do`, source `common/decisions/006_independence_wave_iberian_decisions.txt`, and the declared NAV/GLC candidate pool `independence_wave_nav_hold_fueros_together`, `independence_wave_glc_hold_council_together`. It returned `PROBABILITY_SOURCE_INSPECTED` with workspace `mod_chaos_redux_ea3b2d67c2c0`, source revision `b261f5cd32f39068e2919235cc1adca9ea363daca320b359aee25362c63d7adb`, source hash `8a8f0e9d341c7963e8d341fe6d99e1f1509597f1e110db0651bcb3a78a446720`, `poolComplete = true`, two requested candidates, zero available candidates, zero available adapters, and no discovered weighted surface. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5c1a5ea370aea69840053788790830841316a06a6cf45ebb2fb7de21ca184985/4e0944b3b39bb07200b14162b3d533a108b12e1ddd022bfbfd12827aa90cd5f6/probability-inspect-8a8f0e9d341c.json`.

A second `hoi4.probability_inspect` on `common/scripted_triggers/006_independence_wave_decision_triggers.txt` with the complete eight-mission helper candidate list returned `PROBABILITY_SOURCE_DISCOVERED` with `discoveryReason = no_weighted_surfaces`, zero candidates, and zero available adapters. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2827cf3b343c930634e30590a7b7d684898e32fb0b51a8a45409d451b3e40026/594e48f2157ca783d0b621f04fc67b5f539ce0866c431cf620af6cf9d1ba9fc9/probability-inspect-89df08180fe9.json`.

For same-scenario baseline evidence, `hoi4.probability_evaluate` used adapter `mission_ai_will_do`, source `common/decisions/006_independence_wave_iberian_decisions.txt`, the complete declared candidate list of the six generic founding missions plus the two Iberian founding missions, and scenario set `006_iberian_foundation_overlap_complete_pool_baseline` with `nav_setup` and `glc_setup` states. Each state declared the package setup flag and an empty active-mission list. The call returned `PROBABILITY_ANALYZED_PARTIAL`, analysis id `probability-7b923983bca4eda53f7fc2ab`, source revision `b261f5cd32f39068e2919235cc1adca9ea363daca320b359aee25362c63d7adb`, source hash `8a8f0e9d341c7963e8d341fe6d99e1f1509597f1e110db0651bcb3a78a446720`, scenario hash `b6c7a5642e2d327364acb84a8b61084f4ff43f36bc4c7e920413ca0d177cedcb`, six unresolved items, and diagnostics that both `independence_wave_nav_hold_fueros_together` and `independence_wave_glc_hold_council_together` were never eligible across the supplied scenarios. The candidate pool was declared, but external package state was incomplete, so this is unresolved/partial evidence, not an exact score or probability. Artifacts: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16b1e29abc79421936f5ac7784f7ca1fd40fc8e47054ffc139b6331ae2781d2/6c114d31a7aeb02f1f3c62f1339db6abd8d8a0ea42076d4d6759e5c9a92ec069/probability-7b923983bca4eda53f7fc2ab.json`, ranking render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a87c56d6b811db06aea7460d12f212f01b1aa02b38912fe762df701e89faf8b7/e19c34d045884886b3abd4cd7a3b6a887138896fab202cfa5782960e2953154d/probability-probability-7b923983bca4eda53f7fc2ab-ranking.svg`, and unresolved render `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/d5d151d6227376ca68967b7c632a698b0a6c55ebc6abf6bb432712d3bedb4670/719d425ecb37a1375b193cff8eb6c8c9394d73f0de08c1dba69878d12cf37ed3/probability-probability-7b923983bca4eda53f7fc2ab-unresolved.svg`.

The required sweep route was attempted with the same source and scenarios, but returned `PROBABILITY_SWEEP_RANGE_REQUIRED` because the only supplied sweep path was a non-numeric active-mission list. No threshold or rank-reversal claim is made. No before/after `hoi4.probability_compare` was run because no source patch was applied.

The NAV and GLC missions have `ai_will_do = { base = constant:independence_wave_decision_ai.urgent }`, but they are non-selectable and `available = { always = no }`; this is a willingness field, not a click probability. MCP did not expose a runnable weighted candidate for either mission, so no AI dominance, starvation, or timing distribution can be inferred.

## Overlap finding

Source review identifies a real serialization gap. When either Iberian founding mission is active, the shared helper remains false because it only checks the six generic IDs. Any generic DM-02/03/04/05 activation whose other flags and costs pass is therefore not blocked by the helper. In the opposite order, if a generic founding mission is active first, the NAV/GLC activation blocks do not test the helper and can become active on their daily activation check. The result is a possible concurrent generic founding mission and Iberian founding mission in the same country.

This is a mission-overlap finding, not proof that every campaign state reaches the overlap. `is_independence_wave_nav_project_ready` and `is_independence_wave_glc_project_ready` do not require compact-crisis resolution, so paid package projects are a separate possible overlap surface; they are guarded by package-specific `has_*_active_package_project` helpers and were not widened in this audit.

## Recommendation to parent

A bounded serialization patch is warranted and appears structurally safe:

1. Extend `has_independence_wave_active_founding_mission` in `common/scripted_triggers/006_independence_wave_decision_triggers.txt` with `has_active_mission = independence_wave_nav_hold_fueros_together` and `has_active_mission = independence_wave_glc_hold_council_together`.
2. Add `NOT = { has_independence_wave_active_founding_mission = yes }` to the NAV and GLC founding-mission `activation` blocks in `common/decisions/006_independence_wave_iberian_decisions.txt`.
3. Do not add package attestation, Join, project-readiness, or paid-project changes as part of this fix. Do not rely on the shared helper to guard DM-01, because its `activation` is permanently `always = no` and its effect uses `activate_mission`, which bypasses activation.
4. If any future effect manually calls `activate_mission` for either Iberian founding mission, guard that effect call explicitly with the same no-active-founding-mission condition because `activate_mission` bypasses the mission's activation block.

The self-reference introduced by step 2 is safe for these non-selectable missions: initial daily activation sees no active founding mission, while an already active mission is not cancelled merely because its activation trigger later becomes false. Cleanup and compact-crisis resolution remain responsible for removal and terminal state.

After the owner applies the patch, rerun the same named scenarios through `hoi4.probability_compare` and add explicit paired states with a generic founding mission active and with the NAV or GLC founding mission active. The expected result is that the opposite founding mission and generic DM-02/03/04/05 activation surfaces are unavailable in each paired state. Complete package flags, package id, active-country membership, compact-crisis flags, and capital-control state must be declared so the post-patch result is not partial for missing external inputs.

## Classification, blockers, and omissions

- Current overlap conclusion: source-derived and bounded; the Clausewitz trigger semantics are supported by the offline wiki and vanilla documentation, but runtime overlap frequency is unresolved.
- MCP probability conclusion: unresolved/partial. The mandatory adapter inspection found no runnable weighted surface, and the baseline evaluation marked both Iberian missions never eligible under the minimal declared states.
- Candidate-pool completeness: the complete eight-mission list was supplied for the baseline evaluation; the analyzer resolved only four internal candidates and reported six unresolved items.
- External-factor completeness: incomplete for package runtime state; no exact probability, exact score race, timing distribution, or rank reversal is claimed.
- Skipped `hoi4.probability_simulate` and `hoi4.probability_sequence`: not applicable because there is no declared stochastic input or custom weighted pool cadence in this surface.
- Skipped `hoi4.probability_compare`: no source change was made in this read-only audit; the owner must run compare after applying any patch.
- No gameplay, localisation, event, attestation, Join, or package source edits were made.

## Parent implementation follow-up

The parent applied the recommended bounded serialization patch in the shared helper and both Iberian founding-mission activation blocks. The helper now includes `independence_wave_nav_hold_fueros_together` and `independence_wave_glc_hold_council_together`, while each Iberian activation requires `NOT = { has_independence_wave_active_founding_mission = yes }`. No DM-01 manual activation, paid-project gate, content attestation, or Join list was changed.

Post-change `hoi4.probability_inspect` on `common/decisions/006_independence_wave_iberian_decisions.txt` returned `PROBABILITY_SOURCE_INSPECTED` at source revision `91164388be8da1b30a3b6a1e3f57def8cc8b795ba7b79ad68793d6333c1adc38`, source hash `467fcfa673e2adfdc29aeb943acbf45bfa8741ae31c892aae8bc39ecd9a0b4e4`, with 22 mission candidates, 12 required inputs, zero inspect-unresolved inputs, zero available candidates, and an incomplete runtime pool. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2875548f0fc197536b3c053228430dd52e748c944aa92612f41448fa797036b8/30bef7e6bd894e5c43c98d1d28978179414be9c321adcd0e5173231bb15f3507/probability-inspect-467fcfa673e2.json`. A true before/after compare with complete typed package states remains pending; no quantitative balance claim is made.
