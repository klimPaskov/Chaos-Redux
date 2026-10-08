# Event016 private Teleportation Deployment: existing-consumer feasibility review

Date: 2026-10-08.
Role: chaosx_scripted_system_architect, bounded read-only source audit.
Disposition: audit delivered; the contract below is an unresolved recommendation requiring parent acceptance within the user's authorized Event016 completion scope.
The earlier Teleportation proposal has no recorded acceptance in the inspected authority.
This report does not promote it to an accepted spec.
Parent disposition on 2026-10-08: the full two-site recommendation is promoted into the accepted final completion contract and tracked in `../016_mengele_transit_deployment_acceptance_2026-10-08.md`.
Its map/output and partial-construction dependencies remain queued, while the separate KRG four-cost fabrication transaction proceeds under `../016_portal_transit_fabrication_receipts_2026-10-08.md`.
The dated audit below retains its original reading-point and validation limits.

## Authority and ownership

Authority: `docs/specs/016_brilliant_scientist_specs/specs/016_final_completion_contract.md`, particularly lines 90-142, 196-201, 271-277 and 298-307, and `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_private_custom_deployment_payoffs_2026-09-08.md`, lines 10-43 and 132-155.
The 2026-10-08 Cloning acceptance in that handoff explicitly applies only to Cloning.
The current parent instruction permits a recommendation, not an invented Teleportation approval.
The parent owns implementation, domain comparisons, probability auditing and live evidence.
No Cloning audit, model inspection, model/package work or HOI4 launch was performed.
No gameplay, localisation, asset, index, Git or existing-document write was authorized or performed.
Only this new report is written; its path was checked absent on disk and in HEAD before writing.

Guidance applied: current `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, `.agents/skills/chaos-redux-decisions-missions/SKILL.md` and `.agents/skills/chaos-redux-subagents/SKILL.md`.
No skill was changed.
No linked focus or GUI was inspected or designed; existing focus-unlock flags below are dependencies, not a focus-tree audit.

## Findings that change implementation

1. There is no equivalent private transit construction or fabrication consumer in the inspected scripted effects, triggers, decisions, constants and on-actions.
The legacy Mengele source mentions Teleportation availability, but does not implement a physical transit producer.
Ordinary equipment manufacture, neutral grants, Event019 equipment consumption and CXT stockpile grants are existing consumers and must remain independent.
This finding is bounded to the searched source directories, not proof of every possible external caller.

2. Kruger has two distinct terminal flag families.
Kruger Deployment marks `brilliant_scientist_quantum_transit_terminal` on the primary and secondary facility targets and sets `brilliant_scientist_quantum_transit_network_ready`.
The later paid terminal decision instead marks `brilliant_scientist_krg_transit_terminal`, increments `brilliant_scientist_krg_terminal_count`, and sets `brilliant_scientist_krg_terminal_network_present`.
These are not interchangeable private endpoint receipts.

3. The paid terminal decision physically adds one infrastructure level.
The paid supply-link decision only sets `brilliant_scientist_krg_terminal_supply_network_linked` and `brilliant_scientist_quantum_transit_network_ready`.
It constructs no railway, supply node or other building.
Calling it from a private country would both leak KRG history and advertise supply output it does not deliver.

4. The fabrication output is exactly 180 `teleportation_equipment_1`.
The output helper also increments `brilliant_scientist_krg_portal_transit_batches`.
Its stockpile line is reusable after extraction; its wrapper is not provider-neutral.

5. The current private Deployment pays 120 Political Power, 900 Support Equipment and 3,000 fuel, reserving six civilian factories for 540 days.
It does not pay the truck/train/manpower/XP/military-factory fields also present in the larger shared KRG stage table.
Its output is an operational grant and private completion receipt, with Deployment modifier restoration; it supplies no endpoint or construction.
A repeated operational grant is not a distinct physical payoff after the native Prototype bridge has supplied neutral access.

6. The KRG fabrication precedent has six spendable burdens: 65 PP, 150 support equipment, 50 trucks, 1,000 fuel, 1,000 manpower and four committed civilian factories.
The decision skill's four-cost limit (lines 187-193) prevents copying that recipe unchanged into a new private adapter.
The proposed private recipe below is explicitly a parent tuning choice, not an accepted reinterpretation of KRG economics.

## Current source and dependency map

Paths in this section are relative to the repository root stated in the delegation.

| Source / lines | Exact symbol or surface | Current inputs, output and dependencies |
| --- | --- | --- |
| `common/scripted_effects/016_brilliant_scientist_project_effects.txt:554-578` | Teleportation branch of shared stage output | KRG family/stage selectors; Deployment writes both quantum terminal flags and shared ready/history state. No physical building here. |
| `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt:68-113` | `brilliant_scientist_has_teleportation_force_history_deployment`, `brilliant_scientist_has_teleportation_force_deployment` | Stage array index 6, KRG personal or country history, shared network flag and an owned quantum terminal. Not a private eligibility API; owned alone is not controlled. |
| `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt:34-59` | `brilliant_scientist_krg_construct_transit_terminal` | Owned-state target; active KRG and focus unlock; count below two; heavy payment; 120 days; four CIC; infrastructure +1 and KRG receipts. |
| Same file, `90-115` | `brilliant_scientist_krg_link_terminal_supply_network` | KRG focus locks and terminal counter at least two; heavy payment; 120 days; four CIC; 180-day re-enable. Flags only. |
| Same file, `213-242` | `brilliant_scientist_krg_fabricate_portal_transit_batch` | KRG operational/focus gates; AI-active OR linked-network flag; project-batch payment; count below four; 90 days and 30-day re-enable; four CIC. |
| `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt:54-65,175-178` | `brilliant_scientist_krg_pay_heavy_material_cost`, `brilliant_scientist_krg_pay_project_batch_cost`, `brilliant_scientist_krg_complete_portal_transit_batch` | Debit-only helpers contain no KRG history writes, but no receipt, revalidation or actual-payment result; final helper mixes stockpile output and KRG count. |
| `common/scripted_triggers/016_brilliant_scientist_kruger_state_decision_triggers.txt:237-251,328-353` | Heavy/batch affordability; `brilliant_scientist_krg_is_valid_owned_construction_state`, `brilliant_scientist_krg_is_valid_terminal_state` | Ownership/control and infrastructure above zero; excludes existing KRG terminal and temporal anchor. No infrastructure slot/cap test, industrial requirement or supply-node test in terminal predicate. |
| `common/decisions/016_mengele_teleportation_stage_decisions.txt:117-155` | `mengele_event016_teleportation_deployment` | Advanced Programs; native `days_remove`; literal private family/stage start/cancel/finish callbacks; four-cost private stage quote. Currently country-targetless. |
| `common/scripted_triggers/016_mengele_teleportation_stage_decision_triggers.txt` | Deployment visibility, requirements, affordability and matching-receipt gates | Private Prototype predecessor; no existing Deployment; own family receipt empty; inclusive resources; exact index 6/stage match. Cancellation tests provider and receipt, not endpoints. |
| `common/scripted_effects/016_mengele_project_stage_effects.txt:696-787,855-867,1092-1117,1871-1875` | `brilliant_scientist_mengele_begin_project_stage`, `...cancel_project_stage`, `...finish_project_stage`, `...grant_custom_stage_package`, `...apply_family_stage_output` | Three direct-paid snapshots and native CIC commitment; receipt consumed before settlement/refund. Teleportation Deployment repeats neutral grant, records private history; no transit output. |
| `common/scripted_triggers/016_mengele_project_stage_triggers.txt:16-56` | `brilliant_scientist_mengele_project_stage_provider_is_valid` | Existing country, genuine registry/program/idea identity, no KRG current host, closed/rejected/defeated/incident/world-end states excluded. Reuse verbatim. |
| `common/scripted_effects/016_mengele_project_bridge_effects.txt:16-34,107-111,136-149`; `016_mengele_native_prototype_effects.txt:622-630` | `brilliant_scientist_mengele_grant_native_custom_operational_package`; exact quantum-transit wrapper | Theory + Prototype + exact completed native source OR fresh native receipt feeds neutral Portal family grant with Mengele provenance. This is already the operational-access boundary. |
| `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt:38-44`; equipment source `140-209` | `chaosx_grant_custom_operational_technology_core`, `chaosx_custom_technology_portal_operational` | Neutral grant supplies existing Portal technology and durable entitlement. Equipment production has inline neutral branches; do not replace them with private Deployment gates. |
| `common/scripted_triggers/016_brilliant_scientist_raid_triggers.txt:28-35` | `brilliant_scientist_portal_raid_actor_is_ready` | Current original Portal raid requires existing weaponization technology plus the Quantum Transit Raiders template; no private history/network requirement. This is a source/spec distinction to retain, not permission to move raid gates in this tranche. |
| `common/scripted_effects/016_mengele_project_stage_effects.txt:1934-1985` | `brilliant_scientist_mengele_cleanup_provider_receipts` | Existing per-family cancellation/refund, native selection and incident cleanup. Hook any private transit cleanup into this existing boundary; do not add periodic world hooks. |

## Construction and receipt feasibility

Native `add_building_construction` is a STATE effect (R3/R4).
The installed command prose confirms scope but does not enumerate its argument readers.
The wiki documents dynamic numeric `level`, instant construction, province selection and supply-node province filtering.
Use the existing infrastructure result only with unlocked infrastructure-level capacity and explicit owned-and-controlled state checks.
A supply node is a province building with province maximum one; an arbitrary state flag cannot substitute for it.
This recommendation uses existing supply nodes, not new supply-node construction.

Native `build_railway` and `can_build_railway` support state or province endpoint fields, explicit paths, allied-only restrictions, ordered fallbacks and controller path costs (R1/R2/R6).
A negative controller cost denies that controller.
An allied-only route alone does not guarantee the intervening territory belongs to the payer.
Copy the actor-only controller predicate structure from the inspected Event035 rail precedent if that restriction is accepted, repeating the same path specification in preflight and output.
Treat its scores as path costs, not selection probabilities.
Native `has_railway_connection` checks connectivity (R7); the cited prose does not prove healthy supply throughput or a required railway level.
Do not describe structural connectivity as proof of undamaged supply or instantaneous unit teleportation.
The installed `has_railway_level` section (triggers documentation, 4628-4640) tests whether a state contains any railway at or above the level; it does not prove that the entire selected route has that level.
A country-wide `num_of_supply_nodes` count is similarly not endpoint proof.
State `supply_node` building counts are documented by `building_count_trigger` (1830-1839), but exact node province binding and whole-corridor live validation still need map/engine evidence.

Useful existing source precedents are:
- `soviet_collapse_build_capital_railway_to_this_state`, `common/scripted_effects/005_soviet_collapse_effects.txt:192-238`: country-held numeric state IDs, `var:` state endpoints and meta-injected rail level, then scratch cleanup.
- Event035 `common/scripted_effects/035_great_depression_public_works_effects.txt:39-68,159-200` and `common/scripted_triggers/035_great_depression_public_works_triggers.txt:95-149`: saved partner scope, owner/controller checks, denied foreign controllers, buildability, physical result comparison and exact authorization.
These effects write their own event history and must not be invoked from private Event016.
- Vanilla `PHI_american_intervention_nationalize_railways`, `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\PHI.txt:460-525`: native timer followed by physical rail output in `remove_effect`.
The payload at 502-513 was read directly.
- Vanilla `common\decisions\ETH.txt:1874,1927` uses `state_target = any_owned_state`, matching the installed KRG source.
The older installed decision prose labels the restriction `state_trigger` (R5); the actual vanilla precedent supports retaining `state_target` rather than assuming that documentation heading is an alias guarantee.

Regular event targets expire with their effect chain and cannot alone bridge separate selection clicks and a 540-day decision timer (R9 and the regular-target reference below).
Store origin/destination as regular country-owned scope variables, with explicit existence/type, ownership, control, distinctness and actor checks.
Use temporary regular event targets only while passing verified endpoints through one synchronous effect chain.
Avoid a global singleton target: multiple countries can own private providers concurrently.
Use state receipts targeted to the original actor, plus country-held endpoint and generation records, so conquest does not transfer the private entitlement.
Reconstruct synchronous aliases from these records after reload; do not infer endpoints from KRG facilities.
Temporary outputs must be caller-preinitialized at every nested boundary under the event skill's documented call-frame rules.

The shared dynamic registry was inspected first.
`remove_support_equipment_from_stockpile` and `remove_fuel_from_stockpile` are reusable debit primitives, but negate their input in place and supply no success/actual-payment receipt.
Preserve the positive payment snapshot independently.
They are not a complete transaction/refund API.
The existing building-damage helper is damage-only and supplies no construction/railway capability.

## One recommended bounded acceptance contract

Route-specific implementation remains blocked pending map output and verified endpoint binding.
The following is one coherent proposal for parent acceptance, not current behavior or a claim of user approval.

**Commission one private pair with the existing Deployment payment.**
Add free origin and destination selection to the existing Advanced Programs category; retain the current Deployment decision ID, 540-day native timer, costs and literal family/stage ownership.
Origin is an owned-and-controlled industrial state with an existing supply endpoint.
Destination is a distinct neighboring owned-and-controlled industrial or supply state with an existing supply endpoint.
Both require capacity for one additional infrastructure level and a buildable actor-controlled local railway.
Neighboring endpoints bound this to a local physical logistics route instead of an arbitrary cross-continent rail grant.
The chosen state IDs must bind to actual inspected supply-node provinces; the native state-endpoint picker prefers capital before nodes, so merely naming two states does not prove hub-to-hub routing.
Prefer explicit saved start/target province IDs once that mapping is verified.
Select both before starting; freeze the pair and intended physical levels at payment.
No alternative flag-only, extra modifier, free stockpile kit or ordinary-access gate satisfies the payoff.

On successful expiry, deliver exactly +1 infrastructure in each endpoint and a native level-2 railway connection between their inspected supply endpoints.
The two infrastructure increments ensure tangible additional construction even if a level-2 connection already exists.
Do not claim the railway was upgraded if its actual before/after level did not change.
Validate both states and the complete permitted route again before any construction.
Record actual before/after infrastructure and the railway result, then publish private commissioning history and the exact `mengele_event016_teleportation_deployment_completed` receipt.
Failure before physical output refunds the matching original direct stage payment and releases only the native reservation.
If competing construction makes an increment impossible, reject/refund rather than clipping to zero or manufacturing a terminal flag.

Use the existing stage finish API's snapshot/receipt-consumption contract.
Insert the physical preflight and output into the Teleportation branch, with caller-owned success/recovery outputs.
The completed-receipt test is appropriate for subsequent production, not for this first stage reward; requiring it before commissioning would deadlock Deployment.
The existing Prototype predecessor and strict provider gate authorize the paid initial reward.
Keep the neutral API grant and learned access independent.

**Expose one supplemental paid fabrication action using that pair.**
Require strict private provider validity, exact private Deployment history, neutral Portal entitlement, both private actor-bound endpoints, real current ownership/control, physical infrastructure and valid railway proof.
Use one active private fabrication receipt, one native 90-day timer, four committed CIC, and a 30-day cooldown.
Recommended quote: 65 PP, 200 Support Equipment and 1,000 fuel; output 180 `teleportation_equipment_1`.
This is four spendable cost types including CIC; no truck, manpower, train, XP or hidden fifth fee.
Use actual positive paid snapshots and exact concrete equipment accounting for refunds; the existing archetype debit helper alone does not witness which inventory was removed.
Use a private maximum of four successful batches, with a private persistent success counter; failed/cancelled attempts do not consume the cap.
These values and the neighboring-site restriction are proposed tuning choices for parent acceptance.
Ordinary factory production, existing raids and neutral research/manufacture never read this private counter or private endpoint history.

**Suspend supplemental work on site loss without revoking knowledge.**
A captured/destroyed endpoint or broken qualifying route cancels unresolved private work once and disables this supplemental consumer.
Permanent paid stage/commissioning history and already-produced equipment survive.
Reacquisition and repair can restore the same pair's live eligibility without free replacement infrastructure.
A new owner cannot use the former owner's targeted state receipt.
Provider departure invokes existing provider cleanup, with no site transfer, no shared/KRG flag clear and no automatic replay of an output.

For an already genuine private Deployment history without a physical commissioning receipt, recommend an explicit one-use commissioning claim under the same pair selection/physical checks, funded by the recorded paid stage rather than charging Deployment twice.
It creates no native project or new stage receipt and cannot infer authority from neutral technology alone.
This migration choice also requires parent acceptance; do not silently award construction during availability reconciliation or modifier restoration.

## Proposed helper map and migration seams

All names below are proposed, absent implementation claims.
No public central router or wrapper skill is needed.

| Proposed helper | Scope and inputs | Outputs/defaults | Side effects / planned direct callers |
| --- | --- | --- | --- |
| `brilliant_scientist_transit_endpoint_is_valid` | STATE; explicit paying COUNTRY, role, intended increment | Boolean, fail closed on missing/invalid input | Read-only ownership/control, industry/supply, slot and site tests; private selection, start and finish. |
| `brilliant_scientist_transit_route_is_valid` | COUNTRY; verified two endpoints and explicit rail specification | Boolean, no inferred facility | Read-only buildability/control/connectivity; private Deployment preflight and fabrication live gate. |
| `brilliant_scientist_apply_transit_construction` | COUNTRY; two explicit state scopes, snapshotted infrastructure targets and rail specification | Caller-owned `transit_construction_applied = 0` plus component outcomes | Physical native buildings/rail only; private Deployment branch. Add a KRG caller only if parent explicitly accepts correcting its flag-only link. |
| `brilliant_scientist_add_portal_transit_equipment` | COUNTRY; explicit positive amount | Caller-owned delivered amount, zero on rejected input | Only adds existing equipment; KRG completion wrapper and private batch finish. KRG wrapper retains its own counter. |
| `brilliant_scientist_mengele_begin_transit_batch` | COUNTRY; private pair, quote and current serial | Caller-owned start result; no defaults for quote | Publish exact active actor/pair/payment/output receipt; charge once; new private fabrication decision. |
| `brilliant_scientist_mengele_finish_transit_batch` | COUNTRY; literal action identity and matching active receipt | Exact settlement result | Consume receipt, output snapshotted quantity once, increment private count and cooldown; native expiry only. |
| `brilliant_scientist_mengele_cancel_transit_batch` | COUNTRY; exact active receipt | Refund/closed result | Snapshot, clear, refund actual direct payment once; native cancellation and existing provider cleanup. |
| `brilliant_scientist_mengele_cleanup_transit_receipts` | Original COUNTRY; selected/pending/live records | Idempotent cleanup | Clears transient selectors/payments and retires only own live receipts as appropriate, preserves history and learned tech; existing `...cleanup_provider_receipts`. |

Place feature orchestration in an Event016-owned effects file and matching markdown contract.
A genuinely neutral construction/output extraction with multiple direct consumers may remain Event016-owned and be indexed from `common/scripted_effects/chaosx_dynamic_effects.md`; do not move broad KRG decision systems into the shared registry.
Document scope, explicit inputs, caller-owned result storage, defaults, side effects and one real call-site example.
First extract the equipment stockpile line while retaining the KRG counter in its current wrapper.
Then implement private endpoint selection/receipt storage, connect the existing Deployment output branch, and add the private fabrication wrapper.
Do not broaden the KRG category to private countries or call KRG initialization, stage grants, supply-link or batch-completion history wrappers.
Leave the parent Cloning tranche untouched.

Constants belong in a feature-owned category under `common/script_constants/`, e.g. `mengele_event016_transit`: endpoint count 2; infrastructure increment 1; rail target 2; supplemental days 90; cooldown 30; CIC 4; PP 65; support 200; fuel 1,000; output 180; successful-batch limit 4.
Retain existing authoritative Deployment cost/duration constants.
These are proposed values, not added constants.
Only mirror CIC and fixed AI hint values as file-scoped macros where the existing native consumers reject `constant:` tokens.
For unverified railway fields, stage numbers in temporary/normal variables and use explicit meta text only where the reader requires literal injection; dynamic `level` or `constant:` parsing is not established by sparse native prose (R10/R11/R13).
Do not accept a silent fallback to another endpoint, route or output.

## Economics and existing presentation / CXT reuse

Current KRG heavy material payment is 200 support, 50 trucks and 1,500 fuel, plus native 65 PP/four CIC for each terminal or supply link.
Building two paid terminals plus the flag-only link therefore costs 195 PP, 600 support, 150 trucks and 4,500 fuel, with 1,440 CIC-days across three 120-day actions.
It is not proof of a real three-action railway network.
Private Deployment already commits 3,240 CIC-days and pays 900 support/3,000 fuel/120 PP.
Using that existing payment for the pair's construction avoids selling only an entitlement to pay again.

The equipment source is `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt:47-59,121-139,213-220`.
Portal equipment build cost is 6 IC, with steel 2, tungsten 2 and chromium 1 in the ordinary recipe.
Thus the existing 180-item output represents 1,080 nominal equipment IC.
Vanilla support equipment costs 4 IC (`common/units/equipment/support.txt:23`) and the ordinary truck archetype 2.5 IC (`motorized.txt:26`).
No mod override of those two archetype definitions was found in the bounded equipment search.
KRG's 150 support plus 50 ordinary trucks nominally represents 725 IC.
Proposed 200 support is 800 IC, about 10.3% more nominal equipment input, consolidating the material burden rather than copying six costs.
PP, fuel and four CIC for 90 days remain real additional sacrifices.
Four successful batches yield at most 720 supplemental equipment and spend 260 PP, 800 support and 4,000 fuel with 1,440 CIC-days.
These arithmetic comparisons explain the proposal; they do not establish engine production efficiency, resources, strategic balance or refund execution.

Use existing `mengele_advanced_programs_category` in `common/decisions/categories/germany_mengele_categories.txt:80-83`.
Existing stage localisation is `localisation/english/016_mengele_teleportation_stage_l_english.yml`, including Deployment requirements/cost/effect keys and integer constant getters.
Revise its payoff text only with implementation; add actor-specific endpoint names and separate exact costs/blocked/tooltip strings for fabrication.
Existing reusable decision icon tokens are `GFX_decision_brilliant_scientist_project_teleportation_deployment`, `GFX_decision_brilliant_scientist_krg_portal_terminal` and `GFX_decision_brilliant_scientist_krg_supply_depot`.
The latter two are registered in `interface/016_brilliant_scientist_kruger_state_decisions.gfx:30,6`.
This audit read token definitions only, not textures, models or unit assets.
No new image, category, GUI or asset package is needed.

CXT already registers `teleportation_equipment_1` and `portal_raider` in `common/scripted_effects/016_alien_infantry_cxt_test_effects.txt:198,213`, and its explicit stockpile fill includes Portal equipment.
`chaosx_cxt_event016_enable_mengele_provider_fixture` (same file, 25-48) and `chaosx_test_country_event016_mengele_provider_fixture_decision` in `common/decisions/chaosx_test_country_debug_decisions.txt:49-60` expose a genuine private provider without manufacturing stage/native completion history.
`chaosx_cxt_event016_probe_native_inventory` is an observation-only native inventory probe; `docs/testing/chaosx_test_country.md:224-234` expressly limits its proof.
Extend explicit player-triggered observation of endpoint/payment/result receipts if needed; add no carrier, family registry entry or periodic grant hook for an existing family.
Current CXT registration/stockpiles do not prove a paid private route, native clock or cancellation refund.

## Adverse scenarios and required implementation evidence

| Named scenario | Required result |
| --- | --- |
| `transit_neutral_prototype_only` | Neutral/native Prototype access and ordinary manufacture remain available; private construction/batch access remains absent. Preserve current separate native raid technology gates. |
| `transit_external_grant_only` | Full neutral grant supplies no private Deployment or endpoint history. |
| `transit_two_site_success` | Exact quoted stage payment and original 540-day timer deliver both actual infrastructure increments and inspected railway; only then private commissioning/stage success. |
| `transit_duplicate_stage_callback` | No second construction, history write or charge; incompatible family/stage callback cannot clear another row. |
| `transit_target_invalid_before_payment` | Same state, unowned/occupied site, missing supply endpoint, full infrastructure capacity or foreign-controlled corridor refuses without debit. |
| `transit_target_invalid_after_payment` | No output to captor; matching stage/batch payment refunded once; native CIC released without granting factories. |
| `transit_slot_filled_mid_timer` | No zero-increment terminal receipt; refund before any output or exact partial-output recovery if native failure occurs after a component. |
| `transit_batch_exact_quote` | Below/exact/above costs agree in display, availability and live entry; own reservation not counted twice; resource depletion after payment does not require repurchase at expiry. |
| `transit_batch_duplicate_and_stale` | One active receipt; second start/cancel/finish is harmless; stale owner/pair/action never consumes current work. Same-action generation isolation requires actual callback evidence. |
| `transit_site_loss_reacquire` | Supplemental production suspends on capture/destruction/route loss, resumes only with own physical receipts and repairs, and grants no replacement buildings. |
| `transit_provider_cleanup` | Original owner gets exact unresolved refund once; historical stage, output equipment and neutral technology persist; no KRG/history/other-family writes. |
| `transit_krg_private_coexist` | KRG wrappers retain existing costs/output/count; private count does not satisfy KRG caps/achievements; private endpoints do not set either KRG terminal flag family. |
| `transit_fourth_and_fifth_batch` | Fourth paid output succeeds, fifth refuses; cancellation does not consume lifetime allowance. |
| `transit_reload_and_late_native_output` | Exact endpoints/paid values survive reload; native Prototype cancellation/reselection and delayed-output ownership gaps remain visible rather than being hidden by new receipts. |
| `transit_partial_physical_commit` | Retain component results and spent-payment proof; no full refund plus retained free construction, no replay of delivered increments and no demolition of someone else's later construction. |

Run actual-source transaction tests through the real selectors, quote, debit, refund, physical-result adapters and cleanup; mock only documented native primitives and disclose the boundary.
A slot/buildability preflight is not atomic engine rollback.
If a native construction call fails after another component was delivered, retain a private pending commissioning/recovery record and component results, with no final completion or blind refund.
Retry only undelivered components through an explicit reviewed player action.
The present generic finish helper clears the stage receipt before applying output and refunds when its result stays zero; it needs an explicit partial-output state before it can safely host multi-component construction.
This is a concrete implementation seam, not approval for a generic transaction scheduler.

Current KRG terminal/batch decisions have cancellation predicates but no direct-payment refund receipt/cancel effect; the supply-link decision has neither explicit cancellation predicate nor physical revalidation.
Do not inherit those gaps as the private transaction standard.
Current private stage callbacks identify family and stage, not an immutable native callback generation.
The accepted native ownership amendment (`docs/specs/016_brilliant_scientist_specs/specs/016_native_prototype_ownership_amendment_2026-10-03.md:19-27,59-61`) still leaves native start/cancel synchronization, persistence/reselection and delayed-output isolation unresolved.
Private endpoint receipts cannot close those native gaps.


## MCP evidence, exact gaps and completion boundary

Connected reference, source, event, map, probability and script-validation tool schemas were discovered from the exposed tool list before use.
Workspace ID: `mod_chaos_redux_ea3b2d67c2c0`.
No job/helper-expansion/task-negotiation route, rewrite tool, GUI render or map mutation was used.

Successful source lookup identified one exact KRG completion helper at lines 175-178 and its one indexed decision caller at line 241, workspace index revision `e48072d49d9032bcd239a6c3e1f0b0b8b02741a1b9fdcf519630dc7a080b36f8`.
The lookup reported `referencesComplete = false` and 20,107 unresolved reference findings; its exact caller observation is not complete whole-repository consumer proof.
Private-stage structure lookup returned revision `54c722329c02d3e3670afc6b8f3c5b141b85ccfebbd6932a861f73dce228f97b`.
The nested query using that expected revision returned `SOURCE_REVISION_STALE`, current revision `e48072d49d9032bcd239a6c3e1f0b0b8b02741a1b9fdcf519630dc7a080b36f8`; the revision-free retry then timed out after 600 seconds.
Underlying Teleportation source was read directly and its raw hash rechecked unchanged; no stale index result is presented as a stable workspace snapshot.
Vanilla structure lookup found `PHI_american_intervention_nationalize_railways` at `game:common/decisions/PHI.txt:460-525`, same later index revision, but its nested payload lookup timed out after 600 seconds.
A narrower three-line lookup was attempted; detailed payload evidence in this report is the cited direct local read.

Private event inspection used `selector = { kind: file, sourcePath: common/decisions/016_mengele_teleportation_stage_decisions.txt }`, helper expansion false, depth 1, nodes 8, edges 10.
It returned `EVENT_INSPECTED_PARTIAL`, focused analysis and zero expanded helpers; whole-workspace helper/lifecycle projections were deferred.
Two earlier selector argument rejections were corrected using the returned live validation requirements; they are not service failures.
Event report revision: `db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5`.
Report artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/eb70a8618535234cca36f1edaf466106381fd813d1840704c2d70fc677867d21/6f52a394a9d9b75c2547a02ea5da5028af801f474152b23ecf618830fccc5c35/event-scan-db07bcddfa36.json`.
The server also returned the workspace graph artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/77cb0ba17d9f169c19ee52572d30e46e25940e67acd4ac8c775a3038a45b5beb/113ab135dc4d7bb2a2bb5eef4289a29641b74e3f701686652d5fc359922417bd/event-graph-db07bcddfa36d3e812d8f033f1f08177ead60ee2d6bc5c59d90d89970b63e2a5.json`.
Its 96,333,999-byte graph was neither requested as a wide helper graph nor opened; no complete-graph or lifecycle acceptance is claimed.
A corrected KRG file scan was separately requested with helper expansion false, depth 1, nodes 3, edges 4.
No final result was observed before report sealing; the client observation cell was stopped, with no server job handle or claim that the server analysis was cancelled.
KRG event-domain evidence remains unresolved; the successful private file inspection is not substituted for it.

`hoi4.map_inspect({ lookupOnly: true, includeOverview: false, stateIds: [64,65], queryLimit: 2 })` returned exactly `timed out awaiting tools/call after 600s`.
The narrower lookup of state 64 only, limit 1, also returned `timed out awaiting tools/call after 600s`.
Both map requests therefore have final transport timeout results, not usable map evidence.
States 64/65 were inspection probes, not chosen or accepted private endpoints.
There is no returned topology, adjacency, supply-node or railway artifact proving this proposal.
The map contract is blocked, and local construction references are not equivalent map evidence.

The initial probability discovery requested `decision_ai_will_do` for only `mengele_event016_teleportation_deployment`.
It returned `requested_adapter_empty`, zero selected candidates, and suggested `mission_ai_will_do`, classifying the four timed stage decisions under that adapter.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/942770f8abfdddfdab4c7270652cb392eaca32fd34d38dc2936f5d7b688eb62d/cd7233c989f7e55c63d98c522d876c3a12e877299e00dd67aa0c20a90d2e31fd/probability-inspect-6979d81d3d4c.json`.
Normalized source hash: `6979d81d3d4c11c58783d38458c2294e8bdd6c8a63fbe2dfb06e38323ffdf6cc`; source revision `4dd7316586d148c231670041356f65f63deb5308dba7e6dad9d706e8cfc23483`.
The corrected one-candidate `mission_ai_will_do` inspection timed out after 600 seconds; a further bounded observation retry used the same minimum one-candidate scope because no finer confirmed selector was available.
Empty discovery inputs are not complete AI scenario coverage.
No AI weight was designed, changed or numerically evaluated; this is not a probability-auditor evidence pass.
The orchestrator must route baseline/evaluation/sweeps and any post-patch comparison through `chaosx_ai_probability_auditor` with the named scenarios above, preserving exact before bytes and scenario identity.
Willingness scores are not click probabilities.
New endpoint availability and new fabrication candidates also require that audit even if a copied base value is unchanged.

`hoi4.script_validate` on one state-scope infrastructure construction snippet returned `SCRIPT_CHECK_PARTIAL`, `valid = null`, `parametersChecked = false`, with `SCRIPT_ARGUMENT_BLOCK_UNCHECKED`.
Only syntax, native command kind and declared STATE scope were checked.
Documentation database revision: `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.
It is not argument, slot, construction-result, transaction or runtime proof.

Reference context included installed and wiki sources but omitted Localisation at limit 6; targeted GetName search/read and direct native contextual-localisation reading addressed that source omission.
`script_doc` coverage was unavailable (zero files); installed `game_doc` and offline wiki references were available.
The regular-target, variable-lifetime and native contextual-localisation MCP reads each timed out after 600 seconds.
They were retried at one-line bounds and read locally with matching raw revisions as shown below.
The two-result railway-level search also timed out after 600 seconds and was retried at one installed-source result.
One-line native-localisation, variable-lifetime and regular-target reads, two-line private-stage lookup, three-line vanilla payload lookup, one-result railway-level search and the minimum one-candidate probability retry each returned no tool result within a bounded 30-second observation window.
Their final server outcomes are unobserved, rather than asserted to have failed or completed.
The prior 600-second failures remain the exact route blockers.
All relevant local text is reference data, not instructions.

### Successfully read MCP reference sections

| Ref | Exact Windows path | Read lines / section | Source revision |
| --- | --- | --- | --- |
| R1 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 2535-2571 (build_railway) | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| R2 | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 373-373 (build_railway) | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| R3 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 839-847 (add_building_construction) | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| R4 | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Effects - Hearts of Iron 4 Wiki.md` | 3614-3614 (add_building_construction) | `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c` |
| R5 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\_documentation.md` | 1-46 (Country Decisions) | `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019` |
| R6 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 1884-1919 (can_build_railway) | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| R7 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 4603-4627 (has_railway_connection) | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| R8 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md` | 2901-2915 (free_building_slots) | `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29` |
| R9 | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md` | 263-269 (Event targets) | `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4` |
| R10 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md` | 216-222 (Script Constants) | `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7` |
| R11 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\script_constants\documentation.md` | 1-34 (Constants) | `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c` |
| R12 | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Scopes - Hearts of Iron 4 Wiki.md` | 32-64 (Types) | `18ef5249e4991f5427eca9ec4a2f66dd47f51e26a491c730adc622f1f5db1b49` |
| R13 | `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\effects_documentation.md` | 4833-4852 (meta_effect) | `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af` |
| R14 | `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Localisation - Hearts of Iron 4 Wiki.md` | 564-564 (GetName) | `1a8f72362a34b4bb653186746b9fae0b98e463205cb02f12ccf2c3d9ccd3a064` |

### Additional direct reads after route timeout / sparse documentation

- `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux\paradox_wiki\Data structures - Hearts of Iron 4 Wiki.md:303-305,435-449`: regular targets, call-frame lifetime and regular-variable scoping; raw SHA-256 `62273f37ed30e5479acb331a8973f48dadc1867c4913c8a940e3e790e7af32d4`, matching returned wiki revision.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\script_concept_documentation.md:125-159`: contextual/scripted scope localisation; raw SHA-256 `884bfe9f9207ea4b25b36b5129d0f77d11d4b2f7eb0592587767ec58d24930c7`, matching returned reference revision.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\triggers_documentation.md:1830-1839,4628-4640,6840-6847`: building counts, limited railway-level predicate, country-only supply-node count; reference revision `7d27ed77dadaf3a213a4b3e2c624bf9c02dae495317abe8eee833b27c2d1de29`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\documentation\dynamic_variables_documentation.md:1101-1140`: building/undamaged-building/infrastructure readers; raw SHA-256 `538525747f0c285062c9ce8db14b4e07c3cf6bac1013115fa4f57291cb4ebdda`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\decisions\PHI.txt:460-525`: timed rail precedent; raw SHA-256 `468ae9a96eacd0e6339a810931a69c0228ad08eb652f8a0a0d58bcf48044a914`.
- `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\common\buildings\00_buildings.txt:34-47,98-124`: native infrastructure cap five, province supply-node cap one, physical rail cost definition. Values are source facts, not permission to exceed caps.

### Task source identities

Initial HEAD observed: `03447df6c5e4226525d2c26dc450f103d2297e78`.
Final HEAD observed at source sealing: `0a21069f8c89d24466a86fdbd1959ef522860a22`.
Parent checkpoint reports Cloning throughput commit `c9010602374a24bcb63aa3e70e3962843adcaa8f` and index reconciliation; no Cloning audit or source change is duplicated here.
The seven Teleportation/KRG/equipment source hashes below were rechecked unchanged at final sealing, including the exact private grant and Deployment receipt branches.
This is a shared-tree reading point, not an immutable whole-workspace audit baseline.
Raw SHA-256 identities:
- `common/scripted_effects/016_mengele_project_stage_effects.txt`: `209ee22fc5461e9e07463c39349723685510052294ee2e8ca4f6db42a4a6425c`.
- `common/decisions/016_mengele_teleportation_stage_decisions.txt`: `55c65ca1d2e143c414c0131c149b0f561d97090be1ee48df146ae3fd4ceb0f42`.
- `common/scripted_effects/016_brilliant_scientist_project_effects.txt`: `7588dcb2090e25fdca3c863cc19878b417f13d5bdf5281d5295a78e1acc3de0f`.
- `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`: `40f6793acffa140b7eb42582e10af206638bbbbb7f35783c99cccdd83c0bbcdb`.
- `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt`: `ae9980b982ae360c347ce1e1d78e16598d10930c47b650ac0afda69e3132b1e9`.
- `common/script_constants/016_brilliant_scientist_kruger_state_decision_constants.txt`: `c7f4b8af4aeb9ffcf208cea948b9390aff72445340ca8faf3ad403d199a28978`.
- `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`: `4687027a01dbc8cd1bee2ea0a872ec418fa85628ef2c554857a2c6320285a2e0`.
- Final contract: `711b3b7fb61971d5c5ca12bb8f67b72d16fd49dc4f32f3dcf8c02681e8d85bab`.
- Prior payoff handoff: `cdfe7c897ca1ec476606bd3a8232381063657d7deed312792043d996a4fcd0cf`.

### Completed, blocked and skipped work

Completed: bounded source/caller inspection, KRG-history separation, construction/reference feasibility, cost/output arithmetic, existing-consumer and CXT/presentation reuse review, helper/receipt/migration proposal and adverse-scenario contract.
Only this report is added; no helper, call site, constant, cleanup code or gameplay text is implemented.
No gameplay simplification or fallback was applied.
The proposed changes remain explicitly unresolved rather than being substituted for accepted gameplay.

Blocked or unresolved: actual map topology/supply/endpoint evidence; whole-route level and damage proof; native argument semantics beyond sparse prose; multi-component construction settlement and partial recovery; exact actual-payment/refund execution; native reservation/callback ordering and generation identity; outstanding native Prototype cancellation/reselection ownership; parent acceptance of the proposed payoff and tuning; probability-auditor baseline/comparison and domain/audit acceptance.
Skipped intentionally: implementation tests for unwritten code, broader event/helper graphs, focus/GUI/technology rendering outside this bounded surface, Cloning work, assets/models and all game launching.
No paid private transit completion, balance approval or live readiness is claimed.

