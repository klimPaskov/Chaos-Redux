# Event 006 IW-050 Komi completion tranche

Date: 2026-09-19

Disposition: audited, no source-safe gameplay patch, central admission remains blocked and fail-closed.

Owner: `/root/iw050_kom_completion_tranche`

Next owner: Event 006 parent admission owner.

## Scope and authority

This tranche reviewed the accepted IW-050 Komi package against the accepted package research resolution, the Event 006 country-package specification, the 2026-08-24 and 2026-08-29 improvement addenda, and the previous Komi roster and identity handoffs.

The review also read the required offline Paradox wiki pages, the applicable Chaos Redux event, focus-tree, decision-mission, event-asset, and subagent skills, and the relevant vanilla country, state, character, focus, localisation, and documentation files.

The review preserved the identity-rights gate, the absolute no-pre-event contract, fail-closed setup and cleanup behavior, the existing vanilla `KOM` carrier and roster, the exact Event 006 release ladder `3/4/5/7/10`, and the existing central admission ownership boundary.

## Files changed

Only this handoff file was added:

- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw050_kom_completion_tranche_2026-09-19.md`

No gameplay, localisation, asset, map, central adapter, attestation, preflight, capacity, or Join source file was changed. Nothing was staged or committed. The worktree contains unrelated pre-existing Event 023 and temporary changes that were left untouched.

## Country package coverage checklist

- Tag and history: IW-050 correctly reuses the registered vanilla `KOM` carrier. The vanilla history remains the source of the 1936 starting setup with capital state `397` Syktyvkar and three research slots. No mod duplicate country, tag, history, or character file was added.
- Map and state setup: the accepted anchor remains state `397` with optional extension states `262` and `581`. The local reservation registry still loads and reserves `397`, then tries `262` and `581`. The protected former-host binding remains an event target rather than a speculative host edit. No map write was attempted.
- Politics and package lifecycle: the Komi package-local setup, route flags, baseline laws, project lifecycle, final validation, and cleanup callbacks remain wired through `common/scripted_effects/006_independence_wave_komi_package_effects.txt`. The setup callback still fails closed when the exact package, anchor, former-host, roster, route, or crisis conditions are not met.
- Leader and identity: `has_independence_wave_komi_command_roster` in `common/scripted_triggers/006_independence_wave_komi_package_triggers.txt:94` requires both `independence_wave_iw_050_identity_rights_cleared` and the exact vanilla character `KOM_pavel_murashev`. The same guard is enforced by `independence_wave_komi_checkpoint_vanilla_roster` in `common/scripted_effects/006_independence_wave_komi_package_effects.txt:321`. This preserves the existing roster and prevents an unsubstantiated identity from entering setup.
- Portrait and flag: the current vanilla portrait is only a generic carrier asset and has no accepted exact Pavel Murashev source and rights receipt. The accepted research also has no defensible neutral 1936 Komi flag provenance. No generated portrait, committee substitute, modern flag, later ASSR flag, or speculative emblem was introduced.
- Focus tree: the shared `independence_wave_focus_tree` was inspected and rendered read-only. It contains 184 focuses and 196 connectors with zero crossings or intersections. The only reported warnings are one long connector and one vanilla continuous-focus localisation warning outside the IW-050 package. No focus edit is justified.
- Decisions and mission: the Komi package has one serialized mission, `independence_wave_komi_hold_northern_council`, and ten package projects. The mission remains unavailable until setup activates it, so a direct empty-fixture probability evaluation correctly returned `PROBABILITY_OUTCOME_NEVER_ELIGIBLE`; this is not evidence of a runtime defect and does not justify changing its gate.
- Ideas and localisation: the package retains its seven Komi ideas and package localisation. The project-wide localisation audit found zero parse errors, duplicate keys, missing BOMs, encoding artifacts, or undefined event roots. Its unrelated global counts of 312 undefined key bindings, six missing event title/description pairs, and 22,565 dead keys were not modified.
- AI and playability: the four Komi strategy blocks remain present, but the mandatory named `chaosx_ai_probability_auditor` route is not exposed in this environment. Direct read-only probability inspection found no AI-strategy weighted candidates, so no quantitative weight or balance claim is made and no AI patch is safe.
- Technology: no IW-050-specific technology-tree dependency was found in the accepted package surfaces. The exposed read-only `hoi4_tech_inspect` route timed out after 180 seconds, and no standalone Technology Tree Viewer was present in the tool inventory. Technology validation is therefore recorded as unavailable rather than inferred.

## Central admission audit

Central admission remains blocked. Source inspection confirms that `KOM` and `iw_050` are intentionally absent from the central runtime adapter, content-attestation, exact preflight, and deterministic Join registries.

The relevant central surfaces are:

- `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt`, including `has_independence_wave_runtime_package_adapter_for_execution_id`, `has_independence_wave_runtime_package_content_attestation_for_execution_id`, and `is_independence_wave_runtime_package_preflight_ready`.
- `common/scripted_effects/006_independence_wave_join_effects.txt`, including `independence_wave_join_probe_attested_package` and its fixed attestation order.
- `common/scripted_effects/006_independence_wave_effects.txt`, where IW-050 only has a zero allocation-weight reset and no admission branch.
- `common/scripted_effects/006_independence_wave_scenario_effects.txt`, where IW-050 appears only in the scenario-ranked package array and not as an executable admission registration.

The package-region planner and reservation registry do contain IW-050 load, planning, and state-footprint entries. Those entries do not establish playable admission and must not be promoted without the accepted identity, asset, map, probability, and transaction evidence.

The prior roster checkpoint repair is correct and must remain unchanged. Adding only a central list entry would bypass the unresolved portrait-rights and symbol gates and would violate the accepted fail-closed contract. No partial central adapter, attestation, preflight, dispatch, capacity, or Join patch was applied.

## Read-only MCP evidence

The required read-only event, focus, map, and weighted passes were attempted before reporting this surface.

- `hoi4_event_inspect` on `chaosx.nr6.1` and `chaosx.nr6.350` returned `EVENT_INSPECTED_PARTIAL` with zero blocking diagnostics. The deferred workspace helper and lifecycle projection is an MCP limitation, not a source admission result. Useful artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/dde38e0008418a4e71b039d0bb6d97dd5f63316f5d288bfb034e017d2bb3945d/0ebbce4847fc1f1c061ee219a82f237622bed2a0400c392897c436539b9739d5/event-lint-dec87bc5349e.json`.
- `hoi4_event_render` on `chaosx.nr6.1` returned `EVENT_RENDERED_PARTIAL` with layout hash `3ba5f18a64912a9ece6fe76dde07333dd05321a92381135e629786aae491844d`. The render is read-only and does not clear the package gates.
- `hoi4_focus_inspect` and `hoi4_focus_render` on `common/national_focus/006_independence_wave_focus.txt` and `independence_wave_focus_tree` passed. Useful inspect artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eae1f472587011322690ab116004d3db67bd01cd8c436ed23b90653885eb68a7/202e4b33fe49ea53c91ffcbfce8c114ef46172d272b2585501454e9bb56d34b1/focus-inspect.ad81c1bbd0f22311.json`.
- `hoi4_map_inspect` on states `397`, `262`, and `581` passed the selected state, region-membership, network, and adjacency checks with no unknown province IDs or missing state geometry. Global map validation remains false because the workspace has 1,323 building-position and 1,331 floating-port diagnostics outside this package. Useful artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/1ac0c927a7d41bbeff6fd291c2edbc147e43ff1a3e55911cc111bbc5475d06d1/8049491d9653cd25b4fe8d84f0684ccfe4acaa1d5b1f00c9d12db02456cf962a/map-inspect.efeafc61af55c46e.json`.
- The first weighted pass used `hoi4_probability_inspect` on the Komi AI-strategy source and returned `PROBABILITY_SOURCE_DISCOVERED` with zero candidates and no available adapters. The direct evaluate attempt returned `PROBABILITY_SURFACE_EMPTY`. This is evidence of absent typed adapter coverage, not a balance result.
- The Komi mission source was inspected through the decision and mission adapters. The mission pool reported 88 candidates, 19 required inputs, and no unresolved bindings. The empty-fixture evaluate returned `PROBABILITY_OUTCOME_NEVER_ELIGIBLE` for `independence_wave_komi_hold_northern_council`, as expected before package setup.
- No callable `chaosx_ai_probability_auditor` tool appeared in the tool inventory, so the mandatory auditor route and its compare pass could not be completed. This is recorded as an evidence blocker rather than substituted with a source-only balance claim.
- No standalone Technology Tree Viewer tool appeared in the tool inventory. The exposed `hoi4_tech_inspect` call timed out after 180 seconds. No technology conclusion is promoted from that failed route.

## Validation

Focused repository validators completed without changing source:

- `python -B .tools/audit_event6_country_api.py` passed with no missing or duplicate country carriers.
- `python -B .tools/audit_event6_allocator.py` passed with the exact ladder `3/4/5/7/10`, 40 runtime adapters, 32 content-attested packages, and the expected pre-event crisis retirement and ordering checks.
- `python -B .tools/audit_event6_flags.py --strict` passed with 102 registered Event 006 tags and no incomplete flag families.
- `python -B .tools/audit_localisation_static.py` completed with zero parse errors, duplicate keys, missing BOMs, encoding artifacts, or undefined event roots.

## Blockers and next owner

1. The identity and portrait owner must provide a defensible Pavel Murashev source and rights receipt, or an explicitly accepted institutional identity route, through `chaosx_portrait_creator`. The existing vanilla generic portrait cannot be promoted as an exact identity.
2. The symbol and flag owner must resolve a stable neutral opening identity with provenance and rehash evidence. Modern, later ASSR, or speculative symbols remain rejected.
3. The parent admission owner may add IW-050 to central adapter, attestation, preflight, setup/final/cleanup dispatch, capacity, and Join surfaces only after the identity, visual, map-host, typed-probability, and manual transaction gates are all evidenced in one atomic tranche.
4. The AI owner must rerun the Komi weighted scenarios through `chaosx_ai_probability_auditor` when that named route is available, then perform the required same-scenario compare pass before changing any weight or probability-bearing surface.
5. The MCP technology service and standalone viewer need to become available if technology evidence is required for the final package claim.

## Simplifications, omissions, and risks

No gameplay patch, central admission, portrait, flag, map write, AI weight, or probability claim was made. These omissions are intentional because the accepted package gates remain unresolved and the required named probability and technology evidence routes were unavailable. No speculative fallback was used.

The package remains package-local and not centrally playable. This tranche does not claim complete IW-050 admission.

Skills used: `chaos-redux-subagents`, `chaos-redux-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, and `chaos-redux-event-assets`. No skill was created or changed.
