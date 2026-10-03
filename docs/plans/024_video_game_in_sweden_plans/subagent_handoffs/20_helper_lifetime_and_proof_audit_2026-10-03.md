# Event 24 helper lifetime and mission proof audit

Status: read-only source audit completed, three owner repairs verified by conservative source regressions, remaining mission/scope work and native evidence unresolved.
Acceptance basis: the parent explicitly requested this bounded audit of the accepted Event 24 package.
The user’s 2026-09-20 retirement of Field-Validated Planner supersedes older conversion wording.
Field-validation mechanics remain required, and the selected experimental spirit picture remains vanilla `SWE_wargames`.
No gameplay, localisation, existing documentation, index, or commit was changed by this auditor.
Only this handoff and scratch files under `tests/lifetime/` were written.
No omission, weaker proof, supply approximation, or new feature is approved here.

## Evidence identities and scope

The final scratch run inventories 183 Event 24 APIs: 93 main effects, two CXT effects, four runtime effects, 65 triggers, and 19 scripted-localisation definitions.
It also records source-linked caller locations and follows the directly consumed shared ticket, derived-load, and CXT-registration outputs.
Inventory is complete for these files, but execution coverage is deliberately limited to the named cases below.
The inventory does not claim that every native effect, trigger, event, mission, or random branch was executed.

| BEFORE audit source | SHA-256 frozen in `before_lifetime_results.json` |
| --- | --- |
| `common/scripted_effects/024_video_game_in_sweden_effects.txt` | `36b7a83af58de302240c561cc95fb45892b856e0b302a9c2afcd74b874ef499c` |
| `common/scripted_triggers/024_video_game_in_sweden_triggers.txt` | `d0a2a95c4ee89f908f41adf618f616c28ab3a794155c243640922977e71760ad` |
| `common/decisions/024_video_game_in_sweden_decisions.txt` | `8b19fcb187ff40bcfd66c49ff54ec18b009d5724cc6d74ec5bc416af463b6eef` |
| `common/scripted_localisation/024_video_game_in_sweden.txt` | `8d1d97965bbcdd572503950684bb8677d10bb65a124146bbbb20011e616a92ad` |
| `events/024_hearts_of_iron.txt` | `75e81ff4f8889a30957f23bc67a473f617fc4238b8dda07eca0a6edb8693798c` |
| `common/scripted_effects/024_video_game_in_sweden_cxt_effects.txt` | `84e2d9f1143504fb308720047d33c7e669cbecbe6e2cd29309a372855095469d` |
| `common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt` | `fda4e7869525bb22c3956bc5d6015b59dbac10f82ab80b402cce68bcd1028d64` |
| `common/scripted_effects/individual_crisis_targeting_effects.txt` | `903562c1dc27bf9367e5a8ab8a807047a798fb16de0bd8e1df2841b6a2c40b16` |
| `common/scripted_triggers/individual_crisis_targeting_triggers.txt` | `af537f93e969948ca5cb35e1d06c504f6797ccbaaf659a13c9a661db8e510b70` |
| `common/scripted_effects/chaosx_test_country_effects.txt` | `fb9b483db5d1a70b4f0900135b22815c612989ae0b3a4d50bca05072b22c39c3` |

The trigger file changed during the shared-tree audit when its quote API comment gained four lines.
The earlier trigger identity was `81c4b0839b9e3c22c03e268a8f91cc4039cbbab0596d5f629c2ab6682b622b9f`, matching the existing post-emergency snapshot.
The detailed findings below retain BEFORE spans bound to `d0a2...` for triggers and `36b7...` for main effects.
The owner subsequently changed these files, and the following AFTER section and current JSON inventory supply the current identities and spans.
The scratch result records hashes of all its inputs, including the immutable pre-output-lifetime payer used for the regression.
Later owner changes supersede these source findings only after review against their own identities.

Artifacts:

- `docs/plans/024_video_game_in_sweden_plans/tests/lifetime/actual_source_lifetime_audit.py`
- `docs/plans/024_video_game_in_sweden_plans/tests/lifetime/actual_source_lifetime_results.json`
- `docs/plans/024_video_game_in_sweden_plans/tests/lifetime/before_lifetime_results.json`, SHA-256 `1687d865ee8f17b7dd663497ef2983174220fe1514f3cace982a64802120f48e`.
- Existing baseline input `probability_snapshots/2026-10-03_pre_output_lifetime/024_video_game_in_sweden_effects.txt`, retained without overwrite.

## Owner lifetime tranche and AFTER proof

The parent applied three narrow repairs during this audit, and this auditor changed only its permitted tests and handoff to verify them.
The BEFORE cases and source identities were frozen before the current result artifact was regenerated.
The tests read actual immutable BEFORE inputs and actual current AFTER inputs separately, rather than expecting old defects from current code.

| Owner repair | Current source boundary | BEFORE and AFTER conservative result |
| --- | --- | --- |
| Nested ticket/load output storage | `common/scripted_effects/024_video_game_in_sweden_effects.txt:14-26`, initialization at 17-18 before call at 19 | Actual BEFORE helper returns 0 tickets without external scalar storage, 4 with weight only, and 2 with both outputs initialized. Actual AFTER helper returns 2 without external scalar initialization because it owns both outputs before the nested calls. |
| Calling-country host identity | `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:46-56`, target `tag = PREV` at 52 | Entered SWE returns true with SWE/NOR/GER ROOT after the repair. BEFORE rejected NOR/GER ROOT. Entered NOR from SWE ROOT returns false using the complete actual current guard and explicit foreign eligibility facts. |
| Foreign event gate affected by host identity | `events/024_hearts_of_iron.txt:533-542` | Whole actual immutable BEFORE `.40` trigger rejects a valid NOR recipient and SWE host. Whole actual current AFTER trigger accepts the same declared native facts. |
| CXT caller-owned added receipt | `common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt:24-28`, initialization at 24 before wrapper at 25 | Actual BEFORE daily caller prefix has no returned receipt. Actual AFTER daily caller prefix retains receipt 1. The subsequent package-sync operation is deliberately not executed by the model. |

Current AFTER hashes in the final regression are `95ec123ba5e2382db5653a28b8c0a71f2f8858d18a7cf19921d6c31ce2609955` for main effects, `d030792f946030bd262c4a3ec873bde1b2febf431f0b41595c68782c2b2ad39c` for triggers, `859cad1c74ee1dd4b92e6a3f416402eb181d9744cf9137dc27e475cf245aae87` for events, and `34ab09370af68a547cf69c99626c8a42c0dd4747efda7efe84fa75ae40905812` for CXT on-actions.
The JSON retains every other current source hash.
Immutable BEFORE inputs are the pre-output-lifetime effects snapshot `07a41c3ee9c2d47243121eb0320508da87e4444e543f62f28b304afbf3abc620`, post-emergency trigger snapshot `81c4b0839b9e3c22c03e268a8f91cc4039cbbab0596d5f629c2ab6682b622b9f`, post-emergency event snapshot `75e81ff4f8889a30957f23bc67a473f617fc4238b8dda07eca0a6edb8693798c`, and pre-remaining-routes CXT on-action snapshot `fda4e7869525bb22c3956bc5d6015b59dbac10f82ab80b402cce68bcd1028d64`.

The parent’s quote payer/getter repair also retains its separate actual BEFORE/AFTER regression.
Six model tests complete successfully against the patched source, with all previously documented unsupported native operations still excluded.
Source-model success does not establish native payment, event delivery, weighted behavior, package application, or mission proof.

## Final runtime observation review and correction

The parent added `common/scripted_effects/024_video_game_in_sweden_runtime_effects.txt`, SHA-256 `d24367c6a27c636c7396d2358155c91d1fe8037e05fe064363cb2175c11571e9`, and `common/on_actions/024_video_game_in_sweden_lifecycle_on_actions.txt`, SHA-256 `146ae2ff3ca85adf67a11de3374e842173e530f394cfc597e4b316d4cf1a68de`.
The new runtime file was read completely, as were its lifecycle hooks and the parent’s `tests/test_runtime_observation.py`.
The four runtime APIs export no temporary scalars or arrays and keep their lasting state in actor flags and regular variables.
Initialization now starts the bounded watch, `.91:707-716` receives it on the chosen country, and the observer increments elapsed days by the one-day constant at runtime-effect line 35.
Monthly mission elapsed increments were removed from the main maintenance helper.
Daily resource/region interruption receipts at runtime-effect lines 37-71 remain sticky until their explicit lifecycle cleanup.
State transfer calls the old controller’s loss helper through FROM at lifecycle lines 11-14, preserving native ROOT/new controller and FROM.FROM/state.
Control-loss lines 122-150 record Stockholm disqualification and actual Swedish core loss at the transaction.
Capitulation and annexation invoke actor-loss cleanup through the documented losing-country scope at lifecycle lines 16-21.
Runtime-effect lines 73-83 add a current commander-owner/role check before clean removal.
Installed `tag` documentation explicitly supports CHARACTER at `triggers_documentation.md:7649-7656`, so that owner check is not rejected merely because it enters a commander target.

The parent’s five observer source tests were run successfully: one-day elapsed advancement without the monthly increment, sticky interruption receipts, one pending watch, permanent Stockholm loss disqualification, and early reassessment scheduling.
The tests explicitly stub native predicates and record delayed events without delivering them, so they do not prove native supply, callback ordering, runtime persistence, or game delivery.
These owner changes supersede the historical missing-daily-observation/core-callback findings below at the source level.
Exact supplied-unit proof, equivalent-front definition, reachable full-audit reviews, and independent institutional proof remain unresolved.

Correction: the earlier periodic CXT application finding was an auditor error inferred from the helper’s name.
The current shared file has the same audited hash `fb9b...`, and its `chaosx_test_country_sync_registered_content:442-444` only sets `chaosx_test_country_registered_sync_pending`.
The separate `chaosx_test_country_sync_registered_content_apply:449-474` owns grants and invokes registered packages.
The Event 24 daily caller reaches the pending-only helper, so it complies with the pending registration boundary and needs no additional owner patch for periodic application.
The receipt lifetime repair remains valid and separate from that retracted finding.

## Prioritized findings and minimum owner patch scope

### P1 BEFORE finding: foreign response rejects its own recipient, source repaired by parent

Caller: `events/024_hearts_of_iron.txt:533-542`, especially line 537.
Callee: `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:46-55`.
Dispatch: `common/scripted_effects/024_video_game_in_sweden_effects.txt:2163-2183`.
`.40` is received by the foreign country, so ROOT is that recipient.
Entering `event_target:video_game_in_sweden_host` changes THIS to Sweden but retains the foreign ROOT.
`is_current_host` then checks the saved host’s tag against ROOT, rejecting a valid Swedish host.
The whole actual `.40` trigger evaluates false in the conservative scope test with a living SWE host, living NOR recipient, no war, and the correct pending flag.
This is a source scope result, not observed engine delivery.

Minimum patch: make `is_current_host` compare the target with the actual country invoking the helper, such as the verified immediate PREV inside its own target block, or use an explicit actor pointer.
Review its foreign-event consumers and country/state callback entry points together.
Do not rewrite the foreign AI pool or choose new weights for this repair.

### P1 BEFORE finding: nested prefire outputs are lost, source repaired by parent

Event 24 caller: `common/scripted_effects/024_video_game_in_sweden_effects.txt:14-23`, call at 16 and read at 17.
Shared wrapper: `common/scripted_effects/individual_crisis_targeting_effects.txt:11-15`.
Shared worker: the same file at `27-79`, load-trigger call at 38 and returned-load reads at 43-69.
Derived-load callee: `common/scripted_triggers/individual_crisis_targeting_triggers.txt:12-119`, creation at 15.
`individual_crisis_candidate_adjusted_weight` is first created in the worker and forwarded through the public wrapper without outer caller storage.
`individual_crisis_active_load` is first created in the load trigger and consumed after it returns to the worker.
Both boundaries matter independently.

For a declared one-load candidate, the actual source model produces zero tickets without preinitialization, four tickets with only the adjusted weight preinitialized, and two tickets with both adjusted weight and active load preinitialized outside the nested chain.
The load test supplies all other provider predicates as explicit false scenario facts and does not execute those providers or calculate a native probability.

Minimum local patch: initialize both scalar names before Event 24’s line 16.
Preferred shared API repair: initialize the worker’s consumed `individual_crisis_active_load` before its trigger call, require caller-owned adjusted-weight storage in the public contract, and initialize adjusted weight in Event 24’s caller.
The shared helper’s Markdown example currently initializes only its input and must document the output contract if the owner changes that API.
Do not clear the accumulating host array in the per-candidate helper.
The probability auditor must compare any changed weighted behavior under the parent’s named scenarios.

### P1: Exact supplied-field proof remains absent, historical observation gaps repaired by parent

Quantity/location helpers: `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:710-755`.
Field objectives: `619-637`.
Audit objectives: `639-668`.
National stockpile proxy: `255-266`, and committed-resource checks at `215-223`.
Maintenance consumers: `common/scripted_effects/024_video_game_in_sweden_effects.txt:2504-2525`, `2526-2539`, and `2581-2594`.
Timer increment: `2540-2549`, using the 30-day maintenance constant.

`has_front_presence` accepts two divisions in any one of states 138, 141, or 666.
It does not identify an active front, prove control of that one field state, or inspect any division’s supply.
The full audit checks all three states, two divisions per state, and full control, but still has no per-division supply test.
The country supply-gap trigger is false at peace and otherwise checks national train/truck/fuel stores.
Adequate national stores cannot prove local delivery, and an interruption between maintenance samples can disappear from the source record.
Only Stockholm loss sets the core-loss flag in the Event 24 source examined here.
There is no Event 24 `on_state_control_changed` handler that records loss of another Swedish core or continuous Stockholm control.

Minimum owner scope: existing field-package/objective helpers, their setup and maintenance consumers, mission outcome classifiers, and bounded relevant state-control hooks.
Maintain actual qualifying-time or interruption receipts separate from total elapsed time.
Record any qualifying core loss and relevant field-state turnover when the callback occurs.
Keep the accepted three-condition training package or a fully evidenced equivalent active-front package.
The missing documented per-division supply-satisfaction reader is a blocker, detailed below, and is not permission to call national stores supplied proof.
The final runtime section supersedes the missing daily observation and state-control callback portions of this BEFORE finding.

### P1: High-Chaos recovery cannot reliably obtain full-audit prerequisites

Callee gate: `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:445-461`, requiring both logistics and red-team completion.
Logistics caller visibility: `common/decisions/024_video_game_in_sweden_decisions.txt:41-46`, baseline or Evolution I only.
Red-team caller visibility and availability: `196-206`, Evolution I only and no active mission.
High-Chaos commercial setup: `common/scripted_effects/024_video_game_in_sweden_effects.txt:434-458`.
Reassessment option: `events/024_hearts_of_iron.txt:646-660`.
The high-Chaos commercial opening can enter Evolution II without either review.
The normal review actions are then unavailable, and full Reality Audit remains gated behind them.
Rare incidents can set individual review flags but do not constitute a guaranteed recovery route.

Minimum patch: expose the existing accepted logistics/red-team review work in the appropriate recovery context and verify that it can be completed without circular no-active-mission gates.
Do not remove the prerequisites or substitute the narrow audit for the full achievement route.

### P2 BEFORE finding: CXT receipt is lost, lifetime repaired and pending-only caller confirmed

Consumer: `common/on_actions/024_video_game_in_sweden_cxt_on_actions.txt:24-27`.
Wrapper: `common/scripted_effects/024_video_game_in_sweden_cxt_effects.txt:12-18`.
Callee: `common/scripted_effects/chaosx_test_country_effects.txt:353-373`, output creation at 354 and positive receipt at 370.
The global regular registration array survives, but `chaosx_test_country_extension_registration_added` does not survive the returning nested helpers without caller storage.
The source test reproduces absent returned receipt and persistent registration, then returns one with outer preinitialization.

Minimum lifetime patch: initialize that receipt in the daily caller before line 24 and document its outer caller requirement.
The daily hook calls `chaosx_test_country_sync_registered_content`, whose current body only marks pending work.
The earlier assertion that this applies packages was incorrect and is retracted.
No further CXT owner patch is required for that claimed issue.
Startup registration has no returned-receipt consumer and needs no receipt output solely for this audit.

### P2: Foreign fallback relation checks become self-comparisons

Candidate helper: `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:280-293`, especially 290-291.
Selection caller: `common/scripted_effects/024_video_game_in_sweden_effects.txt:2113-2123`, especially 2118-2119.
Inside `ROOT = { ... }`, THIS is ROOT, not the foreign candidate.
The faction check therefore asks about Sweden with itself, and the subject check asks whether Sweden is its own subject.
The same error appears in the available-partner predicate and selection fallback.

Minimum patch: compare the actual candidate through correctly nested PREV or an explicit captured pointer in both predicate and selector.
Retain the valid-host actor explicitly when the helper is reached from a foreign event or callback.
Convoy access, blockade, autonomy, and overlord permission remain accepted work queued in report 16, and this scope repair does not implement them.

### P2: Dual-Track and restriction verify elapsed time rather than their institutions

Dual-Track objective: `common/scripted_triggers/024_video_game_in_sweden_triggers.txt:670-680`.
Restriction objective: `682-690`.
Decision/mission consumers: `common/decisions/024_video_game_in_sweden_decisions.txt:735-796`.
Dual-Track currently needs only active/current host, 90 elapsed days, and Stockholm ownership/control.
No distinct simulated plan, independent conventional plan, or comparison result is produced or checked.
Restriction currently needs only active/current host and 60 elapsed days.
No official-league closure, policy-use removal, or state-supported facility withdrawal receipt is checked.

Minimum owner scope: existing start/objective/complete helpers and their mission callbacks, using country-owned persistent receipts for the accepted work.
Dual-Track requires three distinct results for simulated plan, conventional plan, and comparison, with independent production paths.
Restriction should record and enforce the three accepted closures deterministically within its existing period.
It must remain available with zero reserves and must not gain resource, unit, supply, or subjective compliance failure gates.
Only invalid host/system state may fail emergency restriction.

The restriction result also calls `start_recovery` at `common/scripted_effects/024_video_game_in_sweden_effects.txt:1587`.
That reaches `refresh_stage_idea:369-381`, granting Validated Wargaming Methods after restriction.
The accepted restriction outcome removes Event 24 benefits, so the owner must distinguish its finite backlash/closure from an earned validated-methods reward.
This is a route-semantics finding, not a proposal to rebalance the reward.

## Complete temporary-output classification

| API group and exact boundary | Output/input ownership and result |
| --- | --- |
| BEFORE `add_current_country_to_prefire_pool:14-23` to shared ticket wrapper/worker/load | Historical unsafe outputs, repaired by the parent’s current initialization at 17-18. Current array output remains caller-owned. Base weight and remaining-ticket scalar are local. |
| Stockholm selectors `25-44`, `46-64`, per-candidate calls at 34/54 | Host pool is cleared before nested calls, then consumed by the same selector. The source model assumes clear allocates caller storage, but installed documentation only promises clearing contents. Native allocation behavior remains unverified. Newly callee-created arrays are dropped by the model. Host output is a global event target, not a temporary array return. |
| `prepare_random_event_fire:66-161` to `chaosx_settings_effects.txt:4301-4305` | `prefire_ready` is initialized in the actual outer caller before helper entry. Its consumed output is lifetime-safe in this source contract. The host pointer and opening flag are persistent side effects. |
| `quote_restriction:151-177` to payer `751-765` | All three consumed quote scalars have caller storage at payer lines 753-755. Available-stability and available-war-support scratch values are local to the quote. Confirmed by source call-frame regression. |
| Quote to `can_pay_restriction:179-181` | Boolean-only caller, no quote output consumed after its return. No output preinitialization is required solely to obtain that Boolean. |
| Quote to numeric getters `scripted_localisation:332-374` | Each `text.trigger` initializes only the quote scalar that its selected YAML key consumes. Whole/fractional PP branches and Stability/War Support getters retain their consumed scalar in the model. Rendering remains unverified. |
| Exercise getter `scripted_localisation:311-330` | Its display scalar is created directly in `text.trigger`, with no nested helper boundary. YAML consumer is the named display key. No persistent display global is needed. |
| `change_reliance:256-275`, all action/incident callers | Action and option callers create `reliance_delta` before entering the helper. `reliance_next` is local and written into regular country `simulation_reliance` before return. Delta reset is an intentional consumed-input mutation. |
| Incident wrapper `1946-1949`, event option callers `events:298-411` | Caller-created delta survives wrapper and nested reliance helper. Incident ID/last-ID/cooldown are regular country state, not returned temporary outputs. |
| Ordinary payers `586-749`, `767-778` | Reused cost scratch is debited inside each payer, and no Event 24 caller reads it afterwards. Factory-burden state is regular country storage. No output lifetime defect found in these payer boundaries. Native payment execution is not tested. |
| Timed idea/modifier helpers `321-407`, `1246-1270`, `1348-1395`, `1435-1460`, foreign resolvers `2251-2356` | Duration scratch is consumed inside its creating helper. Persistent modifier/idea application is distinct from temporary lifetime. Parser acceptance of every duration field remains native evidence, not proved by this audit. |
| Evolution recorder `907-917`, callees at 912/916 | `current_chaos_tier_value` is initialized at 911 before its getter. Logger input scalars and actor target are supplied before logger entry and need not survive the Event 24 recorder’s return. No consumed external output was found here. Full shared logger implementation is not executed by the scratch model. |
| Incident roller `1951-2093` | Availability sentinels and seven weights are local and consumed by `random_list` before return. They are not caller-return outputs. Native random selection and the Boolean-sentinel rule remain separate acceptance items. |
| Maintenance `2439-2736` | Burden delta and timed-flag days are local and consumed before return. Mission progress and other values are country-scoped regular state. There is no temporary progress return API. |
| Foreign selector/dispatch/resolvers `2095-2372` | Outputs are persistent country flags, country outcome state, and global event targets. Local durations/deltas are consumed internally. Scope and target lifecycle defects are separate from output lifetime. |
| CXT wrapper `12-18` to registration receipt, current daily consumer `24-28` | Historical missing receipt repaired by caller initialization at 24. Token input is created in the wrapper and consumed in its callee. Regular global registration persists, and the subsequent helper only marks pending work. |
| Runtime watch/observer/control-loss/actor-loss APIs | No temporary outputs. Current-country flags, regular elapsed state, and pending event receipts persist separately from call-frame storage. Source observer cases pass under declared native predicate assumptions. |
| Remaining inventoried effects/triggers/localisation definitions | No direct temporary return output is created or consumed. Their saved state, flags, targets, Boolean gates, and visible strings still require their own gameplay/native validation. The JSON lists every definition, nested call, and temporary write rather than marking unexecuted APIs as passed. |

## Exact owner scope and object-target findings

All main program state belongs to the selected Swedish country.
The prefire candidate helper is called in each candidate country, not necessarily ROOT.
The CXT fixture belongs to CXT and cannot be used as proof that CXT is Sweden.
The saved host/foreign partner/last partner/opponent targets are country objects, while the commander target is a leader/character object.

Country pointers must combine target presence with `exists = yes` and the relevant active/identity conditions before effects are applied.
Foreign dispatch already checks recipient existence and capitulation at `effects:2173-2178`.
Foreign report queue checks host existence at `2202-2203`.
Foreign resolver entry blocks at `2253-2254`, `2280-2281`, `2306-2307`, `2334-2335`, and `2360-2361` only check target presence, so they need valid-host/active-context revalidation after asynchronous delivery.
The foreign `.40` event also does not prove that its recipient is the country currently named by `foreign_partner`.

Trust opponent tracking at `effects:1305-1346` and `1660-1736` explicitly uses ROOT for opponent comparisons and receipt writes.
Its present direct callers are Swedish country events/decisions/maintenance, so a different ROOT is an API constraint risk rather than a reproduced current callback failure.
The new lifecycle state callback calls the old controller’s `record_control_loss` helper and uses the repaired calling-country host predicate.
It invokes reassessment opening, while Trust opponent progress remains on country event/observer paths.
Further callbacks must carry the host explicitly and must not enter Sweden assuming ROOT has changed.
Use callback-native ROOT/new controller, FROM/old controller, and FROM.FROM/changed state as distinct objects.

Commander cleanup at `effects:551-584` uses `scope_exists` plus `has_trait` on a saved leader target and deliberately follows a transferred commander.
This is not the documented always-true `var:` scope error, and `exists = yes` must not replace it in CHARACTER scope because installed docs restrict that trigger to COUNTRY.
Assignment in the BEFORE main source at `497-549` uses assigned army leaders with units.
The final runtime source adds ongoing owner/role observation, whose native death/transfer behavior remains unverified.
The assigned receipt is not cleared in cleanup’s successful target branch in the BEFORE main source at `560-570`.
The retired replacement trait is absent from the inspected Event 24 gameplay, and cleanup must continue to remove only the Rulebook Commander trait.

Closure at `effects:1810-1865` clears shared global partner/commander/opponent/host pointers without proving that the closing country owns each pointer.
Current source exposes no ordinary host-migration transaction, so stale-old-host cleanup is an unresolved ownership risk rather than a demonstrated gameplay occurrence.
Before adding migration or callbacks, require pointer/context ownership before clearing globals and preserve earned finite aftermath and achievement receipts.
`last_partner` plus the host’s `foreign_outcome` form a single report slot, which is not a stable per-delivery identity if reports overlap.
Current UI rendering and delayed delivery cannot establish that overlap is harmless.

## Native division, transport, and front evidence

Installed documentation and vanilla precedents support the following exact mechanisms.

| Mechanism | Scope and useful proof | Reference |
| --- | --- | --- |
| `divisions_in_state` | COUNTRY, owned divisions located in a specified state, optional majority type/unit. Current `size > 1` means two divisions. No supply or continuous-time proof. | Installed `triggers_documentation.md:2648-2661`, offline Triggers `1279`, examples `1380-1392`. |
| `num_armies_in_state@<state>` | COUNTRY dynamic reader for state quantity, usable with variable comparisons and shared constant thresholds. It does not filter supplied divisions. | Installed `dynamic_variables_documentation.md:526-533`. |
| `any_state_division` / `every_state_division` | STATE to actual division objects. Filter through OWNER to the host. The effect iterator can count qualifying objects in a bounded sampled pass, with caller-owned temporary counters. | Installed triggers `1684-1691`, effects `4173-4190`, vanilla `common/decisions/NOR.txt:2411-2423`. |
| `any_country_division` / `every_country_division` | COUNTRY to owned division objects. Useful for declared field packages and typed unit checks. | Installed triggers `1345-1352`, effects `3858-3875`, vanilla NOR `1425-1435`. |
| `unit_strength`, `unit_organization` | Actual division readiness, each on 0-1 scale. Installed generated scope columns are blank, and offline Triggers explicitly classifies these as Division triggers. Neither measures supplied status. | Installed triggers `7686-7702`, offline Triggers `2217-2225`. |
| `get_supply_vehicles_temp = { var = <name> type = truck/train need = yes/no }` | COUNTRY, actual required or stockpiled supply-vehicle totals. Initialize all consumed outputs in their caller before a helper computes them. These totals do not prove a local division’s delivery. | Installed triggers `2979-2992`. |
| `has_railway_connection` | Real existing rail path using path/province/state endpoints. Validate controller/path context separately. Connectivity alone cannot prove capacity, delivery, or satisfaction. | Installed triggers `4603-4626`. |
| `has_railway_level` | Real state railway level at or above the selected level. This alone cannot prove the chosen field party receives supply. | Installed triggers `4628-4640`. |
| `is_fully_controlled_by` | STATE, full control by the explicitly chosen host. | Installed triggers `5585-5592`. |
| Leader `num_units_in_state`, `num_units_in_combat`, `num_units_defensive_combats`, `num_units_offensive_combats`, `num_battle_plans` | UNIT_LEADER, useful bounded actual-front or plan evidence with a valid host-owned leader. Combat/plan presence is not independent adjudication or supplied status. | Installed dynamic variables `1262-1263`, `1310-1332`. |

Exact per-division supplied proof is blocked.
No division supply-satisfaction predicate or reader was found in the inspected installed trigger/dynamic-variable documentation, the offline division trigger table, or the bounded installed scripted-trigger/effect search.
`is_unit_template_reserves` reports supply priority rather than whether supply arrived.
`unit_ratio_ready_for_plan` is documented only as ratio ready for plan and must not be renamed supply evidence.
`frontage_full` describes combat width, not a stable strategic front.
Do not invent `is_supplied`, `is_in_supply`, `supply_ratio`, an unsupported iterator `count` argument, or a state supply-status field.
Read-only MCP script validation is not exposed in the connected registry or the bridge’s filtered live tool list.
The missing exact reader and validation route must remain an unsupported-field blocker until authoritative native evidence establishes a real mechanism.
An accepted equivalent-front route still requires actual unit/front/transport evidence and must not silently waive its supplied requirement.

## Owner helper, tuning, lifecycle, and migration plan

No central router, wrapper skill, broad helper rewrite, or new subsystem is proposed.
Keep the owner patch inside existing Event 24 APIs and their direct consumers.

| Existing helper to repair | Owner scope, inputs, outputs, side effects, and consumers |
| --- | --- |
| `is_current_host` | Current country as actor, saved host as comparison target, Boolean output, no persistent mutation. Consumers include Swedish decisions, foreign event `.40`, and future bounded callbacks. ROOT must remain inherited. |
| `add_current_country_to_prefire_pool` | Candidate country, base weight plus caller-owned adjusted-weight/load storage, appended candidate tickets, temporary array mutation only. Stockholm selectors consume the accumulating pool. |
| `register_cxt_test_content` | Current registration country, carrier token, caller-owned added receipt, regular global registry mutation. Parent lifetime repair is verified, and the current daily caller already marks pending without applying packages. |
| Field start/package/objective helpers | Explicit Swedish actor, declared states/fronts, committed resources, and caller-owned calculation outputs. Store lasting proof on the actor, with distinct interruption/core-loss receipts. Decisions and mission resolvers consume the same proof contract. |
| Dual-Track start/objective/result helpers | Swedish actor and independent plan producers, three persistent receipts and comparison outcome, bounded burden and finite recovery. Existing verification mission consumes them. |
| Restriction start/objective/result helpers | Swedish actor and deterministic closure work, persistent policy/league/facility enforcement receipts, reserve-limited payment and finite backlash. Existing enforcement mission resolves without an extra economic or military failure gate. |

Keep existing money, Reliance, mission bands, and probability targets unchanged unless the parent explicitly applies accepted tuning work.
Use the existing shared quantity/duration constants, preserving documented units.
If exact `divisions_in_state.size` cannot read constants, the documented dynamic state-count reader can remove threshold duplication for quantity checks, or a verified meta trigger can inject the static literal.
Neither method solves the missing supplied-unit reader.
Any new proof threshold, comparison duration, or enforcement band belongs in the event-owned constants and needs owner acceptance rather than an auditor-selected target.

Global event targets are justified for the persistent host and ongoing asynchronous contexts, and must have ownership-aware cleanup.
Short-lived actor/candidate capture should use regular event targets or caller-owned temporary object pointers, with explicit lifetime across any nested calls.
Saved mission progress, plan results, interruption history, and enforcement receipts belong in regular actor storage or flags, not temporary outputs.
Do not put temporary results into scoped `ROOT.temp` / `PREV.temp` tokens.

Migration order: repair returned scalar contracts, repair actor identity and candidate relations, establish evidenced field/transport mechanisms, make recovery reviews reachable, implement distinct institutional receipts, then review mission callbacks and cleanup against the same contract.
Use active mission type and setup receipts in callback resolution so stale callbacks cannot publish another outcome after cleanup or restart.
Run the required read-only probability baseline/compare through `chaosx_ai_probability_auditor` if the owner changes weighted eligibility or targeting.
Keep all remaining accepted work in report 16 unresolved or accepted and queued, without promoting an incomplete mission to implemented.

## Meaningful validation and limits

Command: `python -X utf8 docs/plans/024_video_game_in_sweden_plans/tests/lifetime/actual_source_lifetime_audit.py`.
Six lifetime/scope model tests completed successfully, with 183 source API inventory entries, and the parent’s five observer source tests also completed successfully.
They reproduce defects or verify narrow contracts, rather than asserting the event is correct.

- Immutable before payer with reserves `100/.8/.75` debits `0/0/0` after callee-created quote storage is discarded.
- Current payer debits `-30/-.04/-.03`, zero-PP partial reserves debit `0/-.02/-.01`, negative reserves debit zero, and five-decimal reserves preserve exact debit arithmetic.
- Current numeric getters retain only their consumed quote output.
- Actual immutable BEFORE one-load ticket case returns 0/4/2 tickets for no output storage, weight-only storage, and weight-plus-load storage respectively. Actual current AFTER returns two without external scalar storage.
- A newly callee-created host array is dropped, while outer initialized array storage survives nested calls under the declared allocation model.
- Actual BEFORE CXT daily caller loses the nested receipt, while persistent global registration survives. Actual current AFTER daily caller retains one through its source preinitialization.
- Actual immutable BEFORE host guard and `.40` trigger demonstrate ROOT rejection. Actual current AFTER accepts entered SWE under NOR/GER ROOT and the complete valid foreign event, while entered NOR under SWE ROOT still rejects.
- Actual CXT fixture writes regular state on CXT separately from another country’s saved state and same-named temporary storage.
- An executed unsupported `is_supplied` node raises an explicit error instead of being treated as a pass.

Unsupported or skipped execution includes native currency/stockpile binding, true division supply, actual array allocation on clear, complete mission timer/callback behavior, event delivery, save/reload, native character retirement/transfer, meta expansion, random selection/probabilities, and localisation rendering.
The scratch interpreter uses named native/provider scenario facts for scope and ticket cases, and does not pretend to execute those engine predicates or unrelated providers.
All unsupported execution categories are retained in the JSON artifact.

## MCP evidence and blockers

Connected HOI4 reference, event, decision, map, and probability routes are exposed in this auditor’s registry.
Exposure differs from successful domain execution.
Connected reference context, reference search, valid-scenario decision inspect, and Event24 state-flow inspect each returned `timed out awaiting tools/call after 600s`.
Initial invalid selector/scenario probes were schema rejections and were not treated as inspection evidence.

The parent-supplied read-only bridge was read completely and used with the installed official schemas.
Its initialize and filtered `tools/list` succeeded against server `hoi4-agent-tools` version `3.6.0`, protocol `2024-11-05`.
Client capabilities were empty, so native task negotiation was not claimed.
Exact `get_supply_vehicles_temp` reference search with limit one, adjusted-weight helper source lookup with references disabled / one definition / fifteen lines, and `.40` trace with depth one / four nodes / four edges each timed out after 40 seconds.
Every owned bridge process was cleaned up, with `ownedSessionSurvivors: []`.
No service was restarted and Hearts of Iron IV was not launched.

`chaosx_ai_probability_auditor` was delegated only the helper probability inspection evidence pass.
It verified live probability route exposure and server 3.6.0, then attempted `hoi4.probability_inspect` on the actual Event 24 effects path.
Its exact result was `TimeoutError: MCP id 2 returned no result after 40s`, empty stderr tail, and no owned survivors.
No candidate pool, trace, artifact URI, source revision, scenario hash, or numerical result was returned.
It did not choose balance targets or write files.

After the parent reported restored native routes, this auditor retried the exact supply-vehicle reference search and bounded `.40` trace, and requested map lookup for only states 138/141/666.
Both restored native reference/event retries returned `timed out awaiting tools/call after 600s`.
The bounded map lookup also returned that same 600-second timeout.
All pending MCP requests have now returned, and no further requests were made after the parent instructed the auditor to finish.
No successful current reference-read, event render/compare, decision lifecycle scenario, probability evaluate/compare, or map proof is claimed.
The exact timeouts remain the established blocker, and no domain artifact was returned.

## Reference ledger

Installed documentation root: `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/`.
Offline wiki root: this repository’s `paradox_wiki/`.
Pertinent sections were read directly after route failure, as allowed for references, and never represented as equivalent MCP or engine evidence.

| Reference | Read spans and SHA-256 revision |
| --- | --- |
| Offline Data structures | `275-325`, `426-490`, `1069-1091`. `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`. Line 440 is the conservative helper-output lifetime basis. |
| Offline Scopes | `249-270`, generic iterator explanation at `47`, division iterator rows around `550-552`. `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49`. |
| Offline Effects | Scripted effects `4683-4707`. `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`. |
| Offline Triggers | Division quantity rows `1276-1282`, examples around `1380`, division table `2217-2225`. `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06`. |
| Offline Localisation | Temporary display `729-791`. `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064`. |
| Offline Decision modding | Mission lifecycle `464-478`. `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`. |
| Offline On actions | Annex/civil-war contract `257-260`, state-control contract `450-461`. `6822adc85a374a1c1364f2def6f32c6d66da9fb0280319ddd6af4b84b33d882a`. |
| Installed triggers documentation | Native sections in the division/transport table, plus `2708-2715`, `3022-3029`, `3410-3420`, `4951-4958`, `6321-6328`, `7450-7471`. `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`. |
| Installed effects documentation | `2312-2325`, `2763-2771`, `3858-3875`, `4173-4190`, `6496-6512`. `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`. |
| Installed dynamic variables | State army counts `526-533`, leader plan/combat/location readers `1262-1263`, `1310-1332`, ready-for-plan `1382-1383`. `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`. |
| Installed script concepts | Script constants `216-240`. `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`. |
| Installed script_constants documentation | Entire schema/examples file. `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`. |
| Installed decisions documentation | Entire `common/decisions/_documentation.md`, including evaluation cadence and scopes. `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`. |
| Vanilla division precedent | `common/decisions/NOR.txt:1425-1435`, `2411-2423`. `dcb40a1a2f2e1a484df677ef44451920ccf7f2d123db1dd035d2166cf1ebb531`. |
| Vanilla scripted localisation | `common/scripted_localisation/00_scripted_localisation.txt:1-65`, native namespace warning and named keys. `6f490e33736f4dc31568add5753a1afdef916f3993804febfbbe6d1583827587`. |

All accepted Event 24 spec files and supporting prompts were read, including the full four-part specification, decision map, achievement prompt, probability scenario package, asset prompt, research notes, acceptance/review handoff, catalog notes, and goal/coding/decision prompts.
Report 16 was read as incomplete implementation evidence and does not authorize omissions.
Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`, read completely including Helper output lifetime.
No skill was created or changed.

## Completion disposition

Completed: actual-source API/output inventory, immutable BEFORE case evidence, actual current AFTER verification of the parent’s three narrow repairs and quote repair, bounded runtime-source review and five observer cases, correction of the CXT helper interpretation, scope counterexamples, native syntax/reference audit, prioritized remaining owner patch scope, and this bounded handoff.
Blocked: exact native supplied-unit proof, successful MCP domain evidence, full mission/foreign delivery/runtime validation, and dependent probability comparison.
Accepted and queued with the parent’s stated basis: unresolved field, audit, Dual-Track, restriction, recovery-review, persistence, and other report-16 acceptance work.
No gameplay fix was implemented by this audit and no simplification was applied.
The parent owns implementation and final review, and this report makes no Event 24 completion claim.
