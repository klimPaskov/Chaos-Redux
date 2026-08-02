# Fallout Exact Province Sweep: Engine-Native and Runtime Verdict

Status: documentation-only handoff. No gameplay files, scenario registry entries, or SCN-014 wiring were changed.

## Scope read

- Parent task: determine whether the manual Fallout scenario can be proven, without running HOI4, to thermonuclear-strike every valid land province, complete the batch, wait exactly seven days, and then enter the standard blackout/rewrite.
- Explicit constraints: one native strike per valid province; no one-strike-per-state substitute, province modifiers, or variable-only fallout; no HOI4 run; report blockers where exact engine-native enumeration or runtime acceptance is not proven.
- Skills and references read: `AGENTS.md`, `chaos-redux-events`, `chaos-redux-subagents`, required offline Paradox wiki references, installed official documentation, and vanilla nuclear/on-action precedents.

## Primary findings

### Native launch syntax: PROVEN statically

Official `effects_documentation.md` lines 4745-4758 document `launch_nuke` in COUNTRY scope with `province`, `use_nuke`, and `nuke_type` (including `thermonuclear_bomb`). Vanilla `common/raids/nuclear_raids.txt` lines 797-801 and 833-837 pass a variable-backed province to that effect with `use_nuke = no` and `nuke_type = thermonuclear_bomb`.

The generated Chaos Redux substrate uses that same native call. `common/scripted_effects/fallout_consolidated_effects.txt` lines 4-8 pin the installed-map and ledger hashes and require regeneration after map changes; lines 12-25 show the first batch's numeric ranges and native launch. The generated file contains 41 batches: 0-39 contain 250 IDs each and 40 contains 154. The independent proof records 10,154 unique assigned land IDs and one native call per ID.

### Engine-native enumeration: BLOCKED

The official surface does not expose a global `every_province`/`all_valid_land_provinces` enumerator. `for_loop_effect` (official `effects_documentation.md` lines 4312-4328) iterates numeric values into a temporary variable; it does not discover valid map membership. Offline Scopes line 504 documents a maximum of 1000 loop iterations before automatic stopping. Official script collections show `game:all_states` (`script_concept_documentation.md` lines 100-108), while official dynamic arrays expose `province_controllers^ID` and `states` (`dynamic_variables_documentation.md` lines 1042-1046). Offline Data structures lines 1261-1272 list states and indexed province controllers, but no enumerable all-province collection.

The documented `all_provinces` syntax (`effects_documentation.md` lines 1934-1944) is a province selector inside a state-scoped modifier effect. It cannot be supplied to `launch_nuke` and does not prove a global valid-land enumeration. Therefore, the current ledger is a version-pinned, offline expansion of `map/definition.csv` plus state history, not an engine-native enumeration. It proves coverage for the pinned installed map only and must be regenerated after map/state changes.

### Batch completion and seven-day handoff: source contract PROVEN, runtime completion BLOCKED

`common/scripted_effects/fallout_consolidated_effects.txt` validates generation, cursor, expected batch size, issued-strike deltas, and callback observations. The completion verifier requires issued = observed = 10,154, 1,081 unique struck states, and a state strike sum of 10,154 before countdown. `fallout_manual_begin_countdown` stores the start day, adds the seven-day constant, and schedules `chaosx.fallout.903 days = @FALLOUT_MANUAL_COUNTDOWN_DAYS`.

Official `country_event` documentation supports an exact `days = 7` delay. `docs/plans/air_cleanliness_fallout_plans/ENGINE_SURFACE_PROOF.md` lines 58-64 correctly limits that proof to a surviving event owner. Source-level barriers are therefore structurally present, but runtime callback delivery and native acceptance are unobserved.

## Scope transitions

1. Coordinator COUNTRY initializes the ledger and schedules one hidden batch event.
2. Batch COUNTRY enters a guarded launch window and executes its generated numeric ranges; each `launch_nuke` targets a province ID.
3. `on_nuke_drop` runs with launcher COUNTRY as ROOT and struck STATE as FROM. `common/on_actions/chaosx_on_actions_chaos_meter.txt` lines 172-186 routes the Fallout observer first.
4. Observer records native callback counts and unique struck states; state aftermath is applied only after observation, not as a strike substitute.
5. Verifier gates aggregate consequences and the hidden seven-day callback; `.903` submits the standard request only when the countdown receipt is valid.

## Runtime and release-safety blockers

Static documentation cannot prove that every one of the 10,154 calls is accepted in the live engine, especially the 126 assigned land IDs in `impassable = yes` states. It also cannot prove that `use_nuke = no` emits exactly one `on_nuke_drop` callback per call, that callback scopes remain synchronized, or that native results are distinct for every province.

The vanilla `common/on_actions/00_on_actions.txt` `on_nuke_drop` branch schedules twelve one-day news events per nuke. If every generated call reaches that branch, the current batch would schedule roughly 121,848 one-day news-event attempts. Frame-time, save, and multiplayer bounds for 250 calls per batch are not proven without a runtime run. These concerns are separate from the missing engine-native enumerator and must not be conflated with static ledger coverage.

The public Triggerable Scenario registry still has no Fallout row. `common/script_constants/fallout_consolidated_constants.txt` reserves ID 14 after live maximum 13, but the registry/dispatch intentionally omit SCN-014 while proof and runtime gates remain unresolved.

## Recommended parent action

Keep the overall claim **BLOCKED** for the user's exact requirement. Report the narrower items as **PROVEN statically**: native thermonuclear province-call syntax, pinned-map ledger expansion, unique-ID/batch arithmetic, source-level observation barriers, and the exact seven-day event schedule. Report as **BLOCKED**: an engine-native all-valid-province enumerator and runtime acceptance/release safety. Do not register or expose SCN-014 until those blockers are resolved.

## Validation evidence

- `docs/plans/air_cleanliness_fallout_plans/FALLOUT_MANUAL_PROVINCE_SWEEP_PROOF.md` records the canonical ID, map, batch, and runtime-gate hashes and the 10,154/1,081 verifier contract.
- The exact-sweep and seven-day-delay sections of `docs/plans/air_cleanliness_fallout_plans/ENGINE_SURFACE_PROOF.md` separate native-call/static-map proof from runtime acceptance, record the missing province enumerator, and preserve the owner-survival limitation.
- No HOI4 executable or MCP viewer was run for this handoff.
