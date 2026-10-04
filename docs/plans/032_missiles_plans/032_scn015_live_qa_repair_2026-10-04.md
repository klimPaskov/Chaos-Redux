# SCN-015 live QA repair — 2026-10-04

Authority: the orchestrator acting for the user supplied fresh 1936 USA, Missile Age, Medium, Global Proliferation live evidence and requested repair, a shared-tree commit, and a retest handoff.
No game was launched and no desktop testing was performed.
The full Event 032 goal remains incomplete and its catalog status remains `To Be Reworked`.

## Disposition of the three reported defects

| Reported failure | Disposition and evidence |
| --- | --- |
| STATE-scoped `exists`, including 35 errors each in scenario capacity and reserve custody | `implemented` source repair: country-only checks are removed from every identified state array, site API, operation roster and target-state helper; state control, capacity and site predicates remain. Country recipient and `CONTROLLER` checks are preserved. Live absence of the errors is not yet observed. |
| Duplicate native ID `1028 4713` | `unresolved`: the reviewed read-only architect handoff proves the technology-activation and instant rocket-site paths but finds no fixed native ID or object-type registry. Missing-tech guards are implemented as content-preserving hardening, not a claimed root-cause fix. Temporary allocation-phase markers are implemented for the next live evidence. |
| Two undefined `missiles_scenario_war_anchor` removals | `implemented` source repair: both transaction boundaries guard the exact clear with `has_event_target`; profiles that never save the anchor no longer attempt to remove it. Live confirmation is pending. |

The review additionally found `has_country_flag = missiles_current_package_upgrade_done` inside a STATE loop.
It is scoped to `ROOT` so the one-upgrade-per-firing receipt remains country-owned.
No operation, evolution, payload, physical building, asset, achievement, scenario profile, or native technology was removed or replaced.
No tuning weight, numeric cost, target score, technology definition, GUI, spreadsheet field, or CSV export was changed by this repair.

## Exact implementation surfaces

- `common/scripted_effects/032_missiles_operations_effects.txt`: scenario capacity, mature site package, custody reset, survey and secondary-site `FROM`, rogue-site recovery, requested site selection, saturation roster, capacity sum, allocation markers, removed-country state settlement, and four missing-tech guards with temporary native-call markers.
- `common/scripted_effects/032_missiles_effects.txt`: country-owned firing upgrade receipt and temporary scenario-only rocket-site construction markers.
- `common/scripted_triggers/032_missiles_operations_triggers.txt`: controlled-state roster witnesses, per-state commitment/allocation validation, project/recovery and secure-site predicates.
- `common/scripted_triggers/032_missiles_triggers.txt`: target-state validity retains native geography and live `CONTROLLER` country validation.
- `common/scripted_effects/032_missiles_scenario_effects.txt`: guarded war-anchor entry/exit cleanup.
- `.tools/test_event32_state_scope.py`: six source-contract regressions for typed STATE arrays/APIs, `FROM`, both cleanup boundaries, stage/missing-tech gates and diagnostic bracketing.
- `.tools/test_event32_ordinary_preparation.py`: the roster witness assertion uses a native state-control predicate instead of the invalid COUNTRY predicate.
- `docs/events/032_missiles/systems/triggerable_scenario.md`: runtime contract and explicit open allocation investigation.
- `docs/plans/032_missiles_plans/subagent_handoffs/032_scn015_duplicate_id_forensics_2026-10-04.md`: reviewed architect evidence, accepted missing-tech hardening recommendation and unresolved allocator attribution.

The architect was spawned as `chaosx_scripted_system_architect` with `fork_context=false`, a complete bounded prompt, and read-only gameplay/Git ownership.
The parent read and reviewed its entire handoff and applied the source repair itself.
Its forensic source hashes describe the inspected checkpoint, not the final patched bytes.
Its missing-tech recommendation is accepted within the user's explicit repair authority; its allocator hypotheses are not promoted into proven findings.

## Meaningful validation

All 40 current source-contract tests passed: state scope 6, ordinary preparation 17, recipient scope 11 and evolution gates 6.
The four original-defect regression methods were also evaluated against pre-repair `HEAD` source; they produced 16 failed subcases and zero parser errors, confirming that the tests distinguish the reported defects from the patched source.
These tests are not engine simulation and do not resolve native object allocation.

The deterministic setup question was checked by the architect's isolated probability auditor.
The two inspected setup sources returned `PROBABILITY_SOURCE_DISCOVERED`, zero adapters/candidates and `no_weighted_surfaces`.
No weight tuning is performed by this patch, and no probability comparison or balance pass is claimed for this QA repair.

The event MCP trace for exact `chaosx.nr32.6` returned `EVENT_INSPECTED_PARTIAL`, helpers 0, revision `f2b8bdff77c9db689497266f8e35cb0795c11751b02e0188f6533efbece85fd5`.
The scope render returned `EVENT_RENDERED_PARTIAL`, selected nodes 0 and omitted nodes 43002 despite source lookup finding the receiver.
This is a selection/coverage gap, not valid closure or engine-scope evidence.
The trace artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c91cf11a36e2377ffbdda88b881f659b7fa298e92500bf0a00859a3e94e04480/207aae59710c5b527cf698271b8018b699f168ec56c5a9b392e809986c9167e0/event-trace-f2b8bdff77c9.json`.
The render manifest is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/03876c091eceb1d187a72be1fe0b4cebfaf9eed9753470333f5625ce86ae3014/4d003905f7af68bb5967ae8b306fb139f98acb890f9aa7026267107948a6fb31/event-scope-f2b8bdff77c9-manifest.json`.
The narrow event comparison using the returned cached revision failed with `EVENT_REVISION_NOT_CACHED`: `Requested event graph revision is not cached or retained as a graph artifact`.
The same exact-event artifact-backed retry failed with `ARTIFACT_NOT_FOUND`: `Artifact provenance manifest is unavailable`.
No before/after graph comparison is claimed.
`hoi4.script_validate` is not exposed by the connected tool list, so no installed-command body validation result is claimed.
Initial selector validation errors were corrected to the live schema `{ kind: "event", eventId: "chaosx.nr32.6" }` before the substantive calls.
No helper-expansion or background-job capability is assumed without health/version and negotiation evidence.

## References actually read

Installed paths below are relative to `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Offline wiki paths are relative to the mod root.

| Source | Read lines | Raw SHA-256/revision | Rule |
| --- | --- | --- | --- |
| `documentation/triggers_documentation.md` | 2708–2716, 3844–3852, 4882–4890, 5381–5389 | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` | `exists` COUNTRY only; target presence any scope; `has_tech` COUNTRY; `is_controlled_by` STATE. Revision-bound MCP reads except the direct `has_tech` section. |
| `documentation/effects_documentation.md` | 2733–2741, 4802–4810, 7805–7819 | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` | Exact global-target clear, any-scope localized log output to `game.log`, and COUNTRY technology grant/popup semantics. Target clear read through MCP; technology and log sections read directly. |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | 634–650, 1838–1849 | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` | Country/general trigger table and separate state ownership/control predicates. Read directly. |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 1937–1952 | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` | Technology activation and suppressed-popup contract. Read directly. |
| `common/scripted_triggers/FRA_scripted_triggers.txt` | 17–33 | `7be15772a641d617bf1421089138b3c7cc23e6c4d6a21fc31d794133ca2ab5d5` | Vanilla STATE control test and explicit `CONTROLLER` country transition. Read directly. |

The existing researched-technology union helper at `common/scripted_effects/chaosx_dynamic_effects.txt:483–527` uses a missing-tech guard before activation and was inspected as the Chaos Redux precedent.
The four mod/native rocket technology bodies were reviewed for building/module/equipment unlocks and completion callbacks; the architect handoff retains their exact spans, hashes and deferred-variant documentation.
The broad context response omitted Modifiers and Scopes; it is not claimed as complete rule coverage.
Required task-specific rules were read through targeted sections and direct source inspection.

## Simplifications, omissions and blockers

No gameplay simplification or excluded content family was introduced.
The duplicate-ID root cause and object class remain missing, so this is not a three-defect resolution or Event 032 completion claim.
The missing-tech guard cannot prove that a legitimate first-time allocation will not collide.
The exact remaining evidence is allocator attribution during the live transaction, followed by confirmation that the native-ID error and reported scope/cleanup errors are absent.
The temporary `MISSILES_SCN015_NATIVE` logs must be removed after resolution.
The MCP graph selection and artifact provenance gaps remain; passing source checks are not a substitute.
No new live result is available at commit time, and a clean `error.log` is not claimed.
No new visual asset or spreadsheet edit is warranted by these unchanged presentation/catalog facts.
Skills used: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-shared-git-commit`; no skill change is needed because the existing country-only trigger and shared-index rules already cover this repair.
