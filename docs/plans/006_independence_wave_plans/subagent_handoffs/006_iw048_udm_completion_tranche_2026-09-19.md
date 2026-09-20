# IW-048 UDM completion tranche handoff — 2026-09-19

Status: package-local / fail-closed. No source-safe gameplay patch was justified, no central admission surface was opened, and no file outside this handoff was changed by this tranche. The force/archetype wording finding is resolved by the parent-owned crosswalk receipt `006_iw048_udm_force_crosswalk_resolution_2026-09-20.md`; the identity, map/host, typed-probability, and admission gates remain open. The parent agent owns review and commit.

## Scope and authority

The accepted registry row is `IW-048` / Udmurtia / vanilla carrier `UDM` / compact anchor state `399` (Izhevsk) / reservation group `RG-399`, as recorded in `docs/specs/006_independence_wave_specs/matrices/006_candidate_country_registry.csv:49` and `docs/specs/006_independence_wave_specs/research/006_package_research_resolution.csv:49`.

The package-local source and the Event 006 contract were reviewed in `docs/events/006_independence_wave/udmurtia_package.md`, `common/scripted_triggers/006_independence_wave_udm_package_triggers.txt`, `common/scripted_effects/006_independence_wave_udm_package_effects.txt`, the UDM section of `common/decisions/006_independence_wave_siberian_decisions.txt:2328`, `common/decisions/categories/006_independence_wave_categories.txt:673`, the UDM idea section of `common/ideas/006_independence_wave_ideas_registry.txt`, the UDM strategy section of `common/ai_strategy/006_independence_wave_ai_strategy_registry.txt`, `common/national_focus/006_independence_wave_focus.txt`, and `localisation/english/006_independence_wave_udm_l_english.yml`.

The no-pre-event contract remains intact through `common/scripted_triggers/006_independence_wave_triggers.txt:25-52`; UDM package content requires an active Event 006 origin or the bounded adapter receipts and does not publish the player-facing Event 006 surface during the adapter window.

## Coverage checklist

- Tag and identity: `UDM`, `UDM_boris`, vanilla country history, vanilla leader token, vanilla ideology flag ladder, and the parent-owned `independence_wave_iw_048_identity_rights_cleared` gate are wired locally without inventing a leader, portrait, flag, or history replacement.
- State and map: state `399` / Izhevsk is used as the compact anchor and capital in the local setup and readiness predicates; no state, ownership, controller, capital, railway, port, resource, building, or map allocation was written.
- Package lifecycle: `independence_wave_setup_iw_048_udm`, `independence_wave_validate_iw_048_udm`, `independence_wave_cleanup_iw_048_udm`, and their dispatch wrappers are generation-gated and package-local.
- Politics and parties: baseline laws, provisional politics, four route governments, party names, route ideas, and cleanup are present in the package-local effects and localization surfaces.
- Focus integration: the shared Event 006 tree has five UDM helper call sites for workshop council, rail communities, industrial guards, former-host ledgers, and the Volga–Ural corridor; no new focus node or shared-tree layout change was proposed.
- Decisions and mission: the UDM category exposes the 420-day founding mission plus ten serialized projects, with package/force/origin/capital/route locks and local cost/effect text.
- Ideas, AI, and playability: seven UDM ideas and four package AI strategy blocks are present; no AI factor or probability-bearing source was edited.
- Assets and localization: authored UDM decision, mission, idea, party, cost, and effect-tooltip keys are present in `localisation/english/006_independence_wave_udm_l_english.yml`; no portrait, flag, focus icon, idea icon, or manifest was created or replaced.
- Central Event 006 admission: `iw_048` is present in the ranked scenario inventory at `common/scripted_effects/006_independence_wave_scenario_effects.txt:192` and in the package planner at `common/scripted_triggers/006_independence_wave_package_region_triggers_registry.txt:421-428` plus `common/scripted_effects/006_independence_wave_package_region_effects_registry.txt:1060-1070,1213`, but it remains absent from the central adapter/attestation/preflight/normal/SCN-008/Join admission surfaces.

## Why no gameplay patch was safe

1. Identity and portrait rights are unresolved. `UDM_boris` is only a vanilla carrier until the parent-owned `independence_wave_iw_048_identity_rights_cleared` receipt exists, and the accepted research row requires a defensible sourced period leader or institution before admission. Setting the flag, changing the character, or wiring a generated portrait would invent or bypass the accepted identity contract.

2. The force/archetype wording finding is resolved. The accepted force mapping row assigns `industrial_security` and p48, while the planner and shared setup contract independently assign the economic/package archetype `industrial_breakaway`; the separate enums and consumers are documented in `006_iw048_udm_force_crosswalk_resolution_2026-09-20.md`. No source change is required.

3. Map and host-retention proof is incomplete. The planner reserves state `399` and `RG-399`, but the current `hoi4.map_inspect` run returned a global diagnostic truncation with 2,654 omitted building-position/port errors, the targeted follow-up timed out after 180 seconds, and the package still lacks current runtime proof that the former host retains a valid protected state. No map rewrite or reservation change is justified.

4. Central admission is intentionally fail-closed. No UDM entry was added to `common/scripted_effects/006_independence_wave_event021_adapter_registry_effects.txt` or `common/scripted_triggers/006_independence_wave_event021_adapter_registry_triggers.txt`, and no central attestation, preflight, normal, SCN-008, or deterministic Join entry was added. The package documentation explicitly requires identity, map, asset, lifecycle, and typed-probability evidence before those surfaces can change.

5. Typed probability evidence is unavailable for an admission or balance claim. `hoi4.probability_inspect` source discovery on `common/decisions/006_independence_wave_siberian_decisions.txt` found the `mission_ai_will_do` adapter with 88 source candidates and zero inspect-unresolved inputs (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63dfc6cfff32fd0ac5c535177e6f999ade7ad17b168dd7b2b0c66fafe8a79beb/27fef7cf4a1308583fcc8b27687e70bcf26b4cf9b378ee75133761588c96dccc/probability-inspect-9fe87c1b20f9.json`), while the AI-strategy source discovery found no weighted surfaces (`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/29c1829662afa3e1465b87eee7794222c5f75d5fbbae2f0cdc19a1cb0fd6fe20/734ad119c790625fa2decd514629344870037f452a15cd886c1dfb248396ab55/probability-inspect-b84ee2ca17f4.json`). The required `chaosx_ai_probability_auditor` route is not callable in this runtime, so no evaluate, sweep, compare, numeric probability, or AI-balance claim is made and no weighted source was changed.

6. Standalone Technology Tree Viewer availability is a separate package gap. The exposed read-only technology inspect/render routes do not prove a standalone viewer, and no standalone viewer was available in the current evidence; UDM has no technology surface that can be safely invented to close this gap.

## Read-only MCP evidence

- Focus inspection of `independence_wave_focus_tree` over `common/national_focus/006_independence_wave_focus.txt` returned `FOCUS_INSPECTED`, 184 focuses, 196 connectors, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e80d6962600e43baaba3eb1717efa0e2d47f598e4de9a5c23fcb7a945a2b34c1/e34768f24c3048393db4092d7cc367bb0d061556411a3b6701ebb19303df3a16/focus-inspect.9312a71b9076b9b6.json`.
- Focus rendering returned `FOCUS_RENDERED` with artifact set rooted at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/fdebf536d2d08d79fe87e7b92c0cc3c3df83ebd1812cd8aaaf3b82357db60585/98dad1bfc04e0d82b83cd3ad4e4c4945331cf10ab2546fc152fe60c95ec0b3ba/independence_wave_focus_tree.focus.html`; the only reported warnings were one unrelated long connector and one vanilla continuous-focus localization warning.
- Event inspection of `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with no blocking diagnostics but deferred workspace-wide helper/lifecycle projections; trace artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5853140b2015bb53388c9798fc15c02bbc5fec69b98f5b03aac236e0cc0d46bf/33c59b619e0a38713ea3dfca02bb83dc4494ff77178d38dd71586e1563903f3a/event-trace-dec87bc5349e.json`.
- Event rendering returned `EVENT_RENDERED_PARTIAL` with the same deferred workspace-wide limitation and overview artifacts rooted at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/51a29b783f006ca0cc24d9b0419b7cfc2f0acaf9ac39d404c77fe6d2dcf4e529/121dec5c0c9c99101ac75a26e02375aec71574d089a4608757d07489425c534f/event-overview-dec87bc5349e-manifest.json`.
- State/map inspection of state `399` returned `MAP_INSPECTED` and a catalog artifact rooted at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c193b6c5e5234fc0084d9fcddd057102582c4aa913efff3eed8894a0657d118f/04477fd67be2822c5c434ab2ea31abc9a699381a2d164c6a04ee44711793d8df/map-inspect.efeafc61af55c46e.json`; the selected-state count was one, but global position/port validation failed and the targeted query timed out after 180 seconds.
- Map rendering returned `MAP_RENDERED` with `map-state.png` and source-linked JSON/HTML artifacts rooted at `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/93579ebbcf243cf732e420ad841da32dff2c2fc226c1010c08e6977533db9678/1dd88db77fe180d78c0593b1101f0e83e4fbdf17d10ae9dc75e1a9c77a705676/map-state.png`; rendering is read-only and does not prove host retention.

## Focused validation

- `python -B .tools/audit_event6_country_api.py` passed with 242 broad tags, 191 resolved carriers, zero missing, and zero duplicates.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 registered Event 006 tags and 102 complete flag families.
- `python -B .tools/audit_event6_allocator.py` passed with 40 runtime adapters, 32 attested packages, and the documented retired pre-event crisis surface; this is repository-wide allocator evidence, not UDM admission proof.
- `python -B .tools/audit_event6_scenario_matrix.py` passed the SCN-008 32-cell matrix and eight recorded edge cases; this does not admit IW-048.
- The broad static localization audit reported zero parse errors, duplicate keys, missing BOMs, and missing `l_english` headers, but also reported unrelated repository-wide undefined/dead-key counts; no UDM localization repair was made from those global findings.

## Changed files and identifiers

- Changed file: `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw048_udm_completion_tranche_2026-09-19.md`.
- Gameplay files changed: none.
- Tags changed: none; `UDM` remains the registered carrier.
- States, reservation groups, leaders, parties, ideas, focus tree IDs, localization keys, formable IDs, portraits, flags, and AI weights changed: none.
- Map writes, central adapter/attestation/preflight/scenario/Join writes, probability patches, and asset writes: none.

## Exact next owner

The parent Event 006 country-package/admission owner should first close the identity/portrait rights receipt and obtain current state-399/former-host retention evidence. After those are accepted, the central admission owner may prepare the bounded IW-048 adapter, attestation, preflight, scenario, and Join entries and route the complete UDM mission/focus AI surfaces through the callable `chaosx_ai_probability_auditor` with named scenarios and same-scenario comparison. Until then, keep IW-048 package-local and fail-closed.

## Simplifications and omissions

No gameplay simplification, fallback identity, placeholder portrait, flag substitution, map rewrite, probability claim, central admission, or unrelated Event 021/CXT change was made. Live HOI4 execution and save/load validation remain parent/user-owned and were not attempted.
