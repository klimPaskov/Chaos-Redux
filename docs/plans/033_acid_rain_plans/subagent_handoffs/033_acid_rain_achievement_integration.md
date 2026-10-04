# Event 033 achievement integration handoff

Disposition: implemented source integration, blocked acceptance.
Acceptance basis: the parent explicitly requested Event033 achievement integration, required the ten contracts in Part 10 and the achievement prompt, and later authorized existing achievement effects/triggers plus narrow event, runtime, and preparedness hooks.
The parent then explicitly accepted the strict per-state 0.05 percent evacuation ceiling and supplied durable launcher markers within the user/orchestrator authorization to choose recommended options and fully implement them.
That acceptance is recorded in `docs/specs/033_acid_rain_specs/specs/033_acid_rain_achievement_threshold_and_launch_acceptance.md` and linked from Part 10 and the achievement prompt.
This handoff does not assert full Event033 completion or observed game behavior.
No commit was created.

## Ownership and changed files

The integration changes are confined to:

- `common/scripted_effects/033_acid_rain_achievement_effects.txt`
- `common/scripted_triggers/033_acid_rain_achievement_triggers.txt`
- Authoritative achievement hooks in `common/scripted_effects/033_acid_rain_effects.txt`
- Paid completion, evacuation, recovery, and administrative cleanup hooks in `common/scripted_effects/033_acid_rain_preparedness_effects.txt`
- The hidden deadline callback `chaosx.nr33.41` in `events/033_acid_rain.txt`
- This handoff.

The accepted follow-up additionally changes only the shared severe-survival numerator/denominator in `common/script_constants/033_acid_rain_constants.txt`, the Three Evacuations DESC/tooltip keys in `localisation/english/chaosx_achievements_l_english.yml`, and the relevant accepted achievement spec/prompt clarification.

The validator was never edited by this subagent.
The resumed parent lock on `acid_rain_remove_legacy_missions`, migration/census call sites, the inert legacy decisions, and `.tools/validation/validate_033_acid_rain.py` was preserved.
The pre-resume bridge set already contained a census recipient correction from `ROOT` to `event_target:acid_rain_census_country` in formation and responsibility census helpers.
That correction must be reviewed with the parent's migration tranche because country census inputs also feed cost bands and AI scenarios.
No probability weights, random draws, weighted target selection, weather duration rolls, decision costs, CXT hooks, GUI files, assets, or catalog files were edited during the resumed review.
The follow-up localisation edit is limited to `acid_rain_033_three_evacuations_DESC` and `acid_rain_033_three_evacuations_tooltip`.
The deterministic achievement deadline callback is distinct from the weather and probability timers.

## Ten-achievement review

| Achievement | Authoritative facts and edges | Source disposition and remaining limitation |
| --- | --- | --- |
| `before_the_first_drop` | Formation controlled-state census, paid component tier-4 completions, exact Preparedness observations, first opening pulse | Wired. Requires all four paid tier-4 dates and 100 Preparedness before an opening receipt. The permanent award is not revoked by a later opening shock. |
| `shelters_held` | Committed severe/superstorm forecast targets, forecast-time population, paid shelter/evacuation receipts, exact severe pulse outputs, episode closure | Wired. Requires at least three frozen target rows, two actual per-state episode pulses, a protection receipt, and deaths strictly below 0.05 percent. State pulse counts are not summed to manufacture two episode pulses. Early phase retirement cannot satisfy completed-cell validity. |
| `three_evacuations` | Paid evacuation start and completion with matching forecast/episode identity, completion strictly before first severe pulse, frozen per-state forecast population, final episode deaths, distinct state IDs | Wired with the explicitly accepted strict 0.05 percent ceiling for each state separately. The wrapper divides the frozen baseline by 10000, then multiplies by 5 without rounding. Final episode settlement compares actual applied deaths with strict less-than. New valid records have a calculated ceiling rather than a zero placeholder. |
| `railways_still_run` | Formation state/capital baseline, measured national exposure intervals, three paid reroutes, native current-capital railway checks, natural acute closure | Wired for native connectivity. Required checks use `has_railway_connection` with allied-territory restriction and a different controlled railway state as the endpoint. Full damaged-route and delivered-supply semantics remain unverified. An award is deferred until natural closure so a later required isolation check can still disqualify it. |
| `under_one_sky` | Global transition, previous and current Preparedness, actual elapsed check dates, current capital ID and stored aftermath tier | Wired. Checks credit actual elapsed intervals of at most three days, require the preceding floor observation, and reject skipped intervals, a floor breach, or tier-3 capital at a required check. The transition itself contributes no free days. |
| `after_the_clouds` | Natural dissipation, immutable owned-core state snapshot credited to OWNER, actual recovery changes to tier 0, frozen 180-day deadline | Wired. The snapshot remains with its original owner across controller changes. Recovery on day 180 is accepted. Remaining unresolved rows are audited on day 181. |
| `five_states_few_dead` | Frozen starting national population, distinct states actually touched, exact applied death ledger, natural acute closure | Wired. Uses closure deaths strictly below 0.10 percent of the immutable baseline. Administrative closure and missing population proof cannot qualify. |
| `small_state_civil_defense` | Starting civilian factories, formation eligibility, paid Preparedness peak, first exposure, tier-3 responsibility snapshot at natural closure | Wired. Uses fewer than ten starting civilian factories, at least 60 Preparedness, and zero tier-3 states at closure. Current factory growth cannot replace the starting band. |
| `two_regions_ready` | A real warning region/visit captured when a paid urgent action starts, its completion, actual front arrival | Wired. One national action captures one warning visit. Completion is stored until actual arrival, rather than crediting an estimated future date. Two distinct region and visit receipts are required. |
| `no_severe_ruins` | Actual tier-3 entry, unchanged per-state deadline, paid downgrade date, current unresolved responsibility transfer, natural closure | Wired. A downgrade at age 180 is late. Unresolved duty moves once to the new controller, with the original entry and deadline retained. Award evaluation waits for acute closure. |

All ten root-registry completion triggers read their permanent award receipt.
An unprotected severe episode rejects that episode, rather than making a later fully qualifying one-cell result impossible.
Generation resets preserve those receipts, while current-generation facts and transient pointers are cleared.
Achievement schema version 2 rejects unsupported schema-1 progress instead of reconstructing it from present modifiers.

## Helper map and exact inputs

The existing public recorder contracts remain documented immediately above their definitions.
Runtime bridges populate caller-owned `acid_rain_033_input_*` temporary variables and invoke the public recorders with `= yes`.
No named-argument or `$PARAMETER$` interface was introduced.

| Bridge or settlement helper | Scope | Inputs and source | Output and side effects | Authoritative call site |
| --- | --- | --- | --- | --- |
| `begin_runtime_country` | Country | Current generation, frozen controlled-state count, starting population in people, starting civilian factories, guarded real capital ID, durable global launch origin | Immutable national baseline, formation eligibility, global forced-generation disqualification, retained CXT debug marker | `acid_rain_form_country_registry` |
| `register_runtime_state` | State | Current generation, THIS.id, frozen `acid_rain_state_population_start_k` multiplied by people-per-k | Current-generation state baseline and responsibility pointers | `acid_rain_start_runtime`, after country census |
| `record_runtime_project` | Country | Paid project ID, stored paid target tier, current completion date, actual Preparedness, country receipt sequence | Peak observation and paid component date, then award evaluation | `acid_rain_complete_project`, after tier/gain and before ledger clearing |
| `record_runtime_pulse` | State | Actual pulse key/class/opening flag, matching severe episode or zero, exact `state_civilian_population_loss_applied` | Deduplicated state and current-country death evidence, separate severe evidence, touch/opening facts | `acid_rain_apply_state_pulse`, only inside the new-key branch and after population reconciliation |
| `record_runtime_forecast` | State | Committed forecast ID, episode ID, forecast date, current state population, valid existing shelter receipt | Frozen target baseline and original credit country | `acid_rain_create_severe_cell` and `acid_rain_create_superstorm_forecast`, after target commit |
| `record_runtime_warning` | State | Stored warning visit/region/front/date and current controller | One country warning row | `acid_rain_prepare_front_warning` and an actual pending-warning responsibility transfer |
| `capture_action_start` | Country | Paid action key, actual start date, first qualifying live warning in owned responsibility rows | One persisted warning association per action | `acid_rain_start_action`, after payment |
| `record_runtime_action` | Country | Paid completion key, action type, preserved warning association | Reroute receipt, pending warning completion row, or valid shelter protection rows | `acid_rain_complete_action`, after validated action application |
| `record_runtime_arrival` | State | Stored visit/region/front and actual arrival date | Arrival row and completed urgent-action timing proof | `acid_rain_execute_front_move`, before clearing warning flags |
| `record_runtime_evacuation_start` / `record_runtime_evacuation_completion` | State | Matching forecast/episode, paid country action key, start/completion dates, frozen forecast population, measured episode deaths, first pulse date, calculated strict 5/10000 per-state ceiling | Timing receipts and pending casualty evidence, no immediate three-evacuation award | Paid evacuation state lock and actual evacuation completion |
| `close_runtime_episode` / `settle_episode_evacuations` | State / original credit country | Preserved target identity, per-state actual pulse count, final episode loss, actual scheduled end validity | Episode aggregate, final evacuation evaluation, distinct successful state set | Normal cell/superstorm closure, global transition retirement, and final runtime closure |
| `check_runtime_capital_route` | Country | Real guarded capital and native railway connectivity from a different controlled railway state | Scheduled route row and rail-isolation disqualifier | Exposure checks and paid reroute completion |
| `check_runtime_country` | Country | Actual check date, preceding check date, active exposure, global phase, Preparedness, current capital/tier | Measured exposure days and global continuity rows, bounded deadline refresh | Host worker, exposure entry/departure bookkeeping, global transition |
| `record_aftermath_tier` | State | Current-generation state and actual stored tier | Tier-3 entry, original clock, bounded obligation row | Final aftermath assignment and paid recovery tier change |
| `record_dissipation_state_snapshot` | State | Generation, state ID, snapshot key/date, explicit OWNER core proof, positive actual aftermath tier | Frozen OWNER core list and 180-day recovery deadline | `acid_rain_finish_runtime`, after aftermath assignment |
| `record_recovery_completion` / `refresh_deadlines` | State / country | Actual mutated tier and stored immutable state clocks | Recovery/downgrade dates, recomputed resolved counts, mature disqualifiers | `acid_rain_apply_recovery_result`, relevant worker checks, transfers, deadline callback |
| `schedule_deadline` / `deadline_callback` | Country | Earliest pending frozen recovery/ruin date, generation and due-day receipts | One bounded hidden callback, no world scan or gameplay reward | Snapshot creation, tier-3 entry, obligation transfer, recovery refresh, `chaosx.nr33.41` |
| `record_acute_closure` / `evaluate` | Country | Natural closure, exact national death ledger, immutable baseline, actual tier-3 responsibility | One-time closure facts and ten permanent award writers | Natural `acid_rain_finish_runtime` country pass and relevant accepted achievement edges |
| `transfer_state_responsibility` | State | Current generation, real old/new controller targets, stored responsible ID, distinct new recipient | One responsibility move, original history retained, unresolved ruin clock moved without reset | `acid_rain_handle_state_control_change` |

Helper names in the table carry the common `acid_rain_033_achievement_` prefix.
All chain-local targets expire naturally.
No global achievement event target, central MCP router, or wrapper skill was added.
Stored country pointers and state rows carry generation evidence, and normal generation registration clears obsolete pointers.

## Mortality integrity

The achievement bridge assigns `acid_rain_033_input_applied_deaths` only from `state_civilian_population_loss_applied`.
It does not use the requested amount, prevented-death estimate, country manpower, `local_manpower`, attrition, or a forecast estimate.
The runtime reads state population immediately before and after the shared transaction.
If their difference differs from the shared applied result, `acid_rain_population_contract_fault` prevents achievement progress and marks the affected country migration-disqualified.
The three direct achievement death accumulators consume the same authoritative input for separate state, country, and severe ledgers.
The achievement file never calls the population-loss helper or Deaths registration itself.
There is one runtime population gateway and one achievement bridge inside its strictly increasing pulse-key branch.
Old A-B-A keys remain rejected by the existing `acid_rain_pulse_key_is_new` trigger.
Zero helper output remains zero, although an actual zero-loss exposure can legitimately establish touch/opening facts.
Helper output/result temporary variables are declared before the shared call so returned modifications survive the helper boundary.

Installed `add_manpower` documentation supports STATE and COUNTRY separately.
The offline Effects state section explicitly describes the state form as a total-population mutation and describes its recruitable-manpower side effect.
The shared transaction applies negative `add_manpower` in STATE scope, then reconciles observed owner/controller recruitable-manpower credit in COUNTRY scope.
Those country corrections are not mortality proof.
The state-population before/after comparison is the required proof predicate, and no observed execution of it was supplied by the orchestrator.

## Constants, bounds, and cleanup

Existing achievement tuning remains unchanged: 100/60/75 Preparedness, 60 global days, 120 exposure days, 0.05/0.10 percent strict casualty ceilings, and the existing 180-day response constant.
The new schema value is 2 in the achievement effects and triggers files.
The row-miss sentinel is -1 because index 0 is a valid row.
Superstorm episode IDs use the documented file-local offset 256 to separate them from severe-cell identities.
Paid action receipts use a generation-reset global action sequence so two different controllers' local action number cannot collide in one state's evacuation ledger.
Shelter and evacuation protection keys encode episode plus protection kind, so the two receipt families cannot collide.
The follow-up explicitly authorizes two fields in the existing shared `acid_rain_achievement` group: `severe_survival_death_numerator = 5` and `severe_survival_death_denominator = 10000`.
Shelters Held and Three Evacuations read the same ratio with pooled and per-state baselines respectively.
No new script-constants file or decision/AI tuning change was introduced.
Existing country/state, episode, visit, route, recovery, ruin, and receipt limits are enforced before append operations.
Duplicate gates precede capacity validation, including route checks, reroutes, snapshots, and state exposure.
An overflow fails closed rather than trimming historical achievement proof.
Array iterators replace numeric loops for potentially large achievement row sets.
Existing safe `for_each_scope_loop` weather traversals were retained.
Component arrays explicitly allocate index 0 padding plus component IDs 1 through 4.
Append-based summaries use row_count minus one for their new zero-based index.
The casualty ceilings divide the population baseline before multiplication, avoiding the old scaled-population multiplication.
Generation cleanup clears pending warning action arrays, current clocks, temporary associations, and current eligibility flags.
Permanent award receipts and debug/force/scenario/migration disqualifiers are retained.
Country and state schema/generation rejection prevents invented progress from unsupported old ledgers.

## Source evidence and route gaps

Live routes were discovered before use.
These accepted requests returned `timed out awaiting tools/call after 600s`:

- `hoi4.reference_context`, surface `event`, bounded achievement/population/target question.
- `hoi4.reference_search`, query `add_manpower`, sources `game_doc` and `wiki`, limit 4.
- `hoi4.event_inspect`, mode `trace`, selector `{ kind: event, eventId: chaosx.nr33.1 }`, downstream depth 2, nodes 20, edges 30.
- `hoi4.source_lookup`, symbol `acid_rain_033_achievement_record_runtime_pulse`, kind `scripted_effect`, `includeReferences = false`, one definition, 35 lines.

The first malformed event selectors were rejected before inspection and are not evidence.
No inspect, render, compare, source revision, graph artifact, or live scenario result was obtained.
Event rendering/comparison cannot be claimed on the basis of source assertions.
The connected source schema lacks `view` and `keyPath`, so no unsupported child-structure request was invented.
`hoi4.script_validate` is absent from the connected tool inventory.
Reference-read IDs could not be obtained because the reference discovery requests timed out.
The local sections below were read instead, as authorized for reference route gaps.

The repository base path is `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
The installed-game base path is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Revision identity is the SHA-256 of the local file bytes, not an MCP-issued revision.

| Source under its base path | Read lines/sections | SHA-256 |
| --- | --- | --- |
| Repo `paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263-335 event targets, 434-450 temporary variables/scopes, 1069-1214 zero-based arrays | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| Repo `paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 3358-3365 state population effect | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| Repo `paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 826-844 PREV scoping example | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| Repo `paradox_wiki\Event modding - Hearts of Iron 4 Wiki.md` | 145 triggered-event gates, 194-203 delayed event contract | `96327b896298420d84058394a44ed08be7eb518726b8f207b392fea71f05d43d` |
| Repo `paradox_wiki\Triggers - Hearts of Iron 4 Wiki.md` | 1867, 1961-1993 railway connection | `abc51ad18a2c46e46d47baa795c5a840ebaf7c4ae3e777426c64a9f4c0c0ce06` |
| Game `documentation\effects_documentation.md` | 1468-1476 `add_manpower`, 2943-2970 `country_event`, 4279-4335 array/numeric loops, 6496-6513 saved targets | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| Game `documentation\triggers_documentation.md` | 3844-3853 target existence, 4603-4648 railway connection/level, 6404-6426 meta trigger | `7d27ed77ddadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| Game `documentation\dynamic_variables_documentation.md` | 1168-1175 `state_population_k` | `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda` |
| Game `documentation\script_concept_documentation.md` | Script Constants, 216-264 | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| Game `common\script_constants\documentation.md` | Full schema/examples | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |

Vanilla precedent: `common\decisions\PHI.txt`, lines 2015-2033, scopes to ROOT country and passes state scope endpoints to `has_railway_connection`.
Vanilla `common\achievements.txt`, lines 3272-3285, supplies explicit state/level railway arguments.
The offline Localisation page's variable formatting and scripted-localisation sections, plus the comments and country-scoped example in vanilla `common\scripted_localisation\WTT_infiltration_localisation.txt`, were also read.
No dedicated installed scripted-localisation documentation file was found under the searched documentation and common/scripted_localisation directories.
Existing helpers `apply_exact_state_civilian_population_loss` and `apply_state_population_loss_without_recruitable_manpower_gain`, and their matching dynamic-effect markdown contracts, were reviewed before reusing the public gateway.

## Meaningful validation actually run

The existing `validate_033_acid_rain.py` `source_contract(repo_root)` was imported and run read-only with an explicit repository root.
It passed and reported one population gateway, monotonic per-state-generation deduplication, and ten generation-checked callbacks.
No weighted movement, AI, dissipation, or probability suite was run or changed.

A temporary read-only structural audit extracted actual named effect bodies and checked 24 caller-to-recorder edges, ten unique award writers, three exact-input death accumulators, and the deadline event/receiver linkage.
It also checked that the achievement ledger contains no extra population gateway or Deaths registration, that receipt gates precede capacity validation, and that permanent awards survive generation clearing.
The final source checks additionally passed global action-key uniqueness across controllers, distinct protection receipt domains, the direct paid-project generation guard, schema 2 consistency, and the one deadline-event definition.
The first permanent-receipt assertion accidentally matched internal state receipt flags as awards.
The assertion was narrowed to the ten declared achievement IDs and the corrected check passed.

The existing five-case mortality model was run: tiny-floor zero, protected-floor clamp, ordinary positive loss, dense-state positive loss, and zero request.
All model cases preserved equality between model population decrease and applied amount.
The model reported zero duplicate population losses, zero duplicate death records, and zero positive death records for zero-applied loss.
This is deterministic model evidence, not execution of the Clausewitz population transaction.

### Accepted threshold and launcher follow-up

The parent explicitly accepted the Three Evacuations ceiling on 2026-10-03 and supplied `acid_rain_launch_authorized` and `acid_rain_launch_forced` as the launcher protocol.
The accepted addendum and achievement prompt record that basis without retroactively inferring approval from the earlier unspecified threshold.
The completion wrapper derives `acid_rain_033_input_evacuation_threshold_people` from `acid_rain_033_input_evacuation_baseline_people`, divides by the shared denominator 10000, then multiplies by numerator 5.
It contains no threshold rounding and no current-population lookup or optional threshold override.
The existing per-state completion rows persist that fraction, and final episode settlement retains its strict less-than comparison against actual helper-applied severe deaths.
The two player-facing Three Evacuations keys state the per-state forecast-population denominator and final-episode condition.

Nine numeric boundary cases passed in the read-only model: population 1000000 with deaths 499, 500, and 501, population 10001 with deaths 5 and 6, population 3333 with deaths 1 and 2, and population 1000 with deaths 0 and 1.
The strict ceilings were 500, 5.0005, 1.6665, and 0.5 respectively.
A three-state case whose pooled total passed but whose small second state failed its individual ceiling was rejected for that state.
These are calculation/source checks, not observed engine variable-precision results.

Eight isolated executions of the parsed root flag branches passed: normal authorized start, forced start, both markers, unarmed console start, authorized CXT start, active normal generation with a forced duplicate marker, active forced generation with an authorized duplicate marker, and active forced generation with an unarmed duplicate.
Every case consumed both country markers.
Only new starts changed the durable global origin, forced dominated both markers, and active duplicates preserved the prior origin.
Both `begin_runtime_country` and `initialize_country` read the global origin, so late country ledgers inherit forced disqualification without a world scan.
The CXT debug marker remains separate.
The parent-owned arming block was inspected read-only at `common/scripted_effects/chaosx_settings_effects.txt`, lines 4344-4359, confirming that manual arming clears authorization and normal arming cannot override pending forced arming.

The current parent validator's `source_contract` was run read-only after the changes and passed.
No validator edits were made by this subagent, including the parent's mixed-Major, migration, and arming/provenance checks.
The committed `acid_rain_remove_legacy_missions`, `acid_rain_migrate_legacy_runtime`, and `acid_rain_adopt_legacy_coverage` bodies were compared against `f26768187` and matched after normalizing line endings.
The decision file and preparedness effect file retained SHA-256 `e72d281dabd6f699a4248062aec34817ed921c14f0de6b541531f4306d213679` and `cecbffdfc281fceca23af4764d3c3e1c3d276bc6257c4b9e04ba4143ddeb1c6a` through this follow-up.
The constants diff contains only the two accepted achievement fields and their two explanatory comments.
No cost, weight, random draw, or weather timer changed.

The follow-up repeated narrow live `source_lookup`, `reference_search` for Script Constants, and depth-1 `event_inspect` requests.
Each again returned `timed out awaiting tools/call after 600s`.
No new MCP artifact, source revision, or engine result was obtained.
The already cited installed constants documentation and offline flag sections were read locally for this change.

| Accepted follow-up source | SHA-256 |
| --- | --- |
| `common/scripted_effects/033_acid_rain_achievement_effects.txt` | `f1c3b600ec11ec414ead2f521e4f1c63cbc072f3bf67038958fff72224bf2c1e` |
| `common/script_constants/033_acid_rain_constants.txt` | `2ae19fa866a83b6626653b7a27c3024e6361e8b9532a901405b3d4d97d6a9425` |
| `events/033_acid_rain.txt` | `ce1973d0da2ac3c632c1249ee7f73aaf21e762f35561548aca770296e69c0774` |

## Proposed validator assertions after the parent releases its lock

The initial integration snapshot before the accepted threshold/launcher follow-up is listed below.
The shared runtime can receive further parent-owned migration changes after this snapshot.

| Source | SHA-256 |
| --- | --- |
| `common/scripted_effects/033_acid_rain_effects.txt` | `9bdfb2abfa1a29bea9fdf073026db787e2597295ee7b02aa0fe7f25da1fa8d53` |
| `common/scripted_effects/033_acid_rain_preparedness_effects.txt` | `cecbffdfc281fceca23af4764d3c3e1c3d276bc6257c4b9e04ba4143ddeb1c6a` |
| `common/scripted_effects/033_acid_rain_achievement_effects.txt` | `2a79111dec8b8e75423263eea77ffe8d5cf65e584f6114a38f297d1631889482` |
| `common/scripted_triggers/033_acid_rain_achievement_triggers.txt` | `cbe812415686c463544a1f598a8476fea6c6d5f4ed82ef0a2b250e7f221a4de5` |
| `events/033_acid_rain.txt` | `231f38c756ec4ad69350626c11e0a740487f90a97d15446ddb906ab3dbdb4b04` |

These are proposed task-specific assertions, not claims that engine scenarios were executed:

1. Extract each actual named source block with a brace-aware parser that ignores comments and quoted text.
Assert the 24 direct edges in the helper table in their owning blocks, rather than accepting recorder names anywhere in a file or in comments.
Assert root event 1 reaches formation registration, worker event 20 reaches country checks, and event 41 reaches deadline settlement.
2. Assert the mortality gateway has one shared population-helper call and one achievement bridge, both inside the new-key branch.
Assert every required population input is assigned before the gateway, returned applied/result variables are predeclared, and the achievement death input is assigned exactly from `state_civilian_population_loss_applied`.
Reject requested-death and prevented-death substitutes, direct Deaths calls from achievements, and progress after a population contract fault.
3. Execute deterministic recorder fixtures for applied zero, positive loss, floor clamp, duplicate A, new B, old A, and duplicate at a full ledger.
Require one state/country/severe update per accepted packet, unchanged counters on replay, and zero death progress for zero output.
The current synthetic mortality model alone does not execute these recorder branches.
4. Test all ten criteria with exact boundary packets: 99.999/100 preparation, three states with one versus two episode pulses, shelter death ceiling equality, three distinct evacuations versus repeated state ID, 119/120 exposure days, two/three reroutes, 74.999/75 global preparation, 59/60 consecutive days, 0.10 percent death-ceiling equality, nine/ten starting factories, and one/two distinct warning regions and visits.
5. Read the explicitly accepted 5/10000 fields and test final per-state losses below, equal to, and above the ceiling.
Include fractional ceilings without rounding, such as population 10001 producing 5.0005 people, where five deaths pass and six fail.
Include a pooled total that passes while one state fails its own ceiling, and require that state to remain uncounted.
Malformed zero-baseline/zero-threshold historical packets remain integrity failures, while new valid forecast packets must receive a positive calculated ceiling.
6. Assert component arrays allocate all four managed indexes, zero-based appended row 0 is processed, new summary index equals row_count minus one, and every aligned append group has equal lengths.
Include cap-minus-one, cap, duplicate-at-cap, and over-cap packets without shortening history.
7. Test schema 1 rejection, schema 2 initialization, duplicate same-generation begin, a newer generation, and stale generation packets.
Require immutable formation population/factories and preserved permanent award receipts.
8. Exercise exact warning/visit/action identities, start before warning, start after arrival, completion at arrival, completion before actual arrival, delayed arrival, pending-action cancellation, and two simultaneous warnings.
One action must not satisfy two different regions.
9. Test natural versus administrative closure, owned-core snapshot under a distinct controller, controller transfer before and after a deadline, repeat transfer, annexed recipient, and capital identity changes.
No transfer may reset a tier-3 clock or transfer historical national deaths.
Include two countries whose local action sequence has the same value, plus shelter and evacuation in one episode, and require distinct receipt domains.
10. Test recovery at day 179, day 180, and day 181, ruin downgrade at age 179 and 180, a callback after weather has ended, repeated callbacks, and an obsolete callback during a second generation.
Recovery is inclusive through day 180, while a tier-3 downgrade must precede age 180.
11. Use explicit native route scenarios for a connected capital, no eligible railway endpoint, enemy-controlled intermediary, severed route, repaired route, and moved capital.
Require supplied engine evidence that the native connection predicate handles damaged or interrupted railway segments before claiming the operational-route condition.
12. Test independent and cluster launches as eligible, and forced settings/CXT/debug/direct scenario launches as disqualified with a persisted launch-origin receipt.
Assert both root markers are consumed on every entry, only an inactive/new runtime entry can change `acid_rain_forced_generation`, forced dominates both markers, CXT remains forced, and every initialized country reads the durable flag.
The parent owns the dispatcher arming/provenance validator checks.

## Simplifications, omissions, and blockers

No alternate casualty threshold, shortened achievement condition, modifier-only mortality, free preparation tier, or fabricated engine proof was substituted.
The numeric-threshold and temporary-launch-provenance blockers are resolved in source by the explicitly accepted ratio and durable root protocol.
The old optional threshold variable and temporary manual-trigger check have been removed from the completion and formation wrappers.
The parent confirms that accepted-dispatch marker arming has landed in `chaosx_settings_effects.txt`, with manual/forced requests dominating queued normal requests.
The root consumes those markers after its origin snapshot, and both formation and later country achievement initialization inherit `acid_rain_forced_generation`.
End-to-end dispatcher/receiver behavior still needs supplied engine evidence, and the parent retains the arming/provenance validator checks.

The complete acceptance goal remains limited by:

- Native railway semantics for damaged routes and delivered supply.
The implemented check proves the native engine connection predicate, with allied-route restriction, rather than a documented physical supply-delivery or damaged-segment result.
- Missing MCP inspect/render/compare/source artifacts because the connected requests timed out.
- Missing supplied orchestrator evidence for real population reduction, all ten positive/negative runtime award cases, reload, tag switch, controller/capital changes, deadline delivery, and second generation.
The agent did not launch HOI4.

Event Details presentation, hidden-achievement reveal state, asset registrations, achievement icons, and shared launch/test hooks remain parent-owned.
The runtime's existing aftermath policy creates most stored aftermath at final closure.
Consequently, a capital-tier check during the global layer has only the stored tiers supplied by that policy.
This integration does not redesign when the weather system creates aftermath.
The parent should review that limitation against Part 4's aftermath-on-departure contract.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`.
No skills were created or changed.
