# Event 007 Fury helper audit, 2026-10-05

Disposition: implemented source repairs with required MCP validation blocked.
Acceptance basis: parent delegated local lifetime, accounting, scope, cleanup, and scheduling repairs under G2 popup restraint, G4 visible causes and costs, and G7 actionable Settings outcomes.
The parent explicitly accepted the depot four-resource transaction, current-actor scope repairs, first-conquest baseline/pending proof, weekly major-super check, and one terminal notice per human player.
Parent subsequently accepted removing support equipment from march coring, retaining command power, manpower, rifles, and stability as its four concrete costs.
Parent integration found that this worker's new paid receipt guard also blocked two preexisting one-time focus grants.
Parent explicitly accepted separating those planned one-time recruitment rewards from repeatable paid recruitment, without forging a payment receipt.
Parent also accepted actor-correlated containment proof to stop achievements from borrowing an unrelated actor's border-watch completion.
Later G6 acceptance covers strict actor-specific Firebreak proof, ordinary-neighbor-first rival targeting with an explicit manual-hostile actor exception, manual intensity bypassing only the Chaos tier while honoring disabled evolution checkboxes, preterminal project-pact reserve sharing, and a shared-third-target score bonus of 20 for Rival Map Claims.
The final parent-authorized lifecycle tranche covers ordinary major-Fury threat-source reporting, native Fury-led faction cleanup with leader handover, removal of unconsumed numeric accumulators and paid no-op actions, per-human blocked-seed notices, and receipt-derived physical sharing under an optional deferred-settlement API.
This handoff does not establish whole-event completion or approve unrelated design.

## Ownership and changed files

- `common/scripted_effects/007_fury_effects.txt`, strictly below `fury_unlock_column_equipment`.
- This handoff.

Parent owns the top selection/application block, events, constants, shared wiring, documentation integration, and final commit.
Decision auditor owns decisions and triggers.
Text auditor owns player localisation.
Probability auditor remains read-only and owns baseline/comparison evidence.
No new shared helper, central router, duration value, AI weight, or tuning constant was authored by this worker.
Existing neutral helpers in `common/scripted_effects/chaosx_dynamic_effects.txt` and its Markdown API were inspected before retaining Fury-owned orchestration.

## Helper API and call-site map

All helpers below execute in country scope except target scoring, which executes on a candidate country with a caller-retained actor target.
All temporary outputs require caller-owned storage at every boundary where the output is consumed after return.

| Helper | Inputs and caller-owned outputs | Side effects and consumers |
| --- | --- | --- |
| `fury_prepare_spawn_count` | Current actor size and evolution flags. Caller preinitializes `fury_spawn_count = 0`. | Returns existing 5/7/10/14 starting tier. `fury_spawn_starting_units` initializes it and uses the actual actor as owner. |
| `fury_prepare_initial_reserve_count` | Actor size/evolution. Caller preinitializes `fury_initial_reserve_count = 0`. | Existing 8/12/16/20 reserve tier, consumed by `fury_add_initial_reinforcement_reserve`. |
| `fury_add_reinforcement_reserve` | Current actor. Caller sets unscoped temporary `fury_reinforcement_reserve_add` to the intended addition immediately before calling. No output storage is required. | Rounds and clips the input in place to remaining lifetime room, then adds admitted units to the normal pool and lifetime-granted counters. At total 98, a request of three admits two. At total 100, no addition is admitted. Lifetime cap applies to reserve grants, not separate direct focus columns. |
| `fury_prepare_weekly_unit_count` | Scoped finite pool/tick counters. Caller preinitializes `fury_weekly_unit_count = 0`. | Advances cadence and consumes bounded weekly reserve. `fury_spawn_weekly_reserve_units` retains the count and deploys to its actual actor. |
| `fury_prepare_direct_spawn_count` | Momentum, states, evolution, occupation. Caller preinitializes `fury_direct_spawn_count = 0`. | Existing capped direct-growth calculation. `fury_spawn_weekly_units` and `fury_spawn_focus_depot_units` retain output. Paid depot no longer calls this formula. |
| `fury_spawn_focus_depot_units` | Country scope, current actor size/momentum/evolution/occupation. No payment input and no public temporary output. Internally preinitializes `fury_direct_spawn_count = 0` before preparation. | Preserves the original one-time direct-focus wave, 1-8 full columns with experience factor 0.15. Saves `fury_focus_column_spawn_owner` for the current actor. Consumes no payment receipt or reserve, and grants no extra scaled stockpile/manpower. Called only by `fury_depot_cadres` and `fury_depot_officers_without_leave`. |
| `fury_select_weighted_actor_candidate` | Existing candidate eligibility and weights. Caller preinitializes `fury_weighted_actor_selected = 0`. | Every owned evolution/world-end/scenario fallback caller initializes success before checking it. Parent repairs the top pool call sites. No weight values changed. |
| `fury_prepare_world_end_seed_requirements` | Current actor pool and safe minors. Caller initializes all three `fury_world_end_safe_seed_candidates`, `fury_world_end_existing_actor_count`, `fury_world_end_needed_seed_count` to zero. | `fury_try_start_world_end` retains computed readiness rather than accidentally comparing lost zero outputs. |
| `fury_prepare_triggerable_scenario_actor_count` | Settings intensity. Caller preinitializes `fury_triggerable_actor_goal = 0`. | `trigger_world_in_fury_scenario` retains the intensity-specific goal for all continental/fallback seeding. Existing actor cursor is preserved across nested calls. |
| `fury_decision_pay_reinforcement_cost` | Active actor, finite reserve, owned/controlled deployment state, all four resources. Decision caller initializes `fury_depot_payment_success = 0`. | CP and rifles go through the existing Black Friday payer when active. Support and manpower are charged exactly once after successful payment. Rejected payment leaves output zero. |
| `fury_spawn_depot_decision_units` | Caller-owned `fury_depot_payment_success = 1`, active actor, finite reserve. | Consumes success immediately, creates `constant:fury_units.depot_spawn_units` full columns in an owned and controlled state, decrements the same reserve, and adds no stockpile or manpower grant. A repeated call without another payment creates nothing. |
| `fury_score_current_target_candidate` | Candidate stats and regular `event_target:fury_targeting_actor` established by `fury_choose_next_target` or `fury_declare_all_valid_neighbors`. | Reads the acting Fury's preparation, divisions, momentum, overextension, and history, rather than the original Settings/firing country. Preserves baseline arithmetic and adds the parent-chosen 20-point shared-third-target bonus under existing legal-candidate gates. |
| `fury_declare_on_rival_actor` | Current actor must pass shared `fury_can_target_rival_actor`. | Rejects ordinary actors with a valid normal neighbor before any rival scan. Allows ordinary exhaustion or an explicit hostile manual-scenario actor, then uses the unchanged legal rival selection/declaration path. |
| `fury_apply_triggerable_scenario_actor_package` | Intensity plus per-stage Settings checkbox. Caller-owned `fury_triggerable_actor_count` remains the only forwarded counter. | Initializes event/type/stage/tier context immediately before each checkbox guard. Tier zero gives the accepted manual tier exception. Enabled intensity stages apply independently, disabled stages do not. It does not promote ordinary global evolution unlocks. Actor count and configured reserve bonus remain intensity-owned. Framework metadata scratch values may be modified when already caller-owned. |
| `fury_share_terminal_reserves_effect` | Shared `fury_can_share_reserves`, `fury_can_pay_terminal_reserve_share_cost`, and recipient-scope `fury_is_valid_reserve_share_target` with PREV donor. | Saves actual donor and one recipient as regular targets, initializes its private selection sentinel to zero, and locks/revalidates the same recipient before payment and transfer. No second random selection occurs after payment. It supports the accepted preterminal project-pact representation and existing terminal route. |
| `fury_update_world_threat_source` | Current active actors, their major status/state counts, and terminal-active flag. Country scope with no temporary output. | Sets only `world_threat_source_fury` when a qualifying active actor exists, otherwise clears it, then calls the existing aggregate refresher. Called by the existing weekly tick after readiness and at cleanup completion. |
| `fury_prepare_reserve_share_payload` | Sale-mode snapshot, caller-retained `black_friday_fury_component_resource_kinds` and `black_friday_fury_component_final_costs`, positive transaction ID and primary metadata. Caller initializes all four named payload outputs to zero. | Returns manpower, infantry, support paid amounts and validity. Ordinary mode returns existing full amounts. Sale mode validates receipt shape/metadata and sums matching resource kinds through the aligned index. CP is not transferred. Invalid/nonpositive physical receipts remain invalid. |
| `fury_refund_reserve_share_receipt` | Actual positive pending `black_friday_owner_transaction_id`, payer country scope. Caller owns the three universal refund outputs. | Uses the real generic receipt refund API and resets provisional payment success to zero. It does not reconstruct quotes or reopen settled rows. |
| `fury_deliver_reserve_share_payload` | Recipient country scope and three positive named payload inputs. | Grants exactly the paid manpower, infantry and support quantities. No CP credit. |
| `fury_retract_reserve_share_payload` | Recipient country scope and the same three positive payload inputs. | Negates private copies through multiplication, removes exactly the delivered quantities after rejected settlement, and leaves the original paid outputs intact for refund accounting. |
| `fury_choose_next_target`, `fury_choose_rival_actor_target`, `fury_declare_all_valid_neighbors` | Current Fury actor and unchanged candidate rules. | Save `fury_targeting_actor`, update that actor's selected target, and declare war from that actor. Rival trigger needs the decision owner's matching PREV scope repair. |
| `fury_update_occupation_pressure`, `fury_record_first_conquest_settlement` | Current actor and its controlled states. | Freeze separate occupation/settlement actor targets. State iterators credit the winner under capitulation callbacks rather than the capitulated ROOT. |
| `fury_register_world_end_actor` | Current actor and persistent world-end leader. | Adds PREV to the leader's faction, which is the current iterated actor, rather than repeatedly adding the initiating ROOT. |
| `fury_record_evolution_ii`, `fury_record_evolution_iii` | Unlock flags and historical latest actor pointer. | Initialize `events_log_evolution_has_actor = 0` before optional attribution so missing target cannot reuse an earlier truth value. |
| `fury_track_player_containment_links` | Current actor, humans currently at war with that actor. | Saves `fury_containment_actor`, preserves broad contributor history, and sets each participant's `achievement_fury_containment_@PREV` proof keyed to the actual actor. |
| `anti_fury_border_watch_success` | Successful responder and its selected neighboring Fury actor. | Enters the actor's PREV responder scope and sets both actor-keyed containment and `achievement_fury_border_watch_@PREV` proof through the responder's PREV actor. Keeps existing broad watch history and pressure effects. |
| `fury_cleanup_actor` | Current actor and each human's current war or matching actor-keyed proof. | Saves `fury_cleanup_actor_scope`. Major/Pact/LastNeighbor/NoCores branches execute only for correlated participants. An unrelated historical watch completion is insufficient. Parent clears actor-keyed human proof before later reselection of that actor. |

## Constants and resource plan

Parent added `fury_units.depot_spawn_units = 1` and reinforcement costs/gates for 610 rifles, 40 support equipment, 6,300 manpower, and the existing 15 command power.
The base six-infantry/engineer template uses 610 rifles and 6,300 manpower in installed vanilla.
Base engineers require 30 support equipment, leaving the accepted ten-equipment deployment overhead inside the 40-support debit.
Black Friday pricing applies to the existing CP/rifle components.
The additional support/manpower quantities remain concrete deployment inputs per parent acceptance.
Parent changed terminal target manpower from 1,200 to 1,000, matching its existing 1,000 debit.
Parent added `fury_target_score.shared_rival_target_bonus = 20` for the mapped rival pursuit, with release balance evidence explicitly unresolved rather than claiming a probability delta.
Infantry and support transfers already match their debits, 600 and 40 respectively.
During an active sale, the delivery quantities come from the actual paid component outputs instead of those ordinary anchors.
The parent corrected the shared CP quote/payer inputs to the positive 30-point reserves and 25-point fronts costs, obtained by negating spend constants, while preserving ordinary affordability gates.
Starting and weekly fully equipped mobilisation packages remain deliberate finite grants under the existing lifetime cap of 100.
The parent-authorized focus refill calls request three reserves from Depot Cadres and two from Depot Officers through `fury_add_reinforcement_reserve`, while retaining both one-time direct focus waves.
No unsupported zero-equipment deployment was used.
The ordinary `fury_decision_pay_march_core_cost` path retains exactly four debits: 25 command power, 4,000 manpower, 900 rifles, and three percentage points of stability.
Parent removes the matching support component from the shared Black Friday adapter and constants.
Offline Effects documentation says equipment factor zero is treated as one, so the earlier empty-column proposal was rejected and replaced by the parent-approved four-resource transaction.

## Event targets and cleanup

`fury_column_spawn_owner`, `fury_occupation_actor`, `fury_settlement_actor`, and `fury_targeting_actor` are regular effect-chain targets.
`fury_focus_column_spawn_owner`, `fury_containment_actor`, and `fury_cleanup_actor_scope` use the same short-lived target contract.
`fury_reserve_share_sender` and `fury_reserve_share_recipient` likewise persist only through the immediate transaction chain.
The private recipient-selected temporary prevents an earlier regular target from being reused when this selection fails.
Their uses are synchronous and have distinct names where one helper nests another.
They do not require persistent global storage or manual cleanup.
When the cleaning actor is the live `fury_latest_actor` representative, cleanup clears that pointer and selects the first surviving active actor from the existing country iterator, or leaves it absent when none survive.
Stored historical event-log actor IDs are not changed.
Parent preparation resets the live representative to the first entry actor for each successful batch.
Cleanup recognizes a stored target only while it remains a Fury actor and native faction leader, and the cleaning actor belongs to that faction.
A departing native leader snapshots a living Fury ally, leaves, and refreshes the appropriate global leader pointers through that member's actual `faction_leader` scope.
If succession yields a non-Fury leader, the surviving alliance crosses the accepted ownership boundary and is preserved.
Original Axis or other alliances represented only by project-pact markers are preserved.
The pact-member marker is always cleared.
Cleanup removes the omitted `fury_overextension` idea, clears the new pending-conquest proof and starting-count variable, and clears responder aid source/target variables once all actors are gone.
The continent tally clears temporary storage through `set_temp_variable`, rather than clearing an unrelated regular variable.
Parent guards delayed `.10` and `.20` cleanup against already-cleared actors.
Actor milestone/focus completion reset on later reselection remains a parent-owned lifecycle concern.

## Scheduling and presentation repairs

The South American annexation callback sets `fury_conquest_pending` only after the annex effect.
The weekly first-conquest dispatch requires that proof or growth beyond `fury_starting_controlled_states`.
Parent initializes the baseline and applies the matching `.30` acceptance condition.
The weekly ended-target branch clears its target flag/pointer before scheduling a replacement scan, preventing repeated scans/settlement reports from the stale target.
World-end seed packages no longer queue their extra day-one `.10`, since package application already schedules a scan.
Parent suppresses the package scan in hostile Settings mode where the scenario branch supplies its own scan.
The major-super threshold is checked during the existing bounded weekly actor event, allowing later territorial growth to reach the existing threshold.
World-end readiness runs first and the major helper rejects any `world_end` state, so a successful terminal transition cannot also dispatch the lesser cue in that same weekly call.
`fury_try_terminal_player_target` sets `fury_terminal_target_notice_received` before scheduling `.52`, once per human player across all Fury actors.
There is no new global on-action or recurring world iteration.

## Validation and limitations

A temporary actual-source Clausewitz subset interpreter parsed the current effects and constants.
Each scripted-effect return discarded temporary values first created in the callee, retained caller-owned values, and kept scoped normal variables separate from temporary storage.
Starting-count scenarios returned 5/7/10/14 columns and retained 8/12/16/20 reserves.
Weekly reserve scenarios with zero, one, and 100 remaining reserves created zero/one/one columns and reduced the pool exactly once.
The direct-growth scenario retained its existing cap of eight.
A reserve addition at 99 lifetime grants admitted only one further reserve and reached the cap of 100.
A separate actual-source depot model covered ordinary/sale success, repeated deployment, shortages in each of four resources, empty reserve, inactive actor, and sale rejection.
Success debited four resources once and created one reserve column, while rejection created no column and charged nothing.
Native `create_unit` behavior and the external Black Friday bundle's internals were explicit stubs, so these results prove the source transaction and call-frame model rather than observed engine behavior.
Source ordering proof checks that world-end readiness precedes the major dispatch, `fury_start_world_end` sets `world_end` synchronously, and the major dispatch rejects that flag.
`fury_create_division_template` uses the documented `has_template = "Fury Column"` guard to avoid duplicate named templates on later reselection.
That name guard does not prove the composition of an already modified template, so resource quantities remain calibrated to the package's declared six-infantry/base-engineer composition.
Actual-source assertions verify all four march debit values and unique occurrences, the same-weekly-call world-end/major ordering and rejection flag, and removal of firing-country ROOT from the four nested targeting helpers.
Final dependency checks found the new depot state trigger, caller-owned payment result, all five new depot constant references, and the rival PREV scope correction in the integrated sources.
The weak-state count thresholds now use existing `constant:fury_target_score.two_state_max`, retaining its exact value of three.
Integrated decision review caught a sale-affordability overlap where the ordinary full-price trigger was also required during discounted purchases.
The decision owner was asked to retain quoted Black Friday CP/rifle affordability and separately gate actor, reserve, state, support, and manpower.
The decision owner supplies shared `fury_can_pay_reinforcement_depot_cost` and `fury_can_pay_reinforcement_depot_extra_costs` triggers.
The payment helper and all depot decision affordability/completion gates consume the same composite, whose sale branch uses the existing quote predicate plus concrete extra resources and whose ordinary branch uses the full ordinary affordability predicate.
The final actual-source composite scenario pass verifies a purchase affordable only under a mocked 50-percent sale quote, rejection at ordinary price, each resource shortage, empty reserve, inactive actor, and invalid deployment state.
The composite fixture uses the actual parsed OR/AND/NOT trigger bodies and keeps quote calculation as an explicit external stub.
Focus recruitment tests parsed the actual new helper and direct-count helper, discarding temporary values first created in a returning helper.
Five scenarios produced 1, 5, 6, 8, and 1 columns from base, growing, evolved, cap-reaching, and extreme-pressure inputs.
The owner stayed the focus actor and the actual helper body contains no ROOT reference, so the original caller cannot select its unit owner through ROOT.
No payment/reserve/stockpile mutation was present.
A full `common/` and `events/` scripted-source consumer scan found exactly two unpaid focus calls before migration and only `fury_open_forward_depots` as a paid-helper caller afterwards.
Both original focus rewards now call `fury_spawn_focus_depot_units` and keep their other explicit rewards.
Achievement source scenarios used separate human, actor A, actor B, and original-launcher scopes.
Watching actor A and then defeating actor B produced no actor-B award, while actual war with B qualified.
Tracked war-B proof still qualified after war ended, and a generic historical watch flag without actor proof did not qualify.
The actual PREV-targeting syntax resolved to the Fury actor rather than the human or original launcher.
Native war timing and receipt of runtime callbacks remain unobserved.
Strict Firebreak scenarios additionally verify that watching actor A and then fighting actor B can qualify B containment without awarding Firebreak for B.
Watching B and then defeating B awards the matching Firebreak result.
Five rival-dispatch scenarios verify that normal neighbors prevent both scanning and war declaration, exhausted neighbors allow them, a hostile manual actor is exempt, and a stale global hostile flag alone cannot exempt an ordinary actor.
The rival candidate and focus availability use the same actor predicate as the declaration helper.
The manual stage fixture parses the actual scenario helper and Settings tier trigger over all 32 combinations of four intensities and three disabled checkbox bits at zero Chaos.
It also models an Evolution I callback overwriting tier metadata, proving that the next stage resets tier zero before evaluation.
No ordinary global unlock is promoted, and actor/reserve-count calls remain unchanged.
Maximum's all-neighbor dispatch requires applied Evolution III, while disabled III retains sequential scan and the type-owned hostile rivalry path.
Six shared-third-target score scenarios yield exactly plus 20 for a qualifying rival's matching third target and zero for missing doctrine, a different target, allied actor, inactive actor, or missing current-target proof.
Existing legal-neighbor gates still run before scoring.
Reserve sharing fixtures cover preterminal project-pact and terminal routes, exact-stock ordinary transfer of 1,000 manpower, 600 rifles, and 40 support equipment, all four resource shortages, absent/rival/stale recipients, selection invalidated before debit, and sale-payer failure.
Rejected cases pay nothing or transfer nothing according to the explicit payer-failure result, and the recipient is never selected again after the charge.
The final financial fixture imports the existing exact quotation VM and executes the current real quote, native-payment dispatcher, receipt record, settlement, and refund source definitions.
Every scripted return discards callee-first temporary scalars and arrays, and no fixture declaration repairs the owner's source.
The owner frame explicitly initializes both forwarded receipt arrays, actual transaction ID, primary component/family/ordinary/paid metadata, all four payload outputs, settlement output, and all three refund outputs.
The shared bundle's new optional `black_friday_fury_defer_settlement` input defaults to zero for existing callers.
Sharing sets it to one immediately before the payer and resets it immediately after return and at every final exit.
After validating and delivering the paid vector, sharing settles that actual pending receipt and records the retained primary achievement metadata.
Malformed or missing outputs refund the pending receipt before any shipment or pressure relief.
Rejected settlement retracts the recipient's shipment, refunds the sender, and awards no successful-delivery effects.
Real-source financial cases pass ordinary and 50-percent sale conservation, reordered kind/cost pairing, empty/misaligned/zero/negative/missing-kind/missing-primary receipts, settlement rejection, no recipient, and repeated shipments requiring additional actual payment.
At a 50.01-percent represented price factor, the exact 30-point CP input costs 16, and delivery follows the corresponding 501 manpower, 301 rifles, and 21 support paid outputs.
The missing deferred input also retains the original immediate settlement path for unrelated callers.
Native balances, recipient eligibility, the achievement callback, and injected rejected-settlement behavior are explicit model boundaries.
Native execution itself remains unobserved.
Lifecycle cases pass state threshold eight versus nine, major status independent of size, active terminal qualification, inactive/defeated/no-actor source clearing, and preservation of the existing Zombie threat source.
Faction cases pass native leader handover, later Fury member departure, original Axis preservation, and the deliberate non-Fury-led surviving-alliance boundary.
Native faction successor selection and callback ordering are explicit assumptions rather than observed engine behavior.
Live-attribution cases verify that the cleaning representative moves to a surviving active actor, clears when no survivor exists, and leaves an unrelated representative unchanged.
This source uses a first-eligible country iterator and adds no new attribution lottery.
The blocked-seed notice records `fury_seed_blocked_notice_received` before `.51` dispatch, so repeated cooldown checks notify each human country once while a later human recipient remains eligible for its first notice.

Required MCP event/probability/script validation remains blocked.
Initial tool metadata advertised the routes, but live `hoi4.reference_context` returned `MCP tool hoi4_agent_tools/hoi4.reference_context is not available to the model` after a long pending call.
A subsequent reference-search invocation failed with `TypeError: tools.mcp__hoi4_agent_tools__hoi4_reference_search is not a function`.
The current tool inventory then contained no HOI4 reference, inspect, source, or validation routes.
Follow-up focus-linked work likewise had no callable `hoi4.focus_inspect` or `hoi4.focus_render` route.
No MCP graph, render, comparison, scenario hash, or engine validation artifact was produced by this worker.
This source audit is not an equivalent substitute.
Probability worker was informed before the weighted lifetime/scope repairs and retains the exact baseline `C84B8918...` captured before patching.
Same-scenario probability comparison and final integrated parent review remain required.
No live game was launched, no save supplied, no workbook/CSV edited, and no commit created by this worker.
No unapproved gameplay simplification was made.
The unrun mandatory MCP evidence is a reported blocker, and the rejected equipment-zero proposal was replaced only after explicit parent acceptance.
Effects source audit checkpoint SHA-256 is `89D5A659333491FD82BA3C99FD325AB4EF0281E352AE6137144E89EA126C06FD`, recorded after the final owned lifecycle, attribution, and receipt-accounting tranche while parent integration remains active.

## Direct local source citations

Both required source kinds were read locally after the route gap.
Hashes are SHA-256 revisions of the read files.

| Source and section | Lines | Revision |
| --- | --- | --- |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md`, regular event targets and variable lifetime/scoping | 305-317, 435-449 | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md`, PREV faction precedent and ROOT/THIS/PREV/FROM | 85-94, 260-263 | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md`, equipment debit and create-unit factors | 2253, 3366 | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/effects_documentation.md`, stockpile/manpower, faction, target cleanup/save, create-unit | 1252-1267, 1468-1477, 2293-2301, 2733-2741, 3278-3310, 6496-6514 | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed `documentation/script_concept_documentation.md`, Script Constants | 216-247 | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Installed `common/script_constants/documentation.md`, schema and variable access | 1-62 | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| Installed `events/AAT_Finland.txt`, actual state-scoped units and subsequent distinct stockpile grant | 4650-4674 | `363C53751ED2FBE113FBED5635940F4494B5C67F3BFA0A3787AA327F6CDFDA13` |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md`, named-template guard | 1265 | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| Installed `documentation/triggers_documentation.md`, named-template guard | 4905-4913 | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed `common/scripted_effects/NOR_scripted_effects.txt`, guarded named-template creation | 436-458 | `97B420CACC1628F6ACA85B6608D8F98ACCBA2B22EAA5A0A5CBCCD354D321A57A` |
| `paradox_wiki/National focus modding - Hearts of Iron 4 Wiki.md`, country-scoped ordered completion rewards | 434-441 | `BD989A13237C464F140A0AA671CC42C30A48E84A27DAE791B8914654FB9C6203` |
| Installed `common/national_focus/norway.txt`, scripted helper invoked in focus reward | 936-941 | `8F79AD782160D6BEE22057CAD98BCA497C4BEBAF3404EA3F4F25B09EEE79601B` |
| Installed `events/Generic.txt`, native country-targeted flags | 175-176 | `96D510E119EC0548C3957689395674C7361C6689D2C7D0D65D1C0E024956EC26` |

Targeted country flag syntax is read from Data structures lines 117-125 under the file revision above.
Installed effects lines 6730-6738 and triggers lines 3624-3638 confirm native country-flag command scope and checks.
The manual tier exception is grounded in `docs/specs/007_fury_specs/specs/007_fury_triggerable_scenario_spec.md:16` and its intensity table at lines 67-70, SHA-256 `7DEA944A4E54601F9C897F903C709CEC1DE5BECF9CC14732B835F6805156B12A`.
The spec's absence of an explicit disabled-checkbox exception remained unresolved until the parent accepted the G6 checkbox rule.
`common/scripted_triggers/chaosx_settings_triggers.txt:51` combines disabled-state and tier checks, and its tier helper permits tier below one.
The native faction scope is documented by Scopes line 265 and installed `is_faction_leader` at triggers lines 5525-5533 under the recorded revisions.
The aligned `for_each_loop` index/value contract is read from Data structures lines 1216-1220 under its recorded revision.
Vanilla `events/Generic.txt:798` supplies a `faction_leader` scope precedent under its recorded hash.
Receipt API sections read directly include `common/scripted_effects/chaosx_universal_cost_effects.md:400`, `:430`, and `:467`.
The generic refund API accepts pending recorded/partial rows and treats settled rows as no-ops, which required the parent-owned optional deferral before delivery validation.
Current universal receipt source revision is `D2D04617D66CCB6DBD240E82CCA8B1FABDE24A2FEC7FADC9BFA54C6DE768D7F8`, API Markdown revision `48CA540CF0E44A91CE329849ABA36FA4895C64D0627F1ADA5D3A72FBA7B8E0B2`.
The inspected shared Event 026 source revision after the parent CP/deferral changes is `CDDACA0BD5F845094FBC7247E78C672134DCFD34937069611448AA8C289CECF2`.

Vanilla `common/units/infantry.txt` lines 39 and 48-50 supplies the 1,000-man/100-rifle infantry assumptions.
Vanilla `common/units/engineer.txt` lines 38-61 supplies the 300-man/10-rifle/30-support base engineer assumptions.
The retained `play_current_super_event_audio` alias at `common/scripted_effects/chaosx_settings_effects.txt:4599` forwards to settings-aware `play_current_super_event_sound`.

## Parent integration checklist

- Decision source must preinitialize `fury_depot_payment_success = 0`, call the payer once, and require success before spawning.
- Decision/trigger source must provide `fury_has_depot_spawn_state` and all four resource/actor/reserve gates.
- Resolve the shared composite depot eligibility triggers and use that one predicate in the decision and payment helper.
- Rival eligibility must use the acting PREV country rather than the launcher's ROOT in hostile Settings chains.
- Parent event baseline/pending first-conquest gates, delayed cleanup guards, hostile scheduling suppression, and source docs must match these helpers.
- Resolve source/API dependency gaps before committing the integrated plan.
- Keep required MCP comparison unavailable status explicit if service access remains blocked.
- Check reselection against retained actor milestone flags and completed focus state.
- Parent now resets actor-local milestone/unlock flags before reselection and reloads the focus tree without completed focuses.
- Existing modified templates remain an explicit calibration limitation of the name guard.
- Both focus callers now use the independent one-time recruitment helper.
- Parent's top initialization clears actor-keyed human containment proof before reselection, keeping historical broad contributor flags intact.
- Parent's top initialization also clears actor-keyed watch proof before reselection.
- Preterminal sharing follows the shared trigger's accepted project-pact/cooperation-route representation, rather than assuming a native faction exists before terminal setup.
- Numeric probability/balance comparison for the new Rival Map Claims bonus remains unresolved while mandatory MCP routes are unavailable.
- Final checkpoint constants SHA-256 is `88F9062851295DEF9B73188023674DBDA44B56BCF510034711BF73CDE9779413`, including the two focus refill constants and the shared rival score bonus.
- Discounted-mode physical accounting is implemented through actual receipt components and modeled with real financial APIs.
- Parent removed the top/event normal-variable initializers for Reach, Pact Cohesion, and numeric Compliance Drive.
- Owned source removes all operations on those unused normal variables and all `global.anti_fury_response_pressure` writes.
- The real `fury_compliance_drive` idea remains, including its native modifiers and cleanup.
- Recognition Denial's removed decision leaves no effect consumer, so the two owned recognition payment/effect helpers were deleted.
- The decision owner removes the dead recognition-target trigger, while the legacy shared Event 026 adapters and ordinary cost fallback remain outside this worker's edits.
- Paid Survey Beyond the Border is removed by the decision owner because it had no distinct gameplay consumer.

Skills used: `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-focus-trees`, `chaos-redux-subagents`, and relevant existing-slot wiring sections of `chaos-redux-super-events`.
No skill was created or updated because the documented temporary-output workflow already covered the repeated defect.
