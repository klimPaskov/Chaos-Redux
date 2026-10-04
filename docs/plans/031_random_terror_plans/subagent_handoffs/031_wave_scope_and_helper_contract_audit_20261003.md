# Event 031 wave scope and helper contract audit

Date: 2026-10-03.
Disposition: source contract audit implemented, MCP event and probability evidence blocked.
Authority: the parent requested a bounded read-only audit and this one documentation artifact, with no gameplay edits or commits.
The shared working tree contains parent and other-agent changes and was preserved.
The terminal-role patch and final classification are parent-owned and excluded.
Commit `04689ecb13f203945be130d461fdf4eb957c043b` already preserves wave-count and CXT helper outputs and is not proposed again.

## Findings and evidenced scope rule

**ROOT remains the receiving country of `chaosx.nr31.1`, while THIS changes to each selected country and state.**
Calling an ordinary scripted effect or scripted trigger does not establish a new event ROOT or add a country/state scope transition.
The offline wiki defines event ROOT as the country receiving the event, THIS as the current scope, and PREV as the enclosing scope (`Scopes`, lines 260-263).
It defines scripted effects and triggers as shortened invocations of their bodies (`Effects`, lines 4683-4695, and `Triggers`, lines 2359-2395).
The installed trigger documentation permits ROOT and PREV as country targets of state ownership/control tests, but does not contain a general scripted-helper rerooting specification.
The preserved ROOT contract is corroborated by two exact installed vanilla precedents rather than an assumption that a helper starts a new root:

- `events/WTT_Germany.txt`, lines 3919-3944: event `wtt_germany.71` checks `tag = AUS`, enters `HUN`, and calls `ROOT_inherit_current_scope_wars_effect`.
  `common/scripted_effects/00_scripted_effects.txt`, lines 109-124: the helper iterates enemies of PREV, the invocation country HUN, and makes ROOT inherit their wars.
  Rerooting at the helper would make Hungary inherit its own wars instead of the Austrian event receiver inheriting Hungary's wars.
- `events/BBA_ItaloEthiopianWar.txt`, lines 697-726: a country-event option enters state 838 and calls `is_controlled_by_ROOT_or_ally`.
  `common/scripted_triggers/00_scripted_triggers.txt`, lines 308-319: this state helper enters CONTROLLER and compares the controller to country ROOT.
  Rerooting at the helper would incorrectly make ROOT a state.

This is documentation and installed-source contract evidence, not a live execution test or an MCP result.
The installed documentation's `script_concept_documentation.md`, lines 151-154, contains a TODO for scope-accessor documentation rather than the missing general rule.
`documentation/scopes_documentation.md` does not exist in this installation.

### Consequence for the automatic wave

Let R be the entry-event country and C a candidate country.
In `random_terror_country_is_normal_target`, `any_owned_state` enters a state owned by C, but line 65 asks whether R controls it.
`random_terror_country_has_valid_state` repeats that mistaken comparison at line 98, then calls a state predicate whose lines 82-83 compare ownership/control with R again.
Country C can therefore qualify only through an owned state controlled by R.
After selecting C, `random_owned_controlled_state` restricts the draw to states both owned and controlled by C, as expressly documented in installed effects lines 5512-5519.
The state predicate at effects line 1026 still requires ownership or control by R.
For distinct R and C, an ordinarily owned-and-controlled C state cannot satisfy that final test.
Thus the current contract suppresses incidents outside R even when occupied C states allowed C into the ticket pool.
Such a failed selection still reserves C before discovering that no state can be selected, so it consumes a loop attempt without increasing the affected count.
An R that is ineligible can yield a completely empty wave, and a normal eligible R can receive at most one successful country selection while its reservation is honored.
These conclusions assume the documented scope and iterator rules, not measured campaign probabilities.

## Complete direct caller map for the audited predicates

References below use `E` for `common/scripted_effects/031_random_terror_effects.txt` and `T` for `common/scripted_triggers/031_random_terror_triggers.txt`.
The literal-call inventory covered `common`, `events`, and `interface` with `.txt`, `.gui`, and `.gfx` source files.
No GUI or focus consumer of these predicate names was found.
Dynamic token construction is not proven absent by this literal inventory.

| Predicate and caller | THIS and enclosing scope | ROOT and actual contract | Bounded recommendation |
| --- | --- | --- | --- |
| `country_is_normal_target`, T117 inside `country_is_eligible_wave_target` | Candidate C, then C's `any_owned_state` | Entry R, selected-country eligibility | Change only the country helper's line 65 comparison to PREV, which is C inside that iterator |
| `country_is_normal_target`, T317 inside `scenario_candidate_country` | C from `every_country` at E1206-1209 and E1361-1364 | Scenario initiating country, unless an actual recipient event established another ROOT | Same country-local PREV relationship, retain the scenario OR branches and guards |
| `country_is_normal_target`, T336 inside `scenario_actor_parent` | Owner C reached from `scenario_actor_state` T350 | Scenario initiating country, the preceding state is not ROOT | Inside C's own `any_owned_state`, PREV is C, so the same local correction applies |
| `country_has_valid_state`, T118 inside `country_is_eligible_wave_target` | C, then its owned state | R, needs a state C can actually use | Change line 98 to PREV and use intrinsic state checks, not an additional ROOT relationship |
| `country_is_eligible_wave_target`, E1016 | C from `every_country` | R is `chaosx.nr31.1` receiver | Candidate predicate must be country-local |
| `country_is_eligible_wave_target`, T132 inside `event_pool_available` | C from `any_country` during dispatch eligibility | Current initiating event/effect root | Must answer whether any valid candidate exists, not whether R controls foreign-owned land |
| `country_is_eligible_wave_target`, T303 inside `can_launch_global_jihad` | C from `any_country` | Launch-context ROOT | Same country-local predicate contract, no terminal classification recommendation |
| `state_is_valid_target`, T99 inside `country_has_valid_state` | C-owned state, PREV C | R | Use intrinsic state checks plus the enclosing iterator's `is_controlled_by = PREV` |
| `state_is_valid_target`, E1026 in automatic selection | C-owned-and-controlled state, PREV C | R | Use intrinsic state checks, ownership/control is established by the iterator |
| `state_is_valid_target`, E1328 in `scenario_seed_country` | C-owned-and-controlled state, PREV C | Scenario ROOT | Same intrinsic state check, preserve scenario behavior elsewhere |
| `state_is_valid_target`, T258 in `action_target_is_valid` | FROM state, enclosing current country | Intended decision/event owner as ROOT | Preserve the explicit ROOT relationship here unless a concrete consumer proves another contract |

`random_terror_action_target_is_valid` has no literal consumer in the searched gameplay surfaces.
Its unused status is not authority to remove or change it.
`event_pool_available` is called by `can_prepare_dispatch` at T140, which is called by `prepare_dispatch` at E2536.
The dispatch caller in `chaosx_settings_effects.txt`, lines 4315-4328, correctly initializes `random_terror_prefire_ready` before calling the helper.
OWNER is not a universal replacement: `is_owned_by = OWNER` is a tautology in a state and would weaken the original action-owner restriction.
PREV is safe only where the preceding actual scope is the selected country, not because a helper was entered.

## Proposed narrow helper map and migration

These are owner patch recommendations, not implemented gameplay or accepted balance changes.

| Helper | Scope | Inputs and outputs | Side effects and call sites |
| --- | --- | --- | --- |
| Proposed `random_terror_state_is_eligible_incident_site` | State | Reads population, cooldown/date, and lost-control state flag, returns boolean | No mutation, no country relationship. Extract T75-80. Use in T99, E1026 and E1328 |
| Existing `random_terror_state_is_valid_target` | State in an owner-rooted action contract | Calls the intrinsic helper and retains owned-by-ROOT or controlled-by-ROOT | No mutation. Keep T258's contract intact |
| Existing `random_terror_country_is_normal_target` | Candidate country | Existing guards, one positive-population off-cooldown owned state controlled by this candidate | No mutation. Inside its `any_owned_state`, use PREV at T65. Do not silently add the lost-control guard to this helper, which currently lacks it |
| Existing `random_terror_country_has_valid_state` | Candidate country | Owned state controlled by PREV and intrinsic eligibility | No mutation. Existing T118 consumer remains |
| Existing `random_terror_add_current_country_to_wave_target_pool` | Candidate country | Base weight one, returns entries in caller-owned temporary pool | Adds repeated C scope tickets. Both E1017 and E1363 remain direct consumers |
| Existing two shared adjustment entry points | Candidate country | Base input, caller-owned adjusted weight output, current-provider exclusion policy | Temporary arithmetic only. Initialize forwarded output before private worker, document caller storage |
| Existing `individual_crisis_apply_candidate_ticket_curve` | Candidate country | Base/exclusion inputs, adjusted output, private caller-owned active-load scratch | Initialize active load before its scripted-trigger call at line 38 |

Migration order: preserve exact before sources and scenarios, obtain baseline audit, introduce the intrinsic predicate and change only mapped relationships, repair temporary output ownership, review reservations and failed state draws, then obtain the probability auditor's comparison against the same fixtures.
Update the shared helper Markdown example and API text in the same owner patch.
Document the new state predicate's scope and lack of ownership semantics in the Event 031 helper documentation.
No new central router, wrapper skill, broad redesign, or helper without consumed call sites is needed.

## Temporary helper-return contract

Offline `Data structures`, lines 435-442, explicitly warns that temporary variables first created inside scripted effects/triggers may disappear after return, while variables created by the caller survive and retain modifications.
This is a documented lifetime risk, not proof that every current call fails in every engine build.
The events skill's Helper output lifetime section requires ownership at every consumed or forwarded boundary.

| Storage | Current boundary and receipt | Required ownership |
| --- | --- | --- |
| `random_terror_wave_target_count` | E1038-1040 precedes count resolver | Already fixed by parent, no repeat patch |
| `random_terror_prefire_ready` | settings E4317 precedes `prepare_dispatch` | Already initialized, no patch |
| `individual_crisis_candidate_base_weight` | E997 precedes public ticket helper | Already initialized to one, retain |
| `individual_crisis_candidate_adjusted_weight` | E1000/E1003 public helper, read at E1005. First created inside private curve lines 28-30 | Initialize to zero in the Event31 adder before either public call. Each public entry point must also own its forwarded output before invoking the private worker |
| `individual_crisis_active_load` | Private curve line 38 calls load trigger. Trigger line 15 creates it, curve lines 43/58 read it after return | Initialize to zero in the private curve before evaluating the scripted trigger. Standalone cap callers that consume only its boolean do not require this returned scalar |
| `individual_crisis_exclude_random_terror` | Public entries set zero/one before worker and reset zero afterwards | Existing input initialization is present. Retain zero restoration, including cap failure |
| `random_terror_wave_country_pool` | Selectors E1014 and E1360 clear it before nested adder creates entries, selectors consume it afterwards | Pool belongs to each selector, not the nested adder. Existing clear-before-call pattern is present. Installed `clear_temp_array` docs promise clearing contents, not allocation or scripted-return lifetime, so empty-array creation semantics remain unproven |
| `random_terror_wave_pool_remaining` | E1005-E1009 reads and consumes it within the adder | Local scratch, no outer return initialization needed |
| `random_terror_resolved_evolution` | E930 calls identifier helper, E932 consumes output. Identifier first assigns it at E706 | Additional opening-path return risk. Initialize zero in `random_terror_resolve_evolution` immediately before the identifier call, without redoing the fixed count output |

For the pool, an owner can explicitly create a harmless temporary entry in the selector and then clear it before calling the adder, so storage has demonstrably been introduced in the caller and no sentinel enters the final draw.
Use a verified repo/vanilla pattern or an actual-source conservative frame-lifetime check rather than claiming that the current clear operation fails.
The outer wave caller need not own the pool when it never reads it after the selector returns.
Likewise `random_terror_apply_incident` consumes its incident type inside its own body, so that field is not a selector-return output.

The exact-state loss wrapper sets its inputs before invoking the shared state helper at E379-386 and does not consume `state_civilian_population_loss_applied` or `state_civilian_population_loss_result` after return.
Its major-loss receipt at E388-392 uses requested casualties instead of the shared helper's measured applied loss.
If that receipt is intended to prove actual losses, the owner must initialize both output fields before the shared call and base the receipt on applied loss.
This is an adjacent bounded accounting finding, separate from weighted targeting, and no casualty change was made here.

## Actual source ticket inputs and protected identity

Event31's base candidate weight is exactly one for every candidate at E997.
Neither state population nor a population cohort size multiplies that base.
Positive state population is an eligibility test, not a country ticket multiplier.
Each candidate is repeated in the temporary scope pool once per adjusted whole ticket at E1006-1009.

| Effective other-provider load | Shared cap result | Source ticket count with base one | Relative factor |
| --- | --- | --- | --- |
| 0 | Below 3 | 4 | 1.00 |
| 1 | Below 3 | 2 | 0.50 |
| 2 | Below 3 | 1 | 0.25 |
| 3 or more | Rejected | 0 | 0 |

For an existing Event31 package, the existing-provider entry point excludes exactly its own one provider contribution and counts other active providers.
Two or more active Event31 states do not contribute multiple slots because the provider predicate returns one boolean.
The eligible-wave predicate lets an active Event31 package bypass its initial cap branch, but ticket construction still rejects three or more other providers.
Thus bypassing the initial cap is not unlimited targeting weight.
A country at ordinary total load three because it owns Event31 plus two other providers has effective load two and one ticket.

The shared load trigger counts fourteen provider lifecycle markers, not fourteen demographic cohorts.
The direct curve has no religion, ethnicity, nationality, refugee status, ordinary ideology, population-share, or recruitment inputs.
Increasing counted provider load can only reduce its ticket count under the intended curve.
The current scope/return defects prevent treating this arithmetic as verified realized probabilities.
The evidence pass was delegated to `chaosx_ai_probability_auditor` as agent `01a101b3-5a39-7b33-890d-0cc22aabeefc`, without inherited context and with read-only authority.
It did not return findings during bounded completion checks or after a request to stop further inspection and return its current evidence.
The agent was closed while its reported status was `running` so the architecture handoff would not stall indefinitely.
No auditor result, completed transitive identity review, or probability artifact is claimed.
The fourteen-provider closure and shared special-country classification require an auditor follow-up before asserting full identity invariance across transitive dependencies.
The direct shared-curve and Event31 base-input observations above are architect source findings only.
No balance target or AI weight was chosen or changed.

## One global firing, exact-state application, and cleanup

`events/031_terrorist_attack.txt`, lines 22-51, has one hidden entry event that calls the global wave once.
The fixed count resolver selects 3/5/7/10/15/20 loop attempts for baseline/organized/transnational/territorial/jihadist/final tiers (`031_random_terror_constants.txt`, lines 264-269), with a scenario override at E987-993.
Installed `for_loop_effect` docs, lines 4318-4324, make the default endpoint exclusive, so start zero and end N give N attempts rather than N+1.
It should yield up to N distinct valid countries when enough candidates and valid sites remain.
Insufficient eligible candidates must yield a bounded partial wave with its actual affected count, not fabricated incidents.

The exact selected state is saved as regular `random_terror_current_state` at E404, gets its own cooldown at E405, state mutations occur there, and country effects/report delivery use CONTROLLER at E653-679.
Because the selector uses owned-and-controlled states, OWNER, CONTROLLER, and candidate C coincide at initial incident application.
Those OWNER/CONTROLLER references are correct and do not need blanket ROOT substitution.
Regular targets auto-expire with the effect chain and carry to scheduled child events, as documented in offline Data structures lines 303-316.
Do not add a global target for this synchronous selection.
The existing dispatch host is global at E2542 and has explicit cleanup at E2547-2550, invoked through the scheduled receiver's cleanup path.
The selected pool is cleared at E1031 and E1373, the exclusion scratch is reset by both shared wrappers, and each iteration rebuilds candidate eligibility.

The selector reserves C before incident application at E1023-1024, preventing repeat country picks while that reservation lasts.
Move commitment after a successful valid state selection, or return a caller-owned success receipt and undo a reservation when no state was applied.
Also revalidate country eligibility in the final `random_scope_in_array.limit` if an intervening action could invalidate the candidate.
The current reservation's `days = random_terror_target_reservation_duration` is an unsupported-field concern: the events skill says timed country-flag days reject variable tokens, the wiki documents an integer, and installed `set_country_flag` docs do not resolve the argument semantics.
Use a documentation-backed literal injection or mirrored file-local constant for this fixed cooldown in the owner patch, then include distinct-country selection in auditor scenarios.
This audit did not establish a runtime token error.

At E680 and E683, incident totals and automatic-wave affected payload count successful applications, not pacing firings.
The generic settings dispatch at `chaosx_settings_effects.txt`, lines 4482-4507, queues the one root event and invokes its type handler once.
`chaosx_logic_effects.txt`, lines 1205-1246, contains the repeatable handler's single pacing path.
The root records automatic-wave system history through E3550-3563 with a one-shot flag, after children have been selected, and `.2` report events do not invoke pacing.
Preserve this distinction, do not add pacing to each country or report, and do not add periodic world iteration.

## Required owner snapshots and probability fixtures

No snapshot is created by this docs-only audit.
The paths below are proposed destinations, not existing evidence or valid `before.path` inputs yet.
Before weighted eligibility/return corrections, the owner must byte-copy the actual worktree sources, hash the physical copies, and give the auditor those real paths.
The existing terminal-role fixtures are for another parent-owned patch and cannot stand in for a wave baseline.

Proposed root: `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux/docs/plans/031_random_terror_plans/evidence/wave_scope_before_20261003/`.

Preserve at least these paths beneath it, retaining their relative directories:

- `common/scripted_effects/031_random_terror_effects.txt`.
- `common/scripted_triggers/031_random_terror_triggers.txt`.
- `common/scripted_effects/individual_crisis_targeting_effects.txt`.
- `common/scripted_triggers/individual_crisis_targeting_triggers.txt`.
- `common/script_constants/individual_crisis_targeting_constants.txt`.
- `common/script_constants/031_random_terror_constants.txt`.
- `events/031_terrorist_attack.txt`.
- Any transitive provider predicate or classification file actually altered by the owner patch, plus their resolved pre-edit definitions or a frozen source manifest.

Proposed fixture: `docs/plans/031_random_terror_plans/evidence/031_wave_scope_probability_scenarios_20261003.json`.
These are semantic requirements for the live schema, not invented MCP argument keys.
Save the exact serialized fixture and its SHA-256, using only the installed route's accepted fields.
Start with `hoi4.probability_inspect`, then the auditor owns baseline evaluation and matching `hoi4.probability_compare`.
Pass real `before.path` and `after.path` objects under the same named `scenarioSet`, retain hashes separately, and never compare current source with itself.
Freeze dependent source resolution too, so a before file cannot silently expand current post-edit helpers.

| Scenario IDs | Required fixture inputs and useful assertions |
| --- | --- |
| `wave_three_countries_root_a`, `wave_root_ineligible` | R=A, complete A/B/C country pool with owned-and-controlled populated states, no cooldown or lost-control, live country guards, load zero, baseline count three. Repeat with ineligible/stateless R. Corrected draws can apply exact B/C states independently of R |
| `wave_foreign_owned_root_occupied` | B owns one A-controlled state and another B-controlled state, explicit owners/controllers. Before predicates can admit B but final state draw fails. Corrected predicates/draw must agree on B's own controlled site |
| `wave_load_0_1_2_3`, `wave_existing_provider_exclusion` | All fourteen authoritative provider booleans, base one, own Event31 package zero/one, effective loads 0/1/2/3. Verify 4/2/1/0 source tickets and exactly-one self exclusion |
| `wave_helper_return_frames` | Begin with no adjusted-weight/load/pool storage and model conservative cleanup at each helper return. Repeat with caller-owned storage. Include consecutive candidates at different loads to catch stale reuse |
| `wave_identity_invariance` | Paired candidates with identical state/control/population, provider markers, pressure, capacity, cooldowns and guards. Vary only religion, ethnicity, nationality, refugee status or ordinary ideology. No resulting positive ticket or recruitment delta attributable to those identity inputs |
| `wave_population_cohort_invariance` | Different positive populations and demographic cohort sizes, identical mechanical/provider eligibility. Candidate base remains one. A zero-population state is separately ineligible |
| `wave_site_rejections`, `wave_short_pool` | Expired/current cooldown boundary, zero population, lost local control, actor/nonhuman/special country, reserved country, three-other-provider cap, fewer valid countries than requested. Count actual successful sites and do not reserve failed sites |
| `wave_distinct_countries_once_pacing` | Full pool and fixed tier count, seeded draws where supported, reservation visibility across draws, success payload, automatic history receipt and one root pacing call. A complete sequence manifest must declare removals, reservation expiry, cadence, resets and terminal guards before a sequence claim |
| `wave_scenario_shared_callers` | Scenario host differs from C, both preflight and seed paths, capital/noncapital branch, extra-state and actor-parent scopes. Check the same pool-adder output contract without redesigning scenario content |

## MCP route blockers and validation limits

The connected `ALL_TOOLS` inventory exposes no `mcp__hoi4_agent_tools__hoi4_*` tools and no tool-search route that can discover them.
Therefore `hoi4.reference_context`, `hoi4.reference_search`, `hoi4.reference_read`, `hoi4.source_lookup`, `hoi4.event_inspect`, `hoi4.event_render`, `hoi4.event_compare`, `hoi4.probability_inspect`, `hoi4.probability_evaluate`, `hoi4.probability_sweep`, `hoi4.probability_compare`, and `hoi4.script_validate` are not callable in this session.
This is absent tool exposure, not a timeout or proven service-health failure, so a narrow retry cannot be issued.
No cached artifact is presented as a successful live inspection, no MCP revision or artifact URI was generated, and helper-expansion/task negotiation was not attempted.
Relevant local sections were read directly with path, line, and SHA-256 receipts below, as permitted for reference-route gaps.
Source review remains separate from blocked MCP engine evidence.

Meaningful completed checks: exact installed vanilla cross-scope precedents, complete direct predicate-caller inventory, state eligibility versus final iterator consistency, nested temporary-output ownership, tier counts versus exclusive loop endpoint, shared load/ticket arithmetic and provider self exclusion, exact-state versus controller attribution, and root versus child pacing/history paths.
Skipped or blocked: MCP event helper closure/render/compare, MCP probability baseline/evaluation/compare, a returned probability-auditor evidence pass and completed transitive identity review, realized candidate shares, seeded multi-draw/sequence validation, native timed-flag argument validation, empty temporary-array allocation semantics, live execution and recruitment outcomes outside this bounded selection chain.
The user owns live-game validation and no HOI4 launch or log search was performed.
No gameplay, AI, constants, localization, helper documentation, call sites, or cleanup source was changed.
No commits were created.
The only file added is this handoff.
No gameplay simplification or fallback was implemented.

## Source receipts

All relative paths resolve beneath `C:/Users/klimp/OneDrive/Documents/Paradox Interactive/Hearts of Iron IV/mod/chaos_redux`.
Installed paths below resolve beneath `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV`.
SHA-256 identifies the bytes read in the shared worktree, not an immutable before snapshot or a service revision.
Parent changes can legitimately make a later whole-file hash differ, especially the terminal-role files.
On final recheck the Event031 effects file hash was `8EDD15C352B0B4A8143B7A391078B5B6C0A01A41FE64FEA73CC86CED7B68B37A` rather than the earlier receipt below.
The complete audited wave lines 980-1054 were reread and unchanged, the audited helper declarations and state-predicate caller line locations were unchanged, and the Event031 trigger plus shared ticket trigger/effect hashes in the final targeted check retained their recorded values.
This concurrent source change is preserved and cannot be treated as a frozen baseline.
The `.99` cleanup receiver was also read at `events/031_terrorist_attack.txt`, lines 458-466, confirming its direct `random_terror_dispatch_cleanup` invocation.

| Path | Read sections | SHA-256 |
| --- | --- | --- |
| `common/scripted_effects/031_random_terror_effects.txt` | 271-365, 378-703, 705-706, 922-941, 980-1054, 1199-1244, 1308-1414, 2531-2551, 3550-3563 | `9BEA6830C2A39395F35BB50CE0ABA8B0098326638AB31319790037E5B9FAED70` |
| `common/scripted_triggers/031_random_terror_triggers.txt` | 53-141, 256-260, 281-355 | `3848A99005E8111A45B4BD49EF9C0821ACCD0C41029AAA5B1440182A685089C7` |
| `events/031_terrorist_attack.txt` | 22-65 | `8EA0D99D25C62DE0A4BE6F8D9A64CD827E7F575E158A01C6832A038B84C311BE` |
| `common/scripted_effects/individual_crisis_targeting_effects.txt` | 1-79 | `903562C1DC27BF9367E5A8AB8A807047A798FB16DE0BD8E1DF2841B6A2C40B16` |
| `common/scripted_triggers/individual_crisis_targeting_triggers.txt` | 1-118 | `AF537F93E969948CA5CB35E1D06C504F6797CCBAAF659A13C9A661DB8E510B70` |
| `common/script_constants/individual_crisis_targeting_constants.txt` | 8-23 | `8B4471A8412E3A883570743E0EE17037129DCEAA889D63781AC8FC2C3529E002` |
| `common/scripted_effects/individual_crisis_targeting_effects.md` | Complete API and example | `014ABB19AEF88D1821A10EC63BA16BE0A35A96B85D5B65B5A1B27DC0F62B8155` |
| `common/script_constants/031_random_terror_constants.txt` | 264-270 | `84AECCA5BE338433A9A9BF2BFBA5682BE8256D790A6940E1C5561D7705EA09B8` |
| `common/scripted_effects/chaosx_settings_effects.txt` | 4315-4328, 4482-4507 | `12090796F3234663EAD13AD3B755DB683947440C37592A910239115529C59A29` |
| `common/scripted_effects/chaosx_logic_effects.txt` | 1205-1246 | `C28EE6EAB4A2CEEA866C81CFFD6488E04A0B9D9ED509F650CFDDCC3F49B7548E` |
| `common/scripted_effects/chaosx_dynamic_effects.txt` | 49-60, 629-665 | `8B4DB4F595A607D041D0F072DE65DD906CDB10C40246690F78D3E4305DAB4D49` |
| `common/scripted_effects/chaosx_dynamic_effects.md` | 47-83, 261-283 | `AAF32BEB1ADAC49DFBB1AEFA4AFA274571E35B6DBACD4C302DA661EA1DB0DE39` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md` | 260-263, 388, 811-813 | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` | 213-223, 263-275, 303-324, 435-447, 1088, 1217-1220 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md` | 897, 4683-4730 | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md` | 2359-2400 | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| Installed `documentation/effects_documentation.md` | 2312-2325, 2733-2740, 2763-2771, 2943-2964, 4312-4329, 5512-5519, 5558-5571, 6496-6512, 6730-6737, 7820-7839 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed `documentation/triggers_documentation.md` | 1612-1619, 3844-3851, 5006-5013, 5381-5388, 6088-6095 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `documentation/script_concept_documentation.md` | 151-154, 216-245 | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Installed `common/script_constants/documentation.md` | Complete schema, support rule and examples | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| Installed `common/scripted_effects/00_scripted_effects.txt` | 1-17, 109-124 | `93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF` |
| Installed `common/scripted_triggers/00_scripted_triggers.txt` | 308-319 | `C8470B1937095F1AEC1C09EE78365D770FAB1AA7E28EB21D35924CA1253DD1DB` |
| Installed `events/WTT_Germany.txt` | 3919-3944 | `C7C16433A917B69CF20964833202DCAEBB7DD3118D6E4C89CCA9A1471E36D073` |
| Installed `events/BBA_ItaloEthiopianWar.txt` | 697-726 | `D301769E560A9CD1C6301D265E784E641819B29C009580B2DD4994C55067B179` |

Skills used and completely read: `chaos-redux-events` and `chaos-redux-subagents`.
No skills were created or updated.
No decision, focus, GUI, or map helper design was undertaken beyond documenting the unused action predicate's existing ROOT contract.
