# Mon river-office closure and PUSA education payoff

Date: 2026-10-07.
Disposition: `unresolved` recommendations for parent acceptance and implementation.
The user authorized full Event 006 implementation and recommended choices.
Recommend accepting these two bounded consequences, then stopping broad expansion of these findings.
This is a completed planning handoff, not gameplay completion or final engine evidence.

## Mon: commission the river services

Add one paid capstone decision, `independence_wave_iax_signature_commission_river_services`, to `independence_wave_iax_mon_category`.
The existing focus `independence_wave_iax_focus_place_river_works_under_the_office` authorizes it through its existing `independence_wave_iax_signature_river_charter_complete` receipt.
No additional focus or route is required.
The capstone joins the existing schools, transport and frontier institutions into a domestic service administration.

**Exact gates:** require `can_start_independence_wave_iax_signature = yes`, `independence_wave_iax_signature_river_office_route`, `independence_wave_iax_signature_river_charter_complete`, `has_idea = independence_wave_iax_mon_school_trust`, `independence_wave_iax_signature_transport_complete`, and `independence_wave_iax_signature_border_watch_complete`.
Reject the local-council route, a commissioned receipt, or a durable award receipt matching the current generation.
Selection additionally requires `independence_wave_signature_modules_project_slot_open` and `can_pay_independence_wave_administration_standard_cost`.
Reuse the existing start helper's persistent exact IAX/IW-161 origin, framework/force generation and owned, controlled capital-anchor proof.
Foreign school delegates and BRM/SIA existence are not requirements.

**Payment and duration:** invoke `independence_wave_decision_pay_administration_standard` once at selection for 20 CP and 5,000 manpower.
Reserve two civilian factories through `civilian_factory_use = constant:independence_wave_decision_cost.civilian_factory_standard` for `days_remove = constant:independence_wave_decision_duration.standard`, currently 120 days.
These are three committed resource types for one fixed service-staff project at the package anchor.
Put the factory-affordability check at the selection boundary, rather than rechecking it after the native timer has already reserved the same factories.
The parent must verify native reservation ordering in its action-contract test.

**New identifiers:** use triggers `can_independence_wave_iax_signature_commission_river_services` and `can_independence_wave_iax_signature_finish_river_services`, plus effects `independence_wave_iax_signature_start_river_services`, `independence_wave_iax_signature_complete_river_services` and `independence_wave_iax_signature_clear_river_services_project`.
The active flag is `independence_wave_iax_signature_river_services_project_started`.
Snapshot normal variables `independence_wave_iax_signature_river_services_project_package_id`, `independence_wave_iax_signature_river_services_project_generation` and `independence_wave_iax_signature_river_services_project_anchor_state` from the current package, generation and anchor at selection.
Add the started flag to the existing shared project-slot occupancy predicate.
Selection writer guards must reject duplicate starts before any debit.

**Expiry:** require the continuing route/institution prerequisites and presence of the started flag and all three snapshot variables.
The saved package must equal both the current package and `constant:independence_wave_package_id.iw_161`.
The saved generation must equal `independence_wave_generation_id`, with current framework/force-generation proof still valid.
The saved anchor must equal `independence_wave_anchor_state` and still resolve to IAX's real nonzero, owned, controlled capital state.
Use `has_independence_wave_regional_framework_anchor_capital` alongside snapshot equality.
Do not use fresh affordability or slot-open checks at expiry because this project has already paid and occupies the slot.
Do not retarget an in-flight project after a capital or anchor change.

**Reward:** replace `independence_wave_iax_river_office_terms` with `independence_wave_iax_river_service_administration`.
Its idea modifiers are `political_power_factor = 0.05` and `production_speed_infrastructure_factor = 0.10`, using file-local `@iax_river_service_political_power` and `@iax_river_service_infrastructure` constants in the existing idea file.
It replaces one institution and does not increase the spirit count.
Set every temporary input before calling `independence_wave_focus_apply_value_bundle`: legitimacy = `constant:independence_wave_value.minor_gain` (+5), recognition = `constant:independence_wave_value.minimum` (0), capacity = `constant:independence_wave_value.major_gain` (+15), security = minimum (0), instability = `constant:independence_wave_value.minor_loss` (-5).
Do not also call another administration or public-settlement reward helper.
The shared writer clamps the ledger to 0-100 and refreshes statehood normally.
Capacity 55 reaches the existing capable/regional capacity threshold of 70, while all other phase requirements remain binding.
Capacity 95 realizes only +5 after the clamp.
No buildings, territory, cores, units or FORM-37 readiness are granted.

**Once and cleanup:** before downstream rewards or refresh, write `independence_wave_iax_signature_river_services_reward_generation = independence_wave_generation_id` and `independence_wave_iax_signature_river_services_commissioned`.
Success clears the started flag and all three active snapshots.
Use native `remove_effect` for guarded success and a `cancel_trigger` that rejects an invalid finish predicate.
Cancellation clears those active receipts and releases the native factory reservation without reward or refund.
A fresh paid retry is possible after recovery if the original live origin and anchor contract pass and no reward was issued.
Human wartime use remains legal, and war alone does not cancel the domestic project.
Extend `independence_wave_iax_signature_cleanup` to remove the native decision independently of its private flag, remove the replacement idea, clear the commissioned flag and invoke temporary cleanup.
Preserve the durable reward-generation variable through cleanup, setup and CXT application to block another award in the same generation.
A genuinely new generation may earn the reward only after its own paid preparation is established.
Existing cleanup must clear the preparatory completion flags before new-generation initialization.
CXT, bypass and setup must not manufacture paid preparation or award the capstone.

**AI:** proposed base `constant:independence_wave_decision_ai.high` = 25, multiplied by `constant:independence_wave_decision_ai.modifier_double` = 2 below `constant:independence_wave_capacity_band.capable` = 70, and zero at war.
Wartime zero takes precedence.
These are proposed willingness scores, not measured click probabilities.
Retain existing institution-choice weights and the power-balance availability/bypass contract.

## Aceh: a distinct paid PUSA education reward

Current ordinary and PUSA school-network ideas both give `research_speed_factor = 0.02`, so the paid replacement needs a concrete incremental payoff.
At successful expiry of `independence_wave_atj_signature_organize_pusa`, add one limited-use `industry` research bonus named `independence_wave_atj_pusa_education_bonus` inside `independence_wave_atj_signature_complete_pusa_organization`.
Use `bonus = 0.5`, `uses = 1`, and no ahead-of-time reduction.
The authoritative values are `constant:independence_wave_focus_reward.technology_bonus` and `.technology_uses`.
Use file-local `@atj_pusa_education_bonus` and `@atj_pusa_education_uses` mirrors if these fields reject constant tokens, matching existing Event 006 treasury/civil-servant research consumers.
Keep the existing school-idea replacement and 2% research modifier, without adding another spirit.

Retain `can_independence_wave_atj_signature_finish_pusa_organization`, its exact ATJ/IW-150 paid-project generation proof, school-network prerequisite and `date > 1939.5.4` gate.
Keep the existing 20 CP/5,000 manpower payment, two-factory 120-day reservation, shared slot and AI base `constant:independence_wave_decision_ai.high` = 25.
Before granting the bonus, set the organized flag and durable `independence_wave_atj_signature_pusa_education_reward_generation` to the current generation.
A matching durable receipt rejects any regrant, including after cleanup/setup/CXT.
Preserve this award history through `independence_wave_atj_signature_cleanup` and clear active project receipts with `independence_wave_atj_signature_clear_pusa_project`.
Cancellation grants no research reward or refund.
Do not infer an unpaid bonus entitlement from an existing PUSA idea or achievement flag.
An already earned research bonus remains a country research reward until used, even if its originating institution is removed.
Do not invent a removal command or replenish the bonus during setup.

## Acceptance cases and presentation

Mon scenarios are `MON_RIVER_READY_PEACE` (capacity 55, score 50, one successful award), `MON_RIVER_CAPABLE_PEACE` (capacity 70, score 25), `MON_LOCAL_ROUTE` (absent), `MON_RIVER_WAR` (human eligible, AI zero), `MON_RIVER_NO_RESOURCES` (any shortage prevents selection/debit), `MON_RIVER_STALE_GENERATION` (no reward), `MON_RIVER_ANCHOR_LOST` (cancel without reward/refund), `MON_RIVER_REPEAT` (one reward despite repeat/cleanup/setup), `MON_RIVER_SLOT_OCCUPIED` (no simultaneous start), and `MON_RIVER_NEAR_CEILING` (capacity 95 to 100, instability 3 to 0).
Sweep affordability at CP 19/20/21, manpower 4,999/5,000/5,001, and available factories one/two/three, one resource at a time.
Aceh scenarios are `ATJ_PUSA_BEFORE_FOUNDATION` on 1939-05-04, `ATJ_PUSA_FOUNDATION_DAY` on 1939-05-05, `ATJ_PUSA_PAID_EDUCATION` with an eligible industry technology, `ATJ_PUSA_CANCELLED`, and `ATJ_PUSA_REPEAT`.
Verify one actual bonus use on paid success, none on cancellation and no regrant on repeated completion or same-generation cleanup/setup.
The parent owns final research-consumption and native timer evidence.

Reuse `GFX_decision_independence_wave_integration_missions`, idea picture `independence_wave_founding_identity`, and the existing infrastructure-authority focus icon.
Their definitions in `interface/006_independence_wave.gfx` and corresponding decision, idea and focus DDS paths were verified present.
Add the Mon decision title/description, replacement idea title/description, `independence_wave_iax_signature_river_services_ready_tt` and `independence_wave_iax_signature_commission_river_services_effect_tt`.
Update the existing river-works focus description and effect tooltip to explain the paid follow-through.
Reuse `independence_wave_signature_cost_administration_standard` only with accurate base, `_blocked` and `_tooltip` variants covering its factory reservation.
Update the PUSA decision/completion text and add the research bonus name key.
Write from river communities, teachers, transport workers and frontier staff for Mon, and teacher training/practical technical education for Aceh.
Explain visible requirements, payments, duration, outcomes and cancellation plainly, without internal receipt identifiers or pasteable working labels.
No new portrait, country, map/GUI system, automatic territory transfer or political/military PUSA route is requested.

## Prior design, research and evidence limits

Accepted Mon basis is Part 4 focus architecture lines 891-900 and the IW-161 research dossier lines 97-105.
The dossier provides monasteries, language/cultural associations, notables, merchants, river communities and a provisional federal council as the period bridge.
It excludes post-1947 names from the opening and treats Thai Mon connections as diplomatic, cultural, refugee or federal links.
Accepted Aceh education basis is the IW-150 dossier lines 87-95 and the signature-module foundation research already supplied by the parent.
The commissioned river service and education research award are alternate-history gameplay design, not claims that these exact historical programs existed.
No additional historical claim is needed.

No earlier Mon/IW-161 river-office payoff addendum was found in the improvement/addendum search.
D31 in `agent_decisions_2026-10-04.md` records Mon Level 2 as `implemented` and signature Level 3 as `accepted and queued` pending its separate layer.
`docs/events/006_independence_wave/signature_modules.md` records the 2026-10-06 task authorization and supersedes that prior signature queue.
`subagent_handoffs/signature_focus_review_20261007.md` leaves this central endpoint consequence `unresolved`, and this handoff answers that existing finding without another route plan.
Its follow-up records parent-applied coordinate corrections and supersedes the earlier blanket route-AI finding.
`signature_decision_review_20261007.md` records the live-origin and shared-slot repairs as implemented, with blocked cost text/native row evidence still open.
The earlier core v67 improvement addendum records its uniqueness repair as implemented and recommends stopping broad core expansion.
Unrelated Event 006 addenda and completion blockers retain their own dispositions.

Fresh `hoi4.focus_inspect` and `hoi4.focus_render` succeeded on the owner tree at revision `aaa2bfd731048a1ca2158cd3c061eaf123d93a8be49b280526157a89004aa314`, with layout hash `ea3ad753bd8a8841e959710671564f9fa392b172c9cc8b8d2e7e0f6ea21ccafb`.
The hash-verified inspect artifact contains 184 materialized focuses and zero Mon nodes in `plans[0].focuses`, so imported Mon layout coverage remains unresolved.
Inspection artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/2ac07a0da1de843bc823990ccd54e89e3ca73d85f46c7deb7c4d0d3ca44fe0fd/b264d5d661daf049d12edbff890d45034d07c8dd6e6a50a2ac7cc3f0ef6e4651/focus-inspect.aaa2bfd731048a1c.json`.
Render artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c9e5445b7dbcc2713b92e45bb8ff8aa934920103cefefee78637181d67633f69/a8b0f0b607c1bfe1db9daf1f373876494bc13f77dad0aad28cc5a4ecf4b32c85/independence_wave_focus_tree.focus.html`.

Weighted work began with `probability_inspect` and was routed to read-only `chaosx_ai_probability_auditor`.
Its corrected `mission_ai_will_do` adapter finds seven timed-project candidates, including the three Mon scores of 10 and PUSA's score of 25.
Its complete pool is only the source-file inventory, not campaign eligibility or a global candidate pool.
Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/82879445795ed8d3a1bc90fe87569361f7de0248ac2c3eedb1cd67abf625fb71/3872ac8c404b7206962f2a7dc052b20d34c203464a2ff2e1f5722cffa3b15e9c/probability-inspect-6d61cacde4b7.json`.
Imported focus weights remain undiscovered by that adapter.
Fresh scenario evaluate/sweep/compare evidence is incomplete because the parent requested immediate delivery under service load.
Freeze exact pre-edit sources and use the same named scenarios for the mandatory parent-applied change and auditor comparison.
Never compare current source to itself or present proposed scores as probabilities.

A decision-inspection request without scenarios returned `Decision inspection requires declared scenarios at scenarios`.
A corrected IAX fixture request was submitted, but its final result was not observed before its client observer was stopped for this bounded handoff.
The secondary `tech_inspect(mode = bonus_coverage, categoryId = industry, maxNodes = 10)` and `tech_render(view = bonuses, categoryId = industry, maxNodes = 10)` requests likewise have unobserved final outcomes, with one stopped render reporting `code mode delegate request cancelled`.
These are observation limits, not confirmed server failures, and source review does not replace the missing scenario/research coverage.

Standalone Technology Tree Viewer availability was checked separately from tool exposure and service response.
The configured npm-cache `hoi4-agent-tools` package manifest reports 3.10.0 and provides stdio, HTTP and setup entry points, with zero package-owned standalone viewer launch-file candidates.
Record that scoped absence as a standalone-viewer package gap.
Connected initialization version and native-task negotiation were not established, and no job/helper-expansion/native-task route was used.
No rewrite tool or game launch was used.

Fresh rules read through MCP: offline Decision modding lines 337-356, revision `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162`, installed `common/decisions/_documentation.md` lines 1-46, revision `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`, offline List of modifiers lines 436-445, revision `e93b4998e1e9c8736c1f0744f100f92fd7a5380f74c48ac85004783f6c8f77b9`, installed effects documentation `add_tech_bonus` lines 2226-2234, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`, and offline Effects `add_tech_bonus` line 1936, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
The decision context omitted Triggers/Scopes/Localisation at its requested limit, so their full coverage is not claimed.
Direct installed precedents read were `_generic_decisions.txt` lines 226-263 and `common/ideas/afghanistan.txt` lines 520-529.
Existing Event 006 bundle and research consumers were read at focus-effects lines 340-377 and main-focus lines 817-833 and 2098.
Source lookup read the public-settlement helper at revision `0ef503d655d31750c8492f77c1e54ab850582762b2b00e804246954ae81ae5d5`, confirming why calling it would add another reward bundle.

## Parent implementation and closure

Implement in the existing signature decisions/effects/triggers/ideas and signature English localisation, updating `docs/events/006_independence_wave/signature_modules.md` during integration.
Shared constants and the existing CXT carrier need no new reward-dispatch system.
Record parent acceptance and promote the consequences into the Mon/Aceh portions of Part 4 and the relevant decision design under `docs/specs/006_independence_wave_specs/`.
If PUSA is sequenced later, record `accepted and queued` with the reason that Mon is the current critical implementation tranche.
Keep this handoff in `docs/plans` as provenance and validation limits.
Finish the production receipt/debit/cancel/repeat tests, native timer/research checks, local-route reachability, cost-text review and required probability comparison before claiming the affected systems complete.
Stop broad expansion after these consequence fixes.
Event 006 completion still requires the parent's separate whole-event review and resolution of every remaining accepted plan or blocker.

Only this owned handoff was written.
No gameplay or index changes were made, and staging/committing is deferred to the parent under the explicit index prohibition.
No design simplifications were introduced within this bounded recommendation, while engine evidence limits remain explicit above.
Skills used: improvement-loop, event-planning, events, focus-trees, decisions-missions, event-assets and subagents.
No skill was changed.

## Implementation handoff — signature payoffs, 2026-10-07

Disposition: both recommendations are implemented in the assigned signature-module source.
Acceptance basis: the parent's explicit acceptance under the user's recommended-choice authority, followed by the bounded active implementation assignment and its spirit-count refinement.
This implementation appendix supersedes the earlier unresolved/plan-only status for these two recommendations only.
Parent-owned ready-formable integration, production callback-harness updates, probability comparison, final review and commit remain separate work.
No ready-formable/shared registry, private callback script, national-focus source, on-action source, asset, GUI, portrait or Git/index file was edited.

### Files and call sites changed

- `common/decisions/006_independence_wave_signature_modules_decisions.txt`: eighth timed action `independence_wave_iax_signature_commission_river_services`; PUSA selection delegates to its guarded start writer.
- `common/scripted_effects/006_independence_wave_signature_modules_effects.txt`: Mon start/expiry/active cleanup, PUSA guarded start and education payload, package cleanup extensions, and exactly two parent-requested CXT readiness-relay substitutions.
- `common/scripted_triggers/006_independence_wave_signature_modules_triggers.txt`: eighth shared-slot flag, Mon continuing/selection/expiry gates, pure spendable-reserve gate, PUSA current-school and durable-award protections.
- `common/ideas/006_independence_wave_signature_modules_ideas.txt`: `independence_wave_iax_river_service_administration`, replacing the current river-office institution.
- `localisation/english/006_independence_wave_signature_modules_l_english.yml`: eight new keys and four surgical payoff/focus-follow-through text updates.
- This handoff: implementation API, validation and integration notes appended.

No shared or signature script-constant file changed.
The new idea uses file-local `@iax_river_service_political_power = 0.05` and `@iax_river_service_infrastructure = 0.10`.
The native research payload uses file-local `@atj_pusa_education_bonus = 0.5` and `@atj_pusa_education_uses = 1`, matching `constant:independence_wave_focus_reward.technology_bonus` and `.technology_uses`.
The installed command prose and offline field documentation do not establish dynamic `constant:` support for bonus/uses, so the explicitly authorized file-local mirrors are used.
PUSA's existing 2% school idea, payment, date and AI coefficient remain unchanged.

### Helper contracts

All APIs below run in the actor's country scope, with ROOT equal to that actor.
They take no optional caller parameters or caller-owned output storage.
There are no defaults that grant missing institutions or manufacture paid preparation.

| API | Inputs and gate | Outputs, side effects and callers |
| --- | --- | --- |
| `can_pay_independence_wave_signature_administration_standard_reserves` | Current CP and manpower against the existing shared administration constants | Pure inclusive boolean; Mon/PUSA start writers only. Factory affordability stays in the full selection quote. |
| `has_independence_wave_iax_signature_river_services_preparation` | Exact live IAX/IW-161 module, current controlled capital, river route and completed charter, current river-office idea and school trust, paid transport/watch completion, no local route or current-generation award | Pure continuing boolean shared by selection, start and expiry. No resource, slot or wartime check at expiry. |
| `can_independence_wave_iax_signature_commission_river_services` | Continuing preparation, shared slot, full administration quote | Pure selection boolean; decision availability. |
| `can_independence_wave_iax_signature_finish_river_services` | Continuing preparation, started receipt, three present snapshots; saved generation equals current; saved package equals current and IW-161; saved anchor equals current controlled capital | Pure expiry boolean; callback and native cancellation. |
| `independence_wave_iax_signature_start_river_services` | Continuing preparation, shared slot and spendable reserves | Writes started/package/generation/anchor before debiting 20 CP and 5,000 manpower once. Called by the new decision's complete_effect. |
| `independence_wave_iax_signature_complete_river_services` | Exact paid expiry proof | Publishes durable generation and commissioned flag first; replaces river-office terms with service administration; initializes all five shared-writer inputs; calls the shared value bundle once; always clears active snapshots afterward. Called by remove_effect. |
| `independence_wave_iax_signature_clear_river_services_project` | No optional inputs | Clears started flag and three active snapshots only; never removes durable history or a success receipt. Used after expiry, on cancellation and in package cleanup. |
| `independence_wave_atj_signature_start_pusa_project` | Existing PUSA eligibility plus the current ordinary school-network idea, no current-generation education award, open slot and spendable reserves | Publishes paid project generation/package before a single administration debit. Replaces the former unguarded selection body. |
| `independence_wave_atj_signature_complete_pusa_organization` | Existing legal paid expiry with present exact package/generation snapshots and current school network | Publishes organized/durable generation first, replaces the school network without changing its 2% modifier, grants one named 50% industry research bonus without ahead reduction, then always clears active receipts. |

Mon initializes `independence_wave_focus_legitimacy_delta` to minor_gain, recognition to minimum, capacity to major_gain, security to minimum and instability to minor_loss before `independence_wave_focus_apply_value_bundle`.
The actual shared writer adds those values and runs the existing refresh/clamp path.
No second administration reward, public-settlement reward, building, territory, core, unit or FORM-37 readiness grant is added.

The native decision reserves two factories for the existing standard duration of 120 days.
Full affordability is checked during selection; start rechecks CP/manpower without rejecting factories that the native timer may already have reserved.
Expiry never rechecks affordability or slot openness.
The parent still owns verification of native reservation ordering.
A charter replacing the current river-office idea fails the continuing proof, so the project cancels without reward/refund instead of adding another spirit.
Both start writers set their active marker before debit, rejecting a direct duplicate start even during nested evaluation.
The commissioned/organized success flag is written before rewards and protected by the native cancel guard so successful expiry does not also present cancellation.

### Durable history and cleanup

Mon history is `independence_wave_iax_signature_river_services_reward_generation`.
PUSA history is `independence_wave_atj_signature_pusa_education_reward_generation`.
Both are normal country variables and are intentionally absent from cleanup clear lists.
Package setup/CXT setup does not write a paid completion or durable award.
Matching current-generation history rejects another start after cleanup/setup; a new generation still requires its own paid preparation.

Mon package cleanup removes the native decision independently of its started flag, invokes active cleanup, removes the service-administration idea and clears the commissioned flag.
Existing preparatory flags continue to be cleared by that package cleanup.
PUSA package cleanup retains earned research/history while clearing its active project, organized flag and school idea.
Cancellation and rejected direct expiry grant no bonus, ledger reward or refund.
An earned native research bonus is left available until consumed; no invented removal or replenishment effect is used.

### Parent integration boundary

The parent-owned `independence_wave_ready_formable_request_cxt_readiness_refresh` now replaces direct registration at only the two CXT repair sites in `independence_wave_signature_modules_cxt_extension_apply`.
The ordinary Aceh and Mon `independence_wave_focus_register_formable_family` calls remain unchanged.
The relay effect definition was found in the ready-formable source during final dependency inspection.
The debug readiness feature remains present.

The parent must add the new IAX source institution to both ready-formable installers and both restorers.
Use distinct `independence_wave_ready_formable_carrier_replaced_iw161_river_service_administration` and `independence_wave_ready_formable_member_replaced_iw161_river_service_administration` receipts alongside each generic replaced-institution receipt.
Extend every existing IAX base/local/river installation guard to exclude the new fourth idea.
The new installation branch must exclude the other three choices, reject any installed charter/compact variant and preserve the existing one-time installed marker.
Extend base/local/river restoration exclusions to include the new receipt, add exact new-receipt restoration guarded against the other evolved receipts, and clear the new receipt in each restoration cleanup tail.
Keep the live-framework/package/generation ownership gate.
Do not widen the shared FORM-37 selector.
No ready-formable file was patched by this worker.
The idea was still absent from those adapter branches at the final inspection, so this remains a concrete parent integration dependency.

The parent's private `.git/signature_callback_cases.py` was not edited or run.
It needs the eighth slot receipt and the guarded PUSA start call, normal country reward-generation variables, Mon package/generation/anchor snapshots, the current source-idea requirement, all five bundle inputs, native add_tech_bonus accumulation and file-local @ resolution.
Keep durable normal state separate from temporary call frames and discard only temps first created inside a returning helper.
The actual-source cases below do not substitute for updating that production harness.

### Meaningful source cases

Forty-one in-memory actual-source cases passed.
The model reads the current signature decisions/effects/triggers, the shared payment/bundle/clamp bodies and scalar tuning tables.
It evaluates normal country state, flags, ideas, dates, declared anchor ownership/capital facts, payment, callbacks and ordered receipts.
Temporary scalars first created in a helper are discarded at that helper's return; caller-owned storage retains modifications.
External module/framework/force eligibility is explicitly supplied as fixture facts.
Refresh effects beyond clamping, native factory/timer ordering, research consumption and campaign AI are not executed.

| Cases | Evidence |
| --- | --- |
| Nine Mon quote boundaries | CP 19/20/21, manpower 4,999/5,000/5,001 and available factories one/two/three, varied separately through actual availability and the shared inclusive quote. |
| Reserved-factory start and duplicate start | Selection was valid; start with already-reserved factories debited once; repeated direct start left payment/snapshots unchanged. |
| Legal Mon expiry, stale temp inputs and replay | With no remaining CP/manpower, capacity 55 became 70, legitimacy 50 became 55 and instability 20 became 15; recognition/security remained 50; success preceded cancellation; repeated expiry added nothing. |
| Mon near ceiling | Capacity 95 became 100 and instability 3 became zero through the actual clamp body. |
| Ten failed Mon expiries | Stale generation/package/anchor, absent snapshot, lost/moved anchor, school loss, charter replacement, local-route conflict and invalid force eligibility granted no reward/refund and cleared active receipts. |
| Cancellation and occupied slot | No reward/refund; slot freed on cancellation; occupied-slot Mon and PUSA direct starts did not debit. |
| Durable Mon cleanup/setup | Current-generation replay rejected; a new generation with its own preparation could complete. Cleanup removed the decision/idea and retained history. |
| Six new-action score cases | Peace at capacity 55/69 scored 50; 70/95 scored 25; wartime at 55/70 scored zero. These are declared source scores, not probabilities. |
| Wartime human Mon action | Selection and paid expiry remained legal; war alone did not cancel. |
| PUSA foundation and current school | 1939-05-04 rejected, 1939-05-05 accepted; absent ordinary school network prevented debit. |
| PUSA paid bonus/replay/cleanup | One 0.5, one-use industry bonus with no ahead_reduction; duplicate start/expiry and same-generation cleanup/setup did not grant another use. Spirit count stayed unchanged. |
| Four failed PUSA cases | Cancellation, stale generation/package and school loss granted no bonus/refund and cleared active receipts. |

Seven existing ai_will_do blocks matched the preserved pre-final decision snapshot exactly.
The new eighth action uses the accepted high base, below-capable double factor and wartime zero factor.
The FORM-37 selector and ordinary entry body matched their pre-edit definitions.
Exactly two CXT relay calls were verified.
No weighted evaluation, normalized choice probability or campaign timing pass is claimed.

### MCP and reference coverage

Country-scope `hoi4.script_validate` of the pure reserves predicate returned `SCRIPT_CHECKED`, valid true, four checked commands and zero unresolved/omitted findings.
Coverage was syntax, command kind and declared scope only; parametersChecked was false.
The PUSA reward body returned `SCRIPT_CHECK_PARTIAL`, valid null, seven checked commands, four unresolved findings and two unchecked argument blocks.
Those gaps are its custom finish/cleanup helpers, set_variable and add_tech_bonus arguments.
The Mon reward body returned `SCRIPT_CHECK_PARTIAL`, valid null, ten checked commands, nine unresolved findings and six unchecked argument blocks.
Those gaps are its custom finish/bundle/cleanup helpers, set_variable and all five set_temp_variable blocks.
Neither partial result establishes argument semantics or engine behavior.
No findings were omitted in these two reward checks.

Required probability work began before editing with mission_ai_will_do inspection of the signature decision source in workspace `mod_chaos_redux_ea3b2d67c2c0`.
It returned no result within the 20-second client bound.
One narrow retry selected only `independence_wave_atj_signature_organize_pusa` and likewise returned no result within 20 seconds.
These are precise client coverage gaps, not returned server timeout errors.
The parent-owned probability auditor must compare the accepted Mon/PUSA scenarios after integration.
The source-model score cases above do not replace that comparison.

The add_tech_bonus reference reads succeeded:
installed reference ID `73b876e0d481ee747eecc984f7526866cac7e45e48c3218175699d0b9d837295`, effects documentation lines 2226-2234, revision `2cdc93d26775990468eed167442f7a416b13059fb8fe07d139b54250b79209af`;
offline reference ID `09422a7e8e7f69140dab8a9439f6e673e7d78503569acfe4550d23f61ddb982e`, Effects line 1936, revision `997ddb09bfd63efb41a425149c46bd812d5f8953217a403386b2f6c85196aa0c`.
The exact installed vanilla precedent at `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/common/national_focus/afghanistan.txt:188-193` uses bonus 0.5, uses 1, category industry and a named research bonus.
Its SHA-256 is `87ef0090e8f7ac0e626b747b476771ce14664fe8696348b43770a668aa9ec9a1`.
Shared bonus/uses tuning was read at constants-registry lines 1832-1834.
Script-constant schema reference `48deec564822a81f6806514736148c344258acac56db7e9989998ed30dd26b68` was read at lines 1-34, revision `e2812efbddc7961038e1f1f2b6dd6b059bdc70704ec87d1fe530835d9141be1c`.

Decision reference context returned timer reference `91b27451ff9a5b5e5b74f6b0b8a12b3012a222b3d82681284186751ca59753eb` and installed decision reference `c8ba2a44d708fd3048c019dfb9e36f3ecf59ff754f7cb4ea3bb7c4704deb5c58`.
Their follow-up MCP reads did not return before the bounded observer was stopped, so their actual rule text was read directly from offline Decision modding lines 337-356 and installed common/decisions/_documentation.md lines 1-46.
Their revisions are `7713b9bcee5f3818d63aafbd45d18e812a9173a7c59ab238384b57db60db6162` and `5e7e686b5582f32c38d898d805e17171e88f3bfeee4a030deb1884f9726de019`.
The context omitted other topics; full reference-bundle coverage is not claimed.
Prior scopes/temp-lifetime reference evidence remains in the dependency review.
Native command-index revision for the scope checks was `9227e238bce49345e9c358598b4dd4940c733d906b72324e8a02a57ecb42093b`.

### Presentation and remaining work

Eight keys added: the Mon decision/description, ready/outcome/cancellation tooltips, service-administration idea/description and `independence_wave_atj_pusa_education_bonus`.
Four keys updated: PUSA decision description/outcome and the existing Mon river-works focus description/outcome.
Existing cost base/blocked/tooltip aliases and unrelated localisation-auditor corrections were retained.
Icons are the accepted existing `GFX_decision_independence_wave_integration_missions` and idea picture `independence_wave_founding_identity`; no asset or sprite registration is required.
There is no new GUI, country, portrait or focus node.

No implementation simplification or fallback was introduced.
Remaining validation/integration is the parent-owned new-idea adapter, native factory/research consumption evidence, private callback-harness update, probability comparison, localisation/focus-follow-through review and final commit.
User-owned live evidence was neither requested nor manufactured.
Skills applied: events, decisions-missions, subagents and focus-trees for the bounded focus localisation/vanilla precedent.
No skill was created or changed.
