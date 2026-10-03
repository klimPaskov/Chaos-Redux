# Event 35 synchronous API ROOT-context audit

Date: 2026-10-03.
Role: `chaosx_scripted_system_architect`.
Mode: read-only gameplay audit with an explicitly authorized report write.
Disposition: audit findings recorded, proposed repair unresolved pending parent review, engine evidence blocked.
Workspace: `C:\Users\klimp\OneDrive\Documents\Paradox Interactive\Hearts of Iron IV\mod\chaos_redux`.
Observed Git HEAD: `7ab7b9407dbe3f6812731805e295b5476d18f78b`.

## Finding and recommendation

The existing public effect must remain a synchronous country-scope transaction whose exact target is THIS, independently of ROOT.
Entering a country through an array or event target does not make that country ROOT.
The gateway itself writes its inputs and outputs on the current country, but nested center registration, achievement freezing, evolution-I network initialization, source-context recording, and outgoing-link cleanup assume another actor binding.
The parent's recipient events `chaosx.nr35.8` and `chaosx.nr35.9` address pulse delivery and normal independent selection only.
They do not repair contagion conversion, worldwide conversion, or recovery-watch relapse calls into the same public API.

Recommended repair: retain `great_depression_start_or_deepen = yes` and all immediate caller result reads, make the bounded synchronous helper closure use its actual calling country through PREV at direct child scopes, and freeze contagion conversion bookkeeping in normal target-country variables across the API call.
Use PREV.PREV only where a second intervening country or state scope is present and the source trace proves that depth.
No second public API, central router, extra pacing path, or queued-return substitution is needed.
A single mutable event target shared by all actor and source helpers would introduce another nesting hazard.

No gameplay patch was made.
All patch descriptions below are proposals for the parent.

## Scope, ownership, and evidence boundary

Read current `AGENTS.md`, `.agents/skills/chaos-redux-events/SKILL.md`, and `.agents/skills/chaos-redux-subagents/SKILL.md` completely.
Inspected the named API spec, relevant owner effects and triggers, actual Event 34 caller, external adapters, existing shared dynamic-effect registry and documentation, and pertinent offline and installed references.
No focus tree, GUI layout, map, probability evaluation, game launch, or live consumer test was performed.
Mission cleanup and the supplier-demand caller were inspected only as dependencies, with no decision or GUI implementation proposal.
No skill was created or changed.

The parent's exact `process_active_registry` and `select_independent_target` blocks and `events/035_great_depression.txt` remain parent-owned.
This report does not duplicate or edit them.
The shared worktree already contains unrelated changes.
Only this handoff was written, with no staging or commit.
The repair and required engine evidence are unfinished, so this report must not become a completion commit for the gameplay repair.

The parent reports `hoi4.source_lookup`, `hoi4.event_inspect`, and `hoi4.reference_context` each timed out after 600 seconds.
Those requests were not restarted.
In this subagent's current `ALL_TOOLS` inventory there are no callable `mcp__hoi4_agent_tools__hoi4_*` domain routes and no callable tool-search route to expose their live schemas.
`list_mcp_resource_templates({})` did respond with server `hoi4_agent_tools` and template `hoi4-agent://workspace/{workspaceId}/artifact/{sha256}/{provenanceHash}/{name}`.
Its declared byte-range metadata is version 1 with a 1,048,576-byte maximum chunk.
That response establishes resource-template availability only, not domain service health, server version, inspector coverage, or native-task negotiation.
No artifact URI for this audit was produced or supplied.
No helper-expansion, job, cancellation, native-task, event-render, event-compare, reference-read, or script-validation result exists for this audit.
Local reference reads are authorized by the repository's reference-route-gap rule and the parent assignment.
They are source evidence, not equivalent MCP or engine evidence.

The supplied cycle1 observation of no Event35-labelled errors and mainmenu success is parent-supplied load evidence only.
It does not prove target selection, state ledger ownership, immediate returns, conversion attribution, relapse, or idempotence.

## Exact caller map

Line references below use the rechecked effect headers and calls at the observed SHA-256 revision in the source ledger.
Parent edits during the audit moved some lines, so earlier terminal excerpts should not be used as the final line map.
Rebase by identifier if the parent changes the file again.
`E35` means `common/scripted_effects/035_great_depression_effects.txt`.
`T35` means `common/scripted_triggers/035_great_depression_triggers.txt`.

| Caller | Exact current call and continuation | ROOT versus exact target | Contract implication |
| --- | --- | --- | --- |
| Event 34 inheritance | `events/034_industrial_boom.txt:135-241`, recipient event `chaosx.nr34.3`, API at 213, result reads 214-220, region companion 230-236 | Recipient country is THIS and ROOT in this current caller | Its synchronous returns must remain available for completion accounting and region registration. A baseline recipient call is locally aligned, but its evolution network still enters other countries. |
| Contagion conversion | `E35:5834` helper entry, exact target entry 5959, prepared inputs 6097-6122, API 6123, result reads 6124-6130, attribution 6131-6169 | Source A remains ROOT in today's recipient pulse, while target B is THIS at the API | B must own episode, severity, centers, and outputs. A must retain source and receipt attribution. The API's evolution-I network creates nested exposure work. |
| Worldwide conversion | `E35:6819-6903`, exact country from pressure array at 6842, API 6872, result reads 6873-6879, global-row continuation 6880-6898 | Global lifecycle host remains ROOT, selected pressure country is THIS | Preserve exact global pressure row, activation source, global episode, cursor, interval, and immediate success continuation. |
| Recovery-watch relapse | `E35:4398-4436`, registry country entry 4409, `start_relapse` at 4419. `E35:4340-4396`, API 4382, result reads 4383-4389, watch/cooldown continuation 4390-4393 | Global host remains ROOT, watched country is THIS | The same watched country owns a new episode and return outputs. Prior episode and legacy must remain on that country. |
| Independent cluster member | `events/035_great_depression.txt:14-25`, direct API at 21 | The recipient is THIS and ROOT | Preserve this direct same-country API lane and its existing consequence-no-pacing policy. Parent owns normal independent selection. |

The named `common/scripted_effects/034_industrial_boom_effects.txt` does not exist in the current checkout.
An `rg --files` recovery search found `common/scripted_effects/034_industrial_boom_adapter_effects.txt` instead.
That file owns incoming supplier demand, not the collapse API call.
A repository-wide API-use search located the actual inheritance call at `events/034_industrial_boom.txt:213`.
This is a recorded path discrepancy, not an invented replacement implementation.

The global-host hooks independently invoke recovery-watch and global lifecycle after active processing at `common/on_actions/chaosx_on_actions_chaos_meter.txt:26-30`, `51-55`, and `76-80`.
Consequently, repairing only active pulse delivery does not rebind their later calls.
The global episode calls `great_depression_try_worldwide_conversion` at `E35:7072`.

## ROOT-sensitive dependency map

| Helper | Relevant lines | Meaning of current ROOT | Narrow synchronous repair |
| --- | --- | --- | --- |
| `great_depression_register_initial_centers` | `E35:1520-1705`, inherited-state ownership checks 1559-1561, state entry 1579, actor ledger 1581-1597, episode read 1599, candidates 1632-1644, actor ledger 1669-1685 | Crisis actor | At country to state transitions use PREV for actor checks, actor variables, actor ledger blocks, and owner identity. Country-local counts remain unqualified. |
| `great_depression_score_center_candidate` | `E35:1317-1345`, neighbor check 1339 | Crisis actor two scopes above neighboring state | Under the proven country to candidate state to neighboring state chain, use PREV.PREV for ownership. Preserve score coefficients, candidate order, and tie-break. Required weighted actor-check comparison remains blocked. |
| `great_depression_initialize_achievement_tracking` | `E35:2925-2993`, state iterator 2941-2947 and capital check 2984 | Crisis actor | The state iterator returns to PREV for actor arrays. The capital controller check uses PREV. No achievement criteria or baseline values change. |
| `great_depression_store_call_context` | `E35:2535-2573`, source-country block 2542-2545 | Caller ROOT, incorrectly standing in for supplied source | Inside the validated supplied source scope save that source directly. Honor source proof, not merely a possibly inherited event-target name. Store any durable source pointer as an actor-owned normal variable, with its documented proof/lifecycle, rather than claiming the regular target persists after the chain. |
| `great_depression_apply_evolution_floor` | `E35:2180-2227`, initializes network 2204 | Indirect dependency | Retain floor, lower-stage activation, enablement gates, and milestone path. Make its network closure source-neutral rather than skipping or delaying it. |
| `great_depression_register_contagion_candidate` | `E35:5579-5604`, returns to ROOT at 5583 | Network source, which is the API actor | Candidate country was entered directly from the source. Return to PREV, then invoke exposure in that source country. |
| `great_depression_is_valid_contagion_network_target` | `T35:123-132`, `tag = ROOT` at 125 | Network source | All found effect uses enter the candidate directly from the source, including decision-effect line 1161. Change exclusion to PREV only with this explicit helper contract and complete consumer review. Vulnerability helper at T35:134-149 delegates to it. |
| `great_depression_apply_exposure` | `E35:5834-6177`, target entry 5959, source fields 5978-6137, nested source-row match 6009 | Network source, not the crisis target | In direct target scope source reads and source identity use PREV. Within B's source-row scope the source is PREV.PREV. At the API call B remains THIS. Do not turn all source references into B. Freeze row indexes across the API call. |
| `great_depression_clear_outgoing_contagion_network` | `E35:5734-5832`, source-row match 5788 | Country being cleaned | In actor to recipient to recipient-source-row nesting compare against PREV.PREV. Preserve other source rows and recipient totals. This helper is reachable through API abort cleanup. |
| `great_depression_register_inherited_region` | `E35:5007-5074`, state entry 5011, actor checks 5014-5033, actor ledger 5037-5052 | Crisis actor | Enforce the spec's country-scope companion contract. In its exact state child PREV is the actor. Do not preserve the current comment's unsupported arbitrary state-scope calling promise. Current concrete caller is country-scoped. |

The initial-center helpers also read `building_level@industrial_complex` and `building_level@arms_factory` inside the returned country block at `E35:1586-1587`, `1674-1675`, and the companion at `5042-5043`.
Those are state baselines, so capture them on the exact state before returning to the actor ledger.
Changing ROOT to PREV alone does not correct these value-read locations.

`great_depression_start_or_deepen` at `E35:3355-3480`, `initialize_new_crisis` at `3077-3276`, and `deepen_active_crisis` at `3310-3353` have no direct ROOT use in their bodies.
Their ordinary country variables, output writes, receipt commits, episode allocation, and actor override THIS are already located on the current target.
The hazard is transitive.
A bounded textual closure over the named E35/T35/adapter files reached 90 local definitions, including the cycle through evolution initialization, exposure, and the API.
This was a source discovery aid only, with no claim of full MCP closure, dynamic-call resolution, mission-engine callback coverage, or engine execution.

`great_depression_rebuild_hidden_components` at `E35:3834-4114` aggregates state pressures back through ROOT at 3897-3943.
It is called by weekly pulse, not directly by the inspected public API transaction.
The new-crisis branch initializes hidden pressure values before future pulse evaluation.
Do not introduce a new immediate aggregation call, delay, or formula during this API repair.
The parent's recipient pulse handles its current runtime actor binding.

The humanitarian adapter `great_depression_submit_humanitarian_center_pressure` in `common/scripted_effects/035_great_depression_external_adapters.txt:15-88` uses ROOT for actor coherence, `ROOT.id` request attribution, and actor-observed flags.
Its concrete callers are transfer/failure processing at `E35:1113`, `3651`, and incident effect line 992.
It is not a direct start/deepen dependency.
Preserve its current recipient-actor runtime contract and do not silently substitute state owner or controller for the responsible actor.

The supplier adapter `industrial_boom_receive_depressed_market_demand` in `common/scripted_effects/034_industrial_boom_adapter_effects.txt:13-66` intentionally uses ROOT as requesting depression country while THIS is the supplier.
Its caller is `great_depression_offer_boom_supply_contract` in decision effects at 1350-1374.
This is not the Event 34 collapse API call and is not in the inspected API transaction closure.
Do not rewrite that ROOT to the supplier.

## Public input and output boundary

The spec's scope promise is at `docs/specs/035_great_depression_specs/035_great_depression_reusable_crisis_api.md:13-17`.
The exact target is the current country.
All `great_depression_call_*` scalar inputs and public outputs in the current implementation are normal country variables, not actor-scoped temporary variables.
Source scope inputs additionally include regular or existing global event targets with proof variables.
Do not convert these scalar inputs or outputs into unscoped temporary fields.

Retain all thirteen outputs reset by `great_depression_reset_call_outputs` at `E35:1711-1724`: result, reject reason, episode ID, started, deepened, no-op, active evolution, final severity, opening shock applied, report queued, history recorded, and pacing counted.
Reset before validation, leave outputs on the target through the immediate caller continuation, and clear only public inputs at `E35:1726-1777` before return.
The spec's public output and return cleanup contract is at lines 201-216 and 424-433.
Existing country-block nesting supplies a synchronous source path without relying on event scheduling.

Keep receipt validation and commit on the exact target.
The duplicate path at `E35:3384-3395` returns a no-op with current episode/severity/evolution and must not replay center selection, shock, history, Chaos, or pacing.
Keep the six aligned receipt arrays in `great_depression_record_source_receipt`, `E35:2444-2465`, and their globally allocated receipt identities.
Do not allocate a replacement receipt merely to repair ROOT.

Keep caller-specific pacing enforced by `T35:419-448`: Event34 uses consequence-no-pacing, contagion/worldwide/relapse use conversion-no-pacing, and debug uses debug-no-pacing.
Only the independent normal-event path exposes pacing counted in `E35:3255-3258`.
A root repair must not call the random event scheduler, fired-event handler, or another accounting route.

## Proposed helper map and patch sequence

Existing names remain authoritative.
Scope adapters are local changes to those helpers, with no duplicate start/deepen implementation.

| Helper contract | Inputs | Outputs | Side effects and direct call sites |
| --- | --- | --- | --- |
| `great_depression_start_or_deepen`, COUNTRY | Existing normal country inputs, source-specific proofs and exact supplied scopes | Existing normal country outputs, immediately readable | Existing crisis transaction. Callers at Event34:213 and E35:4382, 6123, 6872 remain direct. |
| `great_depression_register_initial_centers`, COUNTRY | Actor country runtime and existing inherited-state proof | Existing actor arrays, count, registration failure | Same center selection. Called at E35:3229. State helpers access the country through actual PREV. |
| `great_depression_score_center_candidate`, STATE directly under actor country | Candidate state values and actor two scopes above neighbor | Existing temporary score | Same scores and tie-break. Called at E35:1646. No tuning change. |
| `great_depression_initialize_achievement_tracking`, COUNTRY | Current episode and actor center ledger | Existing frozen actor achievement arrays and flags | Same tracking. Called at E35:3238. |
| `great_depression_store_call_context`, COUNTRY | Existing validated source inputs and proofs | Existing episode source fields, exact source pointer when supplied | Called at E35:3239 and 3335. Save supplied source directly and document durable pointer separately. |
| `great_depression_initialize_contagion_network`, COUNTRY source | Existing actor episode, floor and enabled surface | Existing bounded outgoing rows | Same relationship traversal and initial stages. Called at E35:2204. Candidate helper returns to actual source. |
| `great_depression_apply_exposure`, COUNTRY source | Existing exact exposure target and source-owned normal exposure inputs | Existing bilateral rows and same-country conversion outputs | Network initialization, network processing, and decision-effect line 1181 retain one exposure implementation. Target-side child uses PREV for source and THIS for crisis. |
| `great_depression_register_inherited_region`, COUNTRY actor | Proven exact supplied state, committed episode and frozen inheritance fields | Existing center ledger, plus any separately accepted companion receipt outputs | Event34:235. Preserve the current state and actor, do not reroll. Its missing full companion contract is recorded below. |
| Proposed private `great_depression_clear_conversion_frame`, COUNTRY receiving target | Conversion scratch fields only | Scratch cleared, public API outputs retained | Direct calls after conversion continuation and rejection in `apply_exposure`. No use without these call sites and matching docs. |

1. Recheck the parent patch and preserve its two protected effect blocks and recipient events.
2. Change direct country-to-state actor references in initial centers, achievement freezing, and the country-scope region companion to PREV.
   Change the nested candidate-neighbor ownership reference to PREV.PREV only after the required weighted audit.
   Capture state factory baselines before entering the actor ledger.
3. Change network candidate source return to PREV and document the source-to-candidate trigger contract.
   The current trigger consumer scan found only the network/vulnerability closure plus decision-effect line 1161, which itself checks an event-target child from the source country.
   Review all these calls before changing the shared trigger, rather than inventing a new parallel eligibility policy.
4. Within `apply_exposure` keep source-owned inputs on its entry country.
   Replace source ROOT reads at direct target depth with PREV and source-row identity at nested depth with PREV.PREV.
   Preserve the call-source target by saving the actual source through PREV at current line 6117.
5. Freeze the conversion frame on B before the direct API call.
   After return read B's normal outputs and restore the outer source-row index from B's frozen frame before the source ledger continuation.
   Enter source A through the still-correct lexical PREV at current line 6136.
   Preserve pending material-source arrays and their episode validation at 6079-6094 and 6142-6167.
   Clear frame fields on accepted and rejected outcomes without clearing outputs.
6. Fix validated source storage and outgoing cleanup actor identity within the same closure.
   No pulse, independent-selector, global cursor, report delay, or consequence pacing change belongs in this patch.
7. Update the API spec, `docs/events/035_great_depression.md`, and the owner index at `common/scripted_effects/chaosx_dynamic_effects.md:362` with the ROOT-independent synchronous contract, direct-child helper depth, scratch cleanup, source attribution, and immediate-return examples.
   Document any new private helper in the matching Event35 owner documentation.
   Add no shared router or wrapper skill.

For example, inside `register_initial_centers` when the exact state has been entered directly from the actor country, the supported structure is:

```txt
set_variable = { great_depression_center_registry_index = PREV.great_depression_center_count }
set_variable = { great_depression_center_episode_id = PREV.great_depression_active_episode_id }
set_temp_variable = { great_depression_center_civilian_baseline = building_level@industrial_complex }
set_temp_variable = { great_depression_center_military_baseline = building_level@arms_factory }
PREV = {
	add_to_array = { array = great_depression_center_state_ids value = event_target:great_depression_center_candidate_state }
	add_to_array = { array = great_depression_center_factory_baseline_civilian_entries value = great_depression_center_civilian_baseline }
	add_to_array = { array = great_depression_center_factory_baseline_military_entries value = great_depression_center_military_baseline }
	add_to_array = { array = great_depression_center_owner_country_entries value = THIS }
}
```

This is a syntax illustration, not a complete replacement block.
Keep every other aligned row from the existing implementation and the exact candidate selection evidence.
The baseline temporary fields in this illustration are used before any nested external call.

## Conversion frame, targets, and cleanup

Before `E35:6123`, B should own normal scratch fields for the original source country, source episode, link receipt, source-target row, target-source row, and propagation depth.
Suggested names are `great_depression_conversion_source_country`, `great_depression_conversion_source_episode`, `great_depression_conversion_receipt`, `great_depression_conversion_source_row`, `great_depression_conversion_target_row`, and `great_depression_conversion_depth`.
A country flag such as `great_depression_conversion_frame_open` records the frame lifecycle.
These are proposed private fields, not new public inputs, receipts, or balance knobs.
The source pointer can be captured as `set_variable = { great_depression_conversion_source_country = PREV }` inside the direct target-country block.
The already frozen pending-material-source arrays remain B-owned.

Reason: new-crisis evolution initialization calls candidate registration and `apply_exposure` again before the outer conversion continuation resumes.
These nested exposure calls share temporary names such as `great_depression_contagion_source_target_row` and `great_depression_contagion_target_source_row`.
Normal variables on B preserve the outer indexes and receipt independently of work done by B as a new network source.
Reload the required temporary commit index immediately after the API returns, before writing A's row.
Revalidate the row's target country, source episode, and receipt against the frozen frame before attribution.
Do not trust a numeric index alone if the row identity no longer matches.

Current initial exposure stages are observed and pressured, with conversion-ready requiring stage 4.
Therefore network initialization does not by itself establish recursively executed conversion under today's initial stages.
It still overwrites shared exposure scratch and named regular exposure targets, which is enough to require the frame.
Full recursive API behavior and external callback reentrancy remain unresolved.
Do not claim arbitrary reentrant safety or add a silent queue as a substitute.

Regular targets are chain-local and cannot be manually cleared under the offline reference.
Reset or consume their proof fields and overwrite the exact binding immediately before use.
Never treat `has_event_target` alone as proof that an optional source belongs to this call.
Do not apply `clear_global_event_target` to an ordinary chain-local target.
Persistent committed source relationships remain country variables or existing owned arrays.
Validate a stored country pointer through its actual country existence, not `scope_exists` on a variable scope.

The existing temporary global region target is explicitly cleared by Event34 at lines 236 and 239.
Preserve exact inherited state identity and caller cleanup until the parent accepts a separate migration away from these globals.
If the companion remains public country-scope, its state entry always follows that country and PREV is unambiguous.

## Constants and tuning

No tuning table or numeric balance value should change for this repair.
Retain `great_depression_api`, caller, pacing, history, evolution, severity, shock, result and reject enums, center caps, propagation depth, conversion gates, and existing duration bands.
The current result table at `common/script_constants/035_great_depression_constants.txt:999-1024` already has accepted-new, accepted-deepening, accepted-merge, duplicate, invalid-context, invalid-country, invalid-source, incompatible-active, and rollback-compatible rejection surfaces.
Avoid a new result enum unless the parent accepts an explicit previously undocumented failure contract.
Use existing zero/one constants in any numeric frame field initialization.
Frame lifecycle is a flag, not a numeric boolean.
Do not touch weighted target formulas or timings incidentally.

Changing the actor checked by the candidate score at line 1339 is a weighted target-check patch even if every coefficient stays identical.
Required workflow: `chaosx_ai_probability_auditor` starts with `hoi4.probability_inspect`, produces matching named before scenarios, the owner applies the patch, and the auditor performs `hoi4.probability_compare` with the same scenarios and real immutable before-source evidence.
Neither the route nor the auditor spawning capability is callable in this session.
That evidence pass is blocked, and this report provides no probability or balance acceptance claim.

## Contract gaps that ROOT replacement alone cannot settle

1. Event34 consumes `industrial_boom_snapshot_frozen` and removes the active boom at `events/034_industrial_boom.txt:148-150`, before API success is known.
   The frozen numeric fields survive and are copied into the public request, but the one-shot flag and the inherited-region global target are consumed or cleared even if the API rejects.
   The spec at lines 316-330 requires failed uncommitted inheritance to leave the snapshot intact for bounded retry.
   Parent must preserve snapshot proof and exact region identity through rejection, with successful consumption only after the required transaction work.
   This is a concrete current ordering gap and was not patched here.
2. The region companion spec at lines 130-159 requires country scope, exact episode/state proof, region receipt, idempotence, result/reject reason, and center-index outputs.
   Current `register_inherited_region` checks only a named target, coherent ROOT crisis, count cap, and absence of a center flag.
   It lacks the full promised receipt/output contract, accepts an undocumented state-scope comment, and reads `great_depression_call_event34_project_units` after the main API has cleared that field.
   Use committed frozen `great_depression_inherited_event34_project_units`, established by `store_call_context`, for the post-return region continuation.
   A ROOT fix must not claim that this missing companion transaction is complete.
3. The main new-crisis commit records its source receipt before Event34's post-return companion call.
   If region registration is required for acceptance, the companion cannot safely fail after irreversible history/receipt commit without the specified rollback protocol.
   Parent must choose and document whether required inherited registration is completed inside the existing precommit center-registration step or whether a distinct provisional/commit boundary is necessary.
   Keeping the exact inherited state inside the existing initial-center registration is the smaller path for the current single-region caller.
   Do not create a second generic crisis API.
4. `great_depression_center_registration_failed` is set on failure in initial centers but is not explicitly reset to zero at that helper's start in the inspected source.
   Reset transaction scratch on every call to prevent a previous failure in the same effect chain from contaminating a later target.
   This matters for synchronous multi-country callers, and does not justify moving outputs into temporary variables.
5. The spec's Event34 snapshot validator promises exact target and episode proof, but `T35:301-316` presently validates positive proof fields and numeric bounds without comparing a frozen country pointer to THIS or all receipt/episode identities.
   The current Event34 recipient event aligns country identity structurally, but future cross-scope callers must not get the same guarantee from proof values alone.
   The relapse validator at `T35:337-344` likewise relies on supplied positive proofs rather than proving every prior-episode relationship itself.
   Report these as identity-contract limits rather than assuming full fail-closed behavior.

These gaps are separate from the parent's pulse and independent-delivery fixes.
None was silently simplified, queued, or declared resolved.

## Syntax references and precedents

Paths in this section are local reference evidence, with source fingerprints below.
No web Paradox wiki access was used.

| Source and line span read | Rule supported | Limit |
| --- | --- | --- |
| `paradox_wiki/Scopes - Hearts of Iron 4 Wiki.md:253-269`, `811-845` | ROOT remains native, THIS is current scope, PREV follows actual scope nesting, event targets are usable scopes | PREV depth must be proved for each helper call chain. |
| `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:263-327`, `425-459` | Regular/global event-target lifetime, country pointer variables, normal variables scoped, temporary variables unscoped, `event_target:name.variable` access, `var:` scope entry | Does not prove runtime correctness of this coupled Event35 closure. |
| `paradox_wiki/Event modding - Hearts of Iron 4 Wiki.md:25-35`, `180-205` | Recipient ROOT, previous ROOT becomes FROM, regular targets carried, immediate versus option behavior, effect-based event firing | Instant firing wording does not establish sender-side synchronous return ordering. |
| `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:4683-4697` | Direct scripted-effect invocation with `= yes` | No named-argument function API or event-return guarantee. |
| `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:571-602`, `1840-1847` | Scoped variable comparisons and country pointers for state ownership/control/core checks | Rejected or unsupported argument fields still need installed validation. |
| `paradox_wiki/Localisation - Hearts of Iron 4 Wiki.md:531-536`, Data structures line 301 | Scoped namespaces and event-target names without `event_target:` in localisation | No localisation or GUI layout change is proposed. |
| Installed `documentation/effects_documentation.md:2943-2966` | `country_event` COUNTRY scope and optional scheduling fields | No documented guarantee that the sending block's next statement reads completed recipient outputs. |
| Installed `documentation/effects_documentation.md:6496-6512`, `2733-2749` | Save regular/global targets and clear global targets | No regular-target clear effect established. |
| Installed `documentation/effects_documentation.md:7888-7907`, `7820-7839` | Normal and temporary variable assignment | Specific scoped access examples require the precedents below. |
| Installed `documentation/triggers_documentation.md:3844-3851` | `has_event_target` scope support | Target existence alone is not request identity. |
| Installed `documentation/script_concept_documentation.md:216-245`, `common/script_constants/documentation.md:1-83` | Shared constants and explicit supported variable fields | No new tuning values are needed. |

Installed root directory for the shortened installed paths is `C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV`.
Installed `common/scripted_effects/00_scripted_effects.txt:882-895` captures `collaboration_formed_by = PREV`, returns through PREV, and scopes through a variable into an exact country.
Installed `common/scripted_effects/SIA_scripted_effects.txt:1236-1248` reads normal variables through PREV while operating in a child country.
These are direct vanilla precedents for the recommended scope-neutral structure.

A bounded vanilla search under `common` and `events` found no literal `event_target:<name>.<variable>` assignments matching the searched identifiers.
Do not invent a vanilla precedent for that exact spelling.
The offline variable-scoping section explicitly documents it, and repo precedents exist at `common/scripted_effects/006_independence_wave_effects.txt:1080-1088` and `common/scripted_effects/013_natural_disasters_effects.txt:5347-5363`.
The latter saves `famine_adapter_actor` and reads its ID explicitly.
The existing shared helper at `common/scripted_effects/chaosx_dynamic_effects.txt:483-485` reads `event_target:technology_union_donor.researched_techs` without guessing ROOT.
Installed `events/Generic.txt:1984-1992`, `2029-2034`, and `2073-2083` is the named `generic.23` event-target precedent.
It proves explicit demanded-state targeting, not event-return semantics.

## Source revision ledger

SHA-256 hashes are local content fingerprints, not MCP source revisions or immutable before-edit artifacts.
No source copy was created for the parent-owned gameplay patch.

| Source | SHA-256 |
| --- | --- |
| `AGENTS.md` | `38E479CB75828BA888860BE8BC3739F9286C0D925CC7D8DE5ECD3B8DADEC46CF` |
| Events skill | `C8AF998498461944A7419371D4F8236FE216F6A1E235CE1E331C15C80FB6B7A7` |
| Subagents skill | `6E95D9A832AFEE35208F7058B742E6D4E7745B949E474C23FFF9B7F6BBFFCA63` |
| API spec | `CE5394A84CC128896893743E66F09C77C3AADC1F1DA7F6DF3985412E3D2DAE04` |
| E35 effects | `6FDAF35F9D19E264F012CBB675B41B0194868AFA8E48769BD0225FF626431470` |
| T35 triggers | `6BA5CC9AA716BA6E4C7873A59C7A64CED62673B9B06C8F4B09D5CC54C0D41970` |
| Event35 constants | `B14E552EE2176907C3BF05EC2324E7F58A06C72D4F4865DCF3C9A9160AAEB1E7` |
| Event35 decision effects dependency | `725C42FABD30A71D43A7C24F80BC94B99E0653D96C4A685C016E8D840A8F8F17` |
| Event35 incident cleanup dependency | `2F3A9003C2656489F71B0FC71584B598D44E36CBC0CD9402F94DE8E96CB996CB` |
| Global host on-actions | `F6DACD9CBB5E49574CD43E48AB63DD3D486B72812018EB2056E47CCB9BAD08B8` |
| Parent-owned Event35 events | `5F38DF9BF7E5DACAFC3017F4DA45080967473590692AB5946940954420C89137` |
| Event34 event source | `C7BD7B716FB1CA6B87E9016E29231DD9738C95F7B4B4A73416CBB5E39B3B8655` |
| Event34 supplier adapter | `6718BBF533B5A4E10408E700D4C69153B39E889956F81B730609F78ACF6E5A9F` |
| Event35 external adapters | `766A2401CF952333148D28FD1CB0D5AD2B88DA743C3A14FF268AED7D0C7ECAEF` |
| Shared dynamic effects | `91B4609D44FC19D619FC8B6D22EF4A32B78D20AC14F9F2EF58A1B9DA152D7C04` |
| Shared dynamic effects docs | `D81D285736D436296FF8E85500187DC964D4B7F9BA41879891BFDFB9BD4D70D5` |
| Offline Scopes | `18EF5249E4991F5427ECA9EC4A2F66DD47F51E26A491C730ADC622F1F5DB1B49` |
| Offline Data structures | `62273F37ED30E5479ACB331A8973F48DADC1867C4913C8A940E3E790E7AF32D4` |
| Offline Event modding | `96327B896298420D84058394A44ED08BE7EB518726B8F207B392FEA71F05D43D` |
| Offline Effects | `997DDB09BFD63EFB41A425149C46BD812D5F8953217A403386B2F6C85196AA0C` |
| Offline Triggers | `ABC51AD18A2C46E46D47BAA795C5A840EBAF7C4AE3E777426C64A9F4C0C0CE06` |
| Offline Localisation | `1A8F72362A34B4BB653186746B9FAE0B98E463205CB02F12CCF2C3D9CCD3A064` |
| Repo Independence Wave variable-access precedent | `03EF2CD34316A73C382CA18FD6070B17B79E9E03C52C6941ED77FD03C48B7813` |
| Repo natural-disaster actor precedent | `3E5D2134F2059402F976307541B5730D4A30D3A123EE770664209E9A530AD216` |
| Installed effects documentation | `2CDC93D26775990468EED167442F7A416B13059FB8FE07D139B54250B79209AF` |
| Installed triggers documentation | `7D27ED77DADAF3A213A4B3E2C624BF9C02DAE495317ABE8EEE833B27C2D1DE29` |
| Installed script concepts | `884BFE9F9207EA4B25B36B5129D0F77D11D4B2F7EB0592587767EC58D24930C7` |
| Installed constants schema | `E2812EFBDDC7961038E1F1F2B6DD6B059BDC70704EC87D1FE530835D9141BE1C` |
| Installed SIA effects | `AC1E86A0FFE5E46F7083318C584993667EAAFB3CD1585E15DB71FBD51FA276AF` |
| Installed 00 effects | `93DDD0D2E9F7A1A5640CFDAFBAE6B9FF0E1B4EE57E829C81D13B0CAC23AD90BF` |
| Installed Generic events | `96D510E119EC0548C3957689395674C7361C6689D2C7D0D65D1C0E024956EC26` |

## Meaningful validation and remaining work

Completed: repository-wide direct API and companion caller inventory, source-linked actor/source/state scope tracing, immediate output-consumer review, bounded helper-closure discovery, source scratch-overwrite analysis, existing helper and vanilla precedent review, local syntax references, and content fingerprint recording.
No gameplay files, constants, call sites, cleanup logic, localisation, spreadsheet, or helper documentation were changed by this subagent.
No simplification or alternative execution route was implemented.

Required parent validation after the bounded patch:

- Host H distinct from target B starts B through recovery watch and worldwide conversion. B owns all centers, severity, episode, achievement freezes, and outputs, with no H ledger mutations except explicitly global data.
- Source A distinct from B converts B. B's new evolution network touches C, then the original A-to-B source row and receipt commit correctly from the frozen frame. Pending material-source attribution validates original episodes.
- Event34 recipient collapse starts or deepens the same country and preserves the exact inherited state, frozen values, evolution floor, successful synchronous outputs, and zero consequence pacing.
- Floors baseline/I/II/III preserve the current enabled lower-stage behavior and source attribution. A new crisis and an active deepening use the same API, with no extra scheduler accounting.
- Duplicate receipt, invalid source/target, failed center registration, and invalid inherited state reject or no-op without replaying receipts. A rejected uncommitted Event34 transaction preserves frozen retry material according to the accepted contract.
- Two sequential targets in one effect chain do not share stale registration-failure scratch, outputs, source targets, or conversion row indexes.
- Multi-source outgoing cleanup removes only the exact closing actor's row and preserves other sources. Explicit state baselines remain state values after actor scope returns.

Skipped and blocked: mandatory domain event inspect/render/compare and installed script validation because callable routes are absent here and parent requests timed out, weighted target-check baseline/compare through the read-only probability auditor because its route and spawning capability are absent, runtime caller/output and ledger observations because no game was launched and no save was supplied.
The scenarios above are validation requirements, not executed results.
No numerical balance pass, arbitrary event-return guarantee, comprehensive callback reentrancy claim, or full companion transaction completion claim is supported.
Parent review must retain these limits and resolve the listed snapshot/region acceptance boundaries before claiming the API contract is repaired.
