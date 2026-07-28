# Event 006 IW-012 Iceland adapter re-audit

## Scope and verdict

This re-audit covers the installed-map Event 006 candidate `IW-012`, resolved tag `ICE`, reservation group `RG-100`, and fixed anchor state `100`.

Verdict: **HOLD and fail closed.** The repository has a loader, automatic weight row, reservation publisher, and scenario ranking entry, but it has no executable ICE package adapter, content attestation, setup/final-validation/cleanup implementation, or capacity witness. A named fail-closed readiness trigger now exists, but it does not admit ICE or change allocation behavior. No partial adapter or content attestation was added because country setup safety remains unproven.

The safe target remains an additive non-focus overlay. A returned ICE must retain vanilla `iceland_tree`, `ICE_personal_union`, DLC-aware history, vanilla characters, vanilla flags, and dedicated AI plans. Do not add a country tag, duplicate history, copied focus tree, generated portrait, replacement flag, or static Event 006 OOB.

The earlier full audit remains useful background at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw012_ice_package_audit_2026_07_26.md`. This re-audit records the current executable surfaces and the exact admission gaps found on 2026-07-28.

## Country package coverage checklist

| Surface | Status | Evidence and finding |
|---|---|---|
| Tag and identity | Vanilla pass, Event 006 hold | `common/countries/Iceland.txt` and `history/countries/ICE - Iceland.txt` define the existing ICE identity. `common/script_constants/006_independence_wave_country_registry_constants.txt` registers ICE as a carrier tag, but no exact IW-012 runtime identity adapter exists. |
| Map binding and reservation | Valid binding, runtime hold | `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` binds IW-012 to state `100`, ICE, and RG-100. `docs/plans/006_independence_wave_plans/package_bindings/006_current_map_reservation_groups.csv` makes RG-100 unique, but the host-remnant proof is not implemented in executable code. |
| Region loader | Present shell | `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:159-172` publishes package `constant:independence_wave_package_id.iw_012`, RG-100, region `northern_western_europe`, and ICE/state 100 event targets. |
| Candidate and weight row | Stale and blocked | `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt:107-114` calls the generic `is_independence_wave_candidate_tag_available` gate. That gate requires `independence_wave_package_content_ready`, which no ICE history or adapter grants. The same row therefore cannot prove an audited package. |
| Runtime automatic readiness | Defined fail-closed; package still missing | `is_independence_wave_runtime_automatic_package_iw_012_ready` is defined as `always = no` in `common/scripted_triggers/006_independence_wave_triggers.txt`; the named witness remains closed until the additive ICE adapter, full setup/final-validation/cleanup, force materialization, host-survival proof, and exact content attestation exist. |
| Reservation publisher | Present shell, safety incomplete | `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt:324-331` reserves state 100 through the generic planner. It does not prove that the living host keeps a capital or a valid remnant when state 100 is transferred. |
| Host survival | Blocking map issue | Vanilla state 100 is ICE's capital, sole state, and sole core. A standard 1936 ICE therefore must remain ineligible, and a later release must reject any transaction that erases a living host or consumes its protected capital. Generic anchor availability is not this witness. |
| Politics and laws | Vanilla only | `history/countries/ICE - Iceland.txt` supplies democratic 96/2/2 popularity, 0.65 stability, DLC-conditional ideas/laws, `ICE_personal_union`, technologies, and economy variables. No Event 006 ICE politics or cleanup layer exists. |
| Leaders, characters, and advisors | Vanilla roster only | `common/characters/ICE.txt` and the dated/AAT branches in `history/countries/ICE - Iceland.txt` provide real leaders, advisors, service chiefs, and commander roles. No adapter selects a date/DLC-safe consumer without duplicate recruitment, and no new portrait or advisor icon is authorized. |
| Portrait and name policy | No Event 006 package | Vanilla ICE portraits and names are available. No IW-012 portrait manifest, institutional consumer, or source attestation exists. Any future alternate leader must be sourced and gender-matched, while an institutional body must use an institutional name rather than a random personal pool. |
| Flags and cosmetic identity | Preserve | Vanilla `ICE.tga` and ideology variants are present. `ICE_personal_union` must remain intact. No Event 006 flag variant or flag manifest exists. |
| Focus tree | Preserve | `common/national_focus/iceland.txt` loads `iceland_tree` with meaningful Iceland and Nordic content. No Event 006 focus root is wired into that tree. A future adapter must use the shared non-focus mechanics path unless a separate static focus design is approved. |
| Decisions and missions | Shared framework only | `common/decisions/006_independence_wave_decisions.txt` is gated by active Event 006 origin state, but no ICE-specific visibility, route action, mission, or cleanup file exists. |
| Ideas and lifecycle | Vanilla only | Vanilla ICE ideas, including `ICE_the_icelandic_economy_modifier` when supported, have no IW-012 install/remove contract, icon, or localisation. |
| Formables and leagues | Collision unresolved | Event 006 FORM-02 already recognizes ICE/state 100 in `common/scripted_triggers/006_independence_wave_form01_02_04_triggers.txt` and transfers the anchor in `common/scripted_effects/006_independence_wave_form01_02_04_effects.txt:255`. Vanilla `form_nordic_league` also accepts ICE and cores state 100. No adapter precedence or cleanup policy prevents duplicate transfer, coring, or stale invitations. |
| Military setup | Mapping exists, materializer missing | `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` specifies coastal guards, patrol craft, foreign volunteers, navy inheritance, no air inheritance, and military tradition 45 for IW-012. `history/units/ICE_1936.txt` has the Ríkislögreglan template and production but no fielded division, so setup must materialize a playable force through the generic runtime effects. |
| Technology, industry, supply, production | Vanilla baseline only | ICE has two research slots, 30 convoys, vanilla infantry/support/recon and DLC-conditioned air/naval technology, one naval base/dockyard, and one industrial complex in state 100. No ICE adapter proves equipment, manpower, convoy, fuel, supply, or reinforcement behavior for the release force. |
| AI and playability | Vanilla AI only | `common/ai_strategy/ICE.txt` and the historical/alternate ICE strategy plans are dedicated and must be preserved. No origin-aware Event 006 weights, one-state survival plan, convoy/port priorities, or formable collision behavior exists. |
| Localisation and assets | Missing package surfaces | Vanilla ICE localisation and assets exist. No `independence_wave_ice_*` keys, decision/focus/idea icons, report art, portrait manifest, or package asset manifest exists. |
| Runtime dispatch | Missing | `common/scripted_effects/006_independence_wave_package_dispatch_effects.txt:13-52` dispatches other package families only. It has no IW-012 setup, final-validation, or cleanup call. |
| Runtime admission | Missing | `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt:10-159` omits IW-012 from adapter, content-attestation, and exact package/tag preflight lists. Scenario preflight at `:168-247` also omits it. |
| Automatic capacity | Missing | `common/scripted_triggers/006_independence_wave_triggers.txt` has no IW-012 capacity try/witness after the existing region-01 entries. A capacity row must follow the exact runtime preflight and RG-100 host-survival proof. |
| Scenario registry | Ranking only | `common/scripted_effects/006_independence_wave_scenario_effects.txt` ranks IW-012, but scenario dispatch cannot execute it without the central attestation and exact-tag preflight branches. |

## File surface checklist

### Existing authoritative surfaces

- `common/countries/Iceland.txt` provides vanilla graphical identity and colour.
- `history/countries/ICE - Iceland.txt` owns the vanilla capital, OOB, slots, convoys, ideas, technology, DLC branches, economy variables, politics, and dated character recruitment.
- `history/states/100-Iceland.txt` owns the sole ICE state/core, capital, port, dockyard, and industrial complex.
- `history/units/ICE_1936.txt` provides the vanilla Ríkislögreglan template and production lines without a fielded division.
- `common/characters/ICE.txt` provides the AAT character roster, advisors, service chiefs, and commander.
- `common/national_focus/iceland.txt` provides `iceland_tree` and Nordic shared content.
- `common/ai_strategy/ICE.txt`, `common/ai_strategy_plans/ICE_historical_strategy_plan.txt`, and `common/ai_strategy_plans/ICE_alternate_strategy_plan.txt` provide dedicated ICE AI behavior.
- `common/scripted_effects/006_independence_wave_packages_region_01_effects.txt` provides the IW-012 loader, weight row, automatic list entry, and reservation publisher.
- `docs/plans/006_independence_wave_plans/006_force_package_mapping.csv` provides the existing generic coastal-maritime force mapping.
- `docs/plans/006_independence_wave_plans/package_bindings/006_current_installed_map_package_bindings.csv` and `006_current_map_reservation_groups.csv` provide the current-map identity, anchor, and RG-100 policy.

### Missing or stale surfaces

- A named ICE/region-01 package setup effect and trigger file are missing.
- `is_independence_wave_runtime_automatic_package_iw_012_ready` is defined fail-closed at `common/scripted_triggers/006_independence_wave_triggers.txt`; it is not a readiness pass.
- An exact IW-012/ICE identity wrapper that calls `is_independence_wave_runtime_package_preflight_ready` is missing.
- The IW-012 planner row still calls the stale generic content-ready gate instead of a package-specific runtime readiness witness.
- `has_independence_wave_runtime_package_adapter_for_execution_id` lacks `constant:independence_wave_package_id.iw_012`.
- `has_independence_wave_runtime_package_content_attestation_for_execution_id` lacks the same exact package ID.
- `is_independence_wave_runtime_package_preflight_ready` lacks the `iw_012` plus `original_tag = ICE` branch.
- `is_independence_wave_scenario_package_preflight_ready` lacks an IW-012 exact-tag branch.
- `independence_wave_dispatch_package_setup`, `independence_wave_dispatch_package_final_validation`, and `independence_wave_dispatch_package_cleanup` lack ICE calls.
- Automatic capacity has no IW-012 try/witness and no selected RG-100 proof.
- ICE-specific politics, ideas, decisions, missions, localisation, assets, AI weights, formable policy, force materialization, and cleanup are absent.
- No package-level content attestation should be added until every missing surface passes static review.

## Map and state setup issues

State `100` is the ICE capital, sole owner, and sole core in `history/states/100-Iceland.txt`. It contains province 12674 with a naval base, dockyard, and industrial complex. The standard living ICE host therefore fails the candidate contract by design.

The current anchor check at `common/scripted_triggers/006_independence_wave_packages_region_01_triggers.txt:113` proves only generic state availability. A future IW-012 readiness witness must additionally prove that the former host remains valid with a capital/remnant, or reject before reservation and release. It must also reject a protected-capital conflict and prove RG-100 is disjoint from every other selected package.

No state-history or map rewrite is needed for the current IDs. Any future map change requires the parent-owned dry-run, review, apply, post-validation, and rollback/recovery evidence sequence.

## Politics, leader, portrait, flag, advisor, and party issues

Preserve the vanilla ICE democratic setup, party names, DLC branches, `ICE_personal_union`, flags, and real character roster. Do not duplicate the ICE country definition or dated history.

The AAT and non-AAT branches expose different character availability. A future setup effect must choose a valid existing leader, commander, advisor, and service-chief consumer for the release date and DLC state, or use an authenticated institutional provisional authority. It must not recruit duplicates or pair a generated/female-presenting portrait with a male pool, or vice versa. No such consumer selection is currently implemented.

FORM-02 North Atlantic Compact and vanilla `form_nordic_league` both recognize ICE/state 100. A future package must define precedence, invitation cleanup, transfer ownership, and coring behavior before either route is marked playable.

## Focus, decision, idea, and asset issues

Keep `iceland_tree` loaded and preserve its Nordic shared focus behavior. The existing tree does not contain an Event 006 overlay root, and no safe static focus edit is in this task. The Event 006 adapter should therefore expose additive mechanics through decisions and scripted ledgers only after the active-origin and package setup flags are proven.

The shared Event 006 decision layer is not enough to claim ICE content readiness. Every ICE-visible action needs a trigger tooltip, effect description, localisation, lifecycle cleanup, and a one-state playability check. No ICE-specific decision, mission, idea, icon, report image, portrait manifest, or flag manifest currently exists.

## Starting military, technology, industry, supply, and production issues

The existing `coastal_maritime` mapping and IW-012 row are design inputs, not runtime proof. The adapter must materialize the opening coastal guard, patrol craft, and volunteer force, assign equipment and manpower safely, preserve the vanilla technology and production baseline, and provide a conditional reinforcement and supply path. It must not copy `ICE_1936` history or add a static Event 006 OOB.

Because state 100 is a one-state port island, convoy, naval-base, fuel, and supply assumptions must be checked against the actual force setup and AI plan. The vanilla OOB's lack of a fielded division is a blocking setup gap.

## AI and playability issues

Preserve `ICE_avoid_joining_baddies`, the historical plan, and alternate plans. Add only origin-aware weights after package flags and route decisions exist. The AI proof must cover capital/port survival, convoy security, volunteer access, host pressure, and interaction with both North Atlantic Compact and Nordic League formables.

The standard living ICE must remain ineligible. A returned ICE must retain `iceland_tree`, vanilla identity, date/DLC-safe character consumers, and dedicated AI while gaining only the audited additive Event 006 mechanics. No runtime playability claim is possible today.

## Required parent implementation order

1. Author the ICE setup, runtime readiness, final-validation, and cleanup blocks without touching vanilla history, focus loading, characters, flags, or AI identity.
2. Prove exact package ID `12`, `original_tag = ICE`, anchor state `100`, dormant-tag safety, Soviet/Event 006 origin exclusions, and host-remnant/protected-capital safety through the shared preflight contract.
3. Implement force materialization, date/DLC-safe existing character consumers, politics, ideas, additive decisions, AI weights, formable precedence, localisation, and assets with cleanup for every package-owned side effect.
4. Run country-package, focus-tree, decision, localisation, and asset audits before central admission.
5. Perform a dry-run and review of RG-100 reservation, host survival, capacity witness, transaction rollback, and final commit before applying central registry changes.
6. Add IW-012 only then to adapter, content-attestation, exact-tag preflight, scenario preflight, capacity, and setup/final-validation/cleanup dispatch registries.
7. Post-validate every changed script and document rollback/recovery evidence. Runtime and live save testing remain parent-owned and must not be inferred from static source inspection.

## Validation performed

- Read `AGENTS.md`, `.agents/skills/chaos-redux-subagents/SKILL.md`, and `.agents/skills/chaos-redux-events/SKILL.md` before auditing.
- Consulted the required offline Paradox wiki pages and relevant vanilla HOI4 documentation for country history, state ownership, triggers, effects, focus trees, decisions, ideas, AI, event targets, release behavior, and focus loading.
- Inspected vanilla `ICE` country, history, state, OOB, focus tree, character, AI, flag, and formable sources.
- Ran targeted repository searches for IW-012/ICE loaders, readiness witnesses, dispatch hooks, capacity, force mapping, focus loading, decisions, ideas, localisation, portraits, flags, and manifests.
- Confirmed that no Chaos Redux country, state, focus, decision, event, AI, localisation, asset, or runtime script was changed by this audit.
- No in-game execution, save/load, live reservation, map write, or runtime MCP render was performed. Those checks are required before admission and remain parent-owned.

## Changed files

- Added `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw012_ice_adapter_audit_2026_07_28.md`.
- No gameplay file, vanilla country file, state file, focus tree, decision, event, AI, localisation, asset, or registry was patched.

## Simplifications, omissions, and blockers

- No fallback country, copied focus tree, invented leader, generated portrait, replacement flag, static OOB, or package-admission shortcut was added. The named IW-012 witness is intentionally `always = no` until the audited adapter exists.
- IW-012 remains incomplete and must not be described as automatically selectable, scenario-playable, or runtime-ready.
- The fail-closed runtime witness does not remove the stale candidate gate, absent adapter/content attestation, absent dispatch, absent capacity witness, absent host-survival proof, absent force materialization, absent formable collision policy, absent cleanup, or absent package content surfaces; these remain concrete blockers.
- The installed MCP set exposes no Technology Tree Viewer. No technology-tree runtime claim was made, and the vanilla technology baseline remains an unresolved parent validation item.
- No Git commit was created because this is a handoff-only audit in a shared dirty worktree. The parent owns review and any later gameplay commit.
