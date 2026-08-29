# Event 006 runtime absent-carrier completion handoff

Date: 2026-08-29 (Europe/Kyiv).

Owner: `chaosx_scripted_system_architect`.

Parent: `/root` (`006 Independence Wave`).

## Scope and disposition

This tranche audited the Event 006 planner, execution, dispatch, package setup, roster, and capital-check paths against the accepted release diagrams, the no-country failure context, the offline Paradox wiki, and the installed vanilla documentation.

No gameplay source file needed an additional change in this checkout. The source-correct repairs are already present at HEAD `3dbf918b5` (`docs(event006): reconcile eleven portrait consumers`), with the relevant runtime behavior supplied by `caccec722` (absent-country release scope), `182ed53cf` (scope-stack release target), `5edb09471` (absent-carrier roster checkpoint), and `6ed043966` (dormant-carrier capital safety). This handoff is the only file authored by this tranche.

The decision to leave the runtime source unchanged is deliberate. Replacing the current accepted core-masking or target-array sequence without a callable engine inspection would be a speculative semantic rewrite and could break the frozen-plan sovereignty contract. The existing source already matches the available vanilla release precedent and the maintained static audits.

## Runtime identifiers and evidence

`independence_wave_validate_execution_metadata` in `common/scripted_effects/006_independence_wave_execution_effects.txt` loads the aligned country, anchor, and former-host arrays into `independence_wave_execution_country`, `independence_wave_execution_anchor`, and `independence_wave_execution_former_host`, then requires the dormant-country, reservation, exact package, adapter, force-probe, anchor-owner, and surviving-host proofs before setting `independence_wave_execution_metadata_valid`.

`independence_wave_instantiate_frozen_countries` iterates the locked selected rows and calls `independence_wave_release_one_frozen_country` for each row. Existing empty Event 006 shells do not receive a no-op `release`; their planned states are transferred by the following sovereignty pass.

`independence_wave_release_one_frozen_country` keeps the absent-tag branch in the valid vanilla shape: `every_possible_country` is limited to `exists = no` and `tag = event_target:independence_wave_execution_country`, then the saved former-host country runs `release = PREV`. A subject candidate is detached with `set_autonomy = { target = PREV autonomy_state = autonomy_free }`. The former invalid direct event-target release shape is absent.

`is_independence_wave_dormant_country_scope` in `common/scripted_triggers/006_independence_wave_package_triggers.txt` accepts either an absent tag or an existing empty shell with zero owned states, no controlled states, and no Event 006 origin flags. Living carriers remain fail-closed.

`is_independence_wave_runtime_package_preflight_ready` in `common/scripted_triggers/006_independence_wave_package_dispatch_triggers.txt` retains exact package/tag identity checks, runtime adapter and content attestation gates, origin separation, and the dormant-carrier proof. Its absent-tag identities use the explicit `OR = { original_tag = TAG exists = no }` form rather than evaluating a non-existent country as a live carrier.

`chaosx.nr6.10` is the hidden, trigger-only, idempotent runtime roster checkpoint already present in `events/006_independence_wave.txt`. The five package setup callers are:

- `independence_wave_setup_iw_001_scotland` and `independence_wave_setup_iw_002_wales` after `independence_wave_prepare_sco_institutional_roster` and `independence_wave_prepare_wls_institutional_roster`.
- `independence_wave_setup_iw_004_brittany` after `independence_wave_prepare_bri_roster_and_portraits`.
- `independence_wave_setup_iw_008_rhineland` and `independence_wave_setup_iw_009_bavaria` after their guarded RHI/BAY roster preparation effects.

The checkpoint recruits only the package-approved fixed characters when absent and uses `has_character` guards, so it does not add a generic recruitment fallback or alter pre-event visibility. Other admitted packages retain their package-specific vanilla-roster checkpoint or explicit fail-closed readiness gate.

`has_independence_wave_current_capital_controlled_by_root` in `common/scripted_triggers/006_independence_wave_triggers.txt` uses `any_owned_state = { is_capital = yes is_controlled_by = ROOT }`. `can_independence_wave_enter_provisional_phase` calls that helper, preventing a dormant empty shell from dereferencing an invalid `capital_scope` while preserving the live-country capital-control requirement.

## Capital-scope audit

No `capital_scope` call remains in the Event 006 execution, planner, package-dispatch, or consolidated Balkan release paths. The previously reported split Balkan source paths are not present in this checkout; the consolidated package uses fixed numeric anchor-state proofs for its dormant carriers.

The remaining Event 006 `capital_scope` calls are retained because their owning contexts are live-country checks or explicitly filter `exists = yes` before evaluating the capital: compatibility contracts, scenario patron/war target selection, achievement and focus completion, active IW-043/IW-058 actions, Karelia/Crimea and Pacific action cancellation, and the FORM-39/FORM-48 active member contracts. The event `.302` AI modifier at `events/006_independence_wave.txt:479` is also preserved as a valid live event-scope check. No dormant-carrier path was proven to reach those checks in this audit, so broad removal would be incorrect.

## Scope boundaries preserved

This tranche added no decisions, localisation, assets, portraits, spreadsheets, history rows, categories, pressure, missions, queues, fallback package content, or pre-event UI. No new scripted helper, flag, variable, event target, or package admission was introduced.

## Focused validation

The following maintained static checks passed in the shared checkout:

- `python .tools/audit_event6_allocator.py --strict` — 149 publishers, 126 automatic/high-chaos candidates, 138 SCN-ranked candidates, 40 adapters, 32 attestations, 29 reservation groups, exact `3/4/5/7/10` ladder, protected former-host states, and retired pre-event surface.
- `python .tools/audit_event6_country_api.py --strict` — 242 broad tags, 191 resolved carriers, zero missing, zero duplicates, and IW-031 crosswalk pass.
- `python .tools/audit_event6_flags.py --strict` — 102 registered Event 006 tags and 102 complete flag families.
- `python .tools/audit_event6_form16.py --strict` — FORM-16 ARM/GEO/AZR member, consent, mutation, rollback, cleanup, and readiness contract.
- `python .tools/audit_event6_scenario_matrix.py --strict` — all SCN-008 mode/intensity cells and eight edge cases.

These are source/static checks only. They do not prove a live release, event-target resolution after `release`, character recruitment in the running engine, or save/load behavior.

The required `hoi4.event_inspect`, `hoi4.event_render`, and `hoi4.event_compare` routes were not callable in this runtime; tool discovery exposed no `hoi4_agent_tools` event methods. Earlier dated handoffs record timeout and `ARTIFACT_MANIFEST_INTEGRITY_FAILED` attempts, but no current engine evidence is claimed here.

## Unresolved limits and follow-up

Event 006 remains HOLD / PARTIAL for the broader accepted package boundary. The absence repair is source-strong for the admitted set, not a whole-event or live-engine completion claim.

The explicit `.10` roster checkpoint covers the five absent carriers whose package setup requires those fixed character definitions. No blanket roster fallback is authorized. If a future admitted package demonstrates a missing history roster, its owner must add a package-specific, idempotent checkpoint and attestation rather than widening this event or bypassing the package gate.

The execution helper still references `event_target:independence_wave_execution_country` around core masking, planned-core insertion, restoration, and the post-release existence receipt. Those operations are part of the accepted frozen-plan design and have no available engine inspection evidence in this runtime. If a live error proves that an absent-country event target fails in one of those non-capital operations, the next patch should isolate that exact operation and preserve the current `every_possible_country` release shape.

If a later engine trace proves that one of the retained active package capital checks is reached by a dormant shell, guard that local predicate with an explicit live-country/package condition and add a focused regression audit. Do not remove valid post-formation capital checks globally.

No simplification or fallback was introduced by this tranche.
