# IW-048 Udmurtia current admission audit

Date: 2026-08-26.

Auditor: bounded country-package audit subagent.

Status: HOLD / fail-closed. UDM is not safely admissible at the 32-package boundary. No gameplay, central admission, map, asset, spreadsheet, or registry files were changed. This handoff is the only file written by this audit, and no files were staged or committed.

## Accepted contract

- Accepted registry row: `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:49` identifies IW-048 as Udmurtia, tag `UDM`, `reuse_registered_tag`, automatic pool eligibility only when not living, reservation group `RG-399`, anchor state `399` (Izhevsk), depth `Layer B`, compact industrial-forest republic, and high research confidence.
- Research resolution: `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:49` requires a defensible sourced period leader or provisional institution, conditionally reuses the registered flag, binds the compact anchor at release, and explicitly blocks the package until leader/identity and final asset provenance are defensible.
- Anchor reservation: `docs/specs/006_independence_wave_specs/research/006_state_anchor_and_reservation_groups.csv:34` allows RG-399 only when state 399 is unique, UDM is not living, and the host remnant test succeeds; the protected host state must be retained first.
- Authority: `docs/specs/006_independence_wave_specs/quality/package_manifest.md:37-47`, `docs/specs/006_independence_wave_specs/quality/simplifications_omissions_and_blockers.md:47-57`, and `docs/plans/006_independence_wave_plans/006_independence_wave_resume_packet.md:314-330` require package-local fail-closed setup, content attestation, normal and SCN-008 preflight, deterministic Join, and parent-owned identity/asset acceptance before central admission.

## Package coverage checklist

- Identity and tag: covered through vanilla `UDM`; `common/country_tags/00_countries.txt:239` maps `UDM` to `common/countries/Udmurtia.txt`, and no mod tag, country-history, character, or flag override was found.
- Anchor and history: covered by vanilla `history/states/399-Izhevsk.txt` and `history/countries/UDM - Udmurtia.txt`; the package-local trigger/effect contract names state 399 and uses the vanilla capital/history.
- Politics and parties: covered by package-local baseline and four route effects in `common/scripted_effects/006_independence_wave_udm_package_effects.txt:137-214`, with matching localisation in `localisation/english/006_independence_wave_udm_l_english.yml:1-67`.
- Leader and roster: source-wired to vanilla `UDM_boris` through `common/characters/UDM.txt:2-12`, but admission is gated by the parent-owned rights flag and the runtime portrait remains generic.
- Flags: vanilla ideology ladder is reused; `gfx/flags/UDM_communism.tga`, `UDM_democratic.tga`, `UDM_fascism.tga`, and `UDM_neutrality.tga` exist in the installed game, with no mod replacement.
- Forces and ideas: package-local force mapping, seven UDM ideas, four AI strategy profiles, and ten timed projects are present, but force/archetype contract review remains open.
- Focus and decisions: five guarded shared focus callbacks and one local category with a 420-day founding mission plus ten timed projects are present and localised.
- AI and diplomacy: industrial survival, host restraint, settled compact, and emergency guard strategies are present; host, corridor, former-host, and league routes are guarded in the UDM triggers/effects.
- Assets and manifests: no new UDM portrait, flag, focus icon, idea icon, or country asset manifest is claimed; the existing portrait provenance gate is unresolved.

## File surface checklist

- Constants: `common/script_constants/006_independence_wave_constants_registry.txt:1873-1888` defines force profile `industrial_security=2`; `:2149` maps p48 and `:2363` maps military tradition 54; UDM pressure, route, cost, duration, and start values are at `:9262-9331`.
- Scripted triggers: `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:9-202` covers tag/origin, state/host, cost, roster, route, force, generation, readiness, setup, and cleanup guards.
- Scripted effects: `common/scripted_effects/006_independence_wave_udm_package_effects.txt:9-373` covers ledgers, route politics, focus callbacks, setup, force loading, AI profile, projects, and guarded cleanup; its header explicitly records that central wiring is intentionally absent.
- Decisions and category: `common/decisions/categories/006_independence_wave_categories.txt:464-467` defines `independence_wave_udm_industrial_forest_category`; `common/decisions/006_independence_wave_siberian_decisions.txt:2320-2511` contains the founding mission and ten UDM projects.
- Ideas: `common/ideas/006_independence_wave_ideas_registry.txt:4282-4359` defines `udm_fragmented_workshop_mandate`, `udm_industrial_forest_compact`, `udm_workshop_charter`, `udm_worker_forest_councils`, `udm_cultural_register`, `udm_cultural_land_compact`, and `udm_industrial_emergency_command`.
- AI: `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt:3387-3460` defines the four UDM strategy profiles and package/setup gates.
- Focus callbacks: `common/national_focus/006_independence_wave_focus.txt:129,182,216,1447,1718` contains the five guarded shared callbacks; there is no dedicated UDM tree or missing UDM icon surface.
- Localisation: `localisation/english/006_independence_wave_udm_l_english.yml:1-67` covers category, mission, all ten projects, cost/effect text, seven ideas, and four party names.

## Central admission and roster surfaces

- Setup dispatcher: `common/scripted_effects/006_independence_wave_effects.txt:3403-3444` has 27 package setup wrappers and ends at Bashkiria; UDM is absent.
- Final validation dispatcher: `common/scripted_effects/006_independence_wave_effects.txt:3446-3492` has no UDM wrapper.
- Cleanup dispatcher: `common/scripted_effects/006_independence_wave_effects.txt:3494-3522` has no UDM wrapper.
- Adapter registry: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-61` has no IW-048 adapter predicate.
- Content attestation: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:65-202` has 32 accepted rows but no IW-048 row.
- Normal preflight: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:204-405` has no IW-048 branch.
- SCN-008 preflight: `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:411-558+` has no IW-048 branch.
- Deterministic Join: `common/scripted_effects/006_independence_wave_join_effects.txt:213-247` ends at `iw_184` without IW-048; Join is consolidated rather than exposed in a separate file.
- Region planning is intentionally ahead of admission: `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:421-428` can plan/reserve IW-048 when RG-399/state 399 are available, and `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:937-947,1037-1066` loads IW-048 and reserves state 399 with archetype `industrial_breakaway`. Planning availability is not execution admission evidence.

## Highest-impact blocker and smallest next action

The single highest-impact blocker is the unresolved parent-owned identity and portrait-rights gate for `UDM_boris`. `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:90-95` requires `independence_wave_iw_048_identity_rights_cleared` plus `UDM_boris`, and setup can only checkpoint that roster at `common/scripted_effects/006_independence_wave_udm_package_effects.txt:248-250,279-280`. The accepted research row explicitly blocks on a defensible sourced leader or institution. The only exact Boris Berman image located in the prior source gate is a 272x359 fair-use/non-free image with no redistributable license; the vanilla runtime token `GFX_portrait_Boris_Berman` resolves through `interface/_leader_portraits.gfx:7086-7089` to `gfx/leaders/Europe/Portrait_Europe_Generic_1.dds`. This is an unapproved generic/rights fallback, not admission evidence.

Smallest implementable next action: obtain an exact Boris Zakharovich Berman period image with explicit redistributable rights or written permission, or provide authentic archival material for the provisional institution required by the research resolution, then route the complete portrait-specific provenance, framing, runtime-output, and wiring review through `chaosx_portrait_creator`; only the parent/identity owner may set `independence_wave_iw_048_identity_rights_cleared` after that review. Do not substitute a generic texture, wrong Boris, or generated portrait.

## Secondary unresolved gates

- Force/archetype contract: `common/script_constants/006_independence_wave_constants_registry.txt:1873-1888` contains `industrial_security` as a force profile, while the shared archetype table at `:6809-6822` has no `industrial_security` archetype. UDM setup requires archetype `industrial_breakaway` and force profile `industrial_security` at `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt:136-172`; the package mapping is therefore an accepted-but-unresolved `industrial_security` to `industrial_breakaway` substitution. The owner must either register a distinct shared archetype and update generic consumers or explicitly accept `industrial_breakaway` as the UDM package archetype; this is not safe to patch locally.
- State/host proof: vanilla state 399 is owned by SOV, has SOV and UDM cores, capital/VP data, infrastructure 2, chromium 18, and no mod override in `history/states/399-Izhevsk.txt`; dynamic host retention and protected-state proof still require runtime scenario evidence.
- Typed probability fixtures: the mandatory probability inspection found the mission pool incomplete (`candidates=88`, `availableCandidates=0`, `requiredInputs=16`, `unresolved=0`) and no weighted AI strategy surfaces. No owner weight patch occurred, so no `probability_compare` was run and no quantitative balance claim is made.
- Whole-event and central evidence: adapter/attestation/preflight/Join/dispatch coverage is absent by design until the package packet is accepted; adding central rows now would bypass the fail-closed contract.

## Map, state, and setup findings

- Direct vanilla source review confirms `history/states/399-Izhevsk.txt` uses `id=399`, `STATE_399`, owner SOV, core SOV and UDM, capital 399, VP 6278, and the expected province list; no package-specific state rewrite, custom state, railway, port, supply, or resource fallback is present.
- `hoi4.map_inspect` direct inspection of state 399 succeeded with membership, region, networks, and adjacency checks in revision `bc56526e67af5a3c4980b1f8b4679c2ecb937bbeaec1015dc889aad6784ea012`. Useful artifacts are `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/bbe59bf3c5d64437b7e992cbe71c4acb3462c0fef276c518d8706a8827035192/cccda109a572c3e557472c7af103689d8a4151ac635284893e7eb82689727252/map-inspect.bc56526e67af5a3c.json` and the overview PNG under artifact `06862ee46ae6ff2778002719a3bbd5bcd567fefa7fd3c1da0f612bd363b84d11`.
- The MCP map validation result is false because the workspace has 2,654 unrelated building-position and port-adjacency errors; no UDM-specific state 399 error was returned. No map rewrite was attempted, so rollback/recovery evidence is not applicable.
- Package triggers fail closed on state 399 ownership/control/capital, former-host protection, generation, force mapping, and host route state. A live/save-load or dynamic host proof was not claimed.

## Politics, leader, portrait, flag, advisor, and party findings

- Vanilla history provides democratic ruling party, elections, and 60/20/10/10 source popularity ordering at `history/countries/UDM - Udmurtia.txt:86-101`; package setup initializes its own 36/24/30/10 baseline and four route distributions, while guarded cleanup restores vanilla democratic politics and 60/10/10/20 popularity ordering at `common/scripted_effects/006_independence_wave_udm_package_effects.txt:320-370`.
- Four package party names and route effects are localised and wired; no stale party or cosmetic-tag references were found.
- `UDM_boris` is the exact intended character id and is recruited by vanilla history, but the rights flag and exact sourced portrait requirement remain unmet. No package-specific advisor, high-command, commander, or alternate leader surface was added; no generic personal-name fallback is permitted.
- Vanilla UDM ideology flags are present and reused under the accepted conditional contract; no new flag or alternate identity asset is justified before rights/identity clearance.

## Focus, decisions, ideas, and assets

- Focus callbacks are guarded by UDM package/setup checks and render within the shared Event 006 tree; no dedicated UDM focus-tree assignment or icon gap was found.
- The UDM category, 420-day founding mission, and exactly ten timed projects have visible/available/cancel/effect localisation and route-specific trigger guards. Strategic projects use the current shared strategic payment effect; the current UDM trigger file contains the concurrent worktree change to the strategic-cost condition and was not modified by this audit.
- Seven UDM ideas have package-local names, pictures, and lifecycle cleanup. Their stability, supply, recruitable, factory-capacity, production, research, defense, organisation, and training modifiers are package content; no new balance target was introduced or quantitatively claimed.
- No UDM focus/idea/decision art gap was found. The portrait source gate is the only asset-level admission blocker currently evidenced; no RunPod operation or generated fallback was used.

## Starting military, technology, industry, supply, and production

- UDM inherits vanilla country history and starting setup; the package adds guarded force mapping rather than inventing an independent army, navy, air-force, equipment, manpower, or technology baseline.
- Force profile `industrial_security`, p48, and tradition 54 are present in the shared mapping tables, but the archetype mismatch remains an admission gate. Current setup loads the package mapping only after the generation and readiness guards.
- No UDM-specific technology or doctrine dependency is declared. The installed package exposes no Technology Tree Viewer, so that route remains an unresolved tooling limitation even though no UDM tech surface is claimed.
- State 399’s vanilla rural/infrastructure/resource baseline is preserved. Factory/rail and strategic project effects use guarded package costs and one-civilian-factory project patterns; no map or production fallback was added.

## AI and playability

- AI strategy ids and route gates are present for industrial survival, unsettled-host restraint, settled compact, and emergency guard. The package uses explicit UDM package/setup/profile checks and does not introduce a world-iterating on-action.
- `hoi4.probability_inspect` on `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt` returned `PROBABILITY_SOURCE_DISCOVERED`, source hash `f7e270283f6c78fceb8a5cd3ee80f6ede68ca9506f919603e36a92cf8fae1b49`, reason `no_weighted_surfaces`, and zero candidates. The useful artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6ffe3ff4ccfb050702c3cfcaa9516fcb6467917439466b5f2f1cbf625535fae6/60cfe010b1cf4fc3b80dc0f3906a396fdbfe78b0db554c777ed698354b77ac87/probability-inspect-f7e270283f6c.json`.
- `hoi4.probability_inspect` on `common/decisions/006_independence_wave_siberian_decisions.txt` returned source hash `2707b23d58232a2a68ff23b2425f6f279a0b250ceedfbc3e8e9965a7696488a0`, `candidates=88`, `availableCandidates=0`, `requiredInputs=16`, and `unresolved=0`; the useful artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/a86a748e3317cb06403d0524015db0f4304654eb26e9cc5d0d4172b719ad01c0/586b53ea288a31f317295a505cc5d30b4423e1ea5d99ca90005a8235b5c599ff/probability-inspect-2707b23d5823.json`.
- The required `chaosx_ai_probability_auditor` route is not exposed in the installed callable tool set, so the HOI4 probability receipts are recorded but are not represented as a subagent compare. No live AI or save behavior was claimed.

## Required MCP receipts and limitations

- Event 006 setup root `chaosx.nr6.350`: `hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL`, revision `744cd12bca3e5b1a25d3d012a4e58a1e2c4e3623c268724b38679e806883d9c9`, graph hash `4b0d98848c436e8f6c8363056e3ae62cfad7785e4b2f1396ac9f1439f91de8df`, and zero blocking diagnostics; global helper/lifecycle projection was deferred. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/8f2558fbfc93fc211872da229fa0c8d64a25b280ef3ef11cbf100f46b72d0b58/73af459f491e0489a3016e9e342b3a29608327ff3a09969f62073473bf63ccb6/event-lint-744cd12bca3e.json`.
- Event render for the same root returned `EVENT_RENDERED_PARTIAL` with zero blocking diagnostics; manifest artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fb57e107c030355f5de7a2d1c6cc6a00dc8f8b815a10b60b722657bf0f38eec/8fa4d6765e2ef9ed9e60b977233aa4737e189ff50e67c1a323911645d4f9665b/event-overview-744cd12bca3e-manifest.json`.
- Shared focus inspection returned `FOCUS_INSPECTED`, revision `29d11dc2fd7a53df0b4063a230676d287429be55ed619523674f0f8fd4560fd8`, tree count 184, and a single unrelated vanilla brace diagnostic plus one shared-tree spacing warning. Focus render returned `FOCUS_RENDERED` with no blocking diagnostics. Inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/140556f4558021bb0eececc06f16c639dc0f1440815fa9f947a577c601d3aa8b/1c2f72b04358fb9c699d13d0939de8135e86f9d20f564861d9b5b825140f281f/focus-inspect.29d11dc2fd7a53df.json`; render HTML: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c1feaf211f63a77908f40b4a78f6d719201405aa881e3d010158d45f407edcd6/a9db3803bbb15f521c8de7b3c9a3b5c65d96ef87dbdac878434f1cb79eaf7b10/independence_wave_focus_tree.focus.html`.
- No `hoi4_country_inspect` route is exposed in the installed HOI4 MCP tool set, so country inspection used direct Chaos Redux and vanilla source evidence and is not represented as MCP country validation.
- The installed MCP package exposes no Technology Tree Viewer. UDM has no package technology dependency, but the missing viewer remains an unresolved tooling limitation.
- No live game, save-load, RunPod, or map write was performed or claimed.

## Conclusion and owner queue

UDM remains blocked and must not be added to central adapter, attestation, preflight, dispatcher, capacity, or Join lists in this tranche. The immediate owner action is identity/portrait-rights clearance for `UDM_boris`; after that, the owner must resolve the `industrial_security` force-profile versus `industrial_breakaway` archetype contract, prove state 399 host retention in the required scenarios, complete typed probability fixtures and same-scenario comparison, and only then prepare a parent-reviewed central admission patch. No source defect was unequivocal enough to justify a package-local gameplay patch, and no simplification or fallback was made.
