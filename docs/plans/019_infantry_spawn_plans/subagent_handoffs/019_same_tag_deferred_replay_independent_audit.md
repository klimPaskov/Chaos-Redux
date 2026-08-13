# Event 19 same-tag deferred replay — independent transaction audit

> Current extension note (2026-07-15): this audit covers the original 52-route
> contract. The later Evolution II prototype maintenance mission adds a tenth
> mission route and raises the live map to 53. Root structural validation is
> recorded in the parent audit packet; project-agent specialist and final audit
> coverage for the added route remains pending.

Date: 2026-07-15  
Auditor: `event19_deferred_replay_audit`  
Mode: read-only gameplay audit; this report is the only file written  
Audited state: current shared workspace before the replay owner resumed edits

## Verdict

**Not safe to release in the audited state.** There is no P0 finding, but one reachable P1 replay deadlock remains. The 52 requested routes are all wired and the scenario/compaction isolation is otherwise structurally sound.

- P0: none.
- P1: one class — a deferred incident can change a mission target's status before the stricter mission resumer runs, preventing the original mission completion from performing its unconditional terminal cleanup.
- P2: deferred records have no structural-orphan terminal policy. Missing/invalid identity, a missing original context flag, an invalid enum, or an absent row is retained forever and permanently gates compaction.
- P2: named deferred-choice constants exist, but audited event and dispatcher call sites still use raw numeric route values.

## Required references consulted

Repository guidance and skills:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-decisions-missions/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `019_same_tag_deferred_replay_handoff.md`
- `019_performance_isolation_ai_audit_handoff.md`
- `019_lifetime_ledger_compaction_handoff.md`
- `019_scn013_same_tag_transaction_repair_handoff.md`

Offline wiki pages:

- Data structures
- Triggers
- Effects
- Modifiers
- Localisation
- Scopes
- On actions
- Event modding
- Decision modding
- Idea modding
- AI modding

Vanilla documentation and source precedents:

- `documentation/effects_documentation.md`
- `documentation/triggers_documentation.md`
- `documentation/script_concept_documentation.md`
- `common/script_constants/documentation.md`
- Vanilla activated-mission `timeout_effect`, `activate_mission`, `remove_mission`, and delayed country-event precedents

The HOI4 MCP event/decision inspection tools were not exposed in this agent session. Source, offline-wiki, official-documentation, and vanilla-precedent inspection were used instead. This is a tooling limitation, not a gameplay fallback.

## Findings

### P1 — Incident-first replay can permanently strand a UID mission completion

Current aggregate order is:

1. prefire choice
2. claimant choice
3. incident choice
4. all mission completions

Evidence: `common/scripted_effects/019_infantry_spawn_management_effects.txt:6026-6033`.

Incident-first is the correct relative order, but five mission resumers reject status/family drift before calling their original completion:

| Mission record | Extra replay gate | Resumer evidence |
|---|---|---|
| Audit | family `none`, status `auditing` | `4575-4601`, especially `4585-4593` |
| Standardization | family `none`, status `training` | `4603-4629`, especially `4613-4621` |
| Demobilization | status `demobilizing` | `4631-4656`, especially `4641-4648` |
| Training | family `none`, status `training` | `4658-4684`, especially `4668-4676` |
| Specialist preservation | family `none`, status `demobilizing` | `4716-4742`, especially `4726-4734` |

An incident can legally target the same row:

- `infantry_spawn_select_latest_incident_lot` accepts any ordinary live lot with status below `demobilized`; it does not exclude a mission target (`4794-4816`).
- `infantry_spawn_can_roll_lot_incident` does not exclude any running mission (`common/scripted_triggers/019_infantry_spawn_triggers.txt:184-193`).
- Management availability also does not exclude `infantry_spawn_incident_pending` (`195-202`).
- A failed same-tag rollback can keep the transaction locked across delayed retries (`common/scripted_effects/019_infantry_spawn_scenario_effects.txt:2136-2145`, `2147-2188`), so an already-open event choice and an activated mission timeout can both be deferred.

Nine of the 39 incident choices explicitly replace the lot status:

| Choice | Original effect | Replacement status |
|---:|---|---|
| 1 | `infantry_spawn_incident_barracks_local_authority` | `territorial` |
| 6 | `infantry_spawn_incident_ammunition_delay` | `training` |
| 7 | `infantry_spawn_incident_motor_pool_territorial` | `territorial` |
| 10 | `infantry_spawn_incident_village_territorial_service` | `territorial` |
| 18 | `infantry_spawn_incident_staff_reserve_command` | `territorial` |
| 24 | `infantry_spawn_incident_colors_territorial` | `territorial` |
| 33 | `infantry_spawn_incident_radios_split_command` | `isolated` |
| 34 | `infantry_spawn_incident_cavalry_keep_horses` | `territorial` |
| 37 | `infantry_spawn_incident_armored_cars_recon` | `territorial` |

Concrete failure trace:

1. An audit mission owns lot UID X while its status is `auditing`.
2. An incident is open for the same UID X.
3. A delayed same-tag rollback holds the transaction lock long enough for the audit timeout and the player's incident choice to defer.
4. On unlock, incident choice 1 resolves first and sets X to `territorial` (`5077-5085`).
5. `infantry_spawn_resume_deferred_audit_completion` finds exact UID X but refuses to call the original audit completion because X is no longer `auditing` (`4585-4593`).
6. `infantry_spawn_audit_decision_running` and `infantry_spawn_deferred_audit_completion_pending` both remain set.
7. Compaction permanently refuses to advance on both flags (`common/scripted_triggers/019_infantry_spawn_ledger_triggers.txt:128`, `141`). Every later replay repeats the failed gate without progress.

The same class applies to standardization, training, demobilization, and specialist preservation.

#### Why exact-UID delegation to the original completion is safe

Each original completion resolves its own stored target UID, handles an absent or semantically changed row as failure, and clears its running state and target at function depth one — outside all success/failure branches:

| Original completion | Unconditional terminal cleanup |
|---|---|
| `infantry_spawn_complete_selected_lot_audit` (`414-469`) | running flag `465`; target UID `467` |
| `infantry_spawn_complete_selected_lot_training` (`518-553`) | running flag `550`; target UID `551` |
| `infantry_spawn_complete_selected_lot_standardization` (`605-702`) | running flag `697`; target UID `699` |
| `infantry_spawn_complete_supervised_demobilization` (`3067-3099`) | running flag `3096`; target UID `3097` |
| `infantry_spawn_complete_specialist_preservation` (`3129-3152`) | running flag `3150`; target UID `3151` |
| `infantry_spawn_complete_muster_districts` (`3272-3306`) | running flag `3304`; no row target |
| `infantry_spawn_complete_integration_staff_search` (`3319-3328`) | running flag `3325`; no row target |
| `infantry_spawn_complete_rail_corridor_mission` (`3395-3425`) | running flag `3422`; target state `3423` |
| `infantry_spawn_finish_request_cooldown` (`4441-4445`) | cooldown flag `4442`; duration `4443` |

For the five UID records, restoring the immutable deferred UID into the original target and invoking the original completion is therefore fail-closed and does not select another row.

#### Ordering conclusion

Do **not** move mission replay before incident replay as the primary fix. Demobilization or specialist completion can terminalize the incident lot before the player's exact incident choice executes; the current incident resumer would then retain its record forever, and merely clearing it would discard the selected option.

The minimal safe ordering is the current incident-before-missions order, combined with exact-UID mission delegation without the resumer's duplicate semantic status/family gates.

### P2 — Structural orphan records have no terminal policy

Every resumer except request cooldown has conditions under which the pending flag can never clear. None has an `else` branch that distinguishes a temporary wait from a structurally impossible replay.

| Record family | Temporary condition that should remain pending | Structural poison currently retained forever |
|---|---|---|
| Audit / standardization / demobilization / training / specialist | none after unlock | missing running flag, missing stored UID, absent UID row, or semantic mismatch |
| Muster districts / integration staff | none after unlock | original running flag already absent |
| Rail corridor | none after unlock | missing running flag or stored target state |
| Request cooldown | none | none; it terminates from the pending flag alone |
| Incident | exact choice is temporarily unaffordable | missing original pending flag, missing/invalid enum or UID, original/deferred UID mismatch, absent/terminal row |
| Prefire | none | missing original pending flag or invalid/missing enum |
| Claimant | chosen accept response is temporarily unaffordable | missing original pending flag, invalid/missing enum/UID/demand, absent claimant row, or demand mismatch |

Record creation also sets several pending flags before it proves that required identity exists:

- Mission wrappers set the pending flag, clear the deferred UID/state, and copy it only if the original target exists (`4455-4565`).
- Incident recording sets pending and choice before conditionally copying `infantry_spawn_incident_lot_uid` (`5860-5873`).
- Claimant recording sets pending and choice before validating the selected claimant index and conditionally copying UID/demand (`6002-6017`).

All 12 deferred flags block compaction (`common/scripted_triggers/019_infantry_spawn_ledger_triggers.txt:141-152`). That protection is correct while a record is executable, but without a terminal structural-error path it turns one malformed/stale record into a permanent maintenance lock. `infantry_spawn_country_can_continue_pulse` also does not include deferred flags (`common/scripted_triggers/019_infantry_spawn_triggers.txt:56-69`), so an orphaned prefire record with no other active Event 19 state may not even receive the bounded pulse backstop.

Affordability failure must **not** be treated as structural poison: exact incident and claimant accept choices intentionally wait and retry rather than rerolling or substituting another choice. A remediation needs two explicit states:

- transient wait: preserve record and retry;
- structural invalidity: emit an observable diagnostic/failure state, clear or terminate the matching original context without applying another route, and release the deferred gate under an explicitly approved policy.

Because repository policy forbids silent fallbacks, the structural terminal policy must be accepted explicitly rather than inferred.

### P2 — Named choice constants are defined but not used at audited call sites

`common/script_constants/019_infantry_spawn_constants.txt:46-127` defines:

- `infantry_spawn_deferred_replay_marker`
- all 39 `infantry_spawn_deferred_incident_choice` values
- both `infantry_spawn_deferred_prefire_choice` values
- both `infantry_spawn_deferred_claimant_choice` values

The audited event requests and replay comparisons still use raw `1..39` and `1..2` literals (`events/019_infantry_spawn.txt:41-58`, `153-163`, `220-570`; management effects `5557-5819`, `5894-5903`, `5973-5988`). This is not the cause of the P1, but it leaves the exact transaction routing dependent on duplicated magic numbers despite the available shared constants.

## Exact route coverage proof

### Nine activated-mission timeouts

| Mission | Timeout wrapper | Deferred identity | Replay |
|---|---|---|---|
| Formation roll call (`674-684`) | audit wrapper at `683` | lot UID | `4575-4601` |
| Standardization cycle (`686-696`) | standardization wrapper at `695` | lot UID | `4603-4629` |
| Supervised demobilization (`698-708`) | demobilization wrapper at `707` | lot UID | `4631-4656` |
| Training cycle (`710-720`) | training wrapper at `719` | lot UID | `4658-4684` |
| Muster districts (`722-732`) | muster wrapper at `731` | country-running flag | `4686-4699` |
| Officer search (`734-744`) | integration wrapper at `743` | country-running flag | `4701-4714` |
| Specialist preservation (`746-756`) | specialist wrapper at `755` | lot UID | `4716-4742` |
| Rail corridor (`758-768`) | rail wrapper at `767` | state variable | `4744-4760` |
| Request cooldown (`770-780`) | cooldown wrapper at `779` | country cooldown flag | `4762-4770` |

The mission-only aggregate calls all nine independently (`4775-4787`), so simultaneous timeouts do not overwrite one another.

There are no `cancel_trigger`, `cancel_effect`, or exact-ID `remove_mission` call sites for these missions. Exact mission-name search returns only one definition and one activation for each mission, except request cooldown, which has its two intentional activation callers. Under the official mission contract, timeout is therefore the only scripted terminal route audited here.

### Thirty-nine incident options

The 13 event reports provide three options each and write a contiguous immutable enum:

| Event | Choice IDs |
|---|---:|
| `chaosx.nr19.300` | 1-3 |
| `.301` | 4-6 |
| `.302` | 7-9 |
| `.303` | 10-12 |
| `.304` | 13-15 |
| `.305` | 16-18 |
| `.306` | 19-21 |
| `.307` | 22-24 |
| `.308` | 25-27 |
| `.309` | 28-30 |
| `.310` | 31-33 |
| `.311` | 34-36 |
| `.312` | 37-39 |

The dispatcher has 39 unique branch IDs and 39 unique original effects (`management_effects.txt:5623-5820`). It does not call an incident selector or random list during replay. The immutable incident lot UID is captured at incident creation (`5021-5023`), copied into the deferred record (`5860-5873`), and re-resolved by UID (`5822-5858`).

Paywalled option IDs match exactly between event triggers and replay:

- 4: infantry equipment
- 8: motorized equipment
- 12: support equipment
- 25: support equipment + army experience
- 28: support equipment + motorized equipment
- 31: support equipment
- 35: motorized equipment
- 38: army experience

All use the same script constants and `greater_than_or_equals` comparison. An unaffordable exact choice remains pending; no free execution or substitute effect occurs.

### Two prefire choices

- Event `.2.b` stores exact draw choice 1 (`events/019_infantry_spawn.txt:37-50`).
- Event `.2.c` stores exact decline choice 2 (`53-66`).
- Replay maps only 1 to `infantry_spawn_execute_prefire_evolution_iii_initial_draw` and 2 to `infantry_spawn_decline_prefire_evolution_iii_initial_draw` (`management_effects.txt:5886-5913`).
- Both originals clear `infantry_spawn_prefire_opening_pending`, after which the deferred record clears.

### Two claimant choices

- Event `.201.a` stores accept choice 1 and requires the original affordability trigger (`events/019_infantry_spawn.txt:149-157`).
- Event `.201.b` stores refuse choice 2 (`159-166`).
- The deferred record stores exact claimant UID and exact demand enum (`management_effects.txt:6002-6017`).
- Replay finds that UID, proves the demand still equals the stored demand, temporarily selects the row, reuses the original affordability/refusal triggers, invokes the original response, and restores the previous selected index (`5940-6000`).

The UID/demand pair prevents replay against another claimant or a newly issued demand.

### Coverage assertion result

The source assertion extracted route IDs from the event requests and their replay branches:

```text
incident event requests: count=39; unique=39; missing=[]; duplicate=[]; unexpected=[]
incident replay branches: count=39; unique=39; missing=[]; duplicate=[]; unexpected=[]
prefire event requests: count=2; unique=2; missing=[]; duplicate=[]; unexpected=[]
prefire replay branches: count=2; unique=2; missing=[]; duplicate=[]; unexpected=[]
claimant event requests: count=2; unique=2; missing=[]; duplicate=[]; unexpected=[]
claimant replay branches: count=2; unique=2; missing=[]; duplicate=[]; unexpected=[]
mission timeout wrappers: count=9; unique=9
covered route total=52
```

The incident dispatcher assertion additionally returned:

```text
dispatch mappings=39; unique IDs=39; unique effects=39
duplicate effect mappings=0
```

## Transaction, caller, and compaction proof

### Stable identity and rollback preservation

- The same-tag active flag is set before snapshot capture (`scenario_effects.txt:1540-1545`).
- Lot and claimant UIDs come from monotonic global allocators (`common/scripted_effects/019_infantry_spawn_ledger_effects.txt:208-230`). Scenario rollback deliberately does not rewind those allocators (`scenario_effects.txt:1537-1539`), so a removed tail UID is never reused as a substitute identity.
- The transaction captures 18 tail boundaries (`1582-1599`). Rollback resizes 96 unique arrays to those exact boundaries (`1908-2013`), including the lot UID ledger at `1923` and claimant UID ledger at `1989`.
- The boundary assertion found 18 unique rollback boundaries, with no missing capture and no missing snapshot clear. The resize assertion found 96 targets, 96 unique arrays, and no duplicate target.
- `rg -n "infantry_spawn_deferred_" common/scripted_effects/019_infantry_spawn_scenario_effects.txt` returned no matches. The scenario snapshot, restore, and clear paths therefore do not rewind or delete a deferred record created after the snapshot. They also do not mutate the nine original mission-running flags/targets or the original incident, prefire, and claimant pending contexts.
- Normal Event 19 pulse/incident/claimant generation is locked, and the scenario package has no mission activation, incident dispatch, claimant-demand issue, or prefire-choice call site. Deferred records created during a prolonged lock consequently refer to pre-snapshot identities, not rollback-truncated scenario tail rows.

Rollback ordering is safe up to the P1 replay gate:

1. delete package objects and prove them absent (`2147-2159`);
2. resize tails, restore country state, validate ledgers (`2160-2165`);
3. finish only if the transaction can unlock, otherwise schedule another delayed retry (`2165-2176`);
4. finish clears lock/cleanup flags, clears snapshot variables, rebuilds the stable view, replays deferred actions, rebuilds again, and schedules the bounded pulse (`1744-1752`).

Commit calls the same finish effect (`1754-1758`). The commit proof and commit call occur within one synchronous scenario effect chain (`2401-2411`, `2508-2512`), so no delayed mission/event effect interleaves between proof and unlock on the success path.

### Caller ordering and idempotence

There are exactly two aggregate replay callers:

- scenario finish: `scenario_effects.txt:1749`;
- country pulse: `common/scripted_effects/019_infantry_spawn_pulse_effects.txt:13`.

The pulse calls replay before ledger validation, reconciliation, management, claimant work, evolution, and compaction (`pulse_effects.txt:9-66`). Successful resumers clear their deferred record only after the original terminal flag disappears, so the later pulse backstop cannot apply the same completed route twice.

The idle trigger correctly blocks on all three durable scenario ownership flags (`common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt:13-21`). The compaction gate includes the idle trigger plus all 12 deferred flags (`common/scripted_triggers/019_infantry_spawn_ledger_triggers.txt:117-152`). Automated set comparison returned:

```text
record flags=12; compaction gates=12
missing gates=[]
extra gates=[]
```

## Minimal safe remediation plan

1. Keep aggregate choice ordering as prefire → claimant → incident → missions.
2. For audit, standardization, demobilization, training, and specialist records, restore the immutable deferred UID into the original target and call the original completion whenever the record and original running flag exist. Remove the resumer's duplicate family/status gate; the original completion owns success/failure and unconditional cleanup.
3. Add an explicit structural-orphan classifier for every record family. Preserve affordability-only waits. For missing/invalid identity, enum, row, original context, or claimant demand mismatch, use an approved diagnostic terminal policy that cannot execute another row or another choice and cannot leave compaction gated forever.
4. Make record creation atomic: prove/copy required identity before setting the pending flag, or immediately enter the structural diagnostic path.
5. Replace raw route literals at event, affordability, and dispatch call sites with the already-defined script constants.
6. Re-audit these exact scenarios after the patch:
   - audit target + incident choice 1 during delayed rollback cleanup;
   - training/standardization target + a status-changing incident;
   - demobilization/specialist target + an incident, proving the incident applies first and the mission then terminates;
   - missing deferred UID and missing original running flag, proving no substitute row and no permanent gate;
   - unaffordable incident 25 and claimant accept, proving retry without free execution or substitution;
   - two aggregate replay calls after success, proving single application;
   - rollback retry with a deferred record, proving record survival across all 96 tail resizes.

## Commands and meaningful results

Representative source queries:

```powershell
rg -n "infantry_spawn_(resume_deferred_event19_actions|ledger_compaction_may_advance|scenario_transaction_is_idle)" common events
rg -n "infantry_spawn_deferred_" common/scripted_effects/019_infantry_spawn_scenario_effects.txt
rg -n "cancel_trigger|cancel_effect|remove_mission|activate_mission" common/decisions/019_infantry_spawn_decisions.txt common/scripted_effects
rg -n "infantry_spawn_(incident_choice_request|prefire_opening_choice_request|claimant_demand_choice_request)" events/019_infantry_spawn.txt
```

Meaningful scripted assertions performed against the current files:

- 52/52 route requests and replay branches accounted for.
- Incident mapping: 39 unique IDs → 39 unique original effects; no duplicate effect mapping.
- Affordability: exact paywalled set `4,8,12,25,28,31,35,38`; zero event/replay resource-signature mismatch.
- Compaction: 12 unique recorded pending flags and 12 exact gates; zero missing/extra.
- Mission termination: all nine original terminal flags clear at function depth one; all six target UID/state variables clear at function depth one where applicable.
- Rollback: 96 unique resize targets, 18 unique saved boundaries, zero duplicate array target, zero missing boundary capture, zero missing boundary clear.
- Scenario deferred-record mutation search: zero matches.

## Ownership release and safe status

No gameplay, decision, event, localisation, constants, registry, or spreadsheet file was edited. Ownership of all audited replay and transaction files is released to the parent.

**Safe status: blocked by the P1 incident/mission replay deadlock.** The 52-route coverage, affordability mapping, stable UID strategy, caller ordering, rollback snapshot preservation, and 12 compaction gates are otherwise proven in the audited source. Structural orphan handling remains a P2 requirement even after the P1 is fixed.

## Final remediation re-audit, 2026-07-15

This section supersedes the historical verdict and findings above for the current source hashes listed below. The earlier findings remain in this report as the record of what the remediation had to close.

### Final verdict

**Clean for release within the same-tag deferred-replay audit scope.** No P0, P1, or P2 finding remains in the frozen source.

- P0: none.
- P1: none. Incident replay still precedes mission replay, while all five UID-bearing mission resumers restore the exact deferred UID and delegate terminal handling to the original completion effect. Status or family changes made by the incident can no longer strand a mission-running or deferred-pending flag.
- P2: none. Missing or invalid records, missing original contexts, invalid route and demand enums, UID or demand mismatches, absent rows, and failed post-execution terminal checks enter an observable quarantine. The quarantine sets `infantry_spawn_deferred_replay_invariant_failure`, invokes the existing ledger-invariant failure path, terminates the recorded original context without selecting another row or route, and clears the deferred record.

### Frozen gameplay hashes

SHA-256 hashes for the exact source used by this final re-audit:

| File | SHA-256 |
|---|---|
| `common/script_constants/019_infantry_spawn_constants.txt` | `17f0758174404c4ff81f747d0d72923df8ebc3b8af3472897b6b7e72bf4674b3` |
| `common/script_constants/019_infantry_spawn_claimant_constants.txt` | `e2410f289e335dd5b0278426889769fe54df51f31268edf28fde610f08399fce` |
| `events/019_infantry_spawn.txt` | `f0d88177a1c0b348d2485ef44b1eb6e685dec99381f971551a22af3cf2611d46` |
| `common/decisions/019_infantry_spawn_decisions.txt` | `88243ecd6090ba945c4d58bf748482c8358c52639310ea3a73f9ab6a869a76c0` |
| `common/scripted_effects/019_infantry_spawn_management_effects.txt` | `8a966b6f0a6813dc208d5e69bd122f6392b3192999a20535597b4022dc3c38c4` |
| `common/scripted_effects/019_infantry_spawn_claimant_demand_effects.txt` | `0a0e0942707c1d4ee3c962fed46e009ef80bedc0ea2e9e8af2472edf05ebac7d` |
| `common/scripted_effects/019_infantry_spawn_evolution_effects.txt` | `783d02ae55e38b4dd2b7cd23c5e5f076e4c9d2a64b39f3ceade8ef27b4fd4064` |
| `common/scripted_effects/019_infantry_spawn_core_effects.txt` | `6ee213e7d2554b296b67fc33879a07cf2b628c83f70a4d652a66c0b986f015a2` |
| `common/scripted_effects/019_infantry_spawn_ledger_effects.txt` | `d8f7fc86c59283c560c4813a06ca977d662e19d0233ee990822a685d06d3ce84` |
| `common/scripted_effects/019_infantry_spawn_pulse_effects.txt` | `96771a3dd33803f6057c17c5061d631f423c9c8fa5a07d32e01c421726b4e54a` |
| `common/scripted_effects/019_infantry_spawn_scenario_effects.txt` | `8d4200df282fed156f95b14220252cb54608e5674e6c269f80d90b47705ae21d` |
| `common/scripted_triggers/019_infantry_spawn_claimant_triggers.txt` | `db48c0545037142329a03940aaf099d229fd5946d5b9ad032748c22bbb5c8a04` |
| `common/scripted_triggers/019_infantry_spawn_triggers.txt` | `17b27e02b21710ffa7afc477e90fd12bd4736f5f188b556e95c586bb22cf1b4a` |
| `common/scripted_triggers/019_infantry_spawn_ledger_triggers.txt` | `30abc883bd65dcb0db76cb7ed860dc8a6364e4d4a2b15a3077c2c304b59bf806` |
| `common/scripted_triggers/019_infantry_spawn_scenario_triggers.txt` | `966942ef1f644aaae54f93d5c38eacdeb14182a2f989d851673d71ae9ce79f93` |

### Remediation proof

The final source closes each historical finding:

1. Mission replay restores exact identity and terminates once. The nine timeout wrappers remain independently recorded. Audit, standardization, demobilization, training, and specialist preservation copy a named invalid-UID sentinel before setting their pending flag, replace it with the original UID when present, restore that exact value on replay, and invoke the original terminal effect. Muster districts, integration staff, rail corridor, and request cooldown retain their original terminal contracts. All records clear after their terminal attempt, and missing original running context is diagnosed rather than retained forever.
2. Incident replay is exact and fail closed. All 39 named event choices map one-to-one to 39 named dispatcher branches and 39 original incident effects. Missing original pending state, invalid or missing choice and UID, UID mismatch, missing or terminal row, an affordable but unmapped dispatcher result, or an executed effect that leaves the incident pending quarantines. An affordability failure does not execute, clear, or quarantine the record, so the exact choice remains queued.
3. Prefire replay is exact and fail closed. Draw and decline are the only accepted named values. Each calls its original effect once. Missing original pending state, an invalid value, or a response that fails to clear the original pending state quarantines.
4. Claimant replay preserves selection and payment safety. The record stores exact claimant UID and demand. Replay re-resolves that pair, temporarily selects only that row, and restores the previous selection on every executable path. Missing state, an invalid choice, UID, or demand, a demand above `constant:infantry_spawn_generalissimo_demand.parallel_command`, row or demand mismatch, a refusal that does not terminate, and a completed accept that unexpectedly leaves a non-`another_formation` demand pending all quarantine. Unaffordable accepts remain queued without payment. The existing `another_formation` materialization-failure route alone may retry after an affordable attempt because it charges only after materialization succeeds.
5. Repeated callers are idempotent. The aggregate has exactly two callers, the same-tag transaction finish and the bounded country pulse. Successful and quarantined paths clear their record synchronously. A second aggregate call therefore cannot repeat the completed route. The aggregate order remains prefire, claimant, incident, then all nine mission completions, preserving incident-before-mission behavior.
6. Retry scheduling and compaction use one source of truth. `infantry_spawn_has_deferred_event19_action` contains exactly the 12 recorded pending flags. The pulse-continuation branch requires that trigger and no ledger-invariant failure. The compaction gate negates the same trigger. An affordability wait receives the bounded pulse backstop and blocks compaction. A structural quarantine clears the record and leaves Event 19 failed closed through the ledger-invariant flag.
7. Rollback preservation remains intact. The scenario file contains no deferred-record mutation. Its 96 unique rollback resize targets remain unchanged, monotonic UID allocators are not rewound, and both commit and rollback release through the same finish effect before replay. Deferred records therefore survive delayed rollback cleanup and cannot resolve to a reused UID.

### Final assertion results

```text
incident constants/event requests/dispatcher branches: 39/39/39, all unique
prefire routes: 2/2
claimant routes: 2/2
mission timeout wrappers: 9/9
covered route total: 52/52
recorded deferred flags/shared trigger flags: 12/12, no mismatch
aggregate callers: 2
aggregate order: prefire < claimant < incident < missions
raw numeric event/replay route literals: 0
brace failures in the 15 hashed files: 0
```

The final direct source pass also confirmed that the claimant upper-bound check is present, incident and claimant affordability failures retain their exact records, structural incident, prefire, and claimant failures call the quarantine path, and the compaction gate references the shared deferred-action trigger once.

### Completion status

No gameplay file was edited by this auditor. This report is the only auditor-owned change. No simplification, fallback, omission, or blocker remains within the requested audit scope. Skills used for the audit were `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
