# Decision and Mission Cleanup Baseline, 2026-08-22

## Status and constraints

This is a read-only baseline audit of shared decision and mission systems and event-owned decision surfaces for Events 1 through 20. Event 21 and later content was inspected only where it participates in shared decision infrastructure, target helpers, GUI registries, or localisation.

No decision, mission, scripted effect, scripted trigger, scripted localisation, localisation, scripted GUI, interface, GUI asset, or weighted field was changed. This report is the only file written by this pass.

The GUI constraint is absolute. Functional selectors, content gates, toggles, and scripted-GUI bindings remain valid inspection or future cleanup surfaces, but no recommendation in this report requires edits to `interface/*.gui`, visual layout, coordinates, click regions, or GUI assets.

## Required references and method

The audit followed `AGENTS.md`, `docs/plans/repo_cleanup/chaos_redux_repo_cleanup_master_prompt.md`, `chaos-redux-decisions-missions`, `chaos-redux-events`, and `chaos-redux-subagents`. The offline Paradox wiki pages consulted were Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.

The installed vanilla documentation consulted included `documentation/script_concept_documentation.md`, `common/script_constants/documentation.md`, `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, `documentation/loc_formatter_documentation.md`, and `documentation/loc_objects_documentation.md`. `common/decisions/AFG.txt` was used as a vanilla targeted-decision and mission precedent, including `target_root_trigger`, `target_trigger`, `custom_cost_trigger`, `custom_cost_text`, negative payment in `complete_effect`, and cleanup in `cancel_effect`.

The source inventory covered 132 files under `common/decisions`, with 124 shared or Event 1-20 decision files after excluding Event 21 and later event-owned files. The parser found 3,382 decision or mission blocks in scope and no duplicate decision identifiers across those files. Counts below are source-block counts, not proof that every block is simultaneously visible or active in a save.

The audit specifically scanned category ownership and fragmentation, decision and mission lifecycle fields, target selectors, custom cost lanes, payment helpers, texticon usage, scripted-GUI references, localisation keys, cleanup targets, and weighted fields. It also checked for duplicate IDs, missing mission terminal paths, and repeated helper or constant families.

## MCP evidence and exact blockers

The global read-only GUI inspection completed in workspace `mod_chaos_redux_ea3b2d67c2c0` and returned:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2fcf4d171043f7bd5a8dd74de9652dd786f62543e9f6082fdb064c0468d40d21/9a860cafd6ed75c095a6ab0bc57fe767e2695e67a38b518d8e154c7a0e0b0aed/gui-inspect.d9e530cd06397e53.json`

The inspection reported 64,837 nodes, 139,757 edges, 25,319 elements, 28,535 sprites, and 106 scripted GUIs. Its diagnostics included 1,484 retained errors and six warnings, with truncation of 1,490 additional diagnostics. Important diagnostic codes were `INDEX_SYMBOL_COLLISION`, `INDEX_UNRESOLVED_REFERENCE`, `SOURCE_STRING_TOO_LONG`, and `GUI_REFERENCE_UNRESOLVED`. Duplicate GFX definitions were reported for several Event 3 Holy Realm and Event 5 Soviet Collapse textures. These are source/index findings only and are not a recommendation to edit GUI layout or assets in this pass.

The required read-only render for `communism_spread_dashboard_container` completed for normal and disabled states at 1920x1080 and 1280x720:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c6c644783bac9e2a63690c19e146d86fa92af4a9d2d9efca8af5968625ed258c/5ba380a6a92f11de47e8bb39341700361fad6a68244dc08a7a06ff846a7fc387/communism_spread_dashboard_container-full.svg`

The artifact returned only `MCP_RESPONSE_TRUNCATED` and no rendered blocker. A batch render covering the other principal decision-owned windows did not return within the tool response window and was terminated. A targeted `hoi4.gui_inspect` for the same window with a default scenario timed out after 180 seconds. Therefore per-window visual evidence for the remaining surfaces is unavailable, and source review is not treated as equivalent rendered evidence. No `hoi4.gui_rewrite` call was made.

The required probability route was attempted through the installed `hoi4.probability_inspect` tool. The project-specific `chaosx_ai_probability_auditor` route was not callable in this environment, so no balance conclusion is claimed. The successful Event 5 inspect used the `decision_ai_will_do` adapter and produced:

`hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/885b150a178a88e2c19da9c114ffdce2d036c1f13a43980418ca1b179eb8ac84/3101df48fb6ad1b944e33fd18be422b8f27a517e19975f8983f65493523deba1/probability-inspect-72ed3330bb09.json`

That artifact inspected 211 Event 5 candidates, reported zero unresolved inputs, and passed source validation, but the pool was not complete and no scenario comparison was run. Event 6, 12, 13, 14, 16, 18, 19, shared biowarfare, and Fallout source inspections returned `INTERNAL_ERROR`; the Event 20 shared inspection returned `ARTIFACT_STORAGE_LIMIT`; narrower candidate-pool attempts timed out after 180 seconds. These exact blockers are carried into the probability handoff below.

## Issue list sorted by severity

### P1: confirmed or strong cleanup candidates

1. `common/decisions/012_africa_decisions.txt:463` and `:480` use `africa_selected_action_dynamic_cost`. The corresponding localisation in `localisation/english/012_african_union_l_english.yml:169-171` presents political power, command power, manpower, infantry and support equipment, trucks, trains, convoys, fuel, civilian or administrative capacity, intelligence, stability, and war support in one dynamic string. This is approximately 13 distinct spendable or state-value types, mixes costs with requirements, uses literal resource names rather than a complete texticon presentation, and violates the four-spendable-cost ceiling unless most entries are proven to be non-consumed requirements. This needs a broad Africa cost design decision, not a safe wording-only patch.

2. Event 5 contains 118 mission blocks and every one has a `visible` field, while the offline wiki and vanilla documentation state that mission `visible` does not control mission display in the way decision visibility does. Ninety-seven of those missions have no `cancel_trigger`. This does not prove that all 97 are stale: several are timeout-driven or complete through helper effects, but the combination can leave user-facing mission state or cleanup dependent on a path the engine does not evaluate. Review `common/decisions/005_soviet_collapse_decisions*.txt` by mission owner and replace visibility assumptions with activation, category gates, or functional scripted-GUI state where needed.

3. `common/decisions/020_black_plague_rat_decisions.txt:916-923` defines `black_plague_rat_king_execute_terminal_takeover` with `custom_cost_text = black_plague_rat_king_execute_terminal_takeover_cost`, but no `custom_cost_trigger` or visible payment is present in the block. `localisation/english/020_black_plague_rat_decisions_l_english.yml:154` describes marked-continent, crown-preparation, and stable-court requirements rather than a consumed cost. Since `custom_cost_text` is display-only in the documented decision contract, this is a strong candidate for a requirement tooltip lane or for adding an explicitly audited payment path. Do not remove the lane until its helper references and intended balance are confirmed.

4. Approximately 36 targeted decisions or missions use `target_trigger` without a `target_root_trigger`. The largest groups are Event 5 Moscow Republic decisions around `common/decisions/005_soviet_collapse_decisions.txt:4946-5248`, Event 5 Ukrainian League decisions around `:8214-8440`, Event 12 selection and obligation decisions around `common/decisions/012_africa_decisions.txt:67,93,128,488,508,528,548,568,1713,1730,1982,2000,2404,2423,2442,2461,2545`, Event 15 targeted missions around its target blocks at lines 1218, 1298, 1673, 1733, 1987, 2347, 3088, 4292, 4383, 4484, and 4744, Event 16 synthesis at line 14, Event 19 achievement trials at lines 775, 811, 847, and 883, and shared bio/genocide/Japan operations. Missing root filtering is a performance and invalid-target risk, but adding it blindly can change target eligibility. Route each candidate through MCP target inspection and the probability/AI auditor before patching.

5. Several visible categories exceed the six-primary-action cognitive-load ceiling even before mission rows and scripted-GUI state are counted. The largest source categories are `brilliant_scientist_directorate_category` with 149 blocks across seven files, `soviet_collapse_soviet_category` with 127, `natural_disaster_aftermath_category` with 127, `camp_repression_network_category` with 83 across two files, `chaosx_disease_containment_category` with 82 across four files, `africa_priority_member_category` with 72, `secret_alliance_foreign_interference` with 54, `holy_realm_mandala_category` with 51, and `infantry_spawn_formation_management_category` with 51. Source counts are not active counts, but they prove that phase gates and ownership need to be audited before accepting a category as a single player surface.

### P2: probable design or maintenance risks requiring bounded follow-up

6. Category ownership is fragmented across event-owned and shared files. The Directorate category spans seven Event 16 files; disease containment spans Event 20 response and weaponisation files plus shared bio-warfare files; CBRN operations spans five shared CBRN files; Africa and Utopia categories are split between main and evolution or prefire fragments; repression and genocide categories mix generic, colonial, and country-specific files. This increases duplicate cost, tooltip, AI, and cleanup drift. It is a strong architecture finding, not permission to merge files or categories in this baseline.

7. A raw scan found about 1,709 `custom_cost_text` references across about 902 keys. All directly referenced keys had a localisation definition, but that does not establish that their texticons, payment, or requirement semantics are correct. The main duplicated payment families are delegated through helpers such as the Soviet Collapse `soviet_collapse_pay_*` family, Independence Wave `independence_wave_decision_pay_*` family, and Utopia Manifesto `utopia_manifesto_pay_*` family. These are dynamic references and need helper-level tracing rather than block-local deletion.

8. Several direct cost strings exceed four spendable types or omit texticons. Examples include Independence Wave form 8 in `localisation/english/006_independence_wave_formable_registry_l_english.yml:112`, the Form 01/02/04 administrative-diplomatic cost at `localisation/english/006_independence_wave_form01_02_04_l_english.yml:66`, Form 05 cost families at `localisation/english/006_independence_wave_form05_l_english.yml:75-87`, Form 39 at `localisation/english/006_independence_wave_formable_registry_l_english.yml:166`, Pacific forms in `localisation/english/006_independence_wave_pacific_l_english.yml:171-236`, CBRN doctrine at `localisation/english/cbrn_doctrine_l_english.yml:31`, CBRN occupation at `localisation/english/cbrn_occupation_l_english.yml:19`, Infantry Spawn at `localisation/english/019_infrantry_spawn_l_english.yml:299` and `:314`, and Fallout repair costs at `localisation/english/fallout_consolidated_l_english.yml:666-686`. These are broad migrations except for the bounded <=4 cases below.

9. Targeted decisions that are activated through `activate_targeted_decision` require a separate route-lock audit because the documented effect bypasses ordinary triggers, cooldown, and `fire_once` checks when called. Any scripted caller that uses this effect for Soviet, Africa, Independence Wave, or shared formable flows must prove its own cooldown, target validity, and one-shot guard. This is especially relevant to operation, treaty, and achievement targets.

10. Forty-one missions have neither an explicit `complete_effect` nor an explicit `cancel_effect`. The set includes Event 6 founding-package deadlines, Event 11 public-offensive countdown, Event 12 recognition or intervention windows and sponsorship obligations, Event 16 facility defence, Event 18 rescheduling, and Event 19 internal `selectable_mission = no` clocks. Many are likely intentional timeout-only or cancel-driven clocks; none should be deleted without tracing the timeout helper, phase flags, and downstream event or scripted effect.

11. Global event-target saves are widespread and often have matching clears, but ownership is distributed. Confirmed examples include the Fallout NZL partner target at `common/decisions/fallout_consolidated_decisions.txt:2028,2053,2065`, Africa transfer and achievement targets at `common/decisions/012_africa_decisions.txt:614,632,3403,3433,3473`, Directorate facility and foreign targets in `common/decisions/016_brilliant_scientist_directorate_*.txt`, and large Secret Alliance cleanup blocks in `common/scripted_effects/011_secret_alliance_effects.txt:7904-7914`. Saves such as `africa_elephant_band_state`, `independence_wave_reclamation_front_coordinator`, and Fallout world-end external-owner targets require lifecycle tracing before being called leaks. The safe finding is duplicated ownership and stale-target audit debt, not a proven un-cleared target.

12. Formable nation decisions produce about 154 direct-ID localisation candidates without direct decision keys in `common/decisions/formable_nation_decisions.txt`, including `form_scandinavia` at line 3, `form_nordic_league` at line 95, `form_north_sea_empire` at line 496, `form_austria_hungary` at line 785, `form_european_union` at line 2434, and `form_roman_empire` at line 4743. Categories use aliases and state-puzzle scripted GUIs, so these are not confirmed missing keys. Render and scripted-localisation tracing must establish whether the engine supplies standard formable names before any additions.

### P3: positive or low-confidence findings

13. No duplicate decision identifiers were found among the 3,382 in-scope blocks. This rejects deletion or merging based solely on identifier duplication. Category fragmentation and repeated helper calls remain valid cleanup subjects.

14. The Fallout consolidated cost strings around lines 30-150 are a useful positive precedent: they use texticons and keep ordinary spendable cost displays compact. Mirror that pattern only after the underlying payment count is proven to be four or fewer.

## Decision category lifecycle notes

| Category and owner | Source scale | Lifecycle and ownership finding |
| --- | ---: | --- |
| `brilliant_scientist_directorate_category` (Event 16 Directorate) | 149 blocks in 7 files | Project board, facilities, foreign, institutions, containment, synthesis, and evolution fragments share one category. Phase gates may reduce simultaneous rows, but ownership and cleanup are distributed. Keep the category; first define phase-specific primary actions and owner helpers. |
| `soviet_collapse_soviet_category` (Event 5) | 127 blocks | Moscow, Ukraine, Republic, and collapse-phase flows share a large category. Targeted treaty, administration, ultimatum, and reclamation decisions need root target validation and phase cleanup. |
| `natural_disaster_aftermath_category` (shared/Fallout) | 127 blocks | The source ceiling indicates a long-lived response warehouse. Separate active recovery choices from hidden timers and completed-state records through functional gates, not new visual tabs. |
| `camp_repression_network_category` (shared plus colonial) | 83 blocks in 2 files | Generic and colonial ownership is mixed. Duplicate repression actions and postwar review/sunset missions need one cleanup owner and explicit terminal state. |
| `chaosx_disease_containment_category` (Event 20 plus shared bio) | 82 blocks in 4 files | Response, weaponisation, and shared biological actions share a player surface. Counter values and route gates need concise significance and safe target cleanup. |
| `africa_priority_member_category` (Event 12) | 72 blocks | Priority-member actions, host transfer, recognition, and sponsor obligations share a category. The dynamic cost row is too broad for a single action string. |
| `secret_alliance_foreign_interference` (Event 11) | 54 blocks | Foreign-interference operations use many targets and global target callbacks. Functional selector cleanup and explicit operation completion are safer than category expansion. |
| `holy_realm_mandala_category` (Event 3) | 51 blocks | The category owns a dedicated status GUI and many phase actions. GUI content and toggles may be cleaned functionally, but no layout or asset change is accepted here. |
| `infantry_spawn_formation_management_category` (Event 19) | 51 blocks | Lot management, debt, and equipment obligations create raw rows of values. The cost display needs a bounded requirement/cost split before any visual presentation work. |
| `cbrn_operations_category` (shared CBRN) | 38 blocks in 5 files | Doctrine, occupation, and operation fragments repeat cost and helper patterns. Treat as a shared architecture migration, not a local wording edit. |
| `utopia_manifesto_ledger_category` (Event 13) | 40 blocks in 2 files | Main and prefire ledgers split ownership and can duplicate counters or gates. Preserve the ledger binding while tracing one state owner per action. |

For all categories, the source count is not a claim that every action is visible simultaneously. The accepted cleanup threshold is still six or fewer primary actions in each player-facing phase, with no more than three simultaneous active missions unless the mission purpose is explicit. Phase gating, `available`, `visible`, scripted GUI content, and activation effects need scenario evidence before a category can be declared compliant.

## Cognitive-load notes

Visible actions are most overloaded in Directorate, Soviet Collapse, Disaster Aftermath, repression, disease containment, Africa, and Infantry Spawn categories. The category counts above are enough to require a phase-by-phase action inventory, even where `available` gates reduce the live set.

Active missions are most concerning in Event 5, where 118 mission blocks carry `visible` fields, Event 16 project-board and facility flows, Event 12 repeated recognition and sponsorship windows, and Event 6 package suites. The actual simultaneously active set is scenario-dependent and could not be proven by the blocked MCP route.

Player-facing values are not consistently given a clear cause, threshold, consequence, or response. Africa's action cost row, Infantry Spawn's exact-lot obligation row, cannibalism larder and population counters, resource-found state values, CBRN contamination or protection values, and disease containment counters are candidates for concise stage or threshold presentation. This recommendation is functional content and selector work only; it does not authorize new or modified interface layout.

Text density is highest in dynamic cost localisations that enumerate resources and counters in prose. A player should see a short, icon-first consumed-cost line followed by a separate requirement or blocked-reason line. Long category descriptions and raw helper names should remain hidden behind custom trigger tooltips.

Every visible value should answer what it measures, what changes it, which threshold matters, what consequence follows, and which action responds to it. The audit found several values whose source names imply those relationships but whose display strings do not establish them. These are design and localisation follow-ups rather than permission to invent a new meter system.

## Mission quality notes

| Owner and mission family | Category and region | Requirement and duration | Success and failure | Duplicate or stale risk |
| --- | --- | --- | --- | --- |
| Event 5 Soviet Collapse treaty, republic, and reclamation missions | Soviet-collapse categories; Soviet sphere and target republics | Target country, phase flags, war or route state; durations use a mixture of file constants and literal/package values | Several complete through helper or cancellation effects; timeout paths vary; 97 lack explicit `cancel_trigger` in the Event 5 scan | High. Repeated treaty and republic packages can drift in targets, payment, AI, and cleanup. |
| Event 6 Independence Wave founding and integration packages | Formable or package category; package-defined regions and former hosts | Activation flags, host/target checks, package variables, and timed deadlines | Common pattern is `cancel_effect` setting success/failure markers and `timeout_effect` applying failure; missing explicit `complete_effect` is often intentional | High. Repeated country packages are structurally similar and should share verified lifecycle helpers. |
| Event 12 Africa recognition, coalition, intervention, and sponsorship windows | Africa priority, charter, and world-order categories; African states and sponsor targets | Phase flags, host/member/target scopes, obligations, and fixed or scripted duration | Timeout or phase cancellation often advances the route; explicit success is not present in several windows | Medium-high. Four repeated windows and multiple sponsor obligations are drift candidates. |
| Event 15 Utopia objective and targeted mission families | Utopia categories; route and target-defined regions | Target selectors, route flags, and duration constants or package values | Completion often delegates to scripted effects; target failure and cancellation need per-mission review | High. Targeted mission blocks repeat selector and helper shapes. |
| Event 16 Directorate facility defence and project-board missions | Directorate category; facility and research-site states | Facility target, project phase, institution flags, and project duration | Facility and board flows use timeout or cancel-driven terminal paths; phase cleanup is distributed | High. Seven category fragments can leave stale target or project state. |
| Event 18 resource-found prefire and rescheduling missions | Resource-found categories; random resource field/state regions | Prefire owner/state event targets and field variables; timed rescheduling and field windows | Scripted effects handle terminal state; repeated save/re-save of short-lived targets needs chain tracing | Medium. Repeated target pointers can expose stale scope if a chain exits early. |
| Event 19 Infantry Spawn internal clocks | Formation and derivative-operation categories; lot or theatre scopes | Internal variables, lot obligations, and package constants | Ten reviewed system missions are non-selectable and timeout-delegated; they are likely intentional clocks rather than player missions | Low for deletion, medium for stale state if timeout cleanup is skipped. |
| Shared repression and CBRN missions | Repression, CBRN, and disease categories; country, camp, corridor, and operation regions | Country/region ownership, contamination or repression flags, equipment requirements, and timed review windows | Postwar sunset and inspection/training missions often timeout; some lack explicit cancel paths | Medium-high. Shared and event-owned fragments can duplicate cleanup or leave active objectives after route closure. |

The mission owner must document the terminal state before changing a timeout-only mission. A mission with no `complete_effect` is not automatically dead when its `cancel_effect`, timeout helper, event firing, flag, or scripted GUI callback provides the success path.

## Cost and requirement clarity

The direct scan found approximately 1,709 `custom_cost_text` references across approximately 902 localisation keys. The keys exist, but many strings mix consumed resources, non-consumed requirements, counters, and factory or capacity reservations in a single sentence. Helper-generated costs were not counted as safe merely because the block-local `custom_cost_trigger` was present.

| Surface | Observed spendable or displayed types | Texticon and clarity result | Disposition |
| --- | ---: | --- | --- |
| Africa `africa_selected_action_dynamic_cost` | About 13 | Long prose, literal labels, mixed requirements and spendables | Defer to broad mechanic redesign. |
| Independence Wave Form 8, Forms 01/02/04, Form 05, Form 39, Pacific packages | 5-8 in representative strings | Repeated literal resource names and `requires`/`consumes` prose | Defer broad migration; preserve package mechanics until owner selects a four-cost model. |
| CBRN doctrine and occupation | 7 in representative strings | Literal equipment and resource names without complete texticons | Defer broad cost-family migration. |
| Infantry Spawn exact-lot and standardisation | Dozens in the exact-lot row and many in standardisation | Raw dynamic rows are not a readable decision cost | Defer to lot-obligation design; do not hide a fifth cost in a tooltip. |
| Fallout repair rows | Mixed infantry, trains, factories, and counters | Literal labels and cost/requirement mixing at `:666-686`; earlier consolidated costs are a positive icon-first precedent | Review each row; only bounded <=4 rows are local candidates. |
| Africa sponsorship keys | Three representative requirements | `localisation/english/012_africa_world_sponsorship_l_english.yml:92-95` uses prose Political Power and Command Power labels | Safe bounded icon-first localisation candidate after confirming consumed versus required semantics. |
| Africa elephant logistics | Four types in `common/decisions/012_africa_elephant_operations_decisions.txt:79` | `localisation/english/012_africa_elephant_operations_l_english.yml` uses literal elephant equipment, trucks, trains, and fuel names | Safe bounded icon-first localisation candidate if all four are actually consumed. |
| Black Plague Rat King terminal takeover | No proven spendable payment in the block | Cost text describes requirements, not a cost lane | Safe bounded requirement-tooltip candidate after helper tracing. |

No accepted cleanup may leave a fifth or later spendable cost hidden in a tooltip, confirmation, scripted effect, or secondary panel. Literal resource names must be replaced with the correct texticons only when the underlying cost is retained; a missing texticon is not permission to keep prose labels.

## AI validity and route-lock notes

Every decision or mission with `ai_will_do`, AI modifiers, MTTH-backed scores, random-selection weights, target-selection weights, or scripted weighted pools is a probability-auditor candidate. The candidate set for follow-up is:

- Event 1 `common/decisions/001_communism_spread_decisions.txt`.
- Event 2 `common/decisions/002_zombie_outbreak_decisions.txt`.
- Event 3 `common/decisions/003_holy_realm_decisions.txt`.
- All Event 5 `common/decisions/005_soviet_collapse*.txt` decision and mission fragments.
- All Event 6 `common/decisions/006_independence_wave*.txt` package, formable, target, and achievement fragments.
- Event 7 Fury, Event 10 Death, Event 11 Secret Alliance, Event 12 Africa, Event 13 Utopia Manifesto, Event 14 Cannibalism, Event 15 Utopia objective, Event 16 Directorate, Event 17, Event 18 Resource Found, Event 19 Infantry Spawn, and Event 20 Black Plague decision and mission files.
- Shared CBRN, biological warfare, camp repression, fallout, formable nation, genocide, Germany, and other shared decision files that are active in Events 1-20.

The Event 5 probability artifact is evidence that source inspection can succeed, but it is not a balance verdict: it has 211 candidates, an incomplete pool, and no named scenario compare. The other requested source families were blocked by `INTERNAL_ERROR`, `ARTIFACT_STORAGE_LIMIT`, or 180-second tool timeouts. The parent must not accept or alter weights until `chaosx_ai_probability_auditor` is available and runs identical named scenarios through inspect, evaluate or sweep as appropriate, and compare after any owner-applied patch.

Route-lock checks should reject dead countries, disabled evolutions, impossible borders, closed routes, invalid event targets, and stale target scopes before considering an AI weight change. The no-root target groups above and the `kmb_force_mining_concession` block at `common/decisions/005_soviet_collapse_decisions.txt:13677` are priority candidates. The latter has a `target_trigger` without an obvious `state_target`, `target_array`, or target-root limiter and needs engine inspection before any change.

Targeted decisions with `target_root_trigger` but no `target_trigger` are not automatically errors. Fallout filter or convoy decisions and Event 11 suspect selection use target arrays or scripted selectors that may be intentional. Preserve those until MCP target evidence proves otherwise.

## Localisation and tooltip gaps

The exact-ID scan reported about 182 apparent missing decision keys, but most were aliases, explicit `name` fields, hidden missions, vanilla object names, or scripted formable names. The formable suite is the largest uncertain group. Do not mass-add keys until the scripted state-puzzle and standard formable localisation path is rendered and traced.

The strongest confirmed wording gaps are cost and requirement strings that expose literal resource labels, long raw dynamic rows, or mixed requirement and payment prose. The Rat King terminal takeover is the clearest decision-level mismatch because its `custom_cost_text` says requirements while the block has no proven spendable lane.

Review custom trigger tooltips for long raw triggers in Africa, Soviet Collapse, Independence Wave, CBRN, Infantry Spawn, and formable decisions. The visible string should explain the blocked reason, threshold, consequence, and player response, while implementation history and helper names stay hidden.

Decision-owned scripted GUI surfaces found in source include `communism_spread_dashboard_container`, `zzz_cure_progress_container`, `holy_realm_mandala_category_container`, `independence_wave_status_window`, `death_black_atlas_container`, `secret_alliance_counter_network_container`, `africa_charter_window`, the four cannibalism command windows, `utopia_manifesto_ledger_container`, `kruger_directorate_container`, `resources_found_field_window`, `black_plague_response_category_window`, `disease_containment_header_window`, `repression_ledger_category_window`, and the formable state-puzzle windows in `common/scripted_guis/chaosx_formable_state_puzzles.txt`. Functional state, selector, disabled-state, and localisation bindings may be cleaned after per-window MCP inspect and render evidence. No visual layout or asset change is recommended here.

## Cleanup and exploit-risk notes

- Audit all `activate_targeted_decision` callers for explicit cooldown, one-shot, target validity, and payment guards because the engine effect bypasses ordinary decision trigger and cooldown checks.
- Trace payment helpers before declaring a decision free. Soviet Collapse, Independence Wave, Utopia Manifesto, Africa, CBRN, Fallout, Infantry Spawn, and Cannibalism use helper or dynamic cost paths that are not provable from a single decision block.
- Check free unit, equipment, train, convoy, and war-goal loops at timeout, cancellation, reactivation, and phase-transition boundaries. Event 6 package repetition, Event 19 lot obligations, and Event 5 reclamation operations are the highest-risk families.
- Treat Event 5 timeout-only or cancel-driven missions, Event 12 windows, Event 16 project/facility missions, and Event 18 resource targets as stale-flag and stale-target candidates until their terminal effects are traced.
- Global target saves are not proof of leaks. Verify a clear on every terminal route and use the documented global-target cleanup contract. Regular short-lived event targets should not be converted to global targets merely to persist a pointer.
- Repeated category fragments and helper families should be consolidated only after proving that no event, scripted GUI, focus, localisation, spreadsheet, or later-event reference relies on the existing file boundary.

## Recommended fixes

### Safe bounded patch candidates after owner confirmation

1. Trace `black_plague_rat_king_execute_terminal_takeover` and move its marked-continent, crown-preparation, and stable-court text to a concise custom requirement tooltip, or add the exact payment trigger and complete-effect payment if the accepted design truly consumes a cost. Keep the decision identifier and event route unchanged.

2. Convert the Africa sponsorship requirement keys at `localisation/english/012_africa_world_sponsorship_l_english.yml:92-95` to icon-first text only after confirming which values are spendable. Do the same for the four-type elephant logistics string at `common/decisions/012_africa_elephant_operations_decisions.txt:79` and its localisation. This is a localisation/content change, not an interface-layout change.

3. For no-root target candidates, add a narrow `target_root_trigger` or bounded target array only after MCP target inspection proves the same eligible set and the probability auditor confirms no AI rank or availability regression. Start with one Soviet Republic or Africa target family and compare before widening.

4. Replace mission `visible` assumptions with functional activation, category gating, or scripted-GUI state only where a rendered/source-linked lifecycle trace proves the current field is ineffective. Do not attempt a visual mission-panel redesign.

5. Centralise repeated timer and payment values through existing scripted helpers or a documented shared constant only when the field supports the constant and the helper has one owner. Preserve file-scoped constants where cross-file conversion would alter parsing or route timing.

### Uncertain dynamic references

- Event 5, 6, 12, 13, 14, 15, 16, 18, 19, and 20 custom cost blocks whose payment is delegated to scripted effects.
- Formable nation direct-ID localisation candidates and state-puzzle names.
- Target-root additions for selectors backed by `target_array`, `state_target`, `any_country`, or scripted targets.
- Missions without complete or cancel effects where timeout, cancellation, event firing, or helper calls provide the actual terminal path.
- Global event targets with saves and clears in different files, including Africa, Independence Wave, Directorate, Fallout, and Secret Alliance.
- Functional scripted-GUI selectors and toggles because per-window MCP renders were blocked; no layout change is implied.

### Rejected candidates for this baseline

- No decision deletion or merge based on duplicate IDs; the scan found none.
- No interface layout, coordinate, click-region, sprite, GFX, or GUI asset edits.
- No broad category merge or category removal based only on source count.
- No mass formable localisation additions without proving the dynamic name path.
- No AI weight or mission score change without the named probability auditor and scenario compare.
- No deletion of timeout-only or cancel-driven missions without a complete lifecycle trace.
- No Event 21 or later decision cleanup beyond references required by shared infrastructure.

### Deferred broad migrations

- Reduce Africa's dynamic action cost to a comprehensible four-cost maximum and separate consumed costs from non-consumed requirements.
- Redesign the Independence Wave, CBRN, Infantry Spawn, Fallout, and Cannibalism cost families around icon-first bounded cost lanes.
- Phase and possibly split the large Event 5, Event 12, Event 13, Event 16, repression, disease, and formable decision surfaces without introducing extra warehouse tabs or visual GUI changes.
- Perform an owner-by-owner mission lifecycle migration for Event 5's 118 missions and the repeated Event 6 package suites.
- Create a shared helper and constant ownership map after dynamic payment, target, and timeout traces are available.
- Complete per-window GUI inspect/render and functional selector/binding audit when the MCP artifact and response limits are repaired.
- Run the full probability baseline and post-patch comparison for every weighted candidate listed above.

## Completion and remaining blockers

The requested baseline report is complete and no source or GUI implementation was performed. The positive evidence is the absence of duplicate decision IDs, the successful Event 5 source probability inspection, the global GUI graph inspection, and the one completed dashboard render.

The baseline is not a balance approval. Probability auditor routing, most per-window GUI renders, targeted GUI inspection, and scenario-specific active mission counts remain blocked by unavailable custom routing, MCP internal errors, artifact storage limits, and 180-second timeouts. Parent review must carry those blockers forward before accepting any weighted, target-selector, cost-payment, mission-lifecycle, or scripted-GUI cleanup patch.
